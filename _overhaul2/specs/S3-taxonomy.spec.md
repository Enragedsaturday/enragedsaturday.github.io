# SPEC S3 — Taxonomy & Points-of-Law (the spine's classification)

status: APPROVED
depends-on: [S1, S2]   gates: [S4, S5, S6, S7, S8, S9]
last-updated: 2026-07-02

*Amended — see Amendments A3 (depends-on), A1/A2 (new R13/R14).*

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
`AUTO:LINT-S3-overview` · `CHECKLIST:D5`. *Amended — see Amendments A7(3).*

**R3 — Re-homing + multi-homing contract.** S3 owns the **re-homing table** (Appendix B) and the
multi-homing model: a page/case may be **Key on several pages** (framing is per-page), encoded on the case
page's **`homes: [primary, …]`** frontmatter (S2's *preserved* field). S3 fixes each page's **primary**
home and its Key-on set. Confirmed moves: **Brendlin** → Traffic Stops (out of Standing); **Katz** → Two
Definitions/REP (out of Standing); **Graham** → Use of Force (out of §1983); **Plain View** → the Searches
threshold (out of exceptions); **Brady & Giglio** → Fair-Trial & Reliability (out of Use-of-Force). *Check:*
every move in Appendix B is reflected in the target tree; every case has a resolvable primary `homes[0]`;
no case is orphaned. `PROCESS` · `CHECKLIST:D5`. *Amended — see Amendments A1 (R13 URL stability)
and A2 (R14 flashcard-deck stems).*

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
`CHECKLIST:D5`. *Amended — see Amendments A1(b)/(d).*

**R9 — De-rip naming (anti-plagiarism; the book author reviews).** Category and node labels are **our own**
and must not reproduce Bandiero's verbatim part titles (he is an S9 reviewer). Enforced renames: "Levels of
Suspicion" → **Standards of Proof**; "Search Warrant Exceptions" → **Warrant Exceptions**; "The Sixth
Amendment Right to Counsel" → **The Right to Counsel**; "What is a Search/Seizure?" → **Searches /
Seizures**. *Check:* no category label string-matches a Bandiero TOC part title; the copied 7a/7b PC-needed
split is gone. `AUTO:LINT-S3-derip` · `PROCESS`. *Amended — see Amendments A7(5).*

**R10 — Ordering + depth cap.** Intra-category order is **authored, not alphabetical** (e.g. *The Proof
Ladder* precedes *Reasonable Suspicion* / *Probable Cause*), encoded via **numeric filename/slug prefixes +
an explorer `sortFn` on `slugSegment`** (numeric-aware). Nesting is **≤3 levels**, lint-enforced. *Check:*
the rendered order equals the authored order at every level; the depth lint fails on any 4th level.
`AUTO:LINT-S3-depth` · `AUTO:LINT-S3-order`. *Amended — the ordering mechanism (numeric
filename/slug prefixes) is superseded by frontmatter `weight:`; the authored-order principle, the
check, and the depth cap stand. See Amendments A8 (A8 — user decision 2026-07-03).*

**R11 — Hand-off boundaries (S3 → S4 / S5).** S3 delivers the **tree + registry + re-homing + overviews**.
The **nav model is S4's**: S3 hands over the *signed-off prototype* — the **"TOC-tree"** explorer
(top-level categories are the only accordion; nested folders are always-open branches whose header links to
their overview; `├─/└─` connectors; ordering `sortFn`) **and** the **sidebar scroll fix** (`.explorer` /
`.explorer-content` `flex:1 1 auto; min-height:0`; `overscroll-behavior` `contain` on the scroll container /
`auto` on inner folder ULs; scroll save/restore retargeted to `.explorer-content`; nav `scrollIntoView`
smooth→auto) — prototyped in the S3 mockup (generator + patched `quartz/styles/custom.scss`,
`quartz/components/scripts/explorer.inline.ts`, `quartz.layout.ts`). **Page rendering is S5's.** *Check:*
S4 adopts the prototype as its working-standard; no S3 deliverable depends on nav/page rendering.
`PROCESS`. *Amended — see Amendments A7(6) and A8(e): the handed-over `sortFn` reads frontmatter
`weight:`, not numeric prefixes (A8 — user decision 2026-07-03).*

