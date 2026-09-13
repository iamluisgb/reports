#!/usr/bin/env python3
"""Turn a candidate bundle into the day's report and its briefing script.

Three calls to NaN's OpenAI-compatible chat API — news, then papers plus the
closing argument, then the spoken script. The model never writes HTML and never
writes a URL: it returns JSON that *selects* candidates by the id collect.py
assigned them and supplies the prose, and this script renders the page from a
fixed template with the URLs it already verified. A hallucinated link is
therefore not expressible.

Why three calls and not one: these are reasoning models with a hard 16k
completion cap, and they spend five to eight tokens thinking for every token
they write. A whole report in one call reasons its way past the cap and returns
truncated JSON. Each call here writes about a thousand tokens, which fits.

  write_report.py --bundle /tmp/candidates-2026-09-13.json

Needs NAN_API_KEY. Writes reports/ai-news-<day>.html and, unless
--skip-audio-script, audio/ai-news-<day>.txt for make_audio.py to synthesise.
"""
import argparse
import html as htmllib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = os.environ.get("NAN_BASE_URL", "https://api.nan.builders/v1") + "/chat/completions"
# glm5.3-flash is the strongest model on the NaN subscription and worth the
# wait in a cron job; deepseek-v4-flash is competent and three times faster.
MODELS = os.environ.get("NAN_MODELS", "glm5.3-flash,deepseek-v4-flash").split(",")
# Both are reasoning models that spend most of their budget thinking. A budget
# that looks generous for the prose alone returns 200 OK with an EMPTY string —
# the tokens go to reasoning and the answer never starts. 16384 is their hard
# ceiling and asking for more is silently clamped, so the only real lever is
# keeping each call's job small, and complete() treats a short answer as a
# failure rather than publishing it.
CALL_TOKENS = 16000
MIN_REPORT_CHARS = 1200
MIN_AUDIO_WORDS = 700          # ~160 wpm, comfortably over make_audio's 180s floor
# More than this and the prompt is mostly noise the model has to wade through.
# Two orderings, unioned: points finds what the day voted for, rank finds what
# it is voting for right now. Points alone buried the RubyGems attribution — the
# day's actual lead — at 5 points and rank 39 because it was three hours old.
TOP_BY_POINTS = 28
TOP_BY_RANK = 24
MAX_PAPERS = 9
MAX_ABSTRACT = 900
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

VOICE = """You write "AI News Daily", a terse, high-signal briefing read by a senior \
engineer who builds with LLMs. Declarative, specific, no hype, no filler adjectives, \
no "in today's fast-moving landscape", no "it's worth noting". Numbers earn their \
place. Never pad. British-leaning English, em dashes over semicolons."""

PAPERS_LABEL = "Papers — ArXiv CS.AI"
NEWS_SECTIONS = ["Headlines", "AI / LLM / Agents", "Infra / SRE / DevOps", "Hacker News"]

NEWS_PROMPT = """{voice}

Below are today's Hacker News candidates ({day}, {weekday}). Choose the ones worth \
publishing and write them up. Return ONLY a JSON object, no markdown fence, no \
commentary:

{{
  "subtitle": "4 clauses joined by ' · ', naming the day's actual stories",
  "sections": [
    {{"label": "Headlines", "items": [{{"id": "hn-123", "title": "...", "desc": "..."}}]}}
  ]
}}

Rules:
- Section labels, in this order, omitting any you have nothing good for: {sections}.
- This is an AI briefing. "Headlines" is the 4-6 stories that mattered TO THAT \
READER — AI, then the systems and security news a senior engineer would act on. \
Sport, consumer gadgets, history and curiosities go in "Hacker News" or nowhere, \
however many points they have.
- A low score is not a low ranking: a story near the top of the front page with few \
points is hours old and may well be the day's lead. Judge by what happened, not by \
the vote count.
- "AI / LLM / Agents" takes another 4-6, "Infra / SRE / DevOps" and "Hacker News" \
3-5 each. Use each id once, and never run two items about the same event.
- "id" MUST be copied exactly from a candidate below. Never invent one.
- "title" is yours to rewrite — sharper than the source headline, sentence case.
- "desc" is 1-3 sentences: what the thing IS, and the number when the number is the \
story. Cite points or comments only then.
- Skip anything you cannot describe from the material given. A thin day is fine; \
an invented detail is not.

CANDIDATES (rank = position on the front page, lower is hotter):
{candidates}"""

