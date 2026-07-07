# R8 WAVE W3 — batch report (history D2-render + roster 1)

- **Lane/model:** r8-wave-author · `claude-opus-4-8`
- **As-of:** 2026-07-07 · **Branch:** overhaul2/execute · **Base HEAD:** 5a05f8b (git commit: none — orchestrator commits at the gate)
- **Batch:** W3 = 19 rows. **Outcome:** 17 minted · 2 journaled `data-escalation` skips · 1 disclosed lint-gap escalation (page kept).
- **CL discipline:** single serial MCP lane, ~51 CL calls, **0×429**. Two transient upstream errors (one 502 Bad Gateway, one "MCP server connection lost") — YIELDed and backed off (70s, then 90s) before retrying, per L4 discipline. No parallel CL consumer. No CL REST calls.

## Per-row outcomes

### Minted (17) — all born `under_review` (⚪), one page each

**History (D2 render · PRACTICES §7) — 5.** Rendered as HISTORY, never disguised as live law: header-line weight demoted to **Historical**, precise verb + wikilinked successor + demotion, all under the ⚪ born-`under_review` banner (the lake stubs carry Field-I `unverified`, so the subsequent-history note is authored orientation, not machine-certified — see "History-render honesty" below).

| # | Page | Cite | Home · role | Rule pincite (verbatim) | §7 successor |
|---|---|---|---|---|---|
| 1 | Arkansas v. Sanders | 442 U.S. 753 (1979) | Automobile Exception · Historical/origin | 442 U.S. at 766 ("we hold that the warrant requirement…applies to personal luggage taken from an automobile…") | Overruled by [[California v. Acevedo]] (1991) |
| 2 | Frank v. Maryland | 359 U.S. 360 (1959) | Special Needs & Admin. · Historical/origin | 359 U.S. at 373 ("we cannot say that the carefully circumscribed demand…deprived him of due process") | Overruled by [[Camara v. Municipal Court]] (1967) |
| 3 | A Quantity of Copies of Books v. Kansas | 378 U.S. 205 (1964) | The Warrant Requirement · Historical/origin | 378 U.S. at 211 ("in not first affording P-K an adversary hearing, the procedure…was constitutionally deficient") | Foundational origin (not overruled); Marcus–[[Stanford v. Texas\|Stanford]]–[[Heller v. New York\|Heller]]–Roaden line |
| 4 | Robbins v. California | 453 U.S. 420 (1981) | Automobile Exception · Historical/origin | 453 U.S. at 428 ("such a container may not be opened without a warrant, even if…during the…search of an automobile") | Overruled by [[United States v. Ross]] (1982) |
| 5 | Trupiano v. United States | 334 U.S. 699 (1948) | Search Incident to Arrest · Historical/origin | 334 U.S. at 705 ("It is a cardinal rule that…agents must secure and use search warrants wherever reasonably practicable") | Rabinowitz (1950) → superseded by [[Chimel v. California]] (1969) |

**Roster D1-flips — 12.**

