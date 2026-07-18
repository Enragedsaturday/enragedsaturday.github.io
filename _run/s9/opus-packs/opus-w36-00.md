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

## GROUP: content/cases/United States v. Trent.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Trent
type: case
citation: "No. 25-5770, slip op. (6th Cir. 2026)"
parallel_cite: ""
neutral_cite: ""
court: 6th Cir.
court_level: coa
circuit: ca6
year: 2026
date_decided: 2026-05-07
docket: 25-5770
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
  opinion_url: "https://www.courtlistener.com/opinion/10855903/united-states-v-mark-anthony-trent/"
  cluster_id: 10855903
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Trent
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: Key
related:
  - "[[Collective Knowledge and the Fellow-Officer Rule]]"
  - "[[Rodriguez v. United States]]"
  - "[[Whren v. United States]]"
tags:
  - case
  - fourth-amendment
  - collective-knowledge
  - fellow-officer-rule
  - traffic-stop
  - reasonable-suspicion
  - rodriguez-mission
  - sixth-circuit
  - unpublished
holding: "Under the collective-knowledge doctrine, the reasonable suspicion needed to prolong a completed traffic stop for a dog sniff may be imputed to the stopping officer from the knowledge of the investigating agents, even if the responding officer was unaware of the specific facts; because agents surveilling a methamphetamine 'turn-and-burn' operation had ample suspicion and the extension lasted only a minute or two, the brief prolongation was lawful and suppression was properly denied."
aliases:
  - United States v. Trent
  - "United States v. Trent (6th Cir. 2026)"
  - United States v. Mark Anthony Trent
---

# United States v. Trent

*No. 25-5770, slip op. (6th Cir. 2026)* · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10855903 → per curiam opinion 11323299 (No. 25-5770, NOT RECOMMENDED FOR PUBLICATION 26a0207n.06, decided May 7, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (unpublished 6th Cir. slip; no reporter cite — S2 A3). S9-REVERIFY: docket hand-reconstructed, then confirmed live against CL cluster 10855903 (caption/date/court/No. 25-5770); the S9 panel should re-verify the docket and holding before certification. -->

## Background
Investigators developed information from cooperating codefendants, informants, and recorded jail calls that Shaundra Hamilton was making "turn-and-burn" trips to Georgia to obtain methamphetamine for distribution in northeast Tennessee. Cell-phone pings and surveillance placed Mark Anthony Trent, driving a rented Ford Expedition, on such a trip; Homeland Security Special Agent Bulla coordinated with the Sullivan County Sheriff's Office to have Lieutenant Ford stop the vehicle and stage a canine unit. Ford stopped the Expedition for traffic violations around 2:00 a.m., finished a warning citation by about 2:10, and — after Trent and Hamilton declined consent — held them a minute or two until the dog arrived and alerted; the ensuing search found more than 18 kilograms of methamphetamine, a gun, and cash. The district court denied suppression.

## Issue
Whether Lieutenant Ford had reasonable suspicion to prolong the completed traffic stop for a dog sniff, where the facts establishing suspicion were known to the investigating agents rather than to Ford himself.

## Rule
Under *[[Rodriguez v. United States|Rodriguez]]*, prolonging a stop past its mission requires reasonable suspicion of additional wrongdoing, and the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] "includes the officer's own observations as well as information the officer receives from police reports, dispatch, and fellow officers." The court invoked the collective-knowledge doctrine: "Under the 'collective knowledge doctrine,' we may 'impute collective knowledge among multiple law enforcement agencies, even when the evidence demonstrates that the responding officer was wholly unaware of the specific facts that established reasonable suspicion.'" — slip op. at 4. ^pin-slip4

## Application
Although Lieutenant Ford himself may not have known every detail, the investigating officers collectively knew that Hamilton was running methamphetamine from Georgia, that Trent's rented vehicle had made two "turn-and-burn" Atlanta trips, that both had prior drug charges, and that the return route and license-plate cover fit trafficking patterns — knowledge imputed to Ford under the doctrine. Combined with Ford's own observation that the new rental's interior was heavily "trashed up," this supplied reasonable suspicion to extend the stop for the brief time until the canine arrived, so the one-to-two-minute prolongation was lawful.

## Conclusion
**Affirmed.** [[Common Legal Terms#per-curiam|Per curiam]] (McKeague, Readler, Bloomekatz, JJ.); the denial of suppression was upheld.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. **This is an unpublished, [[Common Legal Terms#per-curiam|per curiam]] disposition** ("NOT RECOMMENDED FOR PUBLICATION," 26a0207n.06) and is therefore non-precedential under Sixth Circuit I.O.P. 32.1(b) — persuasive only, notwithstanding the projected in-circuit authority weight. It is a clean illustration of the *[[Collective Knowledge and the Fellow-Officer Rule]]*: reasonable suspicion to extend a *[[Rodriguez v. United States|Rodriguez]]* stop may be supplied by the investigating team's collective knowledge, imputed to the officer on the scene.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key*

## Sources
- [*United States v. Mark Anthony Trent*, No. 25-5770, slip op. (6th Cir. 2026)](https://www.courtlistener.com/opinion/10855903/united-states-v-mark-anthony-trent/) — pinpoint: slip op. at 4 (collective-knowledge doctrine imputes reasonable suspicion to the responding officer). Rule quote string-matched to the CL opinion text 2026-07-07. Unpublished 6th Cir. slip (26a0207n.06), non-precedential; no reporter cite (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "25197dd1e95a8b8e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 25-5770, slip op. (6th Cir. 2026)", "court": "6th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Trent", "year": "2026"}}
{"assertion_id": "504cbaac279106ba", "dimension": "support", "kind": "home_role", "locator": {"home": "Collective Knowledge and the Fellow-Officer Rule"}, "payload": {"home": "Collective Knowledge and the Fellow-Officer Rule", "role": "Key", "title": "United States v. Trent"}}
{"assertion_id": "86e4ae73c375145c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under the collective-knowledge doctrine, the reasonable suspicion needed to prolong a completed traffic stop for a dog sniff may be imputed to the stopping officer from the knowledge of the investigating agents, even if the responding officer was unaware of the specific facts; because agents surveilling a methamphetamine 'turn-and-burn' operation had ample suspicion and the extension lasted only a minute or two, the brief prolongation was lawful and suppression was properly denied.", "title": "United States v. Trent"}}
{"assertion_id": "80f3d501b82b1ac4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "United States v. Trent"}}
{"assertion_id": "ed2ab1579af4a974", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Trent", "varies_by_point": "false"}}
```

### lake record — United States v. Trent

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Trent",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Mark Anthony Trent",
    "case_name_short": "Trent",
    "case_name_full": "",
    "input_case_name": "United States v. Trent",
    "court": "6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2026-05-07",
    "year": 2026,
    "docket": "25-5770",
    "cluster_id": 10855903,
    "lead_opinion_id": 11323299,
    "sibling_ids": [],
    "absolute_url": "/opinion/10855903/united-states-v-mark-anthony-trent/",
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
      "note": "W9 slip disposition. United States v. Mark Anthony Trent, 6th Cir. UNPUBLISHED No. 25-5770, decided 2026-05-07. CL cluster 10855903 Unpublished, citations[] empty (live-verified 2026-07-07). S9-REVERIFY FLAG: docket hand-reconstructed; CL cluster caption/date/court confirmed live, but the S9 panel should re-verify the docket number and the holding on the merits before certification.",
      "legs": [
        {
          "source": "CourtListener",
          "url": "https://www.courtlistener.com/opinion/10855903/united-states-v-mark-anthony-trent/",
          "cite": "cluster 10855903 Unpublished, No. 25-5770, 2026-05-07, citations[] empty"
        },
        {
          "source": "Official court",
          "url": "https://www.opn.ca6.uscourts.gov/",
          "cite": "6th Cir. docket 71229065 (No. 25-5770), unpublished 2026-05-07"
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
    "date_created": "2026-07-07T18:20:54Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "PRE-W5 audit: manually reconstructed identity from directly-verified CL cluster 10855903 (tool docket-collision on 25-5770 landed a wrong same-docket case; case_name rung did not surface Mark Anthony Trent). S9 re-verify."
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-trent--10855903",
      "to_record_id": "United States v. Trent",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Trent

```
                         NOT RECOMMENDED FOR PUBLICATION
                                File Name: 26a0207n.06

                                           No. 25-5770

                          UNITED STATES COURT OF APPEALS
                               FOR THE SIXTH CIRCUIT
                                                                                      FILED
                                                                                    May 07, 2026
UNITED STATES OF AMERICA,                              )                    KELLY L. STEPHENS, Clerk
                                                       )
       Plaintiff-Appellee,                             )
                                                       )    ON APPEAL FROM THE UNITED
v.                                                     )    STATES DISTRICT COURT FOR
                                                       )    THE EASTERN DISTRICT OF
MARK ANTHONY TRENT,                                    )    TENNESSEE
       Defendant-Appellant.                            )
                                                       )                                OPINION
                                                       )

Before: McKEAGUE, READLER, and BLOOMEKATZ, Circuit Judges.

       PER CURIAM. Mark Anthony Trent appeals the district court’s denial of his motion to

suppress evidence. As set forth below, we affirm the district court’s order denying his suppression

motion.

                                                I.

       Beginning in November 2023, law enforcement officers received information from

interviews with cooperating codefendants and other informants as well as from recorded jail calls

that Shaundra Hamilton was traveling to Georgia to obtain large quantities of methamphetamine

for distribution in northeast Tennessee. Based on that information, officers obtained a warrant to

“ping” the location of Hamilton’s cell phone and conducted surveillance at her residence in

Kingsport, Tennessee.

       On March 3, 2024, pings from Hamilton’s cell phone indicated that she traveled to the

Atlanta area for a short period of time and then came straight back—a “turn-and-burn” trip. That

evening, a black Ford Expedition arrived at Hamilton’s residence; officers identified Trent as the
No. 25-5770, United States v. Trent


renter of that vehicle. Criminal history checks revealed that both Trent and Hamilton had prior

drug charges.

       Officers saw Trent and Hamilton leave her residence in the Ford Expedition on March 12,

2024. Trent and Hamilton traveled through Tennessee on Interstate 75 to the Atlanta area and then

came straight back via a different route through North Carolina on Interstate 26. Special Agent

John Bulla with Homeland Security Investigations, who was following the Ford Expedition,

communicated with the Sullivan County Sheriff’s Office (SCSO) about initiating a traffic stop

once the vehicle entered Tennessee and positioning a canine unit in the area.

       Around 2:00 a.m. on March 13, 2024, Lieutenant William Ford with the SCSO stopped the

Ford Expedition for speeding, crossing the fog line, and having an illegal license plate cover. After

speaking with Hamilton, the passenger, and Trent, the driver, and gathering identification and

vehicle information from them, Lieutenant Ford returned to his cruiser, called for the canine unit,

ran a records check through the National Crime Information Center, and wrote a warning citation

for the traffic violations. Upon learning from dispatch that Trent and Hamilton were “clear,”

Lieutenant Ford finished writing the citation and then exited his cruiser around 2:10 a.m. When he

saw the canine unit pass on the other side of the interstate, Lieutenant Ford placed the citation and

other documents on the hood of his cruiser and approached the Ford Expedition to ask Trent and

Hamilton for consent to search the vehicle; they declined. Around 2:11 a.m., the canine unit

arrived. Lieutenant Ford directed Trent and Hamilton to exit the vehicle so that the dog could

perform a free air sniff; they refused. When Trent and Hamilton eventually exited the Ford

Expedition around 2:18 a.m., the dog performed an exterior sniff of the vehicle and alerted by

sitting at the driver door. The officers then searched the Ford Expedition and found 19 bags of




                                                -2-
No. 25-5770, United States v. Trent


methamphetamine with a total weight exceeding 18 kilograms, a loaded gun, cash, and drug

paraphernalia.

       A federal grand jury subsequently returned a multi-defendant, multi-count indictment

charging Trent with drug, money-laundering, and firearm offenses. Following his indictment,

Trent moved to suppress the evidence seized from the Ford Expedition on March 13, 2024, arguing

that the officers unreasonably extended the duration of the traffic stop beyond the time necessary

to address the alleged traffic violations. A magistrate judge conducted an evidentiary hearing and

issued a report recommending the denial of Trent’s suppression motion. Over Trent’s objection,

the district court adopted the magistrate judge’s report and recommendation and denied the motion.

       Trent entered a conditional guilty plea to possession with intent to distribute 50 grams or

more of methamphetamine, in violation of 21 U.S.C. § 841(a)(1) and (b)(1)(A), reserving his right

to appeal the district court’s denial of his suppression motion. See Fed. R. Crim. P. 11(a)(2). The

district court sentenced Trent to 218 months of imprisonment followed by five years of supervised

release.

                                                II.

       In this timely appeal, Trent challenges the district court’s denial of his motion to suppress

the evidence discovered during the March 13, 2024, traffic stop. On appeal from the denial of a

suppression motion, we review the district court’s factual findings for clear error and its legal

conclusions de novo. United States v. Guerrero, 168 F.4th 454, 459–60 (6th Cir. 2026). Whether

reasonable suspicion exists is a mixed question of law and fact, which we review de novo. United

States v. Taylor, 121 F.4th 590, 594 (6th Cir. 2024).

       The Fourth Amendment protects against “unreasonable searches and seizures” by

government officials. U.S. Const. amend. IV. A traffic stop is a reasonable seizure “where the


                                               -3-
No. 25-5770, United States v. Trent


police have probable cause to believe a traffic violation has occurred,” regardless of “the actual

motivations of the individual officers involved.” Whren v. United States, 517 U.S. 806, 810, 813

(1996). Trent does not dispute the legality of the initial traffic stop by Lieutenant Ford.

        Trent instead argues that Lieutenant Ford, after completing the purpose of the traffic stop,

unlawfully extended his detention without reasonable suspicion to conduct a dog sniff. An initially

lawful “traffic stop ‘can become unlawful if it is prolonged beyond the time reasonably required

to complete th[e] mission’ of issuing a warning ticket.” Rodriguez v. United States, 575 U.S. 348,

354–55 (2015) (alteration in original) (quoting Illinois v. Caballes, 543 U.S. 405, 407 (2005)).

“To prolong a traffic stop beyond its original ‘mission,’ police must have reasonable suspicion of

additional wrongdoing.” United Sates v. Jordan, 100 F.4th 714, 718 (6th Cir. 2024) (quoting

Rodriguez, 575 U.S. at 355). “A reasonable suspicion exists when, based on the totality of the

circumstances, a police officer has ‘a particularized and objective basis for suspecting the

particular person stopped of criminal activity.’” United States v. Smith, 140 F.4th 316, 319 (6th

Cir. 2025) (quoting United States v. Gross, 662 F.3d 393, 399 (6th Cir. 2011)). The totality of the

circumstances “includes the officer’s own observations as well as information the officer receives

from police reports, dispatch, and fellow officers.” United States v. McCallister, 39 F.4th 368,

374 (6th Cir. 2022). “It also ‘involves commonsense judgments and inferences about human

behavior, as well as inferences the officer may draw based on his experience and specialized

training.’” Taylor, 121 F.4th at 595 (quoting McCallister, 39 F.4th at 374).

        Lieutenant Ford’s mission effectively ended at approximately 2:10 a.m. when he exited his

cruiser after writing the citation. But contrary to Trent’s argument, Lieutenant Ford had reasonable

suspicion of additional wrongdoing to prolong the traffic stop until the canine unit arrived a minute

or two later.


                                                -4-
No. 25-5770, United States v. Trent


       Under the “collective knowledge doctrine,” we may “impute collective knowledge among

multiple law enforcement agencies, even when the evidence demonstrates that the responding

officer was wholly unaware of the specific facts that established reasonable suspicion.” United

States v. Lyons, 687 F.3d 754, 766 (6th Cir. 2012). At the time of initial traffic stop, law

enforcement officers had received information from multiple sources that Hamilton was traveling

to and from Georgia to obtain large quantities of methamphetamine for distribution in northeast

Tennessee. Officers had observed Trent’s rental vehicle at Hamilton’s residence, and the pings

from her cell phone indicated that Trent and Hamilton had made “turn-and-burn” trips to the

Atlanta area in that vehicle on March 3, 2024, and again on March 12, 2024. Special Agent Bulla

testified that drug traffickers often use rental vehicles and license plate covers, like the one on the

Ford Expedition, and take different routes, like Trent and Hamilton did on their return trip, to avoid

detection by law enforcement. Special Agent Bulla also knew about Trent’s and Hamilton’s prior

drug charges. As for Lieutenant Ford’s own observations, he testified that the Ford Expedition’s

interior was “very trashed up for it to be a brand new vehicle” but “normal” for a vehicle involved

in drug trafficking.

       Trent argues that reasonable suspicion to prolong the traffic stop was lacking because law

enforcement officers did not directly observe him engaging in any drug-trafficking activities.

According to Trent, the trip to the Atlanta area “gave rise to no more than a hunch of criminal

activity.” As the district court pointed out, direct observation of drug-trafficking activities is

relevant but not required to establish reasonable suspicion. See, e.g., United States v. Williams, 68

F.4th 304, 308–09 (6th Cir. 2023). Based on the totality of the circumstances, Lieutenant Ford

had reasonable suspicion to prolong the traffic stop to conduct a dog sniff.




                                                 -5-
No. 25-5770, United States v. Trent


                                            III.

       For these reasons, we AFFIRM the district court’s denial of Trent’s motion to suppress

evidence.




                                            -6-

```

---

## GROUP: content/cases/United States v. Tuggle.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Tuggle"
type: case
citation: "4 F.4th 505 (2021)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Seventh Circuit"
court_level: coa
circuit: 7th
year: 2021
date_decided: 2021-07-14
docket: 20-2352
authority_weight: "Binding in-circuit — 7th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2021-07-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Tuggle
  varies_by_point: false
  scope_note: "Issue of first impression; courts split on long-term pole-camera surveillance."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4899735/united-states-v-travis-tuggle/"
  cluster_id: 4899735
  opinion_id: 4703514
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Recent development (role-based)"
  - page: "[[Aerial and Enhanced Surveillance]]"
    role: "Related (cross-doctrine — pole camera)"
related: ["[[California v. Ciraolo]]", "[[California v. Greenwood]]", "[[Carpenter v. United States]]", "[[United States v. Jones]]"]
aliases: ["United States v. Tuggle (7th Cir. 2021)", "United States v. Travis Tuggle"]
tags: ["case", "fourth-amendment", "plain-view", "pole-camera", "surveillance", "mosaic-theory", "seventh-circuit"]
holding: "Long-term pole-camera surveillance of a home's exterior did not violate the Fourth Amendment under existing doctrine, BUT the court…"
lake:
  record_id: United States v. Tuggle
  status: verified
  projected_at: 2026-07-06
---

# United States v. Tuggle

*4 F.4th 505 (7th Cir. 2021)* · U.S. Court of Appeals, Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Suspecting Travis Tuggle of drug trafficking, the government surveilled him for eighteen months without a warrant, installing three cameras on public property that captured the exterior of his home. When the footage was used to prosecute him, Tuggle moved to suppress it as a Fourth Amendment violation. Whether prolonged warrantless pole-camera surveillance of a home's exterior is a "search" was an issue of first impression in the Seventh Circuit.

## Issue
Whether the warrantless use of pole cameras to observe the exterior of a home on a long-term basis amounts to a "search" under the Fourth Amendment.

## Rule
No, under current doctrine: "we hold that the extensive pole camera surveillance in this case did not constitute a search under the current understanding of the Fourth Amendment." — *United States v. Tuggle*, 4 F.4th 505 (7th Cir. 2021) (slip op., at 5). ^pin-op5

The cameras captured only what was exposed to public view from a place the government was lawfully entitled to occupy. The court declined to adopt the "mosaic theory" — that aggregated long-term surveillance becomes a search — holding current Supreme Court precedent did not support it.

## Application
The three pole cameras recorded only the outside of Tuggle's home — areas exposed to public view — from public property where officers were lawfully entitled to be. Even aggregated over eighteen months, that surveillance was not a search under existing Supreme Court precedent, and the court would not treat the accumulated footage as a search under a mosaic theory. The footage was therefore admissible against Tuggle.

## Conclusion
The warrantless long-term pole-camera surveillance of the home's exterior did not constitute a Fourth Amendment search; the Seventh Circuit affirmed. The court nonetheless flagged at length the privacy dangers of pervasive aggregated surveillance, inviting legislative and further judicial attention.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 7th Cir.**
- No negative treatment within the circuit. *Tuggle* joins most federal courts of appeals in holding that pole-camera surveillance of a residence's exterior is not a search, while expressly flagging the unresolved tension with the [[Carpenter v. United States]] / [[United States v. Jones]] mosaic theory for long-term digital surveillance. Courts remain split on the question.

## Appears on
- [[Plain View Doctrine]] — *Recent development (role-based)*
- [[Aerial and Enhanced Surveillance]] — *Related (cross-doctrine — pole camera)*

## Sources
- *United States v. Tuggle*, 4 F.4th 505 (7th Cir. 2021) — https://www.courtlistener.com/opinion/4899735/united-states-v-travis-tuggle/ — pinpoint given as slip-opinion page (CourtListener carries the slip opinion; cluster 4899735 → opinion 4703514).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "902357bb81f2da42", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "4 F.4th 505 (2021)", "court": "U.S. Court of Appeals, Seventh Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Tuggle", "year": "2021"}}
{"assertion_id": "1a4aec51d86f5942", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Long-term pole-camera surveillance of a home's exterior did not violate the Fourth Amendment under existing doctrine, BUT the court…", "title": "United States v. Tuggle"}}
{"assertion_id": "84099d69f4c930ed", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Recent development (role-based)", "title": "United States v. Tuggle"}}
{"assertion_id": "d7221f37663615df", "dimension": "support", "kind": "home_role", "locator": {"home": "Aerial and Enhanced Surveillance"}, "payload": {"home": "Aerial and Enhanced Surveillance", "role": "Related (cross-doctrine — pole camera)", "title": "United States v. Tuggle"}}
{"assertion_id": "70b6ee3672e736bb", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 7th Cir.", "title": "United States v. Tuggle"}}
{"assertion_id": "a661a4ff0862333a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-07-14", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Tuggle", "field_i_validity": "good_law", "scope_note": "Issue of first impression; courts split on long-term pole-camera surveillance.", "title": "United States v. Tuggle", "varies_by_point": "false"}}
```

