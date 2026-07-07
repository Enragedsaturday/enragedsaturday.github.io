# User dispositions — 2026-07-06 (all three decision surfaces)

Received in one message (new orchestrator session; the prior 669k-token session was retired at
its checkpoint — same branch state, d134883). Recorded verbatim-in-substance:

## 1. R14 whitelist extension (Entick/Wilkes) — **Option 1**
"Extend for English-corpus cases: BAILII + scholarly/facsimile second source."
→ IMPLEMENTED this session: S2 spec amendment **A17**; `OFF_CL_ALLOWED_SOURCES` +
`_overhaul2/lake/_schema.json` extended (BAILII · Founders' Constitution · English Reports
facsimile; pairwise distinct-source constraint regenerated 10→28); orchestrator adjudication
files `offcl-entick-adjudication.json` / `offcl-wilkes-adjudication.json` (all four source
pages live-confirmed 2026-07-06; BAILII via archive.org snapshots — bot-challenge on direct
fetch; per-source precision + court-label honesty recorded in trails); both records elevated
`not_found` → **verified_off_cl** via `--elevate-off-cl`; Field-I treatment re-seeded
good_law/migration-seed (F-S2-31's revert applied only while fail-closed — journaled); pages
re-projected. **LINT-6/12/13/14 all 0; self-test green.** Also cleaned 2 F-S2-33 re-key orphan
shells surfaced by LINT-13 ($8,850/Von Neumann old-id files; journaled).

## 2. S6 Packet A (fabrication resolution) — **all four groups approved**
1. Group 1 (21 re-keys through R7) — APPROVED → builder work order
   `PACKET-A-REKEY-WORKORDER.md` (serial CL lane).
2. Group 2 (3 alias-folds: Morse→French · Carroll/Carman · Chatrie-stub) — APPROVED → same
   work order (ledger/lake operations).
3. Group 3 (2 removals: united-states-v-west--10653830, united-states-v-white--10349533) —
   APPROVED with re-anchor surgery + tombstones. Prose surgery executes AFTER the packet-B
   panel closes (reviewers are reading content/ now; inputs stay stable), before the R8 waves.
4. Group 4 (SEED §a watch-list all refuted) — ACKNOWLEDGED. Their stubs terminate through the
   Group-1 re-key lane; Small/Lyle/Moore-Bush cluster-id nuances resolve authoritatively at
   the re-key per the packet note.

## 3. S6 Packet B (borderline sign-off) — **delegated to a review panel** (user protocol)
User directive: a Fable-level agent adjudicates every item independently ∥ a Codex review
agent does the same (mutually blind, recommendation-stripped items); then a third
Fable adjudicator reconciles the two reviews against the full packet and issues final
determinations + recommendation; the orchestrator then implements. Panel artifacts:
`_run/o2-execute/packetb-panel/` (ITEMS.md neutral form · REVIEW-WORKORDER.md ·
review-fable.jsonl · review-codex.jsonl · ADJUDICATION.md). Dispositions fold into
`_run/s6-borderline.md` + the coverage ledger when the panel closes.
