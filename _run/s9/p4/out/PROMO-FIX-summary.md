# PROMO-FIX — P4 fix packet summary (RULINGS P4-10 + P4-11)

**Lane:** `{lane: PROMO-FIX, model: claude-opus-4-8}` · **Date:** 2026-07-21 · **Branch:** overhaul2/execute
**Authority:** P4-WORKER-BRIEF.md; RULING P4-10 (under_review promotion adjudication); RULING P4-11
(new frontier stubs). Registry read-only (substantiate-from-lake, P3 convention) — no registry edits.

## Deterministic coverage accounting

| Stage | Assigned | Done | Skipped | Notes |
|---|---|---|---|---|
| 1 Promotions | 30 records | 29 flipped `verified_identity` + 1 alias annotated | 0 | field_i unchanged per existing derivation |
| 2 Pin harvest | 4 pin-demanding findings (11 records) | 12 pins harvested, 0 needs_cl | 18 findings demanded no pins | all cache-present |
| 3 Loop-3 | 22 directives | 22 FIXED | 0 NOT-FIXED | apply_fixes queue_outstanding=0 |
| 4 New stubs | 4 stubs + 3 LCD surfaces | 4 created + 3 pages edited | 0 | frontier-stub depth |
| 5 Escalation doc | 1 | resolution block appended | 0 | history preserved |

## Stage 1 — promotions (30 records)
- **29 primary** `under_review -> verified_identity`, each with a `provenance.promotion` block and a
  scope_note good-law-basis line. Identity source recorded per record:
  - Builder-lane batch (20): Horton, Rideau, Nieves, Gonzalez v. Trevino, Kolender, Timbs,
    Bajakajian, Culley, Sorrells, Keith, Imbler, Rehberg, Buckley, Briscoe, Burdeau, Verdugo,
    Egbert, Weeks, Nora, Al-Azzawy.
  - Orchestrator Claude-MCP lane / 429 spillover (8): Vaneaton, Riley, Thompson, Chiaverini,
    Heien, Austin, Youngblood, GM Leasing.
  - Reuse of 2026-07-20 marker poll (1): Chatrie (canonical).
- **Chatrie folded-alias** annotated; status unchanged.
- Breadth-marked (field_i unverified, identity-only): Youngblood, GM Leasing, Nieves, Gonzalez
  (currency stubs); Rideau, Nora, Al-Azzawy, Vaneaton (split-position authorities).
- Case-specific good-law notes: Egbert (contracts Bivens), Keith (FISA codified), Sorrells
  (entrapment foundation, qualified by Mathews line).
- **Cite-selector (P4-10):** Heien official set to CL-verified `135 S. Ct. 530`, `574 U.S. 54`
  whitelisted (kept on page surface); Riley already `134 S. Ct. 2473` (confirmed).
- **Youngblood date-class fix:** `date_decided 1989-01-23 -> 1988-11-29`, `year 1989 -> 1988`.

## Stage 2 — pin harvest (12 pins / 11 records / 0 needs_cl)
Star-verified (U.S.-Reports star matches record official): **Imbler *431**, **Briscoe *328**,
**Buckley *274**, **Austin *604**, **Bajakajian *334**.
Slip-only (0-star opinion, S.Ct.-reporter star ≠ U.S. official, or slip page-proof):
Rehberg, Timbs, Thompson, Chiaverini (page-proof "Page Proof Pending Publication" watermark +
one soft-wrap hyphen normalized), Nieves (rule + comparator), Gonzalez. All quotes verbatim from
`~/cssi-lake/cache/text/<lead_opinion_id>.txt`.

## Stage 3 — loop-3 (22/22 FIXED)
All 22 stored fix directives re-ran mechanically to FIXED. No new judgment. `apply_fixes.py`
reports applied=22, rejected=0, **queue_outstanding=0**. No registry edits; no content-prose edits
required by the 22 (Heien page kept 574 U.S. 54; Brady/Curtilage pages already accurate).

