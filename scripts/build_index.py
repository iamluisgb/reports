#!/usr/bin/env python3
"""Render the index page's content into index.html at build time.

The index used to arrive empty and draw itself from reports.json, which pushed
the whole page down as it loaded (CLS 0.81) and showed crawlers and agents an
empty page. Now the HTML is written here, between the index markers, and the
page's script only filters what is already there.

Called by generate_manifest.py, so every workflow that rebuilds the manifest
also rebuilds the index. Idempotent.
"""
from __future__ import annotations

import html
import json
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
START, END = "<!-- index:start -->", "<!-- index:end -->"

UBIQ = {"models", "agents", "research"}   # on >90% of reports: they don't discriminate
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTHS_LONG = ["January", "February", "March", "April", "May", "June", "July", "August",
               "September", "October", "November", "December"]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
SPECIALS_SHOWN = 6

esc = lambda s: html.escape(str(s), quote=True)
day = lambda s: date.fromisoformat(s)
fmt = lambda s: f"{day(s).day} {MONTHS[day(s).month - 1]} {day(s).year}"
topic_label = lambda t: t.replace("-", " ").capitalize()
spanish = lambda s: bool(re.search(r"[áéíóúñ¿¡]|\b(los|las|del)\b", s, re.I))
broken = lambda r: not r["summary"] or re.search(r"\{\w+\}", r["summary"])
href = lambda r: "reports/" + r["file"]
vt_name = lambda r: "r-" + re.sub(r"[^a-z0-9-]", "-", r["file"][:-5], flags=re.I)


def headline(r: dict) -> str:
    """A daily is titled by its first story; a special by its own title."""
    if r["type"] == "daily":
        return "AI News Daily" if broken(r) else r["summary"].split(" · ")[0]
    return " ".join(r["title"].split())


def tags_attr(r: dict) -> str:
    return esc(" ".join(r["tags"]))


def audio_length(stem: str) -> str:
    peaks = ROOT / "audio" / f"{stem}.json"
    try:
        secs = json.loads(peaks.read_text())["duration"]
        return f"0:00 / {int(secs // 60)}:{int(secs % 60):02d}"
    except (OSError, KeyError, ValueError):
        return ""


