# R8 WAVE W4 — batch report (roster 2)

- **Lane/model:** r8-wave-author · `claude-opus-4-8`
- **As-of:** 2026-07-07 · **Branch:** overhaul2/execute · **Base HEAD:** fdbf931 (git commit: none — orchestrator commits at the gate)
- **Batch:** W4 = 18 roster D1-flip rows. **Outcome:** **11 minted** · **7 journaled skips** (1 known-ahead + 1 empty-cite deferred-recovery + **5 wrong-case mis-keys discovered on read**) · 0 escalations left open.
- **CL discipline:** single serial MCP lane, **~55 CL calls, 0×429**. No parallel CL, no CL REST, no self-relaunch. One incidental extra read (Berkowitz sibling opinion 9481419) to star-verify a reporter pincite during remediation.
- **Delta vs plan estimate:** planning expected ~17 mints; landed **11**. The 6-mint shortfall is 5 newly-discovered wrong-case clusters + the empty-cite Larson — surfaced, not trimmed (identity-scrutiny discipline; two prior W-batch mis-keys were caught the same way).

## Per-row outcomes

### Minted (11) — all born `under_review` (⚪), one page each

| # | Page | Cite | Home(s) · role · prong | Rule pincite (verbatim quote string-matched to CL) | pinpoint_status |
|---|---|---|---|---|---|
| 1 | State v. Karston | 588 So. 2d 165 (La. Ct. App. 1991) | Curtilage · Key · a | 588 So. 2d **at 167** ("…the defendant, a tenant in the apartment complex, had a reasonable expectation of privacy in the area outside his apartment. This legitimate privacy interest was violated when Officer Dabdoub, without probable cause, opened the gate and entered the courtyard.") | reporter star-verified (`^pin-167`) |
| 2 | State v. Weaver | 349 S.W.3d 521 (Tex. Crim. App. 2011) | Curtilage · Key · a | 349 S.W.3d **at 523** ("Because we agree that the resolution of this case turns on the scope of Mr. Weaver's consent, we affirm…") | reporter star-verified (`^pin-523`) — **lake cite-selection quirk flagged (see below)** |
| 3 | State v. Wint | 236 N.J. 174 (2018) | Miranda Waiver & Invocation · Key · a | 236 N.J. **at 181** ("Wint remained in continuous pre-indictment custody for a period of six months…Therefore, no 'break in custody' occurred within the intendment of *Shatzer*.") | N.J.-reporter page-label (`^pin-181`) |
| 4 | United States v. Aigbekaen | 943 F.3d 713 (4th Cir. 2019) | Border Searches · Key · a | slip op. **at 14** ("…the object of that suspicion must bear some nexus to the purposes of the border search exception…Because no such nexus existed here, the warrantless, nonroutine forensic searches violated the Fourth Amendment.") | slip-style (A3; CL text slip-paginated) |
| 5 | United States v. Amos | 88 F.4th 446 (3d Cir. 2023) | Seizure of the Person · Key · a | slip op. **at 10** ("When a uniformed officer approaches an individual in the middle of the night in a marked police car and commands that person to stop and raise his or her hands, that is a show of authority.") + *Brendlin* submission rule | slip-style (A3) |
| 6 | United States v. Berkowitz | 927 F.2d 1376 (7th Cir. 1991) | Arrest in the Home · Key · a | 927 F.2d **at 1386** ("Payton prohibits only a warrantless entry into the home, not a policeman's use of his voice to convey a message of arrest from outside the home.") | reporter star-verified via sibling opinion 9481419 (primary object is ¶-numbered — see below) |
| 7 | United States v. Black | 707 F.3d 531 (4th Cir. 2013) | Terry Stops & Reasonable Suspicion · Key · a | slip op. **at 11** ("the Government attempts to meet its Terry burden by patching together a set of innocent, suspicion-free facts, which cannot rationally be relied on to establish reasonable suspicion.") | slip-style (A3) |
| 8 | United States v. Brinkley | 980 F.3d 377 (4th Cir. 2020) | Arrest in the Home · Key · a | slip op. **at 25** ("We hold that reasonable belief amounts to probable cause, and that the police in this case lacked reason to believe Brinkley resided in the Stoney Trace apartment and would be present when they entered.") | slip-style (A3) |
| 9 | United States v. Camou | 773 F.3d 932 (9th Cir. 2014) | Automobile Exception · Key · a | 773 F.3d **at 944** ("We hold, however, that cell phones are not containers for purposes of the vehicle exception.") | reporter star-verified (`^pin-944`) |
| 10 | United States v. Carlton Williams | 898 F.3d 323 (3d Cir. 2018) | Consent Searches · Key · a | slip op. **at 11** ("…it is his burden to demonstrate that he has withdrawn that consent by pointing to an act or statement that an objective viewer would understand as an expression of his desire to no longer be searched.") | slip-style (A3) |
| 11 | United States v. Daniels | 101 F.4th 770 (10th Cir. 2024) | Terry Stops (Key) + Probable Cause & Reasonable Suspicion (Related x-doctrine) · a | slip op. **at 6** ("the totality of the circumstances known by Officer Idler when he detained Daniels did not amount to reasonable suspicion. As such, Daniels' detention was unreasonable under the Fourth Amendment…") | slip-style (A3) |

