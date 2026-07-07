# Wave work order — R8 authoring batches W1–W8(+W9 tail) (2026-07-07)

Standing per-batch order for the R8 authoring waves. Batch membership is EXACTLY
`_run/o2-execute/R8-WAVE-PLAN.json` (Σ=148, R10 step-5 order); the signed row data is
`_run/o2-execute/R8-WORKLIST.json` (homes/roles/prong/basis/aliases/special/note — ground truth).
Repo `/Users/johngalt/Projects/cssi-quartz`, branch `overhaul2/execute`; **commit nothing**
(orchestrator commits at each batch gate). One batch = one agent session, resumable.

## Read first (every batch agent)
- `_overhaul2/specs/S6-coverage-ingest.spec.md` R8 (+ the transitional amendment in
  `_run/o2-execute/R8-PIPELINE-ADJUDICATION.md` E2/E3 — NO Case-Index/homes writes; the CLI +
  per-batch index regen own that) and `_overhaul2/specs/S5-entry-models.spec.md` R1/R3/R4/R5/R6/
  R12/R15/R16 (the page standard).
- `_overhaul2/PRACTICES.md` §2 (treatment vocabulary), §3 (10-gate verification G-protocol),
  §6 (AI guardrails G1–G10), §7 (reader signaling; history rendering for `special:
  history-render` rows).
- The specimen: `content/cases/United States v. Smith (2024).md` — match its register exactly
  (instructor-grade, brief-first, no filler).
- Per-row verdict context: `_run/s6-*.md` + `_run/o2-execute/DISPOSITIONS-2026-07-06.md` +
  `_run/o2-execute/packetb-dispositions.jsonl` (packet-B rows) + `_run/o2-execute/gap-docket`
  artifacts (GAP rows) + the worklist row's own `note`.

## Per row (serial; CL discipline is absolute)
1. Load the lake record (`_overhaul2/lake/cases/<record_id>.json`) — identity + citations are
   pre-verified; do NOT re-run identity. If `citations.display` is empty → SKIP the row with a
   journaled `deferred-recovery` note in the batch report (recovery lane owns it; tail batch W9
   mints it). Never guess a cite.
2. Read the opinion through the CourtListener MCP tools (`read_document`/`search_document` on the
   record's `lead_opinion_id`; cached reads are free) — quotes must be VERBATIM from CL text with
   **[Amended 2026-07-07, W1 lesson]** MCP `read_document` reads `html_with_citations` and is
   BLIND to opinions whose text lives only in `plain_text` (the W1 Gutierrez false-skip). If a
   read returns empty/no text, do NOT skip yet: check the cluster's sibling opinions, then the
   `plain_text` field via the REST method recorded in
   `_run/o2-execute/CONSOLIDATED-REPAIR-REPORT.md` (Gutierrez §task-5). Only after both are empty
   is a `cl-text-unavailable` skip honest. If the MCP CL connection itself is unauthorized in
   your session, STOP and report — do not improvise an alternative CL access path.
   pins per R16 (`^pin-N` anchors in Rule/Application; slip-style where no reporter pagination —
   S2 A3). Single serial lane, pace ≤14/min across the WHOLE batch, 0×429 tolerance; on any
   backoff YIELD and wait — never parallel CL, never relaunch yourself (L4 scar).
3. Author the BIRAC payload to a scratch file: S5 R3 exact H2 order · header line per R3 ·
   R6-conformant tables only · bracketed Sources (R12) · `opinion` anchor text · `holding:` (one
   sentence, JSON-encoded string) + optional `related`/`tags` in the payload frontmatter block per
   the CLI's payload contract (`scripts/s6/mint_page.py --help` + its report §CLI). Role/home
   framing comes from the worklist row; treatment prose is honest to the record's status
   (`under_review` births render the ⚪ banner — do not overclaim verification). `special:
   history-render` rows follow PRACTICES §7 (precise verb, successor pointer, demotion, never
   disguised). `special: caption-trap` rows carry the disambiguation note.
4. Mint: `python3 scripts/s6/mint_page.py --row <record_id> --payload <file> --as-of <ISO-date>
   --write`. The CLI is atomic and fail-closed — on ANY refusal, fix the payload if it's yours or
   ESCALATE in the batch report if it's data; NEVER hand-write the page/lake/manifest/ledger.
   `reconciled`/`already-authored` outcomes: record them and move on.
5. Checkpoint the batch cursor (update the row's status in your batch report file after each
   mint) — resumable mid-batch.

## Batch close
1. Regenerate the Case Index: `python3 scripts/build_case_index.py` (single writer; diff should
   show exactly your new rows).
2. `npx quartz build` must SUCCEED; run `python3 scripts/lint/run_all.py` (or the individual
   lints if run_all has known-red rows owned by S7/S8/S9 — report deltas only: no NEW violations
   attributable to this batch).
3. Update your batch's `status` in `R8-WAVE-PLAN.json` (pending → authored, plus per-row skip
   list). Write `_run/o2-execute/R8-WAVE-<id>-REPORT.md`: per-row outcome (minted/skipped/
   escalated + CL calls used), quote-fidelity self-check note, lint delta, anything ambiguous.
   Final message: compact summary. The orchestrator commits and dispatches the next batch.

## Non-negotiables
Writer≠checker: you self-check (G-protocol) but S9's panel is the certifier — do not mark
anything verified. No CL REST calls outside the MCP tools. No edits outside: new payload scratch
files, the CLI's own atomic writes, Case-Index regen, your batch report, the wave-plan status
field. Ledger/journal rows come only from the CLI.
