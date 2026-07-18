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

## GROUP: content/cases/United States v. Perez.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Perez
type: case
citation: "89 F.4th 247 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 1st Cir.
court_level: coa
circuit: ca1
year: 2023
date_decided: 2023-12-28
docket: 22-1121
authority_weight: "Binding in-circuit — 1st Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9456060/united-states-v-perez/"
  cluster_id: 9456060
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Perez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[SIA Vehicles]]"
    role: "Lower-court development (role-based)"
related:
  - "[[SIA Vehicles]]"
  - "[[Arizona v. Gant]]"
  - "[[Riley v. California]]"
  - "[[Chimel v. California]]"
tags:
  - case
  - fourth-amendment
  - search-incident-to-arrest
  - grabbing-area
  - container-search
  - backpack
  - first-circuit
holding: "The search-incident-to-arrest exception permits a warrantless search of an arrestee's nearby container, and the First Circuit's decision in United States v. Eatherton — upholding such a search of a bag within an arrestee's reach — retains controlling force notwithstanding the Supreme Court's intervening decisions in Gant and Riley, so the warrantless search of Perez's backpack incident to his arrest did not violate the Fourth Amendment and his conviction was affirmed."
aliases:
  - United States v. Perez
  - "United States v. Perez (1st Cir. 2023)"
---

# United States v. Perez

*89 F.4th 247 (1st Cir. 2023)* (No. 22-1121) · U.S. Court of Appeals for the First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9456060 → lead opinion 9913885 (Barron, C.J.; 89 F.4th 247, decided 2023-12-28); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Gilbert Perez was convicted of a federal drug offense in the District of Maine after the district court denied his motion to suppress the fruits of a warrantless search of his backpack, which officers searched incident to his arrest. The district court rested its ruling on *United States v. Eatherton*, a First Circuit decision upholding a similar warrantless search of a bag within an arrestee's reach under the search-incident-to-arrest exception. On appeal, Perez argued that intervening Supreme Court decisions — *[[Arizona v. Gant]]* and *[[Riley v. California]]* — had stripped *Eatherton* of its controlling force.

## Issue
Whether the First Circuit's search-incident-to-arrest rule permitting the warrantless search of an arrestee's nearby bag, as applied in *Eatherton*, survives the Supreme Court's decisions in *[[Arizona v. Gant|Gant]]* and *[[Riley v. California|Riley]]*.

## Rule
The search-incident-to-arrest exception allows officers, without a warrant, to search the arrestee's person and the area within his immediate control, including containers such as a bag found there; *Eatherton* applied that rule to an arrestee's nearby bag, and the panel held it remains good law after *[[Arizona v. Gant|Gant]]* and *[[Riley v. California|Riley]]*: "Because we conclude that *Eatherton* controls here, we need not evaluate the search of Perez's backpack under *Maldonaldo-Espinosa*." — 89 F.4th 247, slip op. at 17. ^pin-op17

## Application
Perez's core contention was that *[[Arizona v. Gant|Gant]]* (which cabined vehicle [[Search Incident to Arrest|searches incident to arrest]] to circumstances where the arrestee can access the passenger compartment or the vehicle may contain evidence of the offense) and *[[Riley v. California|Riley]]* (which required a warrant to search a cell phone seized incident to arrest) had eroded *Eatherton*'s allowance for a warrantless search of an arrestee's bag. The court disagreed: *[[Arizona v. Gant|Gant]]* addressed the distinct automobile context, and *[[Riley v. California|Riley]]* turned on the unique privacy interests in the vast digital contents of a modern cell phone, not on physical containers generally. Neither displaced *Eatherton*'s rule for a bag within an arrestee's grabbing area. Because *Eatherton* controlled, the panel did not need to reach the government's alternative ground, and the warrantless backpack search was lawful.

