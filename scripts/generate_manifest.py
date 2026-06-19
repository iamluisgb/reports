#!/usr/bin/env python3
"""Generate reports.json and sitemap.xml from the HTML files in reports/.

This removes the site's runtime dependency on the GitHub API: index.html reads
the static reports.json (same-origin, no rate limit) instead of querying
api.github.com on every page load.

Metadata is derived from each report's HTML (title, date, subtitle, word count
for reading time), so adding a new report needs no manual edits here.

Run from the repo root:  python3 scripts/generate_manifest.py
The GitHub Action runs it automatically on every push that touches reports/.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "reports"
MANIFEST_PATH = ROOT / "reports.json"
SITEMAP_PATH = ROOT / "sitemap.xml"
RSS_PATH = ROOT / "rss.xml"

# Primary canonical domain (GitHub Pages also serves iamluisgb.github.io/reports/).
BASE_URL = "https://luisgonzalezbernal.com/reports"
WORDS_PER_MINUTE = 200
RSS_ITEMS = 25

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}

DATE_IN_NAME = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
DATE_LINE = re.compile(r'date-line">\s*([^<]+)', re.IGNORECASE)
TITLE_TAG = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
SUBTITLE = re.compile(r'class="subtitle">\s*(.*?)\s*</div>', re.IGNORECASE | re.DOTALL)
TAG_STRIP = re.compile(r"<(script|style)\b.*?</\1>", re.IGNORECASE | re.DOTALL)
ANY_TAG = re.compile(r"<[^>]+>")

TAG_KEYWORDS = {
    "agent": "agents",
    "memory": "memory",
    "model": "models",
    "architecture": "architecture",
    "engineering": "engineering",
    "framework": "frameworks",
    "adoption": "adoption",
    "security": "security",
    "sre": "sre",
}


def is_daily(name: str) -> bool:
    return name.startswith("ai-news-") and name.endswith(".html")


def clean_text(raw: str) -> str:
    return html.unescape(ANY_TAG.sub(" ", raw)).strip()


def parse_date_line(text: str) -> str | None:
    """Parse '29 MAY 2026' / '08 Jun 2026' -> '2026-05-29'."""
    m = re.search(r"(\d{1,2})\s+([A-Za-z]{3,})\s+(\d{4})", text)
    if not m:
        return None
    day, month_name, year = m.groups()
    month = MONTHS.get(month_name[:3].lower())
    if not month:
        return None
    return f"{year}-{month:02d}-{int(day):02d}"


def git_first_commit_date(path: Path) -> str:
    """Date the file first entered git history (deterministic fallback)."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip().splitlines()
        if out:
            return out[-1][:10]
    except subprocess.CalledProcessError:
        pass
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def resolve_date(name: str, content: str, path: Path) -> str:
    m = DATE_IN_NAME.search(name)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    dl = DATE_LINE.search(content)
    if dl:
        parsed = parse_date_line(clean_text(dl.group(1)))
        if parsed:
            return parsed
    return git_first_commit_date(path)


def clean_title(raw: str) -> str:
    title = clean_text(raw)
    title = re.sub(r"^[^\w]+", "", title)  # leading ⭐/emoji/symbols
    title = re.sub(r"\s*[—-]\s*⭐?\s*Special Report\s*$", "", title, flags=re.IGNORECASE)
    return title.strip()


def reading_time(content: str) -> int:
    text = ANY_TAG.sub(" ", TAG_STRIP.sub(" ", content))
    words = len(text.split())
    return max(1, round(words / WORDS_PER_MINUTE))


def derive_tags(name: str, title: str, kind: str) -> list[str]:
    tags = ["news"] if kind == "daily" else []
    haystack = f"{name} {title}".lower()
    for needle, tag in TAG_KEYWORDS.items():
        if needle in haystack and tag not in tags:
            tags.append(tag)
    return tags


