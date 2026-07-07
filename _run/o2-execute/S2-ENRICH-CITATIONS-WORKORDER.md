# Builder work order — S2 citations enrichment for R8-mintable stubs (2026-07-07)

Context: R8 pipeline adjudication E4 (`_run/o2-execute/R8-PIPELINE-ADJUDICATION.md`). 80 of the
148 signed R8-WORKLIST rows are identity-only stubs (SD10) with no `citations` block; the mint
CLI fail-closes on `record-missing-citation`. Populate citations for exactly those rows.
Repo `/Users/johngalt/Projects/cssi-quartz`, branch `overhaul2/execute`, start from HEAD;
**commit nothing** (orchestrator commits at the gate).

## Step 1 — bounded ingest.py surface (offline, self-tested, fixtured)
Add `--enrich-citations <ids-file>` to `scripts/s2/ingest.py`, styled on the `--apply-web-keys`
precedent (bounded, journaled, refuses out-of-scope rows):
- Input: a text/JSONL file of record_ids. Emit the actual list yourself at runtime: every
  R8-WORKLIST.json row whose lake record lacks `citations.display` (expected 80 at HEAD — report
  the real count; ground truth is the lake, not this prose).
- Per record: require an existing `cluster_id` (identity already verified — do NOT re-run
  identity); fetch the cluster through the existing paced client/cache; populate the `citations`
  block via the existing official-selection serializer path (same shape as verified records —
  official/parallel/all/display/official_selection). No treatment work, no opinion reads, no
  other field touched. Status unchanged (`verified_identity` rows stay `verified_identity`).
- Refuse: rows not in the ids-file scope, rows with no cluster_id (report, don't guess),
  rows already citation-bearing (idempotent no-op, reported).
- Journal per row `{step: "r8.enrich-citations", record_id, before: null|display, after: display,
  source: "cluster.citations[]"}`. Self-test + fixture for: happy path, already-bearing no-op,
  no-cluster refusal, out-of-scope refusal.
- A cluster with **zero citations[]** (possible for very recent/slip-only cases): leave the
  record honest (no fabricated cite), journal `citations-empty`, and LIST those rows in the
  report — the orchestrator will adjudicate slip-cite handling for them (S2 A3 pinpoint_status
  precedent). Do not invent a cite; do not block the rest of the run.

## Step 2 — the paced run (single serial CL lane — you are the only CL user right now)
Same lane discipline as every S2 session: pacing ≤14/min, resumable cursor, log to
`_overhaul2/ledger/cl-calls.log` conventions, `--session-minutes` bound. Expected ~80–160 calls
(cluster fetches; many should hit the HTTP cache). Zero 429 tolerance — back off on the first,
never parallel-lane.

## Report
`_run/o2-execute/R8-ENRICH-CITATIONS-REPORT.md`: real scope count, per-row outcomes summary,
citations-empty list, call count + cache-hit rate, journal pointer, self-test results,
escalations (anything ambiguous). Final message: compact summary.
