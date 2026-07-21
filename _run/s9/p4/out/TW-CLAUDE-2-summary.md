# TW-CLAUDE-2 summary (Claude lane, tripwire 13-cat re-run, categories 6-10)

- Lane: `TW-CLAUDE-2` | model `claude-opus-4-8` | branch `overhaul2/execute`
- Mandate (P4-07/P4-08): blind, WebSearch-only frontier re-derivation of the must-cover caselaw
  frontier for units 6-10. Did NOT read corpus, lake, or `_run/s9/p4/out/codex/*`. WebSearch only
  (no WebFetch, no CL) to preserve blind two-key independence for the DIFF/serial-CL lanes.
- Method per unit: enumerate SCOTUS + published federal circuit decisions 2024-01-01 -> 2026-07-21
  a rigorous federal search-and-seizure instructor wiki MUST cover, plus pre-2024 cases recent
  (2024-2026) commentary treats as newly doctrine-shaping. Thread bound: stop a thread after two
  successive null searches; soft cap ~15 searches/unit. Published-only for circuit rows
  (unpublished dispositions dropped, e.g. 5th Cir. No. 24-20243 unpub).
- Output: `TW-CLAUDE-2-candidates.jsonl` (12 rows, schema-validated) + this file.

## Candidate counts by unit
- exclusionary: 3 | confessions: 3 | counsel: 1 | fairtrial: 2 | foundcraft: 3  (total 12)

## Coverage ledger (searches / stop conditions)

### Unit 6 EXCLUSIONARY, REMEDIES & STANDING  (10 searches)
Threads: good-faith SCOTUS; Strieff/attenuation; SCOTUS-2025-term 4A; inevitable-discovery/independent-source;
standing/REP; Herring/Davis good-faith; +2 caption-confirms (1st Cir 25-1041, Ray/Chatrie); attenuation-circuit.
- FILED: **United States v. Parkerson** (5th Cir. 2025, trespasser no-REP standing);
  **United States v. Gonzalez-Arocho** (1st Cir. No. 25-1041 published, good-faith rejected / warrant-scope);
  **Chatrie v. United States** (SCOTUS No. 25-112, 2026 — LOW; digital-umbrella crossover, likely already in corpus).
- STOP/NULL: attenuation-circuit thread -> null (only Strieff 2016 + state cases); inevitable-discovery/
  independent-source -> null at federal-circuit grain (only Md. COSA + district cases surfaced). Both bounded out.
- Note: an early search's AI-summary asserted a "U.S. v. Ray (4th Cir. 2025)" good-faith phone case; the
  caption-confirm search could NOT substantiate it (results collapsed into Chatrie). DROPPED as unverified.

### Unit 7 CONFESSIONS / INTERROGATION / FIFTH AMENDMENT  (8 searches)
Threads: SCOTUS Miranda/5A; Vega progeny; custody/interrogation circuit; juvenile voluntariness; Pence confirm;
5th-Cir implied-waiver; Weaver confirm; Seibert two-step circuit.
- FILED: **United States v. Pence** (2d Cir. No. 24-1025-cr published, 2026 — custody: FBI-vehicle dawn-warrant
  questioning non-custodial); **United States v. Weaver** (5th Cir. No. 25-60269 published, 2026 — implied
  Miranda waiver / Berghuis; suppression reversed + circuit-precedent reversal on waiver-based remands);
  **Vega v. Tekoh** (597 U.S. 134 (2022) — LOW; pre-2024 doctrine-shaping, Miranda-not-a-1983-basis).
- STOP/NULL: Vega-progeny-circuit -> null; juvenile-voluntariness -> null at federal grain (Texas/Arizona/
  legislation only); Seibert-two-step-circuit -> null. All bounded out.

### Unit 8 RIGHT TO COUNSEL (6A)  (5 searches)
Threads: SCOTUS 6A/IAC; Massiah/informant circuit; Villarreal disposition confirm; choice-of-counsel/Lafler-Frye
circuit; Massiah attachment circuit.
- FILED: **Villarreal v. Texas** (SCOTUS No. 24-557, 607 U.S. ___ (2026), 9-0 — qualified overnight-recess
  conferral order barring only own-testimony discussion does not violate 6A right to counsel; Geders/Perry line).
- STOP/NULL: Massiah/deliberate-elicitation-informant circuit -> two successive nulls (foundational only) =>
  thread closed per stop rule; Lafler/Frye plea-stage-IAC circuit -> null. Unit is tangential to a search-and-
  seizure corpus; Villarreal is the single clear SCOTUS must-cover.

