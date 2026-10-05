#!/usr/bin/env python3
"""Verify a written special report against its evidence pack.

    python3 scripts/research/verify.py reports/<slug>.html data/research/<slug>/evidence.json [--offline]

Checks, sentence by sentence, everything that carries a citation
(<sup class="cite"><a href="#source-n">):
- the cited source exists in the evidence pack and in the report's Sources list
  (same URL under the same number);
- every figure in the sentence (12%, 3.5x, 1,800, 2026…) appears in the cited
  sources — in a claim, its quote, or the source's page text. A figure found in
  none of them is the classic synthesis error: a number moved to the wrong source
  or made up;
- then the URLs themselves (scripts/check_sources.py: alive, or archived if dead).

Also lists evidence the report never used, so a strong source isn't left out by
accident. Exits 1 on errors.
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:[,.]\d{3})+|\d+(?:\.\d+)?)\s*(%|x|×|k|m|bn|million|billion)?", re.I)
YEARS = {str(y) for y in range(1990, 2036)}


def text_of(fragment: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def figures(sentence: str) -> set[str]:
    out = set()
    for m in NUM.finditer(sentence):
        n = m.group(1)
        if n in YEARS or (len(n) == 1 and not m.group(2)):   # years and lone digits are not claims
            continue
        out.add(n.replace(",", ""))
    return out


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        raise SystemExit(__doc__)
    report, pack = Path(args[0]), json.loads(Path(args[1]).read_text(encoding="utf-8"))
    pages = Path(args[1]).parent / "pages"
    t = report.read_text(encoding="utf-8")
    srcs = {s["n"]: s for s in pack["sources"]}
    listed = dict(re.findall(r'<li id="source-(\d+)">.*?href="([^"]+)"', t))
    errors, warnings, used = [], [], set()

    # The Sources list must match the evidence pack, number for number.
    for n, url in listed.items():
        s = srcs.get(int(n))
        if not s:
            errors.append(f"Sources list has [{n}] {url}, which is not in the evidence pack")
        elif s["url"].rstrip("/") != html.unescape(url).rstrip("/"):
            errors.append(f"[{n}] points to {url} but the evidence pack has {s['url']}")

    def haystack(n: int) -> str:
        s = srcs.get(n)
        if not s:
            return ""
        parts = [c["claim"] + " " + c["quote"] + " " + " ".join(c.get("numbers", [])) for c in s["claims"]]
        page = pages / f"{s['id']}.md"
        if page.exists():
            parts.append(page.read_text(encoding="utf-8"))
        return " ".join(parts).replace(",", "")

    body = t[t.find("<body"):]
    body = re.sub(r'<div class="section-label">\s*Sources\s*</div>.*', "", body, flags=re.S)
    blocks = re.findall(r"<(p|li|td|figcaption|div class=\"stat-note\")[^>]*>(.*?)</(?:p|li|td|figcaption|div)>", body, re.S)
    checked = 0
    for _, frag in blocks:
        cites = [int(n) for n in re.findall(r'href="#source-(\d+)"', frag)]
        if not cites:
            continue
        sentence = text_of(re.sub(r'<sup class="cite">.*?</sup>', " ", frag))
        used.update(cites)
        for n in cites:
            if n not in srcs:
                errors.append(f"cites [{n}], not in the evidence pack: «{sentence[:90]}…»")
        hay = " ".join(haystack(n) for n in cites)
        for f in figures(sentence):
            if f not in hay:
                errors.append(f"figure {f} not found in cited source(s) {cites}: «{sentence[:110]}…»")
        checked += 1

    unused = [s for s in pack["sources"] if s["n"] not in used and s["quality"] >= 0.9]
    for s in unused[:10]:
        warnings.append(f"high-quality source never cited: [{s['n']}] {s['title'][:70]}")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"verify: {checked} cited passages, {len(errors)} error(s), {len(warnings)} warning(s)")
    rc = 1 if errors else 0
    if "--offline" not in sys.argv:
        rc |= subprocess.call([sys.executable, str(ROOT / "scripts" / "check_sources.py"), str(report)])
    return rc


if __name__ == "__main__":
    sys.exit(main())