**R12 — Every proposition hangs off one classification (single-source).** Per PRACTICES §1: a rule/term is
stated **once** on its point-of-law node and **transcluded** elsewhere, never re-paraphrased across pages.
S3 fixes the canonical home; S8 mechanizes the embed; S1's term register governs wording. *Check:* no
point-of-law `statement` text is duplicated verbatim on a second page except via transclusion. `AUTO`
(cross-checked in S8) · `CHECKLIST:D5`.

*Amendments add **R13** (URL & slug stability) and **R14** (flashcard-deck stem preservation) — see
Amendments A1/A2.*

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
   filenames for order (R10). *(Superseded in part: folders/files are UNNUMBERED; order comes from
   frontmatter `weight:` — see Amendments A8 (A8 — user decision 2026-07-03).)*
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

*Amended — additional acceptance criteria in Amendments A1, A2, A4–A7.*

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
*The `1.`–`13.` numbers (and any `01-…` prefixes shown here or in the mockup) denote
**display/build order only** — they are NOT literal folder or file names; slugs are unnumbered and
order comes from frontmatter `weight:` (A8 — user decision 2026-07-03).*

1. **Foundations & the Fourth Amendment** — Common Law Origins · The Fourth Amendment Framework · The Analysis Checklist · Fourth Amendment Recalibration
2. **Standards of Proof** — The Proof Ladder `[new]` · Reasonable Suspicion · Probable Cause
3. **Searches** — Two Definitions of Search → (Trespass · Reasonable Expectation of Privacy) · Curtilage · Open Fields · Aerial & Enhanced Surveillance `[new]` · The Third-Party Doctrine & Digital Surveillance · Private & Foreign Searches `[new]` · Abandonment · Tents & Temporary Dwellings · Plain View & Plain Feel *(amended — see A6: digital sub-umbrella + Title III)*
4. **Seizures** — When a Seizure Occurs · Seizure of Property `[new]` · Terry Stops & Reasonable Suspicion · Stop-and-Identify `[new]` · Traffic Stops · Arrests → (Arrest & Arrest Warrants · Arrest in the Home · Prompt Probable-Cause Determination `[new]`) · Collective Knowledge & the Fellow-Officer Rule
5. **The Warrant** — Getting a Warrant → (Probable Cause in the Affidavit · The Neutral & Detached Magistrate · Particularity · Franks Challenges `[new]`) · Executing a Warrant → (Knock-and-Announce · Detention & Search of Persons at the Scene `[new]` · Scope, Manner & Related Issues)
6. **Warrant Exceptions** — Searching a Person → (SIA — Persons · SIA — Cell Phones · SIA — Alcohol Tests) · Searching a Vehicle → (The Automobile Exception · SIA — Vehicles · Inventory Searches · Checkpoints & Roadblocks) · Home Entry & Search → (Entry to Arrest · Exigent Circumstances — Emergency Aid · — Hot Pursuit · — Destruction of Evidence · Protective Sweeps & Securing the Scene · Community Caretaking · Fire-Scene Entries `[new]`) · Searching Effects & Containers · Consent · Programmatic & Special-Needs Searches → (Special Needs & Administrative · Border Searches) · Knock and Talk
7. **The Exclusionary Rule, Remedies & Standing** — The Exclusionary Rule · Standing to Challenge a Search *(amended — see A4: ER sub-umbrella)*
8. **Confessions, Interrogation & the Fifth Amendment** — Due-Process Voluntariness · Miranda & Custodial Interrogation · Miranda Waiver & Invocation · Public-Employee Compelled Statements (Garrity)
9. **The Right to Counsel** — Sixth Amendment Right to Counsel · Lineups & the Right to Counsel `[new]`
10. **Fair-Trial & Reliability Doctrines** — Eyewitness Identification · Brady & Giglio · Entrapment
11. **Use of Force & Liability** — Use of Force · Section 1983 & Municipal Liability · Qualified Immunity `[new-split]` *(amended — see A5: civil-remedies placed nodes)*
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

*Amended — Border & Inventory rows corrected; see Amendments A7(1–2).*

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
  *(Superseded on the numbered-names point by explicit user decision — see Amendments A8; the
  `homes[]` model and re-homing-table ownership stand. (A8 — user decision 2026-07-03))*