## Conclusion
**Affirmed.** Chief Judge Barron wrote for the panel (Barron, C.J., Howard, and Montecalvo, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Perez* is a useful post-*[[Riley v. California|Riley]]* boundary marker for **[[Search Incident to Arrest|search incident to arrest]]**: it confirms that the *[[Chimel v. California|Chimel]]* grabbing-area rule still authorizes the warrantless search of an arrestee's nearby **physical container**, and that *[[Arizona v. Gant|Gant]]* (vehicles) and *[[Riley v. California|Riley]]* (cell phones) did not silently overrule that allowance. Teach it to keep students from over-reading *[[Riley v. California|Riley]]* into a general container rule.

## Appears on
- [[SIA Vehicles]] — *Lower-court development (role-based)*

## Sources
- [*United States v. Perez*, 89 F.4th 247 (1st Cir. 2023)](https://www.courtlistener.com/opinion/9456060/united-states-v-perez/) — pinpoint: slip op. at 17 (*Eatherton*'s search-incident-to-arrest rule for an arrestee's bag survives *Gant* and *Riley*; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "08a951ec9c4ae8fa", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "89 F.4th 247 (2023)", "court": "1st Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Perez", "year": "2023"}}
{"assertion_id": "1bcea861a515fe02", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The search-incident-to-arrest exception permits a warrantless search of an arrestee's nearby container, and the First Circuit's decision in United States v. Eatherton — upholding such a search of a bag within an arrestee's reach — retains controlling force notwithstanding the Supreme Court's intervening decisions in Gant and Riley, so the warrantless search of Perez's backpack incident to his arrest did not violate the Fourth Amendment and his conviction was affirmed.", "title": "United States v. Perez"}}
{"assertion_id": "4e910fed549e22d9", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Vehicles"}, "payload": {"home": "SIA Vehicles", "role": "Lower-court development (role-based)", "title": "United States v. Perez"}}
{"assertion_id": "146b57dcdd8c7be9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 1st Cir.", "title": "United States v. Perez"}}
{"assertion_id": "d35d212ef4805eaa", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Perez", "varies_by_point": "false"}}
```

### lake record — United States v. Perez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Perez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Perez",
    "case_name_short": "Perez",
    "case_name_full": "",
    "input_case_name": "United States v. Perez",
    "court": "1st Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": "2023-12-28",
    "year": 2023,
    "docket": "22-1121",
    "cluster_id": 9456060,
    "lead_opinion_id": 9913885,
    "sibling_ids": [],
    "absolute_url": "/opinion/9456060/united-states-v-perez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "89 F.4th 247",
      "volume": "89",
      "reporter": "F.4th",
      "page": "247",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "89 F.4th 247",
        "volume": "89",
        "reporter": "F.4th",
        "page": "247",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "89 F.4th 247",
    "official_selection": {
      "court_class": "coa",
      "selected": "89 F.4th 247",
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
    "date_created": "2026-07-07T01:40:20Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-perez--9456060",
      "to_record_id": "United States v. Perez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Perez

```
          United States Court of Appeals
                      For the First Circuit

No. 22-1121

                          UNITED STATES,

                            Appellee,

                                v.

                          GILBERT PEREZ,

                      Defendant, Appellant.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                    FOR THE DISTRICT OF MAINE

          [Hon. D. Brock Hornby, U.S. District Judge]


                              Before

                       Barron, Chief Judge,
              Howard and Montecalvo, Circuit Judges.


     Jamesa J. Drake, with whom Drake Law LLC was on brief, for
appellant.
     Brian S. Kleinbord, Assistant United States Attorney, with
whom Darcie N. McElwee, United States Attorney, was on brief, for
appellee.



                        December 28, 2023
          BARRON, Chief Judge.      Gilbert Perez seeks to vacate his

federal drug conviction on the ground that the United States

District Court for the District of Maine wrongly denied his motion

to suppress the fruits of a warrantless search of his backpack.

The District Court rested the denial on our decision in United

States v. Eatherton, 519 F.2d 603 (1st Cir. 1975), which upheld a

similar warrantless search under the search-incident-to-arrest

exception to the warrant requirement of the Fourth Amendment to

the U.S. Constitution, id. at 609-11.        Because we reject Perez's

contention that intervening decisions of the Supreme Court of the

United States have stripped Eatherton of controlling force, we

affirm the judgment of conviction.

                                    I.

          When   reviewing   the    denial   of   a   motion   to   suppress

evidence, "'we recite the facts as found by the district court,

consistent with record support,' including the testimony from the

motion hearing."   United States v. Tom, 988 F.3d 95, 97 (1st Cir.

2021) (quoting United States v. Soares, 521 F.3d 117, 118 (1st

Cir. 2008) (cleaned up)). Massachusetts State Trooper Jason Conant

was conducting a patrol on the evening of August 30, 2019, when he

saw a pickup truck with Maine license plates stop in a McDonald's




                                   - 2 -
parking lot in Lawrence, Massachusetts.            The driver was later

identified as Perez.

            Perez exited the truck, donned a backpack, and walked

towards a residential area near the parking lot.             Conant became

suspicious of the out-of-state truck, as well as Perez's behavior,

and alerted other state troopers in the area to watch for Perez.

            Minutes after Perez left the parking lot, a second

Massachusetts state trooper, Shawn McIntyre, saw Perez exiting a

taxi on a nearby street.       McIntyre watched Perez start to walk in

the direction of the McDonald's where the truck was parked.

            McIntyre stopped the taxi and saw large quantities of

cash at the feet of the taxi's passenger.          McIntyre then radioed

Conant, informing him of the cash and the suspicion that Perez had

participated in a drug transaction with the taxi's passenger.

            Perez,    still   wearing   the   backpack,   returned   to   the

McDonald's parking lot.       Conant pulled his (unmarked) car into the

parking lot and exited the car.          Roughly simultaneously, Conant

began to yell "state police," and Perez began to run from the

parking lot.    Conant gave chase.

            About twenty yards from the parking lot, Perez tripped

and fell.   Conant caught up to Perez after his fall and pinned him

to the ground.       A third state trooper, Ryan Dolan, pulled up in a

patrol car.




                                   - 3 -
          Conant removed the backpack from Perez as Dolan was

handcuffing Perez's hands behind his back.         Dolan then sat Perez

on the pavement.

          After Perez was handcuffed, Conant placed the backpack

on Dolan's car and opened and searched the backpack.           Perez was

not in reaching distance of the backpack when the search of the

backpack took place.

          Conant discovered fentanyl and cocaine in the backpack.

Perez was then searched and formally arrested.

          Perez was indicted on March 12, 2020, on a federal

drug-related charge.       He moved to suppress the drugs, contending

that the backpack's search violated the Fourth Amendment.1

          The government opposed the motion on the ground that the

search was constitutional under Eatherton.         The government also

argued that, in any event, the search was conducted in good-faith

reliance on Eatherton.      See Davis v. United States, 564 U.S. 229,

232   (2011)    (holding    that   "[police]   searches    conducted   in

objectively reasonable reliance on binding appellate precedent are

not subject to the exclusionary rule").

          The    District    Court   denied    Perez's    motion   without

reaching the good-faith issue.       See United States v. Perez, Crim.

No. 2:20-CR-39-DBH-01, 2021 WL 2953671 (D. Me. July 14, 2021).


      1Perez challenged several other aspects of his arrest in the
District Court but raises none of those issues on appeal.


                                   - 4 -
The District Court found that "[t]he police had probable cause to

arrest Perez when they handcuffed him," and it "treat[ed] [the

police] as having effectively arrested him then," although the

District Court also found that it was only later that Perez was

"formally" arrested.   Id. at *2.     The District Court separately

found, moreover, that Perez's handcuffing occurred "as" Conan

"ripped the backpack off" of Perez.        Id.   With that factual

predicate in place, the District Court reasoned that the search of

the backpack was lawful because, when there is probable cause for

an arrest, Eatherton allows for the warrantless "search [of] a

container found on a person being arrested," id. at *3, and our

Court had not "'unmistakably' cast Eatherton 'into disrepute,'"

id. at *4 (quoting Eulitt ex rel. Eulitt v. Me., Dep’t of Educ.,

386 F.3d 344, 349 (1st Cir. 2004)).

          Perez entered a conditional guilty plea, which preserved

his right to appeal his conviction based on the District Court's

Eatherton-based denial of his motion to suppress.     He then filed

this timely appeal.    We review the District Court's "factual

findings for 'clear error'" and its "legal conclusions . . . de

novo."   United States v. Rodríguez-Pacheco, 948 F.3d 1, 6 (1st

Cir. 2020) (quoting United States v. Camacho, 661 F.3d 718, 723-

24 (1st Cir. 2011)).




                              - 5 -
                                       II.

             The Fourth Amendment protects "[t]he right of the people

to be secure in their persons, houses, papers, and effects, against

unreasonable       searches      and    seizures"       by    providing      that

"no Warrants shall issue, but upon probable cause."                   U.S. Const.

amend. IV.    Our focus is on the exception to the Fourth Amendment's

warrant requirement for a search incident to an arrest. See United

States v. Robinson, 414 U.S. 218 (1973).

             Perez does not dispute that the exception covers his

backpack's search if Eatherton remains good law.              He contends only

that   Eatherton    does   not    because      of   either   United    States   v.

Chadwick, 433 U.S. 1 (1977), or Arizona v. Gant, 556 U.S. 332

(2009), or both together.

             Under the law of the circuit doctrine, newly constituted

panels must follow the rulings of preceding panels that are

"directly (or even closely) on point," United States v. Guzman,

419 F.3d 27, 31 (1st Cir. 2005), "even where the succeeding panel

disagrees with the prior one," United States v. Guerrero, 19 F.4th

547, 552 (1st. Cir 2021).         The doctrine recognizes an exception,

however, when "[a]n existing panel decision [is] undermined by

controlling authority, subsequently announced, such as an opinion

of the Supreme Court, an en banc opinion of the circuit court, or

a statutory overruling," Williams v. Ashland Eng'g Co., 45 F.3d

588, 592 (1st Cir. 1995), or when an "authority that postdates the


                                       - 6 -
original decision, although not directly controlling, nevertheless

offers a sound reason for believing that the former panel, in light

of fresh developments, would change its collective mind," United

States v. Barbosa, 896 F.3d 60, 74 (1st Cir. 2018) (quoting

Williams, 45 F.3d at 592).

            The latter exception is very limited, as it applies only

when the new authority "provides a clear and convincing basis" to

conclude    that    the   prior   panel    would    have   changed   its   mind.

Guerrero, 19 F.4th at 552.          For that reason, we have described

cases that trigger this exception as "hen's-teeth-rare."               San Juan

Cable LLC v. P.R. Tel. Co., 612 F.3d 25, 33 (1st Cir. 2010).

            We    begin   by   reviewing   Eatherton       and   describing   its

rationale.       We then explain why we conclude that Eatherton still

controls.

                                      A.

            The defendant in Eatherton was Gilbert Eatherton.                 519

F.2d. at 605.        A suspected bank robber, he was walking down a

street while carrying a briefcase when agents of the Federal Bureau

of Investigation ("FBI") spotted him.              Id. at 609.

            The FBI agents called for Eatherton to come to their

car, and he did so.        Id.    When he was "close to the vehicle the

agents told him he was under arrest [and] instructed him to drop

the briefcase and [lie] spread eagle on the ground."                    Id.    He

complied with the commands, and the FBI agents "thoroughly frisked"


                                    - 7 -
him, handcuffed him, and placed him in the back of their vehicle.

Id.    The FBI agents then picked up the briefcase, opened it, and

found a loaded gun and three brown ski masks, all of which were

later admitted as evidence at trial.     Id.

           Eatherton did not dispute that there was probable cause

to arrest him, and he "concede[d] that the agents could have seized

the briefcase consonant with the [F]ourth [A]mendment."      Id. at

610.   But he argued that the agents "should have obtained a search

warrant before investigating [the briefcase's] contents," and

that, because the agents did not, the search of his briefcase

violated the Fourth Amendment.    Id. He thus argued that the fruits

of the search of the briefcase had to be suppressed because that

search could not be justified merely by the fact of his arrest and

the right to search his person that his arrest entailed.    Id.

           Eatherton relied chiefly on the Supreme Court's decision

in Chimel v. California, 395 U.S. 752 (1969).      There, the Court

held that the bare fact that an arrest occurred inside a home did

not justify a warrantless search of the entirety of the premises.

Id. at 763. The Court also held that although a warrantless search

of the area of the home within the "immediate control" of the

arrestee was reasonable if justified "by the need to seize weapons

and other things which might be used to assault an officer or

effect an escape" or "by the need to prevent the destruction of

evidence of the crime," these "justifications are absent where a


                                 - 8 -
search is remote in time or place from the arrest."      Id. at 764

(quoting Preston v. United States, 376 U.S. 364, 367 (1964)).

           Eatherton argued based on Chimel that the briefcase's

search violated the Fourth Amendment because "any urgency to

inspect the interior of the briefcase was completely removed once

he had been subdued and the [brief]case removed from his possession

and beyond his possible reach."    Eatherton, 519 F.2d at 610.   But,

although the Eatherton panel acknowledged that there was "some

logical cogency" to the contention, id., the panel held that the

search of the briefcase's interior was reasonable.

           The Eatherton panel first pointed out that Chimel had

cited "with apparent approval Draper v. United States, in which a

search virtually identical to that at issue [in Eatherton] was

upheld."   Id. (citation omitted).       Draper involved a criminal

defendant who had evidence admitted against him at his trial that

was obtained from the warrantless search of a bag that he was

carrying when he was arrested.    358 U.S. 307, 310 (1959).

           The Eatherton panel next explained that other courts of

appeals "had little apparent difficulty" rejecting Chimel-based

arguments for prohibiting warrantless "searches identical to that

contested" by Eatherton.   519 F.2d at 610.     Notably, in each of

those cases, as in Draper, the warrantlessly-searched container

was similar in size to the briefcase in Eatherton.       See United

States v. Maynard, 439 F.2d 1086, 1087 (9th Cir. 1971) (rejecting


                                 - 9 -
the argument that a warrantless search of a suitcase the defendant

was carrying when arrested was unconstitutional because the search

was "incident to the lawful arrest of its carrier"); United States

v. Mehciz, 437 F.2d 145, 146-48 (9th Cir. 1971) (relying on Draper

to reject the contention that Chimel governed a warrantless search

of a suitcase carried at the time of arrest); United States ex

rel. Muhammad v. Mancusi, 432 F.2d 1046, 1047-48 (2d Cir. 1970)

(rejecting     as   "frivolous"   a   Chimel-based   challenge   to   the

post-arrest search at a police station of a briefcase in the

"immediate possession" of the defendant at the time of the arrest

when the defendant conceded that the search "would have been proper

if [it] had been conducted at the time [and place] of his arrest").

          The Eatherton panel then addressed three Supreme Court

decisions that post-dated both Chimel and the other circuits'

rulings that had upheld searches like the search of Eatherton's

briefcase: Robinson, 414 U.S. at 218; Gustafson v. Florida, 414

U.S. 260 (1973); and United States v. Edwards, 415 U.S. 800 (1974).

The Eatherton panel explained that this trio showed that the

Chimel-based challenge could not "be sustained."         Eatherton, 519

F.2d at 610.

          In Robinson, the Court held that the warrantless search

of a "crumpled up cigarette package" found in the "breast pocket

of the heavy coat [the arrestee] was wearing" at the time of his

arrest did not violate the Fourth Amendment, even though the


                                  - 10 -
arresting   officer    had   neither    "any     subjective   fear   of   the

[arrestee]" or any "susp[icion] that the [arrestee] was armed."

414 U.S. at 222-23, 236.         The Court explained that because the

"custodial arrest of a suspect based on probable cause is a

reasonable intrusion under the Fourth Amendment[,]" a search "of

the person" of an arrestee incident to that arrest is per se

reasonable.    Id. at 235.     Robinson thus rejected the contention

that a more limited pat-down -- such as the limited frisk permitted

in Terry v. Ohio, 392 U.S. 1 (1968) -- was all that was allowed

for a search incident to the arrest.             See Robinson, 414 U.S. at

235.   And the Court then explained that "[h]aving in the course of

a lawful search come upon the crumpled package of cigarettes, [the

officer who had conducted the search of the arrestee's person] was

entitled to inspect [the package,] and when his inspection revealed

the heroin capsules, he was entitled to seize them as 'fruits,

instrumentalities, or contraband' probative of criminal conduct."

Id. at 236 (quoting Harris v. United States, 331 U.S. 145, 154-55

(1947)).

            Robinson    relied     on      the     rationales    for      the

search-incident-to-arrest exception to the warrant requirement to

justify the ruling that the warrantless search of the cigarette

package was reasonable.      Those rationales are rooted in a concern

for officer safety, the governmental interest in the preservation

of evidence, and the diminished privacy interest of an arrestee


                                  - 11 -
due to the dominion over their person effected by the arrest

itself.     See   Robinson,    414    U.S.     at     226;    see     also    Riley   v.

California, 573 U.S. 373, 386 (2014) ("Robinson regarded any

privacy   interests     retained     by   an   individual           after    arrest   as

significantly diminished by the fact of the arrest itself.").

            In Gustafson, which was decided the same day as Robinson,

the Court went a step further than it had in Robinson.                         It held

that a warrantless search of a cigarette box found in the "front

coat pocket of the coat [the arrestee] was wearing" during a search

of the arrestee's person at the time of his arrest, 414 U.S. at

262, was per se reasonable under Robinson even though the search

of the cigarette box occurred after the arrestee had been placed

"in the back seat of the squad car," id. at 262 n.2, and even

though    there   was   no   "subjective       fear    of     the    [arrestee]"      or

"susp[icion] that the [arrestee] was armed," id. at 266.

            The defendant in Eatherton tried to distinguish Robinson

and Gustafson based on the relatively large size of his briefcase

and the fact that it was not concealed in his pocket but held in

his hand at the time of the arrest.                   But the Eatherton panel

concluded that "[t]he line which [Eatherton] attempts to draw

placing the briefcase beyond the search of his 'person' which

Robinson and Gustafson expressly approve is one requiring gossamer

distinctions."     Eatherton, 519 F.2d at 610.               And Eatherton went on

to state that "[t]here is no indication that the result in those


                                     - 12 -
cases would have been any different had the cigarette packages

been in the defendants' hands rather than in their pockets or if

they had been dropped to the ground in response to [a] police

command." Id. Moreover, Eatherton explained, "[w]hile a briefcase

may be a different order of container than a cigarette box, it is

not easy to rest a principled articulation of the reach of the

[F]ourth [A]mendment upon the distinction."               Id.

           The Eatherton panel also noted that the defendant's

argument was "not unlike" Justice Marshall's in "his dissent to

Gustafson and Robinson."        Id.     The Eatherton panel then cited to

the portion of that dissent that relied on Chimel to dispute the

majority's     decision   to   uphold    the   warrantless       search   of   the

container in that case.        Id. (citing Robinson, 414 U.S. at 256-58

(Marshall, J., dissenting)).          While the argument advanced in that

portion   of    Justice   Marshall's      dissent    "may       have   analytical

appeal," the Eatherton panel concluded, the view set forth there

"does not presently represent the law."             Id.

           The Eatherton panel wound up its analysis by invoking

Edwards, which was decided the year after Robinson and Gustafson.

The Court held in Edwards that the Fourth Amendment permitted the

warrantless search of clothing that an arrestee was wearing at the

time of his arrest even though the search of the clothing occurred

the day after the arrest and while the arrestee was in jail.

Edwards, 415 U.S. at 808-09.            Edwards reasoned that "the legal


                                      - 13 -
arrest of a person" reduces the arrestee's expectation of privacy

in items "in his immediate possession, including his clothing."

Id. at 805, 808 (emphasis added) (quoting United States v. DeLeo,

422 F.2d 487, 493 (1st Cir. 1970)).

             The Eatherton panel observed that the Court in Edwards,

"after noting that the courts of appeals have generally permitted

searches of both 'the person and the property in his immediate

possession,'" stated that "it is difficult to perceive what is

unreasonable about the police examining and holding as evidence

those personal effects of the accused that they already have in

their lawful custody as the result of a lawful arrest." Eatherton,

519 F.2d at 610 (first quoting Edwards, 415 U.S. at 803; then

quoting Edwards, 415 U.S. at 806).       The search in Edwards had been

made   "in    the     station   house   after   an   arrest,"   Eatherton

acknowledged.       But Eatherton explained that there was no reason to

"doubt that [those observations from Edwards] apply equally to

searches in the field immediately incident to the arrest."            Id.

Eatherton thus held that, as the defendant in the case before it

had "conceded the agents properly seized the briefcase as . . .

incident to his arrest . . . any expectation of privacy which he

held with regard to the briefcase was taken out of 'the realm of

protection from police interest in weapons, means of escape, and

evidence.'"    Id. at 610-11 (quoting Edwards, 415 U.S. at 808-09).




                                   - 14 -
                                        B.

               As this extended review of Eatherton reveals, the panel

in that case did more than determine that the rule set forth in

Robinson, Gustafson, and Edwards rather than the rule set forth in

Chimel controlled the briefcase's search.              The panel also made

clear that it based that determination on the considered judgment

that, for purposes of the rule laid down in Robinson and Gustafson,

a search of a container (at least of the "order" of a briefcase,

see Eatherton, 519 F.2d at 610) in the hands of an arrestee at the

time of the arrest was no different from a search of a container

in the pocket of an arrestee at that time.2            As Eatherton put it,

a "line which [would] plac[e] the briefcase beyond the search of

[the] 'person' which Robinson and Gustafson expressly approve is

one requiring gossamer distinctions."             519 F.2d at 610.    And, to

that       point,   the   Eatherton   panel    explained   that,   although   a

briefcase was of "a different order of container from a cigarette

box," it would not be "easy" to make any such distinction for the




       2We understand Eatherton's statement that "[t]here is no
indication that the result in [Robinson and Gustafson] would have
been any different had the cigarette packages been . . . dropped
to the ground in response to police command," 519 F.2d at 610, to
mean only that the determination of whether an item is "of the
person" of the arrestee or in the arrestee's "area of immediate
control" is unaffected by post-arrest, police-ordered conduct.
After all, at the same time that the FBI agents told Eatherton to
drop the briefcase, they also told him he was under arrest. Id.
at 609.


                                      - 15 -
relevant Fourth Amendment purposes in a "principled" manner.                 Id.

Eatherton then reasoned that, as a result, Edwards required the

conclusion that the briefcase's search was reasonable, given that

Edwards concluded that the search of the personal property found

on the person of the arrestee in that case was reasonable.                   In

that regard, Eatherton concluded based on Edwards that because

"the   agents   properly   seized    the     briefcase   . . .    incident   to

[Eatherton's] arrest. . . . any expectation of privacy which he

held with regard to the briefcase was taken out of 'the realm of

protection from police interest in weapons, means of escape, and

evidence.'"     Id. at 610-11 (quoting Edwards, 415 U.S. at 808-09).

           Perez   does    not   suggest     that   there   is   any   relevant

difference between his backpack and the briefcase in Eatherton or

that the backpack was not on his back when the District Court found

that he was arrested, notwithstanding that the District Court found

that he was "formally" arrested only thereafter.             He thus accepts

that his appeal lacks merit if Eatherton controls.                     His sole

contention, therefore, is that Eatherton does not control due to

post-Eatherton developments.

                                      C.

           The post-Eatherton developments that Perez has in mind

are two Supreme Court precedents: Chadwick and Gant.              He contends

that, whether separately or together, they undermine (even if they

do not overrule) Eatherton's holding that a briefcase in the hands


                                    - 16 -
of an arrestee at the time of arrest is no different from the

cigarette containers involved in Robinson and Gustafson.                   But we

cannot agree -- even if we account for post-Chadwick and post-Gant

out-of-circuit precedent that is at odds with Eatherton.                  Thus, we

conclude that Eatherton remains binding on us as a panel.3

                                           1.

               We start with Perez's arguments about Chadwick, which

was decided two years after               Eatherton.       Perez contends that

Chadwick       is    a    significant       intervening     precedent     because

Eatherton's rationale depended on the determination that there was

"no indication" that the result in either Robinson or Gustafson

"would have been any different had the cigarette packages been in

the defendants' hands rather than in their pockets or if they had

been       dropped   to   the   ground    in    response   to   police   command."

Eatherton, 519 F.2d at 610.              Yet, Perez asserts, Chadwick shows

that is not so.



       Neither Perez nor the government addresses whether, even if
       3

Eatherton does not control the outcome of this case, it is
controlled by our post-Chadwick ruling in United States v.
Maldonaldo-Espinosa, 968 F.2d 101, 104 (1st Cir. 1992) (rejecting
an argument that the search of a bag "on the table next to [the
handcuffed defendant] and within reach" could be justified only by
an exigency because "government agents, when arresting a person,
may constitutionally search an arrested person's nearby . . . bag,
without a warrant . . . whether or not [the agents] have reason to
fear that the carry-on bag contains a weapon, another threat to
their safety, or destructible evidence"). Because we conclude that
Eatherton controls here, we need not evaluate the search of Perez's
backpack under Maldonaldo-Espinosa.


                                         - 17 -
           The Supreme Court held in Chadwick that the warrantless

search of an arrestee's      "double-locked,    200-pound footlocker"

violated the Fourth Amendment when the search of that container

was conducted beyond "the area from within which [the arrestees]

might gain possession of a weapon or destructible evidence,"

Chadwick, 433 U.S. at 5 (quoting Chimel, 395 U.S. at 763), and was

not "justified by any other exigency," id. at 15.         But nothing in

Chadwick   disturbs    either    Robinson's    ruling     upholding    the

warrantless search of a cigarette container in the pocket of an

arrestee at the time of the lawful arrest or Gustafson's ruling

upholding such a search even when it is performed after the

cigarette container has been removed from the arrestee's immediate

area of control.

           In   that   regard,   Chadwick     expressly    states     that,

"[u]nlike searches of the person [under] United States v. Robinson

[and] United States v. Edwards, searches of possessions within an

arrestee's immediate control cannot be justified by any reduced

expectations of privacy caused by the arrest."            433 U.S. at 16

n.10 (emphasis added) (citations omitted).        We do not read that

passage, in expressly reaffirming Robinson and Edwards, to be

silently rejecting the parts of their holdings that blessed the

searches of the personal property in those cases that was found on

the person of the defendants.      Nor do we read that passage, in

reaffirming those two cases without mentioning Gustafson, to be


                                 - 18 -
silently    rejecting      Gustafson's     extension    of   Robinson's    rule

regarding a search of personal property on the person of the

arrestee at the time of the arrest to cover the search of such

property even after that property was no longer in the arrestee's

area of immediate control.

            Moreover, nothing in Chadwick purports to address how to

treat a container that an arrestee has in hand at the time of

arrest relative to a container that an arrestee has in a pocket at

that time.      In fact, Chadwick had no reason to address that

question because the arrestee was not holding the container in

Chadwick.    Nor, for that same reason, did Chadwick have reason to

address whether the arrestee's dropping of such a container in

response to a police command upon arrest would change the calculus.

So, not surprisingly, Chadwick does not purport to address that

scenario either.

            True, Chadwick does state that "[o]nce law enforcement

officers have reduced luggage or other personal property not

immediately associated with the person of the arrestee to their

exclusive control, and there is no longer any danger that the

arrestee might gain access to the property to seize a weapon or

destroy evidence, a search of the property is no longer an incident

of the arrest."         433 U.S. at 15 (emphasis added).             But the

emphasized    language     shows   that    Chadwick's   "immediate   area    of

control"     rule   does    not    apply   to   "personal    property     . . .


                                     - 19 -
immediately associated with the person of the arrestee," id., and

so merely operates in parallel to the holdings in                           Robinson,

Gustafson, and Edwards.          Thus, because Chadwick does not address

what, if any, personal property carried or worn by the arrestee at

the time of the arrest beyond the cigarette packages in Robinson

and Gustafson and the clothing in Edwards constitutes "personal

property     . . . immediately         associated   with   the      person    of   the

arrestee," Chadwick does not address whether a held briefcase like

the one in Eatherton is to be treated the way that the personal

property in those three cases was.           As a result, Chadwick gives no

"indication that the result in [Robinson and Gustafson] would have

been   any    different    had    the    cigarette     packages      been     in   the

defendants' hands rather than in their pockets or if they had been

dropped to the ground in response to police command."                    Eatherton,

519 F.2d at 610.

             Simply     put,   Eatherton     was    concerned       about     drawing

distinctions     between       types    of   containers       in    an   arrestee's

"immediate     possession,"      Eatherton,      519   F.2d    at    610     (quoting

Edwards, 415 at 803), at the time of arrest -- a problem that is

hardly trivial given the range of containers people may carry

beyond cigarette packages, from holsters to purses to backpacks.

But, as      Chadwick    had no reason to address that line-drawing

problem, it cannot offer any insight into how to resolve that




                                        - 20 -
problem.    We thus do not see how Chadwick undermines Eatherton's

rationale for upholding the search of the briefcase in Eatherton.

                                 2.

           Perez does argue that Gant undermines Eatherton even if

Chadwick does not.   But here, too, we disagree.

           Gant relied on Chimel in holding that courts had wrongly

interpreted New York v. Belton, 453 U.S. 454 (1981), to have held

that all personal property in an automobile was categorically

searchable incident to an occupant's arrest.       Gant, 556 U.S. at

348-52.    Perez contends that it follows from Gant that the search

of his backpack is no different from the car search in that case.

           But, Gant, like Chadwick, said nothing about whether the

rule of Robinson (as applied in Gustafson and Edwards) governs a

container that an arrestee is carrying at the time of the arrest

(or that is dropped in response to police command at that time).

Indeed, Gant did not address carried personal property at all,

because it concerned only whether a car may be searched incident

to a lawful arrest of an occupant of the car.       Thus, Gant is no

different from Chadwick in the relevant respect, and so provides

no basis for our concluding that Eatherton has been stripped of

its controlling force.     For, like Chadwick, Gant has literally

nothing to say about where the line should be drawn in searches




                               - 21 -
incident to arrest when it comes to things an arrestee carries at

the time of the arrest.4

                                      D.

               The dissent appears to accept that neither Chadwick nor

Gant       directly   overrules   Eatherton.     The   dissent    nonetheless

contends that we still can be confident that if the panel in

Eatherton knew what we do in consequence of Chadwick and Gant,

that panel would have abandoned its hard line about the difficulty

of drawing hard lines.        As the dissent sees it, the panel in that

event would have "centered its analysis around 'immediate control'

rather than shoehorning the search of a closed container into being

'of the [arrestee's] person.'"             Dissent at 49.   But we see no

"clear and convincing" case for that conclusion.                 Guerrero, 19

F.4th at 552.

               Chadwick does make clear that no per se rule establishes

that "luggage" within the "immediate area of control" of an



       Perez does at points argue that, under Gant, the location
       4

of a container "relative to the arrestee at the time of arrest is
irrelevant" when determining whether the container can be searched
without a warrant, because all such searches should be evaluated
based on the container's location at the time of its search. But,
as Gustafson and Edwards show, the application of Robinson's
categorical rule depends, as to at least some personal property,
on the property's location at the time of the arrest and not at
the time of the search.      And, as we have explained, there is
nothing in Gant that undermines Robinson, Gustafson, or Edwards.
We thus do not see how Perez's time-of-the-search contention,
insofar as it is meant to address all containers, can be reconciled
with Robinson as it was applied in Gustafson and Edwards.


                                    - 22 -
arrestee at the time of the arrest may be warrantlessly searched.

See Chadwick, 433 U.S. at 16 n.10.          Thus, Chadwick does prompt the

question of why it would be per se reasonable to search a briefcase

that is held (or dropped upon police command) by an arrestee at

the time of the arrest.

             But Chadwick applied the "immediate control" test to a

container that was not carried by the arrestee at the time of the

arrest.      By contrast, the Eatherton panel was addressing only how

to treat a container that an arrestee was carrying at that time,

so the Eatherton panel did not purport to suggest that the Robinson

rule would apply to nearby containers not carried by the arrestee

at the time of the arrest.        As a result, Chadwick fails to provide

a clear and convincing reason for us to conclude that the Eatherton

panel would have reversed course had it known about Chadwick.

             That is especially so given that Chadwick, in a passage

that   the    dissent     mentions    but   otherwise    ignores,   expressly

distinguishes       searches     of    personal    property     "immediately

associated" with the person of the arrestee (like the personal

property     at   issue   in   Robinson,    Gustafson,   and   Edwards)   from

searches of personal property of the arrestee that is merely within

the "immediate control" of the arrestee.          Id. at 15.    For, because

of that distinction, Chadwick did not address whether principled

lines could be drawn in this context between types of containers

that are carried by the arrestee at the time of arrest -- whether


                                      - 23 -
those types of containers are cigarette packs, wallets, purses,

fanny packs, holsters, or briefcases.                      Yet Eatherton's clearly

expressed concern was that such lines could not be drawn.                              See

Eatherton, 519 F.2d at 610.

              Gant   similarly     offers        no    relevant    insight     into    the

proper way to resolve the line-drawing problem that troubled the

Eatherton      panel.        Because      Gant     addresses      only    searches      of

automobiles, it says nothing about what distinctions might be

tenable when it comes to containers that an arrestee is carrying

at the time of the arrest.

              We thus fail to see how we could be confident that

Chadwick or Gant -- or even the two taken together -- would have

led the Eatherton panel to "center" its analysis of the briefcase

on the "immediate control" question.                   Were the panel to have done

so, it would have been forced to draw the very distinctions between

the   types    of    carried    containers         that    it    concluded     were    too

"gossamer" to make.          Eatherton, 519 F.2d at 610.                But not a word

in either Chadwick or Gant would give the Eatherton panel reason

to    think   that,     contrary     to    the        panel's   initial    assessment,

distinctions of substance as to such containers could be made in

a "principled" manner.          See id.

              Of course, the dissent is right that, in the wake of

Chadwick      and    Gant,   other     circuits         have    drawn    the   kinds   of

distinctions that Eatherton refused to make.                    See United States v.


                                          - 24 -
Knapp, 917 F.3d 1161, 1168 (10th Cir. 2019) (holding that the

search of a purse was governed by the Chimel standard because the

purse   "was    not   concealed   under   or     within   [the    defendant's]

clothing" and "was easily capable of separation from her person");

United States v. Shakir, 616 F.3d 315, 321 (3rd Cir. 2010) ("[A]

search is permissible incident to a suspect's arrest when, under

all the circumstances, there remains a reasonable possibility that

the arrestee could access a weapon or destructible evidence in the

container or area being searched.").         But post-Eatherton precedent

is not uniformly at odds with Eatherton, as even the dissent

acknowledges     in   describing    how     other      circuits   reacted   to

Chadwick -- at least prior to Gant.          See Dissent at 39.

           Indeed, some circuits after Chadwick but before Gant

appeared   to   follow   Eatherton's      lead    in   categorizing   certain

carried items as "of the person."           Two months after Chadwick was

decided, for example, the Fourth Circuit assumed that warrantless

searches of objects carried in an arrestee's hands were permissible

as searches "of the person incidental to an arrest." United States

v. Wyatt, 561 F.2d 1388, 1391 (4th Cir. 1977) (search of a notebook

that arrestee retrieved from his car after being arrested).                 And

four years later, in United States v. Graham, the Seventh Circuit

explained that a "shoulder purse carried by a person at the time

he is stopped lies within the scope of a warrant authorizing the

search of his person."      638 F.2d 1111, 1114 (7th Cir. 1981).


                                   - 25 -
             Although the question in Graham was whether the purse

was "of the person" for purposes of a search warrant authorizing

a search of the person, and there was no issue of a warrantless

search incident to an arrest, the Seventh Circuit's reasoning

nevertheless aligns neatly with Eatherton's.         As the Seventh

Circuit explained, "[c]ontainers . . . while appended to the body,

are so closely associated with the person that they are identified

with and included within the concept of one's person.           To hold

differently would be to narrow the scope of a search of one's

person to a point at which it would have little meaning."           Id.

And almost two decades later, the Eighth Circuit followed the

Seventh Circuit's lead and explained that a purse, for purposes of

the       search-incident-to-arrest   exception,   was     an    object

"immediately associated" with one's person, even though the purse

in that case was also within the arrestee's area of "immediate

control."      Curd v. City Court, 141 F.3d 839, 843-44 (8th Cir.

1998).     Indeed, the Eighth Circuit agreed "with the general view"

of other courts that "concluded that a purse, like a wallet, is an

object 'immediately associated' with the person."        Id. (citations

omitted).5


      5To be sure, four months later, the Eighth Circuit approved
a backpack search because "the search of his person and backpack
was lawful as a search incident to arrest," seemingly
distinguishing "person" from "backpack" and citing a case for the
idea that possessions within "immediate control" can be searched.
United States v. Oakley, 153 F.3d 696, 698 (8th Cir. 1998).


                                 - 26 -
            Thus, to the extent that post-Chadwick precedents from

sister circuits may shed light on what the Eatherton panel would

have done with the benefit of them, we do not see how the pre-Gant

precedents of that ilk do. Even though some of those post-Chadwick

but   pre-Gant   precedents   adopt    the   dissent's    position,    these

precedents are, as a group, too varied to justify application of

the second exception to the law-of-the-circuit doctrine.

            The dissent does also cite to post-Gant sister-circuit

cases that extend Gant to non-vehicle contexts.          See, e.g., United

States v. Davis, 997 F.3d 191, 193 (4th Cir. 2021) ("Gant applies

beyond the automobile context to the search of a backpack.");

United States v. Knapp, 917 F.3d 1161, 1168 (10th Cir. 2019)

("[A]lthough     Gant   specifically    addressed   the    search     of   an

automobile, its principles apply more broadly."); United States v.

Cook, 808 F.3d 1195, 1199 n.1 (9th Cir. 2015) ("We do not read

Gant's holding as limited only to automobile searches because the

Court tethered its rational to the concerns articulated in Chimel,

which involved a search of an arrestee's home."); Shakir, 616 F.3d

at 318 ("[T]he Government contends that the rule of Gant applies

only to vehicle searches.       We do not read Gant so narrowly.").

But these out-of-circuit cases also fail to show what is required

to justify applying the second exception to the law-of-the-circuit

doctrine.




                                 - 27 -
             Even after Gant, the Supreme Court recognized in Riley

v. California that "[l]ower courts applying Robinson and Chimel

. . . have approved searches of a variety of personal items carried

by an arrestee" and cited to a case where the D.C. Circuit upheld

the search of a purse incident to the arrest of its owner.             573

U.S. 373, 392-93 (2014) (citing, inter alia, United States v. Lee,

501   F.2d   890,   892   (D.C.   Cir.   1974)).   And   Riley   repeatedly

described Gant as a case involving automobile searches without in

any way suggesting that Gant had worked a reformation of Robinson's

rule for searches of at least some personal property on the person

of the arrestee at the time of the arrest.           See 573 U.S. at 398

("But Gant relied on 'circumstances unique to the vehicle context'"

(quoting Gant, 556 U.S. at 343)); id. at 385 ("Gant added . . . an

independent exception for a warrantless search of a vehicle's

passenger compartment . . . . That exception stems not from Chimel

. . . but from 'circumstances unique to the vehicle context.'"

(quoting Gant, 556 U.S. at 343)).         Thus, the post-Gant cases from

sister circuits do not show in a clear and convincing way that the

Eatherton panel -- with the benefit of Gant -- would have ruled

the same way that those circuits had.

             We note, too, that Riley made its observation about how

other circuits had applied Robinson post-Chadwick while addressing

whether the rule of Robinson extends to the search of the data on

an arrestee's carried cellphone.         Riley, 573 U.S. at 392-93.   Yet,


                                    - 28 -
in doing so, the Court both expressly reaffirmed that Robinson

survived Chadwick as to at least some personal property on the

person of the arrestee at the time of arrest, id. at 384, 394, and

highlighted the fact that Chadwick expressly exempted from its

"immediate control" test "personal property . . . immediately

associated with the person of the arrestee[,]" id. at 384 (first

alteration in original) (quoting Chadwick, 433 U.S. at 15).

           Finally, although Riley carefully explained that the

officer-safety,     evidence-collection,       and     diminished-privacy

rationales for Robinson's rule did not apply to a cell phone's

data, the Court said nothing in doing so that "clear[ly] and

convincing[ly]"    indicates,    Guerrero,    19     F.4th   at   552,   that

Robinson's rule has no application to a container that is of the

same "order" as a briefcase, Eatherton, 519 F.2d at 610.                 Riley

does   suggest   that,   based   on   those   rationales,     a   200-pound

double-locked storage trunk may fall outside Robinson's rule even

if the arrestee happens to be dragging the trunk along behind him.

See Riley, 573 U.S. at 394.      But Eatherton did not itself suggest

otherwise.   Rather, Eatherton held only that a briefcase that the

arrestee was carrying at the time of the arrest fell within

Robinson's rule because the distinction between such a container

when held in hand and a cigarette package when carried in a pocket

was "gossamer" and because it was "not easy to rest a principled




                                 - 29 -
articulation of the reach of the [F]ourth [A]mendment upon the

distinction."       Eatherton, 519 F.2d at 610.

            We note, too, that Riley's comment about the potential

exclusion of the dragged trunk from Robinson's rule was based on

the   notion      that   "[m]ost      people     cannot   lug     around"     a    trunk

containing "every piece of mail . . . every picture . . . or every

book or article they have read" and on the observation that "nor

would they have any reason to attempt to do so."                    Id. at 393-94.

Yet, of course, most people can carry a briefcase and often have

reason to do so.         Indeed, Perez himself does not argue that Riley

is the case that would have led the Eatherton panel to rule other

than it did, as he contends only that Riley merely excluded digital

content from Robinson's rule.

                                           E.

            We close by addressing what may be our key point of

disagreement with our dissenting colleague -- the proper scope of

the second exception to the law-of-the-circuit doctrine.                          As we

see   it,   the    whole   point      of   the   doctrine    is    to   ensure      that

individual     panels      of   our    court      do   not   --    in   an    ad     hoc

way -- second-guess prior circuit precedents just because the

panels are convinced that those precedents are wrong.                        Thus, the

determination of whether a prior panel decision binds a future

panel cannot depend on whether there are sound reasons to conclude

that the prior panel got it wrong.                Yet, the post-Eatherton body


                                       - 30 -
of precedent that the dissent invokes shows, in our view, that

there are merely reasons of that sort when it comes to Eatherton,

as that body of caselaw fails to provide "a clear and convincing

basis to believe that the [Eatherton] panel would have decided the

issue differently."       Guerrero, 19 F.4th at 552.

            A comparison of this case with Guerrero -- which is our

most     recent    case   to   find   the   second   exception   to   the

law-of-the-circuit doctrine to be satisfied -- underscores the

point.    In finding the second exception to the doctrine applicable

there, we relied on an unbroken string of intervening Supreme Court

precedents.       Id. at 555-57.   Those precedents, we explained, each

had made sweeping statements that contradicted the very rationale

that the prior panel had relied on in ruling that a warrantless

search had to be subjectively and not just objectively aimed at

addressing an exigency to be lawful.         See id., 19 F.4th at 554.

And while we acknowledged that none of those precedents directly

overruled the prior panel decision, we pointed out that one of

them rejected the application of a subjective test with respect to

a home search, notwithstanding that the prior panel had applied

that test to a search of an automobile.       See id. at 555-56 (citing

Maryland v. Buie, 494 U.S. 325 (1990)).         We thus explained that,

given the heightened privacy interests at stake in home searches,

it would be most strange to conclude that the prior panel would

stick with its position that a subjective test had to be used for


                                   - 31 -
a search of a car if that panel had the benefit of the intervening

Supreme Court precedent.     See id. at 557.

          Here, by contrast, the relevant intervening Supreme

Court precedents are Chadwick and Gant -- neither of which even

addresses a search of personal property carried by an arrestee at

the time of the arrest, let alone whether and how to distinguish

between types of such personal property, at least as between

briefcases and cigarette packages.     We thus do not see how we could

reason from either of those precedents to the determination that

there is a clear and convincing basis on which to conclude that

the Eatherton panel would have decided differently with the benefit

of knowing what we now do.    And the fact that sister circuits have

relied on Chadwick and Gant to chart a different course than

Eatherton cannot provide the required clarity, as the second

exception to the law-of-the-circuit doctrine does not apply just

because several other circuits have chosen not to follow one of

our prior rulings.

          Accordingly,       we     conclude    that,    under    the

law-of-the-circuit doctrine, the en banc process supplies the

proper means for our Court to reconsider Eatherton in light of all

that has transpired in its wake.      Through that process, the Court

as a whole rather than this single panel can examine Eatherton and

the question of whether Eatherton's line-drawing concern justifies

its decision to treat an openly carried container like a briefcase


                                  - 32 -
the way that the Supreme Court treated the cigarette containers in

Robinson and Gustafson and the clothing in Edwards.   And so, until

then, the rule laid down in Eatherton controls this case about the

things we carry, as Perez makes no argument that Eatherton can be

distinguished on the facts.6

                                III.

          For the reasons set out above, the District Court's

judgment of conviction is affirmed.



                   -Dissenting Opinion Follows-




     6 We do recognize that a determination that a Fourth Amendment
precedent of our court remains binding may well bear on whether
the good-faith exception to the warrant requirement applies. See
Davis, 564 U.S. at 232 ("[P]olice . . . searches conducted in
objectively reasonable reliance on binding appellate precedent are
not subject to the exclusionary rule.").      But, given the vital
role that the law-of-the-circuit doctrine plays in ensuring the
orderly process of lower court adjudication, that fact provides no
reason for us to be less strict in applying the law-of-the-circuit
doctrine than we have long been.


                               - 33 -
              MONTECALVO, Circuit Judge, dissenting.            I view United

States v. Eatherton, 519 F.2d 603 (1st Cir. 1975), differently

than the majority, particularly as to how the exception to the

law-of-the-circuit      doctrine   applies      here.       Further,    applying

modern Supreme Court precedent, I would find that the search of

Perez's backpack violated his Fourth-Amendment rights.                   I would

also find that the good-faith exception is not applicable here.

Accordingly, and for the reasons that follow, I would reverse the

decision of the district court on Perez's motion to suppress and

vacate the judgment of conviction.

                   I. The Law-of-the-Circuit Doctrine

              This appeal arises from the denial of a motion to

suppress the warrantless search of the backpack Perez was wearing

at the time of his arrest.         As the majority notes, that search

should   be    viewed   through   the   scope   of   "the    basic     rule   that

'searches conducted outside the judicial process, without prior

approval by judge or magistrate are per se unreasonable under the

Fourth Amendment -- subject only to a few specifically established

and well-delineated exceptions.'"         Arizona v. Gant, 556 U.S. 332,

338 (2009) (quoting Katz v. United States, 389 U.S. 347, 357

(2009)).      One such exception is that of the search incident to

arrest. Id. There are two grounding principles to that exception:

(1) to protect officer safety and (2) to preserve evidence.                   Id.




                                   - 34 -
             The     development     of       this   exception    has    evolved   over

decades of caselaw, both in the Supreme Court and this Circuit.

To that end, as to our prior decisions, we are bound by the

law-of-the-circuit doctrine.              United States v. Barbosa, 896 F.3d

60, 74 (1st Cir. 2018).              However, there are exceptions to that

doctrine, as it is "neither a straightjacket nor an immutable

rule."      Id. (quoting Carpenters Local Union No. 26 v. U.S. Fid. &

Guar. Co., 215 F.3d 136, 142 (1st Cir. 2000)).                      One exception is

"when the holding of a previous panel is contradicted by subsequent

controlling authority, such as a decision by the Supreme Court, an

en   banc    decision     of   the    originating        court,     or   a    statutory

overruling."       Id.    Another exception exists "when 'authority that

postdates      the       original     decision,          although       not    directly

controlling, nevertheless offers a sound reason for believing that

the former panel, in light of fresh developments, would change its

collective mind.'"         Id. (quoting Williams v. Ashland Eng'g Co., 45

F.3d 588, 592 (1st Cir. 1995)).

             The majority's opinion rests on a case decided by a panel

of   this    court    nearly   half       a    century    ago:    United      States   v.

Eatherton, 519 F.2d 603 (1st Cir. 1975).                         Admittedly, should

Eatherton remain good law, it is controlling here.                         In my view,

however, the second exception to the law-of-the-circuit doctrine,

delineated above, is applicable under these circumstances.                             In

light of the major developments to the search-incident-to-arrest


                                          - 35 -
exception    postdating   Eatherton,      including       modern     binding      and

persuasive precedent on the propriety of warrantless searches

incident to arrest, I think that the Eatherton panel would have

come to a different conclusion.           To justify this conclusion, an

analysis    of   Eatherton     itself    and     a   brief    history      of     the

developments following Eatherton's publication is necessary.

                                A. Eatherton

            As described in the majority opinion, Eatherton involved

the warrantless search of a briefcase that the arrestee was holding

when first approached by law enforcement.               519 F.2d at 609.        After

the arrestee was frisked and placed in the back of a police

vehicle, the officers searched the briefcase, and the contents

were later admitted at trial.           Id.    The defendant challenged the

search of his briefcase as violative of his Fourth-Amendment

rights.    Id. at 609-10.

            The Eatherton panel noted that the appellant's strongest

support for his Fourth-Amendment challenge laid in Chimel v.

California, 395 U.S. 752 (1962); however, the panel recognized

that Chimel cited with approval to Draper v. United States, 358

U.S. 307 (1959), a case involving a "virtually identical" search

to the one at issue in Eatherton.         519 F.2d at 610.         The Eatherton

panel then cited to a number of cases from our sister circuits

that,     applying   Chimel,    upheld        similar     searches    of    closed

containers carried by the arrestee. 519 F.2d at 610 (citing United


                                   - 36 -
States v. Maynard, 439 F.2d 1086 (9th Cir. 1971); United States v.

Mehciz, 437 F.2d 145 (9th Cir. 1971), cert. denied, 402 U.S. 974

(1971); United States ex rel. Muhammad v. Mancusi, 432 F.2d 1046

(2d Cir. 1970), cert. denied, 402 U.S. 911 (1971)).                Lastly, the

Eatherton    panel    noted   that    the     Supreme   Court's    then-recent

decisions in United States v. Robinson, 414 U.S. 218 (1973);

Gustafson v. Florida, 414 U.S. 260 (1973); and United States v.

Edwards, 415 U.S. 800 (1974), offered further guidance on the

Fourth-Amendment issue.       519 F.2d at 610.

            Relying on this case law, the Eatherton panel determined

that differentiating between the cigarette packages in Robinson

and Gustafson and the briefcase in Eatherton "requir[ed] gossamer

distinctions."       Id. at 610.     The panel further held that "[w]hile

a briefcase may be a different order of container from a cigarette

box, it is not easy to rest a principled articulation of the reach

of the [F]ourth [A]mendment upon the distinction."                Id.   Relying

on Edwards, the Eatherton panel emphasized that once the briefcase

was "properly seized" as "incident to [the defendant's] arrest"

any expectation of privacy the defendant held was diminished.              Id.

at 610-11.

                                B. Chadwick

            After Eatherton, the Supreme Court decided United States

v. Chadwick, 433 U.S. 1 (1977).          In Chadwick, the Court examined

the search of a 200-pound footlocker stowed in the trunk of the


                                     - 37 -
defendant's car at the time of arrest.           433 U.S. at 3-4.       Officers

subsequently seized the footlocker, transported it to a federal

building, and then, an hour and a half later and without a warrant,

searched the footlocker.       Id. at 4.      The officers had no reason to

believe     the   footlocker    held    inherently       dangerous     items   or

contained evidence that could lose value over time. Id. Examining

the nature of the footlocker, the Court noted that "[l]uggage

contents are not open to public view . . . nor is luggage subject

to regular inspections and official scrutiny on a continuing

basis."    Id. at 13.   "[L]uggage is [also] intended as a repository

of personal effects."     Id.

            Chadwick    reiterated     that     "[t]he     potential     dangers

lurking in all custodial arrests make warrantless searches of items

within the 'immediate control' area reasonable without requiring

the arresting officer to calculate the probability that weapons or

destructible evidence may be involved."            433 U.S. at 14-15.          But

Chadwick    importantly   clarified     that    "warrantless     searches       of

luggage or other property seized at the time of an arrest cannot

be justified as incident to that arrest either if the search is

remote in time or place from the arrest . . . or no exigency

exists."     Id. at 15 (cleaned up).          Finally, the Chadwick Court

concluded    that   "[o]nce    law   enforcement     officers   have     reduced

luggage or other personal property not immediately associated with

the person of the arrestee to their exclusive control, and there


                                     - 38 -
is no longer any danger that the arrestee might gain access to the

property to seize a weapon or destroy evidence, a search of that

property is no longer an incident of the arrest."        Id.   Put another

way, "when no exigency is shown to support the need for an

immediate search, the Warrant Clause places the line at the point

where the property to be searched comes under the exclusive

dominion of police authority."      Id.

                      C. Cases Postdating Chadwick

             After Chadwick, several of our sister circuits addressed

situations involving items that an arrestee was holding or carrying

at the time of arrest and questioned the breadth of Chadwick,

reaching mixed results.       See United States v. Han, 74 F.3d 537,

543   (4th    Cir.   1996)   (finding   that,   after   Chadwick,   "[t]he

determinative question appears to be whether the time and distance

between elimination of the danger and performance of the search

were reasonable" and holding that "when a container is within the

immediate control of a suspect at the beginning of an encounter

with law enforcement officers; and when the officers search the

container at the scene of the arrest; the Fourth Amendment does

not prohibit a reasonable delay . . . between the elimination of

danger and the search"); see also United States v. Garcia, 605

F.2d 349, 356-57 (7th Cir. 1979) (noting the "less than uniform"

application of Chadwick across the circuits).




                                  - 39 -
            In United States v. Calandrella, 605 F.2d 236 (6th Cir.

1979), cert. denied, 444 U.S. 991 (1979), the            Sixth Circuit

examined a briefcase seized from the person at the time of arrest.

That court, examining Chadwick, noted that "the primary [F]ourth

[A]mendment interest [is] in the privacy of the contents of [a

container], not in the simple possession of the receptacle."          Id.

at 249. Therefore, the defendant had an increased privacy interest

in the briefcase, like the footlocker in Chadwick, the "very

purpose [for which] is to transport papers and other items of an

inherently personal, private nature."       Id. (internal quotations

omitted).     Ultimately, the Calandrella court found that under

Chadwick, "once the agents had seized the item and reduced it to

their exclusive control there was no further danger that the

defendant     would   secure   therefrom   either   a   weapon   or   an

instrumentality of escape, or would destroy evidence contained in

the briefcase."       Id. at 249, 251-52 (expressly overturning its

prior line of cases upholding searches of suitcases "even after

the item has been seized and the suspect subdued" and citing to

courts that had made similar decisions prior to Chadwick, including

Eatherton).

            Several other circuits also recognized the applicability

of Chadwick to cases involving carried containers.          See United

States v. Berry, 571 F.2d 2, 3 (7th Cir. 1978) (holding that "until

Chadwick, there was no reason for law enforcement officials to


                                 - 40 -
believe that attache cases were not among those personal effects

which, under [Robinson], could be seized as part of a 'full search

of the person' incident to a lawful arrest, and which, under

[Edwards], could be searched several hours after the suspect had

been taken into custody"); see also United States v. Stewart, 595

F.2d 500, 503 (9th Cir. 1979) (finding that if Chadwick was

applicable, "it would require suppression of the contents of the

attache case"); United States v. Myers, 308 F.3d 251, 273 (3d Cir.

2002) (examining the search of a "school bag" under the immediate

control analysis and citing Chadwick's rationale).

                                D. Gant

           Later, in Arizona v. Gant, 556 U.S. 332 (2009), the Court

revisited the search-incident-to-arrest exception.     The Court once

again emphasized that the limitation on that exception "ensures

that the scope of a search incident to arrest is commensurate with

its purposes of protecting arresting officers and safeguarding any

evidence of the offense of arrest that an arrestee might conceal

or destroy."    Id. at 339.    Relying on the principles articulated

in Chimel, the Court reiterated that "[i]f there is no possibility

that an arrestee could reach into [an] area that law enforcement

officers   seek      to   search,   both   justifications   for   the

search-incident-to-arrest exception are absent and the rule does

not apply."    Id.




                                - 41 -
                          E. Cases Postdating Gant

              The   decision     in   Gant   has   been    instrumental     in   the

understanding and application of the Fourth Amendment and the

search-incident-to-arrest doctrine.                After Gant, circuit courts

applied that precedent and the immediate control analysis to

containers outside of the vehicle context.                 See United States v.

Shakir, 616 F.3d 315, 318 (3d Cir. 2010), cert. denied, 562 U.S.

1116 (2010) (examining the search of a gym bag under the "narrowed"

scope    of   the   search-incident-to-arrest            doctrine   under      Gant);

United   States     v.   Cook,    808   F.3d     1195,    1199   (9th   Cir.   2015)

(applying the immediate control analysis to a backpack); United

States v. Davis, 997 F.3d 191, 193 (4th Cir. 2021) (holding that

"Gant applies beyond the automobile context to the search of a

backpack"); United States v. Knapp, 917 F.3d 1161, 1168-70 (10th

Cir. 2019) (considering whether the search of an arrestee's purse

was justified under Chimel and Gant); see also United States v.

Hill, 818 F.3d 289, 295 (7th Cir. 2016) (applying immediate control

analysis to bag); United States v. Matthews, 532 Fed. Appx. 211,

217-19 (3d Cir. 2013) (finding that the search of a backpack could

not be justified under the immediate control analysis of the

search-incident-to-arrest doctrine); cf. United States v. Perdoma,

621 F.3d 745, 750-51 (8th Cir. 2010), cert. denied, 563 U.S. 992

(2011) (upholding the warrantless search of a "small bag" where

"the search of the bag occurred in close proximity to where [the


                                        - 42 -
arrestee] was restrained" and the arrestee had already run from

officers once; but holding that a closer application of Gant was

not necessary under the circumstances).        Many of these cases are

instructive as to how Gant must be applied to cases involving

carried containers.

          In   Shakir,   the   Third    Circuit    was   faced    with     the

warrantless search of a gym bag initially held by an arrestee.

616 F.3d at 316.    The defendant there argued that the search of

his bag was in violation of his Fourth-Amendment rights because he

was already handcuffed at the time of the search and could not

have accessed the bag.    Id. at 317.      In response, the government

cited several cases upholding searches conducted while an arrestee

was handcuffed.    Id.   However, the Third Circuit noted that the

government relied solely on pre-Gant cases.        Id. at 318.    The court

emphasized "Gant as refocusing [its] attention on a suspect's

ability (or inability) to access weapons or destroy evidence at

the time a search incident to arrest is conducted."              Id.     Thus,

the Shakir court was "left to consider, under Gant and other

relevant precedents, whether [the defendant] retained sufficient

potential access to his bag to justify a warrantless search."              Id.

at 319.

          In   considering     that    question,   our   sister        circuit

"underst[ood] Gant to stand for the proposition that police cannot

search a location or item when there is no reasonable possibility


                                 - 43 -
that the suspect might access it."           Id. at 320.      In accordance

with that principle, it held that "a search is permissible incident

to a suspect's arrest when, under all the circumstances, there

remains a reasonable possibility that the arrestee could access a

weapon or destructible evidence in the container or area being

searched."   Id. at 321.    Applying this legal standard to the facts

there, the Third Circuit concluded that the search was justified

because there was a "sufficient possibility" that the arrestee

could have gained access to the bag.          Id.     The court found this

even though the arrestee was handcuffed because the bag was at his

feet, he was in a public area surrounded by approximately twenty

bystanders, and there was at least one suspected confederate in

the area.    Id. at 316, 321.

            The   Ninth   Circuit    confronted     similar   questions   in

assessing the validity of a warrantless backpack search in Cook.

808 F.3d at 1199-1200.     There, the arrestee was wearing a backpack

at the time the officers approached him.          Id. at 1197.    While the

arrestee was handcuffed on the ground, but within one to two

minutes of his arrest, officers picked up the arrestee's backpack,

which was right next to the arrestee, and conducted a twenty- or

thirty-second cursory search.         Id.    The officers then took the

arrestee to a more secluded area several blocks away and performed

a more thorough search of the backpack.             Id.   The arrestee only

challenged the validity of the first cursory search of his backpack


                                    - 44 -
immediately following his arrest.       Id. at 1198.       Relying on Gant,

our sister circuit found that "[t]he brief and limited nature of

the [initial] search, its immediacy to the time of arrest, and the

location of the backpack ensured that the search was 'commensurate

with   its     purposes    of   protecting     arresting        officers   and

safeguarding any evidence of the offense of arrest that [the

arrestee] might conceal or destroy.'"         Id. at 1200 (quoting Gant,

556 U.S. at 339).

             In Davis, the Fourth Circuit examined the history of the

search-incident-to-arrest       exception    and   how   Gant    altered   its

understanding of that exception.       997 F.3d at 195-200.         The Davis

court found that Gant's first holding, "that police can 'search a

vehicle incident to a recent occupant's arrest only when the

arrestee is unsecured and within reaching distance of the passenger

compartment at the time of the search'" -- a holding derived from

Chimel -- applies outside of the automobile context.               Id. at 197

(quoting Gant, 556 U.S. at 343).

             After establishing Gant's applicability outside of the

automobile search context, the Fourth Circuit analyzed whether the

warrantless search of a backpack was permissible under Gant.               Id.

at 198.   In Davis, the arrestee fled from officers while carrying

his backpack but ultimately became bogged down in a swamp with

knee-high water.     Id.   An officer drew his weapon and ordered the

arrestee out of the swamp.      Id.   The arrestee complied and dropped


                                  - 45 -
his backpack on the ground; he then laid down and was handcuffed.

Id.    Two other officers arrived at the scene, and the officers

searched the backpack that was not within the arrestee's reaching

distance.     Id.

             The Fourth Circuit then held that the warrantless search

of the backpack was unlawful, reasoning that there was "no doubt

that [the arrestee] was secured and not within reaching distance

of his backpack when [the officer] unzipped and searched it."                   Id.

At    the   time    of   the    search,    the   arrestee   was   face   down   and

handcuffed, he was outnumbered by officers three to one, and the

events had occurred in a residential area with no other people

present; the court thus had "no difficulty" in determining that

the arrestee was secured.            Id.   The court also emphasized that the

arrestee was not within reaching distance of the backpack at the

time of the search.            Id.

             F. The Impact of Modern Authority on Eatherton

             In examining the above cases carefully, I agree with the

majority that we do not have a Supreme Court opinion that is

"directly on point contradicting our precedent" in Eatherton.

United States v. Wurie, 867 F.3d 28, 34 (1st Cir. 2017).                 However,

I remain convinced that the "less common exception" to the law-

of-the-circuit       doctrine        forecloses    our   present    reliance     on

Eatherton.         The    authorities      discussed     above,    "although    not

directly controlling, offer[] a sound reason for believing that


                                        - 46 -
the [Eatherton] panel would change its collective mind."    Id.   "A

Supreme Court opinion need not be directly on point to undermine

one of our opinions."    United States v. Holloway, 630 F.3d 252,

258 (1st Cir. 2011).    Further, a decision of the Supreme Court

"can extend through its logic beyond the specific facts of its

case."   Id. (quoting Los Angeles Cnty. v. Humphries, 562 U.S. 29,

38 (2010)).

          Unlike the district court, who must apply our "precedent

unless it has unmistakably been cast into disrepute by supervening

authority," the exceptions to the law-of-the-circuit doctrine

provide us with "modest" flexibility in the application of our own

precedents.   Eulitt ex rel. Eulitt v. Me. Dep't of Educ., 386 F.3d

344, 349 (1st Cir. 2004), abrogated on other grounds by Carson as

next friend of O.C. v. Makin, 596 U.S. 767 (2022).     The majority

decision stresses that the second exception to the law-of-the-

circuit doctrine "cannot depend on whether there are sound reasons

to conclude that the prior panel got it wrong."   However, the scope

of the exception applied here is not based on whether I believe

there are sound reasons to conclude that the Eatherton panel was

wrong, but rather whether there are sound reasons for believing

that the Eatherton panel would have changed its collective mind.

And this "sound reason" standard has been reiterated by this court.

See e.g., Lewis, 963 F.3d at 23; United States v. López, 890 F.3d

332, 340 (1st Cir. 2018); Wurie, 867 F.3d at 34.


                              - 47 -
          Given that scope, in my view, had the Eatherton panel

had the benefit of both Chadwick and Gant, that panel would have

changed its collective mind as to its interpretation of the

search-incident-to-arrest doctrine.         As our sister circuits have

concluded,   Chadwick   and,    perhaps     even    more   so,    Gant    have

unquestionably     altered        our       understanding         of      the

search-incident-to-arrest      doctrine    and     "provide   a   clear   and

convincing basis" to determine that the Eatherton panel too would

have come to a different conclusion on the issue.             See Guerrero,

19 F.4th at 552.

          Chadwick made a nuanced distinction between the reduced

expectation of privacy an arrestee has of their person as compared

to possessions within their immediate control at the time of

arrest.   433 U.S. at 16 n.10.      Further, Chadwick's analysis did

not hinge on whether the possession was held by the arrestee or

was elsewhere in their vicinity.        Instead, Chadwick focused on the

nature of containers as "repositor[ies] of personal effects."7 Id.


     7 Indeed, the Supreme Court seems to agree that the result in
Chadwick would not have been different had the arrestee been
"drag[ging] [the trunk] behind them." Riley v. California, 573
U.S. 373, 394 (2014) (acknowledging the difference between the
trunk in Chadwick -- which could hold a large number of personal
items and required a warrant to search -- and "a container the
size of [a] cigarette package" at issue in Robinson). In my view,
Riley lends support for the very line-drawing about different
carried containers that Eatherton believed it was unable to make.
The majority appears to suggest that Riley distinguishes between
personal property that is difficult to carry, either due to its
size or weight, and personal property that is commonly carried,


                                 - 48 -
at 13.     Thus, although the Eatherton panel was understandably

influenced by the then-recent cases of Edwards, Robinson, and

Gustafson when assessing an arrestee's privacy interests, Chadwick

would    have   provided   the   additional   context   that   "possessions

within an arrestee's immediate control cannot be justified by any

reduced expectations of privacy caused by the arrest."            433 U.S.

at 16 n.10 (emphasis added).

            Given this understanding and Gant's refined framework

for "immediate control" searches, the Eatherton panel would have

centered    its   analysis   around   "immediate   control"    rather   than

shoehorning the search of a closed container into being "of the

person."    Specifically, I believe this modern authority would have

led the Eatherton panel to the conclusion, under Chadwick and Gant,

that searches of visible containers held or carried by an arrestee

-- like the briefcase in Eatherton -- must be treated as "immediate



such as a briefcase. See Majority at 30. I do not think this was
the Riley Court's intent. Riley notes that "[m]ost people cannot
lug around every piece of mail they have received for the past
several months, every picture they have taken, or every book or
article they have read -- nor would they have any reason to attempt
to do so." Id. at 393-94. But, the Riley Court then states that
the only way for a person to carry personal property like that
(prior to the existence of cell phones) would be to "drag behind
them a trunk of the sort held to require a search warrant in
Chadwick."    Id. at 394.     In my view, the Riley Court was
differentiating between certain containers that may be receptacles
for other personal property and small containers like those the
size of a cigarette package, while emphasizing that a container
like the trunk in Chadwick would have required a search warrant
just as a cell phone would. Id. at 394.


                                   - 49 -
control" searches.          See Knapp, 917 F.3d at 1167 (limiting Robinson

searches      to   "searches        of   an    arrestee's       clothing,       including

containers concealed under or within her clothing" and holding

that "visible containers in an arrestee's hand . . . are best

considered to be within the area of an arrestee's immediate

control").

              Further,      the    parties      here     have      not   identified    any

post-Gant      published      circuit         opinions      that    adopted     the   same

approach taken in Eatherton.              Indeed, we have found the opposite:

circuits    that     once    took    an    Eatherton-like           approach     to   cases

involving carried containers now applying the "immediate control"

analysis in similar circumstances.                  Cf. United States v. Lewis,

963 F.3d 16, 24 (1st Cir. 2020) (adhering to the law-of-the-circuit

doctrine where three sister circuits retained allegiance to this

Circuit's reasoning despite a recent Supreme Court decision);

Sanchez v. United States, 740 F.3d 47, 57 (1st Cir. 2014) (finding

that just two circuits' decisions contrary to our precedent "hardly

paint a picture of a rush to the exit so as to allow us to overrule

our   own     controlling         precedent").         In    short,      the    continued

application of Eatherton simply "runs counter to the strong modern

trend in the caselaw."             United States v. Guerrero, 19 F.4th 547,

557 (1st Cir. 2021).

              Accordingly, I find "that the gloss added by the Supreme

Court"   to    the   search-incident-to-arrest                exception        requires   a


                                          - 50 -
different approach than that taken by the Eatherton panel.            United

States v. Rodriguez, 527 F.3d 221, 225 (1st Cir. 2008).              Had the

Eatherton panel had the benefit of viewing that case "through the

prism of" Chadwick and Gant, I believe that they would have come

to a different result.       Id. at 226; see Guerrero, 19 F.4th at 559

("The bottom line [] is that given the Supreme Court cases in vogue

after [our prior decision], we believe [that] panel would (if it

had the chance) reverse its view of the . . . issue 180 degrees.").

           For these reasons, I would find that Eatherton is no

longer the law of the circuit. Instead, the appropriate rule under

Chadwick   and   Gant   is   that   the   searches   of   visible,    closed

containers held or carried by an arrestee should be analyzed as

"immediate control" searches.

                   II. Fourth-Amendment Violation

           Because I would hold that Eatherton is no longer the law

of the circuit and that the search of the backpack here should be

treated as an immediate control search, the next step is to

determine whether the search was nonetheless justified under the

circumstances presented.      Appropriate factors to be considered in

that inquiry are: "(1) whether the arrestee is handcuffed; (2) the

relative number of arrestees and officers present; (3) the relative

positions of the arrestees, officers, and the place to be searched;

. . . (4) the ease or difficulty with which the arrestee could

gain access to the searched area"; and (5) "the degree to which


                                    - 51 -
arresting officers have separated an article from an arrestee at

the time of the search."     Knapp, 917 F.3d at 1168-69.

          The district court made the necessary factual findings

to support a conclusion that the search of Perez's backpack was

violative of his Fourth-Amendment rights. The district court found

that "Perez was secured in handcuffs on the ground under [one

officer's] supervision as [another officer] was searching the

backpack on the hood or roof of [one of the officer's] vehicle,

not within reaching distance of Perez, so destruction of evidence

or access to weapons was not at stake."8       Accordingly, I would find

that under the immediate control analysis, the search of Perez's

backpack was in contravention with the warrant requirement of the

Fourth    Amendment    and      did      not      fall    within    the

search-incident-to-arrest exception.

                           III. Good Faith

          Finding that the search of Perez's backpack violated the

Fourth Amendment, however, is not the end of the inquiry.           The



     8 The government has argued before us that the backpack was
near Perez at the time of the search and that "there was a
reasonable possibility that he could access the bag," and the
search was therefore justified under the immediate control
analysis. However, it has not pointed us to any support to find
that the district court's determinations regarding Perez's
inability to reach the backpack at the time of the search were
clearly erroneous. See United States v. Oquendo-Rivas, 750 F.3d
12, 16 (1st Cir. 2014) ("We assess questions of fact . . . for
clear error."). I also do not surmise any support in the record
to find a clear error in the district court's factual findings.


                                - 52 -
Fourth Amendment "says nothing about suppressing evidence obtained

in violation of [its] command."    Davis v. United States, 564 U.S.

229, 236 (2011).    I must thus determine if the exclusionary rule

is applicable here.    "The rule's sole purpose . . . is to deter

future Fourth[-]Amendment violations" and not to redress prior

violations.   Id. at 236-37.      "Our cases have thus limited the

rule's operation to situations in which this purpose is 'thought

most efficaciously served.'"   Id. at 237 (quoting United States v.

Calandra, 414 U.S. 338, 348 (1974)).

          "When the police exhibit 'deliberate,' 'reckless,' or

'grossly negligent' disregard for Fourth[-]Amendment rights, the

deterrent value of exclusion is strong and tends to outweigh the

resulting costs."   Id. at 238 (quoting Herring v. United States,

555 U.S. 135, 144 (2009)).     On the other hand, "when the police

act with an objectively reasonable good-faith belief that their

conduct is lawful . . . or when their conduct involves only simple,

isolated negligence[,] . . . the deterrence rationale loses much

of its force, and exclusion cannot pay its way."      Id. (internal

quotations omitted).   "The government bears the burden of showing

that its officers acted with objective good faith."   United States

v. Sheehan, 70 F.4th 36, 51 (1st Cir. 2023) (quoting United States

v. Brunette, 256 F.3d 14, 17 (1st Cir. 2001)).

          The good-faith exception may be triggered "when the

police conduct a search in objectively reasonable reliance on


                               - 53 -
binding    judicial   precedent."      Davis,    564   U.S.   at   239.   But

importantly, this "exception is available only where the police

rely on precedent that is clear and well-settled."             United States

v. Sparks, 711 F.3d 58, 64 (1st Cir. 2013) (cleaned up).             "[W]here

judicial    precedent   does   not    clearly    authorize     a   particular

practice, suppression has deterrent value because it creates an

'incentive to err on the side of constitutional behavior.'" United

States v. Bain, 874 F.3d 1, 20 (1st Cir. 2017) (quoting Sparks,

711 F.3d at 64).

            Had this case fallen within the first exception to the

law-of-the-circuit doctrine -- where "the holding of a previous

panel is contradicted by subsequent controlling authority" -- the

good-faith exception would plainly not apply.             See Barbosa, 896

F.3d at 74.     For example, imagine a scenario where, post-Gant,

officers searched a vehicle incident to a recent occupant's arrest

after the occupant was secured and not within reaching distance of

the passenger compartment and without probable cause that the

vehicle contained evidence of the offense of arrest.               Regardless

of whether prior circuit law allowed this practice, that search

would be unlawful post-Gant, and the officers could not rely on

good faith.

            Admittedly,    when      the     second    exception     to   the

law-of-the-circuit doctrine applies, as I believe it does here,

there is a much closer question as to whether the good-faith


                                    - 54 -
exception applies.        Ultimately, given the deterrent value of

enforcing a regime where officers err on the side of constitutional

conduct in the face of unclear or eroded precedent, I would not

permit good faith to bar exclusion in this case.

            First and foremost, for the same reasons that I find the

second exception to the law-of-the-circuit doctrine applies here,

I am of the view that Eatherton was not the kind of "clear and

well-settled" precedent that officers could reasonably rely on.

See Sparks, 711 F.3d at 64. At the very minimum, Gant -- a landmark

case in our Fourth-Amendment jurisprudence -- called into question

the continued vitality of Eatherton.              It would be untenable to

require that Supreme Court holdings address virtually identical

factual   scenarios     before    we    consider       our    circuit     precedent

undermined and reject application of the good-faith exception.

Such a requirement would be contrary to the requirement that the

precedent   officers    rely     upon   "be    unequivocal"      when     shielding

unlawfully obtained evidence from exclusion.                 Sparks, 711 F.3d at

64.

            Second,    this   conclusion       aptly   aligns     with    the   very

purpose of the exclusionary rule: to deter future Fourth-Amendment

violations.     Davis, 564 U.S. at 236-37.                   If we do not strip

precedent     that    falls    within    the     second       exception    to   the

law-of-the-circuit doctrine of its weight as forcefully as we do

in cases under the first exception, officers would be encouraged


                                    - 55 -
to adhere to shaky precedent (no matter how potentially abrogated)

until those cases are formally and explicitly overruled.                     Because

suppression is intended to create the "incentive to err on the

side     of   constitutional        behavior,"     I     think   the    appropriate

conclusion is that when opinions authored by the Supreme Court,

particularly landmark cases like Gant, call into question our prior

precedent,      officers     must    conform     their    conduct      to   the   more

protective reading of the Fourth Amendment laid out by the Supreme

Court.    See Bain, 874 F.3d at 20 (quoting Sparks, 711 F.3d at 64).

              Finally, this is not a case where "the police engage[d]

in conduct that complie[d] with existing precedent, and the law

later change[d]."       United States v. Baez, 744 F.3d 30, 33 (1st

Cir. 2014).      Gant was decided a decade before the search at issue

here occurred, and Chadwick's guidance on closed containers has

been binding precedent for over forty years.                Cf. Sparks, 711 F.3d

at 67 (finding good faith applied where the applicable Supreme

Court    case   came   out    three    years     after    the    search     at    issue

occurred); United States v. Moore-Bush, 36 F.4th 320, 359 (1st

Cir. 2022) (mem.) (Barron, C.J., concurring) (concurring opinion

finding that good faith applied when the applicable Supreme Court

decision was published over one year after the search began).

Given my view of the impact of these cases on Eatherton, the

officers were required to follow the logic supplied by Gant and

Chadwick.


                                       - 56 -
           For these reasons, I would conclude that the good-faith

exception is not available under the circumstances and suppression

is the proper outcome to deter future Fourth-Amendment violations.

                              IV. Conclusion

           For the above stated reasons, I would abrogate Eatherton

to the extent it is inconsistent with this analysis, reverse the

district court's decision on the motion to suppress, vacate the

judgment   of   conviction,    and   remand    for   further   proceedings

consistent with this opinion.




                                 - 57 -

```

---

## GROUP: content/cases/United States v. Porter.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Porter
type: case
citation: "No. 25-60163, slip op. (5th Cir. 2026)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir.
court_level: coa
circuit: ca5
year: 2026
date_decided: 2026-03-17
docket: 25-60163
authority_weight: "Binding in-circuit — 5th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10810059/united-states-v-porter/"
  cluster_id: 10810059
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Porter
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (ALPR)"
related:
  - "[[Carpenter v. United States]]"
  - "[[United States v. Knotts]]"
  - "[[Terry Stops and Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - license-plate-reader
  - digital-surveillance
  - plain-view
  - reasonable-suspicion
  - fifth-circuit
holding: "A police officer's use of a fixed license plate reader (LPR) to detect that a vehicle passed a public intersection is not a Fourth Amendment search and requires no warrant; the ensuing traffic stop was supported by reasonable suspicion, the officer lawfully seized a firearm and machinegun conversion switch he saw in plain view, and circuit precedent foreclosed the Second Amendment challenge, so the machinegun conviction was affirmed."
aliases:
  - United States v. Porter
  - "United States v. Porter (5th Cir. 2026)"
  - United States v. Elijah Porter
---

# United States v. Porter

*No. 25-60163, slip op. (5th Cir. 2026)* · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10810059 → published opinion 11276804 (Smith, J.; No. 25-60163, decided Mar. 17, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (published 5th Cir. slip; no F.4th reporter cite assigned yet — S2 A3). S9 promotes. -->

## Background
While on patrol in Gautier, Mississippi, Officer Hoggard received an LPR alert that a plate associated with criminal activity had passed a particular intersection; dispatch tied the vehicle to Elijah Porter, who had an outstanding aggravated-assault warrant. A computer check corroborated the association, and Hoggard located and stopped the vehicle. After identifying Porter and patting him down, Hoggard saw a firearm protruding from under the driver's seat with "a little silver switch" he took to be a machinegun conversion device; he later retrieved the Glock and switch during an inventory search. Porter was charged under 18 U.S.C. § 922(o) and moved to suppress the LPR data and the firearm.

## Issue
Whether the officer's use of an LPR to detect Porter's vehicle was a Fourth Amendment search, and whether the stop and seizure of the firearm were lawful.

## Rule
The court disposed of the Fourth Amendment claims and the § 922(o) challenge together at the outset: "Because the use of an LPR did not constitute a search, no warrant was required; the stop was supported by reasonable suspicion, and the officer found the Glock and its machinegun conversion switch in plain view. Our circuit precedent forecloses Porter's Second Amendment challenge. We affirm." — slip op. at 1. ^pin-slip1

## Application
Detecting a plate as the vehicle passed a fixed public-road camera revealed only a vehicle's public movement and did not invade a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], so it was no search and needed no warrant. The LPR alert plus the confirmed link to a person with an active warrant supplied reasonable suspicion (indeed probable cause) for the stop. Once Porter was stopped, the barrel and switch were visible under the seat, bringing the firearm within the [[Plain View Doctrine|plain-view doctrine]]; its incriminating character (an apparent automatic Glock) was immediately apparent.

## Conclusion
**Affirmed.** Judge Jerry E. Smith wrote for the panel (Smith, Wiener, Higginson, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Porter* sits alongside *[[Robinson v. Commonwealth]]* on the ALPR frontier: like Norfolk's Flock system, a fixed LPR that captures a plate on a public road is treated as no search under the public-movements logic of *[[United States v. Knotts|Knotts]]*, distinguished from the pervasive tracking that made *[[Carpenter v. United States|Carpenter]]* a search.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (ALPR)*

## Sources
- [*United States v. Porter*, No. 25-60163, slip op. (5th Cir. 2026)](https://www.courtlistener.com/opinion/10810059/united-states-v-porter/) — pinpoint: slip op. at 1 (LPR use is not a search; plain-view firearm seizure; reasonable-suspicion stop). Rule quote string-matched to the CL opinion text 2026-07-07. Published 5th Cir. slip; no F.4th cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0e9fb4703e4cdd65", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 25-60163, slip op. (5th Cir. 2026)", "court": "5th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Porter", "year": "2026"}}
{"assertion_id": "2d66a61b2921604d", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Lower-court development (ALPR)", "title": "United States v. Porter"}}
{"assertion_id": "c048b6dd5c903979", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A police officer's use of a fixed license plate reader (LPR) to detect that a vehicle passed a public intersection is not a Fourth Amendment search and requires no warrant; the ensuing traffic stop was supported by reasonable suspicion, the officer lawfully seized a firearm and machinegun conversion switch he saw in plain view, and circuit precedent foreclosed the Second Amendment challenge, so the machinegun conviction was affirmed.", "title": "United States v. Porter"}}
{"assertion_id": "8294679477e1aee4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Porter", "varies_by_point": "false"}}
{"assertion_id": "e02ee312d83e3f4f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "United States v. Porter"}}
```

### lake record — United States v. Porter

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Porter",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Porter",
    "case_name_short": "Porter",
    "case_name_full": "",
    "input_case_name": "United States v. Porter",
    "court": "5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2026-03-17",
    "year": 2026,
    "docket": "25-60163",
    "cluster_id": 10810059,
    "lead_opinion_id": 11276804,
    "sibling_ids": [],
    "absolute_url": "/opinion/10810059/united-states-v-porter/",
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
      "note": "W9 slip disposition. United States v. Porter (Elijah Porter), 5th Cir. PUBLISHED slip No. 25-60163, decided 2026-03-17 (ALPR identification / plain-view firearm). CL cluster 10810059 Published, citations[] empty (live-verified 2026-07-07); no F.4th cite assigned yet.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.ca5.uscourts.gov/opinions/pub/25/25-60163-CR0.pdf",
          "cite": "No. 25-60163 (5th Cir.) PUBLISHED, filed 2026-03-17"
        },
        {
          "source": "Justia",
          "url": "https://law.justia.com/cases/federal/appellate-courts/ca5/25-60163/25-60163-2026-03-17.html",
          "cite": "No. 25-60163 (5th Cir. 2026), no F.4th cite listed"
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
    "warnings": [],
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
      "from_record_id": "united-states-v-porter--10810059",
      "to_record_id": "United States v. Porter",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Porter

```
Case: 25-60163       Document: 89-1       Page: 1   Date Filed: 03/17/2026




        United States Court of Appeals
             for the Fifth Circuit
                             ____________                          United States Court of Appeals
                                                                            Fifth Circuit


                               No. 25-60163
                                                                          FILED
                                                                    March 17, 2026
                             ____________
                                                                     Lyle W. Cayce
United States of America,                                                 Clerk

                                                         Plaintiff—Appellee,

                                   versus

Elijah Porter,

                                        Defendant—Appellant.
               ______________________________

               Appeal from the United States District Court
                 for the Southern District of Mississippi
                         USDC No. 1:24-CR-11-1
               ______________________________

Before Smith, Wiener, and Higginson, Circuit Judges.
Jerry E. Smith, Circuit Judge:
       Elijah Porter was charged with possession of a machinegun in violation
of 18 U.S.C. § 922(o). He challenges (1) the denial of his motion to suppress
vehicle-location data obtained from a license plate reader (“LPR”) and a
firearm obtained in a vehicle search and (2) the district court’s ruling that
18 U.S.C. § 922(o) is not unconstitutional. Because the use of an LPR did
not constitute a search, no warrant was required; the stop was supported by
reasonable suspicion, and the officer found the Glock and its machinegun
conversion switch in plain view. Our circuit precedent forecloses Porter’s
Second Amendment challenge. We affirm.




                                      1
Case: 25-60163        Document: 89-1       Page: 2    Date Filed: 03/17/2026




                                  No. 25-60163


                            I. Factual Background
                           A. Evidentiary Hearing
       At the suppression hearing, the district court heard testimony from
Charles Hoggard, a former officer for the Gautier Police Department. Video
footage from Hoggard’s body camera was also presented.

                       1. Officer Hoggard’s Testimony
       While on patrol in January 2024, Hoggard received an alert on his
phone that an LPR located at a specific intersection captured the license
plate of a vehicle that was associated with criminal activity. He contacted
dispatch and was told that the vehicle was “associated with” Elijah Porter,
who had a warrant for aggravated assault. Hoggard conducted a computer
check for the license plate, which revealed the vehicle was associated with
“James Stewart” or “E.L. Porter.” He located the vehicle and conducted a
traffic stop.
       After identifying Porter as the driver, Hoggard detained him and pat-
ted him down. Hoggard observed a firearm protruding from under the
driver’s seat. He was able to see the slide and barrel of the firearm, and a
“little silver switch on the back of it,” which he “believed to be the switch of
an automatic [G]lock.” Hoggard asked Porter if there were any weapons in
the car “to see if he was going to be honest” and later retrieved the firearm
during an inventory search of the vehicle, at which point he had not yet con-
firmed that “the warrant was valid and true.” After Hoggard secured the
firearm in his patrol car, the warrant was confirmed, and he took Porter to
the police station.
       Hoggard stated that the LPR system allowed him to see when a vehi-
cle had passed an LPR camera at a particular location, and he estimated there
were no more than ten LPR cameras stationed across Gautier. He did not
know how long the location data was stored within the LPR system, but he




                                       2
Case: 25-60163        Document: 89-1       Page: 3    Date Filed: 03/17/2026




                                  No. 25-60163


“could look and see how many times [a vehicle] passed within the general . . .
time period.” Hoggard stated there had been other LPR “hits” on Porter’s
vehicle earlier that day and the day before, but he was not able to locate the
vehicle on those occasions because of heavy traffic. He acknowledged that
he did not have a physical description of Porter when he initiated the traffic
stop. Hoggard also noted that after seeing the firearm, he left it in Porter’s
unlocked car, which was in a residential area, and did not immediately tell his
colleague at the scene about the weapon.

                           2. Body Camera Footage
       The footage is consistent with Hoggard’s testimony. Hoggard patted
Porter down next to the open driver’s side door and asked if he had any weap-
ons, to which Porter said he did not. Hoggard then removed several personal
items from Porter’s pockets and placed them on the driver’s seat. Just as
Hoggard turned toward the driver’s seat, he asked Porter if there were any
weapons in the car—Porter answered no. As Hoggard put Porter into his
patrol unit, Hoggard removed an earbud from Porter’s ear and returned to
Porter’s car to place it on the driver’s seat with his other belongings.
       Hoggard then locked Porter’s car and told his colleague that he had to
confirm “the hit.” He returned to Porter’s vehicle, opened the center con-
sole, and looked underneath the driver’s seat. Immediately thereafter, he
tried to flag down his colleague. Hoggard then reached under the driver’s
seat, pulled out a firearm, and said, “Oh, s--t.” The firearm was not visible
on the video until this point. Hoggard motioned again for his colleague to
come over and told him there’s “a f--king switch on that [G]lock.” Hoggard
then said, “it was basically in plain view,” and “the barrel [was] sticking out
from under the seat, so I saw it in plain view.”

                            3. Porter’s Arguments
       Porter asserts that the use of LPR cameras to detect his vehicle’s




                                       3
Case: 25-60163         Document: 89-1         Page: 4     Date Filed: 03/17/2026




                                    No. 25-60163


location constituted a search under the Fourth Amendment and that the
vehicle-location data should be suppressed. He posits that he had a reasona-
ble expectation of privacy in his location and movements that were captured
by the LPR cameras and that a warrant was required for police to obtain such
data from the LPR system. Porter also urges that the traffic stop was invalid
because it was not supported by reasonable suspicion and that the firearm
should be suppressed. Porter theorizes that even if the stop were lawful, the
firearm was not in plain view and was not discovered during a lawful
inventory search. And Porter claims that § 922(o) violates the Second
Amendment, both facially and as applied to him. 1

                           B. District Court’s Rulings
       In a bench ruling, the district court determined that § 922(o) is not
unconstitutional and denied Porter’s motion to dismiss the indictment. The
court denied his motion to suppress the vehicle-location data, reasoning that
“an individual traveling in an automobile on public thoroughfares has no rea-
sonable expectation of privacy in their movements from one place to
another” and “motorists do not have a privacy interest in their license
plates,” since they are “constantly open to plain view of” passersby.
       The court requested supplemental briefing on the threshold issue of
whether the traffic stop was lawful. The court then stated that if the stop was
valid, it would deny the motion to suppress based on its finding that the plain-
view doctrine applied.       The court also determined that the inevitable-
discovery doctrine would apply because the firearm would have been found
during the inventory search.
       After the parties submitted the requested supplemental briefing, the
       _____________________
       1
         Although he did at the district court, Porter does not make a Commerce Clause
challenge on appeal.




                                          4
 Case: 25-60163           Document: 89-1           Page: 5       Date Filed: 03/17/2026




                                        No. 25-60163


court concluded that the traffic stop was lawful, denied Porter’s motion to
suppress, and explained that the stop was valid for three reasons:
        First, Officer Hoggard, had reasonable suspicion to initiate the
        traffic stop based solely on the automatic license plate reader,
        or the ALPR, hit that revealed an outstanding arrest warrant
        for Mr. Porter; Number 2, the [“be on the lookout”] BOLO
        [report], or ALPR, hit does not need to include a physical de-
        scription of the driver to provide an officer reasonable suspi-
        cion to initiate a traffic stop; and number 3, under the collective
        knowledge doctrine, the ALPR was reliable and provided Offi-
        cer Hoggard with reasonable suspicion to initiate the traffic
        stop.
Thereafter, Porter consented to a bench trial, 2 where he was found guilty.

                           II. Denial of Motion to Suppress
        When reviewing the denial of a suppression motion, we review factual
findings for clear error and legal conclusions—“including whether an expec-
tation of privacy is reasonable under the circumstances”—de novo. United
States v. Gomez, 276 F.3d 694, 697 (5th Cir. 2001) (internal quotation marks
and citation omitted). The evidence is “viewed in the light most favorable to
the Government, as the prevailing party below.” United States v. Garcia,
99 F.4th 253, 266 (5th Cir. 2024). We “uphold the district court’s ruling if
there is any reasonable view of the evidence to support it.” United States v.
Alvarez, 40 F.4th 339, 344 (5th Cir. 2022) (internal quotation marks and cita-

        _____________________
        2
          Porter’s jury-trial waiver, the one that he, his counsel, the prosecutor, and district
judge signed, notes that Porter was “fully informed of [his] right to a trial by jury,”
“waive[d] that right,” and “waive[d] [his] right to special findings.” Some of the stipula-
tions, that Porter “knowingly and voluntarily” agreed to, include that “Officer Hoggard
. . . received an alert for a 2017 White Ford Fusion . . . associated with an outstanding
arrest warrant for Elijah Porter” and “Elijah Porter was the driver, and sole occupant of
the Ford Fusion.”




                                               5
 Case: 25-60163         Document: 89-1            Page: 6      Date Filed: 03/17/2026




                                      No. 25-60163


tion omitted).
       And “[w]hen the denial of a motion to suppress is based on live testi-
mony, the clearly erroneous standard is particularly strong because the judge
had the opportunity to observe the demeanor of the witnesses.” United
States v. Jefferson, 89 F.4th 494, 502 (5th Cir. 2023) (internal quotation marks
and citation omitted). “Where testimony conflicts with video evidence, our
court must view the ‘facts in the light depicted by the videotape,’” 3 but
“[w]hen video evidence is ‘ambiguous,’” no such consideration applies. 4

                                           III.
                              A. Vehicle Location Data
       Contrary to Porter’s assertion, the use of an LPR system did not
invade any reasonable expectation of privacy and did not constitute a search,
so no warrant was required.
       Where an individual has a reasonable expectation of privacy, “official
intrusion into that private sphere generally qualifies as a search and requires
a warrant supported by probable cause.” United States v. Smith, 110 F.4th
817, 830 (5th Cir. 2024) (internal quotation marks and citation omitted), cert.
denied, 146 S. Ct. 356 (2025). “A person does not surrender all Fourth
Amendment protection by venturing into the public sphere,” Carpenter v.
United States, 585 U.S. 296, 310 (2018), but “[a] person travel[]ing in an
automobile on public thoroughfares has no reasonable expectation of privacy
in his movements from one place to another,” United States v. Knotts,
460 U.S. 276, 281 (1983).

       _____________________
       3
         See United States v. Anderson, No. 23-50110, 2024 WL 2829243, at *1 (5th Cir.
2024) (per curiam) (unpublished) (citing Scott v. Harris, 550 U.S. 372, 380-81 (2007)).
       4 See id. (citing Aguirre v. City of San Antonio, 995 F.3d 395, 410 (5th Cir. 2021)).




                                             6
 Case: 25-60163           Document: 89-1           Page: 7       Date Filed: 03/17/2026




                                        No. 25-60163


        The LPR system provides periodic information about a vehicle’s
location on “public streets and highways.” A scan occurs when a vehicle
passes one of the locations where a camera is stationed. 5 The LPR system is
not capable of tracking the “whole of [an individual’s] physical movements,”
much less “for a very long period,” to the extent that a cell phone can
because the LPR system does not “faithfully follow[]” individuals “beyond
public thoroughfares.” 6 Indeed, Hoggard’s previous inability to locate Por-
ter’s vehicle, notwithstanding the earlier “hits” and the LPR technology’s
around-the-clock capabilities, illustrates the significant limitations of this
technology relative to cell-site location information (“CSLI”), which can
“provide[] an intimate window into a person’s life, revealing not only his par-
ticular movements, but through them his familial, political, professional,
religious, and sexual associations.” Carpenter, 585 U.S. at 311 (internal quo-
tation marks and citation omitted).
        With a gloss from Olabisiomotosho v. City of Houston, 7 which made
clear that “[a] motorist has no privacy interest in their [sic] license plate
number,” the LPR system is more analogous to the beeper signals in Knotts 8

        _____________________
        5
          See Knotts, 460 U.S. at 281 (reasoning that law enforcement’s monitoring the
beeper signals after placing a hidden beeper in a barrel of drug-precursor chemicals (which
was later purchased by the suspect’s accomplice and placed in the suspect’s vehicle)
“amounted principally to the following of an automobile on public streets and highways”
and did not constitute a search).
        6
          Cf. Carpenter, 585 U.S. at 310–11 (“A cell phone faithfully follows its owner
beyond public thoroughfares and into private residences, doctor’s offices, political head-
quarters, and other potentially revealing locales.”).
        7
         See Olabisiomotosho, 185 F.3d 521, 529 (5th Cir. 1999) (holding that the police did not
need probable cause to use an onboard computer to check a stranded motorist’s license plate
number since “[a] motorist has no privacy interest in their license plate number”).
        8
          See Knotts, 460 U.S. at 277–79, 285 (noting that the beeper transmitted periodic
radio signals that enhanced the police’s ability to surveil the vehicle’s movements and
allowed police to track the vehicle to a drug lab); see also id. at 285 (reasoning that a “sci-




                                               7
 Case: 25-60163           Document: 89-1           Page: 8       Date Filed: 03/17/2026




                                        No. 25-60163


than to the CSLI at issue in Carpenter. True, the LPR system allows the
government to access an historical record for some time, and that type of
retrospective data can allow police to “travel back in time to retrace a per-
son’s whereabouts” without needing to “know in advance whether they
want to follow a particular individual, or when.” 9 But the LPR technology
in the instant case provides only periodic information about a vehicle’s loca-
tion when a vehicle passes one of its ten locations where an LPR camera is
stationed in Gautier and is much more limited than CSLI and geofence 10
data, which is capable of capturing a greater volume of comprehensive infor-
mation with a higher degree of quality and precision. 11




        _____________________
entific enhancement of this sort raises no constitutional issues which visual surveillance
would not also raise”).
        9
           See Carpenter, 585 U.S. at 312; see also Smith, 110 F.4th at 834 (expressing “par-
ticular concern” with “the fact that a geofence will retroactively track anyone with Loca-
tion History enabled, regardless of whether a particular individual is suspicious or moving
within an area that is typically granted Fourth Amendment protection”).
        10
           Though geofences are typically limited to a discrete time period, “a brief snap-
shot can expose highly sensitive information,” such as a person’s “visit to ‘the psychiatrist,
the plastic surgeon, the abortion clinic, the AIDS treatment center, the strip club, the crim-
inal defense attorney, the by-the-hour-motel, the union meeting, the mosque, synagogue or
church, [or] the gay bar,’ or a location other than home during a COVID-19 shelter-in-place
order.” See Smith, 110 F.4th at 833 (citation omitted; alteration in original).
        11
            Cf. Smith, 110 F.4th at 823 (“Once a person enables Location History, Google
begins to ‘log[] [the] device’s location [into the Sensorvault], on average, every two min-
utes’ by ‘track[ing] [the] user’s location across every app and every device associated with
the user’s account.”) (alteration and emphasis in original); see also id. (noting that the “data
is ‘considerably more precise than other kinds of location data, including cell-site location
information because [Location History] is determined based on multiple inputs, including
GPS signals, signals from nearby Wi-Fi networks, Bluetooth beacons, and cell towers’”)
(alteration in original).




                                               8
 Case: 25-60163          Document: 89-1          Page: 9       Date Filed: 03/17/2026




                                       No. 25-60163


                                   B. Vehicle Search
                                       1. The Stop
        The traffic stop was lawful because Hoggard had reasonable suspicion
to stop Porter’s vehicle. “The ‘touchstone of Fourth Amendment analysis
is reasonableness.’” United States v. Henry, 37 F.4th 173, 176 (5th Cir. 2022)
(per curiam) (quoting United States v. Brigham, 382 F.3d 500, 507 (5th Cir.
2004) (en banc)). “[I]if police have reasonable suspicion, grounded in spe-
cific and articulable facts, that a person they encounter was involved in or is
wanted in connection with a completed felony, then a Terry stop may be made
to investigate that suspicion.” 12
        There is no reason to disagree with the district court’s thorough
rationale:
        Officer Hoggard [ ] had reasonable suspicion to initiate the traf-
        fic stop based solely on the automatic license plate reader, or
        the ALPR, hit that revealed an outstanding arrest warrant for
        Mr. Porter; Number 2, the BOLO, or ALPR, hit does not
        need to include a physical description of the driver to provide
        an officer reasonable suspicion to initiate a traffic stop; and
        number 3, under the collective knowledge doctrine, the ALPR
        was reliable and provided Officer Hoggard with reasonable sus-
        picion to initiate the traffic stop.
After all, the BOLO report “provide[d] the reasonable suspicion necessary
to justify an investigatory stop” because the arrest warrant information from
        _____________________
        12
           United States v. Hensley, 469 U.S. 221, 229 (1985); see United States v. Ochoa,
667 F.3d 643, 649 (5th Cir. 2012) (“The officer making the arrest need not have direct
knowledge of all the facts establishing probable cause, as long as he has communicated with
the officer who does.”); see also United States v. Alvarez, 40 F.4th 339, 352 (5th Cir. 2022)
(“Officers may conduct an investigatory stop in reliance on information issued through
police channels, such as a wanted flyer or bulletin or radio dispatch, if the information is
based on ‘articulable facts supporting a reasonable suspicion that the wanted person has
committed an offense.’”) (citing Hensley, 469 U.S. at 232).




                                             9
Case: 25-60163           Document: 89-1           Page: 10      Date Filed: 03/17/2026




                                       No. 25-60163


the other Mississippi jurisdiction was “credibl[e] and reliabl[e]”—it “speci-
fi[ed] Porter’s vehicle information, allowed Hoggard to “verif[y]” the
match, and related to an active warrant, which turned out to be valid. 13 Even
though he didn’t need to do so because “[t]he reasonable suspicion inquiry
‘falls considerably short’ of 51% accuracy,” Hoggard carefully conducted a
computer check for the license plate, which revealed the vehicle was associ-
ated with “James Stewart” or “E.L. Porter.” 14 That the vehicle may have
belonged to someone other than Porter or that Hoggard lacked a physical
description of the driver does not change the calculus in Porter’s favor 15
because Hoggard had sufficiently specific information to stop the car—he
knew the make and model, its license plate number, its approximate location,
and that Porter was wanted for arrest for aggravated assault.

               2. Glock Pistol and Machinegun Conversion Switch
                                      a. Plain View
        Hoggard found the Glock pistol and machinegun conversion switch
and testified in open court “that the barrel was sticking out from under the
seat” in plain view. Not only was the “incriminating nature” of the auto-
matic conversion switch “immediately apparent,” 16 but the district judge,

        _____________________
        13
           United States v. Gonzalez, 190 F.3d 668 (5th Cir. 1999) (“Whether a particular
tip or BOLO report provides a sufficient basis for an investigatory stop may depend upon
the credibility and reliability of the informant, the specificity of the information contained
in the tip or report, the extent to which the information in the tip or report can be verified
by others in the field, and whether the tip or report concerns active or recent activity, or
has instead gone stale.”) (citing Alabama v. White, 496 U.S. 325, 328-32 (1990)).
        14
           See Kansas v. Glover, 589 U.S. 376, 381 (2020) (noting that “[t]he reasonable
suspicion inquiry ‘falls considerably short’ of 51% accuracy”).
        15
          See Heien v. North Carolina, 574 U.S. 54, 60 (2014) (“To be reasonable is not to
be perfect.”).
        16
          See United States v. Rodriguez, 601 F.3d 402, 407 (5th Cir. 2010) (noting that the
“plain view” exception “allows police to seize items where (1) the police lawfully entered




                                             10
Case: 25-60163            Document: 89-1          Page: 11     Date Filed: 03/17/2026




                                        No. 25-60163


who had an opportunity to observe Hoggard’s demeanor, said in no uncertain
terms, “I do find Officer Hoggard’s testimony to be credible.” 17 There is no
reason to depart from the district court’s sound determination.
        One may be inappropriately tempted to engage in a frame-by-frame,
instant replay-type analysis of Hoggard’s behavior, based on the body camera
footage, considering the proposition that “[w]here testimony conflicts with
video evidence, our court must view the ‘facts in the light depicted by the
videotape.’” 18 But because the video evidence is ambiguous at best for Por-
ter, no such consideration applies. 19
        Although we first notice the gun at about the six-minute mark when
Hoggard physically removes it from under the driver’s seat, his body camera
may not have fully captured everything that he saw at eye-level with a
dynamic field of vision because the camera was in a static position near his
torso. 20 There is nothing that “plainly contradicts the district court’s finding

        _____________________
the area where the item was located; (2) the item was in plain view; (3) the incriminating
nature of the item was ‘immediately apparent’; and (4) the police had a lawful right of
access to the item”) (citing Horton v. California, 496 U.S. 128, 136–37 (1990)).
        17
           See United States v. Gibbs, 421 F.3d 352, 357 (5th Cir. 2005) (“One of the most
important principles in our judicial system is the deference given to the finder of fact who
hears the live testimony of witnesses because of his opportunity to judge the credibility of
those witnesses.”) (internal quotation marks and citation omitted).
        18
             Anderson, 2024 WL 2829243, at *1 (citing Scott v. Harris, 550 U.S. 372, 380–81
(2007)).
        19 See id. (“When video evidence is ‘ambiguous[,]’ however, Scott v. Harris ‘has

no application.’”) (alteration in original) (citing Aguirre v. City of San Antonio, 995 F.3d
395, 410 (5th Cir. 2021)).
        20
           See, e.g., United States v. Stuckey, No.24-CR-2017-CJW-MAR, 2025 WL 34816,
at *2 (N.D. Iowa 2025) (noting that “the body camera is positioned—on [the officer’]s
torso, and thus does not capture what [he] could see from an eye-level angle”); United
States v. Gray, No.20-191 (CKK), 2021 WL 2209462, at *2 (D.D.C. 2021) (“Because the
body-worn cameras focus only straight ahead and are lower than the officers’ sight-line, the




                                             11
Case: 25-60163          Document: 89-1           Page: 12     Date Filed: 03/17/2026




                                      No. 25-60163


that the officer saw” the Glock and the switch “in plain view.” 21
        Another rejoinder is that the factual circumstances suggest that Hog-
gard did not see the Glock and its switch in plain view. True, Hoggard initi-
ally left the Glock in an unlocked car in a residential neighborhood and did
not immediately tell his colleague at the scene about the weapon. But there
was no traffic on the side street, where another patrol car was already present
and blocking incoming traffic from the cross street. And during the three-
and-a-half-minute stretch between Hoggard’s initial discovery of the Glock
and the subsequent physical possession of it, Hoggard had other priorities—
he escorted Porter to his patrol vehicle, put Porter’s personal items in his car,
and rolled its windows up to prevent rain from coming in. Hoggard did not
raise the immediate alarm bells because he wanted “to see if [Porter] was
going to be honest,” something he testified to in open court, which the dis-
trict court found credible.
        The footage is not clear-cut in Porter’s favor. In fact, it shows that
Hoggard seamlessly reached under the seat in a “quick darting motion,”
suggesting that he knew precisely where the Glock and the switch were
because he had previously seen them in plain view. Admittedly, the officer
did exclaim, “Oh s--t,” but that can be explained by the fact that physically
seizing a suspect’s gun that has an attached machinegun conversion device

        _____________________
camera does not capture everything that each officer sees.”); United States v. Rowson,
652 F. Supp. 3d 436, 444 (S.D.N.Y. 2023) (“[B]ody camera footage sometimes does not
pick up nuances visible to the naked eye, including based on the different distances and
angles involved, and that the camera may not have focused on the same, precise part of a
suspect’s anatomy as did the officers.”).
        21
           See United States v. Riggins, No. 22-10306, 2023 WL 2964408, at *1 (5th Cir.
2023) (per curiam) (unpublished) (“Even if the body camera recording does not clearly
show that the syringe was visible inside Riggins’s pocket, we see nothing that plainly con-
tradicts the district court’s finding that the officer saw the syringe in plain view.”).




                                            12
Case: 25-60163          Document: 89-1           Page: 13     Date Filed: 03/17/2026




                                      No. 25-60163


may not be an everyday occurrence even for experienced officers, who may
be rightfully shocked. Far from being clear-cut in Porter’s favor, the footage
confirms that Hoggard contemporaneously corroborated that “[the Glock]
was basically in plain view,” and “the barrel [was] sticking out from under
the seat, so [he] saw it in plain view.”
        Viewing the evidence in the light most favorable to the government as
the prevailing party, there is nothing that plainly contradicts the district
court’s reasoned assessment that Hoggard saw the Glock and its switch in
plain view.

                    IV. Constitutionality of a Criminal Statute
        This court reviews a preserved challenge to the constitutionality of a
statute de novo. United States v. Howard, 766 F.3d 414, 419 (5th Cir. 2014).
“When a litigant brings both facial and as-applied challenges, we generally
decide the as-applied challenge first because it is the narrower question.”
Ostrewich v. Tatum, 72 F.4th 94, 104 (5th Cir. 2023). “To sustain a facial
challenge, ‘the challenger must establish that no set of circumstances exists
under which the statute would be valid.’” 22 A facial challenge will necessar-
ily fail if a statute is constitutional as applied to a defendant’s individual case.
Id.

                                V. 18 U.S.C. § 922(o)
        This court’s jurisprudence forecloses Porter’s Second Amendment
challenge to 18 U.S.C. § 922(o) argument—machineguns “do not receive
Second Amendment protection.” 23 Indeed, very recently, we squarely

        _____________________
        22
           United States v. Diaz, 116 F.4th 458, 471 (5th Cir. 2024) (quoting United States
v. Salerno, 481 U.S. 739, 745 (1987)), cert. denied, 145 S. Ct. 2822 (2025).
        23
         See Hollis v. Lynch, 827 F.3d 436, 451 (5th Cir. 2016) (concluding that machine-
guns “do not receive Second Amendment protection” and noting that “[m]achineguns are




                                            13
Case: 25-60163           Document: 89-1            Page: 14      Date Filed: 03/17/2026




                                        No. 25-60163


answered this question, reasoning that Hollis continues to bind us” and that
the defendant’s “Second Amendment challenge to his § 922(o) conviction
must fail” “because Hollis controls.” United States v. Wilson, 164 F.4th 380,
385–87 (5th Cir. 2026). Wilson makes clear that “Bruen reinforces the por-
tion of Heller on which Hollis relied.” 24 Under our Rule of Orderliness, 25
“only an intervening change in the law . . . permits a subsequent panel to
decline to follow a prior Fifth Circuit precedent.” 26 Bruen does not unequiv-
ocally overrule Hollis because Bruen addressed a law limiting the ability of
law-abiding citizens to carry handguns outside the home. See New York State
Rifle & Pistol Ass’n, Inc. v. Bruen, 597 U.S. 1, 13–14 (2022).
        AFFIRMED.




        _____________________
dangerous and unusual and therefore not in common use”).
        24
          Wilson, 164 F.4th at 386 (“In Hollis, the court cited dicta from Heller for the
proposition that the Second Amendment does not protect dangerous and unusual weapons.
And in Bruen, the Supreme Court reiterated that portion of Heller, observing that it is ‘fairly
supported by the historical tradition of prohibiting the carrying of dangerous and unusual
weapons that the Second Amendment protects the possession and use of weapons that are
in common use at the time.’”).
        25
           See Thompson v. Dall. City Att’y’s Off., 913 F.3d 464, 468 n.17 (5th Cir. 2019)
(“[A] panel’s interpretation of a Supreme Court decision is binding on a subsequent panel
even if the later panel disagrees with the earlier panel’s interpretation.”) (citing United
States v. Traxler, 764 F.3d 486, 489 (5th Cir. 2014) (“Even if persuaded that [our prior
panel opinion] is inconsistent with [an earlier Supreme Court opinion], we may not ignore
the decision, for in this circuit one panel may not overrule the decision of a prior panel.”)
(alteration in original)).
        26
          United States v. Alcantar, 733 F.3d 143, 145 (5th Cir. 2013); id. at 146 (noting that
the intervening change in the law “must be unequivocal”).




                                              14

```

---

## GROUP: content/cases/United States v. Smith (2024).md  (`case`, 7 assertions)

### content_page

```
---
title: "United States v. Smith (2024)"
type: case
citation: "110 F.4th 817 (2024)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Court of Appeals for the Fifth Circuit
court_level: coa
circuit: 5th
year: 2024
date_decided: 2024-08-09
docket: 23-60321
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2026-07-03
  as_of_treatment: 2026-07-03
  composite_basis: principal-holding
  composite_basis_ref: search.digital.geofence-threshold
  varies_by_point: true
  scope_note: "Composite reflects the search-threshold holding (geofence acquisition IS a search), confirmed by Chatrie v. United States (2026). The categorical general-warrant holding is the point that varies — binding in the Fifth Circuit, not adopted by SCOTUS."
  point_overrides:
    - point: search.warrant.geofence-general-warrant
      point_label: Geofence warrants are categorically unconstitutional general warrants
      field_i_validity: caution
      as_of_treatment: 2026-07-03
      s3_binding_status: bound
      by:
        - name: Chatrie v. United States
          cluster_id: 10881683
          cite: "609 U.S. ___ (2026)"
          field_ii: limited
      scope_note: "Binding in the Fifth Circuit; SCOTUS in Chatrie expressly declined to adopt the categorical rule — the probable-cause/particularity of geofence warrants is the live question on Chatrie's remand."
lake:
  record_id: "United States v. Smith (2024)"
  status: verified
  projected_at: 2026-07-06
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10036119/united-states-v-smith/"
  cluster_id: 10036119
  opinion_id: 10502720
  identity_checked: true
homes:
  - page: "[[Reverse-Keyword and Geofence Warrants]]"
    role: "Key — Circuit anchor (geofence)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — umbrella)"
related: ["[[Chatrie v. United States]]", "[[Carpenter v. United States]]", "[[United States v. Leon]]", "[[The Warrant Requirement]]", "[[The Exclusionary Rule]]"]
aliases: ["United States v. Smith", "United States v. Smith (5th Cir. 2024)"]
tags: ["case", "fourth-amendment", "search", "digital-privacy", "geofence", "location-history", "good-faith-exception"]
holding: "Acquiring Google Location History through a geofence warrant is a Fourth Amendment search under Carpenter, and geofence warrants — which identify everyone in an area rather than a particularized suspect — are modern-day general warrants, unconstitutional under the Fourth Amendment; suppression was nonetheless denied under the Leon good-faith exception given the technology's novelty."
---

# United States v. Smith (2024)

*110 F.4th 817 (5th Cir. 2024)* (No. 23-60321) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Good law — varies by point**
<!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-03: cluster 10036119 → opinion 10502720 — see frontmatter/Sources. -->

## Background
On February 5, 2018, three men robbed Sylvester Cobbs, a contract route driver for the U.S. Postal Service, of registered mail bags containing over $60,000 as he arrived at the Lake Cormorant, Mississippi post office. Surveillance video showed the assailant apparently using a cell phone before and after the robbery, but nine months of investigation produced no suspect. Postal inspectors then obtained a **geofence warrant** directing Google to disclose Location History for every device within a roughly 98,000-square-meter box around the post office during the robbery window. The returns led to Jamarr Smith and Gilbert McThunel, and follow-up investigation identified Thomas Iroko Ayodele. A jury convicted all three of robbery and conspiracy; they appealed the denial of their motion to suppress the geofence-derived evidence.

## Issue
Whether obtaining Google Location History through a geofence warrant is a Fourth Amendment search, and whether a warrant that identifies everyone within a geographic area — rather than a particularized suspect — satisfies the Fourth Amendment.

## Rule
Acquiring geofence Location History is a **search** under *[[Carpenter v. United States|Carpenter]]* — the comprehensive, automatically generated record of a phone's movements invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] even though Google holds the data. And because a geofence warrant works backwards — identifying every person in an area on the chance one is the suspect, rather than searching a particularized target — the panel held it fails the Fourth Amendment at the threshold: "We hold that geofence warrants are modern-day general warrants and are unconstitutional under the Fourth Amendment. However, considering law enforcement's reasonable conduct in this case in light of the novelty of this type of warrant, we uphold the district court's determination that suppression was unwarranted under the good-faith exception." — 110 F.4th at 838. ^pin-838

## Application
The geofence returns exposed the private movements of everyone near the Lake Cormorant post office, not just the eventual defendants — the inverted, dragnet character the panel found indistinguishable from a general warrant. But the inspectors had consulted prosecutors, obtained a magistrate's authorization, and navigated a genuinely novel technology with no controlling precedent; on those facts the court applied *[[United States v. Leon|Leon]]* good faith rather than the exclusionary rule.

## Conclusion
Convictions **affirmed**: the geofence warrant was unconstitutional, but suppression was unwarranted under the [[The Good-Faith Exception|good-faith exception]]. King, J., wrote for the panel (King, Ho, Engelhardt, JJ.).

## Treatment & subsequent history

**Composite: Good law — treatment varies by point.** *Smith*'s two holdings have diverged: the search-threshold holding is now nationally settled in its favor; the categorical general-warrant holding remains binding only in the Fifth Circuit.

| Point of law | Status | Controlling authority |
|---|---|---|
| Acquiring geofence Location History is a Fourth Amendment search | **Good law** | Confirmed by *[[Chatrie v. United States]]*, 609 U.S. ___ (2026) — SCOTUS reached the same result, applying and extending *[[Carpenter v. United States\|Carpenter]]* |
| Geofence warrants are categorically unconstitutional general warrants | **Caution** | *[[Chatrie v. United States\|Chatrie]]* expressly declined to adopt the categorical rule; the probable-cause/[[Particularity\|particularity]] question is live on *[[Chatrie v. United States\|Chatrie]]*'s remand. Binding in the Fifth Circuit; the persuasive minority position elsewhere |

The Supreme Court's 2026 *[[Chatrie v. United States|Chatrie]]* decision resolved the circuit split *Smith* anchored: acquiring geofence Location History **is** a search, as *Smith* held (and the Fourth Circuit's [[Reading and Citing Cases#en-banc|en banc]] *[[Chatrie v. United States|Chatrie]]* had fractured over). But the Court stopped at the threshold — it did not decide whether any geofence warrant can satisfy probable cause and [[Particularity|particularity]], so *Smith*'s stronger point remains the minority answer to a question SCOTUS left open.

## Appears on
- [[Reverse-Keyword and Geofence Warrants]] — *Key — Circuit anchor (geofence)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — umbrella)*

## Sources
- [*United States v. Smith*, 110 F.4th 817 (5th Cir. 2024)](https://www.courtlistener.com/opinion/10036119/united-states-v-smith/) — pinpoint: 838 (general-warrant holding + good-faith disposition; quote string-matched against the CL opinion text 2026-07-03).
- [*Chatrie v. United States*, 609 U.S. ___ (2026)](https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/) — the search-threshold confirmation and the reserved probable-cause/particularity question.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3f9f4bc7922196c7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "110 F.4th 817 (2024)", "court": "U.S. Court of Appeals for the Fifth Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Smith (2024)", "year": "2024"}}
{"assertion_id": "32c794501583c7bc", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Related (cross-ref — umbrella)", "title": "United States v. Smith (2024)"}}
{"assertion_id": "3422ef5d07ccfa4b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Acquiring Google Location History through a geofence warrant is a Fourth Amendment search under Carpenter, and geofence warrants — which identify everyone in an area rather than a particularized suspect — are modern-day general warrants, unconstitutional under the Fourth Amendment; suppression was nonetheless denied under the Leon good-faith exception given the technology's novelty.", "title": "United States v. Smith (2024)"}}
{"assertion_id": "4a722a08b21471c5", "dimension": "support", "kind": "home_role", "locator": {"home": "Reverse-Keyword and Geofence Warrants"}, "payload": {"home": "Reverse-Keyword and Geofence Warrants", "role": "Key — Circuit anchor (geofence)", "title": "United States v. Smith (2024)"}}
{"assertion_id": "58f569a1ce8de774", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2026-07-03", "as_of_treatment": "2026-07-03", "composite_basis": "principal-holding", "composite_basis_ref": "search.digital.geofence-threshold", "field_i_validity": "good_law", "scope_note": "Composite reflects the search-threshold holding (geofence acquisition IS a search), confirmed by Chatrie v. United States (2026). The categorical general-warrant holding is the point that varies — binding in the Fifth Circuit, not adopted by SCOTUS.", "title": "United States v. Smith (2024)", "varies_by_point": "true"}}
{"assertion_id": "847b1be345232a0f", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "search.warrant.geofence-general-warrant"}, "payload": {"by": [{"cite": "609 U.S. ___ (2026)", "cluster_id": "10881683", "field_ii": "limited", "name": "Chatrie v. United States"}], "field_i_validity": "caution", "point": "search.warrant.geofence-general-warrant", "point_label": "Geofence warrants are categorically unconstitutional general warrants", "s3_binding_status": "bound", "title": "United States v. Smith (2024)"}}
{"assertion_id": "c1d44f36268736b7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "United States v. Smith (2024)"}}
```

### lake record — United States v. Smith (2024)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Smith (2024)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Smith",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Smith (2024)",
    "court": "U.S. Court of Appeals for the Fifth Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "2024-08-09",
    "year": 2024,
    "docket": "23-60321",
    "cluster_id": 10036119,
    "lead_opinion_id": 10502720,
    "sibling_ids": [
      10502720
    ],
    "absolute_url": "/opinion/10036119/united-states-v-smith/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "110 F.4th 817",
      "volume": "110",
      "reporter": "F.4th",
      "page": "817",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "110 F.4th 817",
        "volume": "110",
        "reporter": "F.4th",
        "page": "817",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "110 F.4th 817",
    "official_selection": {
      "court_class": "coa",
      "selected": "110 F.4th 817",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-838",
      "page": null,
      "quote": "--- # United States v. Smith (2024) *110 F.4th 817 (5th Cir. 2024)* (No. 23-60321) \u00b7 U.S. Court of Appeals for the Fifth Circuit \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **Good law \u2014 varies by point** <!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-03: cluster 10036119 \u2192 opinion 10502720 \u2014 see frontmatter/Sources. --> ## Background On February 5, 2018, three men robbed Sylvester Cobbs, a contract route driver for the U.S. Postal Service, of registered mail bags containing over $60,000 as he arrived at the Lake Cormorant, Mississippi post office. Surveillance video showed the assailant apparently using a cell phone before and after the robbery, but nine months of investigation produced no suspect. Postal inspectors then obtained a **geofence warrant** directing Google to disclose Location History for every device within a roughly 98,000-square-meter box around the post office during the robbery window. The returns led to Jamarr Smith and Gilbert McThunel, and follow-up investigation identified Thomas Iroko Ayodele. A jury convicted all three of robbery and conspiracy; they appealed the denial of their motion to suppress the geofence-derived evidence. ## Issue Whether obtaining Google Location History through a geofence warrant is a Fourth Amendment search, and whether a warrant that identifies everyone within a geographic area \u2014 rather than a particularized suspect \u2014 satisfies the Fourth Amendment. ## Rule Acquiring geofence Location History is a **search** under *[[Carpenter v. United States|Carpenter]]* \u2014 the comprehensive, automatically generated record of a phone's movements invades a reasonable expectation of privacy even though Google holds the data. And because a geofence warrant works backwards \u2014 identifying every person in an area on the chance one is the suspect, rather than searching a particularized target \u2014 the panel held it fails the Fourth Amendment at the threshold:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-07-03",
    "as_of_treatment": "2026-07-03",
    "composite_basis": "principal-holding",
    "composite_basis_ref": "search.digital.geofence-threshold",
    "varies_by_point": true,
    "scope_note": "Composite reflects the search-threshold holding (geofence acquisition IS a search), confirmed by Chatrie v. United States (2026). The categorical general-warrant holding is the point that varies \u2014 binding in the Fifth Circuit, not adopted by SCOTUS.",
    "point_overrides": [
      {
        "point": "search.warrant.geofence-general-warrant",
        "point_label": "Geofence warrants are categorically unconstitutional general warrants",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-07-03",
        "s3_binding_status": "bound",
        "by": [
          {
            "name": "Chatrie v. United States",
            "cluster_id": 10881683,
            "cite": "609 U.S. ___ (2026)",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Binding in the Fifth Circuit; SCOTUS in Chatrie expressly declined to adopt the categorical rule \u2014 the probable-cause/particularity of geofence warrants is the live question on Chatrie's remand."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Ivan Contreras-Sanchez",
          "cluster_id": 10851595,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pennington",
          "cluster_id": 10812356,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Porter",
          "cluster_id": 10810059,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Walker, J.",
          "cluster_id": 10750016,
          "cite": [
            "2025 Pa. Super. 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 10680498,
          "cite": [
            "321 Ga. 137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Choice, K.",
          "cluster_id": 10673715,
          "cite": [
            "2025 Pa. Super. 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Angel Alvarez v. the State of Texas",
          "cluster_id": 10653315,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "WELLS, AARON RAYSHAN v. the State of Texas",
          "cluster_id": 10373456,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Angel Alvarez v. the State of Texas",
          "cluster_id": 10266245,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(10502720) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
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
        "query": "cites:(10502720)",
        "reviewed": 9,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(10502720)",
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
    "complete_query": "cites:(10502720)",
    "indexed_citing_opinions": 9,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 10502720,
        "count": 9,
        "count_source": "search"
      }
    ],
    "citation_count": 11,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-smith-2024.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 9,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 10502720,
        "cited_id": 12977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 49000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 612472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 821120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4089523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4239377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4256321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4274911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 6943812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 7268856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 8408910,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9409113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9423459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9424643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9427321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9428299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9429558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9432890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9434540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9434934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9436658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9895717,
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
    "date_created": "2026-07-06T03:04:09Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
      "controlling case has no official cite in lake; cite omitted",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:04:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
        "at": "2026-07-06T03:04:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:04:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Smith (2024)

```
Case: 23-60321       Document: 113-1         Page: 1   Date Filed: 08/09/2024




        United States Court of Appeals
             for the Fifth Circuit
                             ____________
                                                                  United States Court of Appeals
                                                                           Fifth Circuit
                               No. 23-60321
                             ____________                                FILED
                                                                    August 9, 2024
United States of America,                                           Lyle W. Cayce
                                                                         Clerk
                                                          Plaintiff—Appellee,

                                    versus

Jamarr Smith; Thomas Iroko Ayodele; Gilbert
McThunel, II,

                                       Defendants—Appellants.
               ______________________________

               Appeal from the United States District Court
                 for the Northern District of Mississippi
                        USDC No. 3:21-CR-107-1
               ______________________________

Before King, Ho, and Engelhardt, Circuit Judges.
King, Circuit Judge:
       A jury found Appellants guilty of robbery and conspiracy to commit
robbery based on evidence obtained through a geofence warrant. On appeal,
Appellants challenge the constitutionality of this novel type of warrant under
the Fourth Amendment and maintain that the district court erred by failing
to suppress all evidence derived therefrom.
       We hold that the use of geofence warrants—at least as described
herein—is unconstitutional under the Fourth Amendment. In doing so, we
part ways with our esteemed colleagues on the Fourth Circuit. See United
Case: 23-60321       Document: 113-1       Page: 2     Date Filed: 08/09/2024




                                  No. 23-60321


States v. Chatrie, 107 F.4th 319 (4th Cir. 2024). With that said, we agree with
the district court that, here, law enforcement acted in good faith in relying on
this type of warrant. Accordingly, we AFFIRM the district court’s denial of
Appellants’ motion to suppress.
                   I. Factual & Procedural Background
                           A. Underlying Offense
       On February 5, 2018, three individuals acting in concert robbed
Sylvester Cobbs, a Contract Route Driver with the United States Postal
Service. As a Route Driver, Cobbs delivered and picked up mail from five
rural post offices in DeSoto County and Tunica County, Mississippi. At the
time of the robbery, Cobbs was headed to Lake Cormorant, the fourth of five
stops he would make along his route.
       The mail that Cobbs collected included registered mail bags, which
contained cash receipts collected by the Postal Service from the sale of items
such as money orders and stamps. By the time that Cobbs arrived at Lake
Cormorant, he had already collected registered mail bags from three other
post offices along his route.
       At approximately 5:20 p.m., Cobbs arrived at the Lake Cormorant
Post Office. As he normally would, Cobbs backed his mail truck up to the
back door, where he would retrieve mail bags waiting for him inside the post
office. Before Cobbs could open the back door to the post office, however, an
unknown assailant—later determined to be Defendant-Appellant Gilbert
McThunel—sprayed Cobbs with pepper spray, struck Cobbs multiple times
with a handgun, threatened to kill him, and grabbed the registered mail bags
from Cobbs’s truck. The mail bags contained $60,706. Thereafter, the
assailant fled, and Cobbs drove his truck to the front of the post office and
called 911.




                                           2
Case: 23-60321       Document: 113-1      Page: 3     Date Filed: 08/09/2024




                                 No. 23-60321


       No suspect was arrested in connection to the robbery on the day of the
occurrence. However, around three days after the robbery, Postal Inspector
Stephen Mathews began his investigation and was able to locate a video of
the incident taken from a camera located at a farm office across the street
from the post office. The video showed a red Hyundai and a large white SUV
in the area. The video revealed the assailant getting out of the SUV before
the robbery, walking behind the building, and waiting for Cobbs to arrive.
While behind the building, the assailant had his “hand up to his ear and
elbow[] out” for multiple minutes, consistent with talking on a cell phone.
However, the video does not show an actual cell phone. Later, after assaulting
Cobbs, the assailant went back behind the building, squatted down, and began
“looking at something in his hand” which appeared “indicative of” cell
phone use. Although not visible on video, it is inferred that the suspect got
back into the SUV before fleeing the scene. Based upon his examination of
the video, Mathews surmised that three suspects were involved.
       Sometime after obtaining the video footage, but prior to applying for
any warrants, Mathews located a witness, Forrest Coffman, who lived across
the street. Coffman had seen the red Hyundai “circling the area back and
forth,” and he decided to ask the driver if he was lost. The driver stated that
he was looking for the highway. Coffman gave the driver directions, turned
around, and went back inside his house. A “few moments later,” Coffman
heard a “bunch of commotion,” stepped outside, and saw officers at the post
office. Coffman walked over and spoke with law enforcement, where he
described the person in the red Hyundai as a black male with a reddish color
goatee. After meeting with law enforcement on the day of the incident,
Coffman had no further involvement with the matter for approximately
fifteen months.
       By November 2018, nine months after the robbery, the Postal
Inspection Service had not been able to identify any suspects from video



                                          3
Case: 23-60321         Document: 113-1          Page: 4      Date Filed: 08/09/2024




                                     No. 23-60321


footage or witness interviews, and Postal Inspector Todd Matney testified
that they “were having a problem identifying the individuals.” However,
during the course of their investigation, Matney and Mathews learned about
“a new type of search warrant”—a “geofence warrant”—designed to
“identify who might be present at the scene of a robbery.” Believing that this
warrant could help them rekindle their investigation, on November 8, 2018,
Matney and Mathews applied for a geofence warrant seeking information
from Google to locate potential suspects and witnesses in connection to the
robbery.
                        B. Geofence Warrants: A Primer
        As a relic of their novelty, “[t]here is a relative dearth of case law
addressing geofence warrants.” United States v. Chatrie, 590 F. Supp. 3d 901,
906 (E.D. Va. 2022) [hereinafter Chatrie (Dist.)]. As such, we provide a brief
history of geofence warrants, as well as a description of law enforcement’s
process for obtaining them. 1
        Google received its first geofence warrant request in 2016. 2 Id. at 914;
United States v. Chatrie, 107 F.4th 319, 323 (4th Cir. 2024) [hereinafter


        _____________________
        1
          Congress has not yet taken a stance on law enforcement’s use of geofence
warrants. However, members have expressed their marked disapproval. In July 2020,
Alphabet (Google’s parent company) CEO Sundar Pichai appeared before the House
Judiciary Subcommittee on Antitrust, Commercial, and Administrative Law. See C-SPAN,
CEOs Mark Zuckerberg, Tim Cook, Jeff Bezos & Sundar Pichai Testify Before House Judiciary
Cmte, YouTube (July 29, 2020), https://perma.cc/7K5T-ACHJ (discussion at 1:45:17-
1:47:50). During the hearing, Representative Kelly Armstrong called geofence warrants
“the single most important issue” before the Subcommittee and contended that geofence
warrants violate the Fourth Amendment. Id. In particular, Representative Armstrong
believed that “people would be terrified to know that law enforcement can grab general
warrants and get everybody’s information anywhere.” Id.
        2
         Companies such as Apple, Lyft, Snapchat, and Uber have all received geofence
warrant requests, but Google is the most common recipient and “the only one known to




                                               4
Case: 23-60321        Document: 113-1         Page: 5     Date Filed: 08/09/2024




                                    No. 23-60321


Chatrie (App.)]. Since then, requests for geofence warrants have
“skyrocketed in number.” Chatrie (App.), 107 F.4th at 323–24. From 2017 to
2018 alone, requests to Google for geofence warrants increased over 1,500%.
Id.; Brian L. Owsley, The Best Offense Is a Good Defense: Fourth Amendment
Implications of Geofence Warrants, 50 Hofstra L. Rev. 829, 834 (2022).
In 2019, Google was receiving about 180 geofence warrant requests per week
from law enforcement around the country, amounting to about 9,000
geofence requests for that year. Owsley, Best Offense, supra at 834; Chatrie
(Dist.), 590 F. Supp. 3d at 914. By 2020, that number went up to 11,500
geofence warrant requests. Owsley, Best Offense, supra at 834. By 2021,
geofence warrants comprised more than 25% of all warrant requests Google
received in the United States. See Google, Supplemental
Information on Geofence Warrants in the United States
1, https://perma.cc/XEU3-KEXJ; Haley Amster & Brett Diehl, Note,
Against Geofences, 74 Stan. L. Rev. 385, 389 & n.11 (2022). Moreover, the
use of these warrants has not been limited to egregious or violent crimes. Law
enforcement officials have obtained geofence warrants for investigations into
stolen pickup trucks and smashed car windows. Amster & Diehl, Against
Geofences, supra at 396; see also In re Search of Info. Stored at Premises Controlled
by Google, as Further Described in Attachment A, No. 20 M 297, 2020 WL
5491763, at *8 (N.D. Ill. July 8, 2020) (“The government’s undisciplined and
overuse of this investigative technique in run-of-the-mill cases that present
no urgency or imminent danger poses concerns to our collective sense of
privacy and trust in law enforcement officials.”).
       “Unlike a warrant authorizing surveillance of a known suspect,
geofencing is a technique law enforcement has increasingly utilized when the
       _____________________
respond.” Note, Geofence Warrants and the Fourth Amendment, 134 HARV. L. REV. 2508,
2512–13 (2021).




                                             5
Case: 23-60321          Document: 113-1           Page: 6      Date Filed: 08/09/2024




                                       No. 23-60321


crime location is known but the identities of suspects [are] not.” United
States v. Rhine, 652 F. Supp. 3d 38, 66 (D.D.C. 2023). Thus, geofence
warrants effectively “work in reverse” from traditional search warrants.
Amster & Diehl, Against Geofences, supra at 388 (internal quotation omitted).
In requesting a geofence warrant, “[l]aw enforcement simply specifies a
location and period of time, and, after judicial approval, companies conduct
sweeping searches of their location databases and provide a list of cell phones
and affiliated users found at or near a specific area during a given timeframe,
both defined by law enforcement.” Geofence Warrants and the Fourth
Amendment, supra at 2509.
        So far, Google has been the primary recipient of geofence warrants, in
large part due to its extensive Location History database, known as the
“Sensorvault.” 3 Amster & Diehl, Against Geofences, supra at 389. Google

        _____________________
        3
          In December 2023, Google authored a blog post where it announced its intent to
modify how and where it stores Location History data. See Marlo McGriff, Updates to
Location History and New Controls Coming Soon to Maps, Google: The Keyword (Dec.
12, 2023), https://perma.cc/DN4Z-7CTA; see also Cyrus Farivar & Thomas Brewster,
Google Just Killed Warrants that Give Police Access to Location Data, Forbes (Dec. 14,
2023, 5:43 PM EST), https://perma.cc/WM83-DAXM. Google’s decision should make it
“impossible for the company to access” Location History data in a move made “explicitly
[to] bring an end to . . . dragnet location searches.” Farivar & Brester, Google Just Killed
Warrants that Give Police Access to Location Data, supra. In other words, these changes, in
theory, “will eventually render the company unable to fulfill geofence warrants.” Prathi
Chowdri, Emerging Tech and Law Enforcement: What Are Geofences and How Do They Work?,
Lexipol (Jan. 4, 2024) (internal quotation omitted), https://perma.cc/DNL3-XC56.
        However, Google has not fully implemented its new storage methods; the
migration will only be complete within “the next several months.” See Stan Kaminsky,
Google Location History Is Now Stored Offline . . . Or Maybe Not, Kaspersky Daily (Mar.
1, 2024), https://perma.cc/ZM6X-92JZ. In fact, the Government concedes that it “is still
seeking Google geofences,” and that even after Google changes its storage techniques,
“the United States . . . may in the future seek geofence warrants from sources other than
Google.” Regardless, these facts do not affect this court’s Fourth Amendment analysis
regarding the constitutionality of the practice itself.




                                                 6
Case: 23-60321        Document: 113-1       Page: 7     Date Filed: 08/09/2024




                                  No. 23-60321


collects data from accounts of users who opt in to Google’s Location History
service. Location History is disabled by default. Chatrie (App.), 107 F.4th at
322. For Location History to collect data, a user must make sure that the
device-location setting is activated, and that Location Reporting is enabled.
This is not to say, however, that enabling Location Reporting is a difficult
task. Users are often asked to opt in to Location History “multiple times
across multiple apps.” Id. at 358 n.9 (Wynn, J., dissenting) (quoting Chatrie
(Dist.), 590 F. Supp. 3d at 908–09). In fact, “manually deactivating all
[Location History] sharing remains difficult and discouraged.” Amster &
Diehl, Against Geofences, supra at 396–97 (“In 2018, an internal Google email
explained that ‘[t]he current [user interface] feels like it is designed to make
[limiting Location History collection] possible, yet [it is] difficult enough that
people won’t figure it out.’” (internal citation omitted)); see also In re Search
of Info. Stored at Premises Controlled by Google, 481 F. Supp. 3d 730, 737 n.3
(N.D. Ill. 2020) (“Published reports have indicated that many Google
services on Android and Apple devices store the device users’ location data
even if the users seek to opt out of being tracked by activating a privacy setting
that says it will prevent Google from storing the location data.”).
       Google’s Android cell phones, which “comprise about 74% of the total
number of smartphones worldwide,” “automatically have an Android
operating system, as well as various Google apps that could potentially store
a user’s location.” Owsley, Best Offense, supra at 834. Apple, which makes
approximately 23% of the world’s smartphones, does not keep location data
associated with its phones, but its phones still “often have various apps
that . . . provide Google with a specific device’s location.” Id. at 834–35. In
October 2018, Google estimated that approximately 592 million—or roughly
one-third—of Google’s users had Location History enabled.
       Once a person enables Location History, Google begins to “log[] [the]
device’s location [into the Sensorvault], on average, every two minutes” by



                                            7
Case: 23-60321       Document: 113-1       Page: 8     Date Filed: 08/09/2024




                                  No. 23-60321


“track[ing] [the] user’s location across every app and every device associated
with the user’s account.” Chatrie (Dist.), 590 F. Supp. 3d at 908–09; see also
Chatrie (App.), 107 F.4th at 323 n.6. In other words, “‘[o]nce a user opts into
Location History, Google is always collecting data and storing all of that data’
in the Sensorvault.” Rhine, 652 F. Supp. 3d at 67 (quoting Chatrie (Dist.), 590
F. Supp. 3d at 909). Location History is stored within the Sensorvault for at
least eighteen months, but users may also request that the information be
deleted themselves. Amster & Diehl, Against Geofences, supra at 394; Rhine,
652 F. Supp. 3d at 67.
       Moreover, not only is the volume of data comprehensive, so is the
quality. “Location History appears to be the most sweeping, granular, and
comprehensive tool—to a significant degree—when it comes to collecting
and storing location data.” Chatrie (App.), 107 F.4th at 349 (Wynn, J.,
dissenting) (quoting Chatrie (Dist.), 590 F. Supp. 3d at 907). The data is
“considerably more precise than other kinds of location data, including cell-
site location information because [Location History] is determined based on
multiple inputs, including GPS signals, signals from nearby Wi-Fi networks,
Bluetooth beacons, and cell towers.” Rhine, 652 F. Supp. 3d at 67 (internal
quotations omitted). Google refers collectively to this data, regardless of its
source, as “Location History.” Amster & Diehl, Against Geofences, supra at
394. Location History data allows Google to “potentially locate an individual
within about sixty feet or less,” and in certain circumstances, down to three
meters. Owsley, Best Offense, supra at 835; Chatrie (Dist.), 590 F. Supp. 3d at
909. In fact, Location History data can “even discern elevation, locating the
specific floor in a building where a person might be.” Chatrie (App.), 107 F.4th
at 349 (Wynn, J., dissenting); see also Chatrie (Dist.), 590 F. Supp. 3d at 908
(noting that Location History data can “determine if you are on the second
[or first] floor of [a] mall”). However, Location History cannot estimate a
device’s location with absolute precision. Instead, when Google reports a




                                           8
Case: 23-60321       Document: 113-1      Page: 9    Date Filed: 08/09/2024




                                 No. 23-60321


device’s location, it includes both the source from which the specific
datapoint was derived, and a “confidence interval” indicating Google’s
confidence in that estimated location. The smaller the radius, the more
confident Google is in that phone’s exact location. According to Google, it
“aims to accurately capture roughly 68 percent of users within [its]
confidence intervals.” Chatrie (Dist.), 590 F. Supp. 3d at 909 (internal
quotation omitted); Chatrie (App.), 107 F.4th at 323. “[I]n other words, there
[is] a 68 percent likelihood that a user is somewhere inside the confidence
interval.” Chatrie (Dist.), 590 F. Supp. 3d at 909 (internal quotation
omitted); Chatrie (App.), 107 F.4th at 323.
       Using the raw data that it collects, Google builds “aggregate models”
using a “proprietary, and therefore un-reviewed, algorithm” that transforms
the data to assist with improving Google’s services, including, for example,
“decision-making in Google Maps.” Wells v. State, 675 S.W.3d 814, 830
(Tex. App.—Dallas 2023, pet. granted); Chatrie (Dist.), 590 F. Supp. 3d at
908; Chatrie (App.), 107 F.4th at 323. It also uses the data to analyze “[its]
customers[’] . . . travel patterns, their history patterns, to make
recommendations and sell advertising.” In short, Google does not store this
data for the purpose of law enforcement, but rather for commercial purposes.
Wells, 675 S.W.3d at 830.
       But, if you build it, they will come. See Geofence Warrants and the
Fourth Amendment, supra at 2508. Early on, when law enforcement officials
first started requesting geofence warrants, they would simply ask Google to
identify all users who were in a geographic area during a given time frame.
However, Google began taking issue with these early warrants, believing
them to be a “potential threat to user privacy.” Chatrie (App.), 107 F.4th at
324. Thus, Google developed an internal procedure on how to respond to
geofence warrants. Id. This procedure is divided into three steps.




                                          9
Case: 23-60321      Document: 113-1       Page: 10     Date Filed: 08/09/2024




                                  No. 23-60321


                                    Step 1
       At Step 1, law enforcement provides Google with the geographical and
temporal parameters around the time and place where the alleged crime
occurred. Following, Google searches its Sensorvault for all users who had
Location History enabled during the law enforcement-provided timeframe.
Chatrie (Dist.), 590 F. Supp. 3d at 914–15. Google is not capable of storing
data in a way that enables it to search a specific area, nor does Google know
which users have saved their Location History prior to its search. Id. at 915.
Thus, for every single geofence warrant Google responds to, it must search
each account in its entire Sensorvault—all 592 million—to find responsive
user records. It cannot just look at individual accounts. See Chatrie (App.),
107 F.4th at 324 (“Google does not keep any lists like this on-hand. So it must
first comb through its entire Location History repository to identify users
who were present in the geofence.”).
       After Google searches its Sensorvault, it determines which accounts
were within the geographic parameters of the warrant and lists each of those
accounts with an anonymized device ID. Google also includes the date and
time, the latitude and longitude, the geolocation source used, and the map
display radius (i.e., the confidence interval). The volume of geofence data
produced “depends on the size and nature of the geographic area and length
of time covered by the geofence request.” Chatrie (Dist.), 590 F. Supp. 3d at
915. “Google does not impose specific, objective restraints on the size of the
geofence, the length of the relevant timeframe, or the number of users for
which it will produce data.” Id. Rather, a Google Legal Investigation
Specialist employee reviews the geofence warrant, consults with legal
counsel, and works with law enforcement to assuage any of Google’s
concerns before turning the data over and moving on to Step 2. Id. at 907,
915–16; see also Chatrie (App.), 107 F.4th at 324.




                                          10
Case: 23-60321      Document: 113-1       Page: 11     Date Filed: 08/09/2024




                                 No. 23-60321


                                    Step 2
       At Step 2, law enforcement contextualizes and narrows the data.
During this step, law enforcement reviews the anonymized list provided by
Google and determines which IDs are relevant. As part of this review, “[i]f
law enforcement needs additional de-identified location information for a
certain device to determine whether that device is actually relevant to the
investigation, law enforcement . . . can compel Google to provide
additional . . . location coordinates beyond the time and geographic scope of
the original request.” Chatrie (Dist.), 590 F. Supp. 3d at 916 (cleaned up);
Chatrie (App.), 107 F.4th at 324. The purpose of this additional data is to
assist law enforcement in eliminating devices that are, for example, “not in
the target location for enough time to be of interest, [or] were moving through
the target location in a manner inconsistent with other evidence.” Chatrie
(Dist.), 590 F. Supp. 3d at 916. As a general matter, “Google imposes no
geographical limits on this Step 2 data.” Id. (internal quotation omitted);
Chatrie (App.), 107 F.4th at 324. “Google does, however, typically require
law enforcement to narrow the number of users for which it requests Step 2
data so that the Government cannot . . . simply seek geographically
unrestricted data for all users within the geofence.” Chatrie (Dist.), 590 F.
Supp. 3d at 916; Chatrie (App.), 107 F.4th at 324.
                                    Step 3
       Finally, at Step 3, law enforcement compels Google to provide
account-identifying information for the users that they determine are
“relevant to the investigation.” Chatrie (App.), 107 F.4th at 324. This
identifying information includes the names and emails associated with the
listed device IDs. Using this information, law enforcement can then pursue
further investigative techniques, such as cell phone tracking, or sending out
additional warrants tailored to the specific information received.




                                          11
Case: 23-60321          Document: 113-1           Page: 12       Date Filed: 08/09/2024




                                         No. 23-60321


                                     *        *         *
        As a final note, even given the vast amount of data Google has, and the
unprecedented precision of Google’s Location History, the results are not
always spectacular. First, “[m]any geofence warrants do not lead to arrests.”
Geofence Warrants and the Fourth Amendment, supra at 2520. Moreover,
“[m]any are rendered useless due to Google’s slow response time, which can
take as long as six months because of the Sensorvault’s size and the large
number of warrants that Google receives.” Id. Second, as to warrants that are
issued, the data Google returns is not always perfect, and sometimes contains
false positives. In fact, there are already documented accounts of innocent
bystanders being swept into geofence warrants based solely on their
proximity to a crime. 4 In short, while false negatives appear to be “more
extremely rare”—given the accuracy of Google’s data—false positives are
still an area of concern.
                C. Geofence Application and Warrant at Issue
        Returning to the matter at hand, the warrant here, like any other
warrant, began with an Application for a Search Warrant. That application
contained an attached affidavit from Matney, which Mathews helped write.

        _____________________
        4
          For example, Zachary McCoy, an avid bike rider, was swept into a geofence
search because on the day of a burglary, he biked past the victim’s house three times within
an hour. Jon Schuppe, Google Tracked His Bike Ride Past a Burglarized Home. That Made
Him a Suspect., NBC News (Mar. 7, 2020, 5:22 AM CST), https://perma.cc/9WJK-
67TW. In another case, based on a Google geofence warrant, Arizona police officers jailed
Jorge Molina for six days on suspicion of murder. Meg O’Connor, Avondale Man Sues After
Google Data Leads to Wrongful Arrest for Murder, Phx. New Times (Jan. 16, 2020),
https://perma.cc/GLJ8-AHP9. As it turns out, Molina’s stepfather—the man ultimately
arrested for the murder—had been using one of Molina’s old cell phones, which
inadvertently remained logged in to Molina’s email and social media accounts. Id. As a
result, Molina lost his job, was unable to pass a background check, and even lost title to his
vehicle because police impounded his car during the investigation. Id.




                                                  12
Case: 23-60321      Document: 113-1       Page: 13     Date Filed: 08/09/2024




                                 No. 23-60321


Because this type of warrant was new, particularly to Mathews, the Postal
Inspectors consulted with other law enforcement agencies when writing the
application. Additionally, the Inspectors used several different “go-bys”—
or form documents—to ensure that their application had all the necessary
“technical language.” Finally, the Inspectors also consulted with the U.S.
Attorney’s Office prior to seeking their warrant.
       The affidavit stated that “there is probable cause to believe that the
Google accounts identified in Section I of Attachment A, associated with a
particular specified location at a particular specified time, contain evidence,
fruits and instrumentalities of a violation of 18 U.S.C. section 2114(a),
Robbery of a U.S. Postal Service Employee.” However, as with any geofence
warrant, no specific Google accounts were identified in Section I of
Attachment A; rather, the Attachment only specified specific coordinates
around the Lake Cormorant Post Office. The box created by those
coordinates covered approximately 98,192 square meters.
       The affidavit also provided a specific Probable Cause Statement. In
that statement, the Inspectors detailed the two vehicles implicated in the
robbery, Cobbs’s description of the assailant, and a statement that, through
a review of the video surveillance footage, “it appears the robbery suspect
[was] possibly using a cellular device both before and after the robbery
occur[ed].” Finally, the Inspectors included language in the application
stating, in regard to Step 2 outlined above, that law enforcement “will seek
any additional information regarding [relevant] devices through further legal
process.”
       The application and affidavit were submitted to a U.S. magistrate
judge, who issued the warrant on November 8, 2018. The language of the
warrant largely tracked Google’s three-step process outlined above:




                                          13
Case: 23-60321     Document: 113-1       Page: 14     Date Filed: 08/09/2024




                                No. 23-60321


      To the extent within the Provider’s possession, custody, or
      control, the Provider is directed to produce the following
      information associated with the Subject Accounts, which will
      be reviewed by law enforcement personnel (who may include,
      in addition to law enforcement officers and agents, attorneys
      for the government, attorney support staff, agency personnel
      assisting the government in this investigation, and outside
      technical experts under government control) are authorized to
      review the records produced by the Provider in order to locate
      any evidence, fruits, and instrumentalities of 18 U.S.C. section
      2114(a), Robbery of a U.S. Postal Service Employee.
             1.     Location information. All location data, whether
      derived from Global Positioning System (GPS) data, cell
      site/cell tower triangulation/trilateration, and precision
      measurement information such as timing advance or per call
      measurement data, and Wi-Fi location, including the GPS
      coordinates, estimated radius, and the dates and times of all
      location recordings, between 5:00 p.m. CT and 6:00 p.m. CT
      on February 5, 2018;
              2.    Any user and each device corresponding to the
      location data to be provided by the “Provider” will be
      identified only by a numerical identifier, without any further
      content or information identifying the user of a particular
      device. Law enforcement will analyze this location data to
      identify users who may have witnessed or participated in the
      Subject Offenses and will seek any additional information
      regarding those devices through further legal process.
              3.      For those accounts identified as relevant to the
      ongoing investigation through an analysis of provided records,
      and upon demand, the “Provider” shall provide additional
      location history outside of the predefined area for those
      relevant accounts to determine the path of travel. This
      additional location history shall not exceed 60 minutes plus or
      minus the first and last timestamp associated with the account
      in the initial dataset. (The purpose of path of travel/contextual




                                         14
Case: 23-60321     Document: 113-1      Page: 15     Date Filed: 08/09/2024




                                No. 23-60321


      location points is to eliminate outlier points where, from the
      surrounding data, it becomes clear the reported point(s) are not
      indicative of the device actually being within the scope of the
      warrant.)
             4.    For those accounts identified as relevant to the
      ongoing investigation through an analysis of provided records,
      and upon demand, the “Provider” shall provide the
      subscriber’s information for those relevant accounts to
      include, subscriber’s name, email addresses, services
      subscribed to, last 6 months of IP history, SMS account
      number, and registration IP.
In summary, as to Step 1, the warrant authorized an hour-long search from
5:00 p.m. to 6:00 p.m. on February 5, 2018, within a geofence covering
approximately 98,192 square meters around the Lake Cormorant Post Office.
As to Step 2, the warrant authorized law enforcement to obtain additional
Location History for a registered device identified as relevant within “60
minutes plus or minus the first and last timestamp associated with the
account in the initial dataset.” However, prior to reaching Step 2, law
enforcement was required to conduct “further legal process.”
      Google returned the Step 1 data in April 2019. Notably, Google’s
search was much broader than that specifically sought by the warrant,
producing data from a circular area that was approximately 378,278 square
meters, not 98,192 square meters. The search of Google’s 592 million




                                        15
Case: 23-60321      Document: 113-1      Page: 16     Date Filed: 08/09/2024




                                 No. 23-60321


accounts returned three anonymous device IDs within the requested
parameters:




Inspector Matney testified that after receiving this data, he reviewed the
devices to ensure that they fell within the geofence coordinates.
       However, prior to submitting Step 2, neither Matney nor Mathews
applied for another warrant. Instead, Matney and Mathews decided
themselves which device IDs were relevant and requested additional de-
anonymized information for all three devices. The Inspectors determined
that all three devices were relevant to their Step 2 inquiry because devices
1091610859 and 1577088768 registered multiple times within the geofence,
and the third device—1353630479—could have been a potential witness. The
Step 2 request was placed in May 2019, and the expanded information was
received on May 30. However, no new devices were added through the
information gained at Step 2.
       Again, without seeking any new warrants, Matney and Mathews sent
off their Step 3 request for all three devices on June 7, 2019. They received
the de-anonymized information from Google on June 10, 2019. The following
files were returned:
       •       2165781.Key.cvs
       •       bleek2004.AccountInfo.txt
       •       jamarrsmith33.AcountInfo.txt
       •       permanentwavesrecords.AccountInfo.txt




                                         16
Case: 23-60321     Document: 113-1       Page: 17    Date Filed: 08/09/2024




                                No. 23-60321


       Through these files, Mathews was able to determine that
“jamarrsmith33.AcountInfo.txt” was Jamarr Smith’s email account and
“bleek2004.AcountInfo.txt” was Gilbert McThunel’s email account. The
third email account associated with “permanentwavesrecords.AccountInfo.
txt” was deemed irrelevant to the investigation.
       Now, no longer devoid of leads, Mathews and Matney took “[a]
bunch of investigative steps” related to Smith and McThunel, including
sending additional non-geofence warrants to Google regarding Smith and
McThunel’s Google accounts, accessing their CLEAR database profiles,
investigating cell tower data related to Smith and McThunel, and sending
non-geofence warrants to phone companies for Smith and McThunel’s
account information. These additional steps revealed multiple phone calls
between Smith and McThunel during the time of the robbery, and allowed
for further geolocation of Appellants using historical cell phone record
analysis.
       Additionally, through a search of Smith’s phone records and his
friends on Facebook, the Inspectors were able to identify Thomas Iroko
Ayodele as a suspect. Finally, on July 1, 2019, Postal Inspector Dwayne
Martin reapproached witness Forrest Coffman and asked him to participate
in a photo lineup. Although Coffman was unable to identify McThunel or
Ayodele in their respective lines, Coffman did identify Smith as the person
he saw driving the red Hyundai. In sum, all evidence connecting Appellants
to this crime was derived from information obtained from Google pursuant
to the geofence warrant.
                       D. Pretrial & Trial Posture
       The Government initiated the instant action by issuing an indictment
on October 27, 2021. Count I of the indictment alleged that Appellants had a
conspiracy to rob the Lake Cormorant Post Office, and Count II alleged the




                                        17
Case: 23-60321      Document: 113-1      Page: 18     Date Filed: 08/09/2024




                                 No. 23-60321


actual robbery. On November 4, 2022, Smith filed a Motion to Suppress—
which the other Appellants joined—seeking to suppress all evidence derived
from the November 2018 geofence warrant which was used to identify them
as suspects.
       Appellants raised multiple arguments related to the constitutionality
of the geofence warrant. First, Appellants contended that they had a
reasonable expectation of privacy in their Google Location History data, and
that this geofence warrant violated that privacy interest as a categorically
unconstitutional general warrant. Second, Appellants argued that the specific
warrant at issue was invalid from its inception because it lacked probable
cause and particularity. Third, Appellants argued that even if the warrant was
valid, the Government did not undertake “further legal process” to obtain
additional information from Google as required by the warrant, making Step
2 and Step 3 of the search warrantless and illegal. Finally, Appellants
maintained that the good-faith exception set forth in United States v. Leon,
468 U.S. 897 (1984), did not excuse the defects of the warrant, especially in
light of the fact that the affidavit in support of the warrant contained a
knowing and intentionally false statement—specifically, that “it appear[ed]
the robbery suspect [was] possibly using a cellular device both before and
after the robbery occur[ed]”—making the warrant invalid pursuant to Franks
v. Delaware, 438 U.S. 154, 164–65 (1978). As such, Appellants concluded, the
exclusionary rule should apply, and all the evidence seized should be
suppressed as fruit of the poisonous tree.
       On January 31, 2023, the district court conducted a hearing on
Appellants’ Motion to Suppress. At the hearing, the Government called its
two Investigators, Matney and Mathews, and Appellants called an expert,
Spencer McInvaille. In relevant part, Matney and Mathews testified as to:
their unfamiliarity with geofence warrants; the steps they took to request a
geofence warrant and receive information from Google; their consultation



                                         18
Case: 23-60321       Document: 113-1       Page: 19     Date Filed: 08/09/2024




                                  No. 23-60321


with the U.S. Attorney’s Office; their review of surveillance footage
purporting to show the robbery suspect acting consistently with cell phone
usage (e.g., holding his hand up to his ear); and their understanding that the
language in the warrant requiring “further legal process” at Steps 2 and 3
meant the process of law enforcement “demand[ing]” information from
Google, not the process of law enforcement seeking any additional warrants
from the court.
       McInvaille provided expert testimony to the court about digital
forensics and geolocation analysis, including, in relevant part, Google
Location History data. McInvaille explained to the district court that
warrants submitted to Google are typically used to seek information about
suspects when law enforcement knows the suspect has a Google account. In
contrast, law enforcement utilizes geofence warrants and Google Location
History when they do not have any leads, but nevertheless want to search
through Google’s data (i.e., the Sensorvault) to find suspects. McInvaille
outlined the three-step geofence warrant process described supra, and
explained that as part of that process, Google is required to search every
Google account with Location History enabled. Finally, McInvaille testified
that, given his experience in other cases, the language requiring “further legal
process” in this warrant would have required additional warrants at each step
of the geofence process.
       On February 10, 2023, after considering the parties’ briefing and the
evidence presented at the hearing, the district court denied Appellants’
motion to suppress. Trial commenced on February 21, 2023. After a four-day
trial, the jury returned a guilty verdict against all three Appellants as to both
counts. Appellants were sentenced on June 13, 2023, to prison terms ranging
from 121 to 136 months. Following, Appellants filed a Motion for New Trial
and Motion for Judgment of Acquittal. The district court denied the motion.
Appellants timely appealed.



                                           19
Case: 23-60321      Document: 113-1       Page: 20     Date Filed: 08/09/2024




                                 No. 23-60321


                           II. Standard of Review
       “When reviewing the denial of a motion to suppress evidence, this
court reviews the district court’s factual findings for clear error and the
district court’s conclusions regarding the sufficiency of the warrant and the
constitutionality of law enforcement action de novo.” United States v. Perez,
484 F.3d 735, 739 (5th Cir. 2007). We view the evidence in the light most
favorable to the prevailing party below—here, the Government. See United
States v. Pack, 612 F.3d 341, 347 (5th Cir. 2010).
                                III. Analysis
       The Fourth Amendment guarantees individuals the right “to be
secure in their persons, houses, papers, and effects, against unreasonable
searches and seizures.” U.S. Const. amend IV. The “basic purpose of
this Amendment . . . is to safeguard the privacy and security of individuals
against arbitrary invasions by governmental officials.” Carpenter v. United
States, 585 U.S. 296, 303 (2018) (quoting Camara v. Mun. Ct. of City and
Cnty. of S.F., 387 U.S. 523, 528 (1967)). Moreover, the Supreme Court has
established that “the Fourth Amendment protects people, not places,” and
the Court has “expanded [its] conception of the Amendment to protect
certain expectations of privacy as well.” Id. at 304 (quoting Katz v. United
States, 389 U.S. 347, 351 (1967)). “When an individual ‘seeks to preserve
something as private,’ and his expectation of privacy is ‘one that society is
prepared to recognize as reasonable,’ [the Court] ha[s] held that official
intrusion into that private sphere generally qualifies as a search and requires
a warrant supported by probable cause.” Id. (quoting Smith v. Maryland, 442
U.S. 735, 740 (1979)). Evidence seized in violation of the Constitution is
subject to suppression. See Hudson v. Michigan, 547 U.S. 586, 590 (2006).




                                          20
Case: 23-60321          Document: 113-1          Page: 21       Date Filed: 08/09/2024




                                       No. 23-60321


                      A. Reasonable Expectation of Privacy
        The threshold question posed by this case is whether geofencing is a
search under the Fourth Amendment. “A Fourth Amendment privacy
interest is infringed when the government physically intrudes on a
constitutionally protected area or when the government violates a person’s
‘reasonable expectation of privacy.’” United States v. Turner, 839 F.3d 429,
434 (5th Cir. 2016) (quoting United States v. Jones, 565 U.S. 400, 406 (2012)).
To assess whether a “reasonable expectation of privacy” exists, the Supreme
Court has applied Justice Harlan’s two-fold approach as explained in his
concurrence in Katz v. United States, 389 U.S. 347. See Jones, 565 U.S. at 406.
Specifically, for Fourth Amendment protections to attach to a person’s
privacy interest, the person first must “have exhibited an actual (subjective)
expectation of privacy.” Katz, 389 U.S. at 361 (Harlan, J., concurring).
Second, that expectation must “be one that society is prepared to recognize
as ‘reasonable.’” Id. (Harlan, J., concurring).
        Smith and McThunel contend that they have a reasonable expectation
of privacy in their respective location information retrieved in response to a
geofence warrant. 5 This argument is rooted in the application of Carpenter v.


        _____________________
        5
          Ayodele also attempts to join Smith and McThunel’s arguments. However, as
noted above, Ayodele’s information was never retrieved in response to a geofence
warrant—his involvement in this robbery was deduced through a search of Smith’s phone
records and Smith’s friends on Facebook performed after the geofence search. As such,
Ayodele may lack Fourth Amendment standing to join Smith and McThunel because even
if he has an expectation of privacy in his own Google Location History data, he may not
have an expectation of privacy in the Google Location History data of an unrelated third-
party. See United States v. Davis, No. 23-10184, 2024 WL 3573478, at *5–7 (11th Cir. 2024)
(concluding that a defendant lacked Fourth Amendment standing to challenge a geofence
warrant that produced his girlfriend’s Google Location History data because “[e]ven if a
person has a privacy interest in the data on his own phone, he does not have that interest in
the data on someone else’s phone.”).




                                                 21
Case: 23-60321          Document: 113-1          Page: 22       Date Filed: 08/09/2024




                                       No. 23-60321


United States, 585 U.S. 296, arguably the most relevant Supreme Court
precedent addressing law enforcement’s investigatory use of cellular
consumer data. See Amster & Diehl, Against Geofences, supra at 406. In
Carpenter, prosecutors, without a warrant supported by probable cause,
received from a criminal defendant’s wireless carriers cell-site location
information (“CSLI”) that tracked the defendant’s whereabouts over the
course of several days. 6 585 U.S. at 302. From this data, prosecutors were
able to produce maps that placed the defendant’s phone near four robberies.
Id. at 302–03. The court of appeals affirmed the defendant’s convictions,
concluding that the defendant’s privacy interest in CSLI was not entitled to
Fourth Amendment protection because “cell phone users voluntarily convey
cell-site data to their carriers as a means of establishing communication.” Id.
at 303 (internal quotation omitted).
        The Supreme Court reversed. Id. at 321. As a starting point, the Court
acknowledged that a majority of the Court had “already recognized that
individuals have a reasonable expectation of privacy in the whole of their
physical movements.” Id. at 310; see Jones, 565 U.S. at 430 (Alito, J.,
concurring in the judgment) (“[T]he use of longer term GPS monitoring in
investigations of most offenses impinges on expectations of privacy.”);
Jones, 565 U.S. at 415 (Sotomayor, J., concurring). The Court then expressed

        _____________________
        Regardless, we do not and need not answer this question today—as discussed
further infra, Smith and McThunel do have Fourth Amendment standing to bring their
respective constitutional challenges, and our ultimate disposition as to all three Appellants
hinges on the good faith exception. See Byrd v. United States, 584 U.S. 395, 411 (2018)
(“Because Fourth Amendment standing is subsumed under substantive Fourth
Amendment doctrine, it is not a jurisdictional question and hence need not be addressed
before addressing other aspects of the merits of a Fourth Amendment claim.”).
        6
          As the Supreme Court in Carpenter explained, CSLI is the time-stamped record
that is generated each time a phone connects to “cell sites,” the network of radio antennas
that provide signal to cell phones. 585 U.S. at 300–01.




                                                 22
Case: 23-60321      Document: 113-1       Page: 23     Date Filed: 08/09/2024




                                 No. 23-60321


concern with the government having unfettered access to CSLI, noting that
this data provides “an intimate window into a person’s life, revealing not
only his particular movements, but through them his ‘familial, political,
professional, religious, and sexual associations.’” Carpenter, 585 U.S. at 311
(quoting Jones, 565 U.S. at 415 (Sotomayor, J., concurring)). The Court
further expressed concern that this precise, sensitive data could be accessed
by the government “[w]ith just the click of a button.” Id. And, in contrast to
a GPS device attached to a person’s car, a cell phone “faithfully follows its
owner beyond public thoroughfares and into private residences, doctor’s
offices, political headquarters, and other potentially revealing locales.” Id.
“Accordingly, when the Government tracks the location of a cell phone it
achieves near perfect surveillance, as if it had attached an ankle monitor to
the phone’s user.” Id. at 311–12. The Court concluded that the criminal
defendant had a “reasonable expectation of privacy in the whole of his
physical movements.” Id. at 313.
       The Court then addressed the third-party doctrine, which provides
that generally, “a person has no legitimate expectation of privacy in
information he voluntarily turns over to third parties.” Id. at 308 (quoting
Smith, 442 U.S. at 743–44). The Court declined to apply the third-party
doctrine to the collection of CSLI, notwithstanding the fact that this data is
technically voluntarily provided from users to private wireless carriers. As
the Court noted, there is a “world of difference between the limited types of
personal information” addressed in the Court’s prior third-party doctrine
precedent “and the exhaustive chronicle of location information casually
collected by wireless carriers today.” Id. at 314. Furthermore, the Court
found the notion that users “voluntarily” provide this information to private
entities dubious. Carrying a cell phone is “indispensable to participation in
modern society,” and, “[a]part from disconnecting the phone from the
network, there is no way to avoid leaving behind a trail of location data.” Id.




                                          23
Case: 23-60321       Document: 113-1       Page: 24     Date Filed: 08/09/2024




                                  No. 23-60321


at 315. “As a result, in no meaningful sense does the user voluntarily
‘assume[] the risk’ of turning over a comprehensive dossier of his physical
movements.” Id. (quoting Smith, 442 U.S. at 745).
       Chief Justice Roberts’s majority opinion in Carpenter speaks at length
about the privacy interests inherent in location data, and it expresses grave
concern with the government being able to comprehensively track a person’s
movement with relative ease due to the ubiquity of cell phone possession.
The Court acknowledged “some basic guideposts” in resolving questions
related to the Fourth Amendment’s protections of privacy interests,
including securing “the privacies of life against arbitrary power,” and placing
“obstacles in the way of a too permeating police surveillance.” Carpenter,
585 U.S. at 305 (internal quotations omitted). The Court also recognized the
necessity of applying the Fourth Amendment to systems of advanced
technology, expressing concern that CSLI is approaching “GPS-level
precision,” with wireless carriers having the capability to “pinpoint a
phone’s location within 50 meters.” Id. at 313; see also Riley v. California, 573
U.S. 373, 396 (2014) (acknowledging the privacy concerns implicated by cell
phone location data that “can reconstruct someone’s specific movements
down to the minute, not only around town but also within a particular
building”).
       Many of the concerns expressed by Chief Justice Roberts in his
Carpenter opinion are highly salient in the context of geofence warrants.
Perhaps the most alarming aspect of geofences is the potential for
“permeating police surveillance.” As Chief Justice Roberts explained,
modern cell phones enable the government to achieve “near perfect
surveillance”; carrying one of these devices is essentially a prerequisite to
participation in modern society, and users “compulsively carry cell phones
with them all the time.” Id. at 311–12, 315. Geofences also exemplify the
Court’s concern with pinpoint location data—this technology provides more



                                           24
Case: 23-60321         Document: 113-1           Page: 25       Date Filed: 08/09/2024




                                       No. 23-60321


precise location data than either CSLI or GPS. Geofence Warrants and the
Fourth Amendment, supra at 2510. Furthermore, obtaining data through
geofences, like obtaining data through CSLI, is “remarkably cheap, easy,
and efficient compared to traditional investigative tools.” Carpenter, 585
U.S. at 311. With “just the click of a button,” the government can search the
pinpoint locations of over half a billion people with Location History enabled.
See id.
          But while we see the parallels between CSLI and Location History
data, our colleagues on the Fourth Circuit—the first federal Circuit to
address whether geofencing is a “search” subject to the Fourth
Amendment—saw Location History data differently. See Chatrie (App.), 107
F.4th at 330. Characterizing Location History data as nothing more than a
“record of a person’s single, brief trip,” the Fourth Circuit found that
geofencing does not contravene a person’s “reasonable expectation of
privacy” because the data implicated by geofences is “far less revealing than
that obtained in Jones[ or] Carpenter.” Id. at 330–31. 7 With great respect to
our colleagues on the Fourth Circuit, we disagree. While it is true that
geofences tend to be limited temporally, the potential intrusiveness of even a
snapshot of precise location data should not be understated. As two
commentators noted:

          _____________________
          7
           In United States v. Davis, the Eleventh Circuit appeared to agree with the Fourth
Circuit that geofence warrants “do[] not implicate the same privacy concerns raised in
Carpenter.” See 2024 WL 3573478, at *6. However, Davis ultimately concerned a
defendant’s Fourth Amendment standing to challenge a geofence warrant that obtained his
girlfriend’s Google Location History data, not his own data. Id. at *6. Thus, the Eleventh
Circuit’s discussion of the intrusiveness of Google Location History data ultimately does
not appear to have been dispositive to its holding. See id. at *6–7 (“Because the geofence
revealed the location of an open program that was not [the defendant’s] and was not on a
phone in his exclusive possession or control, he cannot argue that he had a privacy interest
in this data that gives him Fourth Amendment standing to challenge the search.”).




                                                25
Case: 23-60321         Document: 113-1           Page: 26       Date Filed: 08/09/2024




                                       No. 23-60321


        [E]ven a brief snapshot can expose highly sensitive
        information—think a visit to “the psychiatrist, the plastic
        surgeon, the abortion clinic, the AIDS treatment center, the
        strip club, the criminal defense attorney, the by-the-hour-
        motel, the union meeting, the mosque, synagogue or church,
        [or] the gay bar,” or a location other than home during a
        COVID-19 shelter-in-place order.
Amster & Diehl, Against Geofences, supra at 408 (quoting Jones, 565 U.S. at
415 (Sotomayor, J., concurring)). Plus, such location tracking can easily
follow an individual into areas normally considered some of the most private
and intimate, particularly residences. As another commentator described:
        Even a geofence warrant that limits itself to a single day could
        follow a person from the interior of their home, among the
        rooms of their dwelling, to the location of a crime, then to a
        place of worship, then perhaps to a new home, such as that of
        a relative or friend, and among the rooms of that second
        dwelling.
A. Reed McLeod, Note, Geofence Warrants: Geolocating the Fourth
Amendment, 30 Wm. & Mary Bill Rts. J. 531, 549 (2021). 8 In short,

        _____________________
        8
           The Fourth Circuit acknowledged and dismissed these considerations because,
inter alia, the defendant—like the defendants in the case at bar—“d[id] not contend that
the warrant revealed his own movements within his own constitutionally protected space,”
and thus the defendant lacked Fourth Amendment standing to challenge geofencing on
those grounds. See Chatrie (App.), 107 F.4th at 330 n.17, 337 n.26. We disagree—this
conclusion directly conflicts with Carpenter.
         In Carpenter, the Supreme Court’s analysis of whether the government’s access of
the defendant’s CSLI impeded his reasonable expectation of privacy was not based on a
review of the specific results of the search in that case. See generally 585 U.S. at 309–13.
Rather, the Supreme Court analyzed the general capabilities of CSLI, and asked whether
the ability for CSLI “to chronicle a person’s past movements through the record of his cell
phone signals” created an expectation of privacy. Id. at 309. In other words, it did not
matter whether that defendant happened to stay outside of a constitutionally protected area
during a search or not. The question was whether the technology utilized by law




                                                26
Case: 23-60321           Document: 113-1           Page: 27        Date Filed: 08/09/2024




                                        No. 23-60321


geofence location data is invasive for Fourth Amendment purposes. Of
particular concern is the fact that a geofence will retroactively track anyone
with Location History enabled, regardless of whether a particular individual
is suspicious or moving within an area that is typically granted Fourth
Amendment protection. 9
        Moreover, Carpenter’s application to the third-party doctrine in this
case is straightforward. As the Court in Carpenter explained, while cell phone
data is held by private corporations, on a practical level, it is unreasonable to
think of cell phone users as voluntarily assuming the risk of turning over
        _____________________
enforcement had the capability of providing data that offered “an all-encompassing record
of [a person’s] whereabouts,” regardless of whether that person actually entered spaces
that are traditionally considered protected under the Fourth Amendment. Id. at 311. And,
when a person has a “reasonable expectation of privacy in the place or thing searched or
seized,” he or she has Fourth Amendment standing. See United States v. Gaulden, 73 F.4th
390, 392 (5th Cir. 2023).
         Here, the analysis is no different. The question is whether Location History data
has the capability of revealing intimate, private details about a person’s life, thus conferring
a “reasonable expectation of privacy.” This is general inquiry, not a retroactive, post-hoc
examination based on the results of the search in our case. A conclusion to the contrary
would be enigmatic. See Chatrie (App.), 107 F.4th at 351 (Wynn, J., dissenting) (“The
government . . . cannot circumvent the Constitution merely because, by sheer luck, its
target did not stray from the safe zone.”).
        9
            Some have argued that the privacy concerns presented by geofences are
ameliorated by the fact that information sent to law enforcement is, at first, anonymized.
See, e.g., In re Search of Info. Stored at Premises Controlled by Google, No. 2:22-MJ-01325,
2023 WL 2236493, at *8 (S.D. Tex. Feb. 14, 2023). However, it is undisputed that the data
is eventually de-anonymized. And, even setting that point aside, the effectiveness of data
anonymization has been called into question by researchers, given that anonymous data can
be cross-referenced to reveal identities. See Amster & Diehl, Against Geofences, supra at
409; see also Charlie Warzel & Stuart A. Thompson, They Stormed the Capitol. Their Apps
Tracked Them., N.Y. Times (Feb. 5, 2021), https://perma.cc/KMP3-3QSV (detailing
journalists’ efforts to identify individuals contained in anonymized datasets of smartphone
locations); Gina Kolata, Your Data Were ‘Anonymized’? These Scientists Can Still Identify
You, N.Y. Times (July 23, 2019), https://perma.cc/L5DL-MPZM. Thus, we find this
argument wanting.




                                                   27
Case: 23-60321      Document: 113-1       Page: 28     Date Filed: 08/09/2024




                                  No. 23-60321


comprehensive dossiers of their physical movements to third parties.
Carpenter, 585 U.S. at 315. In a way, Carpenter acknowledged that, at least in
some instances, the third-party doctrine is “ill suited to the digital age, in
which people reveal a great deal of information about themselves to third
parties in the course of carrying out mundane tasks.” Jones, 565 U.S. at 417
(Sotomayor, J., concurring). Given the ubiquity—and necessity—in the
digital age of entrusting corporations like Google, Microsoft, and Apple with
highly sensitive information, the notion that users voluntarily relinquish their
right to privacy and “assume[] the risk” of this information being divulged
to law enforcement is dubious. See Smith, 442 U.S. at 745.
       It is true that this case is slightly distinguishable from Carpenter;
namely, that users opt in to having their Location History monitored. Indeed,
this was the other consideration that persuaded the Fourth Circuit that
geofencing is not a “search” subject to the Fourth Amendment. See Chatrie
(App.), 107 F.4th at 331–32. Again, with great respect, we are not convinced.
       As anyone with a smartphone can attest, electronic opt-in processes
are hardly informed and, in many instances, may not even be voluntary. See
Daniel J. Solove, Privacy Self-Management and the Consent Dilemma, 126
Harv. L. Rev. 1880, 1884–88 (2013). See generally Hannah J. Hutton &
David A. Ellis, Exploring User Motivations Behind iOS App Tracking
Transparency Decisions, Proc. of the 2023 CHI Conf. on Hum.
Factors in Computing Sys., Apr. 2023, at 1, 7–8, 10 (detailing
general “confusion” with, and “misconceptions” about, Apple’s data-
tracking opt-in prompts due, in part, to those prompts’ “lack of clarity”).
Google’s Location History opt-in process is no different. As described above,
users are bombarded multiple times with requests to opt in across multiple
apps. See Chatrie (Dist.), 590 F. Supp. 3d at 908–09. These requests typically
innocuously promise app optimization, rather than reveal the fact that users’
locations will be comprehensively stored in a “Sensorvault,” providing



                                          28
Case: 23-60321       Document: 113-1       Page: 29     Date Filed: 08/09/2024




                                  No. 23-60321


Google the means to access this data and share it with the government. See
Chatrie (App.), 107 F.4th at 359–60 (Wynn, J., dissenting); see also Defendant
Okello Chatrie’s Supplemental Motion to Suppress Evidence Obtained from
a “Geofence” General Warrant at 15–17, United States v. Chatrie, No. 19-cr-
00130 (E.D. Va. May 22, 2020), 2020 WL 4551093, ECF No. 104. Even
Google’s own employees have indicated that deactivating Location History
data based on Google’s “limited and partially hidden” warnings is “difficult
enough that people won’t figure it out.” Chatrie (App.), 107 F.4th at 360, 367
(Wynn, J., dissenting) (quoting Chatrie (Dist.), 590 F. Supp. 3d at 913, 936);
Amster & Diehl, Against Geofences, supra at 396–97.
       But you don’t have to take our word for it—others have similarly
questioned the “voluntary” nature of Google’s opt-in process. See, e.g., In re
Search of Info. Stored at Premises Controlled by Google, 481 F. Supp. 3d at 737
& n.3 (“The Court finds it difficult to imagine that users of electronic devices
would affirmatively realize, at the time they begin using the device, that they
are providing their location information to Google in a way that will result in
the government’s ability to obtain—easily, quickly and cheaply—their
precise geographical location at virtually any point in the history of their use
of the device.”); McLeod, Geolocating the Fourth Amendment, supra at 543
(“[C]onsider a Google user’s consent to Location History . . . . [u]sers either
opt in with less than explicit notice given to them, or even with good notice,
without a full realization of the potential consequences to their privacy if they
opt in. Second, users may understand the notice they have been given, but
misunderstand the accuracy of the movement patterns as expressed in the
location data collected by tech companies.”); Chatrie (Dist.), 590 F. Supp. 3d
at 935 (acknowledging that users take “some affirmative steps to enable
location history,” yet concluding that “those steps likely do not constitute a
full assumption of the attendant risk of permanently disclosing one’s
whereabouts during almost every minute of every hour of every day”); see




                                           29
Case: 23-60321         Document: 113-1          Page: 30      Date Filed: 08/09/2024




                                       No. 23-60321


also Chatrie (App.), 107 F.4th at 356–61 (Wynn, J., dissenting); Amster &
Diehl, Against Geofences, supra at 396–97, 409–10.
        Not to mention, the fact that approximately 592 million people have
“opted in” to comprehensive tracking of their locations itself calls into
question the “voluntary” nature of this process. In short, “a user simply
cannot forfeit the protections of the Fourth Amendment for years of precise
location information by selecting ‘YES, I’M IN’ at midnight while setting up
Google Assistant, even if some text offered warning along the way.” Chatrie
(Dist.), 590 F. Supp. 3d at 936.
                                   *        *         *
        To conclude, we hold that law enforcement in this case did conduct a
search when it sought Location History data from Google. Given the
intrusiveness and ubiquity of Location History data, Smith and McThunel
correctly contend that they have a “reasonable expectation of privacy” in
their respective data. Additionally, per Carpenter, the third-party doctrine
does not apply.
                          B. General Constitutionality
        Having concluded that the acquisition of Location History data via a
geofence is a search, it follows that the government must generally obtain a
warrant supported by probable cause and particularity before requesting such
information. Carpenter, 585 U.S. at 316. Accordingly, we turn to the issue of
whether geofence warrants satisfy this mandate, addressing Appellants’
argument that these novel warrants resemble unconstitutional general
warrants prohibited by the Fourth Amendment. 10


        _____________________
        10
         Because the Fourth Circuit concluded that law enforcement did not conduct a
search when it sought Location History data from Google, it did not reach the question of




                                                30
Case: 23-60321       Document: 113-1      Page: 31     Date Filed: 08/09/2024




                                  No. 23-60321


       “[T]he Fourth Amendment was the founding generation’s response
to the reviled ‘general warrants’ and ‘writs of assistance’ of the colonial era,
which allowed British officers to rummage through homes in an unrestrained
search for evidence of criminal activity.” Riley, 573 U.S. at 403. “General
warrants” are warrants that “specif[y] only an offense,” leaving “to the
discretion of the executing officials the decision as to which persons should
be arrested and which places should be searched.” Steagald v. United States,
451 U.S. 204, 220 (1981); Geofence Warrants and the Fourth Amendment, supra
at 2518.
       It is undeniable that general warrants are plainly unconstitutional.
Indeed, “it would be a needless exercise in pedantry to review again the
detailed history of the use of general warrants as instruments of oppression
from the time of the Tudors, through the Star Chamber, the Long
Parliament, the Restoration, and beyond.” Stanford v. Texas, 379 U.S. 476,
482 (1965). Thus, courts have recognized that no warrant “can authorize the
search of everything or everyone in sight.” Geofence Warrants and the Fourth
Amendment, supra at 2518; cf. Marks v. Clarke, 102 F.3d 1012, 1029 (9th Cir.
1996) (“[A] warrant to search ‘all persons present’ for evidence of a crime
may only be obtained when there is reason to believe that all those present
will be participants in the suspected criminal activity.”); Owens ex rel. Owens
v. Lott, 372 F.3d 267, 276 (4th Cir. 2004) (“[A]n ‘all persons’ warrant can
pass constitutional muster if the affidavit and information provided to the
magistrate supply enough detailed information to establish probable cause to
believe that all persons on the premises at the time of the search are involved
in the criminal activity.”).


       _____________________
whether geofence warrants pass muster under the Fourth Amendment’s warrant
requirement.




                                          31
Case: 23-60321         Document: 113-1          Page: 32      Date Filed: 08/09/2024




                                      No. 23-60321


        When law enforcement submits a geofence warrant to Google, Step 1
forces the company to search through its entire database to provide a new
dataset that is derived from its entire Sensorvault. In other words, law
enforcement cannot obtain its requested location data unless Google searches
through the entirety of its Sensorvault—all 592 million individual accounts—
for all of their locations at a given point in time. Moreover, this search is
occurring while law enforcement officials have no idea who they are looking
for, or whether the search will even turn up a result. Indeed, the
quintessential problem with these warrants is that they never include a
specific user to be identified, only a temporal and geographic location where
any given user may turn up post-search. 11 That is constitutionally insufficient.
        Geofence warrants present the exact sort of “general, exploratory
rummaging” that the Fourth Amendment was designed to prevent. Coolidge
v. New Hampshire, 403 U.S. 443, 467 (1971); see also Riley, 573 U.S. at 403;
Geofence Warrants and the Fourth Amendment, supra at 2519. In fact, Google
Maps creator Brian McClendon has called these warrants “fishing
expedition[s],” and explained that Google employees originally assumed law
enforcement would only seek Location History data on specific people—a
reality that did not come true. Jennifer Valentino-DeVries, Tracking Phones,

        _____________________
        11
           As Professor Stephen Henderson explains in his discussion of CSLI, focusing
probable cause on the group rather than the individual “would mean that a larger database
is always preferred” by law enforcement, because “by definition there will be evidence of
crime in that larger set.” Stephen E. Henderson, Response, A Rose by Any Other Name:
Regulating Law Enforcement Bulk Metadata Collection, 94 Tex. L. Rev. See Also 28, 40–
41 (2016). Doing so leads to an “absurd” understanding of probable cause: “[A] prosecutor
confident that a bank customer is committing tax fraud could access the combined records
of all customers of that bank because, somewhere in there, she is very sure is evidence of
crime.” Id. at 41. Henderson argues, in the context of CSLI, it must be the case that
probable cause is required for “each person’s obtained records,” meaning here “each
phone number contained within the dump.” Id. The same argument applies with full force
to Google accounts containing Location History data.




                                               32
Case: 23-60321           Document: 113-1           Page: 33        Date Filed: 08/09/2024




                                        No. 23-60321


Google Is a Dragnet for the Police, N.Y. Times (Apr. 13, 2019),
https://perma.cc/NCF3-H5DP. “Awareness that the government may be
watching chills associational and expressive freedoms.” Jones, 565 U.S. at
416 (Sotomayor, J., concurring.). And, when these core rights are at issue,
the warrant requirement must “be accorded the most scrupulous
exactitude.” See Stanford, 379 U.S. at 485.
        Here, the Government contends that geofence warrants are not
general warrants because they are “limited to specified information directly
tied to a particular [crime] at a particular place and time.” This argument
misses the mark. While the results of a geofence warrant may be narrowly
tailored, the search itself is not. A general warrant cannot be saved simply by
arguing that, after the search has been performed, the information received
was narrowly tailored to the crime being investigated. These geofence
warrants fail at Step 1—they allow law enforcement to rummage through
troves of location data from hundreds of millions of Google users without any
description of the particular suspect or suspects to be found. 12

        _____________________
        12
            The Fourth Circuit—albeit in the context of determining whether law
enforcement’s acquisition of Location History data qualified as a “search” under the
Fourth Amendment—appeared to contend that Google’s search at Step 1 is irrelevant to
our inquiry because Google, rather than law enforcement, conducts that search. See Chatrie
(App.), 107 F.4th at 330 n.16. Instead, the Fourth Circuit concluded that “the proper focus
of our inquiry [should be] . . . the government’s access of two hours’ worth of [defendant’s]
Location History data,” i.e., Step 2, because “a search only occurs once the government
accesses the requested information.” Id.
         This proposition is breathtaking. In essence, the Fourth Circuit appears to
conclude that law enforcement may flaunt the Fourth Amendment by simply offloading
their act of “searching” on to a third party, and waiting to see if that third party’s search
produces any fruit before applying for a warrant. Moreover, by implication, if the third
party’s search produces zero evidence, law enforcement never conducted any search at all.
         But the Supreme Court has clearly stated that the Fourth Amendment protects
against both searches and seizures “effected by a private party . . . if the private party acted
as an instrument or agent of the Government.” Skinner v. Ry. Lab. Execs.’ Ass’n, 489 U.S.




                                                   33
Case: 23-60321         Document: 113-1          Page: 34       Date Filed: 08/09/2024




                                      No. 23-60321


        In sum, geofence warrants are “[e]mblematic of general warrants”
and are “highly suspect per se.” Geofence Warrants and the Fourth
Amendment, supra at 2520; Amster & Diehl, Against Geofences, supra at 433–
34; Chad Marlow & Jennifer Stisa Granick, Celebrating an Important Victory
in the Ongoing Fight Against Reverse Warrants, ACLU (Jan. 29, 2024),
https://perma.cc/SC2R-S7PJ (“The constitutionality of reverse warrants is
highly suspect because, like general warrants that are prohibited by the
Fourth Amendment, they permit searches of vast quantities of private,
personal information without identifying any particular criminal suspects or
demonstrating probable cause to believe evidence will be located in the
corporate databases they search.”); Chatrie (App.), 107 F.4th at 353 (Wynn,
J., dissenting) (“[A] [geofence] warrant is uncomfortably akin to the sort of
‘reviled’ general warrants used by English authorities that the Framers
intended the Fourth Amendment to forbid.”).
        This court “cannot forgive the requirements of the Fourth
Amendment in the name of law enforcement.” Berger v. New York, 388 U.S.
41, 62 (1967). Accordingly, we hold that geofence warrants are general
warrants categorically prohibited by the Fourth Amendment. We now move
on to suppression and the good-faith exception to the warrant requirement.
                             C. Good-Faith Exception
        In United States v. Leon, 468 U.S. 897, 913 (1984), the Supreme Court
evaluated the Fourth Amendment exclusionary rule, and opined that
        _____________________
602, 613–14 (1989). And, here, all of Google’s actions, including at Step 1, are “conducted
in response to legal compulsion and ‘with the participation or knowledge of [a]
governmental official.’” Geofence Warrants and the Fourth Amendment, supra at 2516
(quoting United States v. Jacobsen, 466 U.S. 109, 113 (1984)). Accordingly, law enforcement
must abide by the Fourth Amendment not only when Google provides them with a final list
of names, but also when they instruct Google to search its entire Sensorvault to produce
those names. Id. Put differently, the proper focus of our inquiry does include Step 1.




                                                34
Case: 23-60321          Document: 113-1          Page: 35       Date Filed: 08/09/2024




                                       No. 23-60321


evidence seized by officers reasonably relying on a warrant issued by a
detached and neutral magistrate judge should be admissible. 13 However, the
Court articulated four circumstances where this “good faith” exception does
not apply:
        (1) when the issuing magistrate was misled by information in an
        affidavit that the affiant knew or reasonably should have known
        was false; (2) when the issuing magistrate wholly abandoned
        his judicial role; (3) when the warrant affidavit is so lacking in
        indicia of probable cause as to render official belief in its
        existence unreasonable; and (4) when the warrant is so facially
        deficient in failing to particularize the place to be searched or
        the things to be seized that executing officers cannot
        reasonably presume it to be valid.
United States v. Woerner, 709 F.3d 527, 533–34 (5th Cir. 2013) (citing Leon,
468 U.S. at 921–25).
        Appellants argue that three of the Leon circumstances apply in this
case. First, Appellants contend that Inspectors knowingly or recklessly
included a false statement in the warrant affidavit, specifically, the statement
that “it appear[ed] the robbery suspect [was] possibly using a cellular device

        _____________________
        13
           Appellants argue that “[t]here is no such thing as relying on a general warrant in
good-faith,” and that an application of Leon is categorically unnecessary. Their argument
is well taken, but we decline to adopt that stance today. Appellants point the court to Groh
v. Ramirez, 540 U.S. 551, 558, 563 (2004), which held that “no reasonable officer could
believe that a warrant that plainly did not comply with [the particularity] requirement was
valid,” and which cited Leon even though the issue in Groh was ultimately about qualified
immunity. However, Groh did not involve a novel advancement in law enforcement
technology—in fact, Groh involved an essentially run-of-the-mill warrant to search for guns
in a house. Id. at 554–57. Given the novelty and complexity of geofence warrants, as well as
the dearth of legal authority on the topic of geofence warrants to guide law enforcement,
Groh is distinguishable on its facts. Moreover, the other cases cited by Appellants are also
unavailing, as a majority were decided prior to Leon. Accordingly, we hold that Leon applies
to our analysis.




                                                 35
Case: 23-60321       Document: 113-1       Page: 36      Date Filed: 08/09/2024




                                  No. 23-60321


both before and after the robbery occur[ed].” Appellants maintain that
Matney and Mathew’s use of a “go-by” is indicative of the fact that they had
no idea whether a cell phone was used, and that this is “by definition reckless
at best.” We disagree. As the district court noted, video evidence of the
assailant appears to show body language consistent with cell phone use.
Mathews and Matney reviewed this video footage in addition to using a “go-
by.” In essence, Appellants ask this court to ignore Matney’s testimony that
the Inspectors based their probable cause statement in the warrant affidavit,
in part, on this footage. Because this court is highly deferential to the district
court’s factfinding, and because the court reviews evidence in the light most
favorable to the Government, see Pack, 612 F.3d at 347, Appellants’ argument
fails.
         Appellants’ second and third Leon arguments pertain to probable
cause and particularity—i.e., that the warrant was “completely devoid” of
probable cause, or that it was “facially deficient” in particularity, rendering
the Inspectors’ conclusions unreasonable. Again, we disagree. Here, we find
the rationale behind the Fourth Circuit’s opinion in United States v. McLamb,
880 F.3d 685 (4th Cir. 2018), persuasive. In McLamb, the Fourth Circuit
declined to suppress evidence when officers were utilizing “cutting edge
investigative techniques” and consulted with attorneys from the Department
of Justice. Id. at 690–91. Here, the Inspectors likewise had conversations with
other law enforcement officials and the U.S. Attorney’s Office prior to
submitting their warrant. To this end, we, like the district court “struggle[]
to see any wrongful conduct to deter,” because “the conduct of law
enforcement in this case seem[ed] reasonable and appropriate when
considering the specific circumstances with which the investigators were
faced.”
         At bottom, “but-for causality is only a necessary, not a sufficient,
condition for suppression.” Hudson, 547 U.S. at 592. This court must also



                                           36
Case: 23-60321          Document: 113-1           Page: 37        Date Filed: 08/09/2024




                                        No. 23-60321


weigh the “substantial social costs” of exclusion against “deterrence
benefits,” the “existence of which [is also] a necessary condition for
exclusion.” Id. at 594–96 (internal quotations omitted). Here, the social costs
of exclusion are admittedly considerable, including the consequences “that
exclusion of relevant incriminating evidence always entails (viz., the risk of
releasing dangerous criminals into society).” Id. at 595. Additionally, the
deterrence benefits here are not clear. The Inspectors were utilizing a
cutting-edge investigative technique with which neither Inspector had
personal experience. To that end, the Inspectors diligently attempted to
make sure that their warrant comported with the Fourth Amendment by
communicating with other law enforcement agencies and the U.S.
Attorney’s Office, and the Inspectors exhibited no malicious intent through
the actions that they took. Thus, we cannot fault law enforcement’s actions
considering the novelty of the technique and the dearth of court precedent to
follow. 14 Accordingly, none of Leon’s circumstances apply, and the district
court correctly declined to suppress evidence under the good-faith exception
to the warrant requirement. 15


        _____________________
        14
            For the same reasons, we agree with the district court that the Inspectors’
mistaken belief regarding the meaning of the phrase “further legal process,” and their
failure to apply for additional warrants at Steps 2 and 3, do not preclude the applicability of
the good faith exception.
        15
           Appellants also argue that the district court erred by failing to exclude the
Government’s expert witness, Christopher Moody, at trial as unreliable under Daubert v.
Merrell Dow Pharmaceuticals, Inc., 509 U.S. 579 (1993). We disagree. “District courts enjoy
wide latitude in determining the admissibility of expert testimony, and the discretion of the
trial judge and his or her decision will not be disturbed on appeal unless manifestly
erroneous.” Watkins v. Telsmith, Inc., 121 F.3d 984, 988 (5th Cir. 1997) (internal quotation
omitted). “‘Manifest error’ is one that is ‘plain and indisputable, and that amounts to a
complete disregard of the controlling law.’” Kim v. Am. Honda Motor Co., 86 F.4th 150,
159 (5th Cir. 2023) (quoting Bear Ranch, L.L.C. v. Heartbrand Beef, Inc., 885 F.3d 794, 802
(5th Cir. 2018)).




                                                  37
Case: 23-60321         Document: 113-1          Page: 38       Date Filed: 08/09/2024




                                      No. 23-60321


                                   IV. Conclusion
        We hold that geofence warrants are modern-day general warrants and
are unconstitutional under the Fourth Amendment. However, considering
law enforcement’s reasonable conduct in this case in light of the novelty of
this type of warrant, we uphold the district court’s determination that
suppression was unwarranted under the good-faith exception.
        AFFIRMED.




        _____________________
         Here, Moody testified about two technological areas: (1) CSLI; and (2) Google
Location History. First, Appellants acknowledge that this court has accepted historical
cellular site analysis in the past as the subject of expert testimony. See United States v.
Schaffer, 439 F. App’x 344, 347 (5th Cir. 2011). Second, it is undisputed that Google
Location History is a collection of data that is itself derived from a combination of three
forms of geolocation—CSLI, GPS, and Wi-Fi. Thus, Moody’s extensive knowledge, skill,
experience, training, and education in historically reliable forms of geolocation, such as
CSLI, GPS, and Wi-Fi, allowed him to discuss Google Location History data, which is
itself derived from those very sources. At bottom, the district court did not commit error,
let alone manifest error, by allowing Moody to testify.




                                                38
Case: 23-60321      Document: 113-1       Page: 39   Date Filed: 08/09/2024




                                No. 23-60321


James C. Ho, Circuit Judge, concurring:
      Geofence warrants are powerful tools for investigating and deterring
crime. The defendants here engaged in a violent robbery—and likely would
have gotten away with it, but for this new technology. So I fully recognize
that our panel decision today will inevitably hamper legitimate law
enforcement interests.
      But hamstringing the government is the whole point of our
Constitution. Our Founders recognized that the government will not always
be comprised of publicly-spirited officers—and that even good faith actors
can be overcome by the zealous pursuit of legitimate public interests. “If
men were angels, no government would be necessary.” The Federalist
No. 51, at 349 (J. Cooke ed. 1961). “If angels were to govern men, neither
external nor internal controls on government would be necessary.” Id. But
“experience has taught mankind the necessity of auxiliary precautions.” Id.
It’s because of “human nature” that it’s “necessary to control the abuses of
government.” Id.
       Our decision today is not costless. But our rights are priceless.
Reasonable minds can differ, of course, over the proper balance to strike
between public interests and individual rights. Time and again, modern
technology has proven to be a blessing as well as a curse. Our panel decision
today endeavors to apply our Founding charter to the realities of modern
technology, consistent with governing precedent. I concur in that decision.




                                     39

```

---

## GROUP: content/cases/United States v. Soto-Peguero.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Soto-Peguero"
type: case
citation: "978 F.3d 13 (2020)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, First Circuit"
court_level: coa
circuit: 1st
year: 2020
date_decided: 2020-10-19
docket: ""
authority_weight: "Binding in-circuit — 1st Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2020-10-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Soto-Peguero
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4798028/united-states-v-soto-peguero/"
  cluster_id: 4798028
  opinion_id: 4578375
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Recent development (role-based)"
related: ["[[Nix v. Williams]]", "[[United States v. Neugin]]", "[[Murray v. United States]]"]
aliases: ["United States v. Soto-Peguero (1st Cir. 2020)"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "inevitable-discovery", "search-warrant", "first-circuit"]
holding: "Illustrative application of inevitable discovery: government met its burden (agent would have sought and obtained a warrant regardless),…"
lake:
  record_id: United States v. Soto-Peguero
  status: verified
  projected_at: 2026-07-06
---

# United States v. Soto-Peguero

*978 F.3d 13 (1st Cir. 2020)* · U.S. Court of Appeals, First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While securing Soto-Peguero's apartment, Task Force members exceeded the scope of a [[Securing the Scene|protective sweep]] — manipulating an object in a vent and opening a black bag — and found heroin and a gun. The District Court agreed the search went beyond a lawful [[Securing the Scene|protective sweep]], but denied suppression under the inevitable-discovery exception, crediting Special Agent Rideout's testimony that he would have sought and obtained a search warrant regardless. Soto-Peguero appealed.

## Issue
Whether evidence found during a search that exceeded a lawful [[Securing the Scene|protective sweep]] was nonetheless admissible under the inevitable-discovery exception to the exclusionary rule.

## Rule
Under the inevitable-discovery exception, unlawfully obtained evidence is admissible where the government shows it would have been discovered by lawful means. The government carried that burden here: "Because Soto-Peguero has not succeeded in establishing that the United States failed to meet the requirements for applying the inevitable discovery doctrine, we affirm the District Court's denial of his motion to suppress." — *United States v. Soto-Peguero*, 978 F.3d 13 (1st Cir. 2020) (slip op., at 21). ^pin-op21

## Application
The decisive fact was that Soto-Peguero did not challenge Special Agent Rideout's testimony that he would have pursued a search warrant regardless of what the warrantless sweep turned up — and the record showed a warrant would have issued. Soto-Peguero's catalog of alleged officer misconduct during the entry did not defeat the doctrine on these facts. The heroin and gun therefore would inevitably have been discovered through a lawful warrant, so suppression was not required.

## Conclusion
The inevitable-discovery exception applied; the First Circuit affirmed the denial of Soto-Peguero's motion to suppress.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 1st Cir.**
- No negative treatment. *Soto-Peguero* is an illustrative application in which [[Inevitable Discovery and Independent Source|inevitable discovery]] **succeeded** — the government showed a warrant would have been sought and obtained — the mirror image of [[United States v. Neugin]] (10th Cir.), where the chain to discovery was too speculative.

## Appears on
- [[The Exclusionary Rule]] — *Recent development (role-based)*

## Sources
- *United States v. Soto-Peguero*, 978 F.3d 13 (1st Cir. 2020) — https://www.courtlistener.com/opinion/4798028/united-states-v-soto-peguero/ — pinpoint given as slip-opinion page (CourtListener carries the slip opinion; cluster 4798028 → opinion 4578375).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "925295885649d41e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "978 F.3d 13 (2020)", "court": "U.S. Court of Appeals, First Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Soto-Peguero", "year": "2020"}}
{"assertion_id": "a057c2f34dbdeb79", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Illustrative application of inevitable discovery: government met its burden (agent would have sought and obtained a warrant regardless),…", "title": "United States v. Soto-Peguero"}}
{"assertion_id": "f4bd1307beb89f1b", "dimension": "support", "kind": "home_role", "locator": {"home": "Inevitable Discovery & Independent Source"}, "payload": {"home": "Inevitable Discovery & Independent Source", "role": "Recent development (role-based)", "title": "United States v. Soto-Peguero"}}
{"assertion_id": "bacf6476c9fde07c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2020-10-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Soto-Peguero", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Soto-Peguero", "varies_by_point": "false"}}
{"assertion_id": "d7ad14cbbd9793f3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 1st Cir.", "title": "United States v. Soto-Peguero"}}
```

### lake record — United States v. Soto-Peguero

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Soto-Peguero",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Soto-Peguero",
    "case_name_short": "Soto-Peguero",
    "case_name_full": "",
    "input_case_name": "United States v. Soto-Peguero",
    "court": "U.S. Court of Appeals, First Circuit",
    "court_id": "ca1",
    "court_level": "coa",
    "circuit": "1st",
    "state": null,
    "date_decided": "2020-10-19",
    "year": 2020,
    "docket": null,
    "cluster_id": 4798028,
    "lead_opinion_id": 4578375,
    "sibling_ids": [
      4578375
    ],
    "absolute_url": "/opinion/4798028/united-states-v-soto-peguero/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "978 F.3d 13",
      "volume": "978",
      "reporter": "F.3d",
      "page": "13",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "978 F.3d 13",
        "volume": "978",
        "reporter": "F.3d",
        "page": "13",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "978 F.3d 13",
    "official_selection": {
      "court_class": "coa",
      "selected": "978 F.3d 13",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op21",
      "page": null,
      "quote": "--- # United States v. Soto-Peguero *978 F.3d 13 (1st Cir. 2020)* \u00b7 U.S. Court of Appeals, First Circuit \u00b7 **Binding in-circuit \u2014 1st Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While securing Soto-Peguero's apartment, Task Force members exceeded the scope of a protective sweep \u2014 manipulating an object in a vent and opening a black bag \u2014 and found heroin and a gun. The District Court agreed the search went beyond a lawful protective sweep, but denied suppression under the inevitable-discovery exception, crediting Special Agent Rideout's testimony that he would have sought and obtained a search warrant regardless. Soto-Peguero appealed. ## Issue Whether evidence found during a search that exceeded a lawful protective sweep was nonetheless admissible under the inevitable-discovery exception to the exclusionary rule. ## Rule Under the inevitable-discovery exception, unlawfully obtained evidence is admissible where the government shows it would have been discovered by lawful means. The government carried that burden here:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-10-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Soto-Peguero",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Cruz-Ramos",
          "cluster_id": 4851346,
          "cite": [
            "987 F.3d 27"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McKinney",
          "cluster_id": 4900948,
          "cite": [
            "5 F.4th 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Griffin",
          "cluster_id": 10761945,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez",
          "cluster_id": 5291287,
          "cite": [
            "16 F.4th 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4578375) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca1)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(4578375)",
        "reviewed": 4,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4578375)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4578375)",
    "indexed_citing_opinions": 4,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4578375,
        "count": 4,
        "count_source": "search"
      }
    ],
    "citation_count": 4,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-soto-peguero.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 4,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4578375,
        "cited_id": 195103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 195255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 196856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 197057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 200733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 201990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 202008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 468097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 757241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 775404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 2684150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4194190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4376569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4465506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4554929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 7243442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9429647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9431434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9441370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9490523,
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
    "date_created": "2026-07-06T03:08:45Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:09:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:09:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:10:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:09:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Soto-Peguero

```
          United States Court of Appeals
                       For the First Circuit


No. 18-1897

                     UNITED STATES OF AMERICA,

                             Appellee,

                                 v.

                       ORISTEL SOTO-PEGUERO,

                       Defendant, Appellant.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                FOR THE DISTRICT OF MASSACHUSETTS

              [Hon. Rya W. Zobel, U.S. District Judge]


                               Before

                   Thompson, Kayatta, and Barron,
                           Circuit Judges.


     Jane Elizabeth Lee for appellant.
     Theodore B. Heinrich, Assistant United States Attorney, with
whom Andrew E. Lelling, United States Attorney, was on brief, for
appellee.


                          October 19, 2020
              BARRON, Circuit Judge.           In April 2018, Oristel Soto-

Peguero was convicted in the District of Massachusetts on three

counts related to distribution of heroin in violation of 21 U.S.C.

§ 841(a)(1) and § 846 and one count of discharging a firearm in

furtherance of a drug crime in violation of 18 U.S.C. § 924(c).

The District Court sentenced him to twenty-two years in prison.

Soto-Peguero now argues on appeal that the District Court erred in

denying his motion to suppress certain evidence at trial.                    He also

asserts that the District Court should not have concluded that he

was eligible for a two-level role enhancement under the United

States Sentencing Guidelines.             He thus asks us to vacate his

convictions and resulting sentence.             We affirm.

                                         I.

              We begin by summarizing the facts in the record, viewing

them in the light most favorable to the suppression ruling.                       See

United States v. Arnott, 758 F.3d 40, 43 (1st Cir. 2014).                          In

January 2015, a Task Force consisting of agents from the federal

Drug       Enforcement    Agency   ("DEA")      and    officers     from    several

Massachusetts       law    enforcement    agencies      were      engaged    in    an

investigation       of     potential     heroin       suppliers     in      Taunton,

Massachusetts.1          Pursuant to that joint investigation, between


       1
       We note that this investigation also led to the indictment
of Luis Guzman-Ortiz, whom a separate jury found guilty of
conspiring with Soto-Peguero to distribute heroin. Guzman-Ortiz
successfully filed a motion for acquittal on that charge pursuant


                                       - 2 -
January and July 2015, Task Force members used a series of wiretaps

to   investigate   Eddyberto    Mejia-Ramos,     a     suspected     local

trafficker.

          The   wiretaps   intercepted   a   number    of    conversations

between Mejia-Ramos and Soto-Peguero, which indicated that Soto-

Peguero was supplying Mejia-Ramos with heroin.              Members of the

Task Force suspected that Soto-Peguero's girlfriend, Mercedes

Cabral, sometimes transported the drugs to Mejia-Ramos.

          On the afternoon of July 6, 2015, Task Force members

intercepted conversations that indicated that Soto-Peguero would

deliver drugs to Mejia-Ramos's home later that day.          Specifically,

just before 9 p.m., Mejia-Ramos called Soto-Peguero and asked him

to come at 10 p.m. and "bring something heavy."        Soto-Peguero said

in response that he would "send the woman."          Then, at 9:38 p.m.,

he called Mejia-Ramos to let him know "the woman is on her way."

          Four minutes earlier, Cabral had left the apartment that

she shared with Soto-Peguero.   Several Task Force members followed

her as she drove in the direction of Mejia-Ramos's home.              They

then enlisted two Massachusetts State Police troopers to conduct

a traffic stop.    The troopers pulled Cabral over and determined

that she was driving on a suspended license.          In the process of


to Federal Rule of Criminal Procedure 29.        For our opinion
affirming the District Court's grant of the Rule 29 motion, see
United States v. Guzman-Ortiz, ___ F.3d ___, 2020 WL 5542135 (1st
Cir. 2020) [No. 19-1349].


                                - 3 -
arresting her, they discovered close to a kilogram of heroin in

her pocketbook.

             After Cabral's arrest, Special Agent Carl Rideout, the

DEA agent in charge of the Task Force, directed one of its members

to "freeze" Cabral and Soto-Peguero's residence in order to secure

it   while   he     obtained    a   search   warrant.     Task   Force    members

surrounded the apartment.            As they tried to gain entry, someone

fired a gun from inside the apartment out the front door.                   Task

Force members then managed to enter the premises, without a

warrant, and, while there, found substantial evidence of heroin

possession and trafficking.

             The following day, Special Agent Rideout applied for a

search   warrant      for    Soto-Peguero's      apartment.      The   affidavit

supporting the search warrant stated that during a "security sweep"

of the apartment, "officers observed in plain view two large brick

shaped objects believed to be kilograms of heroin, one in each

bedroom."    Additionally, the affidavit stated, a Task Force member

"moved one of the bricks" and "observed a firearm beneath it."

The Magistrate Judge granted the warrant application.

             Task    Force     members    thereafter    executed   that    search

warrant.     In doing so, they discovered additional heroin and other

evidence of drug trafficking.

             On March 23, 2016, a grand jury in the United States

District     Court    for    the    District     of   Massachusetts    issued   a


                                         - 4 -
superseding eight-count indictment.      Soto-Peguero was not named in

Counts One or Four,2 but he was charged with six counts: possession

with intent to distribute 100 grams of heroin in violation of 21

U.S.C. §§ 841(a)(1), 841(b)(1)(B)(i) (Count Two); possession with

intent to distribute one kilogram of heroin in violation of 21

U.S.C. §§ 841(a)(1), 841(b)(1)(A)(i) (Count Three); two counts of

conspiring to distribute and possess heroin in violation of 21

U.S.C. § 846 (Counts Five and Six); illegally possessing a firearm

in violation of 18 U.S.C. § 922(g)(1) (Count Seven); and using a

firearm during and in relation to a drug offense in violation of

18 U.S.C. § 924(c) (Count Eight).

          Soto-Peguero moved pursuant to the Fourth Amendment of

the United States Constitution to suppress, among other things,

the evidence that law enforcement had found at his apartment,

including both the drugs and gun discovered without a warrant on

the night Task Force members first entered his home, and the

further evidence that law enforcement uncovered pursuant to the

warrant that was later issued.    He contended that, as to the first

batch of evidence, "[n]o exigency justified the police's forced

entry" because even if the Task Force had waited to obtain a

warrant, there would have been no "great likelihood that evidence



     2 Count One was brought against Cabral and Count Four was
brought against Guzman-Ortiz, who was arrested at the same time as
Soto-Peguero.


                                 - 5 -
would [have] be[en] destroyed."         He also asserted that even if the

initial entry had been permissible, "the officers' subsequent

decision to search under the auspices of conducting a 'protective

sweep' [was] unsustainable" because "they had no basis to suspect

another person, let alone a dangerous person, was present."                   In

addition, Soto-Peguero challenged the contention that the drugs

and gun the Task Force recovered during the warrantless entry were

in "plain view" when law enforcement arrived.

             Soto-Peguero separately argued that the search warrant

itself was "defective" because it was "based on evidence that was

illegally obtained" during the course of the warrantless entry

into the apartment.        He thus contended that the evidence the Task

Force found after obtaining that warrant had to be suppressed

pursuant to the Fourth Amendment as well.

             In   reply,    the   United      States   argued   that     exigent

circumstances were present at the time of the initial entry into

the apartment because "[i]t was not unreasonable for DEA officers

to fear that Soto-Peguero might conclude that Cabral had been

arrested when Cabral did not arrive in Taunton, did not return

home, and was unable to communicate with Soto-Peguero."                     The

government    also   argued    that   Soto-Peguero     "created   a     distinct

exigency" when he fired a shot through the front door.                 Moreover,

the government contended that the scope of the protective sweep

was necessary because "having been fired at, the officers were


                                      - 6 -
entitled to account for the presence and location of the firearm

to ensure safety" and pointed out that Task Force members had

"testified [at the grand jury] that the heroin package in the front

bedroom was in plain view."

             Finally, the government contended that, even if the Task

Force members' conduct exceeded that of an appropriate protective

sweep, the exclusionary rule should not apply.                The government

argued there was "no doubt but that agents would have sought and

obtained [a warrant] whether or not they observed the kilograms of

heroin in [the] apartment during the sweep," and therefore that

the evidence "inevitably would have been revealed in some other

lawful way."     For that proposition, the government relied on the

inevitable     discovery     doctrine,    which    provides    that   evidence

obtained in violation of the Fourth Amendment is admissible "if it

ineluctably would have been revealed in some other (lawful) way, so

long as (i) the lawful means of its discovery are independent and

would necessarily have been employed, (ii) discovery by that means

is in fact inevitable, and (iii) application of the doctrine in a

particular case will not sully the prophylaxis of the Fourth

Amendment."     United States v. Zapata, 18 F.3d 971, 978 (1st Cir.

1994) (internal citations omitted).

             Soto-Peguero     responded      in   a   separate      memorandum,

arguing,     among   other    things,     that    applying    the   inevitable

discovery    doctrine   in    this   case    would,   in   fact,    "sully   the


                                     - 7 -
prophylaxis of the Fourth Amendment."         He contended that admitting

the evidence would incentivize police misconduct because it would

"assure[] police that they need not wait for a magistrate's

approval."      He argued that this is "what happened here" because

the officers "had little concern about prematurely prying open a

heating vent and rifling through a closed nightstand" since they

were confident a warrant would later issue.

             The District Court held a hearing on Soto-Peguero's

motion to suppress and heard testimony from both Soto-Peguero and

Task Force members who were involved in the warrantless entry and

the execution of the search warrant. The focus of that evidentiary

hearing   was    on   the   Task   Force   members'   and   the   defendant's

conflicting     accounts     regarding     what   transpired      during   the

warrantless entry of Soto-Peguero's home. There were three salient

points of disagreement:        whether the heroin that law enforcement

found in the front bedroom during the initial entry into the

apartment had been in plain view or was concealed by the cover of

an air vent; whether the heroin found in a black plastic bag in

the rear bedroom that same night had been between the bed and the

nightstand or in a drawer of the nightstand; and whether Special

Agent Meletis, of the DEA, looked inside the black plastic bag

during the warrantless entry, as he testified in the suppression

hearing, or only the next day after having obtained the search

warrant, as he testified before the grand jury in March of 2016.


                                     - 8 -
Soto-Peguero also testified at the hearing that, while he was

detained on the first floor of his apartment, it sounded "[l]ike

they were breaking stuff" upstairs and that his bed frame had been

intact prior to the search.

           Soto-Peguero and the United States then both filed post-

hearing briefs.     As relevant here, in addition to renewing the

objections from his motion to suppress, Soto-Peguero elaborated on

his assertion that the District Court "should not excuse the

officers' misconduct by applying the inevitable discovery rule."

In support of that contention, he pointed to what he characterized

as "[t]he fact that at least one officer testified inconsistently

about the scope of his search -- denying and then admitting that

he looked inside a black bag" and to what he contended was the

fact that the "officers[] unreasonabl[y] delay[ed] in seeking the

search warrant" because "they anticipated entering his home that

day,"   but   "rather   than       bothering   to    apply     for   judicial

authorization, they sent more than ten officers to prepare to

'secure' the apartment without a warrant."

           In its post-hearing filing, the United States contended

that the inevitable discovery doctrine's requirements were met.

First, the government repeated its contention that "there can be

no doubt but that agents would have sought and obtained [a search

warrant] whether or not they observed the kilograms of heroin in

[the]   apartment   during   the    sweep."    The    United    States   also


                                    - 9 -
reiterated that there was "no reason to discredit the testimony of

the officers" who averred that the heroin in the front bedroom was

in plain view.       The government then further contended -- in an

argument that appeared to invoke the distinct exception to the

exclusionary rule known as the independent source doctrine, see

Murray v. United States, 487 U.S. 533, 537 (1988) -- that even "if

the discovery of the heroin and firearm [were] excised from the

affidavit in support of the search warrant, there [was] still

overwhelming      probable    cause    to   justify   the   issuance   of   the

warrant."

            The   District     Court   denied    Soto-Peguero's   motion     to

suppress.    United States v. Soto-Peguero, 252 F. Supp. 3d 1, 14

(D. Mass. 2017).       First, the District Court found that exigent

circumstances justified the initial warrantless entry.            Id. at 11-

12.   The District Court concluded that if Cabral had failed to

return in a timely manner, and if Soto-Peguero had been unable to

reach her, he might have concluded that law enforcement was

"closing in" on him.         Id.

            The District Court also found that it was reasonable for

the Task Force members to delay in obtaining the warrant, even if

they had probable cause to search the apartment before Cabral

departed with some of the drugs.            Id. at 12.   Under Supreme Court

precedent, the District Court reasoned, there are "many entirely

proper reasons why police may not want to seek a search warrant as


                                      - 10 -
soon as the bare minimum of evidence needed to establish probable

cause is acquired."         Id. (quoting Kentucky v. King, 563 U.S. 452,

466-67 (2011)).       And, the District Court further determined, the

fact that "police might have foreseen the eventual entry" was not

enough    on    its   own    to   "prevent    application   of   the   exigent

circumstances doctrine."          Id. (quoting United States v. Samboy,

433 F.3d 154, 160 (1st Cir. 2005)).

               The District Court next explained, however, that it was

"not persuaded by the officers' account that a block of heroin was

sticking out of a floor vent."           Id. at 13.     The District Court

also declined to "resolve the conflicting evidence as to whether

a bag in the back bedroom containing heroin was in a drawer or

next to the bed."      Id.    "[E]ven accepting the government's version

of events as true," the court held that "manipulating an object in

a vent and opening a bag goes beyond the scope of a protective

sweep."   Id.

               Nevertheless, the District Court denied Soto-Peguero's

motion to suppress under the inevitable discovery exception to the

exclusionary rule.      The District Court concluded that, even if the

Task Force members had not found the heroin or the gun in their

warrantless search of Soto-Peguero's home, they would have found

that evidence after obtaining a search warrant. The District Court

credited Special Agent Rideout's testimony that he would have

pursued a warrant even if no evidence had been uncovered during


                                     - 11 -
the "protective sweep."         Id.     And the District Court concluded

that the Task Force had probable cause to support a warrant for

such a search even before a single member entered the apartment.

Id.    Therefore, according to the District Court, the government

had "demonstrate[d], to a high degree of probability," that the

evidence inevitably would have been discovered.             Id. (alteration

in original) (quoting United States v. Almeida, 434 F.3d 25, 29

(1st Cir. 2006)).

               The District Court did express disapproval of the fact

that Task Force members looked inside the vent and the bag.             But,

it went on to conclude that admitting the evidence was "unlikely

to    'erode    [Fourth   Amendment]    protections   or   encourage   police

misconduct.'" Id. at 14 (alteration in original) (quoting Almeida,

434 F.3d at 29).      Thus, it determined that admitting the evidence

would not "sully the prophylaxis of the Fourth Amendment" and

therefore "the deterrence rationale [did] not justify putting the

police in a worse position than they would have been had no

misconduct occurred."       Id. at 13-14 (first quoting Zapata, 18 F.3d

at 978; then quoting United States v. Silvestri, 787 F.2d 736, 740

(1st Cir. 1986)).          The District Court therefore denied Soto-

Peguero's suppression motion.

               The case proceeded to trial, which lasted six days.         On

April 2, 2018, the jury convicted Soto-Peguero on Counts Two,




                                      - 12 -
Three, Five, and Eight of the indictment, but acquitted him on

Count Six (conspiring with Guzman-Ortiz).3

             For   the      purposes      of     calculating       Soto-Peguero's

sentencing     range     under      the    Guidelines,       the     Presentence

Investigation Report ("PSR") that the United States Office of

Probation prepared grouped the first three counts of conviction

(Counts    Two,    Three,    and   Five)       separately   from    the   firearm

conviction (Count Eight).          The PSR determined that, based on the

quantity of heroin discovered, Soto-Peguero's base offense level

should be set at 32 for the three grouped charges.                  The PSR also

applied a two-level role enhancement under § 3B1.1(c) of the

Guidelines, because Soto-Peguero "directed his significant other

at the time, Mercedes Cabral, to deliver drugs for him on at least

four separate occasions."

             Soto-Peguero objected to the role enhancement both in

his sentencing memorandum and at the sentencing hearing.                     The

United States argued that Cabral was "clearly directed by Mr. Soto-

Peguero" and that it was "very plain that Mr. Soto-Peguero was

supervising" her activities.         The District Court agreed that Soto-

Peguero was "much more the head of the enterprise" than Cabral was

and upheld the role enhancement accordingly.




     3   Count Seven was dismissed prior to trial.


                                     - 13 -
           Including the role enhancement, and accounting for the

extent of Soto-Peguero's criminal record, the mandatory 10-year

prison sentence for his firearm charge, and his history of mental

health struggles and childhood abuse, the District Court sentenced

him to a total term of incarceration of 264 months with a five-

year term of supervised release and a $400 special assessment.

     The District Court entered judgment on September 12, 2018.

On September 18, 2018, Soto-Peguero filed a timely notice of

appeal.   We have jurisdiction over his appeal from his conviction

under 28 U.S.C. § 1291.   We have jurisdiction over his appeal from

his sentence under 18 U.S.C. § 3742(a).

                                II.

           When a district court denies a motion to suppress, we

review the legal questions de novo and evaluate the factfinding

for clear error.   United States v. Ackies, 918 F.3d 190, 197 (1st

Cir. 2019).

                                 A.

           Soto-Peguero first asserts that the Fourth Amendment

requires suppression of both the evidence the Task Force found the

night of the warrantless entry and the evidence uncovered the

following day pursuant to the search warrant.     He contends that

"[t]here was no information [in the warrant application], aside

from the illegally obtained evidence, supporting a finding that

enumerated evidence of contraband or of a crime would be found" at


                               - 14 -
his home.      Failing that, he argues that, at the very least, the

"closeness" of the question of whether probable cause existed

without the illegally obtained evidence "makes it impossible to

conclude . . . that the Magistrate's decision to issue the warrant

was unaffected by the illegal evidence."

              But, Soto-Peguero's focus on the warrant application is

misplaced.     The District Court held that the evidence at issue --

both the evidence discovered during the warrantless entry and the

evidence found the following day -- is admissible under the

inevitable     discovery      doctrine.       Under     that   exception       to   the

exclusionary     rule,   "[i]f      the    prosecution       can    establish    by   a

preponderance of the evidence that the information ultimately or

inevitably would have been discovered by lawful means . . . the

evidence should be received."             Nix v. Williams, 467 U.S. 431, 444

(1984).     In this case, that means the government must establish

that,   had    there   been    no    search     in    violation     of   the    Fourth

Amendment,     the   officers       inevitably       would   have   applied     for   a

warrant, obtained it, and discovered the evidence in question when

executing that warrant.          See United States v. Procopio, 88 F.3d

21, 27 (1st Cir. 1996) (applying the inevitable discovery doctrine

to admit the illegally uncovered contents of a briefcase where

there was "little reason to doubt that the local police would have

contacted federal agents, even without the information gleaned

during the search," and where it was "even more certain that


                                       - 15 -
federal agents . . . would have then sought a warrant to search

the briefcase").     Thus, because the Task Force members need not

have   actually   obtained   a   warrant   to   rely   on   the   inevitable

discovery exception, any defects in the warrant that they did

obtain the day after their initial warrantless entry of Soto-

Peguero's apartment are not directly relevant to the question of

whether the evidence at issue must be suppressed.           See Silvestri,

787 F.2d at 744 (contemplating situations where a warrantless

search is never followed by a warrant and yet the government relies

on the inevitable discovery doctrine).

            Moreover, here, the United States has made the required

showing under the inevitable discovery doctrine.            In that regard,

Soto-Peguero does not challenge Special Agent Rideout's testimony

that he would have pursued a warrant regardless of what was found

in securing the apartment.       He also does not argue that, if the

Task Force members had delayed entry until they obtained a valid

search warrant, they would not have found the evidence in question

upon its execution.

            To the extent that we can read Soto-Peguero's claim that

the warrant application would have been insufficient without the

illegally obtained evidence as an argument that the police did not

have probable cause to search his home before they entered it, we

disagree.    Soto-Peguero and Cabral lived together at the searched

location; he spoke to Mejia-Ramos on July 6, indicating that he


                                  - 16 -
would deliver heroin that day; he told Mejia-Ramos that Cabral was

on her way around 9:38 p.m., four minutes after she had left their

apartment; and Cabral was then stopped with close to a kilogram of

heroin in her pocketbook.      We thus agree with the District Court

that "the officers had sufficient probable cause" to substantiate

a   search    warrant   for   Soto-Peguero's    apartment   before   the

protective sweep even began.     Soto-Peguero, 252 F. Supp. 3d at 13.

                                   B.

             Soto-Peguero separately argues that the District Court

erred in insulating the evidence at issue from the exclusionary

rule by adverting to our precedent that, in analyzing whether to

admit evidence through the inevitable discovery doctrine, we must

also consider whether doing so would "encourage police misconduct"

and thereby "sully the prophylaxis of the Fourth Amendment."

United States v. Hughes, 640 F.3d 428, 440-41 (1st Cir. 2011)

(quoting Zapata, 18 F.3d at 978).       In undertaking that inquiry, we

need to "dwell[] closely on the facts" and look toward whether the

record establishes that law enforcement officers intentionally

violated the Fourth Amendment as well as the incentives, if any,

for them to act unconstitutionally.        United States v. Scott, 270

F.3d 30, 45 (1st Cir. 2001); see also Hughes, 640 F.3d at 441.

But, rather than develop an argument along those precise lines,

Soto-Peguero instead directs our attention to an out-of-circuit

case, United States v. Madrid, 152 F.3d 1034 (8th Cir. 1998).


                                 - 17 -
There, the Eighth Circuit recognized an exception to the inevitable

discovery    doctrine    because      police     behaved     egregiously          and

"exploited their presence" in the defendant's home.                 Id. at 1040.

Either way, Soto-Peguero's attempt to make the case that the

conduct by law enforcement here precludes us from affirming the

District Court's inevitable discovery ruling fails.

            Invoking    Madrid,   Soto-Peguero       cites   to     a    number    of

instances   of   purported    misconduct      that   he    argues       necessitate

suppression even if the inevitable discovery exception otherwise

would apply.     Specifically, he alleges that the Task Force members

"tore the residence apart," "destroy[ed] furniture," "open[ed]

drawers," "open[ed] containers," "pr[ied] the lid off [an] air

conditioning vent," and "used this illegally obtained evidence to

secure the warrant" during their first entry to his apartment.                    He

also contends that admitting this evidence would "make[] the court

complicit in the officers' false testimony at the suppression

hearing."

            Soto-Peguero     makes    the     allegation     that       Task   Force

members "tore the residence apart" and "destroy[ed] furniture" in

support of his Madrid-based argument for the first time on appeal.

Thus, our review of it is at most for plain error.                      See United

States v. Lara, 970 F.3d 68, 76 (1st Cir. 2020).              We find none, as

the District Court was not asked to make a finding about what, if

any, damage the Task Force members caused in going through the


                                     - 18 -
apartment during their initial entry and the District Court did

not do so on its own.           See United States v. Takesian, 945 F.3d

553, 563 (1st Cir. 2019) (explaining that "if an error pressed by

the appellant turns on 'a factual finding [he] neglected to ask

the district court to make, the error cannot be clear or obvious

unless' he shows that 'the desired factual finding is the only one

rationally supported by the record below'" (quoting United States

v. Olivier-Diaz, 13 F.3d 1, 5 (1st Cir. 1993))).

           We turn, then, to the aspects of Soto-Peguero's Madrid-

based   argument    that   rely       on   the   remaining    allegations       of

misconduct.      In part, Soto-Peguero relies on the assertion that

the record evidence indicates that Task Force members opened the

drawer of the nightstand and looked inside the floor vent when

they went through the apartment without a warrant.                   But, even

accepting that the evidence supports that understanding of their

conduct, it still "falls short of the blatant search through

personal effects in Madrid," just as we concluded the last time

that a criminal defendant asked us to follow the Eighth Circuit's

lead.   United States v. Dent, 867 F.3d 37, 41 (1st Cir. 2017); see

id.   (holding    that   when    an   officer    exceeded    the   scope   of   a

protective sweep by looking under an air mattress, that did not

bring the case within Madrid's purview).

           So, that leaves only Soto-Peguero's contentions that the

inclusion of a description of the evidence turned up during the


                                      - 19 -
warrantless entry in the warrant affidavit and "the officers' false

testimony" at the suppression hearing satisfy the Madrid standard,

at least when considered in the context of how the officers

conducted themselves at that time.      We assume, for the sake of

argument only, that the Eighth Circuit's holding that the officers

in Madrid "exploited their presence" in the defendant's home

extends to encompass this flavor of alleged misconduct.        Even

still, here, too, we are not persuaded.

            The affidavit attached to the search warrant application

did describe evidence that Task Force members uncovered pursuant

to what that affidavit characterized as a "security sweep."    And,

as Soto-Peguero notes, the District Court later found that some of

that evidence was obtained through methods that exceeded the scope

of such a sweep.   But, we do not see how this mismatch suffices to

support Soto-Peguero's Madrid-based suppression argument.       The

Task Force members had been shot at as they tried to enter the

residence and would later testify that they found the evidence

while trying to secure the apartment and locate the firearm in

question.    In such circumstances, we cannot say that the warrant

application's erroneous description of the means by which that

evidence had been acquired constitutes the kind of egregious

conduct that, per Madrid, could justify suppression.     Cf. United

States v. Paradis, 351 F.3d 21, 29 n.7 (1st Cir. 2003) (describing

scenarios in which a protective sweep might properly authorize an


                               - 20 -
officer to specifically search for weapons).    Consistent with this

conclusion, we note that the District Court made no finding here

that any law enforcement officer involved in the preparation of

the      warrant   application       either    knowingly    included

unconstitutionally obtained evidence or knowingly misdescribed

that evidence as having been lawfully obtained.

           With respect to Soto-Peguero's contention that Madrid

requires suppression here based on his allegation that Task Force

members gave false testimony at the suppression hearing, we are

likewise unpersuaded.   The District Court did explain that it was

not fully persuaded by the Task Force members' testimony at the

suppression hearing regarding what happened during the warrantless

entry.   But, the District Court also concluded that there was no

basis for finding on this record the kind of egregious or flagrant

official misconduct that would require suppression in order to not

sully the prophylaxis of the Fourth Amendment.     Soto-Peguero, 252

F. Supp. 3d at 13-14.   In the face of that ruling and the absence

of any finding by the District Court that the Task Force members

who testified at that hearing did so in bad faith, we see no basis

for requiring suppression even were we to accept Soto-Peguero's

argument that we should adopt the Madrid standard.

           Because Soto-Peguero has not succeeded in establishing

that the United States failed to meet the requirements for applying




                                 - 21 -
the inevitable discovery doctrine, we affirm the District Court's

denial of his motion to suppress.

                                           III.

            Soto-Peguero also challenges the fact that the Probation

Office   applied     a    two-level    role       enhancement     to       increase   the

Guidelines range for his drug possession-related crimes from 168-

210 months to 210-262 months.

            Under    § 3B1.1(c)       of     the       Guidelines,     a    defendant's

offense level is increased by two levels if "the defendant was an

organizer,      leader,     manager,       or     supervisor     in    any     criminal

activity"    involving      four      or    fewer       participants.          For    the

enhancement to apply, the government bears the burden of proving,

by a preponderance of the evidence, that "the criminal enterprise

involved at least two complicit participants (of whom the defendant

may be counted as one)" and that "the defendant, in committing the

offense,    exercised      control    over,       organized,     or    was    otherwise

responsible for superintending the activities of, at least one of

those other persons."         United States v. Cruz, 120 F.3d 1, 3 (1st

Cir.   1997).       "The   determination          of    an   individual's      role    in

committing an offense is necessarily fact-specific.                        Accordingly,

appellate review must be conducted with considerable deference."

Id. (internal citation omitted).                   Even a single instance of

managing the actions of others can substantiate the enhancement.

See United States v. Voccola, 99 F.3d 37, 44 (1st Cir. 1996).


                                       - 22 -
            Soto-Peguero         argues        that     the        entirety   of    the

government's case for the enhancement is that, on two occasions,

he stated that he was "sending" Cabral.                     He asserts that, beyond

that, there is nothing in the record to support the conclusion

that he and Cabral "were anything other than equal participants in

criminal activity."

            The    United      States    points       out   that    Soto-Peguero    had

"scores of communications" with Mejia-Ramos, while Cabral only

interacted with him to ask to which house she should go.                       On one

occasion, Mejia-Ramos contacted Soto-Peguero and told him the

heroin was poor quality.             Soto-Peguero replied:            "My woman is on

the way."       Later, Cabral retrieved what were presumably the

inferior drugs from Mejia-Ramos's cousin.                     On another occasion,

after Cabral dropped off a package, Mejia-Ramos called Soto-

Peguero    to     ask   what    he      had    sent.         Per    the   government's

characterization, "both Mejia-Ramos and his cousin treated Cabral

as   a   mere   delivery    person       and    engaged      only    Soto-Peguero    in

important business decisions."

            At sentencing, the District Court -- after presiding

over a six-day trial and observing both Soto-Peguero and Cabral

-- concluded that "Soto-Peguero was running the show."                        He "told

[Cabral] to go to Brockton or wherever it was on a number of

occasions."     That was where she "ultimately got caught."




                                         - 23 -
          Based on all the evidence cited by the United States,

and accounting for the fact that the District Court had the

opportunity to observe the witnesses and the defendant firsthand,

we cannot conclude that the District Court clearly erred in holding

that the government had shown by a preponderance of the evidence

that Soto-Peguero was managing or supervising Cabral on at least

one occasion.   We therefore affirm the District Court's decision.

                                     IV.

          As    described   above,    we   affirm   both   Soto-Peguero's

convictions and his sentence.




                                - 24 -

```

---