## Stage 4 — new frontier stubs (P4-11) + LCD edits
Stubs (Holcomb shape; status verified_identity, stub true, treatment unverified, citations empty/
slip-pending, P4-11 holding line in scope_note):
- `united-states-v-lowers--10807484` (4th Cir. 2026-03-10, docket 24-4546, lead 11274223)
- `united-states-v-brillhart--10925245` (11th Cir. 2026-07-09, docket 24-13226, lead 11392782)
- `united-states-v-eric-johnson--10648997` (4th Cir. 2025-08-05, docket 23-4255, lead 11115584)
- `united-states-v-wilson--10636220` (5th Cir. 2025-07-17, docket 23-30777, lead 11102807)

LCD content edits (plain-italic brief-mentions, CL opinion links, no page-less wikilinks; S1 A8
weight labels):
- **Private and Foreign Searches.md** — hash-split: Lowers (4th, strict) + Brillhart (11th,
  permissive) joined; summary updated; "The Supreme Court has not resolved it" kept; provenance
  comment + Sources entries added.
- **Curtilage.md** — Eric Johnson (4th Cir.) added beside May-Shaw as the federal multi-unit
  "no-curtilage" data point; Whitaker absent from corpus → cited alone with a lower-court split
  note; provenance comment added.
- **Terry Stops and Reasonable Suspicion.md** — Wilson (5th Cir., post-Bruen) added to the
  frisk-branch split; summary updated; provenance comment (distinguishes 9th Cir. Luke Wilson).

## Files touched (absolute paths)

### Lake records — 29 primary promotions
```
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Horton v. California.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/United States v. Rideau.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Nieves v. Bartlett.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Gonzalez v. Trevino.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Kolender v. Lawson.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Timbs v. Indiana.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/United States v. Bajakajian.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Culley v. Marshall.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Sorrells v. United States.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/United States v. United States District Court (Keith).json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Imbler v. Pachtman.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Rehberg v. Paulk.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Buckley v. Fitzsimmons.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Briscoe v. LaHue.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Burdeau v. McDowell.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/United States v. Verdugo-Urquidez.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Egbert v. Boule.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Weeks v. United States.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/United States v. Nora.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/United States v. Al-Azzawy.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/United States v. Vaneaton.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Riley v. California.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Thompson v. Clark.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Chiaverini v. City of Napoleon.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Heien v. North Carolina.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Austin v. United States.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Arizona v. Youngblood.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/G. M. Leasing Corp. v. United States.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/Chatrie v. United States.json
```
### Lake records — alias + 4 new stubs
```
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/united-states-v-chatrie--10881683.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/united-states-v-lowers--10807484.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/united-states-v-brillhart--10925245.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/united-states-v-eric-johnson--10648997.json
/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases/united-states-v-wilson--10636220.json
```
### Content pages (3)
```
/Users/johngalt/Projects/cssi-quartz/content/searches/Private and Foreign Searches.md
/Users/johngalt/Projects/cssi-quartz/content/searches/Curtilage.md
/Users/johngalt/Projects/cssi-quartz/content/seizures/Terry Stops and Reasonable Suspicion.md
```
### Ledger + artifacts
```
/Users/johngalt/Projects/cssi-quartz/_run/s9/fixes.jsonl                       (22 loop-3 FIXED rows appended)
/Users/johngalt/Projects/cssi-quartz/_run/s9/p4/out/PROMO-FIX-loop3.jsonl      (the 22 rows, source)
/Users/johngalt/Projects/cssi-quartz/_run/s9/p4/out/PROMO-FIX-needscl.jsonl    (empty — 0 needs_cl)
/Users/johngalt/Projects/cssi-quartz/_run/s9/p4/out/PROMO-FIX-summary.md       (this file)
/Users/johngalt/Projects/cssi-quartz/_review-needed/s9-p3-underreview-promotions.md  (resolution block)
```

## Loop-2 — schema remediation (non-author lint verification, coordinator-flagged)

