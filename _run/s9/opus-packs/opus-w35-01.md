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

## GROUP: content/cases/United States v. May-Shaw.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. May-Shaw
type: case
citation: "955 F.3d 563 (2020)"
parallel_cite: ""
neutral_cite: ""
court: 6th Cir. 2020
court_level: coa
circuit: ca6
year: 2020
date_decided: 2020-04-08
docket: 18-1821
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4743325/united-states-v-christopher-may-shaw/"
  cluster_id: 4743325
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. May-Shaw
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[United States v. Dunn]]"
  - "[[Florida v. Jardines]]"
  - "[[Collins v. Virginia]]"
tags:
  - case
  - fourth-amendment
  - curtilage
  - dunn-factors
  - dog-sniff
  - pole-camera
  - apartment
  - sixth-circuit
holding: "The Sixth Circuit affirmed, holding that a covered carport in a communal apartment parking lot — where May-Shaw regularly parked but had no right to exclude others, and which was easily viewable from a public street — was not within the curtilage of his apartment under the Dunn factors, so a drug-dog sniff of his car parked there was not a Fourth Amendment search; nor did the twenty-three-day pole-camera surveillance of the lot violate any reasonable expectation of privacy."
---

# United States v. May-Shaw

*955 F.3d 563 (6th Cir. 2020)* (No. 18-1821) · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4743325 → opinion 4523672 (955 F.3d 563, decided 2020-04-08, Bush, J.); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Grand Rapids police investigated Christopher May-Shaw for drug trafficking after anonymous tips and a check revealing prior felony convictions. With the complex owner's permission, they surveilled the exterior of his apartment building and the communal parking lot — first from cameras in a van moved around the lot, and from January 26, 2016, a camera affixed to a telephone pole on Norman Drive that recorded continuously for twenty-three days. May-Shaw parked his BMW under a covered carport in the communal lot, easily viewable from the public street. After watching suspected drug transactions, officers had a K-9 sniff the BMW parked under the carport; the dog alerted, and the officers obtained a warrant for the apartment and vehicles that turned up cash, wrappers, and cocaine. The district court denied suppression, and May-Shaw entered a conditional guilty plea to conspiracy to distribute cocaine (144 months), preserving the appeal.

## Issue
Whether the covered carport in the communal parking lot was within the [[Curtilage|curtilage]] of May-Shaw's apartment — so that the warrantless drug-dog sniff of his car parked there was an unconstitutional search under *[[Florida v. Jardines]]* — and whether the twenty-three-day pole-camera surveillance of the lot violated his [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Rule
A warrantless dog sniff of a home's [[Curtilage|curtilage]] is a search under *[[Florida v. Jardines|Jardines]]*, but whether ground is [[Curtilage|curtilage]] is resolved with reference to the four *[[United States v. Dunn|Dunn]]* factors — proximity to the home, enclosure, the nature of the area's use, and the steps taken to shield it from observation — with the burden on the defendant to show the area is intimately linked to the home. Applying those factors, the court held: "May-Shaw has failed to establish that the carport constituted the curtilage of his apartment; the drug dog sniff therefore did not constitute a search." — 955 F.3d 563, slip op. at 12. ^pin-op12

## Application
None of the *[[United States v. Dunn|Dunn]]* factors carried May-Shaw's burden. Proximity: the carport was closest to his apartment but not as close as structures previously found to be [[Curtilage|curtilage]], and proximity alone is not determinative. Enclosure: the carport had a roof and two side walls but sat in a communal lot, not within an enclosure around the residence. Use: regularly parking there arguably favored him, but he had no legal right to exclude others from the communal carport. Protection from observation: unlike the petitioner in *[[Collins v. Virginia|Collins]]* (who covered his vehicle), May-Shaw did little to protect the area from the view of passersby, and officers could see into the carport from a pole camera across the street. Because the carport was not [[Curtilage|curtilage]], the dog sniff was not a search — and the pole-camera surveillance captured only what was publicly visible, so it did not violate any [[Reasonable Expectation of Privacy|reasonable expectation of privacy]]. The court therefore did not reach the independent-source or good-faith questions.

## Conclusion
**Affirmed.** Judge Bush wrote for the panel (Merritt, Clay, and Bush, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *May-Shaw* is a useful *[[United States v. Dunn|Dunn]]*-factors application at the **[[Curtilage|curtilage]] / open-view boundary**: a partially enclosed but **communal** carport that the resident cannot exclude others from, and that is plainly visible from a public street, falls outside the [[Curtilage|curtilage]] — so a dog sniff there is not a search, and *[[Collins v. Virginia|Collins]]* (a walled-off driveway the owner shielded) does not compel the opposite result.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*United States v. May-Shaw*, 955 F.3d 563 (6th Cir. 2020)](https://www.courtlistener.com/opinion/4743325/united-states-v-christopher-may-shaw/) — pinpoint: slip op. at 12 (carport-not-curtilage / dog-sniff-not-a-search holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3e651498a5a488fc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "955 F.3d 563 (2020)", "court": "6th Cir. 2020", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. May-Shaw", "year": "2020"}}
{"assertion_id": "b20b57fceb5eeec7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Circuit affirmed, holding that a covered carport in a communal apartment parking lot — where May-Shaw regularly parked but had no right to exclude others, and which was easily viewable from a public street — was not within the curtilage of his apartment under the Dunn factors, so a drug-dog sniff of his car parked there was not a Fourth Amendment search; nor did the twenty-three-day pole-camera surveillance of the lot violate any reasonable expectation of privacy.", "title": "United States v. May-Shaw"}}
{"assertion_id": "f0ac8d3647cbc3d1", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Key", "title": "United States v. May-Shaw"}}
{"assertion_id": "81676854aeba7090", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "United States v. May-Shaw"}}
{"assertion_id": "9f0028bc8cd9fee1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. May-Shaw", "varies_by_point": "false"}}
```

### lake record — United States v. May-Shaw

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. May-Shaw",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Christopher May-Shaw",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. May-Shaw",
    "court": "6th Cir. 2020",
    "court_id": "ca6",
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2020-04-08",
    "year": 2020,
    "docket": "18-1821",
    "cluster_id": 4743325,
    "lead_opinion_id": 4523672,
    "sibling_ids": [],
    "absolute_url": "/opinion/4743325/united-states-v-christopher-may-shaw/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "955 F.3d 563",
      "volume": "955",
      "reporter": "F.3d",
      "page": "563",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "955 F.3d 563",
        "volume": "955",
        "reporter": "F.3d",
        "page": "563",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "955 F.3d 563",
    "official_selection": {
      "court_class": "state",
      "selected": "955 F.3d 563",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:55:59Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-may-shaw--4743325",
      "to_record_id": "United States v. May-Shaw",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. May-Shaw

```
                                RECOMMENDED FOR PUBLICATION
                                Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                       File Name: 20a0109p.06

                    UNITED STATES COURT OF APPEALS
                                   FOR THE SIXTH CIRCUIT



 UNITED STATES OF AMERICA,                                   ┐
                                    Plaintiff-Appellee,      │
                                                             │
                                                              >        No. 18-1821
        v.                                                   │
                                                             │
                                                             │
 CHRISTOPHER PAYTON MAY-SHAW,                                │
                           Defendant-Appellant.              │
                                                             ┘

                          Appeal from the United States District Court
                     for the Western District of Michigan at Grand Rapids.
                   No. 1:17-cr-00057-1—Paul Lewis Maloney, District Judge.

                                   Argued: January 28, 2020

                                Decided and Filed: April 8, 2020

                     Before: MERRITT, CLAY, and BUSH, Circuit Judges.

                                      _________________

                                            COUNSEL

ARGUED: Patrick J. Hanley, Covington, Kentucky, for Appellant. Tonya R. Long, UNITED
STATES ATTORNEY’S OFFICE, Grand Rapids, Michigan, for Appellee. ON BRIEF: Patrick
J. Hanley, Covington, Kentucky, for Appellant. Sally J. Berens, UNITED STATES
ATTORNEY’S OFFICE, Grand Rapids, Michigan, for Appellee.           Christopher Payton
May-Shaw, Sandstone, Minnesota, pro se.
                                      _________________

                                             OPINION
                                      _________________

       JOHN K. BUSH, Circuit Judge. Christopher May-Shaw was sentenced to 144 months in
prison after he entered a conditional guilty plea to a charge of conspiracy to distribute cocaine.
 No. 18-1821                       United States v. May-Shaw                              Page 2


The conviction arose from police surveillance of a parking lot near his apartment building and a
covered carport next to that building, where May-Shaw parked his BMW, one of his several
vehicles. The surveillance lasted for twenty-three days and used a camera affixed to a telephone
pole on a public street and cameras in a surveillance van parked in the parking lot. After
witnessing May-Shaw engage in several suspected drug deals, the police used a drug-detecting
dog to sniff the BMW. The dog indicated the presence of narcotics in the vehicle. Based on the
dog sniff and the surveillance, the officers obtained a search warrant for May-Shaw’s apartment
and all of his vehicles. The search found evidence of drug distribution, including cash, wrappers,
and cocaine. The district court denied his motion under the Fourth Amendment to suppress the
evidence from his apartment and vehicles. May-Shaw then entered a conditional guilty plea for
conspiracy to distribute cocaine, but he preserved the right to appeal the denial of his motion to
suppress.

       As explained below, May-Shaw did not have a reasonable expectation of privacy in the
carport such that police surveillance constituted a search in violation of the Fourth Amendment.
Nor was the carport within the curtilage of his apartment such that the dog sniff was
unconstitutional. Therefore, we AFFIRM the district court’s denial of May-Shaw’s motion to
suppress.

                                                I.

       In December 2015, the City of Grand Rapids Police Department began investigating
May-Shaw for suspected involvement in drug trafficking. The Department had received tips
from Silent Observer—an organization that receives anonymous information from the public—
describing vehicles May-Shaw was using to transport drugs and a specific bag where he kept
drugs, money, and a gun. A criminal history check on May-Shaw revealed that he had one
felony firearm conviction and two felony drug convictions. Based on all of this information, the
Grand Rapids police decided to conduct surveillance of the exterior of May-Shaw’s apartment
building and the parking lot of the apartment complex.

       The apartment where May-Shaw lived is one of several units in the complex, which itself
abuts a communal parking lot. In the parking lot are covered carports, the interiors of which are
 No. 18-1821                        United States v. May-Shaw                             Page 3


easily viewable from a public vantage point on Norman Drive, a road outside of the parking lot.
May-Shaw often parked his vehicles under a covered carport close to the entrance to his
apartment building.    Nothing in the record indicates whether the carport was specifically
assigned to him, or if he had just consistently parked there.

       The carport is next to a parking lot that is accessible only from Norman Drive, and that
entrance affords almost complete visibility of the lot and adjacent apartment complex. The
owner of the complex gave police permission to conduct physical and video surveillance of the
lot. They had a good view, for only a line of trees obstructs the parking lot from public view on
the road, and there was no foliage obstructing the view in February 2016, when the surveillance
occurred.

       Most of the stakeout, lasting several weeks, was done from a van using remotely operated
cameras. Officers would park the van in the lot, moving its location every day or two. Through
this method, police observed May-Shaw loading and unloading drugs and cash from his BMW
and engaging in what officers believed to be drug deals in the parking lot.

       In addition to their surveillance from the van, on January 26, 2016, police installed a
camera on a telephone pole on Norman Drive. Officer Mesman, the principal investigator in
May-Shaw’s case, testified as to the specifics of the pole camera. According to Mesman, the
camera was affixed to the pole approximately twenty feet from the ground, and could pan from
side to side and up and down. The camera, which recorded continuously for twenty-three days,
could produce video as well as still shots. Though officers did not monitor the footage
continuously in real time, they reviewed the footage they missed by watching the recorded video.

       The pole-camera and van-camera footage captured May-Shaw engaging in what the
officers suspected were drug transactions in the parking lot. They based this conclusion on
observations of May-Shaw making brief contact with people inside their vehicles, during which
time he and the person in the car exchanged something. Also, on several occasions May-Shaw
retrieved what appeared to be evidence of drug distribution from his vehicles. For example, on
February 17, 2016, officers observed him lean into the front passenger side of one of his vehicles
and remove cash and a bag of suspected drugs, hide the items under his jacket, and carry them
 No. 18-1821                         United States v. May-Shaw                            Page 4


inside the apartment. The next day, officers watched May-Shaw reach into the back of his car
and remove a large stack of cash, which he also took inside the apartment. Soon thereafter, the
officers saw him put another two bags, which they also suspected contained drugs and cash, in
the trunk of his BMW.

       After witnessing such suspected drug transactions, the officers called in a K-9 unit for a
drug-detecting dog sniff of the BMW, where the officers had just seen May-Shaw stash the bags.
When the dog circled the BMW, which was parked directly under the carport, it alerted the
officers to the odor of narcotics.

       Based on the surveillance and dog sniff, the officers sought a search warrant. The police
