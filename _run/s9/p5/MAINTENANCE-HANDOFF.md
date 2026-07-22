# CSSI maintenance handoff (S9 R12)

**Artifact:** `s9.maintenance-handoff.v1` · **Generated:** 2026-07-22 · **Lane:** P5-R12 · **Model:** claude-opus-4-8
**Machine form:** [`MAINTENANCE-HANDOFF.json`](./MAINTENANCE-HANDOFF.json) (schema-valid; self-describing `_schema` block).
**Filed to:** GH#2 (`Enragedsaturday/cssi` issue #2) at PUBLISH (P6), on gate pass + user go-ahead.

This is the seed for the ongoing maintenance loop. Six sections; every count is derived from the
named source artifacts (findings-only — gate adjudication and ticket closure remain the
orchestrator's). Feed section 1 into CourtListener citation/docket alerts; run sections 2–3 on the
stated cadences; sections 4–6 are precondition, register, and carried notes.

---

## 1. CL citator-alert seed list

Feed each `cluster_id` / `docket` into a CL alert.

| sub-block | count | what to watch |
|---|---|---|
| marker-poll rows | 12 | pending markers re-polled at P4 (incl. **Carter** cert 25-885, **Noem** v. Vasquez Perdomo, **Lange** felony-reservation, and **holcomb-watch** — CHANGED: superseding PUBLISHED opinion cluster **10932458**, filed 2026-07-17, text pending) |
| I4-TRIAGE watch rows | 3 | digital-data-retention frontier (post-Ganias), unmapped-circuit constructive-entry authority, CSLI through-line post-Chatrie |
| post-build recency citers | 31 | federal-circuit decisions filed 2026-07-06..07-21 citing the corpus canon; R7.1 currency-watch, NOT discovery misses |
| companion Brillhart 24-13232 | 1 | *United States v. Richard Brillhart* (11th Cir., cluster 10925245 — shared with the 24-13226 stub); co-defendant appeal; cite-pending |
| cite-pending clusters | 7 | Case v. Montana (10774335), Chatrie (10881683), Zorn v. Linton (10813527), Lowers (10807484), Brillhart (10925245), Eric Johnson (10648997), Wilson (10636220) — all `citations=[]`; upgrade slip-op sourcing when a reporter cite lands |
| **negative-treatment census** | **18** | 7 superseded + 11 caution — the reversal-of-fortune watch |

Carter/Noem/Lange live in the 12 marker-poll rows; Chatrie/Zorn/Case v. Montana appear in both
marker-poll and cite-pending (same watch, two lenses); companion Brillhart is row 14 of the 31
recency citers.

### Negative-treatment census (18) — the reversal-of-fortune watch
Every lake record whose `field_i_validity` is not `good_law`/`unverified`. Monitor each limiting
case's line for further erosion or an overrule that reaches the still-good half.

| case | status | limiting case(s) |
|---|---|---|
| Aguilar v. Texas | superseded | Illinois v. Gates (abrogated) |
| Gouled v. United States | superseded | Warden v. Hayden (overruled) |
| Jones v. United States | superseded | Rakas v. Illinois / United States v. Salvucci (overruled) |
| Michigan v. Jackson | superseded | Montejo v. Louisiana (overruled) |
| Olmstead v. United States | superseded | Katz v. United States (overruled) |
| Spinelli v. United States | superseded | Illinois v. Gates (abrogated) |
| Wolf v. Colorado | superseded | Mapp v. Ohio (overruled) |
| Boyd v. United States | caution | Warden v. Hayden (limited) |
| Coolidge v. New Hampshire | caution | Horton v. California (limited) |
| Escobedo v. Illinois | caution | Miranda / Kirby / Moran v. Burbine (limited) |
| Mathis v. United States (1968) | caution | Howes v. Fields (limited) |
| Monroe v. Pape | caution | Monell v. Dept. of Social Services (limited) |
| New York v. Belton | caution | Arizona v. Gant (limited; from scope_note — principal-holding record, no migration edge) |
| Oregon v. Elstad | caution | Missouri v. Seibert (limited) |
| Saucier v. Katz | caution | Pearson v. Callahan (limited) |
| Thornton v. United States | caution | Arizona v. Gant (limited) |
| United States v. Agurs | caution | United States v. Bagley (limited) |
| United States v. Chadwick | caution | California v. Acevedo (limited) |

---

## 2. Dual-date decay schedule (PRACTICES §6.10)

Dual as-of dating: `as_of_content` (drives G3/G4 cite-existence + quote-fidelity re-run) and
`as_of_treatment` (drives G6 treatment/currency re-run) decay independently. Distribution: 457
records treatment-dated 2026-06-30 (+1 at 2026-07-03), 214 null (frontier/under_review stubs).

| bucket | gate | records | seed date | cadence | next re-check |
|---|---|---|---|---|---|
| A. negative-treatment | G6 treatment/currency | 18 | 2026-06-30 | 90 d | **2026-09-28** |
| B. good_law, treatment-dated | G6 treatment/currency | 440 | 2026-06-30 | 180 d | 2026-12-27 |
| C. content re-verify (all dated) | G3/G4 cite+quote | 458 | (per as_of_content) | 365 d | 2027-06-30 |
| D. null-treatment stubs | none — re-derive at S6 promotion | 214 | — | — | — |

Bucket A (== the negative-treatment census) is the highest priority; COH-27 markers (Carter/Noem/
Lange) ride bucket A. CL-markup drift on fragments is handled by section 3, not bucket C.

---

## 3. Fragment re-validation queue

Re-validate on CourtListener markup drift (S8 §9): fragments are external `#:~:text=` deep-links
whose landing depends on CL's rendered opinion HTML.

- **231 fragments traced** (S8H-B): 230 MATCH + 1 MATCH-VARIANT; G3-passed 226; 2 g3_mismatch_pin,
  3 g3_no_pin, 0 no_record. **5 attention rows** to re-check first on any CL re-render:
  Florida v. Jardines L57 (pin-9 mismatch), United States v. Walker L55 (pin-1364 mismatch),
  Knock and Talk L19 ×3 (no pin).
- **117-row pin-upgrade queue** (37 distinct cases): 85 "no star pagination in cache/html/2nd-source"
  + 31 loop-3 residual interior pins + 1 loop-2 orchestrator ruling. Re-verify each when official
  U.S. Reports star-pagination lands. Heaviest: Riley v. California (14), Cone v. Bell (7),
  Missouri v. McNeely (6), Lange v. California (6).
- **Entick unmonitorable:** *Entick v. Carrington* (19 How. St. Tr. 1029, `verified_off_cl`) has
  **no CL cluster/opinion id** — structurally unmonitorable by the citator loop (RULING P4-06). No
  alert can be seeded; do not mistake its absence from alerts for a gap.

---

## 4. Deck-rebuild precondition attestation

Deferred-run-#2 precondition (S9 §2.2): confirm the frozen deck stems still resolve.
Ran `scripts/lint/lint25_deck.py` against the current (moved/de-numbered) content tree.

- **57 decks · 44 distinct page-stems · 1,773 cards.**
- **LINT-25 result: 0 unresolved stems** (0 high / 0 medium / 0 low) — every deck stem resolves
  against a current page (final-slug or bare-stem alias).
- **Measured: PASS.** (Writer≠checker — the orchestrator adjudicates the gate box.)

---

## 5. Open `_review-needed/` register (9 files)

| file | state | what remains |
|---|---|---|
| chatrie-scotus-2026-correction.md | RESOLVED | Chatrie SCOTUS still cite-less on CL (cluster 10881683 corrupted=Harmon); residual = the cite-pending watch |
| lint3-chatrie-recent-dev-false-positive.md | OPEN (tool-precision) | MEASURED-SUBSUMED: current lint3 emits 0 chatrie/SCOTUS N5 flags post-campaign; confirm + close; content verified correct |
| s9-p2-delgado-inbox.md | OPEN | INS v. Delgado (466 U.S. 210, cluster 111148) gap; NOT ingested; route via S6 R8 (INGEST recommended) |
| s9-p2-entrap2-r7-routing.md | OPEN | R7 absence-sweep on outrageous-government-conduct viability; spawn Entrapment-page finding only if a grounded divide emerges |
| s9-p3-underreview-promotions.md | RESOLVED | none — 22/22 closed via PROMO-FIX; queue_outstanding=0 |
| s9-p4-callout-registry-deepequal.md | CLOSED | resolved as Amendment A2; residual = the 62 registry-notes (informational) |
| s9-p4-lint-baseline-campaign.md | CLOSED | residue = LINT-30's 25 (P5 ledger-tidy) + LINT-1 at the serial gate |
| threadN-lyle-unread.md | OPEN (ESCALATE) | *United States v. Lyle* (lead 8415374) unread on all 3 blind sweeps (2/1218 = 0.16%); single-lane retry in a quiet window |
| coverage/_ESCALATION-batch4-duplicate-CL-lane.md | STALE (no closure stamp) | historical dual-CL-lane incident (2026-06-30); 9 pages written complete-to-spec; confirm closure |

---

## 6. P5-handoff notes (carried this phase)

1. **COH-B registry-notes — 62** (16 pincite_drop + 45 different_authority + 1 miranda-waiver
   scope-divergence). Informational; registry cites poorer-not-wrong; zero registry edits owed.
2. **Secondary-home placement convention** (P4-13(b) / A3): soft relations accepted; 3 unrendered
   Key declarations narrowed (Moore-Bush, Cortez, Sokolow). Open: corpus-wide narrow-vs-add sweep?
3. **S1 §3.1 / S2 SD9 conflict** (P4-20(b)): weight labels derive from court level; overruled status
   lives in field_i + badges + Historical prose. Built convention stands; S1-side text reconcile owed.
4. **+36 LINT-7 register-coverage mediums** (P4-17(e)): from de-hyphenation; S8 coverage-linker lane
   class, not campaign scope; non-blocking.
5. **Haynes v. Washington scope_note variant + Satterfield L80 medium** (P4-19 / WB1): data-hygiene
   normalization owed.
6. **5th-Cir Wilson caption-collision** (P4-18(iii)): `United States v. Wilson` collides — 9th Cir.
   2021 (13 F.4th 961, cluster 5296785) vs 5th Cir. 2025 post-Bruen stub (23-30777, cluster 10636220);
   caption/slug disambiguation owed.
7. **Ledger regen-durability** (P4-18(iii) / P5-01): keep `ledger-exceptions.jsonl` + reconstruction
   provenance durable across future regens (P5-01 reconstructed 2 orphan findings + 21 sub-quorum rows).
8. **LINT-2 mediums census — 683** block-quotations without a nearby pincite across 207 files; all
   medium (0 high, non-blocking). De-quote or add a reporter pincite; maintenance editorial backlog.
9. **Out-of-remit referrals** (P4-09(4), ruling-routed addition): Loper Bright (correctly absent),
   ABA Formal Op. 512, AI-citation-sanctions material, Klein v. Martin (AEDPA), Gonzalez v. United
   States cert-statement — instructor-reference candidates for the maintenance loop, not S6 R8 draft.

---

## GH#2 filing block (intended, filed at P6 publish)

- **Repo:** `Enragedsaturday/cssi` (the FORK) · **Issue:** #2
- **Title:** CSSI maintenance loop — CL citator alerts, dual-date decay, fragment re-validation,
  deck-rebuild precondition, open review-needed register
- **Attach:** `_run/s9/p5/MAINTENANCE-HANDOFF.json` + `_run/s9/p5/MAINTENANCE-HANDOFF.md`
- **Labels:** citator-alert · decay-recheck · fragment-drift · deck-rebuild · review-needed · data-hygiene
- **Status:** PENDING (S9 R12 check: GH#2 references this artifact at publish).
