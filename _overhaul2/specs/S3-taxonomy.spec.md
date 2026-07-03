# SPEC S3 — Taxonomy & Points-of-Law (the spine's classification)

status: APPROVED
depends-on: [S1]   gates: [S4, S5, S6, S7, S8, S9]
last-updated: 2026-07-02

> Our own controlled classification, built from scratch on **NJLEH's practical/object-led methodology**,
> breadth-checked against **LaFave** and **Bandiero**, mapped onto the actual corpus so nothing is orphaned.
> Two coupled layers: **(1) the navigational tree** — 13 top-level categories → sub-umbrellas → pages,
> each node self-contained with an authored overview; **(2) the point-of-law registry** — the controlled
> propositions beneath the pages that case-treatment (S2), assertions (S7), and linking (S8) bind to.
> S3 delivers the tree + the registry + the **`point → node` binding map** that resolves S2's provisional
> `point_override.point` slugs, plus the re-homing table. Read with `PRACTICES.md` (§1 taxonomy-as-spine +
> single-source-of-truth, §7 point-scoped signaling, §8 term register). Conforms to S1. The **nav
> rendering** of this tree (the "TOC-tree" explorer, scroll fix, connectors) is prototyped here but
> **owned by S4**; **page rendering** is S5.

## 1. Objective
Fix the one controlled classification every proposition hangs off, so that (a) an instructor can look at
the left rail and *know where to click*, and (b) every case-treatment and assertion binds to a stable
point-of-law node rather than to a whole case or a whole page. Output: the target tree (13 categories,
≤3-level nesting, overview per node), the re-homing/multi-homing rules, the point-of-law registry, and the
fail-closed `point → S3 node` binding map that unblocks S2's provisional overrides.

## 2. Scope
### 2.1 In scope (S3 designs)
The 13-category target tree + its sub-umbrellas and page roster (existing pages re-homed + greenlit new
nodes placed); the ≤3-level nesting rule; the overview-page pattern (one per category and sub-umbrella);
the re-homing table + the multi-homing (`homes[]`) contract; the **point-of-law registry schema + the seed
node set**; the **`point → S3 node` binding map** for S2's overrides + its fail-closed lint; the
intra-category ordering scheme; `cases/` unlisting; the de-rip naming pass; the depth-cap lint.
### 2.2 Out of scope (owned elsewhere)
The **nav rendering** — the TOC-tree explorer behaviour, the sidebar scroll fix, the tree connectors — is
**S4** (S3 hands over the signed-off prototype, R11). Authoring the newly-placed pages (**S6** verifies +
authors real cases; **S7** writes doctrine prose) — S3 ships them *placed but empty*. Case/term linking and
point transclusion mechanics (**S8**). Case-page rendering, tables, badges, hovers (**S5**). Treatment
derivation itself (**S2** — S3 only supplies the nodes S2's overrides bind to). The per-proposition
adversarial panel (**S9**). Maintenance/citator re-derivation (**GH#2**).

## 3. Requirements (each testable)

**R1 — The 13-category target tree (the controlled classification).** The site is organized as the tree in
**Appendix A**: 13 numbered top-level categories, each self-explanatory and self-contained, nesting no
deeper than *category → sub-umbrella → page*. Built on NJLEH's object-led methodology; **Searches** and
**Seizures** are parallel threshold pillars; **Standards of Proof** precedes them as the shared vocabulary;
the warrantless-search core (**Warrant Exceptions**) is navigable **by object** (person / vehicle / home /
effects) with a programmatic/special-needs sibling group; **Home Entry & Search** is the premises bucket
(multi-homed). *Check:* every one of the 48 existing doctrine/reference pages resolves to exactly one
**primary** home in Appendix A; every top-level category is reachable; no node exceeds depth 3.
`AUTO:LINT-S3-depth` · `CHECKLIST:D5`.

**R2 — Overview page per node.** Every category **and** every sub-umbrella carries an authored **overview**
— broad, plain-English, an on-ramp to its children, **no key-case tables** (those live on doctrine/case
pages, S5/S7). Storage: a top-level category's overview is a first-child `Overview` entry (its header
toggles the tree); a sub-umbrella's overview is its `index.md` (its header *is* the overview link — R11).
*Check:* every category + sub-umbrella has a non-empty overview; no overview contains a case table.
`AUTO:LINT-S3-overview` · `CHECKLIST:D5`.

**R3 — Re-homing + multi-homing contract.** S3 owns the **re-homing table** (Appendix B) and the
multi-homing model: a page/case may be **Key on several pages** (framing is per-page), encoded on the case
page's **`homes: [primary, …]`** frontmatter (S2's *preserved* field). S3 fixes each page's **primary**
home and its Key-on set. Confirmed moves: **Brendlin** → Traffic Stops (out of Standing); **Katz** → Two
Definitions/REP (out of Standing); **Graham** → Use of Force (out of §1983); **Plain View** → the Searches
threshold (out of exceptions); **Brady & Giglio** → Fair-Trial & Reliability (out of Use-of-Force). *Check:*
every move in Appendix B is reflected in the target tree; every case has a resolvable primary `homes[0]`;
no case is orphaned. `PROCESS` · `CHECKLIST:D5`.

