# Builder work order — R8 citation/identity recovery for the 48 mint-blocked rows (2026-07-07)

Authority: `_run/o2-execute/R8-CITATIONS-ADJUDICATION.md` (read first, in full — the R1/R2/R3
partition, per-row notes, and the two ratified mechanisms). Escalation source:
`_run/o2-execute/R8-ENRICH-CITATIONS-REPORT.md` §Escalations. Repo
`/Users/johngalt/Projects/cssi-quartz`, branch `overhaul2/execute`, start from HEAD after the
R8-pipeline gate commit; **commit nothing** (orchestrator commits at the gate). Ground truth for
scope: the lake at runtime (worklist rows lacking `citations.display`), not this prose — expected
48; report the real roster.

## R1 — identity re-keys (≤14 rows; investigate → web-verify → re-key → readjudicate)
For each of the 7 cite-mismatch + 7 no-display suspects (roster in the adjudication):
1. **Investigate first** (web, zero CL): confirm whether the verified cluster is genuinely the
   wrong entry (orders/cert/rehearing/companion/wrong court) or the right cluster with a CL cite
   gap. carroll-v-carman in particular may be the right per-curiam cluster missing only its
   `U.S.` cite — if so it moves to R3 handling, no re-key.
2. **Dual-leg web verification** of the true merits identity (caption, official cite, docket,
   court, date) — two independent sources per row, packet-A style; assemble the web-keys JSONL.
3. `--apply-web-keys` (fabrication/reset path as packet A; refuse on leg disagreement — escalate)
   then `--readjudicate-file` through the single serial CL lane, paced ≤14/min, resumable.
   Expected terminal: `verified_identity` with correct cluster + citations; honest terminals
   with full rung trails otherwise. Journal every step; reset-orphan shells removed + journaled
   per the packet-A precedent.

## R2 — serializer noise-reporter amendment (6 rows; surgical signed-serializer change)
Amend `scripts/s2/serializer.py` official-selection candidacy with a NAMED exclusion list of
specialty/noise reporters observed in this corpus (`Fla. L. Weekly Fed. S`, `FED App.`, plus any
the 6 rows actually present — enumerate from data, keep the list minimal and literal). Behavior:
excluded reporters never compete for official selection; everything else unchanged; still
fail-closed (`same_rank_tie`) when genuine ambiguity remains. Fixtures + self-test for each named
reporter and a not-on-list control. Then re-run `--enrich-citations` over the 6 (cache-served;
verify the expected cites land: mendez 581 U.S. 420 · grady 575 U.S. 306 · manuel 580 U.S. 357 ·
james-daniel-good 510 U.S. 43 · ziglar 582 U.S. 120 · northrup 785 F.3d 1128).

## R3 — dual-leg web-cite recovery (28 citations-empty rows)
1. Extend the schema (`_overhaul2/lake/_schema.json`) + LINT-13 pairwise constraints with a new
   citations source value for web-recovered cites (e.g. `web-dual-leg`); the provenance must
   never masquerade as `cluster.citations[]`. Mirror the A17/A18 amendment style (schema +
   lint + journal all move together).
2. For each row: two INDEPENDENT web legs enumerate the official cite (court PDFs, Justia,
   CaseText, Google Scholar, circuit websites — no Wikipedia-only sourcing). Legs agree → write
   the citations block with the new source + a per-row trail `{leg1: {source_url, cite}, leg2:
   {...}}` in the journal. Legs disagree → escalate the row, write nothing.
3. Genuinely slip-only (no reporter cite exists yet): journal a `slip-only` terminal note on the
   record (S2 A3 precedent), leave `citations.display` empty, and LIST these in the report —
   the mint's `record-missing-citation` handling for slip-only rows is a follow-up orchestrator
   decision; do not improvise one.
4. New ingest surface if needed (`--apply-web-cites <jsonl>`): bounded, journaled, refuses rows
   outside the named scope or already citation-bearing — the `--apply-web-keys` pattern.

## Lane + report
Web legs: zero CL. CL work (R1 readjudication only): single serial lane, ≤14/min, 0×429
tolerance. Deliver `_run/o2-execute/R8-CITE-RECOVERY-REPORT.md`: per-row outcomes for all 48
(R1 re-key results w/ rung trails · R2 before/after + serializer diff summary · R3 cites landed /
slip-only / escalated), call counts, self-test results, escalations. Final message: compact
summary with the new mintable count out of 148.
