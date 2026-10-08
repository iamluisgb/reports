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
   `rss.xml`, `sitemap.md`, `tokens.json`, the `.md` twins in `reports/`, the `og/` images,
   the index content between `<!-- index:start -->` and `<!-- index:end -->`, or the
   `<!-- og:start -->…<!-- og:end -->`, `<!-- ui:start -->…<!-- ui:end -->` and
   `<!-- pwa:start -->…<!-- pwa:end -->` blocks; CI regenerates them all on push.
   Don't add font links, scripts or page chrome (theme code, player code, progress bar,
   prev/next) to a report yourself: the ui block brings the fonts, `site.js`, `report.js`
   and `pwa.js`, which add them to every page. Follow **Design system** below for the markup.

## Audio briefing

Each daily report carries a spoken briefing: `audio/ai-news-YYYY-MM-DD.mp3`, plus the
script it was read from in `audio/ai-news-YYYY-MM-DD.txt` (versioned, so what was said
can be audited without listening).

The pipeline writes that script from the report. If it lands outside 700–860 words —
which is what left 6 Oct 2026 published without a briefing — `write_report.py` sends
the checker's own objection back to the model once, with a word target and the side of
the window that is dangerous, instead of dropping the audio (`AUDIO_ATTEMPTS`). Two
attempts, then the day goes out without a briefing, as before.

Write the script — one segment per paragraph, opened by its voice — then run:

```bash
python3 scripts/make_audio.py YYYY-MM-DD        # reads audio/ai-news-YYYY-MM-DD.txt
python3 scripts/make_audio.py YYYY-MM-DD --check
```

It synthesises each segment with Kokoro (`HOST_A` → `af_heart`, `HOST_B` → `af_bella`;
`FENRIR`/`SARAH` still work as aliases),
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
- injects an idempotent `<!-- ui:start -->…<!-- ui:end -->` block (site fonts, the
  early theme switch, `site.js`, `report.js`) so every report, old or new, gets the current design.

There is nothing to do by hand — the `<title>` and `subtitle` you write feed the
cards automatically. To preview locally: `pip install Pillow && python3
scripts/build_social.py` (idempotent; re-runs are a no-op).

## Installed web app (PWA)

The site installs to a phone or desktop home screen and keeps working offline. Four
source files carry it:

| File | Holds |
|---|---|
| `manifest.json` | Name, icons, `start_url`/`scope` `/reports/`, standalone display, shortcuts to today, the calendar and the specials. `.json`, not `.webmanifest`: Pages serves `.webmanifest` as `application/octet-stream`, which no browser parses. |
| `sw.js` | The cache policy. Served from the repo root, so its scope is `/reports/` without the `Service-Worker-Allowed` header Pages cannot send. |
| `pwa.js` | Registers the worker, raises the toast (a briefing you have not read, a new build, no connection), adds the audio "Keep" button, and keeps `theme-color` on the reader's theme rather than the system's. |
| `offline.html` | What an uncached page falls back to; it lists what *is* on the device. |

`scripts/build_social.py` injects the head block — manifest link, icons, `pwa.js` —
into `index.html`, `about.html` and every report, so a new report gets it without being
edited. `scripts/build_icons.py` draws `assets/icons/` from the Musgo tokens,
idempotent via a fingerprint in the PNG metadata, like the OG cards. Both run in
`build.yml` and `daily.yml`.

Documents and data are network-first on purpose: Pages pins everything to
`Cache-Control: max-age=600` and its headers cannot be changed, so a plain fetch can
answer from a ten-minute-old CDN entry. The worker revalidates against the ETag
instead, and only falls back to its cache when the network fails or takes longer than
4 s. The shell is precached on install, pages are cached as they are read, and audio
only when the reader presses **Keep**, capped at 45 MB, oldest evicted first.

Rules:

- Bump `VERSION` in `sw.js` when the cache policy changes — that is what retires the
  old caches. Do not bump it per deploy.
- Keep `MEDIA_CACHE` unversioned: a briefing the reader asked to keep is their own
  download, and it must survive an update. Only the LRU cap evicts it.
- Keep every path under `/reports/` so the worker's scope stays its own, and keep
  `pwa.js`/`sw.js` inside the byte budgets in `check_design.py`.
- iOS has no background sync, so freshness is checked on open and on
  `visibilitychange` — all a home-screen app gets there. Never promise more.

## Design system

