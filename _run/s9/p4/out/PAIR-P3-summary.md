# PAIR-P3 summary — S9 P4 R6 contradiction sweep

**Packet:** PAIR-P3 (WS=PAIR) · **lane/model:** `claude-opus-4-8`
**Scope:** pairs **PAIR-0221 → PAIR-0330** (110 pairs) in `_run/s9/p4/pair-list.json`.
**Governing:** S9 §5 P4 R6; **RULING P4-02** (per-pair review scoped to shared_items only).
**Write-scope honored:** only `_run/s9/p4/` written.
**Outputs:** `out/PAIR-P3-dispositions.jsonl` (110 `p4.pair.v1` rows), `out/PAIR-P3-findings.jsonl` (empty — 0 HITs), this file.

## Coverage ledger (deterministic)
| metric | value |
|---|---|
| pairs assigned | 110 (PAIR-0221…PAIR-0330) |
| pairs examined | **110 / 110** |
| pairs skipped | 0 |
| dispositions | **110 upheld** (0 hits) |
| candidate findings filed | **0** |
| kinds | 109 shared-case + 1 registry-point (PAIR-0316 `fairtrial.eyewitness`) |
| unique pages touched | 86 · unique shared items | 52 cases + 1 registry point |
| absent-home observations (out of R6 scope) | 12 pairs (see below) |

## Method
Grouped the 110 pairs by shared item (52 cases + 1 point) to read each page once. For every
shared case I read the canonical record (`content/cases/<case>.md` frontmatter `treatment` block +
body) and every doctrine home named in my pairs, then applied **only** the RULING P4-02 legs to
each pair's `shared_items`:
- **(i) treatment status + N4 "limited by" tag identity** — Field-I `field_i_validity` composite on
  the case page vs. how each doctrine page renders the case's status/limitation.
- **(ii) overruled ⇒ Historical on both** — no case in scope is `field_i_validity: overruled`, so
  the leg is vacuously satisfied; also checked the converse (no good-law case rendered
  overruled/Historical on a home). None found.
- **(iii) semantic contradiction in the shared item's framing** — N6 page-specific framing is
  permitted; only genuine incompatibility counts.
- **(iv) nothing else** — full-page/placement re-review is P1's; not re-litigated here.
Cross-checked `_run/s9/adjudications.jsonl` (0 prior R6/pair rows; case-level P2/P3 rows reviewed
for regressions — none). No live CL used.

## Why every pair upheld (representative reasoning)
- **Treatment-varies cases render point-scoped, not contradictory.** *United States v. Chadwick*
  (`caution`, `varies_by_point: true`): Searching Effects & Containers carries the full
  varies-by-point exposition + "limited by *California v. Acevedo* for containers in a car";
  Automobile Exception carries the same Acevedo N4 tag; **SIA Persons** frames only the
  exclusive-control point (the un-limited facet) and correctly omits the Acevedo caveat, which is
  proper under N4 (treatment woven "where asserted"). *United States v. Santana* (`good_law`,
  `varies_by_point: false`) discloses the *Lange v. California* misdemeanor-pursuit limit in its
  case-page `scope_note` + body, and all three homes (Curtilage, Arrest in the Home, Exigent
  Circumstances) carry the same "cabined by *Lange*" tag — consistent. *Escobedo v. Illinois*
  (`caution`/limited) is framed as the *Miranda* precursor "confined to its facts" on the Miranda
  page and "treatment: limited" on the Sixth Amendment page — same status both sides.
- **"Unverified" ≠ "bad law."** The COA cases at `field_i_validity: unverified` (Berkowitz, Burgess,
  Daniels, Maez, Meyer, Moore-Bush, Nora, Vaneaton, Wilson) are cited on their holdings / as
  split-frontier authority on the doctrine pages, with no affirmative good-law treatment pill; an
  N2 authority-weight label ("Binding in-circuit — 10th Cir." for Burgess) is orthogonal to the
  Field-I subsequent-treatment-verification status, so it is not a status contradiction. Moore-Bush
  and Wilson explicitly say "later treatment not yet independently verified, cited on its holding,"
  matching the case-page status.
