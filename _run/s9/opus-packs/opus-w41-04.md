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

## GROUP: content/cases/United States v. Ross.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Ross"
type: case
citation: "456 U.S. 798 (1982)"
parallel_cite: "102 S. Ct. 2157; 72 L. Ed. 2d 572; 50 U.S.L.W. 4580"
neutral_cite: 1982 U.S. LEXIS 18
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1982
date_decided: 1982-06-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1982-06-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ross
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110719/united-states-v-ross/"
  cluster_id: 110719
  opinion_id: 110719
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Anchor"
  - page: "[[Searching Effects and Containers]]"
    role: "Key — Container bridge"
related: ["[[Carroll v. United States]]", "[[California v. Acevedo]]", "[[California v. Carney]]", "[[United States v. Morley]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "containers", "probable-cause", "vehicle-search"]
holding: "When PC justifies the search of a lawfully stopped vehicle, it justifies a search of every part of the vehicle and every container…"
lake:
  record_id: United States v. Ross
  status: verified
  projected_at: 2026-07-09
---

# United States v. Ross

*456 U.S. 798 (1982)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a tip from a reliable informant that Ross was selling narcotics kept in the trunk of his car, detectives stopped the car with probable cause to believe it contained contraband. They searched the trunk and opened a closed brown paper bag, finding heroin; in a later search they opened a zippered leather pouch and found cash. Ross moved to suppress the contents of the containers, arguing that opening closed containers required a warrant.

## Issue
Whether, when officers have probable cause to search a lawfully stopped vehicle, the automobile exception permits a warrantless search of closed containers found inside that may conceal the object of the search.

## Rule
Yes. The scope of a warrantless automobile search is as broad as a magistrate could have authorized by warrant. "We hold that the scope of the warrantless search authorized by that exception is no broader and no narrower than a magistrate could legitimately authorize by warrant. If probable cause justifies the search of a lawfully stopped vehicle, it justifies the search of every part of the vehicle and its contents that may conceal the object of the search." — 456 U.S. at 825. ^pin-825

Scope is fixed by the object sought, not by the kind of container: "The scope of a warrantless search of an automobile thus is not defined by the nature of the container in which the contraband is secreted. Rather, it is defined by the object of the search and the places in which there is probable cause to believe that it may be found." — [*Id.* at 824](https://www.courtlistener.com/opinion/110719/united-states-v-ross/#:~:text=The%20scope%20of%20a%20warrantless%20search%20of). ^pin-824

## Application
The detectives had probable cause to believe Ross's car contained narcotics. That probable cause reached anywhere in the vehicle the drugs might be hidden, including the closed brown paper bag and the leather pouch found in the trunk. Because a magistrate could have issued a warrant to search those containers for the drugs, the officers could open them without one; the warrantless opening of the containers was therefore lawful.

## Conclusion
The warrantless search of the containers found in the trunk was valid under the automobile exception; the Supreme Court reversed the [[Reading and Citing Cases#en-banc|en banc]] Court of Appeals and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ross* overruled *[[Robbins v. California]]* and supplies the foundational scope rule for vehicle searches. [[California v. Acevedo]] later unified the container doctrine — where police have probable cause to search a specific container placed in a car, they may search that container without a warrant — building on, not disturbing, *Ross*.

## Appears on
- [[Automobile Exception]] — *Key — Anchor*

## Sources
- *United States v. Ross*, 456 U.S. 798 (1982) — https://www.courtlistener.com/opinion/110719/united-states-v-ross/ — pinpoints: 824, 825 (parallel 102 S. Ct. 2157).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d8be20c803181f1f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "456 U.S. 798 (1982)", "court": "U.S. Supreme Court", "neutral_cite": "1982 U.S. LEXIS 18", "official_citation_present": true, "parallel_cite": "102 S. Ct. 2157; 72 L. Ed. 2d 572; 50 U.S.L.W. 4580", "title": "United States v. Ross", "year": "1982"}}
{"assertion_id": "90c6fb1adfbba309", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Anchor", "title": "United States v. Ross"}}
{"assertion_id": "cdf7a6e756915d36", "dimension": "support", "kind": "home_role", "locator": {"home": "Searching Effects and Containers"}, "payload": {"home": "Searching Effects and Containers", "role": "Key — Container bridge", "title": "United States v. Ross"}}
{"assertion_id": "f441fc67c1441c8c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "When PC justifies the search of a lawfully stopped vehicle, it justifies a search of every part of the vehicle and every container…", "title": "United States v. Ross"}}
{"assertion_id": "452fab2884b02e51", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Ross"}}
{"assertion_id": "d7ce1378ef8f5285", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1982-06-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Ross", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Ross", "varies_by_point": "false"}}
```

### lake record — United States v. Ross

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ross",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ross",
    "case_name_short": "Ross",
    "case_name_full": "United States v. Ross",
    "input_case_name": "United States v. Ross",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1982-06-01",
    "year": 1982,
    "docket": null,
    "cluster_id": 110719,
    "lead_opinion_id": 110719,
    "sibling_ids": [
      110719,
      9428782,
      9428783,
      9428784,
      9428785,
      9428786
    ],
    "absolute_url": "/opinion/110719/united-states-v-ross/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "456 U.S. 798",
      "volume": "456",
      "reporter": "U.S.",
      "page": "798",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "102 S. Ct. 2157",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2157",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 2d 572",
        "volume": "72",
        "reporter": "L. Ed. 2d",
        "page": "572",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 U.S.L.W. 4580",
        "volume": "50",
        "reporter": "U.S.L.W.",
        "page": "4580",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1982 U.S. LEXIS 18",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "456 U.S. 798",
        "volume": "456",
        "reporter": "U.S.",
        "page": "798",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 2157",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2157",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 2d 572",
        "volume": "72",
        "reporter": "L. Ed. 2d",
        "page": "572",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1982 U.S. LEXIS 18",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 U.S.L.W. 4580",
        "volume": "50",
        "reporter": "U.S.L.W.",
        "page": "4580",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "456 U.S. 798",
    "official_selection": {
      "court_class": "scotus",
      "selected": "456 U.S. 798",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-825",
      "page": null,
      "quote": "--- # United States v. Ross *456 U.S. 798 (1982)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a tip from a reliable informant that Ross was selling narcotics kept in the trunk of his car, detectives stopped the car with probable cause to believe it contained contraband. They searched the trunk and opened a closed brown paper bag, finding heroin; in a later search they opened a zippered leather pouch and found cash. Ross moved to suppress the contents of the containers, arguing that opening closed containers required a warrant. ## Issue Whether, when officers have probable cause to search a lawfully stopped vehicle, the automobile exception permits a warrantless search of closed containers found inside that may conceal the object of the search. ## Rule Yes. The scope of a warrantless automobile search is as broad as a magistrate could have authorized by warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-824",
      "page": null,
      "quote": "The scope of a warrantless search of an automobile thus is not defined by the nature of the container in which the contraband is secreted. Rather, it is defined by the object of the search and the places in which there is probable cause to believe that it may be found.",
      "star_marker": "824",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 50488,
      "fragment": "#:~:text=The%20scope%20of%20a%20warrantless%20search%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1982-06-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ross",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Guardado",
          "cluster_id": 9391153,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McCarthy",
          "cluster_id": 10160868,
          "cite": [
            "369 Or. 129",
            "501 P.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leon",
          "cluster_id": 111262,
          "cite": [
            "82 L. Ed. 2d 677",
            "104 S. Ct. 3405",
            "468 U.S. 897",
            "1984 U.S. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Long",
          "cluster_id": 111020,
          "cite": [
            "77 L. Ed. 2d 1201",
            "103 S. Ct. 3469",
            "463 U.S. 1032",
            "1983 U.S. LEXIS 7",
            "51 U.S.L.W. 5231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jacobsen",
          "cluster_id": 111143,
          "cite": [
            "80 L. Ed. 2d 85",
            "104 S. Ct. 1652",
            "466 U.S. 109",
            "1984 U.S. LEXIS 53",
            "52 U.S.L.W. 4414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New Jersey v. T. L. O.",
          "cluster_id": 111301,
          "cite": [
            "83 L. Ed. 2d 720",
            "105 S. Ct. 733",
            "469 U.S. 325",
            "1985 U.S. LEXIS 41",
            "53 U.S.L.W. 4083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Bradshaw",
          "cluster_id": 110987,
          "cite": [
            "77 L. Ed. 2d 405",
            "103 S. Ct. 2830",
            "462 U.S. 1039",
            "1983 U.S. LEXIS 82",
            "51 U.S.L.W. 4940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lafayette",
          "cluster_id": 110976,
          "cite": [
            "77 L. Ed. 2d 65",
            "103 S. Ct. 2605",
            "462 U.S. 640",
            "1983 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 2347917,
          "cite": [
            "256 S.W.3d 264",
            "2008 Tex. Crim. App. LEXIS 754",
            "2008 WL 2437667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ross:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110719 OR 9428782 OR 9428783 OR 9428784 OR 9428785 OR 9428786) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTcwMDYwODAwMDAwJnM9NDY2NjgwNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110719+OR+9428782+OR+9428783+OR+9428784+OR+9428785+OR+9428786%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110719 OR 9428782 OR 9428783 OR 9428784 OR 9428785 OR 9428786)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNjcmcz0xNDU4NTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110719+OR+9428782+OR+9428783+OR+9428784+OR+9428785+OR+9428786%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110719 OR 9428782 OR 9428783 OR 9428784 OR 9428785 OR 9428786)",
        "reviewed": 94,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 94,
        "triage_read": 1,
        "triage_snippet_classified": 93
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110719 OR 9428782 OR 9428783 OR 9428784 OR 9428785 OR 9428786)",
    "indexed_citing_opinions": 2496,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110719,
        "count": 2156,
        "count_source": "search"
      },
      {
        "opinion_id": 9428782,
        "count": 381,
        "count_source": "search"
      },
      {
        "opinion_id": 9428783,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428784,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428785,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428786,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3987,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ross.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNzEwNjgmcz0xMDU5Mzc0NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110719+OR+9428782+OR+9428783+OR+9428784+OR+9428785+OR+9428786%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9428783,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428783,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428783,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428784,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428784,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428784,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428784,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428784,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428784,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428785,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 94508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 100265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 312363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 315004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 324408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 326798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 351991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 358808,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 366539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 380373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 384730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 392944,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 1452588,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 1666834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 1693668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 1738098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 1842632,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 2121440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 8893666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 8898917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110719,
        "cited_id": 9428782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 100265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 312363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 315004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 324408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 326798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 351991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 358808,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 366539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 380373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 384730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 392944,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 1452588,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 1666834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 1693668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 1738098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 1842632,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 2121440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 8893666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428782,
        "cited_id": 8898917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 94508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 100568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428786,
        "cited_id": 392944,
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
    "date_created": "2026-07-06T02:35:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:35:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:35:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:38:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:35:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ross (truncated)

```
<div>
<center><b><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U.S. 798</a></span> (1982)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
ROSS</h1></center>
<center>No. 80-2209.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 1, 1982.</center>
<center>Decided June 1, 1982.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><span class="star-pagination">*799</span> <i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Lee, Assistant Attorney General Jensen, Joshua I. Schwartz,</i> and <i>John Fichter De Pue.</i></p>
<p><i>William J. Garber</i> argued the cause for respondent. With him on the brief was <i>Dennis M. Hart.</i><sup>[*]</sup></p>
<p><i>Raymond C. Clevenger III, John F. Cooney, Arthur B. Spitzer,</i> and <i>Charles S. Sims</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>In <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, the Court held that a warrantless search of an automobile stopped by police officers who had probable cause to believe the vehicle contained contraband was not unreasonable within the meaning of the Fourth Amendment. The Court in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> did not explicitly <span class="star-pagination">*800</span> address the scope of the search that is permissible. In this case, we consider the extent to which police officers  who have legitimately stopped an automobile and who have probable cause to believe that contraband is concealed somewhere within it  may conduct a probing search of compartments and containers within the vehicle whose contents are not in plain view. We hold that they may conduct a search of the vehicle that is as thorough as a magistrate could authorize in a warrant "particularly describing the place to be searched."<sup>[1]</sup></p>
<p></p>
<h2>I</h2>
<p>In the evening of November 27, 1978, an informant who had previously proved to be reliable telephoned Detective Marcum of the District of Columbia Police Department and told him that an individual known as "Bandit" was selling narcotics kept in the trunk of a car parked at 439 Ridge Street. The informant stated that he had just observed "Bandit" complete a sale and that "Bandit" had told him that additional narcotics were in the trunk. The informant gave Marcum a detailed description of "Bandit" and stated that the car was a "purplish maroon" Chevrolet Malibu with District of Columbia license plates.</p>
<p>Accompanied by Detective Cassidy and Sergeant Gonzales, Marcum immediately drove to the area and found a maroon Malibu parked in front of 439 Ridge Street. A license check disclosed that the car was registered to Albert Ross; a computer check on Ross revealed that he fit the informant's description and used the alias "Bandit." In two passes through the neighborhood the officers did not observe anyone matching the informant's description. To avoid alerting persons on the street, they left the area.</p>
<p><span class="star-pagination">*801</span> The officers returned five minutes later and observed the maroon Malibu turning off Ridge Street onto Fourth Street. They pulled alongside the Malibu, noticed that the driver matched the informant's description, and stopped the car. Marcum and Cassidy told the driver  later identified as Albert Ross, the respondent in this action  to get out of the vehicle. While they searched Ross, Sergeant Gonzales discovered a bullet on the car's front seat. He searched the interior of the car and found a pistol in the glove compartment. Ross then was arrested and handcuffed. Detective Cassidy took Ross' keys and opened the trunk, where he found a closed brown paper bag. He opened the bag and discovered a number of glassine bags containing a white powder. Cassidy replaced the bag, closed the trunk, and drove the car to headquarters.</p>
<p>At the police station Cassidy thoroughly searched the car. In addition to the "lunch-type" brown paper bag, Cassidy found in the trunk a zippered red leather pouch. He unzipped the pouch and discovered $3,200 in cash. The police laboratory later determined that the powder in the paper bag was heroin. No warrant was obtained.</p>
<p>Ross was charged with possession of heroin with intent to distribute, in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a). Prior to trial, he moved to suppress the heroin found in the paper bag and the currency found in the leather pouch. After an evidentiary hearing, the District Court denied the motion to suppress. The heroin and currency were introduced in evidence at trial and Ross was convicted.</p>
<p>A three-judge panel of the Court of Appeals reversed the conviction. It held that the police had probable cause to stop and search Ross' car and that, under <i>Carroll</i> v. <i>United States, supra</i><i>,</i> and <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span>, the officers lawfully could search the automobile  including its trunk  without a warrant. The court considered separately, however, the warrantless search of the two containers found in the trunk. On the basis of <i>Arkansas</i> v. <i>Sanders,</i> <span class="star-pagination">*802</span> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>, the court concluded that the constitutionality of a warrantless search of a container found in an automobile depends on whether the owner possesses a reasonable expectation of privacy in its contents. Applying that test, the court held that the warrantless search of the paper bag was valid but the search of the leather pouch was not. The court remanded for a new trial at which the items taken from the paper bag, but not those from the leather pouch, could be admitted.<sup>[2]</sup></p>
<p>The entire Court of Appeals then voted to rehear the case en banc. A majority of the court rejected the panel's conclusion that a distinction of constitutional significance existed between the two containers found in respondent's trunk; it held that the police should not have opened either container without first obtaining a warrant. The court reasoned:</p>
<blockquote>"No specific, well-delineated exception called to our attention permits the police to dispense with a warrant to open and search `unworthy' containers. Moreover, we believe that a rule under which the validity of a warrantless search would turn on judgments about the durability of a container would impose an unreasonable and unmanageable burden on police and courts. For these reasons, and because the Fourth Amendment protects all persons, not just those with the resources or fastidiousness to place their effects in containers that decision-makers would rank in the luggage line, we hold that the Fourth Amendment warrant requirement forbids the warrantless opening of a closed, opaque paper bag to the same extent that it forbids the warrantless opening of a small unlocked suitcase or a zippered leather pouch." 210 U. S. App. D. C. 342, 344, <span class="citation" data-id="9468224"><a href="/opinion/392944/united-states-v-albert-ross-jr/#1161" aria-description="Citation for case: United States v. Albert Ross, Jr.">655 F. 2d 1159, 1161</a></span> (1981) (footnote omitted).</blockquote>
<p><span class="star-pagination">*803</span> The en banc Court of Appeals considered, and rejected, the argument that it was reasonable for the police to open both the paper bag and the leather pouch because they were entitled to conduct a warrantless search of the entire vehicle in which the two containers were found. The majority concluded that this argument was foreclosed by <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>.</i></p>
<p>Three dissenting judges interpreted <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> differently.<sup>[3]</sup> Other courts also have read the <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> opinion in different ways.<sup>[4]</sup> Moreover, disagreement concerning the proper interpretation of <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> was at least partially responsible for the fact that <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">453 U. S. 420</a></span>, was decided last Term without a Court opinion.</p>
<p>There is, however, no dispute among judges about the importance of striving for clarification in this area of the law. For countless vehicles are stopped on highways and public <span class="star-pagination">*804</span> streets every day, and our cases demonstrate that it is not uncommon for police officers to have probable cause to believe that contraband may be found in a stopped vehicle. In every such case a conflict is presented between the individual's constitutionally protected interest in privacy and the public interest in effective law enforcement. No single rule of law can resolve every conflict, but our conviction that clarification is feasible led us to grant the Government's petition for certiorari in this case and to invite the parties to address the question whether the decision in <i><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">Robbins</a></span></i> should be reconsidered. <span class="citation multiple-matches"><a href="/c/U.%20S./454/891/">454 U. S. 891</a></span>.</p>
<p></p>
<h2>II</h2>
<p>We begin with a review of the decision in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> itself. In the fall of 1921, federal prohibition agents obtained evidence that George Carroll and John Kiro were "bootleggers" who frequently traveled between Grand Rapids and Detroit in an Oldsmobile Roadster.<sup>[5]</sup> On December 15, 1921, the agents unexpectedly encountered Carroll and Kiro driving west on that route in that car. The officers gave pursuit, stopped the roadster on the highway, and directed Carroll and Kiro to get out of the car.</p>
<p>No contraband was visible in the front seat of the Oldsmobile and the rear portion of the roadster was closed. One of the agents raised the rumble seat but found no liquor. He raised the seat cushion and again found nothing. The officer then struck at the "lazyback" of the seat and noticed that it was "harder than upholstery ordinarily is in those backs." <span class="star-pagination">*805</span> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#174" aria-description="Citation for case: Carroll v. United States">267 U. S., at 174</a></span>. He tore open the seat cushion and discovered 68 bottles of gin and whiskey concealed inside. No warrant had been obtained for the search.</p>
<p>Carroll and Kiro were convicted of transporting intoxicating liquor in violation of the National Prohibition Act. On review of those convictions, this Court ruled that the warrantless search of the roadster was reasonable within the meaning of the Fourth Amendment. In an extensive opinion written by Chief Justice Taft, the Court held:</p>
<blockquote>"On reason and authority the true rule is that if the search and seizure without a warrant are made upon probable cause, that is, upon a belief, reasonably arising out of circumstances known to the seizing officer, that an automobile or other vehicle contains that which by law is subject to seizure and destruction, the search and seizure are valid. The Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted, and in a manner which will conserve public interests as well as the interests and rights of individual citizens." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 149</a></span>.</blockquote>
<p>The Court explained at length the basis for this rule. The Court noted that historically warrantless searches of vessels, wagons, and carriages  as opposed to fixed premises such as a home or other building  had been considered reasonable by Congress. After reviewing legislation enacted by Congress between 1789 and 1799,<sup>[6]</sup> the Court stated:</p>
<blockquote>"Thus contemporaneously with the adoption of the Fourth Amendment we find in the first Congress, and in the following Second and Fourth Congresses, a difference made as to the necessity for a search warrant between <span class="star-pagination">*806</span> goods subject to forfeiture, when concealed in a dwelling house or similar place, and like goods in course of transportation and concealed in a movable vessel where they readily could be put out of reach of a search warrant." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#151" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 151</a></span>.</blockquote>
<p>The Court reviewed additional legislation passed by Congress<sup>[7]</sup> and again noted that</p>
<blockquote>"the guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 153</a></span>.</blockquote>
<p>Thus, since its earliest days Congress had recognized the impracticability of securing a warrant in cases involving the transportation of contraband goods.<sup>[8]</sup> It is this impracticability, viewed in historical perspective, that provided the basis for the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> decision. Given the nature of an automobile in transit, the Court recognized that an immediate intrusion is necessary if police officers are to secure the illicit <span class="star-pagination">*807</span> substance. In this class of cases, the Court held that a warrantless search of an automobile is not unreasonable.<sup>[9]</sup></p>
<p>In defining the nature of this "exception" to the general rule that "[i]n cases where the securing of a warrant is reasonably practicable, it must be used," <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States"><i>id.,</i> at 156</a></span>, the Court in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> emphasized the importance of the requirement that <span class="star-pagination">*808</span> officers have probable cause to believe that the vehicle contains contraband.</p>
<blockquote>"Having thus established that contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant, we come now to consider under what circumstances such search may be made. It would be intolerable and unreasonable if a prohibition agent were authorized to stop every automobile on the chance of finding liquor and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in. But those lawfully within the country, entitled to use the public highways, have a right to free passage without interruption or search unless there is known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 153-154</a></span>.</blockquote>
<p>Moreover, the probable-cause determination must be based on objective facts that could justify the issuance of a warrant by a magistrate and not merely on the subjective good faith of the police officers. " `[A]s we have seen, good faith is not enough to constitute probable cause. That faith must be grounded on facts within knowledge of the [officer], which in the judgment of the court would make his faith reasonable.' " <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Id.,</a></span></i> at 161-162 (quoting <i>Director General of Railroads</i> v. <i>Kastenbaum,</i> <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/#28" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">263 U. S. 25, 28</a></span>).<sup>[10]</sup></p>
<p><span class="star-pagination">*809</span> In short, the exception to the warrant requirement established in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i>  the scope of which we consider in this case  applies only to searches of vehicles that are supported by probable cause.<sup>[11]</sup> In this class of cases, a search is not unreasonable if based on facts that would justify the issuance of a warrant, even though a warrant has not actually been obtained.<sup>[12]</sup></p>
<p></p>
<h2>III</h2>
<p>The rationale justifying a warrantless search of an automobile that is believed to be transporting contraband arguably applies with equal force to any movable container that is believed to be carrying an illicit substance. That argument, <span class="star-pagination">*810</span> however, was squarely rejected in <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span>.</p>
<p><i>Chadwick</i> involved the warrantless search of a 200-pound footlocker secured with two padlocks. Federal railroad officials in San Diego became suspicious when they noticed that a brown footlocker loaded onto a train bound for Boston was unusually heavy and leaking talcum powder, a substance often used to mask the odor of marihuana. Narcotics agents met the train in Boston and a trained police dog signaled the presence of a controlled substance inside the footlocker. The agents did not seize the footlocker, however, at this time; they waited until respondent Chadwick arrived and the footlocker was placed in the trunk of Chadwick's automobile. Before the engine was started, the officers arrested Chadwick and his two companions. The agents then removed the footlocker to a secured place, opened it without a warrant, and discovered a large quantity of marihuana.</p>
<p>In a subsequent criminal proceeding, Chadwick claimed that the warrantless search of the footlocker violated the Fourth Amendment. In the District Court, the Government argued that as soon as the footlocker was placed in the automobile a warrantless search was permissible under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i> The District Court rejected that argument,<sup>[13]</sup> and the Government did not pursue it on appeal.<sup>[14]</sup> Rather, the Government contended in this Court that the warrant requirement of the Fourth Amendment applied only to searches of homes and <span class="star-pagination">*811</span> other "core" areas of privacy. The Court unanimously rejected that contention.<sup>[15]</sup> Writing for the Court, THE CHIEF JUSTICE stated:</p>
<blockquote>"[I]f there is little evidence that the Framers intended the Warrant Clause to operate outside the home, there is no evidence at all that they intended to exclude from protection of the Clause all searches occurring outside the home. The absence of a contemporary outcry against warrantless searches in public places was because, aside from searches incident to arrest, such warrantless searches were not a large issue in colonial America. Thus, silence in the historical record tells us little about the Framers' attitude toward application of the Warrant Clause to the search of respondents' footlocker. What we do know is that the Framers were men who focused on the wrongs of that day but who intended the Fourth Amendment to safeguard fundamental values which would far outlast the specific abuses which gave it birth." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#8" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 8-9</a></span> (footnote omitted).</blockquote>
<p>The Court in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> specifically rejected the argument that the warrantless search was "reasonable" because a footlocker has some of the mobile characteristics that support warrantless searches of automobiles. The Court recognized that "a person's expectations of privacy in personal luggage are substantially greater than in an automobile," <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><i>id.,</i> at 13</a></span>, and noted that the practical problems associated with the temporary detention of a piece of luggage during the period of time necessary to obtain a warrant are significantly less than those associated with the detention of an automobile. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 13, n. 7</a></span>. In ruling that the warrantless search of the <span class="star-pagination">*812</span> footlocker was unjustified, the Court reaffirmed the general principle that closed packages and containers may not be searched without a warrant. Cf. <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727</a></span>; <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span>. In sum, the Court in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> declined to extend the rationale of the "automobile exception" to permit a warrantless search of any movable container found in a public place.<sup>[16]</sup></p>
<p>The facts in <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>, were similar to those in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>.</i> In <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> a Little Rock police officer received information from a reliable informant that Sanders would arrive at the local airport on a specified flight that afternoon carrying a green suitcase containing marihuana. The officer went to the airport. Sanders arrived on schedule and retrieved a green suitcase from the airline baggage service. Sanders gave the suitcase to a waiting companion, who placed it in the trunk of a taxi. Sanders and his companion drove off in the cab; police officers followed and stopped the taxi several blocks from the airport. The officers opened the trunk, seized the suitcase, and searched it on the scene without a warrant. As predicted, the suitcase contained marihuana.</p>
<p>The Arkansas Supreme Court ruled that the warrantless search of the suitcase was impermissible under the Fourth Amendment, and this Court affirmed. As in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> the mere fact that the suitcase had been placed in the trunk of the vehicle did not render the automobile exception of <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> applicable; the police had probable cause to seize the suitcase before it was placed in the trunk of the cab and did not <span class="star-pagination">*813</span> have probable cause to search the taxi itself.<sup>[17]</sup> Since the suitcase had been placed in the trunk, no danger existed that its contents could have been secreted elsewhere in the vehicle.<sup>[18]</sup> As THE CHIEF JUSTICE noted in his opinion concurring in the judgment:</p>
<blockquote>"Because the police officers had probable cause to believe that respondent's green suitcase contained marihuana before it was placed in the trunk of the taxicab, their duty to obtain a search warrant before opening it is clear under <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). . . .</blockquote>
<blockquote>". . . Here, as in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> it was the <i>luggage</i> being transported by respondent at the time of the arrest, not the automobile in which it was being carried, that was the suspected locus of the contraband. The relationship between the automobile and the contraband was purely coincidental, as in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>.</i> The fact that the suitcase was resting in the trunk of the automobile at the time of respondent's arrest does not turn this into an `automobile' exception case. The Court need say no more." <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#766" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 766-767</a></span>.</blockquote>
<p>The Court in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> did not, however, rest its decision solely on the authority of <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>.</i> In rejecting the State's <span class="star-pagination">*814</span> argument that the warrantless search of the suitcase was justified on the ground that it had been taken from an automobile lawfully stopped on the street, the Court broadly suggested that a warrantless search of a container found in an automobile could never be sustained as part of a warrantless search of the automobile itself.<sup>[19]</sup> The Court did not suggest that it mattered whether probable cause existed to search the entire vehicle. It is clear, however, that in neither <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> nor <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> did the police have probable cause to search the vehicle or anything within it except the footlocker in the former case and the green suitcase in the latter.</p>
<p><i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">453 U. S. 420</a></span>, however, was a case in which suspicion was not directed at a specific container. In that case the Court for the first time was forced to consider whether police officers who are entitled to conduct a warrantless search of an automobile stopped on a public roadway may open a container found within the vehicle. In the early morning of January 5, 1975, police officers stopped Robbins' station wagon because he was driving erratically. Robbins got out of the car, but later returned to obtain the vehicle's registration papers. When he opened the car door, the officers smelled marihuana smoke. One of the officers searched Robbins and discovered a vial of liquid; in a search of the interior of the car the officer found marihuana. The police officers then opened the tailgate of the station wagon and raised the cover of a recessed luggage compartment. In <span class="star-pagination">*815</span> the compartment they found two packages wrapped in green opaque plastic. The police unwrapped the packages and discovered a large amount of marihuana in each.</p>
<p>Robbins was charged with various drug offenses and moved to suppress the contents of the plastic packages. The California Court of Appeal held that "[s]earch of the automobile was proper when the officers learned that appellant was smoking marijuana when they stopped him"<sup>[20]</sup> and that the warrantless search of the packages was justified because "the contents of the packages could have been inferred from their outward appearance, so that appellant could not have held a reasonable expectation of privacy with respect to the contents." <i>People</i> v. <i>Robbins,</i> <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#40" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d 34, 40</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#783" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr. 780, 783</a></span> (1980).</p>
<p>This Court reversed. Writing for a plurality, Justice Stewart rejected the argument that the outward appearance of the packages precluded Robbins from having a reasonable expectation of privacy in their contents. He also squarely rejected the argument that there is a constitutional distinction between searches of luggage and searches of "less worthy" containers. Justice Stewart reasoned that all containers are equally protected by the Fourth Amendment unless their contents are in plain view. The plurality concluded that the warrantless search was impermissible because <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> had established that "a closed piece of luggage found in a lawfully searched car is constitutionally protected to the same extent as are closed pieces of luggage found anywhere else." <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#425" aria-description="Citation for case: Robbins v. California">453 U. S., at 425</a></span>.</p>
<p>In an opinion concurring in the judgment, JUSTICE POWELL, the author of the Court's opinion in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> stated that "[t]he plurality's approach strains the rationales of our prior cases and imposes substantial burdens on law enforcement without vindicating any significant values of privacy." 453 <span class="star-pagination">*816</span> U. S., at 429.<sup>[21]</sup> He noted that possibly "the controlling question should be the scope of the automobile exception to the warrant requirement," <i>id.,</i> at 435, and explained that under that view</p>
<blockquote>"when the police have probable cause to search an automobile, rather than only to search a particular container that fortuitously is located in it, the exigencies that allow the police to search the entire automobile without a warrant support the warrantless search of every container found therein. See <i>post,</i> at 451, and n. 13 (STEVENS, J., dissenting). This analysis is entirely consistent with the holdings in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> neither of which is an `automobile case,' because the police there had probable cause to search the double-locked footlocker and the suitcase respectively before either came near an automobile." <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Ibid.</a></span></i>
</blockquote>
<p>The parties in <i>Robbins</i> had not pressed that argument, however, <span class="star-pagination">*817</span> and JUSTICE POWELL concluded that institutional constraints made it inappropriate to reexamine basic doctrine without full adversary presentation. He concurred in the judgment, since it was supported  although not compelled  by the Court's opinion in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> and stated that a future case might present a better opportunity for thorough consideration of the basic principles in this troubled area.</p>
<p>That case has arrived. Unlike <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> in this case police officers had probable cause to search respondent's entire vehicle.<sup>[22]</sup> Unlike <i>Robbins,</i> in this case the parties have squarely addressed the question whether, in the course of a legitimate warrantless search of an automobile, police are entitled to open containers found within the vehicle. We now address that question. Its answer is determined by the scope of the search that is authorized by the exception to the warrant requirement set forth in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i></p>
<p></p>
<h2>IV</h2>
<p>In <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> itself, the whiskey that the prohibition agents seized was not in plain view. It was discovered only after an officer opened the rumble seat and tore open the upholstery of the lazyback. The Court did not find the scope of the search unreasonable. Having stopped Carroll and Kiro on a public road and subjected them to the indignity of a vehicle <span class="star-pagination">*818</span> search  which the Court found to be a reasonable intrusion on their privacy because it was based on probable cause that their vehicle was transporting contraband  prohibition agents were entitled to tear open a portion of the roadster itself. The scope of the search was no greater than a magistrate could have authorized by issuing a warrant based on the probable cause that justified the search. Since such a warrant could have authorized the agents to open the rear portion of the roadster and to rip the upholstery in their search for concealed whiskey, the search was constitutionally permissible.</p>
<p>In <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney</a></span></i> the police found weapons and stolen property "concealed in a compartment under the dashboard." <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#44" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 44</a></span>. No suggestion was made that the scope of the search was impermissible. It would be illogical to assume that the outcome of <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i>  or the outcome of <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> itself  would have been different if the police had found the secreted contraband enclosed within a secondary container and had opened that container without a warrant. If it was reasonable for prohibition agents to rip open the upholstery in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> it certainly would have been reasonable for them to look into a burlap sack stashed inside; if it was reasonable to open the concealed compartment in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> it would have been equally reasonable to open a paper bag crumpled within it. A contrary rule could produce absurd results inconsistent with the decision in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> itself.</p>
<p>In its application of <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> this Court in fact has sustained warrantless searches of containers found during a lawful search of an automobile. In <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span>, the Court upheld a warrantless seizure of whiskey found during a search of an automobile, some of which was discovered in "whiskey bags" that could have contained other goods.<sup>[23]</sup> In <i>Scher</i> v. <i>United States,</i> <span class="citation" data-id="103100"><a href="/opinion/103100/scher-v-united-states/" aria-description="Citation for case: Scher v. United States">305 U. S. 251</a></span>, federal officers <span class="star-pagination">*819</span> seized and searched packages of unstamped liquor found in the trunk of an automobile searched without a warrant. As described by a police officer who participated in the search: "I turned the handle and opened the trunk and found the trunk completely filled with packages wrapped in brown paper, and tied with twine; I think somewhere around thirty packages, each one containing six bottles."<sup>[24]</sup> In these cases it was not contended that police officers needed a warrant to open the whiskey bags or to unwrap the brown paper packages. These decisions nevertheless "have much weight, as they show that this point neither occurred to the bar or the bench." <i>Bank of the </i><i>United States</i> v. <i>Deveaux,</i> <span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/#88" aria-description="Citation for case: Bank of the United States v. Deveaux">5 Cranch 61, 88</a></span> (Marshall, C. J.). The fact that no such argument was even made illuminates the profession's understanding of the scope of the search permitted under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i> Indeed, prior to the decisions in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> courts routinely had held that containers and packages found during a legitimate warrantless search of an automobile also could be searched without a warrant.<sup>[25]</sup></p>
<p><span class="star-pagination">*820</span> As we have stated, the decision in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> was based on the Court's appraisal of practical considerations viewed in the perspective of history. It is therefore significant that the practical consequences of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> decision would be largely nullified if the permissible scope of a warrantless search of an automobile did not include containers and packages found inside the vehicle. Contraband goods rarely are strewn across the trunk or floor of a car; since by their very nature such goods must be withheld from public view, they rarely can be placed in an automobile unless they are enclosed within some form of container.<sup>[26]</sup> The Court in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> held that "contraband goods <i>concealed</i> and illegally transported in an automobile or other vehicle may be searched for without a warrant." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span> (emphasis added). As we noted in <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#104" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 104</a></span>, the decision in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> "merely relaxed the requirements for a warrant on grounds of practicability." It neither broadened nor limited the scope of a lawful search based on probable cause.</p>
<p>A lawful search of fixed premises generally extends to the entire area in which the object of the search may be found and is not limited by the possibility that separate acts of entry <span class="star-pagination">*821</span> or opening may be required to complete the search.<sup>[27]</sup> Thus, a warrant that authorizes an officer to search a home for illegal weapons also provides authority to open closets, chests, drawers, and containers in which the weapon might be found. A warrant to open a footlocker to search for marihuana would also authorize the opening of packages found inside. A warrant to search a vehicle would support a search of every part of the vehicle that might contain the object of the search. When a legitimate search is under way, and when its purpose and its limits have been precisely defined, nice distinctions between closets, drawers, and containers, in the case of a home, or between glove compartments, upholstered seats, trunks, and wrapped packages, in the case of a vehicle, must give way to the interest in the prompt and efficient completion of the task at hand.<sup>[28]</sup></p>
<p><span class="star-pagination">*822</span> This rule applies equally to all containers, as indeed we believe it must. One point on which the Court was in virtually unanimous agreement in <i>Robbins</i> was that a constitutional distinction between "worthy" and "unworthy" containers would be improper.<sup>[29]</sup> Even though such a distinction perhaps could evolve in a series of cases in which paper bags, locked trunks, lunch buckets, and orange crates were placed on one side of the line or the other,<sup>[30]</sup> the central purpose of the Fourth Amendment forecloses such a distinction. For just as the most frail cottage in the kingdom is absolutely entitled to the same guarantees of privacy as the most majestic mansion,<sup>[31]</sup> so also may a traveler who carries a toothbrush and a few articles of clothing in a paper bag or knotted scarf claim an equal right to conceal his possessions from official inspection as the sophisticated executive with the locked attache case.</p>
<p>As Justice Stewart stated in <i>Robbins,</i> the Fourth Amendment provides protection to the owner of every container <span class="star-pagination">*823</span> that conceals its contents from plain view. <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#427" aria-description="Citation for case: Robbins v. California">453 U. S., at 427</a></span> (plurality opinion). But the protection afforded by the Amendment varies in different settings. The luggage carried by a traveler entering the country may be searched at random by a customs officer; the luggage may be searched no matter how great the traveler's desire to conceal the contents may be. A container carried at the time of arrest often may be searched without a warrant and even without any specific suspicion concerning its contents. A container that may conceal the object of a search authorized by a warrant may be opened immediately; the individual's interest in privacy must give way to the magistrate's official determination of probable cause.</p>
<p>In the same manner, an individual's expectation of privacy in a vehicle and its contents may not survive if probable cause is given to believe that the vehicle is transporting contraband. Certainly the privacy interests in a car's trunk or glove compartment may be no less than those in a movable container. An individual undoubtedly has a significant interest that the upholstery of his automobile will not be ripped or a hidden compartment within it opened. These interests must yield to the authority of a search, however, which  in light of <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i>  does not itself require the prior approval of a magistrate. The scope of a warrantless search based on probable cause is no narrower  and no broader  than the scope of a search authorized by a warrant supported by probable cause. Only the prior approval of the magistrate is waived; the search otherwise is as the magistrate could authorize.<sup>[32]</sup></p>
<p><span class="star-pagination">*824</span> The scope of a warrantless search of an automobile thus is not defined by the nature of the container in which the contraband is secreted. Rather, it is defined by the object of the search and the places in which there is probable cause to believe that it may be found. Just as probable cause to believe that a stolen lawnmower may be found in a garage will not support a warrant to search an upstairs bedroom, probable cause to believe that undocumented aliens are being transported in a van will not justify a warrantless search of a suitcase. Probable cause to believe that a container placed in the trunk of a taxi contains contraband or evidence does not justify a search of the entire cab.</p>
<p></p>
<h2>V</h2>
<p>Our decision today is inconsistent with the disposition in <i>Robbins</i> v. <i><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">California</a></span></i> and with the portion of the opinion in <i>Arkansas</i> v. <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> on which the plurality in <i>Robbins</i> relied. Nevertheless, the doctrine of <i>stare decisis</i> does not preclude this action. Although we have rejected some of the reasoning in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> we adhere to our holding in that case; although we reject the precise holding in <i>Robbins,</i> there was no Court opinion supporting a single rationale for its judgment, and the reasoning we adopt today was not presented by the parties in that case. Moreover, it is clear that no legitimate reliance interest can be frustrated by our decision today.<sup>[33]</sup> Of greatest importance, we are convinced that the rule we apply in this case is faithful to the interpretation of the Fourth Amendment that the Court has followed with substantial consistency throughout our history.</p>
<p>We reaffirm the basic rule of Fourth Amendment jurisprudence stated by Justice Stewart for a unanimous Court in <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span>, 390:</p>
<blockquote>
<span class="star-pagination">*825A</span> "The Fourth Amendment proscribes all unreasonable searches and seizures, and it is a cardinal principle that `searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendment  subject only to a few specifically established and well-delineated exceptions.' <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (footnotes omitted)."</blockquote>
<p>The exception recognized in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> is unquestionably one that is "specifically established and well delineated." We hold that the scope of the warrantless search authorized by that exception is no broader and no narrower than a magistrate could legitimately authorize by warrant. If probable cause justifies the search of a lawfully stopped vehicle, it justifies the search of every part of the vehicle and its contents that may conceal the object of the search.</p>
<p>The judgment of the Court of Appeals is reversed. The case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p><span class="star-pagination">*825B</span> JUSTICE BLACKMUN, concurring.</p>
<p>My dissents in prior cases have indicated my continuing dissatisfaction and discomfort with the Court's vacillation in what is rightly described as "this troubled area." <i>Ante,</i> at 817. See <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#17" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 17</a></span> (1977); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#768" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 768</a></span> (1979); <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#436" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 436</a></span> (1981).</p>
<p>I adhere to the views expressed in those dissents. It is important, however, not only for the Court as an institution, but also for law enforcement officials and defendants, that the applicable legal rules be clearly established. JUSTICE STEVENS' opinion for the Court now accomplishes much in this respect, and it should clarify a good bit of the confusion that has existed. In order to have an authoritative ruling, I join the Court's opinion and judgment.</p>
<p><span class="star-pagination">*826</span> JUSTICE POWELL, concurring.</p>
<p>In my opinion in <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#429" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 429</a></span> (1981), concurring in the judgment, I stated that the judgment was justified, though not compelled, by the Court's opinion in <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979). I did not agree, however, with the "bright line" rule articulated by the plurality opinion. Rather, I repeated the view I long have held that one's "reasonable expectation of privacy" is a particularly relevant factor in determining the validity of a warrantless search. I have recognized that, with respect to automobiles in general, this expectation can be only a limited one. See <i>Arkansas</i> v. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#761" aria-description="Citation for case: Arkansas v. Sanders"><i>Sanders, supra,</i> at 761</a></span>; <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279</a></span> (1973) (POWELL, J., concurring). I continue to think that in many situations one's reasonable expectation of privacy may be a decisive factor in a search case.</p>
<p>It became evident last Term, however, from the five opinions written in <i>Robbins</i>  in none of which THE CHIEF JUSTICE joined  that it is essential to have a Court opinion in <i>automobile</i> search cases that provides "specific guidance to police and courts in this recurring situation." <i>Robbins</i> v. <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#435" aria-description="Citation for case: Robbins v. California"><i>California, supra,</i> at 435</a></span> (POWELL, J., concurring in judgment). The Court's opinion today, written by JUSTICE STEVENS and now joined by THE CHIEF JUSTICE and four other Justices, will afford this needed guidance. It is fair also to say that, given <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), and <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), the Court's decision does not depart substantially from Fourth Amendment doctrine in automobile cases. Moreover, in enunciating a readily understood and applied rule, today's decision is consistent with the similar step taken last Term in <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981).</p>
<p>I join the Court's opinion.</p>
<p>JUSTICE WHITE, dissenting.</p>
<p>I would not overrule <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">453 U. S. 420</a></span> (1981). For the reasons stated by Justice Stewart in that <span class="star-pagination">*827</span> case, I would affirm the judgment of the Court of Appeals. I also agree with much of JUSTICE MARSHALL's dissent in this case.</p>
<p>JUSTICE MARSHALL, with whom JUSTICE BRENNAN joins, dissenting.</p>
<p>The majority today not only repeals all realistic limits on warrantless automobile searches, it repeals the Fourth Amendment warrant requirement itself. By equating a police officer's estimation of probable cause with a magistrate's, the Court utterly disregards the value of a neutral and detached magistrate. For as we recently, and unanimously, reaffirmed:</p>
<blockquote>"The warrant traditionally has represented an independent assurance that a search and arrest will not proceed without probable cause to believe that a crime has been committed and that the person or place named in the warrant is involved in the crime. Thus, an issuing magistrate must meet two tests. He must be neutral and detached, and he must be capable of determining whether probable cause exists for the requested arrest or search. This Court long has insisted that inferences of probable cause be drawn by `a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.' " <i>Shadwick</i> v. <i>City of Tampa,</i> <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#350" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 350</a></span> (1972), quoting <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948).</blockquote>
<p>A police officer on the beat hardly satisfies these standards. In adopting today's new rule, the majority opinion shows contempt for these Fourth Amendment values, ignores this Court's precedents, is internally inconsistent, and produces anomalous and unjust consequences. I therefore dissent.</p>
<p></p>
<h2>I</h2>
<p>According to the majority, whenever police have probable cause to believe that contraband may be found within an <span class="star-pagination">*828</span> automobile that they have stopped on the highway,<sup>[1]</sup> they may search not only the automobile but also any container found inside it, without obtaining a warrant. The scope of the search, we are told, is as broad as a magistrate could authorize in a warrant to search the automobile. The majority makes little attempt to justify this rule in terms of recognized Fourth Amendment values. The Court simply ignores the critical function that a magistrate serves. And although the Court purports to rely on the mobility of an automobile and the impracticability of obtaining a warrant, it never explains why these concerns permit the warrantless search of a <i>container,</i> which can easily be seized and immobilized while police are obtaining a warrant.</p>
<p>The new rule adopted by the Court today is completely incompatible with established Fourth Amendment principles, and takes a first step toward an unprecedented "probable cause" exception to the warrant requirement. In my view, under accepted standards, the warrantless search of the containers in this case clearly violates the Fourth Amendment.</p>
<p></p>
<h2>A</h2>
<p>"[I]t is a cardinal principle that `searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendment  subject only to a few specifically established and well-delineated exceptions.' " <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978), quoting <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967). The warrant requirement is crucial to protecting Fourth Amendment rights because of the importance of having the probable-cause determination made in the first instance by a neutral and detached magistrate. Time and <span class="star-pagination">*829</span> again, we have emphasized that the warrant requirement provides a number of protections that a <i>post hoc</i> judicial evaluation of a policeman's probable cause does not.</p>
<p>The requirement of prior review by a detached and neutral magistrate limits the concentration of power held by executive officers over the individual, and prevents some overbroad or unjustified searches from occurring at all. See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972); <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#252" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 252</a></span> (1960) (BRENNAN, J., joined by Warren, C. J., and Black and Douglas, JJ., dissenting). Prior review may also "prevent hindsight from coloring the evaluation of the reasonableness of a search or seizure." <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#565" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 565</a></span> (1976); see also <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964). Furthermore, even if a magistrate would have authorized the search that the police conducted, the interposition of a magistrate's neutral judgment reassures the public that the orderly process of law has been respected:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States, supra,</i> at 13-14.</blockquote>
<p>See also <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 323</a></span> (1978); <i>United States</i> v. <i>United States District Court, supra,</i> at 321. The safeguards embodied in the warrant requirement apply as forcefully to automobile searches as to any others.</p>
<p>Our cases do recognize a narrow exception to the warrant requirement for certain automobile searches. Throughout our decisions, two major considerations have been advanced to justify the automobile exception to the warrant requirement. <span class="star-pagination">*830</span> We have upheld only those searches that are actually justified by those considerations.</p>
<p>First, these searches have been justified on the basis of the exigency of the mobility of the automobile. See, <i>e. g., </i><i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). This "mobility" rationale is something of a misnomer, cf. <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#442" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 442-443</a></span> (1973), since the police ordinarily can remove the car's occupants and secure the vehicle on the spot. However, the inherent mobility of the vehicle often creates situations in which the police's only alternative to an immediate search may be to release the automobile from their possession.<sup>[2]</sup> This alternative creates an unacceptably high risk of losing the contents of the vehicle, and is a principal basis for the Court's automobile exception to the warrant requirement. See <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, supra,</i> at 51, n. 9</a></span>.</p>
<p>In many cases, however, the police will, prior to searching the car, have cause to arrest the occupants and bring them to the station for booking. In this situation, the police can ordinarily seize the automobile and bring it to the station. Because the vehicle is now in the exclusive control of the authorities, any subsequent search cannot be justified by the mobility of the car. Rather, an immediate warrantless search of the vehicle is permitted because of the second major justification for the automobile exception: the diminished expectation of privacy in an automobile.</p>
<p>Because an automobile presents much of its contents in open view to police officers who legitimately stop it on a public way, is used for travel, and is subject to significant government <span class="star-pagination">*831</span> regulation, this Court has determined that the intrusion of a warrantless search of an automobile is constitutionally less significant than a warrantless search of more private areas. See <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#761" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 761</a></span> (1979) (collecting cases). This justification has been invoked for warrantless automobile searches in circumstances where the exigency of mobility was clearly not present. See, <i>e. g., </i><i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367-368</a></span> (1976); <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 441-442</a></span>. By focusing on the defendant's reasonable expectation of privacy, this Court has refused to require a warrant in situations where the process of obtaining such a warrant would be more intrusive than the actual search itself. Cf. <i>Katz</i> v. <i>United States, supra</i><i>.</i> A defendant may consider the seizure of the car a greater intrusion than an immediate search. See <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, supra,</i> at 51-52</a></span>. Therefore, even where police <i>can</i> bring both the defendant and the automobile to the station safely and can house the car while they seek a warrant, the police are permitted to decide whether instead to conduct an immediate search of the car. In effect, the warrantless search is permissible because a warrant requirement would not provide significant protection of the defendant's Fourth Amendment interests.</p>
<p></p>
<h2>B</h2>
<p>The majority's rule is flatly inconsistent with these established Fourth Amendment principles concerning the scope of the automobile exception and the importance of the warrant requirement. Historically, the automobile exception has been limited to those situations where its application is compelled by the justifications described above. Today, the majority makes no attempt to base its decision on these justifications. This failure is not surprising, since the traditional rationales for the automobile exception plainly do not support extending it to the search of a container found inside a vehicle.</p>
<p><span class="star-pagination">*832</span> The practical mobility problem  deciding what to do with both the car and the occupants if an immediate search is not conducted  is simply not present in the case of movable containers, which can easily be seized and brought to the magistrate. See <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#762" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 762-766</a></span>, and nn. 10, 14. The lesser-expectation-of-privacy rationale also has little force. A container, as opposed to the car itself, does not reflect diminished privacy interests. See <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#762" aria-description="Citation for case: Arkansas v. Sanders"><i>id.,</i> at 762, 764-765</a></span>. Moreover, the practical corollary that this Court has recognized  that depriving occupants of the use of a car may be a greater intrusion than an immediate search  is of doubtful relevance here, since the owner of a container will rarely suffer significant inconvenience by being deprived of its use while a warrant is being obtained.</p>
<p>Ultimately, the majority, unable to rely on the justifications underlying the automobile exception, simply creates a new "probable cause" exception to the warrant requirement for automobiles. We have soundly rejected attempts to create such an exception in the past, see <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), and we should do so again today.</p>
<p>In purported reliance on <i>Carroll</i> v. <i>United States, supra</i><i>,</i> the Court defines the permissible scope of a search by reference to the scope of a probable-cause search that a magistrate could authorize. Under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> however, the mobility of an automobile is what is critical to the legality of a warrantless search. Of course, <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> properly confined the search to the probable-cause limits that would also limit a magistrate, but it did not suggest that the search could be as <i>broad</i> as a magistrate could authorize upon a warrant. A magistrate could authorize a search encompassing containers, even though the mobility rationale does not justify such a broad search. Indeed, the Court's reasoning might have justified the search of the entire car in <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> despite the fact that the car was not "mobile" at all. Thus, in blithely suggesting that <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> "neither broadened nor limited the scope of a lawful search based on probable cause," <span class="star-pagination">*833</span> <i>ante,</i> at 820, the majority assumes what has never been the law: that the scope of the automobile-mobility exception to the warrant requirement is as broad as the scope of a "lawful" probable-cause search of an automobile, <i>i. e.,</i> one authorized by a magistrate.</p>
<p>The majority's sleight-of-hand ignores the obvious differences between the function served by a magistrate in making a determination of probable cause and the function of the automobile exception. It is irrelevant to a magistrate's function whether the items subject to search are mobile, may be in danger of destruction, or are impractical to store, or whether an immediate search would be less intrusive than a seizure without a warrant. A magistrate's only concern is whether there is probable cause to search them. Where suspicion has focused not on a particular item but only on a vehicle, home, or office, the magistrate might reasonably authorize a search of closed containers at the location as well. But an officer on the beat who searches an automobile without a warrant is not entitled to conduct a broader search than the exigency obviating the warrant justifies. After all, what justifies the warrantless search is not probable cause alone, but <i>probable cause coupled with the mobility of the automobile.</i> Because the scope of a <i>warrantless</i> search should depend on the scope of the justification for dispensing with a warrant, the entire premise of the majority's opinion fails to support its conclusion.</p>
<p>The majority's rule masks the startling assumption that a policeman's determination of probable cause is the functional equivalent of the determination of a neutral and detached magistrate. This assumption ignores a major premise of the warrant requirement  the importance of having a neutral and detached magistrate determine whether probable cause exists. See <i>supra,</i> at 828-829. The majority's explanation that the scope of the warrantless automobile search will be "limited" to what a magistrate could authorize is thus inconsistent with our cases, which firmly establish that an on-the-spot <span class="star-pagination">*834</span> determination of probable cause is <i>never</i> the same as a decision by a neutral and detached magistrate.</p>
<p></p>
<h2>C</h2>
<p>Our recent decisions in <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), <i>Arkansas</i> v. <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders, supra</a></span></i><i>,</i> and <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">453 U. S. 420</a></span> (1981), clearly affirm that movable containers are different from automobiles for Fourth Amendment purposes. In <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> the Court drew a constitutional distinction between luggage and automobiles in terms of substantial differences in expectations of privacy. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 12</a></span>. Moreover, the Court held that the mobility of such containers does not justify dispensing with a warrant, since federal agents had seized the luggage and safely transferred it to their custody under their exclusive control. <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> explicitly held that "the warrant requirement of the Fourth Amendment applies to personal luggage taken from an automobile to the same degree it applies to such luggage in other locations." <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#766" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 766</a></span>. And <i>Robbins</i> reaffirmed the <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> rationale as applied to wrapped packages found in the unlocked luggage compartment of a vehicle. 453 U. S., at 425.<sup>[3]</sup></p>
<p>In light of these considerations, I conclude that any movable container found within an automobile deserves precisely the same degree of Fourth Amendment warrant protection that it would deserve if found at a location outside the automobile. See <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#763" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 763-765</a></span>, and n. 13; <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#17" aria-description="Citation for case: United States v. Chadwick"><i>Chadwick, supra,</i> at 17, n. 1</a></span> (BRENNAN, J., concurring). <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> as the majority notes, "reaffirmed the general principle that closed packages and containers may not be <span class="star-pagination">*835</span> searched without a warrant." <i>Ante,</i> at 812. Although there is no need to describe the exact contours of that protection in this dissenting opinion, it is clear enough that closed, opaque containers  regardless of whether they are "worthy" or are always used to store personal items  are ordinarily fully protected. Cf. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders"><i>Sanders, supra,</i> at 764, n. 13</a></span>.<sup>[4]</sup></p>
<p>Here, because respondent Ross had placed the evidence in question in a closed paper bag, the container could be seized, but not searched, without a warrant. No practical exigencies required the warrantless searches on the street or at the station: Ross had been arrested and was in custody when both searches occurred, and the police succeeded in transporting the bag to the station without inadvertently spilling its contents.<sup>[5]</sup></p>
<p></p>
<h2>II</h2>
<p>In announcing its new rule, the Court purports to rely on earlier automobile search cases, especially <i>Carroll</i> v. <i>United States</i><i>.</i> The Court's approach, however, far from being "faithful to the interpretation of the Fourth Amendment that the Court has followed with substantial consistency throughout our history," <i>ante,</i> at 824, is plainly contrary to the letter and the spirit of our prior automobile search cases. Moreover, the new rule produces anomalous and unacceptable consequences.</p>
<p></p>
<h2>
<span class="star-pagination">*836</span> A</h2>
<p>The majority's argument that its decision is supported by our decisions in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> is misplaced. The Court in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> upheld a warrantless search of an automobile for contraband on the basis of the impracticability of securing a warrant in cases involving the transportation of contraband goods. The Court did not, however, suggest that obtaining a warrant for the search of an automobile is always impracticable.<sup>[6]</sup> "In cases where the securing of a warrant is reasonably practicable, <i>it must be used</i> . . . . In cases where seizure is impossible except without warrant, the seizing officer acts unlawfully and at his peril unless he can show the court probable cause." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S., at 156</a></span> (emphasis added).<sup>[7]</sup> As this Court reaffirmed in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> 399 U. S., <span class="star-pagination">*837</span> at 50, "[n]either <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span></i> nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords."</p>
<p>Notwithstanding the reasoning of these cases, the majority argues that <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> support its decisions because integral compartments of a car are functionally equivalent to containers found within a car, and because the practical advantages to the police of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine "would be largely nullified if the permissible scope of a warrantless search of an automobile did not include containers and packages found inside the vehicle." <i>Ante,</i> at 820. Neither of these arguments is persuasive. First, the Court's argument that allowing warrantless searches of certain integral compartments of the car in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> while protecting movable containers within the car, would be "illogical" and "absurd," <i>ante,</i> at 818, ignores the reason why this Court has allowed warrantless searches of automobile compartments. Surely an integral compartment within a car is just as mobile, and presents the same practical problems of safekeeping, as the car itself. This cannot be said of movable containers located within the car. The fact that there may be a high expectation of privacy in both containers and compartments is irrelevant, since the privacy rationale is not, and cannot be, the justification for the warrantless search of compartments.</p>
<p>The Court's second argument, which focuses on the practical advantages to police of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine, fares no better. The practical considerations which concerned the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> Court involved the difficulty of immobilizing a vehicle while a warrant must be obtained. The Court had no occasion to address whether <i>containers</i> present the same practical difficulties as the car itself or integral compartments of the car. They do not. See <i>supra,</i> at 832. <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> hardly suggested, as the Court implies, <i>ante,</i> at 820, that a warrantless <span class="star-pagination">*838</span> search is justified simply because it assists police in obtaining more evidence.</p>
<p>Although it can find no support for its rule in this Court's precedents or in the traditional justifications for the automobile exception, the majority offers another justification. In a footnote, the majority suggests that "practical considerations" militate against securing containers found during an automobile search and taking them to the magistrate. <i>Ante,</i> at 821, n. 28. The Court confidently remarks: "[P]rohibiting police from opening immediately a container in which the object of the search is most likely to be found and instead forcing them first to comb the entire vehicle would actually exacerbate the intrusion on privacy interests. Moreover, until the container itself was opened the police could never be certain that the contraband was not secreted in a yet undiscovered portion of the vehicle." <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Ibid.</a></span></i> The vehicle would have to be seized while a warrant was obtained, a requirement inconsistent with <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and <i>Chambers. Ante,</i> at 821, n. 28.</p>
<p>This explanation is unpersuasive. As this Court explained in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> and as the majority today implicitly concedes, the burden to police departments of seizing a package or personal luggage simply does not compare to the burden of seizing and safeguarding automobiles. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#765" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 765, n. 14</a></span>; <i>ante,</i> at 811, and n. 16. Other aspects of the Court's explanation are also implausible. The search will not always require a "combing" of the entire vehicle, since police may be looking for a particular item and may discover it promptly. If, instead, they are looking more generally for evidence of a crime, the immediate opening of the container will not protect the defendant's privacy; whether or not it contains contraband, the police will continue to search for new evidence. Finally, the defendant, not the police, should be afforded the choice whether he prefers the immediate opening of his suitcase or other container to the delay incident to seeking a warrant. Cf. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders"><i>Sanders, supra,</i> at 764, n. 12</a></span>. The more reasonable <span class="star-pagination">*839</span> presumption, if a presumption is to replace the defendant's consent, is surely that the immediate search of a closed container will be a greater invasion of the defendant's privacy interests than a mere temporary seizure of the container.<sup>[8]</sup></p>
<p></p>
<h2>B</h2>
<p>Finally, the majority's new rule is theoretically unsound and will create anomalous and unwarranted results. These consequences are readily apparent from the Court's attempt to reconcile its new rule with the holdings of <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>.</i><sup>[9]</sup> The Court suggests that probable cause to search only a container does not justify a warrantless search of an automobile in which it is placed, absent reason to believe that the contents could be secreted elsewhere in the vehicle. This, the majority asserts, is an indication that the new rule is carefully limited to its justification, and is not inconsistent with <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>.</i> But why is such a container more private, less difficult for police to seize and store, or in any other relevant respect more properly subject to the warrant <span class="star-pagination">*840</span> requirement, than a container that police discover in a probable-cause search of an entire automobile?<sup>[10]</sup> This rule plainly has peculiar and unworkable consequences: the Government "must show that the investigating officer knew enough but not too much, that he had sufficient knowledge to establish probable cause but insufficient knowledge to know exactly where the contraband was located." 210 U. S. App. D. C. 342, 384, <span class="citation" data-id="9468224"><a href="/opinion/392944/united-states-v-albert-ross-jr/#1201" aria-description="Citation for case: United States v. Albert Ross, Jr.">655 F. 2d 1159, 1201</a></span> (1981) (en banc) (Wilkey, J., dissenting).</p>
<p>Alternatively, the majority may be suggesting that <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> may be explained because the connection of the container to the vehicle was incidental in these two cases. That is, because police had pre-existing probable cause to seize and search the containers, they were not entitled to wait until the item was placed in a vehicle to take advantage of the automobile exception. Cf. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971); 2 W. LaFave, Search and Seizure 519-525 (1978). I wholeheartedly agree that police cannot employ a pretext to escape Fourth Amendment prohibitions and cannot rely on an exigency that they could easily have avoided. This interpretation, however, might well be an exception that swallows up the majority's rule. In neither <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> nor <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> did the Court suggest that the delay of the police was a pretext for taking advantage of the automobile exception. For all that appears, the Government may have had legitimate reasons for not searching as soon as they had probable cause. In any event, asking police to rely <span class="star-pagination">*841</span> on such an uncertain line in distinguishing between legitimate and illegitimate searches for containers in automobiles hardly indicates that the majority's approach has brought clarification to this area of the law. <i>Ante,</i> at 804; see <i>Robbins,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#435" aria-description="Citation for case: Robbins v. California">453 U. S., at 435</a></span> (POWELL, J., concurring in judgment).<sup>[11]</sup></p>
<p></p>
<h2>III</h2>
<p>The Court today ignores the clear distinction that <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> established between movable containers and automobiles. It also rejects all of the relevant reasoning of <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i><sup>[12]</sup> and offers a substitute rationale that appears inconsistent with the result. See <i>supra,</i> at 832. <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> is therefore effectively overruled. And the Court unambiguously overrules "the disposition" of <i>Robbins, ante,</i> at 824, though it gingerly avoids stating that it is overruling the case itself.</p>
<p>The only convincing explanation I discern for the majority's broad rule is expediency: it assists police in conducting <span class="star-pagination">*842</span> automobile searches, ensuring that the private containers into which criminal suspects often place goods will no longer be a Fourth Amendment shield. See <i>ante,</i> at 820. "When a legitimate search is under way," the Court instructs us, "nice distinctions between . . . glove compartments, upholstered seats, trunks, and wrapped packages . . . must give way to the interest in the prompt and efficient completion of the task at hand." <i>Ante,</i> at 821. No "nice distinctions" are necessary, however, to comprehend the well-recognized differences between movable containers (which, even after today's decision, would be subject to the warrant requirement if located outside an automobile), and the automobile itself, together with its integral parts. Nor can I pass by the majority's glib assertion that the "prompt and efficient completion of the task at hand" is paramount to the Fourth Amendment interests of our citizens. I had thought it well established that "the mere fact that law enforcement may be made more efficient can never by itself justify disregard of the Fourth Amendment." <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 393</a></span>.<sup>[13]</sup></p>
<p>This case will have profound implications for the privacy of citizens traveling in automobiles, as the Court well understands. "For countless vehicles are stopped on highways and public streets every day and our cases demonstrate that it is not uncommon for police officers to have probable cause to believe that contraband may be found in a stopped vehicle." <i>Ante,</i> at 803-804. A closed paper bag, a toolbox, a knapsack, a suitcase, and an attache case can alike be searched without the protection of the judgment of a neutral magistrate, based only on the rarely disturbed decision of a police officer that he has probable cause to search for contraband in the vehicle.<sup>[14]</sup> The Court derives satisfaction from <span class="star-pagination">*843</span> the fact that its rule does not exalt the rights of the wealthy over the rights of the poor. <i>Ante,</i> at 822. A rule so broad that all citizens lose vital Fourth Amendment protection is no cause for celebration.</p>
<p>I dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Fred E. Inbau, Wayne W. Schmidt,</i> and <i>James P. Manak</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al., as <i>amici curiae</i> urging reversal.</p>
<p>[1]  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." U. S. Const., Amdt. 4.</p>
<p>[2]  The court rejected the Government's argument that the warrantless search of the leather pouch was justified as incident to respondent's arrest. App. to Pet. for Cert. 137a. The Government has not challenged this holding.</p>
<p>[3]  Judge Tamm, the author of the original panel opinion, reiterated the view that <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> prohibited the warrantless search of the leather pouch but not the search of the paper bag. Judge Robb agreed that this result was compelled by <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> although he stated that in his opinion "the right to search an automobile should include the right to open any container found within the automobile, just as the right to search a lawfully arrested prisoner carries with it the right to examine the contents of his wallet and any envelope found in his pocket, and the right to search a room includes authority to open and search all the drawers and containers found within the room." 210 U. S. App. D. C., at 363, <span class="citation" data-id="9468224"><a href="/opinion/392944/united-states-v-albert-ross-jr/#1180" aria-description="Citation for case: United States v. Albert Ross, Jr.">655 F. 2d, at 1180</a></span>. Judge MacKinnon concurred with Judge Tamm that <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> did not prohibit the warrantless search of the paper bag. Concerning the leather pouch, he agreed with Judge Wilkey, who dissented on the ground that <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> should not be applied retroactively.</p>
<p>[4]  Many courts have held that <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> requires that a warrant be obtained only for personal luggage and other "luggage-type" containers. See, <i>e. g., </i><i>United States</i> v. <i>Brown,</i> <span class="citation" data-id="384730"><a href="/opinion/384730/united-states-v-norbert-a-brown/" aria-description="Citation for case: United States v. Norbert A. Brown">635 F. 2d 1207</a></span> (CA6 1980); <i>United States</i> v. <i>Jimenez,</i> <span class="citation" data-id="380373"><a href="/opinion/380373/united-states-v-jane-nadia-jimenez/" aria-description="Citation for case: United States v. Jane Nadia Jimenez">626 F. 2d 39</a></span> (CA7 1980). One court has held that <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> does not apply if the police have probable cause to search an entire vehicle and not merely an isolated container within it. Cf. <i>State</i> v. <i>Bible,</i> <span class="citation" data-id="1693668"><a href="/opinion/1693668/state-v-bible/" aria-description="Citation for case: State v. Bible">389 So. 2d 42</a></span> (La. 1980), vacated and remanded, <span class="citation multiple-matches"><a href="/c/U.%20S./453/918/">453 U. S. 918</a></span>; <i>State</i> v. <i>Hernandez,</i> <span class="citation" data-id="1842632"><a href="/opinion/1842632/state-v-hernandez/" aria-description="Citation for case: State v. Hernandez">408 So. 2d 911</a></span> (La. 1981); see also 210 U. S. App. D. C., at 363, <span class="citation" data-id="9468224"><a href="/opinion/392944/united-states-v-albert-ross-jr/#1180" aria-description="Citation for case: United States v. Albert Ross, Jr.">655 F. 2d, at 1180</a></span> (Robb, J., dissenting).</p>
<p>[5]  On September 29, 1921, Carroll and Kiro met the agents in Grand Rapids and agreed to sell them three cases of whiskey. The sale was not consummated, however, possibly because Carroll learned the agents' true identity. In October, the agents discovered Carroll and Kiro driving the Oldsmobile Roadster on the road to Detroit, which was known as an active center for the introduction of illegal liquor into this country. The agents followed the roadster as far as East Lansing, but there abandoned the chase.</p>
<p>[6]  The legislation authorized customs officials to search any ship or vessel without a warrant if they had probable cause to believe that it concealed goods subject to duty. The same legislation required a warrant for searches of dwelling places. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#150" aria-description="Citation for case: Carroll v. United States">267 U. S., at 150-151</a></span>.</p>
<p>[7]  In particular, the Court noted an 1815 statute that permitted customs officers not only to board and search vessels without a warrant "but also to stop, search and examine any vehicle, beast or person on which or whom they should suspect there was merchandise which was subject to duty or had been introduced into the United States in any manner contrary to law." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#151" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 151</a></span>.</p>
<p>[8]  In light of this established history, individuals always had been on notice that movable vessels may be stopped and searched on facts giving rise to probable cause that the vehicle contains contraband, without the protection afforded by a magistrate's prior evaluation of those facts.</p>
<p>[9]  Subsequent cases make clear that the decision in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> was not based on the fact that the only course available to the police was an immediate search. As Justice Harlan later recognized, although a failure to <i>seize</i> a moving automobile believed to contain contraband might deprive officers of the illicit goods, once a vehicle itself has been stopped the exigency does not necessarily justify a warrantless <i>search. </i><i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#62" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 62-64</a></span> (opinion of Harlan, J.). The Court in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> however  with only Justice Harlan dissenting  refused to adopt a rule that would permit a warrantless seizure but prohibit a warrantless search. The Court held that if police officers have probable cause to justify a warrantless seizure of an automobile on a public roadway, they may conduct an immediate search of the contents of that vehicle. "For constitutional purposes, we see no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. Given probable cause to search, either course is reasonable under the Fourth Amendment." <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney"><i>Id.,</i> at 52</a></span>.
</p>
<p>The Court also has held that if an immediate search on the street is permissible without a warrant, a search soon thereafter at the police station is permissible if the vehicle is impounded. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers, supra;</a></span> </i><i>Texas</i> v. <i>White,</i> <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span>. These decisions are based on the practicalities of the situations presented and a realistic appraisal of the relatively minor protection that a contrary rule would provide for privacy interests. Given the scope of the initial intrusion caused by a seizure of an automobile  which often could leave the occupants stranded on the highway  the Court rejected an inflexible rule that would force police officers in every case either to post guard at the vehicle while a warrant is obtained or to tow the vehicle itself to the station. Similarly, if an immediate search on the scene could be conducted, but not one at the station if the vehicle is impounded, police often simply would search the vehicle on the street  at no advantage to the occupants, yet possibly at certain cost to the police. The rules as applied in particular cases may appear unsatisfactory. They reflect, however, a reasoned application of the more general rule that if an individual gives the police probable cause to believe a vehicle is transporting contraband, he loses the right to proceed on his way without official interference.</p>
<p>[10]  After reviewing the relevant authorities at some length, the Court concluded that the probable-cause requirement was satisfied in the case before it. The Court held that "the facts and circumstances within [the officers'] knowledge and of which they had reasonably trustworthy information were sufficient in themselves to warrant a man of reasonable caution in the belief that intoxicating liquor was being transported in the automobile which they stopped and searched." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S., at 162</a></span>. Cf. <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176-177</a></span>; <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#102" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 102</a></span>.</p>
<p>[11]  See <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span>; <i>Scher</i> v. <i>United States,</i> <span class="citation" data-id="103100"><a href="/opinion/103100/scher-v-united-states/" aria-description="Citation for case: Scher v. United States">305 U. S. 251</a></span>; <i>Brinegar</i> v. <i>United States, supra</i><i>; </i><i>Henry</i> v. <i>United States, supra</i><i>; </i><i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span>; <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>; </i><i>Texas</i> v. <i><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">White, supra</a></span></i><i>; </i><i>Colorado</i> v. <i>Bannister,</i> <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">449 U. S. 1</a></span>.
</p>
<p>Warrantless searches of automobiles have been upheld in a variety of factual contexts quite different from that presented in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i> Cf. <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>; <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span>; <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span>. Many of these searches do not require a showing of probable cause that the vehicle contains contraband. We are not called upon to  and do not  consider in this case the scope of the warrantless search that is permitted in those cases.</p>
<p>[12]  As the Court in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> concluded:
</p>
<p>"We here find the line of distinction between legal and illegal seizures of liquor in transport in vehicles. It is certainly a reasonable distinction. It gives the owner of an automobile or other vehicle seized under Section 26, in absence of probable cause, a right to have restored to him the automobile, it protects him under the <i>Weeks</i> [<i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>] and <i>Amos</i> [<i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>] cases from use of the liquor as evidence against him, and it subjects the officer making the seizures to damages. On the other hand, in a case showing probable cause, the Government and its officials are given the opportunity which they should have, to make the investigation necessary to trace reasonably suspected contraband goods and to seize them." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S., at 156</a></span>.</p>
<p>[13]  The District Court noted:
</p>
<p>"In this case, there was no nexus between the search and the automobile, merely a coincidence. The challenged search in this case was one of a footlocker, not an automobile. The search took place not in an automobile, but in [the federal building]. The only connection that the automobile had to this search was that, prior to its seizure, the footlocker was placed on the floor of an automobile's open trunk." <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="1452588"><a href="/opinion/1452588/united-states-v-chadwick/#772" aria-description="Citation for case: United States v. Chadwick">393 F. Supp. 763, 772</a></span> (Mass. 1975).</p>
<p>[14]  This Court specifically noted: "The Government does not contend that the footlocker's brief contact with Chadwick's car makes this an automobile search, but it is argued that the rationale of our automobile search cases demonstrates the reasonableness of permitting warrantless searches of luggage; the Government views such luggage as analagous to motor vehicles for Fourth Amendment purposes." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 11-12</a></span>.</p>
<p>[15]  See <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#17" aria-description="Citation for case: United States v. Chadwick"><i>id.,</i> at 17</a></span> (BLACKMUN, J., dissenting).</p>
<p>[16]  The Court concluded that there is a significant difference between the seizure of a sealed package and a subsequent search of its contents; the search of the container in that case was "a far greater intrusion into Fourth Amendment values than the impoundment of the footlocker." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#14" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 14, n. 8</a></span>. A temporary seizure of a package or piece of luggage often may be accomplished without as significant an intrusion upon the individual  and without as great a burden on the police  as in the case of the seizure of an automobile. See n. 9, <i>supra.</i></p>
<p>[17]  The Arkansas Supreme Court carefully reviewed the facts of the case and concluded: "The information supplied to the police by the confidential informant is adequate to support the State's claim that the police had probable cause to believe that appellant's green suitcase contained a controlled substance when the police confiscated the suitcase and opened it." <i>Sanders</i> v. <i>State,</i> <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#599" aria-description="Citation for case: Sanders v. State">262 Ark. 595, 599</a></span>, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#706" aria-description="Citation for case: Sanders v. State">559 S. W. 2d 704, 706</a></span> (1977). The court also noted: "The evidence in this case supports the conclusion that the relationship between the suitcase and the taxicab is coincidental." <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#600" aria-description="Citation for case: Sanders v. State"><i>Id.,</i> at 600, n. 2</a></span>, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#706" aria-description="Citation for case: Sanders v. State">559 S. W. 2d, at 706, n. 2</a></span>.</p>
<p>[18]  Moreover, none of the practical difficulties associated with the detention of a vehicle on a public highway that made the immediate search in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> reasonable could justify an immediate search of the suitcase, since the officers had no interest in detaining the taxi or its driver.</p>
<p>[19]  The Court stated that "the extent to which the Fourth Amendment applies to containers and other parcels depends not at all upon whether they are seized from an automobile." <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 764, n. 13</a></span>. This general rule was limited only by the observation that "[n]ot all containers and packages found by police during the course of a search will deserve the full protection of the Fourth Amendment. Thus, some containers (for example a kit of burglar tools or a gun case) by their very nature cannot support any reasonable expectation of privacy because their contents can be inferred from their outward appearance. Similarly, in some cases the contents of a package will be open to `plain view,' thereby obviating the need for a warrant." <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-

