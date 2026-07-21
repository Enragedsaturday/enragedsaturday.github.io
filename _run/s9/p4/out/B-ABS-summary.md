# B-ABS summary — absence-claim enumeration (S9 P4, R7.4)

Packet **B-ABS** (bootstrap, WS=I4). Findings-only. Model `claude-opus-4-8`.
Output: `_run/s9/p4/absence-claims.jsonl` (181 rows). WRITE-SCOPE `_run/s9/p4/` only.

## Deliverable
- **181** absence/negative-claim rows, schema `{claim_id, file, line, claim_text, class, subject, search_terms_suggested}`.
- Every `claim_text` is **verbatim** — sliced directly from the file at the recorded line by a
  start/end-anchor extractor (`scratchpad/build_abs.py`); a validator confirms all 181 texts are
  exact substrings of their `file:line`, all 7 keys present, all `claim_id`s unique. `line` is
  1-indexed (matches `rg -n`). `claim_id` assigned after a deterministic sort by (file, line).

## Counts by class
| class | rows |
|---|---|
| not-decided (Court/court "did not decide / left open / reserved / declined to decide") | 72 |
| split (circuit split, circuits divide, majority/minority, ⚖ split) | 42 |
| no-court-has (no SCOTUS / no circuit / no controlling precedent / never addressed) | 34 |
| open-question (remains open / unsettled / unresolved / live frontier) | 25 |
| first-impression | 4 |
| other (explicit "no split" assertions; "unmapped circuits" build-caveat) | 4 |
| **total** | **181** |

93 rows are on case pages (`content/cases/`), 88 on doctrine / index / reference pages.
Across **109 distinct files**. Densest: Case Index (8, holding mirrors), Third-Party Doctrine & CSLI (5), Aerial (4), Cell-Site Simulators (4), Collective Knowledge (4).

## Deterministic coverage
- **Assigned:** every `.md` under `content/` — 724 files (610 cases + 114 doctrine/index/reference).
- **Examined:** all 724 via 3 seeded grep passes (below); 355 unique candidate lines from pass 1,
  +57 unique new lines from pass 2, +29 unique new lines from pass 3 = **441 candidate lines** read
  and adjudicated for include/exclude; PLUS 6 frontier hubs read in full end-to-end.
- **Emitted:** 181 rows. **Skipped candidate lines:** ~260 (excluded classes below, each with reason).
- No silent truncation: the 6 anchor failures during build were line-number typos I re-grepped and
  corrected (Hayes 61, Evans 61, Castillo 65/68, McDonough 73; one Chatrie row dropped as a duplicate
  of Smith(2024):83 already captured).

## Pages read FULLY (end-to-end, to catch paraphrased negatives grep alone would miss)
1. `searches/the-third-party-doctrine-and-digital-surveillance/Cell-Site Simulators.md`
2. `searches/the-third-party-doctrine-and-digital-surveillance/Real-Time Tracking.md`
3. `searches/the-third-party-doctrine-and-digital-surveillance/Investigative Genetic Genealogy.md`
4. `searches/the-third-party-doctrine-and-digital-surveillance/Reverse-Keyword and Geofence Warrants.md`
5. `searches/the-third-party-doctrine-and-digital-surveillance/Third-Party Doctrine and CSLI.md`
6. `warrant-exceptions/home-entry-and-search/Entry to Arrest.md`

These are the highest absence-claim-density surfaces. Full reads confirmed grep had already caught
every rendered absence claim on them, and surfaced the "Unmapped circuits" build-caveat (Entry to
Arrest:60) and the twin "SCOTUS has never decided … circuits divide" statements (Entry to Arrest:28,56).

## Other frontier/split surfaces covered (grep returns whole markdown paragraphs, so their
Splits / Lower-court developments / Frontier / Recent-developments sections were read as paragraph
context, not just keyword hits): Tents, Plain View Doctrine, Aerial and Enhanced Surveillance,
Curtilage, Private and Foreign Searches, Reasonable Expectation of Privacy, Abandonment,
Collective Knowledge and the Fellow-Officer Rule, Terry Stops and Reasonable Suspicion, Arrest in the
Home, Border Searches, Inevitable Discovery and Independent Source, Standing to Challenge a Search,
Good-Faith Exception, Use of Force, Qualified Immunity, Brady and Giglio, Entrapment, Eyewitness
Identification, Sixth Amendment Right to Counsel, Lineups, Stop-and-Identify, Electronic Surveillance
and Title III, Automobile Exception, the four "Role-based … no SCOTUS" home-entry pages, and the
digital-surveillance/index pages.

## Grep patterns used (ripgrep 15, `-i`, across `content/**/*.md`)
**Pass 1 (core R7.4 vocabulary):**
- no-court: `no (court|circuit|federal court|appellate court|published|reported|state court|lower court|supreme court|controlling|binding|precedent|reported decision|published decision)`, `not one court`, `no court has`
- first-impression: `first impression`, `novel (question|issue|legal question)`
- split: `\bsplit\b`, `circuits? (are|remain|have)? ?(divided|split)`, `(majority|minority) (rule|view|position|approach)`, `circuit (conflict|split)`, `\bdisagree`, `in tension`, `\bdiverge`, `are divided`
- not-decided: `(has|have|had|has not|have not) not (yet )?(decided|addressed|reached|resolved|held|considered|determined|squarely)`, `did not (decide|reach|address|resolve|consider)`, `declined to (decide|address|reach|resolve|consider)`, `left open`, `reserved (the question|judgment|decision|this question|that question)`, `expressly reserved`, `has yet to`, `have yet to`
- open: `open question`, `remains? (open|unsettled|unresolved|an open)`, `unresolved`, `unsettled`, `not yet (been )?(resolved|decided|settled|addressed)`, `yet to be (decided|resolved|settled|addressed)`, `still (open|unresolved|unsettled)`
- never: `never (held|decided|addressed|resolved|reached|squarely|expressly)`, `has never`, `have never`

