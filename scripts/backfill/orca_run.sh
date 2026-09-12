#!/usr/bin/env bash
# Backfill through Orca: one throwaway worktree + supervised agent terminal per
# day, torn down as soon as that day lands.
#
# Why a worktree each: the agents run concurrently, and an isolated checkout
# means a crashed or half-written day can never leave debris in the main tree.
# The generated file is copied back into the main checkout, where verification
# and committing happen serially (git's index is not concurrency-safe).
#
#   ./scripts/backfill/orca_run.sh                     # every missing day
#   ./scripts/backfill/orca_run.sh --days 2026-08-20
#   JOBS=6 MODEL=nan/deepseek-v4-flash ./scripts/backfill/orca_run.sh
#   KEEP=1 ./scripts/backfill/orca_run.sh              # keep worktrees to debug
set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_DIR"

JOBS="${JOBS:-4}"
MODEL="${MODEL:-nan/glm5.3-flash}"
KEEP="${KEEP:-0}"
TIMEOUT_MS="${TIMEOUT_MS:-900000}"
STATE="$REPO_DIR/.backfill/orca"
DAYS_ARG=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --days) DAYS_ARG="$2"; shift 2 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

command -v orca >/dev/null || { echo "orca not found in PATH" >&2; exit 1; }
[[ "$(orca status 2>/dev/null | awk '/runtimeReachable/{print $2}')" == "true" ]] || {
  echo "orca runtime not reachable — run 'orca open' first" >&2; exit 1; }

REPO_ID=$(orca repo list --json | python3 -c "
import sys, json
for r in json.load(sys.stdin)['result']['repos']:
    if r['path'] == '$REPO_DIR':
        print(r['id']); break
")
[[ -n "$REPO_ID" ]] || { echo "repo not registered: orca repo add --path $REPO_DIR" >&2; exit 1; }

echo "syncing with origin/master…"
for attempt in 1 2 3; do
  git fetch --quiet origin master && break
  [[ $attempt == 3 ]] && { echo "git fetch failed 3x" >&2; exit 1; }
  sleep $((attempt * 5))
done
[[ "$(git rev-list --count HEAD..origin/master)" == "0" ]] || {
  echo "local master is behind origin — git pull origin master --no-rebase first" >&2; exit 1; }

if [[ -n "$DAYS_ARG" ]]; then
  DAYS="${DAYS_ARG//,/$'\n'}"
else
  DAYS="$(python3 scripts/backfill/missing_days.py)"
fi
[[ -z "$DAYS" ]] && { echo "nothing missing"; exit 0; }

COUNT=$(wc -l <<< "$DAYS" | tr -d ' ')
mkdir -p "$STATE"
echo "$COUNT day(s) via orca, $JOBS at a time, model $MODEL"

# ── one worktree + agent terminal per day ───────────────────────────────────
launch_day() {
  # bash 3.2 does not expose an earlier assignment to a later one on the same
  # `local` line, and `set -u` turns that into a hard failure.
  local day="$1"
  local name="backfill-$day"
  local wt=""
  local term=""
  wt=$(orca worktree create --name "$name" --repo "id:$REPO_ID" --setup skip --json 2>/dev/null \
       | python3 -c "import sys,json; print(json.load(sys.stdin)['result']['worktree']['path'])" 2>/dev/null)
  if [[ -z "$wt" ]]; then echo "  ✗ $day — worktree create failed"; return 1; fi
  echo "$wt" > "$STATE/$day.worktree"

  term=$(MODEL="$MODEL" orca terminal create --worktree "path:$wt" --title "backfill $day" \
          --command "MODEL=$MODEL bash scripts/backfill/one_day.sh $day" --json 2>/dev/null \
        | python3 -c "import sys,json; print(json.load(sys.stdin)['result']['terminal']['handle'])" 2>/dev/null)
  if [[ -z "$term" ]]; then echo "  ✗ $day — terminal create failed"; return 1; fi
  echo "$term" > "$STATE/$day.terminal"

  orca terminal wait --terminal "$term" --for exit --timeout-ms "$TIMEOUT_MS" --json >/dev/null 2>&1

  orca terminal read --terminal "$term" --json 2>/dev/null \
    | python3 -c "
import sys, json
try: t = json.load(sys.stdin)['result']['terminal']
except Exception: sys.exit()
print('\n'.join(t.get('tail', [])))" > "$STATE/$day.log" 2>/dev/null

  if [[ -f "$wt/reports/ai-news-$day.html" ]]; then
    cp "$wt/reports/ai-news-$day.html" "$REPO_DIR/reports/ai-news-$day.html"
    echo "  · $day generated"
  else
    echo "  · $day produced nothing (see $STATE/$day.log)"
  fi

  if [[ "$KEEP" != "1" ]]; then
    orca terminal stop --worktree "path:$wt" --json >/dev/null 2>&1
    orca worktree rm --worktree "path:$wt" --force --json >/dev/null 2>&1 \
      && rm -f "$STATE/$day.worktree" "$STATE/$day.terminal"
  fi
}

for DAY in $DAYS; do
  while [[ $(jobs -rp | wc -l) -ge $JOBS ]]; do sleep 2; done
  launch_day "$DAY" &
done
wait
echo "agents done."

# ── verify + commit serially, in date order ─────────────────────────────────
echo
OK=0; FAILED=()
for DAY in $(tr ' ' '\n' <<< "$DAYS" | sort); do
  FILE="reports/ai-news-$DAY.html"
  if [[ ! -f "$FILE" ]]; then echo "✗ $DAY — no report"; FAILED+=("$DAY"); continue; fi
  if ! VERDICT=$(python3 scripts/backfill/verify_report.py "$FILE" 2>&1); then
    echo "✗ $DAY — failed verification:"; sed 's/^/    /' <<< "$VERDICT"
    FAILED+=("$DAY"); continue
  fi
  git add "$FILE"
  if git diff --staged --quiet -- "$FILE"; then echo "· $DAY — unchanged"; continue; fi
  git commit --quiet -m "📰 AI News Daily — $(date -j -f %Y-%m-%d "$DAY" "+%d %b %Y") (backfill)"
  echo "✓ $DAY — committed"; OK=$((OK + 1))
done

echo
echo "════════════════════════════════════════"
echo "done: $OK/$COUNT committed"
[[ ${#FAILED[@]} -gt 0 ]] && {
  echo "failed: ${FAILED[*]}"
  echo "retry:  ./scripts/backfill/orca_run.sh --days $(IFS=,; echo "${FAILED[*]}")"
}
echo "worktrees left: $(orca worktree list --json | python3 -c "import sys,json; print(len(json.load(sys.stdin)['result']['worktrees']))")"
echo "not pushed — review: git log --oneline origin/master..HEAD"
