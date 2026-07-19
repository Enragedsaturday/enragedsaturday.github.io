# S9 R1 panel-review — Opus model-diversity lane (prompt pack)

You are the **Claude/Opus** leg of the S9 three-lane adversarial panel (1 Claude + 2 Codex, R1). The two Codex lanes carry the A (support/quote-fidelity) and B (currency/treatment) attack lenses; **you carry model diversity and MUST vote on every paneled assertion across BOTH lenses' concerns.** You are refute-framed: try hard to break each assertion; **default to REFUTED on uncertainty**; never fabricate a cite, quote, or holding; use ONLY the evidence inlined below (no search, no outside knowledge). You are a SIGHTED reviewer — the FULL lake record (judgment fields included) is inlined.

You are a WRITER lane, not an adjudicator: you FIND and VOTE. You do not tally, adjudicate, or close any row — the orchestrator does.

For EACH group below, return one JSON object with the exact `reviewed[]` shape from the output contract (identical framing to the Codex lenses). Emit a finding object ONLY for a real defect (verdict refuted / stands-modified); a group you find wholly clean returns all-`stands` verdicts (the harness records a clean attestation). Concatenate the per-group JSON objects into a top-level `{"packs": [ ... ]}` array, one entry per group, each carrying its `group_id`.


OUTPUT CONTRACT — return ONE JSON object, nothing else:
{
  "lens": "A" | "B",
  "group_id": "<echo the group id>",
  "reviewed": [
    {
      "assertion_id": "<from group_inventory.jsonl>",
      "dimension": "existence|support|quote_fidelity|pincite|treatment|black_letter",
      "verdict": "stands" | "refuted" | "stands-modified",
      "verifiable_from_disclosed": true | false,
      "defect": null,   // null when verdict=="stands"; else an object:
      //  {"problem": "...", "severity": "high|medium|low", "proposed_fix": "...", "evidence_quote": "verbatim from disclosed evidence or null", "needs_cl": true|false, "locator_note": "..."}
      "reasons": ["short evidence-grounded reason", "..."],
      "breaks_true_positives": true | false,
      "residual_risks": ["..."],
      "suggested_tightening": "... or null"
    }
  ],
  "notes": ""
}
Rules: verdict=='stands' <=> defect==null (assertion survives your attack). verdict=='refuted' <=> a real defect (the assertion as framed is wrong). verdict=='stands-modified' <=> survives but needs a stated modification (a minor defect). Review EVERY assertion_id in group_inventory.jsonl exactly once. Output ONLY the JSON object.
---

## GROUP: content/cases/United States v. Lyle.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Lyle
type: case
citation: "919 F.3d 716 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 2d Cir.
court_level: coa
circuit: ca2
year: 2019
date_decided: 2019-04-01
docket: 15-958
authority_weight: "Binding in-circuit — 2d Cir."
treatment:
  field_i_validity: unverified
  as_of_content: null
  as_of_treatment: null
  composite_basis: unverified
  composite_basis_ref: null
  varies_by_point: false
  scope_note: "Frontier stub: treatment/progeny intentionally not derived until S6 promotion."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/8443943/united-states-v-lyle/"
  cluster_id: 8443943
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Lyle
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: Key
related:
  - "[[Standing to Challenge a Search]]"
  - "[[Byrd v. United States]]"
  - "[[Rakas v. Illinois]]"
  - "[[Abandonment]]"
tags:
  - case
  - fourth-amendment
  - standing
  - reasonable-expectation-of-privacy
  - rental-car
  - byrd
  - inventory-search
  - second-circuit
holding: "On remand from the Supreme Court in light of Byrd v. United States, the Second Circuit reaffirmed that Lyle lacked standing to challenge the inventory search of a rental car, holding that he had no reasonable expectation of privacy in it because he was not merely an unauthorized driver but an unlicensed one — his possession was both unauthorized and unlawful — so Byrd, which protects an unauthorized driver in lawful possession, did not require a different result; convictions affirmed."
---

# United States v. Lyle

