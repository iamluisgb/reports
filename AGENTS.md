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
   `<!-- og:start -->…<!-- og:end -->` and `<!-- ui:start -->…<!-- ui:end -->` blocks in each
   report; CI regenerates them all on push.
   Don't add font links, scripts or page chrome (theme code, player code, progress bar,
   prev/next) to a report yourself: the ui block brings the fonts, `site.js` and `report.js`,
   which add them to every page. Follow **Design system** below for the markup.

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
- injects an idempotent `<!-- ui:start -->…<!-- ui:end -->` block (site fonts, the
  early theme switch, `site.js`, `report.js`) so every report, old or new, gets the current design.

There is nothing to do by hand — the `<title>` and `subtitle` you write feed the
cards automatically. To preview locally: `pip install Pillow && python3
scripts/build_social.py` (idempotent; re-runs are a no-op).

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

Before pushing, run `python3 scripts/check_design.py reports/<file>.html`. CI runs it too.

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