- **SD3** overview pattern = broad, no key-case tables, on-ramp.
- **SD4** `cases/` unlisted via `filterFn`; Case Index routes.
- **SD5** de-rip every label (Bandiero reviews).
- **SD6** new nodes *placed* empty; authoring → S6/S7.
- **SD7** S3/S4/S5 boundary — tree+registry = S3; nav rendering (TOC-tree + scroll fix + connectors) = S4
  (prototype handed over); page rendering = S5; depth ≤3 lint-enforced.

---

## Amendments — 2026-07-02 (audit integration)

*Gap-analysis diff of the signed spec against `_overhaul2/AUDIT-2026-07-02.md` (rows routed
`amend:S3 (gap-analysis-first)`). Rows the spec already handles are dispositioned `covered-by-spec`
in the register — no text here. Amendments are additive: new requirements are numbered R13+ so the
signed body is not renumbered. The one conflict with a signed decision (TAX-09) was escalated and
is now RESOLVED by explicit user decision → A8; the original both-positions writeup is preserved
at the end (A8 — user decision 2026-07-03).*

### A1 — R13: URL & slug stability (old-path aliases · `cases/` frozen · link sweep · `/cases/` fate)
**Register:** TAX-03a · TAX-03c · TAX-10.
**Context (rev. per A8 review 2026-07-03):** R3/R8 move pages and regenerate the Case Index, but
the spec is silent on the *old URLs*. Slugs on the live site embed the numbered folder path; the
migration **de-numbers** every slug (A8) and moves/renames pages, so every doctrine URL on the
live site changes. Existing `aliases:` are bare titles, not old paths.
**New requirement — R13 (fail-closed).**
(a) **Old-path aliases (rev. per A8 review 2026-07-03):** every page whose **full site path
changes, from any cause** — Appendix B moves/re-parenting, R9 renames, the A8 de-numbering of
folder and file slugs (see A8(e)), or any other restructure step — gets an `aliases:` entry for
**each previous full site path** (not a bare title), so Quartz's alias-redirect emitter serves
every pre-O2 URL.
(b) **`cases/` frozen:** `content/cases/` files are neither moved nor renamed — their URLs are
preserved verbatim (the corpus's one stability win). R8's unlisting is explorer-only (`filterFn`),
never a file move.
(c) **Link sweep:** every `homes:`/`related:` frontmatter value and every path-based wikilink is
rewritten to the new paths; zero old-path references remain in source.
(d) **`/cases/` landing:** because the files stay, Quartz still emits an auto folder-listing at
`/cases/` — replace it with a minimal authored `cases/index.md` that routes readers to the Case
Index (URL stays live; the 457-row auto listing dies).
*Check:* a crawl of the complete pre-move URL inventory returns a page (directly or via alias
redirect) for 100% of URLs; zero dangling old-path wikilinks. `AUTO:LINT-S3-urls` (new, CI).
**Lint mechanics (rev. per Codex review 2026-07-02):**
- **Inventory artifact:** `_overhaul2/url-inventory.json` — the complete list of site-relative
  page paths emitted by the **current (pre-move) build**, generated from the build's emitted slugs
  (the built `contentIndex.json` / emitted-HTML set). It MUST be generated and committed **before
  the first move**; the lint FAILS if the artifact is absent or empty.
- **Normalization (both sides):** path-only comparison (no origin/query/fragment); percent-decode;
  lowercase; strip one trailing slash; `/x/index` ≡ `/x`.
- **Inputs checked:** every normalized inventory path must resolve on the **rebuilt** site to
  either (i) an emitted page at that path or (ii) an alias-redirect stub emitted at that path
  (from an R13(a) `aliases:` entry).
- **Fail conditions (fail-closed):** any inventory path with neither page nor alias stub → FAIL;
  any surviving old-path `homes:`/`related:`/wikilink reference (the R13(c) sweep) → FAIL.
**Acceptance:** pre-move URL inventory fully resolves; `cases/` paths unchanged; `/cases/` routes.
**Rationale:** the site is live in production; the restructure (de-numbering + moves, per A8)
otherwise 404s every bookmark, inbound link, and the frozen flashcard deck (A2). *(rev. per A8
review 2026-07-03)*

### A2 — R14: flashcard-deck stem/alias preservation
**Register:** COH-05b.
**Context:** the O1 flashcard deck is frozen and references pages by stem/alias under a
non-breakage guarantee; R3 re-homings, R9 renames, and the renumbering can silently break it — the
spec never mentions the deck.
**New requirement — R14 (rev. per Codex review 2026-07-02 — self-contained: R13(a)'s aliases
cover full site *paths*, while the deck references path-less *stems*).**
- **Deck location:** the frozen deck's source of truth is **`flashcard-src/decks/*.json`**
  (merged published artifact `public/static/flashcards/flashcards.json`; Anki export
  `public/static/flashcards/cssi-search-and-seizure.apkg`).
- **Reference grammar:** each card references its page via the **path-less slug stem** in its
  `"page"` field (e.g. `"arrest-in-the-home"`); card `id`s are prefixed with that same stem and
  each deck filename equals it (`flashcard-src/DECK-GEN-BRIEF.md` card schema). The extraction
  set = the union of `page` values across all deck files, cross-checked against deck filename
  stems. Cards carry no wiki URLs (their only links are CourtListener `source` URLs), so stems
  are the sole join key.
- **Resolution rule:** post-move, every extracted stem must — after normalization (lowercase
  kebab; stem-only, so folder re-parenting/renumbering alone breaks nothing; only a filename-stem
  rename does) — match either (i) the final slug segment of an emitted page or (ii) a **bare-stem
  `aliases:` entry** on some page. Consequence: any page whose filename stem changes (R9 renames;
  A4/A6 splits) MUST carry its old stem as a bare-stem alias — a **deck-stem alias required by
  R14 itself**, in addition to R13(a)'s full-path aliases.
- **Accepted-breakage table:** any stem knowingly left unresolved (none expected) is recorded in
  a table appended to **Appendix B**, schema:
  `| deck_stem | card_count | successor_page (new path) | reason | user_ack (date) |`.
  The deferred flashcard rebuild (named run #2, audit decision D3) consumes it.
*Check:* a script resolves 100% of extracted stems against the built site per the rule above; the
accepted-breakage table is empty or every row carries `user_ack`. `AUTO:LINT-S3-deck` (new, CI,
fail-closed on any unresolved, unacknowledged stem).
**Rationale:** honors O1's guarantee without blocking the tree; the rebuild run — not S3 — is what
retires it.

### A3 — Frontmatter: `depends-on: [S1, S2]`
**Register:** COH-04b.
**Context (was):** `depends-on: [S1]`. **Change (applied in the header):** `depends-on: [S1, S2]`.
**Rationale:** factual, not a decision — R5 consumes S2's `treatment.point_overrides[].point`
slugs and the spec itself "closes S2 §9"; the binding map cannot be authored without S2's override
schema. This is an *authoring/design* dependency, consistent with COH-04a's runbook-side fix (S2
`gates:` vs execution concurrency is the runbook's problem, not this header's).

### A4 — Exclusionary Rule sub-umbrella (Appendix A, cat 7)
**Register:** TAX-02a.
**Context (was):** "**The Exclusionary Rule, Remedies & Standing** — The Exclusionary Rule ·
Standing to Challenge a Search".
**New text (cat 7):** **The Exclusionary Rule, Remedies & Standing** — The Exclusionary Rule →
(Fruits & Attenuation `[new-split]` · The Good-Faith Exception `[new-split]` · Inevitable Discovery
& Independent Source `[new-split]`) · Standing to Challenge a Search.
**Acceptance:** the ER page's 44 homed cases re-point across the split per R3; no orphan.
**Rationale:** the ER page is the wiki's true mega-page (44 homed cases — heavier than the
31-case Special Needs page the spec's §4 "mega-page cure" already splits); leaving it whole is
inconsistent with the spec's own R1/R2 cure. Splits follow the doctrine's joints; `[new-split]`
nodes inherit R7 (placed; S6/S7 author). Standing's cat-7 placement is signed and unchanged
(register TAX-11 = covered).

### A5 — Civil-remedies placed nodes (Appendix A, cat 11)
**Register:** GAP-01a · GAP-02a · GAP-07 · TAX-02b (partial).
**Context (was):** "**Use of Force & Liability** — Use of Force · Section 1983 & Municipal
Liability · Qualified Immunity `[new-split]`".
**New text (appends to cat 11):** · Retaliatory Arrest `[new]` (*Nieves/Gonzalez*) · Malicious
Prosecution under the Fourth Amendment `[new]` (*Thompson/Chiaverini*) · Civil Asset Forfeiture
`[new]` (*Culley*). All three join R7's greenlit placed-empty list (S6 verifies + authors the
cases; S7 the prose). **Partial closure of TAX-02b (rev. per Codex review 2026-07-02):** this
amendment fully closes GAP-01a/GAP-02a/GAP-07 but only **partially** closes TAX-02b. The
residual is the **Bivens/§242 substructure** inside *Section 1983 & Municipal Liability*, which
this amendment deliberately does NOT add. The residual resolves **at execution** via an R6
granularity decision (split into placed nodes vs keep as in-page sections), and that decision
MUST be logged in this spec's Decision Log; the register pointer for TAX-02b cites this paragraph
plus that future log entry.
**Rationale:** the audit found these doctrines absent corpus-wide (0 hits) with no reservable
home — cat 11 (only adjacent-doctrine cluster) is their natural seat; reserving nodes now prevents
re-cutting the signed tree after S6 ingest.