[...TRUNCATED 23975 of 143975 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/United States v. Russell.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Russell"
type: case
citation: "411 U.S. 423 (1973)"
parallel_cite: "93 S. Ct. 1637; 36 L. Ed. 2d 366"
neutral_cite: 1973 U.S. LEXIS 79
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-04-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-04-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Russell
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108768/united-states-v-russell/"
  cluster_id: 108768
  opinion_id: 108768
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Anchor"
related: ["[[Sorrells v. United States]]", "[[Sherman v. United States]]", "[[Hampton v. United States]]", "[[Jacobson v. United States]]"]
aliases: []
tags: ["case", "entrapment", "predisposition", "subjective-test", "outrageous-government-conduct", "due-process"]
holding: "There is no entrapment where the defendant was predisposed, even though a government agent supplied a difficult-to-obtain but legal…"
lake:
  record_id: United States v. Russell
  status: verified
  projected_at: 2026-07-06
---

# United States v. Russell

*411 U.S. 423 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An undercover federal agent offered to supply Russell with phenyl-2-propanone — a scarce but legal chemical essential to manufacture methamphetamine — in exchange for half the drug produced and a look at the laboratory. Russell and his associates were already manufacturing methamphetamine before the agent appeared and continued after he left; the propanone could have been, and in part was, obtained without the agent. Russell was convicted, but the Court of Appeals reversed, finding entrapment as a matter of law because the agent had supplied an essential ingredient.

## Issue
Whether a predisposed defendant may establish the entrapment defense merely because a government agent supplied an essential (though legal) ingredient for the crime — or whether such government participation independently bars conviction.

## Rule
No. Entrapment is a limited defense centered on the defendant's predisposition, not on judicial disapproval of police methods. The Court reaffirmed the subjective test: "It is only when the Government's deception actually implants the criminal design in the mind of the defendant that the defense of entrapment comes into play." — 411 U.S. at 436. ^pin-436

The Court left open, without applying, a separate due-process limit for the most extreme cases: "While we may some day be presented with a situation in which the conduct of law enforcement agents is so outrageous that due process principles would absolutely bar the government from invoking judicial processes to obtain a conviction . . . the instant case is distinctly not of that breed." — 411 U.S. at 431–432. ^pin-431

## Application
Russell conceded he may have been predisposed, and the evidence showed he was an active participant in a methamphetamine operation that began before the agent appeared and continued after he left. Because the criminal design originated with Russell rather than being implanted by the agent, supplying the legal ingredient did not establish entrapment; and the agent's conduct was not so outrageous as to bar prosecution on due-process grounds.

## Conclusion
A predisposed defendant cannot claim entrapment merely because an agent supplied a lawful, hard-to-obtain ingredient; the Supreme Court reversed the Court of Appeals and reinstated the conviction.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Russell* reaffirms the subjective predisposition test rooted in [[Sorrells v. United States]] and [[Sherman v. United States]], and is the origin of the (rarely successful) due-process "outrageous government conduct" bar, revisited in [[Hampton v. United States]].

## Appears on
- [[Entrapment]] — *Key — Anchor*

## Sources
- *United States v. Russell*, 411 U.S. 423 (1973) — https://www.courtlistener.com/opinion/108768/united-states-v-russell/ — pinpoints: 431–432, 436 (parallel 93 S. Ct. 1637).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c193b0d746449fa4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "411 U.S. 423 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 79", "official_citation_present": true, "parallel_cite": "93 S. Ct. 1637; 36 L. Ed. 2d 366", "title": "United States v. Russell", "year": "1973"}}
{"assertion_id": "8e4009f49f63ab23", "dimension": "support", "kind": "home_role", "locator": {"home": "Entrapment"}, "payload": {"home": "Entrapment", "role": "Key — Anchor", "title": "United States v. Russell"}}
{"assertion_id": "964c7bd128783685", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is no entrapment where the defendant was predisposed, even though a government agent supplied a difficult-to-obtain but legal…", "title": "United States v. Russell"}}
{"assertion_id": "186bfd520fcc6467", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-04-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Russell", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Russell", "varies_by_point": "false"}}
{"assertion_id": "6976c164b8fc65dd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Russell"}}
```

### lake record — United States v. Russell

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Russell",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Russell",
    "case_name_short": "Russell",
    "case_name_full": "United States v. Russell",
    "input_case_name": "United States v. Russell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-04-24",
    "year": 1973,
    "docket": null,
    "cluster_id": 108768,
    "lead_opinion_id": 108768,
    "sibling_ids": [
      108768,
      9425257,
      9425258,
      9425259
    ],
    "absolute_url": "/opinion/108768/united-states-v-russell/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "411 U.S. 423",
      "volume": "411",
      "reporter": "U.S.",
      "page": "423",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 1637",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "1637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 366",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "366",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 79",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "79",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "411 U.S. 423",
        "volume": "411",
        "reporter": "U.S.",
        "page": "423",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 1637",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "1637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 366",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "366",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 79",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "79",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "411 U.S. 423",
    "official_selection": {
      "court_class": "scotus",
      "selected": "411 U.S. 423",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-436",
      "page": null,
      "quote": "--- # United States v. Russell *411 U.S. 423 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An undercover federal agent offered to supply Russell with phenyl-2-propanone \u2014 a scarce but legal chemical essential to manufacture methamphetamine \u2014 in exchange for half the drug produced and a look at the laboratory. Russell and his associates were already manufacturing methamphetamine before the agent appeared and continued after he left; the propanone could have been, and in part was, obtained without the agent. Russell was convicted, but the Court of Appeals reversed, finding entrapment as a matter of law because the agent had supplied an essential ingredient. ## Issue Whether a predisposed defendant may establish the entrapment defense merely because a government agent supplied an essential (though legal) ingredient for the crime \u2014 or whether such government participation independently bars conviction. ## Rule No. Entrapment is a limited defense centered on the defendant's predisposition, not on judicial disapproval of police methods. The Court reaffirmed the subjective test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-431",
      "page": null,
      "quote": "While we may some day be presented with a situation in which the conduct of law enforcement agents is so outrageous that due process principles would absolutely bar the government from invoking judicial processes to obtain a conviction . . . the instant case is distinctly not of that breed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-04-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Russell",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Brock",
          "cluster_id": 7861353,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Darius McKeever",
          "cluster_id": 3212091,
          "cite": [
            "423 U.S. App. D.C. 102",
            "824 F.3d 1113",
            "2016 U.S. App. LEXIS 10517"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Washington",
          "cluster_id": 7315755,
          "cite": [
            "131 F. Supp. 3d 1007",
            "2015 U.S. Dist. LEXIS 124545",
            "2015 WL 5522286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alex Pedrin, Jr.",
          "cluster_id": 2827677,
          "cite": [
            "797 F.3d 792",
            "2015 U.S. App. LEXIS 14409",
            "2015 WL 4879850"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Barta",
          "cluster_id": 2774293,
          "cite": [
            "776 F.3d 931",
            "2015 WL 350672",
            "2015 U.S. App. LEXIS 1382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 2649659,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cordae Black",
          "cluster_id": 1086588,
          "cite": [
            "733 F.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Uribe",
          "cluster_id": 5810602,
          "cite": [
            "199 Cal. App. 4th 836",
            "132 Cal. Rptr. 3d 102",
            "2011 Cal. App. LEXIS 1253"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anderson",
          "cluster_id": 4282316,
          "cite": [
            "68 M.J. 378",
            "2010 CAAF LEXIS 207",
            "2010 WL 759182"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. George William Blood (04-5101) and Stephen L. Crittenden (04-5261)",
          "cluster_id": 793047,
          "cite": [
            "435 F.3d 612",
            "69 Fed. R. Serv. 391",
            "2006 U.S. App. LEXIS 1656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cunningham",
          "cluster_id": 3952337,
          "cite": [
            "808 N.E.2d 488",
            "156 Ohio App. 3d 714",
            "2004 Ohio 1935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gary Bradley v. W.A. Duncan, Warden",
          "cluster_id": 780450,
          "cite": [
            "315 F.3d 1091",
            "2002 Cal. Daily Op. Serv. 12349",
            "2002 Daily Journal DAR 14581",
            "2002 U.S. App. LEXIS 26580",
            "2002 WL 31866175"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maffett",
          "cluster_id": 1986216,
          "cite": [
            "633 N.W.2d 339",
            "464 Mich. 878"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kennedy",
          "cluster_id": 160210,
          "cite": [
            "225 F.3d 1187",
            "2000 Colo. J. C.A.R. 5486",
            "2000 U.S. App. LEXIS 23501",
            "2000 WL 1352891"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richmond Newspapers, Inc. v. Virginia",
          "cluster_id": 110339,
          "cite": [
            "65 L. Ed. 2d 973",
            "100 S. Ct. 2814",
            "448 U.S. 555",
            "1980 U.S. LEXIS 18",
            "6 Media L. Rep. (BNA) 1833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weatherford v. Bursey",
          "cluster_id": 109590,
          "cite": [
            "51 L. Ed. 2d 30",
            "97 S. Ct. 837",
            "429 U.S. 545",
            "1977 U.S. LEXIS 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scott",
          "cluster_id": 109895,
          "cite": [
            "57 L. Ed. 2d 65",
            "98 S. Ct. 2187",
            "437 U.S. 82",
            "1978 U.S. LEXIS 109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mathews v. United States",
          "cluster_id": 112012,
          "cite": [
            "99 L. Ed. 2d 54",
            "108 S. Ct. 883",
            "485 U.S. 58",
            "1988 U.S. LEXIS 943"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hampton v. United States",
          "cluster_id": 109437,
          "cite": [
            "48 L. Ed. 2d 113",
            "96 S. Ct. 1646",
            "425 U.S. 484",
            "1976 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacobson v. United States",
          "cluster_id": 112720,
          "cite": [
            "118 L. Ed. 2d 174",
            "112 S. Ct. 1535",
            "503 U.S. 540",
            "1992 U.S. LEXIS 2117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peo v. Houser",
          "cluster_id": 4780480,
          "cite": [
            "2020 COA 128"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Anthony Rivera",
          "cluster_id": 539940,
          "cite": [
            "900 F.2d 1462",
            "1990 U.S. App. LEXIS 4934",
            "1990 WL 37854"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Voigt",
          "cluster_id": 722380,
          "cite": [
            "89 F.3d 1050",
            "78 A.F.T.R.2d (RIA) 5577",
            "1996 U.S. App. LEXIS 16287",
            "1996 WL 380609"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Christopher Twigg, Iii, United States of America v. Henry Alfred Neville",
          "cluster_id": 361264,
          "cite": [
            "588 F.2d 373"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gordon Pennell",
          "cluster_id": 437507,
          "cite": [
            "737 F.2d 521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Toscanino",
          "cluster_id": 320547,
          "cite": [
            "500 F.2d 267"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Philip Berrigan, in No. 72-1938, and Elizabeth McAlister Appeal of Elizabeth McAlister In",
          "cluster_id": 312647,
          "cite": [
            "482 F.2d 171",
            "21 A.L.R. Fed. 105",
            "1973 U.S. App. LEXIS 9126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John M. Murphy",
          "cluster_id": 456168,
          "cite": [
            "768 F.2d 1518"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sonya Evette Singleton",
          "cluster_id": 754623,
          "cite": [
            "144 F.3d 1343",
            "1998 U.S. App. LEXIS 15451",
            "1998 WL 350507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terence George Kelly",
          "cluster_id": 531294,
          "cite": [
            "888 F.2d 732",
            "28 Fed. R. Serv. 992",
            "106 A.L.R. Fed. 965",
            "1989 U.S. App. LEXIS 15297",
            "1989 WL 125733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Bagnariol, United States of America v. Gordon L. Walgren, United States of America v. Patrick Gallagher",
          "cluster_id": 397437,
          "cite": [
            "665 F.2d 877",
            "1981 U.S. App. LEXIS 15028"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Norman Archer",
          "cluster_id": 314188,
          "cite": [
            "486 F.2d 670",
            "1973 U.S. App. LEXIS 7745"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, in No. 81-1020 v. Jannotti, Harry P. United States of America, in No. 81-1021 v. Schwartz, George X",
          "cluster_id": 401021,
          "cite": [
            "673 F.2d 578",
            "1982 WL 602723"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bullock",
          "cluster_id": 1599814,
          "cite": [
            "485 N.W.2d 866",
            "440 Mich. 15"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Zavaras",
          "cluster_id": 158747,
          "cite": [
            "195 F.3d 573",
            "1999 Colo. J. C.A.R. 6110",
            "1999 U.S. App. LEXIS 26874",
            "1999 WL 973608"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rahman",
          "cluster_id": 7078717,
          "cite": [
            "189 F.3d 88"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Russell:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108768 OR 9425257 OR 9425258 OR 9425259) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NDY1MTIwMDAwMDAmcz03NDIwMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108768+OR+9425257+OR+9425258+OR+9425259%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 17,
        "triage_snippet_classified": 183
      },
      "lane2_top_cited": {
        "query": "cites:(108768 OR 9425257 OR 9425258 OR 9425259)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODImcz01ODM3MjUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108768+OR+9425257+OR+9425258+OR+9425259%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108768 OR 9425257 OR 9425258 OR 9425259)",
        "reviewed": 17,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 17,
        "triage_read": 0,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108768 OR 9425257 OR 9425258 OR 9425259)",
    "indexed_citing_opinions": 1351,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108768,
        "count": 1216,
        "count_source": "search"
      },
      {
        "opinion_id": 9425257,
        "count": 159,
        "count_source": "search"
      },
      {
        "opinion_id": 9425258,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425259,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2014,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-russell.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5MDMzNDYmcz03ODYxMzUzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108768+OR+9425257+OR+9425258+OR+9425259%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108768,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 101251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 105682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 105981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 230738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 245604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 264312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 268751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 280730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 298766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 301226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 306412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 1457023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 1468773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108768,
        "cited_id": 1982864,
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
    "date_created": "2026-07-06T02:38:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:38:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:38:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:43:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:38:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Russell

```
<div>
<center><b><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/" aria-description="Citation for case: United States v. Russell">411 U.S. 423</a></span> (1973)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
RUSSELL.</h1></center>
<center>No. 71-1585.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 27, 1973.</center>
<center>Decided April 24, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><i>Deputy Solicitor General Lacovara</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Griswold, Assistant Attorney General Petersen, Edward R. Korman, Jerome M. Feit,</i> and <i>Roger A. Pauley.</i></p>
<p><span class="star-pagination">*424</span> <i>Thomas H. S. Brucker,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./409/946/">409 U. S. 946</a></span>, argued the cause for respondent. With him on the brief was <i>Robert E. Prince.</i><sup>[*]</sup></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Respondent Richard Russell was charged in three counts of a five-count indictment returned against him and codefendants John and Patrick Connolly.<sup>[1]</sup> After a jury trial in the District Court, in which his sole defense was entrapment, respondent was convicted on all three counts of having unlawfully manufactured and processed methamphetamine ("speed") and of having unlawfully sold and delivered that drug in violation of <span class="citation no-link">21 U. S. C. §§ 331</span> (q) (1), (2), 360a (a), (b) (1964 ed., Supp. V). He was sentenced to concurrent terms of two years in prison for each offense, the terms to be suspended on the condition that he spend six months in prison and be placed on probation for the following three years. On appeal, the United States Court of Appeals for the Ninth Circuit, one judge dissenting, reversed the conviction solely for the reason that an undercover agent supplied an essential chemical for manufacturing the methamphetamine which formed the basis of respondent's conviction. The court concluded that as a matter of law "a defense to a criminal charge may be founded upon an intolerable degree of governmental participation in the criminal enterprise." <span class="citation multiple-matches"><a href="/c/F.%202d/459/671/">459 F. 2d 671</a></span>, 673 (1972). We granted <span class="star-pagination">*425</span> certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./409/911/">409 U. S. 911</a></span> (1972), and now reverse that judgment.</p>
<p>There is little dispute concerning the essential facts in this case. On December 7, 1969, Joe Shapiro, an undercover agent for the Federal Bureau of Narcotics and Dangerous Drugs, went to respondent's home on Whidbey Island in the State of Washington where he met with respondent and his two codefendants, John and Patrick Connolly. Shapiro's assignment was to locate a laboratory where it was believed that methamphetamine was being manufactured illicitly. He told the respondent and the Connollys that he represented an organization in the Pacific Northwest that was interested in controlling the manufacture and distribution of methamphetamine. He then made an offer to supply the defendants with the chemical phenyl-2-propanone, an essential ingredient in the manufacture of methamphetamine, in return for one-half of the drug produced. This offer was made on the condition that Agent Shapiro be shown a sample of the drug which they were making and the laboratory where it was being produced.</p>
<p>During the conversation, Patrick Connolly revealed that he had been making the drug since May 1969 and since then had produced three pounds of it.<sup>[2]</sup> John Connolly gave the agent a bag containing a quantity of methamphetamine that he represented as being from "the last batch that we made." Shortly thereafter, Shapiro and Patrick Connolly left respondent's house to view the laboratory which was located in the Connolly house on Whidbey Island. At the house, Shapiro observed an empty bottle bearing the chemical label phenyl-2-propanone.</p>
<p><span class="star-pagination">*426</span> By prearrangement, Shapiro returned to the Connolly house on December 9, 1969, to supply 100 grams of propanone and observe the manufacturing process. When he arrived he observed Patrick Connolly and the respondent cutting up pieces of aluminum foil and placing them in a large flask. There was testimony that some of the foil pieces accidentally fell on the floor and were picked up by the respondent and Shapiro and put into the flask.<sup>[3]</sup> Thereafter, Patrick Connolly added all of the necessary chemicals, including the propanone brought by Shapiro, to make two batches of methamphetamine. The manufacturing process having been completed the following morning, Shapiro was given one-half of the drug and respondent kept the remainder. Shapiro offered to buy, and the respondent agreed to sell, part of the remainder for $60.</p>
<p>About a month later, Shapiro returned to the Connolly house and met with Patrick Connolly to ask if he was still interested in their "business arrangement." Connolly replied that he was interested but that he had recently obtained two additional bottles of phenyl-2-propanone and would not be finished with them for a couple of days. He provided some additional metham-phetamine to Shapiro at that time. Three days later Shapiro returned to the Connolly house with a search warrant and, among other items, seized an empty 500-gram bottle of propanone and a 100-gram bottle, not the one he had provided, that was partially filled with the chemical.</p>
<p>There was testimony at the trial of respondent and Patrick Connolly that phenyl-2-propanone was generally difficult to obtain. At the request of the Bureau of <span class="star-pagination">*427</span> Narcotics and Dangerous Drugs, some chemical supply firms had voluntarily ceased selling the chemical.</p>
<p>At the close of the evidence, and after receiving the District Judge's standard entrapment instruction,<sup>[4]</sup> the jury found the respondent guilty on all counts charged. On appeal, the respondent conceded that the jury could have found him predisposed to commit the offenses, 459 F. 2d, at 672, but argued that on the facts presented there was entrapment as a matter of law. The Court of Appeals agreed, although it did not find the District Court had misconstrued or misapplied the traditional standards governing the entrapment defense. Rather, the court in effect expanded the traditional notion of entrapment, which focuses on the predisposition of the defendant, to mandate dismissal of a criminal prosecution whenever the court determines that there has been "an intolerable degree of governmental participation in the criminal enterprise." In this case the court decided that the conduct of the agent in supplying a scarce ingredient essential for the manufacture of a controlled substance established that defense.</p>
<p>This new defense was held to rest on either of two alternative theories. One theory is based on two lower court decisions which have found entrapment, regardless of predisposition, whenever the government supplies contraband to the defendants. <i>United States</i> v. <i>Bueno,</i> 447 <span class="star-pagination">*428</span> F. 2d 903 (CA5 1971); <i>United States</i> v. <i>Chisum,</i> <span class="citation" data-id="1468773"><a href="/opinion/1468773/united-states-v-chisum/" aria-description="Citation for case: United States v. Chisum">312 F. Supp. 1307</a></span> (CD Cal. 1970). The second theory, a nonentrapment rationale, is based on a recent Ninth Circuit decision that reversed a conviction because a government investigator was so enmeshed in the criminal activity that the prosecution of the defendants was held to be repugnant to the American criminal justice system. <i>Greene</i> v. <i>United States,</i> <span class="citation" data-id="9457787"><a href="/opinion/301226/earl-d-greene-v-united-states-of-america-john-becker-v-united-states-of/" aria-description="Citation for case: Earl D. Greene v. United States of America, John Becker...">454 F. 2d 783</a></span> (CA9 1971). The court below held that these two rationales constitute the same defense, and that only the label distinguishes them. In any event, it held that "[b]oth theories are premised on fundamental concepts of due process and evince the reluctance of the judiciary to countenance `overzealous law enforcement.'" 459 F. 2d, at 674, quoting <i>Sherman</i> v. <i>United States,</i> <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#381" aria-description="Citation for case: Sherman v. United States">356 U. S. 369, 381</a></span> (1958) (Frank-furter, J., concurring in result).</p>
<p>This Court first recognized and applied the entrapment defense in <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932).<sup>[5]</sup> In <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span>,</i> a federal prohibition agent visited the defendant while posing as a tourist and engaged him in conversation about their common war experiences. After gaining the defendant's confidence, the agent asked for some liquor, was twice refused, but upon asking a third time the defendant finally capitulated, and was subsequently prosecuted for violating the National Prohibition Act.</p>
<p>Mr. Chief Justice Hughes, speaking for the Court, held that as a matter of statutory construction the defense of entrapment should have been available to the defendant. Under the theory propounded by the Chief Justice, the entrapment defense prohibits law enforcement officers from instigating a criminal act by persons "otherwise innocent <span class="star-pagination">*429</span> in order to lure them to its commission and to punish them." <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#448" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 448</a></span>. Thus, the thrust of the entrapment defense was held to focus on the intent or predisposition of the defendant to commit the crime. "[I]f the defendant seeks acquittal by reason of entrapment he cannot complain of an appropriate and searching inquiry into his own conduct and predisposition as bearing upon that issue." <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#451" aria-description="Citation for case: Sorrells v. United States"><i>Id.,</i> at 451</a></span>.</p>
<p>Mr. Justice Roberts concurred but was of the view "that courts must be closed to the trial of a crime instigated by the government's own agents." <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#459" aria-description="Citation for case: Sorrells v. United States"><i>Id.,</i> at 459</a></span>.<sup>[6]</sup> The difference in the view of the majority and the concurring opinions is that in the former the inquiry focuses on the predisposition of the defendant, whereas in the latter the inquiry focuses on whether the government "instigated the crime."</p>
<p>In 1958 the Court again considered the theory underlying the entrapment defense and expressly reaffirmed the view expressed by the <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> majority. <i>Sherman</i> v. <i>United States, supra</i><i>.</i> In <i><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span></i> the defendant was convicted of selling narcotics to a Government informer. As in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span>,</i> it appears that the Government agent gained the confidence of the defendant and, despite initial reluctance, the defendant finally acceded to the repeated importunings of the agent to commit the criminal act. On the basis of <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span>,</i> this Court reversed the affirmance of the defendant's conviction.</p>
<p>In affirming the theory underlying <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span>,</i> Mr. Chief Justice Warren for the Court, held that "[t]o determine whether entrapment has been established, a line must be drawn between the trap for the unwary innocent and the trap for the unwary criminal." <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S., at 372</a></span>. Mr. Justice Frankfurter stated in an opinion concurring <span class="star-pagination">*430</span> in the result that he believed Mr. Justice Roberts had the better view in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and would have framed the question to be asked in an entrapment defense in terms of "whether the police conduct revealed in the particular case falls below standards . . . for the proper use of governmental power." <i>Id.,</i> at 382.<sup>[7]</sup></p>
<p>In the instant case, respondent asks us to reconsider the theory of the entrapment defense as it is set forth in the majority opinions in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and <i><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span>.</i> His principal contention is that the defense should rest on constitutional grounds. He argues that the level of Shapiro's involvement in the manufacture of the methamphetamine was so high that a criminal prosecution for the drug's manufacture violates the fundamental principles of due process. The respondent contends that the same factors that led this Court to apply the exclusionary rule to illegal searches and seizures, <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), and confessions, <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), should be considered here. But he would have the Court go further in deterring undesirable official conduct by requiring that any prosecution be barred absolutely because of the police involvement in criminal activity. The analogy is imperfect in any event, for the principal reason behind the adoption of the exclusionary rule was the Government's "failure to observe its own laws." <i>Mapp</i> v. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#659" aria-description="Citation for case: Mapp v. Ohio"><i>Ohio, supra,</i> at 659</a></span>. Unlike the situations giving rise to the holdings in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Government's conduct here violated no independent constitutional right of the respondent. Nor did Shapiro violate any federal statute or rule or commit any crime in infiltrating the respondent's drug enterprise.</p>
<p><span class="star-pagination">*431</span> Respondent would overcome this basic weakness in his analogy to the exclusionary rule cases by having the Court adopt a rigid constitutional rule that would preclude any prosecution when it is shown that the criminal conduct would not have been possible had not an undercover agent "supplied an indispensable means to the commission of the crime that could not have been obtained otherwise, through legal or illegal channels." Even if we were to surmount the difficulties attending the notion that due process of law can be embodied in fixed rules, and those attending respondent's particular formulation, the rule he proposes would not appear to be of significant benefit to him. For, on the record presented, it appears that he cannot fit within the terms of the very rule he proposes.<sup>[8]</sup></p>
<p>The record discloses that although the propanone was difficult to obtain, it was by no means impossible. The defendants admitted making the drug both before and after those batches made with the propanone supplied by Shapiro. Shapiro testified that he saw an empty bottle labeled phenyl-2-propanone on his first visit to the laboratory on December 7, 1969. And when the laboratory was searched pursuant to a search warrant on January 10, 1970, two additional bottles labeled phenyl-2-propanone were seized. Thus, the facts in the record amply demonstrate that the propanone used in the illicit manufacture of methamphetamine not only <i>could</i> have been obtained without the intervention of Shapiro but was in fact obtained by these defendants.</p>
<p>While we may some day be presented with a situation in which the conduct of law enforcement agents is so outrageous that due process principles would absolutely bar the government from invoking judicial processes to <span class="star-pagination">*432</span> obtain a conviction, cf. <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952), the instant case is distinctly not of that breed. Shapiro's contribution of propanone to the criminal enterprise already in process was scarcely objectionable. The chemical is by itself a harmless substance and its possession is legal. While the Government may have been seeking to make it more difficult for drug rings, such as that of which respondent was a member, to obtain the chemical, the evidence described above shows that it nonetheless was obtainable. The law enforcement conduct here stops far short of violating that "fundamental fairness, shocking to the universal sense of justice," mandated by the Due Process Clause of the Fifth Amendment. <i>Kinsella</i> v. <i>United States ex rel. Singleton,</i> <span class="citation" data-id="9421900"><a href="/opinion/105981/kinsella-v-united-states-ex-rel-singleton/#246" aria-description="Citation for case: Kinsella v. United States Ex Rel. Singleton">361 U. S. 234, 246</a></span> (1960).</p>
<p>The illicit manufacture of drugs is not a sporadic, isolated criminal incident, but a continuing, though illegal, business enterprise. In order to obtain convictions for illegally manufacturing drugs, the gathering of evidence of past unlawful conduct frequently proves to be an all but impossible task. Thus in drug-related offenses law enforcement personnel have turned to one of the only practicable means of detection: the infiltration of drug rings and a limited participation in their unlawful present practices. Such infiltration is a recognized and permissible means of investigation; if that be so, then the supply of some item of value that the drug ring requires must, as a general rule, also be permissible. For an agent will not be taken into the confidence of the illegal entrepreneurs unless he has something of value to offer them. Law enforcement tactics such as this can hardly be said to violate "fundamental fairness" or "shocking to the universal sense of justice," <i><span class="citation" data-id="9421900"><a href="/opinion/105981/kinsella-v-united-states-ex-rel-singleton/" aria-description="Citation for case: Kinsella v. United States Ex Rel. Singleton">Kinsella, supra</a></span></i><i>.</i></p>
<p>Respondent also urges, as an alternative to his constitutional argument, that we broaden the nonconstitutional <span class="star-pagination">*433</span> defense of entrapment in order to sustain the judgment of the Court of Appeals. This Court's opinions in <i>Sorrells</i> v. <i>United States, supra</i><i>,</i> and <i>Sherman</i> v. <i>United States, supra</i><i>,</i> held that the principal element in the defense of entrapment was the defendant's predisposition to commit the crime. Respondent conceded in the Court of Appeals, as well he might, "that he may have harbored a predisposition to commit the charged offenses." 459 F. 2d, at 672. Yet he argues that the jury's refusal to find entrapment under the charge submitted to it by the trial court should be overturned and the views of Justices Roberts and Frankfurter, in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and <i><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span>,</i> respectively, which make the essential element of the defense turn on the type and degree of governmental conduct, be adopted as the law.</p>
<p>We decline to overrule these cases. <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> is a precedent of long standing that has already been once reexamined in <i><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span></i> and implicitly there reaffirmed. Since the defense is not of a constitutional dimension, Congress may address itself to the question and adopt any substantive definition of the defense that it may find desirable.<sup>[9]</sup></p>
<p>Critics of the rule laid down in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and <i><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span></i> have suggested that its basis in the implied intent of Congress is largely fictitious, and have pointed to what they conceive to be the anomalous difference between the treatment of a defendant who is solicited by a private individual and one who is entrapped by a government agent. Questions have been likewise raised as to whether "predisposition" can be factually established with the requisite degree of certainty. Arguments such as these, while not devoid of appeal, have been twice <span class="star-pagination">*434</span> previously made to this Court, and twice rejected by it, first in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and then in <i><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span>.</i></p>
<p>We believe that at least equally cogent criticism has been made of the concurring views in these cases. Commenting in <i><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span></i> on Mr. Justice Roberts' position in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> that "although the defendant could claim that the Government had induced him to commit the crime, the Government could not reply by showing that the defendant's criminal conduct was due to his own readiness and not to the persuasion of government agents," <i>Sherman</i> v. <i>United States,</i> <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#376" aria-description="Citation for case: Sherman v. United States">356 U. S., at 376-377</a></span>, Mr. Chief Justice Warren quoted the observation of Judge Learned Hand in an earlier stage of that proceeding:</p>
<blockquote>" `Indeed, it would seem probable that, if there were no reply [to the claim of inducement], it would be impossible ever to secure convictions of any offences which consist of transactions that are carried on in secret.' <i>United States</i> v. <i>Sherman,</i> <span class="citation" data-id="230738"><a href="/opinion/230738/united-states-v-sherman/#882" aria-description="Citation for case: United States v. Sherman">200 F. 2d 880, 882</a></span>." <i>Sherman</i> v. <i>United States,</i> <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">356 U. S., at 377</a></span> n. 7.</blockquote>
<p>Nor does it seem particularly desirable for the law to grant complete immunity from prosecution to one who himself planned to commit a crime, and then committed it, simply because government undercover agents subjected him to inducements which might have seduced a hypothetical individual who was not so predisposed. We are content to leave the matter where it was left by the Court in <i>Sherman:</i></p>
<blockquote>"The function of law enforcement is the prevention of crime and the apprehension of criminals. Manifestly, that function does not include the manufacturing of crime. Criminal activity is such that stealth and strategy are necessary weapons in the arsenal of the police officer. However, `A different question is presented when the criminal design originates <span class="star-pagination">*435</span> with the officials of the Government, and they implant in the mind of an innocent person the disposition to commit the alleged offense and induce its commission in order that they may prosecute.'" <i>Id.,</i> at 372, quoting <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 442</a></span>.</blockquote>
<p>Several decisions of the United States district courts and courts of appeals have undoubtedly gone beyond this Court's opinions in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and <i>Sherman</i> in order to bar prosecutions because of what they thought to be, for want of a better term, "overzealous law enforcement." But the defense of entrapment enunciated in those opinions was not intended to give the federal judiciary a "chancellor's foot" veto over law enforcement practices of which it did not approve. The execution of the federal laws under our Constitution is confided primarily to the Executive Branch of the Government, subject to applicable constitutional and statutory limitations and to judicially fashioned rules to enforce those limitations. We think that the decision of the Court of Appeals in this case quite unnecessarily introduces an unmanageably subjective standard which is contrary to the holdings of this Court in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and <i>Sherman.</i></p>
<p>Those cases establish that entrapment is a relatively limited defense. It is rooted, not in any authority of the Judicial Branch to dismiss prosecutions for what it feels to have been "overzealous law enforcement," but instead in the notion that Congress could not have intended criminal punishment for a defendant who has committed all the elements of a proscribed offense, but was induced to commit them by the Government.</p>
<p><i>Sorrells</i> and <i>Sherman</i> both recognize "that the fact that officers or employees of the Government merely afford opportunities or facilities for the commission of the offense does not defeat the prosecution," <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#441" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 441</a></span>; <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S., at 372</a></span>. Nor will the mere fact of <span class="star-pagination">*436</span> deceit defeat a prosecution, see, <i>e. g., </i><i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#208" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 208-209</a></span> (1966), for there are circumstances when the use of deceit is the only practicable law enforcement technique available. It is only when the Government's deception actually implants the criminal design in the mind of the defendant that the defense of entrapment comes into play.</p>
<p>Respondent's concession in the Court of Appeals that the jury finding as to predisposition was supported by the evidence is, therefore, fatal to his claim of entrapment. He was an active participant in an illegal drug manufacturing enterprise which began before the Government agent appeared on the scene, and continued after the Government agent had left the scene. He was, in the words of <i>Sherman, supra,</i> not an "unwary innocent" but an "unwary criminal." The Court of Appeals was wrong, we believe, when it sought to broaden the principle laid down in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and <i>Sherman.</i> Its judgment is therefore.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE DOUGLAS, with whom MR. JUSTICE BRENNAN concurs, dissenting.</p>
<p>A federal agent supplied the accused with one chemical ingredient of the drug known as methamphetamine ("speed") which the accused manufactured and for which act he was sentenced to prison. His defense was entrapment, which the Court of Appeals sustained and which the Court today disallows. Since I have an opposed view of entrapment, I dissent.</p>
<p>My view is that of Mr. Justice Brandeis expressed in <i>Casey</i> v. <i>United States,</i> <span class="citation" data-id="9418615"><a href="/opinion/101251/casey-v-united-states/#421" aria-description="Citation for case: Casey v. United States">276 U. S. 413, 421</a></span> (dissent), that of Mr. Justice Frankfurter stated in <i>Sherman</i> v. <i>United States,</i> <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#378" aria-description="Citation for case: Sherman v. United States">356 U. S. 369, 378</a></span> (concurring in result), and that of Mr. Justice Roberts contained in <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#453" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435, 453</a></span> (concurrence).</p>
<p><span class="star-pagination">*437</span> In my view, the fact that the chemical ingredient supplied by the federal agent might have been obtained from other sources is quite irrelevant. Supplying the chemical ingredient used in the manufacture of this batch of "speed" made the United States an active participant in the unlawful activity. As stated by Mr. Justice Brandeis, dissenting in <i>Casey</i> v. <i>United States, supra,</i> at 423:</p>
<blockquote>"I am aware that courtsmistaking relative social values and forgetting that a desirable end cannot justify foul meanshave, in their zeal to punish, sanctioned the use of evidence obtained through criminal violation of property and personal rights or by other practices of detectives even more revolting. But the objection here is of a different nature. It does not rest merely upon the character of the evidence or upon the fact that the evidence was illegally obtained. The obstacle to the prosecution lies in the fact that the alleged crime was instigated by officers of the Government; that the act for which the Government seeks to punish the defendant is the fruit of their criminal conspiracy to induce its commission. The Government may set decoys to entrap criminals. But it may not provoke or create a crime and then punish the criminal, its creature."</blockquote>
<p>Mr. Justice Frankfurter stated the same philosophy in <i>Sherman</i> v. <i>United States, supra,</i> at 382-383: "No matter what the defendant's past record and present inclinations to criminality, or the depths to which he has sunk in the estimation of society, certain police conduct to ensnare him into further crime is not to be tolerated by an advanced society." And he added: "The power of government is abused and directed to an end for which it was <span class="star-pagination">*438</span> not constituted when employed to promote rather than detect crime . . . ." <i>Id.,</i> at 384.</p>
<p>Mr. Justice Roberts in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> put the idea in the following words:</p>
<blockquote>"The applicable principle is that courts must be closed to the trial of a crime instigated by the government's own agents. No other issue, no comparison of equities as between the guilty official and the guilty defendant, has any place in the enforcement of this overruling principle of public policy." <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#459" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 459</a></span>.</blockquote>
<p>May the federal agent supply the counterfeiter with the kind of paper or ink that he needs in order to get a quick and easy arrest? The Court of Appeals in <i>Greene</i> v. <i>United States,</i> <span class="citation" data-id="9457787"><a href="/opinion/301226/earl-d-greene-v-united-states-of-america-john-becker-v-united-states-of/" aria-description="Citation for case: Earl D. Greene v. United States of America, John Becker...">454 F. 2d 783</a></span>, speaking through Judges Hamley and Hufstedler, said "no" in a case where the federal agent treated the suspects "as partners" with him, offered to supply them with a still, a still site, still equipment, and an operator and supplied them with sugar. <span class="citation" data-id="9457787"><a href="/opinion/301226/earl-d-greene-v-united-states-of-america-john-becker-v-united-states-of/#786" aria-description="Citation for case: Earl D. Greene v. United States of America, John Becker..."><i>Id.,</i> at 786</a></span>.</p>
<p>The Court of Appeals in <i>United States</i> v. <i>Bueno,</i> <span class="citation" data-id="298766"><a href="/opinion/298766/united-states-v-david-bueno/" aria-description="Citation for case: United States v. David Bueno">447 F. 2d 903</a></span>, speaking through Judges Roney, Coleman, and Simpson, held that where an informer purchased heroin for the accused who in turn sold it to a federal agent, there was entrapment because the sale was made "through the creative activity of the government." <span class="citation" data-id="298766"><a href="/opinion/298766/united-states-v-david-bueno/#906" aria-description="Citation for case: United States v. David Bueno"><i>Id.,</i> at 906</a></span>.</p>
<p>In <i>United States</i> v. <i>Chisum,</i> <span class="citation" data-id="1468773"><a href="/opinion/1468773/united-states-v-chisum/" aria-description="Citation for case: United States v. Chisum">312 F. Supp. 1307</a></span>, the federal agent supplied the accused with the counterfeit money, the receipt of which was the charge against him. Judge Ferguson sustained the defense of entrapment saying, "When the government supplies the contraband, the receipt of which is illegal, the government cannot be permitted to punish the one receiving it." <span class="citation" data-id="1468773"><a href="/opinion/1468773/united-states-v-chisum/#1312" aria-description="Citation for case: United States v. Chisum"><i>Id.,</i> at 1312</a></span>.</p>
<p><span class="star-pagination">*439</span> The Court of Appeals in the instant case relied upon this line of decisions in sustaining the defense of entrapment, <span class="citation multiple-matches"><a href="/c/F.%202d/459/671/">459 F. 2d 671</a></span>. In doing so it took the view that the "prostitution of the criminal law," as Mr. Justice Roberts described it in <i>Sorrells,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#457" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 457</a></span>, was the evil at which the defense of entrapment is aimed.</p>
<p>Federal agents play a debased role when they become the instigators of the crime, or partners in its commission, or the creative brain behind the illegal scheme. That is what the federal agent did here when he furnished the accused with one of the chemical ingredients needed to manufacture the unlawful drug.</p>
<p>MR. JUSTICE STEWART, with whom MR. JUSTICE BRENNAN and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>It is common ground that "[t]he conduct with which the defense of entrapment is concerned is the <i>manufacturing</i> of crime by law enforcement officials and their agents." <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#434" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 434</a></span> (1963). For the Government cannot be permitted to instigate the commission of a criminal offense in order to prosecute someone for committing it. <i>Sherman</i> v. <i>United States,</i> <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S. 369, 372</a></span> (1958). As Mr. Justice Brandeis put it, the Government "may not provoke or create a crime and then punish the criminal, its creature." <i>Casey</i> v. <i>United States,</i> <span class="citation" data-id="9418615"><a href="/opinion/101251/casey-v-united-states/#423" aria-description="Citation for case: Casey v. United States">276 U. S. 413, 423</a></span> (1928) (dissenting opinion). It is to prevent this situation from occurring in the administration of federal criminal justice that the defense of entrapment exists. <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932); <i>Sherman</i> v. <i>United States, supra</i><i>.</i> Cf. <i>Masciale</i> v. <i>United States,</i> <span class="citation" data-id="9421600"><a href="/opinion/105682/masciale-v-united-states/" aria-description="Citation for case: Masciale v. United States">356 U. S. 386</a></span> (1958); <i>Lopez</i> v. <i>United States, supra</i><i>.</i> But the Court has been sharply divided as to the proper basis, scope, and focus of the entrapment defense, and <span class="star-pagination">*440</span> as to whether, in the absence of a conclusive showing, the issue of entrapment is for the judge or the jury to determine.</p>
<p></p>
<h2>I</h2>
<p>In <i>Sorrells</i> v. <i>United States, supra</i><i>,</i> and <i>Sherman</i> v. <i>United States, supra</i><i>,</i> the Court took what might be called a "subjective" approach to the defense of entrapment. In that view, the defense is predicated on an unexpressed intent of Congress to exclude from its criminal statutes the prosecution and conviction of persons, "otherwise innocent," who have been lured to the commission of the prohibited act through the Government's instigation. <i>Sorrells</i> v. <i>United States, supra,</i> at 448. The key phrase in this formulation is "otherwise innocent," for the entrapment defense is available under this approach only to those who would not have committed the crime but for the Government's inducements. Thus, the subjective approach focuses on the conduct and propensities of the particular defendant in each individual case: if he is "otherwise innocent," he may avail himself of the defense; but if he had the "predisposition" to commit the crime, or if the "criminal design" originated with him, thenregardless of the nature and extent of the Government's participationthere has been no entrapment. <i>Id.,</i> at 451. And, in the absence of a conclusive showing one way or the other, the question of the defendant's "predisposition" to the crime is a question of fact for the jury. The Court today adheres to this approach.</p>
<p>The concurring opinion of Mr. Justice Roberts, joined by Justices Brandeis and Stone, in the <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> case, and that of Mr. Justice Frankfurter, joined by Justices DOUGLAS, Harlan, and BRENNAN, in the <i>Sherman</i> case, took a different view of the entrapment defense. In their concept, the defense is not grounded on some unexpressed <span class="star-pagination">*441</span> intent of Congress to exclude from punishment under its statutes those otherwise innocent persons tempted into crime by the Government, but rather on the belief that "the methods employed on behalf of the Government to bring about conviction cannot be countenanced." <i>Sherman</i> v. <i>United States, supra,</i> at 380. Thus, the focus of this approach is not on the propensities and predisposition of a specific defendant, but on "whether the police conduct revealed in the particular case falls below standards, to which common feelings respond, for the proper use of governmental power." <i>Id.,</i> at 382. Phrased another way, the question is whetherregardless of the predisposition to crime of the particular defendant involvedthe governmental agents have acted in such a way as is likely to instigate or create a criminal offense. Under this approach, the determination of the lawfulness of the Government's conduct must be madeas it is on all questions involving the legality of law enforcement methodsby the trial judge, not the jury.</p>
<p>In my view, this objective approach to entrapment advanced by the Roberts opinion in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and the Frankfurter opinion in <i>Sherman</i> is the only one truly consistent with the underlying rationale of the defense.<sup>[1]</sup> Indeed, the very basis of the entrapment defense itself demands adherence to an approach that focuses on the conduct of the governmental agents, rather than on whether the defendant was "predisposed" or "otherwise innocent." I find it impossible to believe that the purpose of the defense is to effectuate some unexpressed congressional intent to exclude from its criminal statutes persons who committed a prohibited act, but would not have <span class="star-pagination">*442</span> done so except for the Government's inducements. For, as Mr. Justice Frankfurter put it, "the only legislative intention that can with any show of reason be extracted from the statute is the intention to make criminal precisely the conduct in which the defendant has engaged." <i>Sherman</i> v. <i>United States, supra,</i> at 379. See also <i>Sorrells</i> v. <i>United States, supra,</i> at 456 (Roberts, J., concurring). Since, by definition, the entrapment defense cannot arise unless the defendant actually committed the proscribed act, that defendant is manifestly covered by the terms of the criminal statute involved.</p>
<p>Furthermore, to say that such a defendant is "otherwise innocent" or not "predisposed" to commit the crime is misleading, at best. The very fact that he has committed an act that Congress has determined to be illegal demonstrates conclusively that he is not innocent of the offense. He may not have originated the precise plan or the precise details, but he was "predisposed" in the sense that he has proved to be quite capable of committing the crime. That he was induced, provoked, or tempted to do so by government agents does not make him any more innocent or any less predisposed than he would be if he had been induced, provoked, or tempted by a private personwhich, of course, would not entitle him to cry "entrapment." Since the only difference between these situations is the identity of the tempter, it follows that the significant focus must be on the conduct of the government agents, and not on the predisposition of the defendant.</p>
<p>The purpose of the entrapment defense, then, cannot be to protect persons who are "otherwise innocent." Rather, it must be to prohibit unlawful governmental activity in instigating crime. As Mr. Justice Brandeis stated in <i>Casey</i> v. <i>United States, supra,</i> at 425: "This prosecution should be stopped, not because some right of Casey's has been denied, but in order to protect the <span class="star-pagination">*443</span> Government. To protect it from illegal conduct of its officers. To preserve the purity of its courts." Cf. <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#470" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 470</a></span> (1928) (Holmes, J., dissenting); <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States"><i>id.,</i> at 485</a></span> (Brandeis, J., dissenting). If that is so, then whether the particular defendant was "predisposed" or "otherwise innocent" is irrelevant; and the important question becomes whether the Government's conduct in inducing the crime was beyond judicial toleration.</p>
<p>Moreover, a test that makes the entrapment defense depend on whether the defendant had the requisite predisposition permits the introduction into evidence of all kinds of hearsay, suspicion, and rumorall of which would be inadmissible in any other contextin order to prove the defendant's predisposition. It allows the prosecution, in offering such proof, to rely on the defendant's bad reputation or past criminal activities, including even rumored activities of which the prosecution may have insufficient evidence to obtain an indictment, and to present the agent's suspicions as to why they chose to tempt this defendant. This sort of evidence is not only unreliable, as the hearsay rule recognizes; but it is also highly prejudicial, especially if the matter is submitted to the jury, for, despite instructions to the contrary, the jury may well consider such evidence as probative not simply of the defendant's predisposition, but of his guilt of the offense with which he stands charged.</p>
<p>More fundamentally, focusing on the defendant's innocence or predisposition has the direct effect of making what is permissible or impermissible police conduct depend upon the past record and propensities of the particular defendant involved. Stated another way, this subjective test means that the Government is permitted to entrap a person with a criminal record or bad reputation, and then to prosecute him for the manufactured <span class="star-pagination">*444</span> crime, confident that his record or reputation itself will be enough to show that he was predisposed to commit the offense anyway.</p>
<p>Yet, in the words of Mr. Justice Roberts:</p>
<blockquote>"Whatever may be the demerits of the defendant or his previous infractions of law these will not justify the instigation and creation of a new crime, as a means to reach him and punish him for his past misdemeanors. . . . To say that such conduct by an official of government is condoned and rendered innocuous by the fact that the defendant had a bad reputation or had previously transgressed is wholly to disregard the reason for refusing the processes of the court to consummate an abhorrent transaction." <i>Sorrells</i> v. <i>United States, supra,</i> at 458-459.</blockquote>
<p>And as Mr. Justice Frankfurter pointed out:</p>
<blockquote>"Permissible police activity does not vary according to the particular defendant concerned; surely if two suspects have been solicited at the same time in the same manner, one should not go to jail simply because he has been convicted before and is said to have a criminal disposition. No more does it vary according to the suspicions, reasonable or unreasonable, of the police concerning the defendant's activities." <i>Sherman</i> v. <i>United States, supra,</i> at 383.</blockquote>
<p>In my view, a person's alleged "predisposition" to crime should not expose him to government participation in the criminal transaction that would be otherwise unlawful.<sup>[2]</sup></p>
<p><span class="star-pagination">*445</span> This does not mean, of course, that the Government's use of undercover activity, strategy, or deception is necessarily unlawful. <i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#208" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 208-209</a></span> (1966). Indeed, many crimes, especially so-called victimless crimes, could not otherwise be detected. Thus, government agents may engage in conduct that is likely, when objectively considered, to afford a person ready and willing to commit the crime an opportunity to do so. <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/#331" aria-description="Citation for case: Osborn v. United States">385 U. S. 323, 331-332</a></span> (1966). See also <i>Sherman</i> v. <i>United States, supra,</i> at 383-384 (Frankfurter, J., concurring).</p>
<p>But when the agents' involvement in criminal activities goes beyond the mere offering of such an opportunity, and when their conduct is of a kind that could induce or instigate the commission of a crime by one not ready and willing to commit it, thenregardless of the character or propensities of the particular person induced I think entrapment has occurred. For in that situation, the Government has engaged in the impermissible manufacturing of crime, and the federal courts should bar the prosecution in order to preserve the institutional integrity of the system of federal criminal justice.<sup>[3]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*446</span> II</h2>
<p>In the case before us, I think that the District Court erred in submitting the issue of entrapment to the jury, with instructions to acquit only if it had a reasonable doubt as to the respondent's predisposition to committing the crime. Since, under the objective test of entrapment, predisposition is irrelevant and the issue is to be decided by the trial judge, the Court of Appeals, I believe, would have been justified in reversing the conviction on this basis alone. But since the appellate court did not remand for consideration of the issue by the District Judge under an objective standard, but rather found entrapment as a matter of law and directed that the indictment be dismissed, we must reach the merits of the respondent's entrapment defense.</p>
<p>Since, in my view, it does not matter whether the respondent was predisposed to commit the offense of which he was convicted, the focus must be, rather, on the conduct of the undercover government agent. What the agent did here was to meet with a group of suspected producers of methamphetamine, including the respondent; to request the drug; to offer to supply the chemical phenyl-2-propanone in exchange for one-half of the methamphetamine to be manufactured therewith; and, when that offer was accepted, to provide the needed chemical ingredient, and to purchase some of the drug from the respondent.</p>
<p><span class="star-pagination">*447</span> It is undisputed that phenyl-2-propanone is an essential ingredient in the manufacture of methamphetamine; that it is not used for any other purpose; and that, while its sale is not illegal, it is difficult to obtain, because a manufacturer's license is needed to purchase it, and because many suppliers, at the request of the Federal Bureau of Narcotics and Dangerous Drugs, do not sell it at all. It is also undisputed that the methamphetamine which the respondent was prosecuted for manufacturing and selling was all produced on December 10, 1969, and that all the phenyl-2-propanone used in the manufacture of that batch of the drug was provided by the government agent. In these circumstances, the agent's undertaking to supply this ingredient to the respondent, thus making it possible for the Government to prosecute him for manufacturing an illicit drug with it, was, I think, precisely the type of governmental conduct that the entrapment defense is meant to prevent.</p>
<p>Although the Court of Appeals found that the phenyl-2-propanone could not have been obtained without the agent's interventionthat "there could not have been the manufacture, delivery, or sale of the illicit drug had it not been for the Government's supply of one of the essential ingredients," <span class="citation multiple-matches"><a href="/c/F.%202d/459/671/">459 F. 2d 671</a></span>, 672the Court today rejects this finding as contradicted by the facts revealed at trial. The record, as the Court states, discloses that one of the respondent's accomplices, though not the respondent himself, had obtained phenyl-2-propanone from independent sources both before and after receiving the agent's supply, and had used it in the production of methamphetamine. This demonstrates, it is said, that the chemical was obtainable other than through the government agent; and hence the agent's furnishing it for the production of the methamphetamine involved in this prosecution did no more than afford <span class="star-pagination">*448</span> an opportunity for its production to one ready and willing to produce it. Cf. <i>Osborn</i> v. <i>United States, supra,</i> at 331-332. Thus, the argument seems to be, there was no entrapment here, any more than there would have been if the agent had furnished common table salt, had that been necessary to the drug's production.</p>
<p>It cannot be doubted that if phenyl-2-propanone had been wholly unobtainable from other sources, the agent's undercover offer to supply it to the respondent in return for part of the illicit methamphetamine produced therewith an offer initiated and carried out by the agent for the purpose of prosecuting the respondent for producing methamphetaminewould be precisely the type of governmental conduct that constitutes entrapment under any definition. For the agent's conduct in that situation would make possible the commission of an otherwise totally impossible crime, and, I should suppose, would thus be a textbook example of instigating the commission of a criminal offense in order to prosecute someone for committing it.</p>
<p>But assuming in this case that the phenyl-2-propanone was obtainable through independent sources, the fact remains that that used for the particular batch of methamphetamine involved in all three counts of the indictment with which the respondent was charged<i>i. e.,</i> that produced on December 10, 1969was supplied by the Government. This essential ingredient was indisputably difficult to obtain, and yet what was used in committing the offenses of which the respondent was convicted was offered to the respondent by the Government agent, on the agent's own initiative, and was readily supplied to the respondent in needed amounts. If the chemical was so easily available elsewhere, then why did not the agent simply wait until the respondent had himself obtained the ingredients and produced the drug, and <span class="star-pagination">*449</span> then buy it from him? The very fact that the agent felt it incumbent upon him to offer to supply phenyl-2-propanone in return for the drug casts considerable doubt on the theory that the chemical could easily have been procured without the agent's intervention, and that therefore the agent merely afforded an opportunity for the commission of a criminal offense.</p>
<p>In this case, the chemical ingredient was available only to licensed persons, and the Government itself had requested suppliers not to sell that ingredient even to people with a license. Yet the Government agent readily offered, and supplied, that ingredient to an unlicensed person and asked him to make a certain illegal drug with it. The Government then prosecuted that person for making the drug produced <i>with the very ingredient</i> which its agent had so helpfully supplied. This strikes me as the very pattern of conduct that should be held to constitute entrapment as a matter of law.<sup>[4]</sup></p>
<p>It is the Government's duty to prevent crime, not to promote it. Here, the Government's agent asked that the illegal drug be produced for him, solved his quarry's practical problems with the assurance that he could provide the one essential ingredient that was difficult to obtain, furnished that element as he had promised, and bought the finished product from the respondentall so that the respondent could be prosecuted for producing and selling the very drug for which the agent had asked and for which he had provided the necessary component. <span class="star-pagination">*450</span> Under the objective approach that I would follow, this respondent was entrapped, regardless of his predisposition or "innocence."</p>
<p>In the words of Mr. Justice Roberts:</p>
<blockquote>"The applicable principle is that courts must be closed to the trial of a crime instigated by the government's own agents. No other issue, no comparison of equities as between the guilty official and the guilty defendant, has any place in the enforcement of this overruling principle of public policy." <i>Sorrells</i> v. <i>United States, supra,</i> at 459.</blockquote>
<p>I would affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[*]  <i>Paul G. Chevigny</i> and <i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>[1]  John Connolly did not appear for trial. Patrick Connolly was tried with the respondent and found guilty of all five counts against him. The validity of his conviction is not before us in this proceeding.</p>
<p>[2]  At trial Patrick Connolly admitted making this statement to Agent Shapiro but asserted that the statement was not true.</p>
<p>[3]  Agent Shapiro did not otherwise participate in the manufacture of the drug or direct any of the work.</p>
<p>[4]  The District Judge stated the governing law on entrapment as follows: "Where a person already has the willingness and the readiness to break the law, the mere fact that the government agent provides what appears to be a favorable opportunity is not entrapment." He then instructed the jury to acquit respondent if it had a "reasonable doubt whether the defendant had the previous intent or purpose to commit the offense . . . and did so only because he was induced or persuaded by some officer or agent of the government." No exception was taken by respondent to this instruction.</p>
<p>[5]  The first case to recognize and sustain a claim of entrapment by government officers as a defense was apparently <i>Woo Wai</i> v. <i>United States,</i> <span class="citation" data-id="8795796"><a href="/opinion/8811409/woo-wai-v-united-states/" aria-description="Citation for case: Woo Wai v. United States">223 F. 412</a></span> (CA9 1915).</p>
<p>[6]  Justices Brandeis and Stone concurred in this analysis.</p>
<p>[7]  Justices DOUGLAS, Harlan, and BRENNAN shared the views of entrapment expressed in the Frankfurter opinion.</p>
<p>[8]  The language quoted above first appeared in the Government's brief at 32, but was subsequently adopted by the respondent. Brief for Respondent 20-21.</p>
<p>[9]  A bill currently before the Congress contemplates an express statutory formulation of the entrapment defense. S. 1, 93d Cong., 1st Sess., § 1-3B2 (1973).</p>
<p>[1]  Both the Proposed New Federal Criminal Code (1971), Final Report of the National Commission on Reform of Federal Criminal Laws § 702, and the American Law Institute's Model Penal Code § 2.13 (Proposed Official Draft, 1962), adopt this objective approach.</p>
<p>[2]  See Donnelly, Judicial Control of Informants, Spies, Stool Pigeons, and Agent Provocateurs, 60 Yale L. J. 1091, 1111 (1951):
</p>
<p>"Clearly entrapment is a facet of a broader problem. Along with illegal search and seizures, wire tapping, false arrest, illegal detention and the third degree, it is a type of lawless law enforcement. They all spring from common motivations. Each is a substitute for skillful and scientific investigation. Each is condoned by the sinister sophism that the end, when dealing with known criminals or the `criminal classes,' justifies the employment of illegal means."</p>
<p>[3]  Several federal courts have adopted the objective test advanced by Mr. Justice Roberts and Mr. Justice Frankfurter, or a variant thereof, focusing on the conduct of the government agents, rather than the "predisposition" of the particular defendant. See, <i>e. g., </i><i>United States</i> v. <i>McGrath,</i> <span class="citation" data-id="306412"><a href="/opinion/306412/united-states-v-joseph-t-mcgrath/#1030" aria-description="Citation for case: United States v. Joseph T. McGrath">468 F. 2d 1027, 1030-1031</a></span> (CA7 1972); <i>Greene</i> v. <i>United States,</i> <span class="citation" data-id="9457787"><a href="/opinion/301226/earl-d-greene-v-united-states-of-america-john-becker-v-united-states-of/#786" aria-description="Citation for case: Earl D. Greene v. United States of America, John Becker...">454 F. 2d 783, 786-787</a></span> (CA9 1971); <i>Carbajal-Portillo</i> v. <i>United States,</i> <span class="citation" data-id="9453746"><a href="/opinion/280730/javier-carbajal-portillo-rafael-vega-picos-v-united-states/#948" aria-description="Citation for case: Javier Carbajal-Portillo, Rafael Vega-Picos v. United States">396 F. 2d 944, 948</a></span> (CA9 1968); <i>Smith</i> v. <i>United States,</i> 118 U. S. App. D. C. 38, 44, 46, <span class="citation" data-id="9450024"><a href="/opinion/264312/raymond-smith-v-united-states/#790" aria-description="Citation for case: Raymond Smith v. United States">331 F. 2d 784, 790, 792</a></span> (1964) (<i>en banc</i>); <i>United States</i> v. <i>Chisum,</i> <span class="citation" data-id="1468773"><a href="/opinion/1468773/united-states-v-chisum/" aria-description="Citation for case: United States v. Chisum">312 F. Supp. 1307</a></span> (CD Cal. 1970). Cf. <i>United States</i> v. <i>Morrison,</i> <span class="citation" data-id="268751"><a href="/opinion/268751/united-states-v-dillard-morrison/#1004" aria-description="Citation for case: United States v. Dillard Morrison">348 F. 2d 1003, 1004</a></span> (CA2 1965); <i>Accardi</i> v. <i>United States,</i> <span class="citation" data-id="245604"><a href="/opinion/245604/joseph-anthony-accardi-stephen-morales-and-herman-john-doming-v-united/#172" aria-description="Citation for case: Joseph Anthony Accardi, Stephen Morales and Herman John...">257 F. 2d 168, 172-173, n. 5</a></span> (CA5 1958); <i>United States</i> v. <i>Kros,</i> <span class="citation" data-id="1982864"><a href="/opinion/1982864/united-states-v-kros/#979" aria-description="Citation for case: United States v. Kros">296 F. Supp. 972, 979</a></span> (ED Pa. 1969). Moreover, this objective approach is the one favored by a majority of the commentators. In addition to the Proposed New Federal Criminal Code and the Model Penal Code, <i>supra,</i> n. 1, see Williams, The Defense of Entrapment and Related Problems in Criminal Prosecution, <span class="citation no-link">28 Fordham L. Rev. 399</span> (1959); Cowen, The Entrapment Doctrine in the Federal Courts, and Some State Court Comparisons, 49 J. Crim. L. C. &amp; P. S. 447 (1959); Donnelly, <i>supra,</i> n. 2; Comment, Entrapment in the Federal Courts, 1 U. San Francisco L. Rev. 177 (1966).</p>
<p>[4]  Some federal courts have ordered indictments for receipt, possession, or sale of contraband to be dismissed, upon a showing that Government agents themselves had supplied the contraband. See <i>United States</i> v. <i><span class="citation" data-id="306412"><a href="/opinion/306412/united-states-v-joseph-t-mcgrath/" aria-description="Citation for case: United States v. Joseph T. McGrath">McGrath, supra</a></span></i><i>; </i><i>Greene</i> v. <i>United States, supra</i><i>; </i><i>United States</i> v. <i>Bueno,</i> <span class="citation" data-id="298766"><a href="/opinion/298766/united-states-v-david-bueno/" aria-description="Citation for case: United States v. David Bueno">447 F. 2d 903</a></span> (CA5 1971); <i>United States</i> v. <i><span class="citation" data-id="1468773"><a href="/opinion/1468773/united-states-v-chisum/" aria-description="Citation for case: United States v. Chisum">Chisum, supra</a></span></i><i>; </i><i>United States</i> v. <i>Dillet,</i> <span class="citation" data-id="1457023"><a href="/opinion/1457023/united-states-v-dillet/" aria-description="Citation for case: United States v. Dillet">265 F. Supp. 980</a></span> (SDNY 1966). The same considerations obtain here.</p>

