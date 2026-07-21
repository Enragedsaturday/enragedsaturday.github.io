# PAIR-P2 summary — S9 P4 R6 contradiction sweep

**Packet:** PAIR-P2 (WS=PAIR) · **lane/model:** `claude-opus-4-8`
**Scope:** pairs PAIR-0111 through PAIR-0220 in `_run/s9/p4/pair-list.json` (110 pairs).
**Governing:** S9 §5 P4 R6; review scope fixed by **RULING P4-02** (shared_items only:
(i) treatment status + N4 "limited by" tag identity, (ii) overruled = Historical on both,
(iii) shared item's framing not semantically contradictory — N6 divergence allowed, only
genuine incompatibility is a hit, (iv) nothing else — full-page re-review was P1's job).
**Write-scope honored:** only `_run/s9/p4/` written.
**Outputs:** `out/PAIR-P2-dispositions.jsonl` (110 `p4.pair.v1` rows), `out/PAIR-P2-findings.jsonl`
(0 rows), this file.

## Coverage ledger (deterministic)
| metric | value |
|---|---|
| pairs assigned | 110 (PAIR-0111 … PAIR-0220) |
| pairs examined | **110 / 110** |
| pairs skipped | 0 |
| HITs (candidate findings) | **0** |
| dispositions | 110 `upheld` (R6 clean) |
| of which flagged out-of-scope | 4 (`absent-home`) |

All 110 pairs are `kind=shared-case`, `why=multi-home`, **case-anchored**
(`page_a = content/cases/<case>.md`, `page_b =` a resolved doctrine home), each with exactly
one shared item (a case). 48 distinct cases span 94 distinct pages. Grouped by case to read
each canonical case page once.

## Method
1. Parsed each shared case's canonical record (`content/cases/<case>.md`): Field-I validity
   composite, `authority_weight`, header treatment line, `holding`, `scope_note`, `homes[]`.
2. For each `page_b`, harvested every rendered mention of the case (prose, Key/Related tables,
   pitfall callouts, Mermaid nodes, reference list) via distinctive-token grep, then compared
   to the canonical record on the three R6 legs.
3. Cross-checked `_run/s9/adjudications.jsonl` before considering any row a hit
   (`adjudication-regression` guard). No new hit collides with a prior verdict.

## Result: no R6 contradictions
Every shared item reads consistently across its pair. The treatment-carrying cases were the
high-scrutiny targets and all pass:

- **Olmstead v. United States** (`superseded` 🔴 / Historical / overruled) — PAIR-0177
  (Electronic Surveillance and Title III), PAIR-0178 (Trespass). Rendered **overruled by
  *Katz*** + tier-6 Historical on **both** doctrine pages and the case page; the *Jones*
  property-revival is noted per-page (N6), neither page cites it as current good law. Leg ii
  satisfied.
- **Spinelli v. United States** (`superseded` 🔴 / Historical / abrogated) — PAIR-0207
  (Probable Cause), PAIR-0208 (Probable Cause in the Affidavit). Rendered **abrogated by
  *Illinois v. Gates*** + Historical on both pages and the case page. Leg ii satisfied.
- **New York v. Belton** (`caution` 🟡, varies by point) — PAIR-0167 (Traffic Stops), PAIR-0168
  (SIA Vehicles). "limited by / superseded by *Gant*" N4 tag carried on both surfaces; the
  vehicle-trigger point superseded, container/scope point survives — consistent with the
  varies-by-point composite (SIA Vehicles even cross-cites the case page's `Caution — varies
  by point`). STANDARDS §3.2 expressly sanctions the *Belton*→*Gant* edge as "superseded where
  replaced outright." Legs i/ii satisfied.
- **Thornton v. United States** (`caution` 🟡, limited by *Gant*) — PAIR-0217 (Automobile
  Exception), PAIR-0218 (SIA Vehicles). "limited by *Gant*" tag carried on both. Legs i/ii
  satisfied.
- **Knight v. Jacobson** (`unverified` ⚪, 11th Cir. frontier stub) — PAIR-0126/0127; and
  **United States v. Al-Azzawy** (`unverified` ⚪, 9th Cir. frontier stub) — PAIR-0219/0220.
  Each is presented on `page_b` as one labeled side of the constructive-entry circuit split
  (holding stated, currency **not** asserted as good law). No treatment/framing contradiction.

The 98 `good_law` pairs each frame the shared case on a page-specific facet of its holding
(N6 divergence) with no negative Field-II edge on either side; framings are complementary, not
incompatible.

## Out-of-scope triage observations (NOT R6 hits — for orchestrator, per P4-02(iv))
Recorded as `flag: "absent-home"` in the disposition rows; **not** filed to findings.

1. **Kyllo v. United States → Curtilage** (PAIR-0133) — `homes[]` role "Related
   (cross-doctrine)"; case not rendered/linked on `content/searches/Curtilage.md`. *Already
   in the orchestrator's `PAIR-TRIAGE` absent-home aggregate ("Kyllo->Curtilage").*
2. **Peters v. New York → Terry Stops** (PAIR-0184) — `homes[]` role "Related"; only the
   companion *Sibron v. New York* (shared opinion id) is rendered, not *Peters* by name.
   **New** (not yet in the PAIR-TRIAGE aggregate).
3. **Rakas v. Illinois → The Exclusionary Rule** (PAIR-0189) — `homes[]` role "Related"; the
   target resolves to the 51-line `.../the-exclusionary-rule/index.md` **umbrella** landing
   page (zero case tables); *Rakas* not rendered there. Its anchor home Standing (PAIR-0188)
   is present + consistent. **New.**
4. **Pennsylvania Bd. of Probation and Parole v. Scott → The Exclusionary Rule** (PAIR-0182) —
   `homes[]` role **"Key — Limiting"**; on the same umbrella `index.md` the parole-revocation
   POINT appears **unattributed in prose** (`index.md:35`, "…or parole revocation…") but the
   case is **not named or wikilinked** (N7). The point is stated *consistently* with the case
   page — this is a placement/link defect, not a contradiction. **New.**

For all four: no second rendering of the shared case exists to compare, so R6 legs are vacuous
and the disposition is `upheld`. Disposition owed is a **placement adjudication** (narrow the
case's `homes[]`, or add/link the case on the page) — not an R6 contradiction. Note the
umbrella-index pattern (#3, #4) mirrors PAIR-P1's Almeida-Sanchez/Byars → exclusionary-rule
index observations.

**Non-absent, non-R6 nit (informational, not flagged in a disposition):** on
`content/seizures/Seizure of the Person.md:164` the reference-list entry for *Taylor v.
Alabama*, 457 U.S. 687 (1982) carries "(pinpoints: 217–218)", which do not fall within the
U.S.-reporter page span of that case; the in-body table row (line 115) cites 457 U.S. 687
correctly. This is a citation-hygiene / pincite matter (D7/L3), **out of R6 scope** — surfaced
for the QF/pincite lane, not adjudicated here.

## Adjudication cross-check (no regressions)
Reviewed `adjudications.jsonl` for my non-`good_law` cases. Relevant priors — Spinelli
holding-substance (F-S9-PR-30c71f1b3a, **DISMISSED**), Olmstead/Katz electronic-surveillance
rule (F-S9-PR-401600d8a9, UPHELD → P3), Belton bare-*Davis* links (F-S9-R9B, UPHELD,
link-target), Jacobson treatment qualifier (F-S9-PR-1c2fc2e007, MODIFIED) — are all
single-page holding-substance / link-target / treatment-noise items, **not** cross-page R6
contradictions. None is re-litigated and none conflicts with an `upheld` here.
