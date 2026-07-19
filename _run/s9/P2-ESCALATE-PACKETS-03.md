# P2 ESCALATE PACKET 03/12

_findings: 25 | classes: home-mirror=23, identity-miskey=2_

### F-S9-PR-b748c9ff4e · home-mirror · sev=low · needs_cl=true · quorum=3/3
- **object:** content/cases/Anderson v. Creighton.md
- **problem:** The opinion supports Anderson as a qualified-immunity particularization case, but the stronger home-role label "Foundational" is not established by the disclosed lake record or opinion text as a corpus-level importance judgment.
- **verbatim:** must have been “clearly established” in a more particularized, and hence more relevant, sense
- **tally:** codex-A=stands: The opinion directly supports the parenthetical particularization point at page 640.  |  codex-B=stands-modified: The opinion and lake identity show this is a Supreme Court qualified-immunity case, so the home topic itself is not the currency problem.  |  opus=stands-modified: Role fit is correct - Anderson is the foundational particularized 'clearly established' QI case - so the assertion survives.
- **proposed_fix:** Tighten the role to "Key — clearly-established rights must be defined in a particularized sense" or add disclosed corpus/progeny support before using "Foundational."

### F-S9-PR-b604d87ede · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Arkansas v. Sanders.md
- **problem:** The case is properly connected to the Automobile Exception, but the role label 'Historical / origin' is overbroad unless 'origin' is understood as the origin of the former luggage/container limitation, not the origin of the automobile exception itself.
- **verbatim:** In earlier cases, on the other hand, the Court sustained the constitutionality of warrantless searches of automobiles and their contents under what has become known as the “automobile exception” to t…
- **tally:** codex-A=stands-modified: The opinion expressly frames the case as deciding whether Sanders falls on the Chadwick or Chambers/Carroll side of the automobile-exception line.  |  codex-B=stands: Lens B makes no support finding about whether the case belongs under Automobile Exception.  |  opus=refuted: Sanders is a foundational (now-overruled) container/automobile-exception case extending Chadwick; 'Historical / origin' on 'Automobile Exception' is apt.
- **proposed_fix:** Change the home role to something like 'Historical / former container limitation' or 'Historical / luggage-container rule' rather than unqualified 'Historical / origin'.

### F-S9-PR-dbc8d35023 · home-mirror · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/cases/Board of County Commissioners of Bryan County v. Brown.md
- **problem:** The asserted Anchor home-role for Section 1983 Liability and Qualified Immunity does not follow from disclosed opinion text or a lake holding because neither is present.
- **verbatim:** "pinpoints": []
- **tally:** codex-A=stands: The home-role appears in content_page.md, but that is the assertion source under review.  |  codex-B=stands-modified: The page frontmatter lists the home as Section 1983 Liability and Qualified Immunity with role Anchor.  |  opus=refuted: Frontmatter homes[0] = '[[Section 1983 Liability and Qualified Immunity]]' role 'Anchor'; the '## Appears on' section matches exactly ('Section 1983 Liability and Qualified Immunity — Anchor').
- **proposed_fix:** Provide the relevant section-page criteria plus opinion text or lake holding showing why this case is an Anchor for that home.

### F-S9-PR-b21d326d1e · home-mirror · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/cases/Brownback v. King.md
- **problem:** The disclosed authority record does not verify the home placement or role as Suing Federal Officers / Recent development. The lake record supplies identity and citation metadata but no holding or pinpoint support, and no cached opinion text is present.
- **verbatim:** frontier stub, no pinpoints
- **tally:** codex-A=stands: Lens A requires the home role to follow from opinion text and lake holding at the stated breadth.  |  codex-B=refuted: Support classification is outside Lens B.  |  opus=stands-modified: Assertion accurately reflects the frontmatter home '[[Suing Federal Officers]]' / role 'Recent development', and Brownback (FTCA judgment bar interacting with Bivens claims against federal officers)…
- **proposed_fix:** Supply text/Brownback v. King.txt or lake holding/pinpoint fields supporting this placement and role, or remove/mark the home role as unverified.

