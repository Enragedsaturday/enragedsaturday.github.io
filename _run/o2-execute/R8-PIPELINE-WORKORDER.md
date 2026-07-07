# Builder work order — R8 authoring pipeline CLI (S6 SD3), 2026-07-07

The R8 worklist is signed (`_run/o2-execute/R8-WORKLIST.json`, 148 pages; commit d28e200).
No promotion CLI exists yet. This session BUILDS the pipeline tooling only — **zero page
authoring, zero CL calls, commit nothing** (the orchestrator commits at the gate). Repo:
`/Users/johngalt/Projects/cssi-quartz`, branch `overhaul2/execute`, start from HEAD.

## What R8 requires (spec: `_overhaul2/specs/S6-coverage-ingest.spec.md` R8; read it first)

Input: a `verified_identity` stub + home node(s) + role(s) — i.e. one R8-WORKLIST row plus an
authored page body produced by a wave author agent. Output, **atomically**:
1. A BIRAC page in `content/cases/` in the **S5 R3 skeleton** (S5 spec R3: exact H2 order
   `Background → Issue → Rule → Application → Conclusion → Treatment & subsequent history →
   Appears on → Sources`), projected frontmatter shape, tables per **R6 schemas** (exact header
   strings; no authored data in lake-owned cells — R7 boundary; the R5 point-status table is the
   one carve-out), **R12 bracketed Sources**, `opinion` anchor text everywhere, pins per R16,
   born **`lake.status: draft`** (R15 banner renders from that status — no banner text authored).
2. The **stub→record promotion** per S2 spec **A6**: rename `_overhaul2/lake/cases/<record_id>.json`
   → `<page filename stem>.json`, update `record_id` to the stem, drop `stub: true`, write the
   **manifest rename entry** (`_manifest.json`), journal the promotion — atomic with the page write.
3. A **Case-Index row** (`content/legal-system-research-and-reference/Case Index.md`, R6 schema 3,
   alphabetical placement).
4. A **Key cases / Related row on each `homes[]` page** per the row's `roles[]` (R6 schema 1 for
   Key, schema 2 for Related; self-reference ban; Relevance cells open with the bolded 1–2-word tag).
5. A **ledger `authored` row** appended to `_run/o2-execute/s6-authored-ledger.jsonl` (one JSONL row
   per page: record_id before/after, caption, leg, prong, basis, homes/roles, page path, lints-run,
   timestamp arg — see Determinism below). R11 folds this into `_run/s6-coverage-ledger.json` later.

## Deliverables

**`scripts/s6/` (new package)** — a promotion/mint CLI (name it; e.g. `mint_page.py`) styled on
`scripts/s2/project.py` + `ingest.py` conventions (dry-run default, `--write` guarded, journaled,
fixtured, self-tested). Reuse `scripts/s2/serializer.py` / `project.py` machinery for frontmatter
projection — do NOT reimplement projection; if a small refactor is needed to expose it, keep it
surgical and covered by the existing s2 self-tests.

### CLI contract
- `--row <record_id>` — looks the row up in R8-WORKLIST.json (ground truth for homes/roles/aliases/
  special/basis). Refuse rows absent from the worklist; refuse rows whose manifest status is not
  `verified_identity` (or `verified` — see Wyman/GM-Leasing/Verdugo re-key-gated note in
  packetb-dispositions.jsonl; report which statuses you actually accept and why).
- `--payload <path>` — the authored page body (everything below the frontmatter; the author agent
  writes it to a scratch file). The CLI **validates before writing anything**:
  - exact S5 R3 H2 sequence (optional sections may be absent per LINT-15's case half — mirror its
    logic, or better, invoke it);
  - every Case-column table matches a sanctioned R6 header exactly; Case-cell format
    `*[[Case Name]]*, <cite> (<year>)`; anchor text `opinion`;
  - bracketed Sources per R12; header line per R3 (degraded plain-text form);
  - no self-referential Related row.
- Page filename stem: the caption (match existing `content/cases/` naming); collisions →
  year/court disambiguation per R9 — **the standing exhibit is `United States v. Smith (2024)`**.
  A6 invariant: no page stem contains `--`.
- `aliases:` frontmatter from the worklist row's `aliases[]`.
- **History-cluster pages** (user D2: Sanders, Trupiano, Frank v. Maryland, Robbins, Quantity of
  Books): support the history rendering per PRACTICES §7 (precise verb, forward-pointer to the
  successor, visual demotion) — the payload authors it; the CLI verifies the treatment/status class
  coming from the lake record is a history class and does not fight the banner.
- **Atomicity + rollback:** stage all writes (page, lake rename, manifest, Case Index, homes pages,
  ledger row), run LINT-15/16 (and LINT-14 page↔record) against the staged state, then commit all
  or roll back all. A failed lint = no partial writes, non-zero exit, machine-readable reason.
- **Idempotent/resumable:** re-running an already-promoted row is a clean no-op (detect via
  manifest rename entry + existing page), reported as `already-authored`. The waves must be
  resumable mid-batch.
- **Determinism:** no wall-clock reads for journaled values without an explicit `--as-of` arg
  (follow the s2 journal conventions).
- **Zero CL calls** — this CLI is offline; the author agent owns the serial CL lane.

### Conformance specimen
`United States v. Smith (2024)` (page `content/cases/United States v. Smith (2024).md` + lake
record of the same stem, `verified`, `stub: false`) is the born-conformant exhibit. Add a
**specimen self-test**: run the payload-validator over the Smith page body and the projector over
its lake record; both must pass byte-stable (modulo the known verified-vs-draft status delta).
Fixtures: synthesize a fake stub + payload pair (fixtures dir, no real-lake mutation in tests) and
cover: happy path, lint-fail rollback, collision disambiguation, alias row, history class,
already-authored no-op, worklist-absent refusal, wrong-status refusal.

### Out of scope
- The 58 non-page placements (`R8-NONPAGE-LEDGER.json`) — separate lane, R11 fold.
- LINT-17 (R12 CI lint) — separate work order after the waves.
- Any edit to `_overhaul2/lake/**` outside the promotion rename path; any authored prose.

## Report
`_run/o2-execute/R8-PIPELINE-BUILD-REPORT.md`: file list, CLI surface (flags + exit codes),
design decisions taken where this order left latitude (payload interface details, stem rules,
status-acceptance set), self-test + fixture results, specimen result, and ESCALATIONS (anything
ambiguous — do not guess on spec conflicts; the orchestrator adjudicates). Journal-grade honesty:
report what you did NOT cover.

## Process
Writer≠checker: a separate review lane reads your report + diff before the orchestrator commits;
the spec-completion CodeRabbit gate (RUNBOOK §5 standing amendment) will review `scripts/s6/`
as S6 code deliverables on the standing draft PR #3 lane. Loop cap 3 → `_review-needed/`.
