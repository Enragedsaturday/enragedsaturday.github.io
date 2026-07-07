# R8 WAVE W5 — batch report (roster 3)

- **Lane/model:** r8-wave-author · `claude-opus-4-8` (Opus 4.8 [1m])
- **As-of:** 2026-07-07 · **Branch:** overhaul2/execute · **Base HEAD:** 07c041d (git commit: none — orchestrator commits at the gate)
- **Batch:** W5 = 17 roster D1-flip rows (18 signed − 1 folded-duplicate removed pre-mint). **Outcome:** **15 minted** · **2 journaled skips** (both known-ahead) · **1 escalation** (Davis duplicate, folded out of the plan by the orchestrator before the mint phase). Matches the ~15-mint expectation.
- **CL discipline:** single serial MCP lane, **~61 CL calls total, 0×429** (a ~21-call metadata pass, then — after a mid-batch CL outage and clean reconnect — ~40 read/search calls). No parallel CL, no CL REST, no self-relaunch, no alternate CL access path. One incidental extra read (Maez sibling opinion 9478941) to reporter-verify a pincite on a paragraph-numbered majority.
- **Mid-batch note:** the CL MCP server dropped after the metadata pass and did not restore its tools for the remainder of that session; per standing order I STOPPED and returned a definitive handoff (opinion→cluster map cached, Davis duplicate diagnosed, Hunt reclassified) rather than author any page without a verified pincite. The coordinator restored CL, ratified all three adjudications, and re-dispatched; this report supersedes the outage handoff.

## Per-row outcomes

### Minted (15) — all born `under_review` (⚪), one page each

| # | Page | Cite | Home · role | Rule pincite (verbatim quote string-matched to CL) | pinpoint_status |
|---|---|---|---|---|---|
| 1 | United States v. Ganias | 824 F.3d 199 (2d Cir. 2016) (en banc) | Plain View Doctrine · Key | slip op. **at 3** ("We conclude that the Government relied in good faith on the 2006 warrant… we need not decide whether retention of the forensic mirrors violated the Fourth Amendment, and we AFFIRM…") | slip-style (A3); en-banc majority = opinion **3207498** |
| 2 | United States v. Hanapel | 112 F.4th 539 (8th Cir. 2024) | Entrapment · Key | slip op. **at 8** ("Initial hesitance to engage in criminal conduct does not establish lack of predisposition as a matter of law.") | slip-style (A3) |
| 3 | United States v. Hay | 95 F.4th 1304 (10th Cir. 2024) | TPD & Digital Surveillance (index) · Key | slip op. **at 18** ("Our holding in *Jackson* that pole cameras trained on a house do not violate the Fourth Amendment remains binding law, and *Carpenter*, without more, does not disturb it.") | slip-style (internal slip pagination) |
| 4 | United States v. Hunt | No. 23-2342, slip op. (9th Cir. 2025) | Abandonment · Key | slip op. **at 4** ("When determining a person's intent to abandon, courts should analyze the intent to abandon the device separately from the intent to abandon its data.") | **A3 slip mint** (`slip_only`, opinion 11128224; no F.4th cite yet) |
| 5 | United States v. Kolsuz | 890 F.3d 133 (4th Cir. 2018) | Border Searches · Key | slip op. **at 4** ("…under *Riley*, the forensic examination of Kolsuz's phone must be considered a nonroutine border search, requiring some measure of individualized suspicion.") | slip-style (A3) |
| 6 | United States v. Lee | 274 U.S. 559 (1927) | Fourth Amendment Recalibration · Key | 274 U.S. **at 563** ("Such use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution.") | reporter star-pagination (`^pin-563`) |
| 7 | United States v. Liddell | 517 F.3d 1007 (8th Cir. 2008) | Miranda & Custodial Interrogation · Key | 517 F.3d **at 1009–10** ("…the risk of police officers being injured by the mishandling of unknown firearms or drug paraphernalia provides a sufficient public safety basis to ask a suspect who has been arrested and secured whether there are weapons or contraband…") | reporter star-pagination (`^pin-1009`); majority = opinion **1461978** |
| 8 | United States v. Loera | 923 F.3d 907 (10th Cir. 2019) | Plain View Doctrine · Key | 923 F.3d **at 911** ("…the Fourth Amendment does not require police officers to stop executing an electronic search warrant when they discover evidence of an ongoing crime outside the scope of the warrant, so long as their search remains directed at uncovering evidence specified in that warrant.") | reporter page-label star (`^pin-911`) |
| 9 | United States v. Loines | 56 F.4th 1099 (6th Cir. 2023) | Plain View Doctrine · Key | slip op. **at 13** ("The objects purportedly seen by Kopchak were not immediately and apparently incriminating. Accordingly, the officers lacked probable cause to search the vehicle.") | slip-style (internal slip pagination) — **lake docket mismatch flagged** |
| 10 | United States v. Lyle | 919 F.3d 716 (2d Cir. 2019) | Standing to Challenge a Search · Key | 919 F.3d **at 729** ("…Lyle lacked standing not just because he was an unauthorized driver, but because he was an unlicensed one. Accordingly, Lyle's use of the rental car was both unauthorized *and* unlawful.") | reporter page-label star (`^pin-729`); post-*Byrd* remand |
| 11 | United States v. Maez | 872 F.2d 1444 (10th Cir. 1989) | Arrest in the Home · Key | 872 F.2d **at 1451** ("Those courts have held that *Payton* is violated where there is such a show of force that a defendant comes out of a home under coercion and submits to being taken in custody.") | reporter page **verified via the court's own cross-reference** to p. 1451 (majority object 521939 is paragraph-numbered) |
| 12 | United States v. Massenburg | 654 F.3d 480 (4th Cir. 2011) | Collective Knowledge / Fellow-Officer Rule · Key | 654 F.3d **at 493** ("…the collective-knowledge doctrine simply directs us to substitute the knowledge of the *instructing officer or officers* for the knowledge of the *acting officer;* it does not permit us to aggregate bits and pieces of information from among myriad officers, nor does it apply outside the context of communicated alerts or instructions.") | reporter star-pagination (`^pin-493`) |
| 13 | United States v. May-Shaw | 955 F.3d 563 (6th Cir. 2020) | Curtilage · Key | slip op. **at 12** ("May-Shaw has failed to establish that the carport constituted the curtilage of his apartment; the drug dog sniff therefore did not constitute a search.") | slip-style (internal slip pagination) |
| 14 | United States v. Mayville | 955 F.3d 825 (10th Cir. 2020) | Traffic Stops · Key | slip op. **at 1** ("*Rodriguez* does not require courts to second-guess the logistical decisions of officers so long as their actions were reasonable and diligently completed within the confines of a lawful traffic stop. This is because reasonableness — rather than efficiency — is the touchstone of the Fourth Amendment.") | slip-style (internal slip pagination) |
| 15 | United States v. Mendez | 103 F.4th 1303 (7th Cir. 2024) | Border Searches · Key | slip op. **at 13** ("…brief, manual searches of a traveler's electronic device are 'routine' border searches requiring no individualized suspicion.") | slip-style (internal slip pagination) |

