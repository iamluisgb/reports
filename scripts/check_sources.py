#!/usr/bin/env python3
"""Check the sources of special reports: enough of them, and every link real.

    python3 scripts/check_sources.py reports/<special>.html [...]   # these specials
    python3 scripts/check_sources.py --all                          # every special
    python3 scripts/check_sources.py --offline reports/x.html       # count only, no network

Rules (AGENTS.md → Special-report kit):
- at least MIN_SOURCES distinct external sources (the numbered Sources list when
  there is one, otherwise every external link in the body);
- every source URL resolves. When one does not (404/410, DNS, connection error),
  the Wayback Machine decides: archived means the page existed and died (link rot,
  a warning); never archived means it may never have existed — a fabricated
  citation, which fails the check. Sites that refuse bots (401/403/429, 5xx) count
  as alive: they answered.

The Wayback test follows "Detecting and Correcting Reference Hallucinations in
Commercial LLMs and Deep Research Agents" (arXiv 2604.03173), where it separated
dead links from invented ones. Dailies are not checked here: check_report.py
covers them.
"""
from __future__ import annotations

import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_SOURCES = 10
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")
TIMEOUT = 15
SKIP_HOSTS = {"luisgonzalezbernal.com", "iamluisgb.github.io", "twitter.com", "x.com",
              "www.linkedin.com", "linkedin.com"}   # own site; social sites block bots outright

errors: list[str] = []
warnings: list[str] = []


def sources_of(text: str) -> tuple[list[str], str]:
    """External URLs from the numbered Sources list, or from the whole body."""
    body = text[text.find("<body"):]
    m = re.search(r'<div class="section-label">\s*Sources\s*</div>.*?<ol>(.*?)</ol>', body, re.S)
    scope, where = (m.group(1), "Sources list") if m else (body, "body links")
    urls = []
    for u in re.findall(r'href="(https?://[^"#]+)', scope):
        u = html.unescape(u).rstrip("/")
        host = urllib.parse.urlparse(u).netloc.lower()
        if host and host not in SKIP_HOSTS and u not in urls:
            urls.append(u)
    return urls, where


def fetch(url: str, method: str = "HEAD") -> int | str:
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except urllib.error.URLError as e:
        # A name that does not resolve is a strong sign of an invented domain;
        # timeouts and refused connections only mean we could not verify.
        return "dns" if "Name or service not known" in str(e.reason) or "nodename nor servname" in str(e.reason) \
            or "getaddrinfo" in str(e.reason) else "unreachable"
    except Exception:
        return "unreachable"


def archived(url: str) -> bool:
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    try:
        req = urllib.request.Request(api, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            data = json.load(r)
        return bool(data.get("archived_snapshots", {}).get("closest", {}).get("available"))
    except Exception:
        return True   # Wayback unreachable: don't accuse a source of being invented


def status(url: str) -> tuple[str, str]:
    code = fetch(url)
    if code in (405, 400, 501) or isinstance(code, str):   # some servers refuse HEAD
        code = fetch(url, "GET")
    if isinstance(code, int) and (code < 400 or code in (401, 403, 429) or code >= 500):
        return "ok", str(code)
    if code == "unreachable":
        return "unverified", "timeout/connection"
    # 404/410 or an unknown domain: archived means it existed once.
    return ("dead" if archived(url) else "fabricated?"), str(code)


def check(path: Path, offline: bool) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    urls, where = sources_of(text)
    if len(urls) < MIN_SOURCES:
        errors.append(f"{path.name}: {len(urls)} distinct sources in the {where} (minimum {MIN_SOURCES})")
    if offline or not urls:
        return
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(status, urls))
    for url, (state, code) in zip(urls, results):
        if state == "unverified":
            warnings.append(f"{path.name}: could not verify ({code}): {url}")
        elif state == "dead":
            warnings.append(f"{path.name}: dead link, archived by Wayback ({code}): {url}")
        elif state == "fabricated?":
            errors.append(f"{path.name}: link does not resolve ({code}) and was never archived — verify or remove: {url}")


def main(args: list[str]) -> int:
    offline = "--offline" in args
    args = [a for a in args if not a.startswith("--")] if "--all" not in sys.argv else [
        str(p) for p in sorted((ROOT / "reports").glob("*.html")) if not p.name.startswith("ai-news-")]
    specials = [Path(a) for a in args if Path(a).is_file() and not Path(a).name.startswith("ai-news-")]
    for p in specials:
        check(p, offline)
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"::error::{e}" if "GITHUB_ACTIONS" in __import__("os").environ else f"error: {e}")
    print(f"sources check: {len(errors)} error(s), {len(warnings)} warning(s), {len(specials)} special report(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
