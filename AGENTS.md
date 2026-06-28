# AGENTS.md — guidance for the Hermes Agent

This repo is a **GitHub Pages static site**. It has no build step for the agent to run
and no server. The agent's job is to publish report HTML files; everything else is
generated automatically by CI.

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
   `rss.xml`, the `og/` images, or the `<!-- og:start -->…<!-- og:end -->` meta block
   in each report; CI regenerates them all on push.

## Social cards (Open Graph / Twitter)

`scripts/build_social.py` runs in CI and makes every report shareable:
- generates a branded 1200×630 PNG per report under `og/` (fonts bundled in
  `assets/fonts/`, OFL), plus `og/og-default.png` as fallback;
- injects an idempotent `<!-- og:start -->…<!-- og:end -->` block into each
  report's `<head>` (og:*, twitter:summary_large_image, description, canonical),
  with the title/date/summary derived from the same logic as the manifest.

There is nothing to do by hand — the `<title>` and `subtitle` you write feed the
cards automatically. To preview locally: `pip install Pillow && python3
scripts/build_social.py` (idempotent; re-runs are a no-op).

## Rules

- Never edit the generated files (`reports.json`, `sitemap.xml`, `rss.xml`, `og/*.png`,
  the og meta block) by hand.
- Keep all links root-relative (`/reports/…`) or relative so they work on both the
  custom domain and `iamluisgb.github.io`.
- Canonical domain is `https://luisgonzalezbernal.com/reports/`.
- If you change metadata extraction, edit `scripts/generate_manifest.py` and run it
  locally (`python3 scripts/generate_manifest.py`) before pushing.
