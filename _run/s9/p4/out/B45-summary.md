# B45 summary — B4 (missing point-status tables) + B5 (absent-home placement)

**Packet:** B45 (WRITE-SCOPE: `content/` named pages + `_run/s9/p4/`) · **lane/model:** `claude-opus-4-8`
**Outputs:** `out/B45-dispositions.jsonl` (25 rows: 11 B4 + 14 B5), `out/B45-fixes.jsonl` (2 applied), this file.

## Coverage ledger (deterministic)
| metric | value |
|---|---|
| B4 items assigned / examined / skipped | 11 / 11 / 0 |
| B5 unique case→home gaps assigned / examined / skipped | 14 / 14 / 0 |
| B5 raw pair-rows folded in (PAIR-P3 12 + PAIR-P4 13 + PAIR-P1/orch 2) | 27 → 14 unique after dedup |
| content fixes applied | 2 (Scott ADD, Peters narrow) |
| escalations | 8 |

---

## B4 — the 11 "missing point-status table" rows → S5 R5 convention determined, all DISMISS-not-owed

**Convention (from S5-entry-models.spec.md R5 + the two built case-page exemplars).**
R5's point-status table (`| Point of law | Status | Controlling authority |`, "one row per override") is the sanctioned authored rendering of a case whose treatment **genuinely varies by point of law** — a "split case" (R4/R5: composite lead "for split cases", "a simple status lead otherwise"). It is **not** owed on every `varies_by_point:true` page mechanically; it is owed where an override names a real **point of law** whose status differs from the composite. Both case-page exemplars that render it prove the boundary:

| case | composite_basis | override point | s3_binding | override Field-I vs composite | table? |
|---|---|---|---|---|---|
| New York v. Belton | **principal-holding** | `search.vehicle.sia-recent-occupant` (real) | **bound** | superseded ≠ caution (**varies**) | YES (built) |
| United States v. Smith (2024) | **principal-holding** | `search.warrant.geofence-general-warrant` (real) | **bound** | caution ≠ good_law (**varies**) | YES (built) |
| **10 legacy-limited** (Boyd, Coolidge, Escobedo, Mathis 1968, Monroe v. Pape, Oregon v. Elstad, Saucier v. Katz, Thornton, Agurs, Chadwick) | **migration-seed** | `legacy-limited-<slug>` (**synthetic**, label "Legacy limited treatment point") | provisional | caution **==** caution (**no variance**) | **no — not owed** |
| Gouled v. United States | migration-seed | **none (point_overrides = [])** | — | — | **no — not owed (empty)** |

Enumeration of all 13 `varies_by_point:true` case lake records partitions cleanly: 2 GENUINE (principal-holding / bound / status-differs → render) vs 11 non-genuine (10 migration-seed synthetic + 1 empty → the exact gate-b finding set).

**Disposition:** all 11 **DISMISS-not-owed**, 0 content edits.
- **10 legacy-limited:** the synthetic `legacy-limited-<slug>` override is not a point of law; its status equals the composite and its scope_note is identical — no variance to tabulate. Rendering `| Legacy limited treatment point | Caution | … |` would violate the R5 row schema and manufacture noise. Each page already correctly renders R5's "simple status lead otherwise" (verified on Boyd: `**Status:** limited … — **Binding — SCOTUS**` + prose).
- **Gouled:** `point_overrides` is empty → no table owed even under the *literal* R5 ("mandatory whenever `point_overrides` is non-empty"). The `varies_by_point:true`+empty inconsistency is the co-located LINT-12 drift HIGH (differing_fields=`treatment.varies_by_point`) = RULING P4-05 projector class (A1/B3), not a point-status-table defect.

**Prior-adjudication check (per instruction):** none of the 11 gate-b findings is covered by a prior P2 dismissal — the 4 cases carrying adjudications (Escobedo/Gouled/Agurs/Chadwick) carry only P2-QF-RULING **pin-quote** rows; the P2 "treatment-noise" class is about currency/"no negative treatment" sentences. All 11 gate-b assertion_ids are absent from `adjudications.jsonl`. Not re-litigated.

**Lake-note owed (OUT of my write-scope — lake not writable):** for the 10 migration-seed cases, `treatment.varies_by_point` should be `false` with `point_overrides=[]`, matching the migration-seed non-split sibling **Smith v. Maryland** (`varies_by_point:false, point_overrides:[]`). Recommend routing to the lake data-hygiene lane (same class as the Gouled LINT-12 drift). No registry/lake edit made here.

---

## B5 — absent-home placement (14 unique case→home gaps)

`homes[]` is an **author-controlled** field (S2 serializer `PRESERVED_TOP_LEVEL`, not lake-projected) — so narrow and add are both in content write-scope; the call is editorial. In **every** gap the case's **primary/anchor home is already rendered**; the absent home is a secondary/mis-declared entry.