### A6 — Digital-surveillance sub-umbrella + Title III home (Appendix A, cat 3)
**Register:** TAX-05a · TAX-05c · GAP-03a.
**Context (was):** "The Third-Party Doctrine & Digital Surveillance" as a single page; the
technology family (Carpenter/Riley/Jones/Kyllo/Chatrie/Cotterman-Touset/Mansor) is scattered
across ≥5 pages in 4 categories — the hardest family to find — and post-*Chatrie* topics + Title
III have no node anywhere in the signed tree.
**New text (cat 3 entry):** The Third-Party Doctrine & Digital Surveillance → (Third-Party
Doctrine & CSLI · Cell-Site Simulators `[new]` · Reverse-Keyword & Geofence Warrants `[new]` ·
Real-Time Tracking `[new]` · Investigative Genetic Genealogy `[new]`) · Electronic Surveillance &
Title III `[new]` (*Olmstead/Berger* progeny, the statutory regime).
Reserved-child grain settles at execution under R6 (a child may fold into a sibling if S2/S6 yield
too little); **any such fold is itself an R6 decision that MUST be recorded in this spec's Decision
Log — reserved nodes never fold silently** (rev. per Codex re-verify 2026-07-02). Riley (SIA — Cell Phones), Kyllo, Jones, and the border-device pages **keep their
signed primaries** and become **Key-on** the umbrella via `homes[]` (R3) — findability without
re-homing. **BWC disposition (rev. per Codex review 2026-07-02):** body-worn cameras — the one
GAP-03a topic NOT reserved above — get **no taxonomy node**: BWC-as-evidence is a
recording/retention/disclosure policy topic, not search-and-seizure doctrine, so it routes to S7
prose within the Use-of-Force/§1983 pages per GAP-03b (an explicit recorded decision, not an
omission).
**Rationale:** same reserve-don't-recut logic as A5; the digital family is the audit's named
worst find-it failure, and GAP-03a's post-*Chatrie* topics otherwise force a tree re-cut at S6/S7.

