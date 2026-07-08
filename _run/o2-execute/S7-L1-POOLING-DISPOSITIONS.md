# S7 mini-lane L1 — horizontal collective-knowledge pooling: brief-mention dispositions

- **lane / model:** o2-execute mini-lane L1 / `claude-opus-4-8`
- **generated:** 2026-07-08
- **spec authority:** S7 R9 (named per-page fixes) + §11 research annex; `_overhaul2/S7-CHANGELIST.md`
  item 16 — signed named split: *horizontal collective-knowledge pooling = named split
  (Massenburg / communication-nexus circuits **Chavez/Ramirez/Nafzger/Ibarra** / Cook imputation,
  reserved by Balser (2023))*, `Pringle` suspect-side only.
- **identity method:** CourtListener MCP, SEARCH-first, cluster/opinion ids resolved from search
  results (never navigated by guessed ids). **0 REST calls** (per task directive). Read from the
  MCP cache lane only.
- **machine artifact:** `_run/o2-execute/S7-L1-POOLING-DISPOSITIONS.jsonl` (consumed by
  `_overhaul2/scripts/build_coverage_ledger.py` section 6c; `assemble:false` rows are
  documentation-only and NOT assembled).
- **provenance rule honored:** the coverage ledger is regenerated PROGRAMMATICALLY
  (`build_coverage_ledger.py --write`), never hand-edited. The assembler was extended with a
  small S7 loader (section 6c) so the new artifact enters as three brief-mention rows.

## Dispositions

### 1. United States v. Nafzger — brief-mention (NEW terminal)
- **canonical cite:** 974 F.2d 906 (7th Cir. 1992); pincite 913–14.
- **cluster / opinion:** 590298 / 590298. **docket:** 91-3292. **court:** ca7. **year:** 1992.
- **dispatch expectation:** 974 F.2d 906 (7th Cir. 1992) — **CONFIRMED exact.**
- **evidence (MCP opinion read 590298):** applies the *Hensley* collective-knowledge doctrine to a
  jointly-investigating team; the acting officer (Argue), a member of the team investigating
  Nafzger, was entitled to rely on the team's collective knowledge though not personally aware of
  the underlying facts; the court rejected the defendant's narrow reading of imputed knowledge and
  endorsed minimal-communication imputation (quoting the 11th Cir. *Wilson* standard: "when a group
  of officers is conducting an operation and there exists at least minimal communication between
  them, their collective knowledge is determinative of probable cause").
- **gate rationale:** brief-mention — named in doctrine prose as a communication-nexus circuit-split
  member; no standalone page warranted.
- **pointer:** `seizures/Collective Knowledge and the Fellow-Officer Rule.md`.

### 2. United States v. Ibarra — brief-mention (NEW terminal)
- **canonical cite:** 493 F.3d 526 (5th Cir. 2007); pincite 530.
- **cluster / opinion:** 50973 / 50973. **docket:** 06-50783. **court:** ca5. **year:** 2007.
- **dispatch expectation:** "likely 10th Cir." — **CORRECTED to 5th Cir.** The collective-knowledge /
  communication-nexus *Ibarra* is the 5th-Cir. 2007 case (opinion 50973). Namesakes refuted:
  *Oscar Ibarra v. State of Iowa* (Iowa Ct. App. 2015, cluster 3150126) is not a collective-knowledge
  case; *United States v. Ibarra-Sanchez*, 199 F.3d 753 (5th Cir. 1999) is a distinct caption
  (cited in *Chavez*), not the signed "Ibarra".
- **evidence (MCP opinion read 50973):** states the collective-knowledge doctrine imputes probable
  cause where there is "some degree of communication between the arresting officer and an officer who
  has knowledge of all the necessary facts" (493 F.3d at 530); applied to impute Agent Smith's
  probable cause to Trooper McGuairt given communication among the investigating officers. Squarely
  the communication-nexus position.
- **gate rationale:** brief-mention — named in doctrine prose as a communication-nexus circuit-split
  member; no standalone page warranted.
- **pointer:** `seizures/Collective Knowledge and the Fellow-Officer Rule.md`.

### 3. United States v. Balser — brief-mention (NEW terminal)
- **canonical cite:** 70 F.4th 613 (1st Cir. 2023). **docket:** 21-1813. **court:** ca1. **year:** 2023.
  (No reporter star-pagination pincite: the opinion text carries slip pagination only; cited at the
  case level. Reservation content read directly — see evidence.)
- **cluster / opinion:** 9407224 / 9402700.
- **dispatch expectation:** "6th Cir. 2023, F.4th" — **CORRECTED to 1st Cir. 2023** (70 F.4th 613).
- **evidence (MCP opinion read 9402700):** labels the two collective-knowledge categories
  (vertical/horizontal, citing *Massenburg*, *Chavez*); notes courts "are split over how broadly to
  apply the horizontal outgrowth"; states the First Circuit "has yet to squarely address the
  'maximum reach' of the so-called horizontal collective knowledge doctrine (i.e., aggregation of
  information among multiple officers)," citing *United States v. Fiasconaro*, 315 F.3d 28, 36 (1st
  Cir. 2002) (in turn citing *United States v. Cook*, 277 F.3d 82, 86); resolves Balser's own stop as
  vertical, not horizontal, and therefore does not reach the pure-aggregation question. This is the
  case that reserves the pure-horizontal question — the "Balser" of the signed Cook-Balser pair.
- **gate rationale:** brief-mention — named in doctrine prose as the case reserving pure horizontal
  aggregation; no standalone page warranted.