Identity re-verified against the CL opinion text for **every** row before authoring (W1–W3 discipline). Each page carries exactly one pinned Rule quote, string-matched **verbatim** to CL text 2026-07-07. Reporter-star `^pin-N` used where CL text star-paginates (Karston 167, Weaver 523, Camou 944); N.J.-reporter page-label (Wint 181); slip-style pins (A3) where CL text carries only slip-op pagination (Aigbekaen, Amos, Black, Brinkley, Carlton Williams, Daniels); Berkowitz reporter-verified at 1386 via the star-paginated sibling opinion (the primary CL opinion object is paragraph-numbered only).

### Skipped (7) — journaled, no mint attempted, not authored on a broken/wrong identity

| record_id | reason | why (verified against CL opinion text) |
|---|---|---|
| united-states-v-cole--9623101 | data-escalation | **Known-ahead (work order):** military-namesake mis-key — cluster 9623101 is an armed-forces-court namesake, not the intended 7th Cir. traffic-stop *United States v. Cole* (21 F.4th 421). Not read (honored the standing directive). Re-key queued in the repair lane. |
| state-v-larson--10657314 | deferred-recovery | `citations.display` empty → work-order step-1 skip (no projectable cite; no CL call spent). Cluster caption = "State of Iowa v. Allysa Marie Luke, n/k/a Allysa Marie Joyce, **a/k/a Allysa Marie Larson**" (Iowa Ct. App. 2025). Recovery lane owns cite recovery; **also flag the identity** — the "Larson" link is only an a/k/a, worth a second look. |
| united-states-v-burgess--9495745 | data-escalation | **WRONG-CASE CLUSTER.** 9495745 = *United States v. Burgess*, 99 F.4th 1175 (10th Cir. 2024) — a Fed. R. Evid. 807 residual-hearsay / child-sexual-abuse appeal (searched: **0 "plain view", 0 "Fourth Amendment"**). The Plain View (Key) + Border Searches homes require the 2009 computer-search-scope *United States v. Burgess*, **576 F.3d 1078** (10th Cir.). Re-key. |
| united-states-v-capers--5306116 | data-escalation | **WRONG-CASE CLUSTER.** 5306116 = *United States v. Capers*, 20 F.4th 105 (2d Cir. 2021) — a RICO / crime-of-violence (*United States v. Davis*) firearm-murder appeal (searched: **0 "Miranda", 0 "interrogation"**). The Miranda Waiver home requires the *Missouri v. Seibert* "question-first" *United States v. Capers*, **627 F.3d 470** (2d Cir. 2010). Re-key. |
| united-states-v-castillo--10322393 | data-escalation | **WRONG-CASE CLUSTER.** 10322393 = *United States v. Castillo*, 126 F.4th 791 (1st Cir. 2025) — a sentencing / plea-agreement-breach appeal (18 U.S.C. § 2244, child abuse; searched: **0 "border"**). The Border Searches home requires the intended border-search *United States v. Castillo*. Re-key. |
| united-states-v-chavez--10329331 | data-escalation | **WRONG-CASE CLUSTER.** 10329331 = *United States v. Javier Ivan Chavez Dominguez*, 128 F.4th 226 (4th Cir. 2025) — an illegal-reentry sentencing appeal (8 U.S.C. § 1326; searched: **0 "collective knowledge", 0 "fellow officer"**). The Collective Knowledge / Fellow-Officer home requires the intended fellow-officer-rule *United States v. Chavez*. Re-key. |
| united-states-v-crumble--4767477 | data-escalation | **WRONG-CASE CLUSTER.** 4767477 = *United States v. Cortez Crumble*, 965 F.3d 642 (8th Cir. 2020) — a *Rehaif* felon-in-possession-of-ammunition / evidentiary-ruling appeal (searched: **0 "abandon"**). The Abandonment home requires the intended abandonment *United States v. Crumble*. Re-key. |