relied primarily on the footage from the pole camera and the surveillance van, which showed
different angles of the same conduct described earlier. A state magistrate judge authorized a
search warrant for the apartment and three vehicles connected to May-Shaw. The apartment
search resulted in seizure of almost $2,000 in cash, a gun, drug paraphernalia and packaging
material, and nearly a pound of marijuana. In their search of the BMW, police found a kilogram
of cocaine, some fentanyl, and over $200,000 in cash. The search of one of May-Shaw’s other
vehicles, a Chevrolet Tahoe, turned up another $486 in cash. Neither May-Shaw nor his third
car was present when the police conducted the search. May-Shaw was arrested some months
later in Brooklyn, New York.

       A federal grand jury in the U.S. District Court for the Western District of Michigan
returned a superseding indictment charging May-Shaw with conspiracy to distribute and possess
with intent to distribute cocaine, possession with intent to distribute cocaine, and maintaining
drug-involved premises, in violation of 21 U.S.C. §§ 846, 841(b)(1)(A) and 856.

       May-Shaw moved the district court to suppress the evidence seized pursuant to the search
warrant, arguing that the warrantless surveillance through the pole camera and the warrantless
sniff by the drug-detecting dog of the BMW constituted unconstitutional warrantless searches.
The district court denied the motion, holding that (1) May-Shaw had no reasonable expectation
of privacy in the parking lot; (2) the area surveilled by the pole camera was not constitutionally
protected curtilage of the apartment; (3) the dog sniff was permitted under the Fourth
 No. 18-1821                         United States v. May-Shaw                              Page 5


Amendment; and (4) even if the dog sniff was unconstitutional, the remainder of the information
in the warrant affidavit was sufficient to support probable cause for the search warrant.

       May-Shaw entered a conditional guilty plea to the conspiracy count, preserving the right
to appeal the denial of the motion to suppress. He was sentenced to 144 months in prison. He
filed this timely appeal.

                                                II.

       When reviewing a district court’s decision on a motion to suppress, we use a mixed
standard of review, reviewing findings of fact for clear error and conclusions of law de novo.
United States v. Hines, 885 F.3d 919, 924 (6th Cir. 2018). Evidence should be viewed in the
light most favorable to the district court’s conclusions. United States v. McCraney, 674 F.3d
614, 616–17 (6th Cir. 2012). “[A] denial of a motion to suppress will be affirmed on appeal if
the district court’s conclusion can be justified for any reason.” United States v. Moorehead,
912 F.3d 963, 966 (6th Cir. 2019) (alteration in original) (quoting United States v. Pasquarille,
20 F.3d 682, 685 (6th Cir. 1994)).

       May-Shaw’s motion to suppress invokes the Fourth Amendment, which protects “[t]he
right of the people to be secure in their persons, houses, papers, and effects, against unreasonable
searches and seizures.”     U.S. Const. amend. IV.        May-Shaw maintains that his Fourth
Amendment rights were violated when the police conducted warrantless surveillance of the
carport outside of his apartment, and when they used a drug-detecting dog to sniff his car that
was parked in that carport. We address each argument in turn.

                                                A.

       May-Shaw argues that the district court erred in finding that the long-term surveillance of
the carport did not constitute a search. Under Fourth Amendment jurisprudence, there are two
ways in which government action may constitute a search. First, when the government gains
information by physically intruding into a constitutionally protected area—namely, “persons,
houses, papers, and effects,” U.S. Const. amend. IV—“‘a search within the original meaning of
the Fourth Amendment’ has ‘undoubtedly occurred.’” Morgan v. Fairfield Cty., 903 F.3d 553,
 No. 18-1821                       United States v. May-Shaw                               Page 6


561 (6th Cir. 2018) (quoting Florida v. Jardines, 569 U.S. 1, 5 (2013)). Second, as articulated
by the Supreme Court, a search occurs when “a government official invades an area in which ‘a
person has a constitutionally protected reasonable expectation of privacy.’” Taylor v. City of
Saginaw, 922 F.3d 328, 332 (6th Cir. 2019) (quoting Katz v. United States, 389 U.S. 347, 360
(1967) (Harlan, J., concurring)). Under the latter framework, there are two requirements for a
government intrusion to constitute a Fourth Amendment search: first, a person must exhibit “an
actual (subjective) expectation of privacy” in the place or thing searched; second, the expectation
is one “that society is prepared to recognize as ‘reasonable.’” Katz, 389 U.S. at 361.

       Because the officers’ use of the pole camera did not involve any sort of physical intrusion
into a constitutionally protected area, May-Shaw must show that he had a reasonable expectation
of privacy in the carport. Cobbling together dicta from several Fourth Amendment cases, he
argues that, although police may permissibly observe the curtilage of a home for a short period
of time, for example with an aerial flyover, see California v. Ciraolo, 476 U.S. 207, 213 (1986),
long-term video surveillance of a home’s curtilage is problematic under the Fourth Amendment,
see United States v. Anderson-Bagshaw, 509 F. App’x 396, 405 (6th Cir. 2012). There is at least
some support for that proposition, as this court and five Justices of the Supreme Court have
noted concerns about the problems with long-term warrantless surveillance. See id.; see also
United States v. Jones, 565 U.S. 400, 415, 429–30 (2012) (Sotomayor, J., concurring and Alito,
J., concurring).

       Although this argument may be compelling in theory, as applied here, it is foreclosed by
this circuit’s case law, which has consistently held that this type of warrantless surveillance does
not violate the Fourth Amendment. For example, in United States v. Houston, we held that
affixing a video camera to the top of a utility pole to record the defendant’s front porch over a
ten-week period did not violate the defendant’s Fourth Amendment rights because “agents only
observed what [the defendant] made public to any person traveling on the roads” surrounding his
home. 813 F.3d 282, 288 (6th Cir. 2016). We rejected the defendant’s claim that the length of
the period of monitoring made the surveillance constitutionally unreasonable, reasoning that it is
the possibility—not the practicability—that the police could have themselves sat atop the utility
pole and observed the same view for every waking moment of a ten-week period that is critical.
 No. 18-1821                             United States v. May-Shaw                                        Page 7


Id. at 289–90. That reasoning was applied in United States v. Powell, in which we held that the
warrantless surveillance of three buildings through the installation of video cameras on three
public utility poles, for periods of up to 90 days each, did not violate the defendants’ Fourth
Amendment rights. 847 F.3d 760, 773 (6th Cir. 2017). And, even assuming that May-Shaw is
correct that the carport constitutes the curtilage of his apartment—an argument that we find
unpersuasive, for reasons discussed below—that is of no consequence to the constitutional
analysis of the video surveillance. We held in Houston that warrantless video surveillance of the
defendant’s front porch, which is unquestionably within the curtilage of his home, did not violate
his reasonable expectation of privacy because the camera “captured only views that were plainly
visible to any member of the public who drove down the roads bordering” his home. Houston,
813 F.3d at 288.

        May-Shaw contends that the pole camera did not provide the same vantage point that was
readily accessible from the street.1 The district court, however, held that the area surveilled by
the pole camera was readily accessible from a public vantage point. This is a factual finding that
is reviewed for clear error. Officer Mesman testified that the vantage point from the pole camera
was the same as the vantage point from the street, and nothing in the record contradicts that
assertion. Therefore, the district court’s factual finding that the pole camera recorded the same
view enjoyed by an individual standing on Norman Avenue was not clearly erroneous.

        Furthermore, the surveillance footage and photos here did not “generate[] a precise,
comprehensive record of [May-Shaw’s] public movements that reflects a wealth of detail about
[his] familial, political, professional, religious, and sexual associations,” Jones, 565 U.S. at 415


        1The     parties dispute which camera or cameras recorded the illicit activity. May-Shaw claims that the
footage was captured by the pole camera, whereas the government maintains that the incriminating footage came
from the cameras in the van. Though the officers did not keep a log of which images came from each camera, a
comparison of two sets of photos available at R. 60-2, PageID 236–37 clearly indicates that the close-up images
showing May-Shaw engaged in suspected drug transactions did not come from the more remote camera affixed to
the telephone pole. May-Shaw does not point to anything other than the lack of a log to suggest that the images did
not come from the surveillance van cameras. Appellant Br. at 13. If the images were in fact recorded from the
surveillance van rather than from the pole camera, then this is a simple case of police surveillance from a publicly
accessible area, in which the police had permission to conduct the surveillance. This does not raise the same Fourth
Amendment concerns. See United States v. Gooch, 499 F.3d 596, 602–03 (6th Cir. 2007) (noting that an individual
does not have a reasonable expectation of privacy in an openly accessible parking lot, and so police surveillance in
that lot did not constitute a search).
 No. 18-1821                       United States v. May-Shaw                              Page 8


(Sotomayor, J., concurring), which could raise significant Fourth Amendment concerns. Rather,
the footage and photos only revealed what May-Shaw did in a public space—the parking lot.
They captured images of May-Shaw moving things from his car to his apartment. The video
showed when he arrived and left the apartment. In other words, the cameras observed only what
“was possible for any member of the public to have observed . . . during the surveillance period.”
Houston, 813 F.3d at 290.

       May-Shaw has not demonstrated that when the government surveilled the carport for
twenty-three days, it violated his reasonable expectation of privacy and thus conducted an
unconstitutional search. We find no error in the district court’s judgment that the pole-camera
surveillance did not violate May-Shaw’s Fourth Amendment rights.

                                               B.

       May-Shaw also argues that the district court should have granted his motion to suppress
because the use of the drug-detecting dog to sniff his BMW while it was parked in the carport
constituted an unlawful search under the Fourth Amendment. This argument hinges on one
issue: whether the carport where the vehicle was parked constitutes the curtilage of the
apartment.

       As relevant here, the Fourth Amendment protects the people from “unreasonable
searches” of “their . . . houses.” And, as a general rule, the curtilage of a home is protected by
the Fourth Amendment. See United States v. Dunn, 480 U.S. 294, 300 (1987); see also Jardines,
569 U.S. at 6 (noting that the area “immediately surrounding and associated with the home” is
“part of the home itself for Fourth Amendment purposes” (quoting Oliver v. United States, 466
U.S. 170, 180 (1984))). That rule is well-rooted in history. “At the founding, curtilage was
considered part of the ‘hous[e]’ itself.” Collins v. Virginia, 138 S. Ct. 1663, 1676 (2018)
(Thomas, J., concurring) (alteration in original) (quoting 4 W. Blackstone, Commentaries on the
Laws of England 225 (1769) (“[T]he capital house protects and privileges all its branches and
appurtenants, if within the curtilage.”)). “The protection afforded the curtilage is essentially a
protection of families and personal privacy in an area intimately linked to the home, both
 No. 18-1821                       United States v. May-Shaw                               Page 9


physically and psychologically, where privacy expectations are most heightened.” Id. at 1670
(majority opinion) (quoting Ciraolo, 476 U.S. at 212–213).

       Although it is well-settled that the warrantless search of a home’s curtilage with a drug-
sniffing dog violates the Fourth Amendment, Jardines, 569 U.S. at 11–12, what constitutes
curtilage for purposes of the Fourth Amendment generally, and in the present case in particular,
are harder questions. If the carport was within the curtilage of May-Shaw’s apartment, then the
dog sniff constituted an unconstitutional warrantless search under Jardines, but if the carport was
not within the curtilage, then the sniff was not a search, and therefore was not constitutionally
problematic. See United States v. Perez, 440 F.3d 363, 375 (6th Cir. 2006) (holding that using a
drug-sniffing dog on a car parked in a hotel parking lot, which was not stopped, detained, or
moved, did not constitute a search).

       Courts have identified four factors as guideposts to determining whether an area falls
within a home’s curtilage: (1) the proximity of the area to the home, (2) whether the area is
within an enclosure around the home, (3) how that area is used, and (4) what the owner has done
to protect the area from observation from passersby. Morgan, 903 F.3d at 561 (citing Dunn, 480
U.S. at 301). These factors are not to be applied mechanically; rather, they are “useful analytical
tools only to the degree that, in any given case, they bear upon the centrally relevant
consideration—whether the area in question is so intimately tied to the home itself that it should
be placed under the home’s ‘umbrella’ of Fourth Amendment protection.” Dunn, 480 U.S. at
301. In the application of the factors, the onus is on May-Shaw: he “bears the burden of
establishing that the challenged search violated his Fourth Amendment rights.” United States v.
Coleman, 923 F.3d 450, 455 (6th Cir. 2019) (quoting United States v. Witherspoon, 467 F.
App’x 486, 490 (6th Cir. 2012)).

       The Supreme Court recently held that an enclosed driveway abutting a house constituted
the curtilage of the home. Collins, 138 S. Ct. at 1670–71. In Collins, police searched a
motorcycle that was covered by a tarp and was parked in a section of a driveway that was
partitioned off by two brick walls and a wall of the house itself. Id. at 1670. “A visitor
endeavoring to reach the front door of the house would have to walk partway up the driveway,
but would turn off before entering the enclosure and instead proceed up a set of steps leading to
 No. 18-1821                          United States v. May-Shaw                           Page 10


the front porch.” Id. at 1671. The Court held that the driveway enclosure “constitute[d] ‘an area
adjacent to the home and “to which the activity of home life extends,”’ and so is properly
considered curtilage.” Id. (quoting Jardines, 569 U.S. at 7).

       May-Shaw argues that Collins is dispositive here, and that because the carport was
partially enclosed, it constitutes the curtilage of the apartment. But Collins does not mandate
that result. At least three cases in this circuit cut against May-Shaw’s position.

       First, there is Coleman, mentioned above. There, we found that the defendant’s car was
