# CodeRabbit gate S6-R8PIPE — fix report (2026-07-07)

Lane: s6 builder (`claude-opus-4-8`). Source findings: `_run/gates/S6-R8PIPE-coderabbit-da8adb3.md`
(18 findings), dispositions `_run/o2-execute/CR-S6R8PIPE-ADJUDICATION.md`. My scope: CR-01, CR-02,
CR-04..CR-14, CR-16..CR-18 (CR-03 ingest.py + CR-15 serializer.py = recovery lane, untouched).

**Result: 14 fixed + regression-tested · 2 deferred (scope conflict, escalated) · 0 declined.**
Constraints held: committed nothing, zero CL, no `content/` / `_overhaul2/lake/` / `R8-WAVE-*`
mutation, no `scripts/s2/` edit.

## Per-finding

| ID | Sev | Status | Fix + evidence |
|----|-----|--------|----------------|
| **CR-01** | major | **FIXED** | `worklist-fixture.json` row 3 `status_checked` `verified_identity`→`not_found` (aligns with its `not_found` stub). Behavior unchanged (mint reads the lake status, not this field); the fixture is now honest. Mint self-test still 37/37. |
| **CR-02** | minor | **FIXED** | Moved the `homes_roles_desync` gate out of the unconditional top of `plan_mint` into the FRESH path only (after the already-authored/crash-tail/wedged classification). New mint self-test `idempotent survives post-authoring worklist desync (CR-02)` passes: an already-authored row with a later-desynced worklist now returns `already_authored` instead of `REFUSE_HOMES_ROLES_DESYNC`. |
| **CR-04** | major | **FIXED** | `lint15_skeleton.check_case` takes `fm` + exempts a `status: draft` case page with zero H2s (S3 R7 placed-stub parity with `check_doctrine`). Fixture `lint-15-case-draft-stub-pass.md` → 0 viol (was a BIRAC violation before). LINT-15 self-test PASS. |
| **CR-05** | major | **FIXED** | `run_all.py:110` `("SELFTEST", …)`→`(lint_name, …)`. `run_all.py` roster now labels the four self-test gate rows `LINT-10/12/13/14` (verified in the summary table) instead of four identical `SELFTEST` rows. |
| **CR-06** | major | **FIXED** | `_common.weight_label_in_cell` now normalizes every dash variant (hyphen/en/em/minus) on both the cell and the lead before matching. Fixture `lint-16-weight-hyphen-fail.md` (a `Binding - SCOTUS` hyphen leak in a Holding cell) → 1 viol (passed silently before). LINT-16 self-test PASS. |
| **CR-07** | major | **FIXED** | `lint24_urls._retired_in` unwraps `[[…]]` wikilink syntax before the retired-segment match. Isolation fixture `lint-24-oldpath-wikilink-fail.md` (ONLY a wikilink-syntax `related:`) → 1 HIGH (missed before). LINT-24 self-test PASS. |
| **CR-08** | major | **FIXED** | `lint13_schema`: added `SUPPORTED_FORMATS` + `schema_formats()`/`unsupported_schema_formats()`, a fail-closed `run()` gate on unknown formats, and `format_matches` unknown→`False`. Self-test: `unknown format fails closed (CR-08) -> OK`; live schema format coverage OK (only date/date-time/uri). |
| **CR-09** | major | **FIXED** | `lint13_schema`: `check_cases_dir()` fails closed on a missing/empty `lake/cases` dir; `run()` returns it before the empty scan reads as 0 violations. Self-test: `missing/empty cases dir fails closed (CR-09) -> OK` (missing→1, empty→1, populated→0). |
| **CR-10** | major | **FIXED** | `lint21_binding.check_binding`: malformed `bound`/`pending` (not lists) → single HIGH (fail-closed, not coerced to `[]`); non-string node ids (and non-dict rows) rejected as HIGH via `_collect_nodes`. Fixtures `lint-21-binding-badstruct-fail.yaml` + `lint-21-binding-nonstring-node-fail.yaml` → HIGH. LINT-21 self-test PASS. |
| **CR-11** | minor | **FIXED** | `lint22_derip._norm` now collapses `[\s\-_]+`→space so a folder-derived label (`probable-cause-exceptions`→`probable cause exceptions`) reconciles with its banned form. Self-test assertion `CR-11 folder-label reconciles -> OK`. |
| **CR-12** | minor | **FIXED** | `lint14_pagerecord.page_record_id`: `None`-only fallback (was `or`); an explicit `record_id: ""` is returned as-is, not masked to the stem. Fixture `lint-14-page-emptyid-fail.md` (+ a valid stem-record in the self-test map) → 2 viol (passed silently before). LINT-14 self-test PASS. |
| **CR-13** | major | **DEFERRED (escalated)** | `scripts/s2/project.py:73` (`date_from_record` today() fallback). See Escalation below. Dormant per adjudication (all lake records carry `date_modified`). Mint unaffected (`promote_record` always stamps `provenance.date_modified` = `--as-of`). |
| **CR-14** | major | **DEFERRED (escalated)** | `scripts/s2/project.py:300` (pre-validate the write loop). See Escalation. Adjudication notes "Mint's single-record path unaffected." |
| **CR-16** | major | **FIXED** | `convert_tables.convert_tables`: a per-row blank Opinion cell (column present) now DEFERS the whole table (`reason: blank-opinion-cell` + `row_lines`), never blank-fills it. Fixture `blank-opinion-cell.md` → `cr16=True` (deferred, table untouched). |
| **CR-17** | major | **FIXED** | `convert_tables.convert_page` offsets every `line`/`row_lines` by `len(prefix)` (frontmatter length). Same fixture: reported `line=10` (the real file line of the header) and `row_lines=[13]` (the blank row). convert_tables self-test PASS. |
| **CR-18** | minor | **FIXED** | `coderabbit_gate.sh`: `case "$CR_GATE_TIMEOUT" in ''|*[!0-9]*|0) … exit 2` after the default, so `0`/non-numeric can't reach `alarm 0` and cancel the timer. Verified: `CR_GATE_TIMEOUT=0` and `=abc` both exit 2 with the guard message; `bash -n` clean. |

