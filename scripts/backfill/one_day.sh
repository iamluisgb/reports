#!/usr/bin/env bash
# Generate a single day's report. Kept as a script so an orchestrator can launch
# it with one unquoted argument: nesting the prompt's quotes inside another
# tool's --command string mangles them.
#
#   ./scripts/backfill/one_day.sh 2026-08-20
set -euo pipefail

DAY="${1:?usage: one_day.sh YYYY-MM-DD}"
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Orca terminals do not necessarily inherit an interactive shell's environment.
if [[ -z "${NAN_API_KEY:-}" ]]; then
  NAN_API_KEY=$(sed -n 's/^export NAN_API_KEY=//p' "$HOME/.zshrc" | tr -d "\"'" | head -1)
  export NAN_API_KEY
fi
[[ -n "${NAN_API_KEY:-}" ]] || { echo "NAN_API_KEY unavailable" >&2; exit 1; }

opencode run --agent backfill-daily --model "${MODEL:-nan/glm5.3-flash}" \
  --title "backfill $DAY" "Genera el daily report de $DAY."

python3 scripts/backfill/verify_report.py "reports/ai-news-$DAY.html"
