#!/usr/bin/env bash
# Review one day's report for items repeated in neighbouring reports.
# Single unquoted argument so an orchestrator can launch it without escaping.
set -euo pipefail

DAY="${1:?usage: review_one.sh YYYY-MM-DD}"
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

if [[ -z "${NAN_API_KEY:-}" ]]; then
  NAN_API_KEY=$(sed -n 's/^export NAN_API_KEY=//p' "$HOME/.zshrc" | tr -d "\"'" | head -1)
  export NAN_API_KEY
fi
[[ -n "${NAN_API_KEY:-}" ]] || { echo "NAN_API_KEY unavailable" >&2; exit 1; }

opencode run --agent dedup-reviewer --model "${MODEL:-nan/deepseek-v4-flash}" \
  --title "dedup $DAY" "Revisa repeticiones en el report de $DAY."

python3 scripts/backfill/verify_report.py "reports/ai-news-$DAY.html"