</div>
```

---

## GROUP: content/cases/United States v. Sandoval.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Sandoval"
type: case
citation: "200 F.3d 659 (2000)"
parallel_cite: 2000 Daily Journal DAR 907
neutral_cite: "2000 Cal. Daily Op. Serv. 581; 2000 U.S. App. LEXIS 805; 2000 WL 48991"
court: "U.S. Court of Appeals, Ninth Circuit"
court_level: coa
circuit: 9th
year: 2000
date_decided: 2000-01-24
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2000-01-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Sandoval
  varies_by_point: false
  scope_note: "Circuit split: the 10th Cir. reached a different conclusion in United States v. Ruckman, 806 F.2d 1471."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/767260/united-states-v-rodrigo-sandoval/"
  cluster_id: 767260
  opinion_id: 767260
  identity_checked: true
homes:
  - page: "[[Tents]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[California v. Ciraolo]]", "[[United States v. Gooch]]"]
aliases: ["United States v. Sandoval (9th Cir. 2000)", "United States v. Rodrigo Sandoval"]
tags: ["case", "fourth-amendment", "tents", "expectation-of-privacy", "public-land", "blm", "ninth-circuit"]
holding: "(Persuasive (outside circuit) — 9th Cir.) A reasonable expectation of privacy in a tent on public (BLM) land does not turn on whether the camper had permission to be there; denial of suppression reversed."
lake:
  record_id: United States v. Sandoval
  status: verified
  projected_at: 2026-07-06
---

# United States v. Sandoval

*200 F.3d 659 (9th Cir. 2000)* · U.S. Court of Appeals, Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a multi-site marijuana-grow investigation in Idaho, federal agents searching a grow on Bureau of Land Management (BLM) land entered a makeshift tent and found a medicine bottle bearing Sandoval's name. The tent was closed on all four sides and sat in heavy vegetation; the bottle could not be seen from outside. Sandoval moved to suppress, arguing the agents entered without a warrant. The district court denied the motion, holding that because the tent was on BLM land, Sandoval had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Issue
Whether a camper has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a closed tent on public (BLM) land, and whether that expectation depends on whether he had permission to be there.

## Rule
A camper has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a closed tent, and that expectation does not turn on whether he had permission to be on the public land. Applying the two-part *[[Katz v. United States|Katz]]* test (subjective expectation society recognizes as reasonable), the court held: "we do not believe the reasonableness of Sandoval's expectation of privacy turns on whether he had permission to camp on public land. Such a distinction would mean that a camper who overstayed his permit in a public campground would lose his Fourth Amendment rights, while his neighbor, whose permit had not expired, would retain those rights." — *United States v. Sandoval*, 200 F.3d 659, 661 (9th Cir. 2000). ^pin-661

## Application
The closed, four-sided tent in dense vegetation, the bottle's invisibility from outside, and Sandoval's leaving a personal prescription bottle inside all showed a subjective expectation of privacy that the government's "illegal activity / no permission" arguments did not defeat. Extending the circuit's tent cases (*[[LaDuke v. Nelson|LaDuke]]* — private property; *[[United States v. Gooch|Gooch]]* — public campground), the court held the expectation objectively reasonable even on BLM land, regardless of permission. The warrantless entry therefore violated the Fourth Amendment.

## Conclusion
The district court erred in denying suppression; the Ninth Circuit reversed Sandoval's conviction and [[Reading and Citing Cases#on-remand|remanded]] for a new trial.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- No negative treatment within the circuit. **Circuit split:** the court noted that the Tenth Circuit reached a different conclusion in *[[United States v. Ruckman]]*, 806 F.2d 1471 (10th Cir. 1986) (no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] for a person occupying a cave on public land). *Sandoval* anchors the rule that a closed tent on public land retains Fourth Amendment protection independent of the camper's permission to be there.

## Appears on
- [[Tents]] — *Key — Anchor*

## Sources
- *United States v. Sandoval*, 200 F.3d 659 (9th Cir. 2000) — https://www.courtlistener.com/opinion/767260/united-states-v-rodrigo-sandoval/ — pinpoint: 661.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1494dd9051cd3c90", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "200 F.3d 659 (2000)", "court": "U.S. Court of Appeals, Ninth Circuit", "neutral_cite": "2000 Cal. Daily Op. Serv. 581; 2000 U.S. App. LEXIS 805; 2000 WL 48991", "official_citation_present": true, "parallel_cite": "2000 Daily Journal DAR 907", "title": "United States v. Sandoval", "year": "2000"}}
{"assertion_id": "11d69fda096a1231", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "(Persuasive (outside circuit) — 9th Cir.) A reasonable expectation of privacy in a tent on public (BLM) land does not turn on whether the camper had permission to be there; denial of suppression reversed.", "title": "United States v. Sandoval"}}
{"assertion_id": "ea1f45b5bdbe5c44", "dimension": "support", "kind": "home_role", "locator": {"home": "Tents"}, "payload": {"home": "Tents", "role": "Key — Anchor", "title": "United States v. Sandoval"}}
{"assertion_id": "53b0c0bb68e54f0f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2000-01-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Sandoval", "field_i_validity": "good_law", "scope_note": "Circuit split: the 10th Cir. reached a different conclusion in United States v. Ruckman, 806 F.2d 1471.", "title": "United States v. Sandoval", "varies_by_point": "false"}}
{"assertion_id": "785e15d00a3d3315", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Sandoval"}}
```