## FINDING FOR THE ORCHESTRATOR — residual wrong-case-cluster class (5 rows)

Five of my 18 roster rows (**Burgess, Capers, Castillo, Chavez, Crumble**) carry clusters that are **internally identity-consistent** (the lake caption/cite matches the actual cluster) but are the **wrong same-caption case** for the doctrinal home. Every one is an ambiguous-surname federal criminal appeal (`United States v. <common surname>`) where the S2 identity search resolved to a modern (2020–2025) hearsay/RICO/illegal-reentry/*Rehaif*/sentencing case instead of the older Fourth-Amendment doctrinal case the home requires. This is the **same class the "consolidated-repair session" was fixing** (per the worklist notes, it re-keyed Black, Williams, Young, Maez, Lewis, Austin, Board-of-County-Commissioners) — these 5 look like residue that repair pass missed. Recommended re-keys are named per-row above (Burgess→576 F.3d 1078; Capers→627 F.3d 470; Crumble, Castillo, Chavez → the intended doctrinal case). None were authored; all seven skips are page-less flagged exceptions awaiting re-key + re-dispatch (tail batch).

## Data notes (non-blocking, for S2/repair)

- **Weaver cite selection:** the lake selected the LEXIS neutral cite `2011 Tex. Crim. App. LEXIS 1320` as `citations.display`/official; the standard reporter cite is **349 S.W.3d 521**. The page header line + Sources present the S.W.3d reporter (reader-correct) with the LEXIS cite noted as parallel; the projected `citation` frontmatter still shows the LEXIS cite. S2 should re-select the S.W.3d reporter as official so the rendered badge matches.
- **Berkowitz lake gap:** the stub omitted `date_decided` + `docket`; the cluster carries **1991-03-15 / No. 89-2125** (now in the page prose + comment). Projected frontmatter `date_decided`/`docket` render empty until S2 backfills.
- **Berkowitz pincite:** the primary CL opinion object (557342) is paragraph-numbered without 927 F.2d star pagination; the reporter-paginated sibling opinion **9481419** star-paginates the reporter and places the quoted holding at **1386** (used, and noted in Sources). No fabricated pincite.

## Quote-fidelity self-check (G-protocol, writer-side; S9 certifies)
Every minted page's single Rule quote was copied verbatim from the CL opinion text and carries a recognized pincite (reporter `at N`, N.J. page-label, or `slip op. at N`) on the same line. Slip-style pins per S2 A3 wherever the CL text lacked reporter star-pagination. Treatment sections honestly render each birth as ⚪ `under_review` (no over-claim of verification); disposition/authorship named from the opinion caption + signature block. Two-home row (Daniels) lists both homes in "Appears on" (Terry Stops = Key, Probable Cause & Reasonable Suspicion = Related x-doctrine).

