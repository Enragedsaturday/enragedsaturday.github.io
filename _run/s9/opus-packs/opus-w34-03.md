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

## GROUP: content/cases/United States v. Braxton.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Braxton"
type: case
citation: "61 F.4th 830 (2023)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 2023
date_decided: 2023-03-07
docket: 21-1149
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2023-03-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Braxton
  varies_by_point: false
  scope_note: "Good law in-circuit; backpack search conceded invalid as SITA, and inevitable discovery did not save it."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9381854/united-states-v-braxton/"
  cluster_id: 9381854
  opinion_id: 9377330
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Recent development (role-based)"
related: ["[[Arizona v. Gant]]", "[[Chimel v. California]]", "[[Riley v. California]]", "[[Nix v. Williams]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "inevitable-discovery"]
holding: "The government CONCEDED the warrantless search of Braxton's backpack was not a valid search incident to arrest, then relied on…"
lake:
  record_id: United States v. Braxton
  status: verified
  projected_at: 2026-07-09
---

# United States v. Braxton

*61 F.4th 830 (10th Cir. 2023)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers arrested Braxton on a public sidewalk and, without a warrant, searched a backpack associated with him, finding a firearm. He was charged with firearm and drug offenses and moved to suppress the gun. Under the circuit's recent decision in *United States v. Knapp* — which held that a search of an arrestee's bag is not a valid [[Search Incident to Arrest|search incident to arrest]] where the arrestee cannot reach weapons or evidence in the bag at the time — the government conceded the backpack search was not a lawful [[Search Incident to Arrest|search incident to arrest]] and instead relied on [[Inevitable Discovery and Independent Source|inevitable discovery]].

## Issue
Whether evidence from a backpack search that was not a valid [[Search Incident to Arrest|search incident to arrest]] is nonetheless admissible under the inevitable-discovery exception, on the theory that officers would have lawfully impounded the backpack ([[Community Caretaking|community caretaking]]) and discovered the gun in an inventory search.

## Rule
The search-incident-to-arrest point was conceded: "the government concedes that the warrantless search of the backpack was not justified by the warrant exception for searches incident to arrest." — slip op., at 7. ^pin-op7

To salvage the evidence by [[Inevitable Discovery and Independent Source|inevitable discovery]], the government bore the burden of proving lawful impoundment and inventory would have occurred. The court held it had not: "the inevitable-discovery exception to the exclusionary rule does not apply, and the gun discovered during the illegal search of the backpack must be suppressed." — [*Id.* at 17](https://www.courtlistener.com/opinion/9381854/united-states-v-braxton/#:~:text=the%20inevitable%2Ddiscovery%20exception%20to%20the%20exclusionary%20rule%20does). ^pin-op17

## Application
Because Braxton was under arrest and could not access the backpack at the time of the search, the search was not a valid [[Search Incident to Arrest|search incident to arrest]] — a point the government conceded under *Knapp*. The government then failed to prove by a preponderance that officers would have lawfully impounded the backpack as a matter of [[Community Caretaking|community caretaking]] and inventoried it; the record left the impoundment speculative and suggested any on-scene inventory would itself have been improper. [[Inevitable Discovery and Independent Source|Inevitable discovery]] therefore did not apply, and the gun was suppressed.

## Conclusion
The backpack search was an invalid [[Search Incident to Arrest|search incident to arrest]], and [[Inevitable Discovery and Independent Source|inevitable discovery]] did not cure it; suppression was ordered and the denial below reversed. A bag search is not incident to arrest once the arrestee cannot reach it, and [[Inevitable Discovery and Independent Source|inevitable discovery]] requires proof — not speculation — of a lawful alternative route to the evidence.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Braxton* applies the reaching-distance limit on [[Search Incident to Arrest|searches incident to arrest]] from [[Chimel v. California]] and [[Arizona v. Gant]] (and the circuit's *Knapp* rule for bags), and the inevitable-discovery doctrine of [[Nix v. Williams]]; on digital/container limits compare [[Riley v. California]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Recent development (role-based)*

## Sources
- *United States v. Braxton*, 61 F.4th 830 (10th Cir. 2023) — https://www.courtlistener.com/opinion/9381854/united-states-v-braxton/ — pinpoints: slip op., at 7, 17 (CL carries the slip opinion; cluster 9381854 → opinion 9377330).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "935d2f34c364c069", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "61 F.4th 830 (2023)", "court": "U.S. Court of Appeals, 10th Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Braxton", "year": "2023"}}
{"assertion_id": "0f9a79a08a5ce4fe", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The government CONCEDED the warrantless search of Braxton's backpack was not a valid search incident to arrest, then relied on…", "title": "United States v. Braxton"}}
{"assertion_id": "5370903dc6d055cc", "dimension": "support", "kind": "home_role", "locator": {"home": "Inventory Searches"}, "payload": {"home": "Inventory Searches", "role": "Recent development (role-based)", "title": "United States v. Braxton"}}
{"assertion_id": "87c5b0fa654e7f02", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2023-03-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Braxton", "field_i_validity": "good_law", "scope_note": "Good law in-circuit; backpack search conceded invalid as SITA, and inevitable discovery did not save it.", "title": "United States v. Braxton", "varies_by_point": "false"}}
{"assertion_id": "ea3cb2a68bbc05b7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Braxton"}}
```

### lake record — United States v. Braxton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Braxton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Braxton",
    "case_name_short": "Braxton",
    "case_name_full": "",
    "input_case_name": "United States v. Braxton",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2023-03-07",
    "year": 2023,
    "docket": "21-1149",
    "cluster_id": 9381854,
    "lead_opinion_id": 9377330,
    "sibling_ids": [
      9377330
    ],
    "absolute_url": "/opinion/9381854/united-states-v-braxton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "61 F.4th 830",
      "volume": "61",
      "reporter": "F.4th",
      "page": "830",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "61 F.4th 830",
        "volume": "61",
        "reporter": "F.4th",
        "page": "830",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "61 F.4th 830",
    "official_selection": {
      "court_class": "coa",
      "selected": "61 F.4th 830",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op7",
      "page": null,
      "quote": "--- # United States v. Braxton *61 F.4th 830 (10th Cir. 2023)* \u00b7 U.S. Court of Appeals, 10th Circuit \u00b7 **Binding in-circuit \u2014 10th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Braxton on a public sidewalk and, without a warrant, searched a backpack associated with him, finding a firearm. He was charged with firearm and drug offenses and moved to suppress the gun. Under the circuit's recent decision in *United States v. Knapp* \u2014 which held that a search of an arrestee's bag is not a valid search incident to arrest where the arrestee cannot reach weapons or evidence in the bag at the time \u2014 the government conceded the backpack search was not a lawful search incident to arrest and instead relied on inevitable discovery. ## Issue Whether evidence from a backpack search that was not a valid search incident to arrest is nonetheless admissible under the inevitable-discovery exception, on the theory that officers would have lawfully impounded the backpack (community caretaking) and discovered the gun in an inventory search. ## Rule The search-incident-to-arrest point was conceded:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op17",
      "page": null,
      "quote": "the inevitable-discovery exception to the exclusionary rule does not apply, and the gun discovered during the illegal search of the backpack must be suppressed.",
      "star_marker": "3",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 30187,
      "fragment": "#:~:text=the%20inevitable%2Ddiscovery%20exception%20to%20the%20exclusionary%20rule%20does",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2023-03-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Braxton",
    "varies_by_point": false,
    "scope_note": "Good law in-circuit; backpack search conceded invalid as SITA, and inevitable discovery did not save it.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Brandon Christopher Serini v. The State of Wyoming",
          "cluster_id": 10374407,
          "cite": [
            "566 P.3d 190",
            "2025 WY 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Elmore",
          "cluster_id": 9505983,
          "cite": [
            "101 F.4th 1210"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramos",
          "cluster_id": 9452629,
          "cite": [
            "88 F.4th 862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montgomery v. Cruz",
          "cluster_id": 10769646,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Campbell",
          "cluster_id": 10681819,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brandon Christopher Serini v. The State of Wyoming",
          "cluster_id": 10375200,
          "cite": [
            "2025 WY 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9377330) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      },
      "lane2_top_cited": {
        "query": "cites:(9377330)",
        "reviewed": 6,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(9377330)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(9377330)",
    "indexed_citing_opinions": 6,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9377330,
        "count": 6,
        "count_source": "search"
      }
    ],
    "citation_count": 8,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-braxton.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 6,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9377330,
        "cited_id": 1245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 161257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 163326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 220780,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 332335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 436329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 600741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 770086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 795888,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4373735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4530911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4674893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4683374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 8413595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 9430773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 9482577,
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
    "date_created": "2026-07-05T22:45:19Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:45:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:45:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:49:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:45:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Braxton

```
Appellate Case: 21-1149     Document: 010110822581       Date Filed: 03/07/2023    Page: 1
                                                                                  FILED
                                                                      United States Court of Appeals
                                       PUBLISH                                Tenth Circuit

                       UNITED STATES COURT OF APPEALS                        March 7, 2023

                                                                         Christopher M. Wolpert
                              FOR THE TENTH CIRCUIT                          Clerk of Court
                          _________________________________

  UNITED STATES OF AMERICA,

        Plaintiff - Appellee,

  v.                                                          No. 21-1149

  TYRELL BRAXTON,

        Defendant - Appellant.
                       _________________________________

                      Appeal from the United States District Court
                              for the District of Colorado
                           (D.C. No. 1:20-CR-00037-RM-1)
                        _________________________________

 Meredith Esser, Assistant Federal Public Defender, Denver, Colorado (Virginia L. Grady,
 Federal Public Defender, with her on the briefs), for Defendant - Appellant.

 Wayne Paugh, Assistant United States Attorney, Denver, Colorado (Cole Finegan, United
 States Attorney, with him on the brief), for Plaintiff - Appellee.
                         _________________________________

 Before HARTZ, SEYMOUR, and MORITZ, Circuit Judges.
                   _________________________________

 MORITZ, Circuit Judge.
                     _________________________________

       Law enforcement searched Tyrell Braxton’s backpack after arresting him and

 found a gun. Facing several criminal charges, Braxton moved to suppress the gun.

 The government conceded that the warrantless search was not a valid search incident

 to arrest. But it invoked the inevitable-discovery doctrine to avoid suppression of the
Appellate Case: 21-1149     Document: 010110822581         Date Filed: 03/07/2023       Page: 2



 illegally obtained evidence, contending that—assuming the illegal search incident to

 arrest had not occurred—law enforcement would have validly impounded the

 backpack as a matter of community caretaking and then searched it pursuant to a

 standardized policy mandating inventory searches of seized property. The district

 court agreed with the government and denied the motion to suppress.

        But the government’s stated community-caretaking interest in safeguarding

 Braxton’s personal property by impounding it is significantly undercut by the

 presence of an individual who arrived on the scene at Braxton’s request and

 repeatedly asked to take possession of the backpack throughout the arrest process.

 The government’s explanation for why the officers could have properly refused this

 individual’s requests is not persuasive. Nor is it dispositive, on these facts, that

 Braxton himself did not ask the officers to turn the backpack over. Thus, the

 government failed to meet its burden to show that law enforcement would have

 validly retained the backpack, and the inevitable-discovery doctrine does not apply to

 excuse application of the exclusionary rule to suppress evidence discovered during

 the illegal search. We accordingly reverse the district court’s order refusing to

 suppress the gun and remand for further proceedings.

                                       Background

        A Denver police officer monitoring a camera installed in a high-crime area

 saw Braxton exchange drugs for cash. Officers arrived on the scene and arrested

 Braxton. As the district court noted, the details of the arrest are not in dispute

 because one officer’s bodycam captured the arrest on video.


                                             2
Appellate Case: 21-1149   Document: 010110822581        Date Filed: 03/07/2023      Page: 3



       The video shows that at the moment he was handcuffed, Braxton was wearing

 a black backpack with a repeating “Emporio Armani” design on it, which the officers

 removed and placed on the sidewalk. One officer then patted Braxton down and

 discovered suspected crack cocaine and $183 in cash in Braxton’s pockets. During

 the patdown, Braxton called out, “Hey, get my girl, my girl. Tan! Tell her to come

 here!” Supp. R. at 1:51–1:56.

       Less than 30 seconds later, a woman—later identified as Braxton’s girlfriend,

 Tanyrah Gay—approached the officers, and Braxton instructed her, “Get the money

 so you can bond me out.” Id. at 2:18–2:23. Gay then asked the officers, “Can I get his

 bag?” Id. at 2:24–2:26. The officers responded in the negative. Gay stood by for a

 little over a minute while one officer continued searching Braxton. Then, as one

 officer walked away with Braxton and another officer picked up the backpack, Gay

 again asked, “I can’t take my backpack?” Id. at 3:38–3:40. The officer immediately

 responded with a curt “nope.” Id. at 3:40–3:41.

       Gay followed as one officer escorted Braxton to a patrol car and another

 carried the backpack. As Braxton was getting into the patrol car, he said, “She needs

 the money, man.” Id. at 4:10–4:12. Gay then said, “I’m in a hotel. Please give me the

 money at least. I’m in a hotel.” Id. at 4:13–4:18. Before Gay could finish, the answer

 again was an immediate “nope.” Id. at 4:16. Gay then asked if the officers would

 write her number down; they told her they would “get to that in a second.” Id. at

 4:38–4:40.




                                           3
Appellate Case: 21-1149    Document: 010110822581         Date Filed: 03/07/2023     Page: 4



       One officer placed the backpack on the hood of the patrol car and searched it.

 As the officer dug through the backpack’s contents, he found a loaded gun with a

 pink handle. Before the officer completed the search of the backpack, Gay asked him

 if she could retrieve her bus pass and identification from the backpack. The officer

 said they could “talk about that in a second.” Id. at 7:15–7:16. About 20 seconds

 later, after the officer placed the gun into an evidence bag and into the front of the

 patrol vehicle, the bodycam footage ends.

       Based on this event, the government charged Braxton with possession of a

 weapon in furtherance of drug trafficking, possession of crack cocaine with intent to

 distribute, and felon in possession of a weapon. Braxton moved to suppress the gun,

 arguing that the warrantless search of his backpack was not justified as a search

 incident to arrest under this court’s recent precedent. See United States v. Knapp, 917

 F.3d 1161 (10th Cir. 2019) (holding that search of arrestee’s purse was not justified

 as search incident to arrest because arrestee could not access weapons or destroy

 evidence within purse at time of arrest).

       The government conceded that the search was not a valid search incident to

 arrest under Knapp. But it argued that the gun should not be suppressed because law

 enforcement would have inevitably discovered it after impounding the backpack and

 conducting an inventory search. That is, the government reasoned, had the officer not

 searched the backpack at the scene, he would have been obligated to take the

 backpack to the station to prevent theft and to protect the community in case the

 backpack contained dangerous items. And once at the station, the government


                                             4
Appellate Case: 21-1149      Document: 010110822581       Date Filed: 03/07/2023    Page: 5



 continued, standard policy required an inventory search that would have revealed the

 gun. The government supported its position with testimony from the officer who

 searched Braxton’s backpack.

          The district court agreed with the government and denied the motion to

 suppress. Braxton eventually entered a conditional guilty plea to possessing a firearm

 in furtherance of a drug-trafficking crime, and the district court sentenced him to 60

 months in prison and three years of supervised release.1

          Braxton now appeals the suppression ruling.

                                          Analysis

          Our review of the overall reasonableness of a search or seizure is de novo,

 though we accept the district court’s factual findings unless clearly erroneous and

 view the evidence in the light most favorable to the district court’s findings. Knapp,

 917 F.3d at 1165; see also United States v. Cook, 599 F.3d 1208, 1213 (10th Cir.

 2010).

          “The Fourth Amendment’s prohibition of ‘unreasonable searches and seizures’

 means that police generally cannot conduct a search or make a seizure absent a

 warrant.” United States v. Kendall, 14 F.4th 1116, 1122 (10th Cir. 2021) (citation

 omitted) (quoting U.S. Const. amend IV). “A warrantless search or seizure is

 reasonable only ‘if it falls within a specific exception to the warrant requirement.’”


          1
         Braxton also pleaded guilty to a separate count of felon in possession of a
 firearm based on events that occurred on a different date. The district court imposed a
 consecutive 12-month sentence for this additional count (and a concurrent three-year
 term of supervised release), bringing Braxton’s prison sentence to 72 months in total.

                                              5
Appellate Case: 21-1149    Document: 010110822581       Date Filed: 03/07/2023    Page: 6



 Id. at 1121–22 (quoting United States v. Venezia, 995 F.3d 1170, 1174 (10th Cir.

 2021)). These exceptions include, among others, searches incident to arrest, searches

 and seizures justified by a noninvestigatory community-caretaking rationale, and

 searches conducted for administrative inventory purposes. See Knapp, 917 F.3d at

 1165 (discussing exception for searches incident to arrest); United States v. Neugin,

 958 F.3d 924, 931 (10th Cir. 2020) (explaining community-caretaking exception);

 Kendall, 14 F.4th at 1124 (describing exception for inventory searches). It is the

 government’s burden to establish that an exception to the warrant requirement

 applies. Neugin, 958 F.3d at 930.

       If law enforcement searches or seizes without a warrant or applicable warrant

 exception and thus “obtains evidence th[r]ough an unconstitutional search, the

 evidence is inadmissible under the exclusionary rule.” Id. at 931. But like the warrant

 requirement, the exclusionary rule is also subject to some exceptions, one of which is

 the inevitable-discovery doctrine. Id. at 932. Under this doctrine, the exclusionary

 rule does not apply if the government can prove by a preponderance that “the

 evidence inevitably would have been discovered by lawful means.” Id. (quoting

 United States v. Souza, 223 F.3d 1197, 1202 (10th Cir. 2000)). The parties agree that

 the inevitable-discovery doctrine requires a counterfactual inquiry into what “would

 have” happened under lawful circumstances.2 Id. At the same time, “‘[i]n


       2
          Because we rule for Braxton on another ground, we need not address his
 argument that law enforcement violated the Fourth Amendment because the officer
 testified that he did search the backpack with an investigatory motive, under the facts
 as they occurred.

                                            6
Appellate Case: 21-1149     Document: 010110822581         Date Filed: 03/07/2023     Page: 7



 determining whether the government has met its burden of proof, we consider

 “demonstrated historical facts,” not “speculative elements.”’” Id. (quoting United

 States v. White, 326 F.3d 1135, 1138 (10th Cir. 2003)).

        Here, the government concedes that the warrantless search of the backpack

 was not justified by the warrant exception for searches incident to arrest. But it

 contends that the inevitable-discovery exception to the exclusionary rule should

 apply because the officers would have eventually conducted a valid warrantless

 search of the backpack via two other exceptions to the warrant requirement:

 community caretaking and inventory. Specifically, the government argues that the

 officers would have impounded the backpack under a community-caretaking

 rationale to protect Braxton’s property rather than leaving it vulnerable to theft on the

 public sidewalk where Braxton was arrested. See, e.g., Venezia, 995 F.3d at 1180

 (“Certainly, an abandoned vehicle on a public highway may be at risk of theft or

 vandalism, and thus may be impounded under the community-caretaking doctrine.”).

 And it further contends that once the backpack was delivered to the police station,

 law-enforcement policy mandated an inventory search to further protect Braxton’s

 property. See, e.g., Kendall, 14 F.4th at 1124 (explaining that inventory “searches

 serve several administrative purposes, including ‘to protect an owner’s property

 while it is in the custody of the police, to insure against claims of lost, stolen, or

 vandalized property, and to guard the police from danger’” (quoting Colorado v.

 Bertine, 479 U.S. 367, 372 (1987))).




                                              7
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023     Page: 8



       The latter point is not in dispute—as the district court concluded, the parties

 do not “quarrel[] with the need or appropriateness of the inventory” search once the

 backpack reached the police station. R. vol. 3, 147. Instead, this case turns on

 whether the officers would have validly impounded Braxton’s backpack in the

 absence of the illegal search incident to arrest. See United States v. Ibarra, 955 F.2d

 1405, 1410 (10th Cir. 1992) (finding no inevitable discovery because although

 inventory search was valid, “no inventory of the contents of defendant’s vehicle

 could have been conducted but for the unlawful impoundment of the vehicle”). On

 impoundment, the district court concluded that the officers were “entitled to take

 physical possession of” the backpack “on a community[-]caretaker . . . basis.” R. vol.

 3, 146. The district court dismissed the relevance of Gay’s presence and her repeated

 requests to take possession of the backpack, emphasizing that Braxton never asked

 the officers to give the backpack to Gay and reasoning that to the officers at the time,

 the relationship between Braxton and Gay was unclear.

       On appeal, Braxton argues that the government did not meet its burden of

 showing that officers would have impounded the backpack as a matter of community

 caretaking. We have had many recent opportunities to examine community-

 caretaking impoundments, albeit in the context of vehicles rather than personal

 property like Braxton’s backpack. See Kendall, 14 F.4th at 1122 (citing three recent

 published cases). Yet the principles from these vehicle-impoundment cases are

 relevant in the context of personal property. See Knapp, 917 F.3d at 1168 (noting that

 principles articulated in vehicle-impoundment caselaw “apply more broadly” and


                                            8
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023      Page: 9



 using such caselaw to review search of defendant’s purse); United States v. Perea,

 986 F.2d 633, 643 (2d Cir. 1993) (noting that for arrests that do not occur at

 individual’s home, “officers may ‘impound the personal effects that are with him [or

 her] at the time to ensure the safety of those effects or to remove nuisances from the

 area’” (quoting Cabbler v. Superintendent, Va. State Penitentiary, 528 F.2d 1142,

 1146 (4th Cir. 1975))). Indeed, the parties also frame their arguments around our

 vehicle-impoundment caselaw, in particular United States v. Sanders, 796 F.3d 1241

 (10th Cir. 2015).

       Sanders held that impoundment of a vehicle from private property must be

 “justified by both [1] a standardized policy and [2] a reasonable, non[]pretextual

 community-caretaking rationale.” Id. at 1248. We begin (and end) our analysis with

 the second prong.3 On that prong, Sanders set out a nonexclusive list of factors

 relevant to determining whether “a reasonable and legitimate, non[]pretextual

 community-caretaking rationale” exists, including:

       (1) whether the vehicle is on public or private property; (2) if on private
       property, whether the property owner has been consulted; (3) whether

       3
          The government contends that Sanders’s first prong does not apply here
 because we are on public—not private—property. See Kendall, 14 F.4th at 1122 (“In
 one of our recent cases, however, we clarified that the first Sanders prong is ‘specific
 to private property impoundments.’” (quoting Venezia, 995 F.3d at 1178)). But
 Braxton asserts in reply that the government waived such argument by not raising it
 below. See United States v. Martinez, 643 F.3d 1292, 1298 (10th Cir. 2011) (“We
 will not consider a suppression argument raised for the first time on appeal absent a
 showing of good cause for why it was not raised before the trial court.”). In any
 event, we need not address these issues here because even if the government did not
 waive its first-prong argument and its argument is correct, it still needs to satisfy the
 second Sanders prong; and the same is true if the government did waive its first-
 prong argument or if such argument is incorrect.

                                             9
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023      Page: 10



        an alternative to impoundment exists (especially another person capable
        of driving the vehicle); (4) whether the vehicle is implicated in a crime;
        and (5) whether the vehicle’s owner and/or driver have consented to the
        impoundment.

  Id. at 1250. These factors help guide the overall question for Fourth Amendment

  purposes: whether, in the counterfactual world of our inevitable-discovery inquiry,

  the seizure of Braxton’s backpack would have been reasonable. See id. (“Protection

  against unreasonable impoundments . . . is part and parcel of the Fourth

  Amendment’s guarantee against unreasonable searches and seizures.”).

        Four of these factors apply in a relatively straightforward manner here. First,

  the arrest took place on public property, so the backpack itself was also on public

  property. See id. Braxton concedes that this fact would weigh in favor of a reasonable

  community-caretaking rationale for impoundment because the officers obviously

  could not have left the backpack on the sidewalk. See Kendall, 14 F.4th at 1123

  (weighing this factor in favor of reasonable community-caretaking rationale for

  impoundment because it was not “a reasonable option for officers to leave the vehicle

  where it was,” parked on public street). Relatedly, the public location renders the

  second Sanders factor—whether the owner of private property has been consulted—

  simply not relevant here. See id. (omitting second factor from discussion where arrest

  took place on public property). On the fourth and fifth other factors, the government

  concedes that the backpack here was not implicated in a crime and that Braxton did

  not consent to the impoundment. See 796 F.3d at 1250.These two factors accordingly

  would weigh against a reasonable community-caretaking rationale for impoundment.



                                            10
Appellate Case: 21-1149     Document: 010110822581        Date Filed: 03/07/2023     Page: 11



  See United States v. Woodard, 5 F.4th 1148, 1158 (10th Cir. 2021) (weighing these

  factors against valid impoundment).

        Largely agreeing on these four factors, the parties center their disagreement on

  the third Sanders factor, the existence of an alternative to impoundment. See 796

  F.3d at 1250. On this point, recall that Gay appeared less than 30 seconds after

  Braxton called out for his “girl,” Gay twice asked to take the backpack, and the

  officers curtly rejected her requests almost before she could finish her requests. R.

  vol. 3, 143. Braxton contends that giving the backpack to Gay would have been an

  alternative to impoundment and argues that this factor weighs heavily against a

  reasonable community-caretaking rationale for impoundment. In response, the

  government argues that giving the backpack to Gay would not have been an

  alternative to impoundment for two reasons: (1) Braxton did not ask the officers to do

  so and (2) nothing in the record suggests that Braxton and Gay had a relationship that

  warranted giving his backpack to her.

        As to the government’s first point, it is true that Braxton did not expressly ask

  the officers to give Gay the backpack. But we have stated that “[t]he proper inquiry

  under the third factor is ‘whether an alternative to impoundment exists’ and is not

  focused on who suggested that alternative.” Venezia, 995 F.3d at 1181 (emphasis

  added) (quoting Sanders, 796 F.3d at 1250). Braxton’s failure to directly ask the

  officers to give the backpack to Gay is therefore not dispositive. It is just one fact

  among many, and we do not find it particularly meaningful in light of Gay’s physical




                                             11
Appellate Case: 21-1149     Document: 010110822581        Date Filed: 03/07/2023    Page: 12



  presence at the scene and repeated requests to take the backpack. Given these facts, a

  satisfactory alternative to impoundment may have existed.

        As to the government’s second point, the record does not support the notion

  that Braxton and Gay’s relationship negated the plausibility of this alternative. Gay

  appeared less than 30 seconds after Braxton called out for his “girl,” and the officer

  who testified at the suppression hearing said that he assumed the person who arrived

  in response to Braxton’s request was, in fact, the person Braxton had asked for—his

  “girl.” R. vol. 3, 143. Other facts support the conclusion that the two had a

  relationship close enough to merit giving her the backpack: Braxton asked Gay to

  bail him out; Braxton asked the officers to give Gay the money they found on him;

  Gay repeatedly asked to take the backpack; Gay at one point referred to the backpack

  as hers, which suggests that Braxton was carrying it for her; Gay remained nearby

  during the entire arrest process; Gay asked the police to write her number down; and

  Gay told the officers her bus pass and identification were in the backpack. These

  facts suggest that, at a minimum, reasonable officers dealing with the backpack in a

  lawful manner would have inquired further about whether they should give the

  backpack to Gay, either by asking Braxton if he wanted Gay to take the backpack or

  by inquiring into their relationship.4


        4
           The government asserts that the district court made a factual finding that Gay
  was essentially “a stranger” to Braxton. R. vol. 3, 149. But as Braxton points out in
  reply, the district court’s comment on this point was less than clear. The district court
  referred to Gay as “a stranger,” but not necessarily a stranger to Braxton; it could
  have been pointing out that Gay was a stranger to the officers. Id. Because of this
  ambiguity and because this case involves undisputed video evidence of the arrest—in

                                             12
Appellate Case: 21-1149     Document: 010110822581        Date Filed: 03/07/2023     Page: 13



        Importantly, the officer who testified at the suppression hearing provided scant

  explanation for why—in the counterfactual scenario in which he was not going to

  search the backpack incident to arrest—he would have refused Gay’s requests and

  would not have inquired further into their relationship or asked Braxton about giving

  her the backpack. At best, when explaining why he did not ask Braxton if Gay could

  take the backpack, the officer said it was “not common practice to be handing out

  personal property of other persons to other people.” Id. at 93. And it is true that the

  government produced a department policy stating that “[a]ny officer coming into

  possession of personal . . . property will bring such property to the [e]vidence and

  [p]roperty [s]ection[] or an authorized remote evidence locker.” R. vol. 1, 28. But the

  existence of and compliance with such a policy does not by itself establish a

  reasonable community-caretaking rationale. See Sanders, 796 F.3d at 1249–50

  (“Protection against unreasonable impoundments, even those conducted pursuant to a

  standardized policy, is part and parcel of the Fourth Amendment’s guarantee against

  unreasonable searches and seizures.” (emphasis added)); Venezia, 995 F.3d at 1182

  (holding impoundment unreasonable despite compliance with policy because policy


  the words of the district court, its factual findings “really do[]n’t matter . . . because
  it’s all on body[]cam,” id. at 142—we decline to interpret the district court’s
  reference to Gay as “a stranger” as a factual finding that she and Braxton were
  strangers to each other, id. at 149. And even if we were to do so, we would hold that
  finding clearly erroneous in light of the strong record evidence—detailed above,
  supra p. 12—that Gay and Braxton were not at all strangers. See United States v.
  Martinez-Jimenez, 464 F.3d 1205, 1209 (10th Cir. 2006) (stating that factual finding
  is clearly erroneous if it is “without factual support in the record or we are left with
  the definite and firm conviction that a mistake has been made” (quoting United States
  v. Cernobyl, 255 F.3d 1215, 1221 (10th Cir. 2001))).

                                             13
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023     Page: 14



  “did not grant the officers authority to do what the Fourth Amendment forbids—to

  impound a vehicle absent a reasonable community-caretaking rationale”). Nor does

  the policy negate the existence of an alternative to impoundment: The policy defines

  personal property as property that “must be held for safekeeping for the owner.”

  R. vol. 1, 27 (emphasis added). And the officer’s testimony does not meaningfully

  explain why, in light of Gay’s requests, he needed to impound the backpack to keep it

  safe for its owner. We thus conclude, on the record before us, that the alternative to

  impoundment of giving the backpack to Gay weighs heavily against finding a

  reasonable community-caretaking rationale. See Woodard, 5 F.4th at 1156 (weighing

  this factor against community-caretaking rationale where officers refused, without

  reason, to let defendant call someone to take his car); Venezia, 995 F.3d at 1179

  (“Where an alternative to impoundment does not threaten public safety or

  convenience, impoundment is less likely to be justified by a community-caretaking

  rationale.”).

         To recap, the only factor that favors a reasonable community-caretaking

  rationale for impoundment is that the arrest took place on public property. The

  remaining factors—an alternative to impoundment, that the backpack was not

  implicated in the crime, and that Braxton did not consent—cut significantly against a

  community-caretaking rationale. On these facts, we conclude the government failed

  to meet its burden of proving that, despite the alternative of giving the backpack to

  Gay, it was inevitable that the officers would have validly impounded the backpack

  under a reasonable community-caretaking rationale. See Venezia, 995 F.3d at 1182


                                             14
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023       Page: 15



  (concluding that existence of alternative rendered impoundment unreasonable); cf.

  Kendall, 14 F.4th at 1123 (concluding that “balance clearly weighs in favor of the

  reasonableness of impoundment, partly because there were no good alternatives”).

        The government emphasizes that officers are not obligated to explore

  alternatives to impoundment, noting that “[t]he reasonableness of any particular

  governmental activity does not necessarily or invariably turn on the existence of

  alternative ‘less intrusive’ means.” Aplee. Br. 24 (emphasis added) (quoting Bertine,

  479 U.S. at 374). But this general proposition does not mean that reasonableness does

  not sometimes, depending on the facts, turn on the existence of alternatives to

  impoundment. Indeed, “we have recognized that impoundment . . . is not reasonable

  when there are clear and promptly available alternatives.” United States v. Trujillo,

  993 F.3d 859, 868 (10th Cir. 2021); see also United States v. Pappas, 735 F.2d 1232,

  1234 (10th Cir. 1984) (finding impoundment unreasonable in part because

  defendant’s girlfriend and other friends were present and could have taken custody);

  cf. Trujillo, 993 F.3d at 870 (concluding that where vehicle posed traffic hazard and

  defendant was alone at 2:30 a.m., officers “were not required to allow [d]efendant to

  call someone to come pick up the [vehicle] and then, assuming he was successful,

  wait around for the new driver to arrive” and citing cases with similar facts and

  reasoning). Moreover, our precedent establishes that officers generally act

  unreasonably when they ignore or shut down obvious alternatives to impoundment.

  See Woodard, 5 F.4th at 1156 (weighing existence of alternative against community-

  caretaking rationale where defendant asked officers if he could call someone to pick


                                            15
Appellate Case: 21-1149     Document: 010110822581         Date Filed: 03/07/2023     Page: 16



  up vehicle and officers refused to let him do so without explanation); Sanders, 796

  F.3d at 1251 (finding impoundment unreasonable in part because “police impounded

  [defendant’s] vehicle without offering her the opportunity to make alternative

  arrangements, even though she stated that she was willing to have someone pick up

  the vehicle on her behalf”); cf. Kendall, 14 F.4th at 1123–25 (finding impoundment

  reasonable in part because of absence of alternatives).5 And the officer here did just

  that, failing to offer any reasonable rationale for not at least inquiring further about

  whether Gay could take the backpack.6

        In sum, because a clear and promptly available alternative existed here, the

  government cannot show that it would have impounded the backpack under a

  reasonable, nonpretextual community-caretaking rationale. Thus, the government




        5
           Braxton additionally highlights a district-court case that held the
  impoundment of personal property was unjustified by a reasonable community-
  caretaking rationale in a factually similar case. See United States v. Knapp, No. 17-
  CR-207, 2019 WL 11502454, at *3 (D. Wyo. June 13, 2019) (concluding
  impoundment was unreasonable in part because friend who was present during
  defendant’s arrest offered to take her purse, but officers talked friend out of it).
         6
           A separate aspect of the officer’s testimony is also troubling: When prompted
  to expound on what he would have done had he availed himself of the alternative to
  impoundment, the officer said that even if he had given Gay the backpack, he would
  have inventoried it before doing so. The government does not argue on appeal that
  this on-the-scene inventory search would have led to the inevitable discovery of the
  gun, and the district court ruled below that any such on-the-scene inventory search
  would have been constitutionally impermissible. But we note that this testimony
  suggests that in a counterfactual world without the illegal search incident to arrest
  and without an illegal impoundment, an illegal search would still have taken place.
  Although by no means determinative, this testimony further supports our conclusion
  that the inevitable-discovery doctrine does not save the government from the
  exclusionary rule in this case.

                                              16
Appellate Case: 21-1149    Document: 010110822581       Date Filed: 03/07/2023    Page: 17



  failed to meet its burden to show that the gun would have been legally and inevitably

  discovered.

                                       Conclusion

        The government failed to prove by a preponderance of the evidence that if the

  law-enforcement officers had not conducted an illegal search incident to arrest, they

  would have nevertheless lawfully impounded the backpack as a matter of community

  caretaking and then discovered the gun during an inventory search. Thus, the

  inevitable-discovery exception to the exclusionary rule does not apply, and the gun

  discovered during the illegal search of the backpack must be suppressed. We

  accordingly reverse the district court’s order denying suppression and remand for

  further proceedings.




                                            17

```

---

## GROUP: content/cases/United States v. Brinkley.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Brinkley
type: case
citation: "980 F.3d 377 (2020)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir. 2020
court_level: coa
circuit: ca4
year: 2020
date_decided: 2020-11-13
docket: 18-4455
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
  opinion_url: "https://www.courtlistener.com/opinion/4805913/united-states-v-kendrick-brinkley/"
  cluster_id: 4805913
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Brinkley
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Arrest in the Home]]"
    role: Key
related:
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[United States v. Watson]]"
  - "[[United States v. Berkowitz]]"
tags:
  - case
  - fourth-amendment
  - arrest
  - warrantless-arrest
  - payton
  - probable-cause
holding: "To enter a home to execute an arrest warrant, officers must have reason to believe — which in the Fourth Circuit means probable cause — both that the home is the suspect's residence and that the suspect is present; an entry supported only by an arrest warrant and uncorroborated hunches about residence and presence is unlawful, so the evidence obtained must be suppressed."
---

# United States v. Brinkley

*980 F.3d 377 (4th Cir. 2020)* (No. 18-4455) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4805913 → opinion 4586260 (980 F.3d 377, decided 2020-11-13); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In February 2017, a federal-state task force in Charlotte set out to execute an arrest warrant for Kendrick Brinkley, a convicted felon wanted for unlawfully possessing a firearm. Relying only on the arrest warrant — with neither consent nor a search warrant — officers entered the Stoney Trace apartment, a residence they associated with Kayla Chisholm, with whom Brinkley was involved. They found Brinkley inside and seized evidence. Brinkley moved to suppress, explaining that he had been staying at the apartment as Chisholm's overnight guest and did not reside there. The district court denied the motion, and Brinkley entered conditional guilty pleas on two counts arising from the entry.

## Issue
Whether, before entering a home to execute an arrest warrant without consent or a search warrant, the officers had the "reason to believe" *[[Payton v. New York]]* requires — both that the apartment was Brinkley's residence and that he was present inside.

## Rule
Under *[[Payton v. New York|Payton]]*, an arrest warrant carries "the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within," a standard courts apply as a two-prong test — reason to believe both that the home is the suspect's residence and that he will be present. Joining the courts that equate that standard with probable cause, the Fourth Circuit held: "We hold that reasonable belief amounts to probable cause, and that the police in this case lacked reason to believe Brinkley resided in the Stoney Trace apartment and would be present when they entered." — slip op. at 25. Where the suspect may be only a guest, *[[Steagald v. United States]]* requires a separate search warrant.

## Application
The officers rested everything on a single, uncorroborated address linking Brinkley to Chisholm's apartment; that did not establish probable cause that he resided there rather than staying as a guest — a distinction that, under *[[Steagald v. United States|Steagald]]*, would have required a search warrant. And even assuming residence, the officers failed the second prong: generic "signs of life" inside and a resident's understandably nervous reactions, without indicators particular to the suspect, do not amount to probable cause that Brinkley himself was present. Because the entry rested solely on the arrest warrant without the required showing on both prongs, it was unlawful.

## Conclusion
**Reversed, [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]]**: the denial of suppression was reversed and Brinkley's convictions on the two challenged counts [[Reading and Citing Cases#vacated|vacated]]. Motz, J., wrote for the court (Gregory, C.J., joined); Richardson, J., dissented, arguing that *[[Payton v. New York|Payton]]*'s "reason to believe" should not be equated with probable cause.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Brinkley* places the Fourth Circuit among the courts holding that *[[Payton v. New York|Payton]]*'s "reason to believe" means probable cause — deepening an acknowledged circuit split — and reinforces that when officers are uncertain whether their suspect is a resident or merely a guest, *[[Steagald v. United States|Steagald]]* demands a separate search warrant to protect the home's actual occupants.

## Appears on
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Brinkley*, 980 F.3d 377 (4th Cir. 2020)](https://www.courtlistener.com/opinion/4805913/united-states-v-kendrick-brinkley/) — pinpoint: slip op. at 25 (reason-to-believe / probable-cause holding); the CL opinion text carries the slip-opinion page numbers rather than 980 F.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e47608d750117cbf", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "980 F.3d 377 (2020)", "court": "4th Cir. 2020", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Brinkley", "year": "2020"}}
{"assertion_id": "d0173eb49a55131e", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Key", "title": "United States v. Brinkley"}}
{"assertion_id": "f866500defc3aba2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "To enter a home to execute an arrest warrant, officers must have reason to believe — which in the Fourth Circuit means probable cause — both that the home is the suspect's residence and that the suspect is present; an entry supported only by an arrest warrant and uncorroborated hunches about residence and presence is unlawful, so the evidence obtained must be suppressed.", "title": "United States v. Brinkley"}}
{"assertion_id": "194e96cf57b809a7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Brinkley"}}
{"assertion_id": "e3e9918de2156598", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Brinkley", "varies_by_point": "false"}}
```

### lake record — United States v. Brinkley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Brinkley",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Kendrick Brinkley",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Brinkley",
    "court": "4th Cir. 2020",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2020-11-13",
    "year": 2020,
    "docket": "18-4455",
    "cluster_id": 4805913,
    "lead_opinion_id": 4586260,
    "sibling_ids": [],
    "absolute_url": "/opinion/4805913/united-states-v-kendrick-brinkley/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "980 F.3d 377",
      "volume": "980",
      "reporter": "F.3d",
      "page": "377",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "980 F.3d 377",
        "volume": "980",
        "reporter": "F.3d",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "980 F.3d 377",
    "official_selection": {
      "court_class": "state",
      "selected": "980 F.3d 377",
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
    "date_created": "2026-07-06T05:50:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-brinkley--4805913",
      "to_record_id": "United States v. Brinkley",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Brinkley

```
                                      PUBLISHED

                       UNITED STATES COURT OF APPEALS
                           FOR THE FOURTH CIRCUIT


                                       No. 18-4455


UNITED STATES OF AMERICA,

                     Plaintiff - Appellee,

              v.

KENDRICK BRINKLEY,

                     Defendant - Appellant.


Appeal from the United States District Court for the Western District of North Carolina, at
Charlotte. Robert J. Conrad, Jr., District Judge. (3:16-cr-00324-RJC-DSC-1)


Argued: January 31, 2020                                    Decided: November 13, 2020


Before GREGORY, Chief Judge, and MOTZ and RICHARDSON, Circuit Judges.


Reversed, vacated, and remanded by published opinion. Judge Motz wrote the opinion, in
which Chief Judge Gregory joined. Judge Richardson wrote a dissenting opinion.


ARGUED: John Parke Davis, FEDERAL DEFENDERS OF WESTERN NORTH
CAROLINA, INC., Charlotte, North Carolina, for Appellant. Amy Elizabeth Ray,
OFFICE OF THE UNITED STATES ATTORNEY, Asheville, North Carolina, for
Appellee. ON BRIEF: Anthony Martinez, Federal Public Defender, OFFICE OF THE
FEDERAL PUBLIC DEFENDER, Charlotte, North Carolina, for Appellant. R. Andrew
Murray, United States Attorney, OFFICE OF THE UNITED STATES ATTORNEY,
Charlotte, North Carolina, for Appellee.
DIANA GRIBBON MOTZ, Circuit Judge:

       To execute an arrest warrant for Kendrick Brinkley, police officers entered a private

home. They had neither consent to do so nor a search warrant. Brinkley appeals the district

court’s denial of his motion to suppress evidence obtained in the home, arguing that the

officers lacked the necessary reason to believe both that he (1) resided in the home and (2)

would be present when they entered. We agree and so must reverse.



                                             I.

       In February 2017, a federal-state task force in Charlotte, North Carolina, sought to

execute outstanding arrest warrants. J.A. 113. Brinkley, then subject to an arrest warrant

for unlawfully possessing a firearm as a convicted felon, was among the targets. J.A. 111.

                                            A.

       Bureau of Alcohol, Tobacco, and Firearms (ATF) Special Agent Jason Murphy

oversaw the operation. J.A. 110–11. An ATF analyst first provided Agent Murphy with

at least two possible addresses. J.A. 125. Because a water bill for one of these addresses

was in Brinkley’s name, Agent Murphy initially believed that address was Brinkley’s most

likely residence. J.A. 125–26. One of the other addresses that the analyst provided was an

apartment on Stoney Trace Drive in Mint Hill, North Carolina, J.A. 64, 125–26; no utility

bill in Brinkley’s name was associated with this address, J.A. 125.

       Charlotte-Mecklenburg Police Department Detective Robert Stark, a member of

Agent Murphy’s task force, also tried to locate Brinkley. J.A. 63–64, 110–11, 125. On

February 2, Detective Stark searched for Brinkley on CJLEADS, a North Carolina

                                             2
statewide law enforcement database. 1 J.A. 64. Detective Stark found multiple addresses

in the database linked to Brinkley. J.A. 64–66, 154. Two CJLEADS entries — one for a

traffic citation, added January 2, J.A. 155–56, and another from the state department of

corrections, added “at some point in January” — were associated with the Stoney Trace

apartment, J.A. 64–65, 68.

       But other CJLEADS entries that Detective Stark found placed Brinkley at numerous

other addresses. J.A. 74, 87. One entry, added five days before the January 2 traffic

citation, provided an address on Planters View Drive. J.A. 88, 154. Another entry, added

a month before that, gave an address on Stone Post Road in Charlotte. J.A. 88, 154. Older

entries, including at least five more from the same year, and others dating further back,

listed the Planters View Drive address and still other addresses. J.A. 74, 154. Detective

Stark did not look into the Planters View Drive address or any of these other addresses.

Rather, “based on the length of time that those addresses had been associated with”

Brinkley, Detective Stark believed that they “were probably family addresses” where

Brinkley did not reside. J.A. 89. But the detective intended to check these other addresses

if Brinkley was not found at the Stoney Trace apartment. J.A. 89.

       Detective Stark then found Brinkley’s public Facebook page. J.A. 72–73. Posts

and photos there led him to believe that Brinkley was dating one Brittany Chisholm. J.A.

73. Detective Stark searched for Chisholm on CJLEADS and found that she was also



       1
         Detective Stark also searched for Brinkley on KBCOPS, an internal police
department reporting system, but there is no indication in the record that he found anything
there. J.A. 64.
                                             3
associated with the Stoney Trace apartment. J.A. 73–74. Based on this information,

Detective Stark concluded that Brinkley lived there with Chisholm. J.A. 75.

       Detective Stark reported his conclusion to Agent Murphy, who came to agree that

Brinkley probably resided in the Stoney Trace apartment. J.A. 111–12, 126. Neither

officer was certain that they had uncovered Brinkley’s address. J.A. 112, 126. Rather, in

Agent Murphy’s experience, it was “common for someone like Mr. Brinkley . . . to have

more than one place where they will stay the night.” J.A. 126.

       The next day, Agent Murphy, Detective Stark, and three other police officers went

to the Stoney Trace apartment to conduct what both Agent Murphy and Detective Stark

characterized as a “knock-and-talk” to “start [their] search for Mr. Brinkley.” J.A. 75–76,

113, 126–27. The officers intended to “interview the occupants to find out if [he] was

indeed there,” and to arrest him if he was. J.A. 75, 113. Agent Murphy acknowledged that

he “had no idea if [Brinkley] was going to be there that morning,” but thought the Stoney

Trace apartment was the “most likely address” to “find Mr. Brinkley or evidence of his

whereabouts.” J.A. 134.

                                            B.

       The five officers arrived at the Stoney Trace apartment around 8:30 AM on Friday,

February 3, all wearing clothing identifying themselves as police officers. J.A. 75–77, 91.

In Agent Murphy’s words, they intended “to basically secure the area and sit up on the

house and wait to see if Mr. Brinkley left.” J.A. 134. Detective Stark knocked on the front

door, and the officers heard movement inside for about a minute. J.A. 77. A woman asked

who was there, and Detective Stark answered that it was the police. J.A. 77. The officers

                                            4
heard movement for another minute until Chisholm, wearing pajamas, slowly opened the

door. J.A. 77, 114.

       Detective Stark informed Chisholm that the officers were looking for Brinkley and

asked to enter the apartment. J.A. 96. Chisholm denied that Brinkley was there. J.A. 78,

96, 115, 128. According to Detective Stark, Chisholm grew “very nervous”; her “body

tensed” and her “breathing quickened,” and she looked back over her shoulder into the

apartment. J.A. 78. The officers saw another woman they did not recognize, but later

identified as Jermica Prigon, wearing pajamas and folding clothes in the living room. J.A.

79, 97, 116. The officers heard movement coming from a room in the back of the

apartment, and both Chisholm and Prigon repeatedly looked back toward that area. J.A.

78–80, 115–16.

       Detective Stark again asked if Brinkley was present and if the officers could enter

to look for him. J.A. 79, 115. He explained that the police “had information that [Brinkley]

was staying at this residence” and “asked for [Chisholm’s] permission . . . to come through

and just do a walk through to make sure that he was indeed not at the residence.” J.A. 115.

Chisholm, still seeming nervous, answered that she did not want the police officers to enter

her apartment and asked if they had a search warrant authorizing them to do so. J.A. 79,

115.

       Detective Stark estimated the entire exchange with Chisholm lasted “a little more

than a minute”; Agent Murphy thought it lasted more than three. J.A. 96–97, 129. Both

testified that based on Chisholm’s demeanor and behavior, Prigon’s presence, the

movement they heard in the back of the apartment, and the morning hour (8:30 AM), they

                                             5
believed Brinkley was inside. J.A. 81, 117, 133. Agent Murphy testified that the sounds

and the women’s reactions led him to believe “100 percent that Mr. Brinkley was hiding

in the apartment.” J.A. 134.

       At this point, the officers decided not to follow the original plan to secure the area

and wait to see if Brinkley left the home. J.A. 134. Instead, Agent Murphy told Chisholm

that he believed she was hiding Brinkley and that the officers were going to enter the

apartment to serve an arrest warrant on him. J.A. 81, 117. Then the five uniformed and

armed officers entered the apartment. J.A. 99. Detective Stark recalled that he probably

entered with his gun drawn; Agent Murphy believed that he did not draw his weapon at

this time. J.A. 81, 117. The officers found Brinkley in a bedroom. J.A. 82, 99, 118. They

arrested and handcuffed him. J.A. 82, 99, 118.

       The officers conducted a protective sweep to check for others hiding in the

apartment. J.A. 82, 99, 119. They did not find anyone else but did see digital scales, a

plastic baggie containing cocaine base, and a bullet. J.A. 83, 105, 119–20, 131. Chisholm

then gave but subsequently revoked verbal consent to search the apartment, so the officers

obtained a search warrant, pursuant to which they seized three firearms and magazines.

J.A. 83–86, 108–09, 120–23, 159.

                                             C.

       A grand jury indicted Brinkley on two felon-in-possession charges under 18 U.S.C.

§ 922(g)(1), one charge of possession with intent to distribute cocaine base under 21 U.S.C.

§ 841(a)(1), and one charge of firearm possession in furtherance of a drug offense under

18 U.S.C. § 924(c)(1)(A). J.A. 8–10. Brinkley moved to suppress the evidence police

                                             6
obtained after entering the Stoney Trace apartment. J.A. 12–15. He denied that he resided

in the apartment and explained that he was staying there as Chisholm’s overnight guest. 2

J.A. 13, 20. Brinkley argued that when the officers entered the apartment, they lacked

reason to believe that he (1) resided in the apartment or (2) would be present there at that

time. J.A. 19–23. The district court denied the motion. J.A. 144.

       Brinkley entered an unconditional guilty plea to one felon-in-possession charge, the

predicate for the arrest warrant. He entered a conditional guilty plea to two other charges

arising from the search of the home, reserving the right to appeal the suppression ruling.

J.A. 220. The district court sentenced Brinkley to 84 months’ imprisonment and three

years’ supervised release on each count, to run concurrently. J.A. 206, 208. Brinkley

timely appealed.

       We review the district court’s legal conclusions — including determinations of

reasonable suspicion and probable cause — de novo, Ornelas v. United States, 517 U.S.

690, 699 (1996), and its factual findings for clear error, construing the facts in the

Government’s favor, United States v. Alston, 941 F.3d 132, 136–37 (4th Cir. 2019).



                                            II.

                                            A.

       The Fourth Amendment protects “[t]he right of the people to be secure in their

persons, houses, papers, and effects, against unreasonable searches and seizures.” U.S.


       2
        Whether as a resident or as an overnight guest, Brinkley has standing to assert a
Fourth Amendment violation. See Minnesota v. Olson, 495 U.S. 91, 98–100 (1990).
                                             7
Const., amend. IV. In most cases, a search or seizure is unreasonable unless authorized by

a warrant. See, e.g., City of Los Angeles v. Patel, 576 U.S. 409, 419 (2015); Katz v. United

States, 389 U.S. 347, 357 (1967). The warrant requirement “ensures that the inferences to

support a search are ‘drawn by a neutral and detached magistrate instead of being judged

by the officer engaged in the often competitive enterprise of ferreting out crime,’” Riley v.

California, 573 U.S. 373, 382 (2014) (quoting Johnson v. United States, 333 U.S. 10, 14

(1948)), and so safeguards “the individual’s interests in protecting his own liberty and the

privacy of his home,” Steagald v. United States, 451 U.S. 204, 212 (1981).

       The warrant requirement carries special force when police seek to enter a private

home, which is “afforded the most stringent Fourth Amendment protection.” United States

v. Martinez-Fuerte, 428 U.S. 543, 561 (1976). “With few exceptions, the question whether

a warrantless search of a home is reasonable and hence constitutional must be answered

no.” Kyllo v. United States, 533 U.S. 27, 31 (2001). But a valid search warrant of course

authorizes police to enter a home.

       In some circumstances, an arrest warrant can also allow officers to enter a home in

order to apprehend a suspect. But the Supreme Court has held that when police officers

seek to enter a home pursuant to an arrest warrant, the Fourth Amendment imposes specific

and different requirements for entry based on whether the home is the suspect’s own

residence or someone else’s.

       When police armed with an arrest warrant seek to enter a suspect’s own home,

Payton v. New York, 445 U.S. 573 (1980), controls. There the Court concluded that “for

Fourth Amendment purposes, an arrest warrant founded on probable cause implicitly

                                             8
carries with it the limited authority to enter a dwelling in which the suspect lives when

there is reason to believe the suspect is within.” Id. at 603. The Payton Court reasoned

that an arrest warrant “will suffice to interpose the magistrate’s determination of probable

cause between the zealous officer and the citizen,” so it is not constitutionally necessary

for officers to seek additional judicial authorization before entering a suspect’s own home

to arrest him. Id. at 602–03.

       But one year later, in Steagald v. United States, 451 U.S. 204, the Court decided

that an arrest warrant alone did not authorize police to enter a third party’s home. The

Court explained that in this situation, unlike in Payton, “two distinct interests” protected

by the Fourth Amendment are at stake: not only “[the suspect’s] interest in being free from

an unreasonable seizure,” but also “[the third party’s] interest in being free from an

unreasonable search.” Id. at 216. While an arrest warrant may adequately protect the

former interest, it does “absolutely nothing to protect [the third party’s] privacy interest in

being free from an unreasonable invasion and search of [her] home.”               Id. at 213.

Consequently, the Steagald Court held that, absent exigent circumstances or consent, the

Fourth Amendment requires police to obtain a search warrant before trying to apprehend

the subject of an arrest warrant in a third party’s home. Id. at 216.

       Because the officers in this case assertedly believed that Brinkley resided in the

Stoney Trace apartment — and entered it pursuant solely to the authority of the arrest

warrant — Payton’s framework applies. We next consider what, exactly, Payton requires.




                                              9
                                             B.

       The courts of appeals have unanimously interpreted Payton’s standard — “reason

to believe the suspect is within,” 445 U.S. at 603 — to require a two-prong test: the officers

must have reason to believe both (1) “that the location is the defendant’s residence” and

(2) “that he [will] be home” when they enter. United States v. Hill, 649 F.3d 258, 262 (4th

Cir. 2011). But the quantum of proof necessary to satisfy Payton has divided the circuits,

with some construing “reason to believe” to demand less than probable cause and others

equating the two standards. See United States v. Vasquez-Algarin, 821 F.3d 467, 474–77

(3d Cir. 2016) (collecting cases).

       In Hill, 649 F.3d 258, we declined to join either camp, reasoning that the police

there had not satisfied even the lower standard. Id. at 263. In this case, however, we cannot

reach a conclusion as to Payton’s first prong — which was not at issue in Hill — without

first determining the quantum of proof that reasonable belief requires, and so we must

answer that question today.

       The courts that interpret reasonable belief to demand less than probable cause have

done so with scant explanation. See Vasquez-Algarin, 821 F.3d at 474. They simply rest

on the logic “that the Supreme Court in Payton used a phrase other than ‘probable cause’

because it meant something other than ‘probable cause.’” United States v. Thomas, 429

F.3d 282, 286 (D.C. Cir. 2005). At first blush, that certainly seems reasonable. But the

courts that have endorsed the view that reasonable belief amounts to probable cause rely

on two more compelling rationales.



                                             10
       The first is that the Supreme Court itself has often used language apparently

equating “reason to believe” with probable cause. See Vasquez-Algarin, 821 F.3d at 475–

78; United States v. Jackson, 576 F.3d 465, 469 (7th Cir. 2009); United States v. Hardin,

539 F.3d 404, 416 n.6 (6th Cir. 2008). Years before Payton, for instance, the Court

concluded that “police had probable cause to search [a] car” when observations gave them

“reason to believe that the car was used in the commission of [a] crime.” Cardwell v.

Lewis, 417 U.S. 583, 592 (1974). Similarly, the Court has instructed “that ‘the substance

of all the definitions of probable cause is a reasonable ground for belief of guilt.’”

Maryland v. Pringle, 540 U.S. 366, 371 (2003) (alteration omitted) (quoting Brinegar v.

United States, 338 U.S. 160, 175 (1949)). And strikingly, in Maryland v. Buie, 494 U.S.

325 (1990), the Court used the language of probable cause to find Payton’s reasonable

belief standard satisfied, holding that officers with “an arrest warrant and probable cause

to believe [the suspect] was in his home . . . were entitled to enter and to search” for him

within. Id. at 332–33.

       The second is that, as the Third Circuit reasoned in Vasquez-Algarin, 821 F.3d at

477–80, interpreting Payton’s reasonable belief to amount to probable cause is most

consistent with the special protections that the Constitution affords to the home. The home

has long enjoyed “pride of place in our constitutional jurisprudence.” Id. at 478; see, e.g.,

Florida v. Jardines, 569 U.S. 1, 6 (2013); Silverman v. United States, 365 U.S. 505, 511

(1961). Indeed, Payton itself reiterated that “the physical entry of the home is the chief

evil against which the wording of the Fourth Amendment is directed.” 445 U.S. at 585

(internal quotation marks omitted).

                                             11
       Steagald sheds particular light on how Payton must be interpreted to respect the

home’s privileged status under the Fourth Amendment. As noted above, when officers

armed with an arrest warrant seek to apprehend the suspect in a third party’s home,

Steagald, not Payton, controls, and requires police to obtain a search warrant founded on

probable cause in order to enter the home. But Payton controls when officers believe that

the suspect resides in a certain home, even if they are mistaken. See Vasquez-Algarin, 821

F.3d at 472. Under these circumstances, the home’s actual residents are no longer entitled

to the judicial authorization founded on probable cause that Steagald guarantees; Payton’s

“reason to believe” standard is all that protects their weighty Fourth Amendment privacy

interests. Thus, when police seek to enter a home and are uncertain whether the suspect

resides there, interpreting reasonable belief to require less than probable cause “would

effect an end-run around . . . Steagald and render all private homes . . . susceptible to

search by dint of mere suspicion or uncorroborated information and without the benefit of

any judicial determination.” Id. at 480.

       It seems to us that interpreting reasonable belief to require probable cause hews

most closely to Supreme Court precedent and most faithfully implements the special

protections that the Fourth Amendment affords the home. For these reasons, we join those

courts “that have held that reasonable belief in the Payton context ‘embodies the same

standard of reasonableness inherent in probable cause.’” Id. (quoting United States v.

Gorman, 314 F.3d 1105, 1111 (9th Cir. 2002)).




                                           12
                                             C.

       Applying these requirements here means that before entering the Stoney Trace

apartment without a search warrant, the police needed to have probable cause to believe

that Brinkley resided there and would be present when they entered. See Hill, 649 F.3d at

262. We consider the totality of the circumstances in assessing probable cause. Florida v.

Harris, 568 U.S. 237, 244 (2013). The “quantity and quality” of information known to

officers bear on whether they have probable cause, with less reliable information requiring

more corroboration. See Alabama v. White, 496 U.S. 325, 330 (1990). With these

principles in mind, we turn to Payton’s first prong.



                                            III.

       The police could satisfy Payton’s first prong only if the information known to them

at the time they entered the Stoney Trace apartment provided them with probable cause

that Brinkley resided there — that is, if the information sufficed for a person of reasonable

prudence to believe that Brinkley resided there. See Ornelas, 517 U.S. at 696. In

investigating Brinkley’s residence, Agent Murphy relied exclusively on Detective Stark.

Detective Stark’s conclusion that Brinkley resided in the Stoney Trace apartment rested on

two entries on CJLEADS and Brinkley’s public Facebook.               This information was

somewhat sparse, in that police officers typically rely on considerably more evidence to

establish reasonable belief as to a suspect’s residence. See Vasquez-Algarin, 821 F.3d at

482; Hardin, 539 F.3d at 421–22; see also, e.g., United States v. Hamilton, 819 F.3d 503,

507 (1st Cir. 2016) (police found the defendant’s address in an arrest warrant, postal

                                             13
records, a “public database, booking reports, a National Insurance Crime Bureau accident

report, and credit bureau reports”); United States v. Route, 104 F.3d 59, 61 n.1 (5th Cir.

1997) (police found the defendant’s address in his credit card applications, his car

registration, and an electric and water bill in his name and verified that the defendant

received mail there). Probable cause, however, looks to the totality of the circumstances

and does not require any particular source or kind of information.             Accordingly,

information gleaned from online sources like CJLEADS and Facebook could be enough to

establish probable cause of a suspect’s residence in some situations.

       But here, the information Detective Stark gathered from CJLEADS did not point to

just one address but rather indicated that Brinkley might well be transient. Although the

two most recent entries that the detective found linked Brinkley to the Stoney Trace

apartment, many others — including the two immediately preceding entries, one added just

five days earlier 3 — linked Brinkley to other addresses. J.A. 154. The utility bill in

Brinkley’s name that the ATF analyst initially uncovered was associated with not the

Stoney Trace apartment but a different address. J.A. 125–26. This consistent pattern of


       3
         The dissent calls into question the accuracy of the date associated with this entry,
December 28, 2016. See Dissenting Op. at 39 n.11. But as Detective Stark explained,
“[t]he dates [on CJLEADS] before February 2nd probably would not have changed . . . if
it’s anything more than a month [before February 2nd] it’s probably there and present with
what it was” when Detective Stark first searched for Brinkley on CJLEADS. J.A. 88
(confirming that the entry for Planters View Drive is dated December 28, 2016). Thus, we
do not, as the dissent suggests, look upon the CJLEADS entries “with less-than-expert
eyes” and draw our own conclusions. Dissenting Op. at 38. Rather, we rely on Detective
Stark’s expert knowledge of the database’s inner workings. See id. at 39–40 (observing
that officers like Detective Stark “often review and navigate [CJLEADS] to determine the
date” of “addresses [that] are entered and updated”).

                                             14
inconsistent addresses suggests that Brinkley may have tended to stay temporarily in

various places rather than residing at any one address. In fact, Agent Murphy himself

acknowledged that it was “common for someone like Mr. Brinkley . . . to have more than

one place where they will stay the night from time to time.” 4 J.A. 126.

       But the officers investigated only one place. “[P]olice may rely on the totality of

facts available to them in establishing probable cause,” but they cannot “disregard facts

tending to dissipate probable cause.” Bigford v. Taylor, 834 F.2d 1213, 1218 (5th Cir.

1988); accord Hernandez v. United States, 939 F.3d 191, 201 (2d Cir. 2019). The utility

bill in Brinkley’s name initially led Agent Murphy to believe that Brinkley resided at the

address associated with it, J.A. 125–26 — and with good reason, as utility bills typically

constitute strong evidence of a defendant’s residence. See United States v. Graham, 553

F.3d 6, 13 (1st Cir. 2009). But the officers did not look into this address. Nor did they

look into any of the numerous other addresses Detective Stark found on CJLEADS, even

those listed multiple times. J.A. 154. Had the officers ruled out any of these alternatives,

it could have bolstered their theory that Brinkley resided in the Stoney Trace apartment.

See id. (officers ruled out prior residence); cf. United States v. Young, 835 F.3d 13, 21 (1st

Cir. 2016) (no reasonable belief as to residence even where officers eliminated three other




       4
        Similarly, Detective Stark testified that, based on the CJLEADS entries and other
available information, he believed that Brinkley might be found at multiple addresses. J.A.
89 (explaining that while he “believed that [Brinkley] was staying at Stone Trace Drive,”
he also “believed it might be possible to find him at those other addresses” listed on
CJLEADS). Accordingly, the suggestion that Brinkley might be transient originated not
with us but with both experienced officers.
                                             15
possibilities). But because they did not examine any other possibilities, everything hinged

solely on their investigation into that one address.

       Pursuant to Payton and Steagald, the officers needed to establish reason to believe

not just that Brinkley was staying in the Stoney Trace apartment but that he resided there.

If Brinkley was merely staying as a guest in someone else’s home, Steagald would require

the officers to obtain a search warrant before they could enter it. Detective Stark’s

discovery that Brinkley was involved with Chisholm, and that Chisholm was associated

with the Stoney Trace apartment, certainly provided additional evidence that Brinkley

might well have stayed at Chisholm’s home, but it did not speak to whether he did so as a

resident or as Chisholm’s overnight guest. See United States v. Werra, 638 F.3d 326, 338

(1st Cir. 2011). Further investigation was necessary to establish probable cause that

Brinkley resided there. 5

       Police often conduct such further investigation by going to the suspected residence,

where they can obtain “recent, eyewitness evidence connecting the suspect to the residence,

and often even [observe] conduct by the suspect that demonstrates a tie to the residence” —


       5
         The dissent, which repeatedly refers to Chisholm as Brinkley’s “fiancée,”
Dissenting Op. at 35, 44, contends that Detective Stark “believed” that Chisholm and
Brinkley were “living together before marriage” on Stoney Trace Drive, id. at 41. This
contention finds scant support in the record. Detective Stark did refer to a single
photograph on Brinkley’s Facebook page in which Brinkley “appeared to be engaged” to
Chisholm, but in the next sentence of his testimony, the detective explained that he
“believed they were in a dating relationship.” J.A. 73. (emphasis added). All other
testimony by the officers, and even submissions by the Government, either describe
Chisholm and Brinkley as “boyfriend and girlfriend,” J.A. 111, 158, or “dating,” J.A. 26,
75, 89, 133, 142. Nothing in the record supports the dissent’s claim that the officers
“believed” that Brinkley and Chisholm were “living together before marriage.” Dissenting
Op. at 41.
                                             16
“common feature[s]” of cases finding that police satisfied Payton’s first prong. Hardin,

539 F.3d at 421. Officers gather this kind of evidence, for example, by conducting

surveillance at the suspected residence. See Hamilton, 819 F.3d at 505 (“police installed a

pole camera on [the street outside the residence] for surveillance purposes”); United States

v. Barrera, 464 F.3d 496, 498–99 (5th Cir. 2006) (officers found three vehicles associated

with the suspect at the residence). They also talk to people at or near the residence to gather

information from them. See Graham, 553 F.3d at 13 (police corroborated an address from

an incident report by, inter alia, showing a picture of the suspect to a person outside the

residence); Hardin, 539 F.3d at 407 (officers asked property manager who leased the

apartment in question); United States v. Lovelock, 170 F.3d 339, 344–45 (2d Cir. 1999)

(police confirmed address listed on suspect’s arrest warrant with two tenants in building).

In short, going to the residence in question opens several possible avenues for the police to

gather information about whether the suspect in fact resides there.

       The officers in this case explained that they went to the Stoney Trace apartment with

precisely this investigatory intent in mind. Detective Stark testified that they planned to

conduct a “knock-and-talk” at the door of the apartment. J.A. 76. Agent Murphy

confirmed that their intent in doing so “was to interview the occupants to find out if Mr.

Brinkley was indeed there.” J.A. 113. He further explained that when the officers began

speaking with Chisholm at the doorstep, he still intended “to basically secure the area and

sit up on the house and wait to see if Mr. Brinkley left.” J.A. 134. And when the officers

doubted Chisholm’s assertion that Brinkley was not inside, Detective Stark “asked for her



                                              17
permission . . . to come through and just do a walk through to make sure that he was indeed

not at the residence.” J.A. 115.

       That the officers went to the apartment to obtain more information to establish that

Brinkley resided there underscores that at the time of their arrival, they had a “limited basis

to believe” that he did. Vasquez-Algarin, 821 F.3d at 481. On the doorstep of the

apartment, the police officers did talk to an occupant, but they gathered no evidence as to

whether this was Brinkley’s residence. 6 The police officers did not even ask Chisholm if

Brinkley resided there, but only if he was present — a critical difference under Steagald.

The unexpected arrival of five armed officers apparently led Chisholm to grow nervous as

they pressed her to allow them to enter. And the officers heard someone, or something,

moving inside. But these facts did not establish that Brinkley resided in the home. At the

time they entered the Stoney Trace apartment, all the officers had was the same “limited

basis to believe” that Brinkley resided there that they had when they knocked on the door.

       Of course, “the police need not possess . . . rock-solid indicators of residence in

order to form a ‘reasonable belief’ that a suspect resides at a given place.” Graham, 553

F.3d at 13. But we have seen no case finding Payton’s first prong satisfied on evidence as

thin as the evidence here. The information known to the officers suggested that Brinkley

may have stayed temporarily in several places. The officers, however, investigated only



       6
        If anything, the information they learned raised more questions about whether
Brinkley resided there than it answered. For the officers found not just Chisholm but also
Prigon, a woman completely foreign to them, folding laundry in pajamas, as a resident
would.

                                              18
one. Though the officers developed a well-founded suspicion that Brinkley might have

stayed in the Stoney Trace apartment at times, they failed to establish probable cause that

he resided there. And because the officers entered the apartment pursuant solely to the

authority of the arrest warrant, under Payton and its progeny, their entry was unlawful. 7



                                            IV.

       Even if the available information were enough to give police reason to believe that

Brinkley resided in the Stoney Trace apartment and so satisfy Payton’s first prong, the

evidence here falls far short of satisfying Payton’s second; that is, the officers failed to

establish probable cause that Brinkley would be present in the home when they entered.

       In determining reasonable belief as to a suspect’s presence, courts assess the signs

of presence known to officers before they enter a home. See Graham, 553 F.3d at 14.

Though we now know that the officers’ belief that Brinkley would be present proved to be


       7
         Our determination that the officers failed to establish probable cause in no way
denigrates their years of experience. Nor does it suggest that we have not given “due
weight” to the “reasonable inferences” they drew “in light of [their] experience.” Terry v.
Ohio, 392 U.S. 1, 27 (1968); accord Ornelas, 517 U.S. at 699. But experience does not
establish probable cause. See 2 Wayne R. LaFave, Search & Seizure § 3.2(c) (6th ed. 2020)
(observing that “experience, without more, is not a fact to be added to the quantum of
evidence to determine if probable cause exists, but rather a lens through which courts view
the quantum of evidence”) (quotation marks and emphasis omitted). Experienced officers
like Agent Murphy and Detective Stark may not render the probable cause requirement a
“toothless tiger” through reliance on “cop-on-the-beat intuition[s].” United States v.
Rutkowski, 877 F.2d 139, 142 (1st Cir. 1989). Rather, their actions — like those of all law
enforcement officers — must be “judged against an objective standard” with a familiar
lodestar: whether the available information sufficed for a “man of reasonable caution” to
believe that the search was warranted. Terry, 392 U.S. at 22. Contrary to the dissent’s
intimations, Dissenting Op. at 42, even experienced officers may sometimes fail to meet
this standard.
                                            19
correct, the Fourth Amendment demands that we “prevent hindsight from coloring the

evaluation of the reasonableness of a search or seizure.” Martinez-Fuerte, 428 U.S. at 565.

       The Government points to six factors assertedly supporting the officers’ belief that

Brinkley would be present in the Stoney Trace apartment: (1) the officers’ purportedly

reasonable belief that he resided there; (2) the morning hour (8:30 AM); (3) Chisholm’s

delay in opening the door; (4) Chisholm’s nervousness; (5) the sounds of movement in the

apartment; and (6) Chisholm and Prigon’s looks toward the back of the apartment.

Response Br. at 26–28.

       A substantiated belief as to a suspect’s residence is especially important. See Werra,

638 F.3d at 340 (“The fact that an individual is known to live at a particular location is one

sound reason to expect him or her to be there.”). But an ill-founded belief about a suspect’s

residence does not, and cannot, shore up a belief about his presence there. In Hill, for

instance, we noted that police went to the defendant’s suspected residence “to gain

information” and “had documented another primary residence” for the defendant, and we

discounted the probative value of other indicia of the defendant’s presence accordingly.

649 F.3d at 264. Here, too, the officers went to the Stoney Trace apartment to gather more

information. J.A. 89, 113. Moreover, while in Hill the police knew of only one other

possible primary residence, in this case the officers had documented multiple other possible

primary residences for Brinkley. Unlike in Hill, where the defendant’s girlfriend told

police that the defendant resided in the home that the officers entered, id. at 261 — and the

defendant himself had previously told an officer that he had recently moved to the city



                                             20
where the home was located, id. — police here had no firsthand information about where

Brinkley resided.

       The officers’ uncertainty as to Brinkley’s residence undermines the evidentiary

strength of any possible signs of his presence. See Werra, 638 F.3d at 339 (discounting

the probative value of time-of-day evidence for this reason). When police know a suspect

lives somewhere, generic indicia of presence may suggest that he is there, but when police

are uncertain about where he lives, the same signs suggest only that someone is there —

not necessarily the suspect. In this case, counting the officers’ investigation into whether

Brinkley resided in the Stoney Trace apartment as evidence that he would be found inside

would condone “bootstrapping,” allowing police to establish reasonable belief of presence

by poking around a suspected residence until they find “mere signs of life inside.”

Vasquez-Algarin, 821 F.3d at 482. With the officers’ uncertainty about where Brinkley

resided in mind, we look to the other factors to determine whether they established probable

cause that he would be present.

       The hour and Chisholm’s delay in opening the door offer meager support for the

officers’ belief under these circumstances.      It may be reasonable to assume that an

unemployed person would be home at 8:30 AM. See United States v. Magluta, 44 F.3d

1530, 1536 (11th Cir. 1995); United States v. Lauter, 57 F.3d 212, 215 (2d Cir. 1995). But

here the officers did not know whether Brinkley was employed; Agent Murphy

acknowledged that Brinkley might not have been home at 8:30 AM because “[h]e may

have gone to work.” J.A. 134. Cf. Werra, 638 F.3d at 340 (not reasonable to assume

suspect would be home at 10:00 AM without information about her employment status).

                                            21
And as to the purported delay, Detective Stark testified that Chisholm answered the door

no more than two minutes after the officers knocked. J.A. 77. Two minutes is not an

unusual amount of time for a woman, in her pajamas, to respond to an unanticipated knock,

at 8:30 AM. We do not evaluate the totality of the circumstances by running through a list

of factors and ticking off each individually. See Harris, 568 U.S. at 244. But viewing both

of these factors in tandem with the others, we cannot see how they support probable cause

to believe that Brinkley was present in the apartment.

       We are left with the noises in the apartment and Chisholm and Prigon’s reactions to

them and to the police officers. Unlike the “unresponsive noises” in Hill, “which could

have been voices or a television,” 649 F.3d at 264, the sounds of active movement here at

least indicated that some living being was present. But as in Hill, these sounds were not

particularized to the suspect; “at best, the police had reason to believe that someone was

present.” Id. (emphasis added). The same goes for Chisholm and Prigon looking toward

the source of the noises. Their looks toward the back of the apartment were typical

reactions to any source of noises. The noises could have been made by anyone, including

a child (and police knew that children might be present in the apartment, J.A. 90, 127) or a

grandparent, or even a pet. Prigon’s unanticipated presence accentuates the point: the

officers observed one entirely unexpected person in the apartment before they entered, and

they had no reason to think that the noises came from Brinkley rather than some other

unknown person.

       The only evidence that someone was present that was even arguably particularized

to Brinkley was Chisholm’s nervousness. But “[i]t is common for most people to exhibit

                                            22
signs of nervousness when confronted by a law enforcement officer whether or not the

person is currently engaged in criminal activity.” United States v. Massenburg, 654 F.3d

480, 490 (4th Cir. 2011) (alteration omitted) (quoting United States v. Salzano, 158 F.3d

1107, 1113 (10th Cir. 1998)). Here Chisholm was confronted by five armed officers

crowding the door to her apartment. The Government nonetheless insists that Chisholm’s

nervousness was a response to the officers’ questions about Brinkley. But police here did

not merely ask if Brinkley was inside or where he might be. From their very first question,

the officers conveyed their intent to enter the apartment. J.A. 96, 128. Throughout the

conversation, they consistently pressed Chisholm to permit them to enter the apartment.

J.A. 79, 115. Chisholm could have been nervous at the prospect of exposing any number

of people — for example, an elderly parent or a young child — to five armed policemen.

       Chisholm might also have feared for herself. Recent events have underscored how

quickly police encounters with Black Americans may escalate, at times fatally. See Estate

of Jones v. City of Martinsburg, 961 F.3d 661, 673 (4th Cir. 2020). 8 “[W]e recognize that

our police officers are often asked to make split-second decisions,” id., and we respect the


       8
         Two months after this case was argued, police in Louisville, Kentucky, barged into
the home of Breonna Taylor, a 26-year-old emergency medical technician. The officers
entered Taylor’s home pursuant to a search warrant, which they obtained to investigate a
suspected drug dealer who was purportedly associated with the residence. See Tessa
Duvall & Darcy Costello, Louisville Police Pursued “No-Knock” Search Warrant in Fatal
Shooting of ER Tech in Her Home, Louisville Courier J. (June 9, 2020), https://
www.courier-journal.com/story/news/2020/05/12/breonna-taylor-louisville-emt-not-main-
target-drug-investigation/3115928001/ [https://perma.cc/3UGF-XQHA]. The officers
found neither the suspect nor any drugs in the home, but they shot Taylor eight times,
killing her. And this tragedy is hardly an anomaly. See, e.g., Kimberlé Crenshaw, “You
Promised You Wouldn’t Kill Me,” N.Y. Times (Oct. 28, 2019), https://www.nytimes.com/
2019/10/28/opinion/police-black-women-racism.html [https://perma.cc/6QRN-KUHL].
                                            23
challenges that law enforcement officers face in the service of our communities. But we

cannot ignore this context when making sense of how someone reacted to five armed

officers at her door. That would make anyone nervous — including Chisholm, whether

Brinkley was inside the apartment or not. And we cannot conclude that Chisholm’s

understandable response gave rise to probable cause that Brinkley was present within.

       To the contrary, Chisholm’s reluctance to allow the officers to enter her home

without a warrant to do so goes to the “very core” of the Fourth Amendment: “the right of

a man to retreat into his own home and there be free from unreasonable governmental

intrusion.” Silverman, 365 U.S. at 511. That right would not mean much if all officers

needed to enter a private home was a hunch about a suspect’s presence and a resident’s

understandably nervous reaction to the officers’ questioning. Cf. Jardines, 569 U.S. at 6

(“This right would be of little practical value if the State’s agents could stand in a home’s

porch or side garden and trawl for evidence with impunity . . . .”).

       Like Hill, 649 F.3d at 260, this case is ultimately about the “centuries-old principle

of respect for the privacy of the home.” Wilson v. Layne, 526 U.S. 603, 610 (1999). In

recognition of this constitutionally enshrined principle, “law enforcement officers often

rely on independent investigation and observations of the premises to determine whether a

suspect is actually inside before entering.” El Bey v. Roop, 530 F.3d 407, 417 (6th Cir.

2008). But police here conducted no independent investigation or observation of the

Stoney Trace apartment to determine whether Brinkley was within. They stacked a hunch

about Chisholm’s nervousness atop a hunch about Brinkley’s residence.



                                             24
       When police have limited reason to believe a suspect resides in a home, generic

signs of life inside and understandably nervous reactions from residents, without more, do

not amount to probable cause that the suspect is present within. This conclusion follows

from Hill, which for the sake of argument applied the less demanding interpretation of

reasonable belief and found even that not met. 649 F.3d at 263. If police could not satisfy

that lower standard with generic signs of life coming from a suspect’s known residence,

they surely cannot establish probable cause that a suspect is present based on generic signs

of life coming from a potential but uncorroborated residence. All of the facts the officers

in this case relied on, viewed together, did not give rise to reason to believe that Brinkley

would be present in the Stoney Trace apartment when they entered. To hold otherwise

would gut “the most stringent Fourth Amendment protection” that “private dwellings [are]

ordinarily afforded.” Martinez-Fuerte, 428 U.S. at 561.

                                             V.

       We hold that reasonable belief amounts to probable cause, and that the police in this

case lacked reason to believe Brinkley resided in the Stoney Trace apartment and would

be present when they entered. The Fourth Amendment requires a more rigorous showing

of cause before officers may lawfully enter a private home under these circumstances.

        Accordingly, we reverse the district court’s denial of Brinkley’s suppression

motion and vacate Brinkley’s convictions on the two counts at issue. We also vacate

Brinkley’s sentence, see United States v. Pratt, 915 F.3d 266, 275 (4th Cir. 2019), and we

remand the case for further proceedings consistent with this opinion.

                                              REVERSED, VACATED, AND REMANDED

                                             25
RICHARDSON, Circuit Judge, dissenting:

       If equipped with an arrest warrant “founded on probable cause,” officers have “the

limited authority to enter a dwelling in which the suspect lives when there is reason to

believe the suspect is within.” Payton v. New York, 445 U.S. 573, 603 (1980) (emphasis

added). Though the Supreme Court used the phrase “reason to believe,” my colleagues in

the majority hold that officers must have “probable cause to believe that [the suspect]

resided [at the dwelling] and would be present when they entered.” Majority Op. 13

(emphasis added). This divergence from what the Supreme Court said is not without some

support. But I would follow the words used in Payton until I am told otherwise.

       And yet, the majority did not need to wade into this morass. Whatever the standard,

the officers here had enough to enter an apartment to arrest Kendrick Brinkley. Those

experienced officers made reasonable inferences that deserve our respect. Rather than

respecting those inferences and the district court who agreed with them, the majority

invents its own inferences with little support from a database with which judges have

precious little experience. I respectfully dissent.

I.     Background

       Experienced law enforcement, state and federal, 1 sought to arrest Brinkley on an

outstanding arrest warrant. To find him, they turned to a North Carolina law-enforcement

database, Criminal Justice Law Enforcement Automated Data Services (CJLEADS).



       1
         Detective Robert Stark had served as a police officer for twelve years. J.A. 63.
Special Agent Jason Murphy had worked for the ATF for nine years and had served in
other law-enforcement positions for more than seven years before that. J.A. 110.
                                              26
Using that information, along with court records and Facebook, the officers identified

Brinkley’s most probable residence as being an apartment on Stoney Trace Drive.

       The two most recent records in CJLEADS linked Brinkley to the Stoney Trace

address. The first record, from just a month earlier, involved a “ticket citation issued [to

Brinkley] for driving while [his] license [was] revoked.” J.A. 65. Cross-referencing the

North Carolina Courts’ system confirmed that Brinkley had provided the Stoney Trace

address during the traffic stop. A second record, this one from the Department of

Corrections, linked Brinkley to the Stoney Trace address. From this record, the officer

concluded that Brinkley gave the Stoney Trace address to his probation officer “as Mr.

Brinkley was on probation at the time.” J.A. 65. And Brinkley’s own counsel agreed this

second address was the “probation office[’s] indication that that was his residence.” J.A.

137. So it was no surprise that the district court found that Stoney Trace was the “place

that [Brinkley] gave as a residence.” J.A. 145; see also J.A. 144 (concluding that the

database provided “indicators of Mr. Brinkley giving that as an address, recent in time”)

       The Stoney Trace address that Brinkley provided was corroborated by information

from Facebook. Brinkley’s Facebook page showed that Brinkley was engaged to or dating

Brittany Chisholm. CJLEADS identified Chisholm’s address as the same Stoney Trace

address, which the officers felt helped confirm that Brinkley resided there. The district

court agreed.

       Considering this information together, the lead officers (Detective Stark and Special

Agent Murphy) concluded that Brinkley “was residing at the Stoney Trace address.” J.A.

74–75. While other addresses “had been provided over a number of years . . . [t]hey

                                            27
appeared [to Detective Stark] to be family-associated addresses.” J.A. 74. As one officer

explained, the law-enforcement database had no other addresses “within the [prior] year

that [they] felt w[ere] credible as a place [Brinkley] was living.” J.A. 112–113, 126.

       Having concluded that Brinkley likely resided on Stoney Trace, the officers went

“to interview the occupants to find out if Mr. Brinkley was indeed there.” J.A. 113. After

arriving around 8:30am, they knocked on the front door wearing clothing identifying

themselves as law enforcement. After hearing movement inside for “just about a minute,”

they knocked “a few more times and announced ‘police’” because “nobody was coming to

the door.” J.A. 77, 114. Eventually, a female voice asked who was there, and the officers

responded that it was the police. After another “minute’s worth of movement,” a pajama-

clad Chisholm “opened [the front door] slowly” to about “[a] full body length wide” so

that Detective Stark “could see all the way inside the apartment.” J.A. 77.

       When asked if Brinkley was inside, Chisholm “became very nervous. Her body

tensed. Her breathing quickened. She looked back into the apartment and said, ‘He’s not

here.’” J.A. 78. She “looked back over her shoulder . . . multiple times.” J.A. 78. When

told that the officers were there to serve an arrest warrant for Brinkley, “Chisholm become

more and more . . . nervous . . . constantly looking behind her, stammering, [ ] never really

giv[ing] full answers.” J.A. 115.

       While talking to Chisholm, the officers could hear movement coming from the

bedroom area. J.A. 79, 115–16. A second woman, later identified as Jermica Prigon,

crossed from the kitchen to the living room in her pajamas and appeared to be “messing

with [ ] folding clothes or something.” J.A. 79, 116. When another noise came from the

                                             28
bedroom area, the officers saw Prigon “snap[] her head back towards that area to look.”

J.A. 116. And each time the officers told Chisholm that they believed Brinkley was inside,

she “would kind of do . . . a subconscious . . . look back over her shoulder towards the back

of the apartment.” J.A. 117.

       Based on the noise from the bedroom area, Chisholm’s movement and demeanor,

Prigon’s actions, and the time of day, the officers “believed . . . 100 percent that Mr.

Brinkley was hiding in the apartment.” J.A. 134; see also J.A. 81, 117.

       The officers then entered the apartment and, unsurprisingly, found Brinkley in the

bedroom’s hallway. A protective sweep revealed digital scales, a plastic baggie with

suspected crack cocaine, and ammunition in a clear box. After obtaining a search warrant,

the officers also found three guns.

       After Brinkley was indicted, he sought to suppress the seized evidence. The district

court held a hearing and found that the officers reasonably believed that Brinkley lived at

the Stoney Trace address and that he was there when they entered. The district court based

its conclusion on: (1) Detective Stark’s CJLEADS and Facebook research, (2) Chisholm’s

“nervousness” which “[c]ould be explained by the fact that law enforcement was at the

door” but “also [was] highly likely to be connected to . . . [the fact that] they were looking

for Mr. Brinkley,” (3) Chisholm’s demeanor and constant looking back, (4) Prigon’s

looking back toward the bedroom, (5) the noise inside the apartment and the “two women

looking back at the direction of the noise,” (6) Detective Stark recognizing Chisholm as

Brinkley’s girlfriend, tying “Chisholm to that address, and [tying] the defendant” to it, and



                                             29
(7) that the officers were there “early in the morning on a week day when a resident would

likely be at home.” J.A. 144–47.

II.    Legal Framework

       As the majority points out, “a private home . . . is ‘afforded the most stringent Fourth

Amendment protection.’” Majority Op. 8 (quoting United States v. Martinez-Fuerte, 428

U.S. 543, 561 (1976)). That said, officers seeking to execute an arrest warrant may “enter

a dwelling in which [a] suspect lives when there is reason to believe the suspect is within.”

Payton, 445 U.S. at 603 (emphasis added). Courts have disagreed on what the Supreme

Court meant when it said “reason to believe.” Is “reason to believe” the same as “probable

cause,” as the majority suggests? Or does “reason to believe” merely require a “reasonable

belief,” which may be less than probable cause to believe? 2

       One might read inconsistency into the Supreme Court’s use of the terms “reason to

believe” or “reasonable belief.” As the majority points out, there is some language in

Supreme Court opinions that could be read to equate “reason to believe” with “probable

cause.” See Majority Op. 11 (citing Maryland v. Pringle, 540 U.S. 366, 371 (2003);


       2
         Some circuits have equated “reason to believe” and “probable cause.” See United
States v. Vasquez-Algarin, 821 F.3d 467, 480 (3d Cir. 2016); United States v. Gorman, 314
F.3d 1105, 1111 (9th Cir. 2002). Others have suggested the same in dicta. See United
States v. Jackson, 576 F.3d 465, 469 (7th Cir. 2009); United States v. Hardin, 539 F.3d
404, 416 n.6 (6th Cir. 2008). On the other hand, some circuits have found that the “reason
to believe” standard is less stringent than the “probable cause” standard. See United States
v. Thomas, 429 F.3d 282, 286 (D.C. Cir. 2005); Valdez v. McPheters, 172 F.3d 1220, 1225
n.5 (10th Cir. 1999); United States v. Lauter, 57 F.3d 212, 215 (2d Cir. 1995); United States
v. Werra, 638 F.3d 326, 337 (1st Cir. 2011). And still others have side-stepped the
problem. See United States v. Barrera, 464 F.3d 496, 501 n.5 (5th Cir. 2006); United States
v. Risse, 83 F.3d 212, 216 (8th Cir. 1996); United States v. Magluta, 44 F.3d 1530, 1535
(11th Cir. 1995).
                                              30
Cardwell v. Lewis, 417 U.S. 583, 592 (1974)). But other times, the Supreme Court more

plainly equates “reason to believe” with “reasonable suspicion.” See Terry v. Ohio, 392

U.S. 1, 27 (1968) (An officer may conduct a reasonable search “where he has reason to

believe that he is dealing with an armed and dangerous individual, regardless of whether

he has probable cause to arrest.”). Compare Maryland v. Buie, 494 U.S. 325, 337 (1990)

(A protective sweep is permitted when a “reasonable belief” exists that an area harbors a

dangerous individual (emphasis added)), with id. at 335–36 (“The sweep lasts no longer

than is necessary to dispel the reasonable suspicion of danger.” (emphasis added)).

      As an inferior court judge, I must follow the Supreme Court’s guidance. And

although we are left with few tools to reconcile the Supreme Court’s cases in this area,

what we have leads me to conclude that “reason to believe” means a “reasonable belief,”

which is equivalent to “reasonable suspicion.” First, Payton itself sets the standard as

“reason to believe the suspect is within.” Payton, 445 U.S. at 603. The Supreme Court

chose not to use the phrase “probable cause,” a phrase it knows how to use. Instead, the

Court used “reason to believe,” the same phrase it used in Terry, the seminal case on

reasonable suspicion. Terry, 392 U.S. at 27. 3 Second, in Buie, a case that the majority

relies on, the Supreme Court differentiates “reasonable belief” from “probable cause” by



      3
         If “reason to believe,” as Terry uses it, meant “probable cause,” then “reasonable
suspicion” would mean “probable cause.” And yet the Supreme Court has been clear that
Terry’s standard is “obviously less than is necessary for probable cause.” See Kansas v.
Glover, 140 S. Ct. 1183, 1187 (2020) (quoting Prado Navarette v. California, 572 U.S.
393, 397 (2014)).


                                            31
admonishing the Maryland court for requiring the higher probable cause standard and

demanding that it instead use the “reasonable belief” standard. See Buie, 494 U.S. at 336–

37. 4 I think it a more faithful reading of Payton to adhere to the words the Court used,

rather than words they did not. 5

III.   A “Reason to Believe” Existed

       But the dispute over what the Supreme Court meant when they used “reason to

believe,” at least here, should be academic. However one understands a “reason to

believe,” the officers had it here. Drawing on their experience, the officers drew inferences

from the information they had to conclude that Brinkley resided on Stoney Trace. And




       4
         The majority instead relies on Buie’s descriptive phrase that the officers possessed
“an arrest warrant and probable cause to believe Buie was in his home.” 494 U.S. at 332–
33 (emphasis added); see Majority Op. 11. This single sentence reflects only that the
Supreme Court believed that there was in fact “probable cause to believe Buie was in his
home.” See Buie v. State, 550 A.2d 79, 80 (Md. 1988) (explaining that the police were
surveilling Buie’s house and had placed a phone call to confirm he was there before
entering under an arrest warrant). The Supreme Court did not make a broader statement
that Payton required probable cause, particularly since Buie did not address the authority
of officers to enter a home pursuant to an arrest warrant.
       5
         I understand the majority to be concerned that reading Payton to permit warrantless
entries into homes with less knowledge than probable cause might “render all private
homes . . . susceptible to search by dint of mere suspicion or uncorroborated information
and without the benefit of any judicial determination.” Majority Op. 12 (quoting Vasquez-
Algarin, 821 F.3d at 480). But the majority creates a straw man, as “mere suspicion or
uncorroborated information” is far from how this Court has defined “reasonable belief.”
Instead, as the majority fails to recognize, “[a]n objectively reasonable belief,” although a
quantum of proof less than probable cause, still “must be based on specific articulable facts
and reasonable inferences that could have been drawn therefrom.” United States v. Yengel,
711 F.3d 392, 397 (4th Cir. 2012). This is worlds away from a “dint of mere suspicion”
that the majority has characterized the “reason to believe” standard as requiring. Majority
Op. 12 (quoting Vazquez-Algarin, 821 F.3d at 480).
                                             32
once at the residence, the circumstances provided a reason to believe that Brinkley was

home.

        Even using the majority’s probable-cause standard, the officers had “probable cause

to believe that Brinkley” (1) “resided [at the Stoney Trace address],” and (2) “would be

present when they entered.” Majority Op. 13. The majority disagrees. But in conducting

their analysis, the majority fails to give due weight to the inferences made by experienced

officers based on information in a law-enforcement database, a source that we as appellate

judges lack significant experience in interpreting.

        Probable cause is not weighed “in terms of library analysis by scholars, but as

understood by those versed in the field of law enforcement.” United States v. Dickey-Bey,

393 F.3d 449, 453 (4th Cir. 2004) (emphasis added) (quoting Illinois v. Gates, 462 U.S.

213, 232 (1983)). This last part is important. In determining whether probable cause exists,

this Court must use a “pragmatic, common sense approach, [ ] defer[ring] to the expertise

and experience of law enforcement officers at the scene.” Id. (citing Ornelas v. United

States, 517 U.S. 690, 699 (1996)). And we are to give “due weight to inferences drawn

from [the] facts by resident judges,” who, like local officers, “view[] the facts of a particular

case in light of the distinctive features and events of the community.” Ornelas, 517 U.S.

at 699. “The most precise instrument that the judiciary possesses for ensuring the proper

balance between the interests that under-gird the Fourth Amendment is the on-the-ground

assessment of district courts.” United States v. Bumpers, 705 F.3d 168, 173 (4th Cir. 2013).

Local officers and local judges are in a better position, based on their experience in their

own communities, to make logical inferences from facts on the ground. Ornelas, 517 U.S.

                                               33
at 699. And when a resident judge agrees with the officers, we should be particularly

cautious about rejecting the agreed-upon inferences. 6

       The majority errs by rejecting law enforcement’s inferences and replacing them with

its own inferences drawn from a sliver of information. And, in doing so, the majority fails

to “construe the evidence in the light most favorable to the Government, the prevailing

party below,” as we must do. United States v. Seidman, 156 F.3d 542, 547 (4th Cir. 1998).

       A.     The officers had probable cause to believe Brinkley resided at the Stoney
              Trace address

       The information known and the inferences made by these experienced officers

provided probable cause that Brinkley resided at the Stoney Trace address. See J.A. 89,

134. And the information developed when officers visited that address only confirmed that

reasonable belief.

       Detective Stark testified that the two most recent CJLEADS results pointed to the

Stoney Trace address as Brinkley’s residence. That address had been provided once to an

officer and once to the Department of Corrections. And it was new. This led Detective



       6
         This does not mean that we defer to local law enforcement’s subjective belief that
probable cause exists. United States v. Gray, 137 F.3d 765, 769 (4th Cir. 1998). That
subjective belief is owed no deference. But the underlying inferences they make from the
facts are entitled to deference. And again, this is not controlling weight: after all, “while
officers have the advantage of experience, they do not necessarily have the advantage of
neutrality.” United States v. Johnson, 599 F.3d 339, 343 (4th Cir. 2010). But, “that is
where the district courts come in.” Id. And local district courts’ neutral inferences are to
be given not controlling, but “due weight,” at least as to their “finding[s] that [an] officer
was credible and the inference[s made were] reasonable.” Ornelas, 517 U.S. at 700. This
proposition is “an acknowledgement that satellite imagery often cannot replicate
community insights and on-the-ground intelligence.” Johnson, 599 F.3d at 344.

                                             34
Stark to believe that this address was not a “family-associated address[],” but his current

residence. J.A. 74. And this inference was supported by Brinkley’s fiancée’s link to that

address.

       Detective Stark made several inferences based on his experience in concluding that

the Stoney Trace address was Brinkley’s residence. First, Brinkley gave those supervising

his probation the Stoney Trace address as his residence. J.A. 65, 137. 7 Second, Brinkley

gave the Stoney Trace address as his residence to an officer during a traffic stop. J.A. 65.

Third, older addresses in the database were likely “family-associated addresses,” not

Brinkley’s current residence. J.A. 74. Fourth, it is common for someone to live with their

significant other. And finally, given that the two most recent CJLEADS results listed the

same Stoney Trace address where Chisholm lived, Detective Stark concluded that Brinkley

lived with her. J.A. 74–75. Hearing the testimony, the district court found these inferences

and the resulting conclusion persuasive. J.A. 144–47.

       In place of law enforcement’s inferences and analysis, the majority looks at a single-

page printout from the CJLEADS database and hypothesizes that Brinkley “might well be

transient.” Majority Op. 14. The majority then suggests that perhaps “Brinkley may have

tended to stay temporarily in various places rather than residing at any one address.”



       7
        It is true Detective Stark did not try to find the probation officer to confirm his
conclusion, but that “does not mean that [his conclusions] were unreasonable.” Wadkins
v. Arnold, 214 F.3d 535, 543 (4th Cir. 2000). Given probation caseloads, it is far from
apparent that contacting a probation officer is even a realistic investigative technique.
Indeed, Brinkley’s PSR shows that when a U.S. Probation Officer tried to contact
Brinkley’s state probation officer, the state probation officer did not respond. J.A. 246.

                                             35
Majority Op. 15. 8 Perhaps the majority’s own inferences are reasonable ones. But even

so, an alternative inference from the information does nothing to eliminate probable cause.

See District of Columbia v. Wesby, 138 S. Ct. 577, 592 (2018) (explaining that “innocent

explanations—even uncontradicted ones—do not have any automatic, probable-cause-

vitiating effect”). 9

        And yet, the majority’s own inferences rest on meager information. The single-

page printout from the CJLEADS database on which their alternative hypothesis is based

is below.




        8
           The majority suggests that their transience conclusion originated with the officers.
Majority Op. 15 n.4. But Special Agent Murphy did not say that he thought, based on the
CJLEADS data, that it was a reasonable inference that Brinkley lacked a residence.
Instead, he only agreed that “someone like Mr. Brinkley” may stay in various places “from
time to time.” J.A. 126. But even acknowledging that possibility, he rejected the likelihood
of it here. See id. (“[A]nything’s possible . . . [b]ut I felt that all the facts that we had at
that point were pointing to the most likely place he was at was this address at Stoney
Trace.”). And Detective Stark did not say that Brinkley may have resided at multiple
addresses. He only agreed that “it might be possible to find [Brinkley] at those other
addresses if he was not located at Stoney Trace Drive.” J.A. 89 (emphasis added). And he
too rejected the majority’s premise. See id. (In response to the question: “[D]id you deem
. . . that it was possible that Mr. Brinkley was staying at one of those other addresses,”
Detective Stark responded: “No. I believed that [Brinkley] was staying at Stoney Trace
Drive.”). Ultimately, the testimony that the majority points to amounts to no more than a
similar suggestion that it might be possible to find me at my house, but also at my office,
my parent’s house, a vacation home, or my brother’s house, or that I stay at those locations
from time to time. Cf. J.A. 89 (The other addresses on Brinkley’s CJLEADS page were
probably “family addresses.”). That would do little to suggest that I am nomadic and lack
any residence.
        9
         The majority’s theory is also a new one, raised only on appeal. Before the district
court, Brinkley’s counsel admitted the government “certainly had some basis to believe
Mr. Brinkley was residing at 4709 Stoney Trace” and never mentioned transience or a
particular alternative residential address during his argument. J.A. 141.
                                              36
37
       To be clear, this page is not what the officers relied on in February 2017 but is a

later-printed example of what the database’s first page might have looked like at the time.

Compared to what the officers saw before arresting Brinkley, this single page includes

“more addresses,” “changed” addresses, and “changed” dates. J.A. 66–67 (noting Exhibit

1 was made “later” to illustrate the officer testimony and explaining that it included “more

addresses” with “different dates besides the addresses,” and that the addresses may have

changed since February 2, 2017). We are not sure what addresses were added or changed,

or what dates were changed. See J.A. 66–67, 88. So even if we were looking at this with

expert eyes, we would be unable to see what the officers saw. The majority, however,

comes at the illustrative printout with less-than-expert eyes and suggests that a reasonable

inference from the database was that Brinkley might have been transient.

       But even if a sample page could support a new theory, this page only presents us

with skeletal information. We have only limited information about the various entries, no

information about the types of connections they indicate, no information about who else

was linked to the various addresses, nor a plethora of other information that was available

to the officers but is not included in the record. Cf. J.A. 155 (Exhibit 2 showing an

illustrative CJLEADS page that displays when an entry on Exhibit 1 is “clicked on,” see

J.A. 69).

       For example, the majority identifies a Planters View address as having been

“entered” on December 28, 2016, five days before the traffic stop where Brinkley had




                                            38
identified his address as Stoney Trace. 10 The majority says that the addition of another

address “just five days earlier” should undermine the conclusion that Brinkley resided on

Stoney Trace. Majority Op. 14. But we know little about the entry listing Planters View,

as the record does not include the click-through page for that entry. All we as judges know

is that the entry with the Planters View address was updated by someone on December 28,

2016. It seems plausible that Brinkley gave that address to another government actor much

earlier than December 28, 2016. 11 Again, officers have experience using this database as

part of their job responsibilities. They often review and navigate it to determine the date



       10
         Given the import that the majority places on this entry, it should be surprising that
neither the government nor defense counsel found it probative enough to specifically
mention during their arguments and that the district court did not find it worth discussing
when making its ruling.
       11
          Even the limited information in the record should make the majority question its
own hypothesis. The December 28 entry seems—at least to me based on the CJLEADS
printout—to be linked to an earlier criminal charge from 2015: “15CRS228668.” And
Brinkley was indeed arrested under that criminal case number for breaking and entering in
August 2015. See J.A. 246 (listing convictions). A reasonable officer could well conclude
that an address associated with a 2015 offense was an older address than the one that
Brinkley recently provided during a traffic stop and to his probation officer. Cf. J.A. 74
(explaining that the other addresses in the database dated to 2008 or 2009)
       But even if one doubted the connection above, the majority errs in relying on its
hypothesis that the Planters View address was “added [to the system] just five days” before
Brinkley’s traffic offense. Majority Op. 14 (emphasis added). We only know that the
offense occurred on January 2, 2017 because the government provided an illustrative click-
through page showing as much. J.A. 155 (government’s Exhibit 2). The CJLEADS entry
that we have reflects an “update” to that entry on March 1, 2017. J.A. 154–55. So we
know that the date on the illustrative exhibit does not reflect the date of the traffic stop
when Brinkley gave that address as his residence. And yet the majority assumes that the
entry date provides useful timing information about the Planters View address.
       I say all of this not to indicate that I know how to read the illustrative CJLEADS
page any better than the majority. It merely highlights that we, as judges, lack enough
information to say that the officers’ conclusions were unreasonable.
                                             39
and frequency with which addresses are entered and updated. So even if we could explore

the system and learn more about each entry, our review of their inferences should be

deferential. But, given that we cannot, we lack any legitimate basis for finding their

inferences in this case to be unreasonable and for substituting our own inferences and

conclusions. Cf. Glover, 140 S. Ct. at 1188 (crediting the officer’s “commonsense

inference” that the defendant was likely the driver of the truck when a database search

showed that the defendant was the truck’s registered owner).

       The majority also explains that the database included another entry—though we

cannot tell what address or the entry’s date—that was linked to a utility bill. Cf. J.A. 74

(noting that other addresses on CJLEADS dated to 2008 or 2009). The majority suggests

that the utility-bill address is just as likely Brinkley’s address because a utility bill

“constitute[s] strong evidence of a defendant’s residence.” Majority Op. 15 (citing United

States v. Graham, 553 F.3d 6, 13 (1st Cir. 2009)). The majority then says that the officers

should have done more to rule out that utility-bill-associated address, even though the

majority knows next to nothing about that address. Id. 12 Regardless, the majority does not



       12
           It seems difficult on this record to conclude that this utility bill was the “most
reasonably reliable information” as to where Brinkley lived. Appellant Reply 4. The utility
bill is not in the record and there is no discussion about when it was sent. For all we know,
it could have been from years before the February 3, 2017 arrest. Further, as Detective
Stark explained, many of these older addresses were likely “family-associated addresses.”
J.A. 74. Perhaps a member of the family put Brinkley’s name on the water bill, or another
family member bears a similar name. See J.A. 125–26 (noting a water bill that came back
either in “Mr. Brinkley’s name, or at least to a Kendrick Brinkley at another address”). All
of this is to say, just because the CJLEADS search turned up a utility bill with a different
address does not render unreasonable the officers’ conclusion that Brinkley lived on Stoney
Trace.
                                             40
give due weight to the fact that the officers considered that address and found that it was

likely a “family-associated address[]” or was at least not “credible as a place where

[Brinkley] was living.” J.A. 74, 113. It might be true that utility-bill-associated addresses

are particularly strong indicators of where someone lives in some jurisdictions or at a given

time. Or perhaps not. Again, I have not examined an actual CJLEADS profile and had to

conclude whether an older utility-bill-associated address is better evidence of where

someone lives than an address recently provided twice. But we know the experienced

officers considered the utility bill and found it was more likely a family-associated address.

See Ornelas, 517 U.S. at 700.

       The majority also decides that Brinkley’s apparent engagement to Chisholm

“certainly provided additional evidence that Brinkley might well have stayed at Chisholm’s

home, but it did not speak to whether he did so as a resident or as Chisholm’s overnight

guest.” Majority Op. 16. It may well be, in some communities, that living together before

marriage is unusual.     But these officers, based on their own experience, believed

differently. And we must “apply the probable cause standard to the facts in their totality.”

United States v. Thomas, 913 F.2d 1111, 1115 (4th Cir. 1990) (emphasis added). So even

if you might infer that a couple would not live together before marriage, these officers had

more information: Brinkley had recently provided that same address during a traffic stop

and to his probation officer. So I find it hard to conclude that the officers unreasonably

considered his relationship status alongside that information to conclude that Brinkley was

living with Chisholm on Stoney Trace.



                                             41
       The majority repeatedly presses that the officers could have investigated more.

Majority Op. 15–17. And it is true that they could have done more. That is almost always

true. But we do not require officers to “exhaust every potential avenue for investigation.”

Smith v. Munday, 848 F.3d 248, 261 (4th Cir. 2017) (quoting Wadkins v. Arnold, 214 F.3d

535, 543 (4th Cir. 2000) (If officers “could have been more thorough, or even [if] . . . [their]

actions may have been mistaken, [that] does not mean that they were unreasonable.”)).

       In sum, the majority failed to give the appropriate weight to the officer’s inferences,

which were entitled to substantial weight given the limited information in the record and

our lack of expertise with this law-enforcement database. And while the officers could

have done more, they did not have to. In total, the information here established probable

cause to believe Brinkley resided at the Stoney Trace address.

       B.     The officers had probable cause to believe that Brinkley would be at the
              Stoney Trace address when they entered to execute the arrest warrant

       The majority’s second-prong analysis is plagued by their faulty first-prong analysis.

In analyzing the second prong, the majority explains that any belief about Brinkley’s

presence was undermined by “uncertainty about where Brinkley resided.” Majority Op.

21; id. at 20 (“[A]n ill-founded belief about a suspect’s residence does not, and cannot,

shore up a belief about his presence.”). The majority is right that the reasonableness of the

belief of an arrestee’s residence affects the reasonableness of the belief in the arrestee’s

presence. See Vasquez-Algarin, 821 F.3d at 481 (A reasonable belief in an arrestee’s

residence “alone carries significant weight in establishing probable cause to believe the

arrestee is present.”). But this means that the majority’s improper inferences about


                                              42
Brinkley’s residence become the engine behind their conclusion that the officers lacked

probable cause to believe Brinkley was present.

       The majority acknowledges that the sounds coming from the apartment “at least

indicated that some living being was present.” Majority Op. 22. But the majority then

concludes that the police had “no reason to think that the noises came from Brinkley rather

than some unknown person.” Id. If the officers really had no reason to believe Brinkley

resided there, then the majority’s conclusion would hold. But if they did have reason to

believe Brinkley lived there, they would have some “reason to think that the noises [inside

the apartment] came from Brinkley.” Id. 13

       The noises from inside the apartment, Chisholm’s increasing nervousness, and

Chisholm and Prigon’s responses to the noises suggested that someone else was inside the

apartment. And when combined with the reasonable belief that Brinkley resided on Stoney

Trace, officers had probable cause to believe that “someone else” was Brinkley.



       13
          The majority likens this case to United States v. Hill, 649 F.3d 258 (4th Cir. 2011).
But as the district court found, this case is materially different. In Hill, the officers admitted
that they did not believe Hill would be present at the residence when they did the search.
Id. at 263–64 (One officer believed that Hill would not be home because Hill had fled
before and that there was an 80 percent chance Hill would not be present when they went
to the residence. Another characterized the trip as one “in regards to a fugitive
investigation.”). And another resident informed the police that Hill was not there and
attributed the noise inside the apartment to her sister. Id. at 264. In Hill, the primary issue,
and why no “reason to believe” Hill was present was found, was that the police relied
“solely . . . on an unidentified noise coming from within the home.” Id. at 265. That was
not the case here. The officers were sure that Brinkley was present before they entered.
See J.A. 81, 134. And the majority cannot seriously contend that an unidentified noise was
the only evidence the officers had that Brinkley was there after the majority themselves list
five other pieces of evidence that would suggest Brinkley was in the apartment. Majority
Op. 20. Hill simply does not dictate this result.
                                               43
                        *                     *                    *

       Experienced officers used a law-enforcement database and supporting information

to concluded that Brinkley resided at the Stoney Trace address. Rejecting their inferences

and conclusions, the majority looks at the limited information we have in the record and

adopts an alternative theory of the evidence. They posit that Brinkley may have been

transient and without a residence—a theory not even argued below. They then suggest that

Brinkley providing law enforcement and probation with the same address that his fiancée

used could only signify that Brinkley was possibly an overnight guest. The majority then

uses their new theory of Brinkley’s residence to decide the officers lacked probable cause

to believe Brinkley was present at the apartment that morning.

       I disagree. But what really matters is that we, as a court far removed from the reality

on the ground, are commanded to give due deference to law enforcement’s inferences that

the local district court agrees with. Giving due weight to those inferences, these officers

had probable cause to believe that Brinkley lived with Chisholm on Stoney Trace. And,

based on that belief and information developed after they arrived, they had probable cause

to believe that Brinkley was present. I respectfully dissent.




                                             44

```

---

## GROUP: content/cases/United States v. Castillo.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Castillo
type: case
citation: "70 F.4th 894 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir.
court_level: coa
circuit: ca5
year: 2023
date_decided: 2023-06-19
docket: 22-50060
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
  opinion_url: "https://www.courtlistener.com/opinion/9407477/united-states-v-castillo/"
  cluster_id: 9407477
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Castillo
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[Riley v. California]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - border-searches
  - cell-phone
  - manual-search
  - no-suspicion-required
  - fifth-circuit
holding: "Joining every circuit to have addressed the question, the Fifth Circuit held that no individualized suspicion is required for the government to conduct a manual border search of a cell phone; because agents at a port of entry manually scrolled through Castillo's phone and found child pornography, the search was reasonable by virtue of occurring at the border, and suppression was properly denied."
aliases:
  - United States v. Castillo
  - "United States v. Castillo (5th Cir. 2023)"
---

# United States v. Castillo

*70 F.4th 894 (5th Cir. 2023)* (No. 21-50406) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9407477 → majority opinion 9402953 (Ho, J.; 70 F.4th 894, decided June 19, 2023). Re-keyed in the pre-W5 identity audit from a wrong-case namesake (sentencing/plea-breach Castillo) to the intended border-search Castillo; identity re-verified on read 2026-07-07. Rule quote string-matched to the CL opinion text; slip-style pin (the CL text carries only the 5th Cir. slip pagination, not the 70 F.4th star pages) — S9 verifies the reporter pincite. -->

## Background
Alvaro Castillo crossed the international bridge into Presidio, Texas, near midnight in an RV towing a car and was sent to secondary inspection. Border agents found a revolver hidden between frying pans in the oven, ammunition in a taped pressure cooker, and marijuana in luggage. Castillo admitted owning the contraband and gave agents the passcode to his phone; a Homeland Security agent manually scrolled through the phone's apps and found suspected child pornography, prompting a broader forensic search of his devices. Castillo moved to suppress; the district court refused, and he was convicted on six child-pornography counts.

## Issue
Whether a manual border search of a cell phone requires individualized (reasonable) suspicion under the Fourth Amendment.

## Rule
Searches at the border "are reasonable simply by virtue of the fact that they occur at the border," pursuant to the sovereign's right to protect itself. Although cell phones can be "unusually intrusive" (*[[Riley v. California|Riley]]*), the court did not decide the forensic-search question but adopted the circuits' consensus on manual searches, holding: "every circuit to have addressed the issue has agreed that no individualized suspicion is required for the government to undertake a manual border search of a cell phone. We see no reason to depart from the consensus of the circuits." — slip op. at 1. ^pin-slip1

## Application
The agent's search was a manual one — scrolling by hand through apps on the unlocked phone — not a forensic extraction, and it occurred at a port of entry during a routine secondary inspection. Because a manual border search of a cell phone requires no individualized suspicion, the initial search was reasonable; the images it revealed then supported the further forensic examination. The court expressly reserved the harder, circuit-splitting question whether a forensic border search of a phone requires reasonable suspicion, because deciding the manual-search issue resolved the appeal.

## Conclusion
**Affirmed.** Judge Ho wrote for the panel (Jones, Southwick, Ho, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Castillo* places the Fifth Circuit with the consensus that manual cell-phone searches at the border need no suspicion, while deliberately leaving open the *forensic*-search question that divides the circuits after *[[Riley v. California|Riley]]* and *[[Carpenter v. United States|Carpenter]]* — a live frontier of the *[[Border Searches]]* doctrine.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Castillo*, 70 F.4th 894 (5th Cir. 2023)](https://www.courtlistener.com/opinion/9407477/united-states-v-castillo/) — pinpoint: slip op. at 1 (no individualized suspicion for a manual border search of a cell phone; forensic-search question reserved). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is slip-paginated, so the 70 F.4th star page is not asserted here.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6ad93406a38559b2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "70 F.4th 894 (2023)", "court": "5th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Castillo", "year": "2023"}}
{"assertion_id": "9d3db0fb78ccff24", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Joining every circuit to have addressed the question, the Fifth Circuit held that no individualized suspicion is required for the government to conduct a manual border search of a cell phone; because agents at a port of entry manually scrolled through Castillo's phone and found child pornography, the search was reasonable by virtue of occurring at the border, and suppression was properly denied.", "title": "United States v. Castillo"}}
{"assertion_id": "b6da0a8177c1f6b7", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key", "title": "United States v. Castillo"}}
{"assertion_id": "b39174138a260331", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "United States v. Castillo"}}
{"assertion_id": "cf372e5b5e55efd3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Castillo", "varies_by_point": "false"}}
```

### lake record — United States v. Castillo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Castillo",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Castillo",
    "case_name_short": "Castillo",
    "case_name_full": "",
    "input_case_name": "United States v. Castillo",
    "court": "5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2023-06-19",
    "year": 2023,
    "docket": "22-50060",
    "cluster_id": 9407477,
    "lead_opinion_id": 9402953,
    "sibling_ids": [],
    "absolute_url": "/opinion/9407477/united-states-v-castillo/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "70 F.4th 894",
      "volume": "70",
      "reporter": "F.4th",
      "page": "894",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "70 F.4th 894",
        "volume": "70",
        "reporter": "F.4th",
        "page": "894",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "70 F.4th 894",
    "official_selection": {
      "court_class": "coa",
      "selected": "70 F.4th 894",
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
    "date_created": "2026-07-07T18:15:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-castillo--9407477",
      "to_record_id": "United States v. Castillo",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Castillo

```
Case: 21-50406     Document: 00516791307         Page: 1     Date Filed: 06/19/2023




           United States Court of Appeals
                for the Fifth Circuit                                 United States Court of Appeals
                                                                               Fifth Circuit

                                                                             FILED
                                                                         June 19, 2023
                                  No. 21-50406
                                                                        Lyle W. Cayce
                                                                             Clerk

   United States of America,

                                                             Plaintiff—Appellee,

                                       versus

   Alvaro Castillo, Jr.,

                                                         Defendant—Appellant.


                  Appeal from the United States District Court
                       for the Western District of Texas
                           USDC No. 4:19-CR-780-1


   Before Jones, Southwick, and Ho, Circuit Judges.
   James C. Ho, Circuit Judge:
          The Fourth Amendment protects the right of the American people
   “to be secure in their persons, houses, papers, and effects, against
   unreasonable searches and seizures.” U.S. Const. amend. IV. Today we
   address what searches are reasonable and unreasonable at the intersection of
   two established lines of Fourth Amendment precedent—when the
   government searches a cell phone at the border.
          On the one hand, the Supreme Court has long held that “searches
   made at the border . . . are reasonable simply by virtue of the fact that they
Case: 21-50406        Document: 00516791307        Page: 2   Date Filed: 06/19/2023




                                    No. 21-50406


   occur at the border,” “pursuant to the long-standing right of the sovereign
   to protect itself by stopping and examining persons and property crossing
   into this country.” United States v. Ramsey, 431 U.S. 606, 616 (1977).
          But on the other hand, the Court has also made clear that searches of
   modern devices like cell phones can be unusually intrusive. After all, “[c]ell
   phones differ in both a quantitative and a qualitative sense from other objects
   that might be kept on an arrestee’s person.” Riley v. California, 573 U.S. 373,
   393 (2014). Depending on the extent of the search, the government could
   theoretically access virtually every aspect about one’s life based on a single
   handheld device.
          Our circuit has not yet articulated the standard that governs cell phone
   searches at the border. In some circuits, the governing standard depends on
   the extent of the search—whether the government is conducting merely a
   manual search of what is immediately available on the device, or a more
   intrusive forensic search. The circuits are divided over whether reasonable
   suspicion is required for a forensic search of a cell phone at the border. But
   every circuit to have addressed the issue has agreed that no individualized
   suspicion is required for the government to undertake a manual border search
   of a cell phone.
          We see no reason to depart from the consensus of the circuits. And
   adopting that consensus is all we need to do to decide this appeal. We
   accordingly affirm.
                                         I.
          The parties jointly stipulated to the facts that govern this appeal.
   Defendant Alvaro Castillo and two others crossed the international bridge to
   Presidio, Texas, in a recreational vehicle (RV) that was towing a passenger
   car behind it, at around midnight. Upon reaching the port of entry into the
   United States, the RV was sent to secondary inspection—as is standard




                                         2
Case: 21-50406      Document: 00516791307          Page: 3   Date Filed: 06/19/2023




                                    No. 21-50406


   operating procedure when it comes to vehicles of that size entering the
   country at that time of night. Defendant and his companions told border
   agents that they had nothing to declare.
          During the search of the RV, an officer found a .357 revolver taped
   between two frying pans that had been wrapped in packing foam and taped
   inside the oven. The officer also found ammunition for a .357 inside a
   pressure cooker that had been taped shut, as well as evidence of marijuana
   inside of luggage.
          Defendant was placed in a holding cell. He admitted to owning the
   contraband. He also provided the passcode to unlock his cell phone to a
   Homeland Security Investigations special agent.
          The agent manually scrolled through various apps. As a result, he
   found what he believed to be child pornography in the photo section of
   Defendant’s phone.
          Based on those initial findings, various agents conducted a more
   intrusive forensic search of the phone. They also conducted both manual and
   forensic searches of other electronic devices in Defendant’s possession.
   Those efforts produced additional child pornography images.
          Defendant was subsequently indicted on six charges involving child
   pornography. He subsequently moved to suppress the evidence obtained
   from the search of his devices. After a hearing, the district court refused to
   suppress the child pornography. Defendant was found guilty on all six counts
   and sentenced to 720 months imprisonment and a life term of supervised
   release. He filed a timely notice of appeal.
          A district court’s factual findings on a motion to suppress are
   reviewed for clear error, and the court’s ultimate conclusions on whether the
   Fourth Amendment was violated are reviewed de novo. United States v.




                                          3
Case: 21-50406      Document: 00516791307          Page: 4    Date Filed: 06/19/2023




                                    No. 21-50406


   Scroggins, 599 F.3d 433, 440 (5th Cir. 2010). The evidence is reviewed in the
   light most favorable to the prevailing party unless that view is inconsistent
   with the court’s findings or is clearly erroneous in light of the evidence as a
   whole. Id.
                                         II.
          The Fourth Amendment provides that “[t]he right of the people to be
   secure in their persons, houses, papers and effects, against unreasonable
   searches and seizures, shall not be violated.” U.S. Const. amend. IV.
   “[W]arrantless searches are typically unreasonable where a search is
   undertaken by law enforcement officials to discover evidence of criminal
   wrongdoing.” Carpenter v. United States, 138 S. Ct. 2206, 2221 (2018)
   (quotation omitted). “In the absence of a warrant, a search is reasonable only
   if it falls within a specific exception to the warrant requirement.” Riley, 573
   U.S. at 382.
          The border search exception is a “longstanding, historically
   recognized exception to the Fourth Amendment’s general principle that a
   warrant be obtained” for a search. Ramsey, 431 U.S. at 621. “[T]he border-
   search exception allows officers to conduct ‘routine inspections and searches
   of individuals or conveyances seeking to cross . . . borders’ without any
   particularized suspicion of wrongdoing.” United States v. Aguilar, 973 F.3d 445,
   449 (5th Cir. 2020) (quoting Ramsey, 431 U.S. at 619) (emphasis added).
   Moreover, even “[s]o-called ‘nonroutine’ searches need only reasonable
   suspicion, not the higher threshold of probable cause.” United States v.
   Molina-Isidoro, 884 F.3d 287, 291 (5th Cir. 2018). “For border searches both
   routine and not, no case has required a warrant.” Id.
          The “scope of a search conducted under an exception to the warrant
   requirement must be commensurate with its purposes.” Arizona v. Gant, 556
   U.S. 332, 339 (2009). The border search exception reflects “the long-




                                          4
Case: 21-50406     Document: 00516791307           Page: 5   Date Filed: 06/19/2023




                                    No. 21-50406


   standing right of the sovereign to protect itself by stopping and examining
   persons and property crossing into this country.” Ramsey, 431 U.S. at 616.
   “The Government’s interest in preventing the entry of unwanted persons
   and effects is at its zenith at the international border” and has been
   recognized “since the beginning of our Government.” United States v.
   Flores-Montano, 541 U.S. 149, 152–53 (2004). “Historically such broad
   powers have been necessary to prevent smuggling and to prevent prohibited
   articles from entry.” Ramsey, 431 U.S. at 619.
          Accordingly, courts have allowed a variety of border searches without
   requiring either a warrant or reasonable suspicion. See, e.g., Flores–Montano,
   541 U.S. at 155 (“the Government’s authority to conduct suspicionless
   inspections at the border includes the authority to remove, disassemble, and
   reassemble a vehicle’s fuel tank”); Ramsey, 431 U.S. at 620 (“custom
   officials could search, without probable cause and without a warrant,
   envelopes carried by an entering traveler, whether in his luggage or on his
   person,” and “no different constitutional standard should apply simply
   because the envelopes were mailed, not carried”); United States v.
   Chaplinski, 579 F.2d 373, 374 (5th Cir. 1978) (“At the border, customs agents
   need not have a reasonable or articulable suspicion that criminal activity is
   involved to stop one who has traveled from a foreign point, examine his or
   her visa, and search luggage and personal effects for contraband.”).
          To be sure, modern cell phones are fundamentally distinct from other
   personal items. As the Supreme Court observed in Riley, “many of these
   devices are in fact minicomputers that also happen to have the capacity to be
   used as telephones.”      573 U.S. at 393.       “One of the most notable
   distinguishing features of modern cell phones is their immense storage
   capacity.” Id. “Before cell phones, a search of a person was limited by
   physical realities and tended as a general matter to constitute only a narrow
   intrusion on privacy.” Id. But today, “the possible intrusion on privacy is



                                         5
Case: 21-50406      Document: 00516791307          Page: 6   Date Filed: 06/19/2023




                                    No. 21-50406


   not physically limited in the same way when it comes to cell phones.” Id. at
   394. Accordingly, government searches of such devices have the potential to
   be uniquely intrusive.
          The extent of the privacy intrusion, however, will depend on the
   methodology employed by the government agent. “Basic border searches . . .
   require an officer to manually traverse the contents of the traveler’s
   electronic device, limiting in practice the quantity of information available
   during a basic search.” Alasaad v. Mayorkas, 988 F.3d 8, 18 (1st Cir. 2021).
   “And a basic border search does not allow government officials to view
   deleted or encrypted files.” Id. at 19. See also id. at 18–19 (“The CBP Policy
   only allows searches of data resident on the device.”).
          Accordingly, when it comes to manual cell phone searches at the
   border, our sister circuits have uniformly held that Riley does not require
   either a warrant or reasonable suspicion. See, e.g., United States v. Xiang, 67
   F.4th 895, 900 (8th Cir. 2023) (“No Circuit has held that the government
   must obtain a warrant to conduct a routine border search of electronic
   devices.”); Alasaad v. Mayorkas, 988 F.3d 8, 18–19 (1st Cir. 2021) (“We . . .
   agree with the holdings of the Ninth and Eleventh circuits that basic border
   searches are routine searches and need not be supported by reasonable
   suspicion.”); United States v. Cano, 934 F.3d 1002, 1016 (9th Cir. 2019)
   (“manual searches of cell phones at the border are reasonable without
   individualized suspicion”).
          Our sister circuits have differed only as to whether reasonable
   suspicion is required for a more intrusive forensic search of a cell phone at
   the border. Compare, e.g., United States v. Touset, 890 F.3d 1227, 1231 (11th
   Cir. 2018) (“the Fourth Amendment does not require any suspicion [even]
   for forensic searches of electronic devices at the border”), with Cano, 934
   F.3d at 1016 (“we hold that manual searches of cell phones at the border are




                                         6
Case: 21-50406        Document: 00516791307          Page: 7   Date Filed: 06/19/2023




                                      No. 21-50406


   reasonable without individualized suspicion, whereas the forensic
   examination of a cell phone requires a showing of reasonable suspicion”).
             All we need to decide this case, however, is to adopt the consensus
   view of our sister circuits and hold that the government can conduct manual
   cell phone searches at the border without individualized suspicion. After all,
   the manual cell phone search here produced evidence of child pornography.
   So if that search was valid, then it’s hard to see how that would not justify the
   subsequent forensic searches for additional evidence of child pornography.
   And Castillo does not appear to claim otherwise. He argues that the
   government violated the Fourth Amendment by conducting the manual as
   well as forensic searches. But he does not claim that the forensic search was
   invalid even if we find the manual search valid.
             We see no reason to disagree with our sister circuits. Accordingly, we
   hold that no reasonable suspicion is necessary to conduct the sort of routine
   manual cell phone search at the border that occurred here. We therefore
   affirm.




                                            7

```

---

## GROUP: content/cases/United States v. Cole.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Cole
type: case
citation: "21 F.4th 421 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 7th Cir.
court_level: coa
circuit: ca7
year: 2021
date_decided: 2021-12-17
docket: 20-2105
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
  opinion_url: "https://www.courtlistener.com/opinion/5307612/united-states-v-janhoi-cole/"
  cluster_id: 5307612
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Cole
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Traffic Stops]]"
    role: Key
related:
  - "[[Traffic Stops]]"
  - "[[Rodriguez v. United States]]"
  - "[[Whren v. United States]]"
  - "[[Illinois v. Caballes]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - traffic-stop
  - reasonable-suspicion
  - rodriguez-mission
  - seventh-circuit
  - en-banc
holding: "Travel-plan questions ordinarily fall within the mission of a traffic stop and so do not, by themselves, measurably prolong it; like any inquiry during a stop, however, they must be reasonable under the circumstances — and here the trooper's follow-up questions were justified by the driver's evasive answers, and reasonable suspicion of drug trafficking developed before the stop was extended for a dog sniff, so suppression was properly denied."
aliases:
  - United States v. Cole
  - "United States v. Cole (7th Cir. 2021)"
---

# United States v. Cole

*21 F.4th 421 (7th Cir. 2021)* (No. 20-2105, [[Reading and Citing Cases#en-banc|en banc]]) · U.S. Court of Appeals for the Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 5307612 → majority opinion 5136163 (St. Eve, J., en banc; 21 F.4th 421, decided Dec. 17, 2021). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (the CL text carries only the slip-opinion pagination, not the 21 F.4th star pages) — S9 verifies the reporter pincite. -->

## Background
An Illinois state trooper stopped Janhoi Cole for following too closely on an interstate. Cole was driving with an Arizona license and a California registration on a recently purchased, recently insured car; the trooper's questions about his license, registration, and travel plans drew answers he found evasive, inconsistent, and improbable. Combined with other indicators, this led the trooper to suspect drug trafficking; he called a K-9 unit to a nearby gas station, the dog alerted, and officers found methamphetamine and heroin. A divided panel had reversed the denial of suppression, holding that the trooper's roadside travel-plan questioning unreasonably prolonged the stop; the Seventh Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether travel-plan questions are part of the "mission" of a traffic stop under *[[Rodriguez v. United States]]*, such that asking them does not unlawfully prolong the stop.

## Rule
Under *[[Rodriguez v. United States|Rodriguez]]*, a stop may last no longer than needed to complete its mission, and off-mission inquiries that add time require independent reasonable suspicion. Resolving an intra-circuit conflict, the [[Reading and Citing Cases#en-banc|en banc]] court held: "we hold that travel-plan questions ordinarily fall within the mission of a traffic stop. Travel-plan questions, however, like other police inquiries during a traffic stop, must be reasonable under the circumstances." — slip op. at 2. ^pin-slip2

## Application
Because travel-plan questions ordinarily belong to the stop's mission, the trooper's initial inquiries did not prolong the detention at all. His follow-up questions were reasonable responses to Cole's "less-than-forthright answers," and by the time the stop moved to the gas station for the dog sniff, the trooper had developed reasonable suspicion of drug trafficking to support the brief extension. The stop was lawfully initiated and never unreasonably prolonged.

## Conclusion
**Affirmed.** The [[Reading and Citing Cases#en-banc|en banc]] court affirmed the denial of Cole's motion to suppress. Judge St. Eve wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Cole* is a leading [[Reading and Citing Cases#en-banc|en banc]] statement placing routine travel-plan questioning inside the *[[Rodriguez v. United States|Rodriguez]]* mission, consistent with *[[Illinois v. Caballes|Caballes]]* on dog sniffs that do not add time — while cautioning that such questions must still be reasonable in the circumstances.

## Appears on
- [[Traffic Stops]] — *Key*

## Sources
- [*United States v. Cole*, 21 F.4th 421 (7th Cir. 2021)](https://www.courtlistener.com/opinion/5307612/united-states-v-janhoi-cole/) — pinpoint: slip op. at 2 (travel-plan questions within the stop's mission). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is slip-paginated, so the 21 F.4th star page is not asserted here.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8c28b1c2beea25f3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "21 F.4th 421 (2021)", "court": "7th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Cole", "year": "2021"}}
{"assertion_id": "0d77018085a6b1dd", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Travel-plan questions ordinarily fall within the mission of a traffic stop and so do not, by themselves, measurably prolong it; like any inquiry during a stop, however, they must be reasonable under the circumstances — and here the trooper's follow-up questions were justified by the driver's evasive answers, and reasonable suspicion of drug trafficking developed before the stop was extended for a dog sniff, so suppression was properly denied.", "title": "United States v. Cole"}}
{"assertion_id": "e2e9a563b9eae8ab", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key", "title": "United States v. Cole"}}
{"assertion_id": "666a83da1fd6eefe", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 7th Cir.", "title": "United States v. Cole"}}
{"assertion_id": "ece4a3ff82e27f6f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Cole", "varies_by_point": "false"}}
```

### lake record — United States v. Cole

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cole",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Janhoi Cole",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Cole",
    "court": "7th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca7",
    "state": null,
    "date_decided": "2021-12-17",
    "year": 2021,
    "docket": "20-2105",
    "cluster_id": 5307612,
    "lead_opinion_id": 5136163,
    "sibling_ids": [],
    "absolute_url": "/opinion/5307612/united-states-v-janhoi-cole/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "21 F.4th 421",
      "volume": "21",
      "reporter": "F.4th",
      "page": "421",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "21 F.4th 421",
        "volume": "21",
        "reporter": "F.4th",
        "page": "421",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "21 F.4th 421",
    "official_selection": {
      "court_class": "coa",
      "selected": "21 F.4th 421",
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
    "date_created": "2026-07-07T18:18:15Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-cole--5307612",
      "to_record_id": "United States v. Cole",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Cole

```
                                 In the

     United States Court of Appeals
                      For the Seventh Circuit
                        ____________________
No. 20-2105
UNITED STATES OF AMERICA,
                                                     Plaintiﬀ-Appellee,
                                   v.

JANHOI COLE,
                                                 Defendant-Appellant.
                        ____________________

          Appeal from the United States District Court for the
                      Central District of Illinois.
              No. 3:18-cr-30038 — Richard Mills, Judge.
                        ____________________

 ARGUED SEPTEMBER 30, 2021 — DECIDED DECEMBER 17, 2021
                ____________________

   Before SYKES, Chief Judge, and EASTERBROOK, KANNE,
ROVNER, WOOD, HAMILTON, BRENNAN, SCUDDER, ST. EVE, and
KIRSCH, Circuit Judges. *




    * Circuit Judge  Jackson-Akiwumi did not participate in the considera-
tion or decision of this case.
2                                                  No. 20-2105

    ST. EVE, Circuit Judge. An Illinois state trooper stopped
Janhoi Cole for following too closely behind another car. At
the time, Cole was traveling on an Illinois interstate with an
Arizona driver’s license and a California registration. During
the brief roadside detention that followed, the trooper ques-
tioned Cole about his license, registration, and travel plans.
Cole’s answers struck the trooper as evasive, inconsistent, and
improbable. Many of the trooper’s questions were follow-up
questions to Cole’s answers and volunteered information.
Combined with other factors, they led the trooper to suspect
that Cole was traﬃcking drugs. To investigate his suspicions,
the trooper called for a K-9 unit to meet him and Cole at a
nearby gas station. The dog alerted, and oﬃcers found large
quantities of methamphetamine and heroin in Cole’s car.
    Facing federal charges, Cole moved to suppress the drugs
as well as his statements during the stop. He argued that the
trooper unlawfully initiated the stop and unreasonably pro-
longed it without reasonable suspicion of other criminal ac-
tivity. The district court denied the motion, but a divided
panel of this Court reversed on the basis that the trooper’s in-
itial roadside questioning unreasonably prolonged the traﬃc
stop. We reheard the case en banc to resolve an apparent con-
ﬂict between the panel’s decision and United States v. Lewis,
920 F.3d 483 (7th Cir. 2019), as to whether travel-plan ques-
tions are part of the “mission” of a traﬃc stop under Rodriguez
v. United States, 575 U.S. 348 (2015).
   In keeping with Lewis and the consensus of other circuits,
we hold that travel-plan questions ordinarily fall within the
mission of a traﬃc stop. Travel-plan questions, however, like
other police inquiries during a traﬃc stop, must be reasonable
under the circumstances. And here they were. The trooper
No. 20-2105                                                    3

inquired about the basic details of Cole’s travel, and his fol-
low-up questions were justiﬁed given Cole’s less-than-forth-
right answers. The stop itself was lawfully initiated, and the
trooper developed reasonable suspicion of other criminal ac-
tivity before moving the initial stop to the gas station for the
dog sniﬀ. We therefore aﬃrm the district court’s denial of
Cole’s motion to suppress.
                               I.
    A magistrate judge held a hearing on Cole’s motion to
suppress. Evidence at the hearing included the trooper’s po-
lice report and dash camera video as well as testimony from
Cole, the trooper, and another oﬃcer involved in the stop. Af-
ter the hearing, the magistrate judge entered a report and rec-
ommendation with extensive factual ﬁndings, which the dis-
trict court adopted. Absent clear error, we defer to the district
court’s factual ﬁndings. United States v. Bacon, 991 F.3d 835,
840 (7th Cir. 2021).
                               A.
    Sheriﬀ’s Deputy Derek Suttles was on criminal interdic-
tion patrol in central Illinois when he spotted a silver
Volkswagen hatchback traveling east on the interstate. The
car caught his attention because it was travelling 10 to 15 miles
below the posted speed limit. Deputy Suttles also noticed a
covering over the car’s rear cargo area. He messaged Illinois
State Police Trooper Clayton Chapman, who was doing crim-
inal interdiction patrol further east on the interstate, and told
him to look out for the Volkswagen. Trooper Chapman had
about 250 hours of training, mostly related to drug interdic-
tion and other crime interdiction on roadways.
4                                                 No. 20-2105

   Deputy Suttles relayed the information that he considered
to be suspicious, along with the results of a license plate
check. The check revealed that the Volkswagen had been sold
and registered three weeks earlier to Janhoi Cole, with an ad-
dress in Los Angeles, California. It had been insured only four
days earlier.
    Trooper Chapman spotted the Volkswagen, whose driver
was leaned far back in the seat with his arms fully extended,
obscuring his face, and began following the vehicle. Shortly
thereafter, Trooper Chapman saw another car merge in front
of the Volkswagen from the far-left lane. When the other car
merged, the Volkswagen did not move into the right lane, but
instead followed closely behind the merged car. From his van-
tage point—about a football ﬁeld behind the Volkswagen—
Trooper Chapman determined that the Volkswagen was two
car lengths or less behind the merged car.
   Trooper Chapman stopped the Volkswagen for following
too closely, in violation of Illinois law. See 625 ILCS 5/11-
710(a). After calling in the license plate and conﬁrming that
the plate matched the car, Trooper Chapman approached the
Volkswagen and asked the driver (Cole) for his license and
registration. Cole produced his Arizona driver’s license and
California registration. In response to Trooper Chapman’s
questions, Cole conﬁrmed that his license showed his current
address and that he owned the Volkswagen. Trooper Chap-
man then asked Cole to sit in his squad car so he could explain
the purpose of the stop in a quieter and safer setting. While
standing by Cole’s car, Trooper Chapman saw numerous
drinks and snacks in the car, which led him to believe that
Cole had been traveling long distances. He observed, though,
that the only luggage in the car was a small backpack.
No. 20-2105                                                  5

   In the squad car, Trooper Chapman spent about a minute
explaining the details of how Cole had followed the other car
too closely. He then asked Cole about his Arizona driver’s li-
cense and California license plate. Cole oﬀered, “I’m a chef. I
spend most of my time between Los Angeles and Maryland
and New York at work. But I genuinely had a job in Arizona.
And I genuinely keep this driver’s license because of the ex-
piration date.”
    About four minutes into the stop, Trooper Chapman be-
gan inquiring into Cole’s travel plans. He ﬁrst asked where
Cole was headed. Cole answered, Maryland, because his boss
resided in Maryland. Following up, the trooper asked where
Cole worked and for whom. Cole responded that he was a
personal chef for two former professional football players
and, in between, an ordinary chef. After conﬁrming Cole’s
destination (Maryland), the trooper asked Cole where his trip
began. Cole did not answer the question initially. Instead, he
oﬀered that he had met up with some friends and family in
Colorado Springs. The trooper asked again where the trip be-
gan. Cole clariﬁed that his trip started in Maryland. From
there, he went to Cincinnati, before heading to Colorado
Springs, then Boulder, and was going back home to Maryland
when the trooper stopped him. The trooper asked Cole when
he left on the trip. Cole said about four to ﬁve days earlier.
    The trooper then moved on to the vehicle’s information.
He questioned Cole as to how long he had owned the
Volkswagen. Cole said six months, adding that he just had the
paperwork transferred. He explained that the car was a recent
purchase. He had been driving with his friend’s paperwork
and had only recently acquired the insurance and registra-
tion. Looking at Cole’s paperwork, the trooper noted that the
6                                                    No. 20-2105

car had been registered on June 4, 2018. Cole veriﬁed that was
correct; his girlfriend had registered the car then.
    Trooper Chapman next inquired where Cole was living.
Cole said he spent most of his time in Los Angeles, adding
that he had a child in both Los Angeles and Florida and was
planning to move to Florida. The trooper wondered, “So,
you’ve got an Arizona driver’s license that says Tucson … I’m
just trying to … And you said you’ve been traveling from
Maryland, so have you been staying recently in Maryland?”
Cole replied, “Yes. I have family in Maryland. My boss is in
Maryland. When I work in Maryland, I stay by my uncle. But
this driver’s license, I genuinely keep it just because of the ex-
piration. I haven’t been in Arizona in a long time.” The
trooper followed up, “So your primary address, or your cur-
rent address, is in California. But recently you’ve been staying
in ….” Before he could ﬁnish, Cole interjected, “Yeah, cause
I’m a chef. I travel.” The trooper asked, “Back and forth?”
Cole said yes, explaining that he went wherever he got jobs.
The trooper concluded by asking Cole why he did not ﬂy.
Cole responded, “Fly? I have a car. And I travel with pots
sometimes. I’m a chef. Occasionally I travel with a bicycle.”
   Trooper Chapman thought that Cole’s travel details
sounded vague and made up. Cole appeared extremely nerv-
ous during the stop. Among other physical symptoms, he was
breathing heavily, and his neck was sweaty.
    Less than nine minutes into the stop, Trooper Chapman
told Cole that he was going to issue him a warning. He ex-
plained, though, that they would have to relocate to a nearby
gas station for safety reasons. Cole returned to his own car,
and they drove separately to the gas station. At the gas station,
Trooper Chapman called for a K-9 unit. While waiting,
No. 20-2105                                                    7

Trooper Chapman continued questioning Cole about his
travel plans. He regarded Cole’s answers as increasingly sus-
picious. He also learned from dispatch that Cole had been ar-
rested three times on drug traﬃcking charges. About 45
minutes after the stop began, the K-9 unit alerted on Cole’s
car. Oﬃcers searched the car and found large quantities of
methamphetamine and heroin.
                               B.
    A federal grand jury charged Cole with possession with
intent to distribute 500 grams or more of methamphetamine
(Count 1) and heroin (Count 2). Cole moved to suppress the
drugs found in his car and his statements during the stop. The
magistrate judge recommended denying the motion. The dis-
trict court accepted the recommendation and denied the mo-
tion. Cole conditionally pleaded guilty to both counts, while
reserving his right to appeal the denial of his motion to sup-
press. A divided panel of this Court reversed, but we vacated
that opinion and voted to rehear the case en banc.
                               II.
    Cole maintains that Trooper Chapman violated his Fourth
Amendment rights by stopping him without reasonable sus-
picion of a traﬃc violation and by unreasonably prolonging
the stop to inquire into his travel plans. We review the district
court’s legal conclusions de novo, Bacon, 991 F.3d at 840, and
its factual ﬁndings for clear error, United States v. Gholston,
1 F.4th 492, 496 (7th Cir. 2021).
    The Fourth Amendment provides that “[t]he right of the
people to be secure in their persons, houses, papers, and ef-
fects, against unreasonable searches and seizures, shall not be
violated.” U.S. Const. amend. IV. Time and again, the
8                                                        No. 20-2105

Supreme Court has held that “the ultimate touchstone of the
Fourth Amendment is reasonableness.” Lange v. California,
141 S. Ct. 2011, 2017 (2021) (quoting Brigham City v. Stuart, 547
U.S. 398, 403 (2006)). “Reasonableness, in turn, is measured in
objective terms by examining the totality of the circum-
stances.” Ohio v. Robinette, 519 U.S. 33, 39 (1996).
    Traﬃc stops are seizures, so they must be reasonable un-
der the circumstances. Whren v. United States, 517 U.S. 806, 809
(1996). To be reasonable, a traﬃc stop must be “justiﬁed at its
inception, and reasonably related in scope to the circum-
stances which justiﬁed the interference in the ﬁrst place.”
Hiibel v. Sixth Jud. Dist. Ct. of Nevada, Humboldt Cnty., 542 U.S.
177, 185 (2004). Because traﬃc stops are typically brief deten-
tions, more akin to Terry stops than formal arrests, they re-
quire only reasonable suspicion of a traﬃc violation—not
probable cause. Rodriguez, 575 U.S. at 354; Navarette v. Califor-
nia, 572 U.S. 393, 396–97 (2014); see also Terry v. Ohio, 392 U.S.
1 (1968). By the same token, though, traﬃc stops must remain
limited in scope: “A seizure for a traﬃc violation justiﬁes a
police investigation of that violation.” Rodriguez, 575 U.S. at
354. Police may not “detour[]” from that “mission” to investi-
gate other criminal activity. Id. at 356–57. A detour that “pro-
longs the stop” violates the Fourth Amendment unless the of-
ﬁcer has reasonable suspicion of other criminal activity to in-
dependently justify prolonging the stop. Id. at 355.
                                  A.
   The ﬁrst issue we address is whether Trooper Chapman
had a lawful basis to initiate the stop.1 We have little trouble


    1 We, of course, do not consider Trooper Chapman’s subjective moti-
vations for deciding to conduct a traﬃc stop. As the Supreme Court has
No. 20-2105                                                               9

concluding that he did. Under Illinois law, “[t]he driver of a
motor vehicle shall not follow another vehicle more closely
than is reasonable and prudent, having due regard for the
speed of such vehicles and the traﬃc upon and the condition
of the highway.” 625 ILCS 5/11-710(a). Trooper Chapman tes-
tiﬁed that Cole was less than two car lengths behind the car in
front of him. The magistrate judge credited that testimony
and made an express factual ﬁnding that Cole was following
too closely behind the other car. Cole does not challenge that
factual ﬁnding on appeal. Instead, he argues that the district
court failed to consider the statutory factors (speed of other
cars, traﬃc, and road conditions) when determining that
there was reasonable suspicion of a traﬃc violation. The ques-
tion, however, is whether Trooper Chapman reasonably be-
lieved that he saw a traﬃc violation, not whether Cole actu-
ally violated the statute. United States v. Muriel, 418 F.3d 720,
724 (7th Cir. 2005); see also United States v. Simon, 937 F.3d 820,
829 (7th Cir. 2019) (“If an oﬃcer reasonably thinks he sees a
driver commit a traﬃc infraction, that is a suﬃcient basis to
pull him over without violating the Constitution.”). As in
Muriel, the trooper’s “estimation” of a short following dis-
tance justiﬁed the stop. Muriel, 418 F.3d at 724; accord Lewis,
920 F.3d at 490.




unequivocally held, “[s]ubjective intentions play no role in ordinary,
probable-cause Fourth Amendment analysis.” Whren, 517 U.S. at 813. To
the extent that the dissent opposes the objective test established by Whren,
or suggests that police discretion informs how courts should approach
Fourth Amendment law more generally, that is an issue for the Supreme
Court, not us.
10                                                   No. 20-2105

                               B.
   The more substantial issue is whether Trooper Chapman
unlawfully prolonged the traﬃc stop by inquiring about
Cole’s itinerary.
                                1.
    To answer this question, we start with Rodriguez. There,
the Supreme Court held that “the tolerable duration of police
inquiries in the traﬃc-stop context is determined by the sei-
zure’s ‘mission.’” Rodriguez, 575 U.S. at 354 (quoting Illinois v.
Caballes, 543 U.S. 405, 407 (2005)). The mission of a traﬃc stop,
in turn, is “to address the traﬃc violation that warranted the
stop and attend to related safety concerns.” Id. (citations omit-
ted). Tasks within that mission include “determining whether
to issue a traﬃc ticket” and pursuing “‘ordinary inquiries in-
cident to [the traﬃc] stop.’” Id. at 355 (quoting Caballes, 543
U.S. at 408). Typically, the ordinary inquiries incident to a
traﬃc stop “involve checking the driver’s license, determin-
ing whether there are outstanding warrants against the
driver, and inspecting the automobile’s registration and proof
of insurance.” Id. Such inquiries fall within the mission of a
stop because they “serve the same objective as enforcement of
the traﬃc code: ensuring that vehicles on the road are oper-
ated safely and responsibly.” Id. Rodriguez distinguished
those ordinary inquiries from measures aimed at investigat-
ing other criminal activity, such as a dog sniﬀ for drugs. Id.
   As part of making these ordinary inquiries, no one dis-
putes that an oﬃcer may ask questions unrelated to the stop,
and even conduct a dog sniﬀ, if doing so does not prolong the
traﬃc stop. As the Supreme Court explained in Arizona v.
Johnson, 555 U.S. 323 (2009), “[a]n oﬃcer’s inquiries into
No. 20-2105                                                     11

matters unrelated to the justiﬁcation for the traﬃc stop … do
not convert the encounter into something other than a lawful
seizure, so long as those inquiries do not measurably extend
the duration of the stop.” Id. at 333; see Rodriguez, 575 U.S. at
354–55; Caballes, 543 U.S. at 408 (dog sniﬀ). This recognition
does not resolve this appeal because the record is undevel-
oped as to whether Trooper Chapman’s travel-plan questions
prolonged the stop. If they did not, then they would have
been permissible even if they exceeded the mission of the
stop. See Lewis, 920 F.3d at 492; United States v. Walton, 827 F.3d
682, 687 (7th Cir. 2016). But because the district court never
made such a factual ﬁnding, we put this issue aside and ask
whether Trooper Chapman’s travel-plan questions fell within
the mission of the stop, such that they could not have pro-
longed it in the ﬁrst place.
    Rodriguez did not list travel-plan questions among the or-
dinary inquiries of a traﬃc stop. See Rodriguez, 575 U.S. at 351.
From this, Cole infers that the Supreme Court must have
meant to exclude them. Judicial opinions are not statutes,
however, and we decline to extrapolate a holding about
travel-plan questions from the Supreme Court’s silence on
them in a case where they were not at issue. See United States
v. Skoien, 614 F.3d 638, 640 (7th Cir. 2010) (en banc). The ques-
tion presented in Rodriguez was “whether the Fourth Amend-
ment tolerates a dog sniﬀ conducted after completion of a
traﬃc stop.” Rodriguez, 575 U.S. at 350. The Court had no oc-
casion to reach—and did not reach—the propriety and per-
missible scope of travel-plan questions. We decline to read Ro-
driguez as creating an exhaustive list of mission-related in-
quiries. See United States v. Gholston, 1 F.4th 492, 496 (7th Cir.
2021) (noting that “[a] stop may call for a variety of measures
beyond” the ordinary inquiries listed in Rodriguez).
12                                                    No. 20-2105

    Though Rodriguez did not address whether travel-plan
questions fall within the mission of a traﬃc stop, it supplied
an analytical framework for answering that question.
Namely, we must ask whether, in the totality of circum-
stances, reasonable travel-plan questions, like the other ordi-
nary inquiries of a stop, are justiﬁed by the traﬃc violation
itself or by the “related” concerns of “[h]ighway and oﬃcer
safety.” Rodriguez, 575 U.S. at 354, 356–57. Our sister circuits
have followed this approach in deciding whether other un-
listed inquiries fall within the mission of a traﬃc stop. See, e.g.,
United States v. Buzzard, 1 F.4th 198, 203–04 (4th Cir. 2021);
United States v. Clark, 902 F.3d 404, 410–11 (3d Cir. 2018);
United States v. Evans, 786 F.3d 779, 786–87 (9th Cir. 2015).
    Applying the Rodriguez framework, we hold that travel-
plan questions ordinarily fall within the mission of a traﬃc
stop. To begin, travel-plan questions supply important con-
text for the violation at hand. If, for example, “a given driver
was speeding in order to get his pregnant wife to the hospi-
tal,” then perhaps this “extenuating circumstance” might per-
suade the oﬃcer to issue a warning or simply release the
driver. United States v. Brigham, 382 F.3d 500, 508 & n.6 (5th
Cir. 2004) (en banc); accord United States v. Cortez, 965 F.3d 827,
839 (10th Cir. 2020) (reasoning that oﬃcer’s travel-plan ques-
tions “could cast light on why Cortez had been speeding, ty-
ing them to the initial justiﬁcation for the stop”). In other cir-
cumstances, the context of a stop might counsel in favor of a
ticket or arrest. See Brigham, 382 F.3d at 508 & n.6.
    A driver’s travel plans may also inform an oﬃcer’s assess-
ment of roadway safety concerns beyond the immediate vio-
lation. An oﬃcer investigating a broken taillight, for example,
has a legitimate interest in knowing whether the driver is two
No. 20-2105                                                      13

miles from home or halfway through a cross-country trip. Cf.
United States v. Ellis, 497 F.3d 606, 613–14 (6th Cir. 2007) (hold-
ing that oﬃcer who stopped car for weaving “was justiﬁed in
asking the occupants general questions of who, what, where,
and why regarding their 3:23 a.m. travel,” as such questions
could help “determine the driver’s ability to safely operate the
vehicle”).
    At a more general level, “[t]ravel plans typically are re-
lated to the purpose of a traﬃc stop because the motorist is
traveling at the time of the stop.” United States v. Holt, 264 F.3d
1215, 1221 (10th Cir. 2001) (en banc), abrogated on other grounds
as recognized in Cortez, 965 F.3d at 839; see also United States v.
Collazo, 818 F.3d 247, 258 (6th Cir. 2016) (describing travel-
plan questions as “classic context-framing questions directed
at the driver’s conduct at the time of the stop” (quoting United
States v. Lyons, 687 F.3d 754, 770 (6th Cir. 2012))). In that sense,
travel-plan questions comport with the “public’s expectations
regarding ordinary inquiries incidental to traﬃc stops.” Cor-
tez, 965 F.3d at 839.
    In short, travel-plan questions are routine inquiries that
reasonably relate to the underlying traﬃc violation and road-
way safety. As a result, we hold that such questions ordinarily
fall within the mission of a traﬃc stop. This does not mean,
however, that oﬃcers have a free pass to ask travel-plan ques-
tions until they are subjectively satisﬁed with the answers. An
oﬃcer’s travel-plan questions, like the oﬃcer’s other actions
during the stop, must remain reasonable, and reasonableness
is an objective standard based on all the circumstances. Robi-
nette, 519 U.S. at 39.
   We are not alone in holding that travel-plan questions or-
dinarily fall within the mission of a traﬃc stop. In fact, every
14                                                    No. 20-2105

circuit to address the issue post-Rodriguez has reached the
same conclusion. Most recently, the Eleventh Circuit rejected
a defendant’s argument that an oﬃcer’s travel-plan questions
went beyond the mission of a stop, holding that “[g]enerally,
questions related to an individual’s traﬃc plans or itinerary
are ordinary inquires related to a traﬃc stop.” United States v.
Braddy, 11 F.4th 1298, 1311 (11th Cir. 2021). Five other circuits
agree. Cortez, 965 F.3d at 838 (“An oﬃcer may … inquire about
the driver’s travel plans.”); United States v. Garner, 961 F.3d
264, 271 (3d Cir. 2020) (“[S]ome questions relating to a driver’s
travel plans ordinarily fall within the scope of the traﬃc
stop.”); United States v. Smith, 952 F.3d 642, 647 (5th Cir. 2020)
(observing that an oﬃcer “may … ask about the purpose and
itinerary of the occupants’ trip” (quoting Brigham, 382 F.3d at
508)); United States v. Dion, 859 F.3d 114, 125 (1st Cir. 2017)
(“[O]ur case law allows an oﬃcer carrying out a routine traﬃc
stop to … inquire into the driver’s itinerary.”); Collazo, 818
F.3d at 258 (“Questions relating to travel plans … rarely of-
fend our Fourth Amendment jurisprudence.” (quoting Lyons,
687 F.3d at 770)); see also United States v. Callison, 2 F.4th 1128,
1131 n.2 (8th Cir. 2021) (noting that “[i]n some post-Rodriguez
cases we have at least suggested that travel-related questions
remain a ‘permissible’ part of routine traﬃc stops in the
Eighth Circuit.” (citing United States v. Murillo-Salgado, 854
F.3d 407, 415 (8th Cir. 2017))).
    The dissent claims that the Tenth Circuit has taken a more
nuanced approach to travel-related questions in United States
v. Gomez-Arzate. 981 F.3d 832 (10th Cir. 2020). In Gomez-Arzate,
however, the oﬃcers’ travel-plan questions came after the traf-
ﬁc stop was completed, in contrast to the questions from
Trooper Chapman that occurred during the traﬃc stop. Id. at
840 n.3 (“Here, though, the traﬃc stop had eﬀectively been
No. 20-2105                                                            15

completed before the VIN search and questioning about
travel plans.”).
    We, too, have approved of travel-plan questions post-Ro-
driguez. In Lewis, the defendant complained that an oﬃcer
spent several minutes “asking about irrelevant travel matters”
during a traﬃc stop, thereby prolonging the stop in violation
of the rule announced in Rodriguez. 920 F.3d at 492. We re-
jected the argument. To begin, we dismissed the idea that the
oﬃcer’s ﬁrst question—“Where are we headed to today,
sir?”—was unrelated to the stop, remarking that “[o]ﬃcers
across the country would be surprised if we countenanced the
characterization of this basic, routine question as irrelevant to
a traﬃc stop.” Id. Lewis’s response to the oﬃcer’s ﬁrst ques-
tion was “not entirely forthcoming,” and prompted the oﬃcer
to ask several follow-up questions. Lewis answered these
questions in a similarly evasive manner. Again, adhering to
the rule announced in Rodriguez, we squarely rejected Lewis’s
argument that the oﬃcer’s travel-plan questions were imper-
missible: “The Constitution allows an oﬃcer to ask these
questions during a traﬃc stop, especially when the answers
objectively seem suspicious.” 2 Id.
    Lewis reinforces an important corollary of our holding: Of-
ﬁcers asking travel-plan questions may also ask reasonable
follow-up questions based on a driver’s responses. Travel-
plan questions are not mere formalities; they serve important


    2 The dissent attempts to recast Lewis, asserting that “the most im-
portant reason [we] had for aﬃrming denial of the motion to suppress
there was that the defendant had simply failed as a matter of fact to show
that the questioning had actually prolonged the stop.” But that reading
contradicts the opinion’s unambiguous language. Lewis, 920 F.3d at 492.
16                                                 No. 20-2105

law-enforcement purposes, and therefore an oﬃcer has an in-
terest not only in asking such questions but also in receiving
truthful answers to them. If a driver’s responses are evasive,
inconsistent, or improbable, the oﬃcer need not accept them
at face value and move on. To the contrary, the oﬃcer may
ask reasonable follow-up questions to clarify the answers.
This was our point in Lewis, when we said the Fourth Amend-
ment permits travel-plan questions during traﬃc stops “espe-
cially when the answers objectively seem suspicious.” Id.; see
also Murillo-Salgado, 854 F.3d at 415 (holding that an oﬃcer
may take the time to respond to “legitimate complications”
that arise during the “routine tasks” of a traﬃc stop); Dion,
859 F.3d at 124–25 (explaining that a Terry stop is not a “snap-
shot of events frozen in time and place” and that an oﬃcer’s
“actions must be fairly responsive to the emerging tableau”
(internal quotation and citation omitted)). It is only when an
oﬃcer’s follow-up questions go too far and become unreason-
able that a stop risks becoming prolonged.
                               2.
   Applying these principles here, we hold that Trooper
Chapman’s travel-plan questions during the initial roadside
detention fell within the mission of the traﬃc stop and did not
unlawfully prolong the traﬃc stop.
    At the outset, it is important to recall the sequence of
events here. Trooper Chapman asked his travel-plan ques-
tions following Cole’s elusive and confusing account. These
travel-plan questions related closely to his questions about
Cole’s Arizona license and California registration. See Braddy,
11 F.4th at 1311 (holding that the oﬃcer’s questions about li-
cense, registration, and travel plans were within the mission
of stop). Before inquiring into Cole’s travel, Trooper
No. 20-2105                                                    17

Chapman asked Cole about the discrepancy between his Ari-
zona license and California registration. Cole’s response ref-
erenced three other states beyond Arizona and California. He
explained that he was a chef who split his time between Los
Angeles, Maryland, and New York, adding that he kept his
Arizona license because of the expiration date and that he
might be moving to Florida soon. When Trooper Chapman
began generally inquiring about Cole’s travel details, Cole
added two more states into the mix: He said he had stopped
in Cincinnati on his way from Maryland to Colorado. By this
point, Cole had mentioned seven diﬀerent states—none of
which was Illinois—in response to Trooper Chapman’s ques-
tions about his license, registration, and basic trip details. See
id. (holding that the oﬃcer’s travel-plan questions were “or-
dinary inquiries related to the traﬃc stop, especially given the
fact that Braddy was driving a vehicle on Alabama roads with
an obstructed Florida license plate that was not registered to
him”).
    Understandably, Trooper Chapman had follow-up ques-
tions. Cole evaded some of these follow-up questions. After
Cole volunteered that he worked as a chef, for example,
Trooper Chapman asked where he worked. Cole replied with
his occupation, saying he was a personal chef. Trooper Chap-
man tried asking the same question another way: “Who do
you work for?” This time, Cole responded that he worked for
two former professional football players and that “in be-
tween” he was a chef. Cole similarly evaded Trooper Chap-
man’s question about where he began his trip, prompting
Trooper Chapman to repeat the question. Cole’s explanation
for where he was currently living was also hard to pin down.
Initially, he said he spent most of his time in Los Angeles,
while noting that he might be moving to Florida. When
18                                                    No. 20-2105

Trooper Chapman followed up, however, Cole seemed to
agree that he was currently living in Maryland. In addition to
evading questions, Cole gave confusing and improbable an-
swers that prompted other reasonable follow-up questions.
See Dion, 859 F.3d at 125–26 (where driver with Colorado
plates produced an Arizona license and “described his travel
itinerary as a return trip from a cross-country road trip to visit
a CPA in Pennsylvania,” an oﬃcer’s follow-up questions on
the same subject were “both prompted and warranted” by
that “odd answer to a concededly appropriate question about
travel itinerary”).
    Under these circumstances, Trooper Chapman’s travel-
plan questions were reasonable. Trooper Chapman ques-
tioned Cole about the basic details of his travel—which were
relevant to the traﬃc violation and roadway safety—and
asked reasonable follow-up questions based on Cole’s elusive
answers. See Lewis, 920 F.3d at 492. As Trooper Chapman tes-
tiﬁed, his questions were aimed at “piec[ing] together” Cole’s
“inconsistent” answers to basic travel-plan questions. He was
not, as Cole suggests, conducting a “ﬁshing expedition” for
information that might generate reasonable suspicion to pro-
long the stop. Dion, 859 F.3d at 128 n.12 (citing United States v.
Pruitt, 174 F.3d 1215, 1221 (11th Cir. 1999)); cf. Cortez, 965 F.3d
at 840 (holding that “repetitive” and “in depth” questions
about travel details were unrelated to traﬃc stop because
such questions “neither helped investigate the original infrac-
tion—speeding—nor could they reasonably be characterized
as relating to oﬃcer safety”); United States v. Macias, 658 F.3d
509, 519 (5th Cir. 2011) (holding that oﬃcer’s detailed ques-
tions about driver’s mother, children, and past encounters
with law enforcement went beyond mission of stop because
they bore no relation to driver’s failure to wear a seatbelt).
No. 20-2105                                                   19

    Cole complains that Trooper Chapman’s questions went
beyond the details of his travel and into unrelated matters,
such as his occupation. But Cole initially volunteered his oc-
cupation almost three minutes into the stop in response to a
question about his license and registration and repeatedly re-
turned to it when explaining his travel and living situation, so
it was reasonable for Trooper Chapman to ask a few follow-
up questions about it. Cole also complains about the length of
Trooper Chapman’s travel-plan questions (just under ﬁve
minutes). But “we repeatedly have declined to adopt even a
rule of thumb that relies on the number of minutes any given
stop lasts.” Gholston, 1 F.4th at 496 n.4. Reasonableness is the
touchstone, and what is reasonable depends on the circum-
stances of a case. Lange, 141 S. Ct. at 2017. Here, Trooper Chap-
man’s questioning stayed within reasonable limits given
Cole’s responses.
   Because Trooper Chapman’s questioning was reasonable,
we need not speculate about scenarios in which travel-plan
questions might go too far. For now, it is enough to say that
travel-plan questions go too far when they are no longer rea-
sonably related to the stop itself (and related safety concerns)
but rather reﬂect an independent investigation of other crim-
inal activity. See Rodriguez, 575 U.S. at 356–57.
                               3.
    We do not address whether Trooper Chapman’s addi-
tional questions at the gas station stayed within the mission
of the stop because he developed reasonable suspicion of
other criminal activity less than nine minutes into the stop,
before he told Cole he would issue him a warning and before
they drove to the gas station.
20                                                  No. 20-2105

    Reasonable suspicion exists when, considering the totality
of the circumstances, an oﬃcer has “a particularized and ob-
jective basis for suspecting the particular person stopped of
criminal activity.” Navarette, 572 U.S. at 396–97 (quoting
United States v. Cortez, 449 U.S. 411, 417–18 (1981)). A hunch is
not enough, but “the likelihood of criminal activity need not
rise to the level required for probable cause, and it falls con-
siderably short of satisfying a preponderance of the evidence
standard.” United States v. Arvizu, 534 U.S. 266, 274 (2002). The
standard “allows oﬃcers to draw on their own experience
and specialized training to make inferences from and deduc-
tions about the cumulative information available to them that
‘might well elude an untrained person.’” Id. at 273 (quoting
Cortez, 449 U.S. at 418).
     This standard was met here. Cole was driving on an Illi-
nois interstate with an Arizona driver’s license and a Califor-
nia registration, and his explanation for this discrepancy was
confusing at best. According to Cole, he was a traveling per-
sonal chef who split his time between California, Maryland,
and New York, traveling to each destination by car so that he
could bring his pots and bicycle with him. He claimed to have
had a job at one point in Arizona, and he added that he might
be moving to Florida soon, again for job-related reasons. Even
if this story was not inconceivable, Trooper Chapman reason-
ably suspected that it was false. See Walton, 827 F.3d at 688–89
(ﬁnding reasonable suspicion based in part on defendant’s
“implausible” answers).
   The details of Cole’s current trip were equally dubious and
seemed to evolve throughout the conversation. In Cole’s tell-
ing, he had driven from Maryland to Cincinnati to multiple
locations in Colorado and then to Illinois on his way back to
No. 20-2105                                                  21

Maryland—all in just four or ﬁve days. He originally said he
spent two of the four days in Cincinnati for work, but he
quickly changed his answer and said he just passed through
Cincinnati. His story about Colorado also seemed to evolve.
Initially, he said he met friends and family in “the springs.”
Then, he said he met some friends at the Springs and went to
Boulder to visit a buddy. After that, he said he met some
friends in Colorado because one of them was getting a di-
vorce. Cole’s improbable and inconsistent answers about his
trip details reasonably increased Trooper Chapman’s suspi-
cions. See Lewis, 920 F.3d at 493 (ﬁnding reasonable suspicion
based in part on defendant’s “suspiciously inconsistent” an-
swers).
    Cole’s extreme nervousness reinforced the suspicion. See
United States v. Rodriguez-Escalera, 884 F.3d 661, 669 (7th Cir.
2018) (“[N]ervousness is certainly a factor that can support
reasonable suspicion.”). Trooper Chapman testiﬁed that Cole
was “extremely nervous” throughout the stop, adding that
his neck was sweaty and that he was breathing heavily. Cole
suggests that the dash camera video refutes this testimony,
but the dash camera was not pointed at Cole during the con-
versation. Moreover, the dash camera records Cole himself
commenting on how nervous he was, so if anything, it sup-
ports Trooper Chapman’s testimony. Cole cannot show that
the district court’s ﬁnding of extreme nervousness was clearly
erroneous. See id. (holding that the district court did not have
to credit oﬃcer’s testimony that defendant was nervous
“when the court’s own review of the traﬃc stop footage led it
to the opposite conclusion”).
    Additional factors further supported Trooper Chapman’s
belief that Cole was engaged in criminal activity. Cole’s car
22                                                     No. 20-2105

was newly registered and insured. Trooper Chapman found
this suspicious because he knew that drug traﬃckers often
traded and reregistered cars and purchased insurance for spe-
ciﬁc trips rather than maintaining permanent insurance. Cole
disputes the district court’s ﬁnding that Trooper Chapman
possessed this knowledge. But Deputy Suttles’s message to
Trooper Chapman provided the car’s most recent registration
date, and Cole, himself, told Trooper Chapman that he re-
cently acquired the “insurance, registration, and all that
stuﬀ.” So here too, Cole has not shown clear error. In addition
to the recent registration and insurance purchase, Trooper
Chapman knew from Deputy Suttles that Cole had a covering
over his rear cargo area, which was common among persons
engaged in criminal activity. Finally, Trooper Chapman no-
ticed that Cole had limited luggage in his car—one small
backpack—which was hard to square with Cole’s cross-coun-
try road trip.
    Taken together and assessing the totality of the circum-
stances known to Trooper Chapman, these factors created
reasonable suspicion that Cole was engaged in criminal activ-
ity. We need not consider the other factors that the govern-
ment relies on—e.g., the make of Cole’s car (a Volkswagen),
Cole’s origin in Los Angeles (a supposed drug source loca-
tion), his travel on Interstate-55 (a supposed drug corridor),
and his slow speed and rigid driving posture—though we re-
mind the government to refrain from using criteria so broad
as to subject “a very large category of presumably innocent
travelers” to “virtually random seizures.” Reid v. Georgia, 448
U.S. 438, 441 (1980); see also United States v. Street, 917 F.3d 586,
594 (7th Cir. 2019) (“Without more, a description that applies
to large numbers of people will not justify the seizure of a par-
ticular individual.”).
No. 20-2105                                               23

   Because Trooper Chapman developed reasonable suspi-
cion less than nine minutes into the stop, during the initial
roadside detention, he had a lawful basis for prolonging the
stop to conduct a dog sniﬀ at the gas station, where Cole’s
increasingly incoherent answers and criminal history further
increased his suspicions. See Rodriguez, 575 U.S. at 355.
                            III.
  The trooper’s actions in this case complied with the Fourth
Amendment, so we AFFIRM the district court’s denial of Cole’s
motion to suppress.
24                                                     No. 20-2105

    HAMILTON, Circuit Judge, joined by ROVNER and WOOD,
Circuit Judges, dissenting. A broken taillight, a too-sudden
lane change, or tailgating for a few seconds allows a police
officer to carry out a traffic stop even if the officer’s real pur-
pose is to investigate other possible crimes. In such stops, no
one sees a problem with an officer’s question or two about
where the driver is coming from or going. Answers to those
questions may help the officer understand the situation and
assess the driver’s attitude and potential threats. The major-
ity’s decision today errs, however, by going much further.
Under the majority opinion, the officer may also subject a
driver and passengers to repetitive and detailed questioning
about where they are coming from and where they are going
until the officer is satisfied that the answers are truthful. Ante at
15–16. Given the low “hit rate” of police searches of vehicles
for drugs, this decision will enable police officers to harass
and humiliate civilians far more often than they actually turn
up significant quantities of drugs.
     The scope of permissible police activity in pretextual traf-
fic stops is important. By adopting a general presumption al-
lowing such detailed interrogation as occurred in this case,
the majority enables police officers to subject almost any mo-
torist to similar interrogation, delay, and even humiliation, for
little gain in terms of law enforcement. See Jeannine Bell, The
Violence of Nosy Questions, 100 B.U. L. Rev. 935 (2020) (criticiz-
ing wide discretion for officers to ask “nosy” questions on
fishing expeditions that humiliate and anger drivers stopped
for minor traffic infractions).
    This case presents a pretextual traffic stop based on a po-
lice officer’s hunch that the car was carrying drugs. The video
recording and the officer’s later testimony show that, almost
No. 20-2105                                                    25

from the very outset, the officer prolonged the stop by ques-
tioning the driver at length and in detail on subjects beyond
the legal justification for the stop. Under Rodriguez v. United
States, 575 U.S. 348 (2015), the officer’s prolonging of this stop
violated the Fourth Amendment. We should order suppres-
sion of evidence found later in the stop.
   To be sure, in some traffic stops, some questions about
travel plans will be relevant. For example, an officer who has
reason to believe the driver is impaired by fatigue will want
to know how long the driver has been on the road. In such
cases, an officer should have little difficulty explaining his
questioning in terms of the lawful purpose of the stop. This
stop for tailgating was not such a stop, and the officer offered
no such lawful explanation. I respectfully dissent.
    To explain my conclusion, Part I of this opinion outlines
the legal doctrines allowing pretextual stops and their well-
known consequences. Part II lays out important limits the Su-
preme Court has imposed on such pretextual traffic stops, in
terms of both time and the activities an officer may engage in
unless and until he develops at least reasonable suspicion of
some criminal activity. Part III explains why the traffic stop of
defendant Janhoi Cole was prolonged in violation of the
Fourth Amendment. Part IV identifies further problems in the
majority’s decision. Part V concludes with some suggestions
for going forward in similar cases.
I. Pretextual Traffic Stops and Their Effects
   In Whren v. United States, 517 U.S. 806 (1996), the Supreme
Court held that the reasonableness of a traffic stop under the
Fourth Amendment must be decided using an objective
standard, not the officer’s actual purposes. Whren thus gave
26                                                    No. 20-2105

police officers wide latitude to stop vehicles for reasons hav-
ing nothing to do with the traffic laws that provide lawful pre-
texts for the stops.
    Many of those traffic laws also give an officer considerable
room for judgment and discretion in applying them. In this
case, for example, the stop was justified based on a perceived
violation of this law: “The driver of a motor vehicle shall not
follow another vehicle more closely than is reasonable and pru-
dent, having due regard for the speed of such vehicles and the
traffic upon and the condition of the highway.” 625 ILCS 5/11-
710(a) (emphasis added). Extending that discretion even fur-
ther, courts will uphold a traffic stop based on not only the
actual facts and law but even an officer’s reasonable mistake
of fact or law. Heien v. North Carolina, 574 U.S. 54, 61 (2014).
     The combination of the objective test under Whren, the
number and detail of traffic laws, and the discretion inherent
in applying those laws gives police officers the power to stop
nearly any vehicle if they watch it for more than a few
minutes. See David A. Harris, “Driving While Black” and All
Other Traffic Offenses: The Supreme Court and Pretextual Traffic
Stops, 87 J. Crim. L. & Criminology 544, 545, 558–59 (1997) (“In
the most literal sense, no driver can avoid violating some traf-
fic law during a short drive, even with the most careful atten-
tion;” “with the traffic code in hand, any officer can stop any
driver any time”); Barbara C. Salken, The General Warrant of
the Twentieth Century? A Fourth Amendment Solution to Un-
checked Discretion to Arrest for Traffic Offenses, 62 Temp. L. Rev.
221, 223 (1989) (“The innumerable rules and regulations gov-
erning vehicular travel make it difficult not to violate one of
them at one time or another.”). As then-Attorney General
Robert Jackson said long ago, “We know that no local police
No. 20-2105                                                     27

force can strictly enforce the traffic laws, or it would arrest
half the driving population on any given morning.” Robert
Jackson, The Federal Prosecutor, Address Delivered at the Second
Annual Conference of United States Attorneys (April 1, 1940),
quoted in Morrison v. Olson, 487 U.S. 654, 727–28 (1988)
(Scalia, J., dissenting).
    The phrase “Driving While Black” reflects long recogni-
tion of how Whren enables racially discriminatory stops and
searches. See, e.g., Tracey Maclin, Cops and Cars: How the Au-
tomobile Drove Fourth Amendment Law, 99 B.U. L. Rev. 2317,
2347–49 (2019); David A. Harris, Profiles in Injustice: Why Ra-
cial Profiling Cannot Work 30 (2002); David A. Sklansky, Traffic
Stops, Minority Motorists, and the Future of the Fourth Amend-
ment, 1997 Sup. Ct. Rev. 271, 308–16.
    These police tactics subject large numbers of innocent
drivers to this sort of harassment and humiliation for minimal
gains in drug interdiction. For judges who see these tactics
primarily in criminal prosecutions in the rare cases where
dealer quantities of drugs were found, it’s easy to lose sight of
this reality. Empirical studies based on millions of traffic stops
show: (1) that police departments have exploited Whren to
carry out pretextual stops on a massive scale; (2) that Black
and Hispanic drivers are subjected to such stops and ensuing
searches at substantially higher rates than white drivers; and
(3) that pretextual stops rarely find drugs, let alone dealer
quantities of drugs. The empirical studies have used statistical
methods to control for variables other than racial profiling,
and the disparities remain dramatic. E.g., Emma Pierson et al.,
A Large-Scale Analysis of Racial Disparities in Police Stops Across
the United States, 4 Nature Human Behavior 736 (2020) (based
on data from nearly 100 million stops nationwide); Stephen
28                                                    No. 20-2105

Rushin & Griffin Edwards, An Empirical Assessment of Pre-
textual Stops and Racial Profiling, 73 Stan. L. Rev. 637 (2021)
(based on data from over 8 million stops in Washington state);
Frank R. Baumgartner, Derek A. Epp & Kelsey Shoub, Suspect
Citizens 215 (2018) (based on 18 years of data in North Caro-
lina); Samuel R. Gross & Katherine Y. Barnes, Road Work: Ra-
cial Profiling and Drug Interdiction on the Highway, 101 Mich. L.
Rev. 651, 666–67 (2002) (based on three years of data from
Maryland State Police). The Department of Justice’s own data
has long supported the conclusion that Black and Hispanic
drivers are significantly more likely than white drivers to be
searched during a traffic stop. Patrick A. Langan et al., Bureau
of Justice Statistics, Contacts Between Police and the Public, at
18 (2001).
    For example, the North Carolina study found that, on av-
erage, Black drivers were twice as likely to be searched as
white drivers, with some police forces having much higher
rates of racial disparity. The empirical work also shows that
when police use traffic stops to search for drugs, a small frac-
tion of searches turn up any drugs, and the proportion finding
dealer quantities of drugs is much lower still. The North Car-
olina study looked at data from more than 20 million traffic
stops. Searches were carried out in a small fraction, about
690,000, or 3.36%. Baumgartner et al., Suspect Citizens 59.
Drugs were found—in any quantity—in 96,841 of those stops,
or 14% of all searches. Id. at 62. Typically, dealer quantities are
found in a small fraction of those. See Gross & Barnes, 101
Mich. L. Rev. at 695–97 (88.8% of Maryland State Police vehi-
cle searches in drug corridor did not locate dealer quantities
of drugs). In other words, these intrusive and humiliating po-
lice tactics are used disproportionately on Black and Hispanic
drivers, the vast majority of whom are not trafficking drugs,
No. 20-2105                                                              29

and thus whose cases do not wind up in criminal courts to
shape Fourth Amendment jurisprudence. 1
II. Limits on Pretextual Stops
    While pretextual traffic stops are easy to initiate, the Su-
preme Court has tried to impose some legal limits on them.
Most important, such a stop is limited by time and the pur-
pose that makes the stop lawful in the first place. A seizure
that is “lawful at its inception” can violate the Fourth Amend-
ment if it is “prolonged beyond the time reasonably required
to complete” the initial mission of the stop. Illinois v. Caballes,
543 U.S. 405, 407 (2005).
    The Supreme Court took an important step to make this
limit effective in Rodriguez v. United States, 575 U.S. 348 (2015),
which established the governing law for this appeal. In Rodri-
guez, a police officer had carried out a traffic stop for a car that
had driven onto the shoulder of the highway. After the officer
had issued and explained a written warning to the driver, he
insisted that the driver could not leave until another officer
arrived some minutes later with a drug-sniffing dog, which
led to a search that found drugs in the car.
    The district court in Rodriguez denied a motion to sup-
press, applying circuit precedent holding that dog sniffs that
occur shortly after completion of the traffic stop did not vio-
late the Fourth Amendment if the intrusion on the driver’s lib-
erty was “de minimis.” 575 U.S. at 353. Rodriguez rejected that




    1For interested readers, the articles cited in the text cite in turn nu-
merous other sources on the doctrinal questions and empirical effects of
Whren’s pretextual stops.
30                                                 No. 20-2105

“de minimis” exception. The Court vacated the denial of the
motion to suppress and remanded.
    Establishing guidance that applies here, Rodriguez ex-
plained that “a police stop exceeding the time needed to han-
dle the matter for which the stop was made violates the Con-
stitution’s shield against unreasonable seizures.” 575 U.S. at
350. During a traffic stop, the police officer must stick to the
“mission” of the seizure: ensuring road safety and determin-
ing whether to issue a traffic ticket. “Typically such inquiries
involve checking the driver’s license, determining whether
there are outstanding warrants against the driver, and in-
specting the automobile’s registration and proof of insur-
ance.” Id. at 355. An officer may not prolong the stop, “absent
the reasonable suspicion ordinarily demanded to justify de-
taining an individual.” Id. The latter qualification creates an
opportunity for exploiting pretextual stops. The question for
the officer is whether he can see, hear, or smell anything that
provides reasonable suspicion for expanding the scope of the
pretextual traffic stop.
III. Prolonging the Stop in This Case
   One way to prolong a pretextual stop is to question drivers
and passengers about topics beyond the mission authorized
by the supposed ground for the stop. That’s what happened
here, for all to see in Trooper Chapman’s video recording of
the stop.
   The trooper’s tailgating rationale for stopping Janhoi Cole
was obviously pretextual. The trooper had received the tip
from Deputy Suttles, who suspected the car was transporting
No. 20-2105                                                                  31

drugs. 2 The trooper began following Cole’s car, looking for a
reason to stop him. Cole was driving so carefully that it took
a while. (The most startling fact in this case is that Cole was
driving so carefully that Deputy Suttles never managed to
identify even a pretext for stopping him.) Trooper Chapman
also found no basis for a stop until, finally, Cole entered a con-
struction zone where interstate highway lanes had to merge.
The trooper saw another vehicle cut off Cole’s car. The trooper
did not stop the other vehicle for its dangerous maneuver. In-
stead, he stopped Cole on the ground that he had followed
that other car too closely for a few seconds.
    Following too closely was enough, based on the district
court’s factual findings, to permit the stop under Whren. But
the supposed infraction of following too closely also set limits
on the trooper’s powers over Cole and his vehicle, unless and




    2 The tip from Deputy Suttles fell well short of reasonable suspicion.
He observed that Cole was driving below the speed limit on an interstate
highway in a car with California plates. He sat with an erect posture that
Suttles thought was unusual, and he had empty fast-food wrappers in the
car. Suttles also apparently thought that two contradictory observations
added to the suspicion: that the only luggage he could see was a small
backpack and that the cargo area of the car was covered. See generally
Kansas v. Glover, 589 U.S. ––, ––, 140 S. Ct. 1183, 1190 (2020) (traffic stops
do not “allow officers to stop drivers whose conduct is no different from
any other driver’s”); United States v. Flores, 798 F.3d 645, 649 (7th Cir. 2015)
(“A suspicion so broad that would permit the police to stop a substantial
portion of the lawfully driving public ... is not reasonable.”); United States
v. Ingrao, 897 F.2d 860, 865 (7th Cir. 1990) (reversing denial of motion to
suppress where arrest was based in part on defendant’s cautious driving:
“The mere lawful operation of a motor vehicle should not be considered
suspicious activity absent extraordinary contemporaneous events.”).
32                                                    No. 20-2105

until the trooper developed reasonable suspicion for further
investigation.
    Under Rodriguez and Caballes, the trooper’s authority to
pull Cole over did not give him license to detain Cole for a
speculative search or interrogation for “evidence of ordinary
criminal wrongdoing.” Rodriguez, 575 U.S. at 355, quoting City
of Indianapolis v. Edmond, 531 U.S. 32, 41 (2000). Police deten-
tion, however brief, is not a “minor inconvenience and petty
indignity.” Terry v. Ohio, 392 U.S. 1, 10, 16–17 (1968) (citation
omitted). The Supreme Court has “emphatically reject[ed]”
the notion that the Constitution does not regulate an officer’s
actions when he “accosts an individual and restrains his free-
dom to walk away.” Id. at 16.
    In pretextual traffic stops, courts should expect just the
sort of “mission creep” that we see in this case. See State v.
Jimenez, 420 P.3d 464, 476, 308 Kan. 315, 329–30 (2018) (follow-
ing Rodriguez to affirm suppression of evidence from stop pro-
longed by questions about travel plans unrelated to grounds
for stop). After all, if a stop is actually motivated by a different
purpose, we should expect officers to behave consistently
with their actual purposes, not with the legal fiction that
Whren tolerates.
    That’s what happened here, as the record makes obvious.
Even before stopping Cole, the trooper had already obtained
most of the information that Rodriguez treats as routinely
within the scope of a traffic stop: “determining whether to is-
sue a traffic ticket, … checking the driver’s license, determin-
ing whether there are outstanding warrants against the
driver, and inspecting the automobile’s registration and proof
of insurance.” 575 U.S. at 355. The trooper already had ob-
tained the registration information for the car showing Cole
No. 20-2105                                                                33

as the owner. He also had Cole’s license information. (As for
the last Rodriguez item, insurance, the trooper already knew
that insurance information was on file, though he did not yet
have details. He did nothing more about insurance infor-
mation until nearly twenty minutes into the stop, well after he
had improperly prolonged the stop by interrogating Cole on
other topics.)
    Instead of focusing on the tailgating and the routine topics
of license, registration, and insurance, the trooper almost im-
mediately focused on a different topic: detailed, repetitive,
and intrusive questioning about Cole’s travel itinerary. The
questioning went far beyond a quick and routine “where are
you headed?” or “where are you coming from?” In the ten
minutes of the stop while the trooper kept Cole in the police
car at the side of the highway, about six minutes consisted of
questioning about Cole’s itinerary and the related topic of his
work.3
    We now know that Cole’s confusing answers on those top-
ics were not true. And as a person who was transporting a
substantial quantity of illegal drugs, Cole elicits little sympa-
thy. Yet the stakes here are more important than this one drug

    3 The majority suggests that its essay on travel plan questions results
from the record being “undeveloped” on whether the trooper’s question-
ing actually prolonged the stop. Ante at 11. The record is more than suffi-
cient to say that it did. We have the video recording of the stop. We also
know that the trooper already had license and registration information at
the outset, and that he did not seek more insurance information until
much later in the stop. The government has not tried to show that the
trooper was actually making any progress on the subject of the traffic stop
while he interrogated Cole about his travel plans. Cf. United States v. Lewis,
920 F.3d 483, 492 (7th Cir. 2019) (video and testimony showed that officer
worked on warning while questioning driver about itinerary).
34                                                           No. 20-2105

courier. The evidence is clear that police use these tactics to
stop, search, and even humiliate large numbers of innocent
drivers, and that these tactics are used disproportionately on
Blacks and Hispanics.
    Rodriguez makes clear that a traffic stop’s mission is “to
address the traffic violation that warranted the stop and at-
tend to related safety concerns.” 575 U.S. at 354 (internal cita-
tion omitted); United States v. Clark, 902 F.3d 404, 411 (3d Cir.
2018) (affirming suppression of evidence obtained by pro-
longing traffic stop by questioning driver about his criminal
history). Hence the Rodriguez endorsement of the usual litany:
license, registration, and insurance, and an opportunity to
check for outstanding warrants. 575 U.S. at 355.
    Courts need to guard against unjustified expansion and
prolonging of pretextual stops by questioning on other topics.
As the Third Circuit explained in Clark: “Not all inquiries dur-
ing a traffic stop qualify as ordinarily incident to the stop’s
mission. In particular, those ‘measure[s] aimed at detect[ing]
evidence of ordinary criminal wrongdoing’ do not pass mus-
ter.” 902 F.3d at 410 (alterations in original), quoting Rodri-
guez, 575 U.S. at 355. Since detecting evidence of ordinary
criminal wrongdoing is often the officer’s real purpose, we
should not be surprised when an officer devotes his time to
pursuing his real aims rather than the pretext.4


     4 Whren established that whether a stop is constitutionally permissible

depends on objective grounds, not the officer’s subjective purpose,
whether pretextual or not. Contrary to the majority’s footnote, however,
that rule about the legality of the initial stop does not mean that courts
must or may close their eyes to what was really going on. Cf. ante at 8 n.1.
When considering factual issues that govern whether the officer has gone
No. 20-2105                                                                 35

    Where should we draw the lines on how an officer may
spend his time in such a stop? We start with the Rodriguez list
of the activities typically part of the mission of the traffic stop:
checking license, registration, and insurance information, and
the opportunity to check for outstanding warrants. 575 U.S. at
355. Those actions are designed to protect highway safety by
determining whether the vehicle and driver are authorized to
be on the road at all, and whether they might pose a particular
danger to others on the road. Rodriguez also recognized that
traffic stops can be dangerous for police officers, id. at 356, so
that measures to protect an officer’s safety can also be author-
ized. Beyond the listed topics, however, which activities are
permissible quickly becomes a very case-specific problem. It
defies general rules like the majority’s presumption here.
    Courts applying Rodriguez must consider whether an of-
ficer spent time on matters apart from those safety-based mat-
ters authorized by the lawful but pretextual basis for the stop,
at least unless and until the officer developed reasonable sus-
picion to pursue other matters. See, e.g., United States v. Cortez,
965 F.3d 827, 839–40 (10th Cir. 2020) (assuming without de-
ciding that thirteen minutes of repetitive questioning about
how long driver and passenger had been in town where jour-
ney started was not justified by traffic stop, but officer already

beyond the boundaries permitted by the traffic stop, courts should pay
attention to reality rather than legal fiction. Rodriguez itself makes that
much clear. It directs lower federal courts to consider actual facts in eval-
uating whether a stop has been extended impermissibly. 575 U.S. at 357
(“The reasonableness of a seizure, however, depends on what the police
in fact do. See Knowles [v. Iowa, 525 U.S. 113, 115–17 (1998).] In this regard,
the Government acknowledges that ‘an officer always has to be reasona-
bly diligent.’ Tr. of Oral Arg. 49. How could diligence be gauged other
than by noting what the officer actually did and how he did it?”).
36                                                    No. 20-2105

had independent reasonable suspicion of human smuggling
before beginning those questions); Clark, 902 F.3d at 410–11
(stop improperly prolonged to question driver about his crim-
inal history); United States v. Evans, 786 F.3d 779, 787 (9th Cir.
2015) (stop improperly prolonged to see if driver had
properly registered in Nevada registry of ex-felons).
    Turning to questions about travel plans, courts must “in-
quire whether, on the facts of the particular case, [itinerary]
questioning is within the traffic stop’s mission” and if not,
must determine whether the questioning impermissibly
lengthened the stop. 4 Wayne R. LaFave, Search & Seizure
§ 9.3(d) (6th ed. 2020). There has never been a problem with a
brief question or two about travel like, “Where are you
headed today?” or “Where are you coming from?” As the ar-
resting officer in Cortez testified, innocuous background ques-
tions can help an officer assess a driver’s stress and possible
evasion, and they may help an officer gauge how cautious he
needs to be in the stop. 965 F.3d at 839.
    Similarly, if an officer has reason to suspect that a driver
may be impaired by fatigue, alcohol, or drugs, questioning
about how long the driver has been on the road and where he
is headed might help the officer assess the driver’s condition
and any dangers that might be posed. Jimenez, 420 P.3d at 475–
76, 308 Kan. at 329; see also Navarette v. California, 572 U.S. 393,
402–03 (2014) (report that truck had forced another vehicle off
road gave officer reasonable suspicion that driver was im-
paired, permitting stop to investigate). In other cases, infor-
mation about travel plans might help an officer decide
whether to issue a ticket or a warning, or perhaps even to hop
back in the police car and lead a speeding car to a hospital so
No. 20-2105                                                  37

the passenger can safely give birth. See United States v.
Brigham, 382 F.3d 500, 508 & n.6 (5th Cir. 2004) (en banc).
    This case, however, is not about such brief, routine, and
easily justifiable questions. This case is about whether an of-
ficer may start with those questions and then prolong the stop
while continuing to probe the answers, looking for evasion
and contradiction by asking more questions, by repeating the
questions, by asking others the same questions, and by check-
ing answers against other information that might be available
with in-car computers. As Professor LaFave has explained in
his treatise, the controversy is over
      multi-question extended inquiries of vehicle oc-
      cupants into the most minute details regarding
      the parts of the journey completed and lying
      ahead. The officers are “trained to subtly ask
      questions about * * * their destination, their itin-
      erary, the purpose of their visit, the names and
      addresses of whomever they are going to see,
      etc.,” “to make this conversation appear as nat-
      ural and routine a part of the collection of infor-
      mation incident to a citation or warning,” and
      “to interrogate the passengers separately, so
      their stories can be compared.” The objective is
      not to gain some insight into the traffic infrac-
      tion providing the legal basis for the stop, but to
      uncover inconsistent, evasive or false assertions
      that can contribute to reasonable suspicion or
      probable cause regarding drugs.
38                                                             No. 20-2105

4 LaFave, Search & Seizure § 9.3(d) (footnotes omitted), quot-
ing Gross & Barnes, 101 Mich. L. Rev. at 685. 5
    Cases after Rodriguez from around the country illustrate
the wide, almost kaleidoscopic variations in the ways these
questions can arise and play out. Several circuits have taken
the route the majority does here, which I believe is contrary to
Rodriguez, writing that questions about a driver’s travel plans
are ordinarily within the scope of a traffic stop, and that an
officer may prolong a stop to ask follow-up questions to con-
firm or check those answers. United States v. Braddy, 11 F.4th
1298, 1311 (11th Cir. 2021) (following pre-Rodriguez case law
on itinerary questions, at least where driver’s license had in-
correct address and ownership of vehicle was not clear);
United States v. Dion, 859 F.3d 114, 125–26 & n.7 (1st Cir. 2017)
(defendant conceded that pre-Rodriguez case law allowed itin-
erary questions); United States v. Collazo, 818 F.3d 247, 258 (6th
Cir. 2016) (allowing questions to follow up on conflicting an-
swers from driver and passenger). But see United States v.
Callison, 2 F.4th 1128, 1131–32 & n.2 (8th Cir. 2021) (holding
that itinerary questions were permissible because the officer,
as a matter of fact, was still “handl[ing] the matter for which
the stop was made,” but declining to reach the question of
“the extent to which officers may ask travel-related questions


     5 The majority asserts that this stop was not a “fishing expedition,” see

ante at 18, and implies that it was Cole’s answers to the travel plan ques-
tions that led the trooper to suspect that he was transporting drugs. Ante
at 2. The record contradicts both the assertion and the implication. The
trooper was always acting on Deputy Suttles’ hunch that Cole was trans-
porting drugs. He was looking for a way to justify a longer stop that would
lead to a search. And as the trooper later testified, he simply was not going
to let Cole go, no matter what, until a dog could sniff the car for drugs.
No. 20-2105                                                   39

during a routine traffic stop after Rodriguez.”) (alteration in
original), quoting Rodriguez, 575 U.S. at 350.
    The majority’s summary of other courts’ decisions, how-
ever, glosses over substantial variety among the approaches.
Other courts have wisely taken more nuanced and fact-spe-
cific approaches to the problem, recognizing that not all traffic
stops justify prolonged and close interrogation about travel
plans. See, e.g., United States v. Gomez-Arzate, 981 F.3d 832,
836, 840–44 (10th Cir. 2020) (finding that a few minutes of itin-
erary questioning that prolonged an already completed stop
violated Constitution, but noting extended inquiry into car
ownership may be permissible where driver is not listed on
registration and cannot say who owns vehicle); United States
v. Garner, 961 F.3d 264, 271–72 (3d Cir. 2020) (some itinerary
questions were permissible; some follow-up on employment,
family, criminal history, and unrelated conduct was not, but
officer’s reasonable suspicion of criminal activity permitted
the additional questioning); Jimenez, 420 P.3d at 469, 475–77,
308 Kan. at 318, 328–30 (affirming suppression where itiner-
ary questions prolonged stop for following too closely, and
noting that courts must guard against “mission creep” in pre-
textual traffic stops); see also Cortez, 965 F.3d at 839–40 (some
itinerary questions were permissible, but later follow-up
questioning fell outside bounds permitted by original reason
for stop).
    Disagreeing with the majority’s rule in this case, Professor
LaFave’s treatise has this to say about travel-plan questioning
as it is actually carried out by officers who are looking for
drugs:
       The objective is not to gain some insight into the
       traffic infraction providing the legal basis for
40                                                   No. 20-2105

       the stop, but to uncover inconsistent, evasive or
       false assertions that can contribute to reasonable
       suspicion or probable cause regarding drugs.
       Thus, “[n]ot only are questions about travel
       plans investigatory rather than merely conver-
       sational, the ordinary traveler cannot reasona-
       bly be expected to decline to answer such ques-
       tions, particularly if they are posed while an of-
       ficer is holding the driver’s license and other es-
       sential documents.”
4 LaFave, Search & Seizure § 9.3(d) (alteration in original)
(footnote and citation omitted).
    In this case, the trooper’s questions did nothing to advance
the limited road- and driver-safety missions that he was le-
gally authorized to pursue. Cole’s claim to be a California-
based traveling personal chef employed part-time in Mary-
land had nothing to do with whether he was safe to continue
driving. And Trooper Chapman knew that Cole was author-
ized to drive the Volkswagen when he saw that his name
matched the registration mere seconds into the initial ten-mi-
nute stop at the roadside.
    It should not matter here whether, at some later point,
Cole’s answers became suspicious. The critical point under
Rodriguez is that it was unconstitutional to prolong the stop,
the restraint on liberty, to ask those questions to begin with.
United States v. Lopez, 907 F.3d 472, 486–87 (7th Cir. 2018) (sup-
pressing evidence gathered following questioning that pro-
longed seizure); see also Garner, 961 F.3d at 270–71 (looking
for “Rodriguez moment” when officer began pursuing off-mis-
sion tasks); United States v. Childs, 277 F.3d 947, 952 (7th Cir.
2002) (en banc) (“Questioning that prolongs the detention, yet
No. 20-2105                                                   41

cannot be justified by the purpose of such an investigatory
stop, is unreasonable under the fourth amendment.”), citing
United States v. Sharpe, 470 U.S. 675, 685 (1985).
   When asked to explain his actions, Trooper Chapman ad-
mitted that he delayed collecting the last of the authorized in-
formation (for investigating the tailgating and Cole’s driving)
because he “was trying to piece together Mr. Cole’s story,
which was—as we all heard, was kind of inconsistent.
Changed each time.” Tr. 35.
    With respect, that is not how this is supposed to work. Un-
der the Constitution, people do not need “stories” to travel on
interstate highways—even if they have a broken taillight,
don’t signal a lane change, or briefly tailgate another vehicle.
Unless an officer efficiently processing the legitimate purpose
of the stop sees, hears, or smells something new that gives him
reasonable suspicion of other criminal activity, he needs to let
the driver go with a ticket or warning when the legitimate
tasks are done. This rule applies even if the officer still has a
hunch the driver is up to no good.
    We have explained that during a Terry stop, one of three
things must happen:
       (1) the police gather enough information to de-
       velop probable cause and allow for continued
       detention; (2) the suspicions of the police are
       dispelled and they release the suspect; or (3) the
       suspicions of the police are not dispelled, yet the
       officers have not developed probable cause but
       must release the suspect because the length of
       the stop is about to become unreasonable.
42                                                  No. 20-2105

United States v. Leo, 792 F.3d 742, 751 (7th Cir. 2015) (internal
citations omitted). An officer who reasonably believes a
driver is suspicious based on some ambiguous or conflicting
statements may not detain the suspect indefinitely, lest the
stop turn into “a de facto arrest that must be based on proba-
ble cause.” See id., quoting United States v. Bullock, 632 F.3d
1004, 1015 (7th Cir. 2011).
IV. Other Problems with the Majority Holding
    The majority here adopts a different rule, at least “ordinar-
ily.” Ante at 12 (“[W]e hold that travel-plan questions ordi-
narily fall within the mission of a traffic stop.”). The majority
does not hint at what might not be ordinary. It offers instead
what is supposed to be a reassuring limit: “This does not
mean, however, that officers have a free pass to ask travel-
plan questions until they are subjectively satisfied with the
answers. [Such questions] must remain reasonable, and rea-
sonableness is an objective standard based on all the circum-
stances.” Ante at 13. If the officer’s questions “go too far and
become unreasonable,” the stop may no longer be permissi-
ble. Ante at 16.
    Despite that assurance, the majority’s approach invites un-
reasonable restraints on liberty. The majority adds that an of-
ficer asking travel-plan questions may ask “reasonable fol-
low-up questions,” especially if the answers are “evasive, in-
consistent, or improbable.” Ante at 16. That’s the critical door
that enables further abuse of pretextual traffic stops, prolong-
ing those stops as the officer uses the coercive power of the
state and the authority to use force to subject drivers and their
passengers to close questioning in search of other criminal ac-
tivity. That is exactly what Rodriguez rejected. 575 U.S. at 355–
56. All the other questions that Rodriguez treats as part of the
No. 20-2105                                                   43

mission of every stop should quickly produce a clear answer
rather than inviting discretionary interrogation. A driver’s li-
cense can be valid or not, but it is unlikely to call for follow-
up questions.
    In Rodriguez, the Supreme Court pointedly declined to cat-
egorically permit questioning about travel plans as central—
even “ordinarily” central—to traffic stops’ missions. The of-
ficer in Rodriguez had asked the driver and passenger about
their itinerary, 575 U.S. at 351, but the Court left travel plans
out of the topics typically permissible because they help en-
sure that vehicles are “operated safely and responsibly,” id. at
355. The majority responds to this omission by noting that ju-
dicial opinions are not statutes and that the travel-plan ques-
tions were not directly at issue in Rodriguez, so we should in-
fer nothing from the omission of travel-plan questions from
the Rodriguez list. Ante at 11.
    That is an unduly narrow understanding of the opinion.
The Court knew it was providing important and practical
guidance for police officers and motorists all over the nation,
especially with that key passage about what is “typically”
within the scope of a traffic stop. No one suggests that the list
is universal and complete for all cases. As noted above, for
some traffic stops travel plans will be relevant. But those cases
should be evaluated based on their specific facts, not using a
general rule that allows such persistent, repetitive, and close
questioning in a stop legally justified as merely a routine traf-
fic stop. At a minimum, courts should expect an officer who
engages in such questioning to be able to explain how, specif-
ically, the questioning was based on the legal justification for
the stop. As Professor LaFave has explained:
44                                                  No. 20-2105

       [G]iven the Supreme Court’s Rodriguez decision,
       … the contention ”that unrestrained travel plan
       questioning is routine and always within a traffic
       stop’s mission” must be rejected out of hand, and …
       instead courts must inquire whether, on the
       facts of the particular case, such questioning is
       within the traffic stop’s mission.
4 LaFave, Search & Seizure § 9.3(d) (emphasis added) (foot-
note and citation omitted).
    The extraordinary nature of this en banc rehearing also
should not be passed by in silence. After the panel issued its
decision, the government chose not to seek en banc review. It
also informed this court that it did not oppose Cole’s motion
for immediate release from prison. No litigant is better able to
protect its interests in the federal courts than the federal gov-
ernment. This court chose, however, to act sua sponte to re-
hear the case en banc. That is an extraordinary step that this
court has taken very rarely.
    The majority suggests that en banc review was needed to
resolve an apparent conflict between the panel decision here
and another post-Rodriguez decision, United States v. Lewis,
920 F.3d 483 (7th Cir. 2019). The supposed conflict was illu-
sory. Lewis did not hold that an officer may prolong a stop
indefinitely to ask increasingly invasive and repetitive ques-
tions about a driver’s travels and employer—nor could it
have, given Rodriguez. As Lewis explained, the most important
reason it had for affirming denial of the motion to suppress
there was that the defendant had simply failed as a matter of
fact to show that the questioning had actually prolonged the
stop. Id. at 492. Careful analysis of Lewis shows that the case
is distinguishable on that fact, which is decisive under
No. 20-2105                                                   45

Rodriguez. See United States v. Cole, 994 F.3d 844, 855–57 (7th
Cir. 2021) (panel decision here).
V. Moving Forward
    Having explained why I view the majority’s general pre-
sumption in favor of allowing questions about travel plans in
pretextual traffic stops as unwise and contrary to Rodriguez, it
is still necessary to look toward future cases.
    District courts should be alert for unconstitutional “mis-
sion creep” where the stop is justified constitutionally by one
limited purpose but is actually motivated by a different pur-
pose. See Jimenez, 420 P.3d at 476, 308 Kan. at 329–30. In such
cases, district courts must make the joint legal and factual de-
termination of how long was reasonably necessary to execute
the stop’s permissible mission, and must then decide whether
the stop’s duration exceeded that limit or the officer otherwise
unreasonably prolonged the stop. Extensive itinerary ques-
tions posed to a motorist stopped for a broken taillight or tail-
gating, for example, should not pass muster.
    Courts deciding motions to suppress often give officers
substantial leeway in evaluating their actions and credibility.
An obviously pretextual stop, however, calls for more skepti-
cism. We should expect officers to behave in ways that serve
their real purpose, without necessarily working from the pre-
textual basis for the stop. When officers do so, district courts
should make the appropriate factual findings, and our review
of their fact-finding should be deferential. E.g., United States
v. Simon, 937 F.3d 820, 832–33 (7th Cir. 2019) (deferring to dis-
trict court’s credibility determinations as to whether the offic-
ers prolonged a stop); Lewis, 920 F.3d at 492 (similar); see also
United States v. Rodriguez-Escalera, 884 F.3d 661, 672 (7th Cir.
46                                               No. 20-2105

2018) (affirming grant of motion to suppress based on factual
findings, including those on credibility).
   We should reverse this judgment, suppress the evidence
obtained by improperly prolonging this traffic stop, and re-
mand to allow Cole to withdraw his guilty plea.

```

---
