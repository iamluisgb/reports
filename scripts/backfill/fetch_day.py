#!/usr/bin/env python3
"""Collect the real, dated source material for one past day.

The live pipeline (quiron skill `daily-digest`) reads today's HN front page and
the last 48h of blogwatcher, so it cannot be pointed at a date in the past.
This script replaces those sources with their archival equivalents:

  - Hacker News  -> Algolia search_by_date, filtered to that UTC day
  - ArXiv        -> Atom API filtered by submittedDate for that day

Everything it emits is a real item published on that date, with its URL. No
model is involved: the agent writes prose from this JSON, it does not invent it.

Usage: fetch_day.py YYYY-MM-DD [-o out.json] [--min-points N]
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

UA = "reports-backfill/1.0 (+https://luisgonzalezbernal.com/reports/)"

AI_KEYWORDS = (
    "ai", "llm", "gpt", "claude", "anthropic", "openai", "gemini", "deepseek",
    "mistral", "llama", "transformer", "diffusion", "agent", "agents", "rag",
    "embedding", "inference", "fine-tune", "finetune", "prompt", "neural",
    "machine learning", "ml", "model", "chatgpt", "copilot", "cuda", "gpu",
    "training", "reasoning", "hugging face", "pytorch", "tokenizer",
    "qwen", "gemma", "grok", "kimi", "vllm", "ollama", "agentic", "moe",
    "diffusion model", "text-to-image", "speech", "whisper", "benchmark",
)
INFRA_KEYWORDS = (
    "kubernetes", "k8s", "docker", "container", "linux", "kernel", "sre",
    "observability", "postgres", "database", "sqlite", "rust", "go ", "golang",
    "aws", "cloudflare", "terraform", "devops", "ci/cd", "deploy", "latency",
    "distributed", "outage", "incident", "performance", "networking", "systemd",
    "nginx", "redis", "kafka", "compiler", "security", "cve", "vulnerability",
)
PAPER_KEYWORDS = (
    "agent", "llm", "language model", "inference", "reasoning", "security",
    "kubernetes", "transformer", "retrieval", "alignment", "evaluation",
    "benchmark", "fine-tuning", "reinforcement", "multimodal", "efficiency",
)


def get(url, params, retries=3, timeout=30):
    qs = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{qs}", headers={"User-Agent": UA})
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001 - any transport error is retryable
            last = exc
            time.sleep(3 * (attempt + 1))
    raise SystemExit(f"fetch failed for {url}: {last}")


def day_bounds(day):
    start = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return int(start.timestamp()), int((start + timedelta(days=1)).timestamp())


def bucket(title):
    t = title.lower()
    if any(k in t for k in AI_KEYWORDS):
        return "ai"
    if any(k in t for k in INFRA_KEYWORDS):
        return "infra"
    return "hn"


def fetch_hn(day, min_points):
    lo, hi = day_bounds(day)
    raw = get(
        "https://hn.algolia.com/api/v1/search_by_date",
        {
            "tags": "story",
            "numericFilters": f"created_at_i>={lo},created_at_i<{hi},points>={min_points}",
            "hitsPerPage": 100,
        },
    )
    hits = json.loads(raw).get("hits", [])
    stories = [
        {
            "title": h["title"],
            "url": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
            "hn_url": f"https://news.ycombinator.com/item?id={h['objectID']}",
            "points": h.get("points", 0),
            "comments": h.get("num_comments", 0),
            "bucket": bucket(h["title"] or ""),
        }
        for h in hits
        if h.get("title")
    ]
    stories.sort(key=lambda s: s["points"], reverse=True)
    return stories


def arxiv_query(lo, hi, max_results, attempts=3):
    """A rate-limited reply and a genuinely empty day both come back with zero
    <entry> elements; only opensearch:totalResults tells them apart. Without
    this check a throttled query looks like "no papers that day" and the caller
    silently walks back to another date."""
    for attempt in range(attempts):
        xml = _arxiv_get(lo, hi, max_results)
        total = re.search(r"opensearch:totalResults[^>]*>(\d+)", xml or "")
        entries = xml.count("<entry>") if xml else 0
        if entries or not total or total.group(1) == "0":
            return xml
        time.sleep(5 * (attempt + 1))
    return xml


def _arxiv_get(lo, hi, max_results):
    return get(
        "https://export.arxiv.org/api/query",
        {
            "search_query": f"(cat:cs.AI OR cat:cs.LG OR cat:cs.CL) AND submittedDate:[{lo} TO {hi}]",
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        },
    )


def parse_arxiv(xml):
    papers = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        def tag(name):
            m = re.search(rf"<{name}>(.*?)</{name}>", entry, re.S)
            return " ".join(m.group(1).split()) if m else ""
        link = re.search(r'<id>(.*?)</id>', entry, re.S)
        title, summary = tag("title"), tag("summary")
        if not title:
            continue
        score = sum(1 for k in PAPER_KEYWORDS if k in (title + " " + summary).lower())
        papers.append(
            {
                "title": title,
                "abstract": summary,
                "url": link.group(1).strip() if link else "",
                "score": score,
            }
        )
    papers.sort(key=lambda p: p["score"], reverse=True)
    return papers


def already_cited(reports_dir):
    """Every source URL that appears in an already-published report."""
    used = set()
    for f in Path(reports_dir).glob("ai-news-*.html"):
        used.update(re.findall(r'href="(http[^"]+)"', f.read_text(encoding="utf-8", errors="replace")))
    # Strip only a trailing version suffix (…/2609.11900v2): splitting on "v"
    # would cut at the v in "arxiv" and collapse every paper onto one key.
    return {re.sub(r"v\d+$", "", u) if "arxiv.org/abs/" in u else u for u in used}


def fetch_arxiv(day, want=8, used=frozenset()):
    """ArXiv has no submissions at weekends and lags 1-2 days on indexing, so a
    recent date often comes back empty and we walk back for a real batch. Papers
    already cited in another report are dropped: without this, consecutive days
    that all fall back to the same batch publish the same five papers."""
    d = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    for back in range(4):
        probe = d - timedelta(days=back)
        lo = probe.strftime("%Y%m%d") + "0000"
        hi = probe.strftime("%Y%m%d") + "2359"
        papers = parse_arxiv(arxiv_query(lo, hi, 120))
        fresh = [p for p in papers if re.sub(r"v\d+$", "", p["url"]) not in used]
        if fresh:
            return {
                "date": probe.strftime("%Y-%m-%d"),
                "is_fallback": back > 0,
                "dropped_as_already_cited": len(papers) - len(fresh),
                "items": fresh[:want],
            }
        time.sleep(3)
    return {"date": day, "is_fallback": False, "dropped_as_already_cited": 0, "items": []}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("day")
    ap.add_argument("-o", "--output")
    ap.add_argument("--min-points", type=int, default=40)
    ap.add_argument("--exclude-used", action="store_true",
                    help="drop items already cited in reports/ (use when backfilling near other days)")
    args = ap.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.day):
        raise SystemExit("day must be YYYY-MM-DD")

    used = already_cited(Path(__file__).resolve().parents[2] / "reports") if args.exclude_used else frozenset()

    stories = fetch_hn(args.day, args.min_points)
    if len(stories) < 8 and args.min_points > 10:
        stories = fetch_hn(args.day, 10)
    if used:
        stories = [s for s in stories if s["url"] not in used and s["hn_url"] not in used]

    dt = datetime.strptime(args.day, "%Y-%m-%d")
    out = {
        "date": args.day,
        "date_line": f"{dt.strftime('%d %b %Y')} · {dt.strftime('%A').upper()}",
        "hn": {
            "top": stories[:12],
            "ai": [s for s in stories if s["bucket"] == "ai"][:8],
            "infra": [s for s in stories if s["bucket"] == "infra"][:6],
            "other": [s for s in stories if s["bucket"] == "hn"][:8],
            "count": len(stories),
        },
        "papers": fetch_arxiv(args.day, used=used),
    }
    text = json.dumps(out, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"{args.day}: {len(stories)} HN stories, {len(out['papers']['items'])} papers -> {args.output}")
    else:
        print(text)


if __name__ == "__main__":
    main()