Identity re-verified against the CL opinion text for **every** row before authoring (W1–W4 discipline). Reporter-star `^pin-N` where CL star-paginates (Lee 563, Liddell 1009, Loera 911, Lyle 729, Massenburg 493); Maez reporter-page-verified via the majority's own cross-reference (the primary object is paragraph-numbered); slip-style pins (A3) where the CL text carries only slip/internal pagination (Ganias, Hanapel, Hay, Kolsuz, Loines, May-Shaw, Mayville, Mendez); Hunt is the A3 **slip mint** (`citations.slip_only`, no reporter cite yet).

### Skipped (2) — journaled, both known-ahead (not read, not authored)

| record_id | reason | why |
|---|---|---|
| united-states-v-holcomb--10670143 | data-escalation | **Known-ahead (work order):** the wiki cites a **WITHDRAWN** opinion (132 F.4th 1118); investigation queued. Not authored from a withdrawn opinion. |
| united-states-v-lewis--9424185 | deferred-recovery | **Known-ahead (work order):** genuine CL citation gap (empty `citations.display`); tail-batch (W9) recovery class. |

### Escalation (1) — Davis duplicate (folded pre-mint; ratified)

| record_id | reason | resolution |
|---|---|---|
| united-states-v-davis--4881258 | folded-duplicate | Diagnosed during the CL-outage phase: cluster 4881258 / opinion 4685037 (*United States v. Howard Davis*, 997 F.3d 191, 4th Cir. 2021 — Gant extended to a backpack SITA) is **already authored** at `content/cases/United States v. Howard Davis.md`, with the Search Incident to Arrest home already placed. The stub (caption "United States v. Davis") is the redundant frontier twin; the mint CLI collision-checks by stem/filename, not cluster, so it would have silently minted a second page for the same opinion. **RATIFIED and folded** by the orchestrator (W5 count 18→17); the lake-record fold rides the next repair micro-batch. A mint **stem-vs-cluster guard** is queued. |