not within the curtilage of his condo when it was parked in his condominium complex’s
driveway, reasoning in part that the driveway was communal and other condo residents
frequently walked past cars parked in front of the condo units. 923 F.3d at 456–57; see also
United States v. Jones, 893 F.3d 66, 72 (2d Cir. 2018) (“[Collins] has no effect on [the
defendant’s] appeal, which fails because the driveway in which [the defendant’s] vehicle was
parked was the shared driveway of tenants in two multi-family buildings and was not within the
curtilage of [his] private home.”).

       In addition, two Sixth Circuit cases decided prior to Collins—United States v. Galaviz,
645 F.3d 347 (6th Cir. 2011), and United States v. Estes, 343 F. App’x 97 (6th Cir. 2009)—are
instructive. Those cases involved unenclosed driveways that were adjacent to a home, and
abutted a sidewalk or alley, with no steps taken by the resident to obstruct the view of passersby.
Galaviz, 645 F.3d at 356; Estes, 343 F. App’x at 101. In both cases, we held that officers did not
intrude upon the curtilage by entering the driveway. In Galaviz we found that although the
driveway was adjacent to the house, it was not enclosed by any barrier, and the portion where
cars were parked was directly adjacent to a public sidewalk. Galaviz, 645 F.3d at 356. And in
Estes, the driveway was not curtilage because it was not enclosed, the defendant had not taken
any steps to protect it from observation by passersby, and it was used as a point of entry to the
defendant’s residence. Estes, 343 F. App’x at 101.

       May-Shaw directs the court’s attention to several cases—one from the Sixth Circuit, and
three from district courts within our circuit—in an attempt to establish a broad rule that a carport
is always within the curtilage of a home. See Appellant Br. at 26. But each of the cases he cites
 No. 18-1821                       United States v. May-Shaw                              Page 11


is factually distinct. As the first case he cites for that proposition states, “[e]very curtilage
determination is distinctive and stands or falls on its own unique set of facts.” Daughenbaugh v.
City of Tiffin, 150 F.3d 594, 598 (6th Cir. 1998) (alteration in original) (quoting United States v.
Reilly, 76 F.3d 1271, 1276 (2d Cir. 1996))).

       In Daughenbaugh, as May-Shaw notes, our court held that a detached garage was within
the curtilage of a home. Id. at 601. But there, the garage was “within natural boundaries
demarcated by the river and the heavy tree coverage . . . [and] the backyard and garage [were]
not readily visible from the street.” Id. at 599. We considered these natural boundaries to be
compelling evidence that the garage was within the curtilage of the home. Id. Furthermore, the
garage was set far back from the road, and a large tree prevented neighbors, those parked in the
driveway, and those on the street from viewing the interior of the garage. Id. at 600. Important
to the court’s calculus was that the “contents [of the garage] were only visible after a person
entered the backyard and approached the garage.” Id.

       Here, although the carport where May-Shaw parked his vehicles was the closest in
proximity to his apartment, it was not as close to the residence as other structures found to be
curtilage have been. But in any event, that factor is not determinative “without reference to the
additional Dunn factors.” Daughenbaugh, 150 F.3d at 599. In Collins, Coleman, Galaviz, and
Estes, the areas at issue were all driveways that, unlike the carport here, directly abutted homes
or condominiums. And even in those cases where the driveway was connected to the home, the
courts each held that the driveway was not curtilage.

       The second factor—whether the area is an enclosure around the home—also cuts against
May-Shaw. Here, although the area was enclosed, at least to the extent that the carport had a
roof and two side walls, it was not in an enclosure around the residence as was the walled-off
driveway in Collins, nor was it enclosed within natural boundaries of the property like the
detached garage in Daughenbaugh.

       The third factor, which relates to May-Shaw’s use of the carport, arguably weighs in his
favor because, by regularly parking his car in the carport, he contends it was sufficiently
“associated with the activities and privacies of domestic life” to ostensibly support a finding that
 No. 18-1821                        United States v. May-Shaw                              Page 12


it was within the curtilage of his apartment. Dunn, 480 U.S. at 303. However, there is no
evidence that May-Shaw had any legal right to exclude others from the carport.

       Furthermore, May-Shaw did little to protect the area from the view of passersby, and so
the fourth factor weighs against him. With respect to this last consideration, May-Shaw’s case
falls somewhere in between Collins and Coleman. Like the driveway in Collins, the carport here
was partially enclosed, which cuts at least somewhat in his favor. But, like in Coleman, May-
Shaw took no additional steps to protect the area from passersby. He did not, as did the
petitioner in Collins, cover his vehicle to shield it from view from his neighbors. See 138 S. Ct.
at 1668. And because officers could see into the carport from a camera affixed to a utility pole
across a street, it is apparent that May-Shaw did not take significant steps to protect the area from
observation.

       The burden is on May-Shaw to establish that the carport is “intimately linked to the
home, both physically and psychologically, where privacy expectations are most heightened.”
Collins, 138 S. Ct. at 1670 (quoting Ciraolo, 476 U.S. at 212–13). He has not done so. May-
Shaw has failed to establish that the carport constituted the curtilage of his apartment; the drug
dog sniff therefore did not constitute a search. See Perez, 440 F.3d at 375. Because we hold that
neither the pole-camera surveillance nor the dog sniff constituted a search, we need not decide
whether the evidence would have been admissible under the independent-source doctrine or the
good-faith exception.

                                                III.

       May-Shaw has not shown that (1) police surveillance from the pole camera violated his
reasonable expectation of privacy; or (2) the dog sniff constituted an unconstitutional search.
Therefore, we AFFIRM the district court’s denial of his motion to suppress.

```

---

## GROUP: content/cases/United States v. Mayville.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Mayville
type: case
citation: "955 F.3d 825 (2020)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir. 2020
court_level: coa
circuit: ca10
year: 2020
date_decided: 2020-04-07
docket: 19-4008
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
  opinion_url: "https://www.courtlistener.com/opinion/4742862/united-states-v-mayville/"
  cluster_id: 4742862
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Mayville
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Traffic Stops]]"
    role: Key
related:
  - "[[Traffic Stops]]"
  - "[[Rodriguez v. United States]]"
  - "[[Illinois v. Caballes]]"
  - "[[Terry Stops and Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - traffic-stop
  - rodriguez
  - dog-sniff
  - prolonged-detention
  - reasonable-suspicion
  - tenth-circuit
holding: "The Tenth Circuit affirmed, holding that a nineteen-minute traffic stop that ended with a drug-dog alert did not violate Rodriguez v. United States: an officer may run a criminal-history (Triple I) check through dispatch as a negligibly burdensome safety precaution, and because the troopers diligently pursued the stop's mission and the dog sniff was contemporaneous with that pursuit — the alert coming just before the records check returned — the stop was not unreasonably prolonged, since reasonableness, not efficiency, is the touchstone of the Fourth Amendment."
---

# United States v. Mayville

*955 F.3d 825 (10th Cir. 2020)* (No. 19-4008) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4742862 → opinion 4523209 (955 F.3d 825, decided 2020-04-07, Baldock, J.); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Around 1:45 a.m., Utah Highway Patrol Trooper Tripodi stopped John Mayville's red Audi for going 71 in a 60-mph zone and saw him hunched over as if he were trying to stash something. Over roughly the next nineteen minutes, Tripodi spoke with Mayville (about six minutes), obtained his out-of-state license but no registration, and thought him confused and drowsy; he returned to his patrol car about seven minutes in, radioed dispatch to run a warrants check and an Interstate Identification Index ("Triple I") criminal-history check, and requested a narcotics dog while working on the citation. Trooper Mackleprang arrived with a dog, Hasso, around 1:59; after Mayville was patted down and stood roadside, Hasso conducted a free-air sniff and alerted at about 2:05 — less than thirty seconds before dispatch returned the records. The ensuing search found a methamphetamine pipe and two firearms, one with a silencer. Mayville pleaded guilty to drug and unregistered-silencer charges, preserving his challenge to the denial of suppression.

## Issue
Whether the troopers violated *[[Rodriguez v. United States]]* by prolonging the traffic stop beyond the time needed to complete the tasks incident to the stop's mission — in particular, whether running a Triple I criminal-history check through dispatch (rather than the in-car computer) and awaiting the dog sniff unreasonably extended the nineteen-minute detention.

## Rule
Under *[[Rodriguez v. United States|Rodriguez]]*, an officer's authority to detain ends when the tasks tied to the traffic mission "are — or reasonably should have been — completed," and ordinary inquiries plus permissible safety precautions must be completed within a reasonable time, measured by whether officers diligently pursued the stop's mission. But the inquiry is one of reasonableness, not stopwatch efficiency: "Rodriguez does not require courts to second-guess the logistical decisions of officers so long as their actions were reasonable and diligently completed within the confines of a lawful traffic stop. This is because reasonableness — rather than efficiency — is the touchstone of the Fourth Amendment." — 955 F.3d 825, slip op. at 1. ^pin-op1

## Application
A criminal-history check is a permissible, "negligibly burdensome" safety precaution incident to a traffic stop, and *[[Rodriguez v. United States|Rodriguez]]* itself approved the Tenth Circuit's officer-safety justification for such checks. Trooper Tripodi's choice to run the Triple I check through dispatch rather than his in-car computer was reasonable given Mayville's out-of-state license and vehicle, his apparent stashing, his demeanor, and his inability to produce registration — and the district court found, without [[Common Legal Terms#clear-error|clear error]], that the Triple I check did not extend the stop. Mayville's contention that the in-car computer would have been faster failed because the record never showed how long that alternative would have taken, and the Fourth Amendment does not require officers to use the least intrusive or most efficient means conceivable. Because the dog sniff and alert were contemporaneous with the troopers' reasonably diligent pursuit of the stop's mission — the alert preceding the records response — the stop was not unlawfully prolonged, and the search was valid.

## Conclusion
**Affirmed.** Judge Baldock wrote for the panel (Bacharach, Baldock, and Murphy, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Mayville* is a representative Tenth Circuit application of *[[Rodriguez v. United States|Rodriguez]]*'s **mission-and-diligence** limit on traffic-stop duration: a dog sniff that rides along with the officer's reasonable, diligent completion of records and safety tasks — and finishes before those tasks do — does not "prolong" the stop, because reasonableness, not efficiency, controls. Teach it as the diligence-side counterpart to *[[Rodriguez v. United States|Rodriguez]]*'s prohibition on adding time for an unrelated investigation.

## Appears on
- [[Traffic Stops]] — *Key*

## Sources
- [*United States v. Mayville*, 955 F.3d 825 (10th Cir. 2020)](https://www.courtlistener.com/opinion/4742862/united-states-v-mayville/) — pinpoint: slip op. at 1 (the *Rodriguez* reasonableness-not-efficiency holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b9c97e5abfe831a8", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "955 F.3d 825 (2020)", "court": "10th Cir. 2020", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Mayville", "year": "2020"}}
{"assertion_id": "e073c7862fd5a100", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key", "title": "United States v. Mayville"}}
{"assertion_id": "f79a06d7a2b31e5d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Tenth Circuit affirmed, holding that a nineteen-minute traffic stop that ended with a drug-dog alert did not violate Rodriguez v. United States: an officer may run a criminal-history (Triple I) check through dispatch as a negligibly burdensome safety precaution, and because the troopers diligently pursued the stop's mission and the dog sniff was contemporaneous with that pursuit — the alert coming just before the records check returned — the stop was not unreasonably prolonged, since reasonableness, not efficiency, is the touchstone of the Fourth Amendment.", "title": "United States v. Mayville"}}
{"assertion_id": "9233e128fed7292b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Mayville", "varies_by_point": "false"}}
{"assertion_id": "c9dc0da574fd7fc5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Mayville"}}
```