**R4 — The point-of-law registry.** A committed controlled list — `_overhaul2/points/registry.yaml` — of
**points of law**: atomic legal propositions finer than a page that treatment/assertions/terms bind to.
Each node = `{id, label, statement, home_page, also_on[], status ∈ {draft, verified}}`, `id` = kebab
`area.object.point` (e.g. `search.vehicle.sia-recent-occupant`, `search.vehicle.automobile`,
`search.person.sia`, `search.home.exigency.emergency-aid`). `area` ≈ the categories; `object` ∈
{person, vehicle, home, effects, …} where it applies. The **`statement`** is the S1-graded black-letter
proposition, stated **once** and transcluded where reused (S1 single-source; S8 mechanizes the embed). A
committed JSON/YAML schema validates every node. *Check:* every node schema-validates; every `home_page`
(and each `also_on[]`) resolves to a page in the tree; no two nodes share an `id`.
`AUTO:LINT-S3-points` · maps PRACTICES §1/§7.

**R5 — The `point → S3 node` binding map + fail-closed lint.** `_overhaul2/points/s2-binding.yaml` maps
**every** S2 `treatment.point_overrides[].point` provisional slug to **one or more** registry node ids
(**1:N / N:1 allowed**). A **fail-closed CI lint** activates: (a) every override slug in the lake resolves
to ≥1 node; (b) every bound node exists in the registry; (c) the node's `home_page` renders the override's
treatment (per-page routing). Worked binding: S2's *New York v. Belton* (110559) vehicle-search override →
**`search.vehicle.sia-recent-occupant`**, `superseded_by` *Arizona v. Gant* (145887); that node's
`home_page` = **Warrant Exceptions → Searching a Vehicle → Search Incident to Arrest — Vehicles**, so the
`superseded` flag renders exactly there while the Belton page's composite stays `caution / varies`.
*Check:* 100% of S2 override slugs bind; the lint fails on any unbound slug or dangling node.
`AUTO:LINT-S3-binding` · answers S2 §9 open item.

**R6 — Granularity rule (page split = point split).** Mint a node **only** when (a) S2 has, or plausibly
could have, **split treatment** on it, (b) it is a distinct **black-letter rule** a page states, or (c) it
is **transcluded** across pages. Do **not** mint per sentence. The calibration anchor: the point split
mirrors the page split — Belton/Gant forces `search.vehicle.sia-recent-occupant` **distinct from**
`search.person.sia` (Robinson) and `search.vehicle.automobile` (Carroll), which is exactly the SIA
page-split the tree already carries. *Check:* the SIA family resolves to ≥3 distinct nodes across the
person/vehicle objects; a spot audit finds no node without a page-level or treatment-level justification.
`PROCESS` · `CHECKLIST:D3/D5`.

**R7 — New-node placement (placed, not authored).** The greenlit breadth additions are **placed** in the
tree with a point-of-law id but **left empty** — authoring is downstream: **fire-scene entries,
stop-and-identify (Hiibel), prompt-PC/Gerstein-McLaughlin, Franks challenges, detention-at-scene
(Summers/Bailey/Ybarra), aerial & enhanced surveillance, private & foreign searches, State Citations &
Conventions**, plus the doctrine splits (getting/executing a warrant; the three exigency flavors; the SIA
family; §1983 vs Qualified Immunity). **S6 verifies + authors the cases; S7 writes the prose.** *Check:*
every placed node exists in the tree + registry with `status: draft` and no authored body; S6/S7 inherit
the list. `PROCESS`.