### lake record — United States v. Tuggle

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Tuggle",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Travis Tuggle",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Tuggle",
    "court": "U.S. Court of Appeals, Seventh Circuit",
    "court_id": "ca7",
    "court_level": "coa",
    "circuit": "7th",
    "state": null,
    "date_decided": "2021-07-14",
    "year": 2021,
    "docket": "20-2352",
    "cluster_id": 4899735,
    "lead_opinion_id": 4703514,
    "sibling_ids": [
      4703514
    ],
    "absolute_url": "/opinion/4899735/united-states-v-travis-tuggle/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "4 F.4th 505",
      "volume": "4",
      "reporter": "F.4th",
      "page": "505",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "4 F.4th 505",
        "volume": "4",
        "reporter": "F.4th",
        "page": "505",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "4 F.4th 505",
    "official_selection": {
      "court_class": "coa",
      "selected": "4 F.4th 505",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op5",
      "page": null,
      "quote": "under the Fourth Amendment. ## Rule No, under current doctrine:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-07-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Tuggle",
    "varies_by_point": false,
    "scope_note": "Issue of first impression; courts split on long-term pole-camera surveillance.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Elizabeth Alicea v. County of Cook",
          "cluster_id": 9452942,
          "cite": [
            "88 F.4th 1209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis",
          "cluster_id": 7441167,
          "cite": [
            "41 F.4th 732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hay",
          "cluster_id": 9485331,
          "cite": [
            "95 F.4th 1304"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Moore-Bush",
          "cluster_id": 6476395,
          "cite": [
            "36 F.4th 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harry",
          "cluster_id": 10352104,
          "cite": [
            "130 F.4th 342"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pondexter-Moore v. District of Columbia Housing Authority",
          "cluster_id": 10830726,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lane",
          "cluster_id": 10796201,
          "cite": [
            "347 Or. App. 229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Demetrius Green",
          "cluster_id": 10652265,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rolando Antuain Williamson",
          "cluster_id": 10332827,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sidor",
          "cluster_id": 10145062,
          "cite": [
            "558 P.3d 621"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Alaska v. John William Mckelvey III",
          "cluster_id": 9485153,
          "cite": [
            "544 P.3d 632"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4703514) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca7)",
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
        "query": "cites:(4703514)",
        "reviewed": 11,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 11,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4703514)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4703514)",
    "indexed_citing_opinions": 11,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4703514,
        "count": 11,
        "count_source": "search"
      }
    ],
    "citation_count": 16,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-tuggle.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 11,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4703514,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 152441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 204000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 489983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 672897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 777810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 781890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 1027565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 2709321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 2739791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 3173994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4158218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4176845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4453948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4459782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4549954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4681147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 7268856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8312922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8410718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8414506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8704503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8710762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9429102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9429751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9430502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9430504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9431296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9434104,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9435359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9441476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9493097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9501842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9558712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9804255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9821499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9878508,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T03:13:56Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:14:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:14:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:15:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:14:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Tuggle

```
                               In the

    United States Court of Appeals
                 For the Seventh Circuit
                     ____________________
No. 20-2352
UNITED STATES OF AMERICA,
                                                   Plaintiff-Appellee,
                                 v.

TRAVIS TUGGLE,
                                               Defendant-Appellant.
                     ____________________

         Appeal from the United States District Court for the
                    Central District of Illinois.
            No. 16-cr-20070 — James E. Shadid, Judge.
                     ____________________

       ARGUED MAY 12, 2021 — DECIDED JULY 14, 2021
                ____________________

   Before FLAUM, HAMILTON, and BRENNAN, Circuit Judges.
    FLAUM, Circuit Judge. One day, in a not-so-distant future,
millions of Americans may well wake up in a smart-home-
dotted nation. As they walk out their front doors, cameras in-
stalled on nearby doorbells, vehicles, and municipal traﬃc
lights will sense and record their movements, documenting
their departure times, catching glimpses of their phone
screens, and taking note of the people that accompany them.
2                                                   No. 20-2352

    These future Americans will traverse their communities
under the perpetual gaze of cameras. Camera-studded streets,
highways, and transit networks will generate precise infor-
mation about each vehicle and its passengers, for example, re-
cording peoples’ everyday routes and deviations therefrom.
Upon arrival at their workplaces, schools, and appointments,
cameras on buildings will observe their attire and belongings
while body cameras donned on the vests of police and secu-
rity oﬃcers will record snippets of face-to-face or phone con-
versations. That same network of cameras will continue to
capture Americans from many angles as they run errands and
rendezvous to various social gatherings. By the end of the
day, millions of unblinking eyes will have discerned Ameri-
cans’ occupations and daily routines, the people and groups
with whom they associate, the businesses they frequent, their
recreational activities, and much more.
    The setting described above is not yet a total reality. None-
theless, we are steadily approaching a future with a constella-
tion of ubiquitous public and private cameras accessible to the
government that catalog the movements and activities of all
Americans. Foreseeable expansion in technological capabili-
ties and the pervasive use of ever-watching surveillance will
reduce Americans’ anonymity, transforming what once
seemed like science ﬁction into fact. Constitutionally and stat-
utorily mandated protections stand as critical bulwarks in
preserving individual privacy vis-à-vis the government in
this surveillance society. To date, however, such measures
have been challenged by the pace of technological develop-
ments.
    The Framers of the Constitution sought “to place obstacles
in the way of a too permeating police surveillance.” United
No. 20-2352                                                   3

States v. Di Re, 332 U.S. 581, 595 (1948). That central aim ani-
mated their eﬀorts, embodied in the Fourth Amendment to
the Constitution, to preserve the “right of the people to be se-
cure in their persons, houses, papers, and eﬀects, against un-
reasonable searches and seizures.” For most of our country’s
history, the concept of a “search” was tied to common-law
trespass, in other words, physical touch. Over time, however,
the evolution of technology raised complicated questions re-
garding the appropriate interpretation and scope of the
Fourth Amendment. Chief among those questions: What con-
stitutes a search in a digital society whose technology empow-
ers near-perfect surveillance without the need for physical
touch?
    To grapple with the enhanced technological capacity of
law enforcement investigations, the Supreme Court followed
Justice Harlan’s concurrence in Katz v. United States, 389 U.S.
347 (1967), and expanded its understanding of Fourth
Amendment protections. The resulting Katz test, containing
subjective and objective components, instructs courts to as-
sess ﬁrst whether a person has “exhibited an actual (subjec-
tive) expectation of privacy’” and second, whether that “ex-
pectation be one that society is prepared to recognize as ‘rea-
sonable.’” Id. at 361 (Harlan, J., concurring).
    Despite its best intentions, this expectations-based Katz
test has paved the way for a perilous circularity for new tech-
nology. Speciﬁcally, our current formulation of a Fourth
Amendment search often turns on whether a used technology
becomes widespread. Stated diﬀerently, as society’s uptake of
a new technology waxes—cars, GPS devices, cameras, and the
Internet come to mind—expectations of privacy in those tech-
nologies wane. In today’s interconnected, globalized, and
4                                                  No. 20-2352

increasingly digital world, for example, Americans largely ac-
cept that cell phones will track their locations, their Internet
usage will leave digital footprints, and ever-watching ﬁxed
cameras will monitor their movements. These evolving expec-
tations thus continually undermine themselves.
    As long as the government moves discreetly with the
times, its use of advanced technologies will likely not breach
society’s reconstituted (non)expectations of privacy. The up-
shot: the Katz test as currently interpreted may eventually af-
ford the government ever-wider latitude over the most so-
phisticated, intrusive, and all-knowing technologies with
lessening constitutional constraints.
    These observations bring us to the instant case, a harbin-
ger of the challenge to apply Fourth Amendment protections
to accommodate forthcoming technological changes. Suspect-
ing defendant Travis Tuggle’s involvement in drug traﬃck-
ing, the government surveilled him for eighteen months with-
out a warrant. The oﬃcers installed three cameras on public
property that captured the outside of Tuggle’s home. When
the government used the resulting footage to prosecute Tug-
gle, Tuggle moved to suppress the footage as violative of his
Fourth Amendment right.
    Tuggle’s case presents an issue of ﬁrst impression for this
Court: whether the warrantless use of pole cameras to observe
a home on either a short- or long-term basis amounts to a
“search” under the Fourth Amendment. The answer—and
even how to reach it—is the subject of disagreement among
our sister circuits and counterparts in state courts. Their di-
vergent answers reﬂect the complexity and uncertainty of the
prolonged use of this technology and others like it. Neverthe-
less, most federal courts of appeals that have weighed in on
No. 20-2352                                                   5

the issue have concluded that pole camera surveillance does
not constitute a Fourth Amendment search.
    Ultimately, bound by Supreme Court precedent and with-
out other statutory or jurisprudential means to cabin the gov-
ernment’s surveillance techniques presented here, we hold
that the extensive pole camera surveillance in this case did not
constitute a search under the current understanding of the
Fourth Amendment. In short, the government’s use of a tech-
nology in public use, while occupying a place it was lawfully
entitled to be, to observe plainly visible happenings, did not
run afoul of the Fourth Amendment. Therefore, we aﬃrm the
district court’s denial of Tuggle’s motion to suppress.

                      I.   Background

    Between 2013 and 2016, several law enforcement agencies
investigated a large methamphetamine distribution conspir-
acy in central Illinois that resulted in Tuggle’s prosecution.
The focus of this appeal is the government’s warrantless use
of three video cameras affixed to nearby utility poles to mon-
itor Tuggle’s residence.
    The government installed three cameras on public prop-
erty that viewed Tuggle’s home. Agents mounted two cam-
eras on a pole in an alley next to his residence and a third on
a pole one block south of the other two cameras. The first two
cameras viewed the front of Tuggle’s home and an adjoining
parking area. The third camera also viewed the outside of his
home but primarily captured a shed owned by Tuggle’s co-
conspirator and codefendant, Joshua Vaultonburg.
  Together, the three cameras captured nearly eighteen
months of footage by recording Tuggle’s property between
6                                                 No. 20-2352

2014 and 2016. Law enforcement agents installed the first
camera in August 2014, the second in December 2015, and the
third in September 2015. The officers left the three cameras on
their respective poles until March 2016.
     The cameras offered several advantages to the govern-
ment’s investigation of the drug conspiracy. While in use, the
cameras recorded around the clock. Rudimentary lighting
technology improved the quality of overnight footage, alt-
hough the cameras did not have infrared or audio capabilities.
Law enforcement agents could also remotely zoom, pan, and
tilt the cameras and review the camera footage in real time,
though the footage captured only the exterior of Tuggle’s
house. While officers frequently monitored the live feed dur-
ing business hours, they could later review all the footage,
which the government stored at the Federal Bureau of Inves-
tigation office in Springfield, Illinois. More generally, the
cameras had the practical advantage of enabling the govern-
ment to surveil Tuggle’s home without conspicuously de-
ploying agents to perform traditional visual or physical sur-
veillance on the lightly traveled roads of Tuggle’s residential
neighborhood.
    The cameras provided substantial video evidence that
supported the government’s eventual indictment of Tuggle
(and others). The officers tallied over 100 instances of what
they suspected were deliveries of methamphetamine to Tug-
gle’s residence. Camera footage depicted individuals arriving
at Tuggle’s home, carrying various items inside, and leaving
only with smaller versions of those items or sometimes noth-
ing at all. After these alleged “drops,” different individuals
would soon arrive, enter the home, and purportedly pay for
and pick up methamphetamine. Several witnesses
No. 20-2352                                                    7

corroborated these activities. Further evidencing a drug oper-
ation, the recordings showed Tuggle carrying items to Vaul-
tonburg’s shed across the street. All told, the investigating of-
ficers determined that Tuggle’s conspiracy distributed over
twenty kilograms of highly pure methamphetamine.
    Relying heavily on the video evidence, the officers secured
and executed search warrants on several locations, including
Tuggle’s house. A grand jury subsequently indicted him on
two counts: (1) a violation of 21 U.S.C. § 841(a)(1) and
(b)(1)(A) for conspiring to distribute, and possess with intent
to distribute, at least 50 grams of methamphetamine and at
least 500 grams of a mixture containing methamphetamine,
and (2) a violation of 21 U.S.C. § 856(a)(1) for maintaining a
drug-involved premises.
    Before trial, Tuggle moved to suppress the evidence ob-
tained from the pole cameras, arguing that the use of the cam-
eras constituted a warrantless search in violation of the
Fourth Amendment. The district court denied the motion in a
written opinion explaining its view that the camera usage did
not constitute a search. Thereafter, Tuggle twice moved for
the district court to reconsider, but the court denied both mo-
tions on grounds that they raised no novel arguments. The
day before trial, Tuggle entered a conditional guilty plea,
pleading guilty to both counts but reserving his right to ap-
peal the court’s denials of his motions to suppress. The district
court then sentenced him to 360 months’ imprisonment on
Count 1 and a concurrent 240 months’ imprisonment on
Count 2.
   This timely appeal followed.
8                                                    No. 20-2352

                      II.   Discussion

    The issue before us on appeal is whether the district court
correctly denied Tuggle’s motion to suppress. That issue calls
for a “dual standard of review” under which “we review legal
conclusions de novo but findings of fact for clear error.”
United States v. Edgeworth, 889 F.3d 350, 353 (7th Cir. 2018) (ci-
tation omitted).
    The Fourth Amendment provides, in part, for “[t]he right
of the people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” U.S.
Const. amend. IV. “Warrantless searches ‘are per se unreason-
able under the Fourth Amendment—subject only to a few
specifically established and well-delineated exceptions.’”
United States v. Edwards, 769 F.3d 509, 513 (7th Cir. 2014)
(quoting Arizona v. Gant, 556 U.S. 332, 338 (2009)). The gov-
ernment did not seek a warrant for the cameras here, and no
exception to the warrant requirement applies, so the diposi-
tive question is whether a Fourth Amendment search oc-
curred.
    The Supreme Court has developed two distinct paths to
identify a search: “[a] search occurs either when the govern-
ment physically intrudes without consent upon ‘a constitu-
tionally protected area in order to obtain information,’ or
‘when an expectation of privacy that society is prepared to
consider reasonable is infringed.’” United States v. Thompson,
811 F.3d 944, 948 (7th Cir. 2016) (some internal quotation
marks and citations omitted) (first quoting United States v.
Jones, 565 U.S. 400, 407 (2012); and then quoting United States
v. Karo, 468 U.S. 705, 712 (1984)). The first path, a physical in-
trusion, is not relevant because the parties agree that the
No. 20-2352                                                    9

government did not physically intrude on Tuggle’s property
by attaching the cameras to the utility poles on public prop-
erty.
    We therefore focus on the second path to finding a search,
a government infringement upon an expectation of privacy
that society is prepared to consider reasonable. This path de-
rives from Justice Harlan’s famous concurrence in Katz, which
determined that “a person has a constitutionally protected
reasonable expectation of privacy” where that person “ex-
hibit[s] an actual (subjective) expectation of privacy … that
society is prepared to recognize as ‘reasonable.’” 389 U.S. at
360–61 (Harlan, J., concurring); see also Smith v. Maryland,
442 U.S. 735, 740 (1979) (adopting Justice Harlan’s Katz test).
The Supreme Court later clarified that “Katz posits a two-part
inquiry: first, has the individual manifested a subjective ex-
pectation of privacy in the object of the challenged search?
Second, is society willing to recognize that expectation as rea-
sonable?” California v. Ciraolo, 476 U.S. 207, 211 (1986). As
“[t]he party seeking suppression,” Tuggle “bears the burden
of establishing that he had a reasonable expectation of privacy
in what was searched.” United States v. Scott, 731 F.3d 659, 663
(7th Cir. 2013).
    On appeal, Tuggle presents two different, but related, ar-
guments that the government’s use of the three pole cameras
to monitor the activities in front of and outside his house con-
stituted a search under the Fourth Amendment. First, he ar-
gues that the warrantless pole camera surveillance of his res-
idence, irrespective of the length of that surveillance use, vio-
lated his Fourth Amendment rights. Second, he argues—rely-
ing on the mosaic theory—that the “long-term, warrantless
surveillance over a period of approximately eighteen
10                                                No. 20-2352

months” amounted to a Fourth Amendment violation. We
consider each argument in turn.
      A. The Isolated Use of Cameras
    Tuggle first frames the issue as “whether the use of war-
rantless pole camera surveillance of Mr. Tuggle’s private res-
idence violated his Fourth Amendment rights?” For present
purposes, we will consider only whether the isolated use of
pole cameras—by which we mean the use of pole cameras ir-
respective of the length of that use—constitutes a Fourth
Amendment search. In other words, we ask: Did the Fourth
Amendment preclude law enforcement officers from the iso-
lated use of pole cameras on public property without a war-
rant to observe Tuggle’s private home?
    Framed as such, the answer is clearly no. At the outset, we
note that Tuggle likely has not, at Katz’s first prong, “exhib-
ited an actual (subjective) expectation of privacy” in the go-
ings-on outside of his home. Katz, 389 U.S. at 361 (Harlan, J.,
concurring). Nothing in the record suggests that Tuggle
erected any fences or otherwise tried to shield his yard or
driveway from public view, which might have signaled he
feared the wandering eye or camera lens on the street. We
therefore do not confront the more challenging situation in
which the government intentionally places cameras to see over
a fence to observe a private residence in a manner unavailable
to a ground-level passerby. See generally United States v. Cue-
vas-Sanchez, 821 F.2d 248, 251 (5th Cir. 1987) (concluding that
defendant “manifested the subjective expectation of privacy
in his backyard” because “he erected fences around [it],
screening the activity within from views of casual observers,”
and “the area monitored by the camera fell within the curti-
lage of his home, an area protected by traditional fourth
No. 20-2352                                                      11

amendment analysis”). Nevertheless, courts have not uni-
formly applied the subjective prong of the Katz test, and some
legal scholars have called its significance in resolving cases
into question. See generally Orin S. Kerr, Katz Has Only One
Step: The Irrelevance of Subjective Expectations, 82 U. Chi. L. Rev.
113, 113 (2015) (arguing that “the majority of judicial opinions
applying Katz do not even mention the subjective-expecta-
tions test; opinions that mention the test usually do not apply
it; and even when courts apply it, the test makes no difference
to the results”). Thus, we primarily focus our attention on
Katz’s objective inquiry.
    As to that objective prong—those privacy expectations so-
ciety is willing to accept as reasonable—“[t]he expectation of
privacy does not extend to ‘[w]hat a person knowingly ex-
poses to the public, even in his own home or office.’” Thomp-
son, 811 F.3d at 949 (quoting Katz, 389 U.S. at 351). The Su-
preme Court has made clear that “[t]he Fourth Amendment
protection of the home has never been extended to require
law enforcement officers to shield their eyes when passing by
a home on public thoroughfares.” Ciraolo, 476 U.S. at 213; see
also Kyllo v. United States, 533 U.S. 27, 32 (2001) (“[V]isual ob-
servation is no ‘search’ at all.”); California v. Greenwood,
486 U.S. 35, 41 (1988) (“[P]olice cannot reasonably be expected
to avert their eyes from evidence of criminal activity that
could have been observed by any member of the public.”). We
have also observed that home dwellers do not generally enjoy
a “reasonable expectation of privacy in [their] driveway[s].”
See United States v. Evans, 27 F.3d 1219, 1228–29 (7th Cir. 1994)
(collecting cases); see also United States v. French, 291 F.3d 945,
955 (7th Cir. 2002) (holding defendant had “no reasonable ex-
pectation of privacy in the driveway and gravel walkways”
leading to his home).
12                                                  No. 20-2352

    In this case, Tuggle knowingly exposed the areas captured
by the three cameras. Namely, the outside of his house and
his driveway were plainly visible to the public. He therefore
did not have an expectation of privacy that society would be
willing to accept as reasonable in what happened in front of
his home. See Evans, 27 F.3d at 1228. The Fourth Amendment
accordingly did not require officers to “shield their eyes” (or
their cameras) when passing by Tuggle’s “home on public
thoroughfares.” See Ciraolo, 476 U.S. at 213.
   Tuggle’s argument that the cameras transformed other-
wise lawful visual surveillance into unconstitutional techno-
logical surveillance does not undermine our conclusion that
the isolated use of pole cameras here did not constitute a
search. Specifically, Tuggle argues that “[w]hile the ‘fruits’ of
the pole cameras could have been achieved by traditional vis-
ual or physical surveillance, the use of technology change[d]
the reasonableness of the expectation of privacy.” See Jones,
565 U.S. at 412 (“It may be that achieving the same result
through electronic means, without an accompanying tres-
pass, is an unconstitutional invasion of privacy ….”).
    To be sure, the Supreme Court has cautioned that the gov-
ernment’s use of some technologies falls within the ambit of
the Fourth Amendment, but the Court has also affirmed that
“[n]othing in the Fourth Amendment prohibit[s] the police
from augmenting the sensory faculties bestowed upon them
at birth with such enhancement as science and technology af-
forded them in” certain instances. United States v. Knotts,
460 U.S. 276, 282 (1983).
   The prototypical example of impermissible technology for
Fourth Amendment purposes is the government’s use of a
thermal imaging device that detects relative heat levels within
No. 20-2352                                                   13

a residence. The Supreme Court held the use of the device to
be an unlawful search in violation of the Fourth Amendment
in Kyllo v. United States. 533 U.S. at 40. While the thermal im-
aging device did not physically intrude on the defendant’s
property, the Court expressed concern about “leav[ing] the
homeowner at the mercy of advancing technology.” Id. at 35.
The Court therefore held that governmental use of “a device
that is not in general public use, to explore details of the home
that would previously have been unknowable without phys-
ical intrusion,” constitutes a Fourth Amendment search “and
is presumptively unreasonable without a warrant.” Id. at 40.
    Despite the Kyllo standard, the Supreme Court has rou-
tinely approved of law enforcement officers’ use of cameras
to aid investigations. In Dow Chemical Co. v. United States,
476 U.S. 227 (1986), the Supreme Court held “that the taking
of aerial photographs of [a 2,000-acre] industrial plant com-
plex from navigable airspace is not a search prohibited by the
Fourth Amendment.” Id. at 239. The Court acknowledged that
“the technology of photography has changed in this century,”
id. at 231, and said:
       It may well be … that surveillance of private
       property by using highly sophisticated surveil-
       lance equipment not generally available to the
       public, such as satellite technology, might be
       constitutionally proscribed absent a warrant.
       But the photographs here are not so revealing of
       intimate details as to raise constitutional con-
       cerns. Although they undoubtedly give [the
       government] more detailed information than
       naked-eye views, they remain limited to an out-
       line of the facility’s buildings and equipment.
14                                                  No. 20-2352

Id. at 238. To that end, the Court noted that “[t]he mere fact
that human vision is enhanced somewhat, at least to the de-
gree here, does not give rise to constitutional problems” be-
cause the aerial photography cameras did not raise the “far
more serious questions” presented by a device that could
“penetrate walls or windows so as to hear and record confi-
dential discussions.” Id. at 238–39.
    On the same day it issued Dow Chemical, the Supreme
Court held in California v. Ciraolo that law enforcement did not
violate the Fourth Amendment when it observed and photo-
graphed the defendant’s marijuana plants while flying 1,000
feet overhead in a private plane. 476 U.S. at 209–10. The Court
explained that although the defendant may have demon-
strated a subjective expectation of privacy by erecting fences,
society was not prepared to accept that expectation as reason-
able because the government surveilled “within public navi-
gable airspace … in a physically nonintrusive manner.” Id. at
213. In other words, “[a]ny member of the public flying in this
airspace who glanced down could have seen everything that
these officers observed.” Id. at 213–14. The Court did not even
consider the impact of the camera—thus assuming it was en-
tirely permissible for officers to use cameras in that place in
which they were lawfully entitled to be.
   Despite the prevalence of cameras in today’s society, we
have not identified in our own precedent any cases in which
we squarely evaluated the constitutionality of the govern-
ment’s use of remote cameras, pole cameras, or the like, to aid
law enforcement surveillance. We have, however, acknowl-
edged the commonplace role cameras have in our society. Cf.
United States v. Paxton, 848 F.3d 803, 812 (7th Cir. 2017) (“[W]e
are fast approaching a day when police interactions with
No. 20-2352                                                                  15

civilians, including detainees, will be recorded from begin-
ning to end, and for a variety of important ends.”). Thus, the
question of whether the isolated use of pole cameras, without
a warrant, on public property is constitutional is an issue of
first impression. Our sister circuits, including the Fourth and
the Tenth Circuits, that have considered governmental reli-
ance on cameras to observe the exteriors of private homes
have held such uses to be constitutional. 1
    We likewise conclude that, under a straightforward appli-
cation of Kyllo, the isolated use of pole cameras here did not
run afoul of Fourth Amendment protections. Today, cameras
are in “general public use.” Kyllo, 533 U.S. at 40. Now more
than ever, cameras are ubiquitous, found in the hands and
pockets of virtually all Americans, on the doorbells and en-
trances of homes, and on the walls and ceilings of businesses.
See Carpenter v. United States, 138 S. Ct. 2206, 2220 (2018) (de-
clining to “call into question conventional surveillance tech-
niques and tools, such as security cameras” (emphasis added));
Paxton, 848 F.3d at 812. To that point, if some thirty years ago
extensive aerial photography of a 2,000-acre industrial prop-
erty, see Dow Chem., 476 U.S. at 229, or of marijuana plants oth-
erwise concealed at ground level, see Ciraolo, 476 U.S. at 209,
did not qualify as Fourth Amendment searches, then certainly


    1 See, e.g., United States v. Vankesteren, 553 F.3d 286, 287 (4th Cir. 2009)
(holding the government had not violated the defendant’s Fourth Amend-
ment rights through use of “a hidden, fixed-range, motion-activated video
camera placed in the [defendant’s] open fields”); United States v. Jackson,
213 F.3d 1269, 1282 (10th Cir.) (holding that “evidence obtained from the
video cameras installed on the telephone poles and the recordings made
in the undercover FBI car were not introduced in violation of … the Fourth
Amendment”), vacated on other grounds, 531 U.S. 1033 (2000).
16                                                  No. 20-2352

ground-level video footage of an unobstructed home from a
public vantage point is not a search.
    While the video cameras in this case “undoubtedly g[a]ve
[the government] more detailed information than naked-eye
views,” they did not do so to a degree that “give[s] rise to con-
stitutional problems.” See Dow Chem., 476 U.S. at 238. The gov-
ernment only used the cameras to identify who visited Tug-
gle’s house and what they carried, all things that a theoretical
officer could have observed without a camera. Cf. Thompson,
811 F.3d at 950 (“The video cameras in this case captured
nothing more than what the informant could see with his na-
ked eye.”). That the government could replay the footage and
remotely control the camera does not affect our analysis be-
cause these features are a far cry from the “highly sophisti-
cated surveillance equipment not generally available to the
public” that animated the Dow Chemical decision. 476 U.S. at
238. The cameras did not “penetrate walls or windows so as
to hear and record confidential” information, id. at 239, nor
did they “explore details of the home that would previously
have been unknowable without physical intrusion,” Kyllo,
553 U.S. at 40.
    In sum, the government used a commonplace technology,
located where officers were lawfully entitled to be, and cap-
tured events observable to any ordinary passerby. The gov-
ernment did not invade an expectation of privacy that society
would be prepared to accept as reasonable. Accordingly, the
isolated use of pole cameras here did not constitute a Fourth
Amendment search.
No. 20-2352                                                    17

       B. The Prolonged, Round-the-Clock Use of Cameras
    The more challenging question is Tuggle’s second theory
of a Fourth Amendment violation: that the prolonged and un-
interrupted use of those cameras constituted a search. Tuggle
characterizes this theory in two ways. First, he argues more
generally that the “long-term use of the pole cameras over an
extended period of approximately eighteen months violates
the Fourth Amendment.” Second, he asserts that “[a]pplying
the mosaic theory, the use of warrantless pole cameras con-
tinuously for over [eighteen] months is unconstitutional un-
der the Fourth Amendment.” While framed differently, both
Tuggle’s theories functionally ask whether the mosaic theory
supports finding a Fourth Amendment search here. To an-
swer that question, we will begin by explaining the mosaic
theory and noting that while the theory has gained some ju-
dicial traction the Supreme Court has yet to affirmatively re-
quire lower courts to apply it. Then, we will outline how other
courts have disagreed over whether prolonged pole camera
surveillance constitutes a Fourth Amendment search. Draw-
ing on those discussions—and noting our reservations—we
will finally address why the prolonged use of pole cameras
here did not constitute a Fourth Amendment search.
          1. The Mosaic Theory Generally
    In its simplest form, the mosaic theory attempts to capture
the idea that the “government can learn more from a given
slice of information if it can put that information in the context
of a broader pattern, a mosaic.” Matthew B. Kugler & Lior Ja-
cob Strahilevitz, Actual Expectations of Privacy, Fourth Amend-
ment Doctrine, and the Mosaic Theory, 2015 Sup. Ct. Rev. 205,
205 (2015). Thus, it “holds that, when it comes to people’s rea-
sonable expectations of privacy, the whole is greater than the
18                                                      No. 20-2352

sum of its parts.” Id.; see also David Gray & Danielle Keats Cit-
ron, A Shattered Looking Glass: The Pitfalls and Potential of the
Mosaic Theory of Fourth Amendment Privacy, 14 N.C. J. L. &
Tech. 381, 415 (2013) (“The mosaic theory …. recognizes that,
although a collection of dots is sometimes nothing more than
a collection of dots, some collections of dots, when assessed
holistically, are A Sunday Afternoon on the Island of La Grande
Jatte.”); Orin S. Kerr, The Mosaic Theory of the Fourth Amend-
ment, 111 Mich. L. Rev. 311, 313 (2012). For present purposes,
we ground our discussion in these high-level articulations of
the mosaic theory although we note that justices, judges, and
academics vary in how they define and (even whether they
explicitly) refer to the theory and its principles.
    Some judges and justices have relied on mosaic-like rea-
soning, but the Supreme Court has not bound lower courts to
apply the mosaic theory. The theory first emerged in Fourth
Amendment jurisprudence in United States v. Maynard,
615 F.3d 544 (D.C. Cir. 2010). The D.C. Circuit considered
whether the government’s tracking of the defendant’s car for
twenty-eight days by installing a global positioning system
(“GPS”) device onto his car without a valid warrant consti-
tuted a search under the Fourth Amendment. Id. at 555. The
court invoked the “mosaic theory,” id. at 562, to determine
that the surveillance constituted a Fourth Amendment search:
       [W]e hold the whole of a person’s movements
       over the course of a month is not actually ex-
       posed to the public because the likelihood a
       stranger would observe all those movements is
       not just remote, it is essentially nil. It is one thing
       for a passerby to observe or even to follow
       someone during a single journey as he goes to
No. 20-2352                                                   19

       the market or returns home from work. It is an-
       other thing entirely for that stranger to pick up
       the scent again the next day and the day after
       that, week in and week out, dogging his prey
       until he has identified all the places, people,
       amusements, and chores that make up that per-
       son’s hitherto private routine.
Id. at 560. The D.C. Circuit continued:
       Prolonged surveillance reveals types of infor-
       mation not revealed by short-term surveillance,
       such as what a person does repeatedly, what he
       does not do, and what he does ensemble. These
       types of information can each reveal more about
       a person than does any individual trip viewed
       in isolation. Repeated visits to a church, a gym,
       a bar, or a bookie tell a story not told by any sin-
       gle visit, as does one’s not visiting any of these
       places over the course of a month. The sequence
       of a person’s movements can reveal still more; a
       single trip to a gynecologist’s office tells little
       about a woman, but that trip followed a few
       weeks later by a visit to a baby supply store tells
       a different story. A person who knows all of an-
       other’s travels can deduce whether he is a
       weekly church goer, a heavy drinker, a regular
       at the gym, an unfaithful husband, an outpa-
       tient receiving medical treatment, an associate
       of particular individuals or political groups—
       and not just one such fact about a person, but all
       such facts.
Id. at 562 (footnote omitted).
20                                                    No. 20-2352

    Reviewing the issue of GPS monitoring under a different
name, United States v. Jones, a majority of the Supreme Court
affirmed Maynard on a narrow “property-based” theory, see
565 U.S. at 404–11, declining to rely on the mosaic theory, see
id. at 412–13. Specifically, the Jones majority held that the gov-
ernment had effected a physical trespass on private property
by attaching the device on the defendant’s vehicle without a
warrant. Id. at 404–07.
    Concurring in the judgment, however, Justice Alito—
joined by Justices Ginsburg, Breyer, and Kagan—endorsed
the mosaic theory’s logic and rejected the majority’s stringent
reliance on a trespass theory. In Justice Alito’s view, the GPS
monitoring crossed a constitutional line, wherever that line
might be:
       [R]elatively short-term monitoring of a person’s
       movements on public streets accords with ex-
       pectations of privacy that our society has recog-
       nized as reasonable. But the use of longer term
       GPS monitoring in investigations of most of-
       fenses impinges on expectations of privacy. For
       such offenses, society’s expectation has been
       that law enforcement agents and others would
       not—and indeed, in the main, simply could
       not—secretly monitor and catalogue every sin-
       gle movement of an individual’s car for a very
       long period.
Id. at 430 (Alito, J., concurring) (citation omitted). As he wrote,
“the line was surely crossed before the 4–week mark” of the
government’s tracking of “every movement that [the defend-
ant] made in the vehicle he was driving.” Id. While describing
Justice Alito’s Jones concurrence as “cryptic,” scholars have
No. 20-2352                                                    21

read his opinion to “echo[] the D.C. Circuit’s mosaic approach
in Maynard.” Kerr, The Mosaic Theory, supra, at 327.
    Writing separately, Justice Sotomayor joined the majority
but similarly asserted that finding a search was not contingent
on a “trespassory intrusion[] on property.” Jones, 565 U.S. at
414 (Sotomayor, J., concurring). For Justice Sotomayor, the
unique investigatory capabilities of GPS monitoring—includ-
ing its inexpensiveness, precision, and efficiency—posed seri-
ous concerns: “GPS monitoring generates a precise, compre-
hensive record of a person’s public movements that reflects a
wealth of detail about her familial, political, professional, re-
ligious, and sexual associations.” Id. at 415. She explained:
       I would take these attributes of GPS monitoring
       into account when considering the existence of
       a reasonable societal expectation of privacy in
       the sum of one’s public movements. I would ask
       whether people reasonably expect that their
       movements will be recorded and aggregated in
       a manner that enables the government to ascer-
       tain, more or less at will, their political and reli-
       gious beliefs, sexual habits, and so on. I do not
       regard as dispositive the fact that the govern-
       ment might obtain the fruits of GPS monitoring
       through lawful conventional surveillance tech-
       niques.
Id. at 416. As with Justice Alito’s concurring opinion, scholars
argue that “[t]his passage clearly echoes the mosaic theory.”
Kerr, The Mosaic Theory, supra, at 328.
   Drawing on the reasoning of these Jones concurrences,
some scholars have argued that Chief Justice Roberts’s
22                                                   No. 20-2352

unanimous opinion in Riley v. California, 573 U.S. 373 (2014),
further illustrates support for the mosaic theory. Riley held
that the police may not, without a warrant, search digital in-
formation on an arrestee’s seized phone. Id. at 386. “Explain-
ing why the arrestee’s wallet could be searched but his cell
phone could not, Roberts offered an argument that is much
akin to the mosaic theory: …. [‘]The sum of an individual’s
private life can be reconstructed through a thousand photo-
graphs labeled with dates, locations, and descriptions; the
same cannot be said of a photograph or two of loved ones
tucked into a wallet.[’]” See Kugler & Strahilevitz, supra, at 208
(quoting Riley, 573 U.S. at 394).
    Most recently, a five-justice majority of the Supreme Court
held in Carpenter v. United States that the government’s collec-
tion of a defendant’s cell-site location information (“CSLI”)
(the time-stamped records a mobile phone makes every time
it connects to radio antennas known as cell sites) for a period
of 127 days amounted to a search under the Fourth Amend-
ment. 138 S. Ct. at 2211–12, 2220. The Court determined that
this investigative practice violated the defendant’s reasonable
expectation of privacy because it provided “an all-encom-
passing record of the holder’s whereabouts,” uncovering “an
intimate window into a person’s life, revealing not only his
particular movements, but through them his ‘familial, politi-
cal, professional, religious, and sexual associations.’” Id. at
2217 (quoting Jones, 565 U.S. at 415 (Sotomayor, J., concur-
ring)). The Court emphasized that “[a] majority of this Court
has already recognized that individuals have a reasonable ex-
pectation of privacy in the whole of their physical move-
ments.” Id. (citing Justice Alito’s and Justice Sotomayor’s Jones
concurrences). Scholars describe the Carpenter majority as ef-
fectively “endors[ing] the mosaic theory of privacy.” Paul
No. 20-2352                                                                 23

Ohm, The Many Revolutions of Carpenter, 32 Harv. J.L. & Tech.
357, 373 (2019).
    Despite garnering passing endorsement from some—if
not most—of the justices in the various opinions in Jones, Ri-
ley, and Carpenter, the theory has not received the Court’s full
and affirmative adoption. At a minimum, the Supreme Court
has not yet required lower courts to apply it. Moreover, many
courts that have considered the theory have expressed disap-
proval,2 although not without exception.3 Additionally, the


    2 See, e.g., United States v. Howard, 426 F. Supp. 3d 1247, 1255–56 (M.D.
Ala. 2019) (declining to apply the mosaic theory, in part, because “[t]he
idea that constitutionality could hinge on the duration of a ‘search’ has
puzzled a Supreme Court justice, several circuit judges, three district
courts, two state supreme courts, and one of the nation’s leading Fourth
Amendment scholars” (footnotes omitted)), aff’d, No. 20-10877, 2021 WL
2155414 (11th Cir. May 27, 2021); State v. Muhammad, 451 P.3d 1060, 1073
(Wash. 2019) (rejecting government’s argument invoking mosaic theory
and criticizing the theory as eluding a “workable analysis” because
“[r]ather than offering analysis based on a reasonable expectation of pri-
vacy, the mosaic theory instead requires a case-by-case, ad hoc determi-
nation of whether the length of time of a cell phone ping violated the
Fourth Amendment”); Tracey v. State, 152 So. 3d 504, 520 (Fla. 2014) (re-
jecting mosaic theory and “conclud[ing] that basing the determination as
to whether warrantless real time cell site location tracking violates the
Fourth Amendment on the length of the time the cell phone is monitored
is not a workable analysis”).
    3 See, e.g., Commonwealth v. McCarthy, 142 N.E.3d 1090, 1102–03 (Mass.

2020) (“This aggregation principle or mosaic theory is wholly consistent
with the statement in Katz, 389 U.S. at 351, 88 S.Ct. 507, that ‘[w]hat a per-
son knowingly exposes to the public … is not a subject of Fourth Amend-
ment protection,’ because the whole of one’s movements, even if they are
all individually public, are not knowingly exposed in the aggregate.” (al-
terations in original)); United States v. Diggs, 385 F. Supp. 3d 648, 652 (N.D.
24                                                            No. 20-2352

mainstream academic view has urged courts to reject the the-
ory. 4 Accordingly, whether or not the theory has merit from a
theoretical or policy standpoint, Tuggle has not presented us
with binding caselaw indicating that we must apply the mo-
saic theory.
            2. Prolonged Pole Camera Surveillance in Other
               Courts
    Having noted the reluctance of some courts to adopt the
mosaic theory, we now turn to the specific issue at hand: the
constitutionality of prolonged pole camera surveillance. Like
the isolated use of pole cameras, the government’s prolonged
use of pole cameras to surveil someone’s home presents an
issue of first impression for this Court. We therefore begin by
surveying the decisions of courts that have addressed long-
term pole camera or video surveillance.


Ill. 2019) (relying on the “scope of the reasonable expectation of privacy
identified by the Jones concurrences and reaffirmed in Carpenter” to find a
search based on government’s use of GPS data), reconsideration denied, No.
18 CR 185, 2020 WL 208826 (N.D. Ill. Jan. 14, 2020); State v. Jones, 2017 SD
59, ¶ 29, 903 N.W.2d 101, 110 (“The information gathered through the use
of targeted, long-term video surveillance will necessarily include a mosaic
of intimate details of the person’s private life and associations.”).
     4See, e.g., Kerr, The Mosaic Theory, supra, at 344, 353 (detailing case
against mosaic theory in favor of a “sequential approach to Fourth
Amendment analysis” and concluding that “despite … good intentions,
the mosaic theory represents a Pandora’s Box that courts should leave
closed”); Kugler & Strahilevitz, supra, at 259–60 (illustrating, empirically,
“that very large majorities of the American public do not conceptualize
Fourth Amendment expectations of privacy in a manner that is congenial
to the ‘mosaic theory’”). But see generally Gray & Citron, supra, at 411–28
(responding to prominent criticism of, and defending, mosaic theory).
No. 20-2352                                                                 25

    Federal circuit, federal district, and state courts have splin-
tered on how to treat police use of cameras on public property
(or, with consent, on private property) to record what hap-
pens outside one’s home. That said, not all the cases we dis-
cuss specifically addressed the issue of the government using
cameras to paint a mosaic of a person’s private life, nor did all
the cases deal specifically with pole cameras.
    Our sister circuits have almost uniformly declined to find
Fourth Amendment searches in situations similar to the one
presented here. For example, in United States v. Houston,
813 F.3d 282 (6th Cir. 2016), the Sixth Circuit concluded the
government’s use of pole cameras installed on public prop-
erty and trained on the defendant’s home for ten weeks did
not constitute a Fourth Amendment search. Id. at 287–88. The
Sixth Circuit reasoned the defendant did not have a “reason-
able expectation of privacy in video footage recorded by a
camera that was located on top of a public utility pole and that
captured the same views enjoyed by passersby on public
roads.” Id. The Sixth Circuit emphasized that the agents “only
observed what [the defendant] made public to any person
traveling on the roads surrounding the farm” and that the
camera accomplished what agents “stationed … round-the-
clock” could have observed. Id. at 288. Furthermore, they ex-
plicitly rejected that the duration of surveillance altered their
analysis “because the Fourth Amendment does not punish
law enforcement for using technology to more efficiently con-
duct their investigations.” Id. 5


    5 See also United States v. Trice, 966 F.3d 506, 516 (6th Cir. 2020) (reaf-
firming Houston post-Carpenter), cert. denied, 141 S. Ct. 1395 (2021). But see
United States v. Anderson-Bagshaw, 509 F. App’x 396, 405 (6th Cir.
26                                                             No. 20-2352

    In harmony with the Sixth Circuit, the First,6 Fourth,7 and
Tenth 8 Circuits (and arguably the Ninth Circuit 9) have simi-
larly approved of governmental use of cameras, but we again


2012) (“[W]e confess some misgivings about a rule that would allow the
government to conduct long-term video surveillance of a person’s back-
yard without a warrant. Few people, it seems, would expect that the gov-
ernment can constantly film their backyard for over three weeks using a
secret camera that can pan and zoom and stream a live image to govern-
ment agents.”).
     6See, e.g., United States v. Bucci, 582 F.3d 108, 116–17 (1st Cir. 2009)
(holding defendant did not establish “a reasonable objective expectation
of privacy” that was invaded by eight-month long video surveillance of
his home from a utility pole). But see United States v. Moore-Bush, 982 F.3d
50, 50 (1st Cir. 2020) (mem.) (scheduling en banc hearing for March 23,
2021, to review panel decision affirming Bucci on stare decisis grounds).
     7The Fourth Circuit held that the government’s use of “a hidden,
fixed-range, motion-activated video camera placed in the [defendant’s]
open fields” did not violate the Fourth Amendment. Vankesteren, 553 F.3d
at 287, 288–91. This decision, however, did not turn on how long the gov-
ernment used the camera.
     8The Tenth Circuit held that “evidence obtained from the video cam-
eras installed on the telephone poles and the recordings made in the un-
dercover FBI car were not introduced in violation of … the Fourth Amend-
ment.” Jackson, 213 F.3d at 1282; see also United States v. Cantu, 684 F. App’x
703, 703 (10th Cir. 2017) (unpublished) (reaffirming Jackson’s holding that
warrantless video surveillance did not constitute search). Like the Fourth
Circuit in Vankesteren, however, neither Jackson nor Cantu centered on the
mosaic or a like theory.
     9In holding that footage obtained from surveillance camera installed
without warrant in a common area of hospital did not constitute Fourth
Amendment search, the Ninth Circuit reasoned “the defendant had no ob-
jectively reasonable expectation of privacy that would preclude video sur-
veillance of activities already visible to the public.” See United States v.
Gonzalez, 328 F.3d 543, 548 (9th Cir. 2003).
No. 20-2352                                                               27

note these cases did not squarely address the same factual and
legal circumstances presented here.
    Furthermore, the only circuit to require the government to
seek a court order authorizing video surveillance is the Fifth
Circuit, which, decades before Jones and Carpenter, found the
government’s use of a pole camera for more than thirty days
to record the exterior of defendant’s home “qualif[ied] as a
search under the [F]ourth [A]mendment ….” See Cuevas-
Sanchez, 821 F.2d at 251. Significantly, however, the govern-
ment positioned the camera in that case to look over a ten-
foot-tall fence and capture images unviewable to passersby.
See id. Thus, for now, no federal circuit court has found a
Fourth Amendment search based on long-term use of pole
cameras on public property to view plainly visible areas of a
person’s home. To part ways with our sister circuits that have
spoken to pole cameras, then, would likely create a circuit
split, which “generally requires quite solid justification; we
do not lightly conclude that our sister circuits are wrong.” An-
drews v. Chevy Chase Bank, 545 F.3d 570, 576 (7th Cir. 2008).
    Federal district courts are mixed on whether pole cam-
era surveillance constitutes a search. Following the trend lines
of the federal circuit courts, district courts in the Seventh Cir-
cuit have found no Fourth Amendment searches when
law enforcement officers made extended use of pole cam-
eras. 10 Some federal district courts outside the Seventh Circuit


    10  See, e.g., United States v. Kubasiak, No. 18-CR-120, 2018 WL 4846761,
at *3, *7 (E.D. Wis. Oct. 5, 2018) (finding monthslong use of a camera in-
stalled on defendant’s neighbor’s property was not a Fourth Amendment
search because footage revealed “only what the neighbor, or a police of-
ficer standing in the neighbor’s house, could have seen”); United States v.
28                                                            No. 20-2352




Kay, No. 17-CR-16, 2018 WL 3995902, at *1, *3 (E.D. Wis. Aug. 21, 2018)
(concluding eighty-seven days of pole camera surveillance “[did] not con-
stitute a Fourth Amendment search” and noting “nearly every federal
court which has addressed the issue has held that pole camera surveil-
lance of a person’s driveway or the exterior of his residence does not vio-
late the person’s reasonable expectation of privacy”); United States v.
Tirado, No. 16-CR-168, 2018 WL 1806056, at *3–4 (E.D. Wis. Apr. 16, 2018)
(finding three-month use of pole camera was not a search because, prior
to Carpenter, “the Seventh Circuit ha[d] not so held [that to be unconstitu-
tional], and the other circuit courts of appeal ha[d] rejected such claims”);
see also generally United States v. Harris, No. 17-CR-175, 2021 WL 268322
(E.D. Wis. Jan. 27, 2021) (finding warrantless video surveillance cameras
in and outside of defendant’s apartment complex did not amount to
Fourth Amendment search because “[u]nlike [the CSLI in Carpenter], the
video surveillance did not track the totality of the defendant’s move-
ments” (citation omitted)).
No. 20-2352                                                                 29

agree that use of pole cameras does not constitute a search.11
Nevertheless, that view is not unanimous. 12



    11  See, e.g., United States v. Flores, No. 19-CR-364, 2021 WL 1312583, at
*8 (N.D. Ga. Apr. 8, 2021) (finding no Fourth Amendment search from
pole camera footage because “[t]he images of a single, fixed location cap-
tured by the pole camera in this case d[id] not equate with the activities
revealed by cell-site location information considered by the Court in Car-
penter”); United States v. Edmonds, 438 F. Supp. 3d 689, 694 (S.D. W. Va.
2020) (“declin[ing] to adopt the Defendant’s proposed blanket rule that a
warrant is required for use of a pole camera placed in a public location
with a view available to the public”); United States v. Mazzara, No. 16 CR.
576, 2017 WL 4862793, at *10–12 (S.D.N.Y. Oct. 27, 2017) (finding that
twenty-one-month “video surveillance at issue … did not violate any ex-
pectation of privacy that modern society is prepared to recognize as rea-
sonable under Katz and its progeny”); United States v. Pratt, No. 16-CR-
20677-06, 2017 WL 2403570, at *4 (E.D. Mich. June 2, 2017) (“Continuous
camera surveillance of private property does raise privacy concerns and
is evocative of an ‘Orwellian state.’ But there are mitigating factors and
controlling precedent which justify denial of the motion to suppress here.”
(citation omitted)); United States v. Gilliam, No. 12-CR-93, 2015 WL
5178197, at *9 (W.D. Pa. Sept. 4, 2015) (finding no “objectively reasonable
expectation of privacy when the images captured by the pole camera were
visible to any person who was located in the public street looking at his
home”); United States v. Brooks, 911 F. Supp. 2d 836, 843 (D. Ariz. 2012)
(“[L]aw enforcement’s use of the pole camera did not violate the Fourth
Amendment ….”).
    12 See, e.g., United States v. Houston, 965 F. Supp. 2d 855, 898 (E.D. Tenn.

2013) (finding that “warrantless video surveillance of the curtilage of [the
Defendant’s home], beyond fourteen (14) days violated the Defendant’s
reasonable expectation of privacy”); United States v. Vargas, 2014 U.S. Dist.
LEXIS 184672, *27 (E.D. Wash. Dec. 15, 2014) (“[L]aw enforcement’s video
surveillance of [the defendant’s] front yard for six weeks with a camera
that could zoom and record violated his reasonable expectation of privacy:
an expectation that society is prepared to recognize as reasonable.”).
30                                                               No. 20-2352

   State courts likewise disagree whether pole camera use
constitutes a search. Some state courts have joined the chorus
determining that pole camera use does not qualify as a Fourth
Amendment search. 13 However, other state supreme and ap-
pellate courts have found the use of pole cameras for varying
durations violates the Fourth Amendment. 14 Mirroring this
array of opinions, scholars and students have puzzled over
how the law ought to treat pole camera surveillance. 15


     13 See, e.g., State v. Duvernay, 2017-Ohio-4219, 92
                                                       N.E.3d 262, 269–70, at
¶ 25 (3d Dist.) (affirming an Ohio “trial court’s determination that law en-
forcement’s use of the pole camera [for nine days] did not violate [the de-
fendant’s] Fourth Amendment right to privacy”).
     14 See, e.g., State v. Jones, 903 N.W.2d at 111–13 (holding that govern-
ment had executed a search through “the warrantless use of a pole camera
to surveil a suspect’s activities outside his residence for two months”); Peo-
ple v. Tafoya, 2019 COA 176, ¶¶ 2, 33–52, No. 17CA1243, 2019 WL 6333762,
at *1, *6–10 (holding that “the continuous, three-month-long use of the
pole camera constituted a search under the Fourth Amendment”), cert.
granted, No. 20SC9, 2020 WL 4343762 (Colo. June 27, 2020); cf. Common-
wealth v. Mora, 150 N.E.3d 297, 302 (Mass. 2020) (concluding that “contin-
uous, long-term pole camera surveillance targeted at the residences of [the
defendants] well may have been a search within the meaning of the Fourth
Amendment, a question we do not reach, but certainly was a search under
art. 14” of the Massachusetts Declaration of Rights); Commonwealth v.
Comenzo, No. 1482CR01050, 2021 WL 616548, at *8 (Mass. Super. Jan. 11,
2021) (“[T]he seventeen-day video surveillance in this case would have
required a warrant under Mora.”).
     15 See, e.g., Taylor H. Wilson, Jr., Note, The Mosaic Theory's Two Steps:
Surveying Carpenter in the Lower Courts, 99 Tex. L. Rev. Online 155, 173–75
(2021) (discussing the “close case” pole camera surveillance presents un-
der the mosaic theory); Aparna Bhattacharya, Note, The Impact of Carpen-
ter v. United States on Digital Age Technologies, 29 S. Cal. Interdisc. L.J. 489,
501–07 (2020) (discussing and applying Carpenter to pole camera
No. 20-2352                                                                   31

             3. The Pole Camera Surveillance Here Was Not a
                Search Under the Mosaic Theory
   Having outlined the theoretical and jurisprudential un-
derpinnings of the mosaic theory and various courts’ treat-
ment of pole camera footage, we now turn to Tuggle’s case.
The thrust of Tuggle’s argument—rooted in the mosaic the-
ory—is that the government’s use of the three pole cameras
unconstitutionally “captured the whole of Mr. Tuggle’s
movements.” See Carpenter, 138 S. Ct. at 2217 (“[I]ndividuals
have a reasonable expectation of privacy in the whole of their
physical movements.”). Even if we accepted the mosaic the-
ory, however—and we do not go that far—current Supreme
Court precedent does not support Tuggle’s argument.
   Of course, the stationary cameras placed around Tuggle’s
house captured an important sliver of Tuggle’s life, but they
did not paint the type of exhaustive picture of his every move-
ment that the Supreme Court has frowned upon. If the facts
and concurrences of Jones and Carpenter set the benchmarks,
then the surveillance in this case pales in comparison.


surveillance); Matthew Tokson, The Next Wave of Fourth Amendment Chal-
lenges After Carpenter, 59 Washburn L.J. 1, 17–19 (2020) (predicting the Su-
preme Court will “rule that [pole camera] surveillance violates the Fourth
Amendment”); Taylor Cutteridge, Comment, Now You See Me: An Exami-
nation of the Legality of Police Use of Utility Pole Surveillance Cameras, 48 Cap.
U. L. Rev. 75, 102 (2020) (concluding that the Supreme Court should hold
pole camera surveillance does “not constitute a search under the Fourth
Amendment”); Tiffany M. Russo, Comment, Searches and Seizures As Ap-
plied to Changing Digital Technologies: A Look at Pole Camera Surveillance,
12 Seton Hall Cir. Rev. 114, 115–18 (2015) (arguing that courts should
broadly apply Ciraolo’s holding—that the defendant did not have an ob-
jectively reasonable expectation of privacy when his marijuana crop was
visible to the naked eye—to video surveillance).
32                                                   No. 20-2352

    In those cases, the justices expressed concerns about sur-
veillance leading to “a precise, comprehensive record of a per-
son’s public movements that reflects a wealth of detail about
her familial, political, professional, religious, and sexual asso-
ciations.” See Jones, 565 U.S. at 415 (Sotomayor, J., concurring)
(emphasis added); Carpenter, 138 S. Ct. at 2217 (same). Follow-
ing this reasoning, many justices saw the GPS and CSLI tech-
nologies in Jones and Carpenter as capable of capturing the
whole of the defendants’ movements, therefore implicating
the Fourth Amendment. The CSLI at issue in Carpenter even
tracked the defendant’s movement through not only public
areas, but also private places, which the Court likened to “at-
tach[ing] an ankle monitor to the phone’s user.” 138 S. Ct. at
2218.
    Unlike those technologies, the cameras here exposed no
details about where Tuggle traveled, what businesses he fre-
quented, with whom he interacted in public, or whose homes
he visited, among many other intimate details of his life. If
anything, far from capturing the “whole of his physical move-
ments,” id. at 2219, or his “public movements,” Jones, 565 U.S.
at 415 (Sotomayor, J., concurring), the cameras only high-
lighted Tuggle’s lack of movement, surveying only the time
he spent at home and thus not illuminating what occurred
when he moved from his home.
   Beyond the justices’ “cryptic” embrace of the mosaic the-
ory, Kerr, The Mosaic Theory, supra, at 326, the theory, in its
inception, drew a distinction between the “passerby … ob-
serv[ing] or even … follow[ing] someone during a single jour-
ney as he goes to the market or returns home from work” and
the far more problematic “stranger [who] pick[s] up the scent
again the next day and the day after that, week in and week
No. 20-2352                                                    33

out, dogging his prey until he has identified all the places,
people, amusements, and chores that make up that person’s
hitherto private routine.” Maynard, 615 F.3d at 560. The pole
cameras in this case likely lie somewhere between these ex-
tremes but more closely resemble the former. In one sense, the
recordings painted a whole picture of the happenings outside
Tuggle’s front door by recording nonstop for eighteen
months. See, e.g., State v. Jones, 903 N.W.2d at 111 (“[O]fficers
[were] able to ‘capture[] something not actually exposed to
public view—the aggregate of all of [the defendant’s] coming
and going from the home, all of his visitors, all of his cars, all
of their cars, and all of the types of packages or bags he carried
and when.’” (some alterations in original) (quoting United
States v. Garcia-Gonzalez, No. 14-10296, 2015 WL 5145537, at *5
(D. Mass. Sept. 1, 2015))). In another important sense, how-
ever, the footage only depicted one small part of a much
larger whole: Tuggle’s life or the “whole of his physical move-
ments.” Carpenter, 138 S. Ct. at 2219. Given their immobile na-
ture, the cameras could not make out an exhaustive record of
Tuggle’s “hitherto private routine,” Maynard, 615 F.3d at 560,
because much if not most of the relevant details occurred out-
side of the immediate area in front of Tuggle’s home.
    The prospective and nonhistorical use of the pole cameras
here further distinguishes them from the technologies in cases
where the Supreme Court relied on mosaic-styled arguments,
which had retrospective capabilities. In Riley v. California, the
Court determined that the government had unlawfully
searched the defendant’s phone based in part on the widening
“gulf between physical practicability and digital capacity” of
phones. 573 U.S. at 394. The court noted the immense amount
of information and data that phones contain, including “pho-
tographs, picture messages, text messages, Internet browsing
34                                                 No. 20-2352

history, a calendar, a thousand-entry phone book, and so on.”
Id. As for Internet browsing, the court said it could “reveal an
individual’s private interests or concerns.” Id. at 395. Fore-
shadowing the main issue in Carpenter, the Court commented
that “[h]istoric location information is a standard feature on
many smart phones and can reconstruct someone’s specific
movements down to the minute, not only around town but
also within a particular building,” essentially allowing the
government to go back in time. Id. at 396.
    The Supreme Court brought this idea to the fore in Carpen-
ter when it highlighted CSLI’s “retrospective quality” that
“gives police access to a category of information otherwise
unknowable.” 138 S. Ct. at 2218. The advent of CSLI-like tech-
nology therefore allows the government to “travel back in
time to retrace a person’s whereabouts,” obviating what
would have been previous “attempts to reconstruct a person’s
movements [that] were limited by a dearth of records and the
frailties of recollection.” Id. at 2218. We recently suggested
that Carpenter should be read narrowly to proscribe only the
collection of historical CSLI but not real-time CSLI. See United
States v. Hammond, 996 F.3d 374, 383 (7th Cir. 2021) (conclud-
ing that government only searched defendant when it col-
lected “historical CSLI,” but otherwise finding no search in
government’s collection of defendant’s “real-time CSLI”).
   By the logic of Riley and Carpenter, and our recent obser-
vations in Hammond, the pole camera surveillance here did
not run afoul of the Fourth Amendment because the govern-
ment could not “travel back in time to retrace [Tuggle’s]
whereabouts,” Carpenter, 138 S. Ct. at 2218, to say nothing of
the thorny questions presented by a pre-existing network of
No. 20-2352                                                            35

government cameras. 16 The government had to decide ex ante
to collect the video footage by installing the cameras. The gov-
ernment did not tap into an expansive, pre-existing database
of video footage of Tuggle’s home akin to the Internet brows-
ing history and extensive photos stored on cell phones con-
sidered in Riley, or the expansive CSLI in Carpenter. Until the
Supreme Court or Congress instructs otherwise, we will read
Carpenter as limited to the unique features of the historical
CSLI at issue there, as distinct from the real-time video foot-
age here. See Hammond, 996 F.3d at 387 (“The ‘narrow’ Carpen-
ter decision did not determine whether the collection of real-
time CSLI constitutes a Fourth Amendment search.”). The
majority opinion in Carpenter itself offers support for this in-
terpretation, as it stated that the Court was not “call[ing] into
question conventional surveillance techniques and tools, such
as security cameras.” 138 S. Ct. at 2220 (emphasis added).
Whether pole cameras are the same as security cameras is ir-
relevant because the cameras here would clearly qualify as a
“conventional surveillance technique[].”See id.
    We emphasize, however, that our decision in Tuggle’s
case does not rest on the premise that the government could
have—in theory—obtained the same surveillance by station-
ing an agent atop the utility poles outside Tuggle’s home, thus
rendering the decision to instead use pole cameras constitu-
tional. See Houston, 813 F.3d at 289 (“[I]t is only the possibility


    16 See, e.g., Rebecca Lipman, Protecting Privacy with Fourth Amendment
Use Restrictions, 25 Geo. Mason L. Rev. 412, 436–37 (2018) (“Cameras have
existed for a long time; networks of cameras blanketing an entire metro
area that are equipped with facial recognition technology have not. Such
a network could allow law enforcement to search for any individual, any-
where in a city, going back for weeks or months ….” (footnotes omitted)).
36                                                  No. 20-2352

that a member of the public may observe activity from a pub-
lic vantage point—not the actual practicability of law enforce-
ment’s doing so without technology—that is relevant for
Fourth Amendment purposes.”). This fiction contravenes the
Fourth Amendment and Katz’s command to assess reasona-
bleness. To assume that the government would, or even
could, allocate thousands of hours of labor and thousands of
dollars to station agents atop three telephone poles to con-
stantly monitor Tuggle’s home for eighteen months defies the
reasonable limits of human nature and finite resources. In our
view, the premise that the government could realistically ac-
complish the pole camera surveillance here for more than a
few days is a fiction that courts should not rely on to limit the
Fourth Amendment’s protections. See Jones, 565 U.S. at 416
(Sotomayor, J., concurring) (“I do not regard as dispositive the
fact that the government might obtain the fruits of GPS mon-
itoring through lawful conventional surveillance tech-
niques.”). We thus close the door on the notion that surveil-
lance accomplished through technological means is constitu-
tional simply because the government could theoretically ac-
complish the same surveillance—no matter how laborious—
through some nontechnological means.
    Although we now hold that the pole camera surveillance
of the exterior of Tuggle’s home did not constitute a Fourth
Amendment search, we are not without unease about the im-
plications of that surveillance for future cases. The eighteen-
month duration of the government’s pole camera surveil-
lance—roughly four and twenty times the duration of the
data collection in Carpenter and Jones, respectively—is con-
cerning, even if permissible.
No. 20-2352                                                  37

    That concern presents us with an obvious line-drawing
problem: How much pole camera surveillance is too much?
Most might agree that eighteen months (roughly 554 days) is
questionable, but what about 250 days? 100 days? 20 days? 1
day? See also Kerr, The Mosaic Theory, supra, at 329–43 (detail-
ing the “remarkable set of novel and difficult questions”
posed by the mosaic theory). Despite the inherent problems
with drawing an arbitrary line, the status quo in which the
government may freely observe citizens outside their homes
for eighteen months challenges the Fourth Amendment’s
stated purpose of preserving people’s right to “be secure in
their persons, houses, papers, and effects.” Drawing our own
line, however, risks violating Supreme Court precedent and
interfering with Congress’s policy-making function, which
would exceed our mandate to apply the law. United States v.
Cuevas-Perez, 640 F.3d 272, 276, 285 (7th Cir. 2011) (Flaum, J.,
concurring) (“The matter is, as they say, above our pay
grade.”), judgment vacated, 565 U.S. 1189 (2012).
    Beyond the line-drawing issues, we conclude by sounding
a note of caution regarding the current trajectory of Fourth
Amendment jurisprudence. As technological capabilities ad-
vance, our confidence that the Fourth Amendment (as cur-
rently understood by the courts) will adequately protect indi-
vidual privacy from government intrusion diminishes. Kyllo,
533 U.S. at 33–34 (“It would be foolish to contend that the de-
gree of privacy secured to citizens by the Fourth Amendment
has been entirely unaffected by the advance of technology.”).
Current Fourth Amendment jurisprudence admits of a pre-
carious circularity: Cutting-edge technologies will eventually
and inevitably permeate society. In turn, society’s expecta-
tions of privacy will change as citizens increasingly rely on
and expect these new technologies. Once a technology is
38                                                 No. 20-2352

widespread, the Constitution may no longer serve as a back-
stop preventing the government from using that technology
to access massive troves of previously inaccessible private in-
formation because doing so will no longer breach society’s
newly minted expectations. With the advent of digital, cloud-
based, and smart capabilities, these new technologies will sel-
dom contravene the traditional limitations imposed by the
Fourth Amendment on physical invasions. Jones, 565 U.S. at
404–11.
    Cameras are a perfect example of the circularity. In 1791,
no one would expect—because the technology did not exist—
that the government could capture a still (or moving) image
of a citizen at a given time or place. Even once invented and
introduced to society, few would have expected that the gov-
ernment would use then-unwieldy and expensive cameras to
aid in fast-moving law enforcement investigations. Eventu-
ally, cameras grew so sophisticated, discrete, portable, and in-
expensive that they pervaded society. By that point, the gov-
ernment’s use of cameras was entirely unsurprising, even
though the Framers might have balked at such a prospect
when they penned the Fourth Amendment. See David Alan
Sklansky, Too Much Information: How Not to Think About Pri-
vacy and the Fourth Amendment, 102 Cal. L. Rev. 1069, 1085
(2014) (“Cameras mounted in public and semi-public
places … are increasingly unremarkable, their presence taken
for granted.”). In other words, once society sparks the prome-
thean fire—shifting its expectations in response to technolog-
ical developments—the government receives license under
current Fourth Amendment jurisprudence to act with greater
constitutional impunity.
No. 20-2352                                                                39

    Barring a transformation in governing law, we expect this
chronicle of cameras to repeat itself again and again with the
evolution of far more invasive technologies. Today’s pole
cameras will be tomorrow’s body cameras, 17 “protracted lo-
cation tracking using [automatic license plate readers],”18
drones, 19 facial recognition, 20 Internet-of-Things and smart
devices, 21 and so much more that we cannot even begin to

    17 See Erik Nielsen, Comment, Fourth Amendment Implications of Police-

Worn Body Cameras, 48 St. Mary’s L.J. 115, 120 (2016) (“[T]he increased use
of widespread video recording, although intended to prevent misconduct
of police officers, creates concerns over the Fourth Amendment rights of
individuals to be free from unreasonable searches.”).
    18 See Samuel D. Hodge, Jr., Big Brother Is Watching: Law Enforcement’s
Use of Digital Technology in the Twenty-First Century, 89 U. Cin. L. Rev. 30,
40 (2020) (“[L]icense plate reader databases provide the opportunity for
institutionalized abuse by allowing anyone who has access to the infor-
mation to snoop into an individual’s daily activities, habits, or present and
past relationships.”).
    19 See Jennifer M. Bentley, Note, Policing the Police: Balancing the Right
to Privacy Against the Beneficial Use of Drone Technology, 70 Hastings L.J.
249, 251 (2018) (“[D]rones are … potent tools that can be used to invade
privacy and conduct highly intrusive surveillance.”).
    20See Andrew Guthrie Ferguson, Facial Recognition and the Fourth
Amendment, 105 Minn. L. Rev. 1105, 1108 (2021) (asserting that “the Fourth
Amendment will not save us from the privacy threat created by facial
recognition surveillance”).
    21 See Eunice Park, Objects, Places and Cyber-Spaces Post-Carpenter: Ex-
tending the Third-Party Doctrine Beyond CSLI: A Consideration of IoT and
DNA, 21 Yale J.L. & Tech. 1, 58 (2019) (arguing that “clarity [in Fourth
Amendment jurisprudence] is needed for the vast array of unregulated
technologies growing in popularity, and for those yet to emerge”); An-
drew Guthrie Ferguson, The “Smart” Fourth Amendment, 102 Cornell L.
Rev. 547, 631 (2017) (“In a world that needs both smart devices and the
40                                                            No. 20-2352

envision. New technologies of this sort will not disappear, nor
will the complicated Fourth Amendment problems that ac-
company them. If anything, we should expect technology to
continue to grow exponentially. And if current technologies
are any indication, that technological growth will predictably
have an inverse and inimical relationship with individual pri-
vacy from government intrusion, presenting serious concerns
for Fourth Amendment protections.
    Assuming as much, it might soon be time to revisit the
Fourth Amendment test established in Katz. See Cuevas-Perez,
640 F.3d at 276 (Flaum, J., concurring) (“If the doctrine needs
clarifying, tweaking, or an overhaul in light of technologies
employed by law enforcement, that additional guidance
should come from the Supreme Court.”). Indeed, almost four
decades ago, when considering a respondent’s argument that
“twenty-four hour surveillance of any citizen of this country
will be possible, without judicial knowledge or supervision,”
the Court reserved judgement because, “if such dragnet type
law enforcement practices as respondent envisions should
eventually occur, there will be time enough then to determine
whether different constitutional principles may be applica-
ble.” Knotts, 460 U.S. at 283–84. As this case illustrates, round-
the-clock surveillance for eighteen months is now unextraor-
dinary.
    This could also be an apt area for Congress to legislate be-
cause, as some have noted, “Congress has significant institu-
tional advantages over the courts in trying to regulate privacy

Fourth Amendment, there … needs to be a new theory to protect the data
trails we leave behind. Without such a theory, data trails will exist outside
of Fourth Amendment protection, and an intrusive sensor surveillance
system will be created without any constitutional restraints.”).
No. 20-2352                                                     41

in new technologies.” Kerr, The Mosaic Theory, supra, at 350;
see also Kyllo, 533 U.S. at 51 (Stevens, J., dissenting) (“It would
be far wiser to give legislators an unimpeded opportunity to
grapple with these emerging issues rather than to shackle
them with prematurely devised constitutional constraints.”);
Carpenter, 138 S. Ct. at 2246 (Thomas, J., dissenting) (“With no
sense of irony, the Court invalidates this [statutory] regime
today—the one that society actually created in the form of its
elected representatives in Congress.” (internal quotation
marks and citation omitted)); Cuevas-Perez, 640 F.3d at 286
(Flaum, J., concurring) (“[T]he unsettled, evolving expecta-
tions in this realm, combined with the fast pace of technolog-
ical change, may make the legislature the branch of govern-
ment that is best suited, and best situated, to act.”).
   For now, though, we will continue to faithfully apply our
current understanding of the Constitution and the Supreme
Court’s precedent. With respect to the pole cameras in this
case, that understanding requires that we find no search in
violation of the Fourth Amendment. The district court there-
fore did not err in denying Tuggle’s motion to suppress. As
such, we have no need to consider the government’s fallback
argument that, even if there were a Fourth Amendment
search, the good faith exception to the exclusionary rule
would apply.

                     III.   Conclusion

   For these reasons, we AFFIRM the district court’s denial of
Tuggle’s motion to suppress.

```

---

## GROUP: content/cases/United States v. Wilson.md  (`case`, 6 assertions)

### content_page

```
---
title: United States v. Wilson
type: case
citation: "13 F.4th 961 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir.
court_level: coa
circuit: ca9
year: 2021
date_decided: 2021-09-21
docket: 18-50440
authority_weight: "Binding in-circuit — 9th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/5296785/united-states-v-luke-wilson/"
  cluster_id: 5296785
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Wilson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — hash-match split (9th Cir.)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Fourth Amendment Framework]]"
  - "[[Two Definitions of Search]]"
  - "[[United States v. Jacobsen]]"
  - "[[United States v. Reddick]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - private-search-doctrine
  - hash-value
  - child-pornography
  - digital-privacy
  - ninth-circuit
holding: "Under the private-search doctrine of Walter and Jacobsen, the government may repeat a private party's search without a warrant only insofar as it does not exceed the scope of that private search; where Google's automated system flagged four email attachments as matching known child-pornography hashes but no person had actually viewed those images, a government agent's warrantless opening and viewing of them exceeded the antecedent private search — learning new information and expanding the intrusion — so it was not justified by the private-search exception, and Wilson's conviction was reversed."
aliases:
  - United States v. Wilson
  - "United States v. Wilson (9th Cir. 2021)"
---

# United States v. Wilson

*13 F.4th 961 (9th Cir. 2021)* (No. 18-50440) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 5296785 → lead opinion 5125347 (13 F.4th 961, decided 2021-09-21); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Google's automated systems detected that four email attachments in Luke Wilson's account matched the hash values of images previously identified as child pornography, and Google reported them to the National Center for Missing and Exploited Children, which forwarded the report to a law-enforcement task force. Critically, no Google employee — or any other person — had actually opened and viewed those particular four images; the match was generated by algorithm alone. A government agent then opened and viewed the four attachments without a warrant, described them in detail, and used them to obtain warrants to search Wilson's email account and home. The district court denied suppression, reasoning the agent's viewing did not exceed Google's private search.

## Issue
Whether a government agent's warrantless opening and viewing of email attachments — flagged by a private company's automated hash-matching but never actually viewed by any person — was justified by the private-search exception to the Fourth Amendment.

## Rule
The private-search doctrine excuses a warrant only when the government's search does not exceed the scope of an antecedent private search; the government may not learn new, critical information or intrude on privacy interests beyond what the private party already exposed. Measuring the agent's conduct against Google's algorithmic match, the panel held: "we hold that it was not. We therefore reverse the district court's denial of Wilson's motion to suppress and vacate Wilson's conviction." — 13 F.4th 961, slip op. at 6. ^pin-op6

## Application
The court concluded the agent's warrantless viewing exceeded Google's antecedent private search in two ways. First, it produced new, critical information: because no person had ever viewed the four images, opening them told the government something Google's hash-matching had not — the actual visual content — which the agent then used to secure warrants and prosecute. Second, it expanded the intrusion on Wilson's privacy: the agent's human viewing of the images went beyond the algorithm's limited, non-visual comparison, and on the record the government had not shown the flagged files were exact duplicates of images a person had previously seen. Because the government thereby went beyond the frustrated portion of Wilson's expectation of privacy, the private-search exception did not apply and the warrantless viewing violated the Fourth Amendment.

## Conclusion
The Ninth Circuit **reversed** the denial of suppression and **[[Reading and Citing Cases#vacated|vacated]]** Wilson's conviction, holding the warrantless viewing exceeded the private search.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Wilson* is the Ninth Circuit's counterweight on the digital **private-search** frontier: applying *[[United States v. Jacobsen|Jacobsen]]*'s exceed-the-scope test, it holds that an **algorithmic hash-match no human has viewed** does not let the government open the file without a warrant. That squarely diverges from the Fifth Circuit's *[[United States v. Reddick|Reddick]]* (and the Sixth Circuit's *[[United States v. Miller|Miller]]*), which treat the confirmatory viewing as within the private search — an unresolved split worth teaching alongside *[[Carpenter v. United States|Carpenter]]*'s caution about extending old doctrines to new technology.

## Appears on
- [[Private and Foreign Searches]] — *Key — hash-match split (9th Cir.)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- [*United States v. Wilson*, 13 F.4th 961 (9th Cir. 2021)](https://www.courtlistener.com/opinion/5296785/united-states-v-luke-wilson/) — pinpoint: slip op. at 6 (government's warrantless viewing exceeded the antecedent private search; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "430f9b0b42b05049", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "13 F.4th 961 (2021)", "court": "9th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Wilson", "year": "2021"}}
{"assertion_id": "5ba29d2ad9376c04", "dimension": "support", "kind": "home_role", "locator": {"home": "Private and Foreign Searches"}, "payload": {"home": "Private and Foreign Searches", "role": "Key — hash-match split (9th Cir.)", "title": "United States v. Wilson"}}
{"assertion_id": "7ab1d0d9b9d5e197", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "United States v. Wilson"}}
{"assertion_id": "f2d538e70d30f6e0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under the private-search doctrine of Walter and Jacobsen, the government may repeat a private party's search without a warrant only insofar as it does not exceed the scope of that private search; where Google's automated system flagged four email attachments as matching known child-pornography hashes but no person had actually viewed those images, a government agent's warrantless opening and viewing of them exceeded the antecedent private search — learning new information and expanding the intrusion — so it was not justified by the private-search exception, and Wilson's conviction was reversed.", "title": "United States v. Wilson"}}
{"assertion_id": "476671f0cba6fc18", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Wilson", "varies_by_point": "false"}}
{"assertion_id": "5a7cc66f804e96bf", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Wilson"}}
```

### lake record — United States v. Wilson

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Wilson",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Luke Wilson",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Wilson",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2021-09-21",
    "year": 2021,
    "docket": "18-50440",
    "cluster_id": 5296785,
    "lead_opinion_id": 5125347,
    "sibling_ids": [],
    "absolute_url": "/opinion/5296785/united-states-v-luke-wilson/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "13 F.4th 961",
      "volume": "13",
      "reporter": "F.4th",
      "page": "961",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "13 F.4th 961",
        "volume": "13",
        "reporter": "F.4th",
        "page": "961",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "13 F.4th 961",
    "official_selection": {
      "court_class": "coa",
      "selected": "13 F.4th 961",
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
    "date_created": "2026-07-07T18:19:50Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-wilson--5296785",
      "to_record_id": "United States v. Wilson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Wilson

```
                       FOR PUBLICATION

   UNITED STATES COURT OF APPEALS
        FOR THE NINTH CIRCUIT


 UNITED STATES OF AMERICA,                     No. 18-50440
           Plaintiff-Appellee,
                                                 D.C. No.
                  v.                       3:15-cr-02838-GPC-1

 LUKE NOEL WILSON,
        Defendant-Appellant.                      OPINION

        Appeal from the United States District Court
          for the Southern District of California
        Gonzalo P. Curiel, District Judge, Presiding

         Argued and Submitted November 15, 2019
                   Pasadena, California

                    Filed September 21, 2021

   Before: Marsha S. Berzon and Paul J. Watford, Circuit
      Judges, and Robert H. Whaley, * District Judge.

                    Opinion by Judge Berzon




     *
       The Honorable Robert H. Whaley, United States District Judge for
the Eastern District of Washington, sitting by designation.
2                  UNITED STATES V. WILSON

                          SUMMARY **


                          Criminal Law

    The panel vacated a conviction for possession and
distribution of child pornography, reversed the district
court’s denial of a motion to suppress, and remanded for
further proceedings in a case in which the panel addressed
whether the government’s warrantless search of the
defendant’s email attachments was justified by the private
search exception to the Fourth Amendment.

    As required by federal law, Google reported to the
National Center for Missing and Exploited Children
(NCMEC) that the defendant had uploaded four images of
apparent child pornography to his email account as email
attachments. No one at Google had opened or viewed the
defendant’s email attachments; its report was based on an
automated assessment that the images the defendant
uploaded were the same as images other Google employees
had earlier viewed and classified as child pornography.
Someone at NCMEC then, also without opening or viewing
them, sent the defendant’s email attachments to the San
Diego Internet Crimes Against Children Task Force, where
an officer ultimately viewed the email attachments without
a warrant. The officer then applied for warrants to search
both the defendant’s email account and his home, describing
the attachments in detail in the application.




    **
       This summary constitutes no part of the opinion of the court. It
has been prepared by court staff for the convenience of the reader.
                 UNITED STATES V. WILSON                       3

    The private search doctrine concerns circumstances in
which a private party’s intrusions would have constituted a
search had the government conducted it and the material
discovered by the private party then comes into the
government’s possession. Invoking the precept that when
private parties provide evidence to the government on their
own accord, it is not incumbent on the police to avert their
eyes, the Supreme Court formalized the private search
doctrine in Walter v. United States, 447 U.S. 649 (1980),
which produced no majority decision, and United States v.
Jacobson, 466 U.S. 109 (1984), which did.

    The panel held that the government did not meet its
burden to prove that the officer’s warrantless search was
justified by the private search exception to the Fourth
Amendment’s warrant requirement. The panel wrote that
both as to the information the government obtained and the
additional privacy interests implicated, the government’s
actions here exceed the limits of the private search exception
as delineated in Walter and Jacobsen and their progeny.
First, the government search exceeded the scope of the
antecedent private search because it allowed the government
to learn new, critical information that it used first to obtain a
warrant and then to prosecute the defendant. Second, the
government search also expanded the scope of the
antecedent private search because the government agent
viewed the defendant’s email attachments even though no
Google employee—or other person—had done so, thereby
exceeding any earlier privacy intrusion. Moreover, on the
limited evidentiary record, the government has not
established that what a Google employee previously viewed
were exact duplicates of the defendant’s images. And, even
if they were duplicates, such viewing of others’ digital
communications would not have violated the defendant’s
expectation of privacy in his images, as Fourth Amendment
4               UNITED STATES V. WILSON

rights are personal. The panel concluded that the officer
therefore violated the defendant’s Fourth Amendment right
to be free from unreasonable searches when he examined the
defendant’s email attachments without a warrant.


                       COUNSEL

Devin Burstein (argued), Warren & Burstein, San Diego,
California, for Defendant-Appellant.

Peter Ko (argued), Assistant United States Attorney; Helen
H. Hong, Chief, Appellate Section, Criminal Division;
Robert S. Brewer, Jr., United States Attorney; United States
Attorney’s Office, San Diego, California; for Plaintiff-
Appellee.

Jennifer Lynch and Andrew Crocker, Electronic Frontier
Foundation, San Francisco, California; Jennifer Stisa
Granick, American Civil Liberties Union Foundation, San
Francisco, California; Brett Max Kaufman and Nathan Freed
Wessler, American Civil Liberties Union Foundation, New
York, New York; for Amici Curiae Electronic Frontier
Foundation and American Civil Liberties Union Foundation.

Marc Rotenberg, Alan Butler, and Megan Iorio, Electronic
Privacy Information Center, Washington, D.C., for Amicus
Curiae Electronic Privacy Information Center (EPIC).

Ryan T. Mrazik, Erin K. Earl, and Rachel A.S. Haney,
Perkins Coie LLP, Seattle, Washington, for Amici Curiae
Google LLC and Facebook, Inc.
                 UNITED STATES V. WILSON                    5

                         OPINION

BERZON, Circuit Judge:

    We once again consider the application of the Fourth
Amendment’s warrant requirement to new forms of
communication technology. See, e.g., United States v. Cano,
934 F.3d 1002 (9th Cir. 2019); cf. Carpenter v. United
States, 138 S. Ct. 2206 (2018). “When confronting [such]
concerns wrought by digital technology, th[e] [Supreme]
Court [and this court] ha[ve] been careful not to uncritically
extend existing precedents.” Id. at 2222. Our question this
time concerns the private search exception to the Fourth
Amendment—specifically, the intersection between
electronic communications providers’ control over material
on their own servers and the Fourth Amendment’s restriction
of warrantless searches and seizures, which limits only
governmental action. See Burdeau v. McDowell, 256 U.S.
465 (1921); Walter v. United States, 447 U.S. 649 (1980);
United States v. Jacobsen, 466 U.S. 109 (1984).

    The events giving rise to Luke Wilson’s conviction and
this appeal were triggered when Google, as required by
federal law, reported to the National Center for Missing and
Exploited Children (NCMEC) that Wilson had uploaded
four images of apparent child pornography to his email
account as email attachments. No one at Google had opened
or viewed Wilson’s email attachments; its report was based
on an automated assessment that the images Wilson
uploaded were the same as images other Google employees
had earlier viewed and classified as child pornography.
Someone at NCMEC then, also without opening or viewing
them, sent Wilson’s email attachments to the San Diego
Internet Crimes Against Children Task Force (ICAC), where
an officer ultimately viewed the email attachments without
a warrant. The officer then applied for warrants to search
6                   UNITED STATES V. WILSON

both Wilson’s email account and Wilson’s home, describing
the attachments in detail in the application.

    Our question is whether the government’s warrantless
search of Wilson’s email attachments was justified by the
private search exception to the Fourth Amendment. See
Walter, 447 U.S. at 655–56; Jacobsen, 466 U.S. at 113–14.
For the reasons that follow, we hold that it was not. We
therefore reverse the district court’s denial of Wilson’s
motion to suppress and vacate Wilson’s conviction.

I. Background

    A. Google’s Identification              of    Apparent        Child
       Pornography

    Electronic communication service providers are not
required “affirmatively [to] search, screen, or scan” for
apparent violations on their platforms of federal child
pornography laws. 18 U.S.C. §§ 2258A(f), 2258E. But “[i]n
order to reduce . . . and . . . prevent the online sexual
exploitation of children,” such providers, including Google,
are directed, “as soon as reasonably possible after obtaining
actual knowledge” of “any facts or circumstances from
which there is an apparent violation of . . . child pornography
[statutes],” to “mak[e] a report of such facts or
circumstances” to NCMEC. 18 U.S.C. § 2258A(a). 1
NCMEC then forwards what is known as a CyberTip to the


    1
      “A provider that knowingly and willfully failed to make a report
required . . . shall be fined.” 18 U.S.C. § 2258A(e). Further, in the case
of “intentional, reckless, or other misconduct,” there may be “a civil
claim or criminal charge against a provider . . . arising from the
performance of the reporting or preservation responsibilities.” Id. at
§§ 2258B(a), (b).
                   UNITED STATES V. WILSON                           7

appropriate law enforcement agency for                       possible
investigation. Id. at §§ 2258A(a)(1)(B)(ii), (c).

    According to a two-page declaration from a senior
manager at Google, the company “independently and
voluntarily take[s] steps to monitor and safeguard [its]
platform,” including using a “proprietary hashing
technology” to identify apparent child pornography. 2

    As described in the record—vaguely, and with the gaps
noted—the process works as follows:

   First, a team of Google employees are “trained by
counsel on the federal statutory definition of child
pornography and how to recognize it.” Neither the training
materials themselves nor a description of their contents
appear in or are attached to the Google manager’s
declaration.

    Second, these employees “visually confirm[]” an image
“to be apparent child pornography.” According to an
industry classification standard created by various electronic
service providers, there are four industry categorizations:
“A1” for a sex act involving a prepubescent minor; “A2” for
a lascivious exhibition involving a prepubescent minor;
“B1” for a sex act involving a pubescent minor; and “B2”
for a lascivious exhibition involving a pubescent minor.

    Third, “[e]ach offending image” judged to be “apparent
child pornography as defined in 18 USC § 2256” is given a
hash value, which is “added to [the] repository of hashes.”

    2
      “A hash value is (usually) a short string of characters generated
from a much larger string of data (say, an electronic image) using an
algorithm.” United States v. Ackerman, 831 F.3d 1292, 1294 (10th Cir.
2016).
8               UNITED STATES V. WILSON

As far as the record shows, Google “stores only the hash
values” of images identified as apparent child pornography,
not the actual images. The government does not represent
otherwise.

    Finally, Google “[c]ompare[s] these hashes to hashes of
content uploaded to [their] services.” The exact manner in
which hash values are assigned to either the original
photographs or the ones deemed to replicate them is not
described in the Google manager’s declaration or anywhere
else in the record.

    B. Government Search

    On June 4, 2015, Google, using its propriety technology,
“became aware” that Wilson had attached to emails in his
email account—which may or may not have been sent—four
files that included apparent child pornography. United States
v. Wilson, No. 3:15-cr-02838-GPC, 2017 WL 2733879, at
*3 (S.D. Cal. June 26, 2017). In compliance with its
reporting obligations, Google automatically generated and
sent an electronic CyberTipline report to NCMEC. The
CyberTipline report included Wilson’s four email
attachments. According to the Google manager’s
declaration, “a Google employee did not view the images . . .
concurrently to submitting the report to NCMEC.” The
CyberTipline report did specify that Google had classified
each of Wilson’s four email attachments as “A1” under an
industry classification standard for “content [which]
contain[s] a depiction of a prepubescent minor engaged in a
sexual act.”

   Google’s report included Wilson’s email address,
secondary email address, and IP addresses. NCMEC
supplemented Google’s report with geolocation information
                    UNITED STATES V. WILSON                             9

associated with Wilson’s IP addresses, but did “not open[]
or view[] any uploaded files submitted with this report.”

    NCMEC then forwarded the CyberTip to the San Diego
Internet Crimes Against Children Task Force (“ICAC”).
Agent Thompson, a member of the San Diego ICAC,
received the report. He followed San Diego ICAC
procedure, which at the time called for inspecting the images
without a warrant whether or not a Google employee had
reviewed them. 3

    After Agent Thompson looked at Wilson’s four email
attachments, he applied for a search warrant of Wilson’s
email account. His affidavit asserted that probable cause for
the warrant was based on two facts: first, that “Google
became aware of four (4) image files depicting suspected
child pornography;” and second, that he had “reviewed the
four (4) images reported by Google to NCMEC and
determined they depict child pornography.” In support of his
own child pornography assessment, he included in the
warrant application detailed “descriptions of each of these
images.” The affidavit did not include the fact that Google
had originally classified the images as “A1” or provide any
detail about how Google had either classified or later
automatically identified Wilson’s images as apparent child
pornography.

   On the basis of the application and affidavit submitted
by Agent Thompson, a magistrate judge issued a search


    3
      Agent Thompson testified that San Diego ICAC, which includes
both local, county, regional, and federal agencies, now obtains a search
warrant before opening a CyberTip when the provider has not viewed
the images. It is not clear from the record whether other ICAC task forces
across the country have adopted the same policy.
10              UNITED STATES V. WILSON

warrant for Wilson’s email account. When Agent Thompson
executed the warrant, he discovered numerous email
exchanges in which Wilson received and sent images and
video files of alleged child pornography and in which
Wilson offered to pay for the creation of child pornography.

    Agent Thompson then obtained a search warrant for
Wilson’s residence. On executing the warrant, law
enforcement officers found and seized several electronic
devices that contained evidence of child pornography. One
officer observed a backpack being tossed over Wilson’s
balcony at the time officers were knocking on Wilson’s door
and announcing their presence. Wilson’s checkbook and a
thumb drive containing thousands of images of child
pornography—including the four images reported by
Google—were found in the backpack.

     C. Motion to Suppress

    Wilson filed a motion to suppress all evidence seized
from his email account and residence, arguing that Agent
Thompson’s review of his email attachments without a
warrant was impermissible under the Fourth Amendment.
Relying principally on Jacobsen, 466 U.S. 109, and United
States v. Tosti, 733 F.3d 816 (9th Cir. 2013), the government
maintained in response that Agent Thompson’s review of the
four images did not exceed the scope of Google’s private
search and so, under the private search doctrine as
enunciated in Jacobsen and Tosti, was valid without a
warrant.

    The district court agreed. The court denied Wilson’s
motion to suppress on the ground that the government’s
warrantless search did not exceed the scope of the antecedent
private search and so did not require a warrant. The district
court also concluded that “if [Agent] Thompson’s
                     UNITED STATES V. WILSON                            11

warrantless viewing of the four images constituted an illegal
search, neither excising the tainted evidence from the
affidavit nor the good faith exception would prevent
operation of the exclusionary rule.” 4 Wilson, 2017 WL
2733879, at *12–13.

   After waiving his right to a jury trial, Wilson was
convicted of possession and distribution of child
pornography 5 and sentenced to 11 years of incarceration and


    4
        The government does not contest these contingent rulings.
      5
        While this appeal was pending, the California Court of Appeal held
that “the government’s warrantless search of Wilson’s four images was
permissible under the private search doctrine.” People v. Wilson, 56 Cal.
App. 5th 128, 147 (2020), as modified on denial of reh’g (Nov. 6, 2020),
review denied (Jan. 20, 2021). We have not squarely addressed the
preclusive effect of the denial of a suppression motion in an earlier state-
court proceeding. Other circuits, however, have held that “the
government may not collaterally estop a criminal defendant from
relitigating an issue against the defendant in a different court in a prior
proceeding.” United States v. Harnage, 976 F.2d 633, 636 (11th Cir.
1992); accord United States v. Pelullo, 14 F.3d 881, 896 (3d Cir. 1994);
United States v. Gallardo-Mendez, 150 F.3d 1240, 1244 (10th Cir.
1998). Citing those cases, we came to the similar conclusion that, in
criminal trials, the government “may not use collateral estoppel to
establish, as a matter of law, an element of an offense or to conclusively
rebut an affirmative defense on which the Government bears the burden
of proof beyond a reasonable doubt.” United States v. Smith-Baltiher,
424 F.3d 913, 920 (9th Cir. 2005) (quoting United States v. Arnett,
353 F.3d 765, 766 (9th Cir. 2003) (en banc) (per curiam)).

     We need not definitively resolve the preclusion question as it relates
to a motion to suppress, here, as the government has not asserted
collateral estoppel, so the argument is waived. Harbeson v. Parke Davis,
Inc., 746 F.2d 517, 520 (9th Cir. 1984) (“The United States was unaware
that Mr. Wilson had raised the same issue in his state appeal until the
letter filed in this case by [defense counsel] on October 16, 2020.”).
12                  UNITED STATES V. WILSON

10 years of supervised release for each count, to run
concurrently. 6

II. Discussion

    The government does not dispute for purposes of this
case Wilson’s assertion that Agent Thompson’s review of
his email attachments was a search within the meaning of the
Fourth Amendment. We proceed on that assumption as
well—that is, we assume that Wilson had a subjective
expectation of privacy in his email attachments that society
is prepared to recognize as reasonable, see Kyllo v. United
States, 533 U.S. 27, 33 (2001) (citing Katz v. United States,
389 U.S. 347, 361 (1967) (Harlan, J., concurring)); see also
United States v. Miller, 982 F.3d 412, 427 (6th Cir. 2020)
(taking the same approach); cf. United States v. Ackerman,
831 F.3d 1292, 1308 (10th Cir. 2016) (holding that when the
government views email attachments it is a “search” for
Fourth Amendment purposes under both an expectation-of-
privacy and a trespass-to-chattels theory). 7 Our question,
then, is whether Agent Thompson was permitted to look at
Wilson’s email attachments under the private search


     6
      Wilson maintains that the district court did not obtain a valid
waiver of his right to a jury trial, as required by Fed. R. Crim. P. 23(a).
Because we vacate Wilson’s conviction and reverse the district court’s
denial of Wilson’s motion to suppress, we do not reach this issue.
     7
      Because we hold that the government’s warrantless search violated
Wilson’s privacy-based Fourth Amendment rights, we do not consider
Wilson’s alternative argument that the government’s search violated his
property-based Fourth Amendment rights. See Carpenter v. United
States, 138 S. Ct. 2206, 2269 (2018) (Gorsuch, J. dissenting) (“[F]ew
doubt that e-mail should be treated much like the traditional mail it has
largely supplanted—as a bailment in which the owner retains a vital and
protected legal interest.”).
                UNITED STATES V. WILSON                   13

exception, such that the Fourth Amendment did not require
him to procure a warrant.

    We review the district court’s denial of Wilson’s motion
to suppress de novo and the district court’s underlying
factual findings for clear error. See United States v. Camou,
773 F.3d 932, 937 (9th Cir. 2014); see also United States v.
Mulder, 808 F.2d 1346, 1348 (9th Cir. 1987).

   A. Private Search Exception

    As the Fourth Amendment protects individuals from
government actors, not private ones, see Burdeau v.
McDowell, 256 U.S. 465 (1921), a private party may conduct
a search that would be unconstitutional if conducted by the
government. The private search doctrine concerns
circumstances in which a private party’s intrusions would
have constituted a search had the government conducted it
and the material discovered by the private party then comes
into the government’s possession. Invoking the precept that
when private parties provide evidence to the government “on
[their] own accord[,] … it [i]s not incumbent on the police
to . . . avert their eyes,” Coolidge v. New Hampshire,
403 U.S. 443, 489 (1971), the Supreme Court formalized the
private search doctrine in a pair of decisions about four
decades ago: Walter v. United States, 447 U.S. 649 (1980),
which produced no majority decision, and United States v.
Jacobsen, 466 U.S. 109 (1984), which did.

       1. Doctrinal Foundations

    Beginning from the initial articulation of the private
search doctrine, the extent to which it excuses the
government from compliance with the warrant requirement
of the Fourth Amendment has been the subject of concern.
The exception has, for example, been described as
14               UNITED STATES V. WILSON

“unsettling” for its potential reach. 1 Wayne R. LaFave,
Search and Seizure: A Treatise on the Fourth Amendment
§1.8(b) (6th ed. 2020); see also Jacobsen, 466 U.S. at 129–
34 (White, J., concurring in part and concurring in
judgment). On examination, however, the history of the
exception confirms that it is, in truth, a narrow doctrine with
limited applications.

    Beginning with Burdeau, the Supreme Court has
distinguished between government agents and private
parties for purposes of the Fourth Amendment. Burdeau
considered whether the Fourth Amendment restricts the
government’s ability to use papers incriminating an
individual when those papers were volunteered to the
government by a private party who had stolen them. Burdeau
disregarded the private theft, noting that although “[t]he
Fourth Amendment gives protection against unlawful
searches and seizures, . . . its protection applies to
governmental action.” 256 U.S. at 475.

    Coolidge, decided 50 years after Burdeau, addressed
whether a private party who provides the government with
another person’s contraband or evidentiary material can be
considered an agent of the government for purposes of the
Fourth Amendment. In that case, local police officers arrived
at a suspect’s home, questioned his wife about his
involvement in a murder, and obtained from his wife a rifle
and articles of clothing belonging to the suspect. Coolidge,
403 U.S. at 446, 486. The opinion does not explain whether
the suspect’s wife had proper possession of the items. The
Court stated only that, had the suspect’s wife, “wholly on her
own initiative, sought out her husband’s guns and clothing
and then taken them to the police station to be used as
evidence against him, there can be no doubt under [Burdeau]
that the articles would later have been admissible in
                UNITED STATES V. WILSON                   15

evidence.” Id. at 487. The relevant inquiry, according to the
Court, was whether the suspect’s wife, “in light of all the
circumstances of the case, must be regarded as having acted
as an instrument or agent of the state when she produced her
husband’s belongings.” Id. (internal quotation marks
omitted). As the record showed that the suspect’s wife had
shared the suspect’s guns and clothes with the local police
“of her own accord,” Coolidge held that “it was not
incumbent on the police to stop her or avert their eyes” when
offered the critical evidence. Id. at 489.

       2. Doctrinal Scope

    Following Burdeau and Coolidge, both Walter and
Jacobsen considered a warrantless government search after
a private party “freely made available” certain information
for the government’s inspection. Jacobsen, 466 U.S. at 119–
20 (citing Coolidge, 403 U.S. at 487–90). Together, the cases
determined that an antecedent private search excuses the
government from obtaining a warrant to repeat the search but
only when the government search does not exceed the scope
of the private one. That is, “[t]he additional invasions of
respondents’ privacy by the government agent must be tested
by the degree to which they exceeded the scope of the private
search.” Id. at 115.

    In Walter, a package of obscene films was mistakenly
delivered to the wrong recipient. 447 U.S. at 651. The
recipient opened the external packaging and examined the
boxes containing individual films. Id. at 651–52. Each box
displayed “suggestive drawings” on one side and “explicit
descriptions of the contents” of the film on the other. Id.
at 652. After reading these descriptions, and “attempt[ing]
without success to view portions of the film by holding it up
to the light,” the recipient notified the FBI about the
mistaken delivery. Id. The FBI then seized the boxes and
16               UNITED STATES V. WILSON

screened one of the films without first obtaining a warrant.
Id.

    Walter did not result in a majority opinion, but a majority
of the justices concluded that there had been a violation of
the Fourth Amendment, and a different majority of justices
agreed on the standard to be applied.

    Justice Stevens, joined by Justice Stewart, announced the
judgment of the Court. Their opinion concluded that the
government search exceeded the scope of the antecedent
actions by the private individuals in two respects. First, the
government agents had screened the film for the purpose of
learning information necessary to determine that a crime had
been committed:

       It is perfectly obvious that the agents’ reason
       for viewing the films was to determine
       whether their owner was guilty of a federal
       offense. To be sure, the labels on the film
       boxes gave them probable cause to believe
       that the films were obscene and that their
       shipment in interstate commerce had
       offended the federal criminal code. . . . [But]
       a search of the contents of the films . . . was
       necessary in order to obtain the evidence
       which was to be used at trial.

Id. at 654. Second, the government agents had gone beyond
the physical bounds of the private search, because “the
private party had not actually viewed the films.” Id. at 657.
“The private search [thus] merely frustrated [the]
expectation [of privacy] in part,” not in full. Id. at 659. “It
                    UNITED STATES V. WILSON                          17

did not simply strip the remaining unfrustrated portion of
that expectation of all Fourth Amendment protection.” Id. 8

    The four justices in dissent would have concluded that
there was no Fourth Amendment violation. The dissenters
disputed not the basic approach of Justice Stevens’ opinion
but its application to the facts of the case. Specifically, the
dissent stressed that “[t]he containers . . . clearly revealed the
nature of their contents,” such that the private employees “so
fully ascertained the nature of the films . . . [that] the FBI’s
subsequent viewing of the movies . . . was not an additional
search subject to the warrant requirement.” Id. at 663–64
(Blackmun, J., dissenting, joined by Burger, C.J., and Powell
and Rehnquist, JJ.).

    Four years after Walter, the Supreme Court again applied
the private search doctrine. Importantly, Jacobsen
recognized “the agreement [in Walter] on the standard to be
applied in evaluating the relationship between the two
searches.” 466 U.S. at 117 n.12.

   Jacobsen concerned a government search of a Federal
Express (“FedEx”) package that had been partially opened
by FedEx employees. See 466 U.S. at 111. While examining
a damaged package, the FedEx employees “opened the

     8
       Justice Marshall concurred only in the judgment. Justice White,
joined by Justice Brennan, concurred, noting that “the packages already
had been opened, and the Government saw no more than what was
exposed to plain view.” Walter, 447 U.S. at 661 (White, J., concurring
in part and concurring in judgment). Although Justice Stevens
emphasized that the private parties had not screened the film, see id. at
657 & n.9, the concurring justices would have found a Fourth
Amendment violation even if the private parties had done so, as “a
private screening of the films would not have destroyed petitioners’
privacy interest in them.” Id. at 662.
18               UNITED STATES V. WILSON

package,” “cut open the tube” within the package, and
“found a series of four zip-lock plastic bags, the outermost
enclosing the other three and the innermost containing about
six and a half ounces of white powder.” Id. The employees
“observed . . . white powder in the innermost plastic bag,”
but did not open the (presumably transparent) bag. Id.
Instead, they called the Drug Enforcement Administration
(DEA), put the plastic bags back in the tube, and placed the
tube back in the box. Id.

    When DEA agents arrived, they did two things: First, to
visually inspect the contents of the plastic bags, DEA agents
removed the tube from the box and the plastic bags from the
tube. See id. Second, federal agents “opened each of the four
bags and removed a trace of the white substance with a knife
blade.” Id. at 111–12. They performed a field test to
determine whether the powder in the plastic bags was
cocaine. See id.

    Jacobsen considered whether the private search
exception as adopted by a majority of justices in Walter
applied to the facts at hand. In doing so, Jacobsen, like
Justice Stevens’ opinion in Walter, looked at both the degree
to which the government’s actions led to observing new
information not uncovered by the private search and the
extent to which the government’s investigation intruded on
the package owner’s privacy interests to a greater degree
than had the private party’s actions. As to the first parameter,
the information gleaned by the government, Jacobsen
permitted the government agent to “reexamine”—that is,
examine in the same manner—the package previously
examined by FedEx, the private party. The government
“could utilize the [private] employees’ testimony concerning
the contents of the package,” noted Jacobsen; “[p]rotecting
the risk of misdescription . . . is not protected by the Fourth
                UNITED STATES V. WILSON                   19

Amendment.” 466 U.S. at 119. As to the second parameter,
the additional impairment of privacy interests, Jacobsen
emphasized that the private search exception turns on parity
with the impact of the private search: “[O]nce frustration of
the original expectation of privacy occurs, the Fourth
Amendment does not prohibit governmental use of the now-
nonprivate information.” Id. at 117.

    Applying these precepts, Jacobsen concluded that the
“removal of the plastic bags from the tube and the
[government] agent’s visual inspection of their contents” did
not exceed the scope of the private search as to the
information obtained. Id. at 120. “[T]he agent[s] . . .
learn[ed] nothing [from those actions] that had not
previously been learned during the private search” and
conveyed to the federal agents by the FedEx employees. Id.
And as to the privacy interests, the governmental search to
that point “infringed no legitimate expectation of privacy
and hence was not a ‘search’ within the meaning of the
Fourth Amendment,” id., as “[t]he package itself, which had
previously been opened, remained unsealed, and the Federal
Express employees had invited the agents to examine its
contents,” such that “the package could no longer support
any expectation of privacy,” id. at 121.

    Jacobsen then separately considered the chemical field
test, conducted by the DEA agents, including the federal
agents’ removal of the white powder from the plastic bag.
Critically for our purposes, Jacobsen began this inquiry from
the premise that because the field test “had not been
conducted by the Federal Express agents,” it “therefore
exceeded the scope of the private search.” Id. at 122
(emphasis added). The majority then determined that the
government’s chemical field test of the substance in the
properly seized plastic bags was nonetheless not a search
20                 UNITED STATES V. WILSON

within the meaning of the Fourth Amendment, because
“governmental conduct that can reveal whether a substance
is cocaine, and no other arguably ‘private’ fact, compromises
no legitimate privacy interest.” Id. at 122–23. This
conclusion, Jacobsen explained, was “dictated” by the
Court’s earlier decision in United States v. Place, 462 U.S.
696 (1983), “in which the Court held that subjecting luggage
to a ‘sniff test’ by a trained narcotics detection dog was not
a ‘search’ within the meaning of the Fourth Amendment.”
Jacobsen, 466 U.S. at 123.

     B. Application of the Private Search Exception to
        This Case

    The government bears the burden to prove Agent
Thompson’s warrantless search was justified by the private
search exception to the Fourth Amendment’s warrant
requirement. Before considering the private search
exception, Coolidge emphasized “the most basic
constitutional rule” in the Fourth Amendment arena:
warrantless searches are per se unreasonable, subject to few
exceptions that are “jealously and carefully drawn.”
403 U.S. at 454–55. Accordingly, “[t]he burden is on those
seeking the exemption.” Id. at 455 (quoting United States v.
Jeffers, 342 U.S. 48, 51 (1951)). The government has not
met its burden here.

    Both as to the information the government obtained and
the additional privacy interests implicated, the government’s
actions here exceed the limits of the private search exception
as delineated in Walter and Jacobsen and their progeny. 9

     Wilson opines that the private search exception to the Fourth
     9

Amendment should be overruled, and seeks to preserve that question for
any Supreme Court review of this case. As a court of appeals, we of
                    UNITED STATES V. WILSON                            21

First, the government search exceeded the scope of the
antecedent private search because it allowed the government
to learn new, critical information that it used first to obtain a
warrant and then to prosecute Wilson. Second, the
government search also expanded the scope of the
antecedent private search because the government agent
viewed Wilson’s email attachments even though no Google
employee—or other person—had done so, thereby


course cannot overrule Supreme Court cases. United States v. Weiland,
420 F.3d 1062, 1079 n.16 (9th Cir. 2005) (“[W]e are bound to follow a
controlling Supreme Court precedent until it is explicitly overruled by
that Court.”); accord Nunez-Reyes v. Holder, 646 F.3d 684, 692 (9th Cir.
2011). We do note that the private search doctrine rests directly on the
same precepts concerning the equivalence of private intrusions by
private parties and the government that underlie the so-called third-party
doctrine. See e.g., Smith v. Maryland, 442 U.S. 735, 744 (1979) (holding
that by “voluntarily” conveying to his telephone company the phone
numbers he dialed, the defendant forsook his reasonable expectation of
privacy in that information); United States v. Miller, 425 U.S. 435, 442
(1976) (holding the defendant lacked a reasonable expectation of privacy
in “information [he had] voluntarily conveyed to [his] bank[]” like
financial statements and deposit slips). In Jacobsen, the Supreme Court
reasoned that the private search exception follows from the premise,
underlying the third-party doctrine, that “when an individual reveals
private information to another, he assumes the risk that his confidant will
reveal that information to the authorities.” 466 U.S. at 117. In recent
years, however, the Court has refused to “mechanically apply[] the third-
party doctrine,” stressing that “the fact of ‘diminished privacy interests
does not mean that the Fourth Amendment falls out of the picture
entirely.’” Carpenter, 138 S. Ct. at 2219 (quoting Riley, 573 U.S. at 392);
see United States v. Jones, 565 U.S. 400, 417 (2012) (Sotomayor, J.,
concurring) (explaining that the third-party doctrine “is ill suited to the
digital age, in which people reveal a great deal of information about
themselves to third parties in the course of carrying out mundane tasks”);
Susan Freiwald & Stephen Wm. Smith, The Carpenter Chronicle: A
Near-Perfect Surveillance, 132 Harv. L. Rev. 205, 224 (2018) (noting
that Carpenter “significantly narrowed the [third-party] doctrine’s
scope”).
22              UNITED STATES V. WILSON

exceeding any earlier privacy intrusion. Moreover, on the
limited evidentiary record, the government has not
established that what a Google employee previously viewed
were exact duplicates of Wilson’s images. And, even if they
were duplicates, such viewing of others’ digital
communications would not have violated Wilson’s
expectation of privacy in his images, as Fourth Amendment
rights are personal.

       1. Additional Information

    The district court analogized Agent Thompson’s review
of Wilson’s email attachments to the government search in
Jacobsen, concluding that Agent Thompson’s search
allowed him to “learn nothing new,” because Google had
already classified the images as child pornography. Wilson,
2017 WL 2733879, at *10–11. The government similarly
argues on appeal that its official search did not
impermissibly expand the scope of the private search
because it “just confirmed what Google employees already
knew and could say.” Both the district court’s conclusion
and the governments’ argument misstate the record.

    The record indicates that Google does not keep a
repository of child pornography images, so no Google
employee could have shown the government the images it
believed to match Wilson’s. Nor does the record identify the
individual who viewed those images in the repository, so no
identified Google employee “knew and could say” what
those images showed. Instead, Google keeps a repository of
unique hash values corresponding to illicit images, and tags
each image with one of four generic labels. All Google
communicated to NCMEC in its CyberTip was that the four
images Wilson uploaded to his email account matched
images previously identified by some Google employee at
some time in the past as child pornography and classified as
                  UNITED STATES V. WILSON                         23

depicting a sex act involving a prepubescent minor (the “A1”
classification). 10 Based only on the barebones CyberTip,
Agent Thompson testified, he opened and reviewed each of
Wilson’s images to determine “whether or not it is a case
that . . . can be investigated” for violations of federal law.

    A detailed description of the images was then included
in the applications for search warrants. The gulf between
what Agent Thompson knew about Wilson’s images from
the CyberTip and what he subsequently learned is apparent
from those descriptions. In contrast to Google’s label of the
images just as “A1,” which the government did not mention
in the warrant application, the government learned the
following:

         1. 140005125216.jpg – This image depicts a
         young nude girl, approximately five (5) to
         nine (9) years of age, who is lying on her
         stomach with her face in the nude genital
         region of an older female who is seated with
         her legs spread. A second young girl,
         approximately five (5) to nine (9) years of
         age, is also visible in this image and she is
         partially nude with her vagina exposed.
         Google identified this image was uploaded
         on June 4, 2015, at 16:11:04 UTC.

         2. 140005183260.jpg – This image depicts a
         young nude girl, approximately five (5) to
         nine (9) years of age, who is lying on top of

    10
       Perhaps a Google employee could also have testified to details
about the company’s proprietary technology. But no such information
appears in the record, and the CyberTip did not convey any more
information than what is now included in the record.
24              UNITED STATES V. WILSON

       an older nude female, approximately
       eighteen years of age. Within this image the
       girl’s genital regions are pressed against one
       another and the older girl appears to be
       touching the face of the younger child with
       her tongue. Google identified this image was
       uploaded on June 4, 2015, at 16:11:21 UTC.

       3. 140005129034.jpg – This image depicts a
       partially nude young girl, approximately five
       (5) to nine (9) years of age, who is lying on
       her back with her legs spread and her vagina
       exposed. An older female is positioned in
       front of this girl’s exposed vagina in this
       image and the younger girl has her left hand
       on the vaginal/buttocks area of a second nude
       girl of similar age. Google identified this
       image was uploaded on June 4, 2015, at
       16:11:06 UTC.

       4. 1400052000787.jpg – This image depicts
       a wider angle view of the previously
       referenced images possessing file names
       140005125216.jpg and 140005129034.jpg as
       reported by Google.

Wilson, 2017 WL 2733879, at *4–5.

    Given the large gap between the information in the
CyberTip and the information the government obtained and
used to support the warrant application and to prosecute
Wilson, the government search in Walter offers a much more
apt comparison to the circumstances here than does the
government search in Jacobsen. Google’s categorization of
Wilson’s email attachments as “A1” functioned as a label for
                 UNITED STATES V. WILSON                    25

the images in the same way that the boxes describing the
films in Walter suggested that the images on the films were
obscene. The “A1” labels, in fact, provided less information
about the images’ contents than did the boxes in Walter,
which had “explicit descriptions of the contents” of the film.
447 U.S. at 652. The “A1” labels, in contrast, specified only
the general age of the child and the general nature of the acts
shown.

    Viewing Wilson’s email attachments—like viewing the
movie in Walter—substantively expanded the information
available to law enforcement far beyond what the label alone
conveyed, and was used to provide probable cause to search
further and to prosecute. The government learned at least
two things above and beyond the information conveyed by
the CyberTip by viewing Wilson’s images: First, Agent
Thompson learned exactly what the image showed. Second,
Agent Thompson learned the image was in fact child
pornography. Until he viewed the images, they were at most
“suspected” child pornography. Just as it “was clearly
necessary for the FBI to screen the films [in Walter], which
the private party had not done, in order to obtain the evidence
needed to accomplish its law enforcement objectives,”
Walter, 447 U.S. at 659 n.14 (plurality), so here, to prosecute
Wilson it was necessary for Agent Thompson to view the
images no Google employee had opened. Id. Until Agent
Thompson viewed Wilson’s images, no one involved in
enforcing the child pornography ban had seen them. Only by
viewing the images did the government confirm, and convey
to the fact finder in Wilson’s criminal case, that they
depicted child pornography under the applicable federal
standard.

    Importantly, the district court found—and we agree—
that if Agent Thompson’s affidavit in support of a warrant
26                 UNITED STATES V. WILSON

had been “excise[d]” of “the tainted evidence,” “the affidavit
would not support issuance of the search warrant for
Defendant’s email account.” Wilson, 2017 WL 2733879,
at *12. 11 The district court’s findings about the inadequacy
of the warrant application without the important information
Agent Thompson obtained by viewing Wilson’s images
demonstrate that the government learned new, critical
information by viewing Wilson’s images, information “not
previously . . . learned during the private search,” Jacobsen,
466 U.S. at 120. Because the government saw more from its
search than the private party had seen, it exceeded the scope
of the private search.

          2. Additional Intrusion on Wilson’s Privacy
             Interest

    The government also maintains that directly viewing
Wilson’s images for the first time was not a further invasion
of Wilson’s privacy, beyond any privacy invasion by
Google. The government’s expectation of privacy analysis
fails for much the same reason as did its argument that it
learned nothing new by viewing the images.

    The government’s central submission in this regard is
that Wilson’s expectation of privacy in his images was fully
frustrated when Google’s computer technology scanned
them, such that any further government search of the images




      We also agree with the district court that the government might
     11

have been able to demonstrate probable cause sufficient to obtain a
warrant without the descriptions of Wilson’s images, by presenting, for
example, more “information about Google’s screening process for child
pornography,” Wilson, 2017 WL 2733879, at *12.
                   UNITED STATES V. WILSON                          27

should be exempt from the Fourth Amendment’s warrant
requirement. 12 We cannot agree.

     Although Google’s proprietary technology labelled
Wilson’s email attachments as “A1,” “the content of the
[images] . . . was [no more] apparent” to Google than the
image content was to the private party in Walter, as no
Google employee had opened and viewed the attachments,
and Google does not appear to retain any record of the
original images used to generate hash matches. See Tosti,
733 F.3d at 823. Agent Thompson did not obtain a specific
description of the content of Wilson’s attachments from
Google, so he was not simply confirming what he had been
told. Until he viewed the images, he had no image at hand at
all; the entire composition was hidden. Only the image itself
could reveal, for example, the number of minors depicted,
their identity, the number of adults depicted alongside the
minors, the setting, and the actual sexual acts depicted.
Reading a label affixed to an image is a different experience
entirely from looking at the image itself. To read even a
detailed description, which this A1 classification was not, is
still not to see. Wilson’s privacy interest was in the actual
image—which could have included features in addition to
child pornography—not just in its classification as child
pornography.

   The government’s argument to the contrary
mischaracterizes the record, by representing that Google’s
scan “equates to a full-color, high-definition view” of
Wilson’s images. It does not. The critical fact is that no
Google employee viewed Wilson’s files before Agent

    12
       The government stated at oral argument that it is not relying on
the contraband nature of child pornography as a justification for the
search.
28               UNITED STATES V. WILSON

Thompson did. When the government views anything other
than the specific materials that a private party saw during the
course of a private search, the government search exceeds
the scope of the private search. That is the clear holding of
Jacobsen. In that case, “[t]he field test . . . had not been
conducted by the Federal Express agents and therefore
exceeded the scope of the private search.” 466 U.S. at 122
(emphasis added); see supra Part II.B.1.

       3. Personal Nature of the Fourth Amendment

    The government attempts to save its warrantless search
by shifting the analysis from the private search of Wilson’s
files, flagged by Google and classified as A1 by its
proprietary technology, to the private search of other
individuals’ files, which some Google employee previously
viewed and classified as child pornography in Google’s
database of hash values. The government argues that Agent
Thompson’s search did not exceed the bounds of the private
search because a Google employee had previously viewed
different child pornography files, and Google’s computers
flagged Wilson’s email attachments as containing the same
images as those files, using an unspecified hash value
comparison system. This line of argument cannot save the
validity of the government’s search. Even if Wilson’s email
attachments were precise duplicates of different files a
Google employee had earlier reviewed and categorized as
child pornography, both Walter and Jacobsen—and general
Fourth Amendment principles—instruct that we must
specifically focus on the extent of Google’s private search of
Wilson’s effects, not of other individuals’ belongings, to
assess whether “the additional invasions of [Wilson’s]
privacy by the government agent . . . exceeded the scope of
the private search.” Jacobsen, 466 U.S. at 115.
                 UNITED STATES V. WILSON                    29

    To see why, consider whether Walter would have come
out differently had the misdirected package come into the
hands of someone who had previously viewed another copy
of the same film and, recognizing the box, told the police
that the film in it was, in her view, legally obscene. Under
Walter, the government in the hypothesized circumstance
would still need a warrant to view the film in the box.
Viewing the copy of the film actually in the box, which the
mistaken recipient of the box had not done, would still entail
an additional governmental intrusion on both the physical
integrity of the film and the owner’s privacy interest in its
content.

     Fourth Amendment rights are personal rights. Rakas v.
Illinois, 439 U.S. 128 (1978), is illustrative: Rakas held that
a passenger could not challenge a police search as violative
of the Fourth Amendment because he owned neither the
vehicle that was searched nor the rifle found. Although the
owners of each item had an expectation of privacy, the
defendant did not. See id. at 134.

    So Wilson did not have an expectation of privacy in
other individuals’ files, even if their files were identical to
his files. The corollary of this principle must also be true:
Wilson did have an expectation of privacy in his files, even
if others had identical files. If, for example, police officers
search someone else’s house and find documents evidencing
wrongdoing along with notes indicating that I have identical
documents in my house, they cannot, without a warrant or
some distinct exception to the warrant requirement, seize my
copies. I would retain a personal expectation of privacy in
them, and in my connection to them, even if law enforcement
had a strong basis for anticipating what my copies would
contain. A violation of a third party’s privacy has no bearing
30               UNITED STATES V. WILSON

on my reasonable expectation of privacy in my own
documents. The government does not argue otherwise.

    In short, whether Google had previously reviewed, at
some earlier time, other individuals’ files is not pertinent to
whether a private search eroded Wilson’s expectation of
privacy. Under the private search doctrine, the Fourth
Amendment remains implicated “if the authorities use
information with respect to which the expectation of privacy
has not already been frustrated.” Jacobsen, 466 U.S. at 117
(emphasis added).

     C. Relevant Appellate Caselaw

    (i) Our application of Jacobsen and Walter is consistent
with Ninth Circuit case law. The district court misapplied
United States v. Tosti, 733 F.3d 816 (9th Cir. 2013), in
reaching the contrary conclusion.

    In Tosti, a private party entrusted with the defendant’s
computer found thumbnails of images believed to be child
pornography and alerted law enforcement officers. 733 F.3d
at 818–19. The private party showed the thumbnails to law
enforcement, and the agents “could tell from viewing the
thumbnails that the images contained child pornography.”
Id. at 822.

    Tosti held that law enforcement’s enlarging of the
thumbnails did not expand on the antecedent private search.
For one, based on the standard articulated in Jacobsen, “the
police learned nothing new through their actions.” Tosti,
733 F.3d at 822. Further, “scrolling through the images [the
private party] had already viewed was not a search because
any private interest in those images had been extinguished.”
Id.
                 UNITED STATES V. WILSON                    31

    Neither is true in this case. Here, what was conveyed to
Agent Thompson was that a not-yet-viewed image uploaded
by Wilson matched a different image that an unidentified
Google employee had previously viewed and classified as
child pornography. So until Agent Thompson actually
viewed the images, he knew only that Google’s propriety
technology had identified a match between Wilson’s images
and other images that Google had classified as child
pornography. He “learned . . . [a]new through [his] actions,”
for the first time, what the images actually showed. See
supra pp. 23–24. And, as no one at Google had previously
viewed Wilson’s attachments, “any privacy interest in those
images had [not] been extinguished.” Tosti, 733 F.3d at 822.
Google’s algorithm “frustrated [Wilson’s] [privacy]
expectation in part,” but it “did not . . . strip the remaining
unfrustrated portion of that expectation of all Fourth
Amendment protection.” Walter 447 U.S. at 659 (plurality);
see also Jacobsen, 466 U.S. at 116 n.11.

   For these reasons, Tosti is fully consistent with our
conclusion that Agent Thompson’s search exceeded the
scope of the private search and so required a warrant.

   (ii) In so holding, we contribute to a growing tension in
the circuits about the application of the private search
doctrine to the detection of child pornography.

    In United States v. Ackerman, 831 F.3d 1292, 1294 (10th
Cir. 2016), AOL automatically identified one of the
defendant’s four email attachments as apparent child
pornography, based on a hash value match. AOL then sent
the text of the defendant’s email and all four attachments to
NCMEC, where an analyst “opened the email, viewed each
of the attached images, and confirmed that all four [images]
(not just the one AOL’s automated filed identified) appeared
to be child pornography.” Id. Ackerman emphasized that
32              UNITED STATES V. WILSON

“AOL never opened the email itself. Only NCMEC did
that.” Id. at 1305–06. Then-Judge Gorsuch, after holding that
NCMEC is either a governmental entity or a government
agent, see id. at 1308, concluded that “in at least this way
[the government] exceeded rather than repeated AOL’s
private search,” id. at 1305–06.

    Ackerman did suggest that, had the government viewed
only the attachment AOL identified as a hash value match
and not other attachments and the text of the defendant’s
email, that distinction might “bring the government closer to
a successful invocation of the private search doctrine.” Id.
at 1308 (emphasis added). But Ackerman also noted that in
that circumstance—which appears to be what happened
here—the government’s action may still be a new search, as
the government, “might . . . have risked exposing new and
protected information, maybe because the hash value match
could have proven mistaken . . . or because the AOL
employee who identified the original image as child
pornography was mistaken in his assessment.” Id. at 1306.
Although Ackerman did not decide the precise issue before
us, and expressly disavowed “prejudg[ing]” it, id. at 1308–
09, its underlying analysis is entirely consistent with ours,
and its suggestions about why there could be a search in our
circumstances echo some of the reasons we have given for
so concluding.

    Other private search cases concerning the discovery of
child pornography, outside the context of automated hash
value matching, have also ruled consistently with our
understanding of the limited scope of the private search
exception. For example, in United States v. Lichtenberger,
786 F.3d 478 (6th Cir. 2015), the defendant’s girlfriend had
discovered child pornography on his computer. She later
showed his computer to the police and opened some
                    UNITED STATES V. WILSON                            33

computer files that were determined to contain child
pornography. But the defendant’s girlfriend was “not at all
sure whether she opened the same files with [the police] as
she had opened earlier that day.” Id. at 490. As a result, the
Sixth Circuit concluded that the government search
exceeded the scope of the private search. This reasoning
supports our result here. The record does not identify the
Google analyst who could have stated that the images Agent
Thompson viewed were identical to images the analyst
previously viewed, nor does it explain Google’s algorithm in
any detail. Given these gaps, there is no way to be “at all
sure” that the images Agent Thompson viewed were the
same images a Google analyst had earlier viewed, so the
government search exceeded the scope of Google’s search.

    Further, in United States v. Sparks, 806 F.3d 1323 (11th
Cir. 2015), overruled on other grounds by United States v.
Ross, 963 F.3d 1056 (11th Cir. 2020), a store employee and
her fiancé discovered child pornography on a lost cell phone
and showed the phone to the police. The police officer
ultimately viewed two videos on the cell phone, one of
which the private parties “had not watched.” Id. at 1332.
Because the government search exposed new information,
not seen by the private party, the Eleventh Circuit concluded
that the government search exceeded the scope of the private
search. 13


    13
       Both the Fifth Circuit and the Seventh Circuit have held that an
individual’s privacy interest in a digital container, such as an email
account, cell phone, or laptop, is entirely frustrated whenever any part of
the container is searched. See United States v. Runyan, 275 F.3d 449, 465
(5th Cir. 2001); Rann v. Atchison, 689 F.3d 832 (7th Cir. 2012). But this
approach is squarely contrary to the Ninth Circuit’s approach to digital
devices, has been undermined by more recent Supreme Court cases about
34                  UNITED STATES V. WILSON

    Conversely, the Fifth and Sixth Circuits recently decided
the issue before us and came to a conclusion contrary to the
one we reach, although the reasoning of the two opinions
diverged. The circumstances in both cases were similar to
those here. See United States v. Reddick, 900 F.3d 636 (5th
Cir. 2018); United States v. Miller, 982 F.3d 412, 427 (6th
Cir. 2020). In both cases, after an electronic service provider
flagged certain email attachments as apparent child
pornography, the attachments were forwarded to a local law
enforcement agency, whose officers viewed the images for
the first time without a warrant.

    The Fifth Circuit held the private search exception
justified the government’s warrantless search because the
government agent’s “visual review of the suspect images . . .

the scope of digital information, and is inconsistent with Jacobsen. For
starters, Tosti did not regard the viewing of some files as sufficient for
purposes of the private search doctrine to show that the government only
invaded a defendant’s privacy interests to the same extent as the private
party. See 733 F.3d at 822. More generally, and dispositively, the Ninth
Circuit has not treated digital devices as unitary, such that a permissible
search of one file or attachment justifies a search of a larger swatch of
digital material. See United States v. Cotterman, 709 F.3d 952 (9th Cir.
2013) (en banc); United States v. Cano, 934 F.3d 1002, 1007 (9th Cir.
2019). Further, Runyan and Rann are in tension with recent Supreme
Court cases, which express concern that given the “immense storage
capacity” of modern technology, the Fourth Amendment will be
undermined unless government searches of digital material are
meaningfully confined in accord with established Fourth Amendment
doctrine. Riley v. California, 573 U.S. 373, 393 (2014); see also
Carpenter v. United States, 138 S. Ct. 2206, 2214 (2018). Finally, if, in
Jacobsen, law enforcement officers had opened and searched not only
the specific containers investigated by the FedEx employees but others
included in the same box, the private search doctrine would not have
applied to the still-sealed containers. There is no basis for ruling
otherwise with regard to unopened digital files. Runyan and Rann were
in our view wrongly decided.
                 UNITED STATES V. WILSON                   35

was akin to the government agents’ decision to conduct
chemical tests on the white powder in Jacobsen,” insofar as
“opening the file merely confirmed that the flagged file was
indeed child pornography, as suspected.” Reddick, 900 F.3d
at 639.

    We cannot accept this analysis for several reasons. First,
and most important, Reddick conflates Jacobsen’s first
holding regarding the private search exception to the Fourth
Amendment with its second holding regarding whether the
field test constituted a search under the Fourth Amendment.
The private search exception excuses a warrantless
government search that would otherwise violate the Fourth
Amendment; the field test determination in Jacobsen, based
on Fourth Amendment law outside the private search
context, was that a warrantless government field drug test
simply does not trigger the Fourth Amendment’s
protections. 466 U.S. at 123–24. In other words, the
warrantless chemical test in Jacobsen was not excused via
the private search exception but for an entirely different
reason—that confirming through a field test that an already
exposed and seized contraband substance was a drug is not
a search for Fourth Amendment purposes. Id. at 122.

    Moreover, in Jacobsen, the white powder was fully
visible to the government officers when they repeated the
steps taken by the FedEx employees to inspect the package.
Not so here, as no human had viewed Wilson’s images
before. The part of Jacobsen that does elucidate the private
search doctrine cannot govern here.

   Notably, we have held that the chemical field test
exception to the Fourth Amendment’s warrant requirement
does not apply to a more complete chemical analysis of a
drug. In United States v. Mulder, 808 F.2d 1346 (9th Cir.
1987), a hotel security officer removed items left behind in
36               UNITED STATES V. WILSON

a hotel room after a guest’s scheduled departure, including
plastic bags full of tablets, and provided them to federal
agents. Id. at 1347. The tablets “were tested at the Western
Regional Laboratory through the use of mass spectrometry,
infrared spectroscopy and gas chromatography.” Id. at 1348.
Mulder distinguished between the chemical field test in
Jacobsen and a laboratory test: “[T]he chemical testing in
this case was not a field test which could merely disclose
whether or not the substance was a particular substance, but
was a series of tests designed to reveal the molecular
structure of a substance and indicate precisely what it is.
Because of the greater sophistication of these tests, they
could have revealed an arguably private fact,” and thus
compromised the defendant’s legitimate privacy interest. Id.
at 1348–49.

    To the extent opening an email attachment to view its
contents is analogous to drug testing at all, it is akin to a
laboratory test with the potential to reveal new private
information, as in Mulder, not a binary field test that yields
either a positive or negative result. Just as a laboratory test
of a suspected drug reveals its precise molecular structure
and so potentially exposes additional private information
like other illicit contaminants or the source of the substance,
so viewing an image of suspected child pornography reveals
innumerable granular private details—for example, the faces
of the people depicted, the setting, and, perhaps, other
speech or conduct also in the frame. Viewing the images
here allowed the government to do more than just confirm
the images’ classification as child pornography, implicating
privacy interests beyond a binary classification. Contrary to
Reddick, the government’s “visual review of the suspect
images” was not analogous to “the government agents’
decision to conduct chemical tests on the white powder in
Jacobsen.” 900 F.3d at 639 (emphasis added).
                 UNITED STATES V. WILSON                    37

    The Sixth Circuit recognized the error in Reddick
concerning the reach of the private search holding in
Jacobsen and “opt[ed] not to rely” on it. Miller, 982 F.3d
at 429. As Miller points out, the government agent’s
“inspection (unlike the [field] test) qualifies as the invasion
of a ‘legitimate privacy interest’ unless Google’s actions had
already frustrated the privacy interest in the files.” Id.

     Miller instead resolved the Fourth Amendment question
it faced by focusing exclusively on the assumed reliability of
Google’s proprietary technology. “At bottom,” Miller
explained, “this case turns on the question whether Google’s
hash-value matching is sufficiently reliable.” Id. at 429–30.
Because the defendant in Miller “never challenged the
reliability of hashing,” id. at 430 (internal brackets and
quotation omitted) (Miller thought the burden was on the
defendant, see id. at 430), Miller deferred to the district
court’s finding “that the technology was ‘highly reliable.’”
Id.

    Wilson, by contrast, did challenge the “accuracy and
reliability” of Google’s hashing technology in the district
court. And, contrary to Miller’s assertion, the government
bears the burden to prove its warrantless search was
permissible, see supra p. 20—a burden it failed to carry.

    Our analysis, however, relies only contingently on the
adequacy of the record with regard to the hash match
technology. In our view, the critical factors in the private
search analysis, both unacknowledged in Miller, include the
personal nature of Fourth Amendment rights and the breadth
of essential information Agent Thompson obtained by
opening the attachment, information—and a privacy
invasion—well beyond what Google communicated to
NCMEC. See supra Parts II.B.1, II.B.2. The reliability of
Google’s proprietary technology, in our estimation, is
38              UNITED STATES V. WILSON

pertinent to whether probable cause could be shown to
obtain a warrant, not to whether the private search doctrine
precludes the need for the warrant.

    And, as the district court noted, and we have noted as
well, the warrant application here contained inadequate
information about Google’s proprietary technology to
establish probable cause without reliance on the descriptions
of the actual images. See supra p. 25.

III.   Conclusion

    “When confronting new concerns wrought by digital
technology, this Court has been careful not to uncritically
extend existing precedents.” Carpenter, 138 S. Ct. at 2222.
The government reports there were 18.4 million CyberTips
in 2018, making it all the more important that we take care
that the automated scanning of email, and the automated
reporting of suspected illegal content, not undermine
individuals’ Fourth Amendment protections.

    Having examined this case with the requisite care, we
hold, for the reasons explained, that Agent Thompson
violated Wilson’s Fourth Amendment right to be free from
unreasonable searches when he examined Wilson’s email
attachments without a warrant. Wilson’s conviction is
vacated, the district court’s denial of Wilson’s motion to
                   UNITED STATES V. WILSON                         39

suppress is reversed, and this case is remanded for further
proceedings. 14




    14
       As noted, the district court concluded that if Agent Thompson’s
warrantless actions constituted an illegal search, no exception “would
prevent operation of the exclusionary rule.” Wilson, 2017 WL 2733879,
at *13. The government did not raise before us any argument to the
contrary, and thus waived any challenge. See United States v. Gamboa-
Cardenas, 508 F.3d 491, 502 (9th Cir. 2007).

```

---

## GROUP: content/cases/United States v. Xiang.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Xiang
type: case
citation: "67 F.4th 895 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 8th Cir. 2023
court_level: coa
circuit: ca8
year: 2023
date_decided: 2023-05-05
docket: 22-1801
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9397097/united-states-v-haitao-xiang/"
  cluster_id: 9397097
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Xiang
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[United States v. Kolsuz]]"
  - "[[Riley v. California]]"
  - "[[United States v. Flores-Montano]]"
tags:
  - case
  - fourth-amendment
  - border-search
  - outbound-search
  - forensic-search
  - electronic-devices
  - economic-espionage
  - eighth-circuit
holding: "The border-search exception applies with equal force to travelers and objects leaving the country, so CBP's warrantless seizure and forensic examination of Haitao Xiang's electronic devices as he departed for China fell within the exception; the court adopted the consensus that a non-routine forensic device search requires reasonable, individualized suspicion but not a warrant or probable cause, and held the officers had reasonable suspicion here, so it affirmed the denial of suppression."
aliases:
  - United States v. Xiang
  - "United States v. Xiang (8th Cir. 2023)"
---

# United States v. Xiang

*67 F.4th 895 (8th Cir. 2023)* (No. 22-1801) · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9397097 → lead opinion 9392573 (Loken, J.; 67 F.4th 895, decided 2023-05-05); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Haitao Xiang, a Chinese citizen who worked for Monsanto in St. Louis, was suspected of stealing a proprietary agricultural algorithm. The day after his company exit interview, he boarded a one-way flight from Chicago's O'Hare International Airport bound for Shanghai, without his family. Alerted by the FBI and Monsanto, U.S. Customs and Border Protection conducted an interview and initial border inspection at O'Hare and seized his cell phone, laptop, SD card, and SIM card as he was leaving the country. The devices were sent to St. Louis, where an FBI Computer Analysis Response Team created forensic images and examined them. Xiang was convicted of economic espionage under 18 U.S.C. § 1831 and moved to suppress the device evidence; the district court, applying the border-search exception, found reasonable suspicion supported the non-routine forensic searches.

## Issue
Whether the warrantless seizure and forensic search of a departing traveler's electronic devices falls within the Fourth Amendment's border-search exception, and if so, whether the officers needed — and had — the requisite suspicion.

## Rule
The border-search exception permits routine searches and seizures at the border without a warrant or probable cause, and — critically here — it "applies with equal force to persons or objects leaving the country," not just those entering. Distinguishing routine from non-routine searches, the Eighth Circuit adopted the cross-circuit consensus that a forensic or "advanced" device search is non-routine and requires reasonable, individualized suspicion (though not probable cause or a warrant): "We think it is an appropriate standard, particularly given the heightened personal privacy interest in electronic devices recognized in Riley." — 67 F.4th 895, slip op. at 8. ^pin-op8

## Application
The court had little difficulty concluding that CBP's seizure and forensic examination of the devices Xiang was carrying abroad was a "border search," rejecting his argument that *[[Riley v. California|Riley]]* — a search-incident-to-arrest case — required a warrant to open electronic devices at a port of entry. It also rejected the contention that the search was untethered to border-search justifications: protecting the nation's economic and trade-secret interests is a legitimate border objective, and the border-search power reaches evidence of crime. The court did not have to decide categorically whether reasonable suspicion is always required for a forensic device search, because it agreed with the district court that the officers had reasonable suspicion — Xiang's abrupt one-way departure, his suspicious searches, his extreme nervousness, and his signed trade-secret obligations supplied particularized, objective facts. The denial of suppression was therefore correct.

## Conclusion
**Affirmed.** Judge Loken wrote for the panel (Smith, C.J., Wollman, and Loken, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Xiang* is a useful **outbound**-border-search anchor: the border-search exception protects departures as well as arrivals, and a forensic examination of seized electronic devices is a **non-routine** border search calling for reasonable suspicion. Like the Fourth Circuit's *[[United States v. Kolsuz|Kolsuz]]*, the court reserved whether reasonable suspicion is strictly *required* for forensic device searches, resolving the case on the ground that suspicion was present. Teach the routine/non-routine line and note the unresolved circuit split on the precise standard for forensic device searches.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Xiang*, 67 F.4th 895 (8th Cir. 2023)](https://www.courtlistener.com/opinion/9397097/united-states-v-haitao-xiang/) — pinpoint: slip op. at 8 (adopting the reasonable-suspicion standard for non-routine forensic border searches of electronic devices; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8705c244fbcb60e6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "67 F.4th 895 (2023)", "court": "8th Cir. 2023", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Xiang", "year": "2023"}}
{"assertion_id": "82c8819ea20a2df9", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key", "title": "United States v. Xiang"}}
{"assertion_id": "97b99d0553394fe8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The border-search exception applies with equal force to travelers and objects leaving the country, so CBP's warrantless seizure and forensic examination of Haitao Xiang's electronic devices as he departed for China fell within the exception; the court adopted the consensus that a non-routine forensic device search requires reasonable, individualized suspicion but not a warrant or probable cause, and held the officers had reasonable suspicion here, so it affirmed the denial of suppression.", "title": "United States v. Xiang"}}
{"assertion_id": "6f74ef5c6a2f0881", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "United States v. Xiang"}}
{"assertion_id": "ad9fb2765232031d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Xiang", "varies_by_point": "false"}}
```

### lake record — United States v. Xiang

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Xiang",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Haitao Xiang",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Xiang",
    "court": "8th Cir. 2023",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": "2023-05-05",
    "year": 2023,
    "docket": "22-1801",
    "cluster_id": 9397097,
    "lead_opinion_id": 9392573,
    "sibling_ids": [],
    "absolute_url": "/opinion/9397097/united-states-v-haitao-xiang/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "67 F.4th 895",
      "volume": "67",
      "reporter": "F.4th",
      "page": "895",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "67 F.4th 895",
        "volume": "67",
        "reporter": "F.4th",
        "page": "895",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "67 F.4th 895",
    "official_selection": {
      "court_class": "state",
      "selected": "67 F.4th 895",
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
    "date_created": "2026-07-06T06:01:10Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-xiang--9397097",
      "to_record_id": "United States v. Xiang",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Xiang

```
               United States Court of Appeals
                          For the Eighth Circuit
                      ___________________________

                              No. 22-1801
                      ___________________________

                           United States of America

                      lllllllllllllllllllllPlaintiff - Appellee

                                         v.

                                  Haitao Xiang

                    lllllllllllllllllllllDefendant - Appellant

                           ------------------------------

       Electronic Frontier Foundation; American Civil Liberties Union;
          Knight First Amendment Institute at Columbia University;
                Reporters Committee for Freedom of the Press

                 lllllllllllllllllllllAmici on Behalf of Appellant
                                      ____________

                  Appeal from United States District Court
                for the Eastern District of Missouri - St. Louis
                                ____________

                         Submitted: January 12, 2023
                            Filed: May 5, 2023
                              ____________

Before SMITH, Chief Judge, WOLLMAN and LOKEN, Circuit Judges.
                             ____________
LOKEN, Circuit Judge.

      “Congress, since the beginning of our Government, has granted the Executive
plenary authority to conduct routine searches and seizures at the border, without
probable cause or a warrant, in order to regulate the collection of duties and to
prevent the introduction of contraband into this country.” United States v. Flores-
Montano, 541 U.S. 149, 153 (2004) (quotation omitted). “[T]he rationale behind this
[border search] exception [to the Fourth Amendment’s warrant requirement] applies
with equal force to persons or objects leaving the country.” United States v. Udofot,
711 F.2d 831, 839 (8th Cir. 1983).

       Haitao Xiang, a citizen of the People’s Republic of China and long-time
resident of the United States, conditionally pleaded guilty to conspiracy to commit
economic espionage in violation of 18 U.S.C. §§ 1831(a)(5).1 He appeals the
conviction and sentence. The principal issue is whether the district court2 erred in
denying Xiang’s motion to suppress evidence obtained by a warrantless seizure and
forensic search of Xiang’s digital devices as he was leaving Chicago’s O’Hare
International Airport, with Shanghai, China his final destination. Applying the
Fourth Amendment border search exception, the district court concluded that U.S.
Customs and Border Protection (“CBP”) officers had reasonable suspicion to conduct
non-routine forensic searches of Xiang’s electronic devices and acted reasonably in
doing so. We agree. We also conclude that Xiang waived his appeal of the $150,000
fine the district court imposed as part of his sentence. Accordingly, we affirm.


      1
        As relevant, the statute is violated by “[w]hoever, intending or knowing that
the offense will benefit any foreign government, foreign instrumentality, or foreign
agent, knowingly” conspires to “steal[], or without authorization . . . carr[y] away . . .
a trade secret.”
      2
        The Honorable Henry E. Autrey, United States District Judge for the Eastern
District of Missouri, adopting the Report and Recommendation of the Honorable John
M. Bodenhausen, United States Magistrate Judge for the Eastern District of Missouri.

                                           -2-
                                  I. Background

       From September 2008 to June 2017, Xiang was employed as an Advanced
Imaging Scientist with Monsanto Co., headquartered in St. Louis, Missouri. On May
25, 2017, Xiang tendered his resignation. On June 5 and June 8, Anne Luther, a
Senior Investigator for Monsanto’s Global Security Team, met with FBI Special
Agent Jaret Depke, who was then assigned to the Foreign Counterintelligence Squad
and was an officer with the Joint Terrorism Task Force at the FBI office in St. Louis.
Luther advised Agent Depke that Xiang was a senior research application engineer
who had been on Monsanto Security’s radar in 2008 for misrepresenting himself as
a University of Illinois student while attempting to acquire information about
hyperspectral imaging technology; that Xiang had submitted his resignation; and that
an exit interview was scheduled for June 9. Depke also talked to others at Monsanto.
He learned that Xiang had “conducted some suspicious Google searches” that
suggested a plan to send company documents to a third party; “sent packets of
information” to a Chinese competitor called NERCITA; and “sent confidential
Monsanto information from his work email to his personal email.” Xiang was also
known to be an associate of a former Monsanto employee named Jiunnren Chen, who
the FBI investigated after he took a job with China National Seed, a Monsanto
competitor; downloaded documents containing trade secrets; and sent emails
containing confidential information from his work account to a personal account.
Xiang was telling people that he planned to work for a potential Monsanto competitor
called Ag-Sensus, a remote-sensing agriculture start-up company with Lei Tian, his
former PhD advisor at the University of Illinois. Agent Depke considered this a
national security investigation involving potential theft of trade secrets.

      On June 8, following his second meeting with Luther, Depke contacted CBP
Officer Art Beck, a fellow member of the Joint Terrorism Task Force and the
Counterintelligence Squad, to discuss what Depke learned from his Monsanto
contacts. Beck ran a check on Xiang, learning he was married with one child residing

                                         -3-
in St. Louis. A travel notification told Beck that Xiang planned to travel to Shanghai
on a one-way ticket without his family on June 10th, the day after his exit interview.
Beck considered this information and the fact that Xiang was leaving Monsanto to
work for a start-up company to be suspicious “red flags.” He decided to subject
Xiang to a CBP inspection at O’Hare Airport on June 10 and advised Agent Depke
of CBP’s inspection, interview, and border search capabilities.3 Beck put in a CBP
“Record Lookout” alerting O’Hare officials that a secondary inspection of electronic
devices might be needed, based on national security concerns such as theft of trade
secrets. See Directive 3340-049, § 5.3, Detention and Review in Continuation of
Border Search of Information. Because the port of entry decides whether to inspect,
Beck advised CBP Officer Swiatek in Chicago of the reasons for Beck’s suspicions
(“the articulables,” as he described them at the suppression hearing).

       After Xiang’s June 9 exit interview, Monsanto personnel told Agent Depke that
Xiang was “extremely nervous” and “sweating” when asked about the suspicious
Google searches. Luther gave Depke a copy of Xiang’s signed termination in which
he agreed he would have no devices, records, data, notes, etc. in his possession that
belonged to Monsanto and would not share confidential information with any third
parties. Monsanto personnel described Xiang as extremely nervous while reviewing


      3
        See CBP Directive 3340-049, Border Searches of Electronic Devices
Containing Information, § 5.1, Border Searches (Aug. 20, 2009). This Directive was
in effect when Xiang’s devices were searched in 2017. CBP issued Directive 3340-
049A in January 2018, which superseded Directive 3340-049. Section 5.1.4 of the
later Directive expressly provides that “an Officer may perform an advanced search
of an electronic device,” which includes forensic searches, if “there is reasonable
suspicion of activity in violation of the laws enforced or administered by CBP, or in
which there is a national security concern.” Directive 3340-049 did not address this
issue. The government has argued to many of our sister circuits that reasonable
suspicion is not required, with mixed results. Our decision in this case is consistent
with the current Directive. We need not decide whether reasonable suspicion was
required under the prior Directive, on which there is circuit conflict.

                                         -4-
those provisions and assessed him as “blatantly deceptive.” Monsanto provided
Depke a copy of Xiang’s “suspicious Google searches” that included searches for
“company information to the third party,” “I don’t want it to be an evidence,” and “as
evidence to accuse me.”

      Xiang rented a car in St. Louis on June 9 and drove to Chicago. At O’Hare on
June 10, CBP Agents conducted an interview and initial border search of Xiang’s
checked and carry-on baggage prior to his flight. Based on the interview and prior
information, CBP seized a cell phone, laptop computer, SD card, and a SIM card from
Xian’s baggage for a secondary inspection. Xiang boarded his flight and left. Officer
Swiatek took custody of the seized devices and advised Officer Beck of the seizure.
Beck alerted FBI Agent Depke. Because Monsanto’s trade secret personnel are in St.
Louis and Depke had an established relationship with Monsanto, Depke had “a better
chance of quickly and expediently identifying anything that would be of interest or
potentially identified as that company’s trade secrets.” Therefore, exercising
Chicago’s extended CBP border search authority, Beck had the devices sent to St.
Louis for “subject matter expertise review” by an assisting federal agency. See
Directive 3340-049, § 5.3.2.3.

       Depke received the devices on June 13. The FBI Chief Division Counsel
confirmed that Depke could, within the authority of CBP, review the electronic
devices. The devices were opened and examined by a Computer Analysis Response
Team (“CART”) on June 14, 2017. CART created forensic images, and Depke began
a preliminary search on June 20. He identified six documents believed to be
Monsanto trade secrets or intellectual property, which Monsanto confirmed that day
or on June 21. At that point, CBP transferred its seizing authority to the FBI. See
Directive 3340-049, § 5.4.2.3. On July 27, the FBI applied for and obtained a warrant
to search the electronic devices.




                                         -5-
                           II. Motion to Suppress Issues

       After the district court denied his motion to suppress, Xiang entered a
conditional plea of guilty, reserving the right to appeal that ruling. See Fed. R. Crim.
P. 11(a)(2). When reviewing the denial of a motion to suppress, we review findings
of fact for clear error and conclusions of law de novo. See United States v. Taylor,
519 F.3d 832, 833 (8th Cir. 2008) (standard of review).

       A. Xiang’s primary argument on appeal is that the government needed a
warrant to search his electronic devices “because the forensic search did not fall
within the Fourth Amendment border search exception,” and therefore the general
rule applies that, “[i]n the absence of a warrant, a search is reasonable only if it falls
within a specific exception to the warrant requirement.” See Riley v. California, 573
U.S. 373, 382 (2014). As the opening paragraph of this opinion hopefully makes
clear, it blinks at reality to assert that CBP’s seizure and search of the electronic
devices Xiang was about to carry abroad was not a “border search” of the type
conducted by the Executive throughout our nation’s history. Xiang’s argument is that
“electronic devices are different,” as the Supreme Court recognized in Riley, and
therefore the government must get a warrant to even open them up at a port of entry,
when all other property is subject to “routine searches and seizures at the border,
without probable cause or a warrant.” Flores-Montano, 541 U.S. at 153. Riley
involved a different Fourth Amendment exception, searches incident to arrest. No
Circuit has held that the government must obtain a warrant to conduct a routine
border search of electronic devices. The First Circuit carefully explained why
Xiang’s broad argument “rests on a misapprehension of the applicability” of Riley.
Alasaad v. Mayorkas, 988 F.3d 8, 16-19 (1st Cir. 2021); see United States v.
Wanjiku, 919 F.3d 472, 484-85 (7th Cir. 2019). We agree.

      Xiang further argues that the search of his electronic devices was outside the
scope of the border search exception because it was “not tethered to any border search

                                           -6-
justifications.” The Ninth Circuit has stated that “[a] border search must be
conducted to enforce importation laws, and not for general law enforcement
purposes.” United States v. Cano, 934 F.3d 1002, 1013 (9th Cir. 2019) (quotation
omitted); see United States v. Aigbekaen, 943 F.3d 713, 721 (4th Cir. 2019).
Conversely, the Second Circuit has stated, more sensibly in our view, that CBP
officers “have the authority to search and review a traveler’s documents and other
items at the border when they reasonably suspect that the traveler is engaged in
criminal activity, even if the crime falls outside the primary scope of their official
duties.” United States v. Levy, 803 F.3d 120, 124 (2d Cir. 2015). But regardless of
whether there is any limitation on using border searches “to investigate general
criminal wrongdoing,” the assertion that the search of Xiang’s electronic devices was
“not tethered to any border search justifications” is absurd. Congress passed the
Economic Espionage Act of 1996 because:

      There can be no question that the development of proprietary economic
      information is an integral part of America’s economic well-being.
      Moreover, the nation’s economic interests are a part of its national
      security interests. Thus, threats to the nation’s economic interest are
      threats to the nation’s vital security interests.

H.R. Rep. No. 104-788, at 4 (1996), as reprinted in 1996 U.S.C.C.A.N. 4021, 4023;
see United States v. Hsu, 155 F.3d 189, 194-95 (3d Cir. 1998).

       Xiang’s additional assertion that the Fourth Amendment does not permit border
searches for mere evidence of criminal activity was rejected by the Supreme Court
over fifty years ago, see Warden v. Hayden, 387 U.S. 294, 300-02 (1967), and more
recently by circuit courts in this context, see Alasaad, 988 F.3d at 20.

       The real issue in this case is not whether the border search exception applies,
but whether the extended border search conducted by CBP officers, with technical
assistance from the FBI and Monsanto, is consistent with the Fourth Amendment’s

                                         -7-
overriding purpose to protect “against unreasonable searches and seizures.” In
United States v. Montoya de Hernandez, the Supreme Court held that when a routine
border search becomes non-routine -- in that case, the 16-hour detention of an
arriving traveler -- “customs agents, considering all the facts surrounding the traveler
and her trip, [must] reasonably suspect that the traveler is smuggling contraband in
her alimentary canal.” 473 U.S. 531, 541 (1985).

       Many of our sister circuits have distinguished between “routine” and “non-
routine” border searches of electronic devices. Most have concluded that a seizure
at the port of entry, followed by a forensic or “advanced” search, particularly if time
consuming and conducted away from the port of entry, becomes a non-routine border
searches requiring some level of reasonable, individualized suspicion, but not
probable cause or a warrant.4 As discussed, see note 3 supra, Directive 3340-049A
adopted this fact-intensive approach. We think it is an appropriate standard,
particularly given the heightened personal privacy interest in electronic devices
recognized in Riley. But like the Seventh Circuit in Wanjiku, we need not decide
today whether reasonable suspicion is required for an advanced or forensic border
search of electronic devices because we agree with the district court that CBP officers
had reasonable suspicion for the forensic search they conducted.

       B. Xiang argues that, if the border search exception does apply, the CBP
officers lacked the requisite reasonable suspicion. “Reasonable suspicion exists when
an officer is aware of particularized, objective facts which, taken together with


      4
        Compare Alasaad, 988 F.3d at 13 (1st Cir. 2021); United States v. Kolsuz, 890
F.3d 133, 144 (4th Cir. 2018); and United States v. Cotterman, 709 F.3d 952, 967-68
(9th Cir. 2013) (en banc), with United States v. Touset, 890 F.3d 1227, 1233 (11th
Cir. 2018) (reasonable suspicion not required for personal property including
electronic devices), and Wanjiku, 919 F.3d at 489 (7th Cir. 2019) (declining to reach
the issue).


                                          -8-
rational inferences from those facts, reasonably warrant suspicion that a crime is
being committed.” United States v. Tamayo-Baez, 820 F.3d 308, 312 (8th Cir. 2016)
(quotation omitted). We must review “the totality of the circumstances of each case
to see whether the detaining officer has a particularized and objective basis for
suspecting legal wrongdoing.” United States v. Arvizu, 534 U.S. 266, 273 (2002)
(quotation omitted).

      When CBP Officers seized Xiang’s devices at O’Hare Airport, officers were
aware of the following information: Xiang resigned from his position as a Monsanto
imaging scientist the day before; he was leaving the country without his family on a
one-way trip to China and then planned to work for an agricultural start-up company;
Monsanto personnel were concerned about Xiang stealing trade secrets -- he had
conducted suspicious Google searches and was visibly nervous when asked about the
searches during his exit interview; he had transferred unknown company information
from his company email account to a personal email account and appeared nervous
and deceptive when signing a termination contract that barred him from sharing
Monsanto trade secrets and confidential information with others; previously, Xiang
associated with a former colleague who downloaded and transmitted confidential
Monsanto documents to a personal email account before leaving to work for a
Chinese competitor; Xiang had sent packets of unknown information to a Chinese
competitor, NERCITA; and Monsanto’s security team believed that Xiang, as a new
Monsanto employee in 2008, misrepresented himself as a University of Illinois
student in an attempt to acquire information about an imaging company named
SpecTIR.

       Xiang argues that this gave CBP officers no reasonable suspicion he was
engaged in even a violation of company policy, much less economic espionage or
criminal theft of trade secrets. They did not know what “packets of information” he
sent to NERCITA. Sending emails from his work account to a personal account does
not point to criminal activity. There was no evidence he was involved in coworker

                                        -9-
Chen’s wrongdoing. The Google searches were stale evidence -- over a year prior to
the seizure of his electronic devices. Resigning and traveling to visit his family in
China are not indicative of any criminal wrongdoing. The agents’ “background” on
the “trend” of Chinese trade are “profiling” that provides little to no value, nothing
more than “unparticularized suspicion or hunch.”

       We agree with the district court that this argument is contrary to well-
established Fourth Amendment principles. “The totality-of-the-circumstances test
precludes this sort of divide-and-conquer analysis.” United States v. Quinn, 812 F.3d
694, 698 (8th Cir. 2016) (quotation omitted). Even though “each of these
[suspicious] factors alone is susceptible of innocent explanation, and some factors are
more probative than others[,] . . . together . . . they sufficed to form a particularized
and objective basis.” Arvizu, 534 U.S. at 277. The officers and agents had
background information, much of it corroborated, that provided a basis for assessing
Xiang’s actions in May and June 2017. Their experience and training in international
economic espionage and theft of trade secrets gave them reasonable suspicion for an
extended border search that included a forensic search of electronic devices.

       C. Finally, Xiang argues the search of his devices was constitutionally
unreasonable because it was akin to an “invasive rummage,” violated CBP policies,
was unreasonable in duration, and CBP calling on the FBI for subject matter expertise
was pretextual. These contentions require little discussion. The “rummaging” cases
on which Xiang relies -- Kremen v. United States, 353 U.S. 346, 347-48 (1957) and
Go-Bart Importing Co. v. United States, 282 U.S. 344, 358 (1931) -- bear no
resemblance to the focused search of electronic devices in this case. If law
enforcement officers have reasonable suspicion to search a container, such as a
backpack, briefcase, or electronic device, they have not conducted an unconstitutional
“rummaging” if they find the contraband at issue at the bottom of the backpack,
underneath lots of innocent items they did not seize or further search. As presented,
the argument is frivolous.

                                          -10-
       Xiang’s other arguments are likewise without merit. We agree with the district
court that “exclusion based on a failure to follow regulatory procedure is only
warranted if (1) the procedure is mandated by the Constitution or (2) the defendants
reasonably relied on the procedure in governing his conduct.” United States v. Xiang,
No. 4:19CR980, 2021 WL 4810556 at *3 (E.D. Mo. Oct. 15, 2021), citing United
States v. Caceres, 440 U.S. 741, 749-53 (1979). There was no such showing here.
Xiang’s argument that the CBP search was “a pre-textual search . . . to gather
evidence for SA Depke’s investigation” disregards Officer Beck’s credited testimony
that his actions were taken in exercise of CBP border search authority; the express
authorization for interagency cooperation and sharing of information in Directive
3340-049, § 5.4; and the common sense reality that there is nothing “pretextual”
about members of an interagency Counterintelligence Squad working together to
ferret out economic espionage and international trade secret theft that violates 18
U.S.C. § 1831(a).

       Finally, as we have explained, the record demonstrates why, after Xiang’s
devices were retained for extended inspection, it took time to send the devices to St.
Louis, where FBI Agent Depke could most efficiently conduct the search, and
Monsanto’s trade secrets security professionals could then confirm that the devices
contained trade secrets and proprietary information. During the interim, neither
Xiang nor anyone acting on his behalf asked that the devices be returned, or even
inquired about them. Thus, the extended seizure “did not meaningfully interfere with
his possessory interests,” United States v. Clutter, 674 F.3d 980, 984 (8th Cir.), cert.
denied, 133 S. Ct. 272 (2012), and CBP was obligated to “appropriately safeguard
information retained, copied, or seized under this Directive and during transmission
to another federal agency.” Directive 3340-049, § 5.4.1.5. The search was not
constitutionally unreasonable.




                                         -11-
                             III. Imposition of a Fine

       In his plea agreement, Xiang “waive[d] all rights to appeal all sentencing
issues” except for those explicitly preserved -- the district court’s determination of
the applicable guidelines and Xiang’s criminal history and the substantive
reasonableness of any sentence above the guidelines sentencing or fine range.
Xiang’s PSR stated that he has “the ability to pay a fine” and calculated his advisory
guidelines range as 10-16 months imprisonment, one to three years supervised
release, and a fine of $55,000.00 to $5,000,000.00. At sentencing, Xiang renewed his
objection to the PSR’s restitution recommendation. The district court imposed an
above-range sentence of twenty-nine months’ imprisonment, imposed a $150,000
fine, and held “in abeyance its judgment on restitution.” Xiang did not object to the
fine.

       Xiang appeals imposition of the $150,000 fine, arguing “the district court made
no factual findings.” He does not challenge the substantive reasonableness of the
fine, only the imposition of a fine without factual findings. This is an alleged
procedural error he waived in his plea agreement. Moreover, as he did not object at
sentencing, the challenge is not only waived but forfeited and may only be reviewed
for plain error. See United States v. Wohlman, 651 F.3d 878, 886 (8th Cir. 2011).
The district court did not err, much less plainly err in imposing a $150,000 fine.

      The judgment of the district court is affirmed.
                     ______________________________




                                        -12-

```

---
