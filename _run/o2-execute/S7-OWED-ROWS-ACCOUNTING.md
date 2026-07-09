# S7 Owed-Rows Accounting — the zero-drop proof

> **O2 EXECUTE · branch `overhaul2/execute` · HEAD `66d8f79` · 2026-07-09.**
> Worker: S7 CLOSE (`claude` / `claude-opus-4-8`). Machine accounting of the two owed classes the S6
> handoff (§2.1, §2.2) transferred to S7: the **home-page Key/Related rows** and the **non-page
> placements**. Rule: **ZERO silent drops** — every owed unit gets a landing site or an honest terminal;
> anything unaccounted is surfaced, not hidden. Writer ≠ checker — the orchestrator adjudicates the
> residue class.

---

## Part A — Home-page rows (R8 E2/E3)

### A.0 The owed count, reconciled
The S6 handoff owed **158 `home_rows[]`** (148 key + 10 related) across the 148 authored records. During
S7 the D7 SACO mint wave (mini-lane L2) appended **3 case pages** (Nora / Al-Azzawy / Vaneaton) to the
authored ledger, each with its own key+related rows. The **current** `s6-authored-ledger.jsonl` therefore
holds:
```
authored ledger rows: 151        (148 S6 + 3 S7-minted)
total home_rows      : 164        (151 key + 13 related)   ← 158 owed + 6 from the 3 S7 mints
```
All 164 are accounted below.

### A.1 Discharge tally (machine)
For every `home_row {home, stem}` I checked (a) the exact ledger `home` page for the case wikilink/name,
(b) failing that, every other doctrine page (index excluded), (c) failing that, the whole corpus + the
case's own frontmatter `homes[]`:

| Class | Count | Meaning |
|---|---:|---|
| **Discharged on the exact ledger home page** | 83 | case wikilinked/named on the page the ledger row names |
| **Discharged on a successor doctrine page (re-homed)** | 63 | S7 split/dissolution moved the case to a sibling/child page |
| **Frontmatter-homed but not body-materialized** | ~18 | live frontmatter home + Case Index row + coverage terminal, but no Key/Related row on the (table-bearing or table-less) home page |
| **Not found anywhere / dead frontmatter home** | **0** | — |
| **TOTAL** | 164 | |

**Zero silent drops in the strong sense:** every one of the 164 case pages persists, every frontmatter
`homes[]` resolves to a **live** doctrine page, and the coverage ledger confirms it
(`151/151/151 authored page+record+rename`, 0 conflicts — Part C). No case vanished from the corpus.

### A.2 The ~18 frontmatter-homed-but-not-body-materialized rows (the honest residue)
These retain a live frontmatter home + a Case Index row + a coverage-ledger terminal (so **not** drops),
but the Key/Related row was not written into the home page's prose. Two sub-classes:

**(i) Home page is a lean R2 overview — carries NO case table by design (discharge = frontmatter + index).**
Legitimate; a table row is structurally impossible on an R2 overview (LINT-19).
- `Stone v. Powell`, `United States v. Blue`, `United States v. Caceres` → **[[The Exclusionary Rule]]**
  (`the-exclusionary-rule/index.md`, no case-table). Batch-15 adjudicated the boundary trio
  "**retained on the persisting overview**" — i.e. frontmatter-homed to the overview, the R2 conversion
  removed its tables. DOCUMENTED.
- `South Dakota v. Neville` → **[[Confessions, Interrogation & the Fifth Amendment]]** (index, no table).
  (Its homes-wikilink was repaired in repair-phase-(a).)