## Body-only prose finalization (ratified W1–W3 precedent; frontmatter/lake/manifest/ledger/page↔record binding UNTOUCHED)
The mint gate covers only LINT-14/15/16, so a first-write pass introduced **2 LINT-9** (mid-line `^pin` on Weaver + Camou, where explanatory prose followed the pincited quote) and **6 LINT-2** (inline quotes lacking a nearby recognized pincite, incl. Berkowitz's `(¶ 45)` paragraph-pincite which `PINCITE_RE` does not match). Remediated **body-only**:
- **Weaver / Camou:** reordered the Rule paragraph so the pincited holding quote is last (`^pin-N` ends its line) and de-quoted the secondary "premised…"/paraphrase so no orphaned quote was created.
- **Berkowitz:** replaced the `(¶ 45)` paragraph-pincite with the star-verified reporter pincite **at 1386** (clears all three same-line LINT-2s and upgrades the pincite).
- **Carlton Williams / Weaver-Treatment:** de-quoted two factual/shorthand phrases.
LINT-14/15/16 re-checked **0** on the four edited pages (binding intact). Net: LINT-2 corpus 316→**310**, LINT-9 299→**297** (the 8 findings my mint introduced, removed).

## Lint delta (baseline = post-W3 corpus; run_all non-CL roster)
- **Mint gate (LINT-14/15/16): all 11 pages 0/0/0** at dry-run, post-mint, and post-remediation.
- **Case Index regenerated → 523 rows (+11, exactly the W4 pages)**, 0 blank Good-law cells; diff = 11 insertions, no churn on prior rows.
- **`npx quartz build` → SUCCESS**, 625 Markdown files parsed (+11), 2215 emitted; only benign git-untracked-date warnings on the new files.
- **Corpus totals:** HIGH 4789→**4833 (+44)**, MED 2737→**2772 (+35)**, LOW 135 (=). Findings attributable to my 11 pages are **exclusively the accepted endemic classes** — LINT-10 em-dash ×43 (S8-owned, the signed register uses em-dashes), LINT-5 bare-case/wikilink ×33 (S8 D13 materialization class, incl. self-name refs), LINT-7 glossary/"knock-and-talk"-family term-register ×2 — plus the Case Index regen's rows in the same profile (LINT-10/5/7 + LINT-4 authority-lexicon on new index rows). **Zero new-signature violations** (LINT-9/2/3/4/8/12/14/15/16 all clean on my pages after remediation).
- **Known-endemic S8-owned reds (LINT-10, LINT-5) unchanged in class;** no delta reported beyond my pages' accepted contribution. LINT-19 (8, overview case tables) and LINT-21 (10, bound-PENDING overrides) are pre-existing corpus reds untouched by this batch.

## Working-tree note (NOT mine)
`scripts/s2/project.py`, `scripts/s6/mint_page.py`, `scripts/s6/stamp_slip_only.py`, and `R8-PIPELINE-BUILD-REPORT.md` show as modified in the working tree — these are the **parallel offline lane's** work (per the dispatch: "offline scripts/s6+s2 work only"), not this authoring lane's. LINT-12 = 0 corpus-wide confirms my minted pages' managed frontmatter is consistent with the current projector, so no mid-run projector drift reached my pages.

## For the orchestrator
1. **Re-key + re-dispatch the 5 wrong-case clusters** (Burgess→576 F.3d 1078; Capers→627 F.3d 470; Castillo→the border-search *Castillo*; Chavez→the fellow-officer *Chavez*; Crumble→the abandonment *Crumble*) — residual class from the consolidated-repair session.
2. **Larson (state-v-larson--10657314):** recover a citation AND re-confirm identity (the "Larson" link is only an a/k/a on an Iowa Ct. App. 2025 caption).
3. **Cole (united-states-v-cole--9623101):** re-key per the known military-namesake escalation; re-dispatch (tail batch).
4. **Ratify (or revert) the body-only prose finalization** on Weaver / Camou / Berkowitz / Carlton Williams (W1–W3 precedent; LINT-14/15/16 re-checked 0).
5. **S2 data notes:** re-select Weaver's S.W.3d reporter as official over the LEXIS neutral cite; backfill Berkowitz `date_decided` (1991-03-15) + `docket` (No. 89-2125).
6. S7 owes the homes-page Key/Related materialization for the 11 W4 pages from `s6-authored-ledger.jsonl` (incl. Daniels's two homes).
