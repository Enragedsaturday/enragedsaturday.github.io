# COH-B disposition summary (Wave-F B1/B2, callout↔registry gate-a)

Lane: COH-B · model claude-opus-4-8 · WRITE-SCOPE: content/ doctrine callouts (ruled adds only) + `_run/s9/p4/`.
Governing rulings: **P4-04** (callout↔registry deep-equal is a spec-vs-build convention conflict; no mass rewrite; framing tolerance; systemic → C1/P5) and triage rows **B1/B2/B3**.
Registry (`_overhaul2/points/registry.yaml`) treated **READ-ONLY** — every registry-side defect filed as a note, zero registry edits.

## Coverage (deterministic)
- Assigned: **78** (14 content-divergence + 3 no-callout + 61 cite-divergence).
- Examined: **78/78**. Skipped: **0**. needs_cl: **0** (all decided from lake / case pages / registry; no live CL).
- Outputs: `COH-B-dispositions.jsonl` (78) · `COH-B-fixes.jsonl` (1) · `COH-B-registry-notes.jsonl` (62, → P5 handoff).

## Disposition tally
| disposition | n | where |
|---|---|---|
| DISMISS (framing tolerance / correct-scope / hub-index convention) | 15 | 13 content + 2 no-callout |
| REGISTRY-NOTE (no edit; P5 deep-equal handoff) | 62 | 1 content (miranda-waiver) + 61 cite |
| PAGE-FIX (callout add) | 1 | remedy.exclusionary |

## B1a — 14 content-divergence
**0 callout fixes.** All 14 home-page callouts are legally correct statements; none carries a substantive error, so the high bar for editing verified content is not met.
- **13 DISMISS (N6 framing tolerance, P4-04):** proof.proof-ladder, search.rep, search.trespass, search.open-fields, **search.digital.geofence-warrant** (registry statement is correctly scoped to the categorical/particularity question — the threshold-search holding in the callout belongs to the *separate* node `search.digital.geofence-threshold`, registry:144), seizure.person.when-seized, seizure.property, search.person.sia, search.person.sia-cellphone, search.person.sia-alcohol, liability.section-1983, liability.retaliatory-arrest, liability.malicious-prosecution. Each divergence is compression/reorder/synonym/pincite-glyph with identical black-letter + identical anchors (per-row reasons in dispositions.jsonl).
- **1 REGISTRY-NOTE — confession.miranda-waiver:** genuine *scope* divergence, not mere paraphrase. Node `why` (registry:656) defines the node as "waiver/invocation/Edwards **+ Miranda-fruits** rule"; the registry statement carries the Miranda-fruits line (Elstad/Seibert/Patane) while the page callout realizes only the waiver/invocation half (Minnick/Edwards/Mosley/Thompkins/Davis) and adds silence-invocation cases the registry omits. Both are correct Miranda law → no callout fix, no registry edit; recorded for P5 to decide which half the home callout must realize.

