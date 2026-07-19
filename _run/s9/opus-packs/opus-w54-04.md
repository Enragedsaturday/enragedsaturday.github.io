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

## GROUP: content/cases/United States v. Sokolow.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Sokolow"
type: case
citation: "490 U.S. 1 (1989)"
parallel_cite: "109 S. Ct. 1581; 104 L. Ed. 2d 1; 57 U.S.L.W. 4401"
neutral_cite: 1989 U.S. LEXIS 1694
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-04-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-04-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Sokolow
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112239/united-states-v-sokolow/"
  cluster_id: 112239
  opinion_id: 112239
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[United States v. Cortez]]", "[[United States v. Arvizu]]", "[[Illinois v. Wardlow]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "reasonable-suspicion", "totality-of-the-circumstances", "drug-courier-profile"]
holding: "Factors each individually consistent with innocence can, taken together, amount to reasonable suspicion."
lake:
  record_id: United States v. Sokolow
  status: verified
  projected_at: 2026-07-09
---

# United States v. Sokolow

*490 U.S. 1 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DEA agents stopped Andrew Sokolow at Honolulu International Airport. He had paid $2,100 in cash for two airline tickets from a roll of $20 bills containing roughly twice that amount, appeared to be traveling under a name that did not match his telephone listing, flew to Miami (a source city) and stayed only 48 hours despite a 20-hour round-trip flight, and checked no luggage. After the stop, a trained dog alerted to his bags, a warrant issued, and cocaine was found. He moved to suppress, and the Ninth Circuit held the stop was not supported by reasonable suspicion.

## Issue
Whether a set of factors, each individually consistent with innocent travel, can together furnish the reasonable suspicion needed for an investigative *[[Terry v. Ohio|Terry]]* stop.

## Rule
Reasonable suspicion is judged by the whole picture, not a divide-and-conquer of innocent explanations: "In evaluating the validity of a stop such as this, we must consider 'the totality of the circumstances — the whole picture.'" — 490 U.S. at 8. ^pin-8

