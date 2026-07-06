# Orchestrator notice — 2026-07-05 (side-session, user-directed; adversarially reviewed)

Items landed on the branch while session 12 was running; pick up at this gate:

1. **F-S2-25 work order** (`S2-FIX-25-WORKORDER.md`) — dispatch to the builder lane **before the
   93-row stub leg**. The T–Z page rows are already past (session 12 wrote through the U's), so
   expect a small **readjudication batch on the F-S2-25 party-key class**: any T–Z row that
   landed `fabrication_suspected` where the caption carries a T6 contraction-family token
   (Ass'n/Association etc.) is a candidate FP of this class — fail-closed held, so it's rework,
   not corruption. The word-boundary bound in the work order is mandatory (see its Gate note).
2. **RUNBOOK §5 gained two standing amendments** (user decisions 2026-07-05): the spec-completion
   CodeRabbit gate (run `scripts/gates/coderabbit_gate.sh S2` at S2 close, before verified-flips)
   and the session-gate checkpoint + pause-notification protocol. Read both §5 blocks — short and
   self-contained. The EXECUTE wrapper's Standing disciplines carry matching lines.
3. **From this gate on:** end every session gate with `scripts/gates/session_checkpoint.sh`.
   It pushes the branch and backs up `~/cssi-lake` (git leg to the private `cssi-lake-backup`
   repo first; rsync legs are TCC-gated fallbacks). It is fail-soft and alarm-bounded — it cannot
   hang your gate. Journal its output; on a `CHECKPOINT-ESCALATE` line, push-notify the user.
   Note for THIS session: the auto-mode classifier may block the lake repo's first-ever push
   ("bulk relocation") — the user runs that one directly; incremental pushes thereafter are
   normal. If the git leg is blocked in-session, the WARN is expected until the user's push
   lands.
4. **Pause surfacing:** any §0 pause / lane-outage halt now fires a push notification + a served
   HTML-brief evidence packet before waiting. Surfacing only — the register is unchanged.
5. **Standing draft PR #3** (`overhaul2/execute` → `main`) exists; session-gate pushes keep it
   fresh. RETRO-W0W1 CodeRabbit artifacts land in `_run/gates/` (scoped: scripts/lint, quartz,
   scripts/s5, scripts/gates — scripts/s2 deliberately excluded, its gate runs at S2 close);
   any resulting work orders will sit alongside this notice.
6. **S2 § A16 (user-approved 2026-07-05) + F-S2-26** (`S2-FIX-26-WORKORDER.md`): the
   `verified_off_cl` resting state for outside-CL-corpus cases (Entick) + the terminal-not_found
   churn fix. Dispatch F-S2-26 with F-S2-25 at the next fix window — same loop, no session
   interrupt (spec/schema text is inert to the running process; code changes bind at relaunch).
   Do NOT hand-edit the Entick record while a session is live (the churn bug rewrites it every
   session until Defect 1 lands); its elevation runs through the new `--elevate-off-cl` path
   with an orchestrator-prepared, web-verified adjudication file. Mind the work order's R14
   whitelist caveat — a whitelist-extension decision may need to surface to the user.