PAPERS_PROMPT = """{voice}

Two jobs: write up today's arXiv papers, and write the closing argument for the \
whole report. Return ONLY a JSON object, no markdown fence, no commentary:

{{
  "papers": [{{"id": "arxiv-2609.11318", "title": "...", "desc": "..."}}],
  "why_it_matters": ["bullet", "bullet", "bullet"]
}}

Rules:
- Choose 4-6 papers. "id" MUST be copied exactly. "title" may keep the paper's own \
name; drop a subtitle that adds nothing.
- "desc" is 2-4 sentences: lead with the problem the paper attacks, then the result \
with its actual numbers, and end with **[three, lowercase, comma-separated tags]** \
in double asterisks.
- "why_it_matters": exactly 3 bullets, 2-4 sentences each, covering the news and the \
papers together. Find the through-line; do not summarise item by item. This is the \
part a reader cannot get from the headlines, so it is where the judgement goes. It \
may disagree with the sources.

TODAY'S NEWS, already written up:
{news}

PAPER CANDIDATES:
{candidates}"""

AUDIO_PROMPT = """{voice}

Write the spoken briefing script for this report — a two-host dialogue, HOST_A and \
HOST_B. Return ONLY the script, no preamble.

Format: one segment per paragraph, each opened by its speaker tag on the same line:

    [HOST_A] AI News Daily, {weekday} the ... of ..., twenty twenty-six. ...

    [HOST_B] ...

Rules:
- HOST_A reports: what happened, the numbers, the names. HOST_B interprets: why it \
matters, what to watch, where to disagree. Alternate; never let one run twice.
- Open with the date and the day's lead story. Close by pointing at the written report.
- It is read aloud by a TTS model: spell numbers as words ("thirty-eight point eight \
percent", "twenty twenty-six"), expand acronyms it would garble (S W E, N L D O), \
and never use a bullet, a heading, a URL or a bracket.
- 900-1300 words, 12-18 segments. Under 700 words the audio is rejected.
- Cover the headlines and the papers properly; sweep the rest in one segment.

REPORT:
{report}"""


def post(payload, key, timeout=240):
    """A working glm5.3-flash call lands in ~70s; past four minutes it is hung,
    and waiting is worse than moving to the next model."""
    body = json.dumps(payload).encode()
    req = urllib.request.Request(API, data=body, method="POST", headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        # NaN's edge answers 403/1010 to non-browser user agents, and urllib
        # announces itself as Python-urllib by default.
        "User-Agent": UA,
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def complete(prompt, key, label, tries=2):
    """Ask each model in turn until one returns something substantial.

    Two things go wrong in practice and both are survivable by moving on: the
    edge answers 524 when a model thinks for longer than it will wait, and a
    model that spends its whole budget reasoning returns 200 OK with an empty
    string. NaN also rejects concurrent calls on one key, so this is serial by
    construction, not by accident.
    """
    for model in MODELS:
        for attempt in range(tries):
            started = time.time()
            try:
                data = post({"model": model, "temperature": 0.6,
                             "max_tokens": CALL_TOKENS,
                             "messages": [{"role": "user", "content": prompt}]}, key)
            except Exception as exc:
                detail = getattr(exc, "read", lambda: b"")()[:160].decode("utf-8", "replace")
                print(f"  ! {label}: {model} failed ({exc}) {detail}", file=sys.stderr)
                time.sleep(5)
                continue
            text = (data["choices"][0]["message"].get("content") or "").strip()
            usage = data.get("usage", {})
            reasoning = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0)
            print(f"  {label}: {model} {time.time() - started:.0f}s "
                  f"{usage.get('completion_tokens', 0)} tok ({reasoning} reasoning) "
                  f"-> {len(text)} chars", file=sys.stderr)
            if len(text) >= 400:
                return text, model
            print(f"  ! {label}: {model} returned {len(text)} chars — "
                  f"budget went to reasoning", file=sys.stderr)
    raise SystemExit(f"{label}: every model failed or returned nothing")


def parse_json(text):
    """Pull the JSON object out of a reply that may be fenced or chatty."""
    text = re.sub(r"^\s*```(?:json)?\s*|\s*```\s*$", "", text.strip())
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    depth, start = 0, None
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                try:
                    return json.loads(text[start:i + 1])
                except json.JSONDecodeError:
                    start = None
    raise SystemExit("model did not return parseable JSON")


