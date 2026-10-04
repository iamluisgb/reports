#!/usr/bin/env python3
"""Write the files agents read: a markdown twin of every report, sitemap.md and tokens.json.

GitHub Pages cannot negotiate on `Accept: text/markdown`, so each report gets a
static twin at the same path with a .md extension, announced in its <head> by
<link rel="alternate" type="text/markdown"> (build_social.py adds it). sitemap.md
lists every report by kind, series and month — the hierarchy a flat XML sitemap
cannot express. tokens.json publishes the design tokens from styles.css so an
agent writing a report gets the system instead of guessing it.

Called by generate_manifest.py. Idempotent: files are only rewritten when they change.
"""
from __future__ import annotations

import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
BASE = "https://luisgonzalezbernal.com/reports"
MONTHS_LONG = ["January", "February", "March", "April", "May", "June", "July", "August",
               "September", "October", "November", "December"]

# Page chrome and anything that is not reading content.
SKIP_TAGS = {"script", "style", "svg", "nav", "button", "audio", "head", "noscript", "canvas"}
SKIP_CLASSES = {"back-link", "field-mark", "footer", "audio-player", "progress-bar", "report-nav",
                "theme-toggle", "player-body", "pager", "page-toc", "topbar", "header-top-actions"}


class Markdown(HTMLParser):
    """A small HTML → markdown converter for the report vocabulary (see AGENTS.md)."""

    def __init__(self, page_url: str):
        super().__init__(convert_charrefs=True)
        self.url = page_url
        self.out: list[str] = []
        self.skip = 0                 # depth inside a skipped subtree
        self.stack: list[tuple[str, set[str]]] = []
        self.links: list[str] = []    # hrefs of open <a>
        self.lists: list[str] = []    # 'ul' / 'ol' nesting
        self.ol_n: list[int] = []
        self.row: list[str] | None = None
        self.table: list[list[str]] = []
        self.cell: list[str] | None = None
        self.pre = 0

    # ---- helpers
    def emit(self, s: str):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.out.append(s)

    def block(self, prefix: str = ""):
        self.emit("\n\n" + prefix)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = set((a.get("class") or "").split())
        void = tag in {"br", "img", "hr", "input", "meta", "link", "source"}
        if self.skip or tag in SKIP_TAGS or cls & SKIP_CLASSES:
            if not void:
                self.skip += 1
            if tag == "svg" and a.get("aria-label") and not self.skip - 1:
                self.block(f"*[{a['aria-label']}]*")
            return
        if not void:
            self.stack.append((tag, cls))
        if tag in {"h1", "h2", "h3", "h4"}:
            self.block("#" * int(tag[1]) + " ")
        elif "section-label" in cls:
            self.block("## ")
        elif "title" in cls and self._inside("news-item"):
            self.block("### ")
        elif "num" in cls:
            pass   # the story number; its text is dropped in handle_data
        elif cls & {"category", "special-category", "date-line", "special-date", "eyebrow"}:
            self.block("")
        elif cls & {"subtitle", "special-subtitle", "desc", "stat-note"} or tag in {"p", "figcaption"}:
            self.block("*" if tag == "figcaption" else "")
        elif "stat-card" in cls:
            self.block("- ")
        elif "stat-value" in cls or "value" in cls:
            self.emit("**")
        elif "sources" in cls:
            self.block("Sources: ")
        elif "follow-item" in cls:
            self.block("- ")
        elif "bullet" in cls:
            self.skip += 1
        elif tag in {"ul", "ol"}:
            self.lists.append(tag)
            self.ol_n.append(0)
            self.emit("\n")
        elif tag == "li":
            indent = "  " * (len(self.lists) - 1)
            if self.lists and self.lists[-1] == "ol":
                self.ol_n[-1] += 1
                self.emit(f"\n{indent}{self.ol_n[-1]}. ")
            else:
                self.emit(f"\n{indent}- ")
        elif tag == "blockquote":
            self.block("> ")
        elif tag == "pre":
            self.pre += 1
            self.block("```\n")
        elif tag == "code" and not self.pre:
            self.emit("`")
        elif tag in {"strong", "b"}:
            self.emit("**")
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag == "a":
            self.links.append(a.get("href") or "")
            if not self._inside("cite"):
                self.emit("[")
        elif tag == "br":
            self.emit("  \n")
        elif tag == "hr":
            self.block("---")
        elif tag == "table":
            self.table = []
        elif tag == "tr":
            self.row = []
        elif tag in {"td", "th"}:
            self.cell = []
        elif tag == "sup" and "cite" in cls:
            self.emit("[")

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            return
        if not self.stack:
            return
        open_tag, cls = self.stack.pop()
        while open_tag != tag and self.stack:   # tolerate unclosed tags
            open_tag, cls = self.stack.pop()
        if "stat-value" in cls or "value" in cls and self._inside("stat-card", cls):
            self.emit("** ")
        elif tag in {"strong", "b"}:
            self.emit("**")
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag == "figcaption":
            self.emit("*")
        elif tag == "code" and not self.pre:
            self.emit("`")
        elif tag == "pre":
            self.pre -= 1
            self.emit("\n```")
        elif tag == "a":
            href = self.links.pop() if self.links else ""
            if href.startswith("#source-"):
                pass   # a citation number: the enclosing [n] is written by the <sup>
            else:
                self.emit(f"]({urljoin(self.url, href)})" if href and not href.startswith("#") else "]")
        elif tag in {"ul", "ol"}:
            self.lists and self.lists.pop()
            self.ol_n and self.ol_n.pop()
            self.emit("\n")
        elif tag in {"td", "th"} and self.cell is not None and self.row is not None:
            self.row.append(" ".join("".join(self.cell).split()).replace("|", "\\|"))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table:
            width = max(len(r) for r in self.table)
            rows = [r + [""] * (width - len(r)) for r in self.table]
            lines = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * width]
            lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
            self.block("\n".join(lines))
            self.table = []
        elif tag == "sup" and "cite" in cls:
            self.emit("]")

    def handle_data(self, data):
        if self.skip:
            return
        if self.stack and "num" in self.stack[-1][1]:
            return
        if self.pre:
            self.emit(data)
        else:
            self.emit(re.sub(r"\s+", " ", data))

    def _inside(self, name, extra=None):
        return any(name in c for _, c in self.stack) or (extra is not None and name in extra)

    def markdown(self) -> str:
        text = "".join(self.out)
        text = re.sub(r"\n## Audio Briefing\s*\n", "\n", text)   # the player itself is not text
        text = re.sub(r"Sources: +", "Sources: ", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def report_markdown(entry: dict) -> str:
    path = REPORTS / entry["file"]
    html = path.read_text(encoding="utf-8", errors="replace")
    body = html[html.find("<body"):]
    url = f"{BASE}/reports/{entry['file']}"
    conv = Markdown(url)
    conv.feed(body)
    front = [
        "---",
        f"title: {json.dumps(entry['title'] if entry['type'] == 'special' else 'AI News Daily — ' + entry['date'], ensure_ascii=False)}",
        f"date: {entry['date']}",
        f"type: {entry['type']}",
        f"url: {url}",
        f"summary: {json.dumps(entry['summary'], ensure_ascii=False)}",
        f"tags: [{', '.join(entry['tags'])}]",
        f"reading_time_minutes: {entry['readingTime']}",
        "---",
        "",
    ]
    return "\n".join(front) + conv.markdown()


def headline(entry: dict) -> str:
    if entry["type"] == "daily":
        s = entry["summary"]
        return "AI News Daily" if not s or re.search(r"\{\w+\}", s) else s.split(" · ")[0]
    return " ".join(entry["title"].split())


def sitemap_md(reports: list[dict]) -> str:
    daily = [r for r in reports if r["type"] == "daily"]
    special = [r for r in reports if r["type"] == "special"]
    line = lambda r: f"- [{headline(r)}]({BASE}/reports/{r['file'][:-5]}.md) — {r['date']} · {r['readingTime']} min"
    out = ["# AI Reports", "",
           "Daily briefings and long-form special reports on AI, agents, models and AI engineering, "
           "written by Hermes Agent and edited by Luis González.", "",
           f"Every report has an HTML page and a markdown twin at the same path (`.html` / `.md`). "
           f"Index: {BASE}/ · RSS: {BASE}/rss.xml · Design tokens: {BASE}/tokens.json", ""]
    if daily:
        out += ["## Latest briefing", "", line(daily[0]), ""]
    out += ["## Special reports", ""]
    series: dict[str, list[dict]] = {}
    for r in special:
        series.setdefault(r.get("series") or "Other", []).append(r)
    for name in sorted(series):
        out += [f"### {name}", ""] + [line(r) for r in series[name]] + [""]
    out += ["## Daily briefings", ""]
    month = None
    for r in daily:
        y, m, _ = r["date"].split("-")
        label = f"{MONTHS_LONG[int(m) - 1]} {y}"
        if label != month:
            out += ["", f"### {label}", ""]
            month = label
        out.append(line(r))
    return "\n".join(out).replace("\n\n\n", "\n\n").strip() + "\n"


def tokens_json() -> str:
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    block = lambda sel: dict(re.findall(r"(--[\w-]+):\s*([^;]+);", re.search(re.escape(sel) + r"\s*\{(.*?)\n\}", css, re.S).group(1)))
    dark, light = block(":root"), block('[data-theme="light"]')
    pick = lambda prefixes: {k: re.sub(r"\s*/\*.*?\*/", "", v).strip() for k, v in dark.items() if k.startswith(prefixes)}
    tokens = {
        "$description": "AI Reports design tokens, generated from styles.css. Use the custom properties, never raw values. "
                        "Patterns: " + BASE + "/patterns.html · Rules: AGENTS.md in github.com/iamluisgb/reports",
        "color": {"dark": {k: v for k, v in dark.items() if k in light}, "light": light},
        "type": pick(("--f-", "--fs-")),
        "shape": pick(("--r-",)),
        "motion": pick(("--ease", "--spring", "--dur-")),
        "layout": pick(("--measure", "--topbar-h")),
    }
    return json.dumps(tokens, ensure_ascii=False, indent=2) + "\n"


def _write(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def write(reports: list[dict]) -> int:
    changed = 0
    for entry in reports:
        changed += _write(REPORTS / (entry["file"][:-5] + ".md"), report_markdown(entry))
    changed += _write(ROOT / "sitemap.md", sitemap_md(reports))
    changed += _write(ROOT / "tokens.json", tokens_json())
    return changed


if __name__ == "__main__":
    data = json.loads((ROOT / "reports.json").read_text(encoding="utf-8"))
    print(f"agent files updated: {write(data['reports'])}")