## Escalation — CR-13 / CR-14 (scripts/s2/project.py)

The work order's scope names `project.py` (CR-13/14) as mine, but the same paragraph states **"do not
touch `scripts/s2/` at all this session"** (the recovery lane owns scripts/s2/; `ingest.py` + CR-15
`serializer.py` are both `M` in the tree right now). These two directives directly conflict for
`project.py`. Per the standing "escalate rather than guess" rule and the hard prohibition, I **did not
edit `scripts/s2/project.py`** (it is currently unmodified by any lane — I left it that way to avoid a
concurrent-edit hazard with the active recovery lane). Both findings are **dormant** per the
adjudication and non-wave-blocking. **Re-task CR-13/CR-14 once `scripts/s2/` is released by the recovery
lane, or confirm `project.py` is exempt from the prohibition** — the two fixes are:
- CR-13: `date_from_record` should raise (fail-closed) instead of `dt.date.today()` on missing
  `provenance.date_modified` (the exact idempotence break the tool's own `verify_idempotent()` guards).
- CR-14: pre-validate `project_record(record)` for every matched record before any `os.replace`, so a
  bad circuit blocks the batch cleanly instead of a partial mid-loop crash.

## Files touched (this lane only)

Code: `scripts/s6/mint_page.py`, `scripts/s6/fixtures/worklist-fixture.json`,
`scripts/lint/{lint13_schema,lint14_pagerecord,lint15_skeleton,lint21_binding,lint22_derip,lint24_urls,run_all,_common}.py`,
`scripts/s5/convert_tables.py`, `scripts/gates/coderabbit_gate.sh`.
New fixtures: `scripts/lint/fixtures/{lint-15-case-draft-stub-pass.md, lint-16-weight-hyphen-fail.md,
lint-24-oldpath-wikilink-fail.md, lint-21-binding-badstruct-fail.yaml,
lint-21-binding-nonstring-node-fail.yaml, lint-14-page-emptyid-fail.md}`,
`scripts/s5/fixtures/blank-opinion-cell.md`.

*(`_common.py` is also being edited by the recovery lane in a different function (`_scalar`, CR-15
parse-side `{}` support); my CR-06 edit is in `weight_label_in_cell` — no overlap. The `scripts/s2/`
and `_overhaul2/lake/**` changes in the working tree are the recovery/E4 lanes, not this lane. The
`lint-13-record-webcite-*.json` untracked fixtures are the recovery lane's R3 web-cite extension, not
mine.)*

## Test evidence (all green)

- `py_compile` on every touched Python file: OK.
- `bash -n scripts/gates/coderabbit_gate.sh`: OK; `CR_GATE_TIMEOUT=0`/`=abc` → exit 2 (CR-18).
- Per-lint self-tests PASS: LINT-13 (incl. CR-08/09 assertions), LINT-14 (CR-12 emptyid → 2 viol),
  LINT-15 (CR-04 draft-stub → 0 viol), LINT-16 (CR-06 hyphen leak → 1 viol), LINT-21 (CR-10 badstruct +
  non-string node → HIGH), LINT-22 (CR-11 reconcile → OK), LINT-24 (CR-07 wikilink-only → HIGH).
- `convert_tables --self-test`: PASS incl. `blank-opinion-cell.md -> cr16=True cr17_line=10 row_lines=[13]`.
- `scripts/s6/mint_page.py --self-test`: **37/37 PASS** (+1 CR-02 regression); `--specimen-test`: PASS.
- `scripts/lint/run_all.py --quiet`: completes; self-test gate rows now read `LINT-10/12/13/14`
  (CR-05), all 0-violation; corpus red state unchanged (pre-overhaul, not this lane's).