### A7 — Calibrations (Appendix B corrections · overview template · master index · naming grammar · mockup authority)
**Register:** TAX-04a · TAX-04b · TAX-07 · TAX-08b · TAX-08c · TAX-08d · CODE-01b.
1. **Appendix B, Border row (TAX-04a):** Border Searches is *already standalone* today — the row
   is a **re-parent** under Programmatic & Special-Needs (keep-standalone), not an extraction from
   the mega-page.
2. **Appendix B, Inventory row (TAX-04b):** the Inventory extraction pulls from **two** sources —
   its homes on Special Needs **and** the teaching text inside the SITA page.
3. **R2 overview template (TAX-07):** the donor template for authored overviews is
   `content/index.md`'s annotated-MoC style — all 15 current category indexes are identical
   8-line stubs; none is a usable donor.
4. **Master index (TAX-08b/c):** regenerate the root `content/index.md` from the final tree so
   every page has an index line — cures the missing Garrity line and Emergency Aid's alias-only
   reachability.
5. **R9 naming grammar (TAX-08d):** the de-rip pass also enforces **one grammar per level** —
   plain nouns (no question titles), consistent article use, one CREW spelling ("C.R.E.W." per
   Appendix A).
6. **R11 mockup authority (CODE-01b):** commit `8655398` is the nav-model *prototype only*.
   **Appendix A is authoritative** wherever the mockup diverges; the `displayNames`/`filterFn`
   tables are regenerated from Appendix A at execution (the mapped folders don't exist until
   Method step 1 — today's build showing fallback names is by design, and the mockup carries no
   `cases` mapping because R8 filters it). **Ordering (rev. per A8 review 2026-07-03):** there are
   **no regenerated `sortFn` tables** — Appendix A drives the **assigned `weight:` values** at
   execution, and the S4 comparator simply reads `weight:` per A8(d) (the mockup's numeric-prefix
   `sortFn` is superseded on this point).

