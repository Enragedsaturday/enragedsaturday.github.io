# RETRO-W0W1 work order — CodeRabbit retro gates over pre-gate code (2026-07-05)

Provenance: RUNBOOK §5 amendment #2(d). Four scoped runs (artifacts in `_run/gates/`, CLI 0.6.4):
`scripts/lint` (19 findings: 2 critical · 10 major · 7 minor) · `quartz` (1 major · 4 minor) ·
`scripts/s5` (1 critical · 1 minor) · `scripts/gates` (5 major). **31 total.** Orchestrator-grade
adjudication (Fable side-session): the three criticals + the lint16 security major
**CONFIRMED by code-reading**; `scripts/gates` findings fixed in-session (4 applied, 1 refuted);
the rest are **PLAUSIBLE — fix lane verifies each against code before applying** (standard
find→adjudicate→fix; CodeRabbit's proposed patches are suggestions, never apply blind).

## Dispatch A — lint roster (o2-opus-xhigh lint lane; HIGHEST priority: these lints are the
## fail-closed CI substrate S9 will trust)

CONFIRMED critical:
1. `lint21_binding.py:136-145` — a `bound[]` row with missing/empty `nodes` registers its slug in
   `slug_map` with an empty list; `if slug in slug_map` then treats the override as bound with
   ZERO nodes. Fix: `if slug_map.get(slug)`. Add a fixture (empty-nodes row → HIGH).
2. `lint21_binding.py:74-78` — `except (OSError, ValueError): continue` silently drops corrupt/
   unreadable lake case files from the override scan (fail-open). Fix: collect and surface as
   HIGH violations. Also close the unclosed file handle (same lines, separate major).

CONFIRMED major (security): 3. `lint16_casetables.py:83-94` — `_host()` regex + `.split(":")[0]`
is bypassed by URL userinfo (`https://good.com:x@evil.com/` → returns `good.com`). Fix with
`urllib.parse.urlsplit().hostname` + scheme check. Companion major: short rows / hostless
`https:///` URLs skip the whitelist checks — flag as violations.

PLAUSIBLE major (verify then fix): lint18 empty/missing content tree passes (fail-open) ·
lint18 paths outside content_root miscounted (minor) · lint19 `cases/*` exemption over-broad
(spec exempts only `cases/index.md`) · lint19 table rows count as prose (minor) · lint22
BANNED_TITLES missing the slash-combined originals · lint24 all-non-string `paths` inventory
passes clean (fail-open) · lint25 corrupt deck JSON silently excluded (fail-open) · lint20
malformed `also_on` skipped silently · lint4 lane (b) `_table_rows()` lacks the fenced-block
guard · lint26 `_index` suffix handling diverges from Quartz `slugifyFilePath` (minor) · lint7
UnicodeDecodeError escapes the OSError guard (minor). Docs: run_all.py docstring + README row
omit LINT-18..25; lint-3-n5 fixture Sources incomplete (minors).

## Dispatch B — S5 converter (before its corpus-wide run in Wave 2/3)

CONFIRMED critical: `convert_tables.py:514-565` — `sys.exit(0)` unconditionally; per-page
exceptions and zero-file globs report success. Fix: exit 2 on empty page set, exit 1 if any
per-page error; count and print `n_errors`. Minor: `dropped_columns` under-reports (only
weight/treatment/year recorded).

## Dispatch C — quartz (S4 lane; small)

Major (a11y): `casetable.scss` — the now-interactive `a.casetable-pill` has `:hover` but no
`:focus-visible`; add the outline rule (keyboard users get no focus indicator). Minors: two
stylelint nits (bare `//` empty comments, `currentColor` casing), and a `decodeURIComponent`
guard in `spa.inline.ts` flashTargetBlock (malformed hash throws after preventDefault on the
same-page click path — wrap in try/catch).

## Dispatch D — scripts/gates: DONE in-session (no action)

Applied: bounded+fallback LOG_DIR mkdir · fail-count state sanitized · timeout env validation
(reset-to-default + WARN, not exit) · SPEC filename sanitizer in coderabbit_gate.sh.
REFUTED: "exit non-zero on failure" — the always-exit-0 fail-soft contract is the adversarially
reviewed design (a session gate must never be blocked by checkpoint failure); the failure signal
is the WARN lines + the 2-strike CHECKPOINT-ESCALATE line, which the orchestrator journals and
push-notifies on.

## Acceptance

Per dispatch: fixes land with fixtures reproducing each confirmed defect (fail-open cases must
have a red fixture before the fix and green after); lint self-test suite green; no lint's
violation vocabulary changes (S9 reads it); the S5 converter re-run on its fixture set
byte-identical except exit codes. Journal per the run ledger; this order closes when all four
dispatches are journaled done or refuted-with-rationale.
