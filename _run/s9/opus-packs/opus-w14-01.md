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

## GROUP: _overhaul2/lake/cases/United States v. August.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. August"
type: case
citation: "136 F.4th 595 (2025)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 5th Circuit"
court_level: coa
circuit: 5th
year: 2025
date_decided: 2025-05-08
docket: 24-30457
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2025-05-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. August
  varies_by_point: false
  scope_note: "Recent published 5th Circuit decision; good law in-circuit."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10574922/united-states-v-august/"
  cluster_id: 10574922
  opinion_id: 11041510
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Recent development (role-based)"
related: ["[[Maryland v. Buie]]", "[[United States v. Conner]]"]
aliases: []
tags: ["case", "fourth-amendment", "protective-sweep", "securing-the-scene"]
holding: "(Binding in-circuit — 5th Cir.; Persuasive (outside circuit)) Articulates a four-part protective-sweep test and extends *Buie*'s officer-safety rationale to curtilage and to a non-arrest, investigatory entry."
lake:
  record_id: United States v. August
  status: verified
  projected_at: 2026-07-06
---

# United States v. August

*136 F.4th 595 (5th Cir. 2025)* · U.S. Court of Appeals, 5th Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A neighbor told officers she had just seen August — a felon — firing a handgun in his fenced backyard, that he did so frequently, and that stray bullets had struck her home. Officers ordered August to the fence, patted him down (no weapon), and entered the backyard to conduct a [[Securing the Scene|protective sweep]], finding spent shell casings. Unable to locate the firearm and doubting August's claim that the house was empty, they swept the home (finding a magazine) and searched his car (finding methamphetamine in plain view), then obtained and executed a search warrant.

## Issue
Whether the protective-sweep doctrine justified the warrantless sweeps of August's [[Curtilage|curtilage]] (backyard) and home during a non-arrest, investigatory encounter.

## Rule
The court applied the circuit's four-part protective-sweep test, extending it by its terms to [[Curtilage|curtilage]]: "A protective sweep is lawful if: (1) the government agents have a legitimate law enforcement purpose for being in the house [or curtilage]; (2) the sweep is supported by a reasonable, articulable suspicion that the area to be swept harbors an individual posing a danger to those on the scene; (3) the sweep is no more than a cursory inspection of those spaces where a person may be found; and (4) the sweep lasts no longer than is necessary to dispel the reasonable suspicion of danger and lasts no longer than the police are justified in remaining on the premises." — slip op., at 5 (quoting *United States v. Mendez*, 431 F.3d 420, 428 (5th Cir. 2005)). ^pin-op5

## Application
On these facts the officers had a legitimate law-enforcement purpose in the backyard and home (investigating reported illegal gunfire by a felon while awaiting a warrant), and a reasonable, articulable suspicion of danger: a reported, recently fired but unlocated firearm, a cluttered yard offering hiding spots, and August's shifting, untrustworthy statements made it reasonable to fear another person or accessible weapon. The sweeps were brief and cursory inspections of spaces where a person could hide. Because each element was satisfied — including in the [[Curtilage|curtilage]] — the warrantless protective sweeps were reasonable, and the shell casings and other evidence were not suppressed.

## Conclusion
The protective sweeps of August's backyard and home were lawful and the evidence was admissible; the district court's denial of suppression was affirmed. In the Fifth Circuit, the protective-sweep doctrine's four-part test extends to [[Curtilage|curtilage]] and to non-arrest, investigatory entries supported by articulable suspicion of danger.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 5th Cir.**
- *August* extends the officer-safety protective-sweep rationale of [[Maryland v. Buie]] beyond the arrest context to [[Curtilage|curtilage]] and investigatory entries, applying the circuit's *Mendez* four-part test.

## Appears on
- [[Securing the Scene]] — *Recent development (role-based)*

## Sources
- *United States v. August*, 136 F.4th 595 (5th Cir. 2025) — https://www.courtlistener.com/opinion/10574922/united-states-v-august/ — pinpoint: slip op., at 5 (CL carries the slip opinion; cluster 10574922 → opinion 11041510).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "92aabf18771c7b8d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. August"}, "payload": {"all": [{"cite": "136 F.4th 595", "page": "595", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "136"}], "display": "136 F.4th 595", "official": {"cite": "136 F.4th 595", "page": "595", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "136"}, "official_selection_present": true, "record_id": "United States v. August"}}
{"assertion_id": "918704732f03eacf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op5", "record_id": "United States v. August"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op5", "pinpoint_status": "slip-only", "quote": "--- # United States v. August *136 F.4th 595 (5th Cir. 2025)* · U.S. Court of Appeals, 5th Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A neighbor told officers she had just seen August — a felon — firing a handgun in his fenced backyard, that he did so frequently, and that stray bullets had struck her home. Officers ordered August to the fence, patted him down (no weapon), and entered the backyard to conduct a protective sweep, finding spent shell casings. Unable to locate the firearm and doubting August's claim that the house was empty, they swept the home (finding a magazine) and searched his car (finding methamphetamine in plain view), then obtained and executed a search warrant. ## Issue Whether the protective-sweep doctrine justified the warrantless sweeps of August's curtilage (backyard) and home during a non-arrest, investigatory encounter. ## Rule The court applied the circuit's four-part protective-sweep test, extending it by its terms to curtilage:", "quote_fidelity": "mismatch", "record_id": "United States v. August", "star_marker": null}}
{"assertion_id": "bfbae02e5183bfe8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. August"}, "payload": {"as_of_content": "2025-05-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. August", "scope_note": "Recent published 5th Circuit decision; good law in-circuit.", "varies_by_point": false}}
```

### lake record — United States v. August

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. August",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. August",
    "case_name_short": "August",
    "case_name_full": "",
    "input_case_name": "United States v. August",
    "court": "U.S. Court of Appeals, 5th Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "2025-05-08",
    "year": 2025,
    "docket": "24-30457",
    "cluster_id": 10574922,
    "lead_opinion_id": 11041510,
    "sibling_ids": [
      11041510
    ],
    "absolute_url": "/opinion/10574922/united-states-v-august/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "136 F.4th 595",
      "volume": "136",
      "reporter": "F.4th",
      "page": "595",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "136 F.4th 595",
        "volume": "136",
        "reporter": "F.4th",
        "page": "595",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "136 F.4th 595",
    "official_selection": {
      "court_class": "coa",
      "selected": "136 F.4th 595",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op5",
      "page": null,
      "quote": "--- # United States v. August *136 F.4th 595 (5th Cir. 2025)* \u00b7 U.S. Court of Appeals, 5th Circuit \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A neighbor told officers she had just seen August \u2014 a felon \u2014 firing a handgun in his fenced backyard, that he did so frequently, and that stray bullets had struck her home. Officers ordered August to the fence, patted him down (no weapon), and entered the backyard to conduct a protective sweep, finding spent shell casings. Unable to locate the firearm and doubting August's claim that the house was empty, they swept the home (finding a magazine) and searched his car (finding methamphetamine in plain view), then obtained and executed a search warrant. ## Issue Whether the protective-sweep doctrine justified the warrantless sweeps of August's curtilage (backyard) and home during a non-arrest, investigatory encounter. ## Rule The court applied the circuit's four-part protective-sweep test, extending it by its terms to curtilage:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-05-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. August",
    "varies_by_point": false,
    "scope_note": "Recent published 5th Circuit decision; good law in-circuit.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11041510) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      },
      "lane2_top_cited": {
        "query": "cites:(11041510)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11041510)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(11041510)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11041510,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-august.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11041510,
        "cited_id": 9280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 39963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 49000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 65023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 69228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 71470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 178767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 527826,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 596417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 775796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 785402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 4159168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 4177578,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9414811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9431434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9431933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9436658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9802250,
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
    "date_created": "2026-07-05T22:24:27Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:25:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. August

```
Case: 24-30457       Document: 68-1      Page: 1     Date Filed: 05/08/2025




        United States Court of Appeals
             for the Fifth Circuit                                  United States Court of Appeals
                                                                             Fifth Circuit
                             ____________                                  FILED
                                                                        May 8, 2025
                              No. 24-30457
                                                                      Lyle W. Cayce
                             ____________
                                                                           Clerk
United States of America,

                                                          Plaintiff—Appellee,

                                    versus

Kirk August,

                                        Defendant—Appellant.
               ______________________________

               Appeal from the United States District Court
                  for the Western District of Louisiana
                         USDC No. 2:23-CR-23-1
               ______________________________

Before King, Jones, and Oldham, Circuit Judges.
Edith H. Jones, Circuit Judge:
       Kirk August pled guilty to one count of possession of a firearm by a
convicted felon in violation of 18 U.S.C. § 922(g)(1). He reserved the right
to argue in this appeal that the district court should have granted his motion
to suppress evidence. Finding no error, we AFFIRM.
                       I. Factual Background
       On May 14, 2022, the Lake Charles Police Department received a call
about gunshots on the 700 block of N. Lyons Street, a residential street in
Lake Charles, Louisiana.     Officers Baccigalopi, Bernat, and Rainwater
 Case: 24-30457          Document: 68-1          Page: 2      Date Filed: 05/08/2025




                                       No. 24-30457


responded. Baccigalopi arrived on scene and spoke with the caller, who
pointed him to the blue home where August resided.
        Baccigalopi, Bernat, and Rainwater descended on the home at
virtually the same time. Baccigalopi and Bernat approached August’s home
through the next-door neighbor’s property, and they encountered August
standing in his backyard behind a chain-link fence. The backyard was
cluttered with junk, which officers believed gave August ample cover to hide
a weapon. A top-down convertible was parked in his driveway with the
driver-side door left ajar and music playing from the radio. Mattresses were
stacked against the main door to the home, preventing it from being used as
an entrance.
        Baccigalopi spoke with August while still standing on the neighbor’s
side of the fence. He asked August whether he had heard gunshots or had
any “weapons or anything” on the property. August responded “no” to
both of Baccigalopi’s questions. Meanwhile, Rainwater had gotten held up
in a conversation with the next-door neighbor, who explained to Rainwater
that she had “just now” seen August firing a handgun in his backyard.1 The
neighbor also stated that August discharged firearms in his backyard
frequently, and that stray bullets had previously struck her home. Rainwater
promptly informed his colleagues that August might have a firearm.2



        _____________________
        1
          Rainwater had assisted in executing a search warrant at August’s home a year
earlier when police located a .22 revolver in the home.
        2
          This information was enough to give the officers reasonable suspicion that a crime
had been committed. La. Rev. Stat. 14:94 prohibits the discharge of a firearm in a
residential neighborhood. See United States v. LeJeune, 2021 WL 3926154, at *2
(W.D. La. 2021). And the officers were all aware soon after arriving at the scene that
August was a felon barred from possessing a firearm.




                                             2
Case: 24-30457        Document: 68-1       Page: 3   Date Filed: 05/08/2025




                                 No. 24-30457


       Baccigalopi—still on the neighbor’s side of the fence—then ordered
August to walk backward with his hands on his head toward the fence.
August was patted down, and no weapon was found on his person. He
remained near the fence this entire time. Rainwater and Bernat entered the
backyard and began conducting a protective sweep. Bernat testified that they
entered the backyard “mostly” for safety reasons: “There was a lot of junk
behind the house . . . So if he did have a firearm within close proximity, I’d
rather be on that side.” During the protective sweep, Bernat discovered shell
casings on the ground and a large sign riddled with bullet holes. He returned
to where August was standing and handcuffed him. August continued to
contend that there was no gun on the property.
       The government maintains that officers next decided to seek a warrant
authorizing them to search the property. The officers knew they would have
to remain at the scene while they waited for the warrant application’s
approval. Given that none of them had been able to locate the alleged
firearm—and having little reason to trust August’s claim that the house was
empty—police decided to conduct a protective sweep of the home. But the
only accessible door was locked. August told police that his sister had the
only set of keys, which contradicted his previous statement that he had been
taking a bath before police arrived.
       Baccigalopi walked over to the vehicle parked in the driveway and
removed August’s keys from the ignition. While doing so, Baccigalopi
noticed a baggie of methamphetamine in plain view near the center console.
August was secured in the back of Baccigalopi’s police vehicle. Officers then
used the keys that were retrieved from the car to enter a side door of the
house and conduct a protective sweep. The sweep lasted approximately
three minutes, during which the officers located a magazine clip for a firearm.
Baccigalopi and Bernat returned to the convertible. Bernat found a gray




                                       3
Case: 24-30457        Document: 68-1        Page: 4    Date Filed: 05/08/2025




                                  No. 24-30457


plastic bag containing ammunition inside the side pocket of the open driver’s
door. Bernat stated that the ammunition itself was not in plain view.
       Satisfied that they were not in imminent danger by remaining on the
scene, police formally requested a search warrant for August’s entire
property. They remained on the scene until after they received and executed
the warrant. Their search of August’s property ultimately yielded a .22
caliber rifle, .410 shotgun, and ammunition.
                    II. Procedural Background
       August was charged with violating 18 U.S.C. § 922(g)(1) for
knowingly possessing a firearm in and affecting commerce while knowing he
had been convicted of a crime punishable by imprisonment for a term
exceeding one year. The district court denied a motion by August to dismiss
the indictment. August moved to suppress nearly all of the relevant evidence:
(1) shell casings found in the backyard; (2) the magazine clip found in the
home; (3) ammunition found in the car; and (4) firearms found in the home.
A magistrate judge issued a report and recommendation that suggested the
district court should deny the motion to suppress, reasoning that protective
sweeps of the backyard and home were justified by exigent circumstances,
and that any constitutional defect pertaining to the car search was excused
under the independent source doctrine. The district court adopted the
report and recommendation in full. August pled guilty but reserved the right
to argue that the district court should have granted his motion to suppress.
The district court sentenced August to 63 months in prison and three years
of supervised release.
                         III. Standard of Review
       When considering a district court’s denial of a motion to suppress,
this court reviews the district court’s factual findings for clear error and legal
conclusions de novo. United States v. Pack, 612 F.3d 341, 347 (5th Cir. 2010).




                                        4
Case: 24-30457       Document: 68-1       Page: 5    Date Filed: 05/08/2025




                                 No. 24-30457


A few words on the Fourth Amendment doctrines that the district court
relied on, and then on how the standard of review applies to those doctrines.
                       A. Protective Sweep Doctrine
       Under the protective sweep doctrine, police may conduct, without a
warrant, “a quick and limited search of premises for the safety of the agents
and others present at the scene.” United States v. Mendez, 431 F.3d 420, 428
(5th Cir. 2005) (citation omitted). A protective sweep is lawful if:
       (1) the government agents have a legitimate law enforcement
       purpose for being in the house [or curtilage]; (2) the sweep is
       supported by a reasonable, articulable suspicion that the area
       to be swept harbors an individual posing a danger to those on
       the scene; (3) the sweep is no more than a cursory inspection
       of those spaces where a person may be found; and (4) the sweep
       lasts no longer than is necessary to dispel the reasonable
       suspicion of danger and lasts no longer than the police are
       justified in remaining on the premises.
Id. (internal quotation marks and citation omitted). See also United States v.
Mendoza–Burciaga, 981 F.2d 192, 196 (5th Cir. 1992) (explaining that exigent
circumstances provide officers a legitimate law enforcement purpose to
conduct a warrantless entry when “officers reasonably fear for their safety,
where firearms are present, or where there is risk of a criminal suspect's
escaping or fear of destruction of evidence”) (citations omitted).
       In evaluating the legality of a protective sweep conducted because of
exigent circumstances, courts consider how “the scene of the search . . .
would appear to reasonable and prudent men standing in the shoes of the
officers.” United States v. Menchaca-Castruita, 587 F.3d 283, 290 (5th Cir.
2009) (internal quotation marks and citation omitted). Where “reasonable
minds could differ on [] whether the sweep was warranted,” courts “do not




                                      5
Case: 24-30457       Document: 68-1        Page: 6    Date Filed: 05/08/2025




                                 No. 24-30457


second-guess the judgment of experienced law enforcement officers
concerning the risks in a particular situation.” United States v. Silva, 865
F.3d 238, 242 (5th Cir. 2017) (citation omitted).
       In the context of appellate review, protective sweep cases present
mixed questions of law and fact, with the ultimate issue of whether there was
reasonable suspicion of danger being subject to de novo review. United States
v. Scroggins, 599 F.3d 433, 441 (5th Cir. 2010). This court, however, “view[s]
the evidence [going toward reasonable suspicion] in the light most favorable
to the party prevailing below, which in this case is the Government,” and
gives “due weight to inferences drawn from those facts by . . . local law
enforcement officers.”      United States v. Henry, 853 F.3d 754, 756
(5th Cir. 2017) (internal quotation marks and citations omitted).
                     B. Independent Source Doctrine
       Under the independent source doctrine, “‘information which is
received through an illegal source is considered to be cleanly obtained when
it arrives through an independent source.’” United States v. Hearn, 563 F.3d
95, 102 (5th Cir. 2009) (quoting Murray v. United States, 484 U.S. 533, 538–
39, 108 S. Ct. 2529, 2534 (1988)). This court conducts a two-step analysis to
determine whether the independent source doctrine cures an issue when
police subsequently obtain a warrant, asking whether (1) “the warrant
affidavit, when purged of tainted information gained through the initial
illegal entry, contain[ed] sufficient remaining facts to constitute probable
cause”; and (2) “the illegal search affect[ed] or motivate[d] the officers’
decision to procure the search warrant.” Id. (citation omitted).
       In the context of appellate review, this court reviews de novo a district
court’s determination that a search warrant affidavit establishes probable
cause after the warrant has been purged of potentially “tainted” information,
and it reviews for clear error a district court’s findings regarding whether an




                                       6
Case: 24-30457         Document: 68-1       Page: 7   Date Filed: 05/08/2025




                                No. 24-30457


unlawful prior search or entry motivated officers’ decision to obtain a
warrant. See United States v. Hassan, 83 F.3d 693, 697 (5th Cir. 1996)
(citations omitted).
                              IV. Analysis
       August contends that law enforcement erred at every step of their
operation: (1) the protective sweep of his backyard; (2) the protective sweep
of his home; (3) searches of his car; and therefore (4) the execution of a
search warrant in his home. His claims pertaining to each of these searches
are considered in turn.
                   A. Protective Sweep of the Backyard
       August argues that the protective sweep doctrine did not justify the
search of his backyard because police hopped the gate and did not stay nearby
to prevent him from grabbing a weapon but continued to search beyond his
immediate vicinity. August does not cite an apposite case to support his
argument that the protective sweep of his backyard was unlawful. His
argument fails.
       August was not arrested until after law enforcement officers had
located shell casings and concluded their protective sweep of his yard. He
acknowledged in his objection to the report and recommendation that his
lawn was “surrounded by hurricane fencing and filled with spillover objects
from the home’s interior.” Without a protective sweep of the entire
backyard, it remained possible that someone else might be present, or that
August’s questioning might end without an arrest, at which point he could
have accessed a firearm hidden in the yard.
       Police had reasons to distrust August’s insistence that there was no
firearm on the property: their knowledge of his felon status, and his direct
contradictions during their limited encounter. And the presence of a gray




                                        7
Case: 24-30457        Document: 68-1       Page: 8     Date Filed: 05/08/2025




                                  No. 24-30457


convertible in the driveway—top down, driver door left ajar, keys still in the
ignition, and music playing from the radio—was potentially suggestive of a
recent visitor’s arrival or a third party’s presence, especially because August
claimed he had just been taking a bath before officers arrived. The chaos,
contradictions, and incredible story that August attempted to sell the
officers, when considered together and in the light most favorable to the
government, made it completely reasonable for police to fear that someone—
or something—else hiding in August’s backyard posed a serious threat to
their safety.
       August has failed to show that the protective sweep of his backyard
was unlawful. The district court did not err in its refusal to suppress the spent
shell casings.
                     B. Protective Sweep of the Home
       August argues that the protective sweep doctrine did not justify a
search of his home because “officers had been safely outside the home for
almost seven minutes” when they decided to enter, “officers had already
isolated August,” and “there was nothing to suggest that destruction of
evidence was likely or that anyone even remained in the home.” His
argument relies primarily on United States v. Manchaca-Castruita, 587 F.3d
283 (5th Cir. 2009), where this court held that exigent circumstances could
not justify police sweeping a home suspected of storing illegal marijuana
because there was no evidence that any person remained inside the home,
officers stood safely outside with bystanders even further removed from the
home, and a search warrant could readily have been obtained. Id. at 294–95.
       This case is different. Unlike Manchaca-Castruita, (1) the suspected
contraband—firearms—could be used to jeopardize the safety of law
enforcement; (2) the suspect had not left the home, denied any personal
knowledge of a firearm, and contradicted himself to police, and a car




                                       8
Case: 24-30457        Document: 68-1       Page: 9     Date Filed: 05/08/2025




                                  No. 24-30457


