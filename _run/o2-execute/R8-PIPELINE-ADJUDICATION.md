# Orchestrator adjudication — R8 pipeline build escalations E1–E4 (2026-07-07)

Builder report: `_run/o2-execute/R8-PIPELINE-BUILD-REPORT.md` (19/19 self-tests, specimen PASS,
4 escalations, escalate-don't-guess honored). Adjudicated by the orchestrator (Fable) per the
thin-orchestrator find→adjudicate→fix loop; loop 2 work order follows.

## E1 — Born status: `under_review` RATIFIED (builder's default stands)
S6 R8's "born `lake.status: draft`" vs S6 §8's "carries `under_review` until the gates pass":
`under_review` is the schema-real manifest status (the lake vocabulary has no `draft` terminal;
`draft` in R8 reads as the S5 R15 *draft-state banner family*, and R15 renders the identical ⚪
banner for both). §8 names `under_review` for the specimen's own re-entry. **Default
`--born-status under_review` ratified;** the `draft` override stays as an escape hatch, unused.
No code change.

## E2 + E3 — Legacy Case Index / homes pages: NO corpus-wide convert-first. Two amendments.
S5 Method §5.2 is explicit: **S7 runs `convert_tables.py` per-page during doctrine production**
(user decision — prose judgment stays human). A corpus-wide convert-first at S6 would overturn
that; declined. Instead the mint contract is amended (transitional, journaled):

**(a) Case Index — single-writer is the generator, not the CLI.** `scripts/build_case_index.py`
derives rows from pages (`holding:` payload-merged frontmatter + projected `homes` + opinion URL —
all already produced by the mint). **The CLI's index-insertion surface is REMOVED**; each wave
batch closes with an index regen (idempotent, diff-clean by design). The schema-3 flip of the
Index itself stays owed to the S3-owned generator at S7/S8-time — not S6's to force. This also
retires refusal code `case-index-not-r6-converted`.

**(b) Homes-page Key/Related rows — ledger-deferred to S7.** The CLI shall **not write homes
pages at all** (remove the insertion path + `home-not-r6-converted`; KEEP the `home-page-missing`
existence validation). The authored-ledger row already carries `homes[]`+`roles[]` — that is the
owed-row record. **S7 materializes the Key/Related rows from `s6-authored-ledger.jsonl` when it
converts each home page** (it receives the ledger as input per R11 anyway; add to the S7 handoff).
R11's partition/close check gains an owed-homes accounting so no row silently drops. Rationale:
single-writer (S7 owns doctrine-page bodies), zero merge debt vs. transitional sub-tables, and the
S6→S7 window is pre-publish (execute branch; S9 gates release) so no reader ever sees the interim
unlinked state. This amends R8's atomic output list transitionally — recorded here + JOURNAL.

## E4 — 80/148 stubs missing citations: enrichment run BEFORE waves
SD10 stubs are identity-only by design; `citations` come from `cluster.citations[]` (one cluster
fetch per row, HTTP-cache-likely). Work order `S2-ENRICH-CITATIONS-WORKORDER.md`: a bounded
`--enrich-citations` ingest.py surface + a paced serial-lane run over exactly the 80 worklist
record_ids (~80–160 calls, ≪1% envelope). Waves start after it lands; W1–W8 order unchanged.

## Deferred (journaled, non-blocking)
- `verified_off_cl` born-status override dropping `off_cl_links` — no off-CL row exists in the
  148; fix rides the next s6 touch or before any A17 page routes through R8.
- Grouped Key sub-table selection — moot at S6 (homes writes removed); becomes S7 materialization
  guidance.
- R6 schema-3 Case Index flip — owed at S7/S8 with the generator change; tracked in S7 handoff.
