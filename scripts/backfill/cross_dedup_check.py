#!/usr/bin/env python3
"""Find items repeated across published daily reports.

The daily pipeline dedups within a report and against the previous few days at
collection time. Backfilled days were generated in parallel, each blind to the
others, so nothing stopped the same story or paper from landing on two dates.

Two detectors, matching the established cross-dedup algorithm:
  1. normalised URL (scheme://netloc/path, no query, no trailing slash)
  2. fuzzy title, SequenceMatcher ratio >= --threshold (default 0.7)

Usage:
  cross_dedup_check.py [--from YYYY-MM-DD] [--to YYYY-MM-DD]
                       [--window N] [--threshold F] [--json]
"""
import argparse
import json
import re
import sys
from datetime import datetime
from difflib import SequenceMatcher
from html import unescape
from pathlib import Path
from urllib.parse import urlparse

REPORTS = Path(__file__).resolve().parents[2] / "reports"
ITEM = re.compile(
    r'<div class="num">(.*?)</div>\s*<div class="title">(.*?)</div>(.*?)(?=<div class="news-item">|</div>\s*</div>\s*</div>)',
    re.S,
)


def text(raw):
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", raw)).split())


def norm_url(u):
    p = urlparse(u)
    base = f"{p.scheme}://{p.netloc}{p.path.rstrip('/')}".lower()
    # Keep the query: for /item?id=N and /watch?v=N it *is* the identity, and
    # dropping it collapses every such link onto one URL that matches anything.
    # Only strip the params that are pure tracking noise.
    keep = [kv for kv in p.query.split("&")
            if kv and not re.match(r"(utm_|ref|fbclid|gclid|si)=", kv, re.I)]
    return f"{base}?{'&'.join(sorted(keep))}".lower() if keep else base


def norm_title(t):
    t = t.lower().strip()
    t = re.sub(r"^(the|a|an)\s+", "", t)
    t = re.sub(r"\b\d{1,2}\s+\w{3,9}\s+\d{4}\b", "", t)      # embedded dates
    t = re.sub(r"\s+[—–-]\s+[\w .]+$", "", t)                 # " — TechCrunch"
    t = re.sub(r"[^\w\s]", " ", t)
    return " ".join(t.split())


def load(day_file):
    html = day_file.read_text(encoding="utf-8")
    items = []
    for block in re.findall(r'class="section">(.*?)(?=<div class="section">|<div class="footer">)', html, re.S):
        lm = re.search(r'class="section-label">(.*?)</div>', block, re.S)
        section = text(lm.group(1)) if lm else "?"
        for chunk in re.split(r'<div class="news-item">', block)[1:]:
            tm = re.search(r'class="title">(.*?)</div>', chunk, re.S)
            if not tm:
                continue
            urls = re.findall(r'href="([^"]+)"', chunk)
            items.append({
                "section": section,
                "title": text(tm.group(1)),
                "urls": urls,
                "primary": next((u for u in urls if "news.ycombinator.com" not in u), urls[0] if urls else ""),
            })
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="start")
    ap.add_argument("--to", dest="end")
    ap.add_argument("--window", type=int, default=0, help="only compare days <= N apart (0 = all)")
    ap.add_argument("--threshold", type=float, default=0.7)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    days = []
    for f in sorted(REPORTS.glob("ai-news-*.html")):
        m = re.fullmatch(r"ai-news-(\d{4}-\d{2}-\d{2})", f.stem)
        if not m:
            continue
        d = m.group(1)
        if args.start and d < args.start:
            continue
        if args.end and d > args.end:
            continue
        days.append((d, load(f)))

    findings = []
    for i, (day_a, items_a) in enumerate(days):
        for day_b, items_b in days[i + 1:]:
            gap = (datetime.strptime(day_b, "%Y-%m-%d") - datetime.strptime(day_a, "%Y-%m-%d")).days
            if args.window and gap > args.window:
                continue
            for a in items_a:
                for b in items_b:
                    shared = {norm_url(u) for u in a["urls"]} & {norm_url(u) for u in b["urls"]}
                    if shared:
                        findings.append({"kind": "url", "days": [day_a, day_b], "gap": gap,
                                         "sections": [a["section"], b["section"]],
                                         "titles": [a["title"], b["title"]],
                                         "url": sorted(shared)[0]})
                        continue
                    ratio = SequenceMatcher(None, norm_title(a["title"]), norm_title(b["title"])).ratio()
                    if ratio >= args.threshold:
                        findings.append({"kind": "title", "ratio": round(ratio, 3),
                                         "days": [day_a, day_b], "gap": gap,
                                         "sections": [a["section"], b["section"]],
                                         "titles": [a["title"], b["title"]],
                                         "url": a["primary"]})

    if args.json:
        print(json.dumps({"days": len(days), "findings": findings}, indent=2, ensure_ascii=False))
        return 1 if findings else 0

    print(f"{len(days)} reports scanned, {len(findings)} repeat(s)\n")
    for f in findings:
        tag = "URL " if f["kind"] == "url" else f"~{f['ratio']}"
        print(f"[{tag}] {f['days'][0]} ({f['sections'][0]}) ←→ {f['days'][1]} ({f['sections'][1]})  +{f['gap']}d")
        print(f"        {f['titles'][0]}")
        if f["titles"][0] != f["titles"][1]:
            print(f"        {f['titles'][1]}")
        print(f"        {f['url']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
