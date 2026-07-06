#!/usr/bin/env bash
# Spec-completion CodeRabbit gate (RUNBOOK §5 standing amendment, 2026-07-05).
#
# Runs a headless CodeRabbit CLI review of COMMITTED changes in a detached git
# worktree pinned to the spec-close commit, so the live builder working tree
# (S2's paced lane journals/caches/records) is never touched and the review is
# deterministic even while the build keeps moving. Scope is enforced by the
# repo-root .coderabbit.yaml path filters (code paths only — never the lake,
# content/, or run ledgers).
#
# Usage: scripts/gates/coderabbit_gate.sh <SPEC-ID> [ref] [base] [dir]
#   SPEC-ID  e.g. S2 — names the artifact
#   ref      commit to review as of (default HEAD)
#   base     branch or commit to diff against (default main; falls back to
#            origin/main if no local main)
#   dir      optional repo-relative directory — restrict the review to git
#            changes inside it (CLI --dir); use for scoped/retro runs on a
#            branch whose full diff is huge
#
# The CLI call is alarm-bounded (CR_GATE_TIMEOUT, default 3600s) so an
# unattended gate can never hang a session (COH-31: perl alarm survives exec).
#
# Artifact: _run/gates/<SPEC-ID>-coderabbit-<shortsha>.md
# Exit: non-zero only on mechanical failure (CLI/worktree/timeout). Findings
# are NOT an exit condition — they are adjudicated find→adjudicate→fix
# (loop-cap-3 → _review-needed/), never auto-applied. Writer≠approver holds.
set -euo pipefail

SPEC="${1:?usage: coderabbit_gate.sh <SPEC-ID> [ref] [base] [dir]}"
REF="${2:-HEAD}"
BASE="${3:-main}"
SCOPE_DIR="${4:-}"
CR_GATE_TIMEOUT="${CR_GATE_TIMEOUT:-3600}"

bounded() { # bounded <seconds> <cmd...>
  local secs="$1"; shift
  perl -e 'alarm shift @ARGV; exec @ARGV or exit 127' "$secs" "$@"
}

CODERABBIT_BIN="${CODERABBIT_BIN:-$(command -v coderabbit || echo "$HOME/.local/bin/coderabbit")}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
SHA="$(git -C "$REPO_ROOT" rev-parse --short "$REF")"
OUT_DIR="$REPO_ROOT/_run/gates"
# SPEC names the artifact file — sanitize so a stray '/' or '..' can never
# escape _run/gates (the raw SPEC still appears in the artifact header).
SAFE_SPEC="$(printf '%s' "$SPEC" | tr -c 'A-Za-z0-9._-' '_')"
OUT="$OUT_DIR/${SAFE_SPEC}-coderabbit-${SHA}.md"
WT="$(mktemp -d "${TMPDIR:-/tmp}/cr-gate-${SPEC}-XXXXXX")"
mkdir -p "$OUT_DIR"

cleanup() {
  git -C "$REPO_ROOT" worktree remove --force "$WT" 2>/dev/null || true
  rm -rf "$WT" 2>/dev/null || true
}
trap cleanup EXIT

# mktemp created the dir; worktree add needs it absent.
rmdir "$WT"
git -C "$REPO_ROOT" worktree add --detach "$WT" "$SHA" >/dev/null 2>&1

# Branch base -> --base; anything else that resolves to a commit -> --base-commit.
if git -C "$WT" rev-parse --verify --quiet "refs/heads/${BASE}" >/dev/null; then
  BASE_ARGS=(--base "$BASE")
elif git -C "$WT" rev-parse --verify --quiet "refs/remotes/origin/${BASE}" >/dev/null; then
  BASE_ARGS=(--base "origin/${BASE}")
elif git -C "$WT" rev-parse --verify --quiet "${BASE}^{commit}" >/dev/null; then
  BASE_ARGS=(--base-commit "$BASE")
else
  echo "coderabbit_gate: base '${BASE}' resolves to neither branch nor commit" >&2
  exit 2
fi

SCOPE_ARGS=()
if [ -n "$SCOPE_DIR" ]; then
  SCOPE_ARGS=(--dir "$WT/$SCOPE_DIR")
fi

{
  echo "# CodeRabbit gate — ${SPEC} @ ${SHA} (base: ${BASE})"
  echo ""
  echo "- run: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "- cli: $("$CODERABBIT_BIN" --version 2>/dev/null || echo unknown)"
  echo "- mode: --plain --type committed ${BASE_ARGS[*]} ${SCOPE_ARGS[*]:-}"
  echo "- scope: .coderabbit.yaml path filters (code only)${SCOPE_DIR:+ · restricted to $SCOPE_DIR}"
  echo ""
  echo '```'
} > "$OUT"

set +e
(cd "$WT" && bounded "$CR_GATE_TIMEOUT" "$CODERABBIT_BIN" review --plain --type committed "${BASE_ARGS[@]}" ${SCOPE_ARGS[@]+"${SCOPE_ARGS[@]}"}) >> "$OUT" 2>&1
RC=$?
set -e
echo '```' >> "$OUT"
[ "$RC" -eq 142 ] && echo "TIMEOUT: review exceeded ${CR_GATE_TIMEOUT}s" >> "$OUT"

echo "coderabbit_gate: exit=${RC} artifact=${OUT}"
exit "$RC"
