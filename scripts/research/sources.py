"""Search providers for the research pipeline.

Specialised, keyless sources first — they beat generic web search on technical
topics (and generic search favours SEO farms over papers and primary sources):
arXiv, Hacker News (whose stories link to the web articles that mattered),
GitHub, Wikipedia and Semantic Scholar (rate-limited without a key). General web
search needs a key: TAVILY_API_KEY or EXA_API_KEY (both have free monthly tiers);
without one it is skipped and the run says so.

Every provider returns dicts: {url, title, snippet, provider, published}.
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")


def _get(url: str, headers: dict | None = None, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _post(url: str, body: dict, headers: dict, timeout: int = 60) -> dict:
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"User-Agent": UA, "Content-Type": "application/json", **headers})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def arxiv(query: str, n: int = 8) -> list[dict]:
    # Every term must appear (an exact phrase is too strict: most queries returned nothing).
    terms = [w for w in re.findall(r"[\w-]+", query) if len(w) > 2]
    q = urllib.parse.quote(" AND ".join(f"all:{w}" for w in terms) or query)
    xml = _get(f"https://export.arxiv.org/api/query?search_query={q}&max_results={n}&sortBy=relevance")
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in ET.fromstring(xml).findall("a:entry", ns):
        url = e.findtext("a:id", "", ns).replace("http://", "https://")
        out.append({"url": re.sub(r"v\d+$", "", url), "title": " ".join(e.findtext("a:title", "", ns).split()),
                    "snippet": " ".join(e.findtext("a:summary", "", ns).split())[:500],
                    "provider": "arxiv", "published": e.findtext("a:published", "", ns)[:10]})
    return out


def hackernews(query: str, n: int = 10) -> list[dict]:
    data = json.loads(_get("https://hn.algolia.com/api/v1/search?" + urllib.parse.urlencode(
        {"query": query, "tags": "story", "hitsPerPage": n})))
    out = []
    for h in data.get("hits", []):
        if h.get("url"):   # the linked article is the source; the HN thread is context
            out.append({"url": h["url"], "title": h.get("title", ""),
                        "snippet": f"{h.get('points', 0)} points, {h.get('num_comments', 0)} comments on Hacker News",
                        "provider": "hn", "published": (h.get("created_at") or "")[:10],
                        "discussion": f"https://news.ycombinator.com/item?id={h['objectID']}"})
    return out


def github(query: str, n: int = 6) -> list[dict]:
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    data = json.loads(_get("https://api.github.com/search/repositories?" + urllib.parse.urlencode(
        {"q": query, "sort": "stars", "per_page": n}), headers))
    return [{"url": r["html_url"], "title": r["full_name"], "snippet": (r.get("description") or "")[:300]
             + f" ({r['stargazers_count']} stars)", "provider": "github", "published": r.get("pushed_at", "")[:10]}
            for r in data.get("items", [])]


def wikipedia(query: str, n: int = 3) -> list[dict]:
    data = json.loads(_get("https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "list": "search", "srsearch": query, "format": "json", "srlimit": n})))
    return [{"url": "https://en.wikipedia.org/wiki/" + urllib.parse.quote(s["title"].replace(" ", "_")),
             "title": s["title"], "snippet": re.sub(r"<[^>]+>", "", s.get("snippet", "")),
             "provider": "wikipedia", "published": s.get("timestamp", "")[:10]}
            for s in data.get("query", {}).get("search", [])]


def semantic_scholar(query: str, n: int = 6) -> list[dict]:
    headers = {"x-api-key": os.environ["S2_API_KEY"]} if os.environ.get("S2_API_KEY") else {}
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(
        {"query": query, "limit": n, "fields": "title,year,url,abstract,externalIds,citationCount"})
    for wait in (0, 4, 10):   # keyless is rate-limited: back off, then give up quietly
        time.sleep(wait)
        try:
            data = json.loads(_get(url, headers))
            break
        except Exception:
            data = {}
    out = []
    for p in data.get("data", []):
        arx = (p.get("externalIds") or {}).get("ArXiv")
        out.append({"url": f"https://arxiv.org/abs/{arx}" if arx else p.get("url"), "title": p.get("title", ""),
                    "snippet": (p.get("abstract") or "")[:500] + f" ({p.get('citationCount', 0)} citations)",
                    "provider": "semantic_scholar", "published": str(p.get("year") or "")})
    return out


def web(query: str, n: int = 8) -> list[dict]:
    """General web search, when a key is configured."""
    if os.environ.get("TAVILY_API_KEY"):
        data = _post("https://api.tavily.com/search", {"query": query, "max_results": n, "search_depth": "basic"},
                     {"Authorization": f"Bearer {os.environ['TAVILY_API_KEY']}"})
        return [{"url": r["url"], "title": r.get("title", ""), "snippet": r.get("content", "")[:500],
                 "provider": "tavily", "published": r.get("published_date", "")} for r in data.get("results", [])]
    if os.environ.get("EXA_API_KEY"):
        data = _post("https://api.exa.ai/search", {"query": query, "numResults": n, "contents": {"text": {"maxCharacters": 500}}},
                     {"x-api-key": os.environ["EXA_API_KEY"]})
        return [{"url": r["url"], "title": r.get("title", ""), "snippet": (r.get("text") or "")[:500],
                 "provider": "exa", "published": (r.get("publishedDate") or "")[:10]} for r in data.get("results", [])]
    return []


PROVIDERS = {"arxiv": arxiv, "hn": hackernews, "github": github, "wikipedia": wikipedia,
             "semantic_scholar": semantic_scholar, "web": web}


def has_web() -> bool:
    return bool(os.environ.get("TAVILY_API_KEY") or os.environ.get("EXA_API_KEY"))


def read_page(url: str) -> str:
    """Page text as markdown via Jina Reader (keyless works at ~20 requests/minute)."""
    # Jina answers 403 to Python requests that claim to be a browser; an honest UA works.
    headers = {"User-Agent": "ai-reports-research/1.0 (+https://luisgonzalezbernal.com/reports/)",
               "X-Return-Format": "markdown"}
    if os.environ.get("JINA_API_KEY"):
        headers["Authorization"] = f"Bearer {os.environ['JINA_API_KEY']}"
    return _get("https://r.jina.ai/" + url, headers, timeout=60).decode("utf-8", "replace")