### lake record — United States v. Mayville

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mayville",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Mayville",
    "case_name_short": "Mayville",
    "case_name_full": "",
    "input_case_name": "United States v. Mayville",
    "court": "10th Cir. 2020",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2020-04-07",
    "year": 2020,
    "docket": "19-4008",
    "cluster_id": 4742862,
    "lead_opinion_id": 4523209,
    "sibling_ids": [],
    "absolute_url": "/opinion/4742862/united-states-v-mayville/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "955 F.3d 825",
      "volume": "955",
      "reporter": "F.3d",
      "page": "825",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "955 F.3d 825",
        "volume": "955",
        "reporter": "F.3d",
        "page": "825",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "955 F.3d 825",
    "official_selection": {
      "court_class": "state",
      "selected": "955 F.3d 825",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:56:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-mayville--4742862",
      "to_record_id": "United States v. Mayville",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Mayville

```
                                                                                 FILED
                                                                     United States Court of Appeals
                                      PUBLISH                                Tenth Circuit

                      UNITED STATES COURT OF APPEALS                         April 7, 2020

                                                                        Christopher M. Wolpert
                            FOR THE TENTH CIRCUIT                           Clerk of Court
                        _________________________________

 UNITED STATES OF AMERICA,

       Plaintiff - Appellee,

 v.                                                         No. 19-4008
                                                  (D.C. No. 2:16-CR-00266-JNP-1)
 JOHN ELISHA MAYVILLE,                                        (D. Utah)

       Defendant - Appellant.
                      _________________________________

                     Appeal from the United States District Court
                               for the District of Utah
                          (D.C. No. 2:16-CR-00266-JNP-1)
                       _________________________________

Bretta Pirie, Assistant Federal Public Defender (Scott Keith Wilson, Federal Public
Defender, with her on the brief), Salt Lake City, Utah, for Defendant-Appellant.

Stewart M. Young, Assistant United States Attorney (John W. Huber, United States
Attorney, with him on the brief), Salt Lake City, Utah, for Plaintiff-Appellee.
                        _________________________________

Before BACHARACH, BALDOCK, and MURPHY, Circuit Judges.
                 _________________________________

BALDOCK, Circuit Judge.
                    _________________________________

      Defendant–Appellant John Elisha Mayville pleaded guilty to possession of

methamphetamine with intent to distribute in violation of 21 U.S.C. § 841(a)(1) and

possession of an unregistered firearm silencer in violation of 26 U.S.C. § 5861(d).

Exercising his right under the plea agreement, Defendant challenges the district court’s
denials of his motions to suppress evidence of drugs and firearms seized from his car

by Utah Highway Patrol troopers during a traffic stop. On appeal, Defendant argues

the troopers violated his Fourth Amendment rights described in Rodriguez v. United

States, 575 U.S. 348 (2015), because they unjustifiably prolonged the traffic stop

beyond the time needed to complete the tasks incident to the stop’s mission.

      Our jurisdiction arises under 28 U.S.C. § 1291, and we affirm. The Supreme

Court’s decision in Rodriguez constrains what law enforcement officers may do during

a routine traffic stop in the absence of additional reasonable suspicion. But Rodriguez

does not require courts to second-guess the logistical decisions of officers so long as

their actions were reasonable and diligently completed within the confines of a lawful

traffic stop. This is because reasonableness—rather than efficiency—is the touchstone

of the Fourth Amendment. Because the traffic stop here did not exceed the time

reasonably required to execute the tasks relevant to accomplishing the mission of the

stop, Defendant’s nineteen-minute roadside detention accorded with the Fourth

Amendment’s dictates. Thus, the district court did not err in denying Defendant’s

motions to suppress.

                                          I.

      Around 1:45 a.m. on May 6, 2016, Utah Highway Patrol Trooper Jason Tripodi

stopped a red Audi for traveling 71 m.p.h. in a 60-m.p.h. zone, in violation of state

law. After the Audi came to a stop, Trooper Tripodi observed the driver hunched over

in the vehicle as if he was “trying to stash something or hide something.” Trooper



                                          2
Tripodi approached the Audi and spoke with Defendant, who was the driver and sole

occupant of the vehicle, about his speeding.

      During this initial interaction, which lasted about six minutes, Defendant

informed Trooper Tripodi he was traveling to Grand Junction, Colorado, from Lake

Havasu, Arizona. Trooper Tripodi asked for Defendant’s license, registration, and

proof of insurance. While Defendant searched for these documents, Trooper Tripodi

noticed Defendant had trouble finding the requested paperwork. After several minutes,

Defendant provided his out-of-state driver’s license to Trooper Tripodi, but he was

unable to produce any registration documents for the vehicle.

      According to Trooper Tripodi, Defendant “seemed confused” and “wasn’t able

to multitask like a normal individual would be able to” during this initial interaction.

Trooper Tripodi also observed that Defendant seemed like he “was drowsy, or

something was wrong, something was up.” Based on these observations, Trooper

Tripodi asked Defendant if he “was okay” multiple times. Trooper Tripodi asked

Defendant to accompany him to the patrol car to chat while he filled out the paperwork

for the stop. Defendant declined this invitation and remained in his vehicle.

      Around 1:52 a.m., seven minutes after the stop began, Trooper Tripodi returned

to his patrol car and began filling out paperwork for the stop. He also radioed dispatch

to run a records check on Defendant, which consisted of two components. First,

Trooper Tripodi asked dispatch to run Defendant’s license and check for warrants.

Second, the trooper requested Defendant’s criminal history through the Interstate

Identification Index, commonly referred to as a Triple I check. After radioing dispatch

                                           3
for the records, but before dispatch returned the results, Trooper Tripodi requested a

narcotic detector dog.     He then continued working on the citation, including

“attempting to figure out whose vehicle it was because [Defendant] ha[d] no

registration paperwork.”

      At approximately 1:59 a.m., Trooper Scott Mackleprang arrived at the scene

with his narcotic detector dog, Hasso. At this point, Trooper Tripodi backed up his

patrol car because he anticipated possibly “run[ning] through sobriety tests or

something like that at a later point in the stop.” After briefly speaking with Trooper

Tripodi, who remained in his patrol car and continued to work on the citation, Trooper

Mackleprang asked Defendant to exit the vehicle so he could screen it with Hasso.

Because Defendant refused, Trooper Mackleprang requested Trooper Tripodi’s

assistance. Trooper Mackleprang observed that Defendant was “real slow to answer”

and had delayed reactions, “almost like a blank stare,” which caused him to suspect

Defendant was impaired. Defendant ultimately exited the vehicle, and Trooper Tripodi

patted him down for weapons.

      Trooper Tripodi then stood with Defendant on the side of the road while Trooper

Mackleprang had Hasso conduct a free-air sniff around the car. At approximately 2:05

a.m., Hasso alerted to the odor of narcotics in the vehicle. And less than thirty seconds

later, dispatch responded to Trooper Tripodi’s records request with information

indicating Defendant had a criminal record. The entirety of the traffic stop, from

Trooper Tripodi’s initial contact with Defendant to Hasso’s alert, lasted approximately

nineteen minutes.

                                           4
      The subsequent search of Defendant’s vehicle revealed a methamphetamine pipe

under the driver’s seat and two guns, one equipped with a silencer, in the engine

compartment. In the trunk, the troopers found roughly a pound of methamphetamine,

an ounce of heroin, and a scale. After discovering the guns and drugs, the troopers

placed Defendant under arrest.

      The grand jury indicted Defendant for possession of methamphetamine with

intent to distribute, possession of heroin with intent to distribute, possession of an

unregistered firearm silencer, and being a felon in possession of a firearm. Defendant

filed two motions to suppress in the district court, asserting several grounds for

suppressing the evidence seized during the traffic stop. As relevant here, he moved to

suppress evidence of the drugs and firearms as fruit of an unlawful seizure under the

Fourth Amendment. Specifically, Defendant argued Trooper Tripodi’s unreasonable

extension of the traffic stop resulted in the dog sniff and subsequent search of his

vehicle.

      After evidentiary hearings and oral arguments, the district court found the

troopers testified credibly and concluded Trooper Tripodi’s decision to run a Triple I

check through dispatch did not unconstitutionally extend the traffic stop.

Alternatively, the district court held the troopers possessed reasonable suspicion to

prolong the traffic stop to determine whether Defendant was impaired. The district

court accordingly denied Defendant’s motions to suppress.

      Defendant later entered a conditional guilty plea, reserving the right to appeal

the district court’s denials of his motions to suppress. The district court accepted the

                                           5
plea and sentenced Defendant to 126 months’ imprisonment. Exercising his right to

challenge the denials of his suppression motions, Defendant timely filed his notice of

appeal.

                                           II.

      “When reviewing the denial of a motion to suppress, we view the evidence in

the light most favorable to the government, accept the district court’s findings of fact

unless they are clearly erroneous, and review de novo the ultimate question of

reasonableness under the Fourth Amendment.” United States v. McNeal, 862 F.3d

1057, 1061 (10th Cir. 2017) (quoting United States v. Lopez, 849 F.3d 921, 925 (10th

Cir. 2017)). Defendant does not contest the legality of the initial traffic stop. Rather,

he contends the troopers’ actions—namely, Trooper Tripodi’s decision to run a Triple

I criminal-history check—were unrelated to the mission of the traffic stop and extended

its duration in violation of the Fourth Amendment. We disagree with Defendant’s

arguments.

                                           A.

      A traffic stop, even if brief and for a limited purpose, constitutes a “seizure”

under the Fourth Amendment and is subject to review for reasonableness. Whren v.

United States, 517 U.S. 806, 809–10 (1996). To be reasonable, a “traffic stop must be

justified at its inception and, in general, the officer’s actions during the stop must be

reasonably related in scope to ‘the mission of the stop itself.’” United States v. Cone,

868 F.3d 1150, 1152 (10th Cir. 2017) (quoting Rodriguez, 575 U.S. at 356). Because

Defendant does not contend the traffic stop was unjustified at its inception, our analysis

                                            6
is limited to whether the stop’s “manner of execution unreasonably infringe[d]” upon

Defendant’s Fourth Amendment rights. Illinois v. Caballes, 543 U.S. 405, 407 (2005).

      An officer’s authority to seize a driver “ends when tasks tied to the traffic

infraction are—or reasonably should have been—completed.” Rodriguez, 575 U.S. at

354. Officers may not prolong a stop beyond that point for the purpose of detecting

evidence of ordinary criminal wrongdoing unless separate reasonable suspicion exists

to justify further investigation. Id. at 354–55. Even de minimis delays caused by

unrelated inquiries violate the Fourth Amendment. Id. at 355–57.

      Defendant argues Trooper Tripodi unlawfully extended the stop because the

Triple I criminal-history check had no relation to his speeding—the traffic infraction

at issue—and is not one of the ordinary inquiries allowed under Rodriguez. But, as

Rodriguez explained, an officer’s mission during a traffic stop is both “to address the

traffic violation that warranted the stop and attend to related safety concerns.” Id. at

354 (emphasis added and citations omitted).        To be sure, this mission “includes

ordinary inquiries incident to” the traffic stop, which typically involve inspecting the

driver’s license, verifying the vehicle’s registration and insurance coverage, and

checking for any outstanding warrants against the driver.         Id. at 355.   Because,

however, “[t]raffic stops are ‘especially fraught with danger to police officers,’” id. at

356 (citation omitted), the Court has also included “negligibly burdensome” inquiries

an officer needs to make “to complete his mission safely” among permissible actions

incident to a traffic stop. Id. As Rodriguez explained, “[T]he government’s officer

safety interest stems from the mission of the stop itself.” Id.

                                            7
       This court has routinely permitted officers to conduct criminal-history checks

during traffic stops in the interest of officer safety. See, e.g., United States v. Burleson,

657 F.3d 1040, 1046 (10th Cir. 2011) (“[A]n officer may run a background check on a

motorist to check for warrants or criminal history even though the purpose of the stop

had nothing to do with the motorist’s history.”); United States v. Rice, 483 F.3d 1079,

1084 (10th Cir. 2007) (“While a traffic stop is ongoing . . . an officer has wide

discretion to take reasonable precautions to protect his safety. Obvious precautions

include running a background check on the driver . . . .” (citations omitted)). Notably,

in Rodriguez, the Court cited with approval our decision in United States v. Holt, 264

F.3d 1215, 1221–22 (10th Cir. 2001) (en banc), overturned on other grounds by

Muehler v. Mena, 544 U.S. 93 (2005), as an example of a proper inquiry during a traffic

stop. Rodriguez, 575 U.S. at 356; see also Cone, 868 F.3d at 1153 (recognizing

approval of Holt in Rodriguez and concluding an officer may reasonably ask questions

about a driver’s criminal history during a routine traffic stop). Our Holt decision, the

Court ably noted, “recogniz[ed] [an] officer safety justification for criminal record and

outstanding warrant checks.” Rodriguez, 575 U.S. at 356. Thus, an officer’s decision

to run a criminal-history check on an occupant of a vehicle after initiating a traffic stop

is justifiable as a “negligibly burdensome precaution” consistent with the important

governmental interest in officer safety.1


       1
         Several of our sister circuits have likewise concluded, post-Rodriguez, that an
officer may conduct a criminal-history check as part and parcel of the mission of a
traffic stop. See, e.g., United States v. Dion, 859 F.3d 114, 127 n.11 (1st Cir. 2017)
(“[T]he Supreme Court has characterized a criminal-record check as a ‘negligibly
                                             8
                                          B.

      Consistent with Rodriguez and circuit precedent, Trooper Tripodi was entitled

to inquire into Defendant’s criminal record during the traffic stop. But the question

remains whether the troopers’ conduct, including Trooper Tripodi’s decision to request

a Triple I check through dispatch rather than conduct the criminal-history check on the

computer in his patrol car, was reasonable under the circumstances. See United States

v. Windom, 863 F.3d 1322, 1327 (10th Cir. 2017) (“The touchstone of our analysis

under the Fourth Amendment is always ‘the reasonableness in all the circumstances of

the particular governmental invasion of a citizen’s personal security.’”) (citation

omitted). Defendant argues it was not. Again, we disagree.

      To repeat, an officer’s authority to seize a motorist “ends when tasks tied to the

traffic infraction are—or reasonably should have been—completed.” Rodriguez, 575

U.S. at 354. Thus, even ordinary inquiries incident to a traffic stop and permissible

safety precautions must be completed within a reasonable amount of time. Id. at 357.

In determining whether the duration of a traffic stop was reasonable, we consider



burdensome precaution’ that may be necessary in order to complete the mission of the
traffic stop safely.”) (quoting Rodriguez, 575 U.S. at 356)); United States v. Palmer,
820 F.3d 640, 651 (4th Cir. 2016) (“A police officer is entitled to inquire into a
motorist’s criminal record after initiating a traffic stop.”); United States v. Sanford,
806 F.3d 954, 956 (7th Cir. 2015) (“The trooper checked the occupants’ criminal
history on the computer in his car—a procedure permissible even without reasonable
suspicion.”); United States v. Frierson, 611 F. App’x 82, 85 (3d Cir. 2015)
(unpublished) (“Upon initially detaining the men, [the officer] reasonably addressed
the traffic violation that warranted the stop and attended to safety concerns. For
example, any preliminary delay in checking [the driver’s] license, registration, and
criminal history was justified as part of the stop.”).
                                           9
whether the officers diligently pursued the mission of the stop. Id. Accordingly,

officers may not undertake safety precautions for the purpose of lengthening the stop

to allow for investigation of unrelated criminal activity. Id. at 356.

      With these principles in mind, and objectively considering the totality of the

circumstances, we turn to examine Trooper Tripodi’s decision to run a Triple I check.

As explained above, an officer is permitted to run a criminal-history check as a safety

precaution during a traffic stop so long as the check does not unreasonably prolong the

stop. See id.; Holt, 264 F.3d at 1221–22. We see no reason to apply a different rule

simply because an officer elects to conduct a Triple I check through dispatch rather

than research a motorist’s criminal history on the computer in his patrol car. See United

States v. McRae, 81 F.3d 1528, 1536 n.6 (10th Cir. 1996) (indicating, in dicta, it is

reasonable for officers to run Triple I checks through dispatch as part of a routine

traffic stop); see also United States v. Hill, 852 F.3d 377, 380, 383 (4th Cir. 2017)

(holding, in the context of a twenty-minute stop, officers reasonably may search an

additional database for criminal history even though it “can be a lengthy process”).

      Defendant argues the Triple I check unlawfully extended the traffic stop because

Trooper Tripodi would have completed the stop sooner if he had confined himself to

checking records via the computer in his patrol vehicle. The problem with Defendant’s

argument is twofold. First, the district court made a factual finding that the Triple I

check did not extend the time period of the stop, and Defendant has not identified any

evidence demonstrating the court’s finding was clearly erroneous. Defendant points

to evidence showing it took less than a minute for Trooper Tripodi’s onboard computer

                                           10
to return information that showed Defendant had a valid license, his car was insured,

and the car was registered—though not to Defendant. But such a comparison is

irrelevant to our analysis. As defense counsel conceded at oral argument, nothing in

the record indicates how long it would have taken Trooper Tripodi to conduct either a

criminal-history inquiry or warrants check on the computer in his patrol car.

      Second, even if the Triple I check extended the duration of the stop, Trooper

Tripodi’s request for criminal-history records through dispatch was not unreasonable

as a matter of law. Trooper Tripodi, who the district court deemed credible, testified

that he conducted the Triple I check through dispatch because the computer in his

patrol car provides limited information, especially with respect to out-of-state drivers.

The record plainly shows Defendant provided an out-of-state license and was driving

an out-of-state vehicle. Moreover, Trooper Tripodi developed concerns based on

Defendant’s apparent stashing of something under the driver’s seat, Defendant’s

demeanor during their initial six-minute interaction, and Defendant’s inability to

provide registration paperwork for the vehicle. Given these circumstances, Trooper

Tripodi’s decision to run a Triple I check through dispatch—as opposed to limiting his

records check to the computer in his patrol car—did not unreasonably prolong the stop.

      Although Trooper Tripodi could have executed the traffic stop without running

the records check through dispatch, and instead relied exclusively on the information

available on the computer in his patrol car, his actions did not violate Defendant’s

Fourth Amendment rights.       As the Court has repeatedly admonished, the Fourth

Amendment does not require officers to use the least intrusive or most efficient means

                                           11
conceivable to effectuate a traffic stop. United States v. Sharpe, 470 U.S. 675, 687

(1985) (“The question is not simply whether some other alternative was available, but

whether the police acted unreasonably in failing to recognize or to pursue it.”). While

we can imagine other situations in which an officer’s decision to run a Triple I check

through dispatch would unreasonably prolong a traffic stop, that is not the case here.

The evidence in this case shows the troopers acted reasonably diligent in executing the

tasks incident to the traffic stop, and their actions did not unlawfully extend the stop

beyond the pursuit of the stop’s mission.2

      In sum, the district court determined dispatch responded to Trooper Tripodi’s

records request shortly after Hasso alerted to the presence of narcotics in Defendant’s

vehicle. Defendant has not shown, and we have not found, evidence in the record

demonstrating this factual finding was clearly erroneous. Because the dog sniff and

alert were contemporaneous with the troopers’ reasonably diligent pursuit of the stop’s


      2
          Approximately twelve minutes passed between the time Trooper Tripodi
returned to his patrol car after his initial interaction with Defendant and when Hasso
alerted to the odor of narcotics in the vehicle. During this period, Trooper Tripodi
radioed dispatch for records, worked on filling out paperwork for the stop, backed up
his vehicle to possibly perform sobriety tests, assisted Trooper Mackleprang after
Defendant refused to exit his vehicle, patted down Defendant for weapons, and further
questioned Defendant outside of the vehicle during the dog sniff. Before Trooper
Mackleprang arrived on the scene, Trooper Tripodi can be heard on his dash cam
asking a voice-activated google device about Lake Havasu, Arizona. Defendant argues
this shows Trooper Tripodi sat idle rather than performing the tasks incident to the
traffic stop. The district court, however, credited Trooper Tripodi’s testimony that
during this time he was also filling out paperwork for the citation and attempting to
figure out ownership of the vehicle. Defendant does not attempt to show this factual
finding was clearly erroneous. Based on the record before us, none of the trooper’s
individual actions suggest a lack of diligence in pursuing the mission of the stop.

                                             12
mission, the subsequent search of Defendant’s vehicle and discovery of evidence did

not violate his Fourth Amendment rights. The district court, therefore, properly denied

Defendant’s motions to suppress.3

                                          ***

      For the foregoing reasons, the judgment of the district court is AFFIRMED.




      3
         Because Trooper Tripodi did not unconstitutionally extend the traffic stop by
conducting the Triple I check through dispatch, we need not consider whether the
troopers possessed reasonable suspicion to prolong the stop to investigate Defendant’s
potential impairment. We also summarily dispose of Defendant’s meritless argument
that the troopers acted unreasonably in removing Defendant from his vehicle during
the traffic stop. See Maryland v. Wilson, 519 U.S. 408, 413–15 (1997) (reaffirming
rule that an officer may order a driver out of a vehicle during a traffic stop for officer
safety reasons); Holt, 264 F.3d at 1222 (explaining an officer “may order the driver
and passengers out of the vehicle in the interest of officer safety, even in the absence
of any particularized suspicion of personal danger”) (emphasis added).
                                           13

```

---

## GROUP: content/cases/United States v. Mendez.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Mendez
type: case
citation: "103 F.4th 1303 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 7th Cir.
court_level: coa
circuit: ca7
year: 2024
date_decided: 2024-06-10
docket: 23-1460
authority_weight: "Binding in-circuit — 7th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9524074/united-states-v-marcos-mendez/"
  cluster_id: 9524074
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Mendez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[United States v. Kolsuz]]"
  - "[[Riley v. California]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - border-search
  - forensic-search
  - manual-search
  - cell-phone
  - digital-privacy
  - seventh-circuit