### lake record — United States v. Sandoval

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Sandoval",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Rodrigo Sandoval",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Rodrigo SANDOVAL, Defendant-Appellant",
    "input_case_name": "United States v. Sandoval",
    "court": "U.S. Court of Appeals, Ninth Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2000-01-24",
    "year": 2000,
    "docket": null,
    "cluster_id": 767260,
    "lead_opinion_id": 767260,
    "sibling_ids": [
      767260
    ],
    "absolute_url": "/opinion/767260/united-states-v-rodrigo-sandoval/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "200 F.3d 659",
      "volume": "200",
      "reporter": "F.3d",
      "page": "659",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2000 Daily Journal DAR 907",
        "volume": "2000",
        "reporter": "Daily Journal DAR",
        "page": "907",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 Cal. Daily Op. Serv. 581",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. App. LEXIS 805",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "805",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 48991",
        "volume": "2000",
        "reporter": "WL",
        "page": "48991",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "200 F.3d 659",
        "volume": "200",
        "reporter": "F.3d",
        "page": "659",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Cal. Daily Op. Serv. 581",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Daily Journal DAR 907",
        "volume": "2000",
        "reporter": "Daily Journal DAR",
        "page": "907",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. App. LEXIS 805",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "805",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 48991",
        "volume": "2000",
        "reporter": "WL",
        "page": "48991",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "200 F.3d 659",
    "official_selection": {
      "court_class": "coa",
      "selected": "200 F.3d 659",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-661",
      "page": null,
      "quote": "--- # United States v. Sandoval *200 F.3d 659 (9th Cir. 2000)* \u00b7 U.S. Court of Appeals, Ninth Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a multi-site marijuana-grow investigation in Idaho, federal agents searching a grow on Bureau of Land Management (BLM) land entered a makeshift tent and found a medicine bottle bearing Sandoval's name. The tent was closed on all four sides and sat in heavy vegetation; the bottle could not be seen from outside. Sandoval moved to suppress, arguing the agents entered without a warrant. The district court denied the motion, holding that because the tent was on BLM land, Sandoval had no reasonable expectation of privacy. ## Issue Whether a camper has a reasonable expectation of privacy in a closed tent on public (BLM) land, and whether that expectation depends on whether he had permission to be there. ## Rule A camper has a reasonable expectation of privacy in a closed tent, and that expectation does not turn on whether he had permission to be on the public land. Applying the two-part *Katz* test (subjective expectation society recognizes as reasonable), the court held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-01-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Sandoval",
    "varies_by_point": false,
    "scope_note": "Circuit split: the 10th Cir. reached a different conclusion in United States v. Ruckman, 806 F.2d 1471.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Opinion Piedad Barajas-Avaslos",
          "cluster_id": 785295,
          "cite": [
            "359 F.3d 1204",
            "2004 U.S. App. LEXIS 4569",
            "2004 D.A.R. 3084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Piedad Barajas-Avaslos",
          "cluster_id": 787179,
          "cite": [
            "377 F.3d 1040",
            "2004 U.S. App. LEXIS 15362",
            "2004 WL 1656517"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiting v. State",
          "cluster_id": 1479286,
          "cite": [
            "885 A.2d 785",
            "389 Md. 334",
            "2005 Md. LEXIS 643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raphyal Crawford",
          "cluster_id": 781330,
          "cite": [
            "323 F.3d 700",
            "2003 WL 735531"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hughston",
          "cluster_id": 2285590,
          "cite": [
            "168 Cal. App. 4th 1062",
            "85 Cal. Rptr. 3d 890",
            "2008 Cal. App. LEXIS 2361"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nishi",
          "cluster_id": 5811207,
          "cite": [
            "207 Cal. App. 4th 954",
            "143 Cal. Rptr. 3d 882",
            "2012 WL 2870591",
            "2012 Cal. App. LEXIS 806"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Linton",
          "cluster_id": 2209670,
          "cite": [
            "812 A.2d 382",
            "356 N.J. Super. 255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leora Price v. Frank Vance Turner El Dorado County",
          "cluster_id": 774483,
          "cite": [
            "260 F.3d 1144",
            "2001 Cal. Daily Op. Serv. 7031",
            "2001 Daily Journal DAR 8607",
            "2001 U.S. App. LEXIS 18314",
            "2001 WL 909299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Naranjibhai Patel v. City of Los Angeles",
          "cluster_id": 2647586,
          "cite": [
            "738 F.3d 1058",
            "2013 WL 6768090",
            "2013 U.S. App. LEXIS 25609"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dellas",
          "cluster_id": 2453315,
          "cite": [
            "355 F. Supp. 2d 1095",
            "2005 U.S. Dist. LEXIS 1882",
            "2005 WL 310398"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Slavin",
          "cluster_id": 3145304,
          "cite": [
            "2011 IL App (2d) 100764"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. William R. Pippin",
          "cluster_id": 4433202,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Slavin",
          "cluster_id": 2437214,
          "cite": [
            "964 N.E.2d 150",
            "357 Ill. Dec. 787"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(767260) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 1,
        "triage_snippet_classified": 4
      },
      "lane2_top_cited": {
        "query": "cites:(767260)",
        "reviewed": 15,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 14,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(767260)",
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
    "complete_query": "cites:(767260)",
    "indexed_citing_opinions": 15,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 767260,
        "count": 15,
        "count_source": "search"
      }
    ],
    "citation_count": 27,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-sandoval.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 15,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 767260,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 452994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 480405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 654273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 744560,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T02:48:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:52:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Sandoval

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b698-4">
  MICHAEL DALY HAWKINS, Circuit Judge:
 </author>
<p id="b698-5">
  Rodrigo Sandoval appeals his conviction on drug and conspiracy charges, alleging that the district court erred in denying his motion to suppress evidence obtained during the search of a tent. Because we agree that the district court erred in denying Sandoval’s motion, we reverse his conviction and remand for a new trial.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b698-6">
  In early 1997, state and federal officials began an investigation into marijuana growing in Idaho that led to the seizure of marijuana from sixteen growing sites (“grows”) and the indictment of 18 defendants, including Sandoval. During the seizure of one of the grows, which was located on Bureau of Land Management (“BLM”) land, federal agents entered a makeshift tent and found a medicine bottle bearing Sandoval’s name. The tent was closed on all four sides, and the bottle could not be seen from outside. Before trial, Sandoval filed a motion to suppress, alleging that agents had entered the tent without a search warrant and that the evidence was therefore inadmissible. The district court denied the motion, holding that because the tent was on BLM land, Sandoval did not have a reasonable expectation of privacy. Therefore, the court concluded, a search warrant was not required, and the evidence was admissible.
 </p>
<p id="b698-7">
  We review de novo the district court’s denial of a motion to suppress.
  <em>
   See United States v. Kemmish,
  </em>
  <span class="citation" data-id="6952928"><a href="/opinion/7049571/united-states-v-kemmish/#939" aria-description="Citation for case: United States v. Kemmish">120 F.3d 937, 939</a></span> (9th Cir.1997). We review the trial court’s factual findings for clear error.
  <em>
   See <span class="citation" data-id="6952928"><a href="/opinion/7049571/united-states-v-kemmish/" aria-description="Citation for case: United States v. Kemmish">id.</a></span>
  </em>
</p>
<p id="b698-8">
  To determine whether a warrant-less search violates the Fourth Amendment, we must ask two questions: “[Fjirst, has the individual manifested a subjective expectation of privacy in the object of the challenged search? Second, is society willing to recognize that expectation as reasonable?”
  <em>
   California v. Ciraolo,
  </em>
  <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">476 U.S. 207, 211</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. 1809</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">90 L.Ed.2d 210</a></span> (1986) (citing
  <em>
   Katz v. United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 360-61</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967) (Harlan, J., concurring)). Only if both the subjective and objective tests are met can we find that a Fourth Amendment interest has been violated.
 </p>
<p id="b698-12">
  In this case, several factors indicate that Sandoval had a subjective expectation of privacy. First, the tent was located in an area that was heavily covered by vegetation and virtually impenetrable. Second, the makeshift tent was closed on all four sides, and the bottle could not be seen from outside. Third, Sandoval left a prescription medicine bottle inside the tent; a person who lacked a subjective expectation of privacy would likely not leave such an item lying around. The government counters that Sandoval could not have had a subjective expectation of privacy because he was growing marijuana illegally and was not authorized to camp on BLM land. However, we have previously rejected the argument that a person lacks a subjective expectation of privacy simply because he is engaged in illegal activity or could have expected the police to intrude on his privacy.
  <em>
   See United States v. Gooch,
  </em>
  <span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/#677" aria-description="Citation for case: United States v. Kenneth D. Gooch">6 F.3d 673, 677</a></span> (9th Cir.1993). “According to this view, no lawbreaker would have a subjective expectation of privacy in any place because the expectation of arrest is always imminent.”
  <em>
   <span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/" aria-description="Citation for case: United States v. Kenneth D. Gooch">Id.</a></span>
  </em>
</p>
<p id="b698-13">
  Sandoval’s expectation of privacy was also objectively reasonable. In
  <em>
   LaDuke v. Nelson,
  </em>
  <span class="citation" data-id="452994"><a href="/opinion/452994/charles-laduke-v-alan-c-nelson-etc/" aria-description="Citation for case: Charles Laduke v. Alan C. Nelson, Etc.">762 F.2d 1318</a></span>, 1326 n. 11, 1332 n. 19 (9th Cir.1985), we held that a person can have an objectively reasonable expectation of privacy in a tent on private property. In
  <em>
   Gooch,
  </em>
  <span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/#677" aria-description="Citation for case: United States v. Kenneth D. Gooch">6 F.3d at 677</a></span>, we extended that holding to find a reasonable expectation of privacy in a tent on a public campground. Here, the tent was
  <span citation-index="1" class="star-pagination" label="661"> 
   *661
   </span>
  located on BLM land, not on a public campground, and it is unclear whether Sandoval had permission to be there.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  However, we do not believe the reasonableness of Sandoval’s expectation of privacy turns on whether he had permission to camp on public land.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Such a distinction would mean that a camper who overstayed his permit in a public campground would lose his Fourth Amendment rights, while his neighbor, whose permit had not expired, would retain those rights.
 </p>
<p id="b699-4">
  We note that in
  <em>
   Zimmerman v. Bishop Estate,
  </em>
  <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/#787" aria-description="Citation for case: Zimmerman v. Bishop Estate">25 F.3d 784, 787-88</a></span> (9th Cir.1994), this court held that a squatter in a residential home did not have an objectively reasonable expectation of privacy because he had no legal right to occupy the home. However, we find
  <em>
   <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/" aria-description="Citation for case: Zimmerman v. Bishop Estate">Zimmerman</a></span>
  </em>
  distinguishable on two grounds. First, camping on public land, even without permission, is far different from squatting in a private residence. A private residence is easily identifiable and clearly off-limits, whereas public land is often unmarked and may appear to be open to camping. Thus, we think it much more likely that society would recognize an expectation of privacy for the camper on public land than for the squatter in a private residence.
 </p>
<p id="b699-5">
  Second, the facts of
  <em>
   <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/" aria-description="Citation for case: Zimmerman v. Bishop Estate">Zimmerman</a></span>
  </em>
  contrast starkly with the facts presented here. In
  <em>
   <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/" aria-description="Citation for case: Zimmerman v. Bishop Estate">Zimmerman</a></span>,
  </em>
  the appellants were asked on several occasions over the course of eight months to vacate the premises, and there was “no dispute of material fact regarding the ownership of the property or whether the [owners] acquiesced in the presence of the [appellants].”
  <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/#788" aria-description="Citation for case: Zimmerman v. Bishop Estate"><em>
   Id.
  </em>
  at 788</a></span>. By contrast, though Sandoval did not obtain permission to camp on BLM land, he was never instructed to vacate or risk eviction, and the record does not establish any applicable rules, regulations or practices concerning recreational or other use of BLM land. Indeed, whether Sandoval was legally permitted to be on the land was a matter in dispute.
 </p>
<p id="b699-10">
  Because Sandoval had a subjective expectation of privacy and because that expectation was objectively reasonable, we conclude that the district court erred in denying Sandoval’s motion to suppress. His conviction is REVERSED, and the case is REMANDED for a new trial.
 </p>



<div class="footnotes"><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b698-9">
   . Sandoval makes several other claims that we have addressed in a separate, unpublished memorandum disposition filed contemporaneously herewith.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b699-6">
   . The district court assumed that Sandoval lacked authority to erect a tent on BLM land. However, it is unclear whether explicit permission was required.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b699-17">
   . The Tenth Circuit reached a different conclusion in
   <em>
    United States v. Ruckman,
   </em>
   <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1472" aria-description="Citation for case: United States v. Frank William Ruckman">806 F.2d 1471, 1472-73</a></span> (10th Cir.1986). However, we find Judge McKay's dissent in that case more persuasive.
   <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1475" aria-description="Citation for case: United States v. Frank William Ruckman"><em>
    See id.
   </em>
   at 1475-79</a></span> (McKay, J., dissenting).
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/United States v. Santana.md  (`case`, 7 assertions)

### content_page

```
---
title: "United States v. Santana"
type: case
citation: "427 U.S. 38 (1976)"
parallel_cite: "96 S. Ct. 2406; 49 L. Ed. 2d 300"
neutral_cite: 1976 U.S. LEXIS 71
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-24
docket: 75-19
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Santana
  varies_by_point: false
  scope_note: "Hot-pursuit reading for misdemeanor pursuits limited by Lange v. California (2021) — no longer categorical; the threshold/public-place and felony hot-pursuit holdings are intact."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109504/united-states-v-santana/"
  cluster_id: 109504
  opinion_id: 109504
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Key — Anchor"
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Key — Anchor"
  - page: "[[Curtilage]]"
    role: "Related — threshold/public-place line"
related: ["[[United States v. Watson]]", "[[Payton v. New York]]", "[[Lange v. California]]", "[[Hester v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-in-the-home", "hot-pursuit", "exigent-circumstances", "doorway", "public-place"]
holding: "A suspect standing in her own doorway/threshold is in a 'public' place for Fourth Amendment purposes; she cannot defeat a lawful arrest…"
lake:
  record_id: United States v. Santana
  status: verified
  projected_at: 2026-07-06
---

# United States v. Santana

*427 U.S. 38 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an undercover officer's controlled heroin buy through an intermediary who took marked money to "Mom Santana's" house, officers arrested the intermediary (who said "Mom has the money") and drove to Santana's house. They saw Santana standing in her doorway holding a brown paper bag, pulled up, got out shouting "police," and displayed identification. Santana retreated into the vestibule; the officers followed through the open door, caught her, and heroin packets fell from the bag. Marked money was found on her. The District Court suppressed the evidence; the Government appealed.

## Issue
Whether police with probable cause may make a warrantless arrest of a suspect standing in her doorway, and whether they may follow her into the house when she retreats, on a hot-pursuit theory.

## Rule
A suspect standing in her own doorway is in a "public" place for arrest purposes: "While it may be true that under the common law of property the threshold of one's dwelling is 'private,' . . . it is nonetheless clear that under the cases interpreting the Fourth Amendment Santana was in a 'public' place. She was not in an area where she had any expectation of privacy. . . . She was not merely visible to the public but was as exposed to public view, speech, hearing, and touch as if she had been standing completely outside her house." — 427 U.S. at 42. ^pin-42

And a suspect cannot defeat a lawful public arrest by retreating indoors; [[Exigent Circumstances and Hot Pursuit|hot pursuit]] justifies the warrantless entry: "We thus conclude that a suspect may not defeat an arrest which has been set in motion in a public place, and is therefore proper under *Watson*, by the expedient of escaping to a private place." — 427 U.S. at 43. ^pin-43

## Application
Santana was standing in her open doorway with the bag when officers who had probable cause approached to arrest her; she was therefore in a public place and the arrest was proper under [[United States v. Watson]]. When she retreated into the vestibule, the officers' immediate pursuit was a true [[Exigent Circumstances and Hot Pursuit|hot pursuit]] that justified the warrantless entry. The heroin that fell from the bag and the marked money found on her were lawfully seized incident to that arrest.

## Conclusion
The warrantless entry and arrest were valid; the Supreme Court reversed the suppression order.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Santana* establishes the doorway-as-public-place rule and the hot-pursuit entry. [[Payton v. New York]] (1980) later held that a warrantless arrest **inside** the home requires a warrant absent [[Exigent Circumstances and Hot Pursuit|exigency]], and [[Lange v. California]] (2021) held that pursuit of a fleeing **misdemeanant** is not a categorical [[Exigent Circumstances and Hot Pursuit|exigency]] — but neither disturbs *Santana*'s threshold/felony hot-pursuit holding.

## Appears on
- [[Arrest in the Home]] — *Key — Anchor*
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Anchor*

## Sources
- *United States v. Santana*, 427 U.S. 38 (1976) — https://www.courtlistener.com/opinion/109504/united-states-v-santana/ — pinpoints: 42, 43 (parallel 96 S. Ct. 2406).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "752d105867cdfb7b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "427 U.S. 38 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 71", "official_citation_present": true, "parallel_cite": "96 S. Ct. 2406; 49 L. Ed. 2d 300", "title": "United States v. Santana", "year": "1976"}}
{"assertion_id": "3a094c8cf8f78ca0", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Related — threshold/public-place line", "title": "United States v. Santana"}}
{"assertion_id": "7557efe23ce0b9d3", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Key — Anchor", "title": "United States v. Santana"}}
{"assertion_id": "9da29d5a40149920", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspect standing in her own doorway/threshold is in a 'public' place for Fourth Amendment purposes; she cannot defeat a lawful arrest…", "title": "United States v. Santana"}}
{"assertion_id": "d112279612fde589", "dimension": "support", "kind": "home_role", "locator": {"home": "Exigent Circumstances and Hot Pursuit"}, "payload": {"home": "Exigent Circumstances and Hot Pursuit", "role": "Key — Anchor", "title": "United States v. Santana"}}
{"assertion_id": "14f68ac29dc4673d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Santana", "field_i_validity": "good_law", "scope_note": "Hot-pursuit reading for misdemeanor pursuits limited by Lange v. California (2021) — no longer categorical; the threshold/public-place and felony hot-pursuit holdings are intact.", "title": "United States v. Santana", "varies_by_point": "false"}}
{"assertion_id": "39a3902cf89ba3c3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Santana"}}
```

### lake record — United States v. Santana

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Santana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Santana",
    "case_name_short": "Santana",
    "case_name_full": "UNITED STATES v. SANTANA Et Al.",
    "input_case_name": "United States v. Santana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-24",
    "year": 1976,
    "docket": "75-19",
    "cluster_id": 109504,
    "lead_opinion_id": 109504,
    "sibling_ids": [
      109504,
      9426490,
      9426491,
      9426492,
      9426493
    ],
    "absolute_url": "/opinion/109504/united-states-v-santana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "427 U.S. 38",
      "volume": "427",
      "reporter": "U.S.",
      "page": "38",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2406",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 300",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "300",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 71",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "427 U.S. 38",
        "volume": "427",
        "reporter": "U.S.",
        "page": "38",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2406",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 300",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "300",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 71",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "427 U.S. 38",
    "official_selection": {
      "court_class": "scotus",
      "selected": "427 U.S. 38",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-42",
      "page": null,
      "quote": "and displayed identification. Santana retreated into the vestibule; the officers followed through the open door, caught her, and heroin packets fell from the bag. Marked money was found on her. The District Court suppressed the evidence; the Government appealed. ## Issue Whether police with probable cause may make a warrantless arrest of a suspect standing in her doorway, and whether they may follow her into the house when she retreats, on a hot-pursuit theory. ## Rule A suspect standing in her own doorway is in a",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-43",
      "page": null,
      "quote": "We thus conclude that a suspect may not defeat an arrest which has been set in motion in a public place, and is therefore proper under *Watson*, by the expedient of escaping to a private place.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Santana",
    "varies_by_point": false,
    "scope_note": "Hot-pursuit reading for misdemeanor pursuits limited by Lange v. California (2021) \u2014 no longer categorical; the threshold/public-place and felony hot-pursuit holdings are intact.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 4406527,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Allen Decker v. State of Indiana",
          "cluster_id": 2745993,
          "cite": [
            "19 N.E.3d 368",
            "2014 Ind. App. LEXIS 515",
            "2014 WL 5461790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lujano",
          "cluster_id": 2721019,
          "cite": [
            "229 Cal. App. 4th 175",
            "2014 D.A.R. 11",
            "176 Cal. Rptr. 3d 534",
            "2014 Cal. App. LEXIS 771"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Hogan v. City of Corpus Christi, Texas",
          "cluster_id": 1033766,
          "cite": [
            "722 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Agbodjan",
          "cluster_id": 8716573,
          "cite": [
            "871 F. Supp. 2d 95",
            "2012 WL 2552140"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Finnicum",
          "cluster_id": 890584,
          "cite": [
            "206 P.3d 501",
            "147 Idaho 137",
            "2009 Ida. App. LEXIS 35"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steagald v. United States",
          "cluster_id": 110464,
          "cite": [
            "68 L. Ed. 2d 38",
            "101 S. Ct. 1642",
            "451 U.S. 204",
            "1981 U.S. LEXIS 89",
            "49 U.S.L.W. 4418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segura v. United States",
          "cluster_id": 111259,
          "cite": [
            "82 L. Ed. 2d 599",
            "104 S. Ct. 3380",
            "468 U.S. 796",
            "1984 U.S. LEXIS 150",
            "52 U.S.L.W. 5128"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 1228080,
          "cite": [
            "729 P.2d 839",
            "43 Cal. 3d 171",
            "233 Cal. Rptr. 404",
            "1987 Cal. LEXIS 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Berkowitz",
          "cluster_id": 557342,
          "cite": [
            "927 F.2d 1376",
            "1991 U.S. App. LEXIS 4135",
            "1991 WL 33079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramsey",
          "cluster_id": 109675,
          "cite": [
            "52 L. Ed. 2d 617",
            "97 S. Ct. 1972",
            "431 U.S. 606",
            "1977 U.S. LEXIS 101"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanton v. Sims",
          "cluster_id": 2641101,
          "cite": [
            "187 L. Ed. 2d 341",
            "134 S. Ct. 3",
            "2013 U.S. LEXIS 7773",
            "82 U.S.L.W. 4003",
            "571 U.S. 3",
            "24 Fla. L. Weekly Fed. S 473",
            "2013 WL 5878007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Henning",
          "cluster_id": 1060855,
          "cite": [
            "975 S.W.2d 290",
            "1998 Tenn. LEXIS 370",
            "1998 WL 324318"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Johnson",
          "cluster_id": 773999,
          "cite": [
            "256 F.3d 895",
            "2001 Daily Journal DAR 7479",
            "2001 Cal. Daily Op. Serv. 6099",
            "2001 U.S. App. LEXIS 16092",
            "2001 WL 817633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chew v. Gates",
          "cluster_id": 7029311,
          "cite": [
            "27 F.3d 1432",
            "94 Cal. Daily Op. Serv. 4853",
            "94 Daily Journal DAR 9043",
            "1994 U.S. App. LEXIS 16020",
            "1994 WL 280292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Louis Lalonde v. County of Riverside, Robert Moquin, and Jason Horton, Opinion",
          "cluster_id": 767803,
          "cite": [
            "204 F.3d 947",
            "2000 Daily Journal DAR 2031",
            "2000 Cal. Daily Op. Serv. 1433",
            "2000 U.S. App. LEXIS 2778",
            "2000 WL 217552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frierson",
          "cluster_id": 1434797,
          "cite": [
            "599 P.2d 587",
            "25 Cal. 3d 142",
            "158 Cal. Rptr. 281",
            "1979 Cal. LEXIS 302"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Sangineto-Miranda, (87-5667) Luray Betts, (87-5668) Enrique Vargas, (87-5711) & Benjamin Nelson, (87-5712)",
          "cluster_id": 513263,
          "cite": [
            "859 F.2d 1501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Joe Whitten, John Elmer Gaiefsky, Jack Wayne Gish, Richard Lawrence Shimel",
          "cluster_id": 418069,
          "cite": [
            "706 F.2d 1000",
            "13 Fed. R. Serv. 384",
            "1983 U.S. App. LEXIS 27369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 1142777,
          "cite": [
            "666 P.2d 802",
            "295 Or. 227",
            "1983 Ore. LEXIS 1342"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Troy Cooper v. C. J. Fitzharris",
          "cluster_id": 360922,
          "cite": [
            "586 F.2d 1325",
            "1978 U.S. App. LEXIS 7347"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. Luna County",
          "cluster_id": 4321034,
          "cite": [
            "841 F.3d 895",
            "96 Fed. R. Serv. 3d 126",
            "2016 U.S. App. LEXIS 20466",
            "2016 WL 6694533"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTgwMDUxMjAwMDAwJnM9Mjk3NTMzNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109504+OR+9426490+OR+9426491+OR+9426492+OR+9426493%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzAmcz0xODgxNDk2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109504+OR+9426490+OR+9426491+OR+9426492+OR+9426493%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493)",
        "reviewed": 17,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 17,
        "triage_read": 0,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493)",
    "indexed_citing_opinions": 871,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109504,
        "count": 774,
        "count_source": "search"
      },
      {
        "opinion_id": 9426490,
        "count": 113,
        "count_source": "search"
      },
      {
        "opinion_id": 9426491,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426492,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426493,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1384,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-santana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyNDA2NjYmcz05Mzk1NjYwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109504+OR+9426490+OR+9426491+OR+9426492+OR+9426493%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109504,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 106850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 109186,
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
    "date_created": "2026-07-06T02:52:01Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:52:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:52:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:59:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:52:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Santana

```
<div>
<center><b><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U.S. 38</a></span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
SANTANA ET AL.</h1></center>
<center>No. 75-19.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 27, 1976.</center>
<center>Decided June 24, 1976.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE THIRD CIRCUIT.
<p><span class="star-pagination">*39</span> <i>Frank H. Easterbrook</i> argued the cause for the United States <i>pro hac vice.</i> With him on the brief were <i>Solicitor General Bork, Assistant Attorney General Thornburgh, Deputy Solicitor General Frey,</i> and <i>Peter M. Shannon, Jr.</i></p>
<p><i>Dennis H. Eisman</i> argued the cause for respondent Santana. With him on the brief was <i>Gerald A. Stein.</i><sup>[*]</sup></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p></p>
<h2>I</h2>
<p>On August 16, 1974, Michael Gilletti, an undercover officer with the Philadelphia Narcotics Squad arranged a heroin "buy" with one Patricia McCafferty (from whom he had purchased narcotics before). McCafferty told him it would cost $115 "and we will go down to Mom Santana's for the dope."</p>
<p>Gilletti notified his superiors of the impending transaction, recorded the serial numbers of $110 (<i>sic</i>) in marked bills, and went to meet McCafferty at a prearranged location. She got in his car and directed him to drive to 2311 North Fifth Street, which, as she had <span class="star-pagination">*40</span> previously informed him, was respondent Santana's residence.</p>
<p>McCafferty took the money and went inside the house, stopping briefly to speak to respondent Alejandro who was sitting on the front steps. She came out shortly afterwards and got into the car. Gilletti asked for the heroin; she thereupon extracted from her bra several glassine envelopes containing a brownish-white powder and gave them to him.</p>
<p>Gilletti then stopped the car, displayed his badge, and placed McCafferty under arrest. He told her that the police were going back to 2311 North Fifth Street and that he wanted to know where the money was. She said, "Mom has the money." At this point Sergeant Pruitt and other officers came up to the car. Gilletti showed them the envelope and said "Mom Santana has the money." Gilletti then took McCafferty to the police station.</p>
<p>Pruitt and the others then drove approximately two blocks back to 2311 North Fifth Street. They saw Santana standing in the doorway of the house<sup>[1]</sup> with a brown paper bag in her hand. They pulled up to within 15 feet of Santana and got out of their van, shouting "police," and displaying their identification. As the officers approached, Santana retreated into the vestibule of her house.</p>
<p>The officers followed through the open door, catching her in the vestibule. As she tried to pull away, the bag tilted and "two bundles of glazed paper packets with a white powder" fell to the floor. Respondent <span class="star-pagination">*41</span> Alejandro tried to make off with the dropped envelopes but was forcibly restrained. When Santana was told to empty her pockets she produced $135, $70 of which could be identified as Gilletti's marked money. The white powder in the bag was later determined to be heroin.</p>
<p>An indictment was filed in the United States District Court for the Eastern District of Pennsylvania charging McCafferty with distribution of heroin, in violation of <span class="citation no-link">21 U. S. C. § 841</span>, and respondents with possession of heroin with intent to distribute in violation of the same section. McCafferty pleaded guilty. Santana and Alejandro moved to suppress the heroin and money found during and after their arrests.</p>
<p>The District Court granted respondents' motion.<sup>[2]</sup> In an oral opinion the court found that "[t]here was strong probable cause that Defendant Santana had participated in the transaction with Defendant McCafferty." However, the court continued:</p>
<blockquote>"One of the police officers . . . testified that the mission was to arrest Defendant Santana. Another police officer testified that the mission was to recover the bait money. Either one would require a warrant, one a warrant of arrest under ordinary circumstances and one a search warrant."</blockquote>
<p>The court further held that Santana's "reentry from the doorway into the house" did not support allowing the police to make a warrantless entry into the house on the grounds of "hot pursuit," because it took "hot pursuit" to mean "a chase in and about public streets." The court did find, however, that the police <span class="star-pagination">*42</span> acted under "extreme emergency" conditions. The Court of Appeals affirmed this decision without opinion.</p>
<p></p>
<h2>II</h2>
<p>In <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), we held that the warrantless arrest of an individual in a public place upon probable cause did not violate the Fourth Amendment. Thus the first question we must decide is whether, when the police first sought to arrest Santana, she was in a public place.</p>
<p>While it may be true that under the common law of property the threshold of one's dwelling is "private," as is the yard surrounding the house, it is nonetheless clear that under the cases interpreting the Fourth Amendment Santana was in a "public" place. She was not in an area where she had any expectation of privacy. "What a person knowingly exposes to the public, even in his own house or office, is not a subject of Fourth Amendment protection." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967). She was not merely visible to the public but was as exposed to public view, speech, hearing, and touch as if she had been standing completely outside her house. <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924). Thus, when the police, who concededly had probable cause to do so, sought to arrest her, they merely intended to perform a function which we have approved in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i></p>
<p>The only remaining question is whether her act of retreating into her house could thwart an otherwise proper arrest. We hold that it could not. In <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), we recognized the right of police, who had probable cause to believe that an armed robber had entered a house a few minutes before, to make a warrantless entry to arrest the robber and to search for weapons. This case, involving a true "hot <span class="star-pagination">*43</span> pursuit,"<sup>[3]</sup> is clearly governed by <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Warden</a></span>;</i> the need to act quickly here is even greater than in that case while the intrusion is much less. The District Court was correct in concluding that "hot pursuit" means some sort of a chase, but it need not be an extended hue and cry "in and about [the] public streets." The fact that the pursuit here ended almost as soon as it began did not render it any the less a "hot pursuit" sufficient to justify the warrantless entry into Santana's house. Once Santana saw the police, there was likewise a realistic expectation that any delay would result in destruction of evidence. See <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#35" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 35</a></span> (1970). Once she had been arrested the search, incident to that arrest, which produced the drugs and money was clearly justified. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 762-763</a></span> (1969).</p>
<p>We thus conclude that a suspect may not defeat an arrest which has been set in motion in a public place, and is therefore proper under <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>,</i> by the expedient of escaping to a private place. The judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE WHITE, concurring.</p>
<p>It is not disputed here that the officers had probable cause to arrest Santana and to believe that she was in the house. In these circumstances, a warrant was not required to enter the house to make the arrest, at least <span class="star-pagination">*44</span> where entry by force was not required. This has been the longstanding statutory or judicial rule in the majority of jurisdictions in the United States, see ALI, A Model Code of Pre-arraignment Procedure 306-314, 696-697 (1975), and has been deemed consistent with state constitutions, as well as the Fourth Amendment. It is also the Institute's recommended rule. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Id.,</a></span></i> § 120.6. I agree with the Court that the arrest here did not violate the Fourth Amendment.</p>
<p>My Brother MARSHALL, <i>post,</i> p. 45, and <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 433</a></span> (1976) (dissenting opinion), would reinterpret the Fourth Amendment to sweep aside this widely held rule and to establish a constitutional standard requiring warrants for arrests except where exigent circumstances clearly exist. The States are, of course, free to limit warrantless arrests, as is Congress; but I would not impose his suggested nationwide edict, founded as it is on a belief in the superior wisdom of the Members of this Court and their power to divine that the country's practice to this date with respect to arrests is unreasonable within the meaning of the Fourth Amendment.</p>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE STEWART joins, concurring.</p>
<p>When Officer Gilletti placed McCafferty under arrest, the police had sufficient information to obtain a warrant for the arrest of Santana in her home. It is therefore important to note that their failure to obtain a warrant at that juncture was both (a) a justifiable police decision, and (b) even if not justifiable, harmless.</p>
<p>The decision was justified by the significant risk that the marked money would no longer be in Santana's possession if the police waited until a warrant could be obtained. The failure to seek a warrant was harmless <span class="star-pagination">*45</span> because it would have been proper to keep the Santana residence under surveillance while the warrant was being sought; since she ventured into plain view, a warrantless arrest would have been justified before the warrant could have been procured.</p>
<p>I therefore join the opinion of the Court.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>Earlier this Term, I expressed the view that, in the absence of exigent circumstances, the police may not arrest a suspect without a warrant. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 433</a></span> (1976) (dissenting opinion). For this reason, I cannot join either the opinion of the Court or that of MR. JUSTICE WHITE, each of which disregards whether exigency justified the police decision to approach Santana's home without a warrant for the purpose of arresting her. Nor can I accept MR. JUSTICE STEVENS' approach, for while acknowledging that some notion of exigency must be asserted to justify the police conduct in this case, MR. JUSTICE STEVENS fails to consider that the exigency present in this case was produced solely by police conduct. I would remand the case to allow the District Court to determine whether that police conduct was justifiable or was solely an attempt to circumvent the warrant requirement.</p>
<p>The Court declines today to settle the oft-reserved question of whether and under what circumstances a police officer may enter the home of a suspect in order to make a warrantless arrest. <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson, supra,</a></span></i> at 418 n. 6; <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span>, 113 n. 13 (1975); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480-481</a></span> (1971); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958). Seizing upon the fortuity that Santana was standing in her doorway when the police <span class="star-pagination">*46</span> approached her home for the purpose of entering and arresting her, the Court ignores MR. JUSTICE WHITE'S repeated advocacy of the common-law rule on warrantless entries, <i>ante,</i> p. 43; <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#511" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 511-512, n. 1</a></span> (WHITE, J., concurring and dissenting),<sup>[1]</sup> and treats this case as a simple application of <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i></p>
<p>It is somewhat more than that, for the Court takes the opportunity to refine the contours of that decision. Thus, if I correctly read the Court's citation to the "open fields" doctrine of <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924), the Court holds that the police may enter upon private property to make warrantless arrests of persons who are in plain view and outdoors; and the Court applies that doctrine today to persons who are arguably within their homes but who are "as exposed" to the public as if they were outside. But the Court's encroachment upon the reserved question is limited. <span class="star-pagination">*47</span> Thus, the Court's citation of <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), does not suggest that a plain view of a suspect is alone sufficient to justify warrantless entry and seizure in the home. Indeed, the Court's rejection of sight alone as a basis for warrantless entry and arrest is made patent, in MR. JUSTICE STEWART'S phrase, by negative implication from the Court's need to elaborate a hot pursuit justification for the police following Santana into her home. Cf. <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 480-481</a></span>. Presumably, if plain view were the touchstone, Santana would have been just as liable to warrantless arrest as she retreated several feet inside her open door as she was when standing in the doorway.</p>
<p>The Court's doctrine, then, appears <i>sui generis,</i> useful only in arresting persons who are "as exposed to public view, speech, hearing, and touch," <i>ante,</i> at 42, as though in the unprotected outdoors. Narrow though it may be, however, the Court's approach does not depend on whether exigency justifies an arrest on private property, and thus I cannot join it.</p>
<p>MR. JUSTICE STEVENS focuses on what I believe to be the right question in this casewhether there were exigent circumstancesand reaches an affirmative answer because he finds a "significant risk that the marked money would no longer be in Santana's possession if the police waited until a warrant could be obtained." <i>Ante,</i> at 44. I agree that there were exigent circumstances in this case. McCafferty was arrested a block and a half down the street from Santana's home. Although the arresting officers did not see anyone in Santana's home watching the arrest, App. 16, one officer testified: "We were a block and a half from her home when the arrest was made. I am sure that the word would have been back within a matter of seconds or minutes." <i>Id.,</i> at 51. That is undoubtedly a reasonable conclusion to draw <span class="star-pagination">*48</span> from the facts of the arrest; and the danger that the evidence would be destroyed and the suspects gone before a warrant could be obtained would ordinarily justify the police's quick return to Santana's home and the warrantless entry and arrest. If that is the basis of the "significant risk" to which MR. JUSTICE STEVENS refers, I have no difference with him on that score.<sup>[2]</sup></p>
<p>I do not believe, however, that these exigent circumstances automatically validate Santana's arrest. The exigency that justified the entry and arrest was solely a product of police conduct. Had Officer Gilletti driven McCafferty to a more remote location before arresting her, it appears that no exigency would have been created by the arrest; in such an event a warrant would have been necessary, in my view, before Santana could have been arrested. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S., at 433</a></span> (MARSHALL, J., dissenting). It is not apparent on this record why Officer Gilletti arrested McCafferty so close to Santana's home when the arresting officers were clearly aware that such a nearby arrest would necessitate the prompt arrest of Santana. App. 51. While a police decision that the time is right to arrest a suspect should properly be given great deference, cf. <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#310" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 310</a></span> (1966), the power to arrest is an awesome one and is subject to abuse. An arrest may permit a search of premises incident to the arrest, a search that otherwise could be carried out only upon probable cause and pursuant to a search warrant. Likewise, an arrest in circumstances such as those presented here may create exigency that may justify a search <span class="star-pagination">*49</span> or another arrest. When an arrest is so timed that it is no more than an attempt to circumvent the warrant requirement, I would hold the subsequent arrest or search unlawful. See <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#469" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 469-471</a></span>; <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#35" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 35</a></span> (1970); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#767" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 767</a></span> (1969); <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span>, 226 and 230 (1960); <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#82" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 82</a></span> (1950) (Frankfurter, J., dissenting); <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#467" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 467</a></span> (1932). Accordingly, I would remand this case for consideration of whether the police decision to arrest McCafferty a block and a half from Santana's home was for the sole purpose of creating the exigent circumstances that otherwise would justify Santana's subsequent arrest.<sup>[3]</sup></p>
<h2>NOTES</h2>
<p>[*]  <i>Frank Carrington, Wayne W. Schmidt, Vernon S. Gill,</i> and <i>William K. Lambie</i> filed a brief for the Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  An Officer Strohm testified that he recognized Santana, whom he had seen before. He also indicated that she was standing directly in the doorwayone step forward would have put her outside, one step backward would have put her in the vestibule of her residence.</p>
<p>[2]  It is not apparent on what grounds respondent Alejandro had standing to protest the seizures. However, the Government did not raise this issue below and consequently we do not reach it.</p>
<p>[3]  <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Warden</a></span></i> was based upon the "exigencies of the situation," <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 298</a></span>, and did not use the term "hot pursuit" or even involve a "hot pursuit" in the sense that that term would normally be understood. That phrase first appears in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 16 n. 7 (1948), where it was recognized that some element of a chase will usually be involved in a "hot pursuit" case.</p>
<p>[1]  MR. JUSTICE WHITE would have us bequeath our duty to interpret the Constitution to the States and Congress. As I said in response to a similar argument in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>:</i>
</p>
<p>"[T]he doctrine of deference that the Court invokes is contrary to the principles of constitutional analysis practiced since <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137</a></span> (1803). . . . [I]t is well settled that the mere existence of statutes or practice, even of long standing, is no defense to an unconstitutional practice. `[N]o one acquires a vested or protected right in violation of the Constitution by long use, even when that span of time covers our entire national existence and indeed predates it.' <i>Walz</i> v. <i>Tax Comm'n,</i> <span class="citation" data-id="9841980"><a href="/opinion/108135/walz-v-tax-commn-of-city-of-new-york/#678" aria-description="Citation for case: Walz v. Tax Comm&#x27;n of City of New York">397 U. S. 664, 678</a></span> (1970). See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Roe</i> v. <i>Wade,</i> <span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">410 U. S. 113</a></span> (1973); <i>Furman</i> v. <i>Georgia,</i> <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">408 U. S. 238</a></span> (1972); <i>Reynolds</i> v. <i>Sims,</i> <span class="citation" data-id="9422829"><a href="/opinion/106850/reynolds-v-sims/" aria-description="Citation for case: Reynolds v. Sims">377 U. S. 533</a></span> (1964). Our function in constitutional cases is weightier than the Court today suggests: where reasoned analysis shows a practice to be constitutionally deficient, our obligation is to the Constitution, not the Congress." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#443" aria-description="Citation for case: United States v. Watson">423 U. S., at 443</a></span> (dissenting opinion) (footnote omitted).</p>
<p>[2]  I assume that MR. JUSTICE STEVENS is not suggesting that exigent circumstances justifying a warrantless search or arrest are always presentregardless of whether the suspect is aware the police are on his trailwhenever police have probable cause to believe the suspect is in possession of evidence. Cf. <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30</a></span> (1970).</p>
<p>[3]  Because I cannot agree that police may arrest a suspect in a public place solely upon probable cause, I cannot agree with MR. JUSTICE STEVENS that any police error in deciding to return to Santana's home for the purpose of entering and arresting her was harmless.</p>

</div>
```

---
