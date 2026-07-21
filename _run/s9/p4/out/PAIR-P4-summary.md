# PAIR-P4 summary — R6 contradiction sweep (pairs PAIR-0331..0437)

**Packet:** PAIR-P4 (WS=PAIR, S9 §5 P4 R6) · **lane/model:** `claude-opus-4-8`
**Governing:** RULING P4-02 (per-pair review scoped to `shared_items`: (i) treatment
status + N4 "limited by" tag identical across the pair; (ii) overruled cases rendered
Historical on both; (iii) shared point/case framing not semantically contradictory,
N6 divergence allowed; (iv) nothing else — full-page review was P1's job).
**Write-scope honored:** only `_run/s9/p4/` written.
**Outputs:** `out/PAIR-P4-dispositions.jsonl` (107 `p4.pair.v1` rows),
`out/PAIR-P4-findings.jsonl` (0 rows — no HITs), this file.

## Coverage (deterministic)
- **Assigned:** 107 pairs, PAIR-0331 … PAIR-0437 (contiguous, unique). 103 `shared-case` +
  4 `mixed`.
- **Examined:** 107/107. Every pair's `shared_items` reviewed on both pages.
- **Skipped:** 0. No silent truncation.
- **Result:** **107 PASS, 0 HIT.** No R6 cross-page semantic contradiction found; every
  negative-treatment leg verified consistent across its pair; every overruled case rendered
  Historical on both pages.

## Method
1. Extracted the 107 pairs from `pair-list.json`; built a Field-I treatment map for all 610
   `content/cases/*.md` (`treatment.field_i_validity`) via `parse_yaml_subset`-style frontmatter read.
2. Grouped by page (53 unique doctrine pages — all 107 pairs are home×home, no case-anchored
   pairs in this slice). For each `shared_items` case, extracted the **framing signature** on
   both pages by strict full-name wikilink match: (a) the Key/Related table role-description
   cell, (b) the reference-line treatment parenthetical, (c) any prose line carrying a treatment
   keyword (overrule/abrogate/supersede/limited-by/narrow/cabin/Historical/abandoned). Compared
   A-vs-B per case.
3. **High-signal legs given full manual reads** (negative Field-I, i.e. `superseded`/`caution`):
   Olmstead (0339), Coolidge (0345), Belton (0388), Spinelli (0402), Chadwick (0424/0425/0436),
   Thornton (0437) — read the actual page text on both sides for checks (i)+(ii).
4. **4 mixed pairs given extra care** (point statement + its cases on both pages): pulled the
   registry-point `statement` from `registry.yaml` and verified the rendered callout/prose on
   both hosting pages: PAIR-0387 (checkpoint-sobriety + checkpoint-crime-control + Prouse),
   PAIR-0397 (arrest-in-home + constructive-entry + Payton/Steagald/Harris/Al-Azzawy/Berkowitz/
   Maez/Nora/Vaneaton), PAIR-0425 (search.effects.containers + Acevedo/Chadwick/Ross),
   PAIR-0427 (search.home.exigency.destruction + Kentucky v. King).
5. Checked `_run/s9/adjudications.jsonl` before disposing borderline treatment/mirror items
   (below).

## Negative-treatment legs — all consistent (checks i + ii)
| pair | case | treat | result |
|---|---|---|---|
| 0339 | Olmstead | superseded | Overruled/superseded-by-Katz rendered on **both** pages → check(ii) OK |
| 0402 | Spinelli | superseded | Abrogated-by-Gates + "historical backbone" rendered on **both** pages → check(ii) OK |
| 0345 | Coolidge | caution | Two distinct holdings (inadvertence-abandoned-by-Horton vs AG-not-neutral) — page-appropriate point per varies_by_point/N6 |
| 0388 | Belton | caution | Same composite (caution) + controlling case (Gant) both sides; umbrella "limited by Gant" vs precise "trigger superseded/scope survives" = documented varies_by_point granularity |
| 0424/0425/0436 | Chadwick | caution | "limited by Acevedo (container-in-car)" where that point is asserted; good-law exclusive-control SITA point where THAT is asserted — varies_by_point, no divergence |
| 0437 | Thornton | caution | "limited by Gant" on **both** pages |

## Mixed pairs (4) — registry points verified consistent
- **0387**: Sitz (sobriety valid) / Edmond (crime-control unconstitutional) framed identically
  on Traffic Stops (cross-doctrine summary, home=Special Needs) and Checkpoints (full home);
  Prouse consistent.
- **0397**: Arrest-in-Home **transcludes** Entry-to-Arrest's `^rule-entry-to-arrest`;
  constructive-entry deferred to Entry to Arrest and faithfully framed there as an **unsettled
  circuit split** (recognizing: Nora/Al-Azzawy/Maez; voluntary-exposure limit: Vaneaton; narrow:
  Knight/Berkowitz). Payton/Steagald/Harris consistent both sides.
- **0425**: search.effects.containers + the Chadwick→Ross→Acevedo unification story consistent.
- **0427**: Kentucky v. King police-created-exigency rule identical on Destruction of Evidence
  (home) and Exigent Circumstances.

## Out-of-scope / borderline observations (NOT filed as HITs — for orchestrator awareness)
These are recorded because RULING P4-02(iv) excludes them and because each aligns with an
already-**DISMISSED** P2 adjudication class (so filing would be regression/noise):

1. **Treatment-granularity (treatment-noise class, P2-DISMISSED).** PAIR-0388 Belton reference
   tag reads "limited by Arizona v. Gant" on Traffic Stops vs "vehicle-search trigger superseded
   by Gant (2009)" on SIA Vehicles. Directionally identical (both = caution, Gant cut-back),
   difference is documented `varies_by_point`. The P2 panel repeatedly refuted this exact class
   (e.g. F-S9-PR-3e2c7f0d62: "core superseded/overruled-in-part treatment stands, but
   varies_by_point=false too blunt" → DISMISSED). PASS.
2. **Reference-line annotation asymmetry.** PAIR-0402 Spinelli: `Probable Cause` citation line
   carries "(Historical; abrogated by Gates)"; `Probable Cause in the Affidavit` citation line
   (line 101) carries only "(pinpoints: 415, 418)" — but that page's **table** (line 74:
   "the historical backbone…abrogated by Gates") and **prose** (line 32: "Gates abandoned that
   rigid structure") do render the treatment, and Aguilar's citation line on the same page is
   annotated identically (no tag), so it is a uniform page-local citation-list style, not a
   status divergence. check(ii) is met on both pages. PASS.
3. **Home-mirror / appears-on gaps (home-mirror class, P2-DISMISSED; P1/S8H territory).**
   13 pairs have a shared case declared as a home on both pages but **absent** on one page
   (verified genuinely absent, not a grep miss). No cross-page framing exists, so R6 checks are
   vacuously satisfied. Listed for the S8H mirror-verify pass, not filed here:
   - 0331 Kyllo — absent on Curtilage (A)
   - 0344 / 0360 New York v. Class — absent on Traffic Stops (B)
   - 0354 United States v. Smith (2024) — absent on Third-Party Doctrine and CSLI (B)
   - 0359 / 0369 United States v. Van Leeuwen — absent on Terry Stops (B)
   - 0380 United States v. Cortez, United States v. Sokolow — absent on Terry Stops (A)
   - 0383 Peters v. New York — absent on Terry Stops (A)
   - 0406 Rakas v. Illinois — absent on the-exclusionary-rule/index (B)
   - 0410 Byars v. United States — absent on the-exclusionary-rule/index (A)
   - 0411 Almeida-Sanchez v. United States — absent on the-exclusionary-rule/index (A)
   - 0412 Pennsylvania Bd. of Probation and Parole v. Scott — absent on the-exclusionary-rule/index (A)
   - 0423 United States v. Meyer — absent on Exigent Circumstances and Hot Pursuit (B)
   (This is the same "home declared but case not rendered on that page" pattern P2 dismissed as
   home-mirror, e.g. F-S9-PR-89c06ef612 Terry-not-on-Traffic-Stops → DISMISSED.)

## Notes for the orchestrator
- **Zero legal-assertion HITs → no R1 panel referee owed** for this packet.
- The 13 home-mirror absences are a legitimate completeness signal but out of R6 scope; if the
  orchestrator wants them chased, they belong to the S8H mirror-verify list, not a P4 fix packet.
- No CL needed; all evidence from `content/`, `registry.yaml`, `pair-list.json`, `adjudications.jsonl`.