def masthead(reports: list[dict], daily: list[dict]) -> str:
    updated = f" · updated {day(daily[0]['date']).day} {MONTHS[day(daily[0]['date']).month - 1]}" if daily else ""
    counts: dict[str, int] = {}
    for r in reports:
        for t in r["tags"]:
            if t not in UBIQ:
                counts[t] = counts.get(t, 0) + 1
    chips = "".join(
        f'<button class="chip" type="button" data-t="{esc(t)}" aria-pressed="false">{esc(topic_label(t))}<span>{n}</span></button>'
        for t, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
    return f"""
    <header class="mast" id="mast">
      <div>
        <div class="eyebrow"><b>AI Research Briefing</b> · {len(reports)} reports{updated}</div>
        <h1>AI <em>Reports</em></h1>
      </div>
      <div class="tools">
        <button class="btn btn-search" type="button" data-search>Search reports <span class="kbd">⌘K</span></button>
        <a class="btn hide-sm" href="/reports/about.html">About</a>
        <a class="btn hide-sm" href="/reports/rss.xml">RSS</a>
        <button class="btn" type="button" data-theme-toggle aria-label="Switch theme">◐</button>
      </div>
    </header>
    <div class="topics" id="topics" role="group" aria-label="Filter by topic"><span class="eyebrow">Topics</span>{chips}<button class="link" type="button" id="clear" hidden>Clear</button></div>
    <div class="status" id="status" role="status" aria-live="polite"></div>
"""


def today(daily: list[dict]) -> str:
    if not daily:
        return ""
    t = daily[0]
    d = day(t["date"])
    items = [] if broken(t) else t["summary"].split(" · ")
    stem = t["file"][:-5]
    player = ""
    if t.get("audio"):
        player = f"""
        <div class="audio-player">
          <audio preload="none" src="audio/{esc(stem)}.mp3"></audio>
          <button class="play-btn" type="button" aria-label="Play audio briefing">
            <svg class="icon-play" viewBox="0 0 16 16"><path d="M4 2l10 6-10 6V2z"/></svg>
            <svg class="icon-pause" viewBox="0 0 16 16"><path d="M3 2h3.5v12H3zM9.5 2H13v12H9.5z"/></svg>
          </button>
          <div class="player-body">
            <div class="player-meta"><span class="player-title">Audio briefing</span><span class="player-time">{audio_length(stem)}</span></div>
            <input type="range" min="0" max="100" value="0" step="0.1" aria-label="Seek">
          </div>
        </div>"""
    yday = ""
    if len(daily) > 1:
        y = daily[1]
        yday = f'\n        <div class="yday">Yesterday: <a href="{href(y)}" data-file="{esc(y["file"])}">{esc(headline(y))}</a></div>'
    lis = "".join(f"<li>{esc(s)}</li>" for s in items[1:])
    return f"""
    <section class="today" id="today" aria-label="Latest briefing">
      <div>
        <div class="eyebrow"><b>Latest</b> · {WEEKDAYS[d.weekday()]} {d.day} {MONTHS[d.month - 1]} · {t["readingTime"]} min read</div>
        <h2><a href="{href(t)}" data-file="{esc(t["file"])}">{esc(headline(t))}</a></h2>
        <ol>{lis}</ol>
      </div>
      <div class="side">{player}
        <a class="btn-primary" href="{href(t)}" data-file="{esc(t["file"])}">Read the briefing <span class="arrow">→</span></a>{yday}
      </div>
    </section>
"""


def calendar(daily: list[dict]) -> str:
    if len(daily) < 7:
        return ""
    by_date: dict[str, dict] = {}
    for r in daily:
        by_date.setdefault(r["date"], r)
    first, last = day(daily[-1]["date"]), day(daily[0]["date"])
    cur = first - timedelta(days=first.weekday())   # back to Monday
    cells = ['<span></span>'] + [f'<span class="wd">{w}</span>' for w in ("Mon", "", "Wed", "", "Fri", "", "")]
    missing, last_month = 0, -1
    while cur <= last:
        m = cur.month
        cells.append(f'<span class="ml">{MONTHS[m - 1] if m != last_month and cur.day <= 7 else ""}</span>')
        if cur.day <= 7:
            last_month = m
        for _ in range(7):
            k = cur.isoformat()
            r = by_date.get(k)
            if cur < first or cur > last:
                cells.append("<span></span>")
            elif not r:
                missing += 1
                cells.append(f'<span class="cell" title="{fmt(k)} · no briefing"></span>')
            else:
                lvl = 1 if r["readingTime"] <= 3 else 2 if r["readingTime"] <= 6 else 3 if r["readingTime"] <= 8 else 4
                cells.append(f'<a class="cell l{lvl}" href="{href(r)}" data-tags="{tags_attr(r)}" data-meta="{fmt(k)} · {r["readingTime"]} min" data-head="{esc(headline(r))}" aria-label="{fmt(k)}: {esc(headline(r))}"></a>')
            cur += timedelta(days=1)
    streak, d = 0, last
    while d.isoformat() in by_date:
        streak += 1
        d -= timedelta(days=1)
    avg = int(sum(r["readingTime"] for r in daily) / len(daily) + 0.5)
    longest = daily[0]
    for r in daily:
        if r["readingTime"] > longest["readingTime"]:
            longest = r
    covered = len(by_date)
    meta = f"{covered} days covered · {missing} missed" if missing else f"{covered} days · none missed"
    ld = day(longest["date"])
    return f"""
    <section class="sec" id="calendar">
      <div class="sec-head"><h3>Every day since {MONTHS_LONG[first.month - 1]}</h3><span class="eyebrow">{meta}</span></div>
      <div class="cal-wrap">
        <div class="cal-scroll"><div class="cal" id="cal">{"".join(cells)}</div></div>
        <div class="facts">
          <div class="fact"><div class="n">{streak}</div><div class="k">day streak</div></div>
          <div class="fact"><div class="n">{avg}<small> min</small></div><div class="k">average briefing</div></div>
          <a class="fact" href="{href(longest)}" data-file="{esc(longest["file"])}"><div class="n">{longest["readingTime"]}<small> min</small></div><div class="k">longest, {ld.day} {MONTHS[ld.month - 1]} <span class="arrow">→</span></div></a>
        </div>
      </div>
      <div class="cal-foot"><span>Darker means a longer briefing. Hover a day for its headline.</span>
        <span class="legend" aria-hidden="true">Short <i class="cell l1"></i><i class="cell l2"></i><i class="cell l3"></i><i class="cell l4"></i> Long</span></div>
    </section>
"""


def specials(special: list[dict]) -> str:
    cards = []
    for i, r in enumerate(special):
        extra = ' data-extra hidden' if i >= SPECIALS_SHOWN else ''
        lang = '<span class="lang" title="In Spanish">ES</span>' if spanish(r["title"]) else ''
        cards.append(f"""
      <a class="sp" href="{href(r)}" data-file="{esc(r["file"])}" data-vt="{vt_name(r)}" data-tags="{tags_attr(r)}" data-min="{r["readingTime"]}"{extra}>
        <div class="eyebrow"><b>{esc(r.get("series") or "Special report")}</b></div>
        <h4>{esc(headline(r))}{lang}</h4>
        <p>{esc(r["summary"])}</p>
        <div class="meta"><span>{fmt(r["date"])}</span><span>{r["readingTime"]} min <span class="arrow">→</span></span></div>
      </a>""")
    mins = [r["readingTime"] for r in special]
    meta = f"{len(special)} reports · {min(mins)}–{max(mins)} min reads" if special else ""
    more = f'Show all {len(special)} special reports'
    return f"""
    <section class="sec" id="special">
      <div class="sec-head"><h3>Special reports</h3><span class="eyebrow" id="sp-meta">{meta}</span></div>
      <div class="specials" id="specials">{"".join(cards)}
      </div>
      <div class="empty" id="sp-empty" hidden>No special reports on these topics yet.</div>
      <div style="padding-top:6px"><button class="link" id="sp-more" type="button"{"" if len(special) > SPECIALS_SHOWN else " hidden"} data-label="{more}">{more}</button></div>
    </section>
"""


def archive(daily: list[dict]) -> str:
    groups: list[tuple[str, list[dict]]] = []
    for r in daily:
        d = day(r["date"])
        name = f"{MONTHS_LONG[d.month - 1]} {d.year}"
        if not groups or groups[-1][0] != name:
            groups.append((name, []))
        groups[-1][1].append(r)
    out = []
    for name, items in groups:
        rows = []
        for r in items:
            d = day(r["date"])
            parts = ["AI News Daily"] if broken(r) else r["summary"].split(" · ")
            rest = f'<span class="rest"> · {esc(" · ".join(parts[1:]))}</span>' if len(parts) > 1 else ""
            lang = '<span class="lang" title="In Spanish">ES</span>' if spanish(r["summary"]) else ""
            tags = " · ".join([topic_label(t) for t in r["tags"] if t not in UBIQ][:2])
            latest = ' data-latest hidden' if r is daily[0] else ''
            rows.append(f"""
        <a class="row" href="{href(r)}" data-file="{esc(r["file"])}" data-vt="{vt_name(r)}" data-tags="{tags_attr(r)}"{latest}>
          <span class="d"><b>{d.day:02d}</b> {WEEKDAYS[d.weekday()][:3]}</span>
          <span class="t"><span class="lead">{esc(parts[0])}</span>{rest}{lang}</span>
          <span class="r">{f'<span class="tg">{esc(tags)}</span>' if tags else ''}<span>{r["readingTime"]} min</span></span>
        </a>""")
        shown = sum(1 for r in items if r is not daily[0])
        out.append(f"""
      <div class="month"{"" if shown else " hidden"}>
        <div class="month-h"><h5>{name}</h5><span class="eyebrow" data-count>{shown}</span></div>{"".join(rows)}
      </div>""")
    return f"""
    <section class="sec" id="archive" tabindex="-1">
      <div class="sec-head"><h3>Daily archive</h3><span class="eyebrow" id="ar-meta">{len(daily)} daily briefings</span></div>
      <div id="months">{"".join(out)}
      </div>
      <div class="empty" id="ar-empty" hidden>No daily briefings on these topics.</div>
    </section>
"""


def render(reports: list[dict]) -> str:
    # Newest first; same-day reports by file name (stable sort: name first, then date).
    reports = sorted(sorted(reports, key=lambda r: r["file"]), key=lambda r: r["date"], reverse=True)
    daily = [r for r in reports if r["type"] == "daily"]
    special = [r for r in reports if r["type"] == "special"]
    return masthead(reports, daily) + today(daily) + calendar(daily) + specials(special) + archive(daily)


def write(reports: list[dict]) -> bool:
    text = INDEX.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"index.html has no {START} … {END} markers")
    block = START + render(reports) + "    " + END
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, count=1, flags=re.S)
    if new != text:
        INDEX.write_text(new, encoding="utf-8")
        return True
    return False


if __name__ == "__main__":
    data = json.loads((ROOT / "reports.json").read_text(encoding="utf-8"))
    print("index.html", "updated" if write(data["reports"]) else "unchanged")
