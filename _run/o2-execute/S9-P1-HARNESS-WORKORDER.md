# S9 P1-H work order — lane harness + pilot batch (lane: o2-opus-xhigh; COMMIT NOTHING; zero CL)

**Read first:** spec R1 (isolation mechanics — every clause is a hard requirement) · R4/R5 ·
`_overhaul2/s9-demo/LEDGER-SCHEMA.md` (the four signed row types) · spec §9 "Codex
output-schema drift" (your pilot exercises exactly this) · `_run/s9/thread-P.json` header
(FROZEN — the hash is in git at a4e2ac3; Thread-N manifests may now issue) ·
`_run/s9/assertion-inventory.json` header.

## Deliverable 1 — `scripts/s9/lane_runner.py`

The one harness every P1/P2 lane invocation goes through:
- **Codex lane invocation**: fresh `codex exec` per call (NEVER resume), `-s read-only`,
  isolated working dir per invocation (temp dir with ONLY the manifest-listed files copied/
  symlinked in — the sandbox root, so the lane physically cannot read the page/judgment
  fields), model gpt-5.5, `-c model_reasoning_effort=xhigh`, stdin `/dev/null`, `-o` capture,
  caller-side perl-alarm timeout (COH-31), `-c tools.web_search=true` ONLY when the work
  order says discovery (default OFF for reviewers/readers).
- **Manifest emission**: every invocation writes `_run/s9/manifests/<lane-id>.json` BEFORE
  launch: {lane_id, lane_kind, model, files_disclosed[], fields_excluded[], assertion_ids[]/
  case_ids[], issued_at, thread_p_hash_at_issue}. Blind Thread-N manifests MUST exclude: the
  case's content page, the lake record's judgment fields (treatment/homes — identity fields
  only: caption/cluster/opinion ids), and thread-P.json. Reviewer manifests MUST exclude
  sibling votes + in-progress adjudications.
- **Output contract + repair**: lanes return JSON per a schema you define per lane_kind
  (case-read: the R5 structured conclusions incl. the MANDATORY identity assertion
  {parties_in_text, caption_claimed, match: bool}; vote: s9.vote.v1). Strip/repair
  prose-wrapped JSON; unparseable → re-run ONCE → then record `no-vote` (a 2-lane tally then
  requires unanimity to kill — spec §9).
- **Row emission**: append-safe JSONL under `_run/s9/` per LEDGER-SCHEMA (findings.jsonl /
  votes.jsonl / adjudications.jsonl / fixes.jsonl + reads: `thread-N-reads.jsonl`), every row
  carrying {lane, model} exactly (`gpt-5.5` / `claude-opus-4-8` / `claude-fable-5`).
- `--self-test`: fixture manifest + a MOCK lane mode (no live codex) proving isolation
  (manifest violation detection), repair, no-vote fallback, row validity vs LINT-30.

## Deliverable 2 — work-queue partitioner `scripts/s9/build_worklists.py`

From thread-P.json + the inventory: `_run/s9/worklists/thread-n-cases.jsonl` (609 rows:
case_id, caption, cluster_id, lead_opinion_id, cached_text_path, batch assignment — R5
ordering: recency → negatives → rule-bearing → high-profile → rest; batch width ~15) ·
`panel-review.jsonl` (paneled legal-assertion surfaces grouped per object: existence/support/
quote-fidelity/pincite/treatment/black-letter — from inventory kinds, batched per page) ·
`doctrine-rederive.jsonl` (115 doctrine-grain items — FABLE lane, not yours to run).
Verify: every thread-P case appears in exactly one batch; cached text presence checked
(Thornton 9434613 KNOWN-absent → row flagged `no_cached_text`, routed to the live-CL
identity slice, NOT silently dropped).

## Deliverable 3 — PILOT (the drift shakeout, spec §9)

Run ONE case-read batch of 5 (pick: 1 recency [Chatrie], 1 negative-treatment [Belton],
1 rule-bearing [Terry], 1 high-profile [Riley 2014], 1 ordinary) through BOTH Codex lenses
(A: support/quote-fidelity · B: currency/treatment) as real `codex exec` calls, plus the
Opus PANEL-VOTE lane on 5 sampled paneled assertions from those cases (you are the Opus
lane for the pilot — vote via a FRESH sub-invocation of yourself only if you can isolate
manifests; otherwise mark the pilot vote rows lane=o2-opus-xhigh-pilot and note that
production panel votes run as separate lane invocations). Report: parse success rate,
repair/no-vote counts, identity-assertion presence 10/10, a sample read's full JSON, wall
clock + token estimate per read (the scaling lever is batch width — spec §9), and LINT-30
run on the produced rows (must be CHECKED green or enumerate breaches).

## Deliverable 4 (small) — `scripts/lint/lint11_pipeline_vocab.py`

The R8 #11 row (TEACH-02b): the S1 A2 five-class pattern table, rendered-prose scope,
About-page allowlist, committed exclusion list. Read S1 A2 in `_overhaul2/specs/
S1-standards.spec.md` for the pattern classes. Fixtures pass/fail; wire into run_all +
self-test gate; report corpus counts by class (expect near-0 — S7 killed the reader-facing
class; any hits are real findings).

Constraints: stdlib only · COMMIT NOTHING · content read-only · the ONLY live Codex calls
are the pilot's (≤12 invocations) · zero CL anywhere · do not touch sibling scripts/s9 files
(build_inventory/build_thread_p/check_ledger exist; import, don't fork).