**R8 — `cases/` unlisted; the Case Index routes.** The `content/cases/` folder is dropped from the explorer
(a `filterFn`), because the generated **Case Index** is the "which page is *X* on?" router. *Check:* no
`cases/` node renders in the nav; the Case Index resolves every case to its `homes[0]`. `AUTO` ·
`CHECKLIST:D5`.

**R9 — De-rip naming (anti-plagiarism; the book author reviews).** Category and node labels are **our own**
and must not reproduce Bandiero's verbatim part titles (he is an S9 reviewer). Enforced renames: "Levels of
Suspicion" → **Standards of Proof**; "Search Warrant Exceptions" → **Warrant Exceptions**; "The Sixth
Amendment Right to Counsel" → **The Right to Counsel**; "What is a Search/Seizure?" → **Searches /
Seizures**. *Check:* no category label string-matches a Bandiero TOC part title; the copied 7a/7b PC-needed
split is gone. `AUTO:LINT-S3-derip` · `PROCESS`.

**R10 — Ordering + depth cap.** Intra-category order is **authored, not alphabetical** (e.g. *The Proof
Ladder* precedes *Reasonable Suspicion* / *Probable Cause*), encoded via **numeric filename/slug prefixes +
an explorer `sortFn` on `slugSegment`** (numeric-aware). Nesting is **≤3 levels**, lint-enforced. *Check:*
the rendered order equals the authored order at every level; the depth lint fails on any 4th level.
`AUTO:LINT-S3-depth` · `AUTO:LINT-S3-order`.

**R11 — Hand-off boundaries (S3 → S4 / S5).** S3 delivers the **tree + registry + re-homing + overviews**.
The **nav model is S4's**: S3 hands over the *signed-off prototype* — the **"TOC-tree"** explorer
(top-level categories are the only accordion; nested folders are always-open branches whose header links to
their overview; `├─/└─` connectors; ordering `sortFn`) **and** the **sidebar scroll fix** (`.explorer` /
`.explorer-content` `flex:1 1 auto; min-height:0`; `overscroll-behavior` `contain` on the scroll container /
`auto` on inner folder ULs; scroll save/restore retargeted to `.explorer-content`; nav `scrollIntoView`
smooth→auto) — prototyped in the S3 mockup (generator + patched `quartz/styles/custom.scss`,
`quartz/components/scripts/explorer.inline.ts`, `quartz.layout.ts`). **Page rendering is S5's.** *Check:*
S4 adopts the prototype as its working-standard; no S3 deliverable depends on nav/page rendering.
`PROCESS`.

**R12 — Every proposition hangs off one classification (single-source).** Per PRACTICES §1: a rule/term is
stated **once** on its point-of-law node and **transcluded** elsewhere, never re-paraphrased across pages.
S3 fixes the canonical home; S8 mechanizes the embed; S1's term register governs wording. *Check:* no
point-of-law `statement` text is duplicated verbatim on a second page except via transclusion. `AUTO`
(cross-checked in S8) · `CHECKLIST:D5`.

## 4. Lessons enforced
Directly answers Overhaul-2 findings and the O2 disciplines: **taxonomy-as-spine + single-source-of-truth**
(R1/R4/R12) — one controlled classification, each proposition stated once. **Point-scoped treatment**
(R4/R5/R6) — the misscoped good-law/bad-law error is structurally impossible; *Belton* reads good-law with
its vehicle point flagged `superseded by Gant`, not the whole case killed. **Mega-page cure** (R1/R2) —
Special-Needs/Inventory/Checkpoints/Border promoted to findable nodes; exigency exploded into flavors.
**Single-home mis-home** (R3) — multi-homing via `homes[]` fixes Brendlin/Katz/Graham. **Copied structure**
(R9) — the book's PC-needed/not split retired; names de-ripped. Carries S1 R10 (authority lexicon informs
`area`) and closes S2 §9 (the binding map).

