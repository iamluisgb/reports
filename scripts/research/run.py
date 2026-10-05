#!/usr/bin/env python3
"""Research pipeline for special reports: plan → search → read → extract → rank.

    python3 scripts/research/run.py data/research/<slug>/plan.json [--stage all|search|read|extract|rank]

Writes next to the plan:
  candidates.json   search results, deduplicated and pre-ranked per question
  pages/<id>.md     the text of each source (Jina Reader)
  extracts/<id>.json  claims extracted from ONE source by a NaN model, each with a
                    verbatim quote; claims whose quote is not in the page are dropped
  evidence.json     the evidence pack: numbered sources, quality, claims, quotes
  evidence.md       the same, readable, grouped by question — what the writer works from

Every stage is resumable: finished work on disk is not redone.

Why this split (see AGENTS.md → Special reports): in multi-agent deep research the
orchestrating/synthesising step causes most errors, while agents that summarise a
single document are reliable. So NaN models only ever see one source at a time, and
the synthesis is done afterwards by the writer (Claude) from the evidence pack, with
scripts/research/verify.py checking every citation against it.

Plan format (plan.json):
{
  "slug": "context-lake", "title": "...", "thesis": "...", "audience": "...",
  "since": "2025-01-01",                        # ignore sources older than this (optional)
  "per_question": 10,                           # sources kept per question after pre-ranking
  "questions": [
    {"id": "q1", "question": "What is a context lake and who defines it?",
     "queries": ["context lake agents", "shared context layer multi-agent"],
     "providers": ["web", "hn", "arxiv", "github", "wikipedia", "semantic_scholar"]}
  ]
}
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.parse
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nan  # noqa: E402
import sources  # noqa: E402

# How much a kind of source counts. Primary and academic sources first; generic
# search otherwise prefers SEO pages over papers.
TYPE_WEIGHT = {"primary": 1.0, "academic": 1.0, "official": 0.9, "data": 0.9, "news": 0.7,
               "vendor": 0.6, "blog": 0.5, "forum": 0.35, "other": 0.3}
LOW_QUALITY_HOSTS = ("medium.com/@", "linkedin.com/pulse", "towardsdatascience", "geeksforgeeks",
                     "analyticsvidhya", "simplilearn", "quora.com", "pinterest.")
PAGE_CHARS = 24000          # what one extraction call reads; long pages are cut here
READ_DELAY = 3.2            # Jina Reader keyless: ~20 requests/minute


def norm_url(u: str) -> str:
    p = urllib.parse.urlsplit(u.strip())
    q = "&".join(x for x in p.query.split("&") if x and not x.startswith(("utm_", "ref=", "source=")))
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower().removeprefix("www."), p.path.rstrip("/"), q, ""))


def sid(url: str) -> str:
    return hashlib.sha1(norm_url(url).encode()).hexdigest()[:10]


def load(p: Path, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def save(p: Path, data) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- search
def stage_search(plan: dict, d: Path) -> None:
    out = d / "candidates.json"
    if out.exists():
        print("search: done already"); return
    if not sources.has_web():
        print("search: no TAVILY_API_KEY / EXA_API_KEY — general web search skipped; "
              "specialised sources only (HN links stand in for the web)", file=sys.stderr)
    found: dict[str, dict] = {}
    for q in plan["questions"]:
        for query in q["queries"]:
            for prov in q.get("providers", ["web", "hn", "arxiv"]):
                try:
                    hits = sources.PROVIDERS[prov](query)
                except Exception as exc:
                    print(f"  ! {prov} '{query}': {exc}", file=sys.stderr); hits = []
                for h in hits:
                    if not h.get("url"):
                        continue
                    key = sid(h["url"])
                    item = found.setdefault(key, {**h, "id": key, "questions": [], "queries": []})
                    if q["id"] not in item["questions"]:
                        item["questions"].append(q["id"])
                    item["queries"].append(query)
                print(f"  {prov:16} {len(hits):>2}  {query}", file=sys.stderr)
                time.sleep(0.5)
    since = plan.get("since")
    items = [i for i in found.values() if not (since and i.get("published") and i["published"][:4].isdigit()
                                               and i["published"][:10] < since)]
    # Pre-rank per question with NaN's reranker on title + snippet; keep the best N each.
    keep: set[str] = set()
    for q in plan["questions"]:
        pool = [i for i in items if q["id"] in i["questions"]]
        scores = nan.rerank(q["question"], [f"{i['title']}\n{i['snippet']}" for i in pool])
        for i, s in zip(pool, scores):
            i.setdefault("relevance", {})[q["id"]] = round(s, 4)
        for i in sorted(pool, key=lambda i: -i["relevance"][q["id"]])[: plan.get("per_question", 10)]:
            keep.add(i["id"])
    chosen = [i for i in items if i["id"] in keep]
    save(out, {"searched": len(found), "kept": len(chosen), "web_search": sources.has_web(), "candidates": chosen})
    print(f"search: {len(found)} results, {len(chosen)} kept")


# ---------------------------------------------------------------- read
def stage_read(plan: dict, d: Path) -> None:
    cands = load(d / "candidates.json", {}).get("candidates", [])
    failed = 0
    for i, c in enumerate(cands, 1):
        page = d / "pages" / f"{c['id']}.md"
        if page.exists():
            continue
        try:
            text = sources.read_page(c["url"])
        except Exception as exc:
            print(f"  ! read {c['url']}: {exc}", file=sys.stderr)
            text = ""
            failed += 1
        if len(text) < 400 and c.get("snippet"):     # unreadable page: keep at least the abstract
            text = f"Title: {c['title']}\nURL Source: {c['url']}\n\n{c['snippet']}"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(text, encoding="utf-8")
        print(f"  read {i}/{len(cands)} {len(text):>6} chars  {c['url'][:80]}", file=sys.stderr)
        time.sleep(READ_DELAY)
    print(f"read: {len(list((d / 'pages').glob('*.md')))} pages, {failed} unreadable this run")
    # A pack built from search snippets alone looks complete and is not: stop instead.
    if cands and failed > len(cands) / 2:
        raise SystemExit(f"read: {failed} of {len(cands)} pages could not be read — fix the reader "
                         "(rate limit? blocked?), delete pages/ and run again")


# ---------------------------------------------------------------- extract
EXTRACT_PROMPT = """You are extracting evidence from ONE source for a research report.