| # | case → declared home | role | disposition |
|---|---|---|---|
| 1 | Pennsylvania Bd. of Probation & Parole v. Scott → The Exclusionary Rule (index) | Key — Limiting (primary) | **ADD** (fix) |
| 2 | United States v. Burgess → Border Searches | Related | **covered-by-prior** (F-S9-PR-c103f2fbbc) |
| 3 | Rakas v. Illinois → The Exclusionary Rule (index) | Related | **DISMISS-covered-by-convention** |
| 4 | Byars v. United States → The Exclusionary Rule (index) | Related | **DISMISS-covered-by-convention** |
| 5 | Almeida-Sanchez v. United States → The Exclusionary Rule (index) | Related | **DISMISS-covered-by-convention** |
| 6 | Peters v. New York → Terry Stops | Related | **narrow** (fix) |
| 7 | United States v. Cortez → Terry Stops | Key — Progeny | escalate |
| 8 | United States v. Sokolow → Terry Stops | Key — Progeny | escalate |
| 9 | United States v. Van Leeuwen → Terry Stops | Related | escalate |
| 10 | Kyllo v. United States → Curtilage | Related | escalate |
| 11 | United States v. Smith (2024) → Third-Party Doctrine & CSLI | Related (umbrella) | escalate |
| 12 | United States v. Meyer → Exigent Circumstances | Related | escalate |
| 13 | New York v. Class → Traffic Stops | Related | escalate |
| 14 | United States v. Moore-Bush → Fourth Amendment Framework | Key | escalate |

### Fixes applied (2)
- **Scott → exclusionary index (ADD).** Scott's PRIMARY declared home is the index; the index prose (line 39, "Where the rule does not reach") already states the parole-revocation limit **unnamed**. Named the controlling case: `… or parole revocation (*[[Pennsylvania Board of Probation and Parole v. Scott|Scott]]*; the cost-benefit boundaries …)`. Grounded: lake good_law 524 U.S. 357; case-page Rule (524 U.S. at 363). Attribution only, no new proposition. (Task said `:35`; actual clause is line 39.)
- **Peters → Terry Stops (narrow).** Mis-home: Peters's holding is probable-cause-to-arrest + search-incident-to-arrest (homed/rendered on `[[SIA Persons]]`); the Terry/frisk companion holding of the 392 U.S. 40 set is **Sibron v. New York**, already rostered as a Terry Stops Key case (line 85). Removed the unreciprocated Terry Stops entry from Peters `homes[]` + `## Appears on`; `related:` keeps the Sibron/Terry cross-refs. Grounded by identity-miskey F-S9-PR-8ad401eb6b (canonical caption = Sibron).

### Dismissals / covered
- **Burgess** — prior P2 home-mirror **DISMISSED** the exact placement (F-S9-PR-c103f2fbbc: "does not support placing Burgess on a Border Searches home, even as cross-doctrine"). Settled; not re-litigated.
- **Rakas / Byars / Almeida-Sanchez → exclusionary index** — the index is a prose-only umbrella that rosters **no** related cases (7 home-declaring cases absent by design, incl. Key/Anchor roles Lopez-Mendoza / James v. Illinois / Stone v. Powell); each of these three has its primary home honored (Rakas→Standing 9 lines; Byars→PC-in-the-Affidavit; Almeida-Sanchez→Border Searches). A secondary "Related" home to this umbrella does not compel a per-case render (P2 home-mirror principle). **No edit** — a frontmatter narrow of only these 3 would be inconsistent with the unflagged siblings on the same index.

### Escalations (8) — narrow-vs-add ungroundable from lake+conventions
All 8 targets carry a populated Related-cases table (or, for Moore-Bush, no roster at all), and each case is a genuine-but-secondary cross-doctrine relation whose primary home is honored. The direction (narrow the unreciprocated declaration vs. add a Related row) is a doctrine-owner editorial call I decline to guess (writer≠checker). Notable per-case grounding is in the disposition rows; highlights:
- **Cortez / Sokolow → Terry Stops**: two-"Key"-homes anomaly (R6 = one primary home); both are RS-anchored on the separate `[[Reasonable Suspicion]]` standards-of-proof page.
- **Moore-Bush → FA Framework**: structural — FA Framework carries **no case roster** (Brief/Visual/Sources only), so a "Key" case cannot be hosted; Moore-Bush is the sole declarant and a frontier-stub (F-S9-PR-ecdb869fd5).
- **Van Leeuwen** also has an internal `homes[]` vs `## Appears on` mismatch (Appears-on drops its primary Seizure of Property home) — flagged as a separate hygiene item.
- **Smith (2024) → CSLI**: umbrella parent may delegate to the geofence sub-page (its Key home); relates to A3 (the separately-handled geofence Smith-mislink).
- **Meyer/Meyers** name-collision noted (F-S9-PR-6ec527744a is Florida v. **Meyers**, a different case).

**Class-level recommendation for the orchestrator.** The P2 home-mirror (189 rows, overwhelmingly DISMISSED) + P3-HM precedent lean **against** adding unreciprocated secondary relations. Recommend one convention ruling — narrow all unrendered secondary cross-doctrine homes vs. accept them as soft relations — applied to the **full** absent-secondary-home set, not just the PAIR-flagged subset (the sweep flagged only some; e.g. 7 cases sit absent from the exclusionary index, 4 flagged here).

## Ambiguities for the orchestrator
1. B4 lake-hygiene: 10 migration-seed `varies_by_point:true` records should flip to `false` (out of my write-scope) — route to lake lane with the Gouled LINT-12 drift.
2. B5 escalations (8): the narrow-vs-add convention call above.
3. Concurrent-edit note: `the-exclusionary-rule/.../index.md` and `Good-Faith Exception.md` show other-lane edits in the working tree; my single-clause Scott add applied cleanly and independently.