## 5. Method (execution — one autonomous run)
1. **Materialize the tree** — create the 13 numbered category folders + sub-umbrella subfolders per
   Appendix A; author each node's overview (R2); place the greenlit new nodes empty (R7); prefix
   filenames for order (R10).
2. **Move + re-home** existing pages per Appendix B; set `homes[]` primary + Key-on; regenerate the Case
   Index; unlist `cases/` (R3/R8).
3. **Author the point-of-law registry** `_overhaul2/points/registry.yaml` (R4) + seed nodes (Appendix C),
   each with `home_page`/`also_on[]`/`statement` (draft) and the granularity rule (R6).
4. **Write the binding map** `_overhaul2/points/s2-binding.yaml` from S2's `point_overrides` (R5).
5. **Add lints** to `scripts/lint/`: `LINT-S3-depth`, `-overview`, `-points`, `-binding`, `-derip`,
   `-order` — all CI fail-closed.
6. **Hand S4** the nav-model + scroll-fix prototype (R11); **hand S6/S7** the placed-empty node list (R7).
7. **De-rip pass** over every label (R9); coherence check the tree against S2's roster (S9 gate).

## 6. Deliverables
The 13-category tree under `content/` (folders + overviews + placed nodes) · the re-homing applied +
`homes[]` set + regenerated Case Index + `cases/` unlisted · `_overhaul2/points/registry.yaml` +
`_overhaul2/points/s2-binding.yaml` · `scripts/lint/` extensions (`LINT-S3-depth/-overview/-points/
-binding/-derip/-order`) · the S4 nav-model + scroll-fix prototype (handed over) · Appendices A (tree),
B (re-homing table), C (seed point-of-law nodes).

## 7. Acceptance criteria
- [ ] 13-category tree materialized; all 48 existing pages re-homed to exactly one primary; ≤3 levels (R1/R10).
- [ ] Overview per category + sub-umbrella; no key-case tables in overviews (R2).
- [ ] Re-homing table applied; `homes[]` primary+Key-on set; Brendlin/Katz/Graham/Plain-View/Brady moved; no orphan (R3).
- [ ] `registry.yaml` schema-valid; every node's `home_page`/`also_on[]` resolves; ids unique (R4).
- [ ] `s2-binding.yaml` binds 100% of S2 override slugs; fail-closed lint green; Belton→Gant renders on the SIA-Vehicles node (R5).
- [ ] SIA family = ≥3 distinct nodes; granularity spot-audit clean (R6).
- [ ] Greenlit new nodes placed empty with draft point ids; S6/S7 inherit (R7).
- [ ] `cases/` unlisted; Case Index routes every case (R8).
- [ ] No category label matches a Bandiero part title; PC-needed/not split gone (R9).
- [ ] Authored order holds at every level; depth lint fails on a 4th level (R10).
- [ ] S4 adopts the nav prototype; S5 owns page rendering; no cross-dependency (R11).
- [ ] No duplicated point `statement` except via transclusion (R12, cross-checked S8).

## 8. Verification plan
S3's own gates = the six lints (R1/R2/R4/R5/R9/R10) + the re-homing/orphan check (R3) + the Case-Index
resolution (R8). **S9** then reads the registry + binding map: confirms every S2 negative-treatment event
lands on the right node/page, blind-re-derives a sample of the granularity calls, and coherence-checks the
tree against the S2 roster and the S7 prose. The binding, depth, overview, points, de-rip, and order lints
run in CI fail-closed on every change.

## 9. Open items / escalations
- **Top-level overview interaction.** Top-level categories toggle (click = expand) with an "Overview"
  first-child; sub-umbrella headers *are* their overview link. If S4 later unifies them (top-level header
  navigates + expands), the overview-storage in R2 flexes — the point registry is unaffected.
