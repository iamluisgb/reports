#!/usr/bin/env python3
"""List the days that have no daily report yet.

Scans reports/ai-news-YYYY-MM-DD.html and prints every missing date from the
day after the last published report through --until (default: today), one per
line. Used by run.sh to drive the backfill loop.

Usage: missing_days.py [--until YYYY-MM-DD] [--from YYYY-MM-DD]
"""
import argparse
import re
from datetime import date, datetime, timedelta
from pathlib import Path

REPORTS = Path(__file__).resolve().parents[2] / "reports"


def published():
    days = set()
    for f in REPORTS.glob("ai-news-*.html"):
        m = re.fullmatch(r"ai-news-(\d{4}-\d{2}-\d{2})", f.stem)
        if m:
            days.add(datetime.strptime(m.group(1), "%Y-%m-%d").date())
    return days


def resume_point(have):
    """Day after the last day of continuous publishing.

    Not max(have)+1: a single isolated report published after a long gap (a
    manual one-off, or another pipeline pushing straight to master) would hide
    every missing day before it. The last day of the trailing contiguous run is
    the honest resume point.
    """
    contiguous = [d for d in have if d - timedelta(days=1) in have]
    return (max(contiguous) if contiguous else max(have)) + timedelta(days=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--until", default=date.today().isoformat())
    ap.add_argument("--from", dest="start", default=None)
    args = ap.parse_args()

    have = published()
    if not have:
        raise SystemExit("no existing ai-news-*.html reports found")
    until = datetime.strptime(args.until, "%Y-%m-%d").date()
    start = (
        datetime.strptime(args.start, "%Y-%m-%d").date()
        if args.start
        else resume_point(have)
    )

    d = start
    while d <= until:
        if d not in have:
            print(d.isoformat())
        d += timedelta(days=1)


if __name__ == "__main__":
    main()