### F-S9-PR-f7ad539835 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/FBI v. Fazaga.md
- **problem:** The case is connected to suits naming federal officials and agents, but the Court's resolved holding is FISA/state-secrets displacement, and it expressly did not discuss the individual-capacity agent claims. The 'Recent development' role for Suing Federal Officers is broader than the disclosed hold…
- **verbatim:** but we need not discuss those
- **tally:** codex-A=stands-modified: Opinion text says respondents sued the United States, FBI, and two FBI officials in official capacities, plus individual agents.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Placement on a suing-federal-officers hub is doctrinally plausible (plaintiffs sued the FBI and individual agents; Fazaga preserves the state-secrets bar to such suits), so the assertion survives
- **proposed_fix:** Change the role to a narrower related role, or qualify it as a state-secrets/FISA threshold-defense development in litigation naming federal officials.

### F-S9-PR-73501b2915 · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Gaetjens v. Winnebago County.md
- **problem:** Emergency Aid placement and 7th Circuit label are supported, but the 'expands' part of 'expands/illustrates' is not independently shown; the disclosed opinion supports an application/illustration of established emergency-aid doctrine.
- **verbatim:** The home entry in this case likewise falls into the heartland of emergency‐aid situations.
- **tally:** codex-A=stands-modified: The opinion expressly describes the home entry as an emergency-aid situation.  |  codex-B=stands-modified: Lake identity supports that this is a Seventh Circuit court-of-appeals decision.  |  opus=refuted: 2021 7th Cir. application of the emergency-aid exception (Brigham City / Caniglia line); 'Recent development — expands/illustrates (Binding in-circuit — 7th Cir.)' on the Emergency Aid home is suppor…
- **proposed_fix:** Change the role to: Recent application — illustrates (Binding in-circuit — 7th Cir.).

### F-S9-PR-0ffb3e6d01 · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Hanlon v. Berger.md
- **problem:** The Qualified Immunity home is supported, but the role label 'Key — Progeny / Refinement' is not quite supportable as framed. The disclosed evidence characterizes Hanlon as a same-day companion applying Wilson, not as ordinary progeny.
- **verbatim:** Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree.
- **tally:** codex-A=stands-modified: The opinion squarely turns on qualified immunity.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands: Frontmatter home page ([[Qualified Immunity]]) does not match the body 'Appears on' page ([[Section 1983 Liability and Qualified Immunity]]); the other three groups in this pack have matching frontma…
- **proposed_fix:** Change role to 'Key — Companion / Application' or 'Key — Qualified Immunity Application'.

### F-S9-PR-a3de447b27 · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Hernandez v. Mesa.md
- **problem:** The Suing Federal Officers placement is legally supportable, but the built page is internally inconsistent: frontmatter homes lists Suing Federal Officers while the rendered Appears on section lists Section 1983 Liability and Qualified Immunity.
- **verbatim:** - [[Section 1983 Liability and Qualified Immunity]] — *Recent development*
- **tally:** codex-A=stands-modified: The opinion states the parents sought damages under Bivens against Border Patrol Agent Mesa for alleged Fourth and Fifth Amendment violations, supporting a federal-officer-suit placement.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Assertion (home '[[Suing Federal Officers]]', role 'Recent development') matches the frontmatter homes block and is substantively apt for a Bivens cross-border-shooting claim against a federal officer
- **proposed_fix:** Align the rendered Appears on section with the inventoried home, or change the inventoried home to the page actually rendered.

### F-S9-PR-2a6af26eef · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Hester v. United States.md
- **problem:** This is a duplicate Abandonment home-role assertion. The content frontmatter repeats the same Abandonment role, while the page body lists it once.
- **verbatim:** - page: "[[Abandonment]]" role: "Key — Progeny / Refinement" - page: "[[Abandonment]]" role: "Key — Progeny / Refinement"
- **tally:** codex-A=stands: group_inventory contains two identical Abandonment support rows.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Substantively correct — Hester is a Key — Progeny / Refinement case for Abandonment — but this homes[] entry is a byte-identical duplicate of e2b05a4c94a3dcb5.
- **proposed_fix:** Remove the duplicate Abandonment frontmatter entry and retain a single corrected Abandonment role.