### Unit 9 FAIR-TRIAL & RELIABILITY  (5 searches)
Threads: Brady/Napue SCOTUS (Glossip); Smith v. Arizona confrontation/forensics; eyewitness-ID due process;
Brady/Giglio circuit; forensic Daubert/firearms.
- FILED: **Glossip v. Oklahoma** (SCOTUS No. 22-7466, 604 U.S. ___ (2025) — Napue duty to correct false
  testimony; conviction/death sentence reversed); **Smith v. Arizona** (SCOTUS No. 22-899, 602 U.S. ___ (2024),
  9-0 — Confrontation Clause bars surrogate analyst conveying absent analyst's basis-testimony for its truth).
- STOP/NULL: eyewitness-ID-due-process -> null at federal grain (N.M./Wash. state supreme courts only);
  Brady/Giglio-circuit -> null (foundational only); forensic-Daubert/firearms -> only DISTRICT-court rulings +
  the Dec-2023 FRE 702 amendment (rule change, noted; not a case, likely out of corpus scope). Bounded out.

### Unit 10 FOUNDATIONS residual + INSTRUCTOR REFERENCE  (8 searches)
Threads: NCMEC/CyberTipline government-agent circuit; special-needs/admin/DNA; Google-Photos-CSAM caption;
hash-match/private-search circuit; legal-research/citator AI-citation; Barnes v. Felix; incorporation; OT2025 sweep.
- FILED: **United States v. Lowers** (4th Cir. No. 24-4546 published, 2026 — hash-match alone does not trigger
  private-search exception; REP in cloud files; **this is the P4-07 tripwire PREDICATE, independently re-surfaced
  here** => two-key confirmation of the discovery miss); **United States v. Brillhart** (11th Cir. published,
  2026-07-09 — hash-match = private search, warrantless viewing within scope; opposite side of the split;
  MEDIUM, P4-07 already flagged as non-charging R7.1 currency); **ABA Formal Op. 512 (2024) + AI hallucinated-
  citation sanctions wave** (LOW — instructor-reference/citator-practice node; likely R12 maintenance handoff,
  not corpus caselaw).
- STOP/NULL: incorporation (14A selective incorporation) -> null (no 2024-2026 incorporation decision);
  special-needs framework -> null at recent-federal grain (foundational Edmond/Ferguson + 23andMe/DNA policy note).
- NOT FILED (deliberately out of this packet's unit scope; noted for orchestrator routing to categories 1-5 /
  already-run I5 legs, NOT enumerated as my rows):
  - **Barnes v. Felix** (SCOTUS No. 23-1239, 604/23-1239, May 15 2025, 9-0) — 4A excessive-force reasonableness
    is totality-of-circumstances, rejecting the 'moment of threat' rule. Seizure-merits (cat 1-2) + civil-remedies
    (an I5 unit that already ran); not units 6-10.
  - **Case v. Montana** (SCOTUS, Jan 14 2026) — warrantless entry for emergency aid; warrant-exception (cat 1-5).
  - **State v. Rauch Sharak** (Wis. Sup. Ct. 2026) & **People v. Carson** (Mich.) — STATE courts; excluded
    (mandate = SCOTUS or published federal circuit only). Surfaced repeatedly alongside the private-search split.

## Ambiguities flagged for the orchestrator
1. **Private-search cluster (Lowers/Brillhart) unit assignment.** Filed under `foundcraft` because P4-07 names
   the node as the government-actor/NCMEC-agency/private-search line and the tripwire fired on exactly this split.
   They equally live in the `digital` umbrella (I5 unit already run). If the DIFF lane prefers the digital home,
   re-key; either way both are must-cover and Lowers is the predicate.
2. **Chatrie (SCOTUS 2026) double-jeopardy with the digital I5 leg + existing corpus.** Filed LOW only for its
   exclusionary/standing crossover (the 4th Cir en banc rested on the good-faith exception). Expect DIFF to
   dedupe against the digital re-run and the Chatrie/Zorn corpus entry.
3. **Instructor-reference / AI-citator row.** Not caselaw; it satisfies the literal 'legal-research/citator-
   practice changes 2024-2026' node in unit 10's charter but is almost certainly outside the corpus's doctrinal
   caselaw scope. Recommend R12 maintenance-handoff disposition rather than an S6 R8 born-draft.
4. **Coverage-check, not miss, for the LOW/pre-2024 rows** (Vega, Chatrie): filed so the DIFF lane can confirm
   corpus presence; a two-key gate-pass here would only matter if the corpus lacks them.

## Deterministic coverage statement
- Units assigned: 5 (6 exclusionary, 7 confessions, 8 counsel, 9 fairtrial, 10 foundcraft).
- Units examined: 5/5. Searches run: 36 total (6:10, 7:8, 8:5, 9:5, 10:8) — all within the ~15/unit cap.
- Candidates filed: 12 (validated: 12/12 well-formed, correct lane/model/unit enum).
- Threads stopped on null (bounded, not truncated): attenuation-circuit, inevitable-discovery-circuit (u6);
  Vega-progeny, juvenile-voluntariness, Seibert-two-step (u7); Massiah-informant (2 consecutive), Lafler/Frye (u8);
  eyewitness-ID, Brady/Giglio-circuit, forensic (district-only) (u9); incorporation, special-needs (u10).
- Items skipped with reason: state-court decisions (Rauch Sharak, Carson, N.M./Wash. eyewitness) — outside
  SCOTUS/federal-circuit mandate; unpublished dispositions (5th Cir. 24-20243) — published-only rule; district-
  court forensic rulings + FRE 702 amendment — not appellate caselaw; unverified caption (purported "U.S. v.
  Ray" 4th Cir.) — could not substantiate. Barnes v. Felix / Case v. Montana — real SCOTUS must-covers but in
  categories 1-5, out of this packet's units (noted above for routing).