Report: {title}
Thesis being tested (do not assume it is true): {thesis}
Questions:
{questions}

Source URL: {url}
Source text (may be cut):
<<<
{text}
>>>

Return ONLY a JSON object:
{{
  "relevant": true/false,               // does this source help answer any question?
  "source_type": "primary|academic|official|data|news|vendor|blog|forum|other",
  "published": "YYYY-MM-DD or null",    // from the text only; null if not stated
  "author_or_org": "who wrote or published it, or null",
  "claims": [
    {{"question": "q1",
      "claim": "one factual statement in your own words, specific, with numbers if any",
      "quote": "the exact sentence(s) from the source text that support it, copied verbatim",
      "numbers": ["every figure in the claim, as written in the quote"]}}
  ]
}}
Rules: at most 8 claims; only claims the text itself supports; the quote must be copied
character for character from the source text above (no paraphrase, no ellipsis inside);
prefer figures, dates, definitions, named systems and direct statements of position;
skip marketing superlatives without evidence. If not relevant, return claims: [].
"""


def _normalise(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", re.sub(r"[*_`#>\[\]]", "", s)).strip().lower()


def quote_found(quote: str, page: str) -> bool:
    q, p = _normalise(quote), _normalise(page)
    if len(q) < 12:
        return False
    if q in p:
        return True
    # Accept a quote whose every 8-word window occurs in the page (tolerates line-break
    # artefacts from HTML-to-markdown), never a paraphrase.
    words = q.split()
    windows = [" ".join(words[i:i + 8]) for i in range(0, max(1, len(words) - 7), 4)]
    return all(w in p for w in windows)


def stage_extract(plan: dict, d: Path) -> None:
    cands = load(d / "candidates.json", {}).get("candidates", [])
    qtext = "\n".join(f"- {q['id']}: {q['question']}" for q in plan["questions"])
    for i, c in enumerate(cands, 1):
        out = d / "extracts" / f"{c['id']}.json"
        page_p = d / "pages" / f"{c['id']}.md"
        if out.exists() or not page_p.exists():
            continue
        page = page_p.read_text(encoding="utf-8")
        prompt = EXTRACT_PROMPT.format(title=plan["title"], thesis=plan.get("thesis", ""), questions=qtext,
                                       url=c["url"], text=page[:PAGE_CHARS])
        try:
            data, model = nan.chat_json(prompt, f"extract {i}/{len(cands)}")
        except RuntimeError as exc:
            print(f"  ! {exc}", file=sys.stderr); continue
        kept, dropped = [], 0
        for cl in data.get("claims") or []:
            if cl.get("quote") and quote_found(cl["quote"], page):
                kept.append(cl)
            else:
                dropped += 1
        save(out, {**data, "claims": kept, "dropped_unverified_quotes": dropped, "model": model, "url": c["url"]})
    print(f"extract: {len(list((d / 'extracts').glob('*.json')))} sources extracted")


# ---------------------------------------------------------------- rank → evidence pack
def quality(url: str, stype: str, snippet: str = "") -> float:
    w = TYPE_WEIGHT.get(stype or "other", 0.3)
    if any(h in url for h in LOW_QUALITY_HOSTS):
        w *= 0.5
    # A repository is primary evidence of what it does, not of adoption or quality:
    # weigh it by its stars, so a personal project with none doesn't rank like a paper.
    if "github.com/" in url:
        m = re.search(r"\((\d+) stars\)", snippet or "")
        stars = int(m.group(1)) if m else 0
        w = min(w, 0.4 if stars < 50 else 0.6 if stars < 1000 else 0.9)
    return round(w, 2)


def stage_rank(plan: dict, d: Path) -> None:
    cands = {c["id"]: c for c in load(d / "candidates.json", {}).get("candidates", [])}
    srcs = []
    for p in sorted((d / "extracts").glob("*.json")):
        x = load(p, {})
        c = cands.get(p.stem)
        if not c or not x.get("relevant") or not x.get("claims"):
            continue
        srcs.append({"id": p.stem, "url": c["url"], "title": c["title"], "provider": c["provider"],
                     "discussion": c.get("discussion"), "type": x.get("source_type") or "other",
                     "published": x.get("published") or c.get("published") or None,
                     "org": x.get("author_or_org"), "quality": quality(c["url"], x.get("source_type"), c.get("snippet", "")),
                     "claims": x["claims"], "dropped": x.get("dropped_unverified_quotes", 0)})
    # Deduplicate claims across sources: near-identical statements become one claim
    # with corroborating sources (kept on the best-quality source).
    flat = [(s, cl) for s in srcs for cl in s["claims"]]
    vecs = nan.embed([cl["claim"] for _, cl in flat]) if flat else []
    owner = list(range(len(flat)))
    for i in range(len(flat)):
        for j in range(i):
            if owner[j] == j and nan.cosine(vecs[i], vecs[j]) > 0.92:
                a, b = (j, i) if flat[j][0]["quality"] >= flat[i][0]["quality"] else (i, j)
                owner[b] = a
                break
    for idx, (s, cl) in enumerate(flat):
        cl["corroborated_by"] = sorted({flat[k][0]["id"] for k in range(len(flat)) if owner[k] == idx and k != idx})
        cl["duplicate"] = owner[idx] != idx
    # Number sources by quality, then by how many claims they carry.
    srcs.sort(key=lambda s: (-s["quality"], -len(s["claims"])))
    num = {s["id"]: n for n, s in enumerate(srcs, 1)}
    for s in srcs:
        s["n"] = num[s["id"]]
        s["claims"] = [dict(cl, id=f"S{s['n']}.{k}", corroborated_by=[num[c] for c in cl["corroborated_by"] if c in num])
                       for k, cl in enumerate((c for c in s["claims"] if not c["duplicate"]), 1)]
        for cl in s["claims"]:
            cl.pop("duplicate", None)
    meta = load(d / "candidates.json", {})
    stats = {"searched": meta.get("searched"), "candidates": meta.get("kept"), "web_search": meta.get("web_search"),
             "read": len(list((d / "pages").glob("*.md"))), "sources_with_evidence": len(srcs),
             "claims": sum(len(s["claims"]) for s in srcs),
             "quotes_dropped_as_unverified": sum(s["dropped"] for s in srcs)}
    save(d / "evidence.json", {"plan": plan, "generated": date.today().isoformat(), "stats": stats, "sources": srcs})
    # Readable version for the writer: by question, best sources first.
    lines = [f"# Evidence — {plan['title']}", "", f"Generated {date.today().isoformat()} · " +
             " · ".join(f"{k}: {v}" for k, v in stats.items()), ""]
    for q in plan["questions"]:
        lines += [f"## {q['id']}. {q['question']}", ""]
        for s in srcs:
            for cl in s["claims"]:
                if cl.get("question") == q["id"]:
                    also = f" (also {', '.join(f'[{n}]' for n in cl['corroborated_by'])})" if cl["corroborated_by"] else ""
                    lines += [f"- **[{s['n']}] {cl['claim']}**{also}", f"  > {cl['quote']}"]
        lines.append("")
    lines += ["## Sources", ""] + [f"{s['n']}. {s['title']} — {s['org'] or ''} ({s['type']}, {s['published'] or 'undated'}, "
                                   f"quality {s['quality']}) — {s['url']}" for s in srcs]
    (d / "evidence.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("rank: " + ", ".join(f"{k}={v}" for k, v in stats.items()))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--stage", default="all", choices=["all", "search", "read", "extract", "rank"])
    a = ap.parse_args()
    plan_p = Path(a.plan)
    plan, d = load(plan_p, None), plan_p.parent
    if not plan:
        raise SystemExit(f"no plan at {plan_p}")
    stages = ["search", "read", "extract", "rank"] if a.stage == "all" else [a.stage]
    for s in stages:
        {"search": stage_search, "read": stage_read, "extract": stage_extract, "rank": stage_rank}[s](plan, d)


if __name__ == "__main__":
    main()
