# FIN-MINI — fix packet summary (RULING P4-13)

Lane `FIN-MINI` · model `claude-opus-4-8` · branch `overhaul2/execute`.
Write-scope honored: `_overhaul2/lake/cases/` (11 named records), `content/cases/` (4 named
pages, frontmatter + `## Appears on` only), `_run/s9/p4/`. No other paths touched.

## Coverage (deterministic)

### P4-13(a) — B4 lake hygiene (varies_by_point flip + synthetic override removal)
- Records assigned: **11**. Records examined: **11**. Records edited: **11**. Skipped: 0.
- Method: `json.load` → set `treatment.varies_by_point=false` and `treatment.point_overrides=[]`
  → re-serialize with `json.dumps(indent=2, ensure_ascii=True) + "\n"`. Exact round-trip was
  pre-verified per file (dump(load(raw))==raw for all 11), so every non-target byte is preserved
  (scope_note, edges, derivation untouched). Per-file unified-diff confirmed the only changed
  lines are the `varies_by_point` flip and the `point_overrides` block collapse.
- 10 records carried one synthetic `legacy-limited-<slug>` override (removed → `[]`); **Gouled**
  already had `point_overrides: []` (varies_by_point flip only, single-line diff). Post-edit shape
  matches the `Smith v. Maryland` sibling (`varies_by_point:false`, `point_overrides:[]`).

  | record | override removed | page re-projected |
  |---|---|---|
  | Boyd v. United States | legacy-limited-boyd-v-united-states | yes |
  | Coolidge v. New Hampshire | legacy-limited-coolidge-v-new-hampshire | yes |
  | Escobedo v. Illinois | legacy-limited-escobedo-v-illinois (3 authorities) | yes |
  | Gouled v. United States | — (already []) | no (already in sync) |
  | Mathis v. United States (1968) | legacy-limited-mathis-v-united-states-1968 | yes |
  | Monroe v. Pape | legacy-limited-monroe-v-pape | yes |
  | Oregon v. Elstad | legacy-limited-oregon-v-elstad | yes |
  | Saucier v. Katz | legacy-limited-saucier-v-katz | yes |
  | Thornton v. United States | legacy-limited-thornton-v-united-states | yes |
  | United States v. Agurs | legacy-limited-united-states-v-agurs | yes |
  | United States v. Chadwick | legacy-limited-united-states-v-chadwick | yes |

  Disambiguation applied: "Mathis 1968" = `Mathis v. United States (1968).json` (NOT
  `United States v. Mathis.json`); "Saucier v. Katz" = `Saucier v. Katz.json` (NOT
  `Katz v. United States.json`). Both look-alikes left untouched.

- Re-projection: `scripts/s2/project.py` over the 11 pages. Dry-run first —
  `field_counts = {treatment.point_overrides: 10, treatment.varies_by_point: 10}` (limited to
  treatment fields, no other managed field touched), gate `ok_to_project: true`, `pages_changed: 10`
  (Gouled absent — page already matched lake). Then `--write`: 10 pages rewritten. Idempotence
  re-check: 2nd dry-run `pages_changed: 0`.

### P4-13(b) — B5 placement (narrow unrendered KEY homes + hygiene sync)
- Pages assigned: **4**. Edited: **4**. Skipped: 0. Surgical frontmatter `homes[]` +
  body `## Appears on` edits only; each page's two surfaces verified in sync (page-list + roles)
  after the edit.
  1. **Moore-Bush** → removed `[[Fourth Amendment Framework]]` (role Key) from `homes[]` and
     `## Appears on`. `related[]` retains it (soft relation, per ruling). Premise verified:
     `Fourth Amendment Framework.md` hosts no roster (`## Key cases` absent; 0 Moore-Bush refs).
  2. **Cortez** → removed `[[Terry Stops and Reasonable Suspicion]]` (Key — Progeny/Refinement);
     kept `[[Reasonable Suspicion]]` (Key — Anchor). Terry Stops page: 0 Cortez refs;
     Reasonable Suspicion page renders Cortez 4× under `## Key cases`.
  3. **Sokolow** → removed `[[Terry Stops and Reasonable Suspicion]]`; kept `[[Reasonable Suspicion]]`.
     Terry Stops page: 0 Sokolow refs; Reasonable Suspicion page renders Sokolow 5×.
  4. **Van Leeuwen** → hygiene sync: restored `[[Seizure of Property]]` (Key — package / mail
     detention) to `## Appears on` (present in `homes[]`, dropped from Appears-on). `homes[]`
     untouched. Seizure of Property page renders Van Leeuwen 6× under `## Key cases`.

## Lint before / after (corpus-wide)

| lint | before (high) | after (high) | delta |
|---|---|---|---|
| LINT-12 (S2 drift) | 6 | 5 | **Gouled row dropped**; no new highs |
| LINT-13 (S2 schema) | 29 | 29 | unchanged; no new highs |

- LINT-12: the Gouled row (`treatment.varies_by_point`, page=false vs lake=true) is RESOLVED by
  the lake flip and drops. The 5 remaining highs are pre-existing drift OUTSIDE this packet's
  scope: `Arizona v. Roberson`, `Arkansas v. Sanders`, `Frank v. Maryland`,
  `Kalkines v. United States`, `United States v. Trent`. None of the 10 re-projected pages drift.