def esc(text):
    """Escape everything, then re-enable the one bit of markup the prose uses."""
    out = htmllib.escape(str(text), quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)


def render(day, chosen, subtitle, why, index):
    stamp = datetime.strptime(day, "%Y-%m-%d")
    pretty = f"{stamp.day} {stamp.strftime('%b %Y')}"
    parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI News Daily — {pretty}</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
</head>
<body>
  <div class="page">
    <a class="back-link" href="../index.html">← Index</a>
    <div class="header" style="position:relative;">
      <div class="field-mark"></div>

      <div class="header-top">
        <div>
          <div class="category">AI NEWS DAILY</div>
          <h1>The <em>AI</em> Briefing</h1>
          <div class="date-line">{pretty} · {stamp.strftime('%A').upper()}</div>
          <div class="subtitle">{esc(subtitle)}</div>
        </div>
        <button class="theme-toggle" onclick="toggleTheme()">◐ DARK</button>
      </div>
    </div>
"""]

    for section in chosen:
        parts.append('\n    <div class="section">\n'
                     f'      <div class="section-label">{esc(section["label"])}</div>\n')
        for n, item in enumerate(section["items"], 1):
            source = index[item["id"]]
            if item["id"].startswith("arxiv-"):
                links = f'          <a href="{source["url"]}">arXiv</a>\n'
            else:
                links = (f'          <a href="{source["url"]}">Original</a>\n'
                         f'          <a href="{source["hn_url"]}">HN</a>\n')
            parts.append(f"""
      <div class="news-item">
        <div class="num">{n:02d}</div>
        <div class="title">{esc(item["title"])}</div>
        <div class="desc">{esc(item["desc"])}</div>
        <div class="sources">
{links}        </div>
      </div>
""")
        parts.append("\n    </div>\n")

    parts.append('\n    <div class="section">\n'
                 '      <div class="section-label">Why It Matters</div>\n')
    for bullet in why:
        parts.append(f"""
      <div class="follow-item">
        <span class="bullet">▸</span>
        <span>{esc(bullet)}</span>
      </div>
""")
    parts.append(f"""
    </div>

    <div class="footer">
      <span class="handle">@iamluisgb</span>
      <span class="date">{pretty}</span>
    </div>
  </div>

<script>
  function toggleTheme() {{
    const html = document.documentElement;
    const current = html.getAttribute('data-theme');
    const next = current === 'light' ? 'dark' : 'light';
    const btn = document.querySelector('.theme-toggle');
    if (next === 'light') {{
      html.setAttribute('data-theme', 'light');
      btn.textContent = '◑ LIGHT';
    }} else {{
      html.removeAttribute('data-theme');
      btn.textContent = '◐ DARK';
    }}
    localStorage.setItem('ai-reports-theme', next);
  }}

  (function() {{
    const saved = localStorage.getItem('ai-reports-theme');
    if (saved) {{
      const html = document.documentElement;
      const btn = document.querySelector('.theme-toggle');
      if (saved === 'light') {{
        html.setAttribute('data-theme', 'light');
        btn.textContent = '◑ LIGHT';
      }}
    }}
  }})();
