# SPEC S7 — Doctrine Production (brief-first rewrite)

**Status: APPROVED (signed at interview, 2026-07-03).**
gates: S1 (constitution), S2 (lake/projection), S3 (tree + registry + placed nodes), S5 (entry
models — the skeleton S7 pages conform to), S6 (R8 authoring pipeline + R11 coverage ledger).
Authoring order only; execution = wave 3 (RUNBOOK §3, COH-04), interleaved with S6's authoring
waves.

Interview: 2026-07-03 (2 rounds + open floor; 8 user decisions D1–D8) + visible self-interview
(SD1–SD8, full text in the thread).
Exhibits: pattern page `content/7-exceptions-warrant/7b-pc-not-needed/Knock and Talk.md` (live on
the branch — commits `e0935ce` + `4b48a4a`, served on :8080; **the normative template reference**,
user D1) · per-page change-list `_overhaul2/S7-CHANGELIST.md` (the run ledger; tiers assigned,
user-signed with this spec) · research annex (§11).

Precedence: this spec wins over RUNBOOK §4-S7 and the S7 wrapper (RUNBOOK §0 stack).

---

## 1. Objective

Produce or rewrite every doctrine, narrative, craft, and reference page — 48 existing pages plus
~44 new-prose units from S3's placed-empty and split nodes — through draft → review → verified:
brief-first under one signed template (the pattern page), tiered depth (user D4/D6), every carried
assertion re-verified (no verification inheritance, D8), every named per-page fix and corpus pass
from the audit landed, and every rewrite-time case discovery routed through S6 R8's pipeline. The
deliverable is a corpus in which the prose layer is as verified as the case layer beneath it.

## 2. Scope

### 2.1 In scope (S7 owns)
- Rewrites of all 46 substantive non-case pages that S7 touches (2 reference no-ops) + new prose
  for the S3 placed-empty/new-split nodes (`S7-CHANGELIST.md` Tables 1–2; ~77 authored units).
- The doctrine-brief **internal template** (R1) inside S5 R1's H2 skeleton; tier system (R2).
- The corpus-wide passes (change-list Table 3): TEACH-03 four-tier pinpoint conversion (R5),
  TEACH-05 em-dash rewrite (R11), TEACH-02c pipeline-vocab strip (R8), TEACH-04d label-order
  fixes, TEACH-08 heading rename + move, TEACH-12a H1s, TEACH-12b legacy-skeleton migrations,
  running S5's mechanical converter (R15 staging).
- The named per-page fixes (R9): RUNBOOK §4-S7 fix-list (verify-then-apply, D3) + TEACH-04a–h +
  TEACH-01 relocations + LAW-05 + GAP-06 residue check.
- New coverage decided at interview: non-investigative person seizures, caretaking-adjacent (D5);
  SACO/constructive entry head-on (D7); emerging-tech depths (D6); GAP-03c §702 mention.
- S5 R5 point-status tables + reconciling prose for the 11 `limited` + 7 `overruled/abrogated`
  migrations (S5 Method 3).
- Fabrication-removal **prose surgery** at mention sites, coordinated with S6 R4.

### 2.2 Out of scope (owned elsewhere)
- Case-page authoring and existence verification (**S6**; S7 discoveries go through S6 R8 — no
  second page-mint). The lake, treatment data, projections (**S2**). The tree, re-homings,
  registry ids, category/sub-umbrella **overviews** (**S3** — SD7 boundary; S7 flags overview
  contradictions to the coherence pass, never rewrites them silently).
- Table/pill/hover rendering and mechanisms (**S4/S5**); S7 pages conform, never re-interview.
- Corpus-wide linking, transclusion mechanics, glossary (**S8**). Lint implementation in CI +
  review-panel mechanics + `^pin-N` remediation (**S9**).
- The officer-BLUF / field-application layer: **banned project-wide** (S1 §2.2 + R6); TEACH-04e
  migrates the survivors out (R7).

## 3. Requirements (each testable)

