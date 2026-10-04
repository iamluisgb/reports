#!/usr/bin/env python3
"""Move existing reports onto the shared design system (Oct 2026).

site.js now drives the theme toggle and the audio player, and report.js the
prev/next links, so the per-report copies of that code are dead weight. This
removes them, along with inline styles the stylesheet now covers. Idempotent:
a second run changes nothing. Hand-written script blocks that mix the theme
with other logic (charts, progress bars) are left alone; site.js overrides
their toggleTheme() anyway.

    python3 scripts/backfill/migrate_design_system.py [--check]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PLAYER_JS = re.compile(r"[ \t]*\(function\(\) \{\s*const player = document\.getElementById\('audioPlayer'\);.*?\}\)\(\);\n", re.S)
SCRIPT = re.compile(r"[ \t]*<script>(.*?)</script>\n?", re.S)
THEME_BUTTON = re.compile(r'<button class="theme-toggle"[^>]*>[^<]*</button>')
REPORT_NAV = re.compile(r'[ \t]*<nav class="report-nav"[^>]*>.*?</nav>\n?', re.S)
# Code that marks a script block as more than theme handling.
OTHER_LOGIC = ("progress", "Chart", "NAV_API", "IntersectionObserver", "fetch(", "addEventListener", "canvas")
STYLED = re.compile(r'(<(?:div|span|a)\b[^>]*?class="(?:stats-grid|stat-card|stat-value|stat-label|stat-note|sources|header)"[^>]*?)\s+style="[^"]*"')
NOTE_LINK = re.compile(r'(<div class="stat-note">.*?)<a ([^>]*?)\s*style="[^"]*"', re.S)


def migrate(text: str) -> tuple[str, list[str]]:
    done = []

    new = PLAYER_JS.sub("", text)
    if new != text:
        done.append("player script")
    text = new

    def drop_block(m):
        body = m.group(1)
        theme_only = ("toggleTheme" in body or "applyTheme" in body) and not any(k in body for k in OTHER_LOGIC)
        nav_only = "NAV_API_URL" in body and "toggleTheme" not in body and "progress" not in body
        empty = not body.strip()
        if theme_only or nav_only or empty:
            done.append("theme script" if theme_only else "github-api nav script" if nav_only else "empty script")
            return ""
        return m.group(0)
    text = SCRIPT.sub(drop_block, text)

    if "NAV_API_URL" not in text:
        new = REPORT_NAV.sub("", text)
        if new != text:
            done.append("report-nav markup")
        text = new

    new = THEME_BUTTON.sub('<button class="theme-toggle" type="button" data-theme-toggle>◐</button>', text)
    if new != text:
        done.append("theme button")
    text = new

    for _ in range(3):   # an element can carry the class first and the style later; repeat until stable
        new = STYLED.sub(r"\1", text)
        new = NOTE_LINK.sub(r"\1<a \2", new)
        if new == text:
            break
        if "inline styles" not in done:
            done.append("inline styles")
        text = new

    return text, done


def main() -> None:
    check = "--check" in sys.argv
    changed = 0
    for path in sorted((ROOT / "reports").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        new, done = migrate(text)
        if new != text:
            changed += 1
            print(f"{path.name}: {', '.join(dict.fromkeys(done))}")
            if not check:
                path.write_text(new, encoding="utf-8")
    print(f"{'would change' if check else 'changed'} {changed} report(s)")


if __name__ == "__main__":
    main()
