#!/usr/bin/env bash
# Write and synthesise one day's audio briefing.
set -euo pipefail

DAY="${1:?usage: audio_one.sh YYYY-MM-DD}"
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

if [[ -z "${NAN_API_KEY:-}" ]]; then
  NAN_API_KEY=$(sed -n 's/^export NAN_API_KEY=//p' "$HOME/.zshrc" | tr -d "\"'" | head -1)
  export NAN_API_KEY
fi
[[ -n "${NAN_API_KEY:-}" ]] || { echo "NAN_API_KEY unavailable" >&2; exit 1; }

opencode run --agent audio-briefing --model "${MODEL:-nan/deepseek-v4-flash}" \
  --title "audio $DAY" "Escribe y genera el briefing en audio de $DAY."

python3 scripts/backfill/make_audio.py "$DAY" --check
python3 scripts/backfill/verify_report.py "reports/ai-news-$DAY.html"