## Data notes (for S2)
- **loines lake docket mismatch:** `identity.docket = "21-1516"`, but the opinion caption is **No. 22-3073** (D. Ohio No. 1:20-cr-00293-2; 56 F.4th 1099, 6th Cir. 2023). Identity is otherwise fully confirmed (cite + caption + court + year + the plain-view holding match the read opinion); the docket field is stale. The page header + comment carry the correct **22-3073**; the projected `docket` frontmatter will show 21-1516 until S2 backfills.
- **davis lake docket** (moot — stub folded): `19-4930` vs opinion **No. 20-4035**.
- **kolsuz cluster citations empty:** the CL cluster carries no `citations[]`, but the lake stub carries **890 F.3d 133** (used, reader-correct). S2 could enrich the cluster's official cite.
- **Multi-opinion clusters resolved on read:** Ganias en-banc majority = **3207498** (Livingston & Lynch, JJ.; Lohier concurrence, Chin dissent); Liddell majority = **1461978** (Loken, C.J.; Gruender concurrence); Maez majority = **521939** (Holloway, C.J.).

## Quote-fidelity self-check (G-protocol, writer-side; S9 certifies)
Every minted page carries exactly **one** pinned Rule quote, copied **verbatim** from the CL opinion text and carrying a recognized pincite on the same line (`^pin-N` ends its line — LINT-9 clean). Reporter pins used where CL star-paginates; slip-style pins (S2 A3) where the CL text is slip/internal-paginated; Hunt minted via the sanctioned A3 slip cite. Treatment sections render each birth honestly as ⚪ `under_review` (no over-claim of verification); disposition/authorship named from the opinion caption + signature block. Cross-doctrine framing kept honest to each home (e.g., Ganias/Loera on the digital plain-view frontier; Kolsuz/Mendez on the unresolved forensic-device split; Hay on the unsettled pole-camera question — never stated as settled nationwide rules).

## Body-only prose finalization (ratified W1–W4 precedent; frontmatter/lake/manifest/ledger/page↔record binding UNTOUCHED)
The mint gate covers only LINT-14/15/16, so a first-write pass left **21 LINT-2** (inline quotations ≥6 words in Background/Application/Treatment lacking a same-line pincite — the single pinned Rule quote per page was already clean). Remediated **body-only** across 11 pages by **de-quoting** the secondary/narrative phrases (record testimony and characterizations), integrating them as prose while preserving accuracy; the authoritative pinned Rule quote on each page is untouched. Post-remediation: **LINT-2 = 0, LINT-9 = 0** on all 15 pages; **LINT-14/15/16 re-checked 0/0/0** (page↔record binding intact); `npx quartz build` re-run **SUCCESS**.

## Lint delta (baseline = post-W4 corpus; non-CL roster)
- **Mint gate (LINT-14/15/16): all 15 pages 0/0/0** at dry-run, post-mint, and post-remediation.
- **Case Index regenerated → 538 rows (+15, exactly the W5 pages)**, 0 blank Good-law cells; diff = 15 insertions, no churn on prior rows.
- **`npx quartz build` → SUCCESS**, 640 Markdown files parsed (+15), 2263 emitted; only benign git-untracked-date warnings on the new files.
- **Corpus totals:** HIGH 4833→**4911 (+78)**, MED 2772→**2814 (+42)**, LOW 135 (=). Findings attributable to my 15 pages are **exclusively the accepted endemic classes** — LINT-10 em-dash ×71 (S8-owned; the signed register uses em-dashes), LINT-5 bare-case/wikilink ×38 (S8 D13 materialization class, incl. self-name refs), LINT-7 glossary term-register ×3 — plus the Case Index regen's new rows in the same profile (LINT-10/5/7 + LINT-4 authority-lexicon). **Zero new-signature violations** (LINT-2/3/4/8/9/12/14/15/16 all clean on my pages after remediation).
- Pre-existing corpus reds untouched by this batch: LINT-19 (8, overview case tables), LINT-21 (10, bound-PENDING overrides).

## For the orchestrator
1. **Commit W5:** 15 new `content/cases/*.md` (Ganias, Hanapel, Hay, Hunt, Kolsuz, Lee, Liddell, Loera, Loines, Lyle, Maez, Massenburg, May-Shaw, Mayville, Mendez), 15 lake stub→record promotions, 15 `s6-authored-ledger.jsonl` rows, the regenerated Case Index (+15), and the W5 wave-plan status update.
2. **S2 data note:** backfill Loines docket **22-3073** (over the stale 21-1516); optionally enrich the Kolsuz cluster's official cite (890 F.3d 133).
3. **Davis fold:** the lake-record fold of `united-states-v-davis--4881258` rides the next repair micro-batch (per your ratification); the mint stem-vs-cluster guard is queued.
4. **Ratify (or revert) the body-only prose finalization** on the 11 de-quoted pages (Hanapel, Hay, Lee, Liddell, Loera, Loines, Lyle, Maez, Massenburg, May-Shaw, Mayville) — LINT-14/15/16 re-checked 0/0/0, build green.
5. S7 owes the homes-page Key/Related materialization for the 15 W5 pages from `s6-authored-ledger.jsonl`.
