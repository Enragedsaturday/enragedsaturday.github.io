# P2 ESCALATE PACKET 11/12

_findings: 25 | classes: quote-fidelity=2, treatment-noise=18, truncated-holding=5_

### F-S9-PR-084b660f04 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Wright v. City of Euclid.json
- **problem:** The pin-op17 stored/payload quote is not the cited opinion quotation; it is harvested page boilerplate ending before the actual excessive-force sentence.
- **verbatim:** --- # Wright v. City of Euclid
- **tally:** codex-A=stands: The payload quote begins with the content page header, not the Sixth Circuit opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B.  |  opus=stands-modified: Payload quote is a harvest artifact (front-matter), not an opinion quotation.
- **proposed_fix:** Replace pin-op17 with the actual opinion sentence beginning at slip page 17, or re-extract the quote from the cached opinion text.

### F-S9-PR-8123d93e82 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Wright v. City of Euclid.json
- **problem:** The pin-op23 stored/payload quote is truncated and not character-faithful to the opinion passage; the opinion continues through the clearly-established-right language and uses different quotation marks.
- **verbatim:** probable cause is a “quintessential example[] of [a] ‘clearly established’ constitutional right.”
- **tally:** codex-A=stands: The lake/payload quote stops at "[a]" and omits the rest of the quoted phrase.  |  codex-B=refuted: Quote fidelity is outside Lens B.  |  opus=stands-modified: Payload quote is truncated (harvest artifact), not the full attributed quotation.
- **proposed_fix:** Replace the pin-op23 quote with the exact sentence from slip page 23, preserving the opinion's quotation marks, or paraphrase without quotation marks.

### F-S9-PR-5a79835d2c · treatment-noise · sev=medium · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/Arizona v. Roberson.json
- **problem:** The good_law status itself matches the lake judgment field, but the content page's categorical 'No negative treatment' language is too strong because the disclosed lake treatment record contains proposed negative/critical treatment edges and audit_needed markers.
- **verbatim:** "audit_marker": "R15 treatment audit required"
- **tally:** codex-A=refuted: Lens A does not evaluate treatment or currency merits.  |  codex-B=stands-modified: Lake treatment.field_i_validity is good_law as of 2026-06-30, so the basic status survives.  |  opus=stands-modified: The validity call (good_law) survives: composite_basis migration-seed, all 33 negative edges proposed:true (un-adopted), and Shatzer refines rather than overrules Roberson per the rendered subsequent…
- **proposed_fix:** Keep good_law as the headline status, but replace 'No negative treatment' with a qualified statement such as: 'No confirmed downgrade in the current lake treatment field; treatment derivation contain…

### F-S9-PR-bef1d30412 · treatment-noise · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brendlin v. California.json
- **problem:** The good_law treatment call itself matches the lake judgment, but the content page's categorical 'No negative treatment' wording is too strong because the disclosed lake contains proposed negative-treatment edges and audit-needed derivation signals.
- **verbatim:** "audit_needed": true, "proposed_negative_events": 25, "audit_marker": "R15 treatment audit required"
- **tally:** codex-A=refuted: The treatment payload matches the lake treatment fields and content page front matter.  |  codex-B=stands-modified: Lake treatment.field_i_validity is good_law, as_of_treatment is 2026-06-30, varies_by_point is false, and point_overrides is empty.  |  opus=stands-modified: field_i_validity='good_law' is correct/uncontradicted: Brendlin (2007) is a solid, oft-cited SCOTUS holding; the content page reports 'No negative treatment.'
- **proposed_fix:** Keep Status: good as of 2026-06-30, but replace 'No negative treatment' with a qualified statement such as 'No confirmed negative treatment in the lake judgment; proposed negative-treatment edges/aud…