*919 F.3d 716 (2d Cir. 2019)* (No. 15-958) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 8443943 → majority opinion 8415374 (919 F.3d 716, decided 2019-04-01, Chin, J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
James Lyle and Michael Van Praagh were convicted in the Southern District of New York of offenses relating to methamphetamine distribution. On December 11, 2013, NYPD officers saw Lyle park and exit a car in midtown Manhattan, noticed an illegal gravity knife clipped to his pants, confirmed that his driver's license was suspended, and determined that the car was a rental for which he was not an authorized driver (Lyle said his girlfriend had rented it and let him drive). The officers arrested Lyle for driving on a suspended license and possessing the knife, impounded the car, and at the precinct conducted an inventory search that turned up over a pound of methamphetamine and roughly $39,000 in the trunk. The district court denied Lyle's motion to suppress. On his first appeal the Second Circuit affirmed; the Supreme Court then granted [[Reading and Citing Cases#certiorari-cert|certiorari]], [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]] for reconsideration in light of *[[Byrd v. United States|Byrd v. United States]]*, 138 S. Ct. 1518 (2018).

## Issue
Whether Lyle had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] — and thus standing — to challenge the inventory search of a rental car he was driving without authorization and on a suspended license, given *[[Byrd v. United States|Byrd]]*'s holding that an unauthorized driver in lawful possession of a rental car may nonetheless retain a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Rule
*[[Byrd v. United States|Byrd]]* held that the "mere fact that a driver in lawful possession or control of a rental car is not listed on the rental agreement will not defeat his or her otherwise reasonable expectation of privacy" — but its protection is confined to **lawful** possession. Where the driver is not only unauthorized but also unlicensed, his possession is unlawful and he retains no legitimate privacy interest: "we concluded, and now reaffirm, that Lyle lacked standing not just because he was an unauthorized driver, but because he was an unlicensed one. Accordingly, Lyle's use of the rental car was both unauthorized *and* unlawful." — 919 F.3d at 729. ^pin-729

## Application
Lyle was not merely off the rental agreement: his license was suspended, so under N.Y. Vehicle & Traffic Law § 511 he could not lawfully operate any car, and a rental company aware of the facts certainly would not have permitted him to drive its car. His possession was therefore both unauthorized and unlawful — unlike the driver in *[[Byrd v. United States|Byrd]]*, who could have lawful possession and control and the attendant right to exclude. Because Lyle lacked a legitimate expectation of privacy, he had no [[Standing to Challenge a Search|standing to challenge]] the search, and the district court properly denied suppression. The court added, in the alternative, that the impoundment and inventory search were independently reasonable.

## Conclusion
**Affirmed.** Judge Chin wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Lyle* is the Second Circuit's post-*[[Byrd v. United States|Byrd]]* marker on **standing / [[Reasonable Expectation of Privacy|reasonable expectation of privacy]]** in a rental car: *[[Byrd v. United States|Byrd]]* rejected a *[[Common Legal Terms#per-se|per se]]* no-privacy rule for unauthorized drivers, but it protects only those in **lawful** possession — a driver who is both unlisted on the rental agreement and unlicensed falls outside its shelter and lacks standing. Pair it with *[[Byrd v. United States|Byrd]]* and *[[Rakas v. Illinois|Rakas]]* on the possession-and-right-to-exclude basis for [[Standing to Challenge a Search|Fourth Amendment standing]].

## Appears on
- [[Standing to Challenge a Search]] — *Key*

## Sources
- [*United States v. Lyle*, 919 F.3d 716 (2d Cir. 2019)](https://www.courtlistener.com/opinion/8443943/united-states-v-lyle/) — pinpoint: 729 (no-reasonable-expectation-of-privacy / *Byrd*-does-not-help holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5db35d601835b1f2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "919 F.3d 716 (2019)", "court": "2d Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Lyle", "year": "2019"}}
{"assertion_id": "23231a784d9d4380", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key", "title": "United States v. Lyle"}}
{"assertion_id": "61fadf7b68f54369", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "On remand from the Supreme Court in light of Byrd v. United States, the Second Circuit reaffirmed that Lyle lacked standing to challenge the inventory search of a rental car, holding that he had no reasonable expectation of privacy in it because he was not merely an unauthorized driver but an unlicensed one — his possession was both unauthorized and unlawful — so Byrd, which protects an unauthorized driver in lawful possession, did not require a different result; convictions affirmed.", "title": "United States v. Lyle"}}
{"assertion_id": "02e183798e1dae7f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Lyle", "varies_by_point": "false"}}
{"assertion_id": "fe9db41ffb8c1dae", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 2d Cir.", "title": "United States v. Lyle"}}
```

### lake record — United States v. Lyle

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lyle",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Lyle",
    "case_name_short": "Lyle",
    "case_name_full": "United States v. James LYLE, aka Sealed 3, Michael Van Praagh, aka Sealed 1, Anthony Tarantino, aka Sealed 2",
    "input_case_name": "United States v. Lyle",
    "court": "2d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "2019-04-01",
    "year": 2019,
    "docket": "15-958",
    "cluster_id": 8443943,
    "lead_opinion_id": 8415374,
    "sibling_ids": [],
    "absolute_url": "/opinion/8443943/united-states-v-lyle/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "919 F.3d 716",
      "volume": "919",
      "reporter": "F.3d",
      "page": "716",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "919 F.3d 716",
        "volume": "919",
        "reporter": "F.3d",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "919 F.3d 716",
    "official_selection": {
      "court_class": "coa",
      "selected": "919 F.3d 716",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [],
  "treatment": {
    "field_i_validity": "unverified",
    "as_of_content": null,
    "as_of_treatment": null,
    "composite_basis": "unverified",
    "composite_basis_ref": null,
    "varies_by_point": false,
    "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.",
    "point_overrides": [],
    "edges": [],
    "derivation": {}
  },
  "progeny": {
    "complete_query": null,
    "indexed_citing_opinions": null,
    "count_source": null,
    "per_sibling": [],
    "citation_count": null,
    "cache_path": null,
    "enumeration": null,
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": null,
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-07T18:16:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-lyle--8443943",
      "to_record_id": "United States v. Lyle",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Lyle

```
<opinion type="majority">
<author id="p-10">Chin, Circuit Judge:</author>
<p id="p-11"><a class="page-label" data-citation-index="1" data-label="722" href="#p722" id="p722">*722</a>Defendants-appellants James Lyle and Michael Van Praagh appeal from judgments of the United States District Court for the Southern District of New York (Crotty, <em>J.</em> ) convicting them on charges relating to the distribution of methamphetamine. Lyle challenges the admission at trial of evidence seized during a December 11, 2013 inventory search of a rental car and a January 9, 2014 search of his hotel room. He also challenges the admission at trial of certain post-arrest and proffer statements. Van Praagh challenges the sufficiency of the evidence of his participation in a methamphetamine distribution conspiracy, the admission of Lyle's post-arrest and proffer statements in their joint trial, and the reasonableness of his sentence. Because we conclude that the evidence at trial was sufficient to support all convictions, the challenged searches and seizures did not violate the Fourth Amendment, the admission of Lyle's statements did not violate the Fifth Amendment, and Van Praagh's sentence was reasonable, we affirm the judgments of the district court.</p>
<p id="p-12"><strong><em>BACKGROUND</em></strong></p>
<p id="p-13"><strong>I. <em>The Facts</em></strong></p>
<p id="p-14">Because Van Praagh and Lyle appeal convictions following a jury trial, we view the evidence in "the light most favorable to the government, crediting any inferences that the jury might have drawn in its favor." <em>United States v. Rosemond</em> , <extracted-citation case-ids="12173717" index="0" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d 95</a></span></extracted-citation>, 99-100 (2d Cir. 2016) (quoting <em>United States v. Dhinsa</em> , <extracted-citation case-ids="11124472" index="1" url="https://cite.case.law/f3d/243/635/#p643"><span class="citation" data-id="9843214"><a href="/opinion/772486/united-states-v-gurmeet-singh-dhinsa/" aria-description="Citation for case: United States v. Gurmeet Singh Dhinsa">243 F.3d 635</a></span></extracted-citation>, 643 (2d Cir. 2001) ).</p>
<p id="p-15"><strong><em>A. Overview</em></strong></p>
<p id="p-16">Throughout 2013, Van Praagh regularly sold pound quantities of methamphetamine. These deals generally occurred once a week and often took place in Manhattan hotels. Van Praagh also sold smaller quantities of methamphetamine out of his apartment in Queens and through in-person deliveries to his customers. Brandon Hodges, an Arizona-based methamphetamine supplier, sent Van Praagh methamphetamine on three or four occasions during this time, with the largest shipment containing four ounces of methamphetamine. Van Praagh regularly sold methamphetamine to Lyle, who was also a methamphetamine dealer in the New York area. Lyle regularly sold methamphetamine to Anthony Tarantino. Tarantino initially purchased methamphetamine for personal use, but eventually started selling small quantities of methamphetamine to his own clients. Both Hodges and Tarantino cooperated with the government and testified at trial.</p>
<p id="p-17">In January 2013, Lyle introduced Tarantino to Van Praagh. Tarantino accompanied Lyle to Van Praagh's apartment so that Lyle could restock his methamphetamine supply. While at Van Praagh's apartment, Tarantino saw Lyle purchase methamphetamine from Van Praagh, which Lyle later sold to Tarantino. In April 2013, Lyle took Tarantino to Van <a class="page-label" data-citation-index="1" data-label="723" href="#p723" id="p723">*723</a>Praagh's apartment a second time, where Tarantino again observed Lyle "re-up," <em>i.e.</em> , purchase methamphetamine, from Van Praagh. After this second visit, Tarantino and Van Praagh became romantically involved, and eventually Tarantino moved in with Van Praagh and began helping him sell methamphetamine.</p>
<p id="p-18"><strong><em>B. The Seizure of Methamphetamine from Van Praagh's Hotel Room</em></strong></p>
<p id="p-19">On May 29, 2013, Van Praagh and Tarantino checked into the Out Hotel in midtown Manhattan. That night, they sold pound quantities of methamphetamine to several customers, including Lyle. The next day, they checked out of the hotel but accidentally left approximately a pound of methamphetamine and $20,000 cash in the hotel room safe. Hotel staff found the drugs and money and called the New York City Police Department ("NYPD"), and officers arrived to seize the drugs and cash. After Van Praagh realized his mistake later that day, he returned to the hotel, where he was arrested by the NYPD. During the arrest, the officers seized a cellular phone and over $1,000 cash from Van Praagh's pocket. The officers also searched Van Praagh's Vespa scooter parked outside the hotel, where they found part of and packaging for a digital scale.</p>
<p id="p-20">Soon thereafter, Tarantino brought Lyle money to give to Van Praagh's father to bail Van Praagh out of jail. The day after Van Praagh got out of jail, he and Tarantino flew to Arizona to ensure that Van Praagh's methamphetamine suppliers would continue to sell to him. Van Praagh and Tarantino returned to New York and continued their sale of methamphetamine.</p>
<p id="p-21"><strong><em>C. Lyle's Arrests</em></strong></p>
<p id="p-22">On December 11, 2013, NYPD officers observed Lyle park and exit a car in midtown Manhattan. The officers noticed a knife clipped to Lyle's pants, which they later determined to be an illegal gravity knife. The officers approached Lyle as he was closing the trunk of the car. Lyle told the officers that he was legally permitted to carry a gravity knife because he was a member of the stagehands union and used the knife to perform his job. Lyle initially said he had not driven the car but when the officers informed him that they had seen him driving it, Lyle admitted as much. When asked for identification, Lyle produced a New York State ID with the expiration date scratched off. The officers confirmed that Lyle's driver's license was suspended. The officers also determined that the vehicle Lyle was driving was a rental car and that Lyle was not an authorized driver under the rental agreement. Lyle claimed that his girlfriend had rented the car and had given him permission to drive it. The officers arrested Lyle for driving with a suspended license and for possessing an illegal knife.</p>
<p id="p-23">Before heading to the station for processing, Lyle asked if the car could be left at the location and stated that his girlfriend would pick it up. The officers denied the request and impounded the vehicle. At the police precinct, an inventory search was conducted. Over one pound of methamphetamine and approximately $39,000 cash were found in the trunk of the car.</p>
<p id="p-24">The following day-December 12, 2013-Lyle was brought to the District Attorney's Office where he made certain statements in custody after being read his <em>Miranda</em> rights. When asked about the methamphetamine that was in the trunk of the rental car, Lyle stated that "an individual ... had contacted him and asked him to hold something for him." Tr. 435.<footnotemark>1</footnotemark> He <a class="page-label" data-citation-index="1" data-label="724" href="#p724" id="p724">*724</a>stated that upon meeting with that individual and another individual, he stayed in the car and did not see what was placed in the trunk but presumed it to be drugs because the individual that he was meeting with was known to distribute large quantities of methamphetamine in the New York area. When asked about his relationship with these two individuals, Lyle stated that he was friends with them, and had eventually begun working with one of them in delivering methamphetamine to the individual's customers.</p>
<p id="p-25">Lyle stated that the person in charge had a source of supply in Arizona named either Brendan or Brandon. Lyle also "provided a few names" of other people in the New York area who distributed large quantities of methamphetamine. Tr. 436.</p>
<p id="p-26">On January 9, 2014, police in East Windsor, New Jersey responded to an anonymous call that people were using methamphetamine in a hotel room. When they got to the hotel room, Lyle opened the door and invited the officers inside. The officers heard the toilet flush and saw Lyle's girlfriend come out of the bathroom. The officers observed a torch lighter on the bathroom shelf, a small clear bag next to the trash can, and a partial clear straw wrapper containing white residue on the bathroom floor. Additionally, they observed a towel under the bathroom doorway. In the bedroom, the officers noticed that a clear bag had been affixed to the smoke detector with rubber bands.</p>
<p id="p-27">Officers then performed a consent search of the room, and found approximately fourteen grams of methamphetamine, $3,270 cash, a digital scale, and numerous plastic baggies. Lyle and his girlfriend were both arrested.</p>
<p id="p-28"><strong>II. <em>The Proceedings Below</em></strong></p>
<p id="p-29"><strong><em>A. The Indictment and Van Praagh's Arrest</em></strong></p>
<p id="p-30">Van Praagh, Lyle, and Tarantino were indicted on March 20, 2014. On March 31, 2014, Drug Enforcement Administration ("DEA") agents arrested Van Praagh at his apartment. After receiving consent to search the apartment, agents found tools used to sell drugs, including a heat-sealer, packaging materials, and multiple scales, and a note from Hodges asking Van Praagh to have Lyle call him.</p>
<p id="p-31">On April 6, 2013, Van Praagh called his father from jail and told him, in a recorded call, "they got nothing.... I sterilized the house like I told you." Supp. App. 104. He also told him, "[t]hey got Anthony [Tarantino], but I'm expecting that he'll be disappearing any day now.... I believe that he had been talking." Supp. App. 105.</p>
<p id="p-32"><strong><em>B. Lyle's Proffer Session</em></strong></p>
<p id="p-33">On April 7, 2014, Lyle participated in a proffer session with the government in hope of reaching a cooperation agreement. A proffer agreement was executed, stipulating that the government would not use any of Lyle's statements made during the proffer sessions against him, except "to rebut any evidence or arguments offered by or on behalf of [Lyle]." Lyle App. 36.</p>
<p id="p-34">During the proffer session, Lyle admitted that (1) around 2011 or 2012, he sometimes stayed with Van Praagh while working on projects in New York City; (2) he observed Van Praagh smoking and using methamphetamine; (3) he occasionally delivered packages to Van Praagh's clients; (4) he accompanied Van Praagh to deliver methamphetamine thirty to fifty times; (5) Van Praagh told Lyle his supplier was in <a class="page-label" data-citation-index="1" data-label="725" href="#p725" id="p725">*725</a>Arizona; and (6) on one occasion, Lyle accompanied Van Praagh to pick up methamphetamine from a library in New York City.</p>
<p id="p-35"><strong><em>C. The Superseding Indictment and Pretrial Motions</em></strong></p>
<p id="p-36">A superseding indictment was filed September 30, 2014, charging (1) Van Praagh and Lyle with conspiring to distribute 500 grams or more of methamphetamine, in violation of <extracted-citation index="2" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20846"><span class="citation no-link">21 U.S.C. §§ 846</span></extracted-citation> and 841(b)(1)(A), from December 2012 to January 2014; (2) Van Praagh with distributing and possessing with intent to distribute 50 grams or more of methamphetamine, in violation of <extracted-citation index="3" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. §§ 841</span></extracted-citation>(a)(1) and 841(b)(1)(B), on or about May 30, 2013; and (3) Lyle with distributing and possessing with intent to distribute 50 grams or more of methamphetamine, in violation of <extracted-citation index="4" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. §§ 841</span></extracted-citation>(a)(1) and 841(b)(1)(B), on or about December 11, 2013.</p>
<p id="p-37">Before trial, Lyle moved to suppress the physical evidence recovered from the search of the automobile, as well as his subsequent post-arrest statements. In an affidavit filed in support of the motion, Lyle admitted that (1) just prior to his arrest, he had been driving the car that had been rented by his girlfriend with her permission; (2) he possessed a gravity knife that day; (3) he initially told the police officers he had not been driving the car but later admitted to driving the car; and (4) his license was suspended at the time.</p>
<p id="p-38">On September 11, 2014, the district court held an evidentiary hearing on the voluntariness of Lyle's post-arrest statements and, on October 1, 2014, the court denied Lyle's motion to suppress. The court found there was probable cause for Lyle's arrest, based on his possession of a gravity knife. The court then concluded that the search of the rental car was justified on two independent bases. First, Lyle had no reasonable expectation of privacy in the rental car because he was not an authorized driver under the rental agreement. Second, the search of the rental car was a valid inventory search. The court also found that Lyle's post-arrest statements were made voluntarily and pursuant to a valid <em>Miranda</em> waiver.</p>
<p id="p-39"><strong><em>D. The Trial</em></strong></p>
<p id="p-40">Lyle and Van Praagh's trial began on October 14, 2014, and ended on October 20, 2014. The government called nineteen witnesses, and introduced physical evidence consisting of drugs and drug processing materials, text messages between the defendants, testimony regarding Lyle's post-arrest and proffer statements, and the recorded call Van Praagh made to his father while incarcerated. Van Praagh called one witness who testified about the circumstances of Van Praagh's March 31, 2014 arrest. Lyle did not put on a case.</p>
<p id="p-41">During his opening statement, Lyle's counsel stated that "[Lyle] obtained, bought, borrowed, was given methamphetamine for his own use. Where we dispute is the idea that he was a dealer." Tr. 28. Later that day, the government submitted a letter brief, asserting that Lyle's counsel's argument that Lyle was not a dealer opened the door to Lyle's proffer statements about distributing drugs with Van Praagh.</p>
<p id="p-42">Lyle's statements to law enforcement were admitted in two contexts. First, the district court allowed testimony regarding Lyle's December 12, 2013 post-arrest statements to law enforcement to be admitted only as against him, prohibiting mention of Van Praagh. Van Praagh did not object to the redacted testimony. Government witnesses testified that Lyle admitted that an "individual" for whom he worked as a "runner" "asked him to hold something for him" in the trunk of the <a class="page-label" data-citation-index="1" data-label="726" href="#p726" id="p726">*726</a>rental car, which Lyle "presumed ... to be drugs" because Lyle knew "[t]hat individual along with another individual" distributed "large quantities of crystal meth in the New York area." Tr. 435, 534. Lyle was friends "[m]ore so with the individual that had not placed the drugs in the trunk.... He said that he began as friends, and eventually he began working with that individual"-the "individual who was in charge"-"assisting him in delivering ... methamphetamine to that individual's customers." Tr. 435-36. Lyle told law enforcement that the individuals for whom he was working as a runner had a source of supply in Arizona named either Brendan or Brandon. Lyle also gave law enforcement "a few names" of other people in the New York area who distributed methamphetamine, including the names of three competitor drug dealers. Tr. 436. On cross-examination, Lyle's attorney elicited testimony that, during the post-arrest interview, Lyle "gave names of people during the conversation," one of which was Brandon or Brendan. Tr. 448.</p>
<p id="p-43">Second, toward the close of the government's case, the district court ruled-over Lyle's objection-that Lyle's proffer statements were admissible, but again prohibited mention of Van Praagh. Van Praagh did not object. The government witness then testified that Lyle admitted he had "first become involved in methamphetamine" in 2012 through "someone" he "knew ... from work." Tr. 517-18. Lyle observed "that person ... using and distributing crystal methamphetamine." Tr. 518. Lyle "began distributing small packages" for that person and "accompanying that person on deals as well as picking up crystal methamphetamine." <em><extracted-citation index="5" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">Id.</span></extracted-citation></em> Lyle admitted that "he accompanied this person ... [on] between 30 to 50 occasions. And that at one point they had gone to a library in the New York City area ... to pick up crystal methamphetamine." <em><extracted-citation index="6" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">Id.</span></extracted-citation></em> Lyle said the methamphetamine supplier was in Arizona.</p>
<p id="p-44">On cross-examination, Lyle's attorney elicited from the witness that "[Lyle] actually g[a]ve real names of people" during his proffer session, and provided "some names of people whose last names he didn't know." Tr. 524. These names included "Zaron," "Ted," "Bob," and "Joe." Tr. at 525.</p>
<p id="p-45">At the close of trial, the district court instructed the jury, in pertinent part: "There has been evidence that Mr. Lyle made statements to law enforcement authorities.... I want to let you know that ... Mr. Lyle's statement about his own conduct may not be considered or discussed by you with regard to Mr. Van Praagh." Tr. 713.</p>
<p id="p-46">On October 20, 2014, the jury found the defendants guilty on all counts. On March 25, 2015, the district court sentenced Lyle principally to the statutory mandatory minimum of 120 months' imprisonment and, on April 2, 2015, the district court sentenced Van Praagh principally to 144 months' imprisonment. In imposing a higher sentence on Van Praagh, the district court concluded that "Van Praagh had a higher role, more important role. He dealt in more drugs than did Mr. Lyle." Van Praagh App. 62.</p>
<p id="p-47">These appeals followed. On May 9, 2017, we issued an opinion affirming the district court's judgments. <em>United States v. Lyle</em> , <extracted-citation case-ids="12276679" index="7" url="https://cite.case.law/f3d/856/191/"><span class="citation" data-id="8414644"><a href="/opinion/8443281/united-states-v-lyle/" aria-description="Citation for case: United States v. Lyle">856 F.3d 191</a></span></extracted-citation> (2d Cir. 2017). Lyle petitioned for and was granted certiorari by the Supreme Court. On May 21, 2018, the Supreme Court vacated the judgment and remanded the case for further consideration in light of its intervening decision in <em>Byrd v. United States</em> , --- U.S. ----, <extracted-citation case-ids="12611477" index="8" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. 1518</a></span></extracted-citation>, <extracted-citation case-ids="12611477" index="9" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">200 L.Ed.2d 805</a></span></extracted-citation> (2018), which addressed the issue of the reasonable expectation of privacy of an unauthorized driver of a rental car. On July 6, 2018, the parties submitted letter briefs addressing <em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> 's impact upon this case. For the reasons <a class="page-label" data-citation-index="1" data-label="727" href="#p727" id="p727">*727</a>set forth below, we adhere to our original decision.</p>
<p id="p-48"><strong><em>DISCUSSION</em></strong></p>
<p id="p-49">Six issues are presented: (1) the validity of the warrantless search and seizure of the rental car; (2) the interpretation of Lyle's proffer agreement; (3) the sufficiency of the redactions to Lyle's proffer statements; (4) the admissibility of Lyle's New Jersey arrest; (5) the sufficiency of the conspiracy evidence against Van Praagh; and (6) the reasonableness of Van Praagh's sentence. We address each issue in turn.</p>
<p id="p-50"><strong>I. <em>Warrantless Search of Rental Car</em></strong></p>
<p id="p-51">We review a district court's ruling on a suppression motion for clear error as to factual findings, "giving special deference to findings that are based on determinations of witness credibility," and <em>de novo</em> as to questions of law. <em>United States v. Hussain</em> , <extracted-citation case-ids="4354628" index="10" url="https://cite.case.law/f3d/835/307/#p312"><span class="citation" data-id="8414221"><a href="/opinion/8442908/united-states-v-hussain/" aria-description="Citation for case: United States v. Hussain">835 F.3d 307</a></span></extracted-citation>, 312-13 (2d Cir. 2016) (quoting <em>United States v. Lucky</em> , <extracted-citation case-ids="3660831" index="11" url="https://cite.case.law/f3d/569/101/#p106"><span class="citation" data-id="1238356"><a href="/opinion/1238356/united-states-v-lucky/" aria-description="Citation for case: United States v. Lucky">569 F.3d 101</a></span></extracted-citation>, 106 (2d Cir. 2009) ). We conclude that Lyle's motion was properly denied for two independent reasons: first, Lyle had no reasonable expectation of privacy in the rental car, and, second, the inventory search of the rental car was reasonable.</p>
<p id="p-52"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-53"><strong><em>i. Reasonable Expectation of Privacy in Rental Car</em></strong></p>
<p id="p-54">The Fourth Amendment guarantees citizens the "right ... to be secure in their ... effects, against unreasonable searches and seizures." U.S. Const. amend. IV. To prove that a search violated the Fourth Amendment, "an accused must show that he had a legitimate expectation of privacy in a searched place or item." <em>United States v. Rahme</em> , <extracted-citation case-ids="1689797" index="12" url="https://cite.case.law/f2d/813/31/#p34"><span class="citation" data-id="484266"><a href="/opinion/484266/united-states-v-riad-youssef-rahme/" aria-description="Citation for case: United States v. Riad Youssef Rahme">813 F.2d 31</a></span></extracted-citation>, 34 (2d Cir. 1987) (citing <em>Rawlings v. Kentucky</em> , <extracted-citation case-ids="1787600" index="13" url="https://cite.case.law/us/448/98/#p104"><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98</a></span></extracted-citation>, 104, <extracted-citation case-ids="1787600" index="14" url="https://cite.case.law/us/448/98/#p104"><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">100 S.Ct. 2556</a></span></extracted-citation>, <extracted-citation case-ids="1787600" index="15" url="https://cite.case.law/us/448/98/#p104"><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">65 L.Ed.2d 633</a></span></extracted-citation> (1980) ). The person challenging the search must demonstrate a subjective expectation of privacy in the place searched, and that expectation must be objectively reasonable. <em>United States v. Paulino</em> , <extracted-citation case-ids="1792539" index="16" url="https://cite.case.law/f2d/850/93/#p97"><span class="citation" data-id="9477828"><a href="/opinion/508162/united-states-v-francisco-paulino/" aria-description="Citation for case: United States v. Francisco Paulino">850 F.2d 93</a></span></extracted-citation>, 97 (2d Cir. 1988).</p>
<p id="p-55">When we previously ruled in this case, the question of whether an unauthorized driver has a reasonable expectation of privacy in a rental car divided the various circuit courts, resulting in at least three approaches. <em>See</em> <em>Lyle</em> , <extracted-citation case-ids="12276679" index="17" url="https://cite.case.law/f3d/856/191/"><span class="citation" data-id="8414644"><a href="/opinion/8443281/united-states-v-lyle/#200" aria-description="Citation for case: United States v. Lyle">856 F.3d at 200-01</a></span></extracted-citation> (reviewing circuit split). We did not rule on the question, as we decided the appeal on other grounds, as discussed below.</p>
<p id="p-56">The Supreme Court's recent decision in <em>Byrd v. United States</em> resolved the circuit split, holding that the "mere fact that a driver in lawful possession or control of a rental car is not listed on the rental agreement will not defeat his or her otherwise reasonable expectation of privacy." <extracted-citation case-ids="12611477" index="18" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. at 1531</a></span></extracted-citation>. The Court rejected the government's suggestion of a <em>per se</em> rule that unauthorized drivers "always lack an expectation of privacy in the automobile based on the rental company's lack of authorization alone." <em><extracted-citation case-ids="12611477" index="19" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12611477" index="19" url="https://cite.case.law/s-ct/138/1518/"> at 1527</extracted-citation>. Drawing from property principles, the Supreme Court reasoned that "[o]ne of the main rights attaching to property is the right to exclude others, and, in the main, one who owns or lawfully possesses or controls property will in all likelihood have a legitimate expectation of privacy by virtue of the right to exclude." <em><extracted-citation case-ids="12611477" index="20" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12611477" index="20" url="https://cite.case.law/s-ct/138/1518/"> at 1527</extracted-citation> (quoting <em>Rakas v. Illinois</em> , <extracted-citation case-ids="11329017" index="21" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span></extracted-citation>, 144 n. 12, <extracted-citation case-ids="11329017" index="22" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span></extracted-citation>, <extracted-citation case-ids="11329017" index="23" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span></extracted-citation> (1978) (internal quotation marks omitted)). It further noted, however, that the concept of lawful possession is central to the expectation of privacy inquiry, for a " 'wrongful' presence at the scene of a search would not enable a defendant to object to the legality of the search." <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Id.</a></span></em> at 1529 (quoting <em>Rakas</em> , <extracted-citation case-ids="11329017" index="24" url="https://cite.case.law/us/439/128/">439 U.S. at </extracted-citation>141 n. 9, <extracted-citation case-ids="11329017" index="25" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span></extracted-citation> ). Thus, "a person present in a stolen automobile at the time of the search may [not] object to the lawfulness of the search of the automobile"</p>
<p id="p-57"><a class="page-label" data-citation-index="1" data-label="728" href="#p728" id="p728">*728</a>regardless of his level of possession and control over the automobile. <em>See</em> <em>id</em> .</p>
<p id="p-58"><strong><em>ii. Community Caretaking Function</em></strong></p>
<p id="p-59">It is well established that police have the authority, despite the absence of a warrant, to seize and remove from the streets automobiles in the interests of public safety and as part of their community caretaking functions-an authority that is beyond reasonable challenge. <em>South Dakota v. Opperman</em> , <extracted-citation case-ids="6177992" index="26" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. 364</a></span></extracted-citation>, 368-69, <extracted-citation case-ids="6177992" index="27" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">96 S.Ct. 3092</a></span></extracted-citation>, <extracted-citation case-ids="6177992" index="28" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">49 L.Ed.2d 1000</a></span></extracted-citation> (1976). In <em>Colorado v. Bertine</em> , the Supreme Court explained that, under this community caretaking exception to the warrant requirement, police officers may exercise their discretion in deciding whether to impound a vehicle, "so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity." <extracted-citation case-ids="6216740" index="29" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U.S. 367</a></span></extracted-citation>, 375, <extracted-citation case-ids="6216740" index="30" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">107 S.Ct. 738</a></span></extracted-citation>, <extracted-citation case-ids="6216740" index="31" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">93 L.Ed.2d 739</a></span></extracted-citation> (1987). The question of whether <em>Bertine</em> and similar Supreme Court precedent require an officer's decision to impound a car to be made pursuant to standardized criteria, a question we have not addressed, has created a split among the circuits.</p>
<p id="p-60">Relying on a stricter interpretation of <em>Bertine</em> , two circuits have concluded that an officer's decision to impound a vehicle as part of its role as a community caretaker must be guided by a standardized procedure. <em>See</em> <em>United States v. Petty</em> , <extracted-citation case-ids="9249130" index="32" url="https://cite.case.law/f3d/367/1009/#p1012"><span class="citation" data-id="786133"><a href="/opinion/786133/united-states-v-jerry-l-petty/" aria-description="Citation for case: United States v. Jerry L. Petty">367 F.3d 1009</a></span></extracted-citation>, 1012 (8th Cir. 2004) (holding that "[s]ome degree of standardized criteria or established routine must regulate these police actions ... to ensure that impoundments and inventory searches are not merely a ruse for general rummaging in order to discover incriminating evidence" (internal quotation marks omitted)); <em>United States v. Duguay</em> , <extracted-citation case-ids="7630921" index="33" url="https://cite.case.law/f3d/93/346/#p351"><span class="citation" data-id="9489468"><a href="/opinion/724910/united-states-v-christopher-duguay/" aria-description="Citation for case: United States v. Christopher Duguay">93 F.3d 346</a></span></extracted-citation>, 351 (7th Cir. 1996) ("Among those criteria which must be standardized are the circumstances in which a car may be impounded."). Taking a slightly different approach, the D.C. Circuit has held that "if a standard impoundment procedure exists, a police officer's failure to adhere thereto is unreasonable and violates the Fourth Amendment." <em>United States v. Proctor</em> , <extracted-citation case-ids="3484762,3563372" index="34" url="https://cite.case.law/f3d/489/1348/"><span class="citation" data-id="186948"><a href="/opinion/186948/united-states-v-proctor-douglas/" aria-description="Citation for case: United States v. Proctor, Douglas">489 F.3d 1348</a></span></extracted-citation>, 1354 (D.C. Cir. 2007). The Tenth Circuit has held that standardized procedures are not required where an officer exercises "the community-caretaking functions of protecting public safety and promoting the efficient movement of traffic," but are required in other cases. <em>United States v. Sanders</em> , <extracted-citation case-ids="5767964" index="35" url="https://cite.case.law/f3d/796/1241/#p1245"><span class="citation" data-id="8413595"><a href="/opinion/8442347/united-states-v-sanders/" aria-description="Citation for case: United States v. Sanders">796 F.3d 1241</a></span></extracted-citation>, 1245 (10th Cir. 2015).</p>
<p id="p-61">The First, Third, and Fifth Circuits, however, have rejected the standardized criteria requirement, and instead focus their inquiry on the reasonableness of the impoundment under the circumstances. <em>See</em> <em>United States v. McKinnon</em> , <extracted-citation case-ids="3885876" index="36" url="https://cite.case.law/f3d/681/203/#p208"><span class="citation" data-id="2310827"><a href="/opinion/2310827/united-states-v-mckinnon/" aria-description="Citation for case: United States v. McKinnon">681 F.3d 203</a></span></extracted-citation>, 208 (5th Cir. 2012) (per curiam) (hinging analysis upon "the reasonableness of the 'community caretaker' impound viewed in the context of the facts and circumstances encountered by the officer" (citation omitted)); <em>United States v. Smith</em> , <extracted-citation case-ids="3761335" index="37" url="https://cite.case.law/f3d/522/305/#p314"><span class="citation" data-id="1240302"><a href="/opinion/1240302/united-states-v-smith/" aria-description="Citation for case: United States v. Smith">522 F.3d 305</a></span></extracted-citation>, 314 (3d Cir. 2008) (declining to adopt "the more structured approach ... requiring that there be standardized police procedures governing impoundments"); <em>United States v. Coccia</em> , <extracted-citation case-ids="2843114" index="38" url="https://cite.case.law/f3d/446/233/#p239"><span class="citation" data-id="202190"><a href="/opinion/202190/united-states-v-coccia/" aria-description="Citation for case: United States v. Coccia">446 F.3d 233</a></span></extracted-citation>, 239 (1st Cir. 2006) ("[I]mpoundments of vehicles for community caretaking purposes are consonant with the Fourth Amendment so long as the impoundment decision was reasonable under the circumstances."). These circuits read <em>Bertine</em> "to indicate that an impoundment decision made pursuant to standardized procedures will most likely, although not necessarily always, satisfy the Fourth Amendment." <em>Coccia</em> , <extracted-citation case-ids="2843114" index="39" url="https://cite.case.law/f3d/446/233/#p239"><span class="citation" data-id="202190"><a href="/opinion/202190/united-states-v-coccia/" aria-description="Citation for case: United States v. Coccia">446 F.3d at 238</a></span></extracted-citation>.</p>
<p id="p-62"><a class="page-label" data-citation-index="1" data-label="729" href="#p729" id="p729">*729</a><strong><em>B. Application</em></strong></p>
<p id="p-63"><strong><em>i. Reasonable Expectation of Privacy in Rental Car</em></strong></p>
<p id="p-64">In our prior decision, we specifically declined to decide whether an unauthorized driver ever has a reasonable expectation of privacy in a rental car. Instead, we concluded, and now reaffirm, that Lyle lacked standing not just because he was an unauthorized driver, but because he was an unlicensed one. Accordingly, Lyle's use of the rental car was both unauthorized <em>and</em> unlawful. <em>See</em> <extracted-citation index="40" url="https://cite.case.law/citations/?q=N.Y.%20Vehicle%20%26%20Traffic%20Law%20%C2%A7%20511"><span class="citation no-link">N.Y. Vehicle &amp; Traffic Law § 511</span></extracted-citation> (prohibiting operating a car without a valid license). Lyle should not have been driving any car because his license was suspended, and a rental company with knowledge of the relevant facts certainly would not have given him permission to drive its car nor allowed a renter to let him do so. Under these circumstances, Lyle did not have a reasonable expectation of privacy in the rental car. <em>See</em> <em>United States v. Haywood</em> , <extracted-citation case-ids="2160886" index="41" url="https://cite.case.law/f3d/324/514/#p516"><span class="citation" data-id="781422"><a href="/opinion/781422/united-states-v-eugene-haywood/" aria-description="Citation for case: United States v. Eugene Haywood">324 F.3d 514</a></span></extracted-citation>, 516 (7th Cir. 2003) (declining to resolve circuit split over whether unauthorized driver had reasonable expectation of privacy in rental car, because unauthorized driver also had suspended license and the combination resulted in no reasonable expectation of privacy); <em>cf.</em> <em>United States v. Tropiano</em> , <extracted-citation case-ids="7412372" index="42" url="https://cite.case.law/f3d/50/157/#p161"><span class="citation" data-id="691961"><a href="/opinion/691961/united-states-v-daniel-michael-tropiano/" aria-description="Citation for case: United States v. Daniel Michael Tropiano">50 F.3d 157</a></span></extracted-citation>, 161 (2d Cir. 1995) ("[W]e think it obvious that a defendant who knowingly possesses a stolen car has no legitimate expectation of privacy in the car."); <em>United States v. Ponce</em> , <extracted-citation case-ids="10522522" index="43" url="https://cite.case.law/f2d/947/646/#p649"><span class="citation" data-id="570497"><a href="/opinion/570497/united-states-v-gerardo-i-ponce-juan-c-gonzalez-calas-and-hipolito/" aria-description="Citation for case: United States v. Gerardo I. Ponce, Juan C. Gonzalez-Calas...">947 F.2d 646</a></span></extracted-citation>, 649 (2d Cir. 1991) ("To mount a challenge to a search of a vehicle, defendants must show, among other things, a legitimate basis for being in it, such as permission from the owner.").</p>
<p id="p-65"><em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> does not require a different result. The Court there held that an unauthorized driver in sole possession of a rental car could have a legitimate expectation of privacy in the vehicle because even an unauthorized driver, in the right circumstances, could have "lawful possession and control and the attendant right to exclude." <extracted-citation case-ids="12611477" index="44" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. at 1528</a></span></extracted-citation>. The Court noted that "there may be countless innocuous reasons why an unauthorized driver might get behind the wheel of a rental car and drive it-perhaps the renter is drowsy or inebriated." <em><extracted-citation case-ids="12611477" index="45" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12611477" index="45" url="https://cite.case.law/s-ct/138/1518/"> at 1529</extracted-citation>.</p>
<p id="p-66">This reasoning does not apply to the circumstances here, where Lyle was not only the driver of the vehicle but the sole occupant. Because Lyle did not have a valid driver's license, it was unlawful for him to be operating the vehicle. He did not have <em>lawful</em> possession and control of the vehicle in the sense that he unlawfully drove the vehicle onto the scene and could not lawfully drive it away. <em>See <extracted-citation case-<span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">ids="12611477" index="46" url="https://cite.</a></span>case.law/s-ct/138/1518/">id.</extracted-citation></em> (reaffirming conclusion in <em>Rakas v. Illinois</em> that " 'wrongful' presence at the scene of a search would not enable a defendant to object to the legality of the search," "[n]o matter the degree of [a defendant's] possession and control.")<em>.</em> While the absence of a valid license alone may not destroy an unauthorized driver's expectation of privacy, Lyle's possession and control of the car was unlawful the moment he started driving it. Just as a car thief would not have a reasonable expectation of privacy in a stolen car, <em><extracted-citation case-ids="12611477" index="47" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">id.</a></span></extracted-citation></em> , an unauthorized, unlicensed driver in sole possession of a rental car does not have a reasonable expectation of privacy in the vehicle. Therefore, because Lyle's operation of the car rendered his possession and control unlawful, <em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> is distinguishable.</p>
<p id="p-67">Further, unlike the Eighth and Ninth Circuits, which have held that a defendant may have standing to challenge a search of a rental car despite lacking a valid license and authorization under the rental agreement if he received an authorized driver's permission, <em>United States v. Best</em> , <extracted-citation case-ids="11877555" index="48" url="https://cite.case.law/f3d/135/1223/"><span class="citation" data-id="751576"><a href="/opinion/751576/united-states-v-tony-cornelius-best/" aria-description="Citation for case: United States v. Tony Cornelius Best">135 F.3d 1223</a></span></extracted-citation> (8th Cir. 1998) ;</p>
<p id="p-68"><a class="page-label" data-citation-index="1" data-label="730" href="#p730" id="p730">*730</a><em>United States v. Thomas</em> , <extracted-citation case-ids="5860809" index="49" url="https://cite.case.law/f3d/447/1191/"><span class="citation" data-id="794349"><a href="/opinion/794349/united-states-v-roshon-e-thomas-aka-rollin-roy-phillips/" aria-description="Citation for case: United States v. Roshon E. Thomas, AKA Rollin Roy Phillips">447 F.3d 1191</a></span></extracted-citation> (9th Cir. 2006), we conclude that an authorized renter's permission is not determinative of whether a defendant has a reasonable expectation of privacy. Indeed, <em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> explicitly rejected the notion that legitimate presence alone affords a defendant with a reasonable expectation of privacy. <extracted-citation case-ids="12611477" index="50" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. at 1527</a></span></extracted-citation> (quoting <em>Rakas</em> , <extracted-citation case-ids="11329017" index="51" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. at 148</a></span></extracted-citation>, <extracted-citation case-ids="11329017" index="52" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span></extracted-citation> (noting that legitimate presence is relevant, but not controlling)). While a defendant does not lose all his Fourth Amendment rights simply by engaging in illegal acts, he may still lack standing to challenge a search when the law prevents him from being there in the first place, even with the owner's permission. <em>See</em> <em>United States v. Schram</em> , <extracted-citation case-ids="12518285" index="53" url="https://cite.case.law/f3d/901/1042/#p1045"><span class="citation" data-id="4305748"><a href="/opinion/4528495/united-states-v-gerald-schram/" aria-description="Citation for case: United States v. Gerald Schram">901 F.3d 1042</a></span></extracted-citation>, 1045 (9th Cir. 2018) (rejecting argument that defendant had standing to object to the search of his girlfriend's house because the no-contact order prohibiting him from contacting his girlfriend was vitiated by her consent to enter the property). Here, even assuming that, under different circumstances, an unlicensed driver may have an expectation of privacy in a rental car, Lyle's possession and control was unlawful while driving the rental car both without a license and without authorization. <em>Cf.</em> <em>United States v. Walton</em> , <extracted-citation case-ids="4180655" index="54" url="https://cite.case.law/f3d/763/655/#p663"><span class="citation" data-id="2717801"><a href="/opinion/2717801/united-states-v-kenyon-walton/" aria-description="Citation for case: United States v. Kenyon Walton">763 F.3d 655</a></span></extracted-citation>, 663 (7th Cir. 2014) (holding that defendant, who was passenger at time of search and sole authorized driver listed on rental agreement, had reasonable expectation of privacy in rental car despite lacking driver's license because "[a] driver of a car does not lose all Fourth Amendment protections simply because his license is invalid," but observing that conclusion would not obtain if person were both unlicensed and unauthorized).</p>
<p id="p-69">Lyle argues that he was not operating the vehicle when he was arrested and that he lawfully possessed the vehicle. These arguments ignore the fact that Lyle was seen by the agents driving the vehicle, and, indeed, he eventually admitted as much. Because he was driving the vehicle illegally, Lyle did not have <em>lawful</em> possession or control of the vehicle and he does not have standing to challenge the search.</p>
<p id="p-70">Lyle's reliance on the Sixth Circuit's decision in <em>United States v. Smith</em> , <extracted-citation case-ids="9484437" index="55" url="https://cite.case.law/f3d/263/571/#p586"><span class="citation" data-id="774727"><a href="/opinion/774727/united-states-v-steven-eugene-smith-randy-ray-smith/" aria-description="Citation for case: United States v. Steven Eugene Smith, Randy Ray Smith">263 F.3d 571</a></span></extracted-citation>, 586 (6th Cir. 2001), is misplaced. <em>Smith</em> presented unique facts. Specifically, Smith was not only the husband of the renter, but he also "had a business relationship with the rental company" because he had "called the rental company to reserve the rental vehicle," "was given a reservation number," and "provided the company with his credit card number, and that credit card was subsequently billed for the rental of the vehicle." <em><extracted-citation case-ids="9484437" index="56" url="https://cite.case.law/f3d/263/571/#p586">Id.</extracted-citation></em> In light of these facts, the Sixth Circuit determined that "Smith was the <em>de facto</em> renter of the vehicle" and that, therefore, he had a legitimate expectation of privacy in the rental car. <em><extracted-citation case-ids="9484437" index="57" url="https://cite.case.law/f3d/263/571/#p586">Id.</extracted-citation></em><extracted-citation case-ids="9484437" index="57" url="https://cite.case.law/f3d/263/571/#p586"> at 586-87</extracted-citation>. Lyle was not the <em>de facto</em> renter of the car at issue here. Moreover, the Sixth Circuit also noted that Smith was a licensed driver. <em><extracted-citation case-ids="9484437" index="58" url="https://cite.case.law/f3d/263/571/#p586">Id.</extracted-citation></em><extracted-citation case-ids="9484437" index="58" url="https://cite.case.law/f3d/263/571/#p586"> at 586</extracted-citation> ("Smith was a licensed driver .... Therefore, it was not illegal for Smith [to] drive the vehicle."). For these reasons, <em>Smith</em> is distinguishable.</p>
<p id="p-71">Accordingly, we adhere to our original conclusion that Lyle lacked a reasonable expectation of privacy in the rental car, and the district court did not err in denying his motion to suppress.</p>
<p id="p-72"><strong><em>ii. Impoundment of Rental Car</em></strong></p>
<p id="p-73">Even assuming Lyle had a legitimate privacy interest in the rental car, his challenge to the inventory search fails on the merits as the impoundment of the rental car did not violate the Fourth Amendment.<footnotemark>2</footnotemark> The Supreme Court has repeatedly <a class="page-label" data-citation-index="1" data-label="731" href="#p731" id="p731">*731</a>held that the touchstone of the Fourth Amendment is reasonableness, <em>see</em> <em>United States v. Ramirez</em> , <extracted-citation case-ids="11503214" index="59" url="https://cite.case.law/us/523/65/#p71"><span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">523 U.S. 65</a></span></extracted-citation>, 71, <extracted-citation case-ids="11503214" index="60" url="https://cite.case.law/us/523/65/#p71"><span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">118 S.Ct. 992</a></span></extracted-citation>, <extracted-citation case-ids="11503214" index="61" url="https://cite.case.law/us/523/65/#p71"><span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">140 L.Ed.2d 191</a></span></extracted-citation> (1998), which "in turn, is measured in objective terms by examining the totality of the circumstances," <em>Ohio v. Robinette</em> , <extracted-citation case-ids="11594631" index="62" url="https://cite.case.law/us/519/33/#p39"><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33</a></span></extracted-citation>, 39, <extracted-citation case-ids="11594631" index="63" url="https://cite.case.law/us/519/33/#p39"><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">117 S.Ct. 417</a></span></extracted-citation>, <extracted-citation case-ids="11594631" index="64" url="https://cite.case.law/us/519/33/#p39"><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">136 L.Ed.2d 347</a></span></extracted-citation> (1996). Thus, in line with the First, Third, and Fifth Circuits, we conclude that "whether a decision to impound is reasonable under the Fourth Amendment is based on all the facts and circumstances of a given case." <em>Coccia</em> , <extracted-citation case-ids="2843114" index="65" url="https://cite.case.law/f3d/446/233/#p239"><span class="citation" data-id="202190"><a href="/opinion/202190/united-states-v-coccia/" aria-description="Citation for case: United States v. Coccia">446 F.3d at 239</a></span></extracted-citation>. While the existence of and an officer's adherence to a standardized criteria may be helpful in evaluating the reasonableness of an impoundment, we decline to adopt a standardized impoundment procedure requirement.</p>
<p id="p-74">Using a totality of the circumstances analysis, we conclude that the impoundment here was reasonable under the Fourth Amendment even absent standardized procedures. Here, at the time of his arrest for driving with a suspended license and for possessing an illegal knife, Lyle was the rental car's driver and sole occupant. As there was no third party immediately available to entrust with the vehicle's safekeeping, the officers could not be certain how long the rental car would be unattended in Lyle's absence. Even if Lyle did not expect to be in custody long, Lyle would not have been able to operate the car himself upon release due to his suspended license. Although Lyle asked for the opportunity to arrange for his girlfriend, the authorized driver under the rental agreement, to remove the rental car, the police were not required to grant the request. <em>See</em> <em>Bertine</em> , <extracted-citation case-ids="6216740" index="66" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U.S. at 374</a></span>-75</extracted-citation>, <extracted-citation case-ids="6216740" index="67" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">107 S.Ct. 738</a></span></extracted-citation> ; <em>see also</em> <em>Duguay</em> , <extracted-citation case-ids="7630921" index="68" url="https://cite.case.law/f3d/93/346/#p351">93 F.3d at </extracted-citation>353 &amp; n. 2 (holding impoundment of car unconstitutional when the vehicle's other occupant was present at the arrest and could "provide for the speedy and efficient removal of the car from public thoroughfares," but noting that the Seventh Circuit has affirmed impoundments where the arrestee is the vehicle's sole occupant and is legitimately arrested). Instead, by impounding the vehicle, the officer ensured that the rental vehicle was not left on a public street in a busy midtown Manhattan location where it could have become a nuisance or been stolen or damaged and could have become illegally parked the next day. <em>See</em> <em>Opperman</em> , <extracted-citation case-ids="6177992" index="69" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. at 368</a></span>-69</extracted-citation>, <extracted-citation case-ids="6177992" index="70" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">96 S.Ct. 3092</a></span></extracted-citation> (describing as "beyond challenge" the authority of police "to seize and remove from the streets vehicles impeding traffic or threatening public safety and convenience," such as vehicles that "violate parking ordinances"); <em>Sanders</em> , <extracted-citation case-ids="5767964" index="71" url="https://cite.case.law/f3d/796/1241/#p1245"><span class="citation" data-id="8413595"><a href="/opinion/8442347/united-states-v-sanders/#1249" aria-description="Citation for case: United States v. Sanders">796 F.3d at 1249</a></span></extracted-citation> (" <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span></em> establishes that if a vehicle is obstructing or impeding traffic on public property, it can be impounded regardless of whether the impoundment is guided by standardized procedures."). Moreover, there is no indication that the officers did not act in good faith or solely for the purpose of investigation in exercising their discretion to impound the rental car.</p>
<p id="p-75">Our decision in <em>United States v. Lopez</em> , <extracted-citation case-ids="6051917" index="72" url="https://cite.case.law/f3d/547/364/"><span class="citation" data-id="1225666"><a href="/opinion/1225666/united-states-v-lopez/" aria-description="Citation for case: United States v. Lopez">547 F.3d 364</a></span></extracted-citation> (2d Cir. 2008), is instructive. There, although our discussion primarily concerned the constitutionality of the inventory search itself, we concluded that the circumstances called for the impoundment of Lopez's car despite any showing of a standardized impoundment policy. <em><extracted-citation case-ids="6051917" index="73" url="https://cite.case.law/f3d/547/364/"><span class="citation" data-id="1225666"><a href="/opinion/1225666/united-states-v-lopez/" aria-description="Citation for case: United States v. Lopez">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6051917" index="73" url="https://cite.case.law/f3d/547/364/"> at 372</extracted-citation>. Similar to Lyle, Lopez was arrested <a class="page-label" data-citation-index="1" data-label="732" href="#p732" id="p732">*732</a>and there was no one immediately available to move his car for safekeeping in Lopez's case because the only other passenger was also arrested. <em>See</em> <em>id</em> . at 366-67. Moreover, like Lyle's car, Lopez's car was parked on a city street. <em><extracted-citation case-ids="6051917" index="74" url="https://cite.case.law/f3d/547/364/"><span class="citation" data-id="1225666"><a href="/opinion/1225666/united-states-v-lopez/" aria-description="Citation for case: United States v. Lopez">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6051917" index="74" url="https://cite.case.law/f3d/547/364/"> at 366</extracted-citation>.</p>
<p id="p-76">Thus, even if Lyle had a reasonable expectation of privacy in the rental car, the district court did not err in denying his motion to suppress.</p>
<p id="p-77"><strong>II. <em>The Proffer Agreement Waiver</em></strong></p>
<p id="p-78">We review the district court's interpretation of the scope of a proffer agreement waiver <em>de novo</em> and its evidentiary rulings for abuse of discretion. <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="75" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d at 107</a></span></extracted-citation>.</p>
<p id="p-79"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-80">Ordinarily, a "statement made during plea discussions with an attorney for the prosecuting authority" that does not result in a guilty plea is not admissible against the defendant who made the statement. Fed. R. Evid. 410(a)(4). The protections provided by Rule 410, however, can be waived, including in a proffer agreement with the government, provided that such waiver is knowing and voluntary. <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="76" url="https://cite.case.law/f3d/841/95/#p99">841 F.3d at </extracted-citation>107 ; <em>United States v. Velez</em> , <extracted-citation case-ids="9294404" index="77" url="https://cite.case.law/f3d/354/190/#p194"><span class="citation" data-id="784640"><a href="/opinion/784640/united-states-v-jose-velez/" aria-description="Citation for case: UNITED STATES v. JOSÉ VELEZ">354 F.3d 190</a></span></extracted-citation>, 194-95 (2d Cir. 2004).</p>
<p id="p-81">To determine whether a proffer agreement's waiver provision applies, we ask first whether the defendant has offered any evidence or made a factual assertion that would trigger the Rule 410 waiver, and, "if so, whether the proffer statement 'fairly rebut[s]' the fact asserted or evidence offered or elicited." <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="78" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d at 107</a></span></extracted-citation>. If the waiver has been triggered and the proffer statement properly rebuts the assertion triggering the waiver, the government may offer the proffer statement. <em><extracted-citation case-ids="12173717" index="79" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">Id.</a></span></extracted-citation></em></p>
<p id="p-82">In <em><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">Rosemond</a></span></em> , we gave examples of factual assertions that will trigger the proffer waiver, including "asserting, in an opening statement, that someone other than the defendant was the real perpetrator of the crime," <em><extracted-citation case-<span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">ids="12173717" index="80" url="https://cite.</a></span>case.law/f3d/841/95/#p99">id.</extracted-citation></em> at 109 (citing <em>United States v. Barrow</em> , <extracted-citation case-ids="9170857" index="81" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">400 F.3d 109</a></span></extracted-citation>, 114, 119 (2d Cir. 2005) ), and "arguing that a shooting was 'an intended kidnapping gone wrong,' when the defendant admitted in a proffer session that the shooting was 'an intentional murder,' " <em><extracted-citation case-<span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">ids="9170857" index="82" url="https://cite.</a></span>case.law/f3d/400/109/#p114">id.</extracted-citation></em><extracted-citation case-ids="9170857" index="82" url="https://cite.case.law/f3d/400/109/#p114"> at 110</extracted-citation> (quoting <em>United States v. Gomez</em> , <extracted-citation case-ids="9403243" index="83" url="https://cite.case.law/f-supp-2d/210/465/#p472"><span class="citation" data-id="2579550"><a href="/opinion/2579550/united-states-v-gomez/" aria-description="Citation for case: United States v. Gomez">210 F.Supp.2d 465</a></span></extracted-citation>, 472 (S.D.N.Y. 2002) ).</p>
<p id="p-83"><strong><em>B. Application</em></strong></p>
<p id="p-84">The district court properly held that the waiver was triggered by Lyle's counsel's statement during opening argument that "we dispute [ ] the idea that [Lyle] was a dealer." Tr. 28. Lyle's proffer agreement contained a waiver that allowed his statements to come in "to rebut any evidence or arguments offered by or on behalf of [Lyle]." Lyle App. 36.</p>
<p id="p-85">As this Court has recognized, a defense argument does not trigger a waiver if it "simply challenge[s] the sufficiency of government proof on [the] elements." <em>Barrow</em> , <extracted-citation case-ids="9170857" index="84" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">400 F.3d at 119</a></span></extracted-citation>. But "a statement of fact in a defense opening, such as [a] statement ... unequivocally identifying [someone other than defendant] as the real perpetrator of the charged crimes," is a factual assertion that would trigger a waiver provision. <em><extracted-citation case-ids="9170857" index="85" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">Id.</a></span></extracted-citation></em> Here, defense counsel did not ascribe the charged crime to someone else, but he did more than challenge the sufficiency of the government's proof. Rather than argue that the government would not adduce credible evidence that Lyle was a drug dealer, counsel disputed the very idea that Lyle was a dealer. This is the functional equivalent of an affirmative statement that Lyle, in fact, did not deal methamphetamine. This assertion was belied by Lyle's proffer admissions and, thus, triggered <a class="page-label" data-citation-index="1" data-label="733" href="#p733" id="p733">*733</a>the waiver provision in the proffer agreement.</p>
<p id="p-86">Lyle's proffer statements fairly rebut his counsel's opening argument that Lyle was not a dealer. The proffer statements at issue included that (1) Lyle repeatedly distributed "small packages" of methamphetamine; (2) Lyle accompanied another person to obtain and deliver methamphetamine; and (3) Lyle knew the location of the methamphetamine supplier. Taken together, these statements imply participation in a drug distribution operation and thus fairly rebut Lyle's counsel's argument in his opening statement that Lyle was a mere user of methamphetamine and not a dealer. <em>See</em> <em>Barrow</em> , <extracted-citation case-ids="9170857" index="86" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/#120" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">400 F.3d at 120-21</a></span></extracted-citation> (emphasizing that "proper rebuttal is not limited to direct contradiction" but "encompasses any evidence that the trial judge concludes fairly counters and casts doubt on the truthfulness of factual assertions advanced, whether directly or implicitly, by an adversary").</p>
<p id="p-87">Hence, we conclude that the district court did not abuse its discretion in admitting Lyle's proffer statements.</p>
<p id="p-88"><strong>III. <em>The Admission of Lyle's Redacted Statements</em></strong></p>
<p id="p-89"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-90">In <em>Bruton v. United States</em> , <extracted-citation case-ids="1767670" index="87" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U.S. 123</a></span></extracted-citation>, 135-36, <extracted-citation case-ids="1767670" index="88" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">88 S.Ct. 1620</a></span></extracted-citation>, <extracted-citation case-ids="1767670" index="89" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">20 L.Ed.2d 476</a></span></extracted-citation> (1968), the Supreme Court held that admission of a non-testifying co-defendant's confession naming the defendant as a perpetrator at their joint trial violates the latter's Sixth Amendment right to cross-examination. The Court later made clear that a non-obvious redaction of a co-defendant's confession to eliminate any references to the defendant will eliminate any <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> problem. <em>See</em> <em>Gray v. Maryland</em> , <extracted-citation case-ids="11503401" index="90" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">523 U.S. 185</a></span></extracted-citation>, 195-97, <extracted-citation case-ids="11503401" index="91" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">118 S.Ct. 1151</a></span></extracted-citation>, <extracted-citation case-ids="11503401" index="92" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">140 L.Ed.2d 294</a></span></extracted-citation> (1998) ; <em>Richardson v. Marsh</em> , <extracted-citation case-ids="6212712" index="93" url="https://cite.case.law/us/481/200/#p208"><span class="citation" data-id="9430922"><a href="/opinion/111865/richardson-v-marsh/" aria-description="Citation for case: Richardson v. Marsh">481 U.S. 200</a></span></extracted-citation>, 208-09, <extracted-citation case-ids="6212712" index="94" url="https://cite.case.law/us/481/200/#p208"><span class="citation" data-id="9430922"><a href="/opinion/111865/richardson-v-marsh/" aria-description="Citation for case: Richardson v. Marsh">107 S.Ct. 1702</a></span></extracted-citation>, <extracted-citation case-ids="6212712" index="95" url="https://cite.case.law/us/481/200/#p208"><span class="citation" data-id="9430922"><a href="/opinion/111865/richardson-v-marsh/" aria-description="Citation for case: Richardson v. Marsh">95 L.Ed.2d 176</a></span></extracted-citation> (1987).</p>
<p id="p-91">We have consistently held that the introduction of a co-defendant's confession with the defendant's name replaced by a neutral noun or pronoun does not violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . <em>See, e.g.</em> , <em>United States v. Jass</em> , <extracted-citation case-ids="3660376" index="96" url="https://cite.case.law/f3d/569/47/#p58"><span class="citation" data-id="2507"><a href="/opinion/2507/united-states-v-jass/" aria-description="Citation for case: United States v. Jass">569 F.3d 47</a></span></extracted-citation>, 58 (2d Cir. 2009) (noting that operative questions when evaluating <em>Bruton</em> claim are "(1) did the redacted statement give any indication to the jury that the original statement contained actual names, and (2) did the statement standing alone otherwise connect co-defendants to the crimes" (internal quotation marks and ellipsis omitted)). In <em>United States v. Tutino</em> , <extracted-citation case-ids="10535824" index="97" url="https://cite.case.law/f2d/883/1125/"><span class="citation" data-id="8972330"><a href="/opinion/8980459/united-states-v-tutino/" aria-description="Citation for case: United States v. Tutino">883 F.2d 1125</a></span></extracted-citation> (2d Cir. 1989), for example, we affirmed a conviction based in part on a co-defendant's statement that was redacted to reference "others," "other people," and "another person." <em><extracted-citation case-ids="10535824" index="98" url="https://cite.case.law/f2d/883/1125/"><span class="citation" data-id="8972330"><a href="/opinion/8980459/united-states-v-tutino/" aria-description="Citation for case: United States v. Tutino">Id.</a></span></extracted-citation></em><extracted-citation case-ids="10535824" index="98" url="https://cite.case.law/f2d/883/1125/"> at 1135</extracted-citation>.</p>
<p id="p-92">To determine whether a redaction is sufficient under <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> , we view the redacted statement separate and apart from any other evidence admitted at trial. <em><extracted-citation case-ids="10535824" index="99" url="https://cite.case.law/f2d/883/1125/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> (citing <em>United States v. Wilkinson</em> , <extracted-citation case-ids="287351" index="100" url="https://cite.case.law/f2d/754/1427/#p1435"><span class="citation" data-id="8927971"><a href="/opinion/8937596/united-states-v-wilkinson/" aria-description="Citation for case: United States v. Wilkinson">754 F.2d 1427</a></span></extracted-citation>, 1435 (2d Cir. 1985) ); <em>see also</em> <em>United States v. Williams</em> , <extracted-citation case-ids="10527462" index="101" url="https://cite.case.law/f2d/936/698/#p700"><span class="citation" data-id="563663"><a href="/opinion/563663/united-states-v-conrad-williams-and-wilbert-mckenzie-conrad-williams/" aria-description="Citation for case: United States v. Conrad Williams and Wilbert McKenzie...">936 F.2d 698</a></span></extracted-citation>, 700-01 (2d Cir. 1991) ("[T]he appropriate analysis to be used when applying the <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> rule requires that we view the redacted confession in isolation from the other evidence introduced at trial. If the confession, when so viewed, does not incriminate the defendant, then it may be admitted with a proper limiting instruction even though other evidence in the case indicates that the neutral pronoun is in fact a reference to the defendant.").</p>
<p id="p-93"><strong><em>B. Application</em></strong></p>
<p id="p-94">Van Praagh contends that his constitutional rights were violated by the admission of Lyle's redacted proffer and post-arrest statements. We ordinarily review evidentiary rulings for abuse of discretion; however, Van Praagh did not object to the introduction of the redacted <a class="page-label" data-citation-index="1" data-label="734" href="#p734" id="p734">*734</a>statements at trial, and so we review the admission of this evidence for plain error. <em>See</em> <em>United States v. Pierce</em> , <extracted-citation case-ids="4182445" index="102" url="https://cite.case.law/f3d/785/832/#p840"><span class="citation" data-id="8413417"><a href="/opinion/8442193/united-states-v-pierce/" aria-description="Citation for case: United States v. Pierce">785 F.3d 832</a></span></extracted-citation>, 840 (2d Cir.), <em>cert. denied</em> , --- U.S. ----, <extracted-citation case-ids="12597176,12597177,12597178,12597179,12597180,12597181,12597182" index="103" url="https://cite.case.law/s-ct/136/172/"><span class="citation multiple-matches"><a href="/c/S.Ct./136/172/">136 S.Ct. 172</a></span></extracted-citation>, <extracted-citation case-ids="12597179,12597182,12597177,12597178,12597115,12597180,12597181,12597114" index="104" url="https://cite.case.law/l-ed-2d/193/139/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/193/139/">193 L.Ed.2d 139</a></span></extracted-citation> (2015).<footnotemark>3</footnotemark></p>
<p id="p-95">The redacted statements did not violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . The neutral terms "individual" and "person," which were substituted for proper names with the exception of that of a supplier-"Brendan or Brandon," Tr. 436, 534-were not so obvious as to indicate to the jury that the original statements contained actual names. This was an ongoing criminal enterprise where many people were involved and the government introduced evidence of methamphetamine dealing by several people. Thus, the substitutions alone did not necessarily identify Van Praagh. Further, Lyle's redacted statements sounded sufficiently natural. For instance, he admitted that he had "first become involved in methamphetamine" through "someone" he "knew ... from work," Tr. 517-18, and that the individual for whom he worked as a "runner" "asked him to hold something for him" in the trunk of the rental car. Tr. 435, 534. Because such statements "might actually have been said by a person admitting his own culpability in the charged conspiracy while shielding the specific identity of his confederate," they do not violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . <em>Jass</em> , <extracted-citation case-ids="3660376" index="105" url="https://cite.case.law/f3d/569/47/#p58"><span class="citation" data-id="2507"><a href="/opinion/2507/united-states-v-jass/" aria-description="Citation for case: United States v. Jass">569 F.3d at 62</a></span></extracted-citation>. Nor did the redacted statements, viewed in isolation, contain any information indicating that Van Praagh was the "individual" in question, let alone information that would "immediately inculpate" him. <em><extracted-citation case-ids="3660376" index="106" url="https://cite.case.law/f3d/569/47/#p58">Id.</extracted-citation></em><extracted-citation case-ids="3660376" index="106" url="https://cite.case.law/f3d/569/47/#p58"> at 61</extracted-citation> (internal quotation marks omitted).</p>
<p id="p-96">Van Praagh relies on <em>United States v. Taylor</em> , <extracted-citation case-ids="4237500" index="107" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">745 F.3d 15</a></span></extracted-citation> (2d Cir. 2014), to support his contention that the redactions violated <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> , but <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> is distinguishable. <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> involved a <em>single</em> robbery of a drug store by four people. <em><extracted-citation case-ids="4237500" index="108" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em><extracted-citation case-ids="4237500" index="108" url="https://cite.case.law/f3d/745/15/"> at 20-21</extracted-citation>. One of the four, Luana Miller, became a cooperating witness, and another, Curtis Taylor, gave post-arrest confessions. <em><extracted-citation case-ids="4237500" index="109" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em> At the trial of Taylor and the two other co-defendants, the trial court admitted Taylor's post-arrest confessions but required their redaction to omit identifications of his two co-defendants. In the portions of the confessions that were admitted, Miller's name was mentioned but the names of the two co-defendants were replaced with "two other individuals," "the person," and "the driver." <em><extracted-citation case-ids="4237500" index="110" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em><extracted-citation case-ids="4237500" index="110" url="https://cite.case.law/f3d/745/15/"> at 29</extracted-citation>. We determined that in this circumstance the redactions were so obvious as to violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . Our reasoning was as follows. First, Miller's name was used throughout and, "[i]f Taylor had been trying to avoid naming his confederates, he would not have identified one of them-Miller-in the very phrase in which the names of the other confederates are omitted." <em><extracted-citation case-ids="4237500" index="111" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> Second, the wording of the redacted statements, <em>i.e.</em> , "[t]he robbery was the idea of the person who waited with Luana Miller and Taylor at the gas station," was stilted and unnatural. <em><extracted-citation case-ids="4237500" index="112" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> Third, in this context, the "reference to 'two other individuals' [was] suspiciously closer to the speech of a prosecutor than that of a perpetrator." <em><extracted-citation case-ids="4237500" index="113" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> On the basis of these factors, we determined that it was obvious that names had been omitted from the statements and, therefore, "the choice of implied identity [was] narrow. The unnamed persons correspond[ed] by number (two) and by role to the pair of co-defendants ... [and] [t]he jury could immediately <a class="page-label" data-citation-index="1" data-label="735" href="#p735" id="p735">*735</a>infer, on the evidence of the redacted confession alone, that Taylor had likely named the co-defendants." <em><extracted-citation case-ids="4237500" index="114" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em></p>
<p id="p-97">This case is unlike <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> . First, Lyle's statements referred to <em>multiple</em> people-not only one unnamed person to correspond to the one co-defendant, Van Praagh. This did not present the necessary process-of-elimination problem that left the jury's "choice of implied identity narrow" as in <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> . <em><extracted-citation case-ids="4237500" index="115" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em> Second, in addition to Van Praagh's methamphetamine dealing, the government introduced evidence of methamphetamine dealing by its two cooperating witnesses-Tarantino and Hodges-as well as several others. Because Lyle's statements did not reference by name those cooperating witnesses, the jury could reasonably have inferred that <em>they</em> were the "other persons" Lyle was referring to in his redacted statements. Third, Lyle's statements referred to people involved in a conspiracy to engage in <em>ongoing</em> criminal conduct, not a single criminal act like in <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> . For all of these reasons, <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> is inapposite.</p>
<p id="p-98">We also note that the district court here gave a limiting instruction. <em>See</em> <em>Taylor</em> , <extracted-citation case-ids="4237500" index="116" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/#28" aria-description="Citation for case: United States v. Taylor">745 F.3d at 28</a></span></extracted-citation> ("It matters that the district court gave limiting instructions" because "[w]e normally assume that jurors follow limiting instructions"). The district court specifically instructed the jury that "Lyle's statement about his own conduct may not be considered or discussed by you with regard to Mr. Van Praagh." Tr. 713.</p>
<p id="p-99">Finally, Van Praagh's constitutional rights were not violated by Lyle's counsel eliciting testimony on cross-examination that his client's statements had been redacted for presentation at trial and that his client had indeed provided actual names in his proffer and post-arrest statements. Again, because Van Praagh did not object during Lyle's attorney's cross-examination, we review for plain error. In urging error, Van Praagh relies on <em>Gray v. Maryland</em> , <extracted-citation case-ids="11503401" index="117" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">523 U.S. 185</a></span></extracted-citation>, <extracted-citation case-ids="11503401" index="118" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">118 S.Ct. 1151</a></span></extracted-citation>, <extracted-citation case-ids="11503401" index="119" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">140 L.Ed.2d 294</a></span></extracted-citation> (holding that "considered as a class, redactions that ... notify the jury that a name has been deleted" violated the Confrontation Clause). But <em><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">Gray</a></span></em> 's focus was on the inadequacy of the government's redaction. Van Praagh can point to no case plainly identifying <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> error when a defendant, whose post-arrest statements are being offered against him, elicits the fact of redaction, or elicits parts of the redacted statement.</p>
<p id="p-100">Van Praagh fails to show plain error here. First, his case is distinguishable from <em><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">Gray</a></span></em> in that there the redaction inadequacy was attributable to the prosecution. In any event, Van Praagh cannot satisfy the prejudice prong of plain error because in his case the redacted statements referred to multiple "individuals," which means the revelation could not have been immediately inculpatory. <em>See</em> <em>Jass</em> , <span class="citation" data-id="2507"><a href="/opinion/2507/united-states-v-jass/#61" aria-description="Citation for case: United States v. Jass">569 F.3d at 61</a></span>.</p>
<p id="p-101">Further, during cross-examination, Lyle's attorney elicited from the same witness several of the names that Lyle mentioned during his post-arrest and proffer statements, including "Zaron," "Ted," "Bob," and "Joe." Tr. 525. In our view, that testimony made it <em>less</em> , not more, obvious to the jury that Lyle had also mentioned Van Praagh. Van Praagh's name was not mentioned at all, and Lyle's counsel's elicitation of other names suggested that the "other persons" mentioned were the individuals whose names Lyle's counsel elicited, not Van Praagh. For all of these reasons, the admission of Lyle's redacted statements was not plainly erroneous.</p>
<p id="p-102"><strong>IV. <em>Admissibility of Lyle's New Jersey Arrest</em></strong></p>
<p id="p-103">We review a district court's evidentiary rulings for abuse of discretion, which we will find only if the district court "acted arbitrarily and irrationally."</p>
<p id="p-104"><a class="page-label" data-citation-index="1" data-label="736" href="#p736" id="p736">*736</a><em>United States v. Greer</em> , <extracted-citation case-ids="4085145" index="120" url="https://cite.case.law/f3d/631/608/#p614"><span class="citation" data-id="184262"><a href="/opinion/184262/united-states-v-greer/" aria-description="Citation for case: United States v. Greer">631 F.3d 608</a></span></extracted-citation>, 614 (2d Cir. 2011) (quoting <em>United States v. Garcia</em> , <extracted-citation case-ids="9429305" index="121" url="https://cite.case.law/f3d/291/127/#p136"><span class="citation" data-id="777745"><a href="/opinion/777745/united-states-v-carlos-garcia/" aria-description="Citation for case: United States v. Carlos Garcia">291 F.3d 127</a></span></extracted-citation>, 136 (2d Cir. 2002) ).</p>
<p id="p-105"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-106">Federal Rule of Evidence 404(b) provides:</p>
<blockquote id="p-107">Evidence of a crime, wrong, or other act is not admissible to prove a person's character in order to show that on a particular occasion the person acted in accordance with the character.</blockquote>
<p id="p-108">Fed. R. Evid. 404(b). "The Second Circuit's 'inclusionary rule' allows the admission of such evidence 'for any purpose other than to show a defendant's criminal propensity, as long as the evidence is relevant and satisfies the probative-prejudice balancing test of Rule 403 of the Federal Rules of Evidence.' " <em>Greer</em> , <extracted-citation case-ids="4085145" index="122" url="https://cite.case.law/f3d/631/608/#p614"><span class="citation" data-id="184262"><a href="/opinion/184262/united-states-v-greer/" aria-description="Citation for case: United States v. Greer">631 F.3d at 614</a></span></extracted-citation> (quoting <em>United States v. Inserra</em> , <extracted-citation case-ids="10522168" index="123" url="https://cite.case.law/f3d/34/83/#p89"><span class="citation" data-id="9487269"><a href="/opinion/677324/united-states-v-george-a-inserra-john-inserra-and-john-giura-dennis/" aria-description="Citation for case: United States v. George A. Inserra John Inserra and John...">34 F.3d 83</a></span></extracted-citation>, 89 (2d Cir. 1994) ).</p>
<p id="p-109">Not all evidence of uncharged misconduct, however, is prohibited by Rule 404(b). Rather,</p>
<blockquote id="p-110">[E]vidence of uncharged criminal activity is not considered other crimes evidence ... if it arose out of the same transaction or series of transactions as the charged offense, if it is inextricably intertwined with the evidence regarding the charged offense, or if it is necessary to complete the story of the crime on trial.</blockquote>
<p id="p-111"><em>United States v. Carboni</em> , <extracted-citation case-ids="11467212" index="124" url="https://cite.case.law/f3d/204/39/#p44"><span class="citation" data-id="767698"><a href="/opinion/767698/united-states-v-harry-r-carboni/" aria-description="Citation for case: United States v. Harry R. Carboni">204 F.3d 39</a></span></extracted-citation>, 44 (2d Cir. 2000) (internal quotation marks omitted); <em>see also</em> <em>Inserra</em> , <extracted-citation case-ids="10522168" index="125" url="https://cite.case.law/f3d/34/83/#p89"><span class="citation" data-id="9487269"><a href="/opinion/677324/united-states-v-george-a-inserra-john-inserra-and-john-giura-dennis/#89" aria-description="Citation for case: United States v. George A. Inserra John Inserra and John...">34 F.3d at 89</a></span></extracted-citation> ("[E]vidence of other bad acts may be admitted to provide the jury with the complete story of the crimes charged by demonstrating the context of certain events relevant to the charged offense.").</p>
<p id="p-112"><strong><em>B. Application</em></strong></p>
<p id="p-113">The district court did not abuse its discretion in admitting the evidence seized during the New Jersey arrest in January 2014. First, that evidence was not barred by Rule 404(b) because the arrest "arose out of the same transaction or series of transactions as the charged offense." <em>Carboni</em> , <extracted-citation case-ids="11467212" index="126" url="https://cite.case.law/f3d/204/39/#p44"><span class="citation" data-id="767698"><a href="/opinion/767698/united-states-v-harry-r-carboni/" aria-description="Citation for case: United States v. Harry R. Carboni">204 F.3d at 44</a></span></extracted-citation>. Specifically, as discussed above, Lyle argued at trial that he was only a methamphetamine user-not a dealer. The government rebutted that argument with evidence of Lyle's New Jersey arrest. In summation, the government argued:</p>
<blockquote id="p-114">14 or 15 grams [of methamphetamine] is still many hundreds, if not thousands, of dollars of meth.... Also, you know what else was in that room? A dozen baggies, a scale, $3,000 in cash. He was not weighing out meth for his own personal use. That was meth he was going to sell.</blockquote>
<p id="p-115">Tr. 629. In other words, the evidence seized pursuant to the New Jersey arrest was not evidence of <em>other</em> crimes; it was evidence of the very crime charged in count one of the indictment, a conspiracy involving Lyle, Van Praagh, and others to distribute methamphetamine from in or about December 2012 through in or about January 2014. Accordingly, evidence of the New Jersey arrest was admissible as direct proof of the methamphetamine distribution conspiracy.</p>
<p id="p-116">Second, and in any event, the evidence of the New Jersey arrest fits within the Rule 404(b) inclusionary rule because it shows Lyle's knowledge and intent regarding the contents of the rental car. Because Lyle argued throughout trial that he did not know what was in the trunk of the rental car, his knowledge and intent were at issue. <em>United States v. Ramirez</em> , <extracted-citation case-ids="10534202" index="127" url="https://cite.case.law/f2d/894/565/#p568"><span class="citation" data-id="535595"><a href="/opinion/535595/united-states-v-john-alonso-ramirez-and-zeir-marulanda/" aria-description="Citation for case: United States v. John Alonso Ramirez, and Zeir Marulanda">894 F.2d 565</a></span></extracted-citation>, 568 (2d Cir. 1990) ("When the defendant disavows awareness that a crime was being perpetrated, and the government bears the burden of proving the defendant's knowing possession as an element of the crime, knowledge is properly put in issue."). The fact that Lyle was in possession of 14-15 grams of methamphetamine <a class="page-label" data-citation-index="1" data-label="737" href="#p737" id="p737">*737</a>and tools of the drug trade less than a month after he was arrested with the rental car is probative of his knowledge and intent regarding the contents of the rental car. In addition, the probative value of this evidence was not "substantially outweighed" by the risk of unfair prejudice as it "did not involve conduct any more sensational or disturbing than the crimes with which [Lyle was] charged." <em>United States v. Pitre</em> , <extracted-citation case-ids="10524117" index="128" url="https://cite.case.law/f2d/960/1112/#p1120"><span class="citation" data-id="580870"><a href="/opinion/580870/united-states-v-joseph-pitre-edwyn-pitre-angel-m-otero-richard-pitre/" aria-description="Citation for case: United States v. Joseph Pitre Edwyn Pitre Angel M. Otero...">960 F.2d 1112</a></span></extracted-citation>, 1120 (2d Cir. 1992) (quoting <em>United States v. Roldan-Zapata</em> , <extracted-citation case-ids="10537862" index="129" url="https://cite.case.law/f2d/916/795/#p804"><span class="citation" data-id="550091"><a href="/opinion/550091/united-states-v-oscar-roldan-zapata-and-pedro-osario-serna/" aria-description="Citation for case: United States v. Oscar Roldan-Zapata and Pedro Osario-Serna">916 F.2d 795</a></span></extracted-citation>, 804 (2d Cir. 1990) ). Accordingly, the district court acted well within its discretion in finding that the probative value of the evidence outweighed the threat of unfair prejudice.</p>
<p id="p-117"><strong>V. <em>Sufficiency of the Conspiracy Evidence</em></strong></p>
<p id="p-118">We review Van Praagh's challenge to whether the evidence was sufficient to support his conspiracy conviction <em>de novo</em> , "view[ing] the evidence in the light most favorable to the government, crediting every inference that could have been drawn in the government's favor, and deferring to the jury's assessment of witness credibility and its assessment of the weight of the evidence." <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="130" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d at 113</a></span></extracted-citation> (quoting <em>United States v. Coplan</em> , <extracted-citation case-ids="3649269" index="131" url="https://cite.case.law/f3d/703/46/#p62"><span class="citation" data-id="9501731"><a href="/opinion/812765/united-states-v-coplan/" aria-description="Citation for case: United States v. Coplan">703 F.3d 46</a></span></extracted-citation>, 62 (2d Cir. 2012) ). We must affirm if "<em>any</em> rational trier of fact could have found the essential elements of the crime beyond a reasonable doubt." <em><extracted-citation case-ids="3649269" index="132" url="https://cite.case.law/f3d/703/46/#p62"><span class="citation" data-id="9501731"><a href="/opinion/812765/united-states-v-coplan/" aria-description="Citation for case: United States v. Coplan">Id.</a></span></extracted-citation></em> (quoting <em>United States v. Vernace</em> , <extracted-citation case-ids="4082128" index="133" url="https://cite.case.law/f3d/811/609/#p615"><span class="citation" data-id="8413796"><a href="/opinion/8442529/united-states-v-vernace/" aria-description="Citation for case: United States v. Vernace">811 F.3d 609</a></span></extracted-citation>, 615 (2d Cir. 2016) ).</p>
<p id="p-119">The crux of a conspiracy is an agreement between two or more persons to join together to accomplish something illegal. <em>United States v. Parker</em> , <extracted-citation case-ids="3684820" index="134" url="https://cite.case.law/f3d/554/230/#p234"><span class="citation" data-id="1278099"><a href="/opinion/1278099/united-states-v-parker/" aria-description="Citation for case: United States v. Parker">554 F.3d 230</a></span></extracted-citation>, 234 (2d Cir. 2009) ("To prove a conspiracy, the evidence must show that 'two or more persons agreed to participate in a joint venture intended to commit an unlawful act.' " (quoting <em>United States v. Desimone</em> , <extracted-citation case-ids="199978" index="135" url="https://cite.case.law/f3d/119/217/#p223"><span class="citation" data-id="6951731"><a href="/opinion/7048410/united-states-v-desimone/" aria-description="Citation for case: United States v. Desimone">119 F.3d 217</a></span></extracted-citation>, 223 (2d Cir. 1997) )). We have recognized a "narrow exception" to the conspiracy rule for a transaction between a buyer and seller of drugs. <em><extracted-citation case-ids="199978" index="136" url="https://cite.case.law/f3d/119/217/#p223"><span class="citation" data-id="6951731"><a href="/opinion/7048410/united-states-v-desimone/" aria-description="Citation for case: United States v. Desimone">Id.</a></span></extracted-citation></em> Under this exception, "the existence of a buyer-seller relationship does not <em>itself</em> establish a conspiracy; however, where there is additional evidence showing an agreement to join together to accomplish an objective beyond the sale transaction, the evidence may support a finding that the parties intentionally participated in a conspiracy." <em>United States v. Hawkins</em> , <extracted-citation case-ids="6050917" index="137" url="https://cite.case.law/f3d/547/66/#p72"><span class="citation" data-id="1225840"><a href="/opinion/1225840/united-states-v-hawkins/" aria-description="Citation for case: United States v. Hawkins">547 F.3d 66</a></span></extracted-citation>, 72 (2d Cir. 2008) ; <em>see also</em> <em>United States v. Rojas</em> , <extracted-citation case-ids="3771399" index="138" url="https://cite.case.law/f3d/617/669/#p674"><span class="citation" data-id="152881"><a href="/opinion/152881/united-states-v-rojas/" aria-description="Citation for case: United States v. Rojas">617 F.3d 669</a></span></extracted-citation>, 674 (2d Cir. 2010) ("[T]he exception does not protect either the seller or buyer from a charge that they conspired together to transfer drugs if the evidence supports a finding that they shared a conspiratorial purpose to advance other transfers, whether by the seller or by the buyer." (alteration and internal quotation marks omitted)). The question thus becomes "whether the evidence in its totality suffices to permit a jury to find beyond a reasonable doubt that the defendant was not merely a buyer or seller of narcotics, but rather that the defendant knowingly and intentionally participated in the narcotics-distribution conspiracy by agreeing to accomplish its illegal objective beyond the mere purchase or sale." <em>Hawkins</em> , <extracted-citation case-ids="6050917" index="139" url="https://cite.case.law/f3d/547/66/#p72"><span class="citation" data-id="1225840"><a href="/opinion/1225840/united-states-v-hawkins/" aria-description="Citation for case: United States v. Hawkins">547 F.3d at 73</a></span>-74</extracted-citation>.</p>
<p id="p-120">Van Praagh did not request a buyer-seller instruction at trial and so we review for plain error. <em>Pierce</em> , <extracted-citation case-ids="4182445" index="140" url="https://cite.case.law/f3d/785/832/#p840"><span class="citation" data-id="8413417"><a href="/opinion/8442193/united-states-v-pierce/" aria-description="Citation for case: United States v. Pierce">785 F.3d at 840</a></span></extracted-citation>. The district court did not plainly err in failing to give a buyer-seller instruction because the government presented ample evidence of a narcotics conspiracy beyond a buyer-seller relationship between Van Praagh and Lyle.</p>
<p id="p-121">First, Van Praagh sold methamphetamine not just to Lyle, but to others. Indeed, he received weekly shipments of methamphetamine, which he then sold to others. With assistance from Tarantino, he <a class="page-label" data-citation-index="1" data-label="738" href="#p738" id="p738">*738</a>regularly sold methamphetamine out of his apartment in Queens as well as out of hotels, and he made deliveries to "[p]robably 50" customers. Tr. 124.</p>
<p id="p-122">Second, the quantity of drugs was consistent with a drug trafficking operation. Tarantino testified that Lyle repeatedly purchased pound-level quantities of methamphetamine at $19,000 to $25,000 per pound. <em>See</em> <em>United States v. Contreras</em> , <extracted-citation case-ids="11099115" index="141" url="https://cite.case.law/f3d/249/595/#p600"><span class="citation" data-id="773155"><a href="/opinion/773155/united-states-v-eliseo-contreras/" aria-description="Citation for case: United States v. Eliseo Contreras">249 F.3d 595</a></span></extracted-citation>, 600 (7th Cir. 2001) (noting that repeat sales suggest "more than a transient relationship," but are "by themselves" insufficient to support an inference of a conspiracy between the supplier and purchaser); <em>see also</em> <em>United States v. Murray</em> , <extracted-citation case-ids="1380727" index="142" url="https://cite.case.law/f2d/618/892/#p902"><span class="citation" data-id="376822"><a href="/opinion/376822/united-states-v-dale-murray-paul-leahey-ronald-vanderbosch-lawrence/" aria-description="Citation for case: United States v. Dale Murray, Paul Leahey, Ronald...">618 F.2d 892</a></span></extracted-citation>, 902 (2d Cir. 1980) ("[O]ne who deals in large quantities of narcotics may be presumed to know that he is a part of a venture which extends beyond his individual participation." (quoting <em>United States v. Magnano</em> , <extracted-citation case-ids="1024903" index="143" url="https://cite.case.law/f2d/543/431/#p433"><span class="citation" data-id="339842"><a href="/opinion/339842/united-states-v-joseph-magnano-aka-joe-the-grind/" aria-description="Citation for case: United States v. Joseph Magnano, A/K/A &quot;Joe the Grind&quot;">543 F.2d 431</a></span></extracted-citation>, 433-34 (2d Cir. 1976) )).</p>
<p id="p-123">Accordingly, the district court did not plainly err in failing to <em>sua sponte</em> give a buyer-seller instruction. <em>See</em> <em>United States v. Medina</em> , <extracted-citation case-ids="10521074" index="144" url="https://cite.case.law/f2d/944/60/#p65"><span class="citation" data-id="567926"><a href="/opinion/567926/united-states-v-luz-medina-silverio-polanco-franklin-marmolejo-juan-a/" aria-description="Citation for case: United States v. Luz Medina, Silverio Polanco, Franklin...">944 F.2d 60</a></span></extracted-citation>, 65-66 (2d Cir. 1991) (holding that the district court was not required to give a buyer-seller instruction "where ... there is advanced planning among the alleged co-conspirators to deal in wholesale quantities of drugs obviously not intended for personal use" because "[u]nder such circumstances, the participants in the transaction may be presumed to know that they are part of a broader conspiracy").</p>
<p id="p-124"><strong>VI. <em>Reasonableness of Van Praagh's Sentence</em></strong></p>
<p id="p-125">We review the substantive reasonableness of a sentence under a "deferential abuse-of-discretion standard." <em>United States v. Aldeen</em> , <extracted-citation case-ids="4275829" index="145" url="https://cite.case.law/f3d/792/247/#p251"><span class="citation" data-id="8413509"><a href="/opinion/8442268/united-states-v-aldeen/" aria-description="Citation for case: United States v. Aldeen">792 F.3d 247</a></span></extracted-citation>, 251 (2d Cir. 2015) (quoting <em>Gall v. United States</em> , <extracted-citation case-ids="3675664" index="146" url="https://cite.case.law/us/552/38/#p41"><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">552 U.S. 38</a></span></extracted-citation>, 41, <extracted-citation case-ids="3675664" index="147" url="https://cite.case.law/us/552/38/#p41"><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">128 S.Ct. 586</a></span></extracted-citation>, <extracted-citation case-ids="3675664" index="148" url="https://cite.case.law/us/552/38/#p41"><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">169 L.Ed.2d 445</a></span></extracted-citation> (2007) ). The question is whether Van Praagh's below-Guidelines sentence of 144 months' imprisonment "shock[s] the conscience," constitutes a "manifest injustice," or is otherwise substantively unreasonable. <em><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">Id.</a></span></em> at 255 (quoting <em>United States v. Rigas</em> , <extracted-citation case-ids="5756241" index="149" url="https://cite.case.law/f3d/583/108/#p123"><span class="citation" data-id="2467"><a href="/opinion/2467/united-states-v-rigas/" aria-description="Citation for case: United States v. Rigas">583 F.3d 108</a></span></extracted-citation>, 123 (2d Cir. 2009) ); <em>see also</em> <em>United States v. Perez-Frias</em> , <extracted-citation case-ids="4103975" index="150" url="https://cite.case.law/f3d/636/39/#p43"><span class="citation" data-id="213681"><a href="/opinion/213681/united-states-v-perez-frias/" aria-description="Citation for case: United States v. Perez-Frias">636 F.3d 39</a></span></extracted-citation>, 43 (2d Cir. 2011) (per curiam) ("[I]n the overwhelming majority of cases, a Guidelines sentence will fall comfortably within the broad range of sentences that would be reasonable in the particular circumstances. It is therefore difficult to find that a below-Guidelines sentence is unreasonable." (internal quotation marks and citation omitted)).</p>
<p id="p-126">Van Praagh's below-Guidelines sentence of 144 months was substantively reasonable. The district court fully explained its reasoning. It considered Van Praagh's "very unhappy upbringing," and the "very positive change" that Van Praagh "seem[ed] to be undergoing." Van Praagh App. 58-59. The district court determined, however, that a 144-month sentence was sufficient but not greater than necessary because Van Praagh (1) had committed a "very serious" crime; (2) had a "long history of drug dealing" and "plenty of opportunities to change"; (3) clearly had been "in charge of dealing more drugs at a higher level than [Lyle]"; and (4) had a "prior record suggest[ing] that he still continues to be a danger to the community." <em><extracted-citation case-ids="4103975" index="151" url="https://cite.case.law/f3d/636/39/#p43"><span class="citation" data-id="213681"><a href="/opinion/213681/united-states-v-perez-frias/" aria-description="Citation for case: United States v. Perez-Frias">Id.</a></span></extracted-citation></em></p>
<p id="p-127">Van Praagh's argument that, like Lyle, he should have been sentenced to the statutory mandatory minimum of 120 months' imprisonment is unavailing. As the district court noted, Van Praagh had a "more important role" than Lyle. <em>See</em> Van Praagh App. 62. Van Praagh supplied Lyle with pound quantities of methamphetamine on multiple occasions. Van Praagh had people working for him to make drug deliveries. Moreover, Van Praagh's criminal history was clearly more serious than Lyle's. Although <a class="page-label" data-citation-index="1" data-label="739" href="#p739" id="p739">*739</a>neither man had previously served any jail time for his crimes, Van Praagh's previous convictions included crimes relating to methamphetamine, while Lyle had only a violation for marijuana possession twenty years prior to the instant offense conduct. In these circumstances, we identify no abuse of the district court's sentencing discretion and no merit in Van Praagh's claim that his sentence is substantively unreasonable.</p>
<p id="p-128"><strong><em>CONCLUSION</em></strong></p>
<p id="p-129">To summarize, we conclude as follows:</p>
<blockquote id="p-130">1. Because Lyle was an unlicensed, as well as unauthorized, driver of the rental car, he had no reasonable expectation of privacy in that car, and the district court did not err in denying his motion to suppress. Even assuming Lyle had a legitimate privacy interest, the search and seizure of the rental car did not violate the Fourth Amendment.</blockquote>
<blockquote id="p-131">2. Lyle's counsel's statement in his opening argument that "we dispute [ ] the idea that [Lyle] was a dealer," Tr. 28, triggered the waiver in Lyle's proffer agreement, and the proffer statements, taken together, fairly rebutted his counsel's argument that Lyle was a mere user of methamphetamine and not a dealer.</blockquote>
<blockquote id="p-132">3. The admission of Lyle's redacted proffer and post-arrest statements in the defendants' joint trial was not plainly erroneous because the statements substituted neutral terms for actual names and had no otherwise identifying information. Further, the district court did not plainly err in allowing Lyle's counsel, without Van Praagh's objection, to elicit testimony that Lyle's statements had been redacted, that Lyle had provided actual names in his proffer and post-arrest statements, and what several of those names were because those disclosures did not prejudice Van Praagh and, indeed, made it <em>less</em> obvious to the jury that Lyle was referring to Van Praagh in his statements.</blockquote>
<blockquote id="p-133">4. The district court did not abuse its discretion in admitting the evidence seized during Lyle's New Jersey arrest because (a) it was direct evidence of the conspiracy charged in count one of the superseding indictment, and (b) even if it was not direct evidence, it was not "other crimes evidence" prohibited by Federal Rule of Evidence 404(b) because it showed Lyle's knowledge and intent regarding the contents of the rental car on December 11, 2013.</blockquote>
<blockquote id="p-134">5. The district court did not plainly err in failing to <em>sua sponte</em> give a buyer-seller instruction to the jury because the government presented ample evidence of a narcotics conspiracy.</blockquote>
<blockquote id="p-135">6. Van Praagh's below-Guidelines sentence of 144 months' imprisonment was substantively reasonable.</blockquote>
<p id="p-136">Accordingly, the judgments of the district court are <strong>AFFIRMED</strong> .</p>
<footnote label="1">
<p id="p-139">Lyle identified this individual as Van Praagh, but at trial, "individual" was substituted for Van Praagh's name pursuant to <em>Bruton v. United States</em> , <extracted-citation case-ids="1767670" index="152" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U.S. 123</a></span></extracted-citation>, <extracted-citation case-ids="1767670" index="153" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">88 S.Ct. 1620</a></span></extracted-citation>, <extracted-citation case-ids="1767670" index="154" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">20 L.Ed.2d 476</a></span></extracted-citation> (1968).</p>
</footnote>
<footnote label="2">
<p id="p-140">Some courts have concluded that there are two inquiries: first, whether the impoundment of a car is reasonable; and second, if so, whether the subsequent search of the car after the impoundment is reasonable. <em>See, e.g.,</em> <em>Duguay</em> , <extracted-citation case-ids="7630921" index="155" url="https://cite.case.law/f3d/93/346/#p351"><span class="citation" data-id="9489468"><a href="/opinion/724910/united-states-v-christopher-duguay/#351" aria-description="Citation for case: United States v. Christopher Duguay">93 F.3d at 351</a></span></extracted-citation> ("[T]he decision to impound (the 'seizure') is properly analyzed as distinct from the decision to inventory (the 'search')."); <em>Coccia</em> , <extracted-citation case-ids="2843114" index="156" url="https://cite.case.law/f3d/446/233/#p239">446 F.3d at </extracted-citation>237 n. 5 (same). Here, Lyle has challenged only the impoundment and not the subsequent search of the rental vehicle. Hence, we need not reach the second inquiry.</p>
</footnote>
<footnote label="3">
<p id="p-141">Van Praagh contends that his <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> argument was preserved by his counsel's objection to the admission of Lyle's unredacted statements and by Lyle's counsel's objection to the redacted statements. Admission of unredacted statements, however, is a different and independent issue, and Van Praagh cites no authority suggesting that one party's counsel may preserve another party's claim of error when the other party's counsel fails timely to join in the objection. Accordingly, plain error review applies.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Maez.md  (`case`, 6 assertions)

### content_page

```
---
title: United States v. Maez
type: case
citation: "872 F.2d 1444 (1989)"
parallel_cite: ""
neutral_cite: "1989 U.S. App. LEXIS 5092; 1989 WL 36532"
court: "U.S. Court of Appeals, 10th Cir."
court_level: coa
circuit: ca10
year: 1989
date_decided: 1989-04-19
docket: 88-1128
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: unverified
  as_of_content: null
  as_of_treatment: null
  composite_basis: unverified
  composite_basis_ref: null
  varies_by_point: false
  scope_note: "Frontier stub: treatment/progeny intentionally not derived until S6 promotion."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/521939/united-states-v-arthur-maez/"
  cluster_id: 521939
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Maez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — constructive-entry (10th Cir. recognizing side: SWAT loudspeaker order = warrantless in-home arrest, 872 F.2d at 1451)"
  - page: "[[Arrest in the Home]]"
    role: "Related — constructive-entry cross-ref"
related:
  - "[[Entry to Arrest]]"
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[Seizure of the Person]]"
  - "[[The Exclusionary Rule]]"
tags:
  - case
  - fourth-amendment
  - arrest-in-the-home
  - payton
  - constructive-entry
  - warrantless-arrest
  - show-of-force
  - tenth-circuit
holding: "The Tenth Circuit held that police effected an unlawful warrantless arrest in the home in violation of Payton v. New York when, without an arrest warrant, a SWAT team surrounded Maez's mobile home and ordered the occupants out over loudspeakers, coercing him from the home into custody — physical entry across the threshold is not required, because such a show of force that makes a suspect come out under coercion is a Payton violation — so the evidence obtained after the tainted arrest required suppression, and the court reversed."
---

# United States v. Maez

*872 F.2d 1444 (10th Cir. 1989)* (No. 88-1128) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 521939 → majority opinion 521939 (872 F.2d 1444, decided 1989-04-19, Holloway, C.J.); Rule quote reporter-page-verified against the CL opinion text (the court's own cross-reference to p. 1451) 2026-07-07. S9 promotes. -->

## Background
Two men robbed an Albuquerque bank in August 1987. A witness's tip led the FBI to trace a getaway truck to Arthur Maez, and officers located his mobile home — the truck parked outside — and put it under surveillance. Without obtaining an arrest warrant, Albuquerque police, the FBI, and a SWAT team planned the arrest, then arrived and surrounded the trailer, which had a single exit. SWAT members dressed in black, with rifles pointed at the home, ordered the occupants out over loudspeakers; no officer went to the door. Maez's wife watched their fifteen-year-old son — never a suspect — be handcuffed across the street, told her husband what was happening, and Maez said, "we have to go outside." He exited and was taken into custody. Maez's wife then signed consent-to-search forms, and officers seized cash, ammunition, and clothing; Maez made incriminating statements. Convicted of armed bank robbery, Maez appealed the denial of his motion to suppress.

## Issue
Whether an unlawful warrantless arrest in the home, in violation of *[[Payton v. New York]]*, occurred where armed officers and a SWAT team — having no arrest warrant — surrounded Maez's home and, over loudspeakers, ordered the occupants out, coercing Maez from the home into custody, even though no officer physically entered the trailer.

## Rule
*[[Payton v. New York|Payton]]* forbids a warrantless, non-consensual entry into the home to make a routine arrest, and that protection is not defeated by the absence of a physical threshold crossing. Following the Ninth and Sixth Circuits, the Tenth Circuit adopted the coercion rule: "Those courts have held that *Payton* is violated where there is such a show of force that a defendant comes out of a home under coercion and submits to being taken in custody." — 872 F.2d at 1451. ^pin-1451

## Application
The officers had no arrest warrant, yet they surrounded Maez's trailer with a SWAT team, trained rifles on it, handcuffed his teenage son in plain view, and ordered the occupants out over loudspeakers — an "extreme coercion" that made Maez leave the home involuntarily. Because it is the location of the arrested person, not the arresting agents, that determines whether an arrest occurs within a home, Maez was arrested inside his home without a warrant, in violation of *[[Payton v. New York|Payton]]*. The evidence and statements obtained after that tainted arrest — including the consent search Mrs. Maez signed while surrounded by officers — were fruits of the illegal arrest and should have been suppressed.

## Conclusion
**Reversed.** Chief Judge Holloway wrote for the panel (Holloway, C.J.; Brorby, Circuit Judge; and Anderson, District Judge, sitting by designation).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Maez* is a leading Tenth Circuit statement of **constructive entry** under *[[Payton v. New York|Payton]]*: police who mount a coercive show of force to draw a suspect out of his home and arrest him have made a warrantless arrest "in the home," even without crossing the threshold — the arrestee's location, not the officers', controls. Pair it with *[[Payton v. New York|Payton]]*'s firm line at the entrance to the house and with the fruit-of-the-poisonous-tree consequences for evidence and consent obtained afterward.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Related*

## Sources
- [*United States v. Maez*, 872 F.2d 1444 (10th Cir. 1989)](https://www.courtlistener.com/opinion/521939/united-states-v-arthur-maez/) — pinpoint: 1451 (the constructive-entry / show-of-force *Payton* holding; the CL majority text is paragraph-numbered, and the court's own opinion cross-references this holding to reporter page 1451). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "45ba4aa77676e33f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "872 F.2d 1444 (1989)", "court": "U.S. Court of Appeals, 10th Cir.", "neutral_cite": "1989 U.S. App. LEXIS 5092; 1989 WL 36532", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Maez", "year": "1989"}}
{"assertion_id": "3345873bf0fc0f7b", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related — constructive-entry cross-ref", "title": "United States v. Maez"}}
{"assertion_id": "7ad3ada5d6372608", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Tenth Circuit held that police effected an unlawful warrantless arrest in the home in violation of Payton v. New York when, without an arrest warrant, a SWAT team surrounded Maez's mobile home and ordered the occupants out over loudspeakers, coercing him from the home into custody — physical entry across the threshold is not required, because such a show of force that makes a suspect come out under coercion is a Payton violation — so the evidence obtained after the tainted arrest required suppression, and the court reversed.", "title": "United States v. Maez"}}
{"assertion_id": "b5cb95ac41ed035f", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — constructive-entry (10th Cir. recognizing side: SWAT loudspeaker order = warrantless in-home arrest, 872 F.2d at 1451)", "title": "United States v. Maez"}}
{"assertion_id": "261c2771d53ca332", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Maez"}}
{"assertion_id": "87096e6748fb89d0", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Maez", "varies_by_point": "false"}}
```

### lake record — United States v. Maez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Maez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Arthur Maez",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Arthur MAEZ, Defendant-Appellant",
    "input_case_name": "United States v. Maez",
    "court": "U.S. Court of Appeals, 10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "1989-04-19",
    "year": 1989,
    "docket": "88-1128",
    "cluster_id": 521939,
    "lead_opinion_id": 9478941,
    "sibling_ids": [],
    "absolute_url": "/opinion/521939/united-states-v-arthur-maez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "872 F.2d 1444",
      "volume": "872",
      "reporter": "F.2d",
      "page": "1444",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. App. LEXIS 5092",
        "volume": "1989",
        "reporter": "U.S. App. LEXIS",
        "page": "5092",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 WL 36532",
        "volume": "1989",
        "reporter": "WL",
        "page": "36532",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "872 F.2d 1444",
        "volume": "872",
        "reporter": "F.2d",
        "page": "1444",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. App. LEXIS 5092",
        "volume": "1989",
        "reporter": "U.S. App. LEXIS",
        "page": "5092",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 WL 36532",
        "volume": "1989",
        "reporter": "WL",
        "page": "36532",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "872 F.2d 1444",
    "official_selection": {
      "court_class": "coa",
      "selected": "872 F.2d 1444",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [],
  "treatment": {
    "field_i_validity": "unverified",
    "as_of_content": null,
    "as_of_treatment": null,
    "composite_basis": "unverified",
    "composite_basis_ref": null,
    "varies_by_point": false,
    "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.",
    "point_overrides": [],
    "edges": [],
    "derivation": {}
  },
  "progeny": {
    "complete_query": null,
    "indexed_citing_opinions": null,
    "count_source": null,
    "per_sibling": [],
    "citation_count": null,
    "cache_path": null,
    "enumeration": null,
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": null,
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-07T13:26:52Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-maez--521939",
      "to_record_id": "United States v. Maez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Maez

```
<opinion type="majority">
<author id="b1538-9">HOLLOWAY, Chief Judge.</author>
<p id="b1538-10">Defendant Maez (Maez) was charged with armed bank robbery, a violation of <span class="citation no-link">18 U.S.C. § 2113</span>(a) &amp; (d) (1982) and aiding and abetting, a violation of <span class="citation no-link">18 U.S.C. § 2</span> (1982). He filed a pretrial motion to suppress evidence seized during a search of his home and truck and incriminating statements he made thereafter. That motion was denied after a suppression hearing and the evidence was admitted at trial. Maez was convicted. He appeals, arguing that the motion to suppress should have been granted.</p>
<p id="b1538-11">The paramount question presented is whether a violation of <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), occurred when a number of armed officers and a SWAT team, having no warrant for an arrest, surrounded a mobile home occupied by Maez, his wife and children, and over loud speakers asked the occupants to remove themselves from the home, which they did, Maez then being taken into custody. We hold that a violation and unlawful arrest occurred. Because evidence obtained after the arrest and admitted at trial over Maez’ objection was tainted, we reverse.</p>
<p id="b1538-15">I</p>
<p id="b1538-16">
<em>Factual Background and Procedural Posture</em>
</p>
<p id="b1538-17">A.</p>
<p id="b1538-18">
<em>The Arrest of Maez</em>
</p>
<p id="b1538-19">Two men robbed an Albuquerque bank on Friday, August 14, 1987. A bank customer reported that an early 1960’s Ford or Dodge pickup truck with a wooden tailgate and a New Mexico license plate number KO-1919 was involved in the robbery. There was no such number, but an FBI dispatcher found that license number KD-1919 belonged to a 1959 Ford pickup truck registered to Maez. A description of the truck, both robbers, and Maez’ address was given over the radio.</p>
<p id="b1538-20">Deputy Sheriff Pacheco heard the broadcast at 3:00 p.m. He knew Maez and contacted a confidential informant who knew where Maez lived. The informant directed Pacheco to the Maez’ home. At the home he saw a truck matching the description he had been given. By now it was 3:30 p.m. II R. 18-19. Pacheco left and the Albuquerque police department and FBI were contacted. The Maez home was left unguarded between approximately 3:30 and 4:30 p.m. Pacheco returned at approximately 4:30 p.m. after meeting with his supervisor. From that point on the trailer (which had only one exit — the front door) was under surveillance. The truck at the residence was later identified as the getaway truck.</p>
<p id="b1538-21">Several Albuquerque police officers, a SWAT team and the FBI met in a restau<page-number citation-index="1" label="1447">*1447</page-number>rant parking lot to plan Maez’ arrest.<footnotemark>1</footnotemark> They arrived at the Maez’ home between 6:00 and 6:30 p.m. Ill R. 106. SWAT team members dressed in black surrounded the trailer and (over loud speakers) asked the occupants of the home to come out. II R. 38-39; III R. 143. None of the officers went to the door. Mrs. Maez heard some commotion outside. When she looked out the front door she saw her fifteen year old son walking across the street with his hands in the air. She watched as he was searched and handcuffed. An FBI agent testified the boy was handcuffed; he was never a suspect in the robbery however. Ill R. 132. There were rifles pointed at the house. Ill R. 152. Mrs. Maez told her husband what was happening and he looked outside and said, “we have to go outside_” III R. 152. Mr. and Mrs. Maez were told to exit one at a time.</p>
<p id="b1539-7">B.</p>
<p id="b1539-8">
<em>Mrs. Maez’ Consents to Search</em>
</p>
<p id="A2HN">By the time Mrs. Maez had left the trailer it was approximately 6:45 p.m. II R. 49-50; III R. 75. She was escorted, with her two month old baby, outside the trailer park fence, past approximately ten police officers and into the presence of five more. Shortly thereafter, she was asked to read and sign consent forms authorizing a search of the trailer. She owned the trailer. Police officer Whitson filled in the blanks on an Albuquerque police department consent form and explained the form to Mrs. Maez before she signed it.<footnotemark>2</footnotemark> Mrs. Maez was given time to read the form.<footnotemark>3</footnotemark> No evidence was seized pursuant to this consent. II R. 44-45.</p>
<p id="b1539-10">After she had signed the Albuquerque police department consent form, Mrs. Maez was asked to sign an FBI consent to search form. Agent Guyman explained that they would be looking for money, weapons, or clothing. He told Mrs. Maez that her husband had been arrested. Guyman filled out the form and had Mrs. Maez read it out loud. Agent Marrero, who was present when the form was signed, testified that Mrs. Maez was visibly upset when she signed the form. She said that she signed the forms only because she had to. Ill R. 97, 157.<footnotemark>4</footnotemark> A bag containing $5,800, a blue stocking cap, a box of ammunition, and two red bandannas were seized. Mrs. Maez signed a third consent to search form relating to her personal automobile; no evidence was seized from the automobile.<footnotemark>5</footnotemark></p>
<p id="b1539-11">C.</p>
<p id="b1539-12">
<em>Maez’ Interrogation</em>
</p>
<p id="b1539-13">Maez was taken into custody by the Albuquerque Police Department and turned over to the FBI at approximately 7:15 p.m. The officers asked if they could search the trailer and vehicles and when they indicated they had no search warrant, Maez <page-number citation-index="1" label="1448">*1448</page-number>said no.<footnotemark>6</footnotemark> He was then taken to an interview room where he was given <em>Miranda </em>warnings and signed a waiver of rights form. There was no conversation prior to their arrival. It was now 8:00 p.m. Maez’ interrogation lasted for an hour and one half. II R. 35. He signed a consent to search form relating to his truck during the interrogation. Guyman was called and he searched the truck.</p>
<p id="b1540-4">During the interrogation FBI agent Ga-ray asked Maez about the dark veins on his arm. Maez admitted that he used heroin three times a week and said that he had taken two valiums two hours before he was taken into custody. Ill R. 122. Maez explained that he had been driving his pickup in the vicinity of the bank (picking up pop cans) on the day of the robbery. He also admitted ownership of the cap found outside the bank doors. However, when Agent Denniston explained where it had been found, Maez denied that it was his. Agent Garay testified that about three quarters of the way through the interview, Maez vomited. Ill R. 135. The interview continued. Garay testified that Maez did not appear to him to be confused, frightened, or under the influence of drugs. Maez said that he felt dizzy from the vali-ums and that he was confused by the questions of the three officers. Ill R. 145-146.</p>
<p id="b1540-5">D.</p>
<p id="b1540-6">
<em>The Trial Court’s Ruling on the Motion to Suppress</em>
</p>
<p id="AA0O">The trial court orally denied the motion to suppress. The court found that “there was probable cause to arrest the defendant,” a fact not disputed on appeal. II R. 162-164. The court further found that Maez was arrested “legally ... after he came out of his trailer.” II R. 164.</p>
<p id="b1540-7">The court found that “while the circumstances may have been tense and while the environment may not have been ... ideal ..., that nevertheless [Ms. Patsy Maez] voluntarily and willingly gave the officers a permission to search.” II R. 164. The court concluded that all of the items which were seized from the trailer were “legally and validly taken under the permission to search....” II R. 164.</p>
<p id="b1540-10">The court further found that after being given <em>Miranda </em>warnings, Maez willingly and knowingly gave permission to search the Ford pickup “in which the holster was found.” II R. 165. The court held that the statements made by Maez, including the statements regarding his cap, were “knowingly and willingly given” after he had been given <em>Miranda </em>warnings. II R. 165.</p>
<p id="b1540-11">E.</p>
<p id="b1540-12">
<em>Evidence At Trial</em>
</p>
<p id="b1540-13">At trial, bank teller Christina Carlsen testified that one of the robbers was wearing a hat and had a red bandanna over his face. The bandanna, which was found during the search of the trailer conducted pursuant to the FBI consent form signed by Mrs. Maez, was admitted into evidence. Carlson identified Maez as the taller of the two robbers and the one who struck Mariana Griego, another teller, unconscious with the gun he was carrying. Griego identified Maez as one of the robbers. IV R. 111. She said that he put a gun under her chin. Griego said that although she could not clearly see his face during the robbery (because it was covered by the bandanna and he was wearing a cap), she was able to see his eyes, a mustache, and dark graying hair. She remembered Maez being about five feet seven inches tall. Griego also said that she recognized a number of tattoos on Maez’ arms and on the web of his thumb. IV R. 105-114.</p>
<p id="b1540-14">On the way out of the bank, one of the robbers hit Ernest Harrison, Jr., vice presi<page-number citation-index="1" label="1449">*1449</page-number>dent of the bank (and a former FBI agent) and knocked him to the ground. The taller robber’s hat fell off. Harrison followed the robbers around a corner and saw them leaving in a light colored pickup with a wooden tailgate. He said that the taller robber was wearing grey pants and was approximately five feet nine inches tall. IV R. 42-43. At the same time, a bank customer, Michael Barnes, saw what he thought was a gun and followed the truck to see the license plate number. He reported the number and also described the truck as an early 1960’s Ford with a wooden tailgate. He testified that the taller robber was wearing a light blue shirt. He also identified photographs of the truck.</p>
<p id="b1541-5">A box of .25 caliber ammunition, which was found in Maez’ trailer during the search, was admitted in evidence, as were the bandannas, cash totalling $5,844, and various pictures of the items seized. The cash consisted of 294 one dollar bills, 118 five dollar bills, 71 ten dollar bills, 120 twenty dollar bills, 7 fifty dollar bills, and 15 one hundred dollar bills. The bank had baited four twenty dollar bills, but none were found in the trailer. No guns or bank wrappers were found.</p>
<p id="b1541-6">Agent Garay testified that a holster had been found in Maez’ truck, but the holster itself was never offered in evidence. Agent Denniston testified regarding statements Maez made during his interrogation. Maez said he had been driving his truck in the vicinity of the bank (picking up cans). Maez denied the robbery, and claimed that the money found in the trailer was his. Denniston also testified that Maez admitted that the cap was his, and then recanted after being told that it had been found outside the bank.</p>
<p id="b1541-7">The sole defense witness was Mrs. Maez. She testified that when her husband left the trailer on the morning of August 14, 1987, he was wearing tennis shoes, green khaki pants, a white shirt, and a yellow hat. Later that day she left. When she returned around 3:00 p.m. Maez was there, wearing the same pants and a t-shirt. Mrs. Maez brought three of her husband’s hats to court, all of which were admitted in evidence.</p>
<p id="b1541-12">The jury returned a guilty verdict. Maez filed a motion for a new trial, arguing that Griego’s identification was impermissibly suggestive and unreliable, violating his due process right to a fair trial. The trial court denied the motion and a timely notice of appeal was filed.</p>
<p id="b1541-13">II</p>
<p id="b1541-14">
<em>Analysis</em>
</p>
<p id="b1541-15">Maez argues that his arrest at his home without a warrant violated the Fourth Amendment and that evidence subsequently obtained was tainted. We first consider whether Maez’ arrest was lawful. If his arrest was unlawful, we must then decide whether the subsequent consents to search given by Mr. and Mrs. Maez and Maez’ incriminating statements were tainted by the unlawful arrest.</p>
<p id="b1541-16">A.</p>
<p id="b1541-17">
<em>Maez’ Warrantless Arrest</em>
</p>
<p id="b1541-18">The Fourth Amendment provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” In <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 576, 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1375" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1375, 1382</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), the Supreme Court held that, absent exigent circumstances, police officers may not enter an individual’s home without consent to make a warrantless routine felony arrest even with probable cause.<footnotemark>7</footnotemark> In the instant case, police officers, FBI agents and a SWAT team surrounded the Maez’ trailer, and with guns pointed at the home, asked him and his family to come <page-number citation-index="1" label="1450">*1450</page-number>out. They did and Maez was taken into custody.</p>
<p id="b1542-4">i</p>
<p id="b1542-5">
<em>The Application of Payton</em>
</p>
<p id="A5l">An arrest or seizure occurs “when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen....” <em>Terry v. Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, 19 n. 16, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, 1879 n. 16, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). <em>See also Dunaway v. New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U.S. 200</a></span>, 207 n. 6, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. 2248</a></span>, 2253 n. 6, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">60 L.Ed.2d 824</a></span> (1979). A show “of official authority such that ‘a reasonable person would have believed he was not free to leave’ ” indicates that an arrest has occurred. <em>Florida v. Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U.S. 491, 502</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1326" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1326</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span> (1983) (plurality opinion) (quoting <em>United States v. Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U.S. 544, 554</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#1877" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. 1870, 1877</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">64 L.Ed.2d 497</a></span> (1980) (opinion of Justice Stewart joined by Justice Rehnquist)). “Examples of circumstances that might indicate a seizure, even when the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer ... or the use of language or tone of voice indicating that compliance with the officer’s request might be compelled.” <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U.S. at 554</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#1877" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. at 1877</a></span>. “[T]he determination of whether an arrest has occurred is not dependent on whether the citizen is formally placed under arrest....” <em>United States v. Hatfield, </em><span class="citation" data-id="486411"><a href="/opinion/486411/united-states-v-richard-lee-hatfield/#1071" aria-description="Citation for case: United States v. Richard Lee Hatfield">815 F.2d 1068, 1071</a></span> (6th Cir.1987) (quoting <em>United States v. Hardnett, </em><span class="citation" data-id="478767"><a href="/opinion/478767/united-states-v-anthony-hardnett/#356" aria-description="Citation for case: United States v. Anthony Hardnett">804 F.2d 353, 356</a></span> (6th Cir.1986), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./479/1097/">479 U.S. 1097</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/1318/">107 S.Ct. 1318</a></span>, <span class="citation" data-id="9060060"><a href="/opinion/9066393/mahoney-v-south-dakota/" aria-description="Citation for case: Mahoney v. South Dakota">94 L.Ed.2d 171</a></span> (1987)).</p>
<p id="b1542-7">The government argues that Maez “chose to exit his home. He was arrested in a public place.” Brief of Appellee at 14. And the trial court found that Maez “was requested to come out of his home, or out of the trailer in which he was living and he was arrested after he came out into the open.” II R. 164. We cannot agree in light of the undisputed facts. The Albuquerque SWAT team had surrounded the Maez’ trailer with rifles pointed at the home. II R. 39-41; III R. 152. Over the loud speakers the occupants “were asked to remove themselves from the mobile home ...,” as Officer Whitson testified. II R. 39. Mrs. Maez saw the officers with rifles pointed at the house and her son being searched and handcuffed. She told her husband what had happened. “[H]e went to the door and he looked out and he said, [‘]We have to go outside,[’] and he got the baby and we were going outside.” Ill R. 152. Given the presence of some ten officers, the drawn weapons of the SWAT team surrounding the trailer, the use of the loudspeakers, and the frightening circumstances his family faced, a reasonable person would have believed he had to come out of the home and submit to the show of authority. Accordingly, we hold that Maez was arrested while in his home.<footnotemark>8</footnotemark></p>
<p id="b1542-11">The government strenuously argues that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>does not apply here because there was no warrantless entry into Maez’ home. It says that the Court drew a firm line at the threshold of the home. Brief of Appellee at 11-14. The contention has considerable force because <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>does make repeated references to entry such as “non-consensual entry into a suspect’s home....” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. at 576</a></span>, 100 S.Ct. at 1375. The Court said the Fourth Amendment “has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.” <em>Id. </em>at 590, 100 S.Ct. at 1382. And the Court noted that “ ‘physical entry of the home is the chief evil against which the wording of <page-number citation-index="1" label="1451">*1451</page-number>the Fourth Amendment is directed.’ ” <em>Id. </em>at 585, 100 S.Ct. at 1379 (quoting <em>United States v. United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. 297, 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#2135" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125, 2135</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">32 L.Ed.2d 752</a></span> (1972)).</p>
<p id="b1543-5">It is true also that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>involved cases where police officers, acting with probable cause but without a warrant, entered the defendants’ homes to make arrests. In the case of Payton, the officers used crowbars to break open the door and enter the apartment. <em>Payton, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. at 576-77</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1374" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1374-75</a></span>. In the case of Riddick, the officers knocked on the door of the house where Riddick lived, and when his son opened the door, entered and arrested Riddick. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#578" aria-description="Citation for case: Payton v. New York"><em>Id. </em>at 578</a></span>, 100 S.Ct. at 1376. In both cases there was physical entry. The government argues that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>does not condemn the arrest in this case because the officers did not physically enter the trailer.</p>
<p id="b1543-6">We are persuaded, however, by the decisions of the courts which have applied <em>Pay-ton </em>where a physical crossing of the threshold did not occur and their reasoning that the lack of physical entry alone is not dispositive. Those courts have held that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>is violated where there is such a show of force that a defendant comes out of a home under coercion and submits to being taken in custody. <em>United States v. Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d 890</a></span>, 893 and n. 1 (9th Cir.1985), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./476/1144/">476 U.S. 1144</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2255/">106 S.Ct. 2255</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/90/700/">90 L.Ed.2d 700</a></span> (1986); <em>United States v. Morgan, </em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1164" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1164</a></span> (6th Cir.1984), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985); <em>Scroggins v. State of Arkansas, </em><span class="citation" data-id="1509909"><a href="/opinion/1509909/scroggins-v-state/" aria-description="Citation for case: Scroggins v. State">276 Ark. 177</a></span>, <span class="citation" data-id="1509909"><a href="/opinion/1509909/scroggins-v-state/#37" aria-description="Citation for case: Scroggins v. State">633 S.W.2d 33, 37</a></span> (1982). <em>Cf. United States v. Edmondson, </em><span class="citation" data-id="471027"><a href="/opinion/471027/united-states-v-gerald-lee-edmondson/#1514" aria-description="Citation for case: United States v. Gerald Lee Edmondson">791 F.2d 1512, 1514-15</a></span> (11th Cir.1986) (FBI agents, with weapons drawn, knocked on door, directed occupant to open the door, which he did, and agents arrested him inside). In both <em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">Al-Azzawy</a></span> </em>and <em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>, </em>as in the case now before us, the police had surrounded the defendants’ homes and requested their exit by bullhorn. Both courts reasoned that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>was violated. <em>Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#893" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 893</a></span>; <em>Morgan, </em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1166</a></span>. “In these circumstances, it is the location of the arrested person, and not the arresting agents, that determines whether an arrest occurs within a home.” <em>United States v. Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#893" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 893</a></span>. We agree and think the important point is that in cases of physical intrusion, or coercion to leave the home, as in this case, the privacy of the home is effectively invaded. Commentators have endorsed such a view of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>where a defendant’s coming out of his home resulted from coercion. <em>See </em>2 LaFave, <em>Search and Seizure </em>§ 6.1(e) at 592-94 (2nd ed. 1987).</p>
<p id="b1543-8"><em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>recognizes that at the “very core [of the Fourth Amendment] stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U.S. at 589-590</a></span>, 100 S.Ct. at 1381-1382 (quoting <em>Silverman v. United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U.S. 505, 511</a></span>, <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#682" aria-description="Citation for case: Silverman v. United States">81 S.Ct. 679, 682</a></span>, <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">5 L.Ed.2d 734</a></span> (1961)). While “physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed” the Court has “refused to lock the Fourth Amendment into instances of actual physical trespass.” <em>United States v. United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. 297, 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#2135" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125, 2135</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">32 L.Ed.2d 752</a></span> (1972). Here the governmental intrusion, without consent and without a warrant, was in the form of extreme coercion which effected the arrest of Maez while he was in his home. We hold that the finding of the trial judge to the contrary is clearly erroneous and that, given the undisputed circumstances here, there was a violation of Maez’ Fourth Amendment rights.</p>
<p id="b1543-9">ii</p>
<p id="b1543-10">
<em>Exigent Circumstances</em>
</p>
<p id="b1543-11">In addition to its argument — which we have rejected — that there was no arrest of Maez in the home, the government says that both probable cause for the arrest and exigent circumstances existed so that there was in any event no violation of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>Brief of Appellee at 13, 15. Emergency conditions may make a warrantless search or arrest constitutional where probable cause exists, <em>see Welsh v. Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#749" aria-description="Citation for case: Welsh v. Wisconsin">466 U.S. 740, 749-50</a></span>, <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#2097" aria-description="Citation for case: Welsh v. Wisconsin">104 S.Ct. 2091, 2097-98</a></span>, <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">80 L.Ed.2d 732</a></span> (1984), and here Maez does not dispute the existence of such prob<page-number citation-index="1" label="1452">*1452</page-number>able cause. Moreover, <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>recognized that if exigent circumstances exist, the constitutional bar against a suspect’s arrest in his home without a warrant does not apply. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. at 590</a></span>, 100 S.Ct. at 1382. Here, however, Maez contends there was no assertion of exigency made in the trial court by the government’s law enforcement witnesses or its counsel. Appellant Maez’ Reply Brief at 12.<footnotemark>9</footnotemark> We agree and reject the government’s argument of exigent circumstances made for the first time on appeal.</p>
<p id="b1544-4">We cannot accept the government’s belated assertion of the exigent circumstances claim for basic reasons. Where police seek to enter a home without a warrant the state bears the burden of proving that sufficient exigency exists. <em>United States v. Aquino, </em><span class="citation" data-id="499820"><a href="/opinion/499820/united-states-v-luis-raul-aquino/#1271" aria-description="Citation for case: United States v. Luis Raul Aquino">836 F.2d 1268, 1271</a></span> (10th Cir.1988) (citing <em>Coolidge v. New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#455" aria-description="Citation for case: Coolidge v. New Hampshire">403 U.S. 443, 455</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#2032" aria-description="Citation for case: Coolidge v. New Hampshire">91 S.Ct. 2022, 2032</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">29 L.Ed.2d 564</a></span> (1971)). That burden is particularly heavy where the police seek to enter a suspect’s home or the home of a third person because warrantless seizures inside a home are presumptively unreasonable. <em>Aquino, </em><span class="citation" data-id="499820"><a href="/opinion/499820/united-states-v-luis-raul-aquino/" aria-description="Citation for case: United States v. Luis Raul Aquino">836 F.2d at 1271</a></span> (quoting <em>Payton, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U.S. at 586</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1380" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1380</a></span>). It is important that the facts on exigent circumstances be developed and that findings be made on them. <em>E.g., United States v. Cuaron, </em>700 F.2d at 586-91.</p>
<p id="b1544-5">In the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>opinion itself, the Supreme Court noted that while it was arguable that the warrantless arrest of Payton might have been justified by exigent circumstances, none of the lower courts had relied on any such justification and accordingly the Court had no occasion to consider such an emergency or dangerous situation. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U.S. at 583</a></span>, 100 S.Ct. at 1378. In <em>Steagald v. United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U.S. 204</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">101 S.Ct. 1642</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">68 L.Ed.2d 38</a></span> (1981), the government argued for the first time on appeal that the record did not clearly show that the petitioner, who was arrested in a third party’s house, had a reasonable expectation of privacy in the home. The Court declined to grant the government’s request for a remand for factual findings on the issue:</p>
<blockquote id="b1544-9">... [T]he Government was initially entitled to defend against petitioner’s charge of an unlawful search by asserting that petitioner lacked a reasonable expectation of privacy in the searched home, or that he consented to the search, <em>or that exigent circumstances justified the entry. The Government, however, may lose its right to raise factual issues of this sort before this Court </em>when it has made contrary assertions in the courts below, when it has acquiesced in contrary findings by those courts, <em>or when it has failed to raise such questions in a timely fashion during the litigation.</em></blockquote>
<blockquote id="b1544-10">We conclude that this is such a case. The Magistrate’s report on petitioner’s suppression motion, which was adopted by the District Court, characterized the issue as whether an arrest warrant was sufficient to justify the search of ‘the home of a third person’ for the subject of the warrant. App. 12. <em>The Government never sought to correct this characterization on appeal, and instead ac</em><page-number citation-index="1" label="1453">*1453</page-number><em>quiesced in the District Court’s view of petitioner’s Fourth Amendment claim.</em></blockquote>
<p id="ANxb"><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#209" aria-description="Citation for case: Steagald v. United States"><em>Id. </em>at 209</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#1646" aria-description="Citation for case: Steagald v. United States">101 S.Ct. at 1646</a></span> (emphasis added). Here, the government concedes in its brief that it did not argue the issue below. Brief of Appellee, 15-16. In fact, the defendant specifically argued below that exigent circumstances did not exist and the government did not dispute the argument.<footnotemark>10</footnotemark> Hence the district court had no reason to consider the issue.</p>
<p id="b1545-5">For these reasons, we must reject the government’s argument that its claim of exigent circumstances be taken up for the first time on this appeal.</p>
<p id="b1545-6">B.</p>
<p id="b1545-7">
<em>The Taint Caused by the Payton Violation</em>
</p>
<p id="b1545-8">Having determined that Maez' warrant-less arrest violated <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and the Fourth Amendment, we must now go on to consider whether the illegal arrest tainted the consents to search subsequently given by him and his wife and his custodial statements, or whether any taint was sufficiently removed and attenuated by intervening circumstances.</p>
<p id="b1545-9">i</p>
<p id="b1545-10">
<em>Mrs. Maez’ Consent to Search</em>
</p>
<p id="AFXS">We first consider whether the consent to search given by Mrs. Maez to the FBI was voluntary in fact so as to remove the taint of Maez’ unlawful arrest. A consent to search which is preceded by a Fourth Amendment violation is valid only if it is voluntary in fact. <em>United States v. Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d 1512, 1520-21</a></span> (10th Cir.1988); <em>United States v. Carson, </em><span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1151" aria-description="Citation for case: United States v. George L. Carson">793 F.2d 1141, 1151</a></span> (10th Cir.1986), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./479/914/">479 U.S. 914</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/315/">107 S.Ct. 315</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/289/">93 L.Ed.2d 289</a></span> (1986)). If the consent is not sufficiently an act of free will to purge the primary taint of the illegal arrest, it must be suppressed as fruit of the poisonous tree. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span> (quoting <em>Brown v. Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590, 601</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2260" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254, 2260</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span> (1975)).</p>
<p id="b1545-15">Without citation to authority, the government initially argues that because Mrs. Maez was not arrested,<footnotemark>11</footnotemark> her consent to search the trailer cannot be tainted by her husband’s prior illegal arrest. We disagree and think the issue, as stated in <em>Wong Sun v. United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471, 488</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#417" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407, 417</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963), is whether “granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.” This conclusion is mandated by the Supreme Court’s decision in <em>United States v. Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">435 U.S. 268</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. 1054</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">55 L.Ed.2d 268</a></span> (1978). <em>See also United States v. Howard, </em><span class="citation" data-id="493964"><a href="/opinion/493964/united-states-v-randy-ray-howard-united-states-of-america-v-robert-leroy/#556" aria-description="Citation for case: United States v. Randy Ray Howard, United States of...">828 F.2d 552, 556</a></span> (9th Cir.1987).</p>
<p id="b1545-16">In <em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">Ceccolini</a></span>, </em>the defendant (a businessman suspected of gambling) moved to suppress damaging statements of an employee, resulting from an unlawful search of his business premises. <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#269" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 269-72</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#1056" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1056-58</a></span>. The employee was not arrested. The Court rejected the government’s argument that “the testimony of a live witness should not be excluded at trial no matter how close and proximate the connection between it and a violation of the Fourth Amendment.” <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#274" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 274-75</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#1059" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059-60</a></span>. While the primary issue before the Court was whether a categorical distinction should be drawn between physical and verbal evidence found as the result of an unlawful search, the Court specifically noted that the witness whose testimony was at issue was not a <page-number citation-index="1" label="1454">*1454</page-number>defendant. <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 275, 277</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#1059" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059, 1060-61</a></span>. The Court nevertheless concluded that “ ‘verbal evidence which derives so immediately from an unlawful entry and an unauthorized arrest as the officers’ action in the present case is no less the “fruit” of the official illegality than the more common tangible fruits of the unwarranted intrusion.’ ” <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 275</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059</a></span> (quoting <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#485" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 485</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416</a></span>). Thus, the defendant could raise the taint issue as to the statements made by his employee. And while the witness in <em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">Ceccolini</a></span> </em>gave statements, as opposed to a consent to search, the same analysis is required here. The question is whether the statements of the witness (or in our case the consent) have “become so attenuated as to dissipate the taint.” <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#274" aria-description="Citation for case: United States v. Ceccolini">435 U.S. at 274</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059</a></span> (quoting <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 487, 491</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#417" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 417, 419</a></span>).</p>
<p id="b1546-4">Whether a consent to search preceded by a Fourth Amendment violation is sufficiently an act of free will to purge the primary taint of the illegal arrest depends upon whether it is voluntary in fact, which in turn depends upon the totality of circumstances surrounding the consent. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span> (citing <em>Schneckloth v. Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 248-49</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2058" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041, 2058-59</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973) and <em>Carson, </em><span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1149" aria-description="Citation for case: United States v. George L. Carson">793 F.2d at 1149</a></span>). In applying the <em>Schneckloth v. Bustamonte </em>voluntariness test to consents to search obtained subsequent to Fourth Amendment violations, this court has considered the three factors articulated in <em>Brown v. Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span> (1975), which apply to confessions. <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520-1521</a></span>. These factors include “[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, and particularly, the purpose and flagrancy of the official misconduct....” <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 603-04</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261-62</a></span> (citation omitted). Weighing these factors the court must decide the ultimate question whether the consent was sufficiently an act of free will to purge the primary taint of the illegal arrest. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span>. <em>See also Florida v. Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer">460 U.S. 491, 501</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1326" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1326</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span> (1983); <em>Wong Sun v. United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471, 486</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407, 416</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963); <em>Carson, </em><span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1152" aria-description="Citation for case: United States v. George L. Carson">793 F.2d at 1152</a></span>; <em>United States v. Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1458" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1458</a></span> (10th Cir.1985).</p>
<p id="b1546-12">As noted, the district judge found that Mrs. Maez’ consent was voluntarily and willingly given, although he expressed reluctance in making this finding.<footnotemark>12</footnotemark> The judge had also held there was no illegal arrest of Mr. Maez and thus had no reason to consider whether Mrs. Maez’ consent was sufficiently an act of free will to purge the primary taint of her husband’s unlawful arrest.</p>
<p id="b1546-13">When consent is obtained after an illegal arrest there must be a break in the causal connection between the illegality and the evidence thereby obtained. <em>Dunaway v. New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York">442 U.S. 200, 217-19</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#2259" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. 2248, 2259-60</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">60 L.Ed.2d 824</a></span> (1979). Here the violation of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and the undisputed train of events that followed compel us to hold that Mrs. Maez’ consent was tainted and invalid.<footnotemark>13</footnotemark> First, <page-number citation-index="1" label="1455">*1455</page-number>the proximity of the arrest and Mrs. Maez’ consents clearly indicate that taint of the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation was not purged. The FBI consent form was signed by Mrs. Maez at approximately 7:15 p.m., just after she had been summoned from the trailer by the bullhorn. And when she signed the form she was still in the trailer park. Ill R. 64-66.</p>
<p id="b1547-5">Second, the intervening circumstances indicate no purging of the primary taint of her husband’s illegal arrest. After leaving the trailer, Mrs. Maez was immediately asked by Albuquerque police officer Whit-son to sign the police department’s consent to search form. II R. 39. She was then approached by FBI agent Gyman who explained that the FBI wanted to search for money, weapons, and clothing, and the second consent form was signed. Ill R. 65-66. There were no intervening circumstances of any significance to purge the taint of the unlawful warrantless arrest of Maez.</p>
<p id="b1547-6">With respect to the purpose and flagrancy of the violation, the last <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>factor, it cannot be said that the officers purposefully violated <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>in the sense that they were aware of the impropriety of their actions, as was the case in <em>Brown. See Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 605</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>. The manner of the arrest, however, created a frightening scene for the Maez family as did Brown’s arrest.<footnotemark>14</footnotemark> <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.</a></span> </em>Agent Marrero, who was present when Mrs. Maez signed the FBI consent form, testified that she was crying and upset when she signed the form. She said that she signed the consent forms only because she had to. Before leaving the trailer Mrs. Maez had seen her fifteen year old son walking across the street with his hands in the air, and she watched as he was handcuffed. She was holding her two month old baby from the time she left the trailer throughout the signing of all three consent forms. II R. 41, 56-57. The undisputed facts clearly indicate that the taint of Maez’ arrest had not been purged when Mrs. Maez signed the FBI consent to search form and the police department consent.<footnotemark>15</footnotemark></p>
<p id="b1548-3"><page-number citation-index="1" label="1456">*1456</page-number>The government argues that Mrs. Maez was advised of her right to refuse consent, both orally and on the consent forms themselves. While this fact is indeed probative it is not dispositive of the voluntariness issue. <em>Schneckloth, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 227, 249</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2047" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2047-48, 2059</a></span>; <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1458" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1458-59</a></span>. We note that Mrs. Maez testified that she was told by the officers that if she refused consent they could simply get a warrant while she waited outside. Ill R. 156. This tends to undermine any salutary effect that advice of the right to refuse consent might have had. <em>United States v. Ocheltree, </em><span class="citation" data-id="9466775"><a href="/opinion/378921/united-states-v-jeffrey-dean-ocheltree/#993" aria-description="Citation for case: United States v. Jeffrey Dean Ocheltree">622 F.2d 992, 993-94</a></span> (9th Cir.1980).</p>
<p id="b1548-4">We hold that Maez’ illegal arrest tainted the subsequent consents to search the trailer given by Mrs. Maez and that her consents were not “ ‘sufficiently an act of free will to purge the primary taint’ [of the illegal arrest].” <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 602</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261</a></span> (quoting <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 486</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416</a></span>). The evidence seized pursuant to the FBI consent to search form, including the paper bag containing $5,844, the box of ammunition, two red bandannas, and the dark blue knit cap should have been suppressed, along with various photographs of the seized evidence.<footnotemark>16</footnotemark></p>
<p id="b1548-5">ii</p>
<p id="b1548-6">
<em>Maez’ Consent to Search</em>
</p>
<p id="A2f_">After exiting the trailer Maez was taken into custody by the Albuquerque police department. He was then turned over to the FBI and given <em>Miranda </em>warnings. He was taken to an interview room at the Albuquerque office of the FBI. He signed a waiver of rights form at 8:00 p.m., approximately 45 minutes after he had been taken into custody. Ill R. 110-111. He was then interrogated. During the interrogation he signed a consent to search form, authorizing a search of his pickup truck. Ill R. 112-115. Doc. 11, Exh. B. Officer Guyman searched the truck and found a holster. The district judge found that Maez, after being advised of his <em>Miranda </em>rights, “willingly and knowingly gave permission to search the Ford pickup....” Ill R. 165. As was true with respect to Mrs. Maez’ consent, the district judge did not discuss the effect of the prior illegal arrest, having held that no violation or unlawful arrest occurred.</p>
<p id="b1548-9">To determine whether Maez’ consent to search the truck was sufficiently an act of free will to purge the taint of his illegal arrest we again consider the three factors enunciated in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>. </em>The proximity of Maez’ arrest and his subsequent consent given 45 minutes later does not indicate that the taint of the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation was purged. In <em>Brown v. Illinois, </em>Brown’s initial statement was separated from his illegal arrest by less than two hours. <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 604</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>. The Court there held that Brown’s statement, like James Wah Toy’s statement in <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>, </em>was the fruit of the poisonous tree. <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Id.</a></span> </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 604-05</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262-63</a></span>. <em>See also Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 486-87</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416-17</a></span>. From the time Maez was taken to the FBI interview room he was in the custody of at least three officers, <em>see </em>III R. 109, and was initially in the presence of ten. <em>See Patino, </em>830 F.2d at 1418 (taint not purged where defendant continually in the company of one officer). His removal to the interview room does not indicate a break in the causal connection between his arrest and the subsequent consent. <em>Hayes v. Florida, </em><span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#816" aria-description="Citation for case: Hayes v. Florida">470 U.S. 811, 816</a></span>, <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#1647" aria-description="Citation for case: Hayes v. Florida">105 S.Ct. 1643, 1647</a></span>, <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/" aria-description="Citation for case: Hayes v. Florida">84 L.Ed.2d 705</a></span> (1985); <em>Dunaway, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U.S. at 212-13</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#2256" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. at 2256-57</a></span>.</p>
<p id="b1549-4"><page-number citation-index="1" label="1457">*1457</page-number>With respect to the second <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>factor, the effect of any intervening circumstances, the government does not point to and we do not find in the record any circumstances which would tend to dissipate the taint.<footnotemark>17</footnotemark> With respect to the last factor, the purpose and flagrancy of the official misconduct, the manner of the arrest was such that it would cause surprise, fright and confusion. <em>See Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 605</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>. Maez testified that he felt dizzy during his interrogation; he vomitted approximately three quarters of the way through the interview, as one of the FBI agents testified. Ill R. 135. Considering all three <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>factors, we hold that Maez’ consent to search the truck was not sufficiently an act of free will to purge the primary taint. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span>.</p>
<p id="b1549-6">The government notes that the consent form was signed after Maez had been advised of his <em>Miranda </em>rights, which is probative. But as the Supreme Court noted, “[i]f <em>Miranda </em>warnings, by themselves, were held to attenuate the taint of an unconstitutional arrest, regardless of how wanton and purposeful the Fourth Amendment violation, the effect of the exclusionary rule would be substantially diluted.” <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 602-03</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261</a></span>. <em>Miranda </em>warnings do not per se break the causal connection between an illegal arrest and evidence subsequently obtained. <em>See Dunaway, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#216" aria-description="Citation for case: Dunaway v. New York">442 U.S. at 216-17</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#2258" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. at 2258-59</a></span>.</p>
<p id="b1549-7">We hold that in these circumstances, notwithstanding the <em>Miranda </em>warnings, Maez’ consent was tainted by his prior illegal arrest and the testimony regarding the holster should have been suppressed.</p>
<p id="Av1j">III</p>
<p id="b1549-10">
<em>Maez’ Custodial Statements</em>
</p>
<p id="AVXA">During his interrogation Maez explained where he had been and what he had been doing on the day of the robbery. He said that he had been in possession of his pickup throughout the day and had been in the area of the bank. He admitted ownership of a cap shown to him during the interrogation by Agent Denniston. When told that the cap had been found outside the doors of the bank which had been robbed, Maez then denied ownership of the cap. Officer Denniston testified about those statements at trial and the cap was admitted. IV R. 153-160.</p>
<p id="b1549-11">The exculpatory and incriminating statements made by Maez during his interrogation are subject to the same analysis as the consent to search the truck. <em>See Taylor v. Alabama, </em><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama">457 U.S. 687, 690-94</a></span>, <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#2667" aria-description="Citation for case: Taylor v. Alabama">102 S.Ct. 2664, 2667-69</a></span>, <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">73 L.Ed.2d 314</a></span> (1982); <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#593" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 593-95</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2256" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2256-58</a></span>; <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 486-87</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416-17</a></span> (exculpatory and incriminating statements entitled to the protection of the exclusionary rule). Applying the same <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>analysis, which we made earlier, we hold that the statements should have been suppressed.<footnotemark>18</footnotemark></p>
<p id="b1549-12">IV</p>
<p id="b1549-13">The judgment is accordingly REVERSED and the case is REMANDED for further proceedings in accord with this opinion.</p>
<footnote label="1">
<p id="b1539-14">. It is not clear from the record precisely when the meeting took place. FBI agent Garay testified that it began around 4:00 p.m. Ill R. 130. Police officer Whitson said that he was at the meeting between 4:30 and 5:00 p.m. II R. 46. Agent Guyman said that he was at the meeting at 5:45 p.m. Ill R. 73.</p>
</footnote>
<footnote label="2">
<p id="b1539-15">. This first consent to search form was obtained so that the officers could enter the trailer to search for Maez, who had not yet exited. By the time the form was signed, he had exited.</p>
</footnote>
<footnote label="3">
<p id="b1539-16">. The form indicates that there is a constitutional right to deny permission to search the property. I R. 11, Exh. C.</p>
</footnote>
<footnote label="4">
<p id="b1539-17">. Mrs. Maez also testified that before she signed the Albuquerque police department consent form she was told that the officers did not have a warrant to search the house, but could get one. Ill R. 156. She thought that she would have to wait outside while they were getting the warrant if she did not sign the consent form. During this time Mrs. Maez was holding their baby. II R. 56; III R. 156, 158.</p>
</footnote>
<footnote label="5">
<p id="b1539-19">.The dissent’s focus on the voluntariness of the third consent and its quotation of testimony about it are misplaced. Nothing was seized pursuant to the third consent to search. Its validity is not at issue. We note this because the consent to search which is at issue, the second consent to search, preceded this third consent to search the automobile. In fact, the third consent form was signed over an hour after the search of the trailer. Ill R. 85. It is difficult to validate the second consent by events which occurred over an hour after it was signed.</p>
</footnote>
<footnote label="6">
<p id="b1540-8">. Maez said that he and his wife communicated with their heads regarding consent to search their trailer. "[S]he was reading the paper and she went like this, you know, and something like that (indicating), you know, to let me know if it’s all right if they can search the trailer. I told her *Well, it's your trailer. It’s up to you,’ and I shook my head up and down, to go ahead if she wanted to, because the trailer is under her name." Ill R. 145. Mrs. Maez said that she had no communication with her husband, although she was not asked specifically about nonverbal communication.</p>
</footnote>
<footnote label="7">
<p id="b1541-8">. A warrantless arrest in public with probable cause does not violate the Fourth Amendment, even though exigent circumstances do not exist. <em>United States v. Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#423" aria-description="Citation for case: United States v. Watson">423 U.S. 411, 423-24</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#827" aria-description="Citation for case: United States v. Watson">96 S.Ct. 820, 827-28</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">46 L.Ed.2d 598</a></span> (1976).</p>
</footnote>
<footnote label="8">
<p id="b1542-8">. As noted, the trial judge found that the "defendant was arrested legally. He came out of his— he was requested to come out of his home, or out of the trailer in which he was living and he was arrested after he came out into the open.” Ill R. 164.</p>
<p id="b1542-9">We review the findings on a motion to suppress under the clearly erroneous standard. <em>United States v. Alonso, </em><span class="citation" data-id="470081"><a href="/opinion/470081/united-states-v-fabio-alonso/#1493" aria-description="Citation for case: United States v. Fabio Alonso">790 F.2d 1489, 1493</a></span> (10th Cir.1986). However, where only an ultimate finding such as consent is made and there are undisputed underlying facts supporting a contrary conclusion, that conclusion may be drawn by the appellate court. <em>See United States v. Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448</a></span>, 1455 n. 7, and 1456 (10th Cir.1985) (citing <em>Brown v. Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590, 604</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254, 2262</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span> (1975)).</p>
</footnote>
<footnote label="9">
<p id="b1544-6">. The government argues that the record supports the existence of exigent circumstances because: (1) the police knew that one of the bank robbers was armed and had used the butt of his handgun to disable (knock unconscious) a bank customer; (2) a large sum of money had been stolen from a bank; (3) the police had physical descriptions of items worn by the robbers which might be destroyed; (4) Maez might seek to warn the other robber or seek assistance if he should become aware of the presence of the police; and (5) the police knew Maez was a heroin addict and a convicted felon.</p>
<p id="b1544-7">Citing <em>United States v. McConney, </em><span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195</a></span> (9th Cir.1984) (en banc), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./469/824/">469 U.S. 824</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984), the government argues that the existence of exigent circumstances is supported by the record and "dictated the arrest procedure.” Brief of Appellee, at pp. 15-16. <em><span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">McConney</a></span> </em>held that the "mixed question of exigency is reviewable de novo as a question of law.” <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1204" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d at 1204-05</a></span>. In <em>United States v. Cuaron, </em><span class="citation" data-id="9470300"><a href="/opinion/414423/united-states-v-frank-armando-cuaron/#586" aria-description="Citation for case: United States v. Frank Armando Cuaron">700 F.2d 582, 586</a></span> (10th Cir.1983), we said that in assessing whether the government’s burden demonstrating exigent circumstances was met, we "evaluate the circumstances as they would have appeared to prudent, cautious and trained officers.” (citations omitted). Since we conclude that the government waived its right to raise the issue of exigent circumstances on appeal for reasons stated in the text, we do not undertake an evaluation of the record.</p>
</footnote>
<footnote label="10">
<p id="b1545-11">. In his "Motion To Suppress Physical Evidence" the defendant argued that “[n]o exigent circumstances existed to justify the search of the residence_” IR. 8. The argument was again made in the "Memorandum Brief In Support of Defendant’s Motion To Suppress Physical Evidence and Motion To Suppress Statements." I R. 12, p. 6. The government’s response brief does not contest these arguments. I R. 11.</p>
</footnote>
<footnote label="11">
<p id="b1545-17">. We accept the government’s contention that Mrs. Maez was not arrested only for the sake of analysis, given our conclusion that Mr. Maez was arrested while in the trailer. If under the <em>Terry, Dunaway, Mendenhall, </em>and <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>arrest analysis, supra, Mr. Maez was arrested, it follows that Mrs. Maez was also arrested. She was in the same position.</p>
</footnote>
<footnote label="12">
<p id="b1546-5">. The court stated in part:</p>
<blockquote id="b1546-6">And I will find that while the circumstances may have been tense and while the environment may not have been that of the most ideal for considering the signing of a permission to search, that nevertheless she voluntarily and willingly gave the officers a permission to search. This is Government’s Exhibit 1.</blockquote>
<p id="b1546-7">Ill R. 164-165.</p>
</footnote>
<footnote label="13">
<p id="b1546-8">. The district court did not discuss the taint issue resulting from the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation. It is not our function to try facts or to substitute our judgment for that of the trial court in determining factual issues. <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1521" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1521</a></span>. However, where the proceedings below "resulted in a record of amply sufficient detail and depth from which the determination may be made,” the appellate court may conduct a taint analysis. <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 604</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>; quoted in <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1521</a></span> n. 10. <em>See also Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1458" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1458-59</a></span> (voluntariness determination held clearly erroneous where, although there was some evidence to support it, the entire record indicated that the defendant’s consent was tainted); <em>United States v. Patino, </em><span class="citation" data-id="495451"><a href="/opinion/495451/united-states-v-josan-wolf-patino/#1418" aria-description="Citation for case: United States v. Josan Wolf Patino">830 F.2d 1413, 1418-19</a></span> (7th Cir.1987).</p>
<p id="A7Go">The dissent argues that it is inappropriate for us to conduct a taint analysis, that only the trial <page-number citation-index="1" label="1455">*1455</page-number>court is in a position to assess credibility and discern truth and that the case should be remanded. But none of the facts relating to the proximity of the arrest and confession, the presence of intervening circumstances, or the flagrancy of official misconduct are in dispute. And these <em>are </em>the facts which are crucial to the taint analysis and upon which the government bore the burden of proof. <em>See Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 603-04</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261-62</a></span>; <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520-21</a></span>; <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1457" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1457-59</a></span>. The record is of "amply sufficient detail and depth” for us to conclude, as the Court did in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>, </em>that the taint of the Fourth Amendment violation was not purged. <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 603-04</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261-62</a></span>. The suppression hearing developed the circumstances in detail (II R. at 4-58; III R. at 62-162) and the basic facts vitiating the consents and statements are undisputed, as noted throughout our opinion.</p>
<p id="A8L">Applying the proper test of considering the whole record, and not merely relying on portions as the dissent does to support its view, we are left with the firm conviction that a mistake was made in finding the consents and Mr. Maez’ statements valid. The correct standard of review is whether "although there is evidence to support [the findings], the reviewing court on the entire evidence is left with the definite and firm conviction that a mistake has been committed.” <em>United States v. Grier, </em><span class="citation" data-id="517661"><a href="/opinion/517661/united-states-v-charles-h-grier-and-isaac-harper/#935" aria-description="Citation for case: United States v. Charles H. Grier and Isaac Harper">866 F.2d 908, 935</a></span> (7th Cir.1989) (quoting <em>United States v. D’Antoni, </em><span class="citation" data-id="511654"><a href="/opinion/511654/united-states-v-todd-a-dantoni/#978" aria-description="Citation for case: United States v. Todd A. D&#x27;Antoni">856 F.2d 975, 978-79</a></span> (7th Cir. 1988)).</p>
</footnote>
<footnote label="14">
<p id="b1547-10">. The dissent rejects the majority’s view that the circumstances created a frightening scene for the Maez family. The dissent’s reasoning is difficult to understand since the dissent accepts the majority’s holding that a violation of <em>Payton v. New York </em>occurred — that holding being grounded on the frightening scene that exerted "extreme coercion which effected the arrest of Maez while he was in his home.” <em>See supra </em>at p. 1451. Our <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>holding follows state and federal courts which hold that a <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation occurs where there is such a show of force that a defendant comes out of his home under coercion and submits to being taken into custody. <em>See supra </em>at p. 1451. The essential facts leading us to hold there was a frightening scene here were undisputed — the presence of ten armed SWAT team members with rifles pointed at the trailer, the request to come out over the bull horn, and the handcuffing of the fifteen year old son.</p>
</footnote>
<footnote label="15">
<p id="b1547-11">. The dissent contends that our opinion misreads the record. When reviewing the denial of a motion to suppress an appellate court must consider the evidence in the light most favorable to the government and must accept the trial court’s findings of fact unless clearly erroneous. <em>United States v. Jimenez, </em><span class="citation" data-id="516255"><a href="/opinion/516255/united-states-v-alfonso-steve-jimenez/#688" aria-description="Citation for case: United States v. Alfonso Steve Jimenez">864 F.2d 686, 688</a></span> (10th Cir.1988). But an appellate court must not simply consider from the record those facts which might support a trial court’s findings and ignore the record as a whole. A trial court’s factual <page-number citation-index="1" label="1456">*1456</page-number>determinations in criminal cases, as in civil cases, <em>see Anderson v. Bessemer City, </em><span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#573" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U.S. 564, 573</a></span>, <span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#1510" aria-description="Citation for case: Anderson v. City of Bessemer City">105 S.Ct. 1504, 1510</a></span>, <span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/" aria-description="Citation for case: Anderson v. City of Bessemer City">84 L.Ed.2d 518</a></span> (1985), may be clearly erroneous even where supported by some evidence, if on the whole record the court is left with a firm and definite conviction that a mistake has been committed. <em>United States v. Grier, </em><span class="citation" data-id="517661"><a href="/opinion/517661/united-states-v-charles-h-grier-and-isaac-harper/#935" aria-description="Citation for case: United States v. Charles H. Grier and Isaac Harper">866 F.2d 908, 935</a></span> (7th Cir.1989). <em>See e.g. United States </em>v. <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1457" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1457-59</a></span> (10th Cir.1985) (voluntariness determination held clearly erroneous where, although there was some evidence to support it, the entire record indicated that the defendant's consent was tainted).</p>
</footnote>
<footnote label="16">
<p id="b1548-11">. The photographs referred to Eire only those photographs of the tainted evidence which were admitted at trial.</p>
</footnote>
<footnote label="17">
<p id="b1549-8">. The government argues that because Maez refused to consent to a search of his home he was capable of exercising his rights, free from the taint of the illegal arrest. While relevant, this fact is not dispositive. In <em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/" aria-description="Citation for case: United States v. Miguel Angel Recalde">Recalde</a></span>, </em>the defendant refused to answer questions and yet subsequently signed a consent form; we nevertheless found that consent tainted. <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1459" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1459</a></span>.</p>
</footnote>
<footnote label="18">
<p id="b1549-9">. While Maez’ Fourth Amendment rights were violated and the evidence outlined in Part B should have been suppressed, we could affirm the conviction if the constitutional errors were harmless beyond a reasonable doubt. <em>Harrington v. California, </em><span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/#254" aria-description="Citation for case: Harrington v. California">395 U.S. 250, 254</a></span>, <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/#1728" aria-description="Citation for case: Harrington v. California">89 S.Ct. 1726, 1728</a></span>, <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">23 L.Ed.2d 284</a></span> (1969); <em>United States v. Morales Quinones, </em><span class="citation" data-id="483643"><a href="/opinion/483643/united-states-v-miguel-morales-quinones/#610" aria-description="Citation for case: United States v. Miguel Morales-Quinones">812 F.2d 604, 610</a></span> (10th Cir.1987). The government concedes, however, that if admission of the paper bag containing the money, the box of ammunition, the red bandannas, the photographs, and the dark blue knit cap was error, its admission cannot be considered harmless error. Brief of Appellee, p. 21.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Massenburg.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Massenburg
type: case
citation: "654 F.3d 480 (2011)"
parallel_cite: ""
neutral_cite: "2011 U.S. App. LEXIS 16849; 2011 WL 3559897"
court: 4th Cir. 2011
court_level: coa
circuit: ca4
year: 2011
date_decided: 2011-08-15
docket: 10-4209
authority_weight: "Binding in-circuit — 4th Cir."
treatment:
  field_i_validity: unverified
  as_of_content: null
  as_of_treatment: null
  composite_basis: unverified
  composite_basis_ref: null
  varies_by_point: false
  scope_note: "Frontier stub: treatment/progeny intentionally not derived until S6 promotion."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/223188/united-states-v-massenburg/"
  cluster_id: 223188
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Massenburg
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: Key
related:
  - "[[Collective Knowledge and the Fellow-Officer Rule]]"
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[United States v. Hensley]]"
  - "[[Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - collective-knowledge
  - fellow-officer-rule
  - terry-stop
  - reasonable-suspicion
  - frisk
  - fourth-circuit
holding: "The Fourth Circuit reversed the denial of suppression, holding that the nonconsensual frisk of Massenburg was not supported by reasonable suspicion and — critically for the collective-knowledge doctrine — that Officer Fries's uncommunicated observation of a 'bulge' could not be imputed to the frisking officer: the collective-knowledge (fellow-officer) doctrine substitutes an instructing officer's knowledge for the acting officer's only where the information was communicated, and does not permit after-the-fact aggregation of uncommunicated facts among officers."
---

# United States v. Massenburg

*654 F.3d 480 (4th Cir. 2011)* (No. 10-4209) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 223188 → majority opinion 223188 (654 F.3d 480, decided 2011-08-15, Davis, J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Responding to an anonymous tip that shots were fired in a high-crime Richmond neighborhood, officers encountered four young men — including Tyerail Massenburg — about four blocks from the reported gunfire. The men were cooperative and not evasive: one reported hearing shots two blocks away, and at least two consented to pat-downs. Massenburg stopped with the group but refused to consent to a frisk. Officer Gaines, thinking him "nervous" and "reluctant," and noting that Massenburg stood a foot or two off from the shoulder-to-shoulder others and did not make eye contact, frisked him without consent, recovering a firearm and marijuana. Notably, a second officer, Fries, had earlier seen "a small bulge" in Massenburg's jacket pocket but "didn't alert" Gaines — and Gaines never saw any signal from Fries and never cited the bulge as a basis for his suspicion. Charged under 18 U.S.C. § 922(g)(3) and 21 U.S.C. § 844, Massenburg moved to suppress; the district court denied the motion, and he entered a conditional guilty plea.

## Issue
Whether the nonconsensual frisk was supported by reasonable suspicion, and whether Officer Fries's uncommunicated observation of a bulge in Massenburg's pocket could be imputed to the frisking officer under the collective-knowledge (fellow-officer) doctrine to supply the suspicion the acting officer otherwise lacked.

## Rule
An officer must have reasonable, articulable suspicion of criminal activity before conducting a frisk, and a suspect's refusal to consent cannot itself justify a nonconsensual search. The collective-knowledge doctrine operates only "vertically," on communicated alerts or instructions: "the collective-knowledge doctrine simply directs us to substitute the knowledge of the *instructing officer or officers* for the knowledge of the *acting officer;* it does not permit us to aggregate bits and pieces of information from among myriad officers, nor does it apply outside the context of communicated alerts or instructions." — 654 F.3d at 493. ^pin-493

## Application
The individualized facts — standing a foot or two apart, declining eye contact, and reluctance to consent — did not add up to reasonable suspicion, and refusing consent could not be spun into it. The Government's fallback was to impute Officer Fries's observation of the "bulge" to Gaines, but Fries never communicated it and Gaines never saw a signal or relied on it. That is "horizontal" aggregation of uncommunicated facts, which the court declined to allow: no Supreme Court or Fourth Circuit case had ever extended the collective-knowledge doctrine beyond the context of information or instructions communicated vertically to acting officers, because after-the-fact aggregation would make a search's legality turn on hindsight and would deprive officers of any way to know *ex ante* whether a search is lawful. Fries's unshared observation therefore could not supply the missing suspicion.

## Conclusion
**[[Reading and Citing Cases#vacated|Vacated]], reversed, and [[Reading and Citing Cases#on-remand|remanded]].** Judge Davis wrote for the panel (Davis, Motz, and Keenan, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Massenburg* is a leading Fourth Circuit statement cabining the **collective-knowledge / fellow-officer** rule to its **vertical**, communicated form: an instructing officer's knowledge may be imputed to the acting officer only when it was actually conveyed, and courts may not retroactively pool officers' uncommunicated observations to manufacture reasonable suspicion or probable cause. Teach it alongside the *[[Whiteley v. Warden|Whiteley]]*/*[[United States v. Hensley|Hensley]]* line and the vertical-versus-horizontal distinction.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key*

## Sources
- [*United States v. Massenburg*, 654 F.3d 480 (4th Cir. 2011)](https://www.courtlistener.com/opinion/223188/united-states-v-massenburg/) — pinpoint: 493 (vertical-only / no-horizontal-aggregation holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ad3f36784d2fa26c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "654 F.3d 480 (2011)", "court": "4th Cir. 2011", "neutral_cite": "2011 U.S. App. LEXIS 16849; 2011 WL 3559897", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Massenburg", "year": "2011"}}
{"assertion_id": "0676f4cec851faea", "dimension": "support", "kind": "home_role", "locator": {"home": "Collective Knowledge and the Fellow-Officer Rule"}, "payload": {"home": "Collective Knowledge and the Fellow-Officer Rule", "role": "Key", "title": "United States v. Massenburg"}}
{"assertion_id": "57404cdbba7cdee2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Circuit reversed the denial of suppression, holding that the nonconsensual frisk of Massenburg was not supported by reasonable suspicion and — critically for the collective-knowledge doctrine — that Officer Fries's uncommunicated observation of a 'bulge' could not be imputed to the frisking officer: the collective-knowledge (fellow-officer) doctrine substitutes an instructing officer's knowledge for the acting officer's only where the information was communicated, and does not permit after-the-fact aggregation of uncommunicated facts among officers.", "title": "United States v. Massenburg"}}
{"assertion_id": "4a6477b96381ca41", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Massenburg"}}
{"assertion_id": "8c0b97186e089060", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Massenburg", "varies_by_point": "false"}}
```

### lake record — United States v. Massenburg

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Massenburg",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Massenburg",
    "case_name_short": "Massenburg",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Tyerail D. MASSENBURG, Defendant-Appellant",
    "input_case_name": "United States v. Massenburg",
    "court": "4th Cir. 2011",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2011-08-15",
    "year": 2011,
    "docket": "10-4209",
    "cluster_id": 223188,
    "lead_opinion_id": 223188,
    "sibling_ids": [],
    "absolute_url": "/opinion/223188/united-states-v-massenburg/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "654 F.3d 480",
      "volume": "654",
      "reporter": "F.3d",
      "page": "480",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. App. LEXIS 16849",
        "volume": "2011",
        "reporter": "U.S. App. LEXIS",
        "page": "16849",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 3559897",
        "volume": "2011",
        "reporter": "WL",
        "page": "3559897",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "654 F.3d 480",
        "volume": "654",
        "reporter": "F.3d",
        "page": "480",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. App. LEXIS 16849",
        "volume": "2011",
        "reporter": "U.S. App. LEXIS",
        "page": "16849",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 3559897",
        "volume": "2011",
        "reporter": "WL",
        "page": "3559897",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "654 F.3d 480",
    "official_selection": {
      "court_class": "coa",
      "selected": "654 F.3d 480",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [],
  "treatment": {
    "field_i_validity": "unverified",
    "as_of_content": null,
    "as_of_treatment": null,
    "composite_basis": "unverified",
    "composite_basis_ref": null,
    "varies_by_point": false,
    "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.",
    "point_overrides": [],
    "edges": [],
    "derivation": {}
  },
  "progeny": {
    "complete_query": null,
    "indexed_citing_opinions": null,
    "count_source": null,
    "per_sibling": [],
    "citation_count": null,
    "cache_path": null,
    "enumeration": null,
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": null,
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T05:55:49Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-massenburg--223188",
      "to_record_id": "United States v. Massenburg",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Massenburg

```
                       PUBLISHED


UNITED STATES COURT OF APPEALS
             FOR THE FOURTH CIRCUIT


UNITED STATES OF AMERICA,             
                Plaintiff-Appellee,
               v.                          No. 10-4209
TYERAIL D. MASSENBURG,
             Defendant-Appellant.
                                      
       Appeal from the United States District Court
     for the Eastern District of Virginia, at Richmond.
        Richard L. Williams, Senior District Judge.
                  (3:09-cr-00276-RLW-1)

                  Argued: May 13, 2011

                 Decided: August 15, 2011

  Before MOTZ, DAVIS, and KEENAN, Circuit Judges.



Vacated, reversed, and remanded by published opinion. Judge
Davis wrote the opinion, in which Judge Motz and Judge
Keenan joined.


                        COUNSEL

ARGUED: Caroline Swift Platt, OFFICE OF THE FED-
ERAL PUBLIC DEFENDER, Alexandria, Virginia, for
Appellant. Michael Arlen Jagels, OFFICE OF THE UNITED
STATES ATTORNEY, Richmond, Virginia, for Appellee.
2                UNITED STATES v. MASSENBURG
ON BRIEF: Michael S. Nachmanoff, Federal Public
Defender, Alexandria, Virginia, Carolyn V. Grady, Assistant
Federal Public Defender, OFFICE OF THE FEDERAL PUB-
LIC DEFENDER, Richmond, Virginia, for Appellant. Neil H.
MacBride, United States Attorney, Alexandria, Virginia, for
Appellee.


                         OPINION

DAVIS, Circuit Judge:

   In this appeal from a judgment of sentence, we are once
again called on to determine whether evidence seized during
a street encounter between law enforcement and citizens was
properly admitted into evidence during a subsequent criminal
prosecution. We conclude that the seizure of the evidence did
not comport with settled Fourth Amendment principles, and
we therefore reverse the district court’s denial of appellant’s
motion to suppress and remand for further proceedings.

   Responding one night to an anonymous tip that shots were
fired in a high-crime neighborhood, Richmond police encoun-
tered four young men, including appellant Tyerail Massen-
burg, four blocks from the reported gunfire. When an officer
approached them in a marked police car, the men were not
evasive; they continued walking forward, toward the car, and
voluntarily paused to speak with the officer upon the officer’s
request. In fact, they were cooperative: one of the men
reported that he had heard shots fired from a passing car two
blocks away and handed over his identification when asked;
and at least two of the men consented to voluntary pat-downs.
Appellant Massenburg stopped with his friends, but he
refused to consent to a frisk. As the officer interacting with
Massenburg testified, he first thought Massenburg nervous
when he began asking him to consent to a pat-down and
Massenburg was "real reluctant to give consent." J.A. 48.
                 UNITED STATES v. MASSENBURG                  3
Based on the fact that appellant stood a foot or two away from
the other men, who were shoulder-to-shoulder, and did not
make eye contact as the officer renewed his requests for a
consensual search, the officer undertook a nonconsensual
search. The search produced a firearm and some marijuana,
the subjects of the suppression motion at issue here.

   Charged with one count of possession of a firearm by a
drug user under 18 U.S.C. § 922(g)(3) and one count of pos-
session of marijuana under 21 U.S.C. § 844, Massenburg
moved to suppress the gun and drugs on the ground that the
officer’s frisk was unlawful. The district court denied that
motion, and Massenburg entered a conditional guilty plea,
reserving his right to appeal the suppression ruling.

   Before an officer can stop and frisk a citizen, she must have
"reasonable and articulable suspicion that the person seized is
engaged in criminal activity." Reid v. Georgia, 448 U.S. 438,
440 (1980). We recently warned against the Government’s
proffering "whatever facts are present, no matter how inno-
cent, as indicia of suspicious activity" and noted that we were
"deeply troubled by the way in which the Government
attempts to spin . . . mundane acts into a web of deception."
United States v. Foster, 634 F.3d 243, 248 (4th Cir. 2011).
This concern is only heightened when the "mundane acts"
emerge from the refusal to consent to a voluntary search. If
the important limitations on the "stop and frisk" regime
crafted by Terry v. Ohio, 392 U.S. 1 (1968), are not to
become dead letters, refusing to consent to a search cannot
itself justify a nonconsensual search.

                               I.

                              A.

  On the night of March 28, 2009, at 10:33 p.m., Richmond
City Police received an anonymous tip that shots had just
been fired. The caller reported eight shots fired "possibly" two
4                UNITED STATES v. MASSENBURG
blocks south of 14th and Hull Streets, a high-crime area in
which "drug activity as well as random gunfire" were
"usual[ ]." J.A. 46, 77. The caller said nothing more; in partic-
ular, he or she included no description of a suspect.

  Officers Stephen Gaines and Eric Fries responded to the
call and arrived at 14th and Hull at 10:48 p.m. They split up
and patrolled the area in marked police cars. Fries soon saw
four young black men, including appellant Massenburg, walk-
ing north at the corner of East 17th Street and Stockton Street,
four blocks west and two south of the intersection of 14th and
Hull and thus four blocks from the alleged origin of the shots.
They were walking in the direction of Fries’s marked car and
did not stop or change course when they saw it.

   Fries approached in his vehicle and asked, "hey guys, can
you stop for a second?" J.A. 31. The men stopped to talk with
him. Fries asked if they had heard gunfire, and one man
reported hearing shots fired from a vehicle on Maury Street,
two blocks south of their present location. Gaines arrived, the
two officers exited their vehicles, and they began taking the
men’s names. Fries then asked if they had weapons on them
and if they would consent to a pat-down. The four men were
now "all basically lined up in a row on the sidewalk," with the
man who reported hearing gunfire on Maury Street on the left
end of the line and Massenburg on the right. J.A. 32. Accord-
ing to Gaines, the three left-most men were "pretty much
shoulder-to-shoulder, and [Massenburg] was kind of offset
from the group" by a "foot or two," "give or take." J.A. 57.

   The man on the left consented to Fries’s request for a pat-
down, as did the man nearest him. Gaines began at the other
end of the line, asking Massenburg if he would consent to a
frisk. Gaines testified that Massenburg, in reply to the request,
"was kind of hesitant and stand-offish, and kind of real reluc-
tant to give consent to a pat down or a search of his person."
J.A. 48. Instead, "[h]e stated he did not have anything. You
don’t need to check me. Stood back and kind of air-patted
                 UNITED STATES v. MASSENBURG                   5
himself down, stating, trying to show he didn’t have any-
thing." J.A. 48. At this point Gaines insisted and patted
Massenburg down without his consent.

   Officer Fries testified that he had seen "a small bulge in the
left jacket pocket of Mr. Massenburg" prior to Officer
Gaines’s frisk, but he "didn’t alert" Gaines to it. J.A. 32, 42.
Officer Gaines, asked multiple times about the basis for his
suspicion of Massenburg, never indicated in his testimony
that he saw a sign or signal from Fries.

   During the frisk of Massenburg, Gaines felt the handle of
a firearm on Massenburg’s waist band (not in the jacket), and
Massenburg fled before Gaines could grab it. Gaines pursued
and directed him to drop the firearm, which Massenburg did,
dropping it on the grass. Massenburg ran another 250 feet
before Gaines caught up and arrested him. In addition to the
firearm, police recovered a small amount of marijuana on
Massenburg’s person.

                               B.

   Massenburg was charged with one count of possession of
a firearm by a drug user, in violation of 18 U.S.C.
§ 922(g)(3), and one count of possession of marijuana, in vio-
lation of 21 U.S.C. § 844. He filed a motion to suppress the
firearm and marijuana, arguing that Gaines lacked the reason-
able, particularized suspicion that he was engaged in criminal
activity necessary to authorize a nonconsensual frisk under
the Fourth and Fourteenth Amendments.

   At the suppression hearing, the Government presented few
objective bases for particularized suspicion of Massenburg. It
was only able to point to the following: (1) Massenburg and
his three friends were walking four blocks from the location
of the shots reported by the tipster, the only people the
responding officers encountered in the vicinity; and (2) sev-
eral observations made by Gaines of Massenburg’s allegedly
6                UNITED STATES v. MASSENBURG
"nervous behavior." In particular: (a) Massenburg was stand-
ing a foot or two from the other three men, who were
"shoulder-to-shoulder," J.A. 57; (b) he did not make eye con-
tact with Gaines as Gaines asked him to consent to a frisk;
and (c) he did not consent. Gaines’s testimony on these points
is instructive.

   Officer Gaines testified that "it wasn’t until actually I made
contact with him that I noticed nervous behavior from him."
J.A. 48. He elaborated:

       A: . . . We questioned if anybody had any weap-
    ons on them. The individuals besides Massenburg
    stated, we don’t have anything, you can check us.
    And Tyerail [Massenburg] was kind of hesitant and
    stand-offish, and kind of real reluctant to give con-
    sent to a pat down or a search of his person.

       ...

       Q: You indicated that Mr. Massenburg, you said,
    was acting nervously. What gave you that impres-
    sion?

       A: Like, I said, he was standing off from the three
    in the group from being questioned. He was reluc-
    tant, didn’t show any eye contact. Looked down.
    Once he stood back and stated, "I don’t need to get
    a pat-down." That kind of raised my suspicion a little
    further. And we were more persistent to find out
    whether he had weapons on his person.

J.A. 48-50. On cross-examination, Massenburg’s attorney
attempted to clarify Gaines’s ostensible particularized suspi-
cion concerning Massenburg.

    Q: And during your conversation with him, he
    wouldn’t look you in the eye?
                   UNITED STATES v. MASSENBURG               7
    A:   Correct.

    Q: And he just kept on saying, I don’t need to be
    patted down?

    A:   Yes.

    Q:   That made you more persistent?

    A:   It did.

    Q:   Because he didn’t want to be patted down?

    A: Correct. As I said, the others made statements
    when asked if they had weapons. Said, you can
    check me. And he was the only one to be reluctant.

    Q: You had no new information to know he was
    armed and dangerous but for the fact he didn’t want
    to be patted down?

    A: I mean the nature of the call and nature of [the]
    area.

    Q: You had no new information, did you, Officer,
    other than his repeated statements that he didn’t want
    to be patted down?

    A:   Besides the statements, the area of the call.

    Q: Right. Nothing new other than the area of the
    call?

    A:   Nothing, ma’am.

J.A. 57-59.
8                  UNITED STATES v. MASSENBURG
   The district court denied Massenburg’s suppression motion,
holding that the search was lawful. It found that reasonable
suspicion existed on the basis of six factors: (1) "a vague
report of shots fired"; (2) the four men were encountered
"roughly two blocks from the location of the reported shoot-
ing incident"1 and were the only people in the area; (3) this
was a "high-drug, high-crime area"; (4) Massenburg was "act-
ing nervously, looked down and refused to make eye contact
and stood off from the group"; (5) Massenburg "continued to
act strangely by making a series of two furtive move-
ments"—that is, he "took a step back away from Officer
Gaines, and he then began pantomiming a self pat-down
search"; (6) Gaines’s actions were informed by a "year’s
worth of practical experience serving as a law enforcement
officer." J.A. 73-75.

   After the denial of his suppression motion, Massenburg
entered a conditional guilty plea, reserving his right to appeal
the court’s ruling. Judgment was entered and he was sen-
tenced to 18 months in prison. He brought this timely appeal
challenging the suppression ruling. We exercise jurisdiction
pursuant to 28 U.S.C. § 1291.

                                  II.

  We review the district court’s legal conclusions de novo
and its factual findings for clear error. See United States v.
Day, 591 F.3d 679, 682 (4th Cir. 2010).

  To comport with the Fourth Amendment, even a "brief"
investigatory detention "must be supported at least by a rea-
sonable and articulable suspicion that the person seized is
    1
   The district court appears to have confused the location given by the
anonymous caller, which was four blocks from the encounter with
Massenburg, and the location reported by one of Massenburg’s compan-
ions, who acknowledged hearing shots fired from a passing car roughly
two blocks away.
                  UNITED STATES v. MASSENBURG                     9
engaged in criminal activity." Reid v. Georgia, 448 U.S. at
440; see United States v. Foster, 634 F.3d 243, 246 (4th Cir.
2011). Considering the totality of the circumstances, we are
to determine whether there was a sufficient objective, particu-
larized basis for suspecting the person seized of criminal
activity. United States v. Arvizu, 534 U.S. 266, 273 (2002).
Evidence that would support only "a mere ‘hunch’ is insuffi-
cient," though a reasonable basis need not establish probable
cause and may well "fall[ ] considerably short of satisfying a
preponderance of the evidence standard." Id. at 274 (quoting
Terry, 392 U.S. at 27); cf. United States v. Digiovanni, ___
F.3d ___, ___ (4th Cir. 2011) ("The reasonable suspicion
standard is an objective one, so we examine the facts within
the knowledge of [the officer] to determine the presence or
nonexistence of reasonable suspicion.").

   This quantum of suspicion is likewise required prior to a
frisk when the officer’s initial encounter with the citizen is
voluntary. See United States v. Burton, 228 F.3d 524, 528 (4th
Cir. 2000) ("[D]uring [initially consensual] police-citizen
encounters, an officer is not entitled, without additional justi-
fication, to conduct a protective search. To conduct such a
protective search, an officer must first have reasonable suspi-
cion supported by articulable facts that criminal activity may
be afoot."); see also Terry, 392 U.S. at 32-33 (Harlan, J., con-
curring) ("[I]f the frisk is justified in order to protect the offi-
cer during an encounter with a citizen, the officer must first
have constitutional grounds to insist on an encounter, to make
a forcible stop. . . . If and when a policeman has a right . . .
to disarm such a person for his own protection, he must first
have a right not to avoid him but to be in his presence. That
right must be more than the liberty . . . to address questions
to other persons, for ordinarily the person addressed has an
equal right to ignore his interrogator and walk away; he cer-
tainly need not submit to a frisk for the questioner’s protec-
tion.") (emphasis added). Thus we can assume without
deciding that Officer Fries’s initial conversation with Massen-
burg and his companions was consensual and that the Fourth
10               UNITED STATES v. MASSENBURG
Amendment was first implicated by Officer Gaines’s frisk of
Massenburg.

   We emphasize that the Constitution requires "a particular-
ized and objective basis for suspecting the particular person
stopped of criminal activity." United States v. Griffin, 589
F.3d 148, 152 (4th Cir. 2009) (quoting United States v. Cor-
tez, 449 U.S. 411, 417-18 (1981)) (emphases added). As the
Supreme Court noted in Cortez, "Chief Justice Warren, speak-
ing for the Court in Terry v. Ohio, said that, "[t]his demand
for specificity in the information upon which police action is
predicated is the central teaching of this Court’s Fourth
Amendment jurisprudence." Cortez, 449 U.S. at 418 (quoting
Terry, 392 U.S. at 21 n. 18 (emphasis added by Cortez)).
Indeed, as our late friend and colleague Judge Michael
reminded us in the 2010 Madison Lecture at New York Uni-
versity, "The Fourth Amendment owes its existence to furious
opposition in the American colonies to British search and sei-
zure practices . . . . Th[e] controversy [over the use of general
warrants] left citizens of the new American states with a deep-
dyed fear of discretionary searches permitted by general war-
rants and writs of assistance." The Honorable M. Blane
Michael, Reading the Fourth Amendment: Guidance from the
Mischief that Gave it Birth, 85 N.Y.U. L. Rev. 905, 907, 911-
12 (2010). Cf. Arizona v. Gant, 556 U.S. 332, ___, 129 S. Ct.
1710, 1720 (2009) (noting "the central concern underlying the
Fourth Amendment" is "the concern about giving police offi-
cers unbridled discretion to rummage at will among a per-
son’s private effects"); Delaware v. Prouse, 440 U.S. 648,
661 (1979) (holding unconstitutional a discretionary, suspi-
cionless stop for a "spot check" of a motorist’s license and
registration, emphasizing that "[t]his kind of standardless and
unconstrained discretion is the evil the Court has discerned
when in previous cases it has insisted that the discretion of the
official in the field be circumscribed").

                              III.

   On the facts of this case, there is precious little to sustain
the district court’s holding that Officer Gaines had reasonable,
                 UNITED STATES v. MASSENBURG                   11
particularized suspicion of Massenburg such that a noncon-
sensual frisk was lawful under the Fourth Amendment.
Among the six factors the district court cited in support of its
ruling is Officer Gaines’s one "year’s worth of practical expe-
rience serving as a law enforcement officer," which of course
is wholly unrelated to appellant. J.A. 74. The first three fac-
tors it listed—that the officers were responding to a "vague
report of shots fired," J.A. 73, that Massenburg was found in
the general vicinity (four blocks) of the reported site of the
gunfire, and that this encounter occurred in a high-crime
area—also do little to create particularized suspicion.

                               A.

   As the district court noted, the officers were responding to
"a vague report of shots fired." J.A. 73. This report was not
only "vague"—indicating only that eight shots were "possi-
bly" fired two blocks south of a certain intersection, J.A.
77—it was also anonymous. Reliance on an anonymous tip
may be reasonable where, "suitably corroborated, [it] exhibits
sufficient indicia of reliability." Florida v. J.L., 529 U.S. 266,
270 (2000). Yet here corroboration did not exist until one of
Massenburg’s       companions        reported     hearing    shots
fired—which cannot be said to increase reasonable suspicion
of the companion’s own party, especially since he also
reported that the shots were fired from a moving car (by
unknown parties) several blocks away. Like the tip of illegal
gun possession held unreliable in J.L., the tip here "provided
no predictive information and therefore left the police without
means to test the informant’s knowledge or credibility." Id. at
271. The tipster here disclosed her basis of knowledge—she
heard the shots herself—but little else. Though that disclosure
"enhance[s] the tip’s reliability," United States v. Perkins, 363
F.3d 317, 322 (4th Cir. 2004), we have held that even a
"nearly contemporaneous report" of a drug transaction the tip-
ster reportedly saw was unreliable in the absence of "[s]ome
corroboration," since "a fraudulent tipster can fabricate her
basis of knowledge," United States v. Reaves, 512 F.3d 123,
12                  UNITED STATES v. MASSENBURG
127-28 (4th Cir. 2008). Cf. Perkins 363 F.3d at 322, 327-28
(anonymous tip held sufficiently reliable where contempora-
neous viewing was corroborated by presence of a known drug
user in front of a known drug house and where tipster, though
she did not explicitly identify herself, was reasonably
assumed to be a known, reliable informant).2

   Furthermore, the poor match between the vague tip and the
individuals encountered substantially undermines reliance on
the tip for reasonable particularized suspicion of Massenburg.
The tip contained no physical description of the perpetrators
or any other outward identifying features; the only link
between the tip and Massenburg’s group was the group’s
rough proximity to the alleged site of the gunfire. The tipster
reported hearing shots two blocks south of the intersection of
Hull and 14th Streets; Massenburg and his friends were
encountered four blocks west of that intersection.
  2
    Though the threat of harassment that occupied the Court in J.L. may
seem substantially lessened here, where the tipster provided no physical
description or any other identifying information concerning the allegedly
armed person(s), this threat always exists in cases where the information
given by an anonymous tip is sufficiently specific to identify individuals.
See J.L., 529 U.S. at 272 (warning that an "automatic firearm exception
to our established reliability analysis would . . . enable any person seeking
to harass another to set in motion an intrusive, embarrassing police search
of the targeted person"). Since, for this issue to arise, individuals must
have been singled out on the basis of an anonymous tip, the possibility of
targeted harassment always exists, no matter how generic the tip itself may
appear. Just as the anonymous tipster in J.L. likely knew that there was
only one "young black male . . . wearing a plaid shirt" at the indicated bus
stop, id. at 268, the tipster here might well have known that the streets in
the indicated area were empty except for Massenburg and his friends.
   We also note that in Reaves, where we held an anonymous tip unreli-
able, the threat of harassment also appeared minimal. There the tipster,
who notified police after she saw what appeared to be a drug deal and
guided police as she followed the car of the alleged drug dealer for several
blocks, ceased pursuit when it came time to turn onto another street to
reach the market, where she was traveling on an errand. Reaves, 512 F.3d
at 125.
                  UNITED STATES v. MASSENBURG                    13
   Thus, while the district court appears to have heavily relied
on the fact that Massenburg and his companions were the only
people encountered as Officers Fries and Gaines responded to
the tip, this provides little basis for reasonable, particularized
suspicion of Massenburg. As J.L. and its progeny indicate,
when a tip lacks sufficient indicia of reliability, presence in
the area identified by the tip does not generate reasonable sus-
picion. Here, Massenburg was not even present at the site of
the alleged gunfire—he was encountered four blocks away.
Cf. United States v. Moore, 817 F.2d 1105, 1106 (4th Cir.
1987) (finding reasonable suspicion where only individual in
the vicinity was found "30 to 40 yards" from the entrance to
a building burglarized two to three minutes before, "moving
away from the scene of the crime"). To the extent that the tip,
together with Massenburg’s location, did identify his group
with particularity, J.L. and Reaves teach that an anonymous
tip, absent some corroboration or sufficient other indicia of
reliability, is not itself a reasonable basis for suspicion justify-
ing a nonconsensual frisk.

    The fact that this was a "high-drug, high-crime area" adds
little to the anonymous tip. J.A. 74. This counts among the
totality of the circumstances we consider, but it does little to
support the claimed particularized suspicion as to Massen-
burg. "An individual’s presence in an area of expected crimi-
nal activity, standing alone, is not enough to support a
reasonable, particularized suspicion that the person is commit-
ting a crime." Illinois v. Wardlow, 528 U.S. 119, 124 (2000);
see Brown v. Texas, 443 U.S. 47, 52 (1979). This is true
because "presence in a high crime neighborhood is a fact too
generic and susceptible to innocent explanation to satisfy the
reasonable suspicion inquiry." Wardlow, 528 U.S. at 139 (Ste-
vens, J., concurring in part and dissenting in part).

   As the officers testified, the city police "usually get com-
plaints . . . [for] random gunfire" in this area. J.A. 46. That
such incidents are common may make it more reasonable for
otherwise innocent behavior to appear suspicious to officers
14               UNITED STATES v. MASSENBURG
on the beat; but where a tip has already indicated that shots
were fired, the level of such crime in the neighborhood does
not provide an additional reasonable basis for suspicion of
particular individuals. That the tip concerned a common inci-
dent in a high-crime neighborhood does little to bolster its
reliability and less to create particularized suspicion. While
we appreciate the danger posed by firearms in our cities, the
Supreme Court has rejected "an automatic firearm exception
to our established reliability analysis." J.L., 529 U.S. at 272.
Like any other anonymous tip, a tip concerning firearms must
present certain indicia of reliability before it can provide a
basis for reasonable, particularized suspicion.

   To hold otherwise would be to authorize general searches
of persons on the street not unlike those conducted of old by
the crown against the colonists. Allowing officers to stop and
frisk any individuals in the neighborhood after even the most
generic of anonymous tips would be tantamount to permitting
a regime of general searches of virtually any individual resid-
ing in or found in high-crime neighborhoods, where "com-
plaints" of "random gunfire" in the night are all too "usual[ ]."
J.A. 46. James Otis famously decried general searches as "in-
struments of slavery . . . and villainy," which "place[ ] the lib-
erty of every man in the hands of every petty officer,"
warning against abuses by "[e]very man prompted by
revenge, ill humor, or wantonness." Timothy Lynch, In
Defense of the Exclusionary Rule, 23 Harv. J. L. & Pub. P.
711, 722 (2000) (quoting James Otis, Speech on the Writs of
Assistance (1761)). The Fourth Amendment, and the courts’
Fourth Amendment jurisprudence, is aimed at this evil. With-
out reasonable particularized suspicion of wrongdoing, such
searches and seizures offend the Constitution.

                               B.

   Reasonable suspicion determinations are made according to
the totality of the circumstances, and in light of the
above—Massenburg’s presence in a high-crime neighborhood
                 UNITED STATES v. MASSENBURG                  15
shortly after an (unreliable) tip concerning random gunfire in
the general vicinity—we give Officer Gaines a good deal of
leeway in his interpretation of Massenburg’s behavior. Yet, as
we recently reminded the Government in Foster, it cannot
simply proffer "whatever facts are present, no matter how
innocent, as indicia of suspicious activity." 634 F.3d at 248.
We expressed serious concerns there about "the way in which
the Government attempts to spin . . . mundane acts into a web
of deception," id.; these concerns are amplified when these
"mundane acts" are incident to the refusal to consent to a vol-
untary search.

   Officer Gaines made clear in his testimony that "it wasn’t
until actually I made contact with [Massenburg] that I noticed
nervous behavior from him." J.A. 48. His "blow-by-blow"
account of the encounter—which is not contradicted by Fries
or any other evidence—indicates that this "nervous behavior"
was his characterization of Massenburg’s repeated refusal to
consent to a voluntary pat-down: "We questioned if anybody
had any weapons on them. The individuals besides Massen-
burg stated, we don’t have anything, you can check us. And
Tyerail [Massenburg] was kind of hesitant and stand-offish,
and kind of real reluctant to give consent to a pat down or a
search of his person." J.A. 48. Gaines reiterated this when
asked a second time to describe Massenburg’s nervous behav-
ior:

    Like, I said, he was standing off from the three in the
    group from being questioned [sic]. He was reluctant,
    didn’t show any eye contact. Looked down. Once he
    stood back and stated, "I don’t need to get a pat-
    down. That kind of raised my suspicion a little fur-
    ther. And we were more persistent to find out
    whether he had weapons on his person.

J.A. 49-50 (emphases added). On cross-examination, Gaines
again explained that Massenburg "was the only one to be
reluctant" and admitted, when asked if it was true he had "no
16               UNITED STATES v. MASSENBURG
new information to know [Massenburg] was armed and dan-
gerous but for the fact he didn’t want to be patted down," that
there was "[n]othing" except Massenburg’s "statements" (he
"kept on saying, I don’t need to be patted down") and "the
area of the call." J.A. 57-59.

   The evidence Gaines cites for Massenburg’s nervousness is
slight: Massenburg was standing a foot or two from the other
three, who were lined up shoulder-to-shoulder, and "[l]ooked
down" or failed to make eye contact as Gaines repeatedly
asked him if he would consent to a search. The district court
accepted the Government’s characterization and deemed
Massenburg’s lack of eye contact "nervous behavior," yet as
Judge Gregory noted in United States v. Foreman, the Gov-
ernment often argues just the reverse: that it is suspicious
when "an individual looks or stares back at [officers]." 369
F.3d 776, 787 n.1 (4th Cir. 2004) (Gregory, J., concurring in
part and dissenting in part) (collecting cases); see also United
States v. McFarley, 991 F.2d 1188, 1192 (4th Cir. 1993) (not-
ing, in support of reasonable suspicion, that appellant and his
companion "each canvassed the terminal area, obtaining eye
contact with Officer Faulkenberry"). Given the complex real-
ity of citizen-police relationships in many cities, a young
man’s keeping his eyes down during a police encounter seems
just as likely to be a show of respect and an attempt to avoid
confrontation. Cf. State v. Scott, 412 So. 2d 988, 989 (La.
1982) ("Nervousness on the part of a black laborer when con-
fronted by an armed uniformed police officer does not seem
so unusual as to indicate guilt or criminal proclivity.")

   It is, of course, highly relevant when suspects "engage[ ] in
evasive behavior or act[ ] nervously." United States v. Mayo,
361 F.3d 802, 806 (4th Cir. 2004). Yet Massenburg did not
attempt to evade the officers—in fact, he and his companions
stopped to speak with Officer Fries, and one volunteered
information about recent gunfire. And looking down as an
officer persists in requesting consent to a search is a far cry
from the "unusually nervous behavior" we cited in United
                 UNITED STATES v. MASSENBURG                17
States v. Mayo, which included "shaking hands, heavy breath-
ing, and providing inconsistent answers." 861 F.3d at 806 (cit-
ing to United States v. McFarley, 991 F.2d 1188, 1192 (4th
Cir. 1993)). As the Tenth Circuit explained in United States
v. Salzano,

    [I]t is common for most people to exhibit signs of
    nervousness when confronted by a law enforcement
    officer whether or not the person is currently
    engaged in criminal activity. Thus, absent signs of
    nervousness beyond the norm, we will discount the
    detaining officer’s reliance on the detainee’s ner-
    vousness as a basis for reasonable suspicion.

158 F.3d 1107, 1113 (10th Cir. 1998) (internal quotation
marks and citations omitted). See also State v. Lee, 658
N.W.2d 669, 678-79 (Neb. 2003) ("[N]ervousness is of lim-
ited value" to reasonable suspicion analyses as "it is common
knowledge that most citizens whether innocent or guilty,
when confronted by a law enforcement officer who asks them
potentially incriminating questions are likely to exhibit some
signs of nervousness.").

   Indeed, the Supreme Court of Wyoming has applied this
commonsense principle to a situation much like this one,
where an officer was asking a motorist for consent to search
his car and, upon the motorist’s refusal, continued to ask him
"whether there was some reason he did not want the officer
looking in the vehicle." Damato v. State, 64 P.3d 700, 709
(Wyo. 2003). Reasoning that "[r]ealistically, few citizens
would not have become uncomfortable to some degree with
these questions," the court discounted as a "factor of no sig-
nificance" far more extreme signs of nervousness, including
the motorist’s "sweating heavily although it was a chilly day,
his carotid artery pulsating hard and fast, and an inability to
keep eye contact." Id.

  And as a reasonable response to continued police question-
ing, looking down is a good deal more innocent than the
18                 UNITED STATES v. MASSENBURG
defendant’s actions in United States v. Sprinkle, where the
defendant "put his head down and his hand up to his face as
if to avoid recognition" as an officer passed the car and then
"drove away as soon as the officers walked by." 106 F.3d 613,
617 (4th Cir. 1997). In Sprinkle we found no reasonable sus-
picion existed, even though the officers knew the defendant
to have been recently released from prison following narcotics
convictions, defendant was in a neighborhood known for drug
trafficking, and his evasive behavior was preceded by some-
one else’s entering the car and making gestures consistent
with a covert exchange ("huddling" with the two men’s hands
"close[ ] together" as if to pass something). Id. at 615-16.
When we have held that behavior far more extreme, by a
known narcotics dealer, in a high-crime area does not create
reasonable suspicion, it is difficult to imagine that Massen-
burg’s keeping his eyes down as he is asked repeatedly to
consent to a voluntary search would suffice.

   Indeed, we are especially conscious here of the fact that
Massenburg’s looking down was incident to his repeated
refusal to consent to a voluntary search. It cannot be doubted
that "a refusal to cooperate [with a police request to conduct
a voluntary search], without more, does not furnish the mini-
mal level of objective justification needed for a detention or
seizure." Florida v. Bostick, 501 U.S. 429, 437 (1991); see
also Mayo, 361 F.3d at 806 ("A suspect’s refusal to cooperate
with police, without more, does not satisfy Terry stop require-
ments."). If the ordinary response of the innocent upon being
asked to consent to a search—some mild nervous-
ness—sufficed to create reasonable suspicion, then Terry’s
reasonable suspicion requirement would become meaningless:
officers could ask a citizen for permission to conduct a volun-
tary search, and, if denied, they could use the citizen’s denial
as evidence of criminal activity and perform the search any-
way. Though, as an analytic matter, nervousness can be sepa-
rated from the denial of consent itself,3 to attempt to extricate
  3
   Indeed, the suggestion in Bostick that the refusal to cooperate may go
even some of the way toward establishing reasonable suspicion is best
read to refer to these sorts of indicators. See Bostick, 501 U.S. at 437.
                 UNITED STATES v. MASSENBURG                   19
the very mildest indicators of nervousness—such as a failure
to maintain eye contact during the refusal, as the officer
becomes "more persistent," J.A. 50—from the denial itself is
too nice a matter. Virtually any denial will be accompanied by
these mild reactions to the request, and thus virtually any
denial would go much of the way toward authorizing a non-
consensual search. This cannot be the case.

   As for the district court’s characterization of Massenburg’s
"self-pat down" as "[f]urtive movements," J.A. 74, it recalls
the Government’s suggestion in Foster that a man’s "sud-
den[ly]" "pop[ping] up" in a car with "his arms going hay-
wire" was suspicious. Foster, 634 F.3d at 247. There we
warned against "using whatever facts are present, no matter
how innocent, as indicia of suspicious activity," and reminded
the Government that it "must do more than simply label a
behavior as ‘suspicious’ to make it so": "The Government
must also be able to either articulate why a particular behavior
is suspicious or logically demonstrate, given the surrounding
circumstances, that the behavior is likely to be indicative of
some more sinister activity than may appear at first glance."
Id. at 248. No such demonstration has been forthcoming.
Massenburg’s "self-pat down" was interpreted as such by
Officer Gaines, and as an obvious attempt to satisfy him with-
out consenting to a frisk, it provided little basis, if any, as a
matter of constitutional analysis, for a reasonable suspicion of
wrongdoing.

   Genuinely suspicious behavior, occurring in a high-crime
neighborhood after a tip concerning gunfire, would certainly
justify a Terry stop and almost certainly a frisk of the
detainee. Where that tip is unreliable, the question becomes
closer. But where the accompanying behavior—the only sub-
stantial basis for particularized suspicion—is simply a mild
reaction to repeated requests to relinquish one’s constitutional
right to be free from unreasonable searches, it is clear that rea-
sonable, particularized suspicion of criminal activity does not
exist.
20                  UNITED STATES v. MASSENBURG
                                   IV.

    The Government suggests that under the collective-
knowledge doctrine (also called the "fellow officer" rule)
Officer Fries’s observation of a bulge in Massenburg’s jacket
pocket should be imputed to Officer Gaines, though, as the
Government concedes, Fries never "inform[ed]" Gaines about
it. Br. of Appellee, at 16 n.1.4 Because this novel application
of the doctrine would stretch it well beyond its purpose, we
decline to do so.

   The collective-knowledge doctrine, as enunciated by the
Supreme Court, holds that when an officer acts on an instruc-
tion from another officer, the act is justified if the instructing
officer had sufficient information to justify taking such action
herself; in this very limited sense, the instructing officer’s
knowledge is imputed to the acting officer. In Whiteley v.
Warden, the Supreme Court recognized in dicta that "officers
called upon to aid other officers in executing arrest warrants
are entitled to assume that the officers requesting aid" had
probable cause to support the issue of the warrant. 401 U.S.
560, 568 (1971). The Court applied this principle in United
States v. Hensley, holding that where officers stopped defen-
dant "in objective reliance" on a flyer from another depart-
ment that explained that defendant was wanted in connection
with an aggravated robbery and requested that other police
   4
     During cross-examination, Fries said that after seeing the bulge he
"made a movement towards him [Gaines? Massenburg?], but that is a
hand gesture, maybe," "[a]t best." J.A. 43. There was no serious conten-
tion by Fries that he communicated his observation to Gaines, see J.A. 32;
he admitted he "didn’t alert" Gaines. J.A. 43. The Government has con-
ceded this point: it relegates discussion of the bulge to a footnote, where
it admits that "before [Fries] could inform Officer Gaines, Gaines began
performing a pat-down of Massenburg." Br. of Appellee, at 16 n.1. More
importantly, Officer Gaines made no mention in his testimony of seeing
a sign or signal from Fries. Accordingly, we conclude that Fries’s observa-
tion of the "bulge" was not communicated to Gaines at the time he under-
took his search.
                 UNITED STATES v. MASSENBURG                  21
departments "pick up and hold" him, the stop was justified if
and only if the officers who issued the request had reasonable,
particularized suspicion sufficient to justify their own stop:

    We conclude that, if a flyer or bulletin has been
    issued on the basis of articulable facts supporting a
    reasonable suspicion that the wanted person has
    committed an offense, then reliance on that flyer or
    bulletin justifies a stop . . . . If the flyer has been
    issued in the absence of a reasonable suspicion, then
    a stop in the objective reliance upon it violates the
    Fourth Amendment.

469 U.S. 221, 223, 232 (1985) (internal citations omitted).

   We have applied the collective-knowledge doctrine often,
both before and after Whiteley and Hensley, and our case law
likewise establishes that the doctrine has a limited domain:
officers acting on the information and instructions of other
officers. In United States v. Pitt, federal police agent Wurms
learned through an informant that a large quantity of heroin
was being driven from New York City to Washington, D.C.
382 F.2d 322 (4th Cir. 1967). Agent Wurms informed fellow
agents, including Agent Worden, and instructed Baltimore
City police to intercept the car. Pitt was arrested by Agent
Worden, with the assistance of city police. Rejecting Pitt’s
claim that Worden lacked personal knowledge of the facts
constituting probable cause, we noted that "[p]robable cause
. . . can rest upon the collective knowledge of the police,
rather than solely on that of the officer who actually makes
the arrest." Id. at 324. Though this shorthand reference to the
collective-knowledge doctrine might be misleading out of
context, we went on in the next sentence to explain that "[i]t
was enough that Agent Wurms reported to Agent Worden the
substance of his telephone conversation with the informant."
Id.

  In our discussion of the doctrine in United States v. Laugh-
man, we made its limitations explicit:
22               UNITED STATES v. MASSENBURG
        The law seems to be clear that so long as the offi-
     cer who orders an arrest or search has knowledge of
     facts establishing probable cause, it is not necessary
     for the officers actually making the arrest or con-
     ducting the search to be personally aware of those
     facts.

        [N.3] When a superior officer orders another offi-
     cer to make an arrest, it is proper to consider the
     superior’s knowledge in determining whether there
     was probable cause. Likewise, when a group of
     agents in close communication with one another
     determines that it is proper to arrest an individual,
     the knowledge of the group that made the decision
     may be considered in determining probable cause,
     not just the knowledge of the individual officer who
     physically effected the arrest. [collecting cases]

618 F.2d 1067, 1072-73 & n.3 (4th Cir. 1980) (emphasis
added). Again, the collective-knowledge doctrine simply
directs us to substitute the knowledge of the instructing offi-
cer or officers for the knowledge of the acting officer; it does
not permit us to aggregate bits and pieces of information from
among myriad officers, nor does it apply outside the context
of communicated alerts or instructions. See 2 Wayne R.
LaFave, Search and Seizure § 3.5(b) (4th ed. 2004) ("[U]nder
the Whiteley rule (or, as it is sometimes termed, the ‘fellow
officer’ rule) police are in a limited sense ‘entitled to act’
upon the strength of a communication through official chan-
nels directing or requesting that an arrest be made."); cf.
United States v. Wells, 98 F.3d 808, 810 (4th Cir. 1996)
("[A]lthough the agent who actually seized the weapon pursu-
ant to the supervising agent’s instructions had no personal
knowledge that Wells was a convicted felon, it is sufficient
that the agents collectively had probable cause to believe the
weapon was evidence of a crime at the time of the seizure.")
(emphasis added); United States v. Gaither, 527 F.2d 456,
458 (4th Cir. 1975) (quoting Pitt to support application of
                 UNITED STATES v. MASSENBURG                   23
collective-knowledge doctrine where arresting officer was
"acting on" a "‘flash’ bulletin" issued by FBI agents who had
just observed a bank robbery).

   The Government would have us recognize a far more
expansive rule, which would look to the aggregated knowl-
edge of all officers involved to determine if reasonable suspi-
cion or probable cause existed. Under this proposed rule, it
would be irrelevant that no officer had sufficient information
to justify a search or seizure. It would be irrelevant that no
officer believed any other officer had pertinent information,
and thus that the acting officer undertook a search or seizure
she should have believed to be illegal. Indeed, as this aggrega-
tion rule is only required when the information at issue has
not been communicated to other officers (as the "aggregation"
it concerns is judicial, after-the-fact aggregation, not an acting
officer’s reliance on instructions or information conveyed by
another officer), this would be the paradigmatic case. Were
we to adopt this rule, the legality of the search would depend
solely on whether, after the fact, it turns out that the disparate
pieces of information held by different officers added up to
reasonable suspicion or probable cause.

   The Tenth Circuit has helpfully distinguished "‘vertical’
collective knowledge relationships in which [one] officer’s
conclusion [i]s conveyed" to others who effect the seizure
from a "‘horizontal’ collective knowledge relationship in
which the knowledge of several officers must be aggregated
to create probable cause." United States v. Rodriguez-
Rodriguez, 550 F.3d 1223, 1228 n.5 (10th Cir. 2008). No case
from the Supreme Court or from our own court has ever
expanded the collective-knowledge doctrine beyond the con-
text of information or instructions communicated
("vertically") to acting officers. Some of our sister courts have
authorized "horizontal" aggregation of uncommunicated
information. See United States v. Ramirez, 473 F.3d 1027,
1032-33 (9th Cir. 2007) (collecting cases). Because we
believe that this expansive aggregation rule strays from the
24               UNITED STATES v. MASSENBURG
purposes of the collective-knowledge doctrine recognized by
the Supreme Court and promotes none of the proper ends of
law enforcement, we decline to follow them.

   The rationale behind the Supreme Court’s collective-
knowledge doctrine is, as the Court noted in Hensley, "a mat-
ter of common sense: [the rule] minimizes the volume of
information concerning suspects that must be transmitted to
other jurisdictions [or officers] and enables police . . . to act
promptly in reliance on information from another jurisdiction
[or officer]." Hensley, 469 U.S. at 231. Thus, law enforcement
efficiency and responsiveness would be increased: Police
department search-and-seizure training would soon reflect
Hensley’s rule, and officers would learn that they need not
relay the information justifying an alert when issuing one nor
wait for such information upon hearing one.

   The Government’s proposed aggregation rule serves no
such ends. Because it jettisons the present requirement of
communication between an instructing and an acting officer,
officers would have no way of knowing before a search or
seizure whether the aggregation rule would make it legal, or
even how likely that is. The officer deciding whether or not
to perform a given search will simply know that she lacks
cause; in ordinary circumstances, she will have no way of
estimating the likelihood that her fellow officers hold enough
uncommunicated information to justify the search. And as an
officer will never know ex ante when the aggregation rule
might apply, the rule does not allow for useful shortcuts when
an officer knows an action to be legal, as Hensley did. Per-
haps an officer who knows she lacks cause for a search will
be more likely to roll the dice and conduct the search anyway,
in the hopes that uncommunicated information existed. But as
this would only create an incentive for officers to conduct
searches and seizures they believe are likely illegal, it would
be directly contrary to the purposes of longstanding Fourth
Amendment jurisprudence.
                   UNITED STATES v. MASSENBURG                       25
   As the Supreme Court recently reaffirmed in Davis v.
United States, the exclusionary rule’s "sole purpose . . . is to
deter future Fourth Amendment violations." ___ U.S. ___,
___, 131 S. Ct. 2419, 2426 (2011). It targets police action that
"exhibit[s] deliberate, reckless, or grossly negligent disregard
for Fourth Amendment rights"—in these cases the "deterrent
value of exclusion is strong and tends to outweigh the result-
ing costs." Id. at 2427 (internal quotation marks omitted). As
the Government’s proposed aggregation rule would do noth-
ing but redeem searches or seizures that the acting officers
should have believed at the time to be unlawful, it would
serve only to erode that deterrence. The Davis Court further
broadened the "good-faith" exception to the exclusionary rule,
recognizing that "when the police act with an objectively rea-
sonable good-faith belief that their conduct is lawful . . . the
deterrence rationale loses much of its force." Id. at 2427-28.
The Government’s proposed aggregation rule would per-
versely reward officers acting in bad faith according to the
result of an after-the-fact aggregation inquiry that is simply
academic.

   Though we have studied our sister circuits’ cases adopting
an aggregation rule, we can find no convincing defense of it.5
Most courts to have adopted the rule appear to have done so
simply on the grounds that officers working closely together
are "a team," United States v. Terry, 400 F.3d 575, 581 (8th
Cir. 2005); United States v. Edwards, 885 F.2d 377, 383 (7th
Cir. 1989), or, as one court put it, "on the theory that officers
working closely together during a stop or an arrest can be
treated as a single organism," United States v. Shareef, 100
F.3d 1491, 1504 & n.6 (10th Cir. 1996) (considering this
rationale after rejecting a general aggregation rule). But why?
We must frame the question in terms of deterrence, and for
the purposes of deterrence we look to each individual offi-
cer’s decision-making process as she considers executing a
  5
   For collections of these cases, see Ramirez, 473 F.3d at 1032-33, and
Bailey v. Newland, 263 F.3d 1022, 1031-32 (9th Cir. 2001).
26                   UNITED STATES v. MASSENBURG
search or effecting a seizure. Where officers working closely
together have not communicated pertinent information, the
acting officer weighs the costs and benefits of performing the
search in total ignorance of the existence of that informa-
tion—it is not known to her, so it cannot enter into the calcu-
lus. Therefore, for purposes of the exclusionary rule, that
additional information must be irrelevant.6

   Furthermore, if the "team" or "single organism" theory
should apply when the information at issue is incriminating,
should it not apply when the information is exculpatory? Yet,
we held in United States v. Holmes that the collective-
knowledge doctrine does not impute uncommunicated excul-
patory knowledge to fellow officers in similar circumstances.
376 F.3d 270, 277 n.3 (4th Cir. 2004). Likewise, though most
courts to allow aggregation have required "some degree of
communication" among the officers, Terry, 400 F.3d at 581,
see also Ramirez, 473 F.3d at 1032-33, it is not clear why. If
the Fourth Amendment is satisfied when, unbeknownst to the
officer conducting a search, a fellow officer on the scene has
the information necessary to justify it, why should the analy-
sis change when the other officer is not on the scene? Yet we
recently held in United States v. Blauvelt that information
held by others in the "law enforcement community at large"
is not imputed to members of a particular investigative team.
638 F.3d 281, 289 (4th Cir. 2011). Cf. People v. Hazelhurst,
662 P.2d 1081, 1087 (Colo. 1983) ("The fellow officer rule,
however, is not a means of creating probable cause by using
  6
    It is true that in the "vertical" collective-knowledge context the acting
officer is ignorant of the actual information held by the instructing officer.
But there the instruction itself communicates to the acting officer that the
instructing officer believes that she has sufficient information to justify the
action; after Hensley, police procedure can have the acting officer defer to
the instructing officer. Thus, the only officer making a reasonable suspi-
cion or probable cause determination is the instructing officer, and she will
be deterred by potential application of the exclusionary rule from ordering
an illegal search in the same way that an officer executing her own search
would be.
                 UNITED STATES v. MASSENBURG                  27
post hoc combinations of information available to the police.
The rule does not permit the police to cull its archives in
hopes of justifying an arrest which is not supported by proba-
ble cause.")

   Because we believe the aggregation rule runs contrary to
the Supreme Court’s Fourth Amendment jurisprudence,
would seriously erode the efficacy of the exclusionary rule’s
deterrent purposes, and serves none of the legitimate ends of
law enforcement, we reject it. We do not impute Officer
Fries’s observation of a "bulge" in Massenburg’s jacket
pocket to Officer Gaines, and thus, for the reasons stated
above, we hold that Gaines lacked the reasonable suspicion
needed to conduct a lawful nonconsensual frisk. Accordingly,
the district court erred when it failed to suppress the fruits of
that unlawful search.

                               V.

   For the reasons set forth herein, the judgment is vacated,
the district court’s order denying the motion to suppress is
reversed, and the case is remanded for further proceedings
consistent with this opinion.

                 VACATED, REVERSED, AND REMANDED

```

---

## GROUP: content/cases/United States v. Mathis.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Mathis"
type: case
citation: "767 F.3d 1264 (2014)"
parallel_cite: ""
neutral_cite: "2014 U.S. App. LEXIS 18297; 2014 WL 4724697"
court: "U.S. Court of Appeals, Eleventh Circuit"
court_level: coa
circuit: 11th
year: 2014
date_decided: 2014-09-24
docket: ""
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Mathis
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2736649/united-states-v-arnold-maurice-mathis/"
  cluster_id: 2736649
  opinion_id: 2736649
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Massachusetts v. Sheppard]]", "[[United States v. Jackson]]", "[[Riley v. California]]"]
aliases: ["United States v. Mathis (11th Cir. 2014)", "United States v. Arnold Maurice Mathis"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith-exception", "leon", "phone-search", "eleventh-circuit"]
holding: "Even assuming the search warrant lacked probable cause, the Leon good-faith exception applied: the detective had an objectively…"
lake:
  record_id: United States v. Mathis
  status: verified
  projected_at: 2026-07-06
---

# United States v. Mathis

*767 F.3d 1264 (11th Cir. 2014)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Detective Vizcarrondo obtained a warrant to search Arnold Mathis's smartphone, and the search produced incriminating evidence. Mathis moved to suppress, arguing the affidavit failed to establish probable cause to search the phone. The district court denied the motion; Mathis was convicted and appealed.

## Issue
Whether, even assuming the warrant to search Mathis's phone was not supported by probable cause, the [[United States v. Leon]] [[The Good-Faith Exception|good-faith exception]] barred suppression of the evidence obtained from the phone.

## Rule
Yes. Where officers obtain and execute a warrant in objectively reasonable, good-faith reliance, the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] applies even if the warrant turns out to lack probable cause. "Alternatively, even if the search warrant was not supported by probable cause, evidence obtained from the search of Mathis's phone was not subject to suppression under the good faith exception to the exclusionary rule." — 767 F.3d at 1276. ^pin-1276

The standard is objective good faith, judged by whether any of the *[[United States v. Leon|Leon]]* exceptions applies: "Because the officers engaged in 'objectively reasonable law enforcement activity and . . . acted in good faith when obtaining [the] search warrant . . . the *Leon* good faith exception applies.'" — *Id.* at 1277. ^pin-1277

## Application
On these facts good faith saved the phone evidence. Nothing showed that Detective Vizcarrondo "was dishonest or reckless in preparing her affidavit or that she could not have harbored an objectively reasonable belief in the existence of probable cause," so the *[[Franks v. Delaware|Franks]]* exception did not apply, and the affidavit was not so lacking in indicia of probable cause as to make reliance unreasonable. Because the officers acted in objectively reasonable, good-faith reliance on the warrant a magistrate had issued, the evidence from the phone search was admissible regardless of whether the warrant ultimately established probable cause — the court did not need to resolve the probable-cause question to affirm.

## Conclusion
Even assuming the warrant lacked probable cause, the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] applied and the phone evidence was admissible; the denial of suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- No negative subsequent treatment identified. The decision applies [[United States v. Leon]] / [[Massachusetts v. Sheppard]] objective good-faith reliance to a phone-search warrant, paralleling [[United States v. Jackson]] (8th Cir.); the underlying warrant requirement for cell phones is governed by [[Riley v. California]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Mathis*, 767 F.3d 1264 (11th Cir. 2014) — https://www.courtlistener.com/opinion/2736649/united-states-v-arnold-maurice-mathis/ — pinpoints: 1276, 1277.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "36ce565e5d02b325", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "767 F.3d 1264 (2014)", "court": "U.S. Court of Appeals, Eleventh Circuit", "neutral_cite": "2014 U.S. App. LEXIS 18297; 2014 WL 4724697", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Mathis", "year": "2014"}}
{"assertion_id": "a704b125d8c3d420", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "United States v. Mathis"}}
{"assertion_id": "f4c8fd51ffafcd5e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Even assuming the search warrant lacked probable cause, the Leon good-faith exception applied: the detective had an objectively…", "title": "United States v. Mathis"}}
{"assertion_id": "1b391ea2b364df8b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 11th Cir.", "title": "United States v. Mathis"}}
{"assertion_id": "c58128bb4d2e8559", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Mathis", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Mathis", "varies_by_point": "false"}}
```

### lake record — United States v. Mathis

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mathis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Arnold Maurice Mathis",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Arnold Maurice MATHIS, Defendant-Appellant",
    "input_case_name": "United States v. Mathis",
    "court": "U.S. Court of Appeals, Eleventh Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2014-09-24",
    "year": 2014,
    "docket": null,
    "cluster_id": 2736649,
    "lead_opinion_id": 2736649,
    "sibling_ids": [
      2736649
    ],
    "absolute_url": "/opinion/2736649/united-states-v-arnold-maurice-mathis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "767 F.3d 1264",
      "volume": "767",
      "reporter": "F.3d",
      "page": "1264",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. App. LEXIS 18297",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "18297",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4724697",
        "volume": "2014",
        "reporter": "WL",
        "page": "4724697",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "767 F.3d 1264",
        "volume": "767",
        "reporter": "F.3d",
        "page": "1264",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. App. LEXIS 18297",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "18297",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4724697",
        "volume": "2014",
        "reporter": "WL",
        "page": "4724697",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "767 F.3d 1264",
    "official_selection": {
      "court_class": "coa",
      "selected": "767 F.3d 1264",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1276",
      "page": null,
      "quote": "--- # United States v. Mathis *767 F.3d 1264 (11th Cir. 2014)* \u00b7 U.S. Court of Appeals, Eleventh Circuit \u00b7 **Binding in-circuit \u2014 11th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Detective Vizcarrondo obtained a warrant to search Arnold Mathis's smartphone, and the search produced incriminating evidence. Mathis moved to suppress, arguing the affidavit failed to establish probable cause to search the phone. The district court denied the motion; Mathis was convicted and appealed. ## Issue Whether, even assuming the warrant to search Mathis's phone was not supported by probable cause, the [[United States v. Leon]] good-faith exception barred suppression of the evidence obtained from the phone. ## Rule Yes. Where officers obtain and execute a warrant in objectively reasonable, good-faith reliance, the *Leon* good-faith exception applies even if the warrant turns out to lack probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1277",
      "page": null,
      "quote": "Because the officers engaged in 'objectively reasonable law enforcement activity and . . . acted in good faith when obtaining [the] search warrant . . . the *Leon* good faith exception applies.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Mathis",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wilson",
          "cluster_id": 10680152,
          "cite": [
            "884 S.E.2d 298",
            "315 Ga. 613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LEDBETTER (And Vice Versa)",
          "cluster_id": 10680366,
          "cite": [
            "899 S.E.2d 222",
            "318 Ga. 457"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Federal Trade Commission v. Steven J. Dorfman",
          "cluster_id": 9371119,
          "cite": [
            "58 F.4th 1322"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randal Wise",
          "cluster_id": 10382388,
          "cite": [
            "134 F.4th 745"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Washington v. Zachary James Fairley",
          "cluster_id": 4727836,
          "cite": [
            "457 P.3d 1150"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dusty J. Cowan v. State of Alaska",
          "cluster_id": 10161720,
          "cite": [
            "559 P.3d 627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2736649) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(2736649)",
        "reviewed": 6,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(2736649)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2736649)",
    "indexed_citing_opinions": 6,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2736649,
        "count": 6,
        "count_source": "search"
      }
    ],
    "citation_count": 53,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-mathis.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 6,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2736649,
        "cited_id": 1990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 75800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 75908,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 76294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 76840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 77529,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 78058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 78534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 118188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 118381,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 145922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 147511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 204288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 392842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 396175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 608150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 622315,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 626752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 657263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 670638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 677467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 772987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 790000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 903985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 1840522,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T01:29:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:30:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:30:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:30:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Mathis

```
           Case: 13-13109   Date Filed: 09/24/2014   Page: 1 of 42


                                                                     [PUBLISH]



            IN THE UNITED STATES COURT OF APPEALS

                     FOR THE ELEVENTH CIRCUIT
                       ________________________

                             No. 13-13109
                       ________________________

               D.C. Docket No. 8:12-cr-00457-SCB-MAP-1



UNITED STATES OF AMERICA,

                                                               Plaintiff-Appellee,

                                   versus

ARNOLD MAURICE MATHIS,

                                                          Defendant-Appellant.

                       ________________________

                Appeal from the United States District Court
                    for the Middle District of Florida
                      ________________________

                            (September 24, 2014)



Before HULL, MARCUS and BLACK, Circuit Judges.

PER CURIAM:
              Case: 13-13109     Date Filed: 09/24/2014    Page: 2 of 42


      Arnold Maurice Mathis, a registered sex offender, enticed a minor to engage

in sexual activity in 2004. Seven years later, in 2011, he attempted to convince a

minor to take sexually explicit pictures and send them to him via text message, and

he actually succeeded in convincing a different minor to do so. Based on this

conduct, a jury convicted Mathis of several child exploitation offenses and the

district court sentenced him to a 480-month total term of imprisonment. On

appeal, Mathis raises numerous challenges to his convictions and sentences, which

we address in turn. After a thorough review of the record and consideration of the

parties’ briefs, and with the benefit of oral argument, we affirm Mathis’s

convictions and sentences. However, we remand to the district court for the

limited purpose of correcting a scrivener’s error in the judgment.

                                 I. BACKGROUND

A. Mathis’s Sexual Abuse of Jarvis J. and Subsequent Arrest

      In 2004, Mathis, who was approximately 34 years old, approached Jarvis J.

after a high school basketball game. Jarvis was 14 years old at the time. Mathis

introduced himself as Pastor Maurice and gave Jarvis approximately $20 to

purchase items at the concession stand. Mathis also told Jarvis that he was willing

to act as a father figure or mentor and that he could assist Jarvis financially by

helping him purchase shoes and clothes. Mathis gave Jarvis his cell phone number

and told Jarvis to call him the next day.


                                            2
              Case: 13-13109    Date Filed: 09/24/2014   Page: 3 of 42


      At some point the following week, Jarvis met Mathis and Mathis gave him a

pair of shoes, a shirt, and $100 to purchase a prepaid cell phone. Jarvis

subsequently purchased a cell phone, phone card, and minutes for the phone.

Jarvis used the phone to talk to Mathis, and the two met a few days after Jarvis

bought the phone. On that occasion, after going to a fast food restaurant, Mathis

took Jarvis to Mathis’s house where Mathis eventually goaded Jarvis into showing

him his penis. Mathis then performed oral sex on Jarvis. Mathis told Jarvis not to

tell anyone about the encounter and promised that he would give Jarvis money and

take care of him. Mathis took Jarvis to an ATM and gave him money.

      Following the incident at Mathis’s house, Jarvis used his cell phone to talk

to Mathis on a daily basis. During his conversations with Jarvis, Mathis became

more explicit and told Jarvis that he wanted to engage in sexual conduct with him.

Mathis eventually met Jarvis again and, after having a meal, Mathis took Jarvis to

Mathis’s house. Mathis performed oral sex on Jarvis and instructed him to

perform anal sex on Mathis. Jarvis complied with Mathis’s instructions.

      Sometime thereafter, Mathis talked to Jarvis on the phone about traveling to

Orlando to go bowling. When Mathis arrived to pick up Jarvis, Jarvis observed

another man in the car with Mathis as well as a boy around Jarvis’s own age. The

group drove to Orlando, but instead of going bowling, they went to a diner and




                                          3
              Case: 13-13109     Date Filed: 09/24/2014   Page: 4 of 42


then a hotel. At the hotel, Mathis performed oral sex on Jarvis and had Jarvis

perform anal sex on him while the other boy performed anal sex on the other man.

      Subsequently, Mathis took Jarvis to a townhouse in Lakeland and tried to

perform oral sex on him, but Jarvis resisted. Jarvis did not tell anyone about his

experiences with Mathis until December 2011, nearly seven years later. At that

time, Jarvis ran into the other man who had gone with him and Mathis to Orlando.

After arguing with the man in a store, Jarvis talked to his pastor and then went to

the Polk County Sheriff’s Office. At the sheriff’s office, Jarvis told Sergeant

James Evans and Detective Zoe Vizcarrondo about his experiences with Mathis.

Detective Vizcarrondo asked Jarvis to make a recorded phone call to Mathis.

During the call, Mathis acknowledged that he had engaged in sexual conduct with

Jarvis.

      A few hours after Jarvis’s recorded call with Mathis, law enforcement

officers arrested Mathis. During the arrest, officers seized Mathis’s cell phone,

which was a Sprint smartphone.

B. The Search of Mathis’s Smartphone

      After Mathis was arrested, Detective Vizcarrondo obtained a search warrant

for the contents of his cell phone. In support of her application for a search

warrant, Detective Vizcarrondo submitted an affidavit which provided in pertinent

part that the victim in the case, Jarvis, was 21 years old and that when he was


                                          4
              Case: 13-13109     Date Filed: 09/24/2014   Page: 5 of 42


between the ages of 14 and 15, Mathis sexually abused him. The affidavit

explained that, according to Jarvis, Mathis continuously called him from Mathis’s

cell phone and that Mathis would also communicate with him via text message.

Detective Vizcarrondo stated that Mathis had maintained the same phone number

since the time of the crimes, and that a forensic examination of the phone would

reveal a log of the recorded phone call between Jarvis and Mathis. In addition,

Detective Vizcarrondo averred that, based on her knowledge, experience, and

training in child sexual abuse investigations,

      [T]here are certain characteristics common to many individuals
      involved in the communication made between the suspect and victim
      of such investigations. These suspects sometimes possess and
      maintain “soft copies” of such communication in the privacy and
      security of their personal cell phones and retain these items for many
      years. They often conceal such correspondence and often maintain
      lists of names, addresses, and telephone numbers of individuals with
      whom they have been in contact with and who share the same
      interests in encounters, sexual in nature, with children.

      Glenn Hayes, a computer forensics examiner with the Polk County Sheriff’s

Office, initially examined Mathis’s cell phone on December 22, 2011. During the

initial examination of Mathis’s phone, Hayes was able to retrieve contact lists,

phone logs, and text messages, but could not retrieve multimedia messages—i.e.,

text messages to which a file was attached. Hayes examined the phone a second

time on August 1, 2012. During the second examination, Hayes was able to

retrieve all of the same data as before in addition to multimedia messages. Based


                                          5
              Case: 13-13109     Date Filed: 09/24/2014   Page: 6 of 42


on information obtained from Mathis’s cell phone, law enforcement officers

believed that he had either persuaded or attempted to persuade two other minors—

Jerel A. and Harold J.—to send him sexually explicit pictures of themselves.

C. The Indictment

      A grand jury returned a second superseding indictment charging Mathis with

(1) knowingly employing, using, persuading, inducing, enticing, and coercing

Jerel A., a minor, to engage in sexually explicit conduct for the purpose of

producing a visual depiction of such conduct, and attempting to do so, in violation

of 18 U.S.C. § 2251(a) (Count One); (2) knowingly attempting to employ, use,

persuade, induce, entice and coerce Harold J., a minor, to engage in sexually

explicit conduct for the purpose of producing a visual depiction of such conduct, in

violation of 18 U.S.C. § 2251(a) (Count Two); (3) knowingly persuading,

inducing, and enticing Jarvis J., a minor, to engage in sexual activity, and

attempting to do so, in violation of 18 U.S.C. § 2422(b) (Count Three); and

(4) committing the offenses in Counts One through Three while he was required to

register as a sex offender under the laws of Florida, in violation of 18 U.S.C.

§ 2260A (Count Four).

D. Mathis’s Motion to Suppress

      Prior to trial, Mathis moved to suppress the evidence obtained from the

search of his cell phone. Mathis argued Detective Vizcarrondo’s affidavit in


                                          6
              Case: 13-13109    Date Filed: 09/24/2014    Page: 7 of 42


support of the search warrant was misleading because it indicated Mathis used his

cell phone to commit crimes against Jarvis J., even though the events giving rise to

the charge occurred in 2004, when Mathis had a different cell phone. Mathis

further maintained the search warrant was not supported by probable cause to

believe evidence of an offense committed seven years prior to the search would be

found on Mathis’s current smartphone; that the information on which the warrant

was based was stale; and that once law enforcement officials determined the

smartphone did not contain text messages from before 2011, any further search

exceeded the scope of the warrant.

      At a suppression hearing held before a magistrate judge, Sergeant Evans

testified that when he spoke with Jarvis J. at the Polk County Sheriff’s Office in

December 2011, Jarvis stated that, in 2004 and 2005, Mathis would communicate

with him on the phone, in person, and via text message. Sergeant Evans stated that

he knew Mathis did not have the same cell phone in 2011 as he did in 2004.

Nevertheless, based on his training and experience, Sergeant Evans believed

evidence of a crime committed in 2004 could be present on a cell phone in 2011.

For instance, the phone could contain soft copies of information, digital images

and media could be placed on a phone from an external source, and digital media

could be transferred from one phone to another with a media card. Sergeant Evans

further testified that, in his experience, individuals who sexually abuse minors


                                          7
             Case: 13-13109     Date Filed: 09/24/2014   Page: 8 of 42


generally maintain soft copies of evidence on their cell phones. Sergeant Evans

acknowledged there was no indication that Mathis took photographs of Jarvis with

his cell phone or that any text messages between Mathis and Jarvis were sexual in

nature.

      Adam Sharp, an expert in data recovery and the forensic analysis of

computers and cell phones, testified it was highly improbable that text messages

sent from a phone in 2004 would be present on a smartphone in 2011. Sharp

explained that cell phones in 2004 could hold approximately one hundred text

messages and that once the phone’s capacity was reached, old text messages would

be cleared when new text messages were received. Furthermore, it was not

generally possible to transfer information from one cell phone to another if an

individual changed cell phone carriers. In addition, data was stored differently in

2004 than in 2011, and various other factors would have made it improbable that a

text message from a cell phone in 2004 would be transferred to subsequent cell

phones.

      The magistrate judge issued a report and recommendation (R&R),

concluding Mathis’s motion to suppress should be denied because Detective

Vizcarrondo did not recklessly mislead the state court judge who issued the search

warrant, and because law enforcement acted in good faith reliance on the warrant




                                          8
               Case: 13-13109   Date Filed: 09/24/2014     Page: 9 of 42


when searching Mathis’s cell phone. Over Mathis’s objections, the district court

adopted the magistrate judge’s R&R and denied the motion to suppress.

E. The Trial

      At trial, Jarvis J. testified and recounted his interactions with Mathis in

detail. In addition, the Government introduced a copy of Mathis’s 1995 judgment

from the Circuit Court for Leon County, which showed that he entered a plea of

nolo contendere to lewd and lascivious assault on a child, in violation of § 800.04

of the Florida Statutes. The Government also introduced a judgment from

February 21, 1997, establishing that Mathis was sentenced to 48 months’

imprisonment for violating his probation on his § 800.04 offense.

      While Hayes was testifying at trial, Mathis renewed his motion to suppress,

arguing for the first time that the second search of his cell phone in August 2012

was not authorized by the search warrant. In response, the Government elicited

testimony from Hayes, who explained that during the December 2011 examination,

the device he used to remove information from Mathis’s cell phone was not able to

extract multimedia messages from the phone. However, the device was

subsequently updated numerous times before Hayes examined the phone again in

August 2012. After the device was updated, Hayes was able to retrieve everything

from Mathis’s phone, including multimedia messages. The district court denied

the renewed motion to suppress. The court explained that law enforcement officers


                                          9
             Case: 13-13109      Date Filed: 09/24/2014    Page: 10 of 42


had not acted in bad faith in waiting approximately eight months before searching

the phone a second time and, regardless, Mathis was not prejudiced by the delay.

      During the third day of trial, the Assistant United States Attorney (AUSA)

advised the district court that earlier that morning she was in the elevator with

Sergeant Evans when a juror stepped into the elevator as the doors were closing.

Before the AUSA noticed the juror, the AUSA told Sergeant Evans that she had

been at work until 2:00 a.m., to which Sergeant Evans responded, “[t]hat sucks.”

      Michelle Gonzalez, a special agent with the Federal Bureau of Investigation

(FBI), testified that, based on their birth certificates, Jerel A. and Harold J. turned

16 years old in 2011, and that Jarvis J. was 14 years old in 2004.

      Rashaad J. testified that he was friends with Harold J. Rashaad first met

Mathis in the summer of 2011, when Rashaad was 17 years old. Rashaad met

Mathis through Harold. Rashaad testified he took three pictures of Harold shirtless

for Harold to send to Mathis, and that he saw Harold send one of the pictures to

Mathis. Rashaad also saw Harold send a pornographic picture to Mathis that he

got from the Internet.

      At the beginning of the fourth day of trial, the AUSA informed the district

court that while Agent Gonzalez was at a coffee shop, a juror possibly overheard

the special agent say “they need to get him” during a conversation on her cell

phone. The district court indicated it did not think there was a problem.


                                           10
             Case: 13-13109     Date Filed: 09/24/2014   Page: 11 of 42


      Harold J. was called as a witness. He testified that he first met Mathis after

a basketball game. Mathis told Harold that he wanted to get to know him and then

began sending Harold text messages. Mathis indicated he was trying to act like a

father figure and told Harold to let him know if he needed anything. For instance,

on May 24, 2011, Mathis sent Harold a text message saying “I’m good people I

promise you can trust me even if you do things wrong” as well as a message

stating in part, “[w]hen I meet you I saw something about you and took interest in

you . . . . Let’s keep in touch so I can do things for you.” Mathis also sent Harold a

text message on May 24, 2011, stating “[l]et me help you. No one will know what

I’m doing unless you tell them. This coming from my heart cause I see good in

you. . . . You will have money in your pocket and lots of nice cloth[e]s and shoes

for next year.”

      On May 31, 2011, in response to a text message from Mathis, Harold sent

Mathis a text message stating he was 15 years old. Mathis continued sending text

messages to Harold encouraging Harold to trust him and professing that he had

strong feelings for Harold. On several occasions, Mathis asked Harold to send him

pictures, and Harold complied by sending pictures of himself in athletic wear and

casual clothing. Mathis also sent Harold text messages asking Harold about his

sexual activity and discussing Harold’s physique.




                                          11
             Case: 13-13109     Date Filed: 09/24/2014   Page: 12 of 42


      On July 16, 2011, Mathis sent Harold a text message asking Harold to send

him a picture of himself shirtless. Harold ignored the text message and Mathis sent

Harold text messages several days later again asking for pictures of Harold without

a shirt. Harold ultimately sent Mathis three pictures of himself in which he was

not wearing a shirt. Mathis subsequently sent Harold text messages asking Harold

to send him pictures of his genitalia. In response, Harold sent Mathis pictures of

male genitalia he obtained from the Internet. After Harold sent one of the pictures,

Mathis sent Harold text messages asking Harold to let him see and touch Harold’s

genitalia.

      Gary Scevola, a senior investigator with the U.S. Marshal Service, testified

that he obtained certified copies of Mathis’s sex offender registration forms from

the Florida Department of Law Enforcement, and the Government introduced the

forms into evidence.

      After Scevola testified, the Government recalled Agent Gonzalez. Agent

Gonzalez testified that as part of her investigation she reviewed text messages

between Mathis and Jerel A. After Mathis objected to the introduction of Jerel’s

text messages as impermissible hearsay, the district court instructed the jurors that

they could not consider Jerel’s text messages for the truth of the matter asserted.

The court further instructed the jurors that they could nevertheless consider

Mathis’s text messages for the truth of the matter asserted. Mathis also objected to


                                          12
             Case: 13-13109     Date Filed: 09/24/2014    Page: 13 of 42


the introduction of the text messages on Confrontation Clause grounds. Over

Mathis’s objections, Agent Gonzalez testified that on May 2, 2011, Jerel sent a text

message to Mathis stating “[h]ey this jerel..this my number,” to which Mathis

replied, “[o]k did you have enough money” and “[o]k well you will get some more.

Also text me tonite when you by yourself want to talk to you, and know I care

about you.” Mathis then sent Jerel text messages expressing affection and

promising to provide for him, as well as messages asking Jerel to send him

pictures. Jerel complied and sent Mathis several pictures of himself. Mathis also

repeatedly sent Jerel text messages discussing the size of Jerel’s genitalia and

Jerel’s sexual activity. Mathis sent Jerel text messages asking Jerel to trust him,

such as the following message on May 8, 2011: “Jerel you got it real good and

don’t realize it. You need to let your guards down and let me be close to you.”

       Eventually, Mathis sent Jerel text messages asking him for pictures of his

genitalia. On June 29, 2011, Jerel sent Mathis a text message containing a picture

of his genitalia. Mathis responded by sending Jerel text messages asking to touch

Jerel’s genitalia. On September 11, 2011, Mathis again sent text messages to Jerel

asking for pictures of Jerel’s genitalia. In response, Jerel sent Mathis a text

message containing a picture of his genitalia. On cross-examination, Agent

Gonzalez acknowledged that Jerel had been present in the courthouse the previous

day.


                                          13
             Case: 13-13109     Date Filed: 09/24/2014     Page: 14 of 42


      After the Government rested its case-in-chief, Mathis moved for a judgment

of acquittal, which the district court denied. Mathis then introduced two exhibits

into evidence and rested his case without renewing his motion for a judgment of

acquittal. Mathis did not testify.

      On the fifth and final day of trial, the district court instructed the jury and

then the parties delivered their closing arguments. During the Government’s

closing argument, the AUSA stated “[i]n 2004 the defendant was 34. Jarvis J. was

14. Jarvis J. told you the defendant, Pastor Maurice, molested him and he

assaulted him. It’s a violation of Florida law. The same statute as defendant’s

1995 conviction.” Mathis objected to the statement and moved for a mistrial. The

district court denied the motion but offered to instruct the jury regarding the

AUSA’s statement. Mathis declined to ask for an instruction.

      When the proceedings resumed following a break between the parties’

closing arguments, defense counsel informed the court that, during the break,

Mathis’s aunt overheard one juror say to another juror, “oh, I just love her.” The

district court stated it did not know to whom or what the comment was referring

and that a cautionary instruction was not warranted. The jury ultimately convicted

Mathis on each count.




                                          14
             Case: 13-13109     Date Filed: 09/24/2014    Page: 15 of 42


F. The Presentence Investigation Report

      In preparing Mathis’s Presentence Investigation Report (PSI), the probation

officer calculated a combined adjusted offense level of 41 as to Counts One

through Three, based in part on a two-level enhancement under U.S.S.G.

§ 2G2.1(b)(6) for Mathis’s use of a computer or interactive computer service to

persuade, induce, entice, coerce, or facilitate the travel of a minor to engage in

sexually explicit conduct. Mathis had a criminal history category of V pursuant to

U.S.S.G. § 4B1.5(a)(2) because he had sustained a prior conviction for a sex

offense. Based on his combined adjusted offense level of 41 and criminal history

category of V, Mathis’s advisory guidelines range on Counts One through Three

was 360 months to life imprisonment, with a consecutive 10-year statutory

mandatory minimum term of imprisonment on Count Four. Mathis was also

subject to statutorily enhanced penalties on Counts One and Two under 18 U.S.C.

§ 2251(e) based on his 1995 conviction. Mathis objected to the PSI’s factual

allegations as well as the enhancements under U.S.S.G. § 2G2.1(b)(6) and 18

U.S.C. § 2251(e).

G. The Sentencing Hearing

      During his sentencing hearing, Mathis reiterated his objection to the

§ 2G2.1(b)(6) enhancement, arguing that he did not use “the computer

components” of his smartphone in committing the offenses in Counts One and


                                          15
             Case: 13-13109     Date Filed: 09/24/2014   Page: 16 of 42


Two, in which he was charged with persuading Jerel A. and attempting to persuade

Harold J. to produce child pornography. Instead, Mathis simply sent text messages

and requested pictures, which he could have done with a basic cell phone. The

district court overruled the objection and found the two-level enhancement applied

because Mathis used a smartphone which had Internet and email capabilities and,

further, Mathis sent and received multimedia messages.

      Relying on Alleyne v. United States, 133 S. Ct. 2151 (2013), Mathis objected

to his sentence being enhanced based on the facts underlying his prior conviction.

Mathis also objected to the statutory enhancements under 18 U.S.C. § 2251(e),

contending that his 1995 conviction was not a qualifying predicate offense because

the statute under which he was convicted did not require contact as an element of

the offense. The district court overruled the objection, finding that the § 2251(e)

enhancements applied because the statute was not limited to prior convictions

involving sexual contact. After ruling on various other objections, the district

court calculated that Mathis had a total offense level of 41 and criminal history

category of V, yielding a guidelines range of 360 months to life imprisonment,

with a mandatory consecutive 10-year sentence on Count Four. The district court

sentenced Mathis to 480 months’ imprisonment, comprised of concurrent terms of

360 months’ imprisonment on Counts One, Two, and Three, and a consecutive

120-month term of imprisonment on Count Four. This appeal followed.


                                         16
               Case: 13-13109       Date Filed: 09/24/2014       Page: 17 of 42


                                      II. DISCUSSION

       Mathis raises a host of issues on appeal related to his trial, convictions, and

total sentence. Specifically, Mathis contends that (1) the district court erred by

denying his motion to suppress and renewed motion to suppress; (2) the

introduction of Jerel A.’s text messages at trial violated his Confrontation Clause

rights; (3) insufficient evidence supported each of his convictions; (4) the district

court erred by denying his motion for a mistrial based on the AUSA’s statements

during closing argument; (5) the district court should have interrogated the jurors

or given them an instruction following the two instances of inadvertent juror

contact and after Mathis’s aunt overheard a comment between two jurors; (6) the

cumulative effect of the alleged trial errors warrants reversal; (7) the district court

erred in applying a two-level sentencing enhancement under U.S.S.G.

§ 2G2.1(b)(6); 1 and (8) the district court erred by enhancing his sentences pursuant

to 18 U.S.C. § 2251(e). We conclude none of the issues raised by Mathis have

merit, and we therefore affirm his convictions and sentences.

A. Motions to Suppress

       Mathis contends the search of his phone violated his Fourth Amendment

rights because the affidavit submitted in support of the search warrant was


       1
         Mathis also argued in his initial brief that the district court erred by applying an
enhancement under U.S.S.G. § 2G2.1(b)(3), but he explicitly abandoned that argument in his
reply brief and we do not address it.
                                               17
              Case: 13-13109     Date Filed: 09/24/2014     Page: 18 of 42


misleading and thus the warrant was not obtained in good faith. He also argues the

second examination of his phone exceeded the scope and timeframe of the search

warrant.

      In considering the district court’s denial of a motion to suppress, we review

the district court’s factual findings for clear error, construing the facts in the light

most favorable to the prevailing party, but review the district court’s application of

law to the facts de novo. United States v. Ransfer, 749 F.3d 914, 921 (11th Cir.

2014). We also review de novo “whether a search warrant affidavit established

probable cause” and we “give due weight to inferences drawn from [the] facts by

resident judges and local law enforcement officers.” United States v. Bush, 727

F.3d 1308, 1315 n.3 (11th Cir. 2013) (internal quotation marks omitted).

      1. The Search Warrant

      Mathis argues the affidavit Detective Vizcarrondo submitted in support of

her application for a search warrant was misleading because (1) the affidavit did

not explicitly state that Mathis’s cell phone was a 2011 smartphone and was not

the same phone Mathis used in 2004, and (2) the affidavit failed to state that Jarvis

never alleged his phone and text message conversations with Mathis were sexual in




                                            18
               Case: 13-13109        Date Filed: 09/24/2014        Page: 19 of 42


nature. Mathis further maintains it was improbable that evidence of a crime

committed in 2004 would be present on a cell phone in 2011. 2

       Mathis’s arguments are unavailing. It is well established that affidavits

submitted in support of search warrants are presumptively valid. Franks v.

Delaware, 438 U.S. 154, 171, 98 S. Ct. 2674, 2684 (1978) (“There is, of course, a

presumption of validity with respect to the affidavit supporting the search

warrant.”); United States v. Lebowitz, 676 F.3d 1000, 1010 (11th Cir. 2012)

(“Affidavits supporting warrants are presumptively valid.”). Thus, “intentional or

reckless omissions will invalidate a warrant only if inclusion of the omitted facts

would have prevented a finding of probable cause.” Lebowitz, 676 F.3d at 1010

(internal quotation marks and alteration omitted).

       Inclusion of the omitted facts would not have prevented a finding of

probable cause. 3 Even if the affidavit had stated that Mathis possessed a different


       2
          At oral argument, counsel argued the information contained in the affidavit was stale.
As counsel noted, she made passing reference to that argument in her opening brief when she
stated “the application was overly-broad in an apparent attempt to avoid the appearance of
staleness and in order to attempt to obtain evidence of other crimes unrelated to J.J.’s
allegations.” That terse statement did not sufficiently raise the issue. See United States v. King,
751 F.3d 1268, 1277 (11th Cir. 2014); Sapuppo v. Allstate Floridian Ins. Co., 739 F.3d 678, 681
(11th Cir. 2014) (“We have long held that an appellant abandons a claim when he either makes
only passing references to it or raises it in a perfunctory manner without supporting arguments
and authority.”). Even if we were to consider the argument, it lacks merit. The affidavit was
based on information from Jarvis’s recorded phone call to Mathis in December 2011.
       3
          It is well settled that “[c]ourts reviewing the legitimacy of search warrants should not
interpret supporting affidavits in a hypertechnical manner; rather, a realistic and commonsense
approach should be employed.” United States v. Miller, 24 F.3d 1357, 1361 (11th Cir. 1994).
Having employed a commonsense approach in reviewing the search warrant in this case, we
                                                 19
               Case: 13-13109       Date Filed: 09/24/2014      Page: 20 of 42


phone in 2011 than the phone he used to contact Jarvis in 2004, and that Jarvis

never claimed his cell phone and text message communications with Mathis were

sexual in nature, the affidavit provided probable cause sufficient to support the

issuance of a warrant. See United States v. Gibson, 708 F.3d 1256, 1278 (11th Cir.

2013) (“To obtain a warrant, police must establish probable cause to conclude that

there is a fair probability that contraband or evidence of a crime will be found in a

particular place.” (internal quotation marks omitted)). We have explained that “an

affidavit should establish a connection between the defendant and the property to

be searched and a link between the property and any criminal activity.” Id.

(internal quotation marks and brackets omitted).

       Detective Vizcarrondo’s affidavit established a connection between Mathis

and the phone to be searched. The affidavit explained that Jarvis made a recorded

phone call to Mathis’s phone number on December 17, 2011, that Mathis did not

maintain a home phone and appeared to exclusively use his cell phone to

communicate with others, and that Mathis had maintained the same phone number

since 2004.

       The affidavit also established a connection between Mathis’s cell phone and

criminal activity. Specifically, the affidavit explained Jarvis had told law




conclude Detective Vizcarrondo did not intentionally or recklessly omit information from the
affidavit she submitted to the state court judge who issued the warrant.
                                              20
               Case: 13-13109       Date Filed: 09/24/2014      Page: 21 of 42


enforcement officers that, during the period in time when Mathis sexually abused

him, Mathis continuously called him from Mathis’s cell phone and that the two

would communicate via text messages. Contrary to Mathis’s contentions, the fact

that Mathis may not have made sexually explicit comments to Jarvis on the phone

or in text messages did not mean evidence of wrongdoing would not be found on

his phone. See United States v. Tinkle, 655 F.2d 617, 621 (5th Cir. Unit A Sept.

1981) (“The currency of probable cause is probability, not legal certainty; it may

exist even though the evidence before the officer is insufficient to convict.”). 4 As

the Supreme Court has stated, “innocent behavior frequently will provide the basis

for a showing of probable cause,” and the relevant inquiry in making a

determination of probable cause “is not whether particular conduct is ‘innocent’ or

‘guilty,’ but the degree of suspicion that attaches to particular types of

non-criminal acts.” Illinois v. Gates, 462 U.S. 213, 243 n.13, 103 S. Ct. 2317,

2335 n.13 (1983). The affidavit, moreover, explained that, based on her

knowledge, experience, and training, Detective Vizcarrondo knew that individuals

who sexually abuse children sometimes maintain copies of communications with

their victims “in the privacy and security of their personal cell phones and retain

these items for many years.” See Riley v. California, 573 U.S. __, __, 134 S. Ct.


       4
          In Bonner v. City of Prichard, 661 F.2d 1206, 1209 (11th Cir. 1981) (en banc), this
Court adopted as binding precedent all decisions of the former Fifth Circuit handed down prior
to the close of business on September 30, 1981.
                                               21
                Case: 13-13109        Date Filed: 09/24/2014        Page: 22 of 42


2473, 2492 (2014) (“In the cell phone context . . . it is reasonable to expect that

incriminating information will be found on a phone regardless of when the crime

occurred.”).

       Alternatively, even if the search warrant was not supported by probable

cause, evidence obtained from the search of Mathis’s phone was not subject to

suppression under the good faith exception to the exclusionary rule. See United

States v. Martin, 297 F.3d 1308, 1313 (11th Cir. 2002) (explaining that “United

States v. Leon, 468 U.S. 897, 922, 104 S. Ct. 3405, 3420 (1984), stands for the

principle that courts generally should not render inadmissible evidence obtained by

police officers acting in reasonable reliance upon a search warrant that is

ultimately found to be unsupported by probable cause”).5 The record contains no

indication Detective Vizcarrondo was dishonest or reckless in preparing her

affidavit or that she could not have harbored an objectively reasonable belief in the

existence of probable cause. Because the officers engaged in “objectively

reasonable law enforcement activity and . . . acted in good faith when obtaining
       5
          Mathis does not argue in his initial brief that any exception to the good faith rule applies
in this case. He does not contend that (1) Detective Vizcarrondo included information in the
affidavit that she knew was false or would have known was false except for her reckless
disregard for the truth; (2) the issuing judge wholly abandoned his judicial role; (3) the affidavit
was so lacking in indicia of probable cause that official belief in its existence was unreasonable;
or (4) the warrant was so facially deficient that the executing officers could not reasonably
presume it was valid. See Martin, 297 F.3d at 1313. Accordingly, Mathis has abandoned any
argument regarding the exceptions to the good faith rule. See United States v. McKinley, 732
F.3d 1291, 1295 n.1 (11th Cir. 2013). In the alternative, even if the issue was sufficiently raised,
Mathis has not demonstrated that any exception to the good faith rule applies and we conclude
the issue lacks merit.


                                                 22
               Case: 13-13109        Date Filed: 09/24/2014        Page: 23 of 42


[the] search warrant . . . the Leon good faith exception applies.” Id. (internal

quotation marks omitted).

       2. The August 2012 Examination 6

       Mathis also contests the validity of the second examination of his

smartphone, which occurred on August 1, 2012. Before the district court, Mathis

argued in his renewed motion to suppress that the multimedia messages obtained

during the August 2012 examination were not in plain view during the December

2011 examination and there was no authorization for the August 2012 examination

because no new search warrant had been obtained.

       On appeal, Mathis contends evidence obtained from his smartphone on

August 1, 2012, should have been suppressed because the examination occurred

well after the expiration of the 10-day period provided in the warrant. Mathis

devotes only two paragraphs of his sixty-one page opening brief to this issue. In

those two paragraphs, Mathis mostly repeats the facts underlying his claim and his

actual argument boils down to three sentences. First, he argues “[t]he district court

erred in not granting Mathis’s motion to suppress at trial where the evidence was

obtained outside the scope and time frame of the search warrant.” Second, he

       6
          Although Mathis arguably waived his challenge to the August 2012 examination
because he did not raise it in his motion to suppress prior to trial, see United States v. Ford, 34
F.3d 992, 994 n.2 (11th Cir. 1994) (concluding a party’s failure to raise a suppression argument
prior to trial resulted in a waiver of the issue); Fed. R. Crim. P. 12(b)(3), (e), the district court
considered and rejected the issue on the merits and we will therefore address it, see United States
v. Lall, 607 F.3d 1277, 1290 (11th Cir. 2010).

                                                 23
               Case: 13-13109        Date Filed: 09/24/2014        Page: 24 of 42


asserts “[e]vidence seized while the police are acting outside the boundaries of the

warrant is subject to suppression.” Third, Mathis contends that “[o]nly during a

search conducted eight mo[n]ths [after the initial search], outside the scope of the

search warrant[,] was Hayes able to determine who sent the MMS messages.”

Mathis does not argue the eight month delay was itself unreasonable or that he was

prejudiced by the delay. In support of his arguments, Mathis cites only a single

Fourth Circuit opinion from 1994 for the proposition that, if officers seize items

which are not enumerated in a search warrant, those items are subject to

suppression.7

       Although Mathis contends the second examination of his phone violated his

constitutional rights, we have held that “[t]he Fourth Amendment does not specify

that search warrants contain expiration dates,” and that a search conducted after a

warrant’s expiration date does not necessarily require suppression of the evidence.

United States v. Gerber, 994 F.2d 1556, 1559-60 (11th Cir. 1993); see also

Herring v. United States, 555 U.S. 135, 144, 135 S. Ct. 695, 702 (2009) (“To

trigger the exclusionary rule, police conduct must be sufficiently deliberate that



       7
          Mathis has waived any arguments that he raises only in his reply brief because those
arguments are too late. United States v. Lopez, 649 F.3d 1222, 1246 (11th Cir. 2011); United
States v. Evans, 473 F.3d 1115, 1120 (11th Cir. 2006) (“Arguments raised for the first time in a
reply brief are not properly before a reviewing court.” (internal quotation marks and alteration
omitted)). In addition, the record does not support Mathis’s contention in his reply brief that the
Government searched his smartphone month after month for eight months. Instead, the record
establishes that Mathis’s smartphone was examined only twice.
                                                24
                Case: 13-13109      Date Filed: 09/24/2014      Page: 25 of 42


exclusion can meaningfully deter it, and sufficiently culpable that such deterrence

is worth the price paid by the justice system.”).

           We need not decide this issue, however, because even if the August 2012

examination violated Mathis’s Fourth Amendment rights, any error in admitting

the evidence at trial was harmless. See United States v. Rhind, 289 F.3d 690, 694

(11th Cir. 2002). The record demonstrates that officers obtained Mathis’s SMS

messages, i.e., plain text messages, during the initial examination of his cell phone,

but could not recover his multimedia messages, i.e., text messages containing

pictures or videos. The initial search was conducted within the ten-day period

provided in the warrant and, as discussed above, was valid. Mathis’s plain text

messages, even without the multimedia messages and accompanying pictures,

provided overwhelming evidence of Mathis’s guilt on Counts One and Two.

Accordingly, any error in admitting the multimedia messages was harmless. 8 See

id. (concluding a Fourth Amendment violation was harmless because evidence of

the defendants’ guilt was overwhelming).

B. The Confrontation Clause

       Mathis argues that the admission of Jerel A.’s text messages at trial violated

his rights under the Confrontation Clause. Mathis contends he was prohibited from


       8
        Counsel agreed at oral argument that any error in the introduction of the multimedia
messages obtained from the August 2012 examination was harmless in light of the plain text
messages retrieved during the December 2011 examination.
                                              25
             Case: 13-13109    Date Filed: 09/24/2014    Page: 26 of 42


cross-examining and impeaching Jerel’s testimony, while the Government was

allowed to introduce favorable evidence in the form of Jerel’s text messages. “We

review a preserved Confrontation Clause claim de novo,” United States v. Curbelo,

726 F.3d 1260, 1271-72 (11th Cir. 2013), and also review de novo “the question of

whether hearsay statements are testimonial for purposes of the Confrontation

Clause,” United States v. Caraballo, 595 F.3d 1214, 1226 (11th Cir. 2010)

(internal quotation marks omitted).

      Mathis’s arguments lack merit. The Confrontation Clause bars the

admission of a witness’s testimonial statements when the witness did not appear at

trial unless the witness was unavailable and the defendant had a prior opportunity

to examine him. Caraballo, 595 F.3d at 1227; see also Crawford v. Washington,

541 U.S. 36, 53-54, 124 S. Ct. 1354, 1365 (2004). Mathis does not argue on

appeal that Jerel’s text messages were testimonial and he has “therefore abandoned

an issue on which he had to prevail in order to obtain reversal.” United States v.

King, 751 F.3d 1268, 1277 (11th Cir. 2014). Regardless, any argument that Jerel’s

text messages were testimonial would be unavailing. We have explained that:

      [F]ormal statements to government officers are generally testimonial
      as are affidavits, custodial examinations, prior testimony that the
      defendant was unable to cross-examine, or similar pretrial statements
      that declarants would reasonably expect to be used prosecutorially.
      Similarly, extrajudicial statements contained in formalized testimonial
      materials, such as affidavits, depositions, prior testimony, or
      confessions, and statements that were made under circumstances
      which would lead an objective witness reasonably to believe that the
                                         26
               Case: 13-13109      Date Filed: 09/24/2014      Page: 27 of 42


        statement would be available for use at a later trial, fall within the core
        class of testimony.

Caraballo, 595 F.3d at 1228 (brackets and alterations omitted). Jerel’s text

messages were not formal statements to government officers, they were not made

during a custodial examination, and they did not constitute an affidavit, prior

testimony, or pretrial statements that he would reasonably expect to be used

prosecutorially. Jerel’s text messages were not formalized testimonial materials,

and they were not made under circumstances that would lead an objective witness

reasonably to believe that they would be available for use at a later trial. See id.

Far from amounting to “the functional equivalent of in-court testimony,” Curbelo,

726 F.3d at 1272 (internal quotation marks omitted), Jerel’s text messages were

informal, haphazard communications sent at all hours and from locations such as

his house, the bus stop, and his school. Jerel’s text messages were not testimonial

statements and Mathis’s right of confrontation was not violated by their admission

at trial.

C. Sufficiency of the Evidence

     Mathis argues that insufficient evidence supported each of his convictions. 9

As to Count One—which charged Mathis with persuading, inducing, enticing, or

        9
         While we ordinarily “review challenges to the sufficiency of the evidence de novo, and
ask whether a reasonable jury could have found the defendant guilty beyond a reasonable doubt,”
when a defendant “fails to renew his motion for judgment of acquittal at the end of all of the
evidence, we review the defendant’s challenge to the sufficiency of the evidence for a manifest
miscarriage of justice.” United States v. House, 684 F.3d 1173, 1196 (11th Cir. 2012) (internal
                                              27
               Case: 13-13109       Date Filed: 09/24/2014       Page: 28 of 42


coercing Jerel A. to engage in sexually explicit conduct for the purpose of

producing a visual depiction of such conduct—Mathis reiterates his Confrontation

Clause arguments and then asserts without elaboration that there was no proof

beyond a reasonable doubt that Jerel produced a sexually explicit visual depiction.

We have already determined that Mathis’s Confrontation Clause arguments lack

merit and we conclude the evidence was more than sufficient to support Mathis’s

conviction on Count One.

       At trial, the Government introduced evidence that Jerel was a minor in 2011

and that Mathis persuaded, induced, enticed, or coerced Jerel to take pictures of his

genitalia and then send them to Mathis in text messages. Specifically, Mathis

asked Jerel for pictures of Jerel’s genitalia in May, June, and September of 2011,

Mathis offered to pay Jerel for a picture of Jerel’s genitalia, and he directed Jerel to

take sexually explicit pictures. For instance, on June 29, 2011, Mathis sent Jerel a

text message stating “I want my picture and it better be hard and I hope you trust

me cause I have been there for you.” Similarly, on September 11, 2011, Mathis

asked Jerel to send him a text message with a picture of his genitalia, stating “[o]k



quotation marks omitted). Although Mathis introduced two exhibits into evidence during his
case-in-chief and then failed to renew his motion for a judgment of acquittal, we need not decide
whether to review his arguments only for a manifest miscarriage of justice because his
sufficiency challenges fail regardless of the standard applied. See United States v. Houser, 754
F.3d 1335, 1349 (11th Cir. 2014) (“Regardless of the standard applied . . . [the defendant’s]
sufficiency challenge fails.”).

                                               28
             Case: 13-13109     Date Filed: 09/24/2014    Page: 29 of 42


just send a good one I want to see how long it is,” and, after receiving a picture,

Mathis sent Jerel a text message saying “[c]an you hold it up please.” The

Government also introduced into evidence two pictures of male genitalia Jerel sent

to Mathis, at least one of which was an image of male genitalia in an aroused state.

The evidence adduced at trial was sufficient for a jury to conclude Mathis

persuaded Jerel to produce and send him a visual depiction of sexually explicit

conduct. See United States v. Grzybowicz, 747 F.3d 1296, 1305-07 (11th Cir.

2014).

      The evidence was also sufficient to support Mathis’s conviction on Count

Two, which charged him with attempting to persuade, induce, entice, or coerce

Harold J. to engage in sexually explicit conduct for the purpose of producing a

visual depiction of such conduct. On appeal, Mathis argues only that his

conviction cannot stand because Harold did not, in fact, produce a visual depiction

of sexually explicit conduct. Mathis’s argument fails to recognize that he was

convicted in Count Two of attempted production of child pornography rather than

actual production. The evidence presented at trial, moreover, demonstrated that

Mathis intentionally attempted to persuade Harold, who was a minor in 2011, to

produce child pornography. Harold testified that Mathis repeatedly sent him text

messages exhorting Harold to trust him. Harold also explained that, on several

occasions, Mathis asked Harold to send him text messages with pictures of


                                          29
             Case: 13-13109      Date Filed: 09/24/2014    Page: 30 of 42


Harold’s genitalia. According to Harold, on one occasion Mathis sent him text

messages offering to pay him $500 in exchange for such a picture and, on another

occasion, Mathis promised to take Harold to Tampa in exchange for Harold taking

and sending a picture of his genitalia. In addition, the Government introduced

copies of the text messages between Mathis and Harold in which Mathis asked

Harold for pictures of his genitalia. A reasonable jury could have found that

Mathis took a substantial step toward persuading, inducing, or enticing Harold to

produce child pornography and that he attempted to produce child pornography.

See United States v. Lee, 603 F.3d 904, 918 (11th Cir. 2010).

      Mathis next contends insufficient evidence supported his conviction on

Count Three because he was charged with enticing and attempting to entice Jarvis

to engage in sexual activity on a cellular phone and that no evidence proved sexual

activity took place on the phone or that Mathis used a phone to commit the offense.

Mathis again misconceives the offense for which he was convicted. Count Three

charged him with using a facility of interstate commerce to knowingly persuade,

induce, or entice Jarvis J., a minor, to engage in illegal sexual activity, in violation

of 18 U.S.C. § 2422(b). Section 2422(b) does not require that the sexual activity

have occurred on the facility of interstate commerce, in this case a cell phone. See

18 U.S.C. § 2422(b).




                                           30
                 Case: 13-13109       Date Filed: 09/24/2014       Page: 31 of 42


         Regardless, Mathis’s argument is contradicted by the record. Jarvis testified

that, after their first sexual interaction, Mathis talked to him on his cell phone in a

sexually explicit manner and that Mathis was more comfortable “talking about

planning it with [him].” Jarvis’s extensive testimony at trial provided sufficient

evidence for the jury to conclude Mathis used his cell phone to induce or entice

Jarvis to engage in sexual activity and his conviction on Count Three must stand.

         Mathis’s conviction on Count Four was also supported by sufficient

evidence. Count Four charged Mathis with violating 18 U.S.C. § 2260A by

committing the offenses charged in Counts One through Three while he was

required to register as a sex offender under Florida law. 10 The Government

introduced a copy of a judgment demonstrating that, on February 22, 1995, Mathis

was convicted of lewd or lascivious assault on a child, in violation of § 800.04 of

the Florida Statutes. 11 Accordingly, Florida law required Mathis to register as a

sex offender if he was released from his sentence for that conviction on or after

10
     Section 2260A provides:

         Whoever, being required by Federal or other law to register as a sex offender,
         commits a felony offense involving a minor under section 1201, 1466A, 1470,
         1591, 2241, 2242, 2243, 2244, 2245, 2251, 2251A, 2260, 2421, 2422, 2423, or
         2425, shall be sentenced to a term of imprisonment of 10 years in addition to the
         imprisonment imposed for the offense under that provision. The sentence
         imposed under this section shall be consecutive to any sentence imposed for the
         offense under that provision.

18 U.S.C. § 2260A.
         11
         Mathis was sentenced to a 52-month term of imprisonment, but his sentence was
suspended and he was placed on a 2-year term of probation.
                                                 31
               Case: 13-13109     Date Filed: 09/24/2014   Page: 32 of 42


October 1, 1997. See Fla. Stat. § 943.0435; Miller v. State, 971 So. 2d 951, 954

(Fla. 5th DCA 2007). Mathis maintains no evidence was introduced at trial

proving when he was released from custody for his § 800.04 offense. Thus, no

evidence was presented that he was required to register as a sex offender under

Florida law.

      Contrary to his contentions, the Government presented sufficient evidence

from which a reasonable jury could have found he was required to register as a sex

offender. The Government introduced a copy of a judgment from February 21,

1997, adjudicating Mathis guilty of violating the term of probation to which he was

sentenced for his § 800.04 conviction. Mathis was sentenced to a 48-month term

of imprisonment for his probation violation and was given credit for 174 days of

time served. Accordingly, the jury could have found Mathis was to be incarcerated

for 1,286 days, placing his release date well beyond October 1, 1997. Such a

finding was supported by copies of Mathis’s sex offender registration forms, which

indicated he registered as a sex offender with the State of Florida in January 1999

due to his § 800.04 conviction.

D. Motion for a Mistrial

      Mathis argues the district court erred by denying his motion for a mistrial

based on the AUSA’s statement during closing argument that Mathis’s conduct in

2004 was a violation of § 800.04, the same statute under which Mathis was


                                           32
              Case: 13-13109     Date Filed: 09/24/2014     Page: 33 of 42


convicted in 1995. We review the denial of a motion for a mistrial for abuse of

discretion. United States v. Garcia, 405 F.3d 1260, 1272 (11th Cir. 2005). An

improper closing argument will justify a new trial only if it was “both improper

and prejudicial to a substantial right of the defendant.” Id. (internal quotation

marks omitted).

      In the context of the entire trial, the AUSA’s comment did not prejudice

Mathis’s substantial rights. See United States v. Hasner, 340 F.3d 1261, 1275

(11th Cir. 2003) (“Prosecutorial misconduct is a basis for reversing an appellant’s

conviction only if, in the context of the entire trial in light of any curative

instruction, the misconduct may have prejudiced the substantial rights of the

accused.” (internal quotation marks omitted)). The jury was provided a copy of the

indictment which clearly revealed the same information referenced by the AUSA,

namely that Mathis’s conduct in 2004 was illegal under § 800.04 of the Florida

Statutes, and that Mathis had previously violated § 800.04. Additionally, the

evidence that Mathis enticed or induced Jarvis to engage in sexual activity was

overwhelming and included Jarvis’s testimony at trial as well as Jarvis’s recorded

conversation with Mathis in which Mathis acknowledged sexually abusing Jarvis

when he was a minor. Thus, no reasonable probability existed that, but for the

remark, the outcome of the trial would have been different. The district court did

not abuse its discretion by denying Mathis’s motion for a mistrial. See United


                                           33
             Case: 13-13109      Date Filed: 09/24/2014    Page: 34 of 42


States v. Capers, 708 F.3d 1286, 1308-09 (11th Cir. 2013) (“A defendant’s

substantial rights are prejudiced if there is a reasonable probability that, but for the

improper remarks, the outcome of the trial would have been different.” (internal

quotation marks omitted)).

E. Juror Encounters

      Mathis next argues that three occurrences during the course of the trial

involving jurors could have affected the impartiality of the jury and rendered his

trial unfair. First, Mathis contends the juror who potentially overheard the AUSA

tell Sergeant Evans that she worked late into the night could have felt sympathy for

the AUSA and, by extension, the Government’s case. Second, Mathis maintains

the jury could have been influenced or affected by the fact that a juror potentially

overheard Agent Gonzalez in a coffee shop say into her cell phone “we need to get

him.” Third, Mathis argues that the two jurors whom Mathis’s aunt overheard

saying “oh, I just love her” could have been expressing a preference for the

Government and bias toward the defense.

      We presume that the jury was impartial, and neither Mathis’s speculation

nor the record establishes that the jurors in the elevator and the coffee shop

actually overheard the statements of which he complains, or that any of the jurors

were biased against him. See United States v. Siegelman, 640 F.3d 1159, 1182

(11th Cir. 2011). Mathis has failed to make a colorable showing that the jury was


                                           34
              Case: 13-13109    Date Filed: 09/24/2014   Page: 35 of 42


exposed to extraneous information, see id., and the district court did not err by

declining to interrogate each member of the jury in response to such fleeting,

innocuous events. Furthermore, the district court instructed the jurors that their

decision had to be based on the evidence presented during trial and that they

should not be influenced in any way by sympathy or prejudice against the

defendant or the Government. The district court also instructed the jurors that they

should not discuss the case among themselves until the court gave them the case to

decide. We presume the jury followed the district court’s instructions, and Mathis

has provided us with no basis for disregarding that presumption. See United States

v. Stone, 9 F.3d 934, 938 (11th Cir. 1993) (“Few tenets are more fundamental to

our jury trial system than the presumption that juries obey the court’s

instructions.”).

F. Cumulative Error

      Mathis argues that the cumulative effect of the alleged errors at trial

deprived him of a fair trial. Mathis, however, has not demonstrated cumulative

error warranting a new trial. See Grzybowicz, 747 F.3d at 1311; Capers, 708 F.3d

at 1299 (explaining a defendant’s substantial rights must be affected to warrant

relief under the cumulative error doctrine).

G. The § 2G2.1(b)(6) Enhancement




                                          35
             Case: 13-13109      Date Filed: 09/24/2014    Page: 36 of 42


      Turning to his 480-month total sentence, Mathis argues the district court

erred by applying a two-level enhancement under U.S.S.G. § 2G2.1(b)(6), which

applies if the defendant, for the purpose of producing sexually explicit material,

used “a computer or an interactive computer service to . . . persuade, induce,

entice, coerce, or facilitate the travel of, a minor to engage in sexually explicit

conduct, or to otherwise solicit participation by a minor in such conduct.”

According to Mathis, the enhancement applies only when a defendant used the

Internet in the commission of the offense and not simply because a phone with

Internet capabilities was used. We disagree.

      Section 2G2.1(b)(6) provides:

      If, for the purpose of producing sexually explicit material or for the
      purpose of transmitting such material live, the offense
      involved . . . the use of a computer or an interactive computer service
      to (i) persuade, induce, entice, coerce, or facilitate the travel of, a
      minor to engage in sexually explicit conduct, or to otherwise solicit
      participation by a minor in such conduct; or (ii) solicit participation
      with a minor in sexually explicit conduct, increase by 2 levels.

U.S.S.G. § 2G2.1(b)(6). The guidelines commentary instructs that the word

“computer” has “the meaning given that term in 18 U.S.C. § 1030(e)(1).” U.S.S.G.

§ 2G2.1 cmt. (n.1). 18 U.S.C. § 1030(e)(1), in turn, defines a computer as:

      an electronic, magnetic, optical, electrochemical, or other high speed
      data processing device performing logical, arithmetic, or storage
      functions, and includes any data storage facility or communications
      facility directly related to or operating in conjunction with such
      device, but such term does not include an automated typewriter or
      typesetter, a portable hand held calculator, or other similar device.
                                           36
             Case: 13-13109     Date Filed: 09/24/2014    Page: 37 of 42




18 U.S.C. § 1030(e)(1).

      It is an issue of first impression in this Circuit whether a cell phone is a

“computer” within the meaning of § 1030(e)(1). The Eighth Circuit, however, has

decided the issue. See United States v. Kramer, 631 F.3d 900, 902-04 (8th Cir.

2011). As that court has noted, the language of § 1030(e)(1) is broad and

encompasses any device that uses a data processor. Id. at 902. We agree with the

Eighth Circuit’s observation that “each time an electronic processor performs any

task—from powering on, to receiving keypad input, to displaying information—it

performs logical, arithmetic, or storage functions. These functions are the essence

of its operation.” Id. at 903. Nothing in the statutory definition of a computer

requires that the device have a connection to the Internet or Internet capabilities.

Id. We will not rewrite the statutory definition to exclude Mathis’s use of a

smartphone to call and send text messages to his minor victims—activities that

undoubtedly employed an electronic or high speed data processing device

performing logical, arithmetic, and storage functions. The Seventh Circuit has

explained in discussing the scope of § 1030, “[a]s more devices come to have

built-in intelligence, the effective scope of the statute grows. This might prompt

Congress to amend the statute but does not authorize the judiciary to give the

existing version less coverage than its language portends.” United States v. Mitra,



                                          37
               Case: 13-13109       Date Filed: 09/24/2014       Page: 38 of 42


405 F.3d 492, 495 (7th Cir. 2005). 12 We therefore hold that a defendant’s use of a

cell phone to call and send text messages constitutes the use of a computer, as that

term is defined in 18 U.S.C. § 1030(e)(1), and warrants imposition of an

enhancement under U.S.S.G. § 2G2.1(b)(6).

       In the alternative, even if the enhancement was not warranted, any error was

harmless. As calculated by the district court, Mathis had a combined total offense

level of 41 and a criminal history category of V, yielding a guidelines range of 360

months to life imprisonment. Without the § 2G2.1(b)(6) enhancement, Mathis’s

offense level of 39 and criminal history category of V would have still yielded a

guidelines range of 360 months to life imprisonment. See U.S.S.G. Ch. 5 pt. A,

sentencing table. Given that Mathis’s guidelines range was the same with or

without the enhancement, any potential error in applying the enhancement does not

warrant reversal. See United States v. Campa, 529 F.3d 980, 1013 (11th Cir. 2008)

(“A sentencing error, under the Guidelines, is harmless if a court considers the

proceedings in their entirety and determines that the error did not affect the

sentence or had but very slight effect.” (internal quotation marks omitted)).

H. The § 2251(e) Enhancement



       12
           We do not mean to say that every use of a device with a data processor necessarily
warrants imposition of an enhancement under § 2G2.1(b)(6). The guidelines commentary
specifies that the enhancement “is intended to apply only to the use of a computer . . . to
communicate directly with a minor,” as Mathis did in this case. U.S.S.G. § 2G2.1 cmt. (n.4).
                                               38
             Case: 13-13109     Date Filed: 09/24/2014    Page: 39 of 42


      Mathis raises several challenges to the district court’s imposition of a

sentencing enhancement under 18 U.S.C. § 2251(e). Specifically, Mathis contends

the enhancement was inapplicable because the Florida statute under which he was

convicted in 1995, i.e, § 800.04, did not require actual touching or contact with a

minor. Mathis also argues that imposition of an enhanced sentence violated his

Sixth Amendment rights.

      We review de novo the interpretation of a statute, United States v. McQueen,

727 F.3d 1144, 1151 (11th Cir. 2013), as well as preserved claims of error under

Alleyne and Apprendi v. New Jersey, 530 U.S. 466, 120 S. Ct. 2348 (2000), see

King, 751 F.3d at 1279. Section 2251 criminalizes the sexual exploitation of

minors and provides for a sentence of not less than 15 years’ or more than 30

years’ imprisonment. 18 U.S.C. § 2251(a), (e). However, if a defendant “has one

prior conviction . . . under the laws of any State relating to aggravated sexual

abuse, sexual abuse, [or] abusive sexual contact involving a minor or ward,” the

defendant is subject to a 25-year mandatory minimum and 50-year statutory

maximum sentence. Id. § 2251(e).

      1. Actual Touching or Contact

      Mathis asserts that for an enhancement to apply under § 2251(e), a prior

state conviction must have required sexual contact, not merely sexual conduct. He

maintains that because he was convicted of lewd or lascivious assault on a minor,


                                          39
               Case: 13-13109         Date Filed: 09/24/2014        Page: 40 of 42


and assault can be committed without actual touching, his conviction under

§ 800.04 of the Florida Statutes was not a qualifying offense.13

       Mathis’s argument is unavailing. His reading of § 2251(e) ignores the plain

text of the statute, which provides for an enhanced sentencing range if the

defendant has previously been convicted under a state law relating to sexual abuse

of a minor. See 18 U.S.C. § 2251(e). We have interpreted the phrase “relating to”

broadly in the context of child exploitation offenses, and have held that a

defendant’s prior conviction under Georgia law for discussing illicit sexual acts

with a minor warranted an enhancement under § 2251(e). See United States v.

McGarity, 669 F.3d 1218, 1262-63 (11th Cir. 2012). We have also held that the

plain meaning of the phrase “sexual abuse of a minor” includes “acts that involve

physical contact between the perpetrator and the victim as well as acts that do not.”

United States v. Padilla-Reyes, 247 F.3d 1158, 1163 (11th Cir. 2001). Mathis

cannot avoid our clear pronouncement that “the phrase ‘sexual abuse of a minor’

means a perpetrator’s physical or nonphysical misuse or maltreatment of a minor

for a purpose associated with sexual gratification.” Id. Mathis’s prior state

conviction under § 800.04 for lewd or lascivious assault on a child related to the



       13
           At the time of Mathis’s offense, § 800.04 provided in pertinent part that “[a] person
who . . . [h]andles, fondles, or assaults any child under the age of 16 years in a lewd, lascivious,
or indecent manner . . . without committing the crime of sexual battery, commits a felony of the
second degree.” Fla. Stat. § 800.04(1) (1994).
                                                 40
             Case: 13-13109     Date Filed: 09/24/2014    Page: 41 of 42


sexual abuse of a minor and the district court did not err by enhancing his sentence

under § 2251(e).

      2. The Sixth Amendment

      Finally, to preserve the issue, Mathis argues that the Supreme Court’s

decision in Almendarez-Torres v. United States, 523 U.S. 224, 118 S. Ct. 1219

(1998), does not apply to this case and the district court’s imposition of a statutory

sentencing enhancement violated his Sixth Amendment rights. Mathis’s argument

is squarely foreclosed by Circuit precedent, see King, 751 F.3d at 1280 (rejecting

the argument that Alleyne is inconsistent with Almendarez-Torres); United States v.

Shelton, 400 F.3d 1325, 1329 (11th Cir. 2005) (explaining that the Supreme

Court’s holding in Almendarez-Torres was left undisturbed by Apprendi), and we

adhere to the Supreme Court’s holding in Almendarez-Torres that “the

Government need not allege in its indictment and need not prove beyond a

reasonable doubt that a defendant had prior convictions for a district court to use

those convictions for purposes of enhancing a sentence,” King, 751 F.3d at 1280

(internal quotation marks and brackets omitted).

                                III. CONCLUSION

      For the foregoing reasons, we affirm Mathis’s convictions and sentences.

However, we note the judgment states Mathis was convicted on Count Two of




                                          41
               Case: 13-13109       Date Filed: 09/24/2014      Page: 42 of 42


production and attempted production of child pornography. 14 We remand to the

district court for the limited purpose of correcting the judgment to reflect that

Mathis was convicted on Count Two only of attempted production of child

pornography. See United States v. Reeves, 742 F.3d 487, 507 n.12 (11th Cir. 2014)

(“We may sua sponte raise the issue of clerical errors in a judgment and remand

with instructions that the district court correct them.”).

       AFFIRMED and REMANDED.




       14
         During the sentencing hearing, the district court judge imposed Mathis’s sentence on
each count by count number. Count Two charged Mathis with attempted production of child
pornography and the typographical error occurred in the clerical entry of “Nature of Offense.”
                                               42

```

---