Factors innocent in isolation can combine into reasonable suspicion: "Any one of these factors is not by itself proof of any illegal conduct and is quite consistent with innocent travel. But we think taken together they amount to reasonable suspicion." — [490 U.S. at 9](https://www.courtlistener.com/opinion/112239/united-states-v-sokolow/#:~:text=Any%20one%20of%20these%20factors). ^pin-9

## Application
Sokolow's large cash payment from a roll of $20 bills, his apparent travel under an alias, and his brief 48-hour trip to a source city after a 20-hour round-trip flight were each consistent with innocent travel standing alone. Taken together, however, they gave the agents the minimal objective justification — less than probable cause — needed to stop him. The Ninth Circuit's attempt to sort the evidence into "ongoing criminal activity" versus "probabilistic" categories was rejected.

## Conclusion
The investigative stop was supported by reasonable suspicion under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]; the Supreme Court reversed the Ninth Circuit.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Sokolow* confirms the totality-of-the-circumstances approach to reasonable suspicion drawn from [[United States v. Cortez]] and [[Terry v. Ohio]], and rejects mechanical sorting of factors — an approach reaffirmed in [[United States v. Arvizu]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key — Progeny / Refinement*
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Sokolow*, 490 U.S. 1 (1989) — https://www.courtlistener.com/opinion/112239/united-states-v-sokolow/ — pinpoints: 8, 9 (parallel 109 S. Ct. 1581).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ec4dcf15b69111d0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "490 U.S. 1 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 1694", "official_citation_present": true, "parallel_cite": "109 S. Ct. 1581; 104 L. Ed. 2d 1; 57 U.S.L.W. 4401", "title": "United States v. Sokolow", "year": "1989"}}
{"assertion_id": "464127b9706c0282", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Factors each individually consistent with innocence can, taken together, amount to reasonable suspicion.", "title": "United States v. Sokolow"}}
{"assertion_id": "a987de016167a6c3", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "United States v. Sokolow"}}
{"assertion_id": "ba12bd3129580ce8", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "United States v. Sokolow"}}
{"assertion_id": "2332d55a74134348", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1989-04-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Sokolow", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Sokolow", "varies_by_point": "false"}}
{"assertion_id": "c646a4d1fd079aa0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Sokolow"}}
```

### lake record — United States v. Sokolow

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Sokolow",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Sokolow",
    "case_name_short": "Sokolow",
    "case_name_full": "United States v. Sokolow",
    "input_case_name": "United States v. Sokolow",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-04-03",
    "year": 1989,
    "docket": null,
    "cluster_id": 112239,
    "lead_opinion_id": 112239,
    "sibling_ids": [
      112239,
      9431641,
      9431642
    ],
    "absolute_url": "/opinion/112239/united-states-v-sokolow/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "490 U.S. 1",
      "volume": "490",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1581",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1581",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 1",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4401",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4401",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1694",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "490 U.S. 1",
        "volume": "490",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1581",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1581",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 1",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1694",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4401",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4401",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "490 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "490 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-8",
      "page": null,
      "quote": "--- # United States v. Sokolow *490 U.S. 1 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DEA agents stopped Andrew Sokolow at Honolulu International Airport. He had paid $2,100 in cash for two airline tickets from a roll of $20 bills containing roughly twice that amount, appeared to be traveling under a name that did not match his telephone listing, flew to Miami (a source city) and stayed only 48 hours despite a 20-hour round-trip flight, and checked no luggage. After the stop, a trained dog alerted to his bags, a warrant issued, and cocaine was found. He moved to suppress, and the Ninth Circuit held the stop was not supported by reasonable suspicion. ## Issue Whether a set of factors, each individually consistent with innocent travel, can together furnish the reasonable suspicion needed for an investigative *Terry* stop. ## Rule Reasonable suspicion is judged by the whole picture, not a divide-and-conquer of innocent explanations:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-9",
      "page": null,
      "quote": "Any one of these factors is not by itself proof of any illegal conduct and is quite consistent with innocent travel. But we think taken together they amount to reasonable suspicion.",
      "star_marker": "9",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15785,
      "fragment": "#:~:text=Any%20one%20of%20these%20factors",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-04-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Sokolow",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane1_negative"
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
        "journal_ref": "United States v. Sokolow:lane1_negative"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. United States",
          "cluster_id": 2795278,
          "cite": [
            "575 U.S. 348",
            "135 S. Ct. 1609",
            "191 L. Ed. 2d 492",
            "2015 U.S. LEXIS 2807",
            "83 U.S.L.W. 4241",
            "25 Fla. L. Weekly Fed. S 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Woods v. State",
          "cluster_id": 1628737,
          "cite": [
            "956 S.W.2d 33",
            "1997 Tex. Crim. App. LEXIS 90",
            "1997 WL 685978"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Retherford",
          "cluster_id": 4001886,
          "cite": [
            "639 N.E.2d 498",
            "93 Ohio App. 3d 586",
            "1994 Ohio App. LEXIS 1066"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Long",
          "cluster_id": 3950093,
          "cite": [
            "713 N.E.2d 1",
            "127 Ohio App. 3d 328"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhodes v. State",
          "cluster_id": 2427083,
          "cite": [
            "945 S.W.2d 115",
            "1997 Tex. Crim. App. LEXIS 26",
            "1997 WL 209529"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kikumura, Yu",
          "cluster_id": 551486,
          "cite": [
            "918 F.2d 1084",
            "1990 WL 166030"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Christopher Lee Davis",
          "cluster_id": 1043997,
          "cite": [
            "354 S.W.3d 718",
            "2011 Tenn. LEXIS 962"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Sandoval",
          "cluster_id": 673938,
          "cite": [
            "29 F.3d 537",
            "1994 U.S. App. LEXIS 16788",
            "1994 WL 321653"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kevin Gamble (071234)",
          "cluster_id": 2686119,
          "cite": [
            "218 N.J. 412",
            "95 A.3d 188",
            "2014 WL 3858497",
            "2014 N.J. LEXIS 801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaupp v. Texas",
          "cluster_id": 127919,
          "cite": [
            "155 L. Ed. 2d 814",
            "123 S. Ct. 1843",
            "538 U.S. 626",
            "2003 U.S. LEXIS 3670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Utah v. Strieff",
          "cluster_id": 3214882,
          "cite": [
            "579 U.S. 232",
            "195 L. Ed. 2d 400",
            "2016 U.S. LEXIS 3926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terry L. Wood",
          "cluster_id": 735391,
          "cite": [
            "106 F.3d 942",
            "1997 U.S. App. LEXIS 2071",
            "1997 WL 49935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112239 OR 9431641 OR 9431642) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk0NzcxMjAwMDAwJnM9NDc2ODE5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112239+OR+9431641+OR+9431642%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(112239 OR 9431641 OR 9431642)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzYmcz0xMDQxNjY4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112239+OR+9431641+OR+9431642%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112239 OR 9431641 OR 9431642)",
        "reviewed": 112,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 112,
        "triage_read": 2,
        "triage_snippet_classified": 110
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112239 OR 9431641 OR 9431642)",
    "indexed_citing_opinions": 2702,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112239,
        "count": 2400,
        "count_source": "search"
      },
      {
        "opinion_id": 9431641,
        "count": 346,
        "count_source": "search"
      },
      {
        "opinion_id": 9431642,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4656,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-sokolow.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0ODE3MTkmcz0xMDY1MDQxMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112239+OR+9431641+OR+9431642%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112239,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 344185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 344429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 345525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 355301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 367117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 374672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 379013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 380029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 393858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 402393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 481401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 496618,
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
    "date_created": "2026-07-06T03:05:35Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:05:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:05:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:08:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:05:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Sokolow

```
<div>
<center><b><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. 1</a></span> (1989)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
SOKOLOW</h1></center>
<center>No. 87-1295.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 10, 1989</center>
<center>Decided April 3, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*3</span> <i>Paul J. Larkin, Jr.,</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Fried, Acting Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Patty Merkamp Stemler.</i></p>
<p><i>Robert P. Goldberg</i> argued the cause and filed a brief for respondent.</p>
<p>CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Respondent Andrew Sokolow was stopped by Drug Enforcement Administration (DEA) agents upon his arrival at Honolulu International Airport. The agents found 1,063 grams of cocaine in his carry-on luggage. When respondent was stopped, the agents knew, <i>inter alia,</i> that (1) he paid $2,100 for two airplane tickets from a roll of $20 bills; (2) he traveled under a name that did not match the name under which his telephone number was listed; (3) his original destination was Miami, a source city for illicit drugs; (4) he stayed in Miami for only 48 hours, even though a round-trip flight from Honolulu to Miami takes 20 hours; (5) he appeared nervous during his trip; and (6) he checked none of his luggage. A divided panel of the United States Court of Appeals for the Ninth Circuit held that the DEA agents did not have a reasonable suspicion to stop respondent, as required by the Fourth Amendment. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d 1413</a></span> (1987). We take the contrary view.</p>
<p><span class="star-pagination">*4</span> This case involves a typical attempt to smuggle drugs through one of the Nation's airports.<sup>[1]</sup> On a Sunday in July 1984, respondent went to the United Airlines ticket counter at Honolulu Airport, where he purchased two round-trip tickets for a flight to Miami leaving later that day. The tickets were purchased in the names of "Andrew Kray" and "Janet Norian" and had open return dates. Respondent paid $2,100 for the tickets from a large roll of $20 bills, which appeared to contain a total of $4,000. He also gave the ticket agent his home telephone number. The ticket agent noticed that respondent seemed nervous; he was about 25 years old; he was dressed in a black jumpsuit and wore gold jewelry; and he was accompanied by a woman, who turned out to be Janet Norian. Neither respondent nor his companion checked any of their four pieces of luggage.</p>
<p>After the couple left for their flight, the ticket agent informed Officer John McCarthy of the Honolulu Police Department of respondent's cash purchase of tickets to Miami. Officer McCarthy determined that the telephone number respondent gave to the ticket agent was subscribed to a "Karl Herman," who resided at 348-A Royal Hawaiian Avenue in Honolulu. Unbeknownst to McCarthy (and later to the DEA agents), respondent was Herman's roommate. The ticket agent identified respondent's voice on the answering machine at Herman's number. Officer McCarthy was unable to find any listing under the name "Andrew Kray" in Hawaii. McCarthy subsequently learned that return reservations from Miami to Honolulu had been made in the names of Kray and Norian, with their arrival scheduled for July 25, three days after respondent and his companion had left. He also learned that Kray and Norian were scheduled to make stopovers in Denver and Los Angeles.</p>
<p><span class="star-pagination">*5</span> On July 25, during the stopover in Los Angeles, DEA agents identified respondent. He "appeared to be very nervous and was looking all around the waiting area." App. 43-44. Later that day, at 6:30 p. m., respondent and Norian arrived in Honolulu. As before, they had not checked their luggage. Respondent was still wearing a black jumpsuit and gold jewelry. The couple proceeded directly to the street and tried to hail a cab, where Agent Richard Kempshall and three other DEA agents approached them. Kempshall displayed his credentials, grabbed respondent by the arm, and moved him back onto the sidewalk. Kempshall asked respondent for his airline ticket and identification; respondent said that he had neither. He told the agents that his name was "Sokolow," but that he was traveling under his mother's maiden name, "Kray."</p>
<p>Respondent and Norian were escorted to the DEA office at the airport. There, the couple's luggage was examined by "Donker," a narcotics detector dog, which alerted on respondent's brown shoulder bag. The agents arrested respondent. He was advised of his constitutional rights and declined to make any statements. The agents obtained a warrant to search the shoulder bag. They found no illicit drugs, but the bag did contain several suspicious documents indicating respondent's involvement in drug trafficking. The agents had Donker reexamine the remaining luggage, and this time the dog alerted on a medium-sized Louis Vuitton bag. By now, it was 9:30 p. m., too late for the agents to obtain a second warrant. They allowed respondent to leave for the night, but kept his luggage. The next morning, after a second dog confirmed Donker's alert, the agents obtained a warrant and found 1,063 grams of cocaine inside the bag.</p>
<p>Respondent was indicted for possession with the intent to distribute cocaine in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). The United States District Court for Hawaii denied his motion to suppress the cocaine and other evidence seized from his luggage, finding that the DEA agents had a reasonable suspicion <span class="star-pagination">*6</span> that he was involved in drug trafficking when they stopped him at the airport. Respondent then entered a conditional plea of guilty to the offense charged.</p>
<p>The United States Court of Appeals for the Ninth Circuit reversed respondent's conviction by a divided vote, holding that the DEA agents did not have a reasonable suspicion to justify the stop. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1423" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d, at 1423</a></span>.<sup>[2]</sup> The majority divided the facts bearing on reasonable suspicion into two categories. In the first category, the majority placed facts describing "ongoing criminal activity," such as the use of an alias or evasive movement through an airport; the majority believed that at least one such factor was always needed to support a finding of reasonable suspicion. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1419" aria-description="Citation for case: United States v. Andrew Sokolow"><i>Id.,</i> at 1419</a></span>. In the second category, it placed facts describing "personal characteristics" of drug couriers, such as the cash payment for tickets, a short trip to a major source city for drugs, nervousness, type of attire, and unchecked luggage. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1420" aria-description="Citation for case: United States v. Andrew Sokolow"><i>Id.,</i> at 1420</a></span>. The majority believed that such characteristics, "shared by drug couriers and the public at large," were only relevant if there was evidence of ongoing criminal behavior and the Government offered "[e]mpirical documentation" that the combination of facts at issue did not describe the behavior of "significant numbers of innocent persons." <i><span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">Ibid.</a></span></i> Applying this two-part test to the facts of this case, the majority found that there was no evidence of ongoing criminal behavior, and thus that the agents' stop was impermissible. The dissenting judge took the view that the majority's approach was "overly mechanistic" and "contrary to the case-by-case determination of reasonable articulable suspicion based on <i>all</i> the facts." <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1426" aria-description="Citation for case: United States v. Andrew Sokolow"><i>Id.,</i> at 1426</a></span>.</p>
<p><span class="star-pagination">*7</span> We granted certiorari to review the decision of the Court of Appeals, <span class="citation multiple-matches"><a href="/c/U.%20S./486/1042/">486 U. S. 1042</a></span> (1988), because of its serious implications for the enforcement of the federal narcotics laws. We now reverse.</p>
<p>The Court of Appeals held that the DEA agents seized respondent when they grabbed him by the arm and moved him back onto the sidewalk. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1416" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d, at 1416</a></span>. The Government does not challenge that conclusion, and we assume  without deciding  that a stop occurred here. Our decision, then, turns on whether the agents had a reasonable suspicion that respondent was engaged in wrongdoing when they encountered him on the sidewalk. In <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 30</a></span> (1968), we held that the police can stop and briefly detain a person for investigative purposes if the officer has a reasonable suspicion supported by articulable facts that criminal activity "may be afoot," even if the officer lacks probable cause.</p>
<p>The officer, of course, must be able to articulate something more than an "inchoate and unparticularized suspicion or `hunch.' " <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 27</a></span>. The Fourth Amendment requires "some minimal level of objective justification" for making the stop. <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#217" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 217</a></span> (1984). That level of suspicion is considerably less than proof of wrongdoing by a preponderance of the evidence. We have held that probable cause means "a fair probability that contraband or evidence of a crime will be found," <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 238</a></span> (1983), and the level of suspicion required for a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop is obviously less demanding than that for probable cause, see <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#541" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 541, 544</a></span> (1985).</p>
<p>The concept of reasonable suspicion, like probable cause, is not "readily, or even usefully, reduced to a neat set of legal rules." <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232</a></span>. We think the Court of Appeals' effort to refine and elaborate the requirements of "reasonable suspicion" in this case creates unnecessary difficulty in dealing with one of the relatively simple concepts embodied <span class="star-pagination">*8</span> in the Fourth Amendment. In evaluating the validity of a stop such as this, we must consider "the totality of the circumstances  the whole picture." <i>United States</i> v. <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981). As we said in <i><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">Cortez</a></span>:</i></p>
<blockquote>"The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain common-sense conclusions about human behavior; jurors as factfinders are permitted to do the same  and so are law enforcement officers." <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez"><i>Id.,</i> at 418</a></span>.</blockquote>
<p>The rule enunciated by the Court of Appeals, in which evidence available to an officer is divided into evidence of "ongoing criminal behavior," on the one hand, and "probabilistic" evidence, on the other, is not in keeping with the quoted statements from our decisions. It also seems to us to draw a sharp line between types of evidence, the probative value of which varies only in degree. The Court of Appeals classified evidence of traveling under an alias, or evidence that the suspect took an evasive or erratic path through an airport, as meeting the test for showing "ongoing criminal activity." But certainly instances are conceivable in which traveling under an alias would not reflect ongoing criminal activity: for example, a person who wished to travel to a hospital or clinic for an operation and wished to conceal that fact. One taking an evasive path through an airport might be seeking to avoid a confrontation with an angry acquaintance or with a creditor. This is not to say that each of these types of evidence is not highly probative, but they do not have the sort of ironclad significance attributed to them by the Court of Appeals.</p>
<p>On the other hand, the factors in this case that the Court of Appeals treated as merely "probabilistic" also have probative significance. Paying $2,100 in cash for two airplane tickets is out of the ordinary, and it is even more out of the ordinary to pay that sum from a roll of $20 bills containing nearly twice that amount of cash. Most business travelers, we feel confident, purchase airline tickets by credit card or check so as to <span class="star-pagination">*9</span> have a record for tax or business purposes, and few vacationers carry with them thousands of dollars in $20 bills. We also think the agents had a reasonable ground to believe that respondent was traveling under an alias; the evidence was by no means conclusive, but it was sufficient to warrant consideration.<sup>[3]</sup> While a trip from Honolulu to Miami, standing alone, is not a cause for any sort of suspicion, here there was more: surely few residents of Honolulu travel from that city for 20 hours to spend 48 hours in Miami during the month of July.</p>
<p>Any one of these factors is not by itself proof of any illegal conduct and is quite consistent with innocent travel. But we think taken together they amount to reasonable suspicion. See <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (opinion of WHITE, J.); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#515" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 515-516</a></span> (BLACKMUN, J., dissenting); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#523" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 523-524</a></span> (REHNQUIST, J., dissenting).<sup>[4]</sup> We said in <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438</a></span> (1980) <i>(per curiam)</i><i>,</i> "there could, of course, be circumstances in which wholly lawful conduct might justify the suspicion that criminal activity was afoot." <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 441</a></span>.<sup>[5]</sup> Indeed, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> itself involved "a series of acts, <span class="star-pagination">*10</span> each of them perhaps innocent" if viewed separately, "but which taken together warranted further investigation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>; see also <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez"><i>Cortez, supra,</i> at 417-419</a></span>. We noted in <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#243" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 243-244, n. 13</a></span>, that "innocent behavior will frequently provide the basis for a showing of probable cause," and that "[i]n making a determination of probable cause the relevant inquiry is not whether particular conduct is `innocent' or `guilty,' but the degree of suspicion that attaches to particular types of noncriminal acts." That principle applies equally well to the reasonable suspicion inquiry.</p>
<p>We do not agree with respondent that our analysis is somehow changed by the agents' belief that his behavior was consistent with one of the DEA's "drug courier profiles."<sup>[6]</sup> Brief for Respondent 14-21. A court sitting to determine the existence of reasonable suspicion must require the agent to articulate the factors leading to that conclusion, but the fact that these factors may be set forth in a "profile" does not somehow detract from their evidentiary significance as seen by a trained agent.</p>
<p>Respondent also contends that the agents were obligated to use the least intrusive means available to verify or dispel their suspicions that he was smuggling narcotics. <i>Id.,</i> at 12-13, 21-23. In respondent's view, the agents should have simply approached and spoken with him, rather than forcibly detaining him. He points to the statement in <i>Florida</i> v. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer"><i>Royer, supra,</i> at 500</a></span> (opinion of WHITE, J.), that "the investigative <span class="star-pagination">*11</span> methods employed should be the least intrusive means reasonably available to verify or dispel the officer's suspicion in a short period of time." That statement, however, was directed at the length of the investigative stop, not at whether the police had a less intrusive means to verify their suspicions before stopping Royer. The reasonableness of the officer's decision to stop a suspect does not turn on the availability of less intrusive investigatory techniques. Such a rule would unduly hamper the police's ability to make swift, on-the-spot decisions  here, respondent was about to get into a taxicab  and it would require courts to "indulge in `unrealistic second-guessing.' " <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#542" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S., at 542</a></span>, quoting <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#686" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 686, 687</a></span> (1985).</p>
<p>We hold that the agents had a reasonable basis to suspect that respondent was transporting illegal drugs on these facts. The judgment of the Court of Appeals is therefore reversed, and the case is remanded for further proceedings consistent with our decision.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE MARSHALL, with whom JUSTICE BRENNAN joins, dissenting.</p>
<p>Because the strongest advocates of Fourth Amendment rights are frequently criminals, it is easy to forget that our interpretations of such rights apply to the innocent and the guilty alike. <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#290" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 290</a></span> (1983) (BRENNAN, J., dissenting). In the present case, the chain of events set in motion when respondent Andrew Sokolow was stopped by Drug Enforcement Administration (DEA) agents at Honolulu International Airport led to the discovery of cocaine and, ultimately, to Sokolow's conviction for drug trafficking. But in sustaining this conviction on the ground that the agents reasonably suspected Sokolow of ongoing criminal activity, the Court diminishes the rights of <i>all</i> citizens "to be secure in their persons," U. S. Const., Amdt. 4, as they <span class="star-pagination">*12</span> traverse the Nation's airports. Finding this result constitutionally impermissible, I dissent.</p>
<p>The Fourth Amendment cabins government's authority to intrude on personal privacy and security by requiring that searches and seizures usually be supported by a showing of probable cause. The reasonable-suspicion standard is a derivation of the probable-cause command, applicable only to those brief detentions which fall short of being full-scale searches and seizures and which are necessitated by law enforcement exigencies such as the need to stop ongoing crimes, to prevent imminent crimes, and to protect law enforcement officers in highly charged situations. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 30</a></span> (1968). By requiring reasonable suspicion as a prerequisite to such seizures, the Fourth Amendment protects innocent persons from being subjected to "overbearing or harassing" police conduct carried out solely on the basis of imprecise stereotypes of what criminals look like, or on the basis of irrelevant personal characteristics such as race. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#14" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 14-15</a></span>, and n. 11 (citation omitted).</p>
<p>To deter such egregious police behavior, we have held that a suspicion is not reasonable unless officers have based it on "specific and articulable facts." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 21</a></span>; see also <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 880</a></span> (1975). It is not enough to suspect that an individual has committed crimes in the past, harbors unconsummated criminal designs, or has the propensity to commit crimes. On the contrary, before detaining an individual, law enforcement officers must reasonably suspect that he is engaged in, or poised to commit, a criminal act <i>at that moment.</i> See, <i>e. g., </i><i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979) (to detain, officers must "have a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity"); <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 30</a></span> (reasonable suspicion exists only where policeman reasonably concludes, <i>inter alia,</i> "that criminal activity may be afoot"). The rationale for permitting brief, warrantless seizures is, after all, that it is impractical to demand strict compliance <span class="star-pagination">*13</span> with the Fourth Amendment's ordinary probable-cause requirement in the face of ongoing or imminent criminal activity demanding "swift action predicated upon the on-the-spot observations of the officer on the beat." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 20</a></span>. Observations raising suspicions of past criminality demand no such immediate action, but instead should appropriately trigger routine police investigation, which may ultimately generate sufficient information to blossom into probable cause.</p>
<p>Evaluated against this standard, the facts about Andrew Sokolow known to the DEA agents at the time they stopped him fall short of reasonably indicating that he was engaged at the time in criminal activity. It is highly significant that the DEA agents stopped Sokolow because he matched one of the DEA's "profiles" of a paradigmatic drug courier. In my view, a law enforcement officer's mechanistic application of a formula of personal and behavioral traits in deciding whom to detain can only dull the officer's ability and determination to make sensitive and fact-specific inferences "in light of his experience," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 27</a></span>, particularly in ambiguous or borderline cases. Reflexive reliance on a profile of drug courier characteristics runs a far greater risk than does ordinary, case-by-case police work of subjecting innocent individuals to unwarranted police harassment and detention. This risk is enhanced by the profile's "chameleon-like way of adapting to any particular set of observation." <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1418" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d 1413, 1418</a></span> (CA9 1987). Compare, <i>e. g., </i><i>United States</i> v. <i>Moore,</i> <span class="citation" data-id="402393"><a href="/opinion/402393/united-states-v-ronnie-d-moore/#803" aria-description="Citation for case: United States v. Ronnie D. Moore">675 F. 2d 802, 803</a></span> (CA6 1982) (suspect was first to deplane), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./460/1068/">460 U. S. 1068</a></span> (1983), with <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#564" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 564</a></span> (1980) (last to deplane), with <i>United States</i> v. <i>Buenaventura-Ariza,</i> <span class="citation" data-id="374672"><a href="/opinion/374672/united-states-v-jorge-buenaventura-ariza-and-delores-quiroz-santi/#31" aria-description="Citation for case: United States v. Jorge Buenaventura-Ariza and Delores...">615 F. 2d 29, 31</a></span> (CA2 1980) (deplaned from middle); <i>United States</i> v. <i>Sullivan,</i> <span class="citation" data-id="380029"><a href="/opinion/380029/united-states-v-diann-pansey-sullivan-aka-brenda-rowe-kathy-ruth/#12" aria-description="Citation for case: United States v. Diann Pansey Sullivan, A/K/A Brenda...">625 F. 2d 9, 12</a></span> (CA4 1980) (one-way tickets), with <i>United States</i> v. <i>Craemer,</i> <span class="citation" data-id="345525"><a href="/opinion/345525/united-states-v-james-mitchell-craemer/#595" aria-description="Citation for case: United States v. James Mitchell Craemer">555 F. 2d 594, 595</a></span> (CA6 1977) (round-trip tickets), with <i>United States</i> v. <i>McCaleb,</i> <span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/#720" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page">552 F. 2d 717, 720</a></span> (CA6 1977) (nonstop flight), with <i>United States</i> v. <i>Sokolow,</i> <span class="citation" data-id="9475720"><a href="/opinion/481401/united-states-v-andrew-sokolow/#1370" aria-description="Citation for case: United States v. Andrew Sokolow">808 F. 2d 1366, 1370</a></span> (CA9), vacated, 831 F. 2d 1413 <span class="star-pagination">*14</span> (1987) (case below) (changed planes); <span class="citation" data-id="345525"><a href="/opinion/345525/united-states-v-james-mitchell-craemer/#595" aria-description="Citation for case: United States v. James Mitchell Craemer"><i>Craemer, supra,</i> at 595</a></span> (no luggage), with <i>United States</i> v. <i>Sanford,</i> <span class="citation" data-id="9468329"><a href="/opinion/393858/united-states-v-jesse-lee-sanford/#343" aria-description="Citation for case: United States v. Jesse Lee Sanford">658 F. 2d 342, 343</a></span> (CA5 1981) (gym bag), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./455/991/">455 U. S. 991</a></span> (1982), with <span class="citation" data-id="380029"><a href="/opinion/380029/united-states-v-diann-pansey-sullivan-aka-brenda-rowe-kathy-ruth/#12" aria-description="Citation for case: United States v. Diann Pansey Sullivan, A/K/A Brenda..."><i>Sullivan, supra,</i> at 12</a></span> (new suitcases); <i>United States</i> v. <i>Smith,</i> <span class="citation" data-id="9464735"><a href="/opinion/355301/united-states-v-erma-smith/#883" aria-description="Citation for case: United States v. Erma Smith">574 F. 2d 882, 883</a></span> (CA6 1978) (traveling alone), with <i>United States</i> v. <i>Fry,</i> <span class="citation" data-id="379013"><a href="/opinion/379013/united-states-v-william-monroe-fry-jr/#1219" aria-description="Citation for case: United States v. William Monroe Fry, Jr.">622 F. 2d 1218, 1219</a></span> (CA5 1980) (traveling with companion); <i>United States</i> v. <i>Andrews,</i> <span class="citation" data-id="367117"><a href="/opinion/367117/united-states-v-tallice-andrews/#566" aria-description="Citation for case: United States v. Tallice Andrews">600 F. 2d 563, 566</a></span> (CA6 1979) (acted nervously), cert. denied <i>sub nom. </i><i>Brooks</i> v. <i>United States,</i> <span class="citation" data-id="9017003"><a href="/opinion/9023762/brooks-v-united-states/" aria-description="Citation for case: Brooks v. United States">444 U. S. 878</a></span> (1979), with <i>United States</i> v. <i>Himmelwright,</i> <span class="citation" data-id="344185"><a href="/opinion/344185/united-states-v-mary-ann-himmelwright/#992" aria-description="Citation for case: United States v. Mary Ann Himmelwright">551 F. 2d 991, 992</a></span> (CA5) (acted too calmly), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./434/902/">434 U. S. 902</a></span> (1977). In asserting that it is not "somehow" relevant that the agents who stopped Sokolow did so in reliance on a prefabricated profile of criminal characteristics, <i>ante,</i> at 10, the majority thus ducks serious issues relating to a questionable law enforcement practice, to address the validity of which we granted certiorari in this case.<sup>[1]</sup></p>
<p>That the factors comprising the drug courier profile relied on in this case are especially dubious indices of ongoing criminal activity is underscored by <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438</a></span> (1980), a strikingly similar case. There, four facts, encoded in a drug courier profile, were alleged in support of the DEA's detention of a suspect at the Atlanta Airport. First, Reid had arrived from Fort Lauderdale, Florida, a source city for cocaine. Second, he arrived in the early morning, when law enforcement activity is diminished. Third, he and his companion appeared to have no luggage other than their shoulder bags. And fourth, he and his companion appeared to be trying to conceal the fact that they were traveling together. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 440-441</a></span>.</p>
<p>This collection of facts, we held, was inadequate to support a finding of reasonable suspicion. All but the last of these facts, we observed, "describe a very large category of presumably <span class="star-pagination">*15</span> innocent travelers, who would be subject to virtually random seizures were the Court to conclude that as little foundation as there was in this case could justify a seizure." <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 441</a></span>. The sole fact that suggested criminal activity was that Reid "preceded another person and occasionally looked backward at him as they proceeded through the concourse." <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Ibid.</a></span></i> This observation did not of itself provide a reasonable basis for suspecting wrongdoing, for inferring criminal activity from such evidence reflected no more than an " `inchoate and unparticularized suspicion or "hunch." ' " <i>Ibid.,</i> quoting <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27</a></span>.<sup>[2]</sup></p>
<p>The facts known to the DEA agents at the time they detained the traveler in this case are scarcely more suggestive of ongoing criminal activity than those in <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span>.</i> Unlike traveler Reid, who sought to conceal the fact that he was traveling with a companion, and who even attempted to run away after being approached by a DEA agent, <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#439" aria-description="Citation for case: Reid v. Georgia">448 U. S., at 439</a></span>, traveler Sokolow gave no indications of evasive activity. On the contrary, the sole behavioral detail about Sokolow noted by the DEA agents was that he was nervous. With news accounts proliferating of plane crashes, near collisions, and air terrorism, there are manifold and good reasons for being agitated while awaiting a flight, reasons that have nothing to do with one's involvement in a criminal endeavor.</p>
<p>The remaining circumstantial facts known about Sokolow, considered either singly or together, are scarcely indicative of criminal activity. Like the information disavowed in <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span></i> as nonprobative, the fact that Sokolow took a brief trip to a <span class="star-pagination">*16</span> resort city for which he brought only carry-on luggage also "describe[s] a very large category of presumably innocent travelers." <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 441</a></span>. That Sokolow embarked from Miami, "a source city for illicit drugs," <i>ante,</i> at 3, is no more suggestive of illegality; thousands of innocent persons travel from "source cities" every day and, judging from the DEA's testimony in past cases, nearly every major city in the country may be characterized as a source or distribution city. See, <i>e. g., </i><i>Buenaventura-Ariza,</i> <span class="citation" data-id="374672"><a href="/opinion/374672/united-states-v-jorge-buenaventura-ariza-and-delores-quiroz-santi/#31" aria-description="Citation for case: United States v. Jorge Buenaventura-Ariza and Delores...">615 F. 2d, at 31, n. 5</a></span>. That Sokolow had his phone listed in another person's name also does not support the majority's assertion that the DEA agents reasonably believed Sokolow was using an alias; it is commonplace to have one's phone registered in the name of a roommate, which, it later turned out, was precisely what Sokolow had done.<sup>[3]</sup> That Sokolow was dressed in a black jumpsuit and wore gold jewelry also provides no grounds for suspecting wrongdoing, the majority's repeated and unexplained allusions to Sokolow's style of dress notwithstanding. <i>Ante,</i> at 4, 5. For law enforcement officers to base a search, even in part, on a "pop" guess that persons dressed in a particular fashion are likely to commit crimes not only stretches the concept of reasonable suspicion beyond recognition, but also is inimical to the self-expression which the choice of wardrobe may provide.</p>
<p>Finally, that Sokolow paid for his tickets in cash indicates no imminent or ongoing criminal activity. The majority "feel[s] confident" that "[m]ost business travelers . . . purchase airline tickets by credit card or check." <i>Ante,</i> at 8. Why the majority confines its focus only to "business travelers" I do not know, but I would not so lightly infer ongoing crime from the use of legal tender. Making major cash purchases, while surely less common today, may simply reflect the traveler's aversion to, or inability to obtain, plastic <span class="star-pagination">*17</span> money. Conceivably, a person who spends large amounts of cash may be trying to launder his proceeds from <i>past</i> criminal enterprises by converting them into goods and services. But, as I have noted, investigating completed episodes of crime goes beyond the appropriately limited purview of the brief, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>-style seizure. Moreover, it is unreasonable to suggest that, had Sokolow left the airport, he would have been gone forever and thus immune from subsequent investigation. <i>Ante,</i> at 11. Sokolow, after all, had given the airline his phone number, and the DEA, having ascertained that it was indeed Sokolow's voice on the answering machine at that number, could have learned from that information where Sokolow resided.</p>
<p>The fact is that, unlike the taking of patently evasive action, <i>Florida</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#6" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1, 6</a></span> (1984), the use of an alias, <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983), the casing of a store, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#6" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 6</a></span>, or the provision of a reliable report from an informant that wrongdoing is imminent, <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#225" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 225-227</a></span>, nothing about the characteristics shown by airport traveler Sokolow reasonably suggests that criminal activity is afoot. The majority's hasty conclusion to the contrary serves only to indicate its willingness, when drug crimes or antidrug policies are at issue, to give short shrift to constitutional rights. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#636" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 636</a></span> (1989) (MARSHALL, J., dissenting).<sup>[4]</sup> In requiring that seizures be based on at least some evidence of criminal conduct, <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1419" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d, at 1419</a></span>, the Court of Appeals was faithful to the Fourth Amendment principle that law enforcement officers <span class="star-pagination">*18</span> must reasonably suspect a person of criminal activity before they can detain him. Because today's decision, though limited to its facts, <i>ante,</i> at 11, disobeys this important constitutional command, I dissent.</p>
<h2>NOTES</h2>
<p>[1]  The facts in this case were developed at suppression hearings held in the District Court over three separate days. The parties also stipulated to certain facts.</p>
<p>[2]  In an earlier decision, the Court of Appeals also reversed the District Court, but on the basis of different reasoning. <span class="citation" data-id="9475720"><a href="/opinion/481401/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">808 F. 2d 1366</a></span>, vacated, <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d 1413</a></span> (1987). The Court of Appeals' second decision was issued after the Government petitioned for rehearing on the ground that the court had erred in considering each of the facts known to the agents separately rather than in terms of the totality of the circumstances.</p>
<p>[3]  Respondent also claims that the agents should have conducted a further inquiry to resolve the inconsistency between the name he gave the airline and the name, "Karl Herman," under which his telephone number was listed. Brief for Respondent 26. This argument avails respondent nothing; had the agents done further checking, they would have discovered not only that respondent was Herman's roommate but also that his name was "Sokolow" and not "Kray," the name listed on his ticket.</p>
<p>[4]  In <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>,</i> the police were aware, <i>inter alia,</i> that (1) Royer was traveling under an assumed name; (2) he paid for his ticket in cash with a number of small bills; (3) he was traveling from Miami to New York; (4) he put only his name and not an address on his checked luggage; and (5) he seemed nervous while walking through Miami airport. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#493" aria-description="Citation for case: Florida v. Royer">460 U. S., at 493, n. 2, 502</a></span> (opinion of WHITE, J.).</p>
<p>[5]  In <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span>,</i> the Court held that a DEA agent stopped the defendant without reasonable suspicion. At the time of the stop, the agent knew that (1) the defendant flew into Atlanta from Fort Lauderdale, a source city for cocaine; (2) he arrived early in the morning, when police activity was believed to be at a low ebb; (3) he did not check his luggage; and (4) the defendant and his companion appeared to be attempting to hide the fact that they were together. The Court held that the first three of these facts were not sufficient to supply reasonable suspicion, because they "describe a very large category of presumably innocent travelers," while the last fact was insufficient on the facts of that case to establish reasonable suspicion. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia">448 U. S., at 441</a></span>.</p>
<p>[6]  Agent Kempshall testified that respondent's behavior "had all the classic aspects of a drug courier." App. 59. Since 1974, the DEA has trained narcotics officers to identify drug smugglers on the basis of the sort of circumstantial evidence at issue here.</p>
<p>[1]  Even if such profiles had reliable predictive value, their utility would be short lived, for drug couriers will adapt their behavior to sidestep detection from profile-focused officers.</p>
<p>[2]  Nor was <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span></i> a close case: eight Members of the Court found the challenged detention insupportable, five of whom saw fit to dispose of the case by reversing the court below in a <i>per curiam</i> opinion. In a separate concurrence, Justice Powell, joined by Chief Justice Burger and JUSTICE BLACKMUN, agreed that "the fragmentary facts apparently relied on by the DEA agents" provided "no justification" for Reid's detention. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#442" aria-description="Citation for case: Reid v. Georgia">448 U. S., at 442, n. 1</a></span>. Only then-JUSTICE REHNQUIST, the author of today's majority opinion, dissented, on the ground that the police conduct involved did not implicate Reid's constitutional rights. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#442" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 442</a></span>.</p>
<p>[3]  That Sokolow was, in fact, using an alias was not known to the DEA agents until <i>after</i> they detained him. Thus, it cannot legitimately be considered as a basis for the seizure in this case.</p>
<p>[4]  The majority also contends that it is not relevant that the DEA agents, in forcibly stopping Sokolow rather than simply speaking with him, did not "use the least intrusive means available." <i>Ante,</i> at 10. On the contrary, the manner in which a search is carried out  and particularly whether law enforcement officers have taken needlessly intrusive steps  is a highly important index of reasonableness under Fourth Amendment doctrine. See, <i>e. g., </i><i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#760" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, 760-761</a></span> (1985).</p>

