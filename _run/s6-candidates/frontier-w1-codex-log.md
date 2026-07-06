## warrant-exceptions

Run date: 2026-07-06. Lane: S6 FRONTIER / Codex leg. Category: warrant-exceptions. Constraints honored: web-only discovery, zero CourtListener opened, no commits, no `s6-frontier-*claude*` files read.

Local skim:
- Read/skimmed only `content/warrant-exceptions/` overview and node pages. Did not read `content/cases/` case pages.
- Seed theories from nodes: consent scope and digital devices; SITA non-vehicle containers after `Gant`; border forensic device searches after `Riley`; special-needs/admin search applications.
- Corpus checks used `content/cases` existence tests and `rg` against `content/warrant-exceptions`/`content/cases`. Missing captions confirmed for Lewis, Kolsuz, Aigbekaen, Alasaad, Perez, Eatherton, Knapp, Cook, Shakir, and Vergara.

Web discovery path:
- Consent digital scope: seed `Jimeno`/node prose -> `United States v. Lewis` (6th Cir. 2023), cross-checked Justia and Sixth Circuit PDF. No further expansion because searches/resurfacing stayed on the same consent-scope issue and produced no split marker stronger than Lewis.
- Border devices: seed `Riley`, `Cotterman`, `Cano`, `Touset` -> `Kolsuz`, `Aigbekaen`, `Alasaad`; cross-checked Justia pages plus official/Justia PDFs. Existing corpus covers Ninth (`Cotterman`/`Cano`) and Eleventh no-suspicion (`Touset`); missing page candidates cover Fourth and First Circuit split/narrowing markers.
- SITA containers: seed `Gant`/`Davis` -> `Perez`; second-hop only through Perez's own cited split cases (`Eatherton`, `Knapp`, `Cook`, `Shakir`, `Vergara` not in this branch). Existing `United States v. Howard Davis` covers the yes-extend side; Perez supplies the missing no-extend First Circuit side.

Stop conditions fired:
- New searches/direct index walks began resurfacing known anchors and local prose-only cases rather than new controlling omissions.
- Both directions run on key split cases: border device searches (Fourth/Ninth/First/Eleventh named) and SITA carried containers (First versus Third/Fourth/Ninth/Tenth, with Eighth noted as reserved/qualified in Perez).
- Circuits accounted or split flagged: 1st, 3d, 4th, 6th, 9th, 10th, 11th; 8th noted through Perez as qualified/reserved but not elevated.
- No unaddressed first-impression marker remained after Kolsuz, Aigbekaen, Alasaad, Lewis, and Perez checks.
- Second source cross-check completed for all page candidates via Justia plus official circuit PDF or Justia PDF.
- Adverse authority captured: Perez against the Davis/Knapp/Cook/Shakir line; Alasaad/Vergara/Touset against broader warrant/probable-cause or digital-contraband-only border-device formulations.

Page candidates:
- `United States v. Lewis` (6th Cir. 2023): consent to preview digital devices does not carry later seizure/forensic search.
- `United States v. Kolsuz` (4th Cir. 2018): forensic border phone search is nonroutine and needs individualized suspicion.
- `United States v. Aigbekaen` (4th Cir. 2019): intrusive border-device suspicion must have a border-purpose nexus.
- `Alasaad v. Mayorkas`/`Alasaad v. Wolf` (1st Cir. 2021): no warrant/probable cause for advanced device searches; scope not limited to digital contraband.
- `United States v. Perez` (1st Cir. 2023): declines to extend `Gant` to carried backpack/container search under First Circuit precedent.

Mention-only finds:
- `United States v. Eatherton`, `United States v. Knapp`, `United States v. Cook`, `United States v. Shakir`, `United States v. Vergara`.

## use-of-force-and-liability

Date: 2026-07-06

Constraints honored: WEB ONLY for discovery; zero CourtListener; no commits; blind-pair constraint honored by not reading any `s6-frontier-*claude*` file.

Local skim:
- Read/skimmed only `content/use-of-force-and-liability/index.md` and the six node pages in that directory.
- Did not read individual `content/cases/` case pages.
- Seed terminology/theories: Fourth Amendment objective reasonableness, deadly force, qualified immunity specificity, Monell policy/custom/final policymaker/failure-to-train, Bivens/FTCA federal-officer remedies, retaliatory arrest, Fourth Amendment malicious prosecution, and civil asset forfeiture.

Corpus existence checks:
- Used `ls content/cases` plus `rg -F -i -l` against `content/cases` for candidate captions.
- Most direct page-candidate captions were missing as case files. `Egbert v. Boule`, `Ziglar v. Abbasi`, and `Wallace v. Kato` appeared only as text references, not as matching case-page filenames.