### F-S9-PR-45e99e9289 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/James v. Illinois.md
- **problem:** The role as a limiting impeachment-exception case is supported, but the asserted home 'Fruits & Attenuation' is not cleanly verified from the disclosed page: the rendered Appears on section identifies a different home.
- **verbatim:** - [[The Exclusionary Rule]] — *Key — Limiting (impeachment exception)*
- **tally:** codex-A=stands-modified: The legal role is supported because the opinion limits the impeachment exception to defendants' own testimony.  |  codex-B=refuted: Lens B review found no current-treatment defect in using James as a limiting impeachment-exception authority.  |  opus=stands: Frontmatter homes[0].page is '[[Fruits & Attenuation]]' but '## Appears on' lists '[[The Exclusionary Rule]]' for the same role string — an internal inconsistency within the disclosed page.
- **proposed_fix:** Align the home metadata with the rendered page, likely to [[The Exclusionary Rule]], or add disclosed taxonomy/page evidence explaining why James belongs under Fruits & Attenuation as an impeachment-…

### F-S9-PR-69a7e8f184 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Mallory v. United States.md
- **problem:** The home-role labels Mallory as a Key Anchor for Due-Process Voluntariness of Confessions, but the disclosed opinion and page frame the case as a Federal Rule of Criminal Procedure 5(a) prompt-presentment case, not a due-process voluntariness anchor.
- **verbatim:** The case calls for the proper application of Rule 5 (a) of the Federal Rules of Criminal Procedure
- **tally:** codex-A=stands: The lake/content holding is limited to unnecessary delay under Federal Rule of Criminal Procedure 5(a).  |  codex-B=stands-modified: The disclosed treatment expressly narrows Mallory to a federal-court Rule 5(a) rule.  |  opus=stands-modified: Opinion decides the case solely on Federal Rule of Criminal Procedure 5(a) (prompt presentment / McNabb-Mallory), never invoking the Due Process Clause or confession voluntariness; the content_page s…
- **proposed_fix:** Move Mallory to a McNabb-Mallory or federal prompt-presentment home, or downgrade it on the due-process voluntariness home to a related/contrast role.

### F-S9-PR-4c051e8e71 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Robbins v. California.md
- **problem:** The Automobile Exception home is supported, but the role label "Historical / origin" overstates origin. The opinion treats Robbins as applying/reaffirming Chadwick and Sanders in the automobile-container setting, not as the origin of the automobile exception.
- **verbatim:** In recent years, we have twice been confronted with the suggestion that this “automobile exception” somehow justifies the warrantless search of a closed container found inside an automobile. Each tim…
- **tally:** codex-A=stands-modified: The opinion directly concerns the automobile exception and closed containers found during lawful automobile searches.  |  codex-B=stands: Lake treatment.field_i_validity is unverified, as_of_treatment is null, and treatment.edges is empty.  |  opus=refuted: Content page frontmatter homes and the 'Appears on' section both list [[Automobile Exception]] with role 'Historical / origin'.
- **proposed_fix:** Keep the Automobile Exception home, but change the role to a narrower historical container-rule label, such as "Historical / container limitation" or "Historical / superseded container rule".