Non-author LINT-13/12 verification found my loop-1 lake edits used unsanctioned schema homes.
Root cause: `_overhaul2/lake/_schema.json` makes `provenance` and `field_provenance` both
`additionalProperties:false`; `field_provenance` permits EXACTLY four fixed keys
(`identity`, `treatment.field_i_validity`, `point_overrides`, `pinpoints`), each exactly
`{src,at,verifier}` (verified against Katz's clean record + the schema). The coordinator's
suggested `field_provenance["status"]` / dotted-key homes would themselves be new LINT-13 highs;
I used the coordinator's alternative sanctioned home, `provenance.warnings[]` (array of strings),
plus `treatment.scope_note` (already carried the good-law basis).

| LINT | class | files | before → after | fix |
|---|---|---|---|---|
| 13 | `provenance.promotion` unsanctioned | 30 | 30 → 0 | key deleted; evidence → `provenance.warnings[]` + scope_note kept |
| 13 | `field_provenance.pinpoints` extra `note` | 3 | 3 → 0 | note folded into `src`; key removed |
| 13 | dotted `identity.date_decided` | 1 | 1 → 0 | removed; date-correction → `warnings[]` |
| 13 | `citations.whitelisted_parallels` | 1 | 1 → 0 | deleted; `574 U.S. 54` → `citations.parallel`+`all`; basis → source/`warnings[]` |
| 13 | stubs missing `point_overrides` | 4 | 4 → 0 | added `field_provenance.point_overrides` |
| 13 | `pinpoints[].notes` (FIX-A3567) | 4 recs / 6 pins | 6 → 0 | notes → `warnings[]` (coordinator directive, cross-packet) |
| 12 | reprojection drift (status+scope_note) | 29 | 35 → 6 | `project.py --write`; projected-fields-only, 0 out-of-frontmatter hunks |

**Verify (after):** `python3 scripts/lint/lint13_schema.py` → **0 highs** (whole lake);
`python3 scripts/lint/lint12_drift.py` → **6 highs**, all pre-existing non-PROMO-FIX
(Arizona v. Roberson serializer FP + 5 FIX-A1 escalations: Arkansas v. Sanders, Frank v. Maryland,
Gouled, Kalkines, Trent — left untouched; re-projecting them would regress Wave-B corrections).
Loop-2 rows: `_run/s9/p4/out/PROMO-FIX-loop2.jsonl`. All lake records still parse (0 failures).

**Deviation flagged for the machine:** the coordinator's step-(1)/(2)/(3) `field_provenance["status"]`,
`["pinpoints.<id>"]`, `["citations.parallel"]` keys are NOT schema-legal under the committed
`_schema.json` (Katz proves only the four fixed keys pass). I met the coordinator's actual goal
(0 LINT-13 highs, evidence preserved) via the schema-legal `provenance.warnings[]` + `citations.parallel`
homes it also named. Heien frontmatter now projects the P4-10 official (`135 S. Ct. 530`) with
`574 U.S. 54` in `parallel_cite`; the page prose keeps `574 U.S. 54` — the ruling-sanctioned
lake/prose cite divergence, not drift.

## Residue / notes for the machine (non-author re-review owed)
- Registry unchanged by design; the 15 registry findings resolve because their blocking lake
  records are now `verified_identity` with documented good-law basis (substantiate-from-lake).
- P4-10 chose `verified_identity` (not `verified`) as the promotion status; the loop-1 authors had
  named `verified`. Treated as ruling-governed and mechanical. If a downstream gate distinguishes
  the two status values, that is an orchestrator/gate call outside this packet's mechanical scope.
- Heien: lake official = 135 S. Ct. 530; page surface = 574 U.S. 54 (whitelisted). Deliberate
  lake/page reporter divergence per P4-10 cite-selector, documented in
  `citations.whitelisted_parallels`.
- Pin star/slip choice: modern-reporter star pages (Nieves, Timbs) recorded slip-only to avoid a
  U.S.-vs-S.Ct. reporter mismatch under the record's U.S.-Reports official cite.
```
