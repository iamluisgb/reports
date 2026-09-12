#!/usr/bin/env bash
# Drive the `backfill-daily` opencode agent over every missing day.
#
# One opencode session per day (fresh context, no cross-day contamination), up to
# JOBS of them at a time. The agents only write HTML: committing is serialised
# here afterwards, because parallel `git add` on one worktree corrupts the index.
# The push happens once at the end so CI rebuilds manifest/RSS/OG a single time.
#
#   ./scripts/backfill/run.sh                    # every missing day up to today
#   ./scripts/backfill/run.sh --until 2026-08-31 # stop earlier
#   ./scripts/backfill/run.sh --days 2026-08-16,2026-08-17
#   JOBS=6 ./scripts/backfill/run.sh             # concurrency (default 4)
#   DRY_RUN=1 ./scripts/backfill/run.sh          # list the days, generate nothing
#   PUSH=1 ./scripts/backfill/run.sh             # push at the end (default: don't)
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO"

MODEL="${MODEL:-nan/glm5.3-flash}"
JOBS="${JOBS:-4}"
PUSH="${PUSH:-0}"
DRY_RUN="${DRY_RUN:-0}"
LOG_DIR="${LOG_DIR:-/tmp/reports-backfill}"
DAYS_ARG=""
UNTIL_ARG=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --days)  DAYS_ARG="$2"; shift 2 ;;
    --until) UNTIL_ARG=(--until "$2"); shift 2 ;;
    --from)  UNTIL_ARG+=(--from "$2"); shift 2 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

command -v opencode >/dev/null || { echo "opencode not found in PATH" >&2; exit 1; }
if [[ -z "${NAN_API_KEY:-}" ]]; then
  echo "NAN_API_KEY not set — the $MODEL provider will refuse to run" >&2
  exit 1
fi

# The day list is computed from the working tree, so a stale clone invents gaps
# for days that are already live (and would then collide on merge). Never skip.
echo "syncing with origin/master…"
FETCHED=0
for attempt in 1 2 3; do
  if git fetch --quiet origin master; then FETCHED=1; break; fi
  echo "  fetch attempt $attempt failed, retrying…" >&2
  sleep $((attempt * 5))
done
if [[ "$FETCHED" != "1" ]]; then
  echo "git fetch failed 3x — refusing to compute the day list from a possibly stale clone" >&2
  exit 1
fi
BEHIND=$(git rev-list --count HEAD..origin/master)
if [[ "$BEHIND" != "0" ]]; then
  echo "local master is $BEHIND commit(s) behind origin — pull first:" >&2
  echo "  git pull origin master --no-rebase" >&2
  exit 1
fi

if [[ -n "$DAYS_ARG" ]]; then
  DAYS="${DAYS_ARG//,/$'\n'}"
else
  DAYS="$(python3 scripts/backfill/missing_days.py ${UNTIL_ARG[@]+"${UNTIL_ARG[@]}"})"
fi

[[ -z "$DAYS" ]] && { echo "nothing missing — every day already has a report"; exit 0; }

COUNT=$(wc -l <<< "$DAYS" | tr -d ' ')
echo "$COUNT day(s) to backfill:"
sed 's/^/  /' <<< "$DAYS"
[[ "$DRY_RUN" == "1" ]] && exit 0

mkdir -p "$LOG_DIR"

# ── generate, JOBS at a time ────────────────────────────────────────────────
echo
echo "generating with $JOBS parallel session(s)…"
for DAY in $DAYS; do
  # macOS ships bash 3.2, which has no `wait -n`: poll the running job count.
  while [[ $(jobs -rp | wc -l) -ge $JOBS ]]; do sleep 2; done
  (
    if opencode run --agent backfill-daily --model "$MODEL" \
         --title "backfill $DAY" \
         "Genera el daily report de $DAY." > "$LOG_DIR/$DAY.log" 2>&1
    then echo "  · $DAY generated"
    else echo "  · $DAY opencode failed (see $LOG_DIR/$DAY.log)"
    fi
  ) &
done
wait
echo "generation done."

# ── verify and commit, one at a time, in date order ─────────────────────────
echo
OK=0; FAILED=()
for DAY in $(tr ' ' '\n' <<< "$DAYS" | sort); do
  FILE="reports/ai-news-$DAY.html"
  if [[ ! -f "$FILE" ]]; then
    echo "✗ $DAY — no report written (see $LOG_DIR/$DAY.log)"
    FAILED+=("$DAY"); continue
  fi
  if ! VERDICT=$(python3 scripts/backfill/verify_report.py "$FILE" 2>&1); then
    echo "✗ $DAY — failed verification:"
    sed 's/^/    /' <<< "$VERDICT"
    FAILED+=("$DAY"); continue
  fi
  git add "$FILE"
  if git diff --staged --quiet -- "$FILE"; then
    echo "· $DAY — unchanged, nothing to commit"
    continue
  fi
  git commit --quiet -m "📰 AI News Daily — $(date -j -f %Y-%m-%d "$DAY" "+%d %b %Y" 2>/dev/null || date -d "$DAY" "+%d %b %Y") (backfill)"
  echo "✓ $DAY — committed"
  OK=$((OK + 1))
done

echo
echo "════════════════════════════════════════"
echo "done: $OK/$COUNT reports committed"
if [[ ${#FAILED[@]} -gt 0 ]]; then
  echo "failed: ${FAILED[*]}"
  echo "re-run just those with: ./scripts/backfill/run.sh --days $(IFS=,; echo "${FAILED[*]}")"
fi

if [[ "$PUSH" == "1" && $OK -gt 0 ]]; then
  echo
  echo "pushing $OK commit(s) to master…"
  git pull origin master --no-rebase && git push origin master
else
  echo
  echo "not pushed. Review with: git log --oneline origin/master..HEAD"
  echo "then: git push origin master   (CI rebuilds manifest, RSS and OG images)"
fi
