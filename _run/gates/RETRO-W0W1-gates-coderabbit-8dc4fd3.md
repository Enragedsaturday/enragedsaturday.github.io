# CodeRabbit gate — RETRO-W0W1-gates @ 8dc4fd3 (base: main)

- run: 2026-07-06T00:47:29Z
- cli: 0.6.4
- mode: --plain --type committed --base main --dir /var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T//cr-gate-RETRO-W0W1-gates-DcRDSp/scripts/gates
- scope: .coderabbit.yaml path filters (code only) · restricted to scripts/gates

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.
Connecting to CodeRabbit... 7s elapsed
Preparing review... 9s elapsed
────────────────────────────────────────
CodeRabbit Review

Diff      : committed changes only
Compare   : HEAD → main
Directory : cr-gate-RETRO-W0W1-gates-DcRDSp/scripts/gates
────────────────────────────────────────

(\(\
(• .•)  I am a verified code reviewer on Twitter.

Preparing sandbox... 10s elapsed
Summarizing changes... 14s elapsed
Finishing analysis tools... 38s elapsed
Writing review comments... 38s elapsed
Writing review comments... 1m 07s elapsed - still working

────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-gates-DcRDSp/scripts/gates/session_checkpoint.sh:132scripts/gates/session_checkpoint.sh:132-144]8;;

  Do not return success for failed checkpoint gates.

  This unconditionally exits 0 even after branch push and all backup legs
  fail, so a status-based gate/orchestrator can record the checkpoint as
  verified. Return non-zero on fail != 0, or require the caller to
  explicitly opt into fail-soft mode. As per path instructions, "Prioritize:
  fail-closed behavior (errors must never pass silently as success)."




  Proposed fix

   else
     echo "0" > "$STATE_FILE"
     echo "checkpoint: completed clean"
   fi
  -exit 0
  +exit "$fail"


────────────────────────────────────────────────────────────────────────
  major [Stability & Availability]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-gates-DcRDSp/scripts/gates/session_checkpoint.sh:110scripts/gates/session_checkpoint.sh:110-112]8;;

  Bound and check log-directory creation.

  mkdir -p "$LOG_DIR" is neither alarm-bounded nor checked, so a stuck
  lake path can hang the checkpoint before the bounded rsync leg starts. As
  per path instructions, "errors must never pass silently as success."




  Proposed fix

     LOG_DIR="$LAKE_SRC/logs"
  -  mkdir -p "$LOG_DIR"
  +  if ! bounded 30 mkdir -p "$LOG_DIR"; then
  +    echo "checkpoint: WARN — could not create rsync log dir $LOG_DIR" >&2
  +    fail=1
  +    LOG_DIR="${TMPDIR:-/tmp}"
  +  fi
     RSYNC_LOG="$LOG_DIR/checkpoint-rsync-$(date +%Y%m%d-%H%M%S).log"


────────────────────────────────────────────────────────────────────────
  major [Stability & Availability]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-gates-DcRDSp/scripts/gates/session_checkpoint.sh:133scripts/gates/session_checkpoint.sh:133-135]8;;

  Handle corrupt fail-count state safely.

  A non-numeric $STATE_FILE can break the arithmetic expansion and skip
  escalation/state repair. Sanitize before incrementing so checkpoint
  resumability survives partial writes or manual edits.




  Proposed fix

   if [ "$fail" -ne 0 ]; then
  -  count=$(( $(cat "$STATE_FILE" 2>/dev/null || echo 0) + 1 ))
  +  prev="$(cat "$STATE_FILE" 2>/dev/null || echo 0)"
  +  case "$prev" in
  +    ''|*[!0-9]*) prev=0 ;;
  +  esac
  +  count=$(( prev + 1 ))
     echo "$count" > "$STATE_FILE"


────────────────────────────────────────────────────────────────────────
  major [Stability & Availability]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-gates-DcRDSp/scripts/gates/session_checkpoint.sh:37scripts/gates/session_checkpoint.sh:37-44]8;;

  Validate timeout env vars before using alarm.

  CHECKPOINT_PUSH_TIMEOUT=0 or a non-numeric value can effectively remove
  the bound, letting git/rsync hang despite the gate’s timeout guarantee.
  Reject invalid values before calling bounded. As per path instructions,
  "Prioritize: fail-closed behavior ... and API-quota safety."




  Proposed fix

   PUSH_TIMEOUT="${CHECKPOINT_PUSH_TIMEOUT:-120}"
   RSYNC_TIMEOUT="${CHECKPOINT_RSYNC_TIMEOUT:-1800}"
  +
  +case "$PUSH_TIMEOUT" in
  +  ''|*[!0-9]*|0) echo "checkpoint: WARN — invalid CHECKPOINT_PUSH_TIMEOUT=$PUSH_TIMEOUT" >&2; exit 1 ;;
  +esac
  +case "$RSYNC_TIMEOUT" in
  +  ''|*[!0-9]*|0) echo "checkpoint: WARN — invalid CHECKPOINT_RSYNC_TIMEOUT=$RSYNC_TIMEOUT" >&2; exit 1 ;;
  +esac


────────────────────────────────────────────────────────────────────────
  major [Security & Privacy]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-gates-DcRDSp/scripts/gates/coderabbit_gate.sh:29scripts/gates/coderabbit_gate.sh:29-45]8;;

  Sanitize SPEC before using it in OUT.

  SPEC is interpolated directly into the artifact filename, so values
  containing / or .. can escape _run/gates and overwrite arbitrary
  files under the repo root. Keep the human-readable SPEC in the header,
  but normalize or whitelist it for filesystem use.




  As per path instructions, scripts/ should prioritize fail-closed behavior
  and correctness of comparison/normalization logic.


  Suggested fix

   SPEC="${1:?usage: coderabbit_gate.sh <SPEC-ID> [ref] [base] [dir]}"
   REF="${2:-HEAD}"
   BASE="${3:-main}"
   SCOPE_DIR="${4:-}"
   CR_GATE_TIMEOUT="${CR_GATE_TIMEOUT:-3600}"
  +
  +SAFE_SPEC="${SPEC//[^A-Za-z0-9._-]/_}"
  @@
  -OUT="$OUT_DIR/${SPEC}-coderabbit-${SHA}.md"
  +OUT="$OUT_DIR/${SAFE_SPEC}-coderabbit-${SHA}.md"


────────────────────────────────────────
Review complete
5 findings ✔

Major    5
────────────────────────────────────────

Print all AI prompts: coderabbit review --show-prompts
```