holding: "The Seventh Circuit affirmed, joining its sister circuits to hold that a border search of a cell phone or other electronic device requires neither a warrant nor probable cause, and that a brief, manual search of a traveler's phone at the border (here, scrolling the photo gallery at O'Hare) is a routine border search requiring no individualized suspicion; because that valid manual search revealed child pornography, the court did not need to decide whether the later forensic extraction required reasonable suspicion, since the agents had ample suspicion by then."
---

# United States v. Mendez

*103 F.4th 1303 (7th Cir. 2024)* (No. 23-1460) · U.S. Court of Appeals for the Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9524074 → opinion 9990687 (103 F.4th 1303, decided 2024-06-10, St. Eve, J.); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Just before midnight on February 20, 2016, Marcos Mendez landed at O'Hare International Airport — a functional equivalent of the border — after a trip to Ecuador, traveling alone with a personal phone, a work phone, and a work iPad. Customs and Border Protection had issued a child-pornography "lookout" for Mendez based on a 2010 arrest and 2011 conviction, a prior inspection, his return from a country classified as a child-trafficking source, and his fitting the profile of a single adult male traveling alone. CBP Officer Callison pulled Mendez aside for secondary inspection; within thirty minutes Mendez handed over his phone and passcode. Callison manually unlocked it, scrolled the camera roll, and found thousands of pornographic images including apparent child pornography, then opened a protected "iSafe" app with more. He next conducted a roughly two-hour "forensic" DOMEX extraction that revealed additional images. Officers seized the phone but released Mendez, who remotely wiped it and fled to Mexico; he was later extradited. Charged with producing, transporting, and possessing child pornography, Mendez moved to suppress; the district court denied the motion (finding reasonable suspicion under *Wanjiku*), and he pled guilty to one production count (300 months), preserving the appeal.

## Issue
Whether the border searches of Mendez's phone — the manual scroll of the photo gallery and the subsequent forensic extraction — required a warrant, probable cause, or at least reasonable suspicion in light of *[[Riley v. California]]* and *[[Carpenter v. United States]]*.

## Rule
At the border and its functional equivalents (like an international airport), the border-search exception permits routine searches without a warrant, probable cause, or any individualized suspicion. Joining the uniform view of its sister circuits, the court held that device searches at the border require neither a warrant nor probable cause, and that a brief, manual search of a phone is routine: "We therefore agree with the consensus among circuits that brief, manual searches of a traveler's electronic device are 'routine' border searches requiring no individualized suspicion." — 103 F.4th 1303, slip op. at 13. ^pin-op13

## Application
The manual search — Officer Callison scrolling the camera roll of a phone handed over at an international airport — was a routine border search requiring no individualized suspicion, so it was valid regardless of whether the CBP lookout independently supplied reasonable suspicion. *[[Riley v. California|Riley]]* ([[Search Incident to Arrest|search incident to arrest]]) and *[[Carpenter v. United States|Carpenter]]* (cell-site location data) did not displace the border-search exception for that manual search. Because the valid manual search already revealed child pornography, the court did not need to resolve whether the more intrusive **forensic** DOMEX extraction required reasonable suspicion — an issue on which the circuits split — because by the time of that forensic search the agents "had that and more" in the way of suspicion.

