# Orchestrator adjudication — CodeRabbit gate S6-R8PIPE @ da8adb3 (2026-07-07)

Artifact: `_run/gates/S6-R8PIPE-coderabbit-da8adb3.md` (18 findings: 13 major / 5 minor). The
`--dir scripts` scope reviewed the whole scripts tree vs main, so most findings land on
PRE-EXISTING, previously-gated code (RETRO/S2-close legs) — a fresh CLI pass cutting deeper.
All 18 adjudicated UPHELD (none refuted); dispositions by owner and urgency:

## This commit's delta — fix now
- **CR-01 `scripts/s6/fixtures/worklist-fixture.json:32` (major):** wrong-status fixture row says
  `verified_identity` while its paired stub is `not_found` — weakens the fail-closed negative
  test. → s6 fix lane.
- **CR-02 `scripts/s6/mint_page.py:744` (minor):** homes/roles desync check runs before the
  already-authored classification — a post-authoring worklist edit breaks the documented
  idempotent no-op. Reorder (desync gate applies to un-minted rows only). → s6 fix lane.
- **CR-03 `scripts/s2/ingest.py:522` (major):** new `parse_circuit` misses CL slugs `cadc`/`cafc`
  (D.C./Federal Circuits drop to None in the enrichment ladder). → RECOVERY lane (owns the file).

## Pre-existing code — upheld, queued to the CR-18 fix lane (before their consumers)
- **CR-04 `lint15_skeleton.py:176` (major):** case-type draft stubs lack the doctrine placed-stub
  exemption. (Mint validates authored payloads, never empty stubs — dormant for waves; fix for
  consistency before S9 CI.)
- **CR-05 `run_all.py:99` (major):** self-test rows hardcode "SELFTEST" instead of lint_name —
  batch-close summaries can't tell which self-test failed.
- **CR-06 `lint/_common.py:647` (major):** `weight_label_in_cell` exact em-dash match — leaked
  labels written with `-`/`–` pass LINT-16. Real FP/FN class in the mint's own validator; fix
  early in the waves.
- **CR-07 `lint24_urls.py:180` (major):** retired-path check misses wikilink-syntax
  homes:/related: values (R13(c) guarantee).
- **CR-08/09 `lint13_schema.py:25/283` (2 major):** unknown `format` values fail OPEN; missing/
  empty lake/cases dir yields silent 0-violations. Both violate the lint's own fail-closed
  mandate. (Note: the recovery lane's R3 schema extension adds an enum source value, not a
  format — no interaction.)
- **CR-10 `lint21_binding.py:139` (major):** malformed binding files coerced to [] — gate can
  pass on broken input.
- **CR-11 `lint22_derip.py:46` (minor):** `_norm` keeps hyphens — folder-derived banned titles
  never match.
- **CR-12 `lint14_pagerecord.py:61` (minor):** empty-string record_id silently falls back to
  filename stem.
- **CR-13 `project.py:73` (major):** `date_from_record` falls back to today() — breaks the
  idempotence contract (dormant: all lake records carry date_modified; fail-closed fix).
- **CR-14 `project.py:300` (major):** corpus write-loop can crash mid-write on a bad circuit
  after the gate passed — pre-validate before any write. (Mint's single-record path unaffected.)
- **CR-15 `serializer.py:202` (minor):** empty dict serializes to bare `key:` → reparses null →
  phantom drift. → RECOVERY lane (amending serializer under R2 anyway).
- **CR-16/17 `convert_tables.py:129/435` (2 major):** blank per-row Opinion cells laundered as
  conformant; reported line numbers off by frontmatter length. **S7-blocking** — must land
  before S7 runs the converter; queued now while warm.
- **CR-18 `gates/coderabbit_gate.sh:33` (minor):** CR_GATE_TIMEOUT=0 disables the alarm.

## Process
CR-01..02 + CR-04..14 + CR-16..18 → one fix work order to the s6 builder lane (mechanical,
fixtured, self-tested; writer≠checker: CodeRabbit found them, builder fixes, orchestrator
spot-checks + the artifact stands as the finding record). CR-03 + CR-15 → recovery-lane addendum.
None block W1 (running): the only wave-facing items are CR-05/06 (batch-close reporting clarity +
a LINT-16 miss class), both landing well before W1 closes.