Web discovery path:
- Hop 0 seeds from node pages: `Graham`, `Garner`, `Mendez`/provocation-rule issue, `Nieves`/retaliatory-arrest issue, `Manuel`/malicious-prosecution issue, `Culley`/civil-forfeiture hearing issue, `Bivens`/federal-officer liability, `Monell`/municipal liability.
- Hop 1 direct SCOTUS searches found omitted controlling cases: `Mendez`, `Zorn`, `Nieves`, `Gonzalez`, `Lozman`, `Reichle`, `Hartman`, `Manuel`, `Thompson`, `Chiaverini`, `Culley`, `Timbs`, `Austin`, `Bajakajian`, `Bennis`, `$8,850`, `Von Neumann`, `Abbasi`, `Egbert`, `Hernandez`, `Martin`, `Owen`, `Bryan County`, `Will`, `Hafer`.
- Hop 2 split/source expansion stayed inside opinions and case summaries: `Chiaverini` names Sixth Circuit versus Second/Third/Eleventh; `Thompson` names Second/Third/Tenth versus Eleventh; `Manuel` names Seventh as outlier versus ten circuits; `Martin` names the Eleventh Circuit's unique FTCA approach versus most courts.

Classification:
- Page-candidate true only where the authority is controlling SCOTUS or the opinion itself resolves/marks a circuit split.
- Mention-only false rows: `Brownback`, `Albright`, `Wallace`, `Calero-Toledo`, and `Millbrook`; each is real and adjacent but lower priority than the direct controlling omissions.
- Not promoted: `Lombardo v. City of St. Louis` (fact-bound per curiam remand, not stronger than `Mendez`/`Zorn`/`Barnes` for the page gap); `Jimerson v. Lewis` was locally mentioned as wrong-house-raid QI adverse authority, but I did not obtain a second non-CourtListener web cross-check in this pass, so I did not row it.

Stop conditions fired:
- New searches began resurfacing the same SCOTUS clusters for retaliatory arrest, malicious prosecution, forfeiture, Bivens/FTCA, and Monell.
- Both directions ran on the key cases: seed-to-cases and case-to-named splits.
- Circuits accounted or split flagged for the major split-resolving cases: Sixth vs Second/Third/Eleventh (`Chiaverini`), Second/Third/Tenth vs Eleventh (`Thompson`), Seventh vs ten circuits (`Manuel`), Eleventh unique approach vs most courts (`Martin`).
- No unaddressed first-impression marker remained in the web-confirmed SCOTUS set.
- Second-source cross-check completed for strongest/newest finds using official SCOTUS PDFs plus Justia/Oyez/Wikipedia/news where available.
- Adverse authority captured: `Zorn`, `Mendez`, `Bennis`, `Culley`, `Egbert`, `Hernandez`, `Martin`, `Owen`, `Will`, and `Bryan County`.

## seizures

Run date: 2026-07-06. Lane: S6 FRONTIER, Codex leg. Constraints observed: WEB ONLY for discovery, zero CourtListener, no commits, and no reads of `s6-frontier-*claude*` files.

Local skim:
- Read `content/seizures/index.md` plus seizures node pages only, including arrests node pages; did not read every `content/cases` page.
- Draft local gaps: `Seizure of Property`, `Stop-and-Identify`, `Arrest & Arrest Warrants`, and `Prompt Probable-Cause Determination`.
- Seed doctrines/cases: seizure of person (`Mendenhall`, `Hodari D.`, `Torres`), Terry/RAS and frisk, stop-and-identify, traffic-stop duration/mission, seizure of property, collective knowledge, arrests/home-entry.

Corpus checks:
- Used `find content/cases -maxdepth 1 -type f` plus targeted `rg --fixed-strings` checks.
- Existing-page collisions noted: `United States v. Robinson.md` is the 1973 SCOTUS search-incident case, not 4th Cir. en banc; `United States v. Ramirez.md` is the 1998 SCOTUS no-knock property-destruction case, not 9th Cir. collective-knowledge.
- Missing candidates confirmed absent: `United States v. James Daniel Good Real Property`, `United States v. $8,850 in Currency`, `United States v. Von Neumann`, `Culley v. Marshall`, `United States v. Landeros`, `United States v. Black`, `Northrup v. City of Toledo Police Department`, and 4th Cir. en banc `United States v. Robinson`.

Web discovery notes:
- Used official SCOTUS PDFs, Supreme Justia, Cornell LII, Justia federal appellate pages/PDFs, Leagle, and Wikipedia only as secondary context; no CourtListener links opened.
- Property-seizure searches from the draft node surfaced the SCOTUS forfeiture line: `Good Real Property` (pre-seizure hearing for real property), `$8,850` (Barker timeliness for delayed forfeiture filing), `Von Neumann` (remission not constitutionally required), and `Culley` (no separate preliminary retention hearing for seized personal property).
- Stop-and-identify / traffic-stop mission searches surfaced `Landeros` as the strongest binding-in-circuit omission on passenger ID demands and Rodriguez prolongation.
- Lawful-carry / frisk searches surfaced the 4th/6th split markers: `Robinson` (4th Cir. en banc armed-during-lawful-stop side), `Northrup` (6th Cir. lawful open carry not enough side), plus `Black` as a 4th Cir. seizure/RAS/open-carry marker.

Mention-only real finds:
- `Noem v. Vasquez Perdomo`, 606 U.S. ___ (2025), No. 25A169: Supreme Court stay order with Kavanaugh concurrence on immigration-stop reasonable suspicion and ethnicity/language/work/location factors; logged as adverse/frontier but not a page-candidate because it is interim stay posture, not a merits holding.

