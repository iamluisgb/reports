# AGENTS.md — guidance for the Hermes Agent

This repo is a **GitHub Pages static site**. It has no build step for the agent to run
and no server. The agent's job is to publish report HTML files; everything else is
generated automatically by CI.

## Who writes what

Since 13 Sep 2026 the daily report builds itself: `.github/workflows/daily.yml`
runs `collect.py` and `write_report.py`. It is the **only** producer of dailies.
The Hermes watchdog dispatches it at 07:00 UTC and reports the outcome on
Telegram; its own `schedule` is a backstop that GitHub starts hours late and that
skips when the day is already published.

**Never write a daily by hand.** On 23-24 Sep 2026 two hand-written dailies with
invented stories and `example.com` links reached production. If the workflow
fails, re-dispatch it (`gh workflow run daily.yml -f day=YYYY-MM-DD`); for a past
day, use `scripts/backfill/` (real archival sources, `verify_report.py`). Hand
authoring is for **special** reports only.

Every daily must pass `python3 scripts/check_report.py reports/ai-news-<day>.html`
(placeholders, placeholder links, missing Hacker News item links). `daily.yml`
runs it before committing and `build.yml` runs it on every pushed daily.

Before rebuilding a day, delete `reports/ai-news-<day>.html` (and its `audio/`
files); the workflow refuses to overwrite, and so should you.

## Publishing a report

1. Write the report as a self-contained HTML file in `reports/`:
   - **Daily:** `reports/ai-news-YYYY-MM-DD.html` (filename prefix `ai-news-` is what
     marks it as daily).
   - **Special:** `reports/<descriptive-slug>.html` (any other name).
2. Each report must include:
   - `<link rel="stylesheet" href="../styles.css">` (shared theme).
   - A real `<title>` — it becomes the card title on the homepage and the RSS title.
   - A `<div class="subtitle">…</div>` (and for specials, a `<div class="date-line">DD Mon YYYY</div>`)
     — the subtitle becomes the card/RSS summary **and** the social share description.
3. Commit and push to `master`. **Do not** hand-edit `reports.json`, `sitemap.xml`,
   `rss.xml`, the `og/` images, or the `<!-- og:start -->…<!-- og:end -->` and
   `<!-- ui:start -->…<!-- ui:end -->` blocks in each report; CI regenerates them all on push.
   Don't add font links or page chrome (progress bar, prev/next) to a report yourself:
   the ui block brings the fonts, `report.css` and `report.js`, which add them to every page.

## Audio briefing

Each daily report carries a spoken briefing: `audio/ai-news-YYYY-MM-DD.mp3`, plus the
script it was read from in `audio/ai-news-YYYY-MM-DD.txt` (versioned, so what was said
can be audited without listening).

Write the script — one segment per paragraph, opened by its voice — then run:

```bash
python3 scripts/make_audio.py YYYY-MM-DD        # reads audio/ai-news-YYYY-MM-DD.txt
python3 scripts/make_audio.py YYYY-MM-DD --check
```

It synthesises each segment with Kokoro (`FENRIR` → `am_fenrir`, `SARAH` → `af_sarah`),
concatenates them, and injects the "Audio Briefing" section and its player JS into the
report with the real duration, and writes `audio/ai-news-YYYY-MM-DD.json` with the
loudness envelope the waveform player draws. Idempotent: re-running replaces, never stacks.
`--peaks` rewrites only that JSON for an existing mp3 (no API key needed).

Needs `NAN_API_KEY` and `ffmpeg`/`ffprobe`. Kokoro is capped at 15 requests/minute, so
never run two days at once.

## Social cards (Open Graph / Twitter)

`scripts/build_social.py` runs in CI and makes every report shareable:
- generates a branded 1200×630 PNG per report under `og/` (fonts bundled in
  `assets/fonts/`, OFL), plus `og/og-default.png` as fallback;
- injects an idempotent `<!-- og:start -->…<!-- og:end -->` block into each
  report's `<head>` (og:*, twitter:summary_large_image, description, canonical),
  with the title/date/summary derived from the same logic as the manifest;
- injects an idempotent `<!-- ui:start -->…<!-- ui:end -->` block (site fonts,
  `report.css`, `report.js`) so every report, old or new, gets the current design.

There is nothing to do by hand — the `<title>` and `subtitle` you write feed the
cards automatically. To preview locally: `pip install Pillow && python3
scripts/build_social.py` (idempotent; re-runs are a no-op).

## Rules

- Never edit the generated files (`reports.json`, `sitemap.xml`, `rss.xml`, `og/*.png`,
  the og and ui blocks) by hand.
- Report styling lives in `styles.css` (tokens, base components) and `report.css`
  (current design layer); the index has its own `home.css`. Restyle there, not inside
  report files.
- Keep all links root-relative (`/reports/…`) or relative so they work on both the
  custom domain and `iamluisgb.github.io`.
- Canonical domain is `https://luisgonzalezbernal.com/reports/`.
- If you change metadata extraction, edit `scripts/generate_manifest.py` and run it
  locally (`python3 scripts/generate_manifest.py`) before pushing.