</script>
</body>
</html>
""")
    return "".join(parts)


def keep_valid(items, index, used, label, want_paper):
    """Keep only what the model was actually given, and say what it lost."""
    kept = []
    for item in items:
        key = str(item.get("id", "")).strip()
        if key not in index:
            print(f"  - dropped unknown id {key!r} in {label}", file=sys.stderr)
            continue
        if key in used:
            print(f"  - dropped duplicate id {key} in {label}", file=sys.stderr)
            continue
        if not item.get("title") or not item.get("desc"):
            print(f"  - dropped {key}: missing title or desc", file=sys.stderr)
            continue
        if key.startswith("arxiv-") != want_paper:
            print(f"  - dropped {key}: wrong section ({label})", file=sys.stderr)
            continue
        used.add(key)
        kept.append(item)
    return kept


def check_audio(script):
    words = len(re.sub(r"\[\w+\]", " ", script).split())
    speakers = set(re.findall(r"\[(\w+)\]", script))
    if words < MIN_AUDIO_WORDS:
        return f"only {words} words (need {MIN_AUDIO_WORDS})"
    if not {"HOST_A", "HOST_B"} <= speakers:
        return f"speakers were {sorted(speakers) or 'none'}, need HOST_A and HOST_B"
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--skip-audio-script", action="store_true")
    ap.add_argument("--dry-run", action="store_true",
                    help="write to /tmp instead of the repo")
    args = ap.parse_args()

    key = os.environ.get("NAN_API_KEY", "").strip()
    if not key:
        raise SystemExit("NAN_API_KEY not set")

    bundle = json.loads(Path(args.bundle).read_text(encoding="utf-8"))
    day = bundle["day"]
    by_points = sorted(bundle["stories"], key=lambda s: -s["points"])[:TOP_BY_POINTS]
    by_rank = sorted(bundle["stories"], key=lambda s: s["rank"])[:TOP_BY_RANK]
    stories = list({s["id"]: s for s in by_points + by_rank}.values())
    stories.sort(key=lambda s: s["rank"])
    papers = bundle["papers"][:MAX_PAPERS]
    index = {c["id"]: c for c in stories + papers}
    used = set()

    # --- news -------------------------------------------------------------
    listing = "\n".join(
        f'{s["id"]} | rank {s["rank"]} | {s["points"]}pts {s["comments"]}c | '
        f'{s["title"]} | {s["url"]}' for s in stories)
    raw, model = complete(NEWS_PROMPT.format(
        voice=VOICE, day=day, weekday=bundle["weekday"],
        sections=", ".join(NEWS_SECTIONS), candidates=listing), key, "news")
    reply = parse_json(raw)
    subtitle = str(reply.get("subtitle", "")).strip() or "The day in AI"

    chosen = []
    for section in reply.get("sections", []):
        label = str(section.get("label", "")).strip()
        items = keep_valid(section.get("items", []), index, used, label, want_paper=False)
        if items:
            chosen.append({"label": label, "items": items})
    if sum(len(s["items"]) for s in chosen) < 6:
        raise SystemExit("fewer than 6 usable news items — refusing to publish a stub")

    # --- papers and the closing argument ----------------------------------
    summary = "\n".join(f'- {i["title"]}: {i["desc"]}'
                        for s in chosen for i in s["items"])
    candidates = "\n".join(f'{p["id"]} | {p["title"]}\n  {p["abstract"][:MAX_ABSTRACT]}'
                           for p in papers)
    why = []
    if papers:
        raw, model = complete(PAPERS_PROMPT.format(
            voice=VOICE, news=summary, candidates=candidates), key, "papers")
        reply = parse_json(raw)
        items = keep_valid(reply.get("papers", []), index, used,
                           PAPERS_LABEL, want_paper=True)
        if items:
            # The papers sit after Headlines and the AI section, before infra.
            at = min(2, len(chosen))
            chosen.insert(at, {"label": PAPERS_LABEL, "items": items})
        why = [str(b).strip() for b in reply.get("why_it_matters", []) if str(b).strip()]
    if len(why) < 2:
        raise SystemExit("Why It Matters came back with fewer than 2 bullets")

    page = render(day, chosen, subtitle, why, index)
    if len(page) < MIN_REPORT_CHARS:
        raise SystemExit(f"rendered page is only {len(page)} chars — not publishing")

    out = (Path(f"/tmp/ai-news-{day}.html") if args.dry_run
           else ROOT / "reports" / f"ai-news-{day}.html")
    out.write_text(page, encoding="utf-8")
    counts = ", ".join(f'{s["label"]}: {len(s["items"])}' for s in chosen)
    print(f"{day}: {out} ({len(page) // 1024} KB, {model}) — {counts}")

    if args.skip_audio_script:
        return

    text = re.sub(r"<[^>]+>", " ", page)
    text = re.sub(r"\s+", " ", text)
    script, model = complete(
        AUDIO_PROMPT.format(voice=VOICE, weekday=bundle["weekday"], report=text),
        key, "audio")
    script = re.sub(r"^\s*```\w*\s*|\s*```\s*$", "", script.strip())
    problem = check_audio(script)
    if problem:
        # The report is already on disk and publishable; the briefing is not
        # worth failing the whole run over.
        print(f"  ! audio script rejected: {problem} — report still stands", file=sys.stderr)
        return
    script_path = (Path(f"/tmp/ai-news-{day}.txt") if args.dry_run
                   else ROOT / "audio" / f"ai-news-{day}.txt")
    script_path.parent.mkdir(exist_ok=True)
    script_path.write_text(script + "\n", encoding="utf-8")
    print(f"{day}: {script_path} ({len(script.split())} words, {model})")


if __name__ == "__main__":
    main()
