# P2 ESCALATE PACKET 01/12

_findings: 25 | classes: alt-cluster-link=2, cite-selector=17, date-drift=1, holding-substance=5_

### F-S9-PR-41b1d36dde · alt-cluster-link · sev=low · needs_cl=false · quorum=3/3
- **object:** content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md
- **problem:** The case name, citation, court, year, and statutory holding stand, but the table's CourtListener opinion link does not match the lake authority record URL.
- **verbatim:** /opinion/118306/nasa-v-flra/
- **tally:** codex-A=stands-modified: Lake record identifies NASA v. FLRA as a U.S. Supreme Court case decided in 1999 with official citation 527 U.S. 229.  |  codex-B=refuted: Lake identity verifies NASA v. FLRA as a U.S. Supreme Court case, 527 U.S. 229, decided 1999-06-17, status verified.  |  opus=stands-modified: Case existence and citation fully verified: NASA lake record confirms cluster 118306, cite 527 U.S. 229, year 1999, scotus; holding (NASA-OIG investigator is a 'representative of the agency' under FS…
- **proposed_fix:** Change the table opinion link to https://www.courtlistener.com/opinion/118306/nasa-v-flra/.

### F-S9-PR-d95d1daec7 · alt-cluster-link · sev=low · needs_cl=false · quorum=3/3
- **object:** content/standards-of-proof/Reasonable Suspicion.md
- **problem:** The case and citation stand, but the table's opinion link does not match the disclosed lake record URL.
- **verbatim:** /opinion/9189388/florida-v-j-l/
- **tally:** codex-A=stands-modified: Lake verifies Florida v. J. L., U.S. Supreme Court, 2000, official citation 529 U.S. 266.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands: Case existence and reporter cite are sound: lake status=verified, display '529 U.S. 266' matches cell cite, year 2000 matches
- **proposed_fix:** Change the opinion link to the lake record URL /opinion/9189388/florida-v-j-l/.

### F-S9-PR-c48f05e89e · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/State v. Weaver.json
- **problem:** The authority exists, but the existence payload packages 2011 Tex. Crim. App. LEXIS 1320 as the selected official/display citation even though the built page flags that selection for correction to the S.W.3d reporter.
- **verbatim:** lake selected the neutral cite 2011 Tex. Crim. App. LEXIS 1320 as official — flagged for S2 re-selection (S.W.3d reporter is the correct primary).
- **tally:** codex-A=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  codex-B=stands-modified: Lake identity verifies the case exists as State v. Weaver, Tex. Crim. App., decided 2011-09-28, docket PD-1635-10, cluster_id 2546485.  |  opus=stands-modified: Cached opinion confirms the case is real: 'COCHRAN, J., delivered the opinion of the Court in which MEYERS, PRICE, WOMACK, JOHNSON and ALCALA, JJ., joined,' Court of Criminal Appeals of Texas; the ^p…
- **proposed_fix:** Keep State v. Weaver as an existing 2011 Tex. Crim. App. authority, but use 349 S.W.3d 521 as the primary/official display citation and treat 2011 Tex. Crim. App. LEXIS 1320 as a parallel vendor cita…

### F-S9-PR-6d1aaf0e17 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Castillo.json
- **problem:** The cited case exists and the reporter/court/year citation matches the lake record, but the rendered page's citation line appends a docket number that conflicts with the lake identity record.
- **verbatim:** *70 F.4th 894 (5th Cir. 2023)* (No. 21-50406); "docket": "22-50060"
- **tally:** codex-A=stands-modified: Lake identity verifies record_id/case_name as United States v. Castillo, court as 5th Cir., year as 2023, and date_decided as 2023-06-19.  |  codex-B=stands: Lake citations confirm the case citation: 70 F.4th 894.  |  opus=stands-modified: '70 F.4th 894' is well-formed for a 2023 5th Cir. decision; cached opinion confirms the case is the border-search Castillo (Ho, J., June 19 2023, manual cell-phone border search) — the citation attac…
- **proposed_fix:** Change the rendered header docket number to No. 22-50060, or omit the docket number from the citation line.

### F-S9-PR-8b77329ed2 · cite-selector · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/California v. Prysock.md
- **problem:** The authority exists and the structured official citation is verified as 453 U.S. 355, but the built page also displays the inconsistent citation 451 U.S. 355 in the body header and Sources section.
- **verbatim:** *451 U.S. 355 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
- **tally:** codex-A=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  codex-B=stands-modified: lake.citations.official.cite verifies 453 U.S. 355 as the selected official citation.  |  opus=stands-modified: Lake official citation is '453 U.S. 355' (vol 453) and parallel '101 S. Ct. 2806; 69 L. Ed. 2d 696; 49 U.S.L.W. 3964' + vendor-neutral '1981 U.S. LEXIS 131' match the asserted payload - so the review…
- **proposed_fix:** Correct the visible body/header and Sources citation to 453 U.S. 355 (1981).

### F-S9-PR-a596cf2c08 · cite-selector · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Carter v. United States.md
- **problem:** The authority identity exists in the disclosed lake record, but the assertion says an official citation is present even though the lake record classifies the case as slip-only with no official/display citation.
- **verbatim:** "official": null
- **tally:** codex-A=stands: Lake identity matches title Carter v. United States, docket 23-CF-0388, court D.C. 2025, and year 2025.  |  codex-B=stands-modified: The lake identity fields verify Carter v. United States, docket 23-CF-0388, D.C. 2025, decided 2025-08-28.  |  opus=refuted: Cached opinion caption confirms 'DISTRICT OF COLUMBIA COURT OF APPEALS, No. 23-CF-0388, DONTE J. CARTER, APPELLANT, v. UNITED STATES, APPELLEE', decided 2025-08-28 — the case exists at the cited slip…
- **proposed_fix:** Keep the slip citation and identity, but set official_citation_present to false and treat the case as slip-only unless an official reporter citation is later verified.

### F-S9-PR-a6ee1850ad · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/District of Columbia v. R.W..md
- **problem:** The authority exists as a SCOTUS slip-only record, but the assertion's official_citation_present=true overstates the disclosed citation record. The lake record has no selected official citation and marks the case slip-only.
- **verbatim:** "official": null, "parallel": [], "vendor_neutral": [], "all": [], "display": null, "official_selection": { "court_class": "scotus", "selected": null, "reason": "no_official_class_citation" }, "slip_…
- **tally:** codex-A=stands-modified: Lake identity lists case_name District of Columbia v. R.W., court scotus, year 2026, and docket 25-248.  |  codex-B=stands-modified: Lake identity confirms District of Columbia v. R.W., SCOTUS, docket 25-248, year 2026, with canonical_name_match=true.  |  opus=refuted: Cached slip op.: 'SUPREME COURT OF THE UNITED STATES / DISTRICT OF COLUMBIA v. R.W.', 'No. 25-248. Decided April 20, 2026', 'Cite as: 608 U. S. ____ (2026)' -- matches docket 25-248, court scotus, ye…
- **proposed_fix:** Set official_citation_present=false and describe the citation as slip-only or placeholder until an official reporter citation is selected.

### F-S9-PR-3cdccf1a78 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Landor v. Louisiana Dept. of Corrections.md
- **problem:** The authority exists as a SCOTUS slip opinion, but the assertion's official_citation_present flag is wrong. The lake record says there is no official citation and the case is slip-only.
- **verbatim:** "official": null,
- **tally:** codex-A=stands-modified: Lake identity gives docket 23-1197, court scotus, and year 2026; the opinion text shows No. 23-1197 and Decided June 23, 2026.  |  codex-B=stands-modified: Lake identity confirms SCOTUS, docket 23-1197, year 2026, cluster_id 10878535, and lead_opinion_id 11346052.  |  opus=refuted: Cached slip opinion confirms Landor v. Louisiana Dept. of Corrections and Public Safety, No. 23-1197, argued Nov. 10, 2025, decided June 23, 2026, Gorsuch, J. (6-3); 'Cite as: 609 U. S. ___ (2026)'.
- **proposed_fix:** Set official_citation_present to false and treat the citation as slip-only/current-term rather than an official reporter citation.

### F-S9-PR-a161ba0f1f · cite-selector · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Olivier v. City of Brandon.md
- **problem:** The case identity, court, year, and docket are supported, but the assertion marks an official citation as present even though the lake record has no official/display citation and treats the case as slip-only.
- **verbatim:** no_official_class_citation
- **tally:** codex-A=stands-modified: Lake identity confirms case_name 'Olivier v. City of Brandon', court 'scotus', year 2026, and docket '24-993'.  |  codex-B=stands-modified: Lake identity confirms the case name, SCOTUS court, docket 24-993, cluster 10811625, and year 2026.  |  opus=refuted: Inlined slip opinion confirms the case: 'OLIVIER v. CITY OF BRANDON, MISSISSIPPI', No. 24–993, Decided March 20, 2026, Kagan, J. for a unanimous Court.
- **proposed_fix:** Keep the SCOTUS 2026 slip-only docket citation, but set official_citation_present to false and do not imply an official reporter citation unless lake.citations.official or lake.citations.display is p…

### F-S9-PR-e5075554d8 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Postal Service v. Konan.md
- **problem:** The case exists as a SCOTUS slip-only authority, but the payload says official_citation_present=true even though the lake record has no official citation selected and marks the record slip-only.
- **verbatim:** "official": null
- **tally:** codex-A=stands-modified: Lake identity lists case_name Postal Service v. Konan, court scotus, year 2026, docket 24-351.  |  codex-B=stands-modified: Lake identity matches Postal Service v. Konan, court scotus, docket 24-351, year 2026, cluster_id 10799651, lead_opinion_id 11266325.  |  opus=refuted: Cached slip opinion confirms the case: 'SUPREME COURT OF THE UNITED STATES ... No. 24-351. Argued October 8, 2025—Decided February 24, 2026' and 'Cite as: 607 U. S. ___ (2026)'.
- **proposed_fix:** Change official_citation_present to false and keep the citation framed as a slip-only/no-reporter citation.

### F-S9-PR-e8068468d5 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Robinson v. Commonwealth.md
- **problem:** The authority exists as a published slip opinion, but the payload's official_citation_present=true is not supported by the lake record, which shows no official/display citation and flags the case as slip-only.
- **verbatim:** "official": null, "display": null, "slip_only": true
- **tally:** codex-A=stands-modified: Lake identity gives court as "Va. Ct. App.", docket "1912-24-1", year 2026, and date_decided "2026-04-07".  |  codex-B=stands-modified: Lake identity matches Robinson, Va. Ct. App., docket 1912-24-1, decided 2026-04-07.  |  opus=refuted: Opinion confirms 'COURT OF APPEALS OF VIRGINIA, Record No. 1912-24-1, EDDIE EUGENE ROBINSON v. COMMONWEALTH OF VIRGINIA, Opinion Issued April 7, 2026, PUBLISHED OPINION BY JUDGE RANDOLPH A. BEALES.'
- **proposed_fix:** Keep the slip citation, but set official_citation_present=false or model this as slip_only=true until an official reporter citation appears.

### F-S9-PR-4e77f991c3 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/The GEO Group, Inc. v. Menocal.md
- **problem:** The authority exists as a SCOTUS slip-only decision, but the payload's official_citation_present=true is inconsistent with the lake record, which has no selected official citation and marks the case slip_only.
- **verbatim:** "official": null, "parallel": [], "vendor_neutral": [], "all": [], "display": null
- **tally:** codex-A=stands-modified: Lake identity confirms record_id The GEO Group, Inc. v. Menocal, court scotus, docket 24-758, and year 2026.  |  codex-B=stands-modified: Lake identity lists court=scotus, docket=24-758, year=2026, cluster_id=10800194, and lead_opinion_id=11266870.  |  opus=refuted: Opinion is GEO Group, Inc. v. Menocal et al., No. 24-758, argued Nov 10 2025, decided Feb 25 2026, slip 'Cite as: 607 U. S. ___ (2026)'.
- **proposed_fix:** Set official_citation_present to false and preserve the citation as slip-only unless a later official reporter citation is added to the disclosed record.

### F-S9-PR-3d0d17e0c0 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Mendoza.md
- **problem:** The authority exists as a precedential Third Circuit slip opinion, but the inventory assertion marks official_citation_present=true even though the lake record says no official citation has been assigned and the case is slip-only.
- **verbatim:** "official": null
- **tally:** codex-A=stands-modified: Lake identity shows United States v. Ryan Mendoza, docket 25-1154, 3d Cir., decided 2026-01-08.  |  codex-B=stands-modified: The lake identity record matches United States v. Ryan Mendoza, No. 25-1154, Third Circuit, decided 2026-01-08.  |  opus=refuted: Opinion caption confirms 'UNITED STATES v. RYAN MENDOZA,' No. 25-1154, Third Circuit, 'PRECEDENTIAL,' 'Opinion filed: January 8, 2026' — matches court/year/docket.
- **proposed_fix:** Retain the slip citation but set official_citation_present=false, or otherwise distinguish docket/slip citation from an official reporter citation.

### F-S9-PR-ab2d347d66 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Porter.md
- **problem:** The case exists and the slip-style citation is supported, but the payload marks official_citation_present=true even though the lake record reports no official citation and treats the case as slip-only.
- **verbatim:** no_official_class_citation
- **tally:** codex-A=stands-modified: Lake identity gives case_name United States v. Porter, court 5th Cir., docket 25-60163, date_decided 2026-03-17, year 2026.  |  codex-B=stands-modified: Lake identity confirms United States v. Porter, No. 25-60163, Fifth Circuit, decided 2026-03-17.  |  opus=stands-modified: Case existence is verified: CL cluster 10810059, published 5th Cir. slip No. 25-60163, decided 2026-03-17; opinion header confirms No. 25-60163, Fifth Circuit, filed March 17, 2026.
- **proposed_fix:** Keep the displayed citation as a slip citation, but set official_citation_present=false or otherwise mark it as slip-only rather than official-reporter citation.

### F-S9-PR-b881e64bdc · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Trent.md
- **problem:** The case identity, docket, court, and year are supported, but the payload's official_citation_present=true is not supported by the lake record, which says there is no official citation and the case is slip-only.
- **verbatim:** "official": null
- **tally:** codex-A=stands-modified: The opinion text shows No. 25-5770, Sixth Circuit, filed May 07, 2026.  |  codex-B=stands-modified: Lake identity confirms United States v. Mark Anthony Trent, 6th Cir., docket 25-5770, decided 2026-05-07.  |  opus=refuted: Inlined opinion header confirms 'No. 25-5770', 'UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT', 'FILED May 07, 2026', 'UNITED STATES OF AMERICA v. MARK ANTHONY TRENT' — docket/court/year all m…
- **proposed_fix:** Keep the slip citation, but set official_citation_present to false or label the citation explicitly as slip-only/no reporter citation.

### F-S9-PR-bafce48906 · cite-selector · sev=low · needs_cl=false · quorum=2/3
- **object:** content/searches/two-definitions-of-search/Reasonable Expectation of Privacy.md
- **problem:** The live-law/treatment call is supported, but the displayed official reporter citation '609 U.S. ___' is not verified by the lake citation fields.
- **verbatim:** recent_or_no_official_cite
- **tally:** codex-A=MISSING  |  codex-B=stands-modified: Lake treatment marks Chatrie as good_law as of 2026-06-30 and describes it as a new binding SCOTUS anchor.  |  opus=refuted: Lake record Chatrie v. United States confirms existence: SCOTUS, docket '25-112', date_decided 2026-06-29, year 2026 — matches asserted '609 U.S. ___ (2026)' slip-op and supremecourt.gov 25-112 URL;…
- **proposed_fix:** Use a slip-opinion/docket form until the lake record contains an official citation, e.g. Chatrie v. United States, No. 25-112, slip op. (U.S. June 29, 2026).

### F-S9-PR-daa75a676f · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/seizures/Collective Knowledge and the Fellow-Officer Rule.md
- **problem:** The case exists in the lake as a frontier SCOTUS slip-only record, but the page's citation form is not exact against the lake citation fields, which have no official/display citation and instead give slip-only provenance.
- **verbatim:** No. 25-248, per curiam 2026-04-20
- **tally:** codex-A=stands-modified: Lake identity gives case_name District of Columbia v. R.W., court_level scotus, docket 25-248, and year 2026.  |  codex-B=stands: lake status is under_review, not verified.  |  opus=refuted: Lake record 'District of Columbia v. R.W.' identity: docket '25-248' matches cell 'No. 25-248'; cluster_id 10845431 matches opinion link; year 2026 matches; canonical_name_match=true.
- **proposed_fix:** Use the lake-supported slip form, e.g. District of Columbia v. R.W., No. 25-248, per curiam (U.S. Apr. 20, 2026), or include the lake's 608 U.S. ___ placeholder if that is the corpus convention.

### F-S9-PR-a914e60561 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/seizures/arrests/Arrest in the Home.md
- **problem:** The authority exists and is good law in the lake record, but the page's official-style citation '607 U.S. ___' is not verifiable from the disclosed citation fields.
- **verbatim:** final U.S. Reports pagination pending
- **tally:** codex-A=stands: Lake identity confirms Case v. Montana, U.S. Supreme Court, decided 2026-01-14, docket 24-624.  |  codex-B=stands-modified: Lake identifies Case v. Montana, docket 24-624, decided 2026-01-14, with treatment.field_i_validity=good_law as of 2026-06-30.  |  opus=refuted: Lake record 'Case v. Montana' confirms the case exists: cluster 10774335, docket 24-624, decided 2026-01-14, year 2026, URL /opinion/10774335/case-v-montana/ matching the table cell; treatment good_l…
- **proposed_fix:** Use a slip/no-official-cite form such as Case v. Montana, No. 24-624 (U.S. Jan. 14, 2026), until the lake record contains an official U.S. Reports citation.

### F-S9-PR-3689ba2d59 · cite-selector · sev=low · needs_cl=false · quorum=3/3
- **object:** content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md
- **problem:** The case and citation are correct, but the Opinion cell URL does not match the lake record's absolute_url for Groh.
- **verbatim:** /opinion/131161/groh-v-ramirez/
- **tally:** codex-A=stands-modified: Lake record for Groh v. Ramirez is verified, U.S. Supreme Court, year 2004, official citation 540 U.S. 551.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands: Case identity, reporter cite (540 U.S. 551 (2004)), and framed Floor-4 holding all match the lake record and its brief ('a warrant that omits the things to be seized is facially invalid').
- **proposed_fix:** Keep 540 U.S. 551 (2004), but change the opinion link to https://www.courtlistener.com/opinion/131161/groh-v-ramirez/.

### F-S9-PR-17e642ea89 · date-drift · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Maryland v. Buie.md
- **problem:** The good_law treatment call survives the disclosed treatment fields, but the treatment payload's as_of_content date uses 1990-03-05 while the cached opinion text states a different decision date.
- **verbatim:** Decided February 28, 1990
- **tally:** codex-A=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  codex-B=stands-modified: Lake treatment field_i_validity is good_law as of 2026-06-30 and point_overrides is empty.  |  opus=stands-modified: Core treatment substance is correct and mirrors the lake: field_i_validity 'good_law', as_of_treatment 2026-06-30, composite_basis 'migration-seed', varies_by_point false; Buie remains good law and t…
- **proposed_fix:** Keep field_i_validity as good_law as of 2026-06-30, but correct as_of_content/date_decided to 1990-02-28 if that field is intended to track the decision date, or clarify that 1990-03-05 is a corpus s…

### F-S9-PR-9031a73c49 · holding-substance · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Arkansas v. Sanders.md
- **problem:** The main holding is supported, but 'absent exigency' is slightly too narrow because the Court said a warrantless search would need some warrant exception other than the automobile exception, not only exigency.
- **verbatim:** Thus, insofar as the police are entitled to search such luggage without a warrant, their actions must be justified under some exception to the warrant requirement other than that applicable to automo…
- **tally:** codex-A=stands-modified: The p. 766 holding supports that the Fourth Amendment warrant requirement applies to personal luggage taken from an automobile to the same degree as luggage elsewhere.  |  codex-B=stands: Lens B makes no quote-fidelity or holding-support finding about the original Sanders rule.  |  opus=refuted: Core holding is verbatim in the cached opinion at *766: 'we hold that the warrant requirement of the Fourth Amendment applies to personal luggage taken from an automobile to the same degree it applie…
- **proposed_fix:** Replace 'absent exigency' with 'unless another warrant exception, independent of the automobile exception, applies.'

### F-S9-PR-b53069e9ca · holding-substance · sev=high · needs_cl=true · quorum=3/3
- **object:** content/cases/Board of County Commissioners of Bryan County v. Brown.md
- **problem:** The asserted holding cannot be verified from the disclosed evidence because there is no cached opinion text and the lake record contains no holding field or pinpoint quotes supporting the proposition.
- **verbatim:** "pinpoints": []
- **tally:** codex-A=stands: The page's own holding is the assertion under review and cannot verify itself.  |  codex-B=stands-modified: Support fidelity is outside this lens.  |  opus=refuted: Cached opinion text (at reporter star *411): 'reflects deliberate indifference to the risk that a violation of a particular constitutional or statutory right will follow the decision' and 'deliberate…
- **proposed_fix:** Add the cached opinion text or populate lake pinpoints/holding fields that support the deliberate-indifference, plainly-obvious-consequence, and specific-injury components of the holding.

### F-S9-PR-9fe4c2a29b · holding-substance · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Brown v. Mississippi.md
- **problem:** The holding is directionally supported but slightly overbroad because it omits Brown's limiting facts: state-officer/state-authority coercion and a conviction resting solely on, or using as its basis, the coerced confessions.
- **verbatim:** conviction resting solely upon confessions obtained by violence; basis for conviction and sentence
- **tally:** codex-A=stands-modified: The opinion frames the case around convictions resting solely on confessions extorted by officers of the State through brutality and violence.  |  codex-B=stands-modified: Lake treatment still marks Brown good_law with no point_overrides.  |  opus=refuted: Cached opinion: 'whether convictions, which rest solely upon confessions shown to have been extorted by officers of the State by brutality and violence, are consistent with the due process of law req…
- **proposed_fix:** Revise to: A state conviction resting solely on confessions extorted by state officers through physical torture, and using those confessions as the basis for conviction and sentence, violates Fourtee…

### F-S9-PR-df4c4fd2d5 · holding-substance · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/City of Los Angeles v. Patel.md
- **problem:** The holding is supported in substance, but framed too generically as 'A hotel guest-registry inspection ordinance' and omits the key limiting facts: the Los Angeles on-demand inspection provision and penalties for refusal before review.
- **verbatim:** Section 41.49(3)(a) is facially unconstitutional because it fails to provide hotel operators with an opportunity for precompliance re- view.
- **tally:** codex-A=stands-modified: The opinion supports facial invalidity of LAMC Section 41.49(3)(a), not a freestanding rule about all hotel guest-registry inspection ordinances.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Substance is supported: the syllabus holds §41.49(3)(a) 'is facially unconstitutional because it fails to provide hotel operators with an opportunity for precompliance review' (slip op. 9-17).
- **proposed_fix:** The Los Angeles on-demand hotel-registry inspection provision is facially unconstitutional because it penalizes refusal without affording hotel operators an opportunity for precompliance review.

### F-S9-PR-3a3d461e12 · holding-substance · sev=high · needs_cl=false · quorum=3/3
- **object:** content/cases/Coolidge v. New Hampshire.md
- **problem:** The holding as framed is incomplete and overclaims an 'ORIGIN of the modern plain-view doctrine' that is not verifiable from the disclosed lake record or opinion text. The opinion itself describes warrantless plain-view seizure as already 'well established' and discusses earlier plain-view applicat…
- **verbatim:** It is well established that under certain circumstances the police may seize evidence in plain view without a warrant.
- **tally:** codex-A=stands: The disclosed lake record has no holdings field confirming the 'origin' characterization.  |  codex-B=stands-modified[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=refuted: Text lays out the plain-view requirements: prior justification, inadvertent discovery, and 'immediately apparent to the police that they have evidence before them' — matches the holding note's framew…
- **proposed_fix:** Replace with a complete, text-grounded holding: Stewart plurality formulated limits on plain-view seizures: plain view supplements a prior lawful intrusion, requires inadvertent discovery under Cooli…