</div>
```

---

## GROUP: content/cases/United States v. Touset.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Touset"
type: case
citation: "890 F.3d 1227 (2018)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Eleventh Circuit"
court_level: coa
circuit: 11th
year: 2018
date_decided: 2018-05-23
docket: ""
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2018-05-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Touset
  varies_by_point: false
  scope_note: "Circuit split: the 9th Cir. (United States v. Cotterman) requires reasonable suspicion for forensic device searches at the border."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4500452/united-states-v-karl-touset/"
  cluster_id: 4500452
  opinion_id: 4277705
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Recent development (role-based)"
related: ["[[United States v. Ramsey]]", "[[United States v. Cotterman]]", "[[United States v. Flores-Montano]]", "[[Riley v. California]]"]
aliases: ["United States v. Touset (11th Cir. 2018)", "United States v. Karl Touset"]
tags: ["case", "fourth-amendment", "border-searches", "forensic-search", "electronic-devices", "eleventh-circuit", "circuit-split"]
holding: "The Fourth Amendment requires no suspicion — not even reasonable suspicion — for a forensic search of an electronic device at the…"
lake:
  record_id: United States v. Touset
  status: verified
  projected_at: 2026-07-06
---

# United States v. Touset

*890 F.3d 1227 (11th Cir. 2018)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Customs agents at the border forensically searched Touset's electronic devices and found child pornography. The investigation had begun with information that Touset made small Western Union payments to an entity in the Philippines (a country associated with child exploitation) that used an email address tied to child pornography. Touset moved to suppress, and the district court — following the Ninth Circuit's *[[United States v. Cotterman|Cotterman]]* — held that reasonable suspicion was required and was present.

## Issue
Whether the Fourth Amendment requires any suspicion — in particular, reasonable suspicion — for a forensic search of electronic devices at the international border.

## Rule
No. The border-search exception requires no suspicion for searches of property at the border, and that rule extends to forensic searches of electronic devices: "the Fourth Amendment does not require any suspicion for forensic searches of electronic devices at the border." — *United States v. Touset*, 890 F.3d 1227 (11th Cir. 2018) (Part III.A). ^pin-IIIa

The court declined to follow the Ninth Circuit's *[[United States v. Cotterman|Cotterman]]*, reasoning that the Supreme Court has never required suspicion to search **property** (as opposed to highly intrusive searches of the **person**) at the border, and that *[[Riley v. California]]* — a search-incident-to-arrest case — does not transplant a warrant or suspicion requirement to the border.

## Application
Touset's laptops, hard drives, and other devices were forensically searched at the border, where no suspicion is required to search property; the searches were therefore lawful. In the alternative, the court held that reasonable suspicion existed anyway — the Western Union payments to a Philippine entity associated with child exploitation supported the search. Either way, suppression was not warranted.

## Conclusion
No suspicion is required for forensic searches of electronic devices at the border; the Eleventh Circuit affirmed the denial of Touset's motion to suppress.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- No negative treatment within the circuit. **Circuit split:** *Touset* expressly rejects the Ninth Circuit's [[United States v. Cotterman]], which requires reasonable suspicion for forensic (as opposed to manual) searches of electronic devices at the border — a recognized split on suspicion requirements for device searches at the border.

## Appears on
- [[Border Searches]] — *Recent development (role-based)*

## Sources
- *United States v. Touset*, 890 F.3d 1227 (11th Cir. 2018) — https://www.courtlistener.com/opinion/4500452/united-states-v-karl-touset/ — CourtListener's text is paragraph-structured rather than reporter-paginated; the pinpoint is given by opinion section (Part III.A). Cluster 4500452 → opinion 4277705.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3858543a67dcea8a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "890 F.3d 1227 (2018)", "court": "U.S. Court of Appeals, Eleventh Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Touset", "year": "2018"}}
{"assertion_id": "24700a907def973a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment requires no suspicion — not even reasonable suspicion — for a forensic search of an electronic device at the…", "title": "United States v. Touset"}}
{"assertion_id": "6ccb630552ac4fa7", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Recent development (role-based)", "title": "United States v. Touset"}}
{"assertion_id": "63d962c9ce366cb4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2018-05-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Touset", "field_i_validity": "good_law", "scope_note": "Circuit split: the 9th Cir. (United States v. Cotterman) requires reasonable suspicion for forensic device searches at the border.", "title": "United States v. Touset", "varies_by_point": "false"}}
{"assertion_id": "6cf955fb27eddc8c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 11th Cir.", "title": "United States v. Touset"}}
```

