#!/usr/bin/env python3
"""Refuse a daily report that shows the signs of being written from memory.

The pipeline never lets a model write a URL: every link comes from a bundle that
collect.py (or backfill/fetch_day.py) fetched and verified. A report that skipped
the pipeline gives itself away in a few cheap, unambiguous ways, all of which
reached production on 23-24 Sep 2026:

  - unfilled template placeholders ({title}, {subtitle}, {date_display}, ...);
  - placeholder links (example.com, /example1, href="URL");
  - no Hacker News item links at all — every pipeline item carries its thread.

This is not a style linter (that is backfill/verify_report.py); it only fails on
fabrication signals, so it can gate CI without false alarms on older reports.

Usage: check_report.py reports/ai-news-YYYY-MM-DD.html [...]   (exit 1 on problems)
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

# A template slot left as an element's whole text (<h1>{title}</h1>) or as the
# href — not braces in general, which specials use for pseudo-code.
PLACEHOLDER = re.compile(r">\s*(\{\{?\s*[a-z_]+\s*\}?\}|DD MMM YYYY[^<]*|DAY_OF_WEEK)\s*<"
                         r"|href=\"(URL|\{[a-z_]+\})\"")
FAKE_HOST = re.compile(r"(^|\.)example\.(com|org|net)$")
FAKE_PATH = re.compile(r"/example\d*(/|\.|$)")
STRIP = re.compile(r"<(script|style)\b.*?</\1>", re.I | re.S)
HREF = re.compile(r'href="(https?://[^"]+)"')
HN_ITEM = re.compile(r"^https://news\.ycombinator\.com/item\?id=\d+$")
MIN_HN_LINKS = 3


def problems(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    body = STRIP.sub(" ", raw)
    found = []
    placeholders = sorted({m.group(0).strip("><") for m in PLACEHOLDER.finditer(body)})
    if placeholders:
        found.append(f"unfilled placeholders: {', '.join(placeholders[:5])}")
    links = HREF.findall(body)
    fake = [u for u in links
            if FAKE_HOST.search(urlparse(u).netloc.lower()) or FAKE_PATH.search(urlparse(u).path.lower())]
    if fake:
        found.append(f"placeholder links: {', '.join(fake[:3])}")
    if path.name.startswith("ai-news-"):
        hn = sum(bool(HN_ITEM.match(u)) for u in links)
        if hn < MIN_HN_LINKS:
            found.append(f"only {hn} Hacker News item links (expected >= {MIN_HN_LINKS}): "
                         "the report did not come from the pipeline")
    return found


def main() -> None:
    failed = False
    for arg in sys.argv[1:]:
        path = Path(arg)
        issues = problems(path)
        for issue in issues:
            print(f"::error file={path}::{issue}" if "GITHUB_ACTIONS" in os.environ
                  else f"{path}: {issue}", file=sys.stderr)
        failed |= bool(issues)
        if not issues:
            print(f"{path.name}: OK")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