## Conclusion
**Affirmed.** Judge St. Eve wrote for the panel (Hamilton, Brennan, and St. Eve, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Mendez* places the Seventh Circuit within the **cross-circuit consensus** that a brief, manual device search at the border is routine and needs no suspicion, and that no border device search requires a warrant or probable cause. Critically, it **leaves open** the forensic-search standard — the live split where the Fourth Circuit's *[[United States v. Kolsuz|Kolsuz]]* and the Ninth's *[[United States v. Cano|Cano]]* require reasonable suspicion while the Eleventh's *[[United States v. Touset|Touset]]* requires none. Teach the manual/forensic distinction and never state a settled nationwide device rule.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Mendez*, 103 F.4th 1303 (7th Cir. 2024)](https://www.courtlistener.com/opinion/9524074/united-states-v-marcos-mendez/) — pinpoint: slip op. at 13 (routine-manual-search-requires-no-suspicion holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "abcfab31a6766e35", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "103 F.4th 1303 (2024)", "court": "7th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Mendez", "year": "2024"}}
{"assertion_id": "4cd3f3009b2ad437", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key", "title": "United States v. Mendez"}}
{"assertion_id": "e0b1b5095452913b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Seventh Circuit affirmed, joining its sister circuits to hold that a border search of a cell phone or other electronic device requires neither a warrant nor probable cause, and that a brief, manual search of a traveler's phone at the border (here, scrolling the photo gallery at O'Hare) is a routine border search requiring no individualized suspicion; because that valid manual search revealed child pornography, the court did not need to decide whether the later forensic extraction required reasonable suspicion, since the agents had ample suspicion by then.", "title": "United States v. Mendez"}}
{"assertion_id": "1d734842273b3dae", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 7th Cir.", "title": "United States v. Mendez"}}
{"assertion_id": "aab3796328a6494b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Mendez", "varies_by_point": "false"}}
```

### lake record — United States v. Mendez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mendez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Marcos Mendez",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Mendez",
    "court": "7th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca7",
    "state": null,
    "date_decided": "2024-06-10",
    "year": 2024,
    "docket": "23-1460",
    "cluster_id": 9524074,
    "lead_opinion_id": 9990687,
    "sibling_ids": [],
    "absolute_url": "/opinion/9524074/united-states-v-marcos-mendez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "103 F.4th 1303",
      "volume": "103",
      "reporter": "F.4th",
      "page": "1303",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "103 F.4th 1303",
        "volume": "103",
        "reporter": "F.4th",
        "page": "1303",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "103 F.4th 1303",
    "official_selection": {
      "court_class": "coa",
      "selected": "103 F.4th 1303",
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
    "date_created": "2026-07-07T01:39:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-mendez--9524074",
      "to_record_id": "United States v. Mendez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Mendez

```
                              In the

    United States Court of Appeals
                For the Seventh Circuit
                    ____________________
No. 23-1460
UNITED STATES OF AMERICA,
                                                  Plaintiﬀ-Appellee,
                                v.

MARCOS MENDEZ,
                                              Defendant-Appellant.
                    ____________________

        Appeal from the United States District Court for the
          Northern District of Illinois, Eastern Division.
           No. 16-cr-163 — Mary M. Rowland, Judge.
                    ____________________

    ARGUED DECEMBER 5, 2023 — DECIDED JUNE 10, 2024
               ____________________

   Before HAMILTON, BRENNAN, and ST. EVE, Circuit Judges.
    ST. EVE, Circuit Judge. Marcos Mendez was passing
through customs at O’Hare International Airport after a trip
abroad when a customs agent pulled him aside for inspection,
unlocked and scrolled through his cell phone, and found child
pornography in the photo gallery. Customs agents then
seized the phone, downloaded its contents, and discovered
additional illicit images and videos of children.
2                                                     No. 23-1460

    After the district court denied Mendez’s motion to sup-
press this evidence, Mendez pled guilty to producing child
pornography but preserved this appeal of the district court’s
suppression-motion ruling. He now argues that the searches
of his phone, in light of the Supreme Court’s decisions in Riley
v. California, 573 U.S. 373 (2014), and Carpenter v. United States,
585 U.S. 296 (2018), required a warrant, probable cause, or at
least reasonable suspicion.
    The “longstanding recognition that searches at our bor-
ders without probable cause and without a warrant are none-
theless ‘reasonable’ has a history as old as the Fourth Amend-
ment itself.” United States v. Ramsey, 431 U.S. 606, 619 (1977).
That history leads us to join the uniform view of our sister
circuits to hold that searches of electronics at the border—like
any other border search—do not require a warrant or proba-
ble cause, and that the kind of routine, manual search of the
phone initially performed here requires no individualized
suspicion. We aﬃrm.
                         I. Background
A. Factual Background
   Just shy of midnight on February 20, 2016, Marcos Mendez
landed at O’Hare International Airport following a trip to Ec-
uador. He was traveling alone. Along with his baggage, Men-
dez carried with him three electronic devices: a personal cell
phone, a work phone, and a work iPad.
    Customs and Border Protection (“CBP”) had issued a
child-pornography-related “lookout” for Mendez based on
his arrest record and prior travel history. Mendez had a 2010
arrest relating to indecent solicitation of a child and child por-
nography, leading to a 2011 conviction for endangering the
No. 23-1460                                                   3

life or health of a child. Additionally, CBP previously had in-
spected Mendez in 2014 after he returned from Mexico. Dur-
ing that inspection, he claimed to have been kidnapped,
robbed of his electronic devices, and told to leave the country.
And on this particular trip, Mendez was returning from Ecua-
dor, which CBP oﬃcers classiﬁed as a potential child-traﬃck-
ing source country. Mendez also ﬁt the proﬁle for child-por-
nography oﬀenders: a single adult male traveling alone.
    Together, this information prompted CBP Investigating
Oﬃcer Richard Callison to pull Mendez aside for secondary
inspection after his arrival at O’Hare. Within the ﬁrst thirty
minutes of the inspection, Mendez gave Callison his cell
phone and its passcode. Callison manually unlocked the
phone and navigated to its camera roll. There he found thou-
sands of pornographic images, including what appeared to be
child pornography. Using the phone’s passcode, Callison also
opened a protected application called “iSafe,” where he dis-
covered more illicit images.
    Callison then moved Mendez to a private location, where
he conducted a more extensive, “forensic” examination of
Mendez’s devices. CBP agents used a data extraction technol-
ogy called “DOMEX” (Document and Media Exploitation) to
download a copy of the devices’ photos and videos. The fo-
rensic examination took about two hours and revealed more
child pornography.
    Oﬃcers seized Mendez’s cell phone but released Mendez,
who, in the days after his arrest, remotely wiped the contents
of his phone and traveled by car into Mexico with his mother.
Meanwhile, a Homeland Security Investigations (“HSI”) team
extracted the metadata—creation dates, geolocation infor-
mation, and so on—from the ﬁles that had earlier been
4                                                 No. 23-1460

downloaded from Mendez’s cell phone. That data revealed
that several of the child pornography images were taken near
Mendez’s residence in Rosemont, Illinois.
B. Procedural Background
    A grand jury indicted Mendez on two counts of producing
child pornography, in violation of 18 U.S.C. § 2251(a), one
count of transporting child pornography, in violation of 18
U.S.C. § 2252A(a)(1), and one count of possessing child por-
nography, in violation of 18 U.S.C. § 2252A(a)(5)(B). He was
extradited to the United States in January 2020.
    Mendez moved to suppress the evidence found on his cell
phone, arguing the searches violated the Fourth Amendment
because they were unsupported by either a probable-cause
supported warrant or reasonable suspicion. After an eviden-
tiary hearing in which Oﬃcer Callison and other investigating
oﬃcers testiﬁed, the district court denied the motion. Relying
in large part on our decision in United States v. Wanjiku, 919
F.3d 472 (7th Cir. 2019), the district court held that the
searches did not violate the Fourth Amendment because cus-
toms agents had reasonable suspicion by the time they began
looking through Mendez’s phone.
   Mendez pled guilty to one count of producing child por-
nography but preserved his right to appeal the district court’s
suppression ruling. He received a 300-month sentence, fol-
lowed by a ten-year term of supervised release. We now con-
sider that preserved issue, reviewing the district court’s ﬁnd-
ings of fact for clear error and questions of law de novo. See
United States v. Ostrum, 99 F.4th 999, 1004 (7th Cir. 2024).
No. 23-1460                                                                 5

                               II. Analysis
   The Fourth Amendment commands that searches and sei-
zures be reasonable. U.S. Const. amend. IV. Ordinarily, “[i]n
the absence of a warrant, a search is reasonable only if it falls
within a speciﬁc exception to the warrant requirement.” Riley,
573 U.S. at 382.
   One such exception is the border search exception. “Con-
gress, since the beginning of our Government, ‘has granted
the Executive plenary authority to conduct routine searches
and seizures at the border, without probable cause or a war-
rant, in order to regulate the collection of duties and to pre-
vent the introduction of contraband into this country.’” 1
United States v. Flores-Montano, 541 U.S. 149, 153 (2004) (quot-
ing United States v. Montoya de Hernandez, 473 U.S. 531, 537
(1985)). The government’s unquestionable authority to search
persons and eﬀects at the border is rooted in “the long-stand-
ing right of the sovereign to protect itself by stopping and ex-
amining persons and property crossing into this country.”
Ramsey, 431 U.S. at 616; see also id. at 619 (“Historically such
broad powers have been necessary to prevent smuggling and
to prevent prohibited articles from entry.”); Flores–Montano,
541 U.S. at 152 (noting that the border exception rests on the
government interest in “preventing the entry of unwanted
persons and eﬀects”). The “Fourth Amendment balance be-
tween the interests of the Government and the privacy right


    1 We treat the customs area of O’Hare International Airport as “the

functional equivalent of an international border for the purpose of inspect-
ing persons and articles arriving on international ﬂights.” Wanjiku, 919
F.3d at 480 (citing United States v. Yang, 286 F.3d 940, 944 (7th Cir. 2002));
see also Almeida-Sanchez v. United States, 413 U.S. 266, 273 (1973).
6                                                       No. 23-1460

of the individual is … struck much more favorably to the Gov-
ernment at the border.” Montoya de Hernandez, 473 U.S. at 540.
When the government acts under its “inherent authority to
protect … its territorial integrity,” its interest is “at its zenith.”
Flores-Montano, 541 U.S. at 152–53. In contrast, a traveler’s ex-
pectation of privacy at the border is simply “less.” Montoya de
Hernandez, 473 U.S. at 539.
    Accordingly, border searches have long been exempted
from warrant and probable cause requirements, and ordinar-
ily “are reasonable simply by virtue of the fact that they occur
at the border.” Flores-Montano, 541 U.S. at 152–53 (quoting
Ramsey, 431 U.S. at 616). “Routine” searches of people and ef-
fects at the border—which have included examining the con-
tents of a person’s purse, wallet, or pockets, United States v.
Carter, 592 F.2d 402 (7th Cir. 1979), opening mail, see Ramsey,
431 U.S. at 620, and disassembling and reassembling a vehi-
cle’s fuel tank, see Flores-Montano, 541 U.S. at 155—are “per se
reasonable” and require no particularized suspicion at all.
Yang, 286 F.3d at 944 (citing Ramsey, 431 U.S. at 616); see also
Montoya de Hernandez, 473 U.S. at 538 (“Routine searches of
the persons and eﬀects of entrants are not subject to any re-
quirement of reasonable suspicion, probable cause, or war-
rant.”); United States v. Johnson, 991 F.2d 1287, 1291 (7th Cir.
1993).
    Even highly intrusive, so-called “non-routine” border
searches need only reasonable suspicion. See Montoya de Her-
nandez, 473 U.S. at 541. But the Supreme Court has recognized
this “non-routine” category only in searches of a suspect’s
person. It held, for example, that a 16-hour detention for mon-
itored bowel movement of a person suspected of “smuggling
contraband in her alimentary canal” requires reasonable
No. 23-1460                                                   7

suspicion given the personal dignity and privacy interests at
stake. Id. at 541. And in this circuit, “we have confronted bor-
der searches and seizures that we characterized as arguably
non-routine”—including pat downs, partial strip searches,
visual body cavity searches, and the dismantling of luggage—
and have applied the reasonable suspicion standard. Wanjiku,
919 F.3d at 482–83 (emphasis added); see also Yang, 286 F.3d at
944, 949; Kaniﬀ v. United States, 351 F.3d 780, 784–85 (7th Cir.
2003); Johnson, 991 F.2d at 1291–94.
    Routine or otherwise, searches at the border “never” re-
quire a warrant or probable cause. Ramsey, 431 U.S. at 619
(“There has never been any additional requirement that the
reasonableness of a border search depended on the existence
of probable cause.”). At most, border searches require reason-
able suspicion. See Wanjiku, 919 F.3d at 481; United States v.
Molina-Isidoro, 884 F.3d 287, 291 (5th Cir. 2018) (“For border
searches both routine and not, no case has required a war-
rant.”). In more than 200 years of border search precedent,
neither the Supreme Court nor we have ever found a border
search unconstitutional.
    Mendez argues that Riley and Carpenter upended that
precedent by recognizing that cell phones fundamentally dif-
fer from other types of personal eﬀects. See Riley, 573 U.S. at
393; Carpenter, 585 U.S. at 318. Yet our caselaw highlights why
neither case supports altering the long-settled rule exempting
border searches from warrant and probable cause require-
ments: Riley and Carpenter had nothing to do with the border
context. See Wanjiku, 919 F.3d at 484; United States v. Wood, 16
F.4th 529, 533 (7th Cir. 2021) (“Given the context-speciﬁc
8                                                              No. 23-1460

nature of the Fourth Amendment, Riley is not readily transfer-
able to scenarios other than the one it addressed.”). 2
     Rather, Riley involved the search incident to arrest excep-
tion and “carefully tailored its analysis to that context.” Wood,
16 F.4th at 533. What is unreasonable after arrest may be per-
fectly reasonable at customs, as Riley itself anticipated. See Ri-
ley, 573 U.S. at 401–02 (“[O]ther case-speciﬁc exceptions may
still justify a warrantless search of a particular phone.”); see
also New Jersey v. T.L.O., 469 U.S. 325, 337 (1985) (Fourth
Amendment reasonableness “depends on the context within
which a search takes place.”). A border search is


    2 Wanjiku and a later decision, United States v. Skaggs, 25 F.4th 494 (7th

Cir. 2022), resolved the identical issue of electronic device searches at cus-
toms under the Fourth Amendment’s good faith exception to the warrant
requirement. “[N]o court,” we observed in Wanjiku, “had ever required
more than reasonable suspicion for any search at the border.” 919 F.3d at
479. And because we found that law enforcement had reasonable suspi-
cion to search the defendant’s phone, “[g]iven the state of the law at the
time of the[] searches,” we concluded that law enforcement had “an ob-
jectively good faith belief that their conduct did not violate the Fourth
Amendment.” Id. at 485–86. While we left the merits of the Fourth Amend-
ment issues open in those cases, we go on to reach those merits issues here
to provide clarity to law enforcement and the public on the burgeoning
practice of electronic device searches. See Molina-Isidoro, 884 F.3d at 293
(Costa, J., specially concurring) (“Courts should resist the temptation to
frequently rest their Fourth Amendment decisions on the safe haven of the
good-faith exception, lest the courts fail to give law enforcement and the
public the guidance needed to regulate their frequent interactions.”);
United States v. Bosyk, 933 F.3d 319, 332 n.10 (4th Cir. 2019) (“[W]hen a
Fourth Amendment case presents a novel question of law whose resolu-
tion is necessary to guide future action by law enforcement oﬃcers and
magistrates, there is suﬃcient reason for [a court] to decide the violation
issue before turning to the good-faith question.” (alterations in original)
(quoting Illinois v. Gates, 462 U.S. 213, 264 (1983) (White, J., concurring))).
No. 23-1460                                                                9

fundamentally diﬀerent from a search incident to arrest, not
least because “the Fourth Amendment’s balance of reasona-
bleness is qualitatively diﬀerent at the international border,”
where the government’s interest in protecting its territorial in-
tegrity is at its peak and travelers’ expectations of privacy are
diminished. Montoya de Hernandez, 473 U.S. at 538; cf. United
States v. 12 200-Ft. Reels of Super 8MM. Film, 413 U.S. 123, 125
(1973) (“Import restrictions and searches of persons or pack-
ages at the national borders rest on diﬀerent considerations
and diﬀerent rules of constitutional law from domestic regu-
lations.”). Underlying the Court’s decision in Riley was the
fact that neither of the search incident to arrest exception’s
twin concerns—preventing harm to oﬃcers and destruction
of evidence—“ha[d] much force with respect to digital con-
tent on cell phones.” Riley, 573 U.S. at 386. Here, in contrast,
we agree with the First Circuit that “given the volume of trav-
elers passing through our nation’s borders, warrantless elec-
tronic device searches are essential to the border search ex-
ception’s purpose of ensuring that the executive branch can
adequately protect the border.” 3 Alasaad v. Mayorkas, 988 F.3d
8, 17 (1st Cir. 2021).
   While Mendez argues that cell phone searches are unteth-
ered to the border search doctrine’s justiﬁcations, this case


    3 We have twice declined to extend Riley beyond the search incident

to arrest exception: to parolee searches in Wood, 16 F.4th at 533, and to
consent searches in United States v. Thurman, 889 F.3d 356, 366 n.9 (7th Cir.
2018) (ﬁnding in the consent-search context that “Riley d[id] not aﬀect our
holding” because “[a]lthough the Court discussed the unique nature of
modern cell phones as unparalleled repositories for personal information,
it did not address the consent-based exception to the warrant require-
ment”).
10                                                            No. 23-1460

illustrates that cell phones can contain the contraband the bor-
der search doctrine means to intercept: here, digital contra-
band in the form of child pornography. See United States v.
Cano, 934 F.3d 1002, 1014 (9th Cir. 2019) (“The best example
[of digital contraband] is child pornography.”). The govern-
ment’s interest in detecting child pornography at the border
is just as strong as its interest in intercepting ﬁrearms, narcot-
ics, or any other prohibited item. 4 See United States v. Touset,
890 F.3d 1227, 1235 (11th Cir. 2018) (“‘[Digital]’ child pornog-
raphy poses the same exact ‘risk’ of unlawful entry at the bor-
der as its physical counterpart.”). That digital contraband like
child pornography can pass into the country electronically or
be accessed remotely does little to diminish the government’s
interest in preventing its physical entry into the country. See


     4 Although the scope of a search conducted under an exception to the

warrant requirement must be “commensurate with its purposes,” Arizona
v. Gant, 556 U.S. 332, 339 (2009), the Ninth Circuit is the only circuit to
cabin the border search exception to detecting contraband itself. Compare
Cano, 934 F.3d at 1019 (holding that “border oﬃcials are limited to search-
ing for contraband only”), with United States v. Levy, 803 F.3d 120, 124 (2d
Cir. 2015) (noting that CBP oﬃcers “have the authority to search and re-
view a traveler’s documents and other items at the border when they rea-
sonably suspect that the traveler is engaged in criminal activity, even if the
crime falls outside the primary scope of their oﬃcial duties.”), and United
States v. Xiang, 67 F.4th 895, 900 (8th Cir. 2023) (adopting the Second Cir-
cuit’s “more sensibl[e]” position), and Alasaad, 988 F.3d at 20 (“[T]he bor-
der search exception’s purpose is not limited to interdicting contraband;
it serves to bar entry to those ‘who may bring anything harmful into this
country.’” (emphasis in original) (quoting Montoya de Hernandez, 473 U.S.
at 544)), and United States v. Aigbekaen, 943 F.3d 713, 721 (4th Cir. 2019)
(ﬁnding the purposes of the exception to be “protecting national security,
collecting duties, blocking the entry of unwanted persons, or disrupting
eﬀorts to export or import contraband”).
No. 23-1460                                                    11

id. (“If anything, the advent of sophisticated technological
means for concealing contraband only heightens the need of
the government to search property at the border.”); United
States v. Thirty-Seven Photographs, 402 U.S. 363, 376 (1971)
(“Customs oﬃcers characteristically inspect luggage and
their power to do so is not questioned … ; it is an old practice
and is intimately associated with excluding illegal articles
from the country.”). And although it was not the case here, a
border search of a cell phone could also facilitate the doc-
trine’s goal of “reasonably requiring one entering the country
to identify himself as entitled to come in.” Carroll v. United
States, 267 U.S. 132, 154 (1925).
    No circuit court has read Riley to require more than rea-
sonable suspicion to support even the most intrusive electron-
ics search at the border. See United States v. Castillo, 70 F.4th
894, 897–98 (5th Cir. 2023) (“[W]hen it comes to manual cell
phone searches at the border, our sister circuits have uni-
formly held that Riley does not require either a warrant or rea-
sonable suspicion.”); Molina-Isidoro, 884 F.3d at 293 (5th Cir.
2018); Xiang, 67 F.4th at 900 (8th Cir. 2023) (“Riley involved a
diﬀerent Fourth Amendment exception, searches incident to
arrest. No Circuit has held that the government must obtain a
warrant to conduct a routine border search of electronic de-
vices.”); Alasaad, 988 F.3d at 17 (1st Cir. 2021) (“Riley does not
command a warrant requirement for border searches of elec-
tronic devices nor does the logic behind Riley compel us to
impose one.”); Cano, 934 F.3d at 1015 (9th Cir. 2019); Touset,
890 F.3d at 1234 (11th Cir. 2018) (“Although the Supreme
Court stressed in Riley that the search of a cell phone risks a
signiﬁcant intrusion on privacy, our [caselaw makes] clear
that Riley, which involved the search-incident-to-arrest excep-
tion, does not apply to searches at the border.”); United States
12                                                   No. 23-1460

v. Vergara, 884 F.3d 1309, 1312–13 (11th Cir. 2018) (“Border
searches have long been excepted from warrant and probable
cause requirements, and the holding of Riley does not change
this rule.”); United States v. Kolsuz, 890 F.3d 133, 147 (4th Cir.
2018). We join our sister circuits to hold that a border search
of a cell phone or other electronic device requires neither a
warrant nor probable cause.
    The question remains whether the agent’s manual search
of Mendez’s phone—scrolling through its photo gallery—was
a routine search permissible without any suspicion or a “non-
routine” search requiring reasonable suspicion. Mendez con-
tends that because electronic devices carry potentially vast
troves of sensitive and personal information, we should treat
all electronic device searches as intrusive border searches re-
quiring at least reasonable suspicion. Riley itself involved a
manual phone search and no doubt indicates that all cell
phone searches are intrusive to some degree, but the privacy
concerns such searches implicate “are nevertheless tempered
by the fact that the searches are taking place at the border.”
Alasaad, 988 F.3d at 18. Moreover, manual electronic searches
at the border are typically “brief procedure[s]”—here, around
thirty minutes—practically limited in intrusiveness by the
fact that the customs agent cannot download and peruse the
phone’s entire contents. Instead, they must physically scroll
through the device, making it less likely for an agent to tap
into the revealing nooks and crannies of the phone’s
metadata, encrypted ﬁles, or deleted contents. Flores-Montano,
541 U.S. at 155; compare United States v. Cotterman, 709 F.3d
952, 960 (9th Cir. 2013) (en banc) (pre-Riley decision ﬁnding
the legitimacy of a suspicion-less “quick look and unintru-
sive” manual laptop search “not in doubt”), with Kolsuz, 890
F.3d at 136 (requiring reasonable suspicion for a month-long,
No. 23-1460                                                  13

oﬀ-site forensic analysis that yielded a nearly 900-page report
cataloguing the phone’s data).
    We therefore agree with the consensus among circuits that
brief, manual searches of a traveler’s electronic device are
“routine” border searches requiring no individualized suspi-
cion. See Castillo, 70 F.4th at 897–98 (“[W]hen it comes to man-
ual cell phone searches at the border, our sister circuits have
uniformly held that Riley does not require either a warrant or
reasonable suspicion.”); Alasaad, 988 F.3d at 19 (“[B]asic bor-
der searches [of electronic devices] are routine searches and
need not be supported by reasonable suspicion.”); Cano, 934
F.3d at 1016 (“[M]anual searches of cell phones at the border
are reasonable without individualized suspicion.”); Touset,
890 F.3d at 1233; Kolsuz, 890 F.3d at 146 n.5 (describing United
States v. Ickes, 393 F.3d 501 (4th Cir. 2005), as “treat[ing] a
[basic] search of a computer as a routine border search, requir-
ing no individualized suspicion”).
    The only point of divergence among the circuits is whether
more intrusive, forensic electronic device searches require in-
dividualized suspicion. Compare Touset, 890 F.3d at 1231 (no
suspicion required for forensic electronics search), with Cano,
934 F.3d at 1016 (reasonable suspicion required). We need not
resolve this issue today because this case does not require it.
The valid manual search of Mendez’s phone revealed child
pornography. So, even if the extensive forensic searches that
followed required reasonable suspicion, customs agents had
that and more once they found illicit images and videos of
children on Mendez’s phone during the routine search.
                                                      AFFIRMED

```

---

## GROUP: content/cases/United States v. Mendoza.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Mendoza
type: case
citation: "No. 25-1154, slip op. (3d Cir. 2026)"
parallel_cite: ""
neutral_cite: ""
court: 3d Cir.
court_level: coa
circuit: ca3
year: 2026
date_decided: 2026-01-08
docket: 25-1154
authority_weight: "Binding in-circuit — 3d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10771114/united-states-v-ryan-mendoza/"
  cluster_id: 10771114
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Mendoza
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: Key
related:
  - "[[Standing to Challenge a Search]]"
  - "[[Katz v. United States]]"
tags:
  - case
  - fourth-amendment
  - standing
  - reasonable-expectation-of-privacy
  - hotel-room
  - checkout
  - third-circuit
holding: "A hotel guest's reasonable expectation of privacy in his room ends when his rental period lapses and possession reverts to the hotel; because police searched the room roughly five hours after the noon checkout time — after the guest had failed to check out, his keycard had been deactivated, and the room had been marked vacant — Mendoza lacked a legitimate expectation of privacy and therefore had no standing to challenge the warrantless search."
aliases:
  - United States v. Mendoza
  - "United States v. Mendoza (3d Cir. 2026)"
  - United States v. Ryan Mendoza
---

# United States v. Mendoza

*No. 25-1154, slip op. (3d Cir. 2026)* · U.S. Court of Appeals for the Third Circuit · **Binding in-circuit — 3d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10771114 → precedential opinion 11237699 (Ambro, J.; No. 25-1154, decided Jan. 8, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (precedential 3d Cir. slip; no F.4th reporter cite assigned yet — S2 A3). S9 promotes. -->

## Background
Ryan Mendoza checked into a Pittsburgh hotel for a two-night stay ending February 25, with a posted noon checkout and keycards set to deactivate two hours after checkout. By noon on the departure day he had not checked out, so the hotel placed his room on a "due-out" list. A manager's check found personal items but no luggage; a later check turned up a backpack of white-powder packages, and staff called police. Officers arrived around 5:20 p.m. — some five hours after checkout — confirmed with the manager that the room was vacant and possession had reverted to the hotel, and searched it without a warrant. Mendoza, arrested that night, moved to suppress; the district court denied the motion for lack of a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Issue
Whether Mendoza retained a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the hotel room — and thus [[Standing to Challenge a Search|standing to challenge]] its search — several hours after the checkout time had passed.

## Rule
[[Standing to Challenge a Search|Fourth Amendment standing]] turns on whether the person "had 'a legitimate expectation of privacy in the invaded place.'" A guest's privacy interest in a rented room is tied to the rental period; once the period ends and control returns to the hotel, that interest dissolves. Applying this rule, the court held: "Five hours after checkout time, any expectation of privacy Mendoza had was not objectively reasonable." — slip op. at 2. ^pin-slip2

## Application
By the time officers entered, checkout had long passed, Mendoza had not extended his stay or notified the front desk, his keycard was set to deactivate, his balance would be charged, and the hotel had marked the room vacant and taken possession. Whatever expectation of privacy he might have retained briefly after noon was no longer objectively reasonable five hours later. Lacking a legitimate expectation of privacy in the room, Mendoza had no standing to contest the warrantless search, and the district court properly denied suppression.

## Conclusion
**Affirmed.** Judge Ambro wrote for the panel (Restrepo, McKee, Ambro, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Mendoza* is a clean precedential illustration of the threshold standing inquiry (*[[Standing to Challenge a Search]]*): the *[[Katz v. United States|Katz]]* reasonable-expectation-of-privacy question is answered against a guest whose rental period has expired and whose room has reverted to the hotel — no privacy interest, no standing to suppress.

## Appears on
- [[Standing to Challenge a Search]] — *Key*

## Sources
- [*United States v. Ryan Mendoza*, No. 25-1154, slip op. (3d Cir. 2026)](https://www.courtlistener.com/opinion/10771114/united-states-v-ryan-mendoza/) — pinpoint: slip op. at 2 (no reasonable expectation of privacy in a hotel room five hours after checkout). Rule quote string-matched to the CL opinion text 2026-07-07. Precedential 3d Cir. slip; no F.4th cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9ee42ce2fb673612", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 25-1154, slip op. (3d Cir. 2026)", "court": "3d Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Mendoza", "year": "2026"}}
{"assertion_id": "2b21e9960d96aeed", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key", "title": "United States v. Mendoza"}}
{"assertion_id": "63f4457b8ea999d0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A hotel guest's reasonable expectation of privacy in his room ends when his rental period lapses and possession reverts to the hotel; because police searched the room roughly five hours after the noon checkout time — after the guest had failed to check out, his keycard had been deactivated, and the room had been marked vacant — Mendoza lacked a legitimate expectation of privacy and therefore had no standing to challenge the warrantless search.", "title": "United States v. Mendoza"}}
{"assertion_id": "a32bb167c3a998ef", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 3d Cir.", "title": "United States v. Mendoza"}}
{"assertion_id": "cf958cffe904a719", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Mendoza", "varies_by_point": "false"}}
```

### lake record — United States v. Mendoza

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mendoza",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Ryan Mendoza",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Mendoza",
    "court": "3d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": "2026-01-08",
    "year": 2026,
    "docket": "25-1154",
    "cluster_id": 10771114,
    "lead_opinion_id": 11237699,
    "sibling_ids": [],
    "absolute_url": "/opinion/10771114/united-states-v-ryan-mendoza/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "coa",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "W9 RE-STAMP after pre-W5 re-key (prior stamp was on cluster 10131439). United States v. Ryan Mendoza, 3d Cir. PRECEDENTIAL slip No. 25-1154, decided 2026-01-08 (hotel-checkout REP). CL cluster 10771114 Published, citations[] empty (live-verified 2026-07-07); no F.4th cite assigned yet.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.govinfo.gov/content/pkg/USCOURTS-ca3-25-01154/pdf/USCOURTS-ca3-25-01154-0.pdf",
          "cite": "No. 25-1154 (3d Cir.) PRECEDENTIAL, filed 2026-01-08"
        },
        {
          "source": "CourtListener",
          "url": "https://www.courtlistener.com/opinion/10771114/united-states-v-ryan-mendoza/",
          "cite": "cluster 10771114 Published, citations[] empty"
        }
      ]
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
    "date_created": "2026-07-07T18:21:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-mendoza--10771114",
      "to_record_id": "United States v. Mendoza",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Mendoza