**R1 — The signed brief template (user D1; within S5 R1's skeleton).** Every Tier A/B doctrine
page renders, inside `## The Brief` and around it: `# Title` → *field-decisive question* (italic
line; S1 N9 judgment) → `[!rule]` callout (S5 R2: owned points, pincited, `^rule-` anchored) →
Brief in this move order: **what-it-is/is-not** → **the test up front** (elements/dimensions,
numbered where genuine) → **one doctrinal move per paragraph** (S1 A9 budget; splits get a
one-line flag in place) → **what-it-yields / limits** → **backstops & doctrine interfaces** →
**burden · standard of review · remedy** → **`**Apply it.**` numbered list** (S1 N3/N8) →
**`**Common pitfalls.**`** (S5 R10) → `## Lower-court developments` (S5 R11: role-tagged bullets,
**no meta intro line**; an optional **closing split-synthesis paragraph** is sanctioned — D1's
signed deviation) → tables (S5 R6) → `## Visual` → `## Sources` (S5 R12; trailing info in
parentheses, never em-dashed). Normative reference: the pattern page as committed. *Check:* H2
order = `AUTO:LINT-15` (S5); Brief-internal move order + callout quality = `CHECKLIST:D10` on
every page review (not machine-checkable); zero LCD meta intros (rides LINT-11 class 4).

**R2 — Tiered depth (user D4/D6).** Tier per page lives in `S7-CHANGELIST.md` (signed with this
spec): **A — exhaustive** (pattern-page depth; the doctrine anchors, ~30 units) · **B — standard
brief** (complete rule + test + pitfalls + lean LCD/tables, ~24) · **C — budgeted ½–1 page**
(question + callout + short brief + pitfalls + Key cases; thin/emerging/craft/reference, ~20).
D6: reverse-keyword/geofence + cell-site simulators = B; real-time CSLI, IGG, Title III = C.
Tier changes during production are **change-list amendments with a reason, never silent** (SD2).
Every tier still passes LINT-15 (optional sections absent, never reordered). *Check:* tier column
complete and user-signed; a sampled C page carries callout + pitfalls; no page balloons past its
tier without a logged amendment. `PROCESS` · `CHECKLIST`.

**R3 — No verification inheritance (user D8 scar; SD4).** A rewrite re-opens every proposition on
the page: legacy page-level `status: verified` confers **nothing** on carried prose; every
carried or new assertion re-enters the 10-gate protocol as if newly authored. Rewritten pages are
born `status: draft` (S5 R15 banner) and pass to S9 unpublished. The scar: the O1 "dog or
flashlight" pitfall rode a verified page into the S7 pattern rewrite (corrected `4b48a4a`).
*Check:* zero rewritten pages carry `verified` before S9; the S9 ledger shows gate rows for
carried assertions, not only new ones. `PROCESS` · S9 `AUTO` (status gate).

**R4 — Per-item citation support (user D8 scar; SD4).** In any enumerated or conjoined assertion
("X, Y, or Z crosses the line"), **each item** must be independently supported by a named
authority at the stated breadth, or the item is cut/qualified. Categorical verbs (breaks · voids
· requires · never · always) trigger an S1 R7 check against the cited holding's actual breadth.
*Check:* S9 G2 sampling runs per enumeration item (routed via RUNBOOK §4-S9 input (b)); the
flashlight fixture (old KT :24/:44 vs corrected page) is the committed exemplar. `CHECKLIST:D1/D2`.

**R5 — TEACH-03: the four-tier pinpoint conversion (absorbs LAW-04; sizing NUM-01).** Every
non-current-term slip-op pinpoint (76 hits / 20 doctrine pages + the 43/47 case pages,
coordinated with S2 A3 `pinpoint_status`) converts by the first tier that succeeds:
**T1 — CAP star pagination** in CL texts (coverage ends mid-2020) — mechanical, cite the star
page. **T2 — citing-case corroboration**: a compound search pairing the exact quote with a
reporter pincite in **≥2 independent citing cases**, consistent with the slip-page mapping —
cite the corroborated page. **T3 — paraphrase-downgrade**: no free pin source (post-2020 F.4th;
bound-volume-only SCOTUS with no T2 hit) — the **quote is replaced by a tight paraphrase** with a
case-level cite; no quotation survives without a located pin (G3/G4 fail-closed). **T4 — slip
pins stand only for the current SCOTUS term** (S1 R14). Every conversion records tier + evidence
pointer (provenance, into the S9 ledger row). Worked exemplars on the pattern page: Carloss
(T1, 818 F.3d at 995) · King (T2, 563 U.S. at 469–70, 10 co-occurrences) · French/Collins (T3).
*Check:* `slip op.` on a non-current-term authority greps to 0 post-rewrite (LINT-3-extended,
S9); sampled conversions re-verify **by tier** (RUNBOOK §4-S9 input (d)). `AUTO` · `PROCESS`.

**R6 — Per-page research protocol (D7 scar).** Per page, before prose: read current text →
re-verify carried assertions (R3) → resolve flagged doctrinal questions with authority →
**case-line expansion AND an officer-tactic vocabulary sweep** (surround-and-call-out, welfare
check, ruse entry, protective sweep, knock-and-announce variants, …) — tactics are not case
names, and case-keyed discovery alone misses them (SACO was nearly adjacent-only) → CL
confirmation through S2 stubs/lake; the Claude MCP lane is interactive spot-checks only and
**resolves `opinions[].id` from search before any document read** (cluster-id trap, RUNBOOK
§4-S9 input (a)). New case discoveries → S6 R8's pipeline, never hand-minted; LCD bullets obey
S6 D5's frontier floor (bullet → page only when prose relies on it). *Check:* per-page research
note in the change-list disposition (tactic sweep run y/n + discoveries routed); zero CL REST
calls from S7 lanes; zero hand-minted case pages (S2 R12 lint holds). `PROCESS` · `AUTO` (lane).

**R7 — Field-framing migration (TEACH-04e; user D2).** The 19 hits / 13 pages: **convert** to a
numbered `**Apply it.**` list when the section is a genuine decision sequence (donor: Seizure of
the Person :54); **delete** when it restates a rule or standard in officer-BLUF voice (S1 R7
drift risk). Disposition logged per page in the change-list. *Check:* zero "field framing" /
"apply it angle" section labels corpus-wide; every one of the 13 pages carries a logged
convert/delete disposition. `AUTO` (grep) · `PROCESS`.

**R8 — Pipeline-vocabulary strip (TEACH-02c per S1 A2).** The 41 verified leak lines / 19 pages
(change-list Table 3 site list): "(No standalone case page…)" ×23 · "CL-confirm pending" ×10 ·
LCD/RD meta intro lines (incl. PC/RS :73 and the four policy intros) · "(woven in)" (Third-Party
:25) · the LAW-05 legend. Persisting state moves to HTML comments or frontmatter. Un-paged cases
formerly labeled "(No standalone…)" are simply **named plainly** — the S6 ledger + LINT-17
account for them; no reader-facing bookkeeping. *Check:* S1 A2's five grep classes = 0 over
reader-facing text on touched pages (pre-LINT-11); the About page remains the one sanctioned
methodology site. `AUTO` (grep now, LINT-11 at S9).

**R9 — Named per-page fixes (verify-then-apply; user D3).** The RUNBOOK §4-S7 surviving fix-list
is consumed item-by-item with verification — a refuted item is **corrected and logged, never
applied** (the exemplar: "community caretaking reaches persons" — REFUTED 2026-07-03, replaced
by D5's coverage rule). Landed with verified sites: Matlock → Consent table-entry · CREW
"R"→"RE" · Herring → Key on Collective Knowledge (+ the *Whiteley* exclusion-premise caveat per
research) · Riley → Related on Common Law Origins · Dunn factors in the Rule (Curtilage) ·
knock-and-talk = implied license (**done**, pattern page) · Bandiero hot/fresh-pursuit line +
Santana "limited by" (Hot Pursuit page, point-scoped per research: doorway + felony-pursuit
points good law, broad reading limited by *Lange*) · consent 3 prongs + scope pitfall · split
Legal Research + State Citations w/ opencase.com. Audit rows with pinned sites: TEACH-04a (PC/RS
:66 maxim inversion) · 04b (Seizure :48 "*force* seizure" qualifier) · 04c ("two C's" —
**cut-not-register**, SD8; rephrase as the two unnamed triggers; user may later register it with
Bandiero provenance) · 04d (21 inverted labels / 5 pages) · 04f (CREW mislink, PC/RS :66) · 04g
("persuasive history" → Historical, Common Law :38) · 04h (Warrant Req Sources :149 residue) ·
TEACH-01 (SCOTUS out of every RD section — 5 pages, verified lines; *Chatrie* material lands in
Brief/Key cases of the right pages) · LAW-05 (§1983 :188 Zorn legend stripped; corrected per S2
A1's cluster-vs-opinion root cause) · GAP-06 (geofence-residue check across Third-Party, Warrant
Req :62, Plain View, Standing, ER during their rewrites) · NUM-08 (negative scope — no work).
*Check:* every item carries a change-list disposition + diff pointer; refuted items carry the
research pointer. `PROCESS` (change-list audit).

**R10 — New-prose units (S3 R7/A4/A5/A6; ~44 units, change-list Table 2).** Authored per R1
template at their signed tiers; split-out material moves **once** (SD2: a parent and its
children are one production batch); S3 R13/R14 aliases ride the splits (S3-owned mechanism).
Interview-decided content: **D5** — Community Caretaking hosts the *Seizing people for
non-investigative purposes (public)* section + point node (unsettled law taught as such:
*Graham v. Barnette* PC-of-emergent-danger; *Morgan* (6th Cir. 2023) function-cabining; Alito's
open flag; welfare-check aliases), with the page shaped **vehicles → persons-in-public → homes
(tombstone → Emergency Aid/Case v. Montana)**; Emergency Aid owns the entry standard
(*Brigham City* "without further gloss"). **D7** — Arrest in the Home / Entry to Arrest gets the
head-on **SACO/constructive-entry** section + point node: the 2d/6th/9th/10th vs 5th/7th/11th
split named (1st/3d/4th/8th unmapped — stated honestly), *Nora* as spine, the
containment-vs-exit-command line, the perimeter-defeats-flight-exigency point (*Nora* at 1055),
the *Harris* remedy tail. **D6** — digital children at their tiers; **GAP-03c** — §702/parallel
construction as a brief section on Electronic Surveillance & Title III + a one-line Third-Party
cross-ref. *Check:* every Table 2 unit exists at its tier with its anchors placed (S6 provides
the case pages); the two new point nodes registered (S3 R6 justification: distinct black-letter
rules with split treatment). `PROCESS` · `AUTO:LINT-15`.

**R11 — Em-dash rewrite (TEACH-05 per S1 A8).** Rides each page's prose pass (never a separate
global sed): budget ≤1 em-dash per **block** (paragraph or list item — the unit clarification
routed to LINT-10, RUNBOOK §4-S9 input (e)); never 2+ in a sentence; quotes + controlled labels
exempt. Survey baseline 3,943 across 48 pages (worst: ER 207 · §1983 172 · Warrant Req 152);
pattern page demonstrated 96 → 38 with all blocks in budget. *Check:* per-batch block-level
counts pass; LINT-10 guards the steady state (S9). `AUTO` (counter script) · `CHECKLIST:D9`.

**R12 — Voice (S1 R8, Appendix A; heaviness = as-shown, user D1).** The Humanizer subset applies
to explanation prose only — never quotes, black-letter text, citations, controlled labels.
Term-of-art discipline per S1 R11 (repeat the exact term). *Check:* `CHECKLIST:D9` on review;
register lint (LINT-7-extended) at S9.

**R13 — Point-status tables + reconciling prose (S5 R5).** S7 authors the point-status table +
explanatory prose for every `varies_by_point` case surfaced by the S2 projector (the 11
`limited` + 7 `overruled/abrogated` + any new), consistent with the lake record; the Santana
worked example (doorway ✓ · felony-pursuit ✓ with *Lange*'s express reservation noted · broad
reading limited) comes from this interview's research annex. *Check:* S5 R5's check + S9
coherence (prose ↔ lake per S2 R12). `AUTO` (S9) · `CHECKLIST:D3`.

**R14 — Mnemonics (S1 R9).** Register-verbatim only; weave where they earn placement (Golden
Rules on PC/RS · hot/fresh-pursuit line on Hot Pursuit · Dominoes on Fruits & Attenuation ·
Rubber band with its multiplier-not-bypass guardrail). No new devices without register
amendment + provenance (SD8). *Check:* `AUTO:LINT-8` + TEACH-11's wikilink-target check (S9).

**R15 — Production staging (SD2).** Order: **(1)** mechanical corpus passes first — S5 converter
(`scripts/s5/convert_tables.py`), TEACH-12a H1s, TEACH-04d label orders, TEACH-08 renames/moves
— cheap, global, reviewable diffs; **(2)** per-page rewrites in S3-category batches, Tier A
anchors first, each parent + its split children as one batch (material moves once); **(3)**
em-dash/voice ride the rewrite pass (no double-touch). Drafts accumulate to S9; writer ≠
checker holds (S7 authors, S9's panel reviews, no self-certification); the pattern page
re-enters the pipeline like any other page. *Check:* run journal shows pass-then-batch order;
no page touched twice for the same defect class. `PROCESS`.

**R16 — Coverage & coherence handoffs.** Every case newly named in S7 prose has an S6 ledger
row before the branch merges (LINT-17's allowlist mechanism; the S6 A1 planning-time sub-leg
pre-seeds the 18 interview-era discoveries). Overviews stay S3's (SD7); contradictions S7 finds
in any page it does not own route to the S9 coherence pass — including the new cross-page
contradiction sweep this interview seeded (RUNBOOK §4-S9 input (c)). *Check:* LINT-17 green at
merge; coherence-pass inbox non-empty only via logged routings. `AUTO` · `PROCESS`.

## 4. Lessons enforced

**The flashlight scar (D8):** cited-list free-riding + verification inheritance — R3/R4, with
the S9 per-item G2 and contradiction-sweep routings; the corrected pitfall is the committed
fixture. **The SACO near-miss (D7):** case-keyed discovery finds doctrine adjacent to cases, not
tactics — R6's tactic-vocabulary sweep. **The refuted fix-list item (D3/D5):** user-intent
records are verify-then-apply inputs, never blind patches — R9. **The O1 prose scars carried
from the RUNBOOK:** "(woven in)"/pipeline leaks (R8), slip-op mislabels (R5), SCOTUS-in-Recent-
developments (R9/TEACH-01), em-dash habit (R11), officer-BLUF ban (R7 migration; the layer
stays dead). **Cluster-vs-opinion ids** bit again live (French/Carloss reads) — R6's id
resolution rule + the S9 routing.

## 5. Method (execution — wave 3)

1. Regenerate survey + change-list against the post-S3/S5 tree (the committed change-list is the
   2026-07-03 snapshot; regenerate, don't hand-edit — S6 SEED discipline).
2. Corpus-mechanical passes (R15 step 1) — one commit per pass, lint-verified.
3. Category batches (R15 step 2): per page — R6 research → R3 re-verification → prose per R1/R2
   → R5 conversions → R7/R8/R9 fixes → LCD per S5 R11 → tables via converter output → Sources.
   Splits: author children with the parent batch; S6 R8 invoked for discoveries as they land.
4. D5/D6/D7 content units with their category batches (cat 6 home-entry batch carries
   Caretaking/Emergency Aid/SACO; cat 3 digital batch carries the D6 children).
5. Point-status tables (R13) as S2's projector surfaces `varies_by_point` pages.
6. Emit per-batch journal + updated change-list dispositions; hand S9 the draft corpus + the
   provenance trail (R5 tiers, R9 diffs).

## 6. Deliverables

- All Table 1 rewrites + Table 2 new-prose units, born `draft`, S5-conformant, at signed tiers.
- `_overhaul2/S7-CHANGELIST.md` maintained as the run ledger (dispositions filled at EXECUTE).
- The corpus passes landed (Table 3) + the S5 converter run corpus-wide.
- Two new point-registry nodes (D5 persons-seizure; D7 SACO) + their `^rule-` anchors.
- Research annex (§11) + provenance trail for every R5 conversion and R9 fix.
- This spec; pattern-page commits `e0935ce` + `4b48a4a` (normative); S8 wrapper handed back.

## 7. Acceptance criteria

- [ ] Every Table 1/2 unit rendered per R1 at its signed tier; LINT-15 green corpus-wide; zero
      tier changes without a logged amendment (R2).
- [ ] Zero rewritten pages reach S9 as `verified`; carried assertions carry gate rows (R3).
- [ ] Zero non-current-term slip-op pinpoints; every conversion carries tier + evidence (R5).
- [ ] Zero field-framing sections; 13/13 logged dispositions (R7). Zero A2-class leaks on
      touched pages (R8). All R9 items landed-or-refuted with pointers.
- [ ] D5 section + node live on Community Caretaking (vehicles → persons → tombstone shape);
      D7 SACO section + node live with the split named honestly; D6 tiers hold; GAP-03c landed.
- [ ] Em-dash blocks in budget corpus-wide (R11); TEACH-04d = 0 inversions; TEACH-12a = 0
      missing H1s; TEACH-08 = 0 RD-family headings; TEACH-12b = 0 legacy skeletons.
- [ ] LINT-17 green at merge — every prose-named case has a ledger terminal state (R16).
- [ ] S9 receives: the per-item G2 fixture, the contradiction-sweep seed, the tier-sampled
      conversion trail (RUNBOOK §4-S9 inputs a–e acknowledged in the S9 spec).

## 8. Verification plan

S9 owns review: 1 Claude + 2 Codex panel per S1 R12; black-letter callouts are the ≥2-reviewer
layer (S5 R2); ≥1-in-10 re-verification of R5 conversions **sampled by tier** and of R3 carried
assertions; per-item G2 on enumerations; the cross-page contradiction sweep; LINT-10/11/15/16/17
fail-closed in CI. The pattern page re-enters like any page. S7 self-verifies only mechanics
(counters, greps, converter diffs) — never its own legal assertions.

## 9. Open items / escalations

- **Tier assignments** are signed with the change-list; promotions during production are
  change-list amendments (R2) — if >10 pages promote, pause and surface the authoring-volume
  delta (mirrors S6's scope guard).
- **"Two C's"**: cut per SD8; if the user supplies Bandiero provenance, S1 R9 register amendment
  + restore as a named device (escalation path logged).
- **Felony hot-pursuit reservation** (*Lange* assumed-without-deciding): the Hot Pursuit page
  states the settled-in-practice rule + the reservation; re-check at S9's COH-27 pending-marker
  poll.
- **SACO unmapped circuits** (1st/3d/4th/8th): taught as open; the GH#2 citator watch inherits
  the marker.
- **F.4th pinpoints**: if a licensed/star-paginated source for post-2020 F.4th enters the stack,
  T3 paraphrase-downgrades may be upgraded at the maintenance loop — the provenance trail makes
  them findable.
- **FA Framework hub treatment** (TEACH-12b): migrated as a hub/router page (no rule callout —
  owns no point; SD1 exempt class); if review finds it reads as doctrine, escalate to a
  placed-node decision.

## 10. Decision log

**User decisions (interview 2026-07-03):**
- **D1 — Template signed as shown** (pattern page = normative): Brief move order, Apply-it +
  pitfalls closing, LCD with optional closing split-synthesis paragraph, voice heaviness.
- **D2 — TEACH-04e = content test**: convert genuine decision sequences to Apply-it lists;
  delete BLUF-flavored restatements; per-page logged dispositions.
- **D3 — Prompt.md dropped** (S5 D12 precedent): RUNBOOK §4-S7's list is the record, consumed
  verify-then-apply; refuted items corrected + logged (COH-14 closed for S7).
- **D4 — Depth tiers A/B/C**, per-page assignments in the signed change-list.
- **D5 — Non-investigative person seizures covered, caretaking-adjacent** ("that is where
  officers will look"): section + point node on Community Caretaking; taught as unsettled with
  the circuit map; page shaped vehicles → persons-in-public → home tombstone.
- **D6 — Emerging tech**: reverse-keyword/geofence + cell-site simulators Tier B; real-time
  CSLI/IGG/Title III Tier C; §702 = Title III section + cross-ref (GAP-03c).
- **D7 — SACO head-on** (open floor): full research run delivered (§11); dedicated section +
  node in Arrest in the Home/Entry to Arrest; split taught honestly; tactic-vocabulary sweep
  generalized into R6.
- **D8 — Flashlight pitfall corrected** (open floor, "do not just agree"): overbreadth confirmed
  and fixed (`4b48a4a`); spawned R3 (no verification inheritance) + R4 (per-item support) + the
  S9 contradiction-sweep routing.

**Self-interview (SD1–SD8, run visibly pre-spec; full text in thread):** SD1 template flex —
exempt classes (overviews S3-owned · craft cat-13 · reference cat-12 · history narrative ·
designated hubs) instead of forcing callouts onto pages owning no point (guards S1 R7:
fake/auto-generated standards). SD2 staging — mechanical passes before category batches,
parent+children as one batch, tier changes as logged amendments (guards double-work and silent
ballooning). SD3 change-list = the resumable run ledger (dispositions in-place). SD4 R3/R4 rule
shapes (argued at D8). SD5 T2 threshold = ≥2 independent citing co-occurrences + slip-mapping
consistency, else T3 (guards single-source pin fabrication). SD6 LINT-10 unit = block; Sources
parentheticals (routed S9(e)). SD7 overview boundary — S7 never silently rewrites S3 overviews;
contradictions route to coherence. SD8 "two C's" cut-not-register — the S1 register is closed +
verified; unverified devices don't enter by prose fiat.

**Audit intake (every injected:S7 row dispositioned):**
- **TEACH-01** ADOPT — 5 pages, verified lines (FA Framework :77–79 worst; Warrant Req
  :111/:114; Two Definitions :75; Standing :76/:80; ER :124/:129); SCOTUS material relocates to
  Brief/Key cases; rides R9 + TEACH-08's rename/move.
- **TEACH-02c** ADOPT — 41 verified leak lines / 19 pages + LCD meta intros; R8.
- **TEACH-03 + NUM-01** ADOPT — four-tier method (R5); 76/20 doctrine + 43/47 case pages;
  absorbs LAW-04; provenance per conversion.
- **TEACH-04a** ADOPT (PC/RS :66) · **04b** ADOPT (Seizure :48) · **04c** ADAPT — cut, not
  register (SD8; escalation path open) · **04d** ADOPT (21/5, sites listed) · **04e** ADOPT per
  D2 (19/13, donor Seizure :54) · **04f** ADOPT (PC/RS :66) · **04g** ADOPT (Common Law :38) ·
  **04h** ADOPT (Warrant Req :149).
- **TEACH-05** ADOPT — R11 per S1 A8; survey baseline 3,943; rides the rewrite pass.
- **TEACH-08** ADOPT — S5 R11 applied corpus-wide (35 pages); PC/RS already conformant.
- **TEACH-12a** ADOPT — 18 pages (survey supersedes the ~14 estimate). **TEACH-12b** ADOPT —
  6 migrations; FA Framework as hub (SD1/§9).
- **GAP-03b** ADOPT-ADAPTED — per D6 tiers; BWC = prose in UoF/§1983 (S3 A6 disposition stands).
- **GAP-03c** ADOPT — Title III section + Third-Party cross-ref.
- **GAP-06** ADOPT — residue check folded into the five geofence-touching rewrites (R9).
- **LAW-05** ADOPT — §1983 :188 legend stripped + corrected per S2 A1 root cause (hotfix-candidate
  status resolved: rides the rewrite, no interim hotfix — the page is mid-queue).
- **NUM-08** ADOPT — negative scope honored; zero budget.

## 11. Research annex (interview-time, all load-bearing holdings primary-confirmed)

Retained in-thread and summarized here; the four full reports (collective knowledge · knock-and-
talk · caretaking-of-persons · Santana/Lange) + the SACO report carry verbatim passages,
pincites, treatment notes, and confidence grades per item. Headline dispositions consumed by
this spec: horizontal collective-knowledge pooling = named split (Massenburg / communication-
nexus circuits / Cook-Balser), *Pringle* is suspect-side only; knock-and-talk's genuine split is
place/perimeter (*Carroll v. Carman* reserved), time = divergent defaults, night-visit language
= *Jardines* dissent + majority n.3; caretaking = vehicles-only post-*Caniglia*, persons →
emergency aid (*Case v. Montana* — "without further gloss") + D5's unsettled public-seizure map;
Santana = point-scoped (doorway ✓ · felony pursuit ✓ with reservation · broad reading limited by
*Lange* 594 U.S. at 303–04, 313); SACO = *Nora* spine, split mapped, containment-vs-command
line, *Harris* remedy tail. S6 A1 carries the 18 resulting candidates.