- **Same case, different doctrinal facet = N6, not contradiction.** *United States v. Place*
  (dog-sniff-not-a-search on REP vs. 90-minute-seizure-too-long on Terry Stops), *Simmons* (photo
  array DP vs. suppression-hearing testimony/standing), *Hester* (abandonment-by-flight vs.
  open-fields origin), *Watson* (public-arrest-no-warrant vs. custody-is-a-factor-consent),
  *Van Leeuwen* (no-privacy-until-opened vs. reasonable-seizure-with-diligence) — each renders a
  distinct true holding of the same case per the hosting doctrine.
- **Registry point PAIR-0316 (`fairtrial.eyewitness`).** Home (Eyewitness Identification) and also_on
  (Lineups and the Right to Counsel) both frame the doctrine as **two independent tracks**
  (14A due-process reliability / 6A counsel-presence), each stating "an identification can pass one
  and fail the other" and cross-referencing the sibling page. Complementary, not contradictory.

## Absent-home observations (OUT of R6 scope — triage deferred to orchestrator)
Per RULING P4-02(iv), a case that is simply **not rendered** on one paired page yields **no second
framing to contradict**, so it is not an R6 hit (dispositioned `upheld`, `flag:"absent-home"`).
Flagged here because it is a placement/Appears-on question P1 owns. Two root-cause clusters plus six
single case-anchor gaps:

**Cluster A — *United States v. Moore-Bush* not written on its declared home
`content/foundations-and-the-fourth-amendment/Fourth Amendment Framework.md`** (4 pairs):
- PAIR-0259 (case page ↔ FA Framework), PAIR-0318 (FA Framework ↔ Curtilage),
  PAIR-0319 (FA Framework ↔ Third-Party Doctrine and CSLI), PAIR-0320 (FA Framework ↔ Reasonable
  Expectation of Privacy). Moore-Bush IS rendered on Curtilage / CSLI / REP consistently; only the
  FA Framework home lacks it.

**Cluster B — *Kyllo v. United States* not written on its declared home `content/searches/Curtilage.md`**
(2 pairs):
- PAIR-0324 (Aerial and Enhanced Surveillance ↔ Curtilage), PAIR-0330 (Curtilage ↔ Third-Party
  Doctrine and CSLI). Kyllo IS rendered on Aerial / CSLI / REP consistently; only the Curtilage home
  lacks it.

**Single case-anchor gaps (case page ↔ doctrine home that omits the case):**
- PAIR-0226 *United States v. Burgess* ↛ `content/warrant-exceptions/programmatic-and-special-needs-searches/Border Searches.md`
- PAIR-0230 *United States v. Cortez* ↛ `content/seizures/Terry Stops and Reasonable Suspicion.md`
- PAIR-0258 *United States v. Meyer* ↛ `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md`
- PAIR-0273 *United States v. Smith (2024)* ↛ `content/searches/the-third-party-doctrine-and-digital-surveillance/Third-Party Doctrine and CSLI.md`
- PAIR-0274 *United States v. Sokolow* ↛ `content/seizures/Terry Stops and Reasonable Suspicion.md`
- PAIR-0280 *United States v. Van Leeuwen* ↛ `content/seizures/Terry Stops and Reasonable Suspicion.md`

(Verified not a grep artifact: short-name and wikilink-target forms were also searched; on the
Third-Party CSLI page the only "Smith" is *Smith v. Maryland*, not *U.S. v. Smith (2024)*. Note the
*Meyer* case page's `homes:` name Knock and Talk + Exigent; Meyer renders on Knock and Talk but not
on the Exigent home. The pair-list generator resolved these home wikilinks (0 unresolved) but a
resolvable target ≠ the case being authored on the page — that is the coverage gap.)

## Ambiguities for the orchestrator
1. **Absent-home disposition.** I ruled these `upheld` (no R6 contradiction) under P4-02(iv). If the
   orchestrator wants absent declared-homes surfaced as candidates, they belong to a placement/
   Appears-on class (P1), not R6 — re-route rather than re-run this lane.
2. **`p4.pair.v1` schema.** No sibling template existed; I mirrored the `p4.mermaid.v1` convention
   (`row`,`pair_id`,`kind`,`shared_item`,`page_a`,`page_b`,`disposition`,`checks`{treatment_status,
   n4_limited_by_tag,overruled_historical,semantic_framing},`flag`,`note`,`lane`,`model`). Adjust if
   the reducer expects different field names.