### F-S9-PR-7ba2db4b28 · treatment-noise · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Gouled v. United States.json
- **problem:** The treatment survives in substance, but the disclosed record is point-specific while the assertion says varies_by_point=false and the built page visibly renders an unqualified Treatment: overruled label. The lake scope note says the mere-evidence rule was overruled/abandoned, while the separate st…
- **verbatim:** The mere-evidence rule was overruled/abandoned by Warden v. Hayden (1967), which held the Fourth Amendment does not bar the seizure of items of solely evidentiary value. The separate Gouled holding —…
- **tally:** codex-A=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  codex-B=stands-modified: Lake treatment gives field_i_validity as superseded as of 2026-06-30 and includes a Warden v. Hayden edge marked overruled.  |  opus=stands-modified: The scope_note itself splits treatment across two holdings (one overruled, one surviving), which contradicts varies_by_point=false.
- **proposed_fix:** Set varies_by_point=true with point treatment for the mere-evidence rule and the stealth/ruse-entry principle, or otherwise render the headline as superseded/overruled in part rather than unqualified…

### F-S9-PR-a283cf0489 · treatment-noise · sev=medium · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/Heien v. North Carolina.json
- **problem:** The good_law status matches the lake treatment field, but the page's categorical 'No negative treatment' is stronger than the disclosed treatment record permits because the treatment is migration-seeded and the derivation flags audit-needed proposed negative-event edges.
- **verbatim:** Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.
- **tally:** codex-A=refuted: The treatment payload matches lake.treatment for field_i_validity=good_law, as_of_content=2014-12-15, as_of_treatment=2026-06-30, varies_by_point=false, and the stated scope_note.  |  codex-B=stands-modified: lake.treatment.field_i_validity is good_law, as_of_treatment is 2026-06-30, varies_by_point is false, and point_overrides is empty.  |  opus=stands-modified: good_law is not refuted by disclosed evidence, but the scope_note is placeholder boilerplate and the record self-labels under_review / seed 'may downgrade'.
- **proposed_fix:** Keep the good_law label as of 2026-06-30, but qualify the body text to say there is no audited negative treatment in this record and that proposed progeny edges require treatment audit.

### F-S9-PR-1c2fc2e007 · treatment-noise · sev=high · needs_cl=true · quorum=2/3
- **object:** _overhaul2/lake/cases/Jacobson v. United States.json
- **problem:** The page's unqualified good/no-negative-treatment presentation is not verifiable from the disclosed treatment record. The lake field says good_law, but its provenance is migration-seeded and the same record contains 37 proposed negative edges plus audit-needed markers, including overruled, question…
- **verbatim:** Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.
- **tally:** codex-A=MISSING  |  codex-B=stands: The disclosed treatment provenance states treatment.field_i_validity comes from _treatment-migration.json plus page frontmatter, not a completed treatment audit.  |  opus=refuted: field_i_validity=good_law is consistent with the disclosed lake: no confirmed (proposed:false) negative edge exists; all negative edges are proposed candidates.
- **proposed_fix:** Replace the unqualified treatment statement with a qualified status such as 'good_law in current seed record; negative-treatment audit pending' and remove 'No negative treatment' unless the proposed…

### F-S9-PR-e3dbc1c7ff · treatment-noise · sev=low · needs_cl=true · quorum=2/3
- **object:** _overhaul2/lake/cases/Taylor v. Riojas.json
- **problem:** The core good_law call matches the lake record, but the page's unqualified 'No negative treatment' language is too strong because the disclosed treatment derivation flags the top-cited lane for audit with proposed negative events; the disclosed edges are proposed and field_iii only says mentioned,…
- **verbatim:** R15 treatment audit required
- **tally:** codex-A=MISSING  |  codex-B=stands-modified: Lake treatment.field_i_validity is good_law as of 2026-06-30 and the scope_note matches the payload.  |  opus=refuted: Disclosed opinion is a 2020 SCOTUS per curiam GVR defeating qualified immunity via the 'obvious case' route (Hope v. Pelzer) — consistent with good_law and the scope_note.
- **proposed_fix:** Keep field_i_validity: good_law, but tighten the prose to 'No confirmed negative treatment in the disclosed lake record; top-cited progeny lane remains audit-flagged.'