The site is one design system. `patterns.html` (https://luisgonzalezbernal.com/reports/patterns.html)
renders every pattern with the real CSS; look there before writing markup.

### Principles

1. **Today first, the archive second.** The newest briefing gets the most room.
2. **Reads like a newspaper, works like a tool.** Serif and space for reading; mono and
   controls for finding, filtering and listening.
3. **Every figure has a source.** A number, a quote or a claim links to where it came from.
4. **One job, one pattern.** If a pattern already does the job, use it. Reports never ship
   their own `<style>`, `style="…"` colours or scripts.

### Where things live

| File | Holds |
|---|---|
| `styles.css` | Tokens, base, shared patterns, report patterns and the special-report kit. The only stylesheet a report loads. |
| `home.css` | Index-only layout (masthead, calendar, cards, archive rows, search palette). |
| `site.js` | Theme, audio player, shared helpers (`window.Site`). Every page loads it. |
| `report.js` | Top bar, reading progress, section index, mini audio control, prev/next. Reports only. |
| `patterns.html` | The living catalogue. Add a pattern here when you add it to the CSS. |
| `scripts/build_index.py` | Renders the index content into `index.html` at build time; the page's script only filters it. |
| `scripts/build_agent_files.py` | Writes a markdown twin of every report (`reports/<name>.md`), `sitemap.md` and `tokens.json`. |
| `scripts/check_design.py` | Token contrast (AA), byte budgets and the report rules below. Runs in CI on the reports a push touches. |
| `assets/fonts/web/` | The three faces, self-hosted (OFL, latin subset). No font CDN. |

### What we don't do

No shadows except on floating layers · no gradients or decorative strips · no side accent
bars · one brand colour · Geist at 400 and 500 only · no emoji in the interface, titles
included. The green marks the brand word, the subject of a title, live state (audio,
progress, calendar) and links — never decoration (table heads, list markers, numbers, code).

The theme follows the reader's system until they pick one; high contrast follows
`prefers-contrast: more`. Both come from tokens, so a pattern built on tokens gets them free.

### Colour

The palette is **Musgo** (October 2026): moss `--primary` on a green-tinted near-black, with a
light theme to match. It replaced GitHub's green. Change it only in the two token blocks at
the top of `styles.css`, run `check_design.py` (it checks AA contrast) and bump `CARD_DESIGN`
in `scripts/build_social.py` so the share images are redrawn.

### Names

Name a pattern by what it does, not how it looks or where its code lives
(`.pager`, not `.rb-pager` or `.green-box`). Legacy report markup keeps a few old names
(`.section-label`, `.category`, `.date-line`, `.special-category`, `.special-date`,
`.player-title`, `.stat-label`); in the CSS they are aliases of `.eyebrow`, not separate patterns.

### Tokens

Use the custom properties at the top of `styles.css`, never raw values:
colour (`--primary`, `--on-surface`, `--on-surface-variant`, `--muted`, `--border`, `--warn` …),
type (`--fs-2xs` 11 · `--fs-xs` 12 · `--fs-sm` 13 · `--fs-base` 15 · `--fs-md` 17 · `--fs-lg` 22 ·
`--fs-xl` 28 · `--fs-2xl` 36 · `--fs-3xl` 46, plus `--fs-display-sm`, `--fs-display`, `--fs-hero`),
shape (`--r-sm` inline bits, `--r-md` controls, `--r-lg` containers, `--r-pill`) and motion
(`--dur-fast`, `--dur-base`, `--dur-slow`, `--ease`).

### Titles

The green italic `<em>` in an `<h1>` marks the **subject** of the title: one per title, at
most three words, never a year, a number or a whole clause.
`Building <em>Agent Skills</em> in 2026` — not `Building Agent Skills in <em>2026</em>`.

### How special reports are produced

Specials are the long-form, sourced analysis — the part of the site that keeps value when
daily summaries are a free feature everywhere. Each one needs **original data or a
point of view, a signed "What I would do", and sources that check out**. The process:

1. **Plan** — `data/research/<slug>/plan.json`: title, thesis to test, audience, 4–6
   questions with search queries and providers (format in `scripts/research/run.py`).
2. **Research** — `python3 scripts/research/run.py data/research/<slug>/plan.json`
   (needs `NAN_API_KEY`; `TAVILY_API_KEY` or `EXA_API_KEY` adds general web search).
   It searches specialised sources first (arXiv, Hacker News, GitHub, Wikipedia,
   Semantic Scholar), reads each page, and has a NaN model extract claims from **one
   source at a time**, each with a verbatim quote; quotes not found in the page are
   dropped. Output: `evidence.json` + `evidence.md`. Resumable; 20–60 min.
3. **Write** from the evidence pack only, with `templates/special.html`: key findings
   first, one part per question, "What I would do" (Luis), "Method and limits" (from
   the pack's stats), numbered Sources matching the pack. Every factual sentence cites
   `<sup class="cite"><a href="#source-n">n</a></sup>`.
4. **Verify** — `python3 scripts/research/verify.py reports/<slug>.html data/research/<slug>/evidence.json`:
   every cited figure must appear in its source; every URL must resolve (or be archived).
5. **Check and publish** — `check_design.py` and `check_sources.py` (≥ 10 sources, no
   invented URLs) run locally and in CI.

Why one source per model call: in multi-agent deep research most errors arise where
information is synthesised across agents; single-document summarisation is reliable.
The synthesis is done once, by the writer, with the whole evidence pack in view.

### Writing for understanding

Readers come to a report to understand something, not to admire prose (Karpathy's
ladder: clean writing → diagram → web page → explainer video, each easier to take in
than the last). So, in order:

1. **Prose at ~80% of ASD-STE100** (Simplified Technical English): one idea per
   sentence; at most 20 words for a sequence of steps, 25 for a description; active
   voice; one word for one thing (don't call the same system three names); common words
   over impressive ones; no idioms, metaphors or hype. Keep technical terms — STE allows
   them. Quotes from sources are never rewritten. `verify.py` lists sentences over 25 words.
2. **A diagram before a paragraph** when the point is a structure or a flow: every
   special has at least one `figure.diagram` (architecture, decision path or timeline).
   If a part needs three paragraphs to describe how things connect, draw it.
3. **Interactive when it beats a table**: a filter, a toggle or a small calculator over
   the report's own data, in plain JS inside the page budget. Never decoration.
4. **Explainer video** is an experiment, not a rule yet (see the backlog): narration
   with the Kokoro voice we already use for audio, visuals from the report's diagrams.

### Special-report kit

A special is `<html data-type="special">` with `.special-header` (`.special-category`, `<h1>`,
`.special-date`, `.special-subtitle`) and `.section` blocks, each with a `.section-label`
and a `.special-content` body. Inside, use only:

- **Prose:** `h2`, `h3`, `h4`, `p`, `ul`/`ol`, `strong`, `em`, inline `code`, `blockquote`, `hr`.
- **Table:** `<div class="table-wrapper"><table>…</table></div>`.
- **Code:** `<pre><code>…</code></pre>`.
- **Figures:** `.stats-grid` > `.stat-card` > `.stat-value` + `.stat-label` + `.stat-note`
  (with a source link).
- **Diagram:** `<figure class="diagram"><svg viewBox="…">…</svg><figcaption>…</figcaption></figure>`.
  Put the text size on each `<text>` (`font-size="13"`, `text-anchor="middle"`) and the role
  and colour in classes: text `.label` `.title` `.kicker` `.value` `.data` `.caption` +
  `.muted` / `.accent`; shapes `.box` `.box-raised` `.box-accent` `.pill` `.outline` `.frame`
  `.bar-base` `.bar-muted` `.bar-accent`; lines `.edge` `.flow` `.dash` `.grid` `.axis`
  `.rail` `.rail-accent`; points `.dot` `.dot-accent`, arrowheads `.marker`.
  No hex colours or `<style>` in the SVG — except a `.frame` showing a swatch or a
  `.specimen` reproducing another product's type.
- **Citations:** number the Sources list (`<li id="source-4">`) and cite with
  `<sup class="cite"><a href="#source-4">4</a></sup>`. A figure caption says what the
  figure shows and its source; it never repeats the paragraph next to it.
- **Chart (canvas):** `<div class="chart-container"><canvas>…</canvas><p class="chart-caption">…</p></div>`.
- **References:** `<div class="ref-section"><h4>…</h4><ul><li>… <a>…</a></li></ul></div>`.

Need something that isn't here? Add it to `styles.css` and `patterns.html` first, then use it.

Before pushing, run `python3 scripts/check_design.py reports/<file>.html` and, for a special,
`python3 scripts/check_sources.py reports/<file>.html`. CI runs both.

## Rules

- Never edit the generated files (`reports.json`, `sitemap.xml`, `rss.xml`, `og/*.png`,
  the og and ui blocks) by hand.
- Report styling lives in `styles.css`; the index adds `home.css`. Restyle there, never
  inside report files. `scripts/backfill/migrate_design_system.py` and
  `scripts/backfill/unify_diagrams.py` record how older reports were brought into the system.
- Keep all links root-relative (`/reports/…`) or relative so they work on both the
  custom domain and `iamluisgb.github.io`.
- Canonical domain is `https://luisgonzalezbernal.com/reports/`.
- If you change metadata extraction, edit `scripts/generate_manifest.py` and run it
  locally (`python3 scripts/generate_manifest.py`) before pushing.
