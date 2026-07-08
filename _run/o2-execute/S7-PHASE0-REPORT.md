# S7 Phase-0 report — survey + change-list regeneration vs the post-S3/S5/S6 tree

Worker: O2 EXECUTE S7 Phase-0 (`claude-opus-4-8`). Spec §5 step 1 ("regenerate
survey + change-list against the post-S3/S5 tree … regenerate, don't hand-edit").
Filesystem-only; zero CourtListener calls; zero mutations outside `scripts/s7/`
and `_run/o2-execute/`. Nothing committed (orchestrator commits).

Deliverables:
- `scripts/s7/survey.py` (+ `fixtures/legacy-page.md`, `fixtures/brief-page.md`) — deterministic survey generator; `--self-test` green (46/46 checks).
- `scripts/s7/build_worklist.py` — regenerates the change-list programmatically from the survey.
- `_run/o2-execute/s7-survey.json` — one row per substantive page + corpus totals.
- `_run/o2-execute/s7-worklist.json` + `_run/o2-execute/S7-WORKLIST.md` — the regenerated change-list (Table 1/2/3).

Every number below is from a survey run or a cited grep. Both scripts are
deterministic (byte-identical across re-runs) and read-only over `content/`.

---

## 1. Headline: the tree is in the expected S7-OPENING state

The signed change-list is the **2026-07-03 pre-S7 snapshot**. Against the current
tree:

- **S3 restructure: DONE.** The 12 numbered O1 directories are gone (verified: no
  `content/1-foundations-history/` … `content/12-instructor-craft-study/`
  survive). The tree is the 13-category taxonomy. **100% of Table-1 pages moved.**
- **S5 converter + S6 case-minting: DONE.** 607 case pages under `content/cases/`
  (survey `case_pages.count`); case tables converted; some Key/Related cells carry
  inverted weight labels S6 populated.
- **S7 doctrine authoring: NOT done except the pattern page (Knock and Talk).**
  - The 41 Table-2 new-prose nodes are **S3 placed-empty stubs** — `status: draft`,
    30–37 words each, all carrying the `**Placed by S3 (Overhaul-2).** … not yet
    authored` placeholder (grep: exactly **41** "Placed by S3" pages, non-case).
  - The 46 non-no-op Table-1 legacy pages remain **`status: verified`** with their
    legacy defects intact (they were mechanically S5/S6-processed but never
    S7-rewritten; R3 would have re-born them `draft`).
  - Only **3** pages carry the R1 `> [!rule]` callout (Knock and Talk — draft;
    Curtilage, PC/RS — verified) and only **1** carries `**Apply it.**` (Knock and
    Talk). The signed R1 brief template has not landed corpus-wide.

**Status distribution (survey):** 46 verified · 42 draft · 1 none (Case Index, generated).
The 42 draft = the 41 placed-stub Table-2 nodes + Knock and Talk. This mapping is
exact and is the cleanest signal that Table-2 authoring is the open queue, not done.

**RED FLAG for the orchestrator (none — this is the healthy reading):** the earlier
worry that "S7 already ran" is refuted — the Table-2 nodes are stubs, the Table-1
pages are unrewritten. S7 opens on a clean pre-authoring baseline with the pattern
page as the single landed exemplar. The change-list's Table-1 defect flags still
substantially describe the legacy pages; the deltas below are bounded and explained.

---

## 2. Pages moved (old → current)

All 48 Table-1 rows resolved (worklist: **48/48 resolved, 0 unresolved**). No page
was guessed. Category-level moves:

| Old dir (O1) | New home (S3) | Notable |
|---|---|---|
| `1-foundations-history/` | `foundations-and-the-fourth-amendment/` | |
| `2-legal-system-research/` | `legal-system-research-and-reference/` | |
| `3-what-is-a-search/` | split across `foundations-…/` (FA Framework/Checklist/Recalibration re-homed), `searches/`, `instructor-craft-and-study/` (CREW) | |
| `4-what-is-a-seizure/` | `seizures/` (+ `seizures/arrests/`) | |
| `5-levels-of-suspicion/` | `standards-of-proof/` | |
| `6-warrant-requirement/` | `the-warrant/` | split into getting/executing children |
| `7-exceptions-warrant/{7a,7b}/` | `warrant-exceptions/` (+ `home-entry-and-search/`, `programmatic-and-special-needs-searches/`, `searching-a-person/`, `searching-a-vehicle/`); Plain View re-homed to `searches/` | |
| `8-exclusionary-rule-remedies/` | `the-exclusionary-rule-remedies-and-standing/` | ER dissolved into sub-umbrella |
| `9-confessions-interrogation/` | `confessions-…-fifth-amendment/`; Sixth-Am RtC → `the-right-to-counsel/`; Eyewitness ID → `fair-trial-and-reliability-doctrines/` | |
| `10-use-of-force-liability/` | `use-of-force-and-liability/`; Brady → `fair-trial-…/` | |
| `11-adjacent-doctrines/` | dissolved; Entrapment → `fair-trial-…/` | |
| `12-instructor-craft-study/` | `instructor-craft-and-study/` | |

### Three Table-1 parents dissolved into sub-umbrella `index.md` LANDINGS

Not anticipated by the change-list's path scheme. Rows **6, 8, 28** have no
standalone page; the parent prose now lives in a substantive `index.md` landing
(the split children sit beside it):

| # | Old page | Current landing (word count) | Children |
|---|---|---|---|
| 6 | Two Definitions of Search.md | `searches/two-definitions-of-search/index.md` (3,533 w) | Trespass, Reasonable Expectation of Privacy |
| 8 | The Third-Party Doctrine and Digital Surveillance.md | `searches/the-third-party-doctrine-and-digital-surveillance/index.md` (2,200 w) | Cell-Site Simulators, Reverse-Keyword & Geofence, Real-Time Tracking, IGG (+ Title III sibling) |
| 28 | The Exclusionary Rule.md | `the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/index.md` (4,795 w) | Fruits & Attenuation, Good-Faith, Inevitable Discovery |

**Partition consequence:** the change-list header excludes "12 category `index.md`
stubs (14–18 words each)". Post-S3 the navigational category/sub-umbrella stubs grew
to **74–239 words** (21 of them), while these three split-parent landings run
**2,200–4,795 words**. The survey therefore separates them by body word count
(threshold 400, a clean gap: max stub 239 ↔ min landing 2,200) and **includes** the
three landings as substantive pages while excluding the 21 nav stubs, `about.md`,
`flashcards.md`, and the root `content/index.md` (2,771 w, S3-owned master index).
Net substantive set = **89 pages** (48 Table-1 pages, with rows 6/8/28 now landings,
+ 41 Table-2 nodes).

---

## 3. Corpus-flag deltas vs the 2026-07-03 snapshot (Table 3)

| Pass | Snapshot | Current | Cause |
|---|---|---|---|
| TEACH-03 slip-op (doctrine) | 76 / 20 pp | **65** / 89 pp | 76 − 11 = 65: the ONLY slip-ops converted are the pattern page's (Knock and Talk 11→0). Every other doctrine page's count is unchanged (Emergency Aid 8, §1983 9, Exigent 7, Plain View 5, Community Caretaking 5, Border 4 all EXACT vs snapshot). The 41 stub nodes add 0. |
| TEACH-03 slip-op (case pages) | 43/47 case pages | **242 hits / 607 case pages** | S6 minted the full case corpus; S2/S6-owned half (reported separately per Table 3). |
| TEACH-05 em-dash | 3,943 / 153,274 w / 48 pp (25.7/1k) | **4,148 / 170,110 w / 89 pp (24.4/1k)** | +41 stub nodes + split landings add ~17k words / ~205 em-dashes; pattern page 96→38. Rewrite pass not run corpus-wide. Per-page densities drift slightly from S5 conversion (Common Law Origins 20.7→20.1; ER 44.1→44.0; Two Definitions 38.2→37.6). |
| TEACH-02c leak lines | 41 / 19 pp (c1=23,c2=10,c3=5,c4=1) | **59** (c1=23, c2=10, **c3=24**, c4=2) | c1/c2 EXACT. **c3 meta-intro proliferated 5→24** — S5/S6 templated a standardized `Role-based … no SCOTUS … homes to Key cases` developments-intro onto nearly every LCD/RD section. c4 1→2 (Tents gained "(woven in)"). |
| TEACH-04d inverted labels | 21 / 5 pp | **36 / 11 pp** | FA Framework 6→12 (hub gained case rows); 6 more pages gained inverted weight cells as S6 populated Key/Related tables (Case Index 3, Collective Knowledge 2, Brady 1, Reading&Citing 1, Two-Def landing 1, SIA 1). FA Recalibration 9, Three Golden Rules 3, Common Law Origins 2, Federal Court System 1 unchanged. |
| TEACH-04e field-framing | 19 / 13 pp | **4 / 4 pp** | **METRIC DIFFERENCE, not migration.** My detector counts the exact donor label "Field framing (the 'apply it' angle)" (Abandonment, Seizure of the Person, Terry, §1983). The snapshot's 19 evidently used a broad officer-framing heuristic — spot-check confirms Tents still carries "Apply it" (:23) and Brady "In the field" (:34), i.e., officer-framing prose the label-detector correctly excludes. TEACH-04e is NOT ~discharged; targets must be re-derived from officer-framing prose at authoring. |
| TEACH-08 RD-family heading | 35 pp (34 + 1) | **34 pp** (33 "Recent developments" + 1 "& subsequent treatment"); 2 pp on LCD standard | Knock and Talk migrated RD→"Lower-court developments" (pattern page). PC/RS was already conformant (both now on LCD). |
| TEACH-12a missing H1 | 18 pp | **17 pp** | Knock and Talk gained its H1 (pattern page). The other 17 legacy pages still lack H1. The 41 placed-stub nodes all carry H1. |
| TEACH-12b legacy Rule skeleton | 6 pp | **6 pp** (unchanged) | Common Law Origins, FA Analysis Checklist, FA Framework, FA Recalibration, CREW, Three Golden Rules — EXACT match to the change-list's Rule-skel rows (1,2,3,4,46,47). |

---

## 4. Fixes already discharged

Only the pattern page discharged defects — cleanly and completely:

- **Knock and Talk (row 23, PATTERN PAGE):** slip-op 11→0; H1 added; RD→"Lower-court
  developments"; em-dash 30.4→10.1/1k; leak lines 0; `> [!rule]` + `**Apply it.**`
  present; `status: draft`. This is the normative exemplar and is the single landed S7 rewrite.
- **PC/RS (row 5):** already on the "Lower-court developments" heading standard
  (change-list already noted this) — TEACH-08 no-op for this page (but still carries
  1 class-3 meta-intro leak at its LCD intro, and the TEACH-04a/04f `:66` fixes are unverified pending rewrite).

**Nothing else is discharged.** The Knock-and-Talk mockup items the task asked me to
check are DONE (implied-license framing, pattern template) and reflected in the page's
cleared flags; no other named per-page fix shows as landed in the survey.

---

## 5. Table-2 node existence (all present as stubs)

**45/45 Table-2 rows located; 0 absent.** Breakdown: **41 placed-empty stubs**
(draft, ~30–37 words, "Placed by S3" placeholder), 1 in-page host (#12 Plain Feel —
Dickerson/plain-feel content present in Plain View Doctrine.md), 2 retained-parent
(#31 Exigent Hot Pursuit = the retained parent page; #33 Securing the Scene =
retained parent; both are Table-1 legacy pages), 1 cross-ref (#45 Automobile
Exception = Table-1 row 19, re-parented, not new prose).

Notes for the orchestrator:
- **#31 (Exigent — Hot Pursuit)** did NOT split into a new "Hot Pursuit" file; the
  parent `Exigent Circumstances and Hot Pursuit.md` was RETAINED (still row 24's
  page) and only `Destruction of Evidence.md` (#32) split out as a new stub. Author
  Hot-Pursuit prose on the retained parent, or rename per S3 intent — a naming
  decision to confirm, not a Phase-0 fix.
- **#40 (Qualified Immunity)** exists as a stub, but the §1983 parent (row 39) still
  carries its full O1 name `Section 1983 Liability and Qualified Immunity.md` — the
  parent has NOT been renamed to "Section 1983 & Municipal Liability" per the split
  design. Flag for S3/authoring reconciliation.
- **#23 filename** is `Scope Manner and Related Issues.md` (no commas) vs the
  change-list node "Scope, Manner & Related Issues" — resolved by basename; cosmetic.

---

## 6. Change-list items that no longer match reality

1. **Path scheme** — every Table-1 path is stale (O1 numbered dirs). Superseded by
   the current-path column in `S7-WORKLIST.md`.
2. **Rows 6/8/28 have no standalone page** — they are sub-umbrella `index.md`
   landings (§2 above). The change-list assumed a same-named page survives.
3. **`index.md` stub partition** — the "14–18 words each" description is stale (nav
   stubs are now 74–239 w). Survey uses a word-count threshold; documented.
4. **TEACH-04e count (19)** — a broad officer-framing heuristic; the literal label
   count is 4. The 19-hit / 13-page working set must be re-derived from the actual
   officer-framing prose, not treated as "mostly done."
5. **TEACH-02c c3 (5) and TEACH-04d (21)** — both grew (24 and 36) via S5/S6
   templating and case-table population; the R8/TEACH-04d passes are LARGER jobs than
   the snapshot implies. c1 (23) and c2 (10) are unchanged and reliable.
6. **A supplementary leak family** exists that the change-list's c1 (23) does not
   count: a lowercase Sources-line variant `; no standalone case page)` adds ~27
   more R8-strippable annotations (loose corpus count of "no standalone case page"
   = 50 vs the 23 template form). Kept OUT of the c1 metric for baseline
   comparability, surfaced here so R8's scope is not undercounted.

---

## 7. Discipline confirmation

- Tiers carried UNCHANGED from the signed change-list (spec R2); zero tier edits.
  No tier looked clearly wrong against the survey; none flagged.
- 0 CourtListener calls. 0 mutations under `content/` (git `content/` clean after all runs).
- `scripts/s7/` did not pre-exist (no conflict). Survey `--self-test`: PASS (46 checks).
  Both generators deterministic (byte-identical re-runs).
- Nothing committed.