## B1b — 3 no-callout
Empirical convention check: **77/80** registry nodes carry a `> [!rule]` callout on their home page; only these 3 lack one.
- **foundations.fourth-amendment-framework → DISMISS (hub convention).** type=hub; page self-describes as "the map, not a rule you apply directly" (line 22); registry `why` (registry:47) = framework is transcluded/referenced across the analysis pages. Hub/map landings carry no callout; the rule is realized on the analysis pages.
- **warrant.requirement → DISMISS (index convention).** type=index; registry `why` (registry:338) = umbrella proposition "homed to the category landing and **realized in the children’s rule callouts**." The four requisites live in the child callouts (PC-in-Affidavit, Neutral Magistrate, Particularity, Franks, Knock-and-Announce…); the Leon good-faith clause is homed at *The Good-Faith Exception.md* (`^rule-good-faith`, I3 note). No callout owed on the landing index.
- **remedy.exclusionary → PAGE-FIX (callout ADDED, loop:2).** type=doctrine; registry `why` (registry:596) = "the overview STATES it." Rule was present in prose (index.md:23) but lacked the `[!rule]` wrapper. Added `^rule-exclusionary` after the H1, deep-consistent with the registry statement + authorities, matching the sibling `^rule-fruits`/`^rule-good-faith` format.
  - **Loop-2 (codex non-author refutation applied).** (1) *Scope:* the loop-1 categorical framing omitted applicability limits; added a compact scope clause — case-in-chief only; as a remedy (not a right) it is bounded by a cost-benefit test and **does not reach grand-jury proceedings** (Calandra's own holding), with the forum/cost-benefit boundaries routed to [[The Good-Faith Exception]] (the page's corpus-homed owner of those boundaries). (2) *Fruits pin:* loop-1 falsely pinned the **fruits** clause to Weeks *393 / Mapp *655 — but those pins support the **core bar** (primary evidence), and Calandra's own text at **\*347** (108898.txt L39) attributes fruits to *Wong Sun* 371 U.S. 471 / *Silverthorne* 251 U.S. 385. Re-anchored: fruits clause retained (deep-consistent with registry statement) but routed by pointer to [[Fruits & Attenuation]] (^rule-fruits owns Wong Sun/Silverthorne); no fruits authority pinned in this overview callout.
  - **Retained pins re-verified against `~/cssi-lake/cache/text` with offsets:** **Weeks** 232 U.S. 383, **393** — 98094.txt L153 (star `*393`; "…is of no value, and…might as well be stricken from the Constitution"; core bar). **Mapp** 367 U.S. 643, **655** — 106285.txt L52 (star `*655`; "all evidence obtained by searches and seizures in violation of the Constitution is…inadmissible in a state court"; core bar → states). **Calandra** 414 U.S. 338, **348** — 108898.txt L44 (star `*348`; "a judicially created remedy…through its deterrent effect, rather than a personal constitutional right"; deterrence-remedy/not-a-right). Corpus ^pin-393 / ^pin-655 / sibling ^rule-good-faith concur.

## B2 — 61 cite-divergence (class review, P4-04(ii))
**0 page-side cite fixes → all 61 REGISTRY-NOTE.** Subclasses: 16 `pincite_drop` (registry carries first-page cite where the callout pincites) + 45 `different_authority` (registry selects a different/narrower authority subset than the callout).
- The page-fix trigger is a *wrong* callout cite. Spot-checks of the unusual/high-risk callout cites all resolve to real, correctly-attributed corpus case pages — **Labron** 518 U.S. 938, **Gooch** 6 F.3d 673, **Steagald** 451 U.S. 204, **Austin** 509 U.S. 602, **Flores-Montano** 541 U.S. 149, **Illinois v. Rodriguez** 497 U.S. 177, **Quarles** 467 U.S. 649, **Wilson v. Arkansas** 514 U.S. 927. No fabricated or misattributed callout cite found.
- Registry-only additions sampled (Adams v. Williams 407 U.S. 143, Alderman 394 U.S. 165, Lafayette 462 U.S. 640 / Bertine 479 U.S. 367, Culley 601 U.S. 377) are all apt for their propositions — registry cites are *different/poorer*, never *wrong*. Consistent with the compact-statement convention; full per-node cite lists preserved in the registry-notes for P5 reconciliation.

## Notes for the orchestrator
1. **No registry edits made** (read-only honored). 62 registry-notes staged for the P5 deep-equal handoff (C1). They are informational; none asserts a legal defect in the registry, except the one *scope* observation on miranda-waiver.
2. **One content write applied** (remedy.exclusionary callout add) — sanctioned by B1/P4-04 as the doctrine-type no-callout remedy. **Loop-2 landed** after codex non-author re-review REFUTED loop-1 (missing applicability limits + fruits falsely pinned to Weeks/Mapp); both grounds fixed, all retained pins re-verified with cache offsets (see B1b). Writer≠checker: the loop-2 callout still needs a non-author re-review pass before close.
3. The 2 `callout-registry-cosmetic` rows (proof.reasonable-suspicion, proof.probable-cause) are **out of my 78** and untouched.
4. `remedy.exclusionary` home is `index.md` but classified type=doctrine (frontmatter `type: doctrine`) — the callout is owed there despite the filename, unlike the two true landing pages (warrant/index = type index, framework = type hub).