### F-S9-PR-cbd174a461 · treatment-noise · sev=medium · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Martinez-Fuerte.json
- **problem:** The top-level good_law call survives, but the page's unqualified treatment presentation, especially 'No negative subsequent treatment identified,' is too strong. The lake record contains proposed negative-treatment edges and marks treatment audit as required.
- **verbatim:** "audit_needed": true, "proposed_negative_events": 11, "audit_marker": "R15 treatment audit required"
- **tally:** codex-A=refuted: Treatment is outside Lens A's support/quote-fidelity charter, so no substantive currency finding is raised.  |  codex-B=stands-modified: Lake treatment.field_i_validity is good_law and varies_by_point is false, matching the inventory payload.  |  opus=stands-modified: No disclosed evidence contradicts good_law: cached text is the intact 1976 opinion plus Brennan dissent, and the lane2 field_ii='overruled'/'abrogated'/'superseded_by_statute' labels are attached to…
- **proposed_fix:** Keep good_law only as the current lake judgment, but replace the no-negative language with a caveat that proposed negative-treatment candidates exist and R15 treatment audit is pending, unless an aud…

### F-S9-PR-ba521c7e42 · treatment-noise · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Matlock.json
- **problem:** The top-level good_law/Binding-SCOTUS treatment survives, but the no-point-variation/no-negative-treatment framing is too categorical because the disclosed page identifies a Randolph carve-out for a physically present, expressly objecting co-occupant.
- **verbatim:** No negative subsequent treatment identified. *Matlock* is the anchor for [[Consent Searches|third-party consent]]: [[Illinois v. Rodriguez]] extends it to officers' reasonable mistakes about *apparen…
- **tally:** codex-A=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  codex-B=stands-modified: The lake treatment field records field_i_validity as good_law as of 2026-06-30, so a complete refutation of good-law status is not supported by the disclosed record.  |  opus=stands-modified: No basis to refute good_law: all 32 disclosed treatment edges classify Matlock's own treatment as field_iii 'mentioned' (neutral); edge field_ii values (overruled/questioned/abrogated/superseded/crit…
- **proposed_fix:** Keep Matlock as good law, but state that it is limited by Georgia v. Randolph for a physically present, expressly objecting co-occupant; remove the blanket 'No negative subsequent treatment identifie…