appeared to have recently arrived, which introduced the possibility that
another person on the property possessed a firearm; (3) there were no
witnesses who had been inside of August’s home to confirm whether
accomplices were inside; (4) the door to August’s home was closed,
suggesting there was no last-minute escape; (5) nobody at the property
received a warning that law enforcement was being contacted, likely
frustrating plans for a last-minute escape; (6) the spent shell casings in the
backyard confirmed that a firearm had probably been discharged at some
point on the property; and (7) the incident occurred on the weekend,
potentially making it more difficult for officers to communicate with a
magistrate and to obtain a search warrant. See id. at 285–88, 294.
       Case law tends to reflect that exigent circumstances are unlikely to
exist if there is “no articulable reason to believe that someone else might be
inside [the] residence.” Id. at 295. See also United States v. Carter, 360 F.3d
1235, 1241 (10th Cir. 2004) (granting motion to suppress) (“[T]he
government points to no reason to believe that other people were in the
garage, or even the house.”) (emphasis added). The outcome is typically
different, though, if law enforcement had at least a reasonable belief that
another dangerous person might be hiding in the residence that they decided
to sweep. See United States v. Watson, 273 F.3d 599, 603 (5th Cir. 2001) (“A
protective sweep of a suspect’s house may be made . . . if the arresting officers
‘have reasonable grounds to believe that there are other persons present
inside who might present a security risk.’”) (quoting United States v. Merritt,
882 F.2d 916, 921 (5th Cir. 1989) (internal citation omitted)); United States
v. Maldonado, 472 F.3d 388, 394 (5th Cir. 2006) (determining that a
protective sweep was justified based in part on the fact that agents were
exposed in an open area surrounding a trailer with “no certain knowledge”
whether others might be in the trailer) (subsequent history omitted).




                                       9
Case: 24-30457        Document: 68-1         Page: 10    Date Filed: 05/08/2025




                                   No. 24-30457


       It cannot be said that police had no articulable reason to fear that
someone remained in August’s home. After sweeping his backyard, the
officers knew that (1) at least two neighbors heard gunshots, and the next-
door neighbor reported seeing someone on the property firing a weapon;
(2) spent shell casings littered the backyard; (3) August had little to no
credibility; (4) a car that looked as if it had just arrived was parked in the
driveway; and (5) most entry points to the house were barricaded. See, e.g.,
United States v. Cousins, 841 F. App’x 885, 899 (7th Cir. 2021) (noting that
an occupant’s “nervous” and “evasive” demeanor when questioned by
officers supported a protective sweep of a home, especially when police are
already aware of a firearm’s presence on the property).             It makes no
difference that officers chose to investigate these concerns only after
arresting August. See Maryland v. Buie, 494 U.S. 325, 333 (1990) (“[T]here
is an analogous interest . . . in [officers] taking steps to assure themselves that
the house in which a suspect . . . has just been[] arrested is not harboring other
persons who are dangerous and who could unexpectedly launch an attack.”).
Any remaining doubt as to the reasonableness of the officers’ concerns is
dispelled by the deferential review that police are entitled to in this context.
See Silva, 865 F.3d at 242 (protective sweep standard) (where “reasonable
minds could differ on . . . whether the sweep was warranted,” a court will not
“second-guess the judgment of experienced law enforcement officers”);
Henry, 853 F.3d at 756 (appellate review standard) (this court views the
evidence going toward reasonable suspicion “in the light most favorable to
the party prevailing below,” and gives “due weight to inferences drawn from
those facts by . . . local law enforcement officers”).




                                        10
Case: 24-30457         Document: 68-1         Page: 11    Date Filed: 05/08/2025




                                    No. 24-30457


         August has failed to show that the protective sweep of his home was
unlawful. The district court did not err in its refusal to suppress the magazine
clip.3
                             C. Searches of the Car
         August argues that law enforcement twice violated the Fourth
Amendment in connection with their searches of the car parked in his
driveway. Officer Baccigalopi walked over to the car and retrieved the keys
from the ignition after August claimed that his sister had the only key to the
house. He noticed a baggie of illicit drugs when he reached for the keys.
Police returned after sweeping the backyard and the home. They conducted
a more thorough search of the car, recovering methamphetamine and
ammunition.      The magistrate judge held that the independent source
doctrine excused any constitutional defect in these searches of the car
without analyzing whether the searches were in fact constitutional. We
similarly limit our discussion to applicability of the independent source
doctrine due to insufficient briefing as to whether (1) the protective sweep
doctrine could justify the police entering the car, (2) the driver’s side door’s
being left open removed any expectation of privacy, or (3) either the
protective sweep doctrine or plain view doctrine authorized law enforcement
to acquire the keys.
         August argues that the independent source doctrine cannot cure
defects in the car searches because (1) there would be no probable cause
supporting the warrant without the magazine clip (which was obtained using
the house keys that were retrieved during the first car search) and
ammunition (which was recovered during the second car search), and (2) the

         _____________________
         3
          The magazine clip was alternatively admissible under the independent source
doctrine as discussed below.




                                         11
Case: 24-30457           Document: 68-1           Page: 12      Date Filed: 05/08/2025




                                       No. 24-30457


magazine clip and ammunition compelled the officers to pursue a search
warrant.4 His argument proves unpersuasive.
        First, aside from mentioning the magazine clip and ammunition, the
search warrant affidavit noted that law enforcement officers responded to a
report of multiple shots fired in the area; another witness advised police
officers that she observed the resident of 710 N. Lyons outside with a firearm;
officers observed multiple spent shell casings on the property of the
residence; officers located Kirk August at the residence; and officers
confirmed that August stays at the residence.
        “Probable cause does not require proof beyond a reasonable doubt.”
United States v. Perez, 484 F.3d 735, 740 (5th Cir. 2007). “[A] magistrate
need only have a substantial basis for concluding that a search would uncover
evidence of wrongdoing.” Id. Scrubbed of the allegedly tainted magazine
clip and ammunition, and considering the issue de novo, the warrant affidavit
still contained sufficient remaining facts to provide the magistrate a
substantial basis for concluding that a search would uncover evidence of
wrongdoing.        The magistrate could reasonably infer from eyewitness
testimony and shell casings on the property that August had discharged a
firearm in violation of Louisiana law.5

        _____________________
        4
          August also argues that the search warrant would not have been granted without
police locating the shell casings in his backyard. However, police clearly did not violate the
Constitution in conducting the protective sweep that produced the shell casings.
        5
          Cf. United States v. Coleman, 540 F. Supp. 3d 596, 611 (S.D. Miss. 2021) (holding
that search warrant was not supported by probable cause) (“The affidavit includes the
informant’s statement that Coleman discharged a firearm on the property against an
intruder ‘several weeks ago.’ But the affiant does not state how the informant obtained this
information, whether by personal observations or from an eyewitness.”); United States v.
Wooldridge, 2016 WL 11473559, at *6 (E.D. Tex. Apr. 22, 2016) (same) (“Here, the search
warrant affidavit describes in detail the particular place to be searched and is appropriately
limited in scope[.] However, the affidavit fails to provide the state judge with facts from




                                             12
Case: 24-30457         Document: 68-1          Page: 13     Date Filed: 05/08/2025




                                    No. 24-30457


       Second, August contends “it was not until after the officers searched
the home and car, finding a magazine and ammunition, that the officers
requested a search warrant.” But the district court’s determination that the
“tainted” magazine clip and ammunition evidence did not influence the
officers is a finding of fact that must stand unless clearly erroneous. And
there is ample evidence in the record to support it. For example, officers
arrested August immediately after they located spent shell casings in the
backyard. At that point, probable cause existed to obtain a proper search
warrant. Police retrieved house keys to access the home and reported that
they swept the home to secure the area while they waited for a search
warrant. This narrative accords with the warrant affidavit, which noted that
officers “cleared the residence . . . for safety and to check for any injured
parties.”     August has not identified any substantial evidence that
undermines this narrative.         The district court did not clearly err by
determining that officers decided to seek a search warrant after they
discovered the spent shell casings but before they discovered the magazine
clip or ammunition.
       To summarize why the district court did not err in applying the
independent source doctrine: The magazine clip and ammunition were not
necessary to establish probable cause and did not motivate the officers to
obtain a search warrant. The magistrate issued a search warrant that
authorized police to search all property located at 710 N. Lyons Street,
including the “interior of the residence, vehicles located on the property,
and curtilage of the property.” This encompassed the areas where the
magazine clip and ammunition were located. The independent source
doctrine permits the magazine clip and ammunition to be introduced as
       _____________________
which he could infer that the firearm was contraband, that it had been used in a crime,
and/or that it was linked to any wrongdoing.” (citation omitted)).




                                          13
Case: 24-30457       Document: 68-1         Page: 14   Date Filed: 05/08/2025




                                  No. 24-30457


evidence in these circumstances regardless whether the initial car searches
were lawful.
                      D. Execution of Search Warrant
       The district court correctly allowed the firearms to be admitted into
evidence because the firearms were recovered through the execution of a
valid search warrant that was obtained without regard to bad acts by law
enforcement. The district court could have alternatively admitted the
“smoking gun” in this case under the good-faith exception to the
exclusionary rule. Under that exception, “if the evidence was obtained by
law enforcement officers who relied on the warrant in objectively reasonable
good-faith, then the evidence obtained during the search is admissible.”
United States v. Allen, 625 F.3d 830, 835 (5th Cir. 2010) (citation omitted).
“This is true even if the evidence in the affidavit . . . was not sufficient to
establish probable cause.” Id.
       August offers scant evidence of bad faith, primarily relying on
exchanges captured by officer body-cam footage that indicate several officers
had a negative opinion of August due to previous interactions with him. But
this evidence fails to move the needle because the good-faith inquiry is
strictly objective. See United States v. Massi, 761 F.3d 512, 530 (5th Cir. 2014)
(“In determining whether the good faith exception applies, ‘we do not
attempt an “expedition into the minds of police officers” to determine their
subjective beliefs regarding the validity of the warrant.’” (citations
omitted)).
       August does not even attempt to allege that it was objectively
unreasonable to rely on the warrant. Nor could he. This is not a case in
which “the magistrate . . . was misled by information in an affidavit that the
affiant knew was false or would have known was false except for his reckless
disregard of the truth.” United States v. Leon, 468 U.S. 897, 923, 104 S. Ct.




                                       14
Case: 24-30457        Document: 68-1         Page: 15   Date Filed: 05/08/2025




                                  No. 24-30457


3405, 3421 (1984) (citation omitted). It is not a case in which the issuing
magistrate “wholly abandoned his judicial role,” or the warrant was based on
an affidavit “so lacking in indicia of probable cause as to render official belief
in its existence entirely unreasonable.” Id. (internal quotation marks and
citations omitted). And it is not a case in which the warrant is “so facially
deficient . . . that the executing officers [could not] reasonably presume it to
be valid.” Id. The good-faith exception therefore supports admitting the
firearms into evidence even if there were a defect in the warrant.
                              V. Conclusion
       For the foregoing reasons, the judgment of the district court is
AFFIRMED.




                                        15

```

---

## GROUP: _overhaul2/lake/cases/United States v. Bagley.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Bagley"
type: case
citation: "473 U.S. 667 (1985)"
parallel_cite: "105 S. Ct. 3375; 87 L. Ed. 2d 481; 53 U.S.L.W. 5084"
neutral_cite: 1985 U.S. LEXIS 130
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-07-02
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-07-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Bagley
  varies_by_point: false
  scope_note: "Good law; the controlling Brady/Giglio materiality standard."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111514/united-states-v-bagley/"
  cluster_id: 111514
  opinion_id: 9430189
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[Kyles v. Whitley]]", "[[Strickler v. Greene]]", "[[Turner v. United States]]"]
aliases: []
tags: ["case", "due-process", "brady"]
holding: "Set the unified MATERIALITY standard for Brady (covering no-request, general-request, and specific-request cases) and confirmed…"
lake:
  record_id: United States v. Bagley
  status: verified
  projected_at: 2026-07-06
---

# United States v. Bagley

*473 U.S. 667 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Bagley was convicted of federal narcotics and firearms charges largely on the testimony of two government informants. Although the defense had specifically requested any deals or inducements, the government did not disclose that the informants had signed contracts promising payment contingent on their assistance. Bagley later discovered the arrangements and sought relief, arguing the suppressed impeachment evidence violated *[[Brady v. Maryland|Brady]]*.

## Issue
What standard of materiality governs a *[[Brady v. Maryland|Brady]]* claim, and whether a single materiality standard applies regardless of whether the defense made no request, a general request, or a specific request for the evidence.

## Rule
The Court adopted one unified materiality standard for all *[[Brady v. Maryland|Brady]]* claims, including suppressed impeachment evidence: "The evidence is material only if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different. A 'reasonable probability' is a probability sufficient to undermine confidence in the outcome." — 473 U.S. at 682. ^pin-682

Impeachment evidence, like [[Brady and Giglio|exculpatory]] evidence, falls within the *[[Brady v. Maryland|Brady]]* rule, and the same reasonable-probability test measures materiality whether or not the defense requested the evidence.

## Application
Because the undisclosed contingent-payment contracts bore on the credibility of the government's two key informant witnesses, they were favorable impeachment evidence within *[[Brady v. Maryland|Brady]]*'s reach. The proper question was therefore whether there was a reasonable probability that disclosure would have produced a different result — a determination the Court [[Reading and Citing Cases#on-remand|remanded]] for the lower courts to make under the newly clarified, single materiality standard rather than under any automatic-reversal or request-specific rule.

## Conclusion
A uniform reasonable-probability materiality standard governs *[[Brady v. Maryland|Brady]]* claims, and it reaches impeachment evidence; the case was [[Reading and Citing Cases#on-remand|remanded]] for application of that standard. Suppressed impeachment evidence is material only where its disclosure would create a reasonable probability of a different outcome.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Bagley* supplies the materiality standard for [[Brady v. Maryland]] and extends it to the impeachment evidence of [[Giglio v. United States]]; it was elaborated in [[Kyles v. Whitley]] (cumulative, whole-record review) and applied in [[Strickler v. Greene]] and [[Turner v. United States]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Bagley*, 473 U.S. 667 (1985) — https://www.courtlistener.com/opinion/111514/united-states-v-bagley/ — pinpoint: 682.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "09753ceebdc179f9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Bagley"}, "payload": {"all": [{"cite": "473 U.S. 667", "page": "667", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "473"}, {"cite": "105 S. Ct. 3375", "page": "3375", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "87 L. Ed. 2d 481", "page": "481", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "1985 U.S. LEXIS 130", "page": "130", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 5084", "page": "5084", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "473 U.S. 667", "official": {"cite": "473 U.S. 667", "page": "667", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "473"}, "official_selection_present": true, "record_id": "United States v. Bagley"}}
{"assertion_id": "22c4dd28c3716295", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-682", "record_id": "United States v. Bagley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-682", "pinpoint_status": "slip-only", "quote": "--- # United States v. Bagley *473 U.S. 667 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Bagley was convicted of federal narcotics and firearms charges largely on the testimony of two government informants. Although the defense had specifically requested any deals or inducements, the government did not disclose that the informants had signed contracts promising payment contingent on their assistance. Bagley later discovered the arrangements and sought relief, arguing the suppressed impeachment evidence violated *Brady*. ## Issue What standard of materiality governs a *Brady* claim, and whether a single materiality standard applies regardless of whether the defense made no request, a general request, or a specific request for the evidence. ## Rule The Court adopted one unified materiality standard for all *Brady* claims, including suppressed impeachment evidence:", "quote_fidelity": "mismatch", "record_id": "United States v. Bagley", "star_marker": null}}
{"assertion_id": "67faf8c4f8fda7c9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Bagley"}, "payload": {"as_of_content": "1985-07-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Bagley", "scope_note": "Good law; the controlling Brady/Giglio materiality standard.", "varies_by_point": false}}
```