| # | Page | Cite | Home · role · prong | Rule pincite (verbatim) | pinpoint_status |
|---|---|---|---|---|---|
| 6 | Alasaad v. Wolf | 988 F.3d 8 (1st Cir. 2021) | Border Searches · Key · a | slip op. at 16 ("neither a warrant nor probable cause is required for a border search of electronic devices") | slip-style (CL plain_text; no F.3d star pagination — A3) |
| 7 | Alvarez v. City of Brownsville | 904 F.3d 382 (5th Cir. 2018) (en banc) | Brady and Giglio · Key · b | 904 F.3d at **389** ("declines the invitation to disturb its precedent concerning a…right to *Brady* material prior to entering a guilty plea") | star-verified (page-label 389) |
| 8 | Carroll v. Carman | 574 U.S. 13 (2014) (per curiam) | Knock and Talk · Key · a | 135 S. Ct. at **352** ("We do not decide today whether…a police officer may conduct a 'knock and talk' at any entrance…rather than only the front door") | star-verified via S. Ct. parallel (CL text star-paginates S. Ct.) |
| 9 | Carter v. United States | No. 23-CF-0388, slip op. (D.C. 2025) | Seizure of the Person · Key · a | slip op. at 30 ("we hold that Mr. Carter was seized…when Officer DelBorrell requested that he raise his pants") | slip-only (A3) — **see LINT-12 escalation** |
| 10 | Gaetjens v. Winnebago County | 4 F.4th 487 (7th Cir. 2021) | Emergency Aid · Recent development · a | 4 F.4th at **493–94** ("The home entry…falls into the heartland of emergency-aid situations…did not violate the Fourth Amendment") | slip→reporter map confirmed by orchestrator escalation note (493-94) |
| 11 | Jimerson v. Lewis | 94 F.4th 423 (5th Cir. 2024) | §1983/QI · Key · c | slip op. at 1–2 ("this officer's efforts to identify the correct residence, though deficient, did not violate clearly established law") | slip-style (CL plain_text — A3) |
| 12 | Johnson v. Glick | 481 F.2d 1028 (2d Cir. 1973) | Use of Force · Key · c | 481 F.2d at **1033** (Friendly, J., four-factor force test: "need…relationship…extent of injury…good faith…or maliciously and sadistically") | star-verified (page-label 1033) |
| 13 | Knight v. Jacobson | 300 F.3d 1272 (11th Cir. 2002) | Arrest in the Home · Key · a | 300 F.3d at **1277** ("*Payton* keeps the officer's body outside the threshold, not his voice…") | star-verified (star-pagination 1277) |
| 14 | LaDuke v. Nelson | 762 F.2d 1318 (9th Cir. 1985) | Tents & Temporary Dwellings · Key · a | 762 F.2d at **1331–1332** ("preserving class members' reasonable expectations of privacy" / farm checks "run afoul of the Fourth Amendment") | star-verified (star-pagination 1331/1332) |
| 15 | Milam v. United States | 296 F. 629 (4th Cir. 1924) | 4A Recalibration · Key · a | 296 F. at **631** ("The constitutional expression, 'unreasonable searches,' is not fixed and absolute in meaning…") + **632** (holding) | star-verified (page-label 631/632) |
| 16 | State v. Christensen | 517 S.W.3d 60 (Tenn. 2017) | Knock and Talk · Key · a | slip op. at 18 ("'No Trespassing' signs posted near his unobstructed driveway were not sufficient to revoke the implied license referred to in *Jardines*") | slip-style (CL plain_text; no S.W.3d star pagination — A3) |
| 17 | State v. Demesme | 228 So. 3d 1206 (La. 2017) | Miranda Waiver & Invocation · Key · a | 228 So. 3d at 1206 (Crichton, J., concurring) ("the defendant's ambiguous and equivocal reference to a 'lawyer dog' does not constitute an invocation of counsel") | writ denial + solo concurrence — **posture caveat authored in-page** |

Identity re-verified against the CL opinion text for every row before authoring (Egbert/W2 discipline). Notable confirmations: the re-keyed history clusters resolve to the correct opinions with the correct decision dates (Frank projected **1959-05-04**, Robbins **1981-07-01** — both correct despite the CL cluster `date_filed` carrying a later reporter date). Milam confirmed as the Prohibition-era 4th Cir. automobile-search case (fits the Recalibration home; its "'unreasonable' is not fixed" passage is the anchor). Every Rule quote string-matched **verbatim** to CL text 2026-07-07.

### Skipped (2) — journaled `data-escalation`, no mint attempted

| record_id | reason | why |
|---|---|---|
| people-v-frederick--10579458 | data-escalation | Known-ahead skip (work order): cluster 10579458 is a New York same-caption namesake; corpus intends the Michigan knock-and-talk *People v. Frederick*. Wrong-case re-key queued in the parallel repair queue. |
| robinson-v-commonwealth--10793178 | data-escalation | **WRONG-CASE CLUSTER discovered on read.** Cluster 10793178 → opinion 11259820 is **Commonwealth v. Daryen T. Robinson, SJC-13756** (Mass. SJC, argued 2025-10-08, decided 2026-02-13) — a traffic-stop exit-order/consent case — **not** the intended Virginia Court of Appeals **Flock-ALPR** case (Robinson v. Commonwealth, Record No. 1912-24-1, the digital-surveillance home). The lake identity metadata (Va. Ct. App. / docket 1912-24-1 / "Eddie Eugene Robinson") mismatches the actual cluster contents (Egbert/frederick precedent — will not author a digital-surveillance page from a Massachusetts consent opinion). The lake record's own `alternates[]` names cluster **10838748** ("Eddie Eugene Robinson v. Commonwealth of Virginia") — the likely-correct case for the repair lane. |

### Escalation — disclosed, page KEPT (writer≠checker; orchestrator adjudicates)

**carter-v-united-states — LINT-12 (S2 managed-frontmatter drift on `citation`).** `derive_slip_cite` writes `No. 23-CF-0388, slip op. (dc 2025)` into the PAGE frontmatter, but the promoted lake record's `citations.display` stays `null` (only `slip_only: true` + provenance were stamped), so `project_record()` returns `citation: ''` and LINT-12 reports drift. This is the sole new-signature HIGH in the batch. It is **R7/tooling, not body-fixable** — I did not hand-edit the frontmatter or lake record. Suggested fix (orchestrator's call): populate the lake record's `citations` at mint (cf. `scripts/s6/stamp_slip_only.py`) OR make LINT-12 slip-aware; then re-project. Robinson (the other slip-only W3 row) did not surface this because it was skipped for the wrong-cluster reason above. Carter's page is substantively CL-verified.