**Pass 2 (paraphrased negatives):** `declined to (extend|adopt|follow|graft|reach|decide|resolve|say|hold)`, `did not (reach|resolve|adopt|extend|address)`, `(has|have) not addressed`, `no controlling (scotus|supreme court|precedent|rationale|rule|federal|circuit|answer)`, `circuits? (divide|diverge|are divided|are split|remain divided|remain split|split|have divided|have split)`, `no (majority|binding circuit rule|controlling rationale|single federal answer|controlling answer|controlling precedent)`, `left (unresolved|unanswered|undecided|open)`, `\breserved\b`, `no (scotus|supreme court)`, `cert\.? denied`, `so far declined`, `have not agreed`, `not (yet )?(uniform|aligned|settled)`, `yet to (squarely|hold|decide|reach|address)`, `undecided|undivided|unmapped`

**Pass 3 (frontier/consensus paraphrase):** `live frontier|new frontier|unsettled frontier|developing frontier|emerging frontier|the frontier`, `no consensus|consensus (has not|is not)|no clear (rule|answer|consensus)`, `in flux|working (it|these|the)? ?out|case by case|case-by-case`, `jurisdiction-dependent|jurisdiction-specific|depends on where you stand`, `few courts|little authority|scant authority|sparse|no case (has|law)`, `courts have not|courts remain|courts are (still )?(working|split|divided)`, `not (been )?(extended|resolved|settled|decided|reached|mapped|addressed)`, `no representative|do not assume how`, `no nationwide|nationwide (rule|law)|national rule|settled national|settled nationwide`, `has never (required|addressed|extended|construed|held)`

## Exclusion classes (skipped, with reason) — flagged for the orchestrator
1. **HTML comments (`<!-- … -->`)** — not rendered final prose. Many carry "No controlling SCOTUS … (GAP-03b)" build notes; excluded per "final prose" scope.
2. **Lake / build-verification status meta** — "subsequent treatment not yet machine-verified", "No validated negative treatment is recorded in the lake (0 confirmed negative edges …)", "current treatment/progeny not yet independently verified". These are R15/citator status, not doctrinal absence claims.
3. **Pedagogical / glossary definitions** — `The Federal Court System.md` (what a "circuit split" *is*; "cert denied sets no precedent"), `Common Legal Terms.md` (plurality-split example; dissent definition), `Verifying Good Law.md` ("flag the split"). These explain the concept, they don't assert a specific doctrine is open/split.
4. **`case-by-case` / `totality`** — a test-*type* (vs. categorical), not a negative/absence claim (Lange, McNeely, Atwater, Robinson, Winston, Knock-and-Announce, etc.).
5. **`split-second`** — officer-perception phrasing (Graham/Ryburn/Nieves), not a circuit split.
6. **Completed limiting holdings "declined to extend/adopt/follow [doctrine]"** — settled negative holdings verifiable in-opinion, not open frontiers: e.g. Bivens/Cady/Caniglia/Carpenter/Case-v-Montana/Havens/Milam/Penn-Bd/Perry/Cobb/Ziglar/Caceres/Payne, and the Egbert First-Amendment-Bivens recital. **Orchestrator call:** if you want these treated as doctrinal-state negatives ("is Bivens still closed to new contexts?"), say so and I will add them; I excluded them as settled.
7. **QI "no precedent clearly established / no precedent squarely governed"** — case-specific clearly-established findings (Tahlequah, Rivas-Villegas, Sheehan, Brosseau, Jimerson-as-QI-holding). I DID include the paired "the Court did not decide whether a constitutional violation occurred" (QI merits-skip) as `not-decided`.
8. **Holding-quote negatives** ("This Court has never indicated…", "We have never approved…", "has never been enough") — the Court's own rule statement, not an open question.

## Ambiguities / orchestrator rulings requested
- **Mirror rows.** I included 8 `Case Index.md` holding mirrors and several frontmatter `holding:`/`scope_note:` rows that restate a case-page prose claim (same `subject`, different `file:line`). Kept because the brief says enumerate EVERY negative claim in final prose and Case Index is a heavily-read surface; they group cleanly by `subject` for two-direction search. Drop if you want one-per-proposition.
- **"No-SCOTUS recent-developments markers"** (class `no-court-has`) — the recurring "Circuit/state developments only; no SCOTUS" section convention (N5) appears on ~9 doctrine pages. Included as genuine field-level absence claims; they are template-shaped, so a reviewer may want to batch-verify them as one family.
- **Resolved-but-stated** claims — several reserved questions the prose itself notes were later answered (Brown→Hiibel, Knights→Samson, Harris→Opperman, Imbler→Buckley, Smith v. Illinois→Davis, Davis v. Mississippi→Hayes, Chatrie "RESOLVES the former split"). Kept (the two-direction search should confirm the stated resolution still holds), flagged here so they aren't mistaken for live gaps.
- **Post-capture 2026 anchors** (Chatrie, Case v. Montana, Smith 2024, Porter, Robinson v. Commonwealth) carry absence claims tied to very recent decisions — highest value for the CL/web recency two-direction search.

## Files
- `_run/s9/p4/absence-claims.jsonl` — 181 rows (deliverable).
- `scratchpad/build_abs.py` — anchor-slice builder + verbatim/schema validator (reproducible).