```
                                       PRECEDENTIAL

       UNITED STATES COURT OF APPEALS
            FOR THE THIRD CIRCUIT
                 ____________

                     No. 25-1154
                    ____________

          UNITED STATES OF AMERICA

                           v.

                 RYAN MENDOZA,

                                               Appellant


      Appeal from the United States District Court
       for the Western District of Pennsylvania
        (District Court No. 2:21-cr-00503-001)
      District Judge: Honorable Arthur J. Schwab

     Submitted Under Third Circuit L.A.R. 34.1(a)
               on November 13, 2025

Before: RESTREPO, McKEE, and AMBRO, Circuit Judges

            (Opinion filed: January 8, 2026)
Ryan R. Smith
Suite 820
310 Grant Street
Pittsburgh, PA 15219

             Counsel for Appellant

Adam N. Hallowell
Laura S. Irwin
Office of United States Attorney
700 Grant Street
Suite 4000
Pittsburgh, PA 15219

             Counsel for Appellee



                OPINION OF THE COURT


AMBRO, Circuit Judge

       Ryan Mendoza moved to suppress evidence the
Government obtained in its search of his hotel room after
checkout time. The District Court denied his motion, holding
that he failed to show he had a reasonable expectation of
privacy in that hotel room. We agree. Five hours after
checkout time, any expectation of privacy Mendoza had was
not objectively reasonable.




                             2
                    I.      BACKGROUND

       Around 1:00 a.m. on February 24, 2021, Ryan Mendoza
checked into a Pittsburgh hotel for a two-night stay—the night
spanning February 23 to 24 and the night spanning February
24 to 25. He obtained a receipt stating that his departure date
was February 25. On the back of each guest room door, and
usually on a plaque behind the front desk, the hotel posted signs
stating that checkout time was noon. The hotel usually set
guests’ key cards to deactivate two hours after checkout time.

         The hotel permitted guests to check out either by going
to the front desk or simply by walking out of the hotel without
notifying anyone. By noon on February 25, Mendoza had not
gone to the front desk to check out. So the hotel’s system
added him to a “due-out” list. Hotel staff check rooms on the
list to ensure they have been vacated. When the hotel manager
checked Mendoza’s room around 2:00 p.m., he saw a number
of personal items but no luggage. He marked the room as a
checkout, but found the situation odd. A few hours later, the
manager returned for another check and discovered a backpack
containing wrapped packages of white powder. He told a staff
member to call the police.

        They arrived around 5:20 p.m. Hotel staff informed the
officers that they had found a bag containing drugs in the room
of a “walk-out” guest whose stay had ended at noon that day.
Police entered the hotel room without a warrant, accompanied
by the hotel manager. In the room, the officers “double-
check[ed]” with the manager that the guest had “checked out.”
Supp. App. 4, at 8:35–8:50. The manager appeared to
understand the question as asking whether the guest physically
checked out at the front desk, so the officer sought to clarify
that the room was “vacant,” the guest “ha[d] nothing to do with




                               3
this room anymore,” possession of the room had reverted to the
hotel, and the guest would not be allowed back in if he tried to
return. Id., at 8:50–9:35. The manager confirmed this
understanding. The police also asked the manager to alert them
if the guest returned.

       Around 10:00 p.m., Mendoza returned to the hotel. He
was arrested with room keycards and the receipt in his pocket.

       Mendoza moved to suppress the fruits of the hotel room
search under the Fourth Amendment, arguing he had not
vacated the room when the police searched it warrantlessly. At
the suppression hearing, the hotel manager testified that guests
could check out either by going to the front desk or by walking
out. After the designated checkout time, walk-out guests’
balances are charged to their credit cards on file, their room
keys are deactivated, and their rooms are considered vacant.

      The District Court denied Mendoza’s motion.           He
appeals.

     II.    JURISDICTION AND STANDARD OF REVIEW

       The District Court had jurisdiction under 18 U.S.C.
§ 3231, and we have jurisdiction under 28 U.S.C. § 1291. “We
review a district court’s order denying a motion to suppress
under a mixed standard of review. We review findings of fact
for clear error, but exercise plenary review over legal
determinations.” United States v. Dyer, 54 F.4th 155, 158 (3d
Cir. 2022) (citation omitted). And “[b]ecause the District
Court denied the suppression motion, we view the facts in the
light most favorable to the Government.” Id. (quoting United
States v. Garner, 961 F.3d 264, 269 (3d Cir. 2020)).




                               4
                        III.    ANALYSIS

       As an initial step in determining whether a search
violated the Fourth Amendment, we ask whether the person
claiming its protection had “a legitimate expectation of privacy
in the invaded place.” United States v. Montalvo-Flores, 81
F.4th 339, 342 (3d Cir. 2023) (quoting Rakas v. Illinois, 439
U.S. 128, 143 (1978)). This inquiry involves a “subjective”
prong—whether the defendant actually expected privacy in
that place—and an “objective” prong—whether any such
expectation was one that society is prepared to recognize as
reasonable.1 Id. (citing Katz v. United States, 389 U.S. 347,
361 (1967) (Harlan, J., concurring)). Mendoza “bears the
burden of proving each element.” Id. at 343. If he fails his
objective burden, he cannot claim Fourth Amendment relief
even if he did have a subjective expectation of privacy.

        Under the Fourth Amendment, a hotel guest’s privacy
interest in a hotel room is the same as that of a tenant in a rented
house. Stoner v. California, 376 U.S. 483, 490 (1964). But
that interest dissipates when the guest vacates the room. Abel
v. United States, 362 U.S. 217, 241 (1960). “The hotel then
ha[s] the exclusive right to its possession,” and hotel
management may consent to a search. Id.

      There is no precedential authority in our Circuit
governing whether hotel guests maintain an objectively

1
  Courts often refer to this doctrine as a Fourth Amendment
standing inquiry because it requires defendants to demonstrate
a privacy interest in a searched place before seeking relief
under the Fourth Amendment. See Montalvo-Flores, 81 F.4th
at 342 & n.4. However, this inquiry is not jurisdictional and
should not be confused with Article III standing. Id. at n.4.




                                 5
reasonable expectation of privacy in their rooms after checkout
time if they have not taken some affirmative action to check
out. However, the many circuits to have confronted the issue
unanimously hold that the expectation lapses after checkout
time. See, e.g., United States v. Parizo, 514 F.2d 52, 55 (2d
Cir. 1975); United States v. Jackson, 585 F.2d 653, 658 (4th
Cir. 1978); United States v. Ramirez, 810 F.2d 1338, 1341 (5th
Cir. 1987); United States v. Lanier, 636 F.3d 228, 232 (6th Cir.
2011); United States v. Akin, 562 F.2d 459, 464 (7th Cir. 1977);
United States v. Larson, 760 F.2d 852, 855 (8th Cir. 1985);
United States v. Dorais, 241 F.3d 1124, 1128–30 (9th Cir.
2001); United States v. Croft, 429 F.2d 884, 887 (10th Cir.
1970); United States v. Ross, 964 F.3d 1034, 1043 (11th Cir.
2020).

        That rule makes sense. Checkout time is an appropriate
marker for the end of a guest’s possession of a room and the
resumption of possession by the hotel. Once checkout time has
passed, hotel staff may—indeed, must—enter a room to clean
it and prepare it for the next guest, who might be arriving just
a short time later.2 Leftover items can be removed by a hotel
after checkout time. Keycards can be deactivated, terminating
the guest’s access to the room. And many hotels, like the one
here, do not require guests to check out affirmatively at the
front desk; instead, they simply charge the credit card on file


2
  That hotel staff may enter a room to maintain it during a
guest’s stay does not defeat the guest’s reasonable expectation
of privacy from police intrusion. See United States v. Jeffers,
342 U.S. 48, 51 (1951). But hotel staff acquire complete
discretion to enter the room after checkout time—for example,
they may reasonably ignore a “Do Not Disturb” doorhanger
left by a guest after checkout. See Ross, 964 F.3d at 1043.




                               6
after checkout time. Accordingly, guests can lose their privacy
interests in a hotel room even without taking affirmative action
to check out.

        To argue otherwise, Mendoza points to testimony from
the hotel manager that “people come in and they think they
have the room for 24 hours.” App. 71. On the basis of this
testimony, Mendoza contends it was objectively reasonable for
him to believe he had the room for a full 48 hours after
checking in for a two-night stay. That argument fails. As a
matter of societal expectation, most hotel guests understand
that the checkout time is a fixed time of day that does not
change based on the time they checked in. Travelers receive
this information in many ways, including signage, receipts, and
the typical check-in colloquy at the front desk. Here, the
manager testified that the hotel had signs about the checkout
time posted in multiple locations. And Mendoza himself
received a receipt stating that his departure date was February
25, not February 26 as it would have been if he had the room
for 48 hours.

       Because this search happened five hours after checkout
time, and there were neither communications between
Mendoza and the hotel regarding a late checkout nor any other
potentially ambiguous circumstances, it does not raise a close
question. A future case nonetheless might. Does the
reasonable expectation of privacy disappear immediately at
checkout time, or might there be a “grace period” for stragglers
who remain slightly overtime? If there should be a grace
period, does it vary based on the patterns and practices at that
particular hotel, or the hotel’s communications with that
particular guest? Circuits disagree on these questions, and we
need not weigh in here. Compare United States v. Kitchens,
114 F.3d 29, 32 (4th Cir. 1997) (allowing guest to retain




                               7
legitimate expectation of privacy after checkout time if hotel
has pattern or practice that would make the expectation
reasonable), and Lanier, 636 F.3d at 232 (same), and Dorais,
241 F.3d at 1129 (same), and United States v. Owens, 782 F.2d
146, 150 (10th Cir. 1986) (same), with Ross, 964 F.3d at 1043
n.6 (expressly rejecting such an exception in favor of “clear
Fourth Amendment rules”).

       Instead, it is sufficient to say that any subjective
expectation of privacy Mendoza had in a hotel room five hours
after checkout time was not one that society is prepared to
recognize as reasonable. Lacking objective reasonableness, his
expectation of privacy cannot support a Fourth Amendment
claim.

                *      *      *      *      *

       To demonstrate that a search violated his rights under
the Fourth Amendment, Mendoza must first show that the
place searched was one in which he maintained a legitimate
expectation of privacy. An expectation of privacy is legitimate
only if it is objectively reasonable. Mendoza’s expectation of
privacy in his former hotel room, five hours after checkout
time, was not. As such, the police’s search of that room did
not violate his Fourth Amendment rights.

      We therefore affirm the District Court’s denial of the
motion to suppress.




                              8

```

---