def build_entry(path: Path) -> dict:
    content = path.read_text(encoding="utf-8", errors="replace")
    name = path.name
    kind = "daily" if is_daily(name) else "special"

    title_match = TITLE_TAG.search(content)
    raw_title = title_match.group(1) if title_match else name
    title = "AI News Daily" if kind == "daily" else clean_title(raw_title)

    subtitle_match = SUBTITLE.search(content)
    summary = clean_text(subtitle_match.group(1)) if subtitle_match else ""

    return {
        "file": name,
        "type": kind,
        "title": title,
        "date": resolve_date(name, content, path),
        "summary": summary,
        "readingTime": reading_time(content),
        "tags": derive_tags(name, title, kind),
    }


def main() -> None:
    reports = sorted(
        (build_entry(p) for p in REPORTS_DIR.glob("*.html")),
        key=lambda r: (r["date"], r["file"]),
        reverse=True,
    )

    manifest = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": len(reports),
        "reports": reports,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    urls = [f"{BASE_URL}/", f"{BASE_URL}/about.html"]
    lastmods = {f"{BASE_URL}/": reports[0]["date"] if reports else None}
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lm = lastmods.get(u)
        sitemap.append(f"  <url><loc>{u}</loc>" + (f"<lastmod>{lm}</lastmod>" if lm else "") + "</url>")
    for r in reports:
        sitemap.append(
            f"  <url><loc>{BASE_URL}/reports/{r['file']}</loc>"
            f"<lastmod>{r['date']}</lastmod></url>"
        )
    sitemap.append("</urlset>\n")
    SITEMAP_PATH.write_text("\n".join(sitemap), encoding="utf-8")

    write_rss(reports)

    print(f"Wrote {MANIFEST_PATH.name} ({len(reports)} reports), {SITEMAP_PATH.name} and {RSS_PATH.name}")


def rss_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=12, tzinfo=timezone.utc)
    return format_datetime(dt)


def write_rss(reports: list[dict]) -> None:
    latest = reports[:RSS_ITEMS]
    build_date = rss_date(reports[0]["date"]) if reports else format_datetime(datetime.now(timezone.utc))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0"',
        '     xmlns:atom="http://www.w3.org/2005/Atom"',
        '     xmlns:dc="http://purl.org/dc/elements/1.1/"',
        '     xmlns:media="http://search.yahoo.com/mrss/">',
        "  <channel>",
        "    <title>AI Reports — Luis GB</title>",
        f"    <link>{BASE_URL}/</link>",
        "    <description>Daily and special reports on artificial intelligence — models, agents, security, and AI engineering. Generated by Hermes Agent.</description>",
        "    <language>en</language>",
        f"    <lastBuildDate>{build_date}</lastBuildDate>",
        f"    <pubDate>{build_date}</pubDate>",
        "    <ttl>60</ttl>",
        f'    <atom:link href="{BASE_URL}/rss.xml" rel="self" type="application/rss+xml"/>',
        "    <category>Technology</category>",
        "    <managingEditor>iamluisgb@protonmail.com (Luis GB)</managingEditor>",
        "    <webMaster>iamluisgb@protonmail.com (Luis GB)</webMaster>",
    ]
    for r in latest:
        url = f"{BASE_URL}/reports/{r['file']}"
        title = "AI News Daily — " + datetime.strptime(r["date"], "%Y-%m-%d").strftime("%-d %b %Y") \
            if r["type"] == "daily" else r["title"]
        lines += [
            "",
            "    <item>",
            f"      <title>{html.escape(title)}</title>",
            f"      <link>{url}</link>",
            f'      <guid isPermaLink="true">{url}</guid>',
            f"      <pubDate>{rss_date(r['date'])}</pubDate>",
            "      <dc:creator>Hermes Agent</dc:creator>",
            f"      <category>{'Daily' if r['type'] == 'daily' else 'Special'}</category>",
        ]
        if r["summary"]:
            lines.append(f"      <description>{html.escape(r['summary'])}</description>")
        lines.append("    </item>")
    lines += ["  </channel>", "</rss>", ""]
    RSS_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