## History-render honesty (PRACTICES §7 under a ⚪ born-status)
The 5 history rows are born `under_review` because their lake stubs carry Field-I `unverified` (frontier stubs; treatment not derived). The CLI history-class gate allows this (`unverified` ≠ `good_law`). The existing corpus history pages (Olmstead/Wolf/Aguilar) carry Field-I `superseded` and render the header weight as **Historical** with `Treatment: overruled/abrogated`. I mirrored the §7 form (demoted **Historical** weight, precise verb, wikilinked successor, prominent demotion) but qualified every treatment note as "⚪ unverified, pending S9" so the well-settled overruled status is shown (never disguised as live law) **without** overclaiming a machine-certified treatment edge. **Observation for the machine:** if the orchestrator wants these to render 🔴 `superseded` like the existing history pages, the lake stubs' Field-I must be promoted from `unverified` → a history class (S2/S9 treatment-derivation step; outside this authoring lane's R7 boundary).

## Quote-fidelity self-check (G-protocol, writer-side; S9 certifies)
Every minted page carries exactly one pinned Rule quote (`^pin-N`, end-of-line), string-matched verbatim to CL text. Reporter-star pincites used where the CL `html_with_citations` carries page-labels/star-pagination (Alvarez 389, Johnson 1033, Knight 1277, LaDuke 1331–32, Milam 631/632; Carroll via the S. Ct. parallel 352). Slip-style pins (S2 A3) used where CL text carries only slip-opinion pagination (Alasaad 16, Jimerson 1–2, Christensen 18) or a slip-only record (Carter 30). **Demesme is rendered honestly as a writ denial + single-justice concurrence** (not a merits holding) — the posture caveat is authored in-page in the Rule and Treatment sections, and the citable proposition is attributed to Justice Crichton's concurrence.

## Lint delta (baseline = pre-mint corpus at HEAD 5a05f8b)
- **Mint gate (LINT-14/15/16): all 17 pages 0/0/0** at dry-run and post-mint. Case Index regenerated → **512 rows (+17, exactly the W3 pages)**, 0 blank Good-law cells. `npx quartz build` → **success**, 614 files parsed (+17), 2192 emitted (only benign git-untracked-date warnings).
- **Corpus HIGH 4731 → 4789 (+58):** LINT-10 em-dash **+53** (S8 style class — the signed specimen register uses em-dashes) · LINT-7 "Knock and Talk" **+4** (pre-existing **term-register-vs-page-name** class: 28 non-W3 findings already exist on `[[Knock and Talk]]` links incl. the Case Index, Florida v. Jardines, Kentucky v. King — my 2 case pages + 2 new Case-Index rows join it) · LINT-12 **+1** (the escalated carter slip-cite gap).
- **Corpus MED 2675 → 2737 (+62):** LINT-5 bare-case-name-not-wikilink **+62** (S8 D13 materialization class — same accepted profile as W1/W2 pages, incl. self-name references).
- **Mint↔lint gap found + remediated (disclosed for ratification — writer≠checker; W2 body-only precedent):** the mint gate covers only LINT-14/15/16, so **LINT-9 (×1: Trupiano visible mid-line `^pin-705`)** and **LINT-2 (×5: Johnson, Trupiano, Demesme×3 inline quotes without a nearby pincite)** slipped through on first write. Fixed by **body-only prose finalization** (frontmatter / lake / manifest / ledger / page↔record binding UNTOUCHED — LINT-14/15/16 re-checked 0 on the edited pages): paragraph break so `^pin-705` ends its line; the five secondary quotes de-quoted to paraphrase or (Demesme) restructured so the one retained verbatim quote sits immediately before its `228 So. 3d at 1206` pincite. Net: LINT-9 and LINT-2 back to baseline; my pages now match the W1/W2 conformance profile (LINT-10 + LINT-5 accepted classes) plus the one escalated LINT-12.

## For the orchestrator
- **Adjudicate the carter LINT-12 slip-cite gap** (fix the amendment to populate lake `citations` at mint, or make LINT-12 slip-aware; or revert carter to a skip). It is the only new-signature HIGH.
- **Ratify (or revert) the body-only prose finalization** on Trupiano / Johnson / Demesme.
- **Two wrong-case re-keys for the repair queue:** people-v-frederick--10579458 (→ Michigan case) and robinson-v-commonwealth--10793178 (cluster is Mass. SJC-13756; correct Va. Flock-ALPR case likely = alternate cluster **10838748**).
- **History Field-I:** decide whether the 5 history stubs should be promoted `unverified` → `superseded` so they render 🔴 like the existing history pages (S2/S9 treatment step; not this lane's R7 boundary).
- S7 owes the homes-page Key/Related materialization + the Gaetjens "Three Golden Rules" mention→page-link conversion, from `s6-authored-ledger.jsonl`.