### F-S9-PR-9dca3712ae · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Soldal v. Cook County.md
- **problem:** The reviewed Trespass role is supportable only as related/cross-doctrine, but the built page's Appears on section assigns Trespass the stronger Key — Anchor role, creating an internal role conflict.
- **verbatim:** - [[Trespass]] — *Key — Anchor (seizure of property)*
- **tally:** codex-A=stands-modified: The opinion includes a requested criminal trespass complaint and unlawful physical removal, which is enough for a related cross-doctrine placement.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Frontmatter role for Trespass ('Related (cross-doctrine)') is doctrinally correct and is the value the assertion mirrors; the '## Appears on' section is the inconsistent artifact (it misapplied the S…
- **proposed_fix:** Synchronize the body Appears on entry for Trespass to 'Related (cross-doctrine)' or remove the conflicting body role.

### F-S9-PR-ad3d40b44e · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/Soldal v. Cook County.md
- **problem:** The Seizure of Property anchor role is strongly supported, but the built page's Appears on section omits Seizure of Property and instead puts the anchor label under Trespass.
- **verbatim:** - [[Trespass]] — *Key — Anchor (seizure of property)*
- **tally:** codex-A=stands-modified: The opinion holds that physically tearing the trailer from its foundation and towing it away sufficed to constitute a Fourth Amendment seizure.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The home/role claim is substantively correct (Soldal is the seizure-of-property anchor: holding protects possessory interests independent of privacy/liberty), and matches frontmatter; the defect is t…
- **proposed_fix:** Add '[[Seizure of Property]] — Key — Anchor (seizure of property)' to the Appears on section and remove that anchor label from Trespass.

### F-S9-PR-427ff67df6 · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Berkowitz.md
- **problem:** The substantive role stands, but the embedded pin '927 F.2d at 1386' is too narrow for the full parenthetical. Page 1386 supports the voice-from-outside/arrest-OK point; the warrantless-entry-before-arrest-not point continues onto the next reporter pages in the cached text.
- **verbatim:** Entering a person’s <page-number citation-index="1" label="1387">*1387</page-number>home without a warrant to arrest him, where no exigent circumstances exist, violates this clear command.
- **tally:** codex-A=stands-modified: The case is key for Entry to Arrest because the opinion's suppression analysis turns on whether agents entered before or after effecting the arrest.  |  codex-B=stands-modified[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=refuted: Frontmatter homes lists Entry to Arrest with the exact Key role string in the payload, including 'voice-from-outside arrest OK, warrantless entry before arrest not, 927 F.2d at 1386'.
- **proposed_fix:** Use a broader pin such as 927 F.2d at 1386-88, or split the parenthetical into voice/surrender at 1386 and entry-before-arrest at 1387-88.

### F-S9-PR-4e15082b87 · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Calandra.md
- **problem:** The disclosed evidence supports Calandra as foundational to later good-faith and cost-benefit exclusionary-rule cases, but not the exact role label 'Progeny / Refinement' on The Good-Faith Exception. The opinion predates and does not itself discuss a good-faith exception.
- **verbatim:** Good law; foundational statement of the exclusionary rule as a deterrent remedy, central to later good-faith and cost-benefit cases.
- **tally:** codex-A=stands-modified: The opinion supports deterrence and cost-benefit relevance: it states the rule's prime purpose is deterrence and weighs grand-jury costs against incremental deterrence.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Substance holds — Calandra's deterrence/cost-benefit rationale is a key antecedent to the good-faith and cost-benefit line — but the specific home label in this assertion conflicts with the page's ow…
- **proposed_fix:** Use a role such as 'Key - Foundation / Deterrence rationale' for The Good-Faith Exception, or move the visible home role to The Exclusionary Rule if the intended label is 'Key - Progeny / Refinement.'

### F-S9-PR-705b6d2725 · home-mirror · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/cases/United States v. Carloss.md
- **problem:** The disclosed evidence supports a judicial divide/dissent over No Trespassing signage, but not the stronger home-role label 'Illustrates a circuit split.' The cached opinion identifies other circuits agreeing that knock-and-talks remain valid after Jardines and does not supply an opposing circuit r…
- **verbatim:** Good law. Then-Judge Gorsuch dissented, illustrating the divide over whether 'No Trespassing' signage revokes the implied knock-and-talk license.
- **tally:** codex-A=stands: Lake treatment scope_note says the case illustrates a divide based on then-Judge Gorsuch's dissent, not a circuit split.  |  codex-B=refuted: Lens B only: the lake scope note itself says the case illustrates the divide over No Trespassing signage and the implied knock-and-talk license.  |  opus=stands-modified: Case correctly belongs on the Knock and Talk home and genuinely illustrates a divide over whether signage revokes the implied license, so the assertion survives in substance.
- **proposed_fix:** Change the role to 'Illustrates a divide over No Trespassing signage and knock-and-talk' or supply disclosed authority records/text for the asserted opposing circuit position.

### F-S9-PR-cd71e4b267 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Evans.md
- **problem:** The home subject 'Inventory Searches' is supported, but the role label 'Recent development (role-based)' is not supported by the opinion text or lake fields, and the disclosed files provide no role taxonomy showing why a 1991 case should be classified as 'Recent development'.
- **verbatim:** Accordingly, we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search, and the evidence discovered subsequently (pursuant to valid search warrants) was not th…
- **tally:** codex-A=stands: The opinion plainly concerns a lawful inventory search, so the home page topic is supported.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The payload (home 'Inventory Searches', role 'Recent development (role-based)') matches the frontmatter homes block verbatim, so the assertion is faithful to its source.
- **proposed_fix:** Keep the Inventory Searches home only with a supportable role such as 'Application of standardized inventory-search procedure' or supply disclosed role-taxonomy evidence for 'Recent development'.

### F-S9-PR-8aa0c71d66 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Janis.md
- **problem:** The disclosed opinion supports Janis as an intersovereign civil-proceeding limitation on the exclusionary rule, not as a key Good-Faith Exception home authority. Good faith is a fact/factor, not the operative home-role shown by the holding.
- **verbatim:** civil proceeding of one sovereign of evidence seized by a criminal law enforcement agent of another sovereign
- **tally:** codex-A=stands: The Court framed the issue as whether to extend the judicially created exclusionary rule to federal civil use of state-seized evidence.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Role 'Key — Limiting' is correct and supported by the holding.
- **proposed_fix:** Move the home role to The Exclusionary Rule as Key — Limiting, or qualify Janis on The Good-Faith Exception only as a cost-benefit/good-faith precursor rather than a key home authority.

### F-S9-PR-420152932d · home-mirror · sev=low · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Maez.md
- **problem:** The Key constructive-entry role is supported, and the 1451 pinpoint lands on the relevant discussion, but 'SWAT loudspeaker order' is slightly overstated against the opinion's wording of 'asked' or 'requested' exit by loudspeaker/bullhorn.
- **verbatim:** Both courts reasoned that Payton was violated. Al-Azzawy, 784 F.2d at 893; Morgan, 743 F.2d at 1166.
- **tally:** codex-A=stands-modified: The 1451 passage explains that physical crossing of the threshold is not dispositive and adopts the show-of-force/coercion reasoning.  |  codex-B=stands-modified: Lake identity supports that Maez is a 10th Circuit case involving the cited constructive-entry topic, but Lens B cannot confirm current doctrinal vitality.  |  opus=refuted: 'Entry to Arrest' Key role with parenthetical '10th Cir. recognizing side: SWAT loudspeaker order = warrantless in-home arrest, 872 F.2d at 1451' matches the coercion holding stated on page *1451 (b1…
- **proposed_fix:** Use 'SWAT loudspeaker request under coercive show of force = warrantless in-home arrest, 872 F.2d at 1451.'

### F-S9-PR-172d07ec2c · home-mirror · sev=medium · needs_cl=true · quorum=3/3
- **object:** content/cases/United States v. Reddick.md
- **problem:** The role label's 'split' component is not verified by the disclosed Reddick materials. The opinion supports a key Fifth Circuit hash-match private-search rule, but the disclosed files do not establish a circuit split.
- **verbatim:** no other circuit has confronted the precise question before us
- **tally:** codex-A=stands-modified: Reddick itself supports the hash-match and Fifth Circuit portions of the role.  |  codex-B=stands-modified: Lake treatment says the record is a frontier stub with treatment/progeny intentionally not derived.  |  opus=refuted: Reddick is a Fifth Circuit private-search-doctrine decision resolving a hash-match viewing question; the opinion contrasts the Tenth Circuit's more privacy-protective Ackerman approach, supporting a…
- **proposed_fix:** Change the role to 'Key — hash-match private-search rule (5th Cir.)' or add disclosed authority establishing the split.

### F-S9-PR-85aee1b757 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/United States v. Touset.md
- **problem:** The disclosed evidence supports placing the case under Border Searches, but it does not verify the role label Recent development (role-based) or define a recency/taxonomy standard for that label.
- **verbatim:** 
- **tally:** codex-A=stands: The opinion is plainly about forensic searches of electronic devices at the border, so the Border Searches home is supported.  |  codex-B=stands-modified: Home-role support is outside Lens B except for currency implications.  |  opus=refuted: Role 'Recent development (role-based)' for home 'Border Searches' is apt: Touset is a 2018 border-search device case; frontmatter and 'Appears on' section agree.
- **proposed_fix:** Retain the Border Searches home only if the corpus permits an unroled home entry, or provide the Border Searches page/role taxonomy supporting Recent development (role-based).

### F-S9-PR-fd78335ed7 · home-mirror · sev=medium · needs_cl=false · quorum=3/3
- **object:** content/cases/Weeks v. United States.md
- **problem:** The disclosed evidence does not support making Weeks a Key — Anchor case for Fruits & Attenuation; the page body instead lists The Exclusionary Rule, and the opinion concerns direct use of seized letters, not derivative fruits or attenuation doctrine.
- **verbatim:** ## Appears on - [[The Exclusionary Rule]] — *Key — Anchor*
- **tally:** codex-A=stands: No Fruits & Attenuation home page or taxonomy criteria were disclosed.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Substance holds — Weeks is the exclusionary-rule origin and a legitimate Key/Anchor for either exclusionary-rule or fruits/attenuation material (related list includes Wong Sun and Leon).
- **proposed_fix:** Change the home to [[The Exclusionary Rule]] — Key — Anchor, or disclose taxonomy evidence showing why Weeks anchors Fruits & Attenuation and narrow the role to background precursor.

### F-S9-PR-f040814daa · identity-miskey · sev=high · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/morse-v-french--6536632.json
- **problem:** The disclosed record does not verify the cited authority as live law. It is only a stub folded-alias record with no derived treatment or progeny, and the provenance warning says it has been subsumed into another record.
- **verbatim:** folded-alias: subsumed into French v. Merrill (packet-A Group-2); see _manifest.json folded_into + journal s6-dedupe-pointer
- **tally:** codex-A=stands-modified: The payload's official citation 68 Mass. 111 matches lake.citations.official.cite and lake.citations.display.  |  codex-B=stands: The record status is folded-alias and stub is true, so the disclosed file does not support treating this as an independent live authority.  |  opus=refuted: Payload (official '68 Mass. 111' selected_official:true; all[] single '68 Mass. 111'; display '68 Mass. 111'; official_selection_present:true) mirrors the lake citations block and official_selection…
- **proposed_fix:** Do not present this record as a current live authority. Replace/promote to the canonical disclosed record with derived treatment/progeny, or label the citation as folded-alias and treatment-unverifie…

### F-S9-PR-cb090fd614 · identity-miskey · sev=low · needs_cl=false · quorum=3/3
- **object:** content/searches/Electronic Surveillance and Title III.md
- **problem:** The citation, court, and year match, but the displayed caption uses the Keith shorthand rather than the lake canonical caption; the lake flags canonical_name_match=false and reason_code=caption_mismatch_accepted_by_citation.
- **verbatim:** United States v. United States District Court for the Eastern District of Michigan
- **tally:** codex-A=stands-modified: Official citation in the lake is 407 U.S. 297 and the decision year is 1972.  |  codex-B=stands: The citation 407 U.S. 297 is present, but the lake record status is under_review.  |  opus=refuted: Lake identity confirms cite 407 U.S. 297, year 1972, cluster 108581; cell URL /opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/ matches the record's absolute_u…
- **proposed_fix:** Use United States v. United States District Court for the Eastern District of Michigan (Keith), 407 U.S. 297 (1972), or otherwise make clear that Keith is a nickname.

