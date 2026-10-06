#!/usr/bin/env python3
"""Check the design system: token contrast, byte budgets, and report markup.

    python3 scripts/check_design.py                 # tokens + budgets + every report
    python3 scripts/check_design.py reports/x.html  # tokens + budgets + these reports

Errors fail the run (exit 1); warnings are printed and let it pass. The rules
are the ones in AGENTS.md → Design system: no private styles or colours in a
report, the title accent on the subject, no emoji in titles, no paragraph
said twice, AA contrast for every text token, and a ceiling on what ships.
"""
from __future__ import annotations

import difflib
import gzip
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []
warnings: list[str] = []

# ---------------------------------------------------------------- tokens
TEXT_TOKENS = ("--on-surface", "--on-surface-variant", "--muted", "--primary")
SURFACES = ("--bg", "--bg-card", "--bg-card-hover")


def luminance(hex_colour: str) -> float:
    h = hex_colour.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def check_tokens() -> None:
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    for name, selector in (("dark", ":root"), ("light", '[data-theme="light"]')):
        body = re.search(re.escape(selector) + r"\s*\{(.*?)\n\}", css, re.S).group(1)
        tokens = dict(re.findall(r"(--[\w-]+):\s*(#[0-9a-fA-F]{6})", body))
        for fg in TEXT_TOKENS:
            for bg in SURFACES:
                if fg in tokens and bg in tokens:
                    ratio = contrast(tokens[fg], tokens[bg])
                    if ratio < 4.5:
                        errors.append(f"styles.css: {name} {fg} on {bg} is {ratio:.2f}:1 (needs 4.5:1)")


# ---------------------------------------------------------------- budgets (gzip bytes)
BUDGETS = {"index.html": 60_000, "styles.css": 16_000, "home.css": 8_000, "site.js": 8_000,
           "report.js": 6_000, "pwa.js": 6_000, "sw.js": 7_000}
REPORT_BUDGET = 60_000
FONTS_BUDGET = 120_000   # raw woff2, all faces


def gz(path: Path) -> int:
    return len(gzip.compress(path.read_bytes(), 9))


def check_budgets(reports: list[Path]) -> None:
    for name, limit in BUDGETS.items():
        size = gz(ROOT / name)
        if size > limit:
            errors.append(f"{name}: {size:,} bytes gzipped, budget {limit:,}")
    fonts = sum(p.stat().st_size for p in (ROOT / "assets/fonts/web").glob("*.woff2"))
    if fonts > FONTS_BUDGET:
        errors.append(f"assets/fonts/web: {fonts:,} bytes, budget {FONTS_BUDGET:,}")
    for p in reports:
        size = gz(p)
        if size > REPORT_BUDGET:
            errors.append(f"{p.name}: {size:,} bytes gzipped, budget {REPORT_BUDGET:,}")


# ---------------------------------------------------------------- reports
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿⌀-⏿]")
HEX_IN_MARKUP = re.compile(r'(?:fill|stroke|color|background)\s*[=:]\s*"?#[0-9a-fA-F]{3,8}')
UI_BLOCK = re.compile(r"<!-- ui:start -->.*?<!-- ui:end -->", re.S)


def text_of(fragment: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", fragment)).split())


def check_report(p: Path) -> None:
    name = p.name
    raw = p.read_text(encoding="utf-8", errors="replace")
    t = UI_BLOCK.sub("", raw)

    if re.search(r"<style[\s>]", t):
        errors.append(f"{name}: has its own <style>; use the kit in styles.css")
    # A .frame or .specimen keeps its own colours on purpose: it reproduces a swatch or another product's type.
    hexes = HEX_IN_MARKUP.findall(re.sub(r'<[^>]*class="(?:frame|specimen)"[^>]*>', "", t))
    if hexes:
        errors.append(f"{name}: {len(hexes)} hard-coded colour(s), e.g. {hexes[0]!r}; use kit classes or tokens")

    title = re.search(r"<title>(.*?)</title>", t, re.S)
    if title and EMOJI.search(title.group(1)):
        errors.append(f"{name}: emoji in <title>")

    h1 = re.search(r"<h1>(.*?)</h1>", t, re.S)
    if h1:
        ems = re.findall(r"<em>(.*?)</em>", h1.group(1), re.S)
        if len(ems) > 1:
            errors.append(f"{name}: {len(ems)} accents in the title; use one")
        for em in ems:
            words = text_of(em).split()
            if len(words) > 3:
                errors.append(f"{name}: title accent covers {len(words)} words ({text_of(em)!r}); mark the subject, max 3")
            if re.fullmatch(r"[\d.,%–-]+", text_of(em)):
                errors.append(f"{name}: title accent on a number ({text_of(em)!r}); mark the subject")

    # Chart captions are alike by nature ("X across 5 dimensions · Scale 0–10"); compare prose only.
    blocks = [text_of(m.group(2)) for m in re.finditer(r"<(p|figcaption)(?![^>]*chart-caption)[^>]*>(.*?)</\1>", t, re.S)]
    blocks = [b for b in blocks if len(b) > 80]
    for i, a in enumerate(blocks):
        for b in blocks[i + 1:i + 3]:
            if difflib.SequenceMatcher(None, a[:300], b[:300]).ratio() > 0.6:
                errors.append(f"{name}: says the same thing twice: {a[:60]!r}…")

    scripts = [s for s in re.findall(r"<script>(.*?)</script>", t, re.S) if s.strip()]
    if scripts:
        warnings.append(f"{name}: {len(scripts)} inline script block(s); theme, audio and navigation come from site.js / report.js")
    if 'style="' in t and not hexes:
        n = t.count('style="')
        if n > 10:
            warnings.append(f"{name}: {n} inline style attributes")


def main(args: list[str]) -> int:
    # With arguments, check only those reports (CI passes the ones a push touched, or none).
    reports = [Path(a) for a in args if Path(a).is_file()] if args else sorted((ROOT / "reports").glob("*.html"))
    reports = [p for p in reports if 'http-equiv="refresh"' not in p.read_text(encoding="utf-8")[:2000]]   # merge stubs
    check_tokens()
    check_budgets(reports)
    for p in reports:
        if p.suffix == ".html" and p.exists():
            check_report(p)
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"::error::{e}" if "GITHUB_ACTIONS" in __import__("os").environ else f"error: {e}")
    print(f"design check: {len(errors)} error(s), {len(warnings)} warning(s), {len(reports)} report(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