### F-S9-PR-b10ce7f97a · treatment-noise · sev=medium · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Ramsey.json
- **problem:** The good_law field is present, but the page's unqualified no-negative-treatment framing is too strong because the lake record says the treatment is migration-seeded and its progeny derivation has audit-needed proposed negative events.
- **verbatim:** Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.
- **tally:** codex-A=refuted: The treatment payload matches the disclosed lake treatment fields: field_i_validity good_law, as_of_content 1977-06-06, as_of_treatment 2026-06-30, and varies_by_point false.  |  codex-B=stands-modified: The lake treatment field itself says field_i_validity is good_law as of 2026-06-30.  |  opus=stands-modified: good_law is correct on the merits: Ramsey is the border-search anchor, and all treatment.edges are 'proposed:true' unadjudicated citator FPs (Caballero/Ezeiruaku 'overruled', Cotterman 'abrogated', I…
- **proposed_fix:** State that Ramsey is listed as good_law as of 2026-06-30, but qualify the subsequent-history note as having no confirmed negative treatment in this record while proposed negative-treatment edges rema…

### F-S9-PR-f54da161d3 · treatment-noise · sev=low · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Van Leeuwen.json
- **problem:** The good_law and Binding-SCOTUS treatment survives, but the content page's unqualified 'No negative treatment' wording is too strong because the disclosed lake derivation flags an unresolved top-cited treatment audit and proposed negative events.
- **verbatim:** "audit_marker": "R15 treatment audit required"
- **tally:** codex-A=refuted: The treatment payload matches the lake treatment fields: field_i_validity good_law, as_of_content 1970-04-27, as_of_treatment 2026-06-30, varies_by_point false.  |  codex-B=stands-modified: Lake treatment field states field_i_validity is good_law as of 2026-06-30 and varies_by_point is false.  |  opus=stands-modified: The doctrinal scope_note (brief detention of mailed packages on reasonable suspicion while a warrant is diligently sought; mere detention invades no privacy interest until opened under a warrant; pre…
- **proposed_fix:** Keep good_law/Binding-SCOTUS, but revise 'No negative treatment' to 'No confirmed negative treatment in the disclosed lake record' or complete the flagged treatment audit before using the unqualified…

### F-S9-PR-47eee5c6da · treatment-noise · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/cases/Ashcraft v. Tennessee.md
- **problem:** The good_law field matches the lake final treatment field, but the page's unqualified 'No negative treatment' overstates the disclosed record. The lake record contains proposed negative-treatment edges and two derivation lanes marked audit_needed, so the defensible statement is 'no confirmed negati…
- **verbatim:** Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.
- **tally:** codex-A=refuted: Treatment/currency is outside Lens A; no treatment merits finding is made.  |  codex-B=stands-modified: Lake treatment.field_i_validity is good_law as of 2026-06-30, with varies_by_point false and no point_overrides.  |  opus=stands-modified: field_i_validity good_law is correct: this 1944 SCOTUS due-process landmark has never been overruled; all negative edges are proposed:true triage candidates (state courts overruling their own precede…
- **proposed_fix:** Keep field_i_validity as good_law, but revise the treatment prose to: 'No confirmed negative treatment in the final lake treatment field; automated derivation lists proposed negative events and an R1…

### F-S9-PR-53b8aa949c · treatment-noise · sev=medium · needs_cl=true · quorum=2/3
- **object:** content/cases/Jacobson v. United States.md
- **problem:** The good_law status matches the lake judgment fields, but the page's unqualified 'No negative treatment' treatment text is too strong because the lake records proposed negative treatment edges and audit-needed derivation lanes.
- **verbatim:** "audit_needed": true, "proposed_negative_events": 15, "audit_marker": "R15 treatment audit required"
- **tally:** codex-A=MISSING  |  codex-B=stands-modified: Lake treatment fields match the asserted good_law, as_of_content, as_of_treatment, composite_basis, varies_by_point, scope_note, and empty point_overrides.  |  opus=refuted: field_i_validity 'good_law', composite_basis 'migration-seed', as_of_content 1992-04-06 (= date_decided) match the lake treatment block.
- **proposed_fix:** Keep good_law as of 2026-06-30, but change the narrative to say no validated negative treatment is recorded in the lake and that proposed negative/audit-needed edges remain unresolved.

### F-S9-PR-ffc452cd3f · treatment-noise · sev=medium · needs_cl=true · quorum=2/3
- **object:** content/cases/Kuhlmann v. Wilson.md
- **problem:** The page presents an uncaveated current good-law treatment as of 2026-06-30, but the disclosed treatment record is migration-seeded and expressly unresolved: derivation lanes require R15 treatment audit and contain proposed negative events. From the disclosed evidence alone, the current blanket goo…
- **verbatim:** Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.
- **tally:** codex-A=MISSING  |  codex-B=stands: The lake treatment field says good_law, but its composite_basis is migration-seed and its scope_note says the derivation may downgrade.  |  opus=stands-modified: field_i_validity good_law itself is uncontradicted: all 37 disclosed negative edges are 'proposed': true / field_iii 'mentioned' lane artifacts; 0 confirmed negatives.
- **proposed_fix:** Downgrade the displayed treatment to provisional/under_review or complete the R15 treatment audit and add point-specific treatment if the Sixth Amendment point remains good while other Kuhlmann point…

### F-S9-PR-0335e1b187 · treatment-noise · sev=low · needs_cl=true · quorum=3/3
- **object:** content/cases/Pennsylvania v. Muniz.md
- **problem:** The good-law call itself matches the lake judgment fields, but the page's categorical 'No negative treatment' phrasing is too strong because the disclosed treatment derivation contains proposed negative-treatment edges and audit_needed flags.
- **verbatim:** "audit_needed": true
- **tally:** codex-A=stands-modified: The lake treatment fields match the content treatment fields, and lens A does not assess good-law currency.  |  codex-B=stands-modified: Lake treatment.field_i_validity, as_of_treatment, varies_by_point, and scope_note match the page treatment payload.  |  opus=refuted: field_i_validity good_law matches lake; scope_note (fractured opinion; slurring non-testimonial, sixth-birthday testimonial/suppressed, booking-question exception) matches lake and is supported by th…
- **proposed_fix:** Keep the status as good_law, but replace the absolute 'No negative treatment' sentence with a narrower statement such as: 'Lake marks Muniz good law as of 2026-06-30; proposed negative-treatment sign…

### F-S9-PR-588808eb93 · treatment-noise · sev=medium · needs_cl=true · quorum=2/3
- **object:** content/searches/two-definitions-of-search/Reasonable Expectation of Privacy.md
- **problem:** The lake record verifies the case identity but does not verify current treatment or progeny, so the page's live split/frontier use cannot be confirmed under Lens B.
- **verbatim:** Frontier stub: treatment/progeny intentionally not derived until S6 promotion.
- **tally:** codex-A=MISSING  |  codex-B=stands: Lake treatment.field_i_validity is unverified.  |  opus=refuted: Lake record (case_name 'United States v. Luke Wilson'): court '9th Cir.', year 2021, display '13 F.4th 961', absolute_url /opinion/5296785/united-states-v-luke-wilson/ — match asserted '(9th Cir. 202…
- **proposed_fix:** Complete treatment/progeny review before presenting Wilson as a current split authority, or qualify/remove it as an unaudited frontier stub.

### F-S9-PR-ecdb869fd5 · treatment-noise · sev=medium · needs_cl=true · quorum=2/3
- **object:** content/searches/two-definitions-of-search/Reasonable Expectation of Privacy.md
- **problem:** The lake record verifies the case identity but does not verify current treatment or progeny, so the page's live split/frontier use cannot be confirmed under Lens B.
- **verbatim:** Frontier stub: treatment/progeny intentionally not derived until S6 promotion.
- **tally:** codex-A=MISSING  |  codex-B=stands: Lake treatment.field_i_validity is unverified.  |  opus=refuted: Lake record United States v. Moore-Bush: court '1st Cir.', year 2022, display '36 F.4th 320', absolute_url /opinion/6476395/united-states-v-moore-bush/ — match asserted '(1st Cir. 2022) (en banc)' an…
- **proposed_fix:** Complete treatment/progeny review before presenting Moore-Bush as a current split authority, or qualify/remove it as an unaudited frontier stub.

### F-S9-PR-e485f73fe8 · treatment-noise · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/use-of-force-and-liability/Suing Federal Officers.md
- **problem:** Konan's current live-law/treatment status is not verified in the disclosed record; the lake record is a frontier stub with no derived treatment or progeny.
- **verbatim:** Frontier stub: treatment/progeny intentionally not derived until S6 promotion.
- **tally:** codex-A=stands-modified: Lake identity gives case_name Postal Service v. Konan, docket 24-351, year 2026, court_level scotus, and matching CourtListener URL.  |  codex-B=stands: The disclosed record identifies Konan as slip-only, but treatment.field_i_validity is unverified.  |  opus=refuted: Lake record confirms Postal Service v. Konan, docket 24-351, year 2026, cluster_id 10799651 — matches cited 'No. 24-351 (2026)' and opinion URL /opinion/10799651/. slip_only=true with no official rep…
- **proposed_fix:** Promote/review the Konan record and add a current treatment/good-law determination before using it as a current key authority.

### F-S9-PR-f546b294a3 · treatment-noise · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/use-of-force-and-liability/Suing Federal Officers.md
- **problem:** The Landor row is stale: it says the case 'Presents' the question, but the disclosed lake citation provenance says the Supreme Court decided it on June 23, 2026; treatment is also unverified.
- **verbatim:** SCOTUS No. 23-1197, decided 2026-06-23 (609 U.S. ___; Gorsuch, 6-3). No S. Ct. page yet.
- **tally:** codex-A=stands-modified: Lake identity case_name is Landor v. Louisiana Dept of Corrections and Public Safety, docket 23-1197, year 2026, court_level scotus, and matching CourtListener URL.  |  codex-B=stands: The table describes Landor as presenting a question rather than as a decided case.  |  opus=stands-modified: Existence/citation stand: lake record confirms Landor v. Louisiana Dept. of Corrections, docket 23-1197, year 2026, cluster_id 10878535, slip_only=true — matches cited 'No. 23-1197 (2026)' and opinio…
- **proposed_fix:** Replace pending-question wording with the decided holding after adding verified treatment; at minimum identify it as decided June 23, 2026 and slip-only.

### F-S9-PR-b2ed2e3db7 · truncated-holding · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Aguilar v. Texas.md
- **problem:** The holding field is truncated mid-parenthetical and omits the second Aguilar prong requiring circumstances supporting informant credibility or information reliability.
- **verbatim:** holding: "A magistrate may issue a warrant on an informant's hearsay only if the affidavit shows **(1) the informant's basis of knowledge** (how…"
- **tally:** codex-A=stands: The opinion states that the magistrate must be informed of circumstances behind both the informant's conclusion and the officer's conclusion that the informant was "credible" or his information "reli…  |  codex-B=stands-modified: Lake treatment field_i_validity is superseded as of 2026-06-30.  |  opus=refuted: Two-prong holding supported by opinion at 114: 'the magistrate must be informed of some of the underlying circumstances from which the informant concluded that the narcotics were where he claimed the…
- **proposed_fix:** Replace the holding with a complete two-prong formulation: a magistrate may issue a warrant on informant hearsay only if the affidavit gives underlying circumstances showing both the informant's basi…

### F-S9-PR-4782779307 · truncated-holding · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Andresen v. Maryland.md
- **problem:** The holding text is truncated and incomplete: it ends with 'does not violate the…' without identifying the Fifth Amendment or the particularity holding.
- **verbatim:** Accordingly, we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that "[n…
- **tally:** codex-A=stands-modified: A completed Fifth Amendment version is supported by the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: As far as it goes the proposition is supported - op.: 'we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend t…
- **proposed_fix:** Replace with: 'The search of an individual's office for pre-existing business records, their seizure, and later introduction into evidence did not offend the Fifth Amendment; the Lot 13T warrant's ca…

### F-S9-PR-c727ce5c4b · truncated-holding · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Arizona v. Evans.md
- **problem:** The core good-faith proposition is supported, but the holding text is truncated and should avoid implying that this record conclusively found a court clerk caused the error in this case.
- **verbatim:** There is no indication that the arresting officer was not acting objectively reasonably when he relied upon the police computer record. Application of the Leon framework supports a categorical except…
- **tally:** codex-A=stands-modified: The opinion supports the legal rule through its categorical-exception language.  |  codex-B=refuted: Lens B does not test holding support or quote fidelity.  |  opus=stands-modified: Substance is supported - op.: 'Application of the Leon framework supports a categorical exception to the exclusionary rule for clerical errors of court employees' and the Arizona Supreme Court judgme…
- **proposed_fix:** Replace with: "The good-faith exception applies when an arresting officer reasonably relies on an erroneous warrant record attributable to clerical errors of court employees; suppression is unwarrant…

### F-S9-PR-97831f6b0e · truncated-holding · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/cases/Arizona v. Roberson.md
- **problem:** The core proposition is supported, but the holding field is truncated after 'including an…' and should state the Edwards limits rather than saying only that police may not interrogate about ANY offense.
- **verbatim:** after a person in custody has expressed his desire to deal with the police only through counsel, he “is not subject to further interrogation by the authorities until counsel has been made available t…
- **tally:** codex-A=stands-modified: The opinion says Arizona sought an exception for interrogation about an unrelated offense and the Court rejected that position.  |  codex-B=stands-modified: The disclosed page itself notes Maryland v. Shatzer as a later refinement of the Edwards line.  |  opus=refuted: Opinion at *683: 'the presumption raised by a suspect's request for counsel ... does not disappear simply because the police have approached the suspect, still in custody, still without counsel, abou…
- **proposed_fix:** Revise to: The Edwards bar is not offense-specific: after a suspect in custody invokes counsel, police may not initiate further custodial interrogation about any offense while counsel has not been ma…

### F-S9-PR-19117c7a18 · truncated-holding · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/California v. Carney.md
- **problem:** The holding is substantively supported, but the content holding is truncated after '(1) ready…' and omits the complete first justification and the second justification.
- **verbatim:** The reasons for the vehicle exception, we have said, are twofold.
- **tally:** codex-A=stands-modified: The opinion supports applying the vehicle exception where the motor home was readily mobile and objectively used as a vehicle, not a residence.  |  codex-B=refuted: Support and holding fidelity are outside Lens B; no disclosed treatment downgrade defeats the proposition as a live-law reference.  |  opus=stands-modified: The stated portion (exception applies to a motor home used as a vehicle; two justifications) is fully supported by the opinion
- **proposed_fix:** Replace with: The automobile exception applies to a readily mobile motor home objectively being used as a vehicle rather than a residence; the exception rests on ready mobility/exigency and reduced e…