### lake record — United States v. Bagley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Bagley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Bagley",
    "case_name_short": "Bagley",
    "case_name_full": "United States v. Bagley",
    "input_case_name": "United States v. Bagley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-07-02",
    "year": 1985,
    "docket": null,
    "cluster_id": 111514,
    "lead_opinion_id": 9430189,
    "sibling_ids": [
      111514,
      9430189,
      9430190,
      9430191,
      9430192
    ],
    "absolute_url": "/opinion/111514/united-states-v-bagley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "473 U.S. 667",
      "volume": "473",
      "reporter": "U.S.",
      "page": "667",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 3375",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 481",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5084",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5084",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 130",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "130",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "473 U.S. 667",
        "volume": "473",
        "reporter": "U.S.",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 3375",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 481",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 130",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "130",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5084",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5084",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "473 U.S. 667",
    "official_selection": {
      "court_class": "scotus",
      "selected": "473 U.S. 667",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-682",
      "page": null,
      "quote": "--- # United States v. Bagley *473 U.S. 667 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Bagley was convicted of federal narcotics and firearms charges largely on the testimony of two government informants. Although the defense had specifically requested any deals or inducements, the government did not disclose that the informants had signed contracts promising payment contingent on their assistance. Bagley later discovered the arrangements and sought relief, arguing the suppressed impeachment evidence violated *Brady*. ## Issue What standard of materiality governs a *Brady* claim, and whether a single materiality standard applies regardless of whether the defense made no request, a general request, or a specific request for the evidence. ## Rule The Court adopted one unified materiality standard for all *Brady* claims, including suppressed impeachment evidence:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-07-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Bagley",
    "varies_by_point": false,
    "scope_note": "Good law; the controlling Brady/Giglio materiality standard.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Jevric",
          "cluster_id": 10873877,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 10309030,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Ex Rel. Darrell J. Robinson v. Darrel Vannoy, Warden, Louisiana State Penitentiary, Angola, Louisiana",
          "cluster_id": 10292764,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 9435476,
          "cite": [
            "2023 Ohio 3894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schlup v. Delo",
          "cluster_id": 117893,
          "cite": [
            "130 L. Ed. 2d 808",
            "115 S. Ct. 851",
            "513 U.S. 298",
            "1995 U.S. LEXIS 701",
            "1995 WL 20524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dominguez Benitez",
          "cluster_id": 136986,
          "cite": [
            "159 L. Ed. 2d 157",
            "124 S. Ct. 2333",
            "542 U.S. 74",
            "2004 U.S. LEXIS 4177",
            "17 Fla. L. Weekly Fed. S 379",
            "72 U.S.L.W. 4478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boyde v. California",
          "cluster_id": 112386,
          "cite": [
            "108 L. Ed. 2d 316",
            "110 S. Ct. 1190",
            "494 U.S. 370",
            "1990 U.S. LEXIS 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sawyer v. Whitley",
          "cluster_id": 112773,
          "cite": [
            "120 L. Ed. 2d 269",
            "112 S. Ct. 2514",
            "505 U.S. 333",
            "1992 U.S. LEXIS 3864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McFarland v. State",
          "cluster_id": 2413967,
          "cite": [
            "928 S.W.2d 482",
            "1996 Tex. Crim. App. LEXIS 19",
            "1996 WL 71513"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coleman",
          "cluster_id": 2115945,
          "cite": [
            "701 N.E.2d 1063",
            "183 Ill. 2d 366",
            "233 Ill. Dec. 789",
            "1998 Ill. LEXIS 938"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyatt v. State",
          "cluster_id": 1991912,
          "cite": [
            "23 S.W.3d 18",
            "2000 Tex. Crim. App. LEXIS 46",
            "2000 WL 526330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pettit",
          "cluster_id": 1250971,
          "cite": [
            "171 Wis. 2d 627",
            "492 N.W.2d 633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greer v. Miller",
          "cluster_id": 111956,
          "cite": [
            "97 L. Ed. 2d 618",
            "107 S. Ct. 3102",
            "483 U.S. 756",
            "1987 U.S. LEXIS 2930"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David C. Hughes, the Office of the Federal Public Defender, Amicus Supporting",
          "cluster_id": 789603,
          "cite": [
            "401 F.3d 540",
            "2005 WL 628224"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William George Bonin v. Arthur Calderon, as Warden of San Quentin State Prison James Rowland, Director of the California Department of Corrections",
          "cluster_id": 699264,
          "cite": [
            "59 F.3d 815",
            "95 Daily Journal DAR 8895",
            "95 Cal. Daily Op. Serv. 5256",
            "1995 U.S. App. LEXIS 16098"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cone v. Bell",
          "cluster_id": 145883,
          "cite": [
            "173 L. Ed. 2d 701",
            "129 S. Ct. 1769",
            "556 U.S. 449",
            "2009 U.S. LEXIS 3298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McFarland v. State",
          "cluster_id": 2429802,
          "cite": [
            "845 S.W.2d 824",
            "1992 Tex. Crim. App. LEXIS 251",
            "1992 WL 438312"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Osband",
          "cluster_id": 5607850,
          "cite": [
            "13 Cal. 4th 622",
            "919 P.2d 640",
            "96 Daily Journal DAR 9137",
            "96 Cal. Daily Op. Serv. 5583",
            "55 Cal. Rptr. 2d 26",
            "1996 Cal. LEXIS 3814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thomas",
          "cluster_id": 2629208,
          "cite": [
            "83 P.3d 970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curry v. State",
          "cluster_id": 1638441,
          "cite": [
            "910 S.W.2d 490",
            "1995 Tex. Crim. App. LEXIS 119",
            "1995 WL 688920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LaMar",
          "cluster_id": 6890210,
          "cite": [
            "95 Ohio St. 3d 181",
            "767 N.E.2d 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haley v. City of Boston",
          "cluster_id": 613874,
          "cite": [
            "657 F.3d 39",
            "2011 U.S. App. LEXIS 19223",
            "2011 WL 4347027"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 844247,
          "cite": [
            "52 Cal. 4th 856",
            "261 P.3d 243",
            "131 Cal. Rptr. 3d 225",
            "2011 Cal. LEXIS 8769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjg2NjE0NDAwMDAwJnM9OTQwNjE4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NDQmcz0xNjk5OTE2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjkwNzYxNjAwMDAwJnM9OTQyMDM1MSZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192)",
    "indexed_citing_opinions": 5258,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111514,
        "count": 4574,
        "count_source": "search"
      },
      {
        "opinion_id": 9430189,
        "count": 761,
        "count_source": "search"
      },
      {
        "opinion_id": 9430190,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430191,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430192,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8547,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-bagley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1NDA0JnM9MTA2NzE2NjUmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111514,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 107361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 107610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 110797,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 229184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 236467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 260996,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 261122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 424868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 426309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 430624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 439958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 1866817,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T22:25:10Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:29:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Bagley

```
<opinion type="majority">
<author id="ASLC">Justice Blackmun</author>
<p id="AmL">announced the judgment of the Court and delivered an opinion of the Court except as to Part III.</p>
<p id="AgWy">In <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87</a></span> (1963), this Court held that “the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or punishment.” The issue in the present case concerns the standard of materiality to be applied in determining whether a conviction should be reversed because the prosecutor failed to disclose requested evidence that could have been used to impeach Government witnesses.</p>
<p id="AcUM">I-H</p>
<p id="Ab3U">In October 1977, respondent Hughes Anderson Bagley was indicted in the Western District of Washington on 15 charges of violating federal-narcotics and firearms statutes. On November 18, 24 days before trial, respondent filed a discovery motion. The sixth paragraph of that motion requested:</p>
<blockquote id="AP8">“The names and addresses of witnesses that the government intends to call at trial. Also the prior criminal records of witnesses, and any deals, promises or induce<page-number citation-index="1" label="670">*670</page-number>ments made to witnesses in exchange for their testimony.” App. 18.<footnotemark>1</footnotemark></blockquote>
<p id="b708-4">The Government’s two principal witnesses at the trial were James F. O’Connor and Donald E. Mitchell. O’Connor and Mitchell were state law enforcement officers employed by the Milwaukee Railroad as private security guards. Between April and June 1977, they assisted the federal Bureau of Alcohol, Tobacco and Firearms (ATF) in conducting an undercover investigation of respondent.</p>
<p id="b708-5">The Government’s response to the discovery motion did not disclose that any “deals, promises or inducements” had been made to O’Connor or Mitchell. In apparent reply to a request in the motion’s ninth paragraph for “[c]opies of all Jencks Act material,”<footnotemark>2</footnotemark> the Government produced a series of affidavits that O’Connor and Mitchell had signed between April 12 and May 4, 1977, while the undercover investigation was in progress. These affidavits recounted in detail the undercover dealings that O’Connor and Mitchell were having at the time with respondent. Each affidavit concluded with the statement, “I made this statement freely and voluntarily without any threats or rewards, or promises of reward having been made to me in return for it.”<footnotemark>3</footnotemark></p>
<p id="b708-6">Respondent waived his right to a jury trial and was tried before the court in December 1977. At the trial, O’Connor <page-number citation-index="1" label="671">*671</page-number>and Mitchell testified about both the firearms and the narcotics charges. On December 23, the court found respondent guilty on the narcotics charges, but not guilty on the firearms charges.</p>
<p id="b709-5">In mid-1980, respondent filed requests for information pursuant to the Freedom of Information Act and to the Privacy Act of 1974, <span class="citation no-link">5 U. S. C. §§552</span> and 552a. He received in response copies of ATF form contracts that O’Connor and Mitchell had signed on May 3, 1977. Each form was entitled “Contract for Purchase of Information and Payment of Lump Sum Therefor.” The printed portion of the form stated that the vendor “will provide” information to ATF and that “upon receipt of such information by the Regional Director, Bureau of Alcohol, Tobacco and Firearms, or his representative, and upon the accomplishment of the objective sought to be obtained by the use of such information to the satisfaction of said Regional Director, the United States will pay to said vendor a sum commensurate with services and information rendered.” App. 22 and 23. Each form contained the following typewritten description of services:</p>
<blockquote id="b709-6">“That he will provide information regarding T-I and other violations committed by Hughes A. Bagley, Jr.; that he will purchase evidence for ATF; that he will cut <em>[sic] </em>in an undercover capacity for ATF; that he will assist ATF in gathering of evidence and testify against the violator in federal court.” <em><span class="citation no-link">Ibid.</span></em></blockquote>
<p id="b709-7">The figure “$300.00” was handwritten in each form on a line entitled “Sum to Be Paid to Vendor.”</p>
<p id="b709-8">Because these contracts had not been disclosed to respondent in response to his pretrial discovery motion,<footnotemark>4</footnotemark> respondent moved under <span class="citation no-link">28 U. S. C. § 2255</span> to vacate his sentence. He <page-number citation-index="1" label="672">*672</page-number>alleged that the Government’s failure to disclose the contracts, which he could have used to impeach O’Connor and Mitchell, violated his right to due process under <em>Brady </em>v. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland, supra.</a></span></em></p>
<p id="b710-5">The motion came before the same District Judge who had presided at respondent’s bench trial. An evidentiary hearing was held before a Magistrate. The Magistrate found that the printed form contracts were blank when O’Connor and Mitchell signed them and were not signed by an ATF representative until after the trial. He also found that on January 4, 1978, following the trial and decision in respondent’s case, ATF made payments of $300 to both O’Connor and Mitchell pursuant to the contracts.<footnotemark>5</footnotemark> Although the ATF case agent who dealt with O’Connor and Mitchell testified that these payments were compensation for expenses, the Magistrate found that this characterization was not borne out by the record. There was no documentation for expenses in these amounts; Mitchell testified that his payment was not for expenses, and the ATF forms authorizing the payments treated them as rewards.</p>
<p id="b710-6">The District Court adopted each of the Magistrate’s findings except for the last one to the effect that “[n]either O’Connor nor Mitchell expected to receive the payment of $300 or any payment from the United States for their testimony.” App. to Pet. for Cert. 7a, 12a, 14a. Instead, the court found that it was “probable” that O’Connor and Mitchell expected to receive compensation, in addition to their expenses, for their assistance, “though perhaps not for their testimony.” <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span> </em>at 7a. The District Court also expressly rejected, <em>ibid., </em>the Magistrate’s conclusion, <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">id.,</a></span> </em>at 14a, that:</p>
<blockquote id="b711-4"><page-number citation-index="1" label="673">*673</page-number>“Because neither witness was promised or expected payment for his testimony, the United States did not withhold, during pretrial discovery, information as to any ‘deals, promises or inducements’ to these witnesses. Nor did the United States suppress evidence favorable to the defendant, in violation of <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).”</blockquote>
<p id="b711-5">The District Court found beyond a reasonable doubt, however, that had the existence of the agreements been disclosed to it during trial, the disclosure would have had no effect upon its finding that the Government had proved beyond a reasonable doubt that respondent was guilty of the offenses for which he had been convicted. <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span> at 8a. The District Court reasoned: Almost all of the testimony of both witnesses was devoted to the firearms charges in the indictment. Respondent, however, was acquitted on those charges. The testimony of O’Connor and Mitchell concerning the narcotics charges was relatively very brief. On cross-examination, respondent’s counsel did not seek to discredit their testimony as to the facts of distribution but rather sought to show that the controlled substances in question came from supplies that had been prescribed for respondent’s personal use. The answers of O’Connor and Mitchell to this line of cross-examination tended to be favorable to respondent. Thus, the claimed impeachment evidence would not have been helpful to respondent and would not have affected the outcome of the trial. Accordingly, the District Court denied respondent’s motion to vacate his sentence.</p>
<p id="b711-6">The United States Court of Appeals for the Ninth Circuit reversed. <em>Bagley </em>v. <em>Lumpkin, </em><span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d 1462</a></span> (1983). The Court of Appeals began by noting that, according to precedent in the Circuit, prosecutorial failure to respond to a specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request is properly analyzed as error, and a resulting conviction must be reversed unless the error is harmless beyond a reasonable doubt. The court noted that the District Judge who had presided over the bench trial <page-number citation-index="1" label="674">*674</page-number>concluded beyond a reasonable doubt that disclosure of the ATF agreement would not have affected the outcome. The Court of Appeals, however, stated that it “disagree[d]” with this conclusion. <em>Id., </em>at 1464. In particular, it disagreed with the Government’s — and the District Court’s — premise that the testimony of O’Connor and Mitchell was exculpatory on the narcotics charges, and that respondent therefore would not have sought to impeach “his own witness.” <em>Id., </em>at 1464, n. 1.</p>
<p id="b712-5">The Court of Appeals apparently based its reversal, however, on the theory that the Government’s failure to disclose the requested <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>information that respondent could have used to conduct an effective cross-examination impaired respondent’s right to confront adverse witnesses. The court noted: “In <em>Davis </em>v. <em>Alaska, . . . </em>the Supreme Court held that the denial of the ‘right of <em>effective </em>cross-examination’ was ‘ “constitutional error of the first magnitude” ’ requiring automatic reversal.” <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span> (quoting <em>Davis </em>v. <em>Alaska, </em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/#318" aria-description="Citation for case: Davis v. Alaska">415 U. S. 308, 318</a></span> (1974)) (emphasis added by Court of Appeals). In the last sentence of its opinion, the Court of Appeals concluded: “we hold that the government’s failure to provide requested <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>information to Bagley so that he could effectively cross-examine two important government witnesses requires an automatic reversal.” <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/#1464" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span>.</p>
<p id="b712-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./469/1016/">469 U. S. 1016</a></span> (1984), and we now reverse.</p>
<p id="b712-7">II</p>
<p id="b712-8">The holding in <em>Brady </em>v. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland</a></span> </em>requires disclosure only of evidence that is both favorable to the accused and “material either to guilt or to punishment.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. See also <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#794" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 794-795</a></span> (1972). The Court explained in <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 104</a></span> (1976): “A fair analysis of the holding in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>indicates that implicit in the requirement of materiality is a concern that the suppressed evidence might have affected the outcome of <page-number citation-index="1" label="675">*675</page-number>the trial.” The evidence suppressed in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>would have been admissible only on the issue of punishment and not on the issue of guilt, and therefore could have affected only Brady’s sentence and not his conviction. Accordingly, the Court affirmed the lower court’s restriction of Brady’s new trial to the issue of punishment.</p>
<p id="b713-5">The <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule is based on the requirement of due process. Its purpose is not to displace the adversary system as the primary means by which truth is uncovered, but to ensure that a miscarriage of justice does not occur.<footnotemark>6</footnotemark> Thus, the prosecutor is not required to deliver his entire file to defense counsel,<footnotemark>7</footnotemark> but only to disclose evidence favorable to the accused that, if suppressed, would deprive the defendant of a fair trial:</p>
<blockquote id="b713-6">“For unless the omission deprived the defendant of a fair trial, there was no constitutional violation requiring that the verdict be set aside; and absent a constitutional violation, there was no breach of the prosecutor’s constitutional duty to disclose. . . .</blockquote>
<blockquote id="b713-7">“. . . But to reiterate a critical point, the prosecutor will not have violated his constitutional duty of disclo<page-number citation-index="1" label="676">*676</page-number>sure unless his omission is of sufficient significance to result in the denial of the defendant’s right to a fair trial.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#108" aria-description="Citation for case: United States v. Agurs">427 U. S., at 108</a></span>.</blockquote>
<p id="b714-4">In <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>, </em>the prosecutor failed to disclose exculpatory evidence. In the present case, the prosecutor failed to disclose evidence that the defense might have used to impeach the Government’s witnesses by showing bias or interest. Impeachment evidence, however, as well as exculpatory evidence, falls within the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule. See <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972). Such evidence is “evidence favorable to an accused,” <em>Brady, </em>873 U. S., at 87, so that, if disclosed and used effectively, it may make the difference between conviction and acquittal. Cf. <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269</a></span> (1959) (“The jury’s estimate of the truthfulness and reliability of a given witness may well be determinative of guilt or innocence, and it is upon such subtle factors as the possible interest of the witness in testifying falsely that a defendant’s life or liberty may depend”).</p>
<p id="b714-5">The Court of Appeals treated impeachment evidence as constitutionally different from exculpatory evidence. According to that court, failure to disclose impeachment evidence is “even more egregious” than failure to disclose exculpatory evidence “because it threatens the defendant’s right to confront adverse witnesses.” <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/#1464" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span>. Relying on <em>Davis </em>v. <em>Alaska, </em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">415 U. S. 308</a></span> (1974), the Court of Appeals held that the Government’s failure to disclose requested impeachment evidence that the defense could use to conduct an effective cross-examination of important prosecution witnesses constitutues “‘constitutional error of the first magnitude’” requiring automatic reversal. <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span> (quoting <em>Davis </em>v. <span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/#318" aria-description="Citation for case: Davis v. Alaska"><em>Alaska, supra, </em>at 318</a></span>).</p>
<p id="b714-6">This Court has rejected any such distinction between impeachment evidence and exculpatory evidence. In <em>Giglio </em>v. <em>United States, supra, </em>the Government failed to disclose impeachment evidence similar to the evidence at issue in the present case, that is, a promise made to the key Government <page-number citation-index="1" label="677">*677</page-number>witness that he would not be prosecuted if he testified for the Government. This Court said:</p>
<blockquote id="b715-5">“When the ‘reliability of a given -witness may well be determinative of guilt or innocence/ nondisclosure of evidence affecting credibility falls -within th[e] general rule [of <em>Brady]. </em>We do not, however, automatically require a new trial whenever ‘a combing of the prosecutors’ files after the trial has disclosed evidence possibly useful to the defense but not likely to have changed the verdict . . . A finding of materiality of the evidence is required under <em>Brady. ... A </em>new trial is required if ‘the false testimony could ... in any reasonable likelihood have affected the judgment of the jury . . . <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S., at 154</a></span> (citations omitted).</blockquote>
<p id="b715-7">Thus, the Court of Appeals’ holding is inconsistent with our precedents.</p>
<p id="b715-8">Moreover, the court’s reliance on <em>Davis </em>v. <em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">Alaska</a></span> </em>for its “automatic reversal” rule is misplaced. In <em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">Davis</a></span>, </em>the defense sought to cross-examine a crucial prosecution witness concerning his probationary status as a juvenile delinquent. The defense intended by this cross-examination to show that the witness might have made a faulty identification of the defendant in order to shift suspicion away from himself or because he feared that his probationary status would be jeopardized if he did not satisfactorily assist the police and prosecutor in obtaining a conviction. Pursuant to a state rule of procedure and a state statute making juvenile adjudications inadmissible, the trial judge prohibited the defense from conducting the cross-examination. This Court reversed the defendant’s conviction, ruling that the direct restriction on the scope of cross-examination denied the defendant “the right of effective cross-examination which “‘would be constitutional error of the first magnitude and no amount of showing of want of prejudice would cure it.” <em>Brookhart </em>v. <em>Janis, </em><span class="citation" data-id="107209"><a href="/opinion/107209/brookhart-v-janis/#3" aria-description="Citation for case: Brookhart v. Janis">384 U. S. 1, 3</a></span>.’” <span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">415 U. S., at 318</a></span> (quoting <em>Smith </em><page-number citation-index="1" label="678">*678</page-number>v. <em>Illinois, </em><span class="citation" data-id="9423611"><a href="/opinion/107610/smith-v-illinois/#131" aria-description="Citation for case: Smith v. Illinois">390 U. S. 129, 131</a></span> (1968)). See also <em>United States </em>v. <em>Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#659" aria-description="Citation for case: United States v. Cronic">466 U. S. 648, 659</a></span> (1984).</p>
<p id="b716-5">The present case, in contrast, does not involve any direct restriction on the scope of cross-examination. The defense was free to cross-examine the witnesses on any relevant subject, including possible bias or interest resulting from inducements made by the Government. The constitutional error, if any, in this case was the Government’s failure to assist the defense by disclosing information that might have been helpful in conducting the cross-examination. As discussed above, such suppression of evidence amounts to a constitutional violation only if it deprives the defendant of a fair trial. Consistent with “our overriding concern with the justice of the finding of guilt,” <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112</a></span>, a constitutional error occurs, and the conviction must be reversed, only if the evidence is material in the sense that its suppression undermines confidence in the outcome of the trial.</p>
<p id="b716-6">Ill</p>
<p id="b716-7">A</p>
<p id="b716-8">It remains to determine the standard of materiality applicable to the nondisclosed evidence at issue in this case. Our starting point is the framework for evaluating the materiality of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence established in <em>United States </em>v. <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>. </em>The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>distinguished three situations involving the discovery, after trial, of information favorable to the accused that had been known to the prosecution but unknown to the defense. The first situation was the prosecutor’s knowing use of perjured testimony or, equivalently, the prosecutor’s knowing failure to disclose that testimony used to convict the defendant was false. The Court noted the well-established rule that “a conviction obtained by the knowing use of perjured testimony is fundamentally unfair, and must be set aside if there is any reasonable likelihood that the false testimony could have affected the judgment of the jury.” <page-number citation-index="1" label="679">*679</page-number><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U. S., at 103</a></span> (footnote omitted).<footnotemark>8</footnotemark> Although this rule is stated in terms that treat the knowing use of perjured testimony as error subject to harmless-error review,<footnotemark>9</footnotemark> it may as <page-number citation-index="1" label="680">*680</page-number>easily be stated as a materiality standard under which the fact that testimony is perjured is considered material unless failure to disclose it would be harmless beyond a reasonable doubt. The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>justified this standard of materiality on the ground that the knowing use of perjured testimony involves prosecutorial misconduct and, more importantly, involves “a corruption of the truth-seeking function of the trial process.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 104</a></span>.</p>
<p id="b718-5">At the other extreme is the situation in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>itself, where the defendant does not make a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request and the prosecutor fails to disclose certain evidence favorable to the accused. The Court rejected a harmless-error rule in that situation, because under that rule every nondisclosure is treated as error, thus imposing on the prosecutor a constitutional duty to deliver his entire file to defense counsel.<footnotemark>10</footnotemark> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs">427 U. S., at 111-112</a></span>. At the same time, the Court rejected a standard that would require the defendant to demonstrate that the evidence if disclosed probably would have resulted in acquittal. <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 111</a></span>. The Court reasoned: “If the standard applied to the usual motion for a new trial based on newly discovered evidence were the same when the evidence was in the State’s possession as when it was found in a neutral source, there would be no special significance to the prosecutor’s obligation to serve the cause of justice.” <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Ibid.</a></span> </em>The <page-number citation-index="1" label="681">*681</page-number>standard of materiality applicable in the absence of a specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request is therefore stricter than the harmless-error standard but more lenient to the defense than the newly-discovered-evidence standard.</p>
<p id="b719-5">The third situation identified by the Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>is where the defense makes a specific request and the prosecutor fails to disclose responsive evidence.<footnotemark>11</footnotemark> The Court did not define the standard of materiality applicable in this situation,<footnotemark>12</footnotemark> but suggested that the standard might be more lenient to the defense than in the situation in which the defense makes no request or only a general request. <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#106" aria-description="Citation for case: United States v. Agurs">427 U. S., at 106</a></span>. The Court also noted: “When the prosecutor receives a specific and relevant request, the failure to make any response is seldom, if ever, excusable.” <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Ibid.</a></span></em></p>
<p id="b719-6">The Court has relied on and reformulated the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>standard for the materiality of undisclosed evidence in two subsequent cases arising outside the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>context. In neither case did the Court’s discussion of the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>standard distinguish among the three situations described in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>. </em>In <em>United States </em>v. <em>Valenzuela-Bernal, </em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#874" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 874</a></span> (1982), the Court held that due process is violated when testimony is made unavailable to the defense by Government deportation of witnesses “only if there is a reasonable likelihood that the testimony could have affected the judgment of the <page-number citation-index="1" label="682">*682</page-number>trier of fact.” And in <em>Strickland </em>v. <em>Washington, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668</a></span> (1984), the Court held that a new trial must be granted when evidence is not introduced because of the incompetence of counsel only if “there is a reasonable probability that, but for counsel’s unprofessional errors, the result of the proceeding would have been different.” <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#694" aria-description="Citation for case: Strickland v. Washington"><em>Id., </em>at 694</a></span>.<footnotemark>13</footnotemark> The <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span> </em>Court defined a “reasonable probability” as “a probability sufficient to undermine confidence in the outcome.” <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Ibid.</a></span></em></p>
<p id="b720-5">We find the <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span> </em>formulation of the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>test for materiality sufficiently flexible to cover the “no request,” “general request,” and “specific request” cases of prosecu-torial failure to disclose evidence favorable to the accused: The evidence is material only if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different. A “reasonable probability” is a probability sufficient to undermine confidence in the outcome.</p>
<p id="b720-6">The Government suggests that a materiality standard more favorable to the defendant reasonably might be adopted in specific request cases. See Brief for United States 31. The Government notes that an incomplete response to a specific request not only deprives the defense of certain evidence, but also has the effect of representing to the defense that the evidence does not exist. In reliance on this misleading representation, the defense might abandon lines of independent investigation, defenses, or trial strategies that it otherwise would have pursued. <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Ibid.</a></span></em></p>
<p id="b720-7">We agree that the prosecutor’s failure to respond fully to a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request may impair the adversary process in this manner. And the more specifically the defense requests certain evidence, thus putting the prosecutor on notice of its value, the more reasonable it is for the defense to assume from the <page-number citation-index="1" label="683">*683</page-number>nondisclosure that the evidence does not exist, and to make pretrial and trial decisions on the basis of this assumption. This possibility of impairment does not necessitate a different standard of materiality, however, for under the <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span> </em>formulation the reviewing court may consider directly any adverse effect that the prosecutor’s failure to respond might have had on the preparation or presentation of the defendant’s case. The reviewing court should assess the possibility that such effect might have occurred in light of the totality of the circumstances and with an awareness of the difficulty of reconstructing in a post-trial proceeding the course that the defense and the trial would have taken had the defense not been misled by the prosecutor’s incomplete response.</p>
<p id="b721-5">B</p>
<p id="b721-6">In the present case, we think that there is a significant likelihood that the prosecutor’s response to respondent’s discovery motion misleadingly induced defense counsel to believe that O’Connor and Mitchell could not be impeached on the basis of bias or interest arising from inducements offered by the Government. Defense counsel asked the prosecutor to disclose any inducements that had been made to witnesses, and the prosecutor failed to disclose that the possibility of a reward had been held out to O’Connor and Mitchell if the information they supplied led to “the accomplishment of the objective sought to be obtained ... to the satisfaction of [the Government].” App. 22 and 23. This possibility of a reward gave O’Connor and Mitchell a direct, personal stake in respondent’s conviction. The fact that the stake was not guaranteed through a promise or binding contract, but was expressly contingent on the Government’s satisfaction with the end result, served only to strengthen any incentive to testify falsely in order to secure a conviction. Moreover, the prosecutor disclosed affidavits that stated that O’Connor and Mitchell received no promises of reward in return for providing information in the affidavits implicating respondent in <page-number citation-index="1" label="684">*684</page-number>criminal activity. In fact, O’Connor and Mitchell signed the last of these affidavits the very day after they signed the ATF contracts. While the Government is technically correct that the blank contracts did not constitute a “promise of reward,” the natural effect of these affidavits would be misleadingly to induce defense counsel to believe that O’Connor and Mitchell provided the information in the affidavits, and ultimately their testimony at trial recounting the same information, without any “inducements.”</p>
<p id="b722-5">The District Court, nonetheless, found beyond a reasonable doubt that, had the information that the Government held out the possibility of reward to its witnesses been disclosed, the result of the criminal prosecution would not have been different. If this finding were sustained by the Court of Appeals, the information would be immaterial even under the standard of materiality applicable to the prosecutor’s knowing use of perjured testimony. Although the express holding of the Court of Appeals was that the nondisclosure in this case required automatic reversal, the Court of Appeals also stated that it “disagreed” with the District Court’s finding of harmless error. In particular, the Court of Appeals appears to have disagreed with the factual premise on which this finding expressly was based. The District Court reasoned that O’Connor’s and Mitchell’s testimony was exculpatory on the narcotics charges. The Court of Appeals, however, concluded, after reviewing the record, that O’Connor’s and Mitchell’s testimony was in fact inculpatory on those charges. <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/#1464" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464, n. 1</a></span>. Accordingly, we reverse the judgment of the Court of Appeals and remand the case to that court for a determination whether there is a reasonable probability that, had the inducement offered by the Government to O’Connor and Mitchell been disclosed to the defense, the result of the trial would have been different.</p>
<p id="b722-6">
<em>It is so ordered.</em>
</p>
<p id="b722-7">Justice Powell took no part in the decision of this case.</p>
<footnote label="1">
<p id="b708-7"> In addition, ¶ 10(b) of the motion requested “[p]romises or representations made to any persons the government intends to call as witnesses at trial, including but not limited to promises of no prosecution, immunity, lesser sentence, etc.,” and ¶11 requested “[a]ll information which would establish the reliability of the Milwaukee Railroad Employees in this case, whose testimony formed the basis for the search warrant.” App. 18-19.</p>
</footnote>
<footnote label="2">
<p id="b708-8"> The Jencks Act, <span class="citation no-link">18 U. S. C. § 3600</span>, requires the prosecutor to disclose, after direct examination of a Government witness and on the defendant’s motion, any statement of the witness in the Government’s possession that relates to the subject matter of the witness’ testimony.</p>
</footnote>
<footnote label="3">
<p id="b708-9"> Brief for United States 3, quoting Memorandum of Points and Authorities in Support of Pet. for Habeas Corpus, CV80-3592-RJK(M) (CD Cal.) Exhibits 1-9.</p>
</footnote>
<footnote label="4">
<p id="b709-9"> The Assistant United States Attorney who prosecuted respondent stated in stipulated testimony that he had not known that the contracts existed and that he would have furnished them to respondent had he known of them. See App. to Pet. for Cert. 13a.</p>
</footnote>
<footnote label="5">
<p id="b710-7"> The Magistrate found, too, that ATF paid O’Connor and Mitchell, respectively, $90 and $80 in April and May 1977 before trial, but concluded that these payments were intended to reimburse O’Connor and Mitchell for expenses, and would not have provided a basis for impeaching O’Connor’s and Mitchell’s trial testimony. The District Court adopted this finding and conclusion. <em><span class="citation no-link">Id.,</span> </em>at 7a, 13a.</p>
</footnote>
<footnote label="6">
<p id="b713-8"> By requiring the prosecutor to assist the defense in making its ease, the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule represents a limited departure from a pure adversary model. The Court has recognized, however, that the prosecutor’s role transcends that of an adversary: he “is the representative not of an ordinary party to a controversy, but of a sovereignty . . . whose interest ... in a criminal prosecution is not that it shall win a case, but that justice shall be done.” <em>Berger </em>v. <em>United States, </em><span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935). See <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87-88</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b713-9"> See <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#106" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 106, 111</a></span> (1976); <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972). See also <em>California </em>v. <em>Trombetta, </em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#488" aria-description="Citation for case: California v. Trombetta">467 U. S. 479, 488, n. 8</a></span> (1984). An interpretation of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>to create a broad, constitutionally required right of discovery “would entirely alter the character and balance of our present systems of criminal justice.” <em>Giles </em>v. <em>Maryland, </em><span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#117" aria-description="Citation for case: Giles v. Maryland">386 U. S. 66, 117</a></span> (1967) (dissenting opinion). Furthermore, a rule that the prosecutor commits error by any failure to disclose evidence favorable to the accused, no matter how insignificant, would impose an impossible burden on the prosecutor and would undermine the interest in the finality of judgments.</p>
</footnote>
<footnote label="8">
<p id="b717-5"> In fact, the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule has its roots in a series of eases dealing with convictions based on the prosecution’s knowing use of perjured testimony. In <em>Mooney </em>v. <em>Holohan, </em><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span> (1935), the Court established the rule that the knowing use by a state prosecutor of perjured testimony to obtain a conviction and the deliberate suppression of evidence that would have impeached and refuted the testimony constitutes a denial of due process. The Court reasoned that “a deliberate deception of court and jury by the presentation of testimony known to be perjured” is inconsistent with “the rudimentary demands of justice.” <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan"><em>Id., </em>at 112</a></span>. The Court reaffirmed this principle in broader terms in <em>Pyle </em>v. <em>Kansas, </em><span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span> (1942), where it held that allegations that the prosecutor had deliberately suppressed evidence favorable to the accused and had knowingly used perjured testimony were sufficient to charge a due process violation.</p>
<p id="b717-6">The Court again reaffirmed this principle in <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959). In <em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span>, </em>the principal witness for the prosecution falsely testified that he had been promised no consideration for his testimony. The Court held that the knowing use of false testimony to obtain a conviction violates due process regardless of whether the prosecutor solicited the false testimony or merely allowed it to go uncorrected when it appeared. The Court explained that the principle that a State may not knowingly use false testimony to obtain a conviction — even false testimony that goes only to the credibility of the witness — is “implicit in any concept of ordered liberty.” <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><em>Id., </em>at 269</a></span>. Finally, the Court held that it was not bound by the state court’s determination that the false testimony “could not in any reasonable likelihood have affected the judgment of the jury.” <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois"><em>Id., </em>at 271</a></span>. The Court conducted its own independent examination of the record and concluded that the false testimony “may have had an effect on the outcome of the trial.” <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#272" aria-description="Citation for case: Napue v. Illinois"><em>Id., </em>at 272</a></span>. Accordingly, the Court reversed the judgment of conviction.</p>
</footnote>
<footnote label="9">
<p id="b717-7"> The rule that a conviction obtained by the knowing use of perjured testimony must be set aside if there is any reasonable likelihood that the false testimony could have affected the jury’s verdict derives from <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois">360 U. S., at 271</a></span>. See n. 8, <em>supra. </em>See also <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972) (quoting <em>Napue, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois">360 U. S., at 271</a></span>). <em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span> </em>antedated <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967), where the “harmless beyond a reasonable doubt” standard was established. The Court in <em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span> </em>noted that there was little, if any, difference between <page-number citation-index="1" label="680">*680</page-number>a rule formulated, as in <em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span>, </em>in terms of “ ‘whether there is a reasonable possibility that the evidence complained of might have contributed to the conviction,’ ” and a rule “ ‘requiring the beneficiary of a constitutional error to prove beyond a reasonable doubt that the error complained of did not contribute to the verdict obtained.’” 386 U. S., at 24 (quoting <em>Fahy </em>v. <em>Connecticut, </em><span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#86" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85, 86-87</a></span> (1963)). It is therefore clear, as indeed the Government concedes, see Brief for United States 20, and 36-38, that this Court’s precedents indicate that the standard of review applicable to the knowing use of perjured testimony is equivalent to the <em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span> </em>harmless-error standard.</p>
</footnote>
<footnote label="10">
<p id="b718-7"> This is true only if the nondisclosure is treated as error subject to harmless-error review, and not if the nondisclosure is treated as error only if the evidence is material under a not “harmless beyond a reasonable doubt” standard.</p>
</footnote>
<footnote label="11">
<p id="b719-7"> The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>identified <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>as a case in which specific information was requested by the defense. <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#106" aria-description="Citation for case: United States v. Agurs">427 U. S., at 106</a></span>. The request in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>was for the extrajudicial statements of Brady’s accomplice. See <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#84" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 84</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b719-8"> The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>noted: “A fair analysis of the holding in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>indicates that implicit in the requirement of materiality is a concern that the suppressed evidence might have affected the outcome of the trial.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs">427 U. S., at 104</a></span>. Since the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>Court identified <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>as a “specific request” case, see n. 11, <em>supra, </em>this language might be taken as indicating the standard of materiality applicable in such a case. It is clear, however, that the language merely explains the meaning of the term “materiality.” It does not establish a standard of materiality because it does not indicate what quantum of likelihood there must be that the undisclosed evidence would have affected the outcome.</p>
</footnote>
<footnote label="13">
<p id="b720-8"> In particular, the Court explained in <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span>: </em>“When a defendant challenges a conviction, the question is whether there is a reasonable probability that, absent the errors, the factfinder would have had a reasonable doubt respecting guilt.” 466 U. S., at 695.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Bajakajian.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Bajakajian
type: case
citation: "524 U.S. 321 (1998)"
parallel_cite: "118 S. Ct. 2028; 141 L. Ed. 2d 314"
neutral_cite: 1998 U.S. LEXIS 4172
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-06-22
docket: No. 96-1487
authority_weight: "Binding — SCOTUS"
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
  opinion_url: "https://www.courtlistener.com/opinion/118234/united-states-v-bajakajian/"
  cluster_id: 118234
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Bajakajian
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[Austin v. United States]]"
  - "[[Timbs v. Indiana]]"
tags:
  - case
  - eighth-amendment
  - excessive-fines
  - civil-forfeiture
  - proportionality
  - currency-reporting
  - punishment
holding: "Requiring forfeiture of the entire $357,144 that the defendant willfully failed to report when transporting currency out of the United States violated the Eighth Amendment's Excessive Fines Clause; a punitive forfeiture is unconstitutionally excessive if the amount forfeited is grossly disproportional to the gravity of the defendant's offense."
aliases:
  - United States v. Bajakajian
  - "United States v. Bajakajian (1998)"
---

# United States v. Bajakajian

*524 U.S. 321 (1998)* (No. 96-1487) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 118234 → combined opinion 118234 (Thomas, J.; 524 U.S. 321, argued Nov. 4, 1997, decided June 22, 1998). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*335` follows the quoted holding, which sits on page 334). S9 promotes. -->

## Background
On June 9, 1994, Hosep Bajakajian and his family were at Los Angeles International Airport waiting to fly to Italy, bound ultimately for Cyprus. Customs inspectors using currency-detecting dogs found cash in the family's baggage; questioned, Bajakajian understated the amount, but a search turned up $357,144 in all. Federal law required travelers to report transporting more than $10,000 out of the country, and 18 U.S.C. § 982(a)(1) directs forfeiture of any property involved in a willful violation. Bajakajian pleaded guilty to the failure-to-report count and had a bench trial on forfeiture. The District Court found the money was not tied to any other crime and was being carried to repay a lawful debt, and that full forfeiture would be "grossly disproportionate" and unconstitutional; it ordered forfeiture of only $15,000 plus a $5,000 fine and probation. The Ninth Circuit affirmed, and the Government sought full forfeiture.

## Issue
Whether forfeiture of the entire $357,144 that the defendant failed to report — a sanction the Court treated as at least partly punitive — would violate the Excessive Fines Clause of the Eighth Amendment.

## Rule
Because the § 982(a)(1) forfeiture functioned as punishment for the reporting offense, it was a "fine" within the Excessive Fines Clause; the Court then supplied the excessiveness standard it had left open in *[[Austin v. United States|Austin]]*. Drawing on the Clause's text and history and on the deference owed to legislative judgments about penalties, the Court adopted a proportionality test: "We now hold that a punitive forfeiture violates the Excessive Fines Clause if it is grossly disproportional to the gravity of a defendant's offense." — 524 U.S. at 334. ^pin-334

## Application
Applying that standard, full forfeiture failed it. Bajakajian's crime was solely a reporting offense: it was lawful to carry the currency abroad so long as he declared it, the money had no connection to any other illegality, and the harm to the Government from the non-report was minimal. Against that, a $357,144 forfeiture dwarfed the $5,000 Guidelines fine by orders of magnitude and bore no articulable correlation to any injury the Government suffered. The Court therefore concluded the forfeiture was grossly disproportional to the gravity of the offense and unconstitutional.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **affirmed**. Thomas, J., delivered the opinion of the Court (Stevens, Souter, Ginsburg, and Breyer, JJ., joined). Kennedy, J., filed a [[Common Legal Terms#dissenting-opinion|dissent]], joined by Rehnquist, C.J., and O'Connor and Scalia, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Bajakajian* is the excessiveness *standard* in the forfeiture line: *[[Austin v. United States]]* (1993) established that punitive civil forfeitures are subject to the Excessive Fines Clause but reserved the test; *Bajakajian* supplies it ("grossly disproportional"); and *[[Timbs v. Indiana]]* (2019) makes the Clause enforceable against the States. It is also the Court's first decision actually striking a federal economic sanction as an excessive fine. Teach it as the operative proportionality rule for challenging a forfeiture as excessive.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. Bajakajian*, 524 U.S. 321 (1998)](https://www.courtlistener.com/opinion/118234/united-states-v-bajakajian/) — pinpoint: 334 (Thomas, J., for the Court; the CL opinion text places the quoted "grossly disproportional" holding immediately before the reporter star `*335`, i.e., on page 334). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "198243d64c228444", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Bajakajian"}, "payload": {"all": [{"cite": "524 U.S. 321", "page": "321", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "524"}, {"cite": "118 S. Ct. 2028", "page": "2028", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "118"}, {"cite": "141 L. Ed. 2d 314", "page": "314", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}, {"cite": "1998 U.S. LEXIS 4172", "page": "4172", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1998"}], "display": "524 U.S. 321", "official": {"cite": "524 U.S. 321", "page": "321", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "524"}, "official_selection_present": true, "record_id": "United States v. Bajakajian"}}
{"assertion_id": "b6dc8fb091b815ed", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Bajakajian"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Bajakajian", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Bajakajian

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Bajakajian",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Bajakajian",
    "case_name_short": "Bajakajian",
    "case_name_full": "United States v. Bajakajian",
    "input_case_name": "United States v. Bajakajian",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-06-22",
    "year": 1998,
    "docket": "No. 96-1487",
    "cluster_id": 118234,
    "lead_opinion_id": 9433683,
    "sibling_ids": [],
    "absolute_url": "/opinion/118234/united-states-v-bajakajian/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "524 U.S. 321",
      "volume": "524",
      "reporter": "U.S.",
      "page": "321",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 2028",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 314",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 4172",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "524 U.S. 321",
        "volume": "524",
        "reporter": "U.S.",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 2028",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 314",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 4172",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "524 U.S. 321",
    "official_selection": {
      "court_class": "scotus",
      "selected": "524 U.S. 321",
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
    "date_created": "2026-07-06T13:16:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-bajakajian--118234",
      "to_record_id": "United States v. Bajakajian",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Bajakajian

```
<opinion type="majority">
<author id="b368-7">Justice Thomas</author>
<p id="AmP">delivered the opinion of the Court.</p>
<p id="b368-8">Respondent Hosep Bajakajian attempted to leave the United States without reporting, as required by federal law, that he was transporting more than $10,000 in currency. Federal law also provides that a person convicted of willfully violating this reporting requirement shall forfeit to the Government “any property . . . involved in such offense.” <span class="citation no-link">18 U. S. C. § 982</span>(a)(1). The question in this case is whether forfeiture of the entire $857,144 that respondent failed to declare would violate the Excessive Fines Clause of the Eighth Amendment. We hold that it would, because full forfeiture of respondent’s currency would be grossly disproportional to the gravity of his offense.</p>
<p id="b368-9">I</p>
<p id="b368-10">On June 9,1994, respondent, his wife, and his two daughters were waiting at Los Angeles International Airport to board a flight to Italy; their final destination was Cyprus. Using dogs trained to detect currency by its smell, customs inspectors discovered some $230,000 in cash in the Bajakaji-ans’ checked baggage. A customs inspector approached respondent and his wife and told them that they were required to report all money in excess of $10,000 in their possession or in their baggage. Respondent said that he had $8,000 and <page-number citation-index="1" label="325">*325</page-number>that his wife had another $7,000, but that the family had no additional currency to declare. A search of their carry-on bags, purse, and wallet revealed more cash; in all, customs inspectors found $357,144. The currency was seized and respondent was taken into custody.</p>
<p id="b369-5">A federal grand jury indicted respondent on three counts. Count One charged him with failing to report, as required by 31U. S. C. § 5316(a)(1)(A),<footnotemark>1</footnotemark> that he was transporting more than $10,000 outside the United States, and with doing so “willfully,” in violation of § 5322(a).<footnotemark>2</footnotemark> Count Two charged him with making a false material statement to the United States Customs Service, in violation of <span class="citation no-link">18 U. S. C. § 1001</span>. Count Three sought forfeiture of the $357,144 pursuant to <span class="citation no-link">18 U. S. C. § 982</span>(a)(1), which provides:</p>
<blockquote id="b369-6">“The court, in imposing sentence on a person convicted of an offense in violation of section . . . 5316, . . . shall order that the person forfeit to the United States any property, real or personal, involved in such offense, or any property traceable to such property.” <span class="citation no-link">18 U. S. C. § 982</span>(a)(1).</blockquote>
<p id="b369-7">Respondent pleaded guilty to the failure to report in Count One; the Government agreed to dismiss the false statement charge in Count Two; and respondent elected to have a bench trial on the forfeiture in Count Three. After the bench trial, the District Court found that the entire $357,144 was subject to forfeiture because it was “involved <page-number citation-index="1" label="326">*326</page-number>in” the offense. <em><span class="citation no-link">Ibid.</span> </em>The court also found that the funds were not connected to any other crime and that respondent was transporting the money to repay a lawful debt. Tr. 61-62 (Jan. 19,1995). The District Court further found that respondent had failed to report that he was taking the currency out of the United States because of fear stemming from “cultural differences”: Respondent, who had grown up as a member of the Armenian minority in Syria, had a “distrust for the Government.” <span class="citation no-link"><em>Id., </em>at 63</span>; see Tr. of Oral Arg. 30.</p>
<p id="b370-5">Although § 982(a)(1) directs sentencing courts to impose full forfeiture, the District Court concluded that such forfeiture would be “extraordinarily harsh” and “grossly disproportionate to the offense in question,” and that it would therefore violate the Excessive Fines Clause. Tr. 63. The court instead ordered forfeiture of $15,000, in addition to a sentence of three years of probation and a fine of $5,000 — the maximum fine under the Sentencing Guidelines — because the court believed that the maximum Guidelines fine was “too little” and that a $15,000 forfeiture would “make up for what I think a reasonable fine should be.” <em>Ibid.</em></p>
<p id="b370-6">The United States appealed, seeking full forfeiture of respondent’s currency as provided in § 982(a)(1). The Court of Appeals for the Ninth Circuit affirmed. <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d 334</a></span> (1996). Applying Circuit precedent, the court held that, to satisfy the Excessive Fines Clause, a forfeiture must fulfill two conditions: The property forfeited must be an “instrumentality” of the crime committed, and the value of the property must be proportional to the culpability of the owner. <em><span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">Id.,</a></span> </em>at 336 (citing <em>United States </em>v. <em>Real Property Located in El Dorado County, </em><span class="citation" data-id="6935354"><a href="/opinion/7033061/united-states-v-real-property-located-in-el-dorado-county-at-6380-little/#982" aria-description="Citation for case: United States v. Real Property Located in El Dorado...">59 F. 3d 974, 982</a></span> (CA9 1995)). A majority of the panel determined that the currency was not an “instrumentality” of the crime of failure to report because “ ‘[t]he crime [in a currency reporting offense] is the withholding of information, . . . not the possession or the transportation of the money.’ ” <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d, at 337</a></span> (quoting <em>United States </em>v. <em>$69,292 </em><page-number citation-index="1" label="327">*327</page-number><em>in United States Currency, </em><span class="citation multiple-matches"><a href="/c/F.%203d/62/1161/">62 F. 3d 1161</a></span>, 1167 (CA9 1995)). The majority therefore held that § 982(a)(1) could never satisfy the Excessive Fines Clause in cases involving forfeitures of currency and that it was unnecessary to apply the “proportionality” prong of the test. Although the panel majority concluded that the Excessive Fines Clause did not permit forfeiture of <em>any </em>of the unreported currency, it held that it lacked jurisdiction to set the $15,000 forfeiture aside because respondent had not cross-appealed to challenge that forfeiture. <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#338" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d, at 338</a></span>.</p>
<p id="b371-6">Judge Wallace concurred in the result. He viewed respondent’s currency as an instrumentality of the crime because “without the currency, there can be no offense,” <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#339" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe..."><em>id., </em>at 339</a></span>, and he criticized the majority for “striking] down a portion of” the statute, <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#338" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe..."><em>id., </em>at 338</a></span>. He nonetheless agreed that full forfeiture would violate the Excessive Fines Clause in respondent’s case, based upon the “proportionality” prong of the Ninth Circuit test. Finding no clear error in the District Court’s factual findings, he concluded that the reduced forfeiture of $15,000 was proportional to respondent’s culpability. <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#339" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe..."><em>Id., </em>at 339-340</a></span>.</p>
<p id="b371-7">Because the Court of Appeals’ holding — that the forfeiture ordered by § 982(a)(1) was <em>per se </em>unconstitutional in cases of currency forfeiture — invalidated a portion of an Act of Congress, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./520/1239/">520 U. S. 1239</a></span> (1997).</p>
<p id="b371-8">hH h-4</p>
<p id="b371-3">The Eighth Amendment provides: “Excessive hail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.” U. S. Const., Arndt. 8. This Court has had little occasion to interpret, and has never actually applied, the Excessive Fines Clause. We have, however, explained that at the time the Constitution was adopted, “the word ‘fine’ was understood to mean a payment to a sovereign as punishment for some offense.” <em>Browning-Ferris Industries of Vt., Inc. </em>v. <em>Kelco Disposal, </em><page-number citation-index="1" label="328">*328</page-number><em>Inc., </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#265" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S. 257, 265</a></span> (1989). The Excessive Fines Clause thus “limits the government’s power to extract payments, whether in cash or in kind, ‘as punishment for some offense.’ ” <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#609" aria-description="Citation for case: Austin v. United States">509 U. S. 602, 609-610</a></span> (1998) (emphasis deleted). Forfeitures — payments in kind— are thus “fines” if they constitute punishment for an offense.</p>
<p id="b372-5">We have little trouble concluding that the forfeiture of currency ordered by § 982(a)(1) constitutes punishment. The statute directs a court to order forfeiture as an additional sanction when “imposing sentence on a person convicted of” a willful violation of §5316’s reporting requirement. The forfeiture is thus imposed at the culmination of a criminal proceeding and requires conviction of an underlying felony, and it cannot be imposed upon an innocent owner of unreported currency, but only upon a person who has himself been convicted of a §5316 reporting violation.<footnotemark>3</footnotemark> Cf. <em>id., </em>at 619 (holding forfeiture to be a “fine” in part because the forfeiture statute “expressly provide[d] an ‘innocent owner’ defense” and thus “look[ed] . .. like punishment”).</p>
<p id="b373-4"><page-number citation-index="1" label="329">*329</page-number>The United States argues, however, that the forfeiture of currency under § 982(a)(1) “also serves important remedial purposes.” Brief for United States 20. The Government asserts that it has “an overriding sovereign interest in controlling what property leaves and enters the country.” <em>Ibid. </em>It claims that full forfeiture of unreported currency supports that interest by serving to “dete[r] illicit movements of cash” and aiding in providing the Government with “valuable information to investigate and detect criminal activities associated with that cash.” <em>Id., </em>at 21. Deterrence, however, has traditionally been viewed as a goal of punishment, and forfeiture of the currency here does not serve the remedial purpose of compensating the Government for a loss. See Black’s Law Dictionary 1293 (6th ed. 1990) (“[R]emedial action” is one “brought to obtain compensation or indemnity”); <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232</a></span> (1972) <em>(per curiam) </em>(monetary penalty provides “a reasonable form of liquidated damages,” <span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States"><em>id., </em>at 237</a></span>, to the Government and is thus a “remedial” sanction because it compensates Government for lost revenues). Although the Government has asserted a loss of information regarding the amount of currency leaving the country, that loss would not be remedied by the Government’s confiscation of respondent’s $357,144.<footnotemark>4</footnotemark></p>
<p id="b373-5">The United States also argues that the forfeiture mandated by § 982(a)(1) is constitutional because it falls within a class of historic forfeitures of property tainted by crime. See Brief for United States 16 (citing, <em>inter alia, The Pal</em><page-number citation-index="1" label="330">*330</page-number><em>myra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#13" aria-description="Citation for case: The Palmyra">12 Wheat. 1, 13</a></span> (1827) (forfeiture of ship); <em>Dobbins’s Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#400" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395, 400-401</a></span> (1878) (forfeiture of distillery)). In so doing, the Government relies upon a series of cases involving traditional civil <em>in rem </em>forfeitures that are inapposite because such forfeitures were historically considered nonpunitive.</p>
<p id="b374-5">The theory behind such forfeitures was the fiction that the action was directed against “guilty property,” rather than against the offender himself.<footnotemark>5</footnotemark> See, <em>e. g., Various Items of Personal Property </em>v. <em>United States, </em><span class="citation" data-id="101673"><a href="/opinion/101673/various-items-of-personal-property-v-united-states/#581" aria-description="Citation for case: Various Items of Personal Property v. United States">282 U. S. 577, 581</a></span> (1931) (“[I]t is the property which is proceeded against, and, by resort to a legal fiction, held guilty and condemned as though it were conscious instead of inanimate and insentient”); see also R. Waples, Proceedings In Rem 13, 205-209 (1882). Historically, the conduct of the property owner was irrelevant; indeed, the owner of forfeited property could be entirely innocent of any crime. See, <em>e. g., Origet </em>v. <em>United States, </em><span class="citation" data-id="92190"><a href="/opinion/92190/origet-v-united-states/#246" aria-description="Citation for case: Origet v. United States">125 U. S. 240, 246</a></span> (1888) (“[T]he merchandise is to be forfeited irrespective of any criminal prosecution. . . . The person punished for the offence may be an entirely different person from the owner of the merchandise, or any person interested in it. The forfeiture of the goods of the principal can form no part of the personal punishment of his agent”). As Justice Story explained:</p>
<blockquote id="b374-6">“The thing is here primarily considered as the offender, or rather the offence is attached primarily to the thing; and this, whether the offence be <em>malum prohibitum, </em>or <page-number citation-index="1" label="331">*331</page-number><em>malum, in se. . . . </em>[T]he practice has been, and so this Court understand the law to be, that the proceeding <em>in rem </em>stands independent of, and wholly unaffected by any criminal proceeding <em>in personam” The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra">12 Wheat., at 14-15</a></span>.</blockquote>
<p id="b375-5">Traditional <em>in rem </em>forfeitures were thus not considered punishment against the individual for an offense. See <span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra"><em>id., </em>at 14</a></span>; <em>Dobbins’s Distillery </em>v. <em>United States, supra, </em>at 401; <em>Van Oster </em>v. <em>Kansas, </em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/#467" aria-description="Citation for case: Van Oster v. Kansas">272 U. S. 465, 467-468</a></span> (1926); <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#683" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663, 683-684</a></span> (1974); <em>Taylor </em>v. <em>United States, </em><span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/#210" aria-description="Citation for case: Taylor v. United States">3 How. 197, 210</a></span> (1845) (opinion of Story, J.) (laws providing for <em>in rem </em>forfeiture of goods imported in violation of customs laws, although in one sense “imposing a penalty or forfeiture[,] . . . truly deserve to be called, remedial”); see also <em>United States </em>v. <em>Ursery, </em><span class="citation" data-id="9433350"><a href="/opinion/118052/united-states-v-ursery/#293" aria-description="Citation for case: United States v. Ursery">518 U. S. 267, 293</a></span> (1996) (Kennedy, J., concurring) (“[Cjivil <em>in rem </em>forfeiture is not punishment of the wrongdoer for his criminal offense”). Because they were viewed as nonpunitive, such forfeitures traditionally were considered to occupy a place outside the domain of the Excessive Fines Clause. Recognizing the nonpunitive character of such proceedings, we have held that the Double Jeopardy Clause does not bar the institution of a civil, <em>in rem </em>forfeiture action after the criminal conviction of the defendant. See <span class="citation" data-id="9433350"><a href="/opinion/118052/united-states-v-ursery/#278" aria-description="Citation for case: United States v. Ursery"><em>id., </em>at 278</a></span>.<footnotemark>6</footnotemark></p>
<p id="b375-6">The forfeiture in this case does not bear any of the hallmarks of traditional civil <em>in rem </em>forfeitures. The Govern<page-number citation-index="1" label="332">*332</page-number>ment has not proceeded against the currency itself, but has instead sought and obtained a criminal conviction of respondent personally. The forfeiture serves no remedial purpose, is designed to punish the offender, and cannot be imposed upon innocent owners.</p>
<p id="b376-5">Section 982(a)(1) thus descends not from historic <em>in rem </em>forfeitures of guilty property, but from a different historical tradition: that of <em>in personam, </em>criminal forfeitures. Such forfeitures have historically been treated as punitive, being part of the punishment imposed for felonies and treason in the Middle Ages and at common law. See W. McKeehnie, Magna Carta 337-339 (2d ed. 1958); 2 F. Pollock &amp; F. Mait-land, The History of English Law 460-466 (2d ed. 1909). Although <em>in personam </em>criminal forfeitures were well established in England at the time of the founding, they were rejected altogether in the laws of this country until very recently.<footnotemark>7</footnotemark></p>
<p id="b377-4"><page-number citation-index="1" label="333">*333</page-number>The Government specifically contends that the forfeiture of respondent’s currency is constitutional because it involves an “instrumentality” of respondent’s crime.<footnotemark>8</footnotemark> According to the Government, the unreported cash is an instrumentality because it “does not merely facilitate a violation of law,” but is “ ‘the very <em>sine qua non </em>of the crime.’ ” Brief for United States 20 (quoting <em>United States </em>v. <em>United States Currency in the Amount of One Hundred Forty-Five Thousand, One Hundred Thirty-Nine Dollars, </em><span class="citation" data-id="6929952"><a href="/opinion/7028172/united-states-v-united-states-currency-in-the-amount-of-one-hundred/#75" aria-description="Citation for case: United States v. United States Currency in the Amount of...">18 F. 3d 73, 75</a></span> (CA2), cert. denied <em>sub nom. Etim </em>v. <em>United States, </em><span class="citation" data-id="9138302"><a href="/opinion/9143616/etim-v-united-states/" aria-description="Citation for case: Etim v. United States">513 U. S. 815</a></span> (1994)). The Government reasons that “there would be no violation at all without the exportation (or attempted exportation) of the cash.” Brief for United States 20.</p>
<p id="b377-5">Acceptance of the Government’s argument would require us to expand the traditional understanding of instrumentality forfeitures. This we decline to do. Instrumentalities historically have been treated as a form of “guilty property” that can be forfeited in civil <em>in rem </em>proceedings. In this ease, however, the Government has sought to punish respondent by proceeding against him criminally, <em>in personam, </em>rather than proceeding <em>in rem </em>against the currency. It is therefore irrelevant whether respondent’s currency is an instrumentality; the forfeiture is punitive, and the test for <page-number citation-index="1" label="334">*334</page-number>the excessiveness of a punitive forfeiture involves solely a proportionality determination. See <em>infra </em>this page and 335-337.<footnotemark>9</footnotemark></p>
<p id="b378-5">Ill</p>
<p id="b378-6">Because the forfeiture of respondent’s currency constitutes punishment and is thus a “fine” within the meaning of the Excessive Fines Clause, we now turn to the question whether it is “excessive.”</p>
<p id="b378-7">A</p>
<p id="b378-8">The touchstone of the constitutional inquiry under the Excessive Fines Clause is the principle of proportionality: The amount of the forfeiture must bear some relationship to the gravity of the offense that it is designed to punish. See <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#622" aria-description="Citation for case: Austin v. United States">509 U. S., at 622-623</a></span> (noting Court of Appeals’ statement that “ ‘the government is exacting too high a penalty in relation to the offense committed’ ”); <em>Alexander </em>v. <em>United States, </em><span class="citation" data-id="9432887"><a href="/opinion/112902/alexander-v-united-states/#559" aria-description="Citation for case: Alexander v. United States">509 U. S. 544, 559</a></span> (1993) (“It is in the light of the extensive criminal activities which petitioner apparently conducted ... that the question whether the forfeiture was ‘excessive’ must be considered”). Until today, however, we have not articulated a standard for determining whether a punitive forfeiture is constitutionally excessive. We now hold that a punitive forfeiture violates the Excessive Fines Clause if it is grossly disproportional to the gravity of a defendant’s offense.</p>
<p id="b379-4"><page-number citation-index="1" label="335">*335</page-number>The text and history of the Excessive Fines Clause demonstrate the centrality of proportionality to the excessiveness inquiry; nonetheless, they provide little guidance as to how disproportional a punitive forfeiture must be to the gravity of an offense in order to be “excessive.” Excessive means surpassing the usual, the proper, or a normal measure of proportion. See 1 N. Webster, American Dictionary of the English Language (1828) (defining excessive as “beyond the common measure or proportion”); S. Johnson, A Dictionary of the English Language 680 (4th ed. 1778) (“[bjeyond the common proportion”). The constitutional question that we address, however, is just how proportional to a criminal offense a fine must be, and the text of the Excessive Fines Clause does not answer it.</p>
<p id="b379-5">Nor does its history. The Clause was little discussed in the First Congress and the debates over the ratification of the Bill of Rights. As we have previously noted, the Clause was taken verbatim from the English Bill of Rights of 1689. See <em>Browning-Ferris Industries of Vt., Inc. </em>v. <em>Kelco Disposal, Inc., </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#266" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 266-267</a></span>. That document’s prohibition against excessive fines was a reaction to the abuses of the Ring’s judges during the reigns of the Stuarts, <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#267" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco..."><em>id., </em>at 267</a></span>, but the fines that those judges imposed were described contemporaneously only in the most general terms. See <em>Earl of Devonshire’s Case, </em>11 State Tr. 1367, 1372 (H. L. 1689) (fine of £30,000 “excessive and exorbitant, against Magna Charta, the common right of the subject, and the law of the land”). Similarly, Magna Charta — which the Stuart judges were accused of subverting — required only that amercements (the medieval predecessors of fines) should be proportioned to the offense and that they should not deprive a wrongdoer of his livelihood:</p>
<blockquote id="b379-6">“A Free-man shall not be amerced for a small fault, but after the manner of the fault; and for a great fault after the greatness thereof, saving to him his contenement; (2) and a Merchant likewise, saving to him his <page-number citation-index="1" label="336">*336</page-number>merchandise; (3) and any other’s villain than ours shall be likewise amerced, saving his wainage.” Magna Charta, 9 Hen. Ill, ch. 14 (1225), 1 Stat. at Large 6-7 (1762 ed.).</blockquote>
<p id="b380-5">None of these sources suggests how disproportional to the gravity of an offense a fine must be in order to be deemed constitutionally excessive.</p>
<p id="b380-6">We must therefore rely on other considerations in deriving a constitutional exeessiveness standard, and there are two that we find particularly relevant. The first, which we have emphasized in our cases interpreting the Cruel and Unusual Punishments Clause, is that judgments about the appropriate punishment for an offense belong in the first instance to the legislature. See, <em>e. g., Solem </em>v. <em>Helm, </em><span class="citation" data-id="9429310"><a href="/opinion/111000/solem-v-helm/#290" aria-description="Citation for case: Solem v. Helm">463 U. S. 277, 290</a></span> (1983) (“Reviewing courts . . . should grant substantial deference to the broad authority that legislatures necessarily possess in determining the types and limits of punishments for crimes”); see also <em>Gore </em>v. <em>United States, </em><span class="citation" data-id="9421677"><a href="/opinion/105742/gore-v-united-states/#393" aria-description="Citation for case: Gore v. United States">357 U. S. 386, 393</a></span> (1958) (“Whatever views may be entertained regarding severity of punishment,... these are peculiarly questions of legislative policy”). The second is that any judicial determination regarding the gravity of a particular criminal offense will be inherently imprecise. Both of these principles counsel against requiring strict proportionality between the amount of a punitive forfeiture and the gravity of a criminal offense, and we therefore adopt the standard of gross dispro-portionality articulated in our Cruel and Unusual Punishments Clause precedents. See, <em>e. g., Solem </em>v. <span class="citation" data-id="9429310"><a href="/opinion/111000/solem-v-helm/#288" aria-description="Citation for case: Solem v. Helm"><em>Helm, supra, </em>at 288</a></span>; <em>Rummel </em>v. <em>Estelle, </em><span class="citation" data-id="9427823"><a href="/opinion/110223/rummel-v-estelle/#271" aria-description="Citation for case: Rummel v. Estelle">445 U. S. 263, 271</a></span> (1980).</p>
<p id="b380-7">In applying this standard, the district courts in the first instance, and the courts of appeals, reviewing the proportionality determination <em>de </em>novo,<footnotemark>10</footnotemark> must compare the amount <page-number citation-index="1" label="337">*337</page-number>of the forfeiture to the gravity of the defendant’s offense. If the amount of the forfeiture is grossly disproportional to the gravity of the defendant’s offense, it is unconstitutional.</p>
<p id="b381-5">B</p>
<p id="b381-6">Under this standard, the forfeiture of respondent’s entire $357,144 would violate the Excessive Pines Clause.<footnotemark>11</footnotemark> Respondent’s crime was solely a reporting offense. It was permissible to transport the currency out of the country so long as he reported it. Section 982(a)(1) orders currency to be forfeited for a “willful” violation of the reporting requirement. Thus, the essence of respondent’s crime is a willful failure to report the removal of currency from the United States.<footnotemark>12</footnotemark> Furthermore, as the District Court found, re<page-number citation-index="1" label="338">*338</page-number>spondent’s violation was unrelated to any other illegal activities. The money was the proceeds of legal activity and was to be used to repay a lawful debt. Whatever his other vices, respondent does not fit into the class of persons for whom the statute was principally designed: He is not a money launderer, a drug trafficker, or a tax evader.<footnotemark>13</footnotemark> See Brief for United States 2-3. And under the Sentencing Guidelines, the maximum sentence that could have been imposed on respondent was six months, while the maximum fine was $5,000. App. to Pet. for Cert. 17a (transcript of District Court sentencing hearing); United States Sentencing Commission, Guidelines Manual §5(e)1.2, Sentencing Table <page-number citation-index="1" label="339">*339</page-number>(Nov. 1994). Such penalties confirm a minimal level of culpability.<footnotemark>14</footnotemark></p>
<p id="b383-5">The harm that respondent caused was also minimal. Failure to report his currency affected only one party, the Government, and in a relatively minor way. There was no fraud on the United States, and respondent caused no loss to the public fisc. Had his crime gone undetected, the Government would have been deprived only of the information that $357,144 had left the country. The Government and the dissent contend that there is a correlation between the amount forfeited and the harm that the Government would have suffered had the crime gone undetected. See Brief for United States 30 (forfeiture is “perfectly calibrated”); <em>post, </em>at 344 (“a fine calibrated with this accuracy”). We disagree. There is no inherent proportionality in such a forfeiture. It is impossible to conclude, for example, that the harm respondent caused is anywhere near 30 times greater than that caused by a hypothetical drug dealer who willfully fails to report taking $12,000 out of the country in order to purchase drugs.</p>
<p id="b383-6">Comparing the gravity of respondent’s crime with the $357,144 forfeiture the Government seeks, we conclude that such a forfeiture would be grossly disproportional to the <page-number citation-index="1" label="340">*340</page-number>gravity of his offense.<footnotemark>15</footnotemark> It is larger than the $5,000 fine imposed by the District Court by many orders of magnitude, and it bears no articulable correlation to any injury suffered by the Government.</p>
<p id="b384-5">C</p>
<p id="b384-6">Finally, we must reject the contention that the proportionality of full forfeiture is demonstrated by the fact that the First Congress enacted statutes requiring full forfeiture of goods involved in customs offenses or the payment of monetary penalties proportioned to the goods’ value. It is argued that the enactment of these statutes at roughly the same time that the Eighth Amendment was ratified suggests that full forfeiture, in the customs context at least, is a proportional punishment. The early customs statutes, however, do not support such a conclusion because, unlike § 982(a)(1), the type of forfeiture that they imposed was not considered punishment for a criminal offense.</p>
<p id="b384-7">Certain of the early customs statutes required the forfeiture of goods imported in violation of the customs laws, and, in some instances, the vessels carrying them as well. See, <em>e. g., </em>Act of Aug. 4, 1790, § 27, <span class="citation no-link">1 Stat. 163</span> (goods unladen without a permit from the collector). These forfeitures, however, were civil <em>in rent, </em>forfeitures, in which the Government proceeded against the property itself on the theory that it was guilty, not against a criminal defendant. See, <em>e. g., Harford </em>v. <em>United States, </em><span class="citation" data-id="85061"><a href="/opinion/85061/harford-v-united-states/" aria-description="Citation for case: Harford v. United States">8 Cranch 109</a></span> (1814) (goods unladen without a permit); <em>Locke </em>v. <em>United States, </em><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#340" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 340</a></span> (1813) (same). Such forfeitures sought to vindicate the Government’s underlying property right in customs duties, and like other traditional <em>in rem </em>forfeitures, they were not considered at the founding to be punishment for an offense. See <em>supra, </em>at 330-331. They therefore indicate <page-number citation-index="1" label="341">*341</page-number>nothing about the proportionality of the punitive forfeiture at issue here. See <em>supra, </em>at 330-332.<footnotemark>16</footnotemark></p>
<p id="b385-5">Other statutes, however, imposed monetary "forfeitures” proportioned to the value of the goods involved. See, <em>e, g., </em>Act of July 31, 1789, §22, <span class="citation no-link">1 Stat. 42</span> (if an importer, “with design to defraud the revenue,” did not invoice his goods at their actual cost at the place of export, “all such goods, wares or merchandise, or the value thereof... shall be forfeited”); §25, <em>id., </em>at 43 (any person concealing or purchasing goods, knowing they were liable to seizure for violation of the customs laws, was liable to “forfeit and pay a sum double the value of the goods so concealed or purchased”); see also Act of Aug. 4, 1790, §§10, 14, 22, <em>id., </em>at 156, 158, 161. Similar statutes were passed in later Congresses. See, <em>e. g., </em>Act of Mar. 2,1799, §§24, 28, 45, 46, 66, 69, 79, 84, <em>id., </em>at 646, 648, 661, 662, 677, 678, 687, 694; Act of Mar. 3,1823, ch. 58, §1, <span class="citation no-link">3 Stat. 781</span>.</p>
<p id="b385-6">These “forfeitures” were similarly not considered punishments for criminal offenses. This Court so recognized in <em>Stockwell </em>v. <em>United States, </em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/" aria-description="Citation for case: Stockwell v. United States">13 Wall. 531</a></span> (1871), a ease interpreting a statute that, like the Act of July 31,1789, provided that a person who had concealed goods liable to seizure for customs violations should “forfeit and pay a sum double the amount or value of the goods.” Act of Mar. 3, 1823, eh. 58, §2, <span class="citation no-link">3 Stat. 781</span>-782. The <em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/" aria-description="Citation for case: Stockwell v. United States">Stockwell</a></span> </em>Court rejected the de<page-number citation-index="1" label="342">*342</page-number>fendant’s contention that this provision was “penal,” stating instead that it was “fully as remedial in its character, designed as plainly to secure [the] rights [of the Government], as are the statutes rendering importers liable to duties.” <span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/#546" aria-description="Citation for case: Stockwell v. United States">13 Wall., at 546</a></span>. The Court reasoned:</p>
<blockquote id="b386-5">“When foreign merchandise, subject to duties, is imported into the country, the act of importation imposes on the importer the obligation to pay the legal charges. Besides this the goods themselves, if the duties be not paid, are subject to seizure .... Every act, therefore, which interferes with the right of the government to seize and appropriate the property which has been forfeited to it... is a wrong to property rights, and is a fit subject for indemnity.” <em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/" aria-description="Citation for case: Stockwell v. United States">Ibid.</a></span></em></blockquote>
<p id="b386-6">Significantly, the fact that the forfeiture was a multiple of the value of the goods did not alter the Court’s conclusion:</p>
<blockquote id="b386-7">“The act of abstracting goods illegally imported, receiving, concealing, or buying them, interposes difficulties in the way of a government seizure, and impairs, therefore, the value of the government right. It is, then, hardly accurate to say that the only loss the government can sustain from concealing the goods liable to seizure is their single value.... Double the value may not be more than complete indemnity.” <span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/#546" aria-description="Citation for case: Stockwell v. United States"><em>Id., </em>at 546-547</a></span>.</blockquote>
<p id="b386-8">The early monetary forfeitures, therefore, were considered not as punishment for an offense, but rather as serving the remedial purpose of reimbursing the Government for the losses accruing from the evasion of customs duties.<footnotemark>17</footnotemark> They <page-number citation-index="1" label="343">*343</page-number>were thus no different in purpose and effect than the <em>in rem </em>forfeitures of the goods to whose value they were proportioned.<footnotemark>18</footnotemark> Cf. <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S., at 237</a></span> (customs statute requiring the forfeiture of undeclared goods concealed in baggage and imposing a monetary penalty equal to the value of the goods imposed a “remedial, rather than [a] punitive sanctio[n]”).<footnotemark>19</footnotemark> By contrast, <page-number citation-index="1" label="344">*344</page-number>the full forfeiture mandated by § 982(a)(1) in this case serves no remedial purpose; it is clearly punishment. The customs statutes enacted by the First Congress, therefore, in no way suggest that § 982(a)(l)’s currency forfeiture is constitutionally proportional.</p>
<p id="b388-8">* * *</p>
<p id="b388-9">For the foregoing reasons, the full forfeiture of respondent’s currency would violate the Excessive Fines Clause. The judgment of the Court of Appeals is</p>
<p id="b388-10">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b369-8"> The statutory reporting requirement provides:</p>
<p id="b369-9">“[A] person or an agent or bailee of the person shall file a report... when the person, agent, or bailee knowingly—</p>
<p id="b369-10">“(1) transports, is about to transport, or has transported, monetary instruments of more than $10,000 at one time—</p>
<p id="b369-11">“(A) from a place in the United States to or through a place outside the United States ....” <span class="citation no-link">31 U. S. C. § 5316</span>(a).</p>
</footnote>
<footnote label="2">
<p id="b369-12"> Section 5322(a) provides: “A person willfully violating this subchapter ... shall be fined not more than $250,000, or imprisoned for not more than five years, or both.”</p>
</footnote>
<footnote label="3">
<p id="b372-6"> Although the currency reporting statute provides that “a person or an agent or bailee of the person shall file a report,” <span class="citation no-link">31 U. S. C. § 5316</span>(a), the statute ordering the criminal forfeiture of unreported currency provides that “[t]he court, in imposing sentence on a person convicted of” failure to file the required report, “shall order that the person forfeit to the United States” any property “involved in” or “traceable to” the offense, 18 U. S. G. § 982(a)(1). The combined effect of these two statutes is that an owner of unreported currency is not subject to criminal forfeiture if his agent or bailee is the one who fails to file the required report, because such an owner could not be convicted of the reporting offense. The United States endorsed this interpretation at oral argument in tins case. See Tr. of Oral Arg. 24-25.</p>
<p id="b372-7">For this reason, the dissent's speculation about the effect of today’s holding on “kingpins” and “cash couriers” is misplaced. See <em>post, </em>at 352, 354. Section 982(a)(l)’s criminal <em>in personam </em>forfeiture reaches only currency owned by someone who himself commits a reporting crime. It is unlikely that the Government, in the course of criminally indicting and prosecuting a cash courier, would not bother to investigate the source and true ownership of unreported funds.</p>
</footnote>
<footnote label="4">
<p id="b373-6"><em> </em>We do not suggest that merely because the forfeiture of respondent’s currency in this case would not serve a remedial purpose, other forfeitures may be classified as lionpunitive (and thus not “fines”) if they serve some remedial purpose as well as being punishment for an offense. Even if the Government were correct in claiming that the forfeiture of respondent’s currency is remedial in some way, the forfeiture would still be punitive in part. (The Government concedes ás much.) This is sufficient to bring the forfeiture within the purview of the Excessive Fines Glause. See <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#621" aria-description="Citation for case: Austin v. United States">509 U. S. 602, 621-622</a></span> (1993).</p>
</footnote>
<footnote label="5">
<p id="b374-7"> The “guilty property” theory behind <em>in rem </em>forfeiture can be traced to the Bible, which describes property being sacrificed to God as a means of atoning for an offense. See Exodus 21:28. In medieval Europe and at common law, this concept evolved into the law of deodand, in which offending property was condemned and confiscated by the church or the Crown in remediation for the harm it had caused. See 1 M. Hale, Pleas of the Crown 420-424 (1st Am. ed. 1847); 1 W. Blackstone, Commentaries on the Laws of England 290-292 (1765); O. Holmes, The Common Law 10-13, 23-27 (M. Howe ed. 1963).</p>
</footnote>
<footnote label="6">
<p id="b375-7"> It does not follow, of course, that all modem civil <em>in rem </em>forfeitures are nonpunitive and thus beyond the coverage of the Excessive Fines Clause. Because some recent federal forfeiture laws have blurred the traditional distinction between civil <em>in rem </em>and criminal <em>in -personam </em>forfeiture, we have held that a modern statutory forfeiture is a “fine” for Eighth Amendment purposes if it constitutes punishment even in part, regardless of whether the proceeding is styled <em>in rem </em>or <em>in personam. </em>See <em>Austin </em>v. <em>United States, supra, </em>at 621-622 (although labeled <em>in rem, </em>civil forfeiture of real property used “to facilitate” the commission of drug crimes was punitive in part and thus subject to review under the Excessive Fines Clause).</p>
</footnote>
<footnote label="7">
<p id="b376-6"> The First Congress explicitly rejected <em>in personam </em>forfeitures as punishments for federal crimes, see Act of Apr. 30, 1790, ch. 9, §24, <span class="citation no-link">1 Stat. 117</span> (“[NJo conviction or judgment.. . shall work corruption of blood, or any forfeiture of estate”), and Congress reenacted this ban several times over the course of two centuries. See Rev. Stat. § 5326 (1875); Act of Mar. 4, 1909, ch. 321, §341, <span class="citation no-link">35 Stat. 1159</span>; Act of June 25,1948, ch. 645, §3563, <span class="citation no-link">62 Stat. 837</span>, codified at <span class="citation no-link">18 U. S. C. § 3563</span> (1982 ed.); repealed effective Nov. 1,1987, <span class="citation no-link">Pub. L. 98-473, 98</span> Stat. 1987.</p>
<p id="b376-7">It was only in 1970 that Congress resurrected the English common law of punitive forfeiture to combat organized crime and major drug trafficking. See Organized Crime Control Act of 1970, <span class="citation no-link">18 U. S. C. § 1963</span>, and Comprehensive Drug Abuse Prevention and Control Act of 1970, <span class="citation no-link">21 U. S. C. § 848</span>(a). In providing for this mode of punishment, which had long been unused in this country, the Senate Judiciary Committee acknowledged that “criminal forfeiture... represents an innovative attempt to call on our common law heritage to meet an essentially modern problem.” S. Rep. No. 91-617, p. 79 (1969). Indeed, it was not until 1992 that Congress provided for the criminal forfeiture of currency at issue here. See <span class="citation no-link">18 U.S.C. § 982</span>(a).</p>
</footnote>
<footnote label="8">
<p id="b377-6"> Although the term “instrumentality” is of recent vintage, see <em>Austin </em>v. <em>United States, </em>509 U. S., at 627-628 (Scalia, J., concurring in part and concurring in judgment), it fairly characterizes property that historically was subject to forfeiture because it was the actual means by which an offense was committed. See <em>infra </em>this page; see, <em>e. g., J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#508" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S. 505, 508-510</a></span> (1921). “Instrumentality” forfeitures have historically been limited to the property actually used to commit an offense and no more. See <em>Austin </em>v. <em>United States, supra, </em>at 627-628 (Scalia, J., concurring in part and concurring in judgment). A forfeiture that reaches beyond this strict historical limitation is <em>ipso facto </em>punitive and therefore subject to review under the Excessive Fines Clause.</p>
</footnote>
<footnote label="9">
<p id="b378-9"> The currency in question is not an instrumentality in any event. The Court of Appeals reasoned that the existence of the currency as a “precondition” to the reporting requirement did not make it an “instrumentality” of the offense. See <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#337" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d 334, 337</a></span> (CA9 1996). We agree; the currency is merely the subject of the crime of failure to report. Cash in a suitcase does not facilitate the commission of that crime as, for example, an automobile facilitates the transportation of goods concealed to avoid taxes. See, <em>e. g., J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, supra, </em>at 508. In the latter instance, the property is the actual means by which the criminal act is committed. See Black’s Law Dictionary 801 (6th ed. 1990) (“Instrumentality” is “[slomething by which an end is achieved; a means, medium, agency”).</p>
</footnote>
<footnote label="10">
<p id="b380-8"> At oral argument, respondent urged that a district court’s determination of excessiveness should be reviewed by an appellate court for abuse of discretion. See Tr. of Oral Arg. 32. We cannot accept this submission. The factual findings made by the district courts in conducting the exces-<page-number citation-index="1" label="337">*337</page-number>siveness inquiry, of course, must be accepted unless dearly erroneous. See <em>Anderson </em>v. <em>Bessemer City, </em><span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#574" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U. S. 564, 574-575</a></span> (1985). But the question whether a fine is constitutionally excessive calls for the application of a constitutional standard to the facts of a particular ease, and in this context <em>de novo </em>review of that question is appropriate. See <em>Ornelas </em>v. <em>United States, </em><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#697" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 697</a></span> (1996).</p>
</footnote>
<footnote label="11">
<p id="b381-8"> The only question before this Court is whether the full forfeiture of respondent’s $357,144 as directed by § 982(a)(1) is constitutional under the Excessive Fines Clause. We hold that it is not. The Government petitioned for certiorari seeking full forfeiture, and we reject that request. Our holding that full forfeiture would be excessive reflects no judgment that "a forfeiture of even $15,001 would have suffered from a gross disproportion,” nor does it “affir[m] the reduced $15,000 forfeiture on <em>de novo </em>review.” <em>Post, </em>at 349. Those issues are simply not before us. Nor, indeed, do we address in <em>any </em>respect the validity of the forfeiture ordered by the District Court, including whether a court may disregard the terms of a statute that commands full forfeiture: As noted, <em>supra, </em>at 327, respondent did not cross-appeal the $15,000 forfeiture ordered by the District Court. The Court of Appeals thus declined to address the $15,000 forfeiture, and that question is not properly presented here either.</p>
</footnote>
<footnote label="12">
<p id="b381-9"> Contrary to the dissent’s contention, the nature of the nonreporting offense in this case was not altered by respondent’s “lies” or by the “suspicious circumstances” surrounding his transportation of his currency. See <em>post, </em>at 352-353. A single willful failure to declare the currency constitutes the crime, the gravity of which is not exacerbated or mitigated by <page-number citation-index="1" label="338">*338</page-number>‘Tablets]” that respondent told one month, or six months, later. See <em>post, </em>at 352. The Government indicted respondent under <span class="citation no-link">18 U. S. C. § 1001</span> for “lying,” but that separate count did not form the basis of the nonreporting offense for which § 982(a)(1) orders forfeiture.</p>
<p id="AQCi">Further, the District Court’s finding that respondent’s lies stemmed from a fear of the Government because of “cultural differences,” <em>supra, </em>at 326, does not mitigate the gravity of his offense. We reject the dissent’s contention that this finding was a “patronizing excuse” that “demeans millions of law-abiding American immigrants by suggesting they cannot be expected to be as truthful as every other citizen.” <em>Post, </em>at 353. We are confident that the District Court concurred in the dissent’s incontrovertible proposition that “[e]ach American, regardless of culture or ethnicity, is equal before the law.” <em>Ibid. </em>The District Court did nothing whatsoever to imply that “cultural differences” excuse lying, but rather made this finding in the context of establishing that respondent’s willful failure to report the currency was unrelated to any other crime — a finding highly relevant to the determination of the gravity of respondent’s offense. The dissent’s charge of ethnic paternalism on the part of the District Court finds no support in the record, nor is there any indication that the District Court’s factual finding that respondent “distrust[ed]... the Government,” see <em>supra, </em>at 326, was clearly erroneous.</p>
</footnote>
<footnote label="13">
<p id="b382-7"> Nor, contrary to the dissent’s repeated assertion, see <em>post, </em>at 344,346-351,354,356, is respondent a “smuggl[er].” Respondent owed no customs duties to the Government, and it was perfectly legal for him to possess the $357,144 in cash and to remove it from the United States. His crime was simply failing to report the wholly legal act of transporting his currency.</p>
</footnote>
<footnote label="14">
<p id="b383-7"> In considering an offense’s gravity, the other penalties that the Legislature has authorised are certainly relevant evidence. Here, as the Government and the dissent stress, Congress authorized a maximum fine of $250,000 plus five years’ imprisonment for willfully violating the statutory reporting requirement, and this suggests that it did not view the reporting offense as a trivial one. That the maximum fine and Guideline sentence to which respondent was subject were but a fraction of the penalties authorized, however, undercuts any argument based solely on the statute, because they show that respondent's culpability relative to other potential violators of the reporting provision — tax evaders, drug kingpins, or money launderers, for example — is small indeed. This disproportion is telling notwithstanding the fact that a separate Guideline provision permits forfeiture if mandated by statute, see <em>post, </em>at 350-351. That Guideline, moreover, cannot override the constitutional requirement of proportionality review.</p>
</footnote>
<footnote label="15">
<p id="b384-8"> Respondent does not argue that his wealth or income are relevant to the proportionality determination or that full forfeiture would deprive him of his livelihood, see <em>supra, </em>at 335-336, and -the District Court made no factual findings in this respect.</p>
</footnote>
<footnote label="16">
<p id="b385-7"> The nonpumtive nature of these early forfeitures was not lost on the Department of Justice, in commenting on the punitive forfeiture provisions of the Organized Crime Control Act of 1970:</p>
<p id="b385-8">‘“The concept of forfeiture as a criminal penalty which is embodied in this provision differs from other presently existing forfeiture provisions under Federal statutes where the proceeding is <em>in rem </em>against the property and the thing which is declared unlawful under the statute, or which is used for an unlawful purpose, or in connection with the prohibited property or transaction, is considered the offender, <em>and the forfeiture is no 'part of the punishment for the criminal offense. Examples of such forfeiture provisions are those contained in the customs, narcotics, and revenue laws.’” </em>S. Rep. No. 91-617, p. 79 (1969) (emphasis added).</p>
</footnote>
<footnote label="17">
<p id="b386-9"> In each of the statutes from the early Congresses cited by the dissent, the activities giving' rise to the monetary forfeitures, if undetected, were likely to cause the Government losses in customs revenue. The forfeiture imposed by the Acts of Aug. 4,1790, and Mar. 2,1799, was not simply for "transferring goods from one ship to another,” <em>post, </em>at 346, but rather for doing so “before such ship . . . shall come to the proper place for the discharge of her cargo . . . and be there duly authorized by the proper officer or officers of the customs to unlade” the goods, see <span class="citation no-link">1 Stat. 157</span>, <page-number citation-index="1" label="343">*343</page-number>158, 648, whereupon duties would be assessed. Similarly, the forfeiture imposed by the Act of Mar. 3, 1823, was for failing to deliver the ship’s manifest of cargo — which was to list “merchandise subject to duty” — to the collector of customs. See Act of Mar. 2,1821, §1, <span class="citation no-link">3 Stat. 616</span>; Act of Mar. 3,1823, §1, <em>id., </em>at 781. And the “invoices” that if “false” gave rise to the forfeiture imposed by the Act of Mar. 3,1863, were to include the value or quantity of any dutiable goods. § 1,<span class="citation no-link">12 Stat. 737</span>-738.</p>
</footnote>
<footnote label="18">
<p id="b387-6"> The nonpunitive nature of the monetary forfeitures was also reflected in their procedure: like traditional <em>in rem, </em>forfeitures, they were brought as civil actions, and as such are distinguishable from the punitive criminal fine at issue here. Instead of instituting an information of libel <em>in rem </em>against the goods, see, <em>e. g., Locke </em>v. <em>United States, </em><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">7 Cranch 339</a></span> (1813), the Government filed “a civil action of debt” against the person from whom it sought payment. See, <em>e. g., Stockwell </em>v. <em>United States, </em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/#541" aria-description="Citation for case: Stockwell v. United States">13 Wall. 531, 541-542</a></span> (1871). In both England and the United States, an action of debt was used to recover import duties owed the Government, being “the general remedy for the recovery of all sums certain, whether the legal liability arise from contract, or be created by a statute. And the remedy as well lies for the government itself, as for a citizen.” <em>United States </em>v. <em>Lyman, </em><span class="citation" data-id="8639012"><a href="/opinion/8659157/united-states-v-lyman/#1030" aria-description="Citation for case: United States v. Lyman">26 F. Cas. 1024, 1030</a></span> (No. 15,647) (CC Mass. 1818) (Story, C. J.). Thus suits for the payment of monetary forfeitures were viewed no differently than suits for the customs duties themselves.</p>
</footnote>
<footnote label="19">
<p id="b387-7"> <em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">One Lot Emerald Cut Stones</a></span> </em>differs from this case in the most fundamental respect. We concluded that the forfeiture provision in <em>Emerald Cut Stones </em>was entirely remedial and thus nonpunitive, primarily because it “provide[d] a reasonable form of liquidated damages” to the Government. <span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S., at 237</a></span>. The additional fact that such a remedial forfeiture also “selves to reimburse the Government for investigation and enforcement expenses,” <em>ibid.; </em>see <em>post, </em>at 346, is essentially meaningless, because even a clearly punitive criminal fine or forfeiture could be said in some measure to reimburse for criminal enforcement and investigation. Contrary to the dissent’s assertion, this certainly does not mean that the forfeiture in this case — which, as the dissent acknowledges, see <em>post, </em>at 344 (respondent’s forfeiture is a “fine”); <em>post, </em>at 353 (§ 982(a)(1) imposes a <page-number citation-index="1" label="344">*344</page-number>“punishment”), is dearly punitive — “would have to [be treated) as nonpu-nitive,” <em>post, </em>at 346.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Banks.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Banks"
type: case
citation: "540 U.S. 31 (2003)"
parallel_cite: "124 S. Ct. 521; 157 L. Ed. 2d 343"
neutral_cite: 2003 U.S. LEXIS 8966
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2003
date_decided: 2003-12-02
docket: 02-473
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2003-12-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Banks
  varies_by_point: false
  scope_note: "Controlling: in a felony drug case, a 15–20-second wait after knock-and-announce before forcible entry is reasonable where the exigency is imminent destruction of easily disposable evidence; reasonableness turns on the time to dispose of evidence, not travel time to the door."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131146/united-states-v-banks/"
  cluster_id: 131146
  opinion_id: 131146
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Progeny"
related: ["[[United States v. Ramirez]]", "[[Richards v. Wisconsin]]", "[[Wilson v. Arkansas]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "warrant-execution", "exigent-circumstances"]
holding: "A 15–20-second wait after knocking and announcing before forcing entry to execute a felony drug warrant is reasonable: when the exigency is the imminent destruction of easily disposable evidence, the relevant time is how long disposal would take, not how long the occupant needs to reach the door."
lake:
  record_id: United States v. Banks
  status: verified
  projected_at: 2026-07-06
---

# United States v. Banks

*540 U.S. 31 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
With a warrant to search Banks's two-bedroom apartment for cocaine, North Las Vegas police and FBI agents arrived about 2 p.m., called out "police search warrant," and knocked hard on the door. After waiting 15 to 20 seconds with no answer, they broke open the front door with a battering ram. Banks, in the shower, heard nothing until the crash. The search produced weapons, crack cocaine, and other drug-dealing evidence. Banks moved to suppress, arguing the officers waited an unreasonably short time before forcing entry.

## Issue
In executing a felony drug warrant, was the officers' 15-to-20-second wait after knocking and announcing, before forcibly entering, reasonable under the Fourth Amendment?

## Rule
Yes. Reasonableness depends on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] and the particular [[Exigent Circumstances and Hot Pursuit|exigency]] claimed. Where the [[Exigent Circumstances and Hot Pursuit|exigency]] is the imminent destruction of easily disposable drugs, "we think that after 15 or 20 seconds without a response, police could fairly suspect that cocaine would be gone if they were reticent any longer." — 540 U.S. at 38. ^pin-38

"[W]hen circumstances are exigent because a pusher may be near the point of putting his drugs beyond reach, it is imminent disposal, not travel time to the entrance, that governs when the police may reasonably enter." — *Id.* at 40. ^pin-40

"Once the exigency had matured . . . the officers were not bound to learn anything more or wait any longer before going in, even though their entry entailed some harm to the building." — *Id.* ^pin-40b

## Application
The police arrived in the afternoon, when occupants would likely be up and about, announced loudly, and waited 15 to 20 seconds — long enough for someone to begin flushing cocaine down a drain. The relevant question was the risk of imminent disposal, not whether Banks (who was actually in the shower and unheard-from) had time to reach the door; reasonableness is judged on the facts known to the officers. Because that disposal risk had matured by the end of the wait, the forcible entry was reasonable, and the resulting damage to the door did not change the analysis.

## Conclusion
The 15-to-20-second wait and forcible entry were reasonable under the Fourth Amendment; the judgment suppressing the evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Banks* remains the controlling treatment of how long officers must wait after [[Knock-and-Announce|knock-and-announce]] before forcing entry, applying a fact-specific [[Exigent Circumstances and Hot Pursuit|exigency]] analysis. It builds on [[Richards v. Wisconsin]] and [[Wilson v. Arkansas]] and pairs with [[United States v. Ramirez]] on property damage during forced entry. No negative treatment.

## Appears on
- [[Knock-and-Announce]] — *Progeny*

## Sources
- *United States v. Banks*, 540 U.S. 31 (2003) — https://www.courtlistener.com/opinion/131146/united-states-v-banks/ — pinpoints: 38, 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "413d24dd6aa3ef50", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Banks"}, "payload": {"all": [{"cite": "540 U.S. 31", "page": "31", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "540"}, {"cite": "124 S. Ct. 521", "page": "521", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "157 L. Ed. 2d 343", "page": "343", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "157"}, {"cite": "2003 U.S. LEXIS 8966", "page": "8966", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2003"}], "display": "540 U.S. 31", "official": {"cite": "540 U.S. 31", "page": "31", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "540"}, "official_selection_present": true, "record_id": "United States v. Banks"}}
{"assertion_id": "149751ffdd71752b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-38", "record_id": "United States v. Banks"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-38", "pinpoint_status": "slip-only", "quote": "and knocked hard on the door. After waiting 15 to 20 seconds with no answer, they broke open the front door with a battering ram. Banks, in the shower, heard nothing until the crash. The search produced weapons, crack cocaine, and other drug-dealing evidence. Banks moved to suppress, arguing the officers waited an unreasonably short time before forcing entry. ## Issue In executing a felony drug warrant, was the officers' 15-to-20-second wait after knocking and announcing, before forcibly entering, reasonable under the Fourth Amendment? ## Rule Yes. Reasonableness depends on the totality of the circumstances and the particular exigency claimed. Where the exigency is the imminent destruction of easily disposable drugs,", "quote_fidelity": "mismatch", "record_id": "United States v. Banks", "star_marker": null}}
{"assertion_id": "634ff1058507b47e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-40b", "record_id": "United States v. Banks"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-40b", "pinpoint_status": "slip-only", "quote": "Once the exigency had matured . . . the officers were not bound to learn anything more or wait any longer before going in, even though their entry entailed some harm to the building.", "quote_fidelity": "mismatch", "record_id": "United States v. Banks", "star_marker": null}}
{"assertion_id": "bf53755c293b24f6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-40", "record_id": "United States v. Banks"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-40", "pinpoint_status": "slip-only", "quote": "[W]hen circumstances are exigent because a pusher may be near the point of putting his drugs beyond reach, it is imminent disposal, not travel time to the entrance, that governs when the police may reasonably enter.", "quote_fidelity": "mismatch", "record_id": "United States v. Banks", "star_marker": null}}
{"assertion_id": "c9a5df3c2fa6aa26", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Banks"}, "payload": {"as_of_content": "2003-12-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Banks", "scope_note": "Controlling: in a felony drug case, a 15–20-second wait after knock-and-announce before forcible entry is reasonable where the exigency is imminent destruction of easily disposable evidence; reasonableness turns on the time to dispose of evidence, not travel time to the door.", "varies_by_point": false}}
```

### lake record — United States v. Banks

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Banks",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Banks",
    "case_name_short": "Banks",
    "case_name_full": "United States v. Banks",
    "input_case_name": "United States v. Banks",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2003-12-02",
    "year": 2003,
    "docket": "02-473",
    "cluster_id": 131146,
    "lead_opinion_id": 131146,
    "sibling_ids": [
      131146
    ],
    "absolute_url": "/opinion/131146/united-states-v-banks/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "540 U.S. 31",
      "volume": "540",
      "reporter": "U.S.",
      "page": "31",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 521",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "521",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 343",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2003 U.S. LEXIS 8966",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "8966",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 31",
        "volume": "540",
        "reporter": "U.S.",
        "page": "31",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 521",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "521",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 343",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2003 U.S. LEXIS 8966",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "8966",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "540 U.S. 31",
    "official_selection": {
      "court_class": "scotus",
      "selected": "540 U.S. 31",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-38",
      "page": null,
      "quote": "and knocked hard on the door. After waiting 15 to 20 seconds with no answer, they broke open the front door with a battering ram. Banks, in the shower, heard nothing until the crash. The search produced weapons, crack cocaine, and other drug-dealing evidence. Banks moved to suppress, arguing the officers waited an unreasonably short time before forcing entry. ## Issue In executing a felony drug warrant, was the officers' 15-to-20-second wait after knocking and announcing, before forcibly entering, reasonable under the Fourth Amendment? ## Rule Yes. Reasonableness depends on the totality of the circumstances and the particular exigency claimed. Where the exigency is the imminent destruction of easily disposable drugs,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-40",
      "page": null,
      "quote": "[W]hen circumstances are exigent because a pusher may be near the point of putting his drugs beyond reach, it is imminent disposal, not travel time to the entrance, that governs when the police may reasonably enter.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-40b",
      "page": null,
      "quote": "Once the exigency had matured . . . the officers were not bound to learn anything more or wait any longer before going in, even though their entry entailed some harm to the building.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2003-12-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Banks",
    "varies_by_point": false,
    "scope_note": "Controlling: in a felony drug case, a 15\u201320-second wait after knock-and-announce before forcible entry is reasonable where the exigency is imminent destruction of easily disposable evidence; reasonableness turns on the time to dispose of evidence, not travel time to the door.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Dennis Russell Callaghan",
          "cluster_id": 2933574,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Najar",
          "cluster_id": 167674,
          "cite": [
            "451 F.3d 710",
            "2006 U.S. App. LEXIS 15171",
            "2006 WL 1689231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Singleton",
          "cluster_id": 793669,
          "cite": [
            "441 F.3d 290",
            "2006 U.S. App. LEXIS 7201",
            "2006 WL 724800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1790339,
          "cite": [
            "177 S.W.3d 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jackie McCraven",
          "cluster_id": 789610,
          "cite": [
            "401 F.3d 693",
            "2005 U.S. App. LEXIS 4450",
            "2005 WL 608263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre J. Scroggins",
          "cluster_id": 785508,
          "cite": [
            "361 F.3d 1075",
            "2004 WL 574495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Joshua M. AARNESS",
          "cluster_id": 10014025,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 1539942,
          "cite": [
            "974 A.2d 1057",
            "200 N.J. 1",
            "2009 N.J. LEXIS 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Deep East Texas Regional Narcotics Trafficking Task Force",
          "cluster_id": 36001,
          "cite": [
            "379 F.3d 293",
            "2004 U.S. App. LEXIS 15493",
            "2004 WL 1662515"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terebesi v. Torreso",
          "cluster_id": 8441937,
          "cite": [
            "764 F.3d 217",
            "2014 U.S. App. LEXIS 16133",
            "2014 WL 4099309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aarness",
          "cluster_id": 2632419,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry J. Leaf, Individually and as Personal Representative of the Estate of John P. Leaf, Deceased, Martha A. Leaf, John P. Leaf v. Ronald Shelnutt",
          "cluster_id": 789551,
          "cite": [
            "400 F.3d 1070",
            "2005 U.S. App. LEXIS 4513",
            "2005 WL 628217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Bynum",
          "cluster_id": 785581,
          "cite": [
            "362 F.3d 574",
            "2004 U.S. App. LEXIS 5703",
            "2004 WL 595136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Snipe",
          "cluster_id": 1387263,
          "cite": [
            "515 F.3d 947",
            "2008 U.S. App. LEXIS 1794",
            "2008 WL 216996"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Estrada",
          "cluster_id": 8439099,
          "cite": [
            "430 F.3d 606"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ellen Storck v. City of Coral Springs",
          "cluster_id": 76396,
          "cite": [
            "354 F.3d 1307",
            "2003 U.S. App. LEXIS 26415",
            "2003 WL 23024573"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Wisconsin",
          "cluster_id": 4633470,
          "cite": [
            "588 U.S. 840",
            "139 S. Ct. 2525",
            "2019 U.S. LEXIS 4400"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Brown v. Battle Creek Police Dep't",
          "cluster_id": 4331219,
          "cite": [
            "844 F.3d 556",
            "2016 FED App. 0293P",
            "2016 U.S. App. LEXIS 22447",
            "2016 WL 7336612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McHugh",
          "cluster_id": 213881,
          "cite": [
            "639 F.3d 1250",
            "2011 U.S. App. LEXIS 6791",
            "2011 WL 1226486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Estrada",
          "cluster_id": 792578,
          "cite": [
            "430 F.3d 606",
            "2005 U.S. App. LEXIS 25680"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lynch Ex Rel. Lynch v. City of Mount Vernon",
          "cluster_id": 1454597,
          "cite": [
            "567 F. Supp. 2d 459",
            "2008 U.S. Dist. LEXIS 47137",
            "2008 WL 2885118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lopez",
          "cluster_id": 2566898,
          "cite": [
            "116 P.3d 80",
            "138 N.M. 9",
            "2005 NMSC 018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Vargas",
          "cluster_id": 2634395,
          "cite": [
            "181 P.3d 684",
            "143 N.M. 692",
            "2008 NMSC 019"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matylinsky v. Budge",
          "cluster_id": 1232674,
          "cite": [
            "577 F.3d 1083",
            "2009 U.S. App. LEXIS 18414",
            "2009 WL 2501932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark D. Jones and Theresa A. Jones v. Ron Wilhelm, Cross-Appellee",
          "cluster_id": 792109,
          "cite": [
            "425 F.3d 455",
            "2005 U.S. App. LEXIS 21386",
            "2005 WL 2417087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvador Martinez-Garcia",
          "cluster_id": 789239,
          "cite": [
            "397 F.3d 1205",
            "2005 U.S. App. LEXIS 2236",
            "2005 WL 326844"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131146) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 150,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 7,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 150,
        "triage_read": 8,
        "triage_snippet_classified": 142
      },
      "lane2_top_cited": {
        "query": "cites:(131146)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00OCZzPTIxNjE2OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28131146%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131146)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 0,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(131146)",
    "indexed_citing_opinions": 212,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131146,
        "count": 212,
        "count_source": "search"
      }
    ],
    "citation_count": 343,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-banks.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MjI2ODYmcz00NzE0MTY4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28131146%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131146,
        "cited_id": 13843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 157939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 499820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 510300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 598972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 609715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 655530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 758684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 760850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 776811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 779415,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T22:29:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:35:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Banks

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b245-8">
<span citation-index="1" class="star-pagination" label="33"> 
   *33
   </span>
  Justice Souter
 </author>
<p id="Ac">
  delivered the opinion of the Court.
 </p>
<p id="b245-9">
  Officers executing a warrant to search for cocaine in respondent Banks’s apartment knocked and announced their authority. The question is whether their 15-to-20-second wait before a forcible entry satisfied the Fourth Amendment and <span class="citation no-link">18 U. S. C. §3109</span>. We hold that it did.
 </p>
<p id="Af_A">
  I
 </p>
<p id="pAKR">
  With information that Banks was selling cocaine at home, North Las Vegas Police Department officers and Federal Bureau of Investigation agents got a warrant to search his two-bedroom apartment. As soon as they arrived there, about 2 o’clock on a Wednesday afternoon, officers posted in front called out “police search warrant” and rapped hard enough on the door to be heard by officers at the back door. Brief for United States 3 (internal quotation marks omitted). There was no indication whether anyone was home, and after waiting for 15 to 20 seconds with no answer, the officers broke open the front door with a battering ram. Banks was in the shower and testified that he heard nothing until the crash of the door, which brought him out dripping to confront the police. The search produced weapons, crack cocaine, and other evidence of drug dealing.
 </p>
<p id="b245-4">
  In response to drug and firearms
  <em>
   charges, Banks moved to
  </em>
  suppress evidence, arguing that the officers executing the search warrant waited an unreasonably short time before forcing entry, and so violated both the Fourth Amendment and <span class="citation no-link">18 U. S. C. § 3109</span>.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The District Court denied the motion, and Banks pleaded guilty, reserving his right to challenge the search on appeal.
 </p>
<p id="b246-3">
<span citation-index="1" class="star-pagination" label="34"> 
   *34
   </span>
  A divided panel of the Ninth Circuit reversed and ordered suppression of the evidence found. <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d 699</a></span> (2002). In assessing the reasonableness of the execution of the warrant, the panel majority set out a nonexhaustive list of “factors that an officer reasonably should consider” in deciding when to enter premises identified in a warrant, after knocking and announcing their presence but receiving no express acknowledgment:
 </p>
<blockquote id="b246-4">
  “(a) size of the residence; (b) location of the residence; (c) location of the officers in relation to the main living or sleeping areas of the residence; (d) time of day; (e) nature of the suspected offense; (f) evidence demonstrating the suspect's guilt; (g) suspect’s prior convictions and, if any, the type of offense for which he was convicted; and (h) any other observations triggering the senses of the officers that reasonably would lead one to believe that immediate entry was necessary.”
  <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#704" aria-description="Citation for case: United States v. Lashawn Lowell Banks"><em>
   Id.,
  </em>
  at 704</a></span>.
 </blockquote>
<p id="b246-5">
  The majority also defined four categories of intrusion after knock and announcement, saying that the classification “aids in the resolution of the essential question whether the entry made herein was reasonable under the circumstances”:
 </p>
<blockquote id="b246-6">
  “(1) entries in which exigent circumstances exist and non-forcible entry is possible, permitting entry to be made simultaneously with or shortly after announcement; (2) entries in which exigent circumstances exist and forced entry by destruction of property is required, necessitating more specific inferences of exigency; (3) entries in which no exigent circumstances exist and non-forcible entry is possible, requiring an explicit refusal of admittance or a lapse of a significant amount of time; and (4) entries in which no exigent circumstances exist and forced entry by destruction of property is required, mandating an explicit refusal of admittance or a
  <span citation-index="1" class="star-pagination" label="35"> 
   *35
   </span>
  lapse of an even more substantial amount of time.”
  <em>
   <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/" aria-description="Citation for case: United States v. Lashawn Lowell Banks">Ibid.</a></span>
  </em>
</blockquote>
<p id="b247-7">
  The panel majority put the action of the officers here in the last category, on the understanding that they destroyed the door without hearing anything to suggest a refusal to admit even though sound traveled easily through the small apartment. The majority held the 15-to-20-second delay after knocking and announcing to be “[insufficient ... to satisfy the constitutional safeguards.”
  <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#705" aria-description="Citation for case: United States v. Lashawn Lowell Banks"><em>
   Id.,
  </em>
  at 705</a></span>.
 </p>
<p id="b247-8">
  Judge Fisher dissented, saying that the majority ought to come out the other way based on the very grounds it stressed: Banks’s small apartment, the loud knock and announcement, the suspected offense of dealing in cocaine, and the time of the day. Judge Fisher thought the lapse of 15 to 20 seconds was enough to support a reasonable inference that admittance had been constructively denied.
  <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#710" aria-description="Citation for case: United States v. Lashawn Lowell Banks"><em>
   Id.,
  </em>
  at 710</a></span>.
 </p>
<p id="b247-9">
  We granted certiorari to consider how to go about applying the standard of reasonableness to the length of time police with a warrant must wait before entering without permission after knocking and announcing their intent in a felony case. <span class="citation multiple-matches"><a href="/c/U.%20S./537/1187/">537 U. S. 1187</a></span> (2003). We now reverse.
 </p>
<p id="AQH">
  II.
 </p>
<p id="pAPl">
  There has never been a dispute that these officers were obliged
  <em>
   to knock and announce their intentions
  </em>
  when
  <em>
   executing
  </em>
  the search warrant, an obligation they concededly honored. Despite this agreement, we start with a word about standards for requiring or dispensing with a knock and announcement, since the same criteria bear on when the officers could legitimately enter after knocking.
 </p>
<p id="b247-4">
  The Fourth Amendment says nothing specific about formalities in exercising a warrant’s authorization, speaking to the manner of searching as well as to the legitimacy of searching at all simply in terms of the right to be “secure . . . against unreasonable searches and seizures.” Although the notion of reasonable execution must therefore be fleshed
  <span citation-index="1" class="star-pagination" label="36"> 
   *36
   </span>
  out, we have done that case by case, largely avoiding categories and protocols for searches. Instead, we have treated reasonableness as a function of the facts of cases so various that no template is likely to produce sounder results than examining the totality of circumstances in a given case; it is too hard to invent categories without giving short shrift to details that turn out to be important in a given instance, and without inflating marginal ones. See,
  <em>
   e. g., Ohio
  </em>
  v.
  <em>
   Robinette,
  </em>
  <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39</a></span> (1996) (“[W]e have consistently eschewed bright-line rules, instead emphasizing the fact-specific nature of the reasonableness inquiry”);
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California">374 U. S. 23, 33</a></span> (1963) (reasonableness not susceptible to Procrustean application);
  <em>
   Go-Bart Importing Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#357" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 357</a></span> (1931) (no formula for determining reasonableness; each case on its own facts and circumstances). We have, however, pointed out factual considerations of unusual, albeit not dispositive, significance.
 </p>
<p id="b248-5">
  In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we held that the common law knock-and-announce principle is one focus of the reasonableness enquiry; and we subsequently decided that although the standard generally requires the police to announce their intent to search before entering closed premises, the obligation gives way when officers “have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or . . . would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence,”
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 394</a></span> (1997). When a warrant applicant gives reasonable grounds to expect futility or to suspect that one or another such exigency already exists or will arise instantly upon knocking, a magistrate judge is acting within the Constitution to authorize a “no-knock” entry.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  And even when executing a warrant silent about
  <span citation-index="1" class="star-pagination" label="37"> 
   *37
   </span>
  that, if circumstances support a reasonable suspicion of exigency when the officers arrive at the door, they may go straight in.
  <em>
   Id,.,
  </em>
  at 394, 396, n. 7.
 </p>
<p id="b249-5">
  Since most people keep their doors locked, entering without knocking will normally do some damage, a circumstance too common to require a heightened justification when a reasonable suspicion of exigency already justifies an unwarned entry. We have accordingly held that police in exigent circumstances may damage premises so far as necessary for a no-knock entrance without demonstrating the. suspected risk in any more detail than the law demands for an unannounced intrusion simply by lifting the latch.
  <em>
   United States
  </em>
  v.
  <em>
   Ramirez, 523
  </em>
  U. S. 65, 70-71 (1998). Either way, it is enough that the officers had a reasonable suspicion of exigent circumstances.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b249-6">
  Ill
 </p>
<p id="b249-7">
  Like
  <em>
   Ramirez,
  </em>
  this case turns on the significance of exigency revealed by circumstances known to the officers, for the only substantive difference between the two situations goes to the time at which the officers reasonably anticipated some danger calling for action without delay.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Whereas the
  <span citation-index="1" class="star-pagination" label="38"> 
   *38
   </span>
<em>
   Ramirez
  </em>
  Magistrate Judge found in advance that the customary warning would raise an immediate risk that a wanted felon would elude capture or pose a threat to the officers, see
  <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#68" aria-description="Citation for case: United States v. Ramirez"><em>
   id.,
  </em>
  at 68</a></span>, here the Government claims that a risk of losing. . evidence arose shortly after knocking and announcing. Although the police concededly arrived at Banks’s door without reasonable suspicion of facts justifying a no-knock entry, they argue that announcing their presence started the clock running toward the moment of apprehension that Banks would flush away the easily disposable cocaine, prompted by knowing the police would soon be coming in. While it was held reasonable for the police in
  <em>
   Ramirez
  </em>
  tó enter forcibly upon arrival, the Government argues it was equally reasonable for the officers to go in with force here as soon as the danger of disposal had ripened.
 </p>
<p id="b250-5">
  Banks does not, of course, deny that exigency may develop in the period beginning when officers with a warrant knock to be admitted, and the issue comes down to whether it was reasonable to suspect imminent loss of evidence after the 15 to 20 seconds the officers waited prior to forcing their way. Though we agree with Judge Fisher’s dissenting opinion that this call is a close one, <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#707" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d, at 707</a></span>, we think that after 15 or 20 seconds without a response, police could fairly suspect that cocaine would be gone if they were reticent any longer. Courts of Appeals have, indeed, routinely held similar wait times to be reasonable in drug cases with similar facts including easily disposable evidence (and some courts have found even shorter ones to be reasonable enough).
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b251-4">
<span citation-index="1" class="star-pagination" label="39"> 
   *39
   </span>
  A look at Banks’s counterarguments shows why these courts reached sensible results, for each of his reasons for saying that 15 to 20 seconds was too brief rests on a mistake about the relevant enquiry: the fact that he was actually in the shower and did not hear the officers is not to the point, and the same is true of the claim that it might have taken him longer than 20 seconds if he had heard the knock and headed straight for the door. As for the shower, it is enough to say that the facts known to the police are what count in judging reasonable waiting time, cf.,
  <em>
   e. g., Graham
  </em>
  v.
  <em>
   Connor,
  </em>
  <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 396</a></span> (1989) (“The ‘reasonableness’ of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight”), and there is no indication that the police knew that Banks was in the shower and thus unaware of an impending search that he would otherwise have tried to frustrate.
 </p>
<p id="b251-5">
  And the argument that 15 to 20 seconds was too short for Banks to have come to the door ignores the very risk that justified prompt entry. True, if the officers were to justify their timing here by claiming that Banks’s failure to admit them fairly suggested a refusal to let them in, Banks could at least argue that no such suspicion can arise until an occu
  <span citation-index="1" class="star-pagination" label="40"> 
   *40
   </span>
  pant has had time to get to the door,
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  a time that will vary with the size of the establishment, perhaps five seconds to open a motel room door, or several minutes to move through a townhouse. In this case, however, the police claim exigent need to enter, and the crucial fact in examining their actions is not time to reach the door but the particular exigency claimed. On the record here, what matters is the opportunity to get rid of cocaine, which a prudent dealer will keep near a commode or kitchen sink. The significant circumstances include the arrival of the police during the day, when anyone inside would probably have been up and around, and the sufficiency of 15 to 20 seconds for getting to the bathroom or the kitchen to start flushing cocaine down the drain. That is, when circumstances are exigent because a pusher may be near the point of putting his drugs beyond reach, it is imminent disposal, not travel time to the entrance, that governs when the police may reasonably enter; since the bathroom and kitchen are usually in the interior of a dwelling, not the front hall, there is no reason generally to peg the travel time to the location of the door, and no reliable basis for giving the proprietor of a mansion a longer wait than the resident of a bungalow, or an apartment like Banks’s. And 15 to 20 seconds does not seem an unrealistic guess about the time someone would need to get in a position to rid his quarters of cocaine.
 </p>
<p id="b252-5">
  Once thé exigency had matured, of course, the officers were not bound to learn anything more or wait any longer before going in, even though their entry entailed some harm to the building.
  <em>
   Ramirez
  </em>
  held that the exigent need of law enforcement trumps a resident’s interest in avoiding all property damage, see <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#70" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 70-71</a></span>, and there is no reason to treat a post-knock exigency differently from the no-knock counterpart in
  <em>
   Ramirez
  </em>
  itself.
 </p>
<p id="b253-7">
<span citation-index="1" class="star-pagination" label="41"> 
   *41
   </span>
  I
  <em>
   V
  </em>
</p>
<p id="b253-3">
  Our emphasis on totality analysis necessarily rejects positions taken on each side of this case.
  <em>
   Ramirez,
  </em>
  for example, cannot be read with the breadth the Government espouses, as “reflectfing] a general principle that the need to damage property in order to effectuate an entry to execute a search warrant should not be part of the analysis of whether the entry itself was reasonable.” Brief for United States 18; Reply Brief for United States 4. At common law, the knock-and-announce rule was traditionally “justified in part by the belief that announcement generally would avoid ‘the destruction or breaking of any house ... by which great damage and inconvenience might ensue.’”
  <em>
   Wilson,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 935</a></span>-936 (quoting
  <em>
   Semayne’s Case,
  </em>
  5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194, 196 (K. B. 1603)). One point in making an officer knock and announce, then, is to give a person inside the chance to save his door. That is why, in the case with no reason to suspect an immediate risk of frustration or futility in waiting at all, the reasonable wait time may well be longer when police make a forced entry, since they ought to be more certain the occupant has had time to answer the door. It is hard to be more definite than that, without turning the notion of a reasonable time under all the . circumstances into a set of sub-rules as the Ninth Circuit has been inclined to do. Suffice it to say that the need to damage property in the course of getting in is a good reason to require more patience than it would be reasonable to expect if the door were open. Police seeking a stolen piano may be able to spend more time to make sure they really need the battering ram.
 </p>
<p id="b253-4">
  On the other side, we disapprove of the Court of Appeals’s four-part scheme for vetting knock-and-announce entries. To begin with, the demand for enhanced evidence of exigency before a door can reasonably be damaged by a warranted no-knock intrusion was already bad law before the Court of Appeals decided this case. In
  <em>
   Ramirez
  </em>
  (a case from the
  <span citation-index="1" class="star-pagination" label="42"> 
   *42
   </span>
  Ninth Circuit), we rejected an attempt to subdivide felony-cases by accepting “mild exigency” for entry without property damage, but requiring “more specific inferences of exigency” before damage would be reasonable. <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#69" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 69-71</a></span> (internal quotation marks omitted). The Court of Appeals did not cite
  <em>
   Ramirez.
  </em>
</p>
<p id="b254-5">
  Nor did the appeals court cite
  <em>
   United States
  </em>
  v.
  <em>
   Arvizu,
  </em>
  <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">534 U. S. 266</a></span> (2002) (again, from the Ninth Circuit). There, we recently disapproved a framework for making reasonable suspicion determinations that attempted to reduce what the Circuit described as “troubling . . . uncertainty” in reasonableness analysis, by “describing] and clearly delimiting]” an officer’s consideration of certain factors.
  <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/#272" aria-description="Citation for case: United States v. Arvizu"><em>
   Id.,
  </em>
  at 272, 275</a></span> (internal quotation marks omitted). Here, as in
  <em>
   <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">Arvizu</a></span>,
  </em>
  the Court of Appeals’s overlay of a categorical scheme on the general reasonableness analysis threatens to distort the “totality of the circumstances” principle, by replacing a stress on revealing facts with resort to pigeonholes.
  <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/#274" aria-description="Citation for case: United States v. Arvizu"><em>
   Id.,
  </em>
  at 274</a></span> (internal quotation marks omitted). Attention to cocaine rocks and pianos tells a lot about the chances of their respective disposal and its bearing on reasonable time. Instructions couched in terms like “significant amount of time,” and “an even more substantial amount of time,” <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#704" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d, at 704</a></span>, tell very little.
 </p>
<p id="b254-6">
  V
 </p>
<p id="b254-7">
  Last, there is Banks’s claim that the entry violated <span class="citation no-link">18 U. S. C. § 3109</span>.
  <em>
   Ramirez
  </em>
  held that the result should be the same under the Fourth Amendment and §3109, permitting an officer to enter by force “if, after notice of his authority and purpose, he is refused admittance.” We explained the statute’s “‘requirement of prior notice . . . before forcing entry . . . [as] codiffying] a tradition embedded in Anglo-American law,’ ” <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 72</a></span> (quoting
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958)); see also
  <em>
   Sabbath
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/#591" aria-description="Citation for case: Sabbath v. United States">391 U. S. 585, 591, n. 8</a></span> (1968), and we held that § 3109 implicates the exceptions to the common law knock-and-
  <span citation-index="1" class="star-pagination" label="43"> 
   *43
   </span>
  announce requirement that inform the Fourth Amendment itself, <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#73" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 73</a></span>. The upshot is that § 3109 is subject to an exigent circumstances exception,
  <em>
   ibid.,
  </em>
  which qualifies the requirement of refusal after notice, just as it qualifies the obligation to announce in the first place. Absent exigency, the police must knock and receive an actual refusal or wait out the time necessary to infer one. But in a case like this, where the officers knocked and announced their presence, and forcibly entered after a reasonable suspicion of exigency had ripened, their entry satisfied § 3109 as well as the Fourth Amendment, even without refusal of admittance.
 </p>
<p id="b255-5">
  The judgment of the Court of Appeals is reversed.
 </p>
<p id="b255-6">
<em>
   So ordered.
  </em>
</p>






<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b245-6">
   The statute provides: “The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance or when necessary to liberate himself or a person aiding him in the execution of the warrant.”
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b248-6">
   Some States give magistrate judges the authority to issue “no-knock” warrants, and some do not. See,
   <em>
    e. g., Richards
   </em>
   v.
   <em>
    Wisconsin,
   </em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#396" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 396, n. 7</a></span> (1997) (collecting state statutes and cases).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b249-8">
   The standard for a no-knock entry stated in
   <em>
    <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>
   </em>
   applies on reasonable suspicion of exigency or futility. Because the facts here go to exigency, not futility, we speak of that alone.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b249-9">
<em>
    Ramirez
   </em>
   and
   <em>
    Richards
   </em>
   v.
   <em>
    Wisconsin,
   </em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U.S. 385</a></span> (1997), our cases addressing the role of exigency in assessing the reasonableness' of a no-knock entry, involved searches by warrant for evidence of a felony, as does this case. In a different context governed by the Fourth Amendment, we have held that the risk of losing evidence of a minor offense is insufficient to make it reasonable to enter a dwelling to make a warrantless arrest. See
   <em>
    Welsh
   </em>
   v.
   <em>
    Wisconsin,
   </em>
   <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984). Courts of Appeals have applied
   <em>
    Welsh
   </em>
   to warrantless entries simply to search for evidence, considering the gravity of the offense in determining whether exigent circumstances exist. See,
   <em>
    e. g., United States
   </em>
   v.
   <em>
    Aquino,
   </em>
   <span class="citation" data-id="499820"><a href="/opinion/499820/united-states-v-luis-raul-aquino/#1271" aria-description="Citation for case: United States v. Luis Raul Aquino">836 F. 2d 1268, 1271-1273</a></span> (CA10 1988);
   <em>
    United States
   </em>
   v.
   <em>
    Clement,
   </em>
   <span class="citation" data-id="9478056"><a href="/opinion/510300/united-states-v-kenneth-clement/#1120" aria-description="Citation for case: United States v. Kenneth Clement">854 F. 2d 1116, 1120</a></span> (CA8 1988)
   <em>
    (per curiam).
   </em>
   We intimate nothing here about such warrantless entry cases. Nor do we express a view on the significance of the existence of a warrant in evaluating whether exigency justifies action in
   <span citation-index="1" class="star-pagination" label="38"> 
    *38
    </span>
   knock-and-armounce cases when the reason for the search is a minor offense.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b250-8">
   Several Courts of Appeals have explicitly taken into account the risk of disposal of drug evidence as a factor in evaluating the reasonableness of waiting time. See,
   <em>
    e. g., United States
   </em>
   v.
   <em>
    Goodson,
   </em>
   <span class="citation" data-id="760850"><a href="/opinion/760850/united-states-v-terrence-eugene-goodson/#612" aria-description="Citation for case: United States v. Terrence Eugene Goodson">165 F. 3d 610, 612, 614</a></span> (CA8 1999) (holding a 20-second wait after a loud announcement at a one-story ranch reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Spikes,
   </em>
   <span class="citation" data-id="758684"><a href="/opinion/758684/united-states-v-james-h-spikes-96-3899-marilyn-smith-96-3660/#925" aria-description="Citation for case: United States v. James H. Spikes (96-3899) Marilyn Smith...">158 F. 3d 913, 925-927</a></span> (CA6 1998) (holding a 15-to-30-second wait in midmorning after a loud announcement reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Spriggs,
   </em>
   <span class="citation" data-id="609715"><a href="/opinion/609715/united-states-v-terrance-kevin-spriggs-aka-bob/" aria-description="Citation for case: United States v. Terrance Kevin Spriggs, A/K/A Bob">996 F. 2d 320</a></span>, 322-
   <span citation-index="1" class="star-pagination" label="39"> 
    *39
    </span>
   323 (CADC 1993) (holding a 15-second wait after a reasonably audible
   <em>
    announcement at
   </em>
   7:45
   <em>
    a.m. on a weekday reasonable); United States v. Garcia,
   </em>
   <span class="citation" data-id="598972"><a href="/opinion/598972/united-states-v-jose-a-garcia-united-states-v-pablo-h-garcia/#1168" aria-description="Citation for case: United States v. Jose A. Garcia, United States v. Pablo...">983 F. 2d 1160, 1168</a></span> (CA1 1993) (holding a 10-second wait after a loud announcement reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Jones,
   </em>
   <span class="citation" data-id="13843"><a href="/opinion/13843/united-states-v-jones/#361" aria-description="Citation for case: United States v. Jones">133 F. 3d 358, 361-362</a></span> (CA5 1998)
   <em>
    (per curiam,)
   </em>
   (relying specifically on the concept of exigency, holding a 15-to-20-second wait reasonable). See also
   <em>
    United States
   </em>
   v.
   <em>
    Chavez-Miranda,
   </em>
   <span class="citation" data-id="779415"><a href="/opinion/779415/united-states-v-tomas-chavez-miranda/#981" aria-description="Citation for case: United States v. Tomas Chavez-Miranda">306 F. 3d 973, 981-982, n. 7</a></span> (CA9 2002)
   <em>
    (“Banks
   </em>
   appears to be a departure from our prior decisions. . . . [W]e have found a 10 to 20 second wait to be reasonable in similar circumstances, albeit when the police heard sounds after the knock and announcement”);
   <em>
    United States
   </em>
   v.
   <em>
    Jenkins,
   </em>
   175 F 3d 1208, 1215 (CA10 1999) (holding a 14-to-20-second wait at 10 am. reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Markling,
   </em>
   <span class="citation" data-id="655530"><a href="/opinion/655530/united-states-v-timothy-w-markling/#1318" aria-description="Citation for case: United States v. Timothy W. Markling">7 F. 3d 1309, 1318-1319</a></span> (CA7 1993) (holding a 7-second wait at a small motel room reasonable when officers acted on a specific tip that the suspect was likely to dispose of the drugs).
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b252-6">
   It is probably unrealistic even on its own terms. The apartment was “small,” <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#704" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d 699, 704</a></span> (CA9 2002), and a man may walk the length of today’s small apartment in 15 seconds.
  </p>
</div></div></opinion>
```

---
