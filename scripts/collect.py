#!/usr/bin/env python3
"""Gather the day's raw candidates — no LLM, no judgement, just fetching.

Reads the Hacker News front pages, validates every story id against the
Firebase API (so a comment id never becomes a "story" link), pulls the arXiv
listings the report draws its papers from (cs.AI, cs.SE, cs.MA) plus an
agent-engineering sweep of arXiv's own API, drops anything the last few reports
already covered, and writes one JSON bundle for write_report.py to choose from.

Every candidate carries a short id (hn-49672510, arxiv-2609.11318). The writer
selects by id and never invents a URL, so a link in the report is a link that
was fetched and checked here.

Usage:
  collect.py                       # today, -> /tmp/candidates-<day>.json
  collect.py --day 2026-09-13 --out bundle.json
  collect.py --dedup-days 5
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# NaN's edge is not the only thing that dislikes Python-urllib: arXiv throttles
# it harder too. Announce a browser everywhere.
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
HN_PAGES = 3
# ~30 stories a page. The third page is cheap and it is where a story that
# broke overnight sits while it is still climbing.
# cs.AI was the only listing this report read, and the discipline it is written
# for gets filed elsewhere: a source-code study of eleven coding harnesses is
# cs.SE with a cs.MA cross-list, so it was never on the page we downloaded —
# not ranked low, absent. Each category now carries its own quota instead of
# competing for one budget of cs.AI submissions.
ARXIV_BUDGET = (
    ("cs.AI", 7),
    ("cs.SE", 3),
    ("cs.MA", 1),
)
# arXiv's listing is submission order, not relevance, so rank titles before
# spending a request per abstract. Without this the papers section fills up
# with species identification and recommender regularisation.
PAPER_KEYWORDS = re.compile(
    r"agent|LLM|language model|reason|inference|eval|benchmark|memory|context|"
    r"retriev|RAG|distill|transformer|attention|reinforcement|RLHF|RLVR|align|"
    r"interpretab|tool.use|code|security|adversarial|jailbreak|scaling|MoE|"
    r"mixture.of.experts|quantiz|serving|latency|throughput|harness|architect|"
    r"orchestrat|scaffold|sandbox|runtime|workflow|repositor|developer|"
    r"multi.agent|coding", re.I)
# arXiv's API answers "Rate exceeded" often enough that the abs pages, one
# request each, are the reliable path. Keep the batch small.
PAUSE = 1.0

# ---------------------------------------------------- the semantic-layer beat
# This section exists because the vocabulary is unstable. "Ontology",
# "knowledge graph", "context graph", "semantic layer", "data fabric" and
# "metric layer" are one conversation held at different altitudes by different
# vendors, so a collector that bet on a single word would miss most of the day.
# Hunt the whole family at once and let the writer judge what it got.
SEMANTIC_TERMS = [
    "ontology", "ontologies", "knowledge graph", "context graph",
    "semantic layer", "semantic model", "semantic web", "property graph",
    "graph database", "GraphRAG", "KG-RAG", "knowledge graph embedding",
    "entity resolution", "RDF", "OWL", "SPARQL", "triplestore", "taxonomy",
    "data fabric", "data mesh", "metadata layer", "metric layer",
    "master data management", "digital twin", "knowledge base",
]
# The distinctive ones are worth an arXiv query; the rest stay in
# SEMANTIC_TERMS to rank whatever that query brings back.
SEMANTIC_QUERY = [
    "ontology", "knowledge graph", "context graph", "semantic layer",
    "semantic model", "GraphRAG", "KG-RAG", "property graph",
    "entity resolution", "knowledge graph embedding", "RDF", "data fabric",
]
SEMANTIC_QUERY_FALLBACK = ["ontology", "knowledge graph", "semantic layer",
                           "context graph", "GraphRAG"]
SEMANTIC_HN_QUERIES = ["ontology", "knowledge graph", "context graph",
                       "semantic layer", "GraphRAG", "property graph",
                       "RDF", "digital twin", "data fabric",
                       "entity resolution"]
# Algolia matches fuzzily, so "Walk the Endless Dungeon" comes back for a
# knowledge-graph query. A hit is only a beat story if its title actually says
# so; arXiv needs no equivalent filter because its query is a phrase match.
SEMANTIC_HIT = re.compile(
    r"ontolog|semantic|knowledge|graphrag|kg-rag|property\s+graph|"
    r"context\s+graph|\bgraphs?\b|\bRDF\b|\bOWL\b|SPARQL|triplestore|"
    r"taxonom|data\s+(?:fabric|mesh)|entity\s+resolution|digital\s+twin|"
    r"metadata\s+layer|metric\s+layer|master\s+data|\bschemas?\b|\bKGs?\b",
    re.I)
SEMANTIC_WANT = 8
SEMANTIC_WINDOW_DAYS = 4        # arXiv does not announce at weekends
SEMANTIC_HN_DAYS = 4


def fetch(url, tries=3, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as exc:
            if attempt == tries - 1:
                print(f"  ! giving up on {url}: {exc}", file=sys.stderr)
                return ""
            time.sleep(2 * (attempt + 1))
    return ""


def clean(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s))).strip()


# ---------------------------------------------------------------- Hacker News

def hacker_news():
    """Front-page stories, ranked, with points and comment counts."""
    rows = []
    for page in range(1, HN_PAGES + 1):
        url = "https://news.ycombinator.com/" + (f"?p={page}" if page > 1 else "")
        page_html = fetch(url)
        for sid, head, sub in re.findall(
                r'<tr class="athing submission" id="(\d+)">(.*?)</tr>\s*<tr>(.*?)</tr>',
                page_html, re.S):
            m = re.search(r'<span class="titleline"><a href="([^"]+)"[^>]*>(.*?)</a>',
                          head, re.S)
            if not m:
                continue
            rank = re.search(r'<span class="rank">(\d+)', head)
            points = re.search(r"(\d+)\s*point", sub)
            comments = re.search(r">(\d+)&nbsp;comments?<", sub)
            rows.append({
                "id": f"hn-{sid}",
                "story_id": sid,
                "rank": int(rank.group(1)) if rank else 999,
                "title": clean(m.group(2)),
                "url": m.group(1),
                "points": int(points.group(1)) if points else 0,
                "comments": int(comments.group(1)) if comments else 0,
                "hn_url": f"https://news.ycombinator.com/item?id={sid}",
            })
        time.sleep(PAUSE)
    rows.sort(key=lambda r: r["rank"])
    return rows


def verify_stories(rows):
    """Drop anything Firebase does not confirm as a story.

    A comment id in a `sources` link is a broken link on the published page,
    and the front-page HTML is not a strong enough guarantee on its own.
    """
    kept = []
    for row in rows:
        raw = fetch(f"https://hacker-news.firebaseio.com/v0/item/{row['story_id']}.json",
                    tries=2, timeout=15)
        try:
            item = json.loads(raw) if raw else None
        except json.JSONDecodeError:
            item = None
        if not item or item.get("type") != "story":
            print(f"  - dropped {row['id']}: not a story", file=sys.stderr)
            continue
        # Trust Firebase's url over the scraped one; Ask HN posts have none.
        row["url"] = item.get("url") or row["hn_url"]
        kept.append(row)
    return kept


# --------------------------------------------------------------------- arXiv

def arxiv_listing(cat, want):
    """`want` papers with abstracts from one category's most recent listing.

    arXiv does not announce at weekends, so on a Saturday or Sunday this
    returns the previous weekday's batch — still fresh relative to the reports,
    because cross-dedup removes whatever yesterday already used.

    A listing shows that category's new submissions *and* the papers
    cross-listed into it, which is how a cs.AI paper about agent coordination
    reaches cs.MA.
    """
    listing = fetch(f"https://arxiv.org/list/{cat}/recent?skip=0&show=100")
    if not listing:
        return []
    day = re.search(r"<h3>(.*?)</h3>", listing)
    print(f"  arXiv {cat} listing: {clean(day.group(1)) if day else 'unknown'}",
          file=sys.stderr)

    # Pair each id with the title that follows it, so relevance can be judged
    # before an abstract is worth a request.
    entries, seen = [], set()
    for paper_id, title in re.findall(
            r"arXiv:(\d{4}\.\d{4,5}).*?<div class='list-title mathjax'>"
            r"<span class='descriptor'>Title:</span>\s*(.*?)\s*</div>", listing, re.S):
        if paper_id in seen:
            continue
        seen.add(paper_id)
        entries.append((paper_id, clean(title)))
    if not entries:  # listing markup changed; fall back to submission order
        entries = [(pid, "") for pid in dict.fromkeys(
            re.findall(r"arXiv:(\d{4}\.\d{4,5})", listing))]

    entries.sort(key=lambda e: -len(set(m.group(0).lower()
                                        for m in PAPER_KEYWORDS.finditer(e[1]))))

    papers = []
    for paper_id, _ in entries[:want]:
        page = fetch(f"https://arxiv.org/abs/{paper_id}", tries=2)
        time.sleep(PAUSE)
        if not page:
            continue
        title = re.search(
            r'<h1 class="title mathjax"><span class="descriptor">Title:</span>(.*?)</h1>',
            page, re.S)
        abstract = re.search(
            r'<blockquote class="abstract mathjax">\s*'
            r'<span class="descriptor">Abstract:</span>(.*?)</blockquote>', page, re.S)
        version = re.search(rf"arXiv:{re.escape(paper_id)}(v\d+)", page)
        if not (title and abstract):
            continue
        papers.append({
            "id": f"arxiv-{paper_id}",
            "cat": cat,
            "title": clean(title.group(1)),
            "abstract": clean(abstract.group(1)),
            "url": f"http://arxiv.org/abs/{paper_id}{version.group(1) if version else 'v1'}",
        })
    return papers


def arxiv():
    """Every category listing the report draws papers from, in quota order.

    The pool is handed to the writer whole, and the writer only ever sees
    write_report.MAX_PAPERS of it, so the quotas have to sum to less than that
    cap: papers appended past it are not ranked low, they are never shown.
    """
    papers = []
    for cat, want in ARXIV_BUDGET:
        papers.extend(arxiv_listing(cat, want))
    return papers


# ------------------------------------------------ the agent-engineering beat
# The extra listing slots are a quota, not a guarantee. A listing only ever
# shows the most recent announcement day, so a Friday submission read on
# Monday is already off the page, and a paper whose primary category we do not
# list stays invisible however relevant it is. This beat asks arXiv's own API
# instead: one request returns titles and abstracts together, over a window
# that spans the weekend.
ENG_TERMS = [
    "agent", "agentic", "harness", "orchestrat", "multi-agent", "LLM",
    "code", "software engineering", "developer", "repo", "sandbox",
    "runtime", "context", "tool use", "scaffold", "workflow",
]
# Two tiers, the shape the semantic beat already uses. The specific phrases go
# first: a generic "agentic" query comes back with sixty papers and buries the
# one worth having. Measured against the July window this report missed, the
# tier below puts the harness-engineering study first of sixteen hits, where
# the generic tier ranks it fifty-eighth of sixty.
ENG_QUERY = ["harness engineering", "coding harness", "agent harness",
             "coding agent", "agentic software engineering",
             "context engineering", "software engineering agent"]
ENG_QUERY_FALLBACK = ["LLM agent", "agentic", "multi-agent",
                      "agent orchestration"]
ENG_WANT = 3
ENG_WINDOW_DAYS = 5


def eng_score(paper):
    """How much of the beat's vocabulary a paper carries.

    Weighted towards the title, which is where a paper says what it is about,
    with the abstract as the tie-breaker.
    """
    title = paper["title"].lower()
    body = paper["abstract"].lower()
    return (3 * sum(1 for t in ENG_TERMS if t in title) +
            sum(1 for t in ENG_TERMS if t in body))


def eng_arxiv(want=ENG_WANT, days=ENG_WINDOW_DAYS):
    """Fresh cs.SE / cs.MA submissions about building and running agents.

    The `cat:` clause matches cross-lists as well as primary categories, so
    this also reaches coding-agent work filed under cs.AI or cs.LG that would
    otherwise only be met if it were announced on a weekday we list.
    """
    cutoff = datetime.now().astimezone() - timedelta(days=days)
    for terms in (ENG_QUERY, ENG_QUERY_FALLBACK):
        query = ("(cat:cs.SE OR cat:cs.MA) AND (" +
                 " OR ".join(f'all:"{t}"' for t in terms) + ")")
        raw = fetch("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
            "search_query": query, "max_results": 60,
            "sortBy": "submittedDate", "sortOrder": "descending"}))
        time.sleep(PAUSE)
        if not raw:
            continue
        found = []
        for entry in re.findall(r"<entry>(.*?)</entry>", raw, re.S):
            ident = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", entry)
            title = re.search(r"<title>(.*?)</title>", entry, re.S)
            abstract = re.search(r"<summary>(.*?)</summary>", entry, re.S)
            published = re.search(r"<published>([^<]+)</published>", entry)
            if not (ident and title and abstract and published):
                continue
            try:
                when = datetime.strptime(published.group(1)[:10], "%Y-%m-%d")
            except ValueError:
                continue
            if when.replace(tzinfo=cutoff.tzinfo) < cutoff:
                continue
            # The API hands back a versioned id, the listing path does not.
            # Both have to name the same paper, or the day carries it twice.
            paper_id = re.sub(r"v\d+$", "", ident.group(1))
            found.append({
                "id": f"arxiv-{paper_id}",
                "cat": "cs.SE/cs.MA",
                "title": clean(title.group(1)),
                "abstract": clean(abstract.group(1)),
                "url": f"https://arxiv.org/abs/{ident.group(1)}",
                "published": published.group(1)[:10],
            })
        if not found:
            continue
        found.sort(key=lambda p: -eng_score(p))
        return found[:want]
    return []


# ---------------------------------------------------------- shared helpers

def _urlkey(url):
    """Scheme- and version-insensitive URL key, for cross-source dedup.

    One paper reaches us as http://arxiv.org/abs/Xv1 from the front-page path
    and https://arxiv.org/abs/X from the beat; comparing raw strings would
    publish it twice.
    """
    key = re.sub(r"^https?://", "", url or "")
    return re.sub(r"v\d+$", "", key).rstrip("/")


def _titlekey(title):
    """Case- and punctuation-insensitive title key, for exact-title dedup.

    Two unrelated papers can open with the same words — "Harness Engineering"
    is the first half of the title of two different 2026 papers — so this only
    ever collapses titles that are equal once normalised, never a near match.
    Genuinely different papers with similar names both survive.
    """
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def merge_papers(*groups):
    """The day's paper pool: first paper per arXiv id, then per exact title.

    The listing path and the API beat both name a paper arxiv-<id>, so an id
    collision is the same paper arriving twice, not two papers.
    """
    papers, ids, titles = [], set(), set()
    for group in groups:
        for paper in group:
            if paper["id"] in ids:
                print(f"  - deduped {paper['id']}: same paper from another source",
                      file=sys.stderr)
                continue
            key = _titlekey(paper["title"])
            if key and key in titles:
                print(f"  - deduped {paper['id']}: same title as a paper already "
                      f"in the pool", file=sys.stderr)
                continue
            ids.add(paper["id"])
            titles.add(key)
            papers.append(paper)
    return papers


# ---------------------------------------------------- the semantic-layer beat

def semantic_arxiv(want=SEMANTIC_WANT, days=SEMANTIC_WINDOW_DAYS):
    """Fresh arXiv submissions in the semantic-layer family.

    One API call returns titles and abstracts together, so this costs a single
    request where the front-page path spends one per paper.
    """
    cutoff = datetime.now().astimezone() - timedelta(days=days)
    for terms in (SEMANTIC_QUERY, SEMANTIC_QUERY_FALLBACK):
        query = " OR ".join(f'all:"{t}"' for t in terms)
        raw = fetch("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
            "search_query": query, "max_results": 60,
            "sortBy": "submittedDate", "sortOrder": "descending"}))
        time.sleep(PAUSE)
        if not raw:
            continue
        found = []
        for entry in re.findall(r"<entry>(.*?)</entry>", raw, re.S):
            pid = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", entry)
            title = re.search(r"<title>(.*?)</title>", entry, re.S)
            abstract = re.search(r"<summary>(.*?)</summary>", entry, re.S)
            published = re.search(r"<published>([^<]+)</published>", entry)
            if not (pid and title and abstract and published):
                continue
            try:
                when = datetime.strptime(published.group(1)[:10], "%Y-%m-%d")
            except ValueError:
                continue
            if when.replace(tzinfo=cutoff.tzinfo) < cutoff:
                continue
            found.append({
                "id": f"kg-arxiv-{pid.group(1)}",
                "title": clean(title.group(1)),
                "abstract": clean(abstract.group(1)),
                "url": f"https://arxiv.org/abs/{pid.group(1)}",
                "published": published.group(1)[:10],
                "kind": "paper",
            })
        if not found:
            continue
        # arXiv's own relevance is blunt; rank on how many of the family's
        # words the title carries, which is where a paper says what it is about.
        found.sort(key=lambda p: -len({t for t in SEMANTIC_TERMS
                                       if t.lower() in p["title"].lower()}))
        return found[:want]
    return []


def semantic_hn(days=SEMANTIC_HN_DAYS, want=SEMANTIC_WANT):
    """Recent Hacker News submissions about the same family, hottest first.

    This is where the naming actually drifts — vendor posts, blog essays and
    releases use words arXiv does not — so the beat is worth its queries.
    """
    since = int(time.time()) - days * 86400
    rows, seen_ids = [], set()
    for query in SEMANTIC_HN_QUERIES:
        raw = fetch("https://hn.algolia.com/api/v1/search_by_date?" +
                    urllib.parse.urlencode({
                        "query": query, "tags": "story", "hitsPerPage": 10,
                        "numericFilters": f"created_at_i>{since}"}),
                    tries=2, timeout=20)
        time.sleep(0.3)
        try:
            hits = json.loads(raw).get("hits", []) if raw else []
        except json.JSONDecodeError:
            continue
        for hit in hits:
            sid = str(hit.get("objectID") or "").strip()
            title = clean(str(hit.get("title") or ""))
            if not sid or not title or sid in seen_ids:
                continue
            if not SEMANTIC_HIT.search(title):
                continue
            seen_ids.add(sid)
            hn_url = f"https://news.ycombinator.com/item?id={sid}"
            rows.append({
                "id": f"kg-hn-{sid}",
                "story_id": sid,
                "title": title,
                "url": hit.get("url") or hn_url,
                "hn_url": hn_url,
                "points": int(hit.get("points") or 0),
                "comments": int(hit.get("num_comments") or 0),
                "created": str(hit.get("created_at") or "")[:10],
                "kind": "story",
            })
    rows.sort(key=lambda r: -r["points"])
    return rows[:want]


# ----------------------------------------------------------------- dedup

def recent_urls(day, days):
    """Every URL the last `days` reports linked to, for cross-dedup."""
    urls = set()
    for back in range(1, days + 1):
        previous = day - timedelta(days=back)
        path = ROOT / "reports" / f"ai-news-{previous.isoformat()}.html"
        if not path.exists():
            continue
        for url in re.findall(r'<a href="([^"]+)">', path.read_text(encoding="utf-8")):
            urls.add(url.rstrip("/"))
    return urls


def drop_seen(items, seen):
    """`seen` holds _urlkey keys, so a scheme or version difference is not a
    new story: the listing links http://arxiv.org/abs/Xv1 and the beat links
    the same paper as https://arxiv.org/abs/X."""
    fresh = []
    for item in items:
        if _urlkey(item["url"]) in seen:
            print(f"  - deduped {item['id']}: already reported", file=sys.stderr)
            continue
        fresh.append(item)
    return fresh


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", default=date.today().isoformat())
    ap.add_argument("--out")
    ap.add_argument("--dedup-days", type=int, default=3)
    args = ap.parse_args()

    day = datetime.strptime(args.day, "%Y-%m-%d").date()
    out = Path(args.out) if args.out else Path(f"/tmp/candidates-{args.day}.json")

    print("collecting Hacker News…", file=sys.stderr)
    stories = verify_stories(hacker_news())
    print("collecting arXiv…", file=sys.stderr)
    papers = merge_papers(arxiv(), eng_arxiv())
    print("collecting the semantic-layer beat…", file=sys.stderr)
    topic = semantic_arxiv() + semantic_hn()

    seen = {_urlkey(url) for url in recent_urls(day, args.dedup_days)}
    stories = drop_seen(stories, seen)
    papers = drop_seen(papers, seen)
    # One story, one section. The beat overlaps the front page by design, so
    # drop whatever the day already carries elsewhere before the writer sees
    # it — otherwise the same link prints in two sections.
    carried = ({_urlkey(s["url"]) for s in stories} |
               {_urlkey(p["url"]) for p in papers})
    topic = [t for t in topic if _urlkey(t["url"]) not in seen
             and _urlkey(t["url"]) not in carried]

    if not stories:
        raise SystemExit("no Hacker News candidates survived — refusing to write a report")

    bundle = {
        "day": args.day,
        "weekday": day.strftime("%A"),
        "collected_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "stories": stories,
        "papers": papers,
        "topic": topic,
    }
    out.write_text(json.dumps(bundle, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{args.day}: {len(stories)} stories, {len(papers)} papers, "
          f"{len(topic)} semantic-layer items "
          f"(deduped against {args.dedup_days} days, {len(seen)} URLs) -> {out}")


if __name__ == "__main__":
    main()