### A8 — Frontmatter-weight ordering; unnumbered slugs (supersedes SD2 + R10's mechanism) (A8 — user decision 2026-07-03)
**Register:** TAX-09 (was `conflict:user-decision-needed`; RESOLVED by user decision 2026-07-03).
**Superseded text (quoted):** R10 — order "encoded via **numeric filename/slug prefixes + an
explorer `sortFn` on `slugSegment`** (numeric-aware)"; Decision-Log SD2 — "tree = numbered
folders/subfolders/files". Superseded **by explicit user decision**, not an audit override: the
user chose after the tradeoff was explained — prefixes embed ordering in URLs, so every future
insert renumbers siblings and churns URLs; weight gives clean, permanently stable URLs, and this
restructure is the one-time moment to pay the alias cost.
**New mechanism:**
(a) **Pages:** intra-category/sub-umbrella order comes from a frontmatter **`weight:`** field on
each page. Filenames/slugs carry **no ordering numbers**.
(b) **Category folders too:** folder slugs are unnumbered (`/standards-of-proof/…`, not
`/02-standards-of-proof/…`); a folder's position comes from the **`weight:`** in its `index.md`
(for sub-umbrellas that file is already the R2 overview; for top-level categories it is
metadata-only — R2's Overview-first-child storage is unchanged). Appendix A's `1.`–`13.`/`01-…`
numbering is to be read as **display/build order only**, never literal names (clarifying line
added at Appendix A).
(c) **Weight convention + lint (rev. per A8 review 2026-07-03):** weights are **gap-valued
(10/20/30…) as an ADVISORY convention, not a fail condition** — a normative gap rule would fail
legitimate mid-gap inserts (e.g. `15`), defeating the purpose. Ties break **alphabetically by
slug** (duplicate weights are therefore legal and deterministic); a missing `weight:` sorts
**last** and is lint-flagged. Enforced by extending the existing **`LINT-S3-order`**, fully
mechanical:
- **Scope (must carry `weight:`):** every explorer-listed content page under `content/`, and
  every category and sub-umbrella `index.md` in the Appendix A tree.
- **Exclusions (no `weight:` required):** `content/cases/**` (unlisted per R8) · `cases/index.md`
  (the R13(d) router landing) · the site root `content/index.md` (not an explorer node) · any
  file excluded by the explorer `filterFn` (the lint reads the same exclusion list as the
  `filterFn`, single-sourced).
- **Fail conditions:** any in-scope file with a **missing or non-positive-integer** `weight:` →
  FAIL. Gap spacing and tie values never FAIL (advisory only).
(d) **S4 handoff:** the explorer `sortFn` reads page `weight:` and folder-index `weight:`; the
committed mockup's numeric-prefix `sortFn` (commit `8655398`) is **superseded on this point** —
S4 implements the weight-reading sort. The rest of the R11 prototype handoff stands.
(e) **R13/A1 unweakened:** unnumbered slugs change nothing about the alias mandate — the current
live site's numbered-path URLs still require R13(a) aliases, and the `_overhaul2/url-inventory.json`
mechanism is unchanged.
**Rationale (decision-log-grade):** decouple ordering from addressing — an order edit becomes a
frontmatter edit, never a URL migration; the alias cost is paid exactly once, now, during the
restructure that already requires it.

### TAX-09 — RESOLVED 2026-07-03 (user decision → A8)
*Original conflict writeup, preserved for the record (both positions as escalated):*
R10 and Decision-Log SD2 explicitly choose **numeric filename/slug prefixes + explorer `sortFn`**;
the audit recommends frontmatter-weight sorting or frozen gap numbering (10/20/30) because
prefix-numbered folders *and* files renumber on any insertion — URL churn on every future insert.
This is a signed, reasoned decision and is not overridden here; it is escalated in the register as
`conflict:user-decision-needed`. Note the interaction: R13(a) old-path aliases absorb the churn
from *this run's* renumbering, but not from future insertions.
*Resolution (A8 — user decision 2026-07-03): the user adopted frontmatter-weight ordering with
unnumbered slugs — see A8 above.*
