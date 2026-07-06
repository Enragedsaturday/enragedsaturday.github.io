#!/usr/bin/env bash
# Session-gate offsite checkpoint (RUNBOOK §5 standing amendment #2, 2026-07-05;
# adversarially reviewed pre-landing — hang-bounds and mount checks are review
# findings #1/#2, not decoration).
#
# Run at EVERY session gate (safe to run any time, foreground or backgrounded).
# Two legs, both FAIL-SOFT and TIME-BOUNDED:
#   1. git push origin <current-branch>   (offsite copy of committed work)
#   2. rsync ~/cssi-lake/ -> Shared_Drive (journal + HTTP cache + db: the
#      quota investment that lives outside the repo)
#
# Guarantees:
# - Exit code is ALWAYS 0; failures print WARN lines for the gate journal.
# - Every external command is alarm-bounded (COH-31: no GNU timeout on macOS;
#   perl alarm survives exec) — a dead NAS or credential prompt cannot stall
#   the gate. Push default 120s, rsync default 1800s (env-tunable).
# - The NAS is verified MOUNTED (mount table, not -d: a stale handle or
#   leftover local dir passes -d) before any write toward it.
# - rsync is additive (no --delete) and read-only on the source; the journal's
#   in-place single file simply re-mirrors. A restored backup may carry a torn
#   final journal line — the resume parser must skip a malformed tail line.
# - Consecutive-failure escalation: >=2 failed checkpoints in a row prints a
#   CHECKPOINT-ESCALATE line — the orchestrator should push-notify the user
#   (a notification, NOT a new pause).
#
# Usage: scripts/gates/session_checkpoint.sh
set -uo pipefail

LAKE_SRC="${CSSI_LAKE_ROOT:-$HOME/cssi-lake}"
# Primary: the NAS (off-machine). Fallback: a local APFS disk separate from the
# boot volume. Either write path requires the sandbox allowlist in
# .claude/settings.json (sandbox.filesystem.allowWrite) or an unsandboxed run.
NAS_MOUNT="/Volumes/Shared_Drive"
NAS_DST="$NAS_MOUNT/cssi-backups/cssi-lake"
LOCAL_DST="/Users/Shared/AIStore/store3/cssi-backups/cssi-lake"
STATE_FILE="$HOME/.cssi-checkpoint-failcount"
PUSH_TIMEOUT="${CHECKPOINT_PUSH_TIMEOUT:-120}"
RSYNC_TIMEOUT="${CHECKPOINT_RSYNC_TIMEOUT:-1800}"

# alarm survives exec, so the exec'd command gets SIGALRM at the bound and
# dies (shell reports 142). Portable caller-side timeout without GNU timeout.
bounded() { # bounded <seconds> <cmd...>
  local secs="$1"; shift
  perl -e 'alarm shift @ARGV; exec @ARGV or exit 127' "$secs" "$@"
}

fail=0

# --- Leg 1: push the current branch ----------------------------------------
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [ -n "$REPO_ROOT" ]; then
  BRANCH="$(git -C "$REPO_ROOT" symbolic-ref --short -q HEAD || true)"
  if [ -z "$BRANCH" ]; then
    echo "checkpoint: WARN — detached HEAD (worktree?); push skipped" >&2
    fail=1
  elif GIT_TERMINAL_PROMPT=0 bounded "$PUSH_TIMEOUT" git -C "$REPO_ROOT" push origin "$BRANCH"; then
    echo "checkpoint: push OK (origin/$BRANCH @ $(git -C "$REPO_ROOT" rev-parse --short HEAD))"
  else
    rc=$?
    [ "$rc" -eq 142 ] && why="timed out after ${PUSH_TIMEOUT}s" || why="failed (rc=$rc; offline? auth?)"
    echo "checkpoint: WARN — git push $why; committed work is NOT offsite this gate" >&2
    fail=1
  fi
else
  echo "checkpoint: WARN — not in a git repo; push skipped" >&2
  fail=1
fi

