# P5-DATES summary — LINT-6 dual-date null-token precision fix + 7-page backfill

Lane **P5-DATES** · model **claude-opus-4-8** · 2026-07-22 · **no live CL** (lake/cache/page evidence only).
Resolves the single DISCREPANCY in `_run/s9/p5/P5-R14B-summary.md` (LINT-6 dual-date guarantee).
WRITE-SCOPE honored: `scripts/lint/lint6_treatment_status.py`, `scripts/lint/_common.py`, fixtures, the 7 named lake records + content pages, `_run/s9/p5/`.

Outputs: `_run/s9/p5/P5-DATES-fixes.jsonl` (16 rows).

---

## (1) LINT-6 precision fix

**Root cause (confirmed).** `_common.split_frontmatter` (stdlib YAML subset) parses `as_of_content: null` as the STRING `"null"`, which is non-blank. LINT-6's `_check_new_schema` dual-date sub-check used `_blank`, so the `null` placeholder passed the R3 non-blank requirement — a false green over 159 pages carrying a literal `null` date token.

**Fix (cleanest layer = shared helper + local date predicate).**
- `_common.py`: added `NULL_TOKENS = {"null","none","~",""}` + `is_null_token(v)` — one shared home for the null spellings, mirroring the lint1 P5 `opinion_id`/`opinion_url` guard (lint1 left untouched — out of scope; it keeps its inline copy).
- `lint6`: added `_blank_date(v) = _blank(v) or c.is_null_token(v)`; the two R3 date sub-checks now use `_blank_date`, and — critically — fire **only when `not banner_driven`**. A banner-driven page (`draft: true` / `lake.status ∈ {draft, under_review}` / validity resolving to `unverified`) legitimately DEFERS currency dates to S6 behind the ⚪ banner, so a null/blank date there is by-design. Docstring (a) updated to state the reader-facing scoping + null-token folding.

**Scoping is exact (census, reproducible).** 159 lake-projected pages carry a null/blank `as_of` date: **152 banner-driven (131 `under_review` + 21 `verified_identity`) — exempt** · **7 unbannered `verified`/`good_law` — must fire**. This reproduces the R14-B breakdown precisely. Tightened LINT-6 fired exactly 7 HIGH (all `as_of_content`) pre-backfill; 0 on the 152 bannered.

**Fixtures (self-tests green, 6/6).**
- `lint-6-null-date-content-fail.md` — unbannered `verified`/`good_law` page, `as_of_content: null` → 1 HIGH (the R14-B negative control the check was missing).
- `lint-6-null-date-bannered-pass.md` — `under_review` page, both dates null → 0 HIGH (locks the banner-driven deferral so a future over-tighten regresses the test).

## (2) The 7 unbannered pages — where the null lived + resolution

**Where the null lived: the LAKE record itself** (not just a stale projection). Every one of the 7 records carried `treatment.as_of_content: null` with a real `treatment.as_of_treatment: 2026-06-30`, `field_i_validity: good_law`, `status: verified`, `composite_basis: migration-seed`. Each record's own evidence carries the content-verification anchor at `identity.date_decided` (top-level `date_decided` is null in these records; the date lives under `identity`).

**Convention applied (Buie precedent).** `Maryland v. Buie` — a `verified` / `migration-seed` record — sets `as_of_content == identity.date_decided (1990-02-28)`. `Arizona v. Youngblood` (`verified_identity` / `composite_basis: unverified`) carries both dates null — i.e. the bannered/deferred class, confirming the exemption. So for the 7 `verified`/`migration-seed` records the correct backfill is `as_of_content := identity.date_decided`.

**Backfill + re-projection (deterministic 7/7).**

| Record | identity.date_decided → as_of_content | page date_decided (agrees) |
|---|---|---|
| United States v. Karo | 1984-09-18 | 1984-09-18 |
| County of Riverside v. McLaughlin | 1991-05-20 | 1991-05-20 |
| United States v. Conner | 1997-10-08 | 1997-10-08 |
| United States v. Mathis | 2014-09-24 | 2014-09-24 |
| United States v. Basher | 2011-01-20 | 2011-01-20 |
| Florida v. Riley | 1989-04-03 | 1989-04-03 |
| United States v. Leary | 1988-05-02 | 1988-05-02 |

- Lake: set `treatment.as_of_content` + appended a `provenance.warnings` entry per record citing the P5-DATES packet and the R14-B discrepancy. Diffs are exactly 2 lines/record (as_of_content + warning); JSON round-trip byte-identical (indent=2, ensure_ascii=False), no reformatting.
- Pages: re-projected via `scripts/s2/project.py --write` scoped to the 7. Projector dry-run reported the ONLY differing field as `treatment.as_of_content` (7/7); each page diff is a single line (`as_of_content: null` → bare date). No other frontmatter/body change.

**No other pages touched.** The 131 `under_review` + 21 `verified_identity` nulls are design-consistent (bannered, dates deferred) and are exempt via `not banner_driven`; post-fix census confirms 0 unbannered null-date pages remain and all 152 bannered null-date pages still pass.

## (3) Verification

| Check | Result |
|---|---|
| LINT-6 corpus-wide (tightened) | **0 high** (was 7 pre-backfill) |
| LINT-6 self-test | PASS (6/6 fixtures) |
| LINT-12 drift corpus-wide | 0 (green) — proves pages == lake projection post-backfill |
| LINT-12 self-test | PASS |
| LINT-13 schema corpus-wide + self-test | 0 / PASS |
| serializer / project.py self-tests | PASS |
| Full non-CL roster (run_all, LINT-2..30) | **0 HIGH** corpus-wide, exit 0 (884 medium / 11 low pre-existing, unrelated) |

## Coverage accounting
- LINT-6 code fix: 1 (files: `_common.py` + `lint6_treatment_status.py`). Fixtures added: 2 (1 fail / 1 pass).
- Lake records backfilled: assigned 7 / done 7 / skipped 0.
- Content pages re-projected: assigned 7 / done 7 / skipped 0.
- Bannered exemption verified: 152 / 152 pass (0 false fires).
- Total fix rows emitted: 16 (`P5-DATES-fixes.jsonl`).

## Note for the orchestrator (not my write)
`_run/s9/p5/lint1-ledger.json` shows as modified in `git status` but is the **concurrent LINT-1 serial-CL sibling lane's** ledger (session-start snapshot was clean; the file grew mid-session with new CL-identity rows incl. HIGH mismatches for Alasaad/Alvarez). No script under `scripts/` writes it, and I never invoked LINT-1. Left untouched per lane-isolation; flagged here only so the diff is not mistaken for P5-DATES output.