- **Registry permanent home.** Built at `_overhaul2/points/` for the run; graduation to `data/points/` is
  a post-publish task, referenced via a single path constant (mirrors S2's lake).
- **Override staleness** (a controlling case's own validity later changes) — the SQLite `overrides` check
  (S2 R13) flags it; auto re-derivation is **GH#2**.
- **`area` enum** finalized against the S1 authority lexicon at build; `object` enum grows as new nodes land.
- **Confrontation Clause / 5A act-of-production / immunity** deliberately out of remit (trial-evidence /
  grand-jury); revisit only if the user pulls them in.

## Appendix A — The target tree (13 categories)
*category → sub-umbrella → page. Overviews implicit per node (R2). `[new]` = placed-empty (R7).*

1. **Foundations & the Fourth Amendment** — Common Law Origins · The Fourth Amendment Framework · The Analysis Checklist · Fourth Amendment Recalibration
2. **Standards of Proof** — The Proof Ladder `[new]` · Reasonable Suspicion · Probable Cause
3. **Searches** — Two Definitions of Search → (Trespass · Reasonable Expectation of Privacy) · Curtilage · Open Fields · Aerial & Enhanced Surveillance `[new]` · The Third-Party Doctrine & Digital Surveillance · Private & Foreign Searches `[new]` · Abandonment · Tents & Temporary Dwellings · Plain View & Plain Feel
4. **Seizures** — When a Seizure Occurs · Seizure of Property `[new]` · Terry Stops & Reasonable Suspicion · Stop-and-Identify `[new]` · Traffic Stops · Arrests → (Arrest & Arrest Warrants · Arrest in the Home · Prompt Probable-Cause Determination `[new]`) · Collective Knowledge & the Fellow-Officer Rule
5. **The Warrant** — Getting a Warrant → (Probable Cause in the Affidavit · The Neutral & Detached Magistrate · Particularity · Franks Challenges `[new]`) · Executing a Warrant → (Knock-and-Announce · Detention & Search of Persons at the Scene `[new]` · Scope, Manner & Related Issues)
6. **Warrant Exceptions** — Searching a Person → (SIA — Persons · SIA — Cell Phones · SIA — Alcohol Tests) · Searching a Vehicle → (The Automobile Exception · SIA — Vehicles · Inventory Searches · Checkpoints & Roadblocks) · Home Entry & Search → (Entry to Arrest · Exigent Circumstances — Emergency Aid · — Hot Pursuit · — Destruction of Evidence · Protective Sweeps & Securing the Scene · Community Caretaking · Fire-Scene Entries `[new]`) · Searching Effects & Containers · Consent · Programmatic & Special-Needs Searches → (Special Needs & Administrative · Border Searches) · Knock and Talk
7. **The Exclusionary Rule, Remedies & Standing** — The Exclusionary Rule · Standing to Challenge a Search
8. **Confessions, Interrogation & the Fifth Amendment** — Due-Process Voluntariness · Miranda & Custodial Interrogation · Miranda Waiver & Invocation · Public-Employee Compelled Statements (Garrity)
9. **The Right to Counsel** — Sixth Amendment Right to Counsel · Lineups & the Right to Counsel `[new]`
10. **Fair-Trial & Reliability Doctrines** — Eyewitness Identification · Brady & Giglio · Entrapment
11. **Use of Force & Liability** — Use of Force · Section 1983 & Municipal Liability · Qualified Immunity `[new-split]`
12. **Legal System, Research & Reference** — The Federal Court System · Reading & Citing Cases · State Citations & Conventions `[new]` · Legal Research Tools · Verifying Good Law · Common Legal Terms · Case Index
13. **Instructor Craft & Study** — The Three Golden Rules · C.R.E.W. — The Three Justifications · Instructor Development

## Appendix B — Re-homing table (primary moves)
| Case / topic | From | To (primary) | Why |
|---|---|---|---|
| Brendlin | Standing | Seizures → Traffic Stops | passenger seizure, not standing |
| Katz | Standing | Searches → Two Definitions → REP | the seminal "what is a search" |
| Graham | §1983 Liability | Use of Force | the seizure-force standard |
| Plain View / Plain Feel | Warrant exceptions (7a) | Searches (threshold) | seizure justification, not a search exception (NJLEH/LaFave) |
| Brady & Giglio | Use of Force & Liability | Fair-Trial & Reliability | a due-process disclosure duty, not force/civil-liability |
| Inventory · Checkpoints · Border | Special-Needs mega-page | Warrant Exceptions → Vehicle / Programmatic | promoted to findable nodes |
| Community Caretaking | (home-entry adjacency) | Warrant Exceptions → Home Entry | vehicles+persons; NOT home entry post-*Caniglia* |
| 4A Framework · Analysis Checklist · Recalibration | What Is a Search? | Foundations | master analysis + framing |
| Standards of Proof | position #5 | position #2 | the precursor vocabulary for stops/arrests/warrants |

## Appendix C — Seed point-of-law nodes (illustrative; full set at build)
| `id` | `home_page` | binds from S2 |
|---|---|---|
| `search.vehicle.automobile` | Searching a Vehicle → Automobile Exception | Carroll/Acevedo |
| `search.vehicle.sia-recent-occupant` | Searching a Vehicle → SIA — Vehicles | **Belton → superseded_by Gant** |
| `search.vehicle.inventory` | Searching a Vehicle → Inventory Searches | Opperman line |
| `seizure.vehicle.checkpoint-sobriety` / `…crime-control` | Checkpoints & Roadblocks | Sitz ✓ / Edmond ✗ |
| `search.person.sia` / `…cellphone` / `…alcohol` | Searching a Person → SIA (Persons/Cell/Alcohol) | Robinson / Riley / Birchfield |
| `search.home.exigency.emergency-aid` / `…hot-pursuit` / `…destruction` | Home Entry → the three exigency pages | Brigham City / Santana-Lange / King |
| `seizure.person.terry-stop` | Terry Stops & Reasonable Suspicion | Terry line |
| `proof.reasonable-suspicion` / `proof.probable-cause` | Standards of Proof | Sokolow / Gates |

## Appendix — Decision log
**User-facing interview (2026-07-01/02):**
- **Methodology** — NJLEH is the *guide, not the rule*; build our own from scratch, breadth-checked against
  LaFave + Bandiero (rejected: copying any book's TOC — Bandiero reviews it).
- **Exceptions axis = by object** (person/vehicle/home/effects) — user's call over by-suspicion; grounded
  in LaFave Ch5/6/7 + NJLEH Ch8.
- **Home Entry & Search** = a real cross-cutting topic (multi-homed premises bucket).
- **Plain View → threshold** (NJLEH + LaFave), not exceptions (Bandiero) — user's call.
- **Parallel Searches / Seizures**, plain nouns (de-ripped from Bandiero's question titles); **Standards of
  Proof** moved to #2; **Two Definitions** → Trespass + REP child pages; **Curtilage** & **Open Fields**
  split (Curtilage is a major training point); **Trespass** label without "physical intrusion" (the Court's
  *Jones* word, but misleads as a label — quoted in-page instead).
- **Fair-Trial & Reliability Doctrines** — new umbrella for Eyewitness ID + Entrapment + **Brady & Giglio**
  (moved off Use-of-Force after adversarial review: Brady is a prosecutorial due-process disclosure duty,
  new-trial remedy — not force/civil-liability).
- **§1983 vs Qualified Immunity split** (adversarial review: two questions/parties/remedies; QI's own huge
  cross-cutting docket; neither goes thin; anti-mega-page).
- **Nav model** — the "TOC-tree": open a category → whole branch expands; subcategory headers *are* the
  overview link, not toggles; tree connectors kept (NN/g + docs-sidebar research). **→ owned by S4.**

**Self-interview (SD1–SD7; SD1 worked to edge cases):**
- **SD1** point-of-law registry + `point → node` binding is the join key; `area.object.point` ids;
  granularity rule = **page split = point split** (Belton/Gant forces three distinct SIA nodes);
  edge cases N:1 / 1:N / multi-home-transclusion / controlling-case drift → GH#2; failure guarded =
  misscoped treatment.
- **SD2** tree = numbered folders/subfolders/files; multi-homing via `homes[]`; S3 owns the re-homing table.
- **SD3** overview pattern = broad, no key-case tables, on-ramp.
- **SD4** `cases/` unlisted via `filterFn`; Case Index routes.
- **SD5** de-rip every label (Bandiero reviews).
- **SD6** new nodes *placed* empty; authoring → S6/S7.
- **SD7** S3/S4/S5 boundary — tree+registry = S3; nav rendering (TOC-tree + scroll fix + connectors) = S4
  (prototype handed over); page rendering = S5; depth ≤3 lint-enforced.