- **pointer:** `seizures/Collective Knowledge and the Fellow-Officer Rule.md`.

### 4. United States v. Cook — IDENTITY CORRECTION (assemble:false; ledger row NOT overwritten)
- **operative authority for the split:** *United States v. Donald Cook*, 277 F.3d 82, 86 (1st Cir.
  2002); cluster/opinion 776186.
- **evidence (MCP opinion read 776186 + Balser's inline characterization):** recognizes a LIMITED
  horizontal pooling — considering "the collective knowledge of all of the officers who participated
  in the stop" who were present and directly involved — while cautioning (via *Meade*, 110 F.3d at
  194) that a broad rendition of the principle could promote illegal searches. This is the imputation
  approach *Balser* reserves the outer reach of.
- **discrepancy found:** the pre-existing R11 ledger row with caption "United States v. Cook" is
  **cluster 3165557 = United States v. Oshan Cook (2015, no reporter cite)** — a DIFFERENT case,
  sourced from `R8-NONPAGE-LEDGER:mentions_and_bullets` with rationale "collective-knowledge
  application; no split/omitted question" and a pointer to this same page (which did not in fact name
  any Cook until this lane).
- **why not overwritten here:** the assembler dedupes by normalized caption; a new "United States v.
  Cook" brief-mention row would silently merge into the Oshan row without correcting its cluster.
  Correcting the R8 lake/ledger identity (3165557 → 776186) is out of this writer-lane's remit and is
  a coverage-machinery repair. Per the fail-closed / writer≠checker rule, it is **reported, not
  improvised.**
- **effect on gates:** LINT-17 coverage of the caption "United States v. Cook" already holds via the
  existing row, so naming the (verified) Donald Cook on the page passes. The page cites the verified
  277 F.3d 82, 86 (1st Cir. 2002).
- **OWED to S2 repair lane / orchestrator (analogous to the batch-8 D.C. v. R.W. lake-flip):** re-key
  the "United States v. Cook" ledger/lake identity from cluster 3165557 (Oshan Cook 2015) to cluster
  776186 (Donald Cook, 277 F.3d 82 (1st Cir. 2002)); or, if Oshan Cook is an independently-wanted
  mention elsewhere, split the caption. Verified target recorded in the `.jsonl` (assemble:false row).

## Page patch (surgical — `content/seizures/Collective Knowledge and the Fellow-Officer Rule.md`)
- **Ramirez bullet (communication-nexus lead):** appended *Accord* *Nafzger*, 974 F.2d 906, 913–14
  (7th Cir. 1992) and *Ibarra*, 493 F.3d 526, 530 (5th Cir. 2007) plain-italic with parenthetical
  holdings, next to the existing Ramirez/Chavez roster.
- **New Cook–Balser bullet** (after *Chavez*): *Cook*'s limited on-scene pooling (277 F.3d 82, 86)
  and *Balser*'s reservation of the maximum reach (70 F.4th 613 (1st Cir. 2023), resolved on the
  vertical prong), with ⚖ Circuit-split + Binding-in-circuit 1st Cir. labels and both [opinion] links.
- **Closing synthesis:** communication-nexus parenthetical expanded to *Ramirez*; *Nafzger*; *Ibarra*
  (with *Chavez* leaving the pure question open); added the First Circuit *Cook* → *Balser*
  reservation sentence.
- **Sources:** added *Nafzger* (913–14), *Ibarra* (530), *Cook* (86), *Balser* entries.

## Ledger regeneration + gates
- **build_coverage_ledger.py --write:** RESULT **PASS**. Partition **243 → 246 distinct captions**
  (brief-mention 55 → 58: +Nafzger, +Ibarra, +Balser). Machine partition check PASS; conflicts 0,
  row-errors 0; authored verified 148/148/148; folded-alias survivors ok 8/bad 0.
  `corpus_mention_baseline` unchanged at 56 (the three new captions are cu_allow rows, excluded from
  the baseline scan; the page's Cook mention resolves to the existing row).
- **LINT-17 corpus:** **0** (the three new names resolve to the new terminals; Cook to the existing
  row).
- **run_all:** 7904 → **7912** (+8), delta **entirely LINT-5 MEDIUM** (2816 → 2824): the four new
  page-less lower-court cases each named once in a bullet/accord-mention and once in Sources
  (8 "bare case name is not a [[wikilink]] to its case page" notices — the identical N7/D13 class as
  the existing *Massenburg/Ramirez/Chavez/Trent* entries). **HIGH unchanged (4825); no new HIGH.**
- **LINT-15 / LINT-16 (touched page, standalone):** **0 / 0.**
- **LINT-2 / LINT-10 (touched page):** **0 / 0** (quotes pincited; em-dash per-block budget held —
  each new bullet carries exactly one counted em-dash; authority-weight labels A8-exempt).
- **build:** `npx quartz build` exit **0** — 721 input files, 2777 emitted (structural counts
  unchanged from baseline).

## Notes for the orchestrator
- **Two dispatch mislabels corrected by identity verification:** Balser is **1st Cir. 2023**, not
  6th; Ibarra is **5th Cir. 2007**, not 10th. Both corrections are load-bearing (Balser being 1st Cir.
  is what ties the reservation to the 1st-Cir. *Cook*).
- **Cook identity repair owed to S2** (cluster 3165557 Oshan → 776186 Donald); reported, not
  self-adjudicated.
- **build_coverage_ledger.py change** is the programmatic ingestion loader (section 6c) for the new
  signed artifact — required because hand-editing the ledger is banned; it is in the diff scope
  alongside the ledger, the artifact, and the page.
