# Data

`candidates/AAAA-MM-DD.json` — everything `scripts/collect.py` gathered for that day's
briefing before the writer chose: Hacker News stories (title, url, points, comments, rank),
arXiv papers and semantic-layer items. Saved by `.github/workflows/daily.yml` from
4 Oct 2026 onwards. It is raw material for special reports built on original data
(what builders paid attention to, which topics rose and fell), so never edit it by hand.

`research/<slug>/` holds the evidence pack behind each special report written with the
research pipeline (`scripts/research/`): the sources, their extracted claims and quotes.