**(ii) Home page HAS a case table, but the case was not added to it — honest-residue.**
- **§1983 out-of-remit satellites** → **[[Section 1983 Liability and Qualified Immunity]]** (file kept as
  the §1983 & Municipal page, which has a table): `Dupree v. Younger`, `FBI v. Fikre`, `Nance v. Ward`,
  `Perttu v. Richards`, `The GEO Group, Inc. v. Menocal`, `Gutierrez v. Saenz`, `Olivier v. City of
  Brandon`. These are §1983-mechanics / PLRA / method-of-execution / prospective-relief cases **outside
  the search-and-seizure remit** (the S6 mega-node's orbit). Batch-20 **documented GEO Group + Fikre as
  "adjudicated OUT of cat-11 scope"**; the other 5 are the honest-residue tail — kept frontmatter home,
  not table-materialized, S8/S9 to decide (excluded-remit vs brief-mention).
- `Ex parte Jackson`, `Rochin v. California` → **[[Common Law Origins]]** (Tier-C, has table). Rochin is
  already S9-owed (handoff §4, history-page Field-I promotion). Ex parte Jackson (1878 mail-privacy) is
  honest-residue.
- `McDonough v. Smith` → **[[Malicious Prosecution under the Fourth Amendment]]** (accrual case; likely a
  brief-mention).
- `United States v. Carpenter (6th Cir. 2019 remand)` → **[[The Good-Faith Exception]]**.
- `Colonnade Catering Corp. v. United States` → **[[Special Needs and Administrative Searches]]** (W10
  mini-wave add; batch-13 intended "closely-regulated Key" — not detected in the body, honest-residue).

**Check-precision caveat:** the strict machine grep also flagged `Northrup v. City of Toledo Police
Dept` and `United States v. Robinson (4th Cir. en banc)`; a direct re-grep **confirms Northrup IS on
[[Terry Stops and Reasonable Suspicion]]** (false-negative of the strict matcher), and Robinson is
ambiguous (multiple "Robinson" pages). So the genuine not-materialized set is **~16**, all with live
homes + terminals. This is the **Cook-caveat class** (honest-residue) — surfaced for S8/S9, zero
silent drops.

### A.3 Dead-parent → successor map
Home_rows whose `home` field names a **dissolved parent file** (9 rows across 3 vanished files); the
cases were re-homed onto the successors (Part A.1 confirms 0 land nowhere). Full S7 dissolution map:

| Dead / dissolved parent | Fate | Successor pages | Batch |
|---|---|---|---|
| **Probable Cause and Reasonable Suspicion** (PC/RS) | SPLIT | Reasonable Suspicion (A) · Probable Cause (A) · Proof Ladder (C) | 1 |
| **Two Definitions of Search** (index) | severed → lean overview | Trespass (A) · Reasonable Expectation of Privacy (A) · overview | 2 |
| **The Warrant Requirement** | DISSOLVED entirely (no App-A node) | PC-in-Affidavit (A) · Neutral Magistrate (B) · Particularity (A) · Franks (B) · Knock-and-Announce (A) · Detention-at-Scene (B) · Scope-Manner (B) **+ category landing** | 10 |
| **Search Incident to Arrest** (SIA) | DISSOLVED (across 2 sub-umbrellas) | SIA Persons (A) · SIA Cell Phones (A) · SIA Alcohol Tests (B) · SIA Vehicles (A) | 11 |
| **The Exclusionary Rule** (ER index) | severed → R2 overview | Fruits & Attenuation (A) · Good-Faith Exception (A) · Inevitable/Independent (B) **+ persisting overview** | 15 |
| **Special Needs** (strand extraction) | extractions | Inventory Searches (B) · Checkpoints & Roadblocks (B) · Border Searches (B, re-parent) | 13 |
| **§1983 mega-node** | DISSOLVED | §1983 & Municipal Liability (A, filename kept) · Qualified Immunity (A) · Suing Federal Officers (B) · Absolute Immunity (C) | 20 |

The 9 dead-parent `home` fields (5 → The Warrant Requirement, 3 → Search Incident to Arrest, 1 → PC/RS)
are the S6-original pointers; discharge landed on the successors above. (The authored ledger `home`
fields were never hand-edited — the assembler is single-writer — so they legitimately still name the
S6-era parent; the successor re-homing is what Part A.1's 63 "re-homed" count captures.)

---

## Part B — Non-page placements (`R8-NONPAGE-LEDGER.json`, 58 + 3 escalations)

Counts (from the ledger): `noted_orders_and_watch_fold 12 + mentions_bullets 44 + split_blocks 2 = 58`,
plus `escalation_resolutions 3`. Machine check: **all 56 target pages exist (0 missing)**.

### B.1 Noted-orders / watch / fold — 12 (terminal states; on-page naming NOT required)
McCoy v. Alamu · Ramirez v. Guadarrama · N.S. v. Kansas City · Villarreal v. Alaniz (noted-order →
Use of Force / Retaliatory Arrest); Baxter v. Bracey · Cope v. Cogdill · Johnson v. Prentice
(noted-order → Qualified Immunity); Bovat v. Vermont (noted-order → Curtilage); Price v. Montgomery
County (noted-order → §1983); Noem v. Vasquez Perdomo (**watch** → Terry Stops); Lombardo v. St. Louis ·
King v. Brownback (**fold** → Use of Force / §1983). These are cert-stage orders / folds / watch items —
their terminal is the disposition; they need not be prose-named. **Accounted.**

### B.2 Split-blocks — 2 (BOTH discharged)
- **Officer-created-danger / pre-seizure-reckless split** → `Use of Force.md`. Batch-20: placed,
  ADJUDICATED **split-block-not-node**; Mendez/Barnes carry; Allen-v-Muskogee/Billington NOT NAMED
  (fail-closed, no terminals). ✓
- **Inevitable-discovery active-pursuit split-block** → the ER family. Batch-15: LANDED on **Inevitable
  Discovery and Independent Source** — Satterfield required-side (★846, MCP-verified) vs Kennedy /
  Cunningham not-required terminals. ✓

### B.3 Mentions & bullets — 44 (24 placed on-page · 20 retained as brief-mention terminals)
A machine sweep of each target page found **24** materialized. The other **20** are **not** on their
target page **but every one carries a `brief-mention` terminal in the coverage ledger** (spot-checked all
16 distinct: Addington v. Texas, In re Winship, Coleman v. Alabama, Hunter v. Bryant, Marron v. United
States, Reid v. Georgia, United States v. Landeros, Kalina v. Fletcher, United States v. Di Re, United
States v. Gratkowski, United States v. Kennedy, Lefkowitz v. Cunningham, United States v. Vergara,
Killian v. United States, United States v. Morrison, United States v. Valenzuela-Bernal — all
`terminal: brief-mention`). **This is NOT a drop:** LINT-17 fails only a prose-**named** case with no
terminal; a terminal case left un-named is permitted. These 20 are the **S8 linking-pass / plain-italic
class** (some target index pages that became lean R2 overviews and cannot host bullets). **Accounted; S8
owns the prose-mention decision.**

### B.4 Escalation resolutions — 3 (all resolved)
- `Commonwealth v. Serge` → **excluded-remit** (citation-format specimen, S8 page).
- `District of Columbia v. Heller` → **excluded-remit** (2A; corpus annotates "not Fourth Amendment
  authority").
- `United States v. Cruz` → **watch_s7_deferred**, RESOLVED at batch-20: S7-owned disposition =
  **TERMINAL WATCH** fail-closed (lake = Negron-Cruz frontier stub, no verified proposition; "not found ≠
  fabricated"; S2 may promote). ✓

---

## Part C — The coverage-ledger close-check (the machine backstop)

```
$ python3 _overhaul2/scripts/build_coverage_ledger.py
  authored 151 + brief-mention 61 + excluded-remit 26 + folded-alias 8 + removed 2
           + unverifiable 1 + watch 3 = 252 distinct captions
  authored verified: page=151 rec=151 rename=151  (of 151)
  folded-alias survivors: ok=8 bad=0
  conflicts: 0   row-errors: 0
  RESULT: PASS
```
Every authored case page has a page-file + lake-record + manifest-rename (151/151/151); every
folded-alias names a live survivor (8/8). This is the independent backstop that **no home_row's case
page vanished** and **no frontmatter home is dead**.

---

## Verdict

**ZERO silent drops.** All 164 home_rows and all 58 (+3) non-page placements are accounted:
- **146 home_rows body-materialized** (83 exact-home + 63 re-homed-to-successor); **~16-18
  frontmatter-homed-but-not-body-materialized**, every one with a live home + Case Index row + coverage
  terminal (overview-no-table class = legitimate; §1983 out-of-remit satellites + a few history/accrual
  cases = the honest-residue / Cook-caveat class, GEO/Fikre already documented out-of-scope).
- **Non-page:** 12 terminal-state orders/folds/watch + 2 split-blocks discharged + 24 bullets placed + 20
  retained as brief-mention terminals + 3 escalations resolved.
- Coverage ledger **PASS**, 0 conflicts, 0 row-errors.

The residue the orchestrator/S8/S9 should note: the ~16 not-materialized rows (mostly §1983 out-of-remit
satellites — likely excluded-remit re-terminals) and the 20 un-placed brief-mentions (S8 linking pass).
None is a drop; all are documented terminals.