Discarded / deferred:
- `District of Columbia v. R.W.`: no reliable non-CourtListener web verification found in this pass.
- `United States v. Amos`, `Daniels`, `Cole`, `Mayville`, `Massenburg`, `Chavez`, and 9th Cir. `Ramirez`: lower-priority/deferred because searches either resurfaced local-known material or lacked a second non-CourtListener cross-check within the two-hop window.

Stops fired:
- New searches only resurfaced knowns after the property-forfeiture SCOTUS line, `Landeros`, and the lawful-carry split markers.
- Both directions run on key cases: seed-to-cites and topic-to-caption for property seizure, stop-and-identify/prolongation, and lawful-carry frisk/detention.
- Circuits accounted or split flagged: 4th versus 6th/7th lawful-carry frisk/detention split flagged; 9th identified for passenger-ID prolongation.
- No unaddressed first-impression markers after excluding unverified `D.C. v. R.W.` and non-merits `Noem`.
- Second-source cross-check completed for included page candidates.
- Adverse authority captured: `Noem v. Vasquez Perdomo` logged mention-only.

## searches

Run date: 2026-07-06. Lane: S6 FRONTIER, Codex leg. Constraints observed: WEB ONLY for discovery, zero CourtListener, no commits, and no reads of `s6-frontier-*claude*` files.

Local skim:
- Read only `content/searches/` overview and node pages: the top-level searches index, authored topic pages, and draft child nodes. Did not read case pages as research inputs; existence checks used `ls content/cases` plus targeted grep.
- Seed/gap signals: two definitions of search, curtilage/open fields, aerial/enhanced surveillance, third-party/digital surveillance, Title III, private/foreign searches, abandonment, tents, and plain-view/plain-feel.

Corpus checks:
- Already present locally: Chatrie, Smith (2024), Tuggle, Morton, Herlth, Volle, Mansor, Hughes, Basher, Gooch, Sandoval, Lundin, Jacobsen, Walter, Silverman, Soldal, Place, New York v. Class, See, and the core aerial/open-fields anchors.
- Missing candidates confirmed absent by `ls content/cases | grep`: Burdeau, Verdugo-Urquidez, Keith, Giordano, United States v. Donovan, Scott v. United States, Leaders of a Beautiful Struggle, Warshak, and Gratkowski.

Web discovery notes:
- Private/foreign searches draft node drove the Burdeau and Verdugo checks. Burdeau is missing but Jacobsen already exists; Verdugo was also flagged in the prior remedies/standing lane, but it is independently searches-relevant here.
- Electronic Surveillance & Title III draft node drove the Keith/Giordano/Donovan/Scott additions. Each is SCOTUS controlling and cross-checked through Justia plus LOC U.S. Reports PDFs.
- Aerial/enhanced surveillance searches found Leaders as the strongest missing federal split-marker: Fourth Circuit en banc treats access to wide-area aerial surveillance data as a search under Carpenter/mosaic logic.
- Third-party/digital surveillance expansion found Warshak (stored email content protected) and Gratkowski (Bitcoin/Coinbase records not protected) as missing binding circuit markers on opposite sides of digital third-party doctrine.
- Cell-site-simulator, drone, reverse-keyword, and investigative-genetic-genealogy searches mostly surfaced state, district, news, or commentary sources. Long Lake Township v. Maxon and State v. Andrews were kept mention-only.

Mention-only real finds:
- Long Lake Township v. Maxon (Mich. 2024): drone frontier, but state civil/exclusionary posture and no constitutional search holding.
- State v. Andrews, 134 A.3d 324 (Md. Ct. Spec. App. 2016): Stingray warrant state authority, useful illustration but below federal page-candidate floor.
- Local seed names not rowed without a second non-CourtListener web source in this pass: Moore-Bush, May-Shaw, Hay, Porter, Wilson/hash-matching, Ruckman, Hunt, Small, Crumble, Loines, Burgess, Ganias, and Loera.

Stops fired:
- New searches only resurfaced knowns: geofence searches returned Chatrie and Smith, both already in `content/cases`; private-search searches returned Jacobsen, already present.
- Both directions run on key cases: Title III statutory suppression/authorization plus minimization; private-search plus foreign-search boundaries; digital third-party protection (Warshak) plus adverse transactional-record authority (Gratkowski).
- Circuits accounted or split flagged: Fourth Circuit Leaders flagged the Carpenter/mosaic aerial-surveillance side against existing public-view/pole-camera authorities; Sixth Circuit Warshak and Fifth Circuit Gratkowski flag the digital-content versus transactional-record boundary.
- No unaddressed first-impression markers after cell-site-simulator, reverse-keyword, drone, and genetic-genealogy searches produced only below-floor state/district/news sources.
- Second source cross-checked for all page candidates: SCOTUS rows via Justia plus LOC; circuit rows via official circuit PDF plus secondary web source.
- Adverse authority captured: Verdugo limits extraterritorial Fourth Amendment coverage; Gratkowski limits Carpenter-style expansion to cryptocurrency/business records; state drone/Stingray finds retained as mention-only.
