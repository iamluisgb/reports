#!/usr/bin/env python3
"""Convert the special reports' own diagram vocabularies to the shared kit (Oct 2026).

Five specials shipped a private <style> block with their own SVG classes
(dg-*, d-*, rl-*, .chart-container svg …). This maps each class to the kit in
styles.css (`figure.diagram .box`, `.flow`, `.data` …), moves text sizes onto
the <text> elements as attributes, and deletes the private styles. Idempotent.

    python3 scripts/backfill/unify_diagrams.py [--check]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "reports"

# old class -> (kit classes, attributes the old CSS carried)
ONTOLOGY = {
    "dg-box": ("box-raised", {}), "dg-in": ("box", {}), "dg-node": ("box-accent", {}),
    "dg-t": ("label", {"font-size": "13", "text-anchor": "middle"}),
    "dg-l": ("label", {"font-size": "13"}),
    "dg-mut": ("muted", {"font-size": "11", "text-anchor": "middle"}),
    "dg-hd": ("kicker accent", {"font-size": "11", "text-anchor": "middle"}),
    "dg-cap": ("caption", {"font-size": "11", "text-anchor": "middle"}),
    "dg-edge": ("edge", {}), "dg-flow": ("flow", {}), "dg-dash": ("dash", {}), "dg-marker": ("marker", {}),
}
WORLD_CLASS = {
    "rl-e": ("kicker muted", {"font-size": "11"}), "rl-ea": ("kicker accent", {"font-size": "11"}),
    "rl-t": ("title", {"font-size": "16"}), "rl-d": ("data", {"font-size": "12"}),
    "rl-da": ("data accent", {"font-size": "12"}), "rl-note": ("data", {"font-size": "11"}),
    "rl-chip": ("outline", {}), "rl-rail": ("rail", {}), "rl-railn": ("rail-accent", {}),
    "rl-dot": ("dot", {}), "rl-dotn": ("dot-accent", {}),
    "d-ax": ("data", {"font-size": "12"}), "d-lbl": ("label", {"font-size": "14"}),
    "d-val": ("value", {"font-size": "14"}), "d-bar": ("bar-base", {}), "d-bar2": ("bar-accent", {}),
    "d-l2": ("label", {"font-size": "13.5"}), "d-v2": ("data", {"font-size": "13"}),
    "d-h2t": ("label", {"font-size": "14"}), "d-bx": ("bar-base", {}), "d-bhi": ("bar-accent", {}),
    "d-blo": ("bar-muted", {}), "d-an": ("data", {"font-size": "13"}),
    "d-t3": ("title", {"font-size": "14"}), "d-s3": ("data", {"font-size": "12"}),
    "d-b3": ("box", {}), "d-b3a": ("box-accent", {}),
    "d-s7t": ("title", {"font-size": "15"}), "d-s7s": ("data", {"font-size": "12"}),
    "d-s7r": ("data accent", {"font-size": "11", "text-anchor": "end"}),
    "d-s7n": ("value accent", {"font-size": "13"}),
    "d-c7l": ("kicker muted", {"font-size": "11"}), "d-c7s": ("data", {"font-size": "12"}),
    "d-c7n": ("data accent", {"font-size": "12"}), "d-panel": ("frame", {}),
}
SINGLE_AGENT = {
    "label": ("muted", {"font-size": "11"}),
    "arrow": ("flow", {"marker-end": "url(#arrowhead)"}),
    "arrowhead": ("marker", {}),
}

PRIVATE_STYLE = re.compile(r"[ \t]*<style>\s*(?:/\*[^*]*\*/\s*)?(?:\.svg-figure|figure\.diagram \.|\.chart-container).*?</style>\n?", re.S)
TAG_WITH_CLASS = re.compile(r'<(text|rect|line|path|polygon|circle|g|tspan)\b([^>]*?)\sclass="([^"]+)"([^>]*?)(/?)>')


def remap(text: str, mapping: dict) -> str:
    def fix(m):
        tag, before, cls, after, close = m.groups()
        if cls not in mapping:
            return m.group(0)
        new_cls, attrs = mapping[cls]
        rest = before + after
        extra = "".join(f' {k}="{v}"' for k, v in attrs.items() if f'{k}="' not in rest)
        if tag not in ("text", "tspan") and new_cls != "frame":   # a frame keeps its swatch fill
            rest = re.sub(r'\s(?:fill|stroke|stroke-width)="#[0-9a-fA-F]{3,6}"', "", rest)
        return f'<{tag}{before} class="{new_cls}"{after}{extra}{close}>'
    return TAG_WITH_CLASS.sub(fix, text)


def ontology(t: str) -> str:
    t = t.replace('<figure class="svg-figure">', '<figure class="diagram">')
    t = remap(t, ONTOLOGY)
    # Arrowheads and the one green dashed loop carried colours inline.
    t = re.sub(r'<path d="M0 0L10 5L0 10z" fill="#[0-9a-fA-F]{6}"/>', '<path d="M0 0L10 5L0 10z" class="marker"/>', t)
    t = t.replace('fill="none" stroke="#7ee0a3" stroke-width="1.6" stroke-dasharray="5 4"', 'class="flow" stroke-dasharray="5 4"')
    return t


def single_agent(t: str) -> str:
    # The one SVG figure here sat in a .chart-container meant for canvas charts.
    m = re.search(r'<div class="chart-container">\s*(<svg viewBox="0 0 700 180".*?</svg>)\s*(?:</svg>\s*)?<p class="chart-caption">(.*?)</p>\s*</div>', t, re.S)
    if m:
        svg = re.sub(r'<g class="node">\s*<rect ([^>]*?) fill="var\(--bg-card\)"/>',
                     r'<g>\n              <rect class="box-raised" rx="8" \1/>', m.group(1))
        svg = remap(svg, SINGLE_AGENT)
        t = t[:m.start()] + f'<figure class="diagram">\n          {svg}\n          <figcaption>{m.group(2)}</figcaption>\n        </figure>' + t[m.end():]
    return t


FILES = {
    "ontology-graph-ml-aiops-2026-10-01.html": ontology,
    "world-class-websites-2026-10-03.html": lambda t: remap(t, WORLD_CLASS),
    "single-agent-vs-multi-agent-llm-systems-2026-07-17.html": single_agent,
    "agents-running-businesses-2026-06-27.html": lambda t: t,
    "ai-native-design-patterns-2026-07-17.html": lambda t: t,
}


def main() -> None:
    check = "--check" in sys.argv
    for name, convert in FILES.items():
        path = R / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new = PRIVATE_STYLE.sub("", convert(text))
        if new != text:
            print(f"{name}: converted")
            if not check:
                path.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