- LINT-13: all 29 highs are the pre-existing `$.pinpoints[*].notes additional property` class;
  none of the 11 FIN-MINI records appear (verified before and after). The new
  `varies_by_point:false` / `point_overrides:[]` shape validates clean (same shape as the
  passing `Smith v. Maryland` record).
- P4-13(b) edits touch `homes[]`/`## Appears on` only — outside the LINT-12 managed subset and the
  LINT-13 lake schema — so they contribute nothing to either count.

## P4-14 — LINT-6 banner-driver third leg (added mid-task)

Write-scope: `scripts/lint/lint6_treatment_status.py` + its fixtures + `_run/s9/p4/`.

- **Root cause:** `_banner_driven()` had only two of `caseHelpers.shouldDraftBanner`'s three legs
  (`draft: true`; `lake.status ∈ {draft, under_review}`). It lacked the third —
  `resolveTreatment().fieldI === "unverified"` (`caseHelpers.ts:326–334`). The 30 promotions
  created the legitimate state `{lake.status: verified_identity, field_i_validity: unverified}`,
  which the component banners via that third leg → **21 false-positive HIGHs** (leg (d)
  "unverified reaches a reader unbannered").
- **Fix (mirror the component exactly):** added `LEGACY_TO_FIELD_I` (= caseHelpers S1 A4 map),
  `_norm_field_i` (= `normFieldI`), `_resolved_field_i` (= `resolveTreatment().fieldI`: projected
  `field_i_validity` normalized, else legacy `status` mapped, unmapped → `unverified`), and a
  third `_banner_driven` leg returning True when the resolved Field-I is `unverified`.
- **Consequence:** leg (d) is now unreachable for a page whose validity *resolves* to the
  `unverified` composite (an unverified page is ALWAYS bannered — correct). Leg (d) survives as a
  belt over legs (a)/(b): a validity that is textually "unverified" but does NOT resolve to that
  composite (malformed/injected) still fails visible.
- **Fixtures:** added `lint-6-verified-identity-unverified-pass.md` (the promotion state → PASS);
  repurposed `lint-6-unverified-unbannered-fail.md` — its old `{verified, unverified}` state is now
  correctly bannered by the component (PASSES), so the negative test moved to the surviving leg-(d)
  case (`field_i_validity: "unverified_stub"` → fails leg (a) out-of-enum + leg (d) unbannered).
- **Self-test:** PASS, 4/4 (`draft-flag-pass`, `minted-underreview-pass`,
  `verified-identity-unverified-pass` all 0 high; `unverified-unbannered-fail` 2 high).

| lint | before | after | delta |
|---|---|---|---|
| LINT-6 high | 21 | 0 | all 21 false positives cleared |
| LINT-6 medium | 7 | 0 | see note |
| LINT-6 low | 0 | 0 | — |

- **Medium note (flagged for the coordinator — the ruling said "no other delta"):** the 7 mediums
  are the "⚪ glyph in a table cell — confirm banner present" rows on
  `Austin v. United States`, `Briscoe v. LaHue`, `Buckley v. Fitzsimmons`,
  `Chiaverini v. City of Napoleon`, `Egbert v. Boule`, `Gonzalez v. Trevino`, `Rehberg v. Paulk` —
  a **strict subset of the same 21** `{verified_identity, unverified}` pages. They drop as the SAME
  correction: `_check_unverified_glyph_in_tables` is gated on `not banner_driven`, and those pages
  are now (correctly) banner-driven, so the "confirm the banner is present" warning is moot (the
  banner IS present). **No page outside the 21 changed**; corpus lint6 total went 28 → 0 with zero
  new violations. This is the same fix's sibling effect, not an unrelated regression.

## Concurrency note (not mine — for the orchestrator)
Working-tree `git diff` at hand-off also shows changes to `Herring v. United States.{json,md}`,
`Peters v. New York.md`, `Case Index.md`, and three exclusionary-rule surfaces. These are
CONCURRENT fleet-worker writes (e.g. B45's Peters→Terry-Stops fix is already in
`out/B45-fixes.jsonl`; a `herring_apply.py` ran mid-session). FIN-MINI did NOT author them and
left them untouched. FIN-MINI's authored surface is exactly: 11 lake records + 10 re-projected
case pages (Gouled page unchanged) + 4 P4-13(b) pages.

## Outputs
- `_run/s9/p4/out/FIN-MINI-fixes.jsonl` — 16 rows (11 × P4-13a, 4 × P4-13b, 1 × P4-14
  `lint6-banner-leg`), schema `s9.fix.v1`.
- `_run/s9/p4/out/FIN-MINI-summary.md` — this file.
- P4-14 authored files: `scripts/lint/lint6_treatment_status.py`,
  `scripts/lint/fixtures/lint-6-verified-identity-unverified-pass.md` (new),
  `scripts/lint/fixtures/lint-6-unverified-unbannered-fail.md` (repurposed).