# --- Leg 2: back up the lake state ------------------------------------------
# Chain, first success wins:
#   1. git commit+push of the lake repo to its private origin (true offsite;
#      works from any session, no TCC/mount dependency)
#   2. rsync to the NAS (needs a live mount + TCC grant to this process tree)
#   3. rsync to the local second disk (needs TCC for external volumes)
try_git_backup() {
  [ -d "$LAKE_SRC/.git" ] || { echo "checkpoint: note — lake repo not initialized; git leg skipped" >&2; return 1; }
  git -C "$LAKE_SRC" remote get-url origin >/dev/null 2>&1 || { echo "checkpoint: note — lake repo has no origin; git leg skipped" >&2; return 1; }
  bounded 600 git -C "$LAKE_SRC" add -A >/dev/null 2>&1 || { echo "checkpoint: note — lake git add failed/timed out" >&2; return 1; }
  if ! git -C "$LAKE_SRC" diff --cached --quiet 2>/dev/null; then
    bounded 120 git -C "$LAKE_SRC" commit -q -m "checkpoint $(date -u +%Y-%m-%dT%H:%M:%SZ)" || { echo "checkpoint: note — lake git commit failed" >&2; return 1; }
  fi
  GIT_TERMINAL_PROMPT=0 bounded "$RSYNC_TIMEOUT" git -C "$LAKE_SRC" push -q origin main || { echo "checkpoint: note — lake git push failed/timed out" >&2; return 1; }
  echo "checkpoint: lake backup OK -> git origin ($(git -C "$LAKE_SRC" rev-parse --short HEAD))"
  return 0
}

# rsync legs: SMB-appropriate flags: no owner/group/perms/xattrs (smbfs rejects
# them and every gate would WARN on exit 23). Exit 24 (source file vanished —
# the builder is live) counts as success.
try_backup() { # try_backup <dst> ; returns 0 on success
  local dst="$1" rc
  bounded 30 mkdir -p "$dst" 2>/dev/null || return 1
  bounded "$RSYNC_TIMEOUT" rsync -rlt --no-owner --no-group --no-perms \
    --exclude ".DS_Store" "$LAKE_SRC/" "$dst/" >"$RSYNC_LOG" 2>&1
  rc=$?
  if [ "$rc" -eq 0 ] || [ "$rc" -eq 24 ]; then
    bounded 30 sh -c "date -u +%Y-%m-%dT%H:%M:%SZ > '$dst/LAST-BACKUP.txt'" 2>/dev/null || true
    echo "checkpoint: lake backup OK -> $dst (rsync rc=$rc; log: $RSYNC_LOG)"
    return 0
  fi
  [ "$rc" -eq 142 ] && echo "checkpoint: note — rsync to $dst timed out after ${RSYNC_TIMEOUT}s" >&2 \
                    || echo "checkpoint: note — rsync to $dst failed (rc=$rc)" >&2
  return 1
}

if [ ! -d "$LAKE_SRC" ]; then
  echo "checkpoint: WARN — lake dir $LAKE_SRC not found; rsync skipped" >&2
  fail=1
else
  LOG_DIR="$LAKE_SRC/logs"
  mkdir -p "$LOG_DIR"
  RSYNC_LOG="$LOG_DIR/checkpoint-rsync-$(date +%Y%m%d-%H%M%S).log"
  backed_up=0
  if try_git_backup; then
    backed_up=1
  # NAS only if genuinely in the mount table (-d passes on a stale handle or
  # leftover local dir; the mount table doesn't).
  elif mount | grep -q " on $NAS_MOUNT " && try_backup "$NAS_DST"; then
    backed_up=1
    echo "checkpoint: note — used NAS fallback (git leg failed)" >&2
  elif try_backup "$LOCAL_DST"; then
    backed_up=1
    echo "checkpoint: note — used LOCAL-disk fallback; off-machine copy is stale" >&2
  fi
  if [ "$backed_up" -ne 1 ]; then
    echo "checkpoint: WARN — no backup leg succeeded; lake NOT backed up this gate (log: $RSYNC_LOG)" >&2
    echo "checkpoint: hint — git leg needs the lake repo origin reachable; rsync legs need a TCC grant (+ sandbox allowlist in .claude/settings.json for sandboxed runs)" >&2
    fail=1
  fi
fi

# --- Escalation counter ------------------------------------------------------
if [ "$fail" -ne 0 ]; then
  count=$(( $(cat "$STATE_FILE" 2>/dev/null || echo 0) + 1 ))
  echo "$count" > "$STATE_FILE"
  echo "checkpoint: completed WITH WARNINGS (consecutive failures: $count)"
  if [ "$count" -ge 2 ]; then
    echo "CHECKPOINT-ESCALATE: $count consecutive checkpoint failures — push-notify the user (notification, not a pause)"
  fi
else
  echo "0" > "$STATE_FILE"
  echo "checkpoint: completed clean"
fi
exit 0