### lake record — United States v. Touset

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Touset",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Karl Touset",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Karl TOUSET, Defendant-Appellant.",
    "input_case_name": "United States v. Touset",
    "court": "U.S. Court of Appeals, Eleventh Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2018-05-23",
    "year": 2018,
    "docket": null,
    "cluster_id": 4500452,
    "lead_opinion_id": 4277705,
    "sibling_ids": [
      4277705
    ],
    "absolute_url": "/opinion/4500452/united-states-v-karl-touset/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "890 F.3d 1227",
      "volume": "890",
      "reporter": "F.3d",
      "page": "1227",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "890 F.3d 1227",
        "volume": "890",
        "reporter": "F.3d",
        "page": "1227",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "890 F.3d 1227",
    "official_selection": {
      "court_class": "coa",
      "selected": "890 F.3d 1227",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-IIIa",
      "page": null,
      "quote": "--- # United States v. Touset *890 F.3d 1227 (11th Cir. 2018)* \u00b7 U.S. Court of Appeals, Eleventh Circuit \u00b7 **Binding in-circuit \u2014 11th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Customs agents at the border forensically searched Touset's electronic devices and found child pornography. The investigation had begun with information that Touset made small Western Union payments to an entity in the Philippines (a country associated with child exploitation) that used an email address tied to child pornography. Touset moved to suppress, and the district court \u2014 following the Ninth Circuit's *Cotterman* \u2014 held that reasonable suspicion was required and was present. ## Issue Whether the Fourth Amendment requires any suspicion \u2014 in particular, reasonable suspicion \u2014 for a forensic search of electronic devices at the international border. ## Rule No. The border-search exception requires no suspicion for searches of property at the border, and that rule extends to forensic searches of electronic devices:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-05-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Touset",
    "varies_by_point": false,
    "scope_note": "Circuit split: the 9th Cir. (United States v. Cotterman) requires reasonable suspicion for forensic device searches at the border.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Jordan Jysae Pulido",
          "cluster_id": 10374408,
          "cite": [
            "133 F.4th 1256"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarissa Gilmore v. Georgia Department of Corrections",
          "cluster_id": 10017987,
          "cite": [
            "111 F.4th 1118"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bruce Mitchell Nicholson",
          "cluster_id": 6244823,
          "cite": [
            "24 F.4th 1341"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Haitao Xiang",
          "cluster_id": 9397097,
          "cite": [
            "67 F.4th 895"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524074,
          "cite": [
            "103 F.4th 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Perkins",
          "cluster_id": 4761795,
          "cite": [
            "126 N.Y.S.3d 745",
            "184 A.D.3d 776",
            "2020 NY Slip Op 3425"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4781994,
          "cite": [
            "973 F.3d 966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarissa Gilmore v. Georgia Department of Corrections",
          "cluster_id": 10631717,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Aaron Mason v. the State of Texas",
          "cluster_id": 10326280,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524075,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alasaad v. Wolf",
          "cluster_id": 4855246,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Adrian Tremayne Wilson",
          "cluster_id": 4800489,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4277705) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      },
      "lane2_top_cited": {
        "query": "cites:(4277705)",
        "reviewed": 13,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 12,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4277705)",
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
    "complete_query": "cites:(4277705)",
    "indexed_citing_opinions": 13,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4277705,
        "count": 13,
        "count_source": "search"
      }
    ],
    "citation_count": 36,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-touset.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 13,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4277705,
        "cited_id": 2420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 76983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 77569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 77895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 78325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 78422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 110794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 112417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 145810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 147332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 151874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 203261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 416536,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 432317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 447050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 626016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 678602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 770469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 771007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 776207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 798197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 1267346,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 1460543,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 2680439,
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
    "date_created": "2026-07-06T03:10:06Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:10:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:10:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:13:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:10:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Touset

```
                Case: 17-11561       Date Filed: 05/23/2018       Page: 1 of 25


                                                                                   [PUBLISH]

                  IN THE UNITED STATES COURT OF APPEALS

                            FOR THE ELEVENTH CIRCUIT
                              ________________________

                                     No. 17-11561
                               ________________________

                      D.C. Docket No. 1:15-cr-00045-MHC-JKL-1



UNITED STATES OF AMERICA,

                                                                        Plaintiff-Appellee,
                                             versus

KARL TOUSET,

                                                                    Defendant-Appellant.

                               ________________________

                      Appeal from the United States District Court
                         for the Northern District of Georgia
                             _______________________

                                       (May 23, 2018)

Before WILLIAM PRYOR and JULIE CARNES, Circuit Judges, and
CORRIGAN, * District Judge.

WILLIAM PRYOR, Circuit Judge:



*
  Honorable Timothy J. Corrigan, United States District Judge for the Middle District of Florida,
sitting by designation.
              Case: 17-11561     Date Filed: 05/23/2018   Page: 2 of 25


      This appeal presents the question whether the Fourth Amendment requires

reasonable suspicion for a forensic search of an electronic device at the border.

U.S. Const. amend. IV. Karl Touset appeals the denial of his motions to suppress

the child pornography found on electronic devices that he carried with him when

he entered the country and the fruit of later searches. We recently held that the

Fourth Amendment does not require a warrant or probable cause for a forensic

search of a cell phone at the border. United States v. Vergara, 884 F.3d 1309 (11th

Cir. 2018). Touset argues that, in the light of the decision of the Supreme Court in

Riley v. California, 134 S. Ct. 2473 (2014), reasonable suspicion was required for

the forensic searches of his electronic devices. But our precedents about border

searches of property make clear that no suspicion is necessary to search electronic

devices at the border. Alternatively, the border agents had reasonable suspicion to

search Touset’s electronic devices. We affirm.

                                I. BACKGROUND

      After a series of investigations by private organizations and the government

suggested that Karl Touset was involved with child pornography, border agents

forensically searched his electronic devices after he arrived at the Atlanta airport

on an international flight. Xoom, a company that transmits money, identified

several people it suspected were involved with child pornography based on a

pattern of “frequent low money transfers to” individuals in “source countries for



                                          2
             Case: 17-11561     Date Filed: 05/23/2018   Page: 3 of 25


sex tourism and child pornography,” including the Philippines. Xoom alerted the

National Center for Missing and Exploited Children and notified Yahoo because

some of the people it suspected were involved with child pornography used Yahoo

email and messenger accounts.

      Yahoo then conducted its own investigation into the accounts identified by

Xoom and found a file with child pornography in the account for the email address

iloveyousomuch0820@yahoo.com. This email account listed a phone number in

the Philippines. Yahoo then sent tips to the National Center, which notified the

Cyber Crime Center of the Department of Homeland Security.

      While performing its own investigation, the Cyber Center subpoenaed

transaction data related to the iloveyousomuch0820@yahoo.com email account

and the Philippine phone number associated with it from several companies that

transmit money. One of those companies, Western Union, provided information

about an account associated with the Philippine phone number. The information

established that an account that listed Touset’s name and a post office box in

Marietta, Georgia, had sent three payments to the account associated with the

Philippine phone number. In March 2013, the account associated with Touset sent

a payment of $35 to the account associated with the Philippine phone number; in

April 2013, it sent another payment of $35; and in July 2013, it sent a payment of

$37. Based on this information, the Department placed a “look-out” on Touset so



                                         3
              Case: 17-11561    Date Filed: 05/23/2018    Page: 4 of 25


that his luggage and electronic devices would be searched when he returned to the

country.

      After Touset arrived on an international flight at the airport in Atlanta,

Georgia, on December 21, 2014, Derek Escobar, an officer of the Customs and

Border Protection Agency, inspected Touset’s luggage. Touset had two iPhones, a

camera, two laptops, two external hard drives, and two tablets. Escobar manually

inspected the iPhones and the camera, found no child pornography, and returned

those devices to Touset. But the Agency detained the remaining electronic devices,

and computer forensic analysts at the Department later searched them. Forensic

searches revealed child pornography on the two laptops and the two external hard

drives.

      Based on that information, Dianna Ford, a special agent of the Department,

obtained a warrant to search Touset’s home in Marietta, Georgia. Ford and about

14 other agents executed the warrant on January 28, 2015. During the execution of

the warrant, Ford and another agent read Touset his rights under Miranda v.

Arizona, 384 U.S. 436 (1966), and recorded an interview with him. Ford arrested

Touset after that interview.

      Evidence obtained by the government established that Touset purchased

thousands of images of child pornography. Over the course of several years,

Touset sent more than $55,000 to the Philippines for pornographic pictures, videos,



                                          4
              Case: 17-11561     Date Filed: 05/23/2018    Page: 5 of 25


and webcam sessions. In some webcam sessions, he instructed prepubescent girls

to display and manipulate their genitals. Touset also created an Excel spreadsheet

that documented the names, ages, and birthdates of those young girls as well as his

notes about them.

      A grand jury indicted Touset on three counts: knowingly receiving child

pornography, 18 U.S.C. § 2252(a)(2) & (b)(1); knowingly transporting and

shipping child pornography, 18 U.S.C. § 2252(a)(1) & (b)(1); and knowingly

possessing a computer and computer-storage device containing child pornography,

18 U.S.C. § 2252(a)(4)(B) & (b)(2). Touset initially pleaded not guilty to the

charges.

      Touset filed motions to suppress the evidence obtained from his electronic

devices at the border, as well as the fruit of those searches. After an evidentiary

hearing at which Escobar and Ford testified, the magistrate judge recommended

denying Touset’s motions to suppress. The magistrate judge explained that the

parties agreed that the government “needed reasonable suspicion of criminal

activity in order to lawfully detain for further analysis and search [Touset’s]

electronic devices.” The magistrate judge found that reasonable suspicion was

present because “[t]he collective information of the officers allowed the reasonable

inference that Touset had made three small payments through Western Union to an

entity in the Philippines, a country known for child exploitation,” and that entity



                                           5
              Case: 17-11561    Date Filed: 05/23/2018    Page: 6 of 25


“used an email address that had previously received or sent child pornography.”

And the magistrate judge rejected Touset’s argument that, because his most recent

payment to the Western Union account associated with the Philippine phone

number occurred about one-and-a-half years before his electronic devices were

searched, that evidence was stale. Instead, the magistrate judge found that the

evidence of Touset’s payments was not stale because “[f]iles on a computer are

less likely than other types of contraband to disappear over time and can often be

recovered even if they are deleted.”

      The district court adopted the magistrate judge’s report and recommendation

over Touset’s objections. The district court relied on the decision of the Ninth

Circuit in United States v. Cotterman, 709 F.3d 952, 968 (9th Cir. 2013) (en banc),

and concluded that reasonable suspicion is required for a forensic search of

electronic devices at the border. The district court found that reasonable suspicion

existed for the detention and forensic search of Touset’s electronic devices. And

the district court agreed with the magistrate judge that the evidence was not stale.

      Touset pleaded guilty to knowingly transporting child pornography, but

reserved his right to appeal the denial of his motion to suppress. The government

dismissed the other two counts. And the district court sentenced Touset to 120

months of imprisonment and supervision for life.




                                          6
              Case: 17-11561     Date Filed: 05/23/2018    Page: 7 of 25


                           II. STANDARD OF REVIEW

      “Because rulings on motions to suppress involve mixed questions of fact and

law, we review the district court’s factual findings for clear error, and its

application of the law to the facts de novo.” United States v. Ransfer, 749 F.3d 914,

921 (11th Cir. 2014) (quoting United States v. Bervaldi, 226 F.3d 1256, 1262 (11th

Cir. 2000)). We construe “all facts . . . in the light most favorable to the prevailing

party below.” Id. (quoting Bervaldi, 226 F.3d at 1262). And “[t]he individual

challenging the search bears the burdens of proof and persuasion.” United States v.

Newsome, 475 F.3d 1221, 1224 (11th Cir. 2007) (citation and internal quotation

marks omitted).

                                  III. DISCUSSION

      We divide our discussion in two parts. First, we explain that the Fourth

Amendment does not require any suspicion for forensic searches of electronic

devices at the border. Second, we explain that, in the alternative, the searches of

Touset’s electronic devices were supported by reasonable suspicion.

   A. The Fourth Amendment Permits Forensic Searches of Electronic Devices
                       at the Border Without Suspicion.

      The Fourth Amendment to the Constitution provides, “The right of the

people to be secure in their persons, houses, papers, and effects, against

unreasonable searches and seizures, shall not be violated, and no Warrants shall

issue, but upon probable cause . . . .” U.S. Const. amend. IV. Ordinarily,


                                           7
              Case: 17-11561    Date Filed: 05/23/2018    Page: 8 of 25


“reasonableness requires the obtaining of a judicial warrant.” United States v.

Vergara, 884 F.3d 1309, 1312 (11th Cir. 2018) (alteration adopted) (quoting Riley

v. California, 134 S. Ct. 2473, 2482 (2014)). But border searches are different. Id.

      As we recently reiterated, searches at the border of the country “‘never’

require probable cause or a warrant.” Id. (quoting United States v. Ramsey, 431

U.S. 606, 619 (1977)). The First Congress—the same one that proposed the Fourth

Amendment—empowered customs officials to stop and search without a warrant

any vessel or cargo suspected of illegally entering our nation. See Act of July 31,

1789, ch. 5, § 24, 1 Stat. 29, 43 (1789); Ramsey, 431 U.S. at 616–17 (“The

historical importance of the enactment of this customs statute by the same

Congress which proposed the Fourth Amendment is, we think, manifest.”); Boyd v.

United States, 116 U.S. 616, 623 (1886) (“[I]t is clear that the members of that

body did not regard searches and seizures of [contraband] as ‘unreasonable,’ and

they are not embraced within the prohibition of the [Fourth] [A]mendment.”). And

a year later, Congress expanded that power by permitting customs officials to

board vessels even before they reached the United States. See Act of Aug. 4, 1790,

ch. 35, § 31, 1 Stat. 145, 164–65 (1790); United States v. Villamonte-Marquez, 462

U.S. 579, 584 (1983).

      “Import restrictions and searches of persons or packages at the national

borders rest on different considerations and different rules of constitutional law



                                          8
              Case: 17-11561     Date Filed: 05/23/2018    Page: 9 of 25


from domestic regulations.” United States v. 12 200-Ft. Reels of Super 8MM. Film,

413 U.S. 123, 125 (1973). Congress has “broad powers . . . to prevent smuggling

and to prevent prohibited articles from entry,” id., under its plenary authority “[t]o

lay and collect Taxes, Duties, Imposts and Excises,” U.S. Const. art. I, § 8, cl. 1,

“[t]o regulate Commerce with foreign Nations,” id. art. I, § 8, cl. 3, and “[t]o

establish a[] uniform Rule of Naturalization,” id. art. I, § 8, cl. 4. And because

child pornography is unprotected by the First Amendment, “Congress may declare

it contraband and prohibit its importation.” United States v. Thirty-Seven

Photographs, 402 U.S. 363, 376–77 (1971) (plurality opinion); accord 12 200-Ft.

Reels, 413 U.S. at 128–29; see also Osborne v. Ohio, 495 U.S. 103, 111 (1990)

(“[W]e cannot fault [the government] for attempting to stamp out [child

pornography] at all levels in the distribution chain.”).

      Ordinarily, searches at the border are reasonable without suspicion “simply

by virtue of the fact that they occur at the border.” United States v. Alfaro-

Moncada, 607 F.3d 720, 728 (11th Cir. 2010) (quoting Denson v. United States,

574 F.3d 1318, 1339 (11th Cir. 2009)). The Supreme Court has held that it is

reasonable to conduct without suspicion “[r]outine searches of the persons and

effects of entrants” at our borders. United States v. Montoya de Hernandez, 473

U.S. 531, 538 (1985). And we have similarly explained that, at the border, routine

“pat-down search[es] or frisk[s]” and searches of “[a] traveler’s luggage,”



                                           9
             Case: 17-11561     Date Filed: 05/23/2018    Page: 10 of 25


“[i]ncoming international mail,” and “[v]ehicles” are all reasonable “without any

level of suspicion.” Alfaro-Moncada, 607 F.3d at 728 (collecting cases). A

traveler’s “right to be let alone neither prevents the search of his luggage nor the

seizure of unprotected, but illegal, materials when his possession of them is

discovered during . . . a search.” Thirty-Seven Photographs, 402 U.S. at 376

(plurality opinion).

      The Supreme Court has never required reasonable suspicion for a search of

property at the border, however non-routine and intrusive, and neither have we.

Although in one decision the Supreme Court required reasonable suspicion for the

prolonged detention of a person until she excreted the contraband that she was

suspected of “smuggling . . . in her alimentary canal” or submitted to an x-ray or

rectal examination, Montoya de Hernandez, 473 U.S. at 541; see also id. at 534–

35, it has never applied this requirement to property. Nor has it “been willing to

distinguish . . . between different types of property.” Cotterman, 709 F.3d at 975

(Callahan, J., concurring in part, dissenting in part, and concurring in the

judgment). Indeed, it held in United States v. Flores-Montano that the government

may “remove, disassemble, and reassemble a vehicle’s fuel tank” at the border

without any suspicion. 541 U.S. 149, 155 (2004). It explained that “the reasons that

might support a requirement of some level of suspicion in the case of highly

intrusive searches of the person—dignity and privacy interests of the person being



                                          10
             Case: 17-11561      Date Filed: 05/23/2018    Page: 11 of 25


searched—simply do not carry over to vehicles.” Id. at 152. And it rejected a

judicial attempt to distinguish between “routine” and “nonroutine” searches and to

craft “[c]omplex balancing tests to determine what [constitutes] a ‘routine’ search

of a vehicle, as opposed to a more ‘intrusive’ search of a person.” Id. We have

been similarly unwilling to distinguish between different kinds of property. For

example, we have upheld “a search without reasonable suspicion of a crew

member’s living quarters on a foreign cargo vessel that [wa]s entering this

country,” Alfaro-Moncada, 607 F.3d at 727, even though “[a] cabin is a crew

member’s home—and a home ‘receives the greatest Fourth Amendment

protection,’” id. at 729 (quoting United States v. McGough, 412 F.3d 1232, 1236

(11th Cir. 2005)); accord id. at 732.

      We see no reason why the Fourth Amendment would require suspicion for a

forensic search of an electronic device when it imposes no such requirement for a

search of other personal property. Just as the United States is entitled to search a

fuel tank for drugs, see Flores-Montano, 541 U.S. at 155, it is entitled to search a

flash drive for child pornography. And it does not make sense to say that electronic

devices should receive special treatment because so many people now own them or

because they can store vast quantities of records or effects. The same could be said

for a recreational vehicle filled with personal effects or a tractor-trailer loaded with

boxes of documents. Border agents bear the same responsibility for preventing the



                                           11
             Case: 17-11561      Date Filed: 05/23/2018    Page: 12 of 25


importation of contraband in a traveler’s possession regardless of advances in

technology. Indeed, inspection of a traveler’s property at the border “is an old

practice and is intimately associated with excluding illegal articles from the

country.” Thirty-Seven Photographs, 402 U.S. at 376 (plurality opinion).

      In contrast with searches of property, we have required reasonable suspicion

at the border only “for highly intrusive searches of a person’s body.” Alfaro-

Moncada, 607 F.3d at 729. Even though the Supreme Court has declined to decide

“what level of suspicion, if any, is required for [such] nonroutine border searches

[of a person],” Montoya de Hernandez, 473 U.S. at 541 n.4, we have required

reasonable suspicion for “a strip search or an x-ray examination,” Alfaro-Moncada,

607 F.3d at 729. We have defined the “intrusiveness” of a search of a person’s

body that requires reasonable suspicion “in terms of the indignity that will be

suffered by the person being searched,” in contrast with “whether one search will

reveal more than another.” United States v. Vega-Barvo, 729 F.2d 1341, 1345

(11th Cir. 1984); accord id. at 1346. And “we have isolated three factors which

contribute to the personal indignity endured by the person searched: (1) physical

contact between the searcher and the person searched; (2) exposure of intimate

body parts; and (3) use of force.” Id. at 1346.

      These factors are irrelevant to searches of electronic devices. A forensic

search of an electronic device is not like a strip search or an x-ray; it does not



                                           12
             Case: 17-11561      Date Filed: 05/23/2018    Page: 13 of 25


require border agents to touch a traveler’s body, to expose intimate body parts, or

to use any physical force against him. Although it may intrude on the privacy of

the owner, a forensic search of an electronic device is a search of property. And

our precedents do not require suspicion for intrusive searches of any property at the

border. See Alfaro-Moncada, 607 F.3d at 728–29, 732.

      To be sure, the Fourth and the Ninth Circuits have concluded—in divided

decisions—that the Fourth Amendment requires at least reasonable suspicion for

forensic searches of electronic devices at the border. United States v. Kolsuz, ___

F.3d ____, No. 16-4687, slip op. at 19 (4th Cir. May 9, 2018); Cotterman, 709

F.3d at 968. In Cotterman, the Ninth Circuit equated a forensic search to “a

computer strip search,” 709 F.3d at 966, and stated that “[s]uch a thorough and

detailed search of the most intimate details of one’s life is a substantial intrusion

upon personal privacy and dignity,” id. at 968. And it reasoned that

“[i]ntrusiveness includes both the extent of a search as well as the degree of

indignity that may accompany a search.” Id. at 967 (quoting United States v.

Ramos-Saenz, 36 F.3d 59, 61 n.3 (9th Cir. 1994)). The Fourth Circuit later

explained that the intervening decision of the Supreme Court in Riley “confirmed”

that reasoning. Kolsuz, slip op. at 21. And it revived the distinction between routine

and nonroutine searches of property, see id. at 19–24, that the Supreme Court

rejected in Flores-Montano, 541 U.S. at 152.



                                           13
             Case: 17-11561     Date Filed: 05/23/2018    Page: 14 of 25


      We are unpersuaded. Although the Supreme Court stressed in Riley that the

search of a cell phone risks a significant intrusion on privacy, our decision in

Vergara made clear that Riley, which involved the search-incident-to-arrest

exception, does not apply to searches at the border. 884 F.3d at 1312 (“[T]he

Supreme Court expressly limited its holding to the search-incident-to-arrest

exception.”). And our precedent considers only the “personal indignity” of a

search, not its extensiveness. Vega-Barvo, 729 F.2d at 1346. Again, we fail to see

how the personal nature of data stored on electronic devices could trigger this kind

of indignity when our precedent establishes that a suspicionless search of a home at

the border does not. See Alfaro-Moncada, 607 F.3d at 729, 732. Property and

persons are different. See Flores-Montano, 541 U.S. at 152.

      We are also unpersuaded that a traveler’s privacy interest should be given

greater weight than the “paramount interest [of the sovereign] in protecting . . . its

territorial integrity.” Id. at 153. The Ninth and Fourth Circuits stressed the former

interest and asserted that travelers have no practical options to protect their privacy

when traveling abroad. For example, the Ninth Circuit explained that it is

“impractical, if not impossible, for individuals to make meaningful decisions

regarding what digital content to expose to the scrutiny that accompanies

international travel” and that “removing files unnecessary to an impending trip” is

“a time-consuming task that may not even effectively erase the files.” Cotterman,



                                          14
             Case: 17-11561     Date Filed: 05/23/2018    Page: 15 of 25


709 F.3d at 965. The Fourth Circuit added that “it is neither ‘realistic nor

reasonable to expect the average traveler to leave his digital devices at home when

traveling.’” Kolsuz, slip op. at 21 (quoting United States v. Saboonchi, 990 F.

Supp. 2d 536, 556 (D. Md. 2014)). But a traveler’s “expectation of privacy is less

at the border,” Flores-Montano, 541 U.S. at 154, and the Fourth Amendment does

not guarantee the right to travel without great inconvenience, even within our

borders, see Corbett v. Transp. Sec. Admin., 767 F.3d 1171, 1179 (11th Cir. 2014)

(holding that airport screening “is a reasonable administrative search under the

Fourth Amendment”); see also Kolsuz, slip op. at 34 (Wilkinson, J., concurring in

the judgment) (“Our new world has brought inconvenience and intrusions on an

indiscriminate basis, which none of us welcome, but which most of us undergo in

the interest of assuring a larger common good.”). Anyone who has recently taken a

domestic flight likely experienced inconvenient screening procedures that require

passengers to unpack electronic devices, separate and limit liquids, gels, and

creams, remove their shoes, and walk through a full-body scanner. See Corbett,

767 F.3d at 1174 (explaining that a traveler must walk through a scanner or

undergo a pat-down in airports). Travelers “crossing a border . . . [are] on notice

that a search may be made,” Alfaro-Moncada, 607 F.3d at 732 (quoting United

States v. Hidalgo-Gato, 703 F.2d 1267, 1271 (11th Cir. 1983)), and they are free to

leave any property they do not want searched—unlike their bodies—at home.



                                          15
             Case: 17-11561     Date Filed: 05/23/2018   Page: 16 of 25


      In contrast with the diminished privacy interests of travelers, “[t]he

Government’s interest in preventing the entry of unwanted persons and effects is at

its zenith at the international border.” Flores-Montano, 541 U.S. at 152. As we

have explained, child pornography, no less than drugs or other kinds of contraband,

is prohibited from “enter[ing] the country,” Ramsey, 431 U.S. at 620, and the

government interest in stopping contraband at the border does not depend on

whether child pornography takes the form of digital files or physical photographs.

      Nothing in Riley undermines this interest. In Riley, the Supreme Court

explained that the rationales that support the search-incident-to-arrest exception—

namely the concerns of “harm to officers and destruction of evidence”—did not

“ha[ve] much force with respect to digital content on cell phones,” 134 S. Ct. at

2484, because “digital data” does not pose “comparable risks,” id. at 2485. But

“digital” child pornography poses the same exact “risk” of unlawful entry at the

border as its physical counterpart. If anything, the advent of sophisticated

technological means for concealing contraband only heightens the need of the

government to search property at the border unencumbered by judicial second-

guessing.

      Indeed, if we were to require reasonable suspicion for searches of electronic

devices, we would create special protection for the property most often used to

store and disseminate child pornography. With the advent of the internet, child



                                          16
               Case: 17-11561   Date Filed: 05/23/2018   Page: 17 of 25


pornography offenses overwhelmingly involve the use of electronic devices for the

receipt, storage, and distribution of unlawful images. See U.S. Sent’g Comm’n,

Federal Child Pornography Offenses 5, 71 (2012); see also United States v.

Williams, 553 U.S. 285, 307 (2008) (“Both the State and Federal Governments

have sought to suppress [child pornography] for many years, only to find it

proliferating through the new medium of the Internet.”). And law enforcement

officers routinely investigate child-pornography offenses by forensically searching

an individual’s electronic devices. See U.S. Sent’g Comm’n, supra, at 67–71. We

see no reason why we would permit traditional, invasive searches of all other kinds

of property, see Alfaro-Moncada, 607 F.3d at 724–25, 728, 732, but create a

special rule that will benefit offenders who now conceal contraband in a new kind

of property.

      After all, our nation has classified child pornography as contraband for good

reason. The possession of child pornography “harms and debases the most

defenseless of our citizens,” Williams, 553 U.S. at 307, in profound and lasting

ways. The harm that victims suffer during the production of child pornography “is

exacerbated by the[] circulation” of “a permanent record of the child[’s]

participation.” New York v. Ferber, 458 U.S. 747, 759 (1982); see also U.S. Sent’g

Comm’n, supra, at 118. Victims know that countless people may obtain their

images, see United States v. Pugh, 515 F.3d 1179, 1196 (11th Cir. 2008), and use



                                         17
             Case: 17-11561     Date Filed: 05/23/2018    Page: 18 of 25


them for sexual gratification, see U.S. Sent’g Comm’n, supra, at 113, 118. Victims

also know that their images may contribute to the abuse of new victims. See id.

The online promotion and sharing of child pornography validates the sexual

exploitation of children and “may incite or encourage others to sexually abuse

children.” United States v. Irey, 612 F.3d 1160, 1208 (11th Cir. 2010) (en banc);

see also U.S. Sent’g Comm’n, supra, at 312. And there is evidence that offenders

use child pornography to convince children to participate in their abuse. U.S.

Sent’g Comm’n, supra, at 312. Consumers of child pornography who “‘merely’ or

‘passively’ receive or possess child pornography directly contribute to this

continuing victimization.” Pugh, 515 F.3d at 1196 (quoting United States v. Goff,

501 F.3d 250, 259 (3d Cir. 2007)). And “[t]he greater the customer demand for

child pornography, the more that will be produced.” Irey, 612 F.3d at 1212

(quoting United States v. Goldberg, 491 F.3d 668, 672 (7th Cir. 2007)). We should

not invent heightened constitutional protection for travelers who cross our borders

with this contraband in tow.

      Of course, nothing prevents Congress from enacting laws that provide

greater protections than the Fourth Amendment requires. Indeed, Congress has

repeatedly exercised this power “to strike a balance between privacy and security

in the context of digital searches.” Kolsuz, slip op. at 32 (Wilkinson, J., concurring

in the judgment) (citing USA Freedom Act of 2015, Pub. L. No. 114-23, 129 Stat.



                                          18
             Case: 17-11561     Date Filed: 05/23/2018    Page: 19 of 25


268; Wiretap Act, Pub. L. No. 90-351, 82 Stat. 197 (1961), amended by Electronic

Communications Privacy Act of 1986, Pub. L. No. 99-508, 100 Stat. 1848, and

Communications Assistance for Law Enforcement Act, Pub. L. No. 103-414, 108

Stat. 4279 (1994) (codified as amended at 18 U.S.C. §§ 2510–2522 (2012)); Orin

S. Kerr, The Effect of Legislation on Fourth Amendment Protection, 115 Mich. L.

Rev. 1117, 1120 (2017)). The First Congress required officers to have “reason to

suspect” the concealment of “goods, wares or merchandise subject to duty” before

the officers could “enter any ship or vessel” “to search for, seize, and secure any

such goods, wares or merchandise.” Act of July 31, 1789, ch. 5, § 24, 1 Stat. at 43.

More recently, Congress enacted special protections for financial records in the

Right to Financial Privacy Act of 1978, Pub. L. No. 95-630, tit. XI, 92 Stat. 3641,

3697 (codified at 12 U.S.C. § 3408), and for cell tower location information in the

Stored Communications Act, Pub. L. No. 99-508, tit. II, 100 Stat. 1848, 1860

(1986) (codified at 18 U.S.C. §§ 2701–2712;); see also United States v. Davis, 785

F.3d 498, 519 (11th Cir. 2015) (en banc) (W. Pryor, J., concurring) (explaining that

the Stored Communications Act provides “additional protections” for that

information).

      Instead of “charging unnecessarily ahead,” we must allow Congress to

design the appropriate standard “through the more adaptable legislative process

and the wider lens of legislative hearings.” Kolsuz, slip op. at 30, 31 (Wilkinson, J.,



                                          19
              Case: 17-11561     Date Filed: 05/23/2018     Page: 20 of 25


concurring in the judgment). Such a “legislative process would be informed by

numerous representatives of the executive branch, who can lend their practical

insights and experience to the inquiry.” Id. at 33. “The dangers of judicial

standard-setting in an area as sensitive as border searches [are] . . . apparent.” Id.

“Simply put, we must apply the law and leave the task of developing new rules for

rapidly changing technologies to the branch most capable of weighing the costs

and benefits of doing so.” Davis, 785 F.3d at 520 (W. Pryor, J., concurring).

Judicial restraint is especially important in the context of border searches, “where

there is a longstanding historical practice . . . of deferring to the legislative and

executive branches.” Kolsuz, slip op. at 36 (Wilkinson, J., concurring in the

judgment).

        B. In the Alternative, Reasonable Suspicion Existed for the Forensic
                        Searches of Touset’s Electronic Devices.
      Alternatively, the district court correctly denied Touset’s motions to

suppress because the forensic searches of his electronic devices were supported by

reasonable suspicion. Touset argues that the government lacked reasonable

suspicion because the evidence that he sent three separate payments to the Western

Union account associated with a Philippine phone number was stale and because

the evidence did not show that he had possessed child pornography or would

possess it on his electronic devices. We disagree.




                                           20
              Case: 17-11561    Date Filed: 05/23/2018   Page: 21 of 25


      “Reasonable suspicion . . . must be based upon a ‘particularized and

objective basis for suspecting the particular person of criminal activity.’” Denson,

574 F.3d at 1341 (alteration adopted) (quoting United States v. Cortez, 449 U.S.

411, 417–18 (1981)). The “inquiry focuses on the information available to the

officers at the time of the stop.” United States v. Lewis, 674 F.3d 1298, 1305 (11th

Cir. 2012).

      The government had a “particularized and objective basis for suspecting”

that Touset possessed child pornography on his electronic devices. Denson, 574

F.3d at 1341 (citation and internal quotation marks omitted). The government

knew that Touset had sent three low-money transfers of $35, $35, and $37 to a

Western Union account; that the Western Union account was associated with a

Philippine phone number that was associated with the email account of

iloveyousomuch0820@yahoo.com; that the email account had contained an image

of child pornography; that the Philippines was a source country for child

pornography; that a pattern of “frequent low money transfers” is associated with

child pornography; and that Touset was traveling with nine electronic devices.

Together, this evidence provided reasonable suspicion for the forensic searches of

Touset’s electronic devices.

      The “staleness doctrine . . . requires that the information supporting the

government’s application for a warrant must show that probable cause exists at the



                                         21
             Case: 17-11561      Date Filed: 05/23/2018    Page: 22 of 25


time the warrant issues.” Bervaldi, 226 F.3d at 1264. And the staleness doctrine

also applies to reasonable suspicion. Id. at 1264–65; see also United States v.

Carter, 566 F.3d 970, 975 (11th Cir. 2009). “[S]taleness is an issue that courts

must decide by evaluating the facts of a particular case . . . .” United States v.

Domme, 753 F.2d 950, 953 (11th Cir. 1985). Courts consider “the length of time”

as well as “the nature of the suspected crime (discrete crimes or ongoing

conspiracy), habits of the accused, character of the items sought, and nature and

function of the premises to be searched.” Bervaldi, 226 F.3d at 1265 (citation and

internal quotation marks omitted). We have explained that “[t]here is no particular

rule or time limit for when information becomes stale.” Id.

      Our sister circuits have repeatedly rejected staleness challenges in appeals

involving child pornography. They have observed that “pedophiles rarely, if ever,

dispose of child pornography.” United States v. Zimmerman, 277 F.3d 426, 434 (3d

Cir. 2002); see also United States v. Burkhart, 602 F.3d 1202, 1206–07 (10th Cir.

2010); United States v. Morales-Aldahondo, 524 F.3d 115, 119 (1st Cir. 2008);

United States v. Hay, 231 F.3d 630, 636 (9th Cir. 2000). And probable cause of

involvement in electronic child pornography remains even longer because deleted

files can remain on electronic devices. See United States v. Frechette, 583 F.3d

374, 379 (6th Cir. 2009); Hay, 231 F.3d at 636. As the Tenth Circuit explained,

“information that a person received electronic images of child pornography is less



                                           22
             Case: 17-11561     Date Filed: 05/23/2018   Page: 23 of 25


likely than information about drugs, for example, to go stale because the electronic

images are not subject to spoilage or consumption.” Burkhart, 602 F.3d at 1207.

And other circuits have ruled that probable cause remained after passages of time

similar to the interval here. See, e.g., Frechette, 583 F.3d at 378–79 (16 months);

Morales-Aldahondo, 524 F.3d at 119 (three years).

      We are persuaded that the reasoning of our sister circuits applies in this

circumstance. The evidence that Touset made three separate payments to the

Western Union account associated with the Philippine phone number was not stale

about a year and a half later. That evidence suggested that Touset likely received

child pornography electronically and had child pornography stored on his

electronic devices.

                                IV. CONCLUSION

      We AFFIRM Touset’s judgment of conviction and sentence.




                                         23
             Case: 17-11561     Date Filed: 05/23/2018    Page: 24 of 25


CORRIGAN, District Judge, concurring in part and concurring in the judgment:

      I concur in the majority opinion, except as to Part III.A. As the Court notes,

the Fourth and Ninth Circuits have concluded that the Fourth Amendment requires

at least reasonable suspicion for forensic searches of electronic devices at the

border. See Maj. Op. at 13, citing United States v. Kolsuz, __ F.3d __, No. 16-

4687, slip op. at 19 (4th Cir. May 9, 2018), and United States v. Cotterman, 709

F.3d 952, 968 (9th Cir. 2013). In the district court, the government agreed that the

applicable Fourth Amendment test was whether there was reasonable suspicion of

criminal activity such that border agents could detain Touset’s electronic devices

for forensic analysis. The district court found reasonable suspicion and upheld the

search.

      However, on appeal, the government goes beyond its position in the district

court and argues that border agents need no justification whatsoever to detain (in

this case for seventeen days) and forensically search electronic devices of any

American citizen returning from abroad. This new-found government position

presents a different and difficult question, one not addressed by the Supreme Court

or (until today) any appellate court. In my view, this Court need not reach this

issue to decide this case. I therefore concur only in the Court’s alternative holding

that “the district court correctly denied Touset’s motions to suppress because the




                                          24
             Case: 17-11561    Date Filed: 05/23/2018   Page: 25 of 25


forensic searches of his electronic devices were supported by reasonable

suspicion.” Maj. Op. at 21.




                                        25

```

---

## GROUP: content/cases/United States v. Vaneaton.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Vaneaton
type: case
citation: "49 F.3d 1423 (1995)"
parallel_cite: 95 Daily Journal DAR 3223
neutral_cite: "95 Cal. Daily Op. Serv. 1884; 1995 U.S. App. LEXIS 4793; 1995 WL 101835"
court: 9th Cir.
court_level: coa
circuit: ca9
year: 1995
date_decided: 1995-03-13
docket: 93-30387
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
  opinion_url: "https://www.courtlistener.com/opinion/691388/united-states-v-jack-palmer-vaneaton/"
  cluster_id: 691388
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Vaneaton
  status: under_review
  projected_at: 2026-07-08
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — voluntary-exposure pole (voluntary doorway exposure = no Payton violation, 49 F.3d at 1426-27)"
  - page: "[[Arrest in the Home]]"
    role: "Related — cross-doctrine (doorway arrests)"
---

# United States v. Vaneaton

*49 F.3d 1423 (9th Cir. 1995)* (No. 93-30387) · U.S. Court of Appeals, 9th Cir. · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 691388 / lead opinion 9487908 → 49 F.3d 1423, No. 93-30387, decided 1995-03-13 (Trott, J.; Tashima, J., dissenting). Rule/Application quotes string-matched to the CL opinion text 2026-07-08. ENRICH-CONFIRM: exact star-pages (1426/1427) inferred from block ids; finalize at mint enrich via read_document offsets. -->

## Background
Bend, Oregon officers with probable cause to arrest John Vaneaton for receiving stolen property went to his motel room without a warrant and knocked. Vaneaton saw the uniformed officers through the window and opened the door; he was arrested while "standing just inside the open door of his motel room." The police did not cross the threshold until after they announced the arrest. Vaneaton moved to suppress, arguing the warrantless arrest violated *[[Payton v. New York]]*; the magistrate found he had opened the door voluntarily and without coercion, and the district court denied suppression.

## Issue
Whether a suspect who opens his door in response to a noncoercive police knock and is arrested at the open doorway is protected by *[[Payton v. New York|Payton]]*'s bar on warrantless in-home arrests, or whether he has voluntarily exposed himself to a warrantless arrest.

## Rule
The dispositive question is voluntary exposure, not the suspect's exact position at the threshold. "As we read the controlling authority, the question presented in this case is not decided only on the basis of whether Vaneaton was standing inside or outside the threshold of his room, but whether he 'voluntarily exposed himself to warrantless arrest' by freely opening the door of his motel room to the police." 49 F.3d at 1426 (quoting *United States v. Johnson*, 626 F.2d 753, 757 (9th Cir. 1980)). ^pin-1426

If he so exposed himself, the *[[Payton v. New York|Payton]]* presumption is overcome: "implicit in *Johnson* is approval of the warrantless arrest of a suspect who voluntarily opens the door of his dwelling in response to a noncoercive knock by the police." *Id.* at 1427. ^pin-1427

## Application
The record showed voluntary exposure. "When Vaneaton saw them through the window, he voluntarily opened the door and exposed both himself and the immediate area to them. No threats or force were used by the police to get him to open the door, and his actions were not taken in response to a claim of lawful authority. The police did not enter the house until they formally placed Vaneaton under arrest." 49 F.3d at 1427. ^pin-1427b

Because voluntariness is a factual finding reviewed only for [[Common Legal Terms#clear-error|clear error]] (*[[United States v. Al-Azzawy]]*, 784 F.2d 890, 895 (9th Cir. 1986)), and the magistrate's findings were supported, no *[[Payton v. New York|Payton]]* violation occurred.

## Conclusion
Affirmed. A suspect who voluntarily opens his door to a noncoercive knock and is arrested at the doorway has exposed himself to a lawful warrantless arrest; *[[Payton v. New York|Payton]]* is not offended. (Tashima, J., dissented, reading the result as contrary to *[[Payton v. New York|Payton]]*.)

## Treatment & subsequent history
- **Status:** ⚪ unverified (frontier stub) — **Binding in-circuit — 9th Cir.** Treatment/progeny not machine-certified until S9 promotion.
- *Vaneaton* is the voluntary-exposure pole of the Ninth-Circuit surround-and-call-out line — the containment-vs-exit-command contrast to *[[United States v. Al-Azzawy]]* (coerced emergence) and *[[United States v. Nora]]* (surround-and-summon under overwhelming force). The line turns on voluntariness: a free response to a noncoercive knock forfeits *[[Payton v. New York|Payton]]*'s protection; a coerced emergence under a show of force does not.

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 691388 + 49 F.3d 1423); renders under the ⚪ banner until S9 promotion.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Limiting*

## Sources
- [*United States v. Vaneaton*, 49 F.3d 1423 (9th Cir. 1995)](https://www.courtlistener.com/opinion/691388/united-states-v-vaneaton/) — pinpoints: 1426 (voluntary-exposure question presented), 1427 (voluntary opening to a noncoercive knock overcomes *Payton*; distinguishing *Al-Azzawy* at 895); quotes string-matched to the CL opinion text 2026-07-08.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4c80133c513237fe", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "49 F.3d 1423 (1995)", "court": "9th Cir.", "neutral_cite": "95 Cal. Daily Op. Serv. 1884; 1995 U.S. App. LEXIS 4793; 1995 WL 101835", "official_citation_present": true, "parallel_cite": "95 Daily Journal DAR 3223", "title": "United States v. Vaneaton", "year": "1995"}}
{"assertion_id": "ac9e78c18c2287c8", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — voluntary-exposure pole (voluntary doorway exposure = no Payton violation, 49 F.3d at 1426-27)", "title": "United States v. Vaneaton"}}
{"assertion_id": "ef6eafec9002f389", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related — cross-doctrine (doorway arrests)", "title": "United States v. Vaneaton"}}
{"assertion_id": "77ec2a26df45fec7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Vaneaton"}}
{"assertion_id": "c5cc6a00381471e3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Vaneaton", "varies_by_point": "false"}}
```

### lake record — United States v. Vaneaton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Vaneaton",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Jack Palmer Vaneaton",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Jack Palmer VANEATON, Defendant-Appellant",
    "input_case_name": "United States v. Vaneaton",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "1995-03-13",
    "year": 1995,
    "docket": "93-30387",
    "cluster_id": 691388,
    "lead_opinion_id": 9487908,
    "sibling_ids": [],
    "absolute_url": "/opinion/691388/united-states-v-jack-palmer-vaneaton/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "49 F.3d 1423",
      "volume": "49",
      "reporter": "F.3d",
      "page": "1423",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "95 Daily Journal DAR 3223",
        "volume": "95",
        "reporter": "Daily Journal DAR",
        "page": "3223",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "95 Cal. Daily Op. Serv. 1884",
        "volume": "95",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. App. LEXIS 4793",
        "volume": "1995",
        "reporter": "U.S. App. LEXIS",
        "page": "4793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 WL 101835",
        "volume": "1995",
        "reporter": "WL",
        "page": "101835",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "49 F.3d 1423",
        "volume": "49",
        "reporter": "F.3d",
        "page": "1423",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 Daily Journal DAR 3223",
        "volume": "95",
        "reporter": "Daily Journal DAR",
        "page": "3223",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 Cal. Daily Op. Serv. 1884",
        "volume": "95",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. App. LEXIS 4793",
        "volume": "1995",
        "reporter": "U.S. App. LEXIS",
        "page": "4793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 WL 101835",
        "volume": "1995",
        "reporter": "WL",
        "page": "101835",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "49 F.3d 1423",
    "official_selection": {
      "court_class": "coa",
      "selected": "49 F.3d 1423",
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
    "date_created": "2026-07-08T16:52:45Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-vaneaton--691388",
      "to_record_id": "United States v. Vaneaton",
      "as_of": "2026-07-08T22:30:00Z",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Vaneaton

```
<opinion type="majority">
<p id="b1468-14">Opinion by Judge TROTT. Dissent by Judge TASHIMA.</p>
<author id="b1468-15">TROTT, Circuit Judge:</author>
<p id="b1468-16">John Vaneaton<footnotemark>1</footnotemark> was arrested on September 9, 1992, while standing just inside the open door of his motel room in Bend, Oregon. He was arrested without a warrant by officers of the Bend Police Department. He concedes that the police who arrested him for receiving stolen property had probable cause to do so, but he contends that the warrant-less arrest violated the rule of <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), a rule ordinarily requiring police to obtain a warrant before arresting a suspect inside his home, or in this case, inside his motel room.</p>
<p id="b1468-20">We have jurisdiction over this timely appeal pursuant to <span class="citation no-link">28 U.S.C. § 1291</span> and Fed. R.Crim.P. 11(e)(2). We affirm the district court’s denial of Vaneaton’s motion to suppress a revolver found in his motel room in connection with his arrest. This revolver was used to secure his conditional plea of guilty to a charge of felon in possession of a firearm.</p>
<p id="b1468-21">I</p>
<p id="b1468-22">On August 25, 1992, officers of the Portland Police Bureau arrested Vaneaton in Portland, Oregon on outstanding no-bail warrants charging him with a parole violation and contempt of court. He had failed to report as required to his parole officer. Va-neaton, a notorious, thrice-convicted burglar known by the police to operate primarily in the Willamette Valley and along the coast of Oregon, lived in Independence, Oregon, some 60 miles from Portland. He was known to have committed crimes in at least four counties: Polk, Lincoln, Jackson, and Multnomah.</p>
<p id="b1468-23">Around the time Vaneaton was arrested, he had been repeatedly selling goods to various pawn shops in the Portland area, an activity that attracted the attention of the police. Among the items he sold were pieces of jewelry that turned out to have been stolen during recent unsolved residential burglaries in the Bend, Oregon area. Bend is located in the middle of the state, approximately 150 miles from Portland, and 100 miles from Independence. When arrested, he had documents on his person indicating he had previously been in Bend. Vaneaton was <page-number citation-index="1" label="1425">*1425</page-number>released shortly after his arrest. The police were unaware of his release.</p>
<p id="b1469-4">As part of an investigation instigated as a result of Vaneaton’s possession of stolen property, and in order to determine if proof could be developed that Vaneaton had been in Bend precisely at the time of the crimes during which the jewelry was stolen, uniformed officers of the Bend Police Department were detailed on September 9, 1992, to tour motels in that area to look for such evidence. They found it at their first stop, the Rainbow Motel. Not only did they discover that Vaneaton had been in Bend at the time of the burglaries, but they also discovered to their surprise that he was back, and staying again in the Rainbow Motel for at least another night. This discovery was unexpected for two reasons. First, the Bend police believed he was still in custody for a parole violation. Second, it was counter intuitive to find him back at the scene of the crime.-</p>
<p id="b1469-5">Armed with this unexpected information, and now with ample probable cause to arrest him for receiving stolen property with respect to the recovered loot he possessed in Portland, the officers called for backup. When it arrived, they went directly to his motel room to see if he was there and to arrest him if he was. .</p>
<p id="b1469-6">Wearing their uniforms and with their guns in their holsters, the officers knocked on the door to Vaneaton’s room. They made no demands; in fact, they said nothing. According to the stipulated facts, Vaneaton opened the curtains of a window, saw the officers, and opened the door. Detective Carpenter asked him if he was Jack Vanea-ton, and when he said he was, he was arrested. At the moment of his arrest, Vaneaton was standing at the doorway but just inside the threshold.- The arresting officer was immediately outside the threshold of the' room and did not enter before advising Vaneaton he was under arrest. Vaneaton was then handcuffed, advised of his <em>Miranda </em>rights, and asked for permission to search the room. He gave verbal permission for such a search and signed a written consent form. Officer Reeves also asked him if he had a gun. Vaneaton said he did and directed them to a closet. The police then found a revolver where Vaneaton had told them it was located.</p>
<p id="b1469-8">II</p>
<p id="b1469-9">The issue Vaneaton raises is whether the police, acting with probable cause but without a warrant and while standing outside his motel room, could lawfully arrest him while he was standing immediately inside the open doorway. Relying on <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), and denying the existence of exigent circumstances, Vaneaton claims, the answer is clear: The arresting officers were required to have had a warrant.</p>
<p id="b1469-10">In <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>the Court drew a bright fine at the identifiable threshold of a protected dwelling and said such a line cannot be crossed !to arrest a suspect inside, absent consent or exigent circumstances:</p>
<blockquote id="b1469-11">The Fourth Amendment protects the individual’s privacy in a variety of settings. In none is the zone of privacy <em>more clearly defined </em>than when bounded by the <em>unambiguous physical dimensions </em>of an individual’s home — a zone that finds its roots in clear and specific constitutional terms: “The right of the people to be secure in their ... houses ... shall not be violated.” ... In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has <em>drawn a firm line </em>at the entrance to the house. Absent exigent circumstances, that <em>threshold </em>may not reasonably be crossed without a warrant.</blockquote>
<p id="b1469-12"><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U.S. at 589-90</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1381" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1381-82</a></span> (citations omitted) (emphasis added). The purpose of this rule is manifest from the rule itself: to protect an individual’s “zone of privacy.” Thus, the result of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>is that “seizures inside a home without a warrant are presumptively unreasonable.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><em>Id. </em>at 586</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1380" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1380</a></span>.</p>
<p id="b1469-13">The government’s response to Vaneaton’s claim is that a warrantless arrest at the doorway of a suspect’s dwelling is constitutionally proper, provided that law enforcement has not misidentified itself, has not used coercion, and the suspect acquiesces to the encounter. In support of this argument, the government invokes this Court’s discus<page-number citation-index="1" label="1426">*1426</page-number>sion in <em>United States v. Whitten, </em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/#1015" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">706 F.2d 1000, 1015-17</a></span> <em>(9th Cir,1983), cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./465/1100/">465 U.S. 1100</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./104/1593/">104 S.Ct. 1593</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/80/125/">80 L.Ed.2d 125</a></span> (1984), of the arrest of Whitten’s codefendant, John Gaiefsky, and <em>United States v. Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d 753</a></span> (9th Cir.1980), <em>aff'd, </em><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U.S. 537</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">102 S.Ct. 2579</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">73 L.Ed.2d 202</a></span> (1982). In <em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">Whitten</a></span>, </em>we held that Gaiefsky’s arrest while standing in the doorway of his hotel room did not violate <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>because “[a] doorway ..., unlike the interior of a hotel room, is a public place.” <span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/#1015" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">706 F.2d at 1015</a></span>. As authority for this proposition, we relied on <em>United States v. Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U.S. 38</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">96 S.Ct. 2406</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">49 L.Ed.2d 300</a></span> (1976).</p>
<p id="b1470-4">As we read the controlling authority, the question presented in this cáse is not decided only on the basis of whether Vaneaton was standing inside or outside the threshold of his room, but whether he “voluntarily exposed himself to warrantless arrest” by freely opening thé door of his motel room to the police. <em>Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#757" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 757</a></span>. If he so exposed himself, the presumption created by <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>is overcome. <em>See <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">id.</a></span></em><footnotemark><em>2</em></footnotemark></p>
<p id="b1470-5">A</p>
<p id="b1470-6">In resolving whether Vaneaton voluntarily exposed himself to warrantless arrest, we find considerable guidance in <em>United States v. Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d 753</a></span> (9th Cir.1980). In <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>, </em>the question before us was whether Johnson’s warrantless arrest as he stood at an open doorway within his home satisfied <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>We held that it did not because of the deceitful manner in which the door was caused by the arresting officers to.be opened. The agents had used a subterfuge to get Johnson to open the door, and because of their use of that subterfuge — they misrepresented. their identities — we held that “Johnson’s initial exposure to the view and the physical control of the agents was not consensual on his part.” <em>Id. </em>at 757.</p>
<p id="b1470-7">On the basis of factual differences, <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span> </em>explicitly distinguished <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>and a <em>pre-Payton </em>case from our circuit, <em>United States v. Botero, </em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/" aria-description="Citation for case: United States v. Diego Botero, United States of America...">589 F.2d 430</a></span> (9th Cir.1978), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./441/944/">441 U.S. 944</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./99/2162/">99 S.Ct. 2162</a></span>, <span class="citation" data-id="9015516"><a href="/opinion/9022296/botero-v-united-states/" aria-description="Citation for case: Botero v. United States">60 L.Ed.2d 1045</a></span> (1979). <em>Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#757" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 757</a></span>. In <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>the United States Supreme Court</p>
<blockquote id="A_FZ">upheld the warrantless arrest of a defendant who was standing within the frame of her doorway as the officers - approached and who then retreated into the vestibule of her home where the officers followed and effected the arrest. The Court held that once the defendant was exposed to public view in her doorway, her act of retreating into her house could not thwart an otherwise proper arrest by officers who pursued her inside.</blockquote>
<p id="b1470-12"><em>Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#756" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 756</a></span>.</p>
<p id="b1470-13">In <em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/" aria-description="Citation for case: United States v. Diego Botero, United States of America...">Botero</a></span>, </em>officers without a warrant knocked on Botero’s door, and when he opened it, he was placed under arrest. We held in <em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/" aria-description="Citation for case: United States v. Diego Botero, United States of America...">Botero</a></span>, </em>citing <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>that under the circumstances the doorway in which he was standing was a public place. <em>Botero, </em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/#432" aria-description="Citation for case: United States v. Diego Botero, United States of America...">589 F.2d at 432</a></span>. Thus, implicit in <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span> </em>is approval of the warrantless arrest of a suspect who voluntarily opens the door of his dwelling in response to a noncoercive knock by the police. This holding is consistent with our holding in <em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">Whitten</a></span>.</em></p>
<p id="b1470-14">As in <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span> </em>and <em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">Whitten</a></span>, </em>the arrest in the instant case involves factors that distinguish it from the arrests made in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and its consolidated companion case, <em>Riddick v. New York. </em>In <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>the police who entered Payton’s apartment broke through a closed door with crowbars. No one was home, but incriminating evidence seen in plain view was seized and used to convict him. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. at 576-77</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1374" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1374-75</a></span>. In <em>Riddick, </em>the closed door of Riddick’s house on which, the police knocked was opened by Riddick’s young son. Riddick could be seen sitting inside the apartment on a bed. He was covered by a sheet. Without any behavior on Riddick’s part that could be construed as consent, the police entered and arrested him on the spot. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#578" aria-description="Citation for case: Payton v. New York">445 U.S. at 578</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1376" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1376</a></span>. In both cases, the entries preceded the arrests.</p>
<p id="b1471-3"><page-number citation-index="1" label="1427">*1427</page-number>By contrast, in Vaneaton’s case the uniformed police used no force or threats, and unlike <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>, </em>they did not resort to a subterfuge or a ruse, or draw weapons-. When Vaneaton saw them through the window, he voluntarily opened the door and exposed both himself and the immediate area to them. No threats or force were used by the police to get him to open the door, and his actions were not taken in response to-a claim of lawful authority. The police did not enter the house until they formally placed Vaneaton under arrest. The magistrate’s findings of fact that (1) Vaneaton opened the door voluntarily, and (2) no coercion was used by the police, are fully supported by the record. “A trial court’s finding on voluntariness should not be overturned unless it is clearly erroneous.” <em>United States v. Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#895" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d 890, 895</a></span> (9th Cir.1985) (citation omitted), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./476/1144/">476 U.S. 1144</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2255/">106 S.Ct. 2255</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/90/700/">90 L.Ed.2d 700</a></span> (1986). Accordingly, by opening the door as he did, Vaneaton exposed himself in a public place. His warrantless arrest, therefore, does riot offerid the Fourth Amendment. <em>United States v. Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#421" aria-description="Citation for case: United States v. Watson">423 U.S. 411, 421-24</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#826" aria-description="Citation for case: United States v. Watson">96 S.Ct. 820, 826-28</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">46 L.Ed.2d 598</a></span> (1976) (The Fourth Amendment is not violated by a warrantless felony arrest in a public place).<footnotemark>3</footnotemark></p>
<p id="b1471-4">In summary, this episode does not materially resemble the kinds of “invasions” or “intrusions” against which <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>seeks to guard. Knocking on a door to attempt to contact a person inside is a common event and hardly a hallmark of a police state, and indeed, <em>under these facts </em>the zone of privacy sought by <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>to be protected is not implicated. Accordingly, we hold that <em>Pay-ton </em>was not violated, and that Vaneaton’s arrest was proper.<footnotemark>4</footnotemark></p>
<p id="b1471-8">CONCLUSION</p>
<p id="b1471-9">We conclude that the seizure in this case did not offend the Fourth Amendment. Thus we affirm the district court’s denial of Vaneaton’s motion to suppress.</p>
<p id="b1471-10">AFFIRMED.</p>
<footnote label="1">
<p id="b1468-24">. The defendant-appellant’s name is spelled many different ways' in the record. We hope our choice is correct.</p>
</footnote>
<footnote label="2">
<p id="b1470-8">. -Because we conclude that Vaneaton’s exposure to the police was voluntary, we need not discuss exigent circumstances.</p>
</footnote>
<footnote label="3">
<p id="b1471-5">. Our analysis is consistent with our holding in <em>United States v. Winsor, </em><span class="citation" data-id="9477657"><a href="/opinion/506186/united-states-v-steven-dale-winsor/" aria-description="Citation for case: United States v. Steven Dale Winsor">846 F.2d 1569</a></span> (9th Cir.1988) (en banc),-which dealt with the validity of a search rather than a seizure. To quote the en banc panel,</p>
<blockquote id="b1471-6">In <em>United States v. Hersh, </em><span class="citation" data-id="304759"><a href="/opinion/304759/united-states-v-clifford-hersh/#229" aria-description="Citation for case: United States v. Clifford Hersh">464 F.2d 228, 229-30</a></span> (9th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./409/1008/">409 U.S. 1008</a></span>, [<span class="citation multiple-matches"><a href="/c/S.Ct./93/442/">93 S.Ct. 442</a></span>, <span class="citation" data-id="8982969"><a href="/opinion/8990796/basyap-inc-v-district-of-columbia-redevelopment-land-agency/" aria-description="Citation for case: Basyap, Inc. v. District of Columbia Redevelopment Land...">34 L.Ed.2d 301</a></span>] ... (1972), the police, while standing on the front porch, looked through a window and saw incriminating evidence inside the residence. We held no search was effected because police merely did what any member of the public was free to do — walk onto the front porch and observe whatever was in plain view through an unobstructed window. Similarly, in <em>Davis v. United States, </em><span class="citation" data-id="263083"><a href="/opinion/263083/albert-douglas-davis-v-united-states/#303" aria-description="Citation for case: Albert Douglas Davis v. United States">327 F.2d 301, 303</a></span> (9th Cir.1964), the police did what any person could do — they knocked on the front door of a residence, hut did not use their authority as police officers to command the occupants to open the door. When the occupant opened the door, he did so voluntarily, not, as Dennis Winsor did, in response to a claim of lawful authority.</blockquote>
<p id="b1471-16"><em>Winsor, </em><span class="citation" data-id="9477657"><a href="/opinion/506186/united-states-v-steven-dale-winsor/#1573" aria-description="Citation for case: United States v. Steven Dale Winsor">846 F.2d at 1573</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b1471-17">. <em>Accord United States v. Carrion, </em><span class="citation" data-id="482020"><a href="/opinion/482020/united-states-v-anthony-nicholas-carrion-and-fred-solmor/#1128" aria-description="Citation for case: United States v. Anthony Nicholas Carrion and Fred Solmor">809 F.2d 1120, 1128</a></span> (5th Cir.1987) (a suspect standing in an open doorway stands in a public place). <em>But cf. United States v. Morgan, </em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158</a></span>, 1166 n. 2 (6th Cir.1984) (P<em>ayton </em>requires exigent circumstances before a warrantless arrest can be made of an individual standing in the doorway of a private residence.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Vasquez-Algarin.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Vasquez-Algarin
type: case
citation: "821 F.3d 467 (2016)"
parallel_cite: ""
neutral_cite: "2016 U.S. App. LEXIS 7889; 2016 WL 1730540"
court: 3d Cir. 2016
court_level: coa
circuit: ca3
year: 2016
date_decided: 2016-05-02
docket: 15-1941
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
  opinion_url: "https://www.courtlistener.com/opinion/3199633/united-states-v-johnny-vasquez-algarin/"
  cluster_id: 3199633
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Vasquez-Algarin
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Arrest in the Home]]"
    role: Key
related:
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[Steagald v. United States]]"
  - "[[Maryland v. Buie]]"
tags:
  - case
  - fourth-amendment
  - arrest-warrant
  - home-entry
  - probable-cause
  - reason-to-believe
  - third-circuit
holding: "To force entry into a dwelling to execute an arrest warrant, officers must have probable cause — not a lesser 'reasonable belief' — that the suspect both resides at and is present within the home; joining the Fifth, Sixth, Seventh, and Ninth Circuits, the Third Circuit held that Payton's 'reason to believe' language means probable cause, and because the officers here forced entry into a residence that was not shown to be the arrestee's home on that standard, the denial of suppression was reversed."
aliases:
  - United States v. Vasquez-Algarin
  - "United States v. Vasquez-Algarin (3d Cir. 2016)"
---

# United States v. Vasquez-Algarin

*821 F.3d 467 (3d Cir. 2016)* (No. 15-1941) · U.S. Court of Appeals for the Third Circuit · **Binding in-circuit — 3d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 3199633 → lead opinion 3199527 (Krause, J.; 821 F.3d 467, decided 2016-05-02); Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star-pagination *477). S9 promotes. -->

## Background
Officers holding an arrest warrant for one individual forced entry into a residence to execute it. Johnny Vasquez-Algarin — who, the record showed, was neither the person named in the warrant nor connected to that arrestee — was found and arrested inside, and evidence recovered there was used against him. He moved to suppress, arguing the officers lacked a sufficient basis to believe that the residence they entered was the named suspect's home. The district court denied suppression, appearing to assume that a probable-cause standard was satisfied, and Vasquez-Algarin appealed, presenting the open question of how certain officers must be before forcing entry into a dwelling to make an arrest.

## Issue
Whether the "reason to believe" that officers must have under *[[Payton v. New York]]* before forcing entry into a residence to execute an arrest warrant — that the suspect resides there and is present — requires probable cause or something less.

## Rule
An arrest warrant carries limited authority to enter the suspect's own dwelling to make the arrest, but only when officers have adequate grounds to believe the suspect lives there and is then present; the Third Circuit held those grounds must rise to probable cause. As the court put it: "we join the Fifth, Sixth, Seventh and Ninth Circuits in holding that Payton's 'reason to believe' language amounts to a probable-cause standard." — 821 F.3d at 477. ^pin-477

## Application
Reading *[[Payton v. New York|Payton]]* in the context of the Supreme Court's Fourth Amendment jurisprudence, the court concluded that the "reason to believe" phrase was used interchangeably with "probable cause" within the bounded factual setting *[[Payton v. New York|Payton]]* addressed, and that the profound protection the Constitution affords the home compels the more demanding standard. Requiring probable cause that the suspect both resides at and is present within the dwelling is the only conclusion commensurate with those protections — particularly where, as here, the person found inside was a third party unconnected to the arrest warrant, implicating the *[[Steagald v. United States|Steagald]]* concern for the privacy of those not named in the warrant. The court cabined its holding to the *[[Payton v. New York|Payton]]* context, disclaiming any effect on the separate reasonable-suspicion line. Because the entry was not justified on the probable-cause standard the court adopted, the suppression ruling could not stand.

## Conclusion
The Third Circuit **reversed** the denial of the suppression motion and [[Reading and Citing Cases#on-remand|remanded]], declining to reach Vasquez-Algarin's separate sentencing challenge. Judge Krause wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Vasquez-Algarin* is a leading circuit statement that *[[Payton v. New York|Payton]]*'s "reason to believe" is a **probable-cause** standard — that officers need probable cause the suspect both **resides at** and **is present in** a home before forcing entry on an arrest warrant. Teach it with *[[Steagald v. United States|Steagald]]* (a search warrant is required to enter a **third party's** home) and note the acknowledged circuit split, with some courts treating "reason to believe" as a lesser standard than probable cause.

## Appears on
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Vasquez-Algarin*, 821 F.3d 467 (3d Cir. 2016)](https://www.courtlistener.com/opinion/3199633/united-states-v-johnny-vasquez-algarin/) — pinpoint: 477 (*Payton*'s "reason to believe" requires probable cause; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "88aa2328b1e32707", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "821 F.3d 467 (2016)", "court": "3d Cir. 2016", "neutral_cite": "2016 U.S. App. LEXIS 7889; 2016 WL 1730540", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Vasquez-Algarin", "year": "2016"}}
{"assertion_id": "3f660c81d5447ca0", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Key", "title": "United States v. Vasquez-Algarin"}}
{"assertion_id": "a74f9fee33295a15", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "To force entry into a dwelling to execute an arrest warrant, officers must have probable cause — not a lesser 'reasonable belief' — that the suspect both resides at and is present within the home; joining the Fifth, Sixth, Seventh, and Ninth Circuits, the Third Circuit held that Payton's 'reason to believe' language means probable cause, and because the officers here forced entry into a residence that was not shown to be the arrestee's home on that standard, the denial of suppression was reversed.", "title": "United States v. Vasquez-Algarin"}}
{"assertion_id": "4374436ea5cc802f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Vasquez-Algarin", "varies_by_point": "false"}}
{"assertion_id": "fbf4200dfcf85f13", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 3d Cir.", "title": "United States v. Vasquez-Algarin"}}
```

### lake record — United States v. Vasquez-Algarin

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Vasquez-Algarin",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Johnny Vasquez-Algarin",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America v. Johnny VASQUEZ-ALGARIN, Appellant",
    "input_case_name": "United States v. Vasquez-Algarin",
    "court": "3d Cir. 2016",
    "court_id": "ca3",
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": "2016-05-02",
    "year": 2016,
    "docket": "15-1941",
    "cluster_id": 3199633,
    "lead_opinion_id": 3199527,
    "sibling_ids": [],
    "absolute_url": "/opinion/3199633/united-states-v-johnny-vasquez-algarin/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "821 F.3d 467",
      "volume": "821",
      "reporter": "F.3d",
      "page": "467",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. App. LEXIS 7889",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "7889",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 1730540",
        "volume": "2016",
        "reporter": "WL",
        "page": "1730540",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "821 F.3d 467",
        "volume": "821",
        "reporter": "F.3d",
        "page": "467",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 7889",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "7889",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 1730540",
        "volume": "2016",
        "reporter": "WL",
        "page": "1730540",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "821 F.3d 467",
    "official_selection": {
      "court_class": "coa",
      "selected": "821 F.3d 467",
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
    "date_created": "2026-07-06T05:59:14Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-vasquez-algarin--3199633",
      "to_record_id": "United States v. Vasquez-Algarin",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Vasquez-Algarin

```
                                        PRECEDENTIAL

      UNITED STATES COURT OF APPEALS
           FOR THE THIRD CIRCUIT
                _____________

                    No. 15-1941
                   _____________

          UNITED STATES OF AMERICA


                          v.

          JOHNNY VASQUEZ-ALGARIN,
                               Appellant
               _______________

    On Appeal from the United States District Court
        for the Middle District of Pennsylvania
             (D.C. No. 1-11-cr-00200-001)
       District Judge: Honorable Sylvia Rambo
                   _______________

              Argued: February 11, 2016

Before: FUENTES, KRAUSE, and ROTH Circuit Judges.

                 (Filed: May 2, 2016)
                  _______________
Ronald A. Krauss, Esq.
Frederick W. Ulrich, Esq. (Argued)
Office of Federal Public Defender
100 Chestnut Street
Suite 306
Harrisburg, PA 17101

               (Counsel for Appellant)

Daryl F. Bloom, Esq. (Argued)
Stephen R. Cerutti, II, Esq.
Office of United States Attorney
228 Walnut Street, P.O. Box 11754
220 Federal Building and Courthouse
Harrisburg, PA 17108

               (Counsel for Appellee)

                      _______________

                 OPINION OF THE COURT
                     _______________

KRAUSE, Circuit Judge.

        Law enforcement officers need both an arrest warrant
and a search warrant to apprehend a suspect at what they
know to be a third party’s home. If the suspect resides at the
address in question, however, officers need only an arrest
warrant and a “reason to believe” that the individual is
present at the time of their entry. This case sits between these
two rules and calls on us to decide their critical point of
inflection: how certain must officers be that a suspect resides




                               2
at and is present at a particular address before forcing entry
into a private dwelling?

       A careful examination of the Supreme Court’s Fourth
Amendment jurisprudence reveals that the standard cannot be
anything less than probable cause. Because here, law
enforcement acted on information that fell short of the
standard, we will vacate the conviction and remand to the
District Court.

I.     Background

       A.     Facts

       In 2010, an arrest warrant was issued for Edguardo
Rivera,1 a suspect in a homicide case. Deputy U.S. Marshal
Gary Duncan, a member of the Dauphin County Fugitive
Task Force, received information from another law
enforcement officer and from street informants that Rivera
was “staying” or “residing” at an address on North 13th Street
in Harrisburg, Pennsylvania. App. 25–26, 35–36. With the
arrest warrant for Rivera in hand, Deputy Marshal Duncan
and officers from the Harrisburg Bureau of Police and the
Dauphin County Drug Task Force arrived at the apartment
and knocked on the door. They received no response but
“heard a lot of movement inside,” as well as a phone ring
once or twice and stop ringing and a dog bark and cease
barking, giving the officers the impression that a person had


       1
         The District Court uses a different spelling than the
party briefs and the court transcripts, referring to the suspect
as “Edwardo Rivera.”




                               3
manually silenced the phone and muzzled the dog. App. 29–
30. The officers then forcibly entered the home.

        As it turned out, however, the sought fugitive, Rivera,
did not live in the apartment and was not present.2 Instead,
upon entering, the officers saw Appellant Johnny Vasquez-
Algarin, and, during a protective sweep, they identified in
plain view sandwich baggies, a razor blade, and what
appeared to be powder cocaine. After Vasquez-Algarin
declined to grant consent for a search, one officer obtained a
search warrant while the other officers waited at the
apartment. During the subsequent search conducted pursuant
to the warrant, the officers discovered ammunition, unused
plastic bags, and hundreds of small black bands, as well as a
cell phone in the master bedroom that was later searched
pursuant to another search warrant. At some point during the
search, the officers identified a set of car keys, which they
used to open a stolen Mazda located across from the
apartment.      Vasquez-Algarin, who had no outstanding
warrants, was then arrested.

       B.     Proceedings

       Vasquez-Algarin and the two brothers with whom he
shared the apartment were each charged with distribution and
possession with intent to distribute cocaine in violation of 21
U.S.C. § 841(a)(1) and (b)(1)(A)(ii) and conspiracy to do the
same in violation of 21 U.S.C. § 846. In October 2013,
Vasquez-Algarin pleaded not guilty to the charges.


       2
        The record contains no evidence of any connection
between the two men.




                              4
       The month before trial, Vasquez-Algarin moved to
suppress the evidence seized from the North 13th Street
residence, arguing that law enforcement’s forced entry into
the apartment was unconstitutional. At his suppression
hearing, the Government presented three witnesses, all
officers involved in various stages of Vasquez-Algarin’s
apprehension and arrest. Two witnesses, Deputy Marshal
Duncan and Middletown Borough Police Detective Dennis
Morris, testified about the sounds that officers heard coming
from inside the residence on their arrival, but only Deputy
Marshal Duncan could speak to the circumstances that led
law enforcement to Vasquez-Algarin’s residence.

        Deputy Marshal Duncan testified that he had an arrest
warrant for Edguardo Rivera and was given “reliable”
information from a detective from the Harrisburg Bureau of
Police and informants that Rivera lived at the North 13th
Street address. App. 25, 26. During cross-examination, when
defense counsel pressed Deputy Marshal Duncan to elaborate
on “the exact factors” that led him to believe that Rivera lived
at the address, Deputy Marshal Duncan reiterated that he had
relied on “[i]nformation being provided to me by another law
enforcement officer, information that we had from informants
on the street that that address was being used by Mr. Rivera.”
App. 36. When counsel asked if, prior to going to the
residence, Deputy Marshal Duncan had checked records for
the resident of the apartment, he confirmed that he had but
was unable to recall whether he had identified the renter of
the apartment.

       The District Court denied Vasquez-Algarin’s motion
to suppress, concluding from Deputy Marshal Duncan and
Detective Morris’s testimony that the officers had a
“reasonable belief” and “probable cause to believe” that the




                               5
fugitive, Rivera, resided at the apartment and was present at
the time of the officers’ entry and that their entry was
therefore constitutional.3 United States v. Vasquez-Algarin,
No. 1:11-CR-0200-01, 2014 WL 1672008, at *1–2 (M.D. Pa.
Apr. 28, 2014). At trial the next month, Deputy Marshal
Duncan provided substantially the same information about
what had led him to the North 13th Street address to
apprehend Rivera.4 However, he offered a different answer to

       3
          At the suppression hearing, there was some question
as to Vasquez-Algarin’s standing to challenge the search
because he testified that the apartment was merely rented in
his name and that he had moved out two months before the
search, leaving only his dog in the apartment with his
brothers. He further represented he was in the apartment at
the time of the search only because he had received a call
from the landlord about problems with the rent and
electricity. The District Court determined that the master
bedroom belonged to Vasquez-Algarin, “as he could not
identify key details related to his alleged other residence, and
was the individual on the lease of the 142 North 13th Street
residence and kept possessions therein,” and expressly
rejected as “not credible” Vasquez-Algarin’s claim that he no
longer resided at the apartment at the time of the search.
Vasquez-Algarin, 2014 WL 1672008, at *2 n.2. In addition,
Vasquez-Algarin maintained at the suppression hearing that
he had standing to assert a Fourth Amendment claim, and the
Government does not now challenge his standing.
       4
         Specifically, at trial Deputy Marshal Duncan testified
that the U.S. Marshals Service “received information that Mr.
Rivera could possibly be residing at an address on North 13th
Street,” App. 136, and that “the information . . . was provided




                               6
a question he also had been asked at the suppression hearing
about why he spent significant time knocking and yelling at
the door. At the suppression hearing, Deputy Marshal
Duncan had testified that often residents will not come to the
door for law enforcement but “if we stay there for a while,
and you continue to knock and continue to not leave, typically
you’ll gain some response from somebody inside.” App. 29.
In his trial testimony, however, he identified a second reason
he knocked for so long at the door in this case: “The address
was not the address of record for Mr. Rivera, so we wanted to
knock and attempt to gain contact with somebody inside and
gain their consent to search the address.” App. 138.

       After a two-day trial, a jury convicted Vasquez-
Algarin on both drug counts. He now appeals the District
Court’s denial of his suppression motion.5 We review the
District Court’s legal conclusions de novo and the underlying
factual findings for clear error. United States v. Torres, 534
F.3d 207, 209 (3d Cir. 2008). In the present context, where
we are reviewing the denial of a motion to suppress to

to [him] by a detective from the City of Harrisburg who
received the information that Mr. Rivera may be staying
there,” App. 137.
      5
          The District Court had jurisdiction pursuant to 18
U.S.C. § 3231, and we have jurisdiction pursuant to 28 U.S.C.
§ 1291. Because we vacate the conviction, we do not reach
the second issue Vasquez-Algarin raises on appeal, whether
the District Court committed clear error in applying a two-
level sentencing enhancement for Vasquez-Algarin’s role as
an organizer, leader, manager or supervisor in the criminal
activity under § 3B1.1(c) of the U.S. Sentencing Guidelines.




                              7
determine whether police officers had probable cause to
believe the subject of their arrest warrant lived in the
apartment they entered, we may look to the entire record and
are “not restricted to the evidence presented at the
suppression hearing where the motion was denied.” United
States v. Silveus, 542 F.3d 993, 1001 (3d Cir. 2008) (quoting
Gov’t of the V.I. v. Williams, 739 F.2d 936, 939 (3d Cir.
1984)).

II.   Discussion

       Vasquez-Algarin argues that law enforcement officers
needed a search warrant to enter the North 13th Street
apartment because the subject of their arrest warrant (the
“arrestee”6) did not in fact reside there. As we will explain
below, however, their entry was constitutional if they had
sufficient information to support a reasonable belief that the
arrestee resided at and was present within the targeted home.
To determine what reasonable belief requires, we will look to
the principles set forth in the Supreme Court’s key
precedents, the views expressed by our sister Circuits and,
most importantly, the fundamental tenets of Fourth

      6
         The term “arrestee” is usually used to describe an
individual who was been arrested, see Black’s Law
Dictionary (10th ed. 2014) (defining “arrestee” as “[s]omeone
who has been taken into custody by legal authority; a person
who has been arrested”), but in the Payton context, the courts
regularly use the term to refer to the intended target of the
arrest warrant. For ease of reference, we use the term in this
sense throughout the opinion, although the person eventually
arrested in this case differed from the person named on the
warrant.




                              8
Amendment jurisprudence governing the home. We conclude
that to satisfy the reasonable belief standard law enforcement
required, but lacked, probable cause. The officers’ entry was
therefore unconstitutional and, because the good-faith
exception to the exclusionary rule is inapplicable here, the
evidence seized from Vasquez-Algarin’s apartment should
have been suppressed.




                              9
       A.     Payton and Steagald

        The Supreme Court has issued two major decisions
regarding the constitutionality of in-home arrests. Because
here law enforcement officers believed, albeit mistakenly,
that the home they were entering was the residence of the
subject of their arrest warrant, the controlling authority is the
first of these decisions, Payton v. New York, 445 U.S. 573
(1980).      There, the Supreme Court considered two
consolidated cases in which police officers entered private
residences without any kind of warrant to make routine felony
arrests and held that the state statutes that had authorized
these warrantless entries were unconstitutional; the officers
were required to have an arrest warrant to arrest a suspect in
his home. Id. at 602–03. In a dictum that has since evolved
into a tenet of Fourth Amendment jurisprudence, the Court
also observed that a search warrant would not be required in
that circumstance because “an arrest warrant founded on
probable cause implicitly carries with it the limited authority
to enter a dwelling in which the suspect lives when there is
reason to believe the suspect is within.” Id. at 603 (emphasis
added).

       In the wake of Payton, to assess the constitutionality of
an officer’s entry into a home to execute an arrest warrant, the
Courts of Appeals have drawn upon the Supreme Court’s
language to develop a two-prong test that extends to
residency: the officer must have a “reasonable belief”7 that


       7
         Close examination reveals the Courts of Appeals
have uniformly cast Payton’s “reason to believe” language as
a reasonable belief standard. See, e.g., United States v.
Gorman, 314 F.3d 1105, 1114–15 (9th Cir. 2002). However,




                               10
(1) the arrestee resides at the dwelling, and (2) the arrestee is
present at the time of the entry. See, e.g., United States v.
Veal, 453 F.3d 164, 167 (3d Cir. 2006) (quoting United States
v. Gay, 240 F.3d 1222, 1226 (10th Cir. 2001)).

        A different framework applies, however, where
officers believe an individual for whom they have an arrest
warrant is a guest in a third-party home. A year after handing
down Payton, the Supreme Court held in Steagald v. United
States, 451 U.S. 204 (1981), that officers may not enter a
third party’s residence to execute an arrest warrant without
first obtaining a search warrant “based on their belief that [the
suspect] might be a guest there,” unless the search is
consensual or justified by exigent circumstances. Id. at 213,
216. In so reasoning, the Court rejected the Government’s
argument as to the “practical problems [that] might arise if
law enforcement officers are required to obtain a search
warrant before entering the home of a third party to make an
arrest,” and concluded that “the inconvenience incurred by
the police is simply not that significant” and in any event
“cannot outweigh the constitutional interests at stake.” Id. at
220–22.

       Before us is a case of mistaken belief that underscores
the tension between the residency test that the Courts of
Appeals have derived from Payton and the relatively robust
Fourth Amendment protections guaranteed to third-party
homes under Steagald.8 Because officers may force entry

as discussed infra in Section II.B, they diverge on what that
standard requires.
       8
         Vasquez-Algarin was not the arrestee sought nor, as
far as the record shows, connected to the arrestee in any way.




                               11
into a home as long as they have a reasonable belief the
suspect resides and is present there, but must have nothing
short of a search warrant where the suspect is a guest in a
third party’s home, law enforcement’s assessment of a
suspect’s residency is, in effect, a determination of the level
of protection to which a dwelling is entitled. Our choice
about how much and what kind of information must form the
basis for that critical determination thus affects not only the
homes of arrestees but also any home that could be mistaken
for one. For that reason, we must draw not only from the
principles laid out in Payton but also from those set forth in
Steagald when determining just how stringent the reasonable
belief standard must be. With these principles in mind, we
next consider our own precedent relevant to this issue and the
case law of our sister Circuits that have addressed the issue
squarely, but with divergent results.

      B.     The reasonable belief standard

      Vasquez-Algarin contends that this Court has already
equated “reason to believe” or “reasonable belief” with a
probable cause standard, and the District Court appears to
have assumed probable cause applied as well. Vasquez-
Algarin, 2014 WL 1672008, at *1. The issue, however,
remains an open question in our Circuit.


This distinguishes this case from any of our relevant
precedents and from many of the cases in which other Courts
of Appeals have had occasion to interpret and apply the
Payton reasonable belief standard. See, e.g., Veal, 453 F.3d
164 (defendant was the intended arrestee); United States v.
Agnew, 407 F.3d 193 (3d Cir. 2005) (same).




                              12
       Vazquez-Algarin is correct that we treated reasonable
belief and probable cause as equivalent in United States v.
Agnew, 407 F.3d 193 (3d Cir. 2005). There, in applying the
Payton reasonable belief test, we observed that “police may
enter a suspect’s residence to make an arrest armed only with
an arrest warrant if they have probable cause to believe that
the suspect is in the home.” Id. at 196. Yet in that case the
government possessed sufficient information to meet the
standard irrespective of its precise definition, so we had no
occasion to analyze the point and it had no effect on our
holding. Recognizing as much, we observed the following
year in Veal that although “[o]ur Court . . . has described the
test using the language of ‘probable cause,’” the courts had
taken different approaches to the question, and we decided,
under these circumstances, that we would “determine whether
a possibly lower standard of reasonable belief should be
applied” another day. 453 F.3d at 167 n.3.

       That day has arrived. Because a number of our sister
Circuits have opined on this issue, we review their
approaches for their persuasive value before staking out our
own. As described below, these approaches vary widely:
Although the Courts of Appeals once overwhelmingly
interpreted reasonable belief as less stringent than probable
cause, they are now nearly evenly divided on this point.9


      9
        In the last decade, a number of Courts of Appeals
have expressed agreement with the Ninth Circuit’s
longstanding view that reasonable belief amounts to probable
cause. See United States v. Harper, 928 F.2d 894, 897 (9th
Cir. 1991), overruled on other grounds by United States v.
King, 687 F.3d 1189, 1189 (9th Cir. 2012) (en banc) (per
curiam); accord United States v. Jackson, 576 F.3d 465, 469




                              13
       The D.C., First, Second and Tenth Circuits have
determined that reasonable belief requires less than probable
cause.10 See United States v. Thomas, 429 F.3d 282, 286
(D.C. Cir. 2005); United States v. Werra, 638 F.3d 326, 337
(1st Cir. 2011); United States v. Lauter, 57 F.3d 212, 215 (2d
Cir. 1995); Valdez v. McPheters, 172 F.3d 1220, 1224–25
(10th Cir. 1999). But those courts have offered little by way
of explanation for this interpretation. In Thomas, the D.C.
Circuit observed that, to date, most of the appellate courts had
determined that reasonable belief is a less stringent standard
than probable cause and that it was “more likely . . . that the
Supreme Court in Payton used a phrase other than ‘probable
cause’ because it meant something other than ‘probable
cause.’” 429 F.3d at 286. In Valdez, the Tenth Circuit
offered a more detailed explanation for its adoption of a
standard less stringent than probable cause, but rather than
explaining why probable cause would be inappropriate, the
court focused entirely on the impracticability of imposing on

(7th Cir. 2009); United States v. Hardin, 539 F.3d 404, 416 &
n.6 (6th Cir. 2008); see also United States v. Barrera, 464
F.3d 496, 501 & n.5 (5th Cir. 2006) (equating the two terms
and describing the disagreement among the appellate courts
as “semantic”); United States v. Route, 104 F.3d 59, 62 (5th
Cir. 1997) (analogizing reasonable belief to probable cause
but ultimately rejecting the latter standard).
       10
          Even those courts that agree that reasonable belief is
a lower standard than probable cause disagree on its precise
definition. Compare, e.g., Gay, 240 F.3d at 1227 (describing
reasonable belief and reasonable suspicion as “two different
legal standards”); with Werra, 638 F.3d at 337 (equating
reasonable belief to reasonable suspicion).




                              14
officers an “actual knowledge” requirement, which none of
the Courts of Appeals has imposed in applying Payton. See
Valdez, 172 F.3d at 1224–25 (10th Cir. 1999) (criticizing the
Ninth Circuit’s adoption of the probable cause standard in
part because “requiring actual knowledge of the suspect’s true
residence would effectively make Payton a dead letter”). But
see United States v. Hill, 649 F.3d 258, 274 (4th Cir. 2011)
(Agee, J., dissenting) (“[N]o court applying [Payton] has ever
held[] that the police must have seen the defendant nearby or
have actual knowledge that he is inside a residence before
they can enter.”); United States v. Magluta, 44 F.3d 1530,
1535 (11th Cir. 1995) (“[P]robable cause itself is a doctrine of
reasonable probability and not certainty.”).

       The Fifth, Sixth, Seventh and Ninth Circuits have
endorsed—or, in the case of the Seventh Circuit, “inclined”
toward—interpreting reasonable belief as the equivalent, or
functional equivalent, of probable cause. See United States v.
Barrera, 464 F.3d 496, 500-01 & n.5 (5th Cir. 2006); United
States v. Hardin, 539 F.3d 404, 415–16 & n.6 (6th Cir. 2008);
United States v. Jackson, 576 F.3d 465, 469 (7th Cir. 2009);
United States v. Gorman, 314 F.3d 1105, 1114–15 (9th Cir.
2002). 11 To reach this conclusion, some of these Courts of
Appeals have looked to the Supreme Court’s own post-

       11
          The Sixth Circuit has reconsidered its position on
the issue. In Hardin, the Sixth Circuit rejected as dictum its
previous determination in United States v. Pruitt that
reasonable belief is a less stringent standard than probable
cause, and, in new dictum, endorsed Judge Clay’s concurring
opinion in Pruitt that equated the two standards. Hardin, 539
F.3d at 415 & n.6 (citing United States v. Pruitt, 458 F.3d
477, 490 (6th Cir. 2006) (Clay, J., concurring)).




                              15
Payton characterization of its “reason to believe” language, as
well as the terms with which the Court has generally defined
the probable cause standard.

        Most notably, in Maryland v. Buie, 494 U.S. 325
(1990), when considering whether officers executing a home
arrest pursuant to Payton could also perform a protective
sweep of the residence, the Supreme Court concluded that
“[p]ossessing an arrest warrant and probable cause to believe
Buie was in his home, the officers were entitled to enter and
to search anywhere in the house in which Buie might be
found.” Id. at 332–33 (emphasis added). According to the
Sixth and Ninth Circuits, this passage is most naturally read
to mean that the Supreme Court intended the Payton “reason
to believe” language to serve as a reference to probable cause.
See Hardin, 539 F.3d at 416 n.6 (“Had the Court truly
intended the ‘reason to believe’ language in Payton to set
forth a new, lesser standard, surely the Court in Buie would
have explained that the officers were entitled to be inside
Buie’s residence on the basis of an arrest warrant and a
‘reasonable belief’ as to Buie’s presence, but the Court used
the term ‘probable cause’ instead.”); accord Gorman, 314
F.3d at 1114.12


       12
          As these courts have pointed out, Justice White’s
description of the majority opinion in his dissent in Payton
provides additional support for interpreting Payton’s “reason
to believe” language as a reference to probable cause.
Hardin, 539 F.3d at 410; Gorman, 314 F.3d at 1114 & n.10.
His disagreement with the majority was predicated in part on
his understanding that “under [the majority’s] decision, the
officers apparently need an extra increment of probable cause
when executing the arrest warrant, namely, grounds to believe




                              16
        As further evidence that reasonable belief amounts to
probable cause, some of these Courts of Appeals have also
considered the Supreme Court’s tendency to explain and
define the term “probable cause” using “grammatical
analogues” of “reason to believe.” Hardin, 539 F.3d at 416
n.6 (citing Pruitt, 458 F.3d at 490 (Clay, J., concurring)). For
example, the Court has described probable cause as requiring
a “reasonable ground for belief.” Pruitt, 458 F.3d at 490
(Clay, J., concurring) (quoting Maryland v. Pringle, 540 U.S.
366, 370–71 (2003); Ybarra v. Illinois, 444 U.S. 85, 91
(1979)); see also Illinois v. Gates, 462 U.S. 213, 243 (1983)
(suggesting that “probable cause” is synonymous with
“‘reasonable grounds’ to believe”).

        Among the Courts of Appeals that have equated
reasonable belief with probable cause, the Fifth Circuit is
notable in that it has also concluded that “the courts that
distinguish the terms have done so because ‘probable cause’
is a term of art.” See Barrera, 464 F.3d at 501 & n.5 (citing
United States v. Woods, 560 F.2d 660 (5th Cir. 1977); United
States v. Route, 104 F.3d 59, 62 (5th Cir. 1997)). We do not
necessarily agree with the suggestion in Barrera that the
disagreement among the Circuits as to whether reasonable
belief equates to probable cause is “more about semantics
than substance.” Id. The D.C. Circuit, for instance, appears
to require significantly less evidence to support a belief of
residency than the other Courts of Appeals, presumably in
part as a result of its choice to depart from the probable cause
standard and the protections it affords. See, e.g., Thomas, 429
F.3d at 286 (holding that officers had requisite reasonable

that the suspect is within the dwelling.” Payton, 445 U.S. at
616 n.13 (White, J., dissenting) (emphasis added).




                              17
belief to enter residence where arresting marshals provided no
testimony about where they had obtained the parolee’s
address except to say that an “investigation was done” and the
address “turned up”).

        We do agree with the Fifth Circuit, however, that
probable cause has specialized usage and is not a standard
typically applied by police to settle a question of the kind
before us about where an individual lives.13 Although the
Supreme Court has long insisted on a “practical,
nontechnical” definition of probable cause, Gates, 462 U.S. at
231 (quoting Brinegar v. United States, 338 U.S. 160, 176
(1949)), describing it as a “fluid concept” that defies
“reduc[tion] to a neat set of legal rules,” id. at 232, the
fluidity of the concept has not translated into diverse
application. A close reading of the case law shows that the
Supreme Court uses the “probable cause” standard almost
exclusively to assess the basis and strength of an officer or

       13
           The awkwardness that the Fifth Circuit has
identified, of applying the probable cause standard in the
Payton context, see Route, 104 F.3d at 62, may be a function
of the appellate courts’ recasting of the Payton “reason to
believe” standard—which the Supreme Court used to describe
only whether the arrestee was present within the residence—
as a two-part test in which that same standard governs both
whether the dwelling is the arrestee’s residence and whether
the arrestee is inside. Applying the probable cause standard
to determine only whether the arrestee is present within the
home presents no such difficulties. Cf. Steagald, 451 U.S. at
213–14 n.7 (“[T]he plain wording of the Fourth Amendment
admits of no exemption from the warrant requirement when
the search of a home is for a person rather than for a thing.”).




                              18
magistrate’s belief that a particular person has committed a
particular crime or that an article subject to seizure can be
found at a particular location—in short, whether criminal
activity is afoot. See, e.g., Brinegar, 338 U.S. at 175 (“The
substance of all the definitions of probable cause is a
reasonable ground for belief of guilt.” (internal quotation
marks omitted)).

        The Supreme Court’s general practice of reserving
probable cause language to these circumstances perhaps helps
account for the Eighth and Eleventh Circuits’ decision to
simply treat reasonable belief as its own standard for purposes
of applying the Payton test. The Eleventh Circuit in Magluta,
observing that “it is difficult to define the Payton ‘reason to
believe’ standard, or to compare the quantum of proof the
standard requires with the proof that probable cause requires,”
side-stepped the comparison altogether and treated the inquiry
as, in essence, its own reasonableness determination. 44 F.3d
at 1535–36 (citing Woods, 560 F.2d at 665); accord United
States v. Risse, 83 F.3d 212, 216–17 (8th Cir. 1996)
(employing a similar test and citing Magluta).14 Relying on
the same case law as the Fifth Circuit in Barrera, the
Eleventh Circuit thus opted for a “practical interpretation of
Payton” that resembles probable cause in that “in order for
law enforcement officials to enter a residence to execute an
arrest warrant for a resident of the premises, the facts and
      14
          Although Woods predated Payton, the Eleventh
Circuit has deemed the cases consistent. Magluta, 44 F.3d at
1536. Decisions of the former Fifth Circuit rendered prior to
October 1, 1981, are precedent in the Eleventh Circuit.
Bonner v. City of Prichard, 661 F.2d 1206, 1209 (11th Cir.
1981) (en banc).




                              19
circumstances within the knowledge of the law enforcement
agents, when viewed in the totality, must warrant a reasonable
belief that the location to be searched is the suspect’s
dwelling, and that the suspect is within the residence at the
time of entry.” Magluta, 44 F.3d at 1535; cf. Gates, 462 U.S.
at 238 (explaining that, for purposes of a probable cause
determination, a “totality of the circumstances” analysis
requires the magistrate issuing a warrant “simply to make a
practical, common-sense decision whether . . . there is a fair
probability that contraband or evidence of a crime will be
found in a particular place.”).

       C.     Reasonable belief as probable cause

        Having considered the different approaches of our
sister Circuits and their reasoning where provided, we join the
Fifth, Sixth, Seventh and Ninth Circuits in holding that
Payton’s “reason to believe” language amounts to a probable
cause standard.15 As explained more fully below, we do so
for two reasons. First, the Supreme Court’s use of the phrase
“reason to believe,” when considered in the context of Payton
and more generally the Court’s Fourth Amendment
jurisprudence, supports a probable cause standard. Second,
and more fundamentally, requiring that law enforcement

       15
          The Seventh Circuit has stated its “inclin[ation] to
adopt the view . . . that ‘reasonable belief’ is synonymous
with probable cause,” Jackson, 576 F.3d at 469, and the Sixth
Circuit has endorsed the view that the two standards are
synonymous in what it conceded was dictum, Hardin, 539
F.3d at 415–16 & n.6.




                              20
officers have probable cause to believe their suspect resides at
and is present within the dwelling before making a forced
entry is the only conclusion commensurate with the
constitutional protections the Supreme Court has accorded to
the home.

       We consider first the Court’s use of the term “reason
to believe” in Payton and other criminal cases. On careful
reading, Payton appears to be a case in which the Court used
the terms “probable cause” and “reason to believe” in close
proximity and interchangeably. This is readily apparent when
we examine how the Payton Court couched its analysis.
Expressly “put[ting] to one side related problems that are not
presented today,” the Court noted that neither of the
consolidated cases before it in Payton involved exigent
circumstances or consent, the home of a third party, or
allegations “that the police lacked probable cause to believe
that the suspect was at home when they entered.” Payton,
445 U.S. at 582–84. It is within this carefully bounded
factual framework—the search of an arrestee’s home without
exigent circumstances or consent but with probable cause to
believe he was present—that the Court concluded its decision
with the observation that “an arrest warrant founded on
probable cause implicitly carries with it the limited authority
to enter a dwelling in which the suspect lives when there is
reason to believe the suspect is within.” Id. at 603.

       Payton is not an anomaly. On several occasions, the
Supreme Court has used the very same “reason to believe”
language that appears in Payton as a stand-in for “probable
cause.” For example, in the landmark case Berger v. New
York, 388 U.S. 41 (1967), where the Court held that the
wiretapping statute in question violated the Fourth
Amendment       because    it   authorized     suspicionless




                              21
eavesdropping, the Court explained that “[t]he purpose of the
probable cause requirement of the Fourth Amendment [is] to
keep the state out of constitutionally protected areas until it
has reason to believe that a specific crime has been or is
being committed.” Id. at 59 (emphases added). In Gerstein v.
Pugh, 420 U.S. 103 (1975), the Court likewise observed that
at common law the justice of the peace would “determine
whether there was reason to believe the prisoner had
committed a crime” and that this “initial determination of
probable cause” could be reviewed on a writ of habeas
corpus. Id. at 114–15. And in Cardwell v. Lewis, 417 U.S.
583 (1974) (plurality opinion), after recounting all of the
evidence that established that police had “probable cause to
search [the suspect’s] car,” the Court concluded that the
resulting composite “provided reason to believe that the car
was used in the commission of the crime.” Id. at 592.
Examples of this kind serve to undercut the D.C. Circuit’s
conclusion that Payton’s “reason to believe” should be
construed loosely simply because the Court elected to use a
phrase other than “probable cause” to describe the requisite
belief law enforcement must have that an arrestee is present
in his dwelling at the time of the search. Thomas, 429 F.3d at
286.

        Although the language of Payton and the Supreme
Court’s other Fourth Amendment decisions provides strong
support for interpreting reasonable belief as a probable cause
standard, it is the nature of the privacy interests at stake that
solidifies our conclusion.16 Without question, the home takes


       16
         We recognize that there are limits to parsing
language alone to determine what the Supreme Court
intended by its use of the phrase “reason to believe” in




                               22
pride of place in our constitutional jurisprudence. As the
Supreme Court has reiterated on numerous occasions, “when
it comes to the Fourth Amendment, the home is first among
equals. At the Amendment’s ‘very core’ stands ‘the right of a
man to retreat into his own home and there be free from


Payton, because the Court has not adhered to hard and fast
rules when using “reasonableness” language. For example,
the Court has sometimes referred to “reasonable belief” when
discussing “reasonable suspicion,” see, e.g., Buie, 494 U.S. at
336–37; United States v. Place, 462 U.S. 696, 703–04 (1983),
a practice that has been cited by at least one Court of Appeals
to suggest Payton may require less than probable cause, see,
e.g., Pruitt, 458 F.3d at 484. The Court’s references to
“reasonable belief” outside the Payton context, however, have
little relevance to our inquiry, particularly as the phrase
“reasonable belief” does not actually appear in Payton and
using it as shorthand for “reason to believe” is an adaptation
of the Courts of Appeals. Conversely, our holding today that
the “reason to believe” or short-hand “reasonable belief”
standard equates to probable cause is limited to the Payton
context and should not be construed to mean that “reasonable
belief,” “reasonable grounds to believe,” or a substantially
similar iteration means probable cause in other circumstances.
While the Supreme Court has occasionally discussed
reasonable suspicion in terms of “reasonable belief,” for
example, reasonable suspicion is “obviously less demanding”
than probable cause, United States v. Sokolow, 490 U.S. 1, 7
(1989), and nothing we have said today bears on that line of
cases, see, e.g., United States v. Arvizu, 534 U.S. 266 (2002);
Alabama v. White, 496 U.S. 325 (1990); Terry v. Ohio, 392
U.S. 1 (1968).




                              23
unreasonable governmental intrusion.’” Florida v. Jardines,
133 S. Ct. 1409, 1414 (2013) (quoting Silverman v. United
States, 365 U.S. 505, 511 (1961)). Indeed, such intrusion is
“the chief evil against which the wording of the Fourth
Amendment is directed.” Payton, 445 U.S. at 585.

       The vaunted place of the home in our constitutional
privacy jurisprudence was central to the Supreme Court’s
analysis in Payton and Steagald. See, e.g., Payton, 445 U.S.
at 585–90; Steagald, 451 U.S. at 220, 222. These cases
together provide insight that neither case provides alone—
insight that leads inexorably to the conclusion that the
Circuit-created two-prong test is workable only if governed
by a robust reasonableness standard akin to probable cause,
and that anything less would defeat the “stringent . . .
protection” the home is due. United States v. Martinez-
Fuerte, 428 U.S. 543, 561 (1976) (private homes are
“ordinarily afforded the most stringent Fourth Amendment
protection”).

       On one hand, adopting a too-rigorous interpretation of
“reason to believe” seems at odds with the portion of Payton
leading up to the Court’s articulation of the “reason to
believe” rule:

      It is true that an arrest warrant requirement may
      afford less protection than a search warrant
      requirement, but it will suffice to interpose the
      magistrate's determination of probable cause
      between the zealous officer and the citizen. If
      there is sufficient evidence of a citizen’s
      participation in a felony to persuade a judicial
      officer that his arrest is justified, it is
      constitutionally reasonable to require him to




                             24
       open his doors to the officers of the law. Thus,
       for Fourth Amendment purposes, an arrest
       warrant founded on probable cause implicitly
       carries with it the limited authority to enter a
       dwelling in which the suspect lives when there
       is reason to believe the suspect is within.

Payton, 445 U.S. at 602–03 (emphasis added). This language
seems to cut against interpreting the “reason to believe”
standard too stringently insofar as the Court clearly indicates
that the probable cause determination required for an arrest
warrant already offers much of the requisite protection.
Payton, by its terms, however, applies only with respect to an
individual for whom an arrest warrant has been issued and
with respect to the place where he resides. See id. at 583.

       On the other hand, where there is uncertainty about
where the arrestee resides—a situation not presented in
Payton but encompassed within the Circuit-created two-prong
test—we must take care not to adopt an interpretation of
“reason to believe” that requires of law enforcement so little
evidence that an arrestee resides at a dwelling as to expose all
dwellings to an unacceptable risk of police error and
warrantless entry. Here, Steagald comes into play, for to
adopt such an interpretation would be to disregard the
explanation the Court provides there for why it chose to
distinguish Payton and to conclude, in effect, that the homes
of fugitives and non-fugitives are entitled to different degrees
of Fourth Amendment protection:

       Because an arrest warrant authorizes the police
       to deprive a person of his liberty, it necessarily
       also authorizes a limited invasion of that
       person’s privacy interest when it is necessary to




                              25
      arrest him in his home. This analysis, however,
      is plainly inapplicable when the police seek to
      use an arrest warrant as legal authority to enter
      the home of a third party to conduct a search.
      Such a warrant embodies no judicial
      determination whatsoever regarding the person
      whose home is to be searched. Because it does
      not authorize the police to deprive the third
      person of his liberty, it cannot embody any
      derivative authority to deprive this person of his
      interest in the privacy of his home. Such a
      deprivation must instead be based on an
      independent showing that a legitimate object of
      a search is located in the third party’s home.
      We have consistently held, however, that such a
      determination is the province of the magistrate,
      and not that of the police officer.

Steagald, 451 U.S. at 214 n.7 (emphasis added). Like
Payton, Steagald does not contemplate the possibility of
uncertain residency, nor does it address the proper means of
resolving that uncertainty. But read alongside Payton, the
Court’s reasoning in Steagald makes clear that its
determination of the legality of a forced home entry in this
context turns on whether the officer has the benefit of some
type of probable cause determination by a neutral arbiter, be
that by way of an arrest warrant or search warrant.

       Given this precedent and the constitutional principles
at stake, law enforcement armed with only an arrest warrant
may not force entry into a home based on anything less than
probable cause to believe an arrestee resides at and is then
present within the residence. A laxer standard would effect
an end-run around the stringent baseline protection




                             26
established in Steagald and render all private homes—the
most sacred of Fourth Amendment spaces—susceptible to
search by dint of mere suspicion or uncorroborated
information and without the benefit of any judicial
determination. Such intrusions are “the chief evil against
which the wording of the Fourth Amendment is directed.”
Payton, 445 U.S. at 585. We therefore join those Courts of
Appeals that have held that reasonable belief in the Payton
context “embodies the same standard of reasonableness
inherent in probable cause.” Gorman, 314 F.3d at 1111;
accord Barrera, 464 F.3d at 501.

      D.      Application

       Having defined the reasonable belief standard as
equivalent to probable cause, we have no trouble concluding
that law enforcement did not meet that standard as to either
prong of the Payton test here, and the District Court erred in
concluding otherwise.

       To make a probable cause determination, we must
consider the “totality of the circumstances,” Silveus, 542 F.3d
at 1000 (citing Gates, 462 U.S. at 238), which, in the context
of second-hand information, encompasses considerations
such as the basis and reliability of the information and the
receiving officer’s ability to corroborate its content, United
States v. Ritter, 416 F.3d 256, 262–64 (3d Cir. 2005) (citing
Alabama v. White, 496 U.S. 325 (1990)).

       Here, to meet Payton’s first prong, Deputy Marshal
Duncan relied entirely on informant tips and the word of
another detective but provided little information by which the
District Court could assess the information he obtained. At
the suppression hearing, Deputy Marshal Duncan explained




                              27
only that he had based his belief that the intended arrestee,
Rivera, lived at the North 13th Street address on information
conveyed to him by another officer and by informants. He
did not identify the number of informants, their reliability
based on any prior interactions he may have had with them,
the specific information they related, or even whether he
obtained information from “informants on the street” first-
hand or through the other officer. App. 36. Nor did he
describe with any specificity the information provided by that
other officer or the basis for that officer’s statement. See
Whiteley v. Warden, 401 U.S. 560, 568 (1971) (“[A]n
otherwise illegal arrest cannot be insulated from challenge by
the decision of the instigating officer to rely on fellow
officers to make the arrest.”); Rogers v. Powell, 120 F.3d 446,
453 (3d Cir. 1997) (“[S]tatements by fellow officers
conveying that there is probable cause for a person’s arrest,
by themselves, cannot provide the “facts and circumstances”
necessary to support a finding of probable cause . . . . The
legality of a seizure based solely on statements issued by
fellow officers depends on whether the officers who issued
the statements possessed the requisite basis to seize the
suspect.”).

       In his trial testimony, moreover, Deputy Marshal
Duncan cast further doubt on the reasonableness of his belief
that the dwelling was Rivera’s residence when he explained
that the officers knocked vigorously and waited at the door
for a prolonged period in part because “[t]he address was not
the address of record for Mr. Rivera, so we wanted to knock
and attempt to gain contact with somebody inside and gain
their consent to search the address.” App. 138. This
explanation suggests that, at the time of entry, Deputy
Marshal Duncan not only had limited basis to believe Rivera




                              28
resided at the apartment but also possessed evidence that gave
him significant doubt. Cf. Hill, 649 F.3d at 263–64 (officers
did not have reason to believe arrestee was present, because,
among other things, police had documented another residence
for arrestee based on a recent traffic citation, and the lead
officer on the scene testified that he did not believe the
arrestee would be present).

        Nor are we persuaded that the Government met its
burden as to Payton’s second prong, i.e., that it established
probable cause to believe Rivera was present in the apartment
by way of the suspicious sounds the officers heard coming
from inside. True, the Government's burden at this stage is
not onerous, for the threshold determination that there is
probable cause to believe the home is the arrestee’s residence
not only entitles that home to lesser protections under Payton
but also, as a logical matter, increases the likelihood the
arrestee can be found within it. See Payton 445 U.S. at 602
(recognizing “that an arrest warrant requirement may afford
less protection than a search warrant requirement”). Thus,
once the predicate of residency is established, that alone
carries significant weight in establishing probable cause to
believe the arrestee is present, necessarily reducing the
quantum of proof needed to meet Payton’s second prong in
the totality of the circumstances analysis.

       Ultimately, however, that analysis must be made on a
case-by-case basis, accounting not only for the fact that there
is an increased likelihood the arrestee will be found in his
own home but also for other indicia supporting law
enforcement’s belief that the suspect is then inside. See, e.g.,
United States v. Diaz, 491 F.3d 1074, 1078 (9th Cir. 2007)
(officers reasonably believed that arrestee was home because
he himself told government agents that he was usually home




                              29
during the day, they knew he worked at home as a mechanic,
and when they had previously visited he was absent only
once); Pruitt, 458 F.3d at 483 (officers had reasonable belief
parolee was inside the residence where, among other things,
an individual exiting the residence matched the parolee’s
picture to the person selling drugs inside); United States v.
Beck, 729 F.2d 1329, 1331–32 (11th Cir. 1984) (per curiam)
(“Beck’s car, identified by the agents, was parked nearby; and
it was reasonable to believe that one would be at home at 7:30
a.m. and be sound asleep . . . .” (footnote omitted)).

        Here, because the officers lacked probable cause to
believe Rivera lived in the home, mere signs of life inside,
even if suspicious, could not establish probable cause to
believe he was present and could not justify their warrantless
entry into Vasquez-Algarin’s apartment.          Indeed, such
bootstrapping would be clearly untenable as a logical matter,
for law enforcement cannot compensate for the deficiency of
the information underlying its belief that a suspect even lives
at a particular residence by way of generic evidence
indicating merely that someone is inside the home. Cf. Shea
v. Smith, 966 F.2d 127, 131 (3d Cir. 1992) (observing that
“[i]f the police lack probable cause to believe the suspect is
an actual resident, but have probable cause to believe he’s
present, they must get a search warrant.” (quoting Harper,
928 F.2d at 896)).

       In sum, we note that on both prongs of the Payton test,
the information that law enforcement relied upon to justify
breaking into Vasquez-Algarin’s apartment contrasts sharply
in kind and quantity from the information deemed sufficient
by this Court and other Courts of Appeals applying the
probable cause standard. See, e.g., Veal, 453 F.3d at 168
(officers lawfully entered the home of the arrestee’s wife




                              30
where the parole violation warrant indicated he was no longer
living at his last known address and listed his wife as a
possible lead, his former landlord reported that the couple had
lived together in the apartment they rented from him, and the
car the arrestee allegedly drove was registered to his wife and
parked near her home); Route, 104 F.3d at 62–63 (officer
confirmed that the arrestee’s credit card applications, utility
bills and vehicle registration matched the address of the
residence, and at the residence observed a known associate
backing out of the driveway, another vehicle in the driveway,
and noise coming from a television inside the home);
Jackson, 576 F.3d at 469 (concluding “the police had enough
evidence to easily satisfy a probable cause standard” where
they received a tip that the arrestee was residing at a friend’s
apartment and, on their arrival, the arrestee’s girlfriend
confirmed he was inside).

       Just as private citizens are provided protection from
mistaken arrest by the requirement that law enforcement have
probable cause to believe they committed the crime in
question, private homes must be protected from mistaken
entry by, at minimum, a probable cause determination as to
whether the suspect sought even lives there. Because the
officers lacked information sufficient to meet that threshold in
this case, their entry into Vasquez-Algarin’s home and the
subsequent searches were unconstitutional, and, absent some
exception to the exclusionary rule, the evidence they seized
should have been suppressed. We turn, then, to the
Government’s argument that one such exception is
applicable.




                              31
      E. The good-faith exception

       The Government argues that even if officers
unlawfully entered Vasquez-Algarin’s home, his conviction
should stand because the exclusionary rule has no application
and the evidence is admissible under the good-faith exception
where law enforcement’s conduct was not “deliberate,
reckless, or grossly negligent.” Gov’t Br. at 24–25 (citing
Herring v. United States, 555 U.S. 135 (2009)). We are not
persuaded on these facts by the Government’s invocation of
the good-faith exception.

       The Supreme Court has “over time applied [the] good-
faith exception across a range of cases” where applying the
exclusionary rule would not “yield ‘appreciable deterrence.’”
Davis v. United States, 131 S. Ct. 2419, 2426, 2428 (2011)
(quoting United States v. Janis, 428 U.S. 433, 454 (1976)).
For example, the Court has held that, under the good-faith
exception, evidence need not be suppressed where police
conduct a search in “objectively reasonable reliance” on a
search warrant subsequently deemed invalid, United States v.
Leon, 468 U.S. 897, 922 (1984), or on a statute subsequently
held unconstitutional, Illinois v. Krull, 480 U.S. 340, 360
(1987).

       Drawing on this line of cases, in Davis, the Supreme
Court held that “[e]vidence obtained during a search
conducted in reasonable reliance on binding precedent is not
subject to the exclusionary rule.” 131 S. Ct. at 2429. And in
our en banc decision in United States v. Katzin, 769 F.3d 163
(3d Cir. 2014), this Court, in turn, relied on Davis and the
Supreme Court’s prior good-faith decisions to conclude that
the exception applies not only where law enforcement agents
act on binding appellate precedent but also, and more




                             32
fundamentally, where the officers act “upon an objectively
reasonable good faith belief in the legality of their conduct.”
Id. at 182.

       In neither respect is the exception warranted in this
case. First, the Government does not purport to rely on
binding appellate precedent for its assertion that the officers
had sufficient information to forcibly enter Vasquez-
Algarin’s home, nor could it in view of the binding Supreme
Court authority in Payton and Steagald that points the other
way. Even Herring—which the Government cites not as
binding appellate precedent on these facts but for the general
proposition that a finding of a Fourth Amendment violation
does not compel automatic reversal—weighs in favor of
suppression. Herring involved a county’s inadvertent failure
to update its database concerning a recalled arrest warrant—
“isolated negligence attenuated from the arrest” that the Court
determined was not “sufficiently deliberate that exclusion can
meaningfully deter it” or “sufficiently culpable that such
deterrence is worth the price paid by the justice system.” 555
U.S. at 137–38, 144. In contrast, here we are confronted not
with an inadvertent recordkeeping error but with a deliberate
decision to force entry into a home based on only vague and
uncorroborated information as to whether the subject of the
arrest warrant even lived there. The gulf between this case
and Herring is only reinforced by Deputy Marshal Duncan’s
trial testimony acknowledging documentation in his
possession that caused him concern that this was a third-party
residence for which he needed consent to search.

       We thus turn to the second and more fundamental
inquiry we undertook in Katzin, the “objectively ascertainable
question whether a reasonably well trained officer would
have known that the search was illegal under all of the




                              33
circumstances.” 769 F.3d at 179 (quoting Leon, 468 U.S. at
922 n.23). In making this determination, we consider the
decisions set forth by the Supreme Court, our Court and our
sister Circuits. See id. at 182–84. As is apparent from our
survey of the case law, however, those decisions also favor
suppression.

        Read together, Payton and Steagald make clear that,
because of the sanctity of the home, nothing less than
probable cause is appropriate when it comes to determining
whether a home belongs to an arrestee and to undertaking a
forced entry on the basis of an arrest warrant alone. See
supra Section II.A. As for our own precedent, although we
have clarified today that “reasonable belief” in the Payton
context does indeed amount to probable cause, our decisions
to date have assumed as much and used probable cause as the
applicable standard. See Veal, 453 F.3d at 167 n.3; Agnew,
407 F.3d at 196. Lastly, where this Court and our sister
Circuits have upheld the validity of police entries into homes
under Payton, it has been on the basis of far more specific and
reliable information than what the officers relied upon here to
enter Vasquez-Algarin’s apartment, see Section II.D, and
conversely, where the only evidence available has been of
such meager quantity and quality, the Courts of Appeals have
held that suppression is appropriate, see, e.g., Werra, 638
F.3d at 341; Hardin, 539 F.3d at 427. Thus, in contrast with
Katzin, where “[t]he constellation of circumstances that
appeared to authorize [the officers’] conduct included well
settled principles of Fourth Amendment law as articulated by
the Supreme Court [and] a near-unanimity of circuit courts
applying these principles to the same conduct,” 769 F.3d at
182, the very opposite is true here.




                              34
       We do not take lightly the “significant social costs of
suppressing reliable, probative evidence.” Id. However, we
are compelled to enforce the exclusionary rule where law
enforcement officers, “at the time they acted, would have or
should have known their [conduct] w[as] unconstitutional.”
Id. at 179. The Government’s argument in this case boils
down to the proposition that law enforcement officers may
forcibly enter a home based on nothing more than the general
representation of another law enforcement officer and the
vague and uncorroborated assertions of unidentified
informants that the intended arrestee lives there. We reject
this position as inconsistent with fundamental Fourth
Amendment principles and the language and logic of
Supreme Court precedent governing in-home arrests. Given
the dictates of Payton and Steagald, our prior applications of
Payton in Veal and Agnew, and the out-of-Circuit precedent
consistently holding law enforcement to a higher bar than
what was proffered here to justify a forced home entry, we
conclude the officers’ conduct was, at a minimum, “grossly
negligent,” and thus was “sufficiently deliberate that
exclusion can meaningfully deter it, and sufficiently culpable
that such deterrence is worth the price paid by the justice
system.” Herring, 555 U.S. at 144.

III.   Conclusion

       For the foregoing reasons, we will reverse the District
Court’s denial of Vasquez-Algarin’s motion to suppress,
vacate the conviction, and remand for proceedings consistent
with this opinion.




                             35

```

---
