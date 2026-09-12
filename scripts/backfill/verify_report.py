#!/usr/bin/env python3
"""Gate a generated daily report before it is committed.

Checks the structural contract the homepage, the RSS feed and build_social.py
all depend on, plus the things a model gets wrong when filling a template:
leftover placeholders, a date that disagrees with the filename, duplicated
items across sections, and dead numbering.

Exit 0 = publishable. Exit 1 = list of problems on stderr.
"""
import re
import sys
from datetime import datetime
from html import unescape
from pathlib import Path

PLACEHOLDERS = (
    "Headline here", "Paper title", "One-line description.", "DD MMM YYYY",
    "DAY_OF_WEEK", "Analysis bullet here.", "Abstract 1-2 lines.",
    "Headline 1 · Headline 2", ">URL<", 'href="URL"',
)
REQUIRED = {
    "stylesheet": '<link rel="stylesheet" href="../styles.css">',
    "back-link": 'class="back-link"',
    "h1": "<h1>The <em>AI</em> Briefing</h1>",
    "theme toggle": 'class="theme-toggle" onclick="toggleTheme()"',
    "handle": "@iamluisgb",
}
SECTIONS = [
    "Headlines",
    "AI / LLM / Agents",
    "Papers",
    "Infra / SRE / DevOps",
    "Hacker News",
    "Why It Matters",
]


def text(raw):
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", raw)).split())


def same_day(s, day):
    """True if the free-text date in `s` is the same calendar day (any casing)."""
    m = re.search(r"(\d{1,2})\s+([A-Za-z]{3,})\s+(\d{4})", s)
    if not m:
        return False
    try:
        parsed = datetime.strptime(
            f"{int(m.group(1)):02d} {m.group(2)[:3].title()} {m.group(3)}", "%d %b %Y"
        )
    except ValueError:
        return False
    return parsed.date() == day.date()


def check(path: Path):
    errors, warnings = [], []
    html = path.read_text(encoding="utf-8")

    m = re.fullmatch(r"ai-news-(\d{4}-\d{2}-\d{2})", path.stem)
    if not m:
        return [f"filename must be ai-news-YYYY-MM-DD.html, got {path.name}"], []
    day = datetime.strptime(m.group(1), "%Y-%m-%d")

    for label, needle in REQUIRED.items():
        if needle not in html:
            errors.append(f"missing {label}: {needle!r}")

    for ph in PLACEHOLDERS:
        if ph in html:
            errors.append(f"template placeholder left in: {ph!r}")

    if "<!-- og:start -->" in html:
        warnings.append(
            "og meta block present — fine on a report CI has already processed, "
            "but never hand-write it into a new one"
        )

    title = re.search(r"<title>(.*?)</title>", html, re.S)
    if not title:
        errors.append("no <title>")
    else:
        got = text(title.group(1))
        if not got.lower().startswith("ai news daily"):
            errors.append(f"title must start with 'AI News Daily —', got {got!r}")
        if not same_day(got, day):
            errors.append(
                f"title date disagrees with filename: {got!r} vs {day.strftime('%d %b %Y')}"
            )

    dl = re.search(r'class="date-line">(.*?)</div>', html, re.S)
    if not dl:
        errors.append("no .date-line")
    else:
        got = text(dl.group(1))
        if not same_day(got, day):
            errors.append(
                f".date-line is {got!r}, expected the {day.strftime('%d %b %Y')} of the filename"
            )
        if day.strftime("%A").lower() not in got.lower():
            warnings.append(f".date-line has no weekday ({day.strftime('%A').upper()})")

    sub = re.search(r'class="subtitle">(.*?)</div>', html, re.S)
    if not sub or len(text(sub.group(1))) < 40:
        errors.append(".subtitle missing or too short (it is the card + og description)")
    elif "·" not in text(sub.group(1)):
        warnings.append(".subtitle should join 3-4 headlines with ' · '")

    labels = [text(s) for s in re.findall(r'class="section-label">(.*?)</div>', html, re.S)]
    for name in SECTIONS:
        if not any(name.lower() in l.lower() for l in labels):
            errors.append(f"missing section: {name}")

    for block in re.findall(r'class="section">(.*?)(?=<div class="section">|<div class="footer">)', html, re.S):
        label = text(re.search(r'class="section-label">(.*?)</div>', block, re.S).group(1)) if re.search(r'class="section-label">', block) else "?"
        nums = [text(n) for n in re.findall(r'class="num">(.*?)</div>', block, re.S)]
        if nums and nums != [f"{i:02d}" for i in range(1, len(nums) + 1)]:
            errors.append(f"section {label!r}: numbering is {nums}, expected 01..{len(nums):02d}")
        if not nums and label not in ("Why It Matters", "?") and not text(block).strip():
            errors.append(f"section {label!r} is empty")

    items = re.findall(r'class="news-item">(.*?)</div>\s*</div>', html, re.S)
    if not 8 <= len(items) <= 18:
        (errors if len(items) < 8 else warnings).append(
            f"{len(items)} news items — expected roughly 12-15"
        )

    hrefs = re.findall(r'class="sources">(.*?)</div>', html, re.S)
    originals = []
    for src in hrefs:
        links = re.findall(r'href="([^"]+)"', src)
        if not links:
            errors.append("a .sources block has no link")
        for href in links:
            if not href.startswith("http"):
                errors.append(f"non-absolute source link: {href}")
        originals.extend(l for l in links if "news.ycombinator.com" not in l)
    dupes = {u for u in originals if originals.count(u) > 1}
    for u in sorted(dupes):
        errors.append(f"duplicate item across sections: {u}")

    if not re.search(r'class="follow-item"', html):
        errors.append("Why It Matters has no .follow-item bullets")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_report.py reports/ai-news-YYYY-MM-DD.html")
    path = Path(sys.argv[1])
    if not path.exists():
        raise SystemExit(f"no such file: {path}")
    errors, warnings = check(path)
    for w in warnings:
        print(f"warn: {w}", file=sys.stderr)
    if errors:
        print(f"\n{path.name}: {len(errors)} problem(s)", file=sys.stderr)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        sys.exit(1)
    print(f"{path.name}: OK")


if __name__ == "__main__":
    main()
