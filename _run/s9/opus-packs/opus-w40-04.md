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

## GROUP: content/cases/United States v. Cortez.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Cortez"
type: case
citation: "449 U.S. 411 (1981)"
parallel_cite: "101 S. Ct. 690; 66 L. Ed. 2d 621; 49 U.S.L.W. 4099"
neutral_cite: 1981 U.S. LEXIS 58
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-01-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Cortez
  varies_by_point: false
  scope_note: "Good law; the 'particularized and objective basis' / 'whole picture' formulation of reasonable suspicion."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110377/united-states-v-cortez/"
  cluster_id: 110377
  opinion_id: 110377
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Anchor"
related: ["[[Terry v. Ohio]]", "[[United States v. Arvizu]]", "[[Navarette v. California]]", "[[Ornelas v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-suspicion", "terry-stop"]
holding: "Reasonable suspicion = a particularized and objective basis on the totality of the circumstances (the 'whole picture')."
lake:
  record_id: United States v. Cortez
  status: verified
  projected_at: 2026-07-06
---

# United States v. Cortez

*449 U.S. 411 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Border Patrol officers studied evidence of an alien-smuggling operation: footprints in a remote desert area showed a guide (nicknamed "Chevron" from a distinctive shoe print) leading groups on certain nights, and the tracks led toward a pickup point near a particular highway. From the pattern of clues — the likely night, time window, direction of travel, and that a vehicle would be needed to carry the group — the officers deduced when and where the smuggler's vehicle would pass, stopped a matching truck, and found illegal aliens inside.

## Issue
What quantum and kind of basis the Fourth Amendment requires for an investigatory vehicle stop — i.e., how reasonable suspicion is assessed.

## Rule
Reasonable suspicion is a particularized, objective judgment drawn from the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]: "the totality of the circumstances—the whole picture—must be taken into account. Based upon that whole picture the detaining officers must have a particularized and objective basis for suspecting the particular person stopped of criminal activity." — 449 U.S. at 417–18. ^pin-417

The assessment permits officers to draw on their experience and to make commonsense inferences and deductions about the cumulative information available to them.

## Application
The officers' chain of inferences — reconstructing the smuggler's method, route, likely night, and the time window from the physical clues, and reasoning that a vehicle would be needed at a predictable point — gave them a particularized and objective basis to suspect that the specific truck they stopped was carrying illegal aliens. Viewed as a whole rather than as isolated facts, that picture supported reasonable suspicion, so the investigatory stop was valid.

## Conclusion
The stop was supported by reasonable suspicion and was upheld. Reasonable suspicion is measured by the whole picture and requires a particularized and objective basis, informed by the officers' experience and reasonable inferences.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Cortez* refines the reasonable-suspicion standard of [[Terry v. Ohio]] and supplied the "whole picture" / "particularized and objective basis" language later applied in [[United States v. Arvizu]] (no divide-and-conquer), [[Ornelas v. United States]], and [[Navarette v. California]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key — Progeny / Refinement*
- [[Reasonable Suspicion]] — *Key — Anchor*

## Sources
- *United States v. Cortez*, 449 U.S. 411 (1981) — https://www.courtlistener.com/opinion/110377/united-states-v-cortez/ — pinpoint: 417–18.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e63a2f87f522ad6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "449 U.S. 411 (1981)", "court": "U.S. Supreme Court", "neutral_cite": "1981 U.S. LEXIS 58", "official_citation_present": true, "parallel_cite": "101 S. Ct. 690; 66 L. Ed. 2d 621; 49 U.S.L.W. 4099", "title": "United States v. Cortez", "year": "1981"}}
{"assertion_id": "1fe5bb7fc52a9630", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Anchor", "title": "United States v. Cortez"}}
{"assertion_id": "5dbd02b530122e8f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Reasonable suspicion = a particularized and objective basis on the totality of the circumstances (the 'whole picture').", "title": "United States v. Cortez"}}
{"assertion_id": "ddf43548ba327b40", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "United States v. Cortez"}}
{"assertion_id": "a00ee67ff7924f56", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Cortez"}}
{"assertion_id": "a0f470e84420b1e5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1981-01-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Cortez", "field_i_validity": "good_law", "scope_note": "Good law; the 'particularized and objective basis' / 'whole picture' formulation of reasonable suspicion.", "title": "United States v. Cortez", "varies_by_point": "false"}}
```

### lake record — United States v. Cortez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cortez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Cortez",
    "case_name_short": "Cortez",
    "case_name_full": "UNITED STATES v. CORTEZ Et Al.",
    "input_case_name": "United States v. Cortez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-01-21",
    "year": 1981,
    "docket": null,
    "cluster_id": 110377,
    "lead_opinion_id": 110377,
    "sibling_ids": [
      110377,
      9428131,
      9428132
    ],
    "absolute_url": "/opinion/110377/united-states-v-cortez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "449 U.S. 411",
      "volume": "449",
      "reporter": "U.S.",
      "page": "411",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 690",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 L. Ed. 2d 621",
        "volume": "66",
        "reporter": "L. Ed. 2d",
        "page": "621",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4099",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4099",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 58",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "449 U.S. 411",
        "volume": "449",
        "reporter": "U.S.",
        "page": "411",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 690",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 L. Ed. 2d 621",
        "volume": "66",
        "reporter": "L. Ed. 2d",
        "page": "621",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 58",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4099",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4099",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "449 U.S. 411",
    "official_selection": {
      "court_class": "scotus",
      "selected": "449 U.S. 411",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-417",
      "page": null,
      "quote": "from a distinctive shoe print) leading groups on certain nights, and the tracks led toward a pickup point near a particular highway. From the pattern of clues \u2014 the likely night, time window, direction of travel, and that a vehicle would be needed to carry the group \u2014 the officers deduced when and where the smuggler's vehicle would pass, stopped a matching truck, and found illegal aliens inside. ## Issue What quantum and kind of basis the Fourth Amendment requires for an investigatory vehicle stop \u2014 i.e., how reasonable suspicion is assessed. ## Rule Reasonable suspicion is a particularized, objective judgment drawn from the totality of the circumstances:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Cortez",
    "varies_by_point": false,
    "scope_note": "Good law; the 'particularized and objective basis' / 'whole picture' formulation of reasonable suspicion.",
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
        "journal_ref": "United States v. Cortez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane1_negative"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 1355298,
          "cite": [
            "158 S.W.3d 488",
            "2005 Tex. Crim. App. LEXIS 399",
            "2005 WL 544796"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110377 OR 9428131 OR 9428132) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQwMDQ0ODAwMDAwJnM9MTAzMTYwNzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110377+OR+9428131+OR+9428132%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110377 OR 9428131 OR 9428132)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODcmcz0xNTE2NTcxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110377+OR+9428131+OR+9428132%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110377 OR 9428131 OR 9428132)",
        "reviewed": 171,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 171,
        "triage_read": 1,
        "triage_snippet_classified": 170
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110377 OR 9428131 OR 9428132)",
    "indexed_citing_opinions": 3643,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110377,
        "count": 3198,
        "count_source": "search"
      },
      {
        "opinion_id": 9428131,
        "count": 501,
        "count_source": "search"
      },
      {
        "opinion_id": 9428132,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5978,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-cortez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0NzA5MyZzPTEwNjQ2MjMxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110377+OR+9428131+OR+9428132%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110377,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 364821,
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
    "date_created": "2026-07-05T23:17:11Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:17:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:17:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:22:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:17:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Cortez

```
<div>
<center><b><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U.S. 411</a></span> (1981)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
CORTEZ ET AL.</h1></center>
<center>No. 79-404.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 1, 1980.</center>
<center>Decided January 21, 1981.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*412</span> <i>Barbara E. Etkind</i> argued the cause for the United States. With her on the briefs were <i>Solicitor General McCree, Assistant Attorney General Heymann, Deputy Solicitor General Frey, William G. Otis,</i> and <i>John C. Winkfield.</i></p>
<p><i>S. Jeffrey Minker</i> argued the cause and filed a brief for respondent Cortez.</p>
<p><i>Bernardo P. Velasco</i> argued the cause for respondent Hernandez-Loera. With him on the brief was <i>Thomas W. O'Toole.</i></p>
<p>CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./447/904/">447 U. S. 904</a></span>, to consider whether objective facts and circumstantial evidence suggesting that a particular vehicle is involved in criminal activity may provide <span class="star-pagination">*413</span> a sufficient basis to justify an investigative stop of that vehicle.</p>
<p></p>
<h2>I</h2>
<p>Late in 1976, Border Patrol officers patrolling a sparsely populated section of southern central Arizona found human footprints in the desert. In time, other sets of similar foot-prints were discovered in the same area. From these sets of footprints, it was deduced that, on a number of occasions, groups of from 8 to 20 persons had walked north from the Mexican border, across 30 miles of desert and mountains, over a fairly well-defined path, to an isolated point on Highway 86, an east-west road running roughly parallel to the Mexican border.</p>
<p>Officers observed that one recurring shoeprint bore a distinctive and repetitive V-shaped or chevron design. Because the officers knew from recorded experience that the area through which the groups passed was heavily trafficked by alines illegally entering the country from Mexico, they surmised that a person, to whom they gave the case-name "Chevron," was guiding aliens illegally into the United States over the path marked by the tracks to a point where they could be picked up by a vehicle.</p>
<p>The tracks led into or over obstacles that would have been avoided in daylight. From this, the officers deduced that "Chevron" probably led his groups across the border and to the pickup point at night. Moreover, based upon the times when they had discovered the distinctive sets of tracks, they concluded that "Chevron" generally traveled during or near weekends and on nights when the weather was clear.</p>
<p>Their tracking disclosed that when "Chevron's" groups came within 50 to 75 yards of Highway 86, they turned right and walked eastward, parallel to the road. Then, approximately at highway milepost 122, the tracks would turn north and disappear at the road. From this pattern, the officers concluded that the aliens very likely were picked up by a vehicle <span class="star-pagination">*414</span> probably one approaching from the east, for after a long overland march the group was most likely to walk parallel to the highway <i>toward</i> the approaching vehicle. The officers also concluded that, after the pickup, the vehicle probably returned to the east, because it was unlikely that the group would be walking away from its ultimate destination.</p>
<p>On the Sunday night of January 30-31, 1977, Officers Gray and Evans, two Border Patrolmen who had been pursuing the investigation of "Chevron," were on duty in the Casa Grande area. The latest set of observed "Chevron" tracks had been made on Saturday night, January 15-16. January 30-31 was the first clear night after three days of rain. For these reasons. Gray and Evans decided there was a strong possibility that "Chevron" would lead aliens from the border to the highway that night.</p>
<p>The officers assumed that, if "Chevron" did conduct a group that night, he would not leave Mexico until after dark, that is, about 6 p. m. They knew from their experience that groups of this sort, traveling on foot, cover about two and a half to three miles an hour. Thus, the 30-mile journey would take from 8 to 12 hours. From this, the officers calculated that "Chevron" and his group would arrive at Highway 86 somewhere between 2 a. m. and 6 a. m. on January 31.</p>
<p>About 1 a. m., Gray and Evans parked their patrol car on an elevated location about 100 feet off Highway 86 at milepost 149, a point some 27 miles east of milepost 122. From their vantage point, the officers could observe the Altar Valley, an adjoining territory they had been assigned to watch that night, and they also could see vehicles passing on Highway 86. They estimated that it would take approximately one hour and a half for a vehicle to make a round trip from their vantage point to milepost 122. Working on the hypothesis that that the pickup vehicle approached milepost 122 from the east and thereafter returned to its starting point, they focused upon vehicles that passed them from the east <span class="star-pagination">*415</span> and, after about one hour and a half, passed them returning to the east.</p>
<p>Because "Chevron" appeared to lead groups of the between 8 and 20 aliens at a time, the officers deduced that the pickup vehicle would be one that was capable of carrying that large a group without arousing suspicion. For this reason, and because they knew that certain types of vehicles were commonly used for smuggling sizable groups of aliens, they decided to limit their attention to vans, pickup trucks, other small trucks, campers, motor homes, and similar vehicles.</p>
<p>Traffic on Highway 86 at milepost 149 was normal on the night of the officers' surveillance. In the 5-hour period between 1 a. m. and 6 a. m., 15 to 20 vehicles passed the officers heading west, toward milepost 122. Only two of themboth pickup trucks with camper shellswere of the kind that the officers had concluded "Chevron" would likely use if he was to carry aliens that night. One, a distinctively colored pickup truck with a camper shell, passed for the first time at 4:30 a. m. Officer Gray was able to see and record only a partial license number, "GN 88."<sup>[1]</sup> At 6:12 a. m., almost exactly the estimated one hour and a half later, a vehicle looking like this same pickup passed them again, this time heading east.</p>
<p>The officers followed the pickup and were satisfied from its license plate, "GN 8804," that it was the same vehicle that had passed at 4:30 a. m. At that point, they flashed their police lights and intercepted the vehicle. Respondent Jesus Cortez was the driver and owner of the pickup; respondent Pedro Hernandez-Loera was sitting in the passenger's seat. Hernandez-Loera was wearing shoes with soles matching the distinctive "Chevron" shoeprint.</p>
<p>The officers identified themselves and told Cortez they were conducting an immigration check. They asked if he was <span class="star-pagination">*416</span> carrying any passengers in the camper. Cortez told them he had picked up some hitchhikers, and he proceeded to open the back of the camper. In the camper, there were six illegal aliens. The officers then arrested the respondents.</p>
<p>Cortez and Hernandez-Loera were charged with six counts of transporting illegal aliens in violation of <span class="citation no-link">8 U. S. C. § 1324</span> (a). By pretrial motion, they sought to suppress the evidence obtained by Officers Gray and Evans as a result of stopping their vehicle. They argued that the officers did not have adequate cause to make the investigative stop. The District Court denied the motion. A jury found the respondents guilty as charged. They were sentenced to concurrent prison terms of five years on each of six counts. In addition, Hernandez-Loera was fined $12,000.</p>
<p>A divided panel of the Court of Appeals for the Ninth Circuit reversed, holding that the officers lacked a sufficient basis to justify the stop of the pickup. <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E....">595 F. 2d 505</a></span> (1979). That court recognized that <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975), provides a standard governing investigative stops of the kind involved in this case, stating:</p>
<blockquote>"The quantum of cause necessary in . . . cases [like this one] was established . . . in <i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i>. . . . `[O]fficers on roving patrol may stop vehicles only if they are aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion that the vehicles contain aliens who may be illegally in the country.'" <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E....">595 F. 2d, at 507</a></span> (quoting <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>) (citations omitted).</blockquote>
<p>The court also recognized that "the ultimate question on appeal is whether the trial judge's finding that founded suspicion was present here was clearly erroneous." <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/#507" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E....">595 F. 2d, at 507</a></span>. Here, because, in the view of the facts of the two judges constituting the majority, "[t]he officers did not have a valid basis for singling out the Cortez vehicle," <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/#508" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E...."><i>id.,</i> at 508</a></span>, and because <span class="star-pagination">*417</span> the circumstances admitted "far too many innocent inferences to make the officers' suspicions reasonably warranted," <i>ibid.,</i> the panel concluded that the stop of Cortez' vehicle was a violation of the respondents' rights under the Fourth Amendment. In dissent, Judge Chambers was persuaded that <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> recognized the validity of permitting an officer to assess the facts in light of his past experience.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>The Fourth Amendment applies to seizures of the person, including brief investigatory stops such as the stop of the vehicle here. <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438, 440</a></span> (1980); <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878</a></span>; <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968). An investigatory stop must be justified by some objective manifestation that the person stopped is, or is about to be, engaged in criminal activity.<sup>[2]</sup><i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979); <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 661</a></span> (1979); <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>; <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146-149</a></span> (1972); <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 16-19</a></span>.</p>
<p>Courts have used a variety of terms to capture the elusive concept of what cause is sufficient to authorize police to stop a person. Terms like "articulable reasons" and "founded suspicion" are not self-defining; they fall short of providing clear guidance dispositive of the myriad factual situations that arise. But the essence of all that has been written is that the totality of the circumstancesthe whole picture must be taken into account. Based upon that whole picture the detaining officers must have a particularized and objective basis for suspecting the particular person stopped of criminal <span class="star-pagination">*418</span> activity. See, <i>e. g., </i><i>Brown</i> v. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>Texas, supra,</i> at 51</a></span>; <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>.</p>
<p>The idea that an assessment of the whole picture must yield a particularized suspicion contains two elements, each of which must be present before a stop is permissible. First, the assessment must be based upon all of the circumstances. The analysis proceeds with various objective observations, information from police reports, if such are available, and consideration of the modes or patterns of operation of certain kinds of lawbreakers. From these data, a trained officer draws inferences and makes deductionsinferences and deductions that might well elude an untrained person.</p>
<p>The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain commonsense conclusions about human behavior; jurors as factfinders are permitted to do the sameand so are law enforcement officers. Finally, the evidence thus collected must be seen and weighed not in terms of library analysis by scholars, but as understood by those versed in the field of law enforcement.</p>
<p>The second element contained in the idea that an assessment of the whole picture must yield a particularized suspicion is the concept that the process just described must raise a suspicion that the particular individual being stopped is engaged in wrongdoing. Chief Justice Warren, speaking for the Court in <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> said that "[t]his demand for specificity in the information upon which police action is predicated is <i>the central teaching of this Court's Fourth Amendment jurisprudence." Id.,</i> at 21, n. 18 (emphasis added). See also <i>Brown</i> v. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>Texas, supra,</i> at 51</a></span>; <i>Delaware</i> v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse"><i>Prouse, supra,</i> at 661-663</a></span>; <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>.</p>
<p></p>
<h2>B</h2>
<p>This case portrays at once both the enormous difficulties of patrolling a 2,000-mile open border and the patient skills <span class="star-pagination">*419</span> needed by those charged with halting illegal entry into this country. It implicates all of the principles just discussed especially the imperative of recognizing that, when used by trained law enforcement officers, objective facts, meaningless to the untrained, can be combined with permissible deductions from such facts to form a legitimate basis for suspicion of a particular person and for action on that suspicion. We see here the kind of police work often suggested by judges and scholars as examples of appropriate and reasonable means of law enforcement. Here, fact on fact and clue on clue afforded a basis for the deductions and inferences that brought the officers to focus on "Chevron."</p>
<p>Of critical importance, the officers knew that the area was a crossing point for illegal aliens. They knew that it was common practice for persons to lead aliens through the desert from the border to Highway 86, where they couldby pre-arrangement be picked up by a vehicle. Moreover, based upon clues they had discovered in the 2-month period prior to the events at issue here, they believed that one such guide, whom they designated "Chevron," had a particular pattern of operations.</p>
<p>By piecing together the information at their disposal, the officers tentatively concluded that there was a reasonable likelihood that "Chevron" would attempt to lead a group of aliens on the night of Sunday, January 30-31. Someone with chevron-soled shoes had led several groups of aliens in the previous two months, yet it had been two weeks since the latest crossing. "Chevron," they deduced, was therefore due reasonably soon. "Chevron" tended to travel on clear weekend nights. Because it had rained on the Friday and Saturday nights of the weekend involved here, Sunday was the only clear night of that weekend; the officers surmised it was therefore a likely night for a trip.</p>
<p>Once they had focused on that night, the officers drew upon other objective facts known to them to deduce a time frame <span class="star-pagination">*420</span> within which "Chevron" and the aliens were likely to arrive. From what they knew of the practice of those who smuggle aliens, including what they knew of "Chevron's" previous activities, they deduced that the border crossing and journey through the desert would probably be at night. They knew the time when sunset would occur at the point of the border crossing; they knew about how long the trip would take. They were thus able to deduce that "Chevron" would likely arrive at the pickup point on Highway 86 in the time frame between 2 a. m. and 6 a. m.</p>
<p>From objective facts, the officers also deduced the probable point on the highwaymilepost 122at which "Chevron" would likely rendezvous with a pickup vehicle. They deduced from the direction taken by the sets of "Chevron" footprints they had earlier discovered that the pickup vehicle would approach the aliens from, and return with them to, a point east of milepost 122. They therefore staked out a position east of milepost 122 (at milepost 149) and watched for vehicles that passed them going west and then, approximately one and a half hours later, passed them again, this time going east.</p>
<p>From what they had observed about the previous groups guided by the person with "chevron" shoes, they deduced that "Chevron" would lead a group of 8 to 20 aliens. They therefore focused their attention on enclosed vehicles of that passenger capacity.</p>
<p>The analysis produced by Officers Gray and Evans can be summarized as follows: if, on the night upon which they believed "Chevron" was likely to travel, sometime between 2 a. m. and 6 a. m., a large enclosed vehicle was seen to make an east-west-east round trip to and from a deserted point (milepost 122) on a deserted road (Highway 86), the officers would stop the vehicle on the return trip. In a 4-hour period the officers observed only one vehicle meeting that description. And it is not surprising that when they stopped the <span class="star-pagination">*421</span> vehicle on its return trip it contained "Chevron" and several illegal aliens.<sup>[3]</sup></p>
<p></p>
<h2>C</h2>
<p>The limited purpose of the stop in this case was to question the occupants of the vehicle about their citizenship and immigration status and the reasons for the round trip in a short timespan in a virtually deserted area. No search of the camper or any of its occupants occurred until after respondent Cortez voluntarily opened the back door of the camper; thus, only the stop, not the search is at issue here. The intrusion upon privacy associated with this stop was limited and was "reasonably related in scope to the justification for [its] initiation," <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 29</a></span>.</p>
<p>We have recently held that stops by the Border Patrol may be justified under circumstances less than those constituting probable cause for arrest or search. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 880</a></span>.<sup>[4]</sup> Thus, the test is not whether Officers Gray and Evans had probable cause to conclude that the vehicle they stopped would contain "Chevron" and a group of illegal aliens. Rather the question is whether, based upon the whole picture, they, as experienced Border Patrol officers, could reasonably surmise that the particular vehicle <span class="star-pagination">*422</span> they stopped was engaged in criminal activity. On this record, they could so conclude.</p>
<p><i>Reversed.</i></p>
<p>JUSTICE MARSHALL concurs in the judgment.</p> <p>JUSTICE MARSHALL concurs in the judgment.</p>
<p>JUSTICE STEWART, concurring in the result.</p>
<p>The Border Patrol officers in this case knew, or had rationally deduced, that "Chevron" had repeatedly shepherded illegal aliens up from the border; that his treks had commonly ended early in the morning around milepost 122 on Highway 86; that he usually worked on weekends; that he probably had made no trips for two weeks; and that trips were most likely when the weather was good. Knowing of this pattern, the officers could reasonably anticipate, even if they could not guarantee, the arrival of another group of aliens, led by Chevron, at milepost 122 on the first clear weekend night in late January 1977. Route 86 leads through almost uninhabited country, so little travelled in the hours of darkness that only 15 to 20 westbound vehicles passed the police during the five hours they watched that Sunday night. Only two vehicles capacious enough to carry a sizable group of illegal aliens went by. One of those two vehicles not only drove past them, but returned in the opposite direction after just enough time had elapsed for a journey to milepost 122 and back. This nocturnal round trip into "desolate desert terrain" would in any event have been puzzling. Coming when and as it did, surely the most likely explanation for it was that Chevron was again shepherding aliens.</p>
<p>In sum, the Border Patrol officers had discovered an abundance of "specific articulable facts" which, "together with rational inferences from [them]," entirely warranted a "suspicion that the vehicl[e] contain[ed] aliens who [might] be illegally in the country." <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="star-pagination">*423</span> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 884</a></span>. Because the information possessed by the officers thus met the requirements established by the <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> case for the kind of stop made here, I concur in the reversal of the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[1]  The second camper passed them 15 or 20 minutes later. As far as the record shows, it did not return.</p>
<p>[2]  Of course, an officer may stop and question a person if there are reasonable grounds to believe that person is wanted for past criminal conduct.</p>
<p>[3]  In <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 884-885</a></span> (1975), the Court listed several factors to be considered as part of the totality of the circumstances in determining the existence <i>vel non</i> of a particularized suspicion in cases treating official attempts to stem the influx of illegal aliens into our country. Though the list did not purport to be exhaustive, it is noteworthy that several of the factors present here were recognized by <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> as significant in this context; for example, information about recent border crossings and the type of vehicle involved.</p>
<p>[4]  The wide public interest in effective measures to prevents the entry of illegal aliens at the Mexican border has been cataloged by this Court. See, <i>e. g., </i><i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#899" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 899-914</a></span> (1975) (BURGER, C. J., concurring in judgment); <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878-879</a></span>.</p>

</div>
```

---

## GROUP: content/cases/United States v. Donovan.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Donovan
type: case
citation: "429 U.S. 413 (1977)"
parallel_cite: "97 S. Ct. 658; 50 L. Ed. 2d 652"
neutral_cite: 1977 U.S. LEXIS 36
court: U.S.
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-18
docket: 75-212
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
  opinion_url: "https://www.courtlistener.com/opinion/109584/united-states-v-donovan/"
  cluster_id: 109584
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Donovan
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Electronic Surveillance and Title III]]"
    role: Anchor
related:
  - "[[Electronic Surveillance and Title III]]"
  - "[[United States v. Giordano]]"
  - "[[Scott v. United States]]"
tags:
  - case
  - fourth-amendment
  - electronic-surveillance
  - title-iii
  - wiretap
  - suppression
  - inventory-notice
holding: "Title III's identification requirement, § 2518(1)(b)(iv), obliges the Government to name in a wiretap application every person it has probable cause to believe is committing the offense and whose communications will be intercepted, and § 2518(8)(d) requires it to give the issuing judge a complete list of identifiable persons overheard so the judge can decide who receives inventory notice; but the failure to comply fully with either provision does not render the interception 'unlawful' and does not require suppression, because those requirements do not directly and substantially implement Congress's purpose of confining wiretaps to situations that clearly call for them."
aliases:
  - United States v. Donovan
  - "United States v. Donovan (1977)"
---

# United States v. Donovan

*429 U.S. 413 (1977)* (No. 75-212) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109584 → combined opinion 109584 (Powell, J.; 429 U.S. 413, argued Oct. 13, 1976, decided Jan. 18, 1977). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted holding sits between `*434` and `*435`, i.e., on page 434). S9 promotes. -->

## Background
A Title III wiretap on gambling-related telephones in Ohio named certain principal targets and "others as yet unknown." During the tap the Government learned that respondents Donovan, Robbins, and Buzzacco were discussing gambling with the named subjects, but when it sought an extension it did not add their names to the application. Later, when the Government proposed a list of persons to receive post-interception inventory notice, two other participants — Merlo and Lauer — were left off through what the Government called "administrative oversight" and never received notice. On the defendants' motions, the District Court suppressed the wiretap evidence: as to Donovan, Robbins, and Buzzacco for the failure to name them, and as to Merlo and Lauer for the failure to serve inventory notice. The Sixth Circuit affirmed, holding both requirements played a "central role" in the statute.

## Issue
Whether § 2518(1)(b)(iv) requires naming every person the Government has probable cause to believe will be overheard committing the offense; whether the Government must give the issuing judge a complete list of identifiable persons overheard under § 2518(8)(d); and whether failure to comply with those provisions requires suppression under § 2518(10)(a).

## Rule
The Court agreed the Government must identify all persons it has probable cause to believe are engaged in the offense and will be intercepted, and must supply the judge a complete list of identifiable persons overheard — but held that violating those requirements does not trigger suppression. Drawing on *[[United States v. Giordano|Giordano]]*, it explained that suppression is required only for a failure to satisfy statutory requirements that "directly and substantially implement the congressional intention to limit the use of intercept procedures"; the identification and notice provisions, though important, are not of that character: "Although both statutory requirements are undoubtedly important, we do not think that the failure to comply fully with those provisions renders unlawful an intercept order that in all other respects satisfies the statutory requirements." — 429 U.S. at 434. ^pin-434

## Application
The failure to name additional targets could not invalidate an order the issuing judge was authorized to enter, because the judge's decision to approve the wiretap turned on probable cause, necessity, and the target facilities — not on a complete roster of everyone who might later be overheard. Likewise, the post-interception notice provisions serve to inform surveilled persons after the fact; their breach did not affect the lawfulness of the interceptions themselves. Because the orders were facially sufficient and the interceptions conformed to them, the communications were not "unlawfully intercepted," and suppression was unwarranted.

## Conclusion
The judgment of the Court of Appeals for the Sixth Circuit was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Powell, J., delivered the opinion of the Court. Burger, C.J., filed an opinion concurring in part and concurring in the judgment, and there were separate opinions concurring and dissenting in part (including Marshall, J., dissenting in part).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Donovan* anchors Title III's suppression calculus: not every statutory violation makes an interception "unlawful," so suppression follows only where the breached requirement "directly and substantially" implements Congress's core limits on wiretapping. Teach it against *[[United States v. Giordano]]* (violation of the senior-approval requirement *does* require suppression) as the two poles of the *Giordano/Chavez* suppression test, and with *[[Scott v. United States]]* on minimization.

## Appears on
- [[Electronic Surveillance and Title III]] — *Anchor*

## Sources
- [*United States v. Donovan*, 429 U.S. 413 (1977)](https://www.courtlistener.com/opinion/109584/united-states-v-donovan/) — pinpoint: 434 (Powell, J., for the Court; the CL opinion text places the quoted holding between the reporter stars `*434` and `*435`, i.e., on page 434). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1fc64116b94e86ed", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "429 U.S. 413 (1977)", "court": "U.S.", "neutral_cite": "1977 U.S. LEXIS 36", "official_citation_present": true, "parallel_cite": "97 S. Ct. 658; 50 L. Ed. 2d 652", "title": "United States v. Donovan", "year": "1977"}}
{"assertion_id": "c24cc20da72360d2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Title III's identification requirement, § 2518(1)(b)(iv), obliges the Government to name in a wiretap application every person it has probable cause to believe is committing the offense and whose communications will be intercepted, and § 2518(8)(d) requires it to give the issuing judge a complete list of identifiable persons overheard so the judge can decide who receives inventory notice; but the failure to comply fully with either provision does not render the interception 'unlawful' and does not require suppression, because those requirements do not directly and substantially implement Congress's purpose of confining wiretaps to situations that clearly call for them.", "title": "United States v. Donovan"}}
{"assertion_id": "cf0decd7642cc1e2", "dimension": "support", "kind": "home_role", "locator": {"home": "Electronic Surveillance and Title III"}, "payload": {"home": "Electronic Surveillance and Title III", "role": "Anchor", "title": "United States v. Donovan"}}
{"assertion_id": "e3a5e6eae3e5ac4a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Donovan"}}
{"assertion_id": "fbcb7ac7064aa168", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Donovan", "varies_by_point": "false"}}
```

### lake record — United States v. Donovan

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Donovan",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Donovan",
    "case_name_short": "Donovan",
    "case_name_full": "UNITED STATES v. DONOVAN Et Al.",
    "input_case_name": "United States v. Donovan",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-18",
    "year": 1977,
    "docket": "75-212",
    "cluster_id": 109584,
    "lead_opinion_id": 9426645,
    "sibling_ids": [],
    "absolute_url": "/opinion/109584/united-states-v-donovan/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 413",
      "volume": "429",
      "reporter": "U.S.",
      "page": "413",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 658",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 652",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 36",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "36",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 413",
        "volume": "429",
        "reporter": "U.S.",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 658",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 652",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 36",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "36",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 413",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 413",
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
    "date_created": "2026-07-07T13:27:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-donovan--109584",
      "to_record_id": "United States v. Donovan",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Donovan

```
<opinion type="majority">
<author id="b566-5">Me. Justice Powell</author>
<p id="AV">delivered the opinion of the Court.</p>
<p id="b566-6">This case presents issues concerning the construction of Title III of the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>. Specifically, we must decide whether <span class="citation no-link">18 U. S. C. §2518</span> (l)(b)(iv), which requires the Government to include in its wiretap applications “the identity of the person, if known, committing the offense and whose communications are to be intercepted,” is satisfied when the Government identifies only the “principal targets” of the intercept. Second, we must decide whether the Government has a statutory responsibility to inform the issuing judge of the identities of persons whose conversations were overheard in the course of the interception, thus enabling him to decide whether they should be served with notice of the interception pursuant to <span class="citation no-link">18 U. S. C. §2518</span>(8)(d). And finally, we must determine whether failure to comply fully with these statutory provisions requires suppression of evidence under <span class="citation no-link">18 U. S. C. §2518</span> (10)(a).</p>
<p id="b566-7">I</p>
<p id="b566-8">On November 28, 1972, a special agent of the Federal Bureau of Investigation applied to the United States District Court for the Northern District of Ohio for an order authorizing a wiretap interception in accordance with Title III.<footnotemark>1</footnotemark> The application requested authorization to intercept <page-number citation-index="1" label="417">*417</page-number>gambling-related communications over two telephones at one address in North Olmstead, Ohio, and two other telephones at a home in Canton, Ohio. The accompanying affidavit recited that the telephones were being used by Albert Kotoch, Joseph Spaganlo, and George Florea' to conduct an illegal gambling business, and that in conducting that business they <page-number citation-index="1" label="418">*418</page-number>would place calls to and receive calls from various persons, three of whom were also named in the wiretap application.<footnotemark>2</footnotemark> The affiant also stated that the Government’s informants would refuse to testify against the persons named ha the application, that telephone records alone would be insufficient to support a gambling conviction, and that normal investigative techniques were unlikely to be fruitful. Pursuant to the Government’s request, the District Court authorized for a period of 15 days the interception of gambling-related wire communications of Kotoch, Spaganlo, Florea, three named individuals other than the respondents, and “others, as yet unknown,” to and from the four listed telephones.<footnotemark>3</footnotemark></p>
<p id="b569-4"><page-number citation-index="1" label="419">*419</page-number>During the course of the wiretap, the Government learned that respondents Donovan, Robbins, and Buzzacco were discussing illegal gambling activities with the named subjects. On December 26, 1972, the Government applied for an extension of the initial intercept order.<footnotemark>4</footnotemark> This time it sought authorization to intercept gambling-related conversations of Kotoch, Spaganlo, Florea, two other named individuals, and “others as yet unknown,” but it did not identify respondents Donovan, Buzzacco, and Robbins in this second application.<footnotemark>5</footnotemark> <page-number citation-index="1" label="420">*420</page-number>The District Court again authorized interception of gambling-related conversations for a maximum of 15 days.</p>
<p id="b570-5">On February 21, 1973, the Government submitted to the District Court a proposed order giving notice of the interceptions to 37 persons, a group which the Government apparently thought included all individuals who could be identified as having discussed gambling over the monitored telephones.<footnotemark>6</footnotemark> The District Court signed the proposed order, and an inventory notice was served on the listed persons, including respondents Donovan, Buzzacco, and Robbins. On September 11, 1973, after the Government submitted the names of two additional persons whose identities allegedly had been omitted inadvertently from the initial list, the District Court entered an amended order giving notice to those individuals. As a result of what the Government labels “administrative oversight,” respondents Merlo and Lauer were not included in either list of names and were never served with inventory notice.<footnotemark>7</footnotemark></p>
<p id="b571-4"><page-number citation-index="1" label="421">*421</page-number>On November 1, 1973, an indictment was returned in the United States District Court for the Northern District of Ohio charging Kotoch, Spaganlo, the five respondents, and 10 other individuals with conspiracy to conduct and conducting a gambling business in violation of <span class="citation no-link">18 U. S. C. §§ 371</span> and 1955. The five respondents filed motions to suppress evidence derived from the wire interception. After an evidentiary hearing on the motions, the District Court suppressed as to respondents Donovan, Robbins, and Buzzacco all evidence derived from the December 26 intercept order on the ground that failure to identify them by name in the application and order of that date violated <span class="citation no-link">18 U. S. C. §§ 2518</span> (l)(b)(iv) and 2518 (4)(a). With respect to Merlo and Lauer, who were not known to the Government until after the December 26 application, the District Court suppressed all evidence derived from both intercept orders on the ground that they had not been served with inventory notice.</p>
<p id="b571-5">The Court of Appeals for the Sixth Circuit affirmed. <span class="citation" data-id="9461598"><a href="/opinion/326404/united-states-v-thomas-w-donovan/" aria-description="Citation for case: United States v. Thomas W. Donovan">513 F. 2d 337</a></span> (1975).<footnotemark>8</footnotemark> On the identification issue, the court held that the wiretap application must identify every person whose conversations relating to the subject criminal activity the Government has probable cause to believe it will intercept. Agreeing with the District Court that at the time of the December 26 application the Government had probable cause to believe that it would overhear Donovan, Robbins, and Buzzacco “committing the offense,” the Court of Appeals affirmed the suppression of evidence derived from <page-number citation-index="1" label="422">*422</page-number>the December 26 order. On the notice question, it held that the Government has an implied statutory duty to inform the issuing judge of the identities of the parties whose conversations were overheard so that he can determine whether discretionary inventory notice should be required.<footnotemark>9</footnotemark> Because the Government had failed to perform this duty with respect to Merlo and Lauer, the Court of Appeals affirmed the District Court’s order suppressing evidence derived from both intercept orders. The court found it unnecessary to determine whether the failure to identify respondents Donovan, Robbins, and Buzzacco in the December 26 application and to name respondents Merlo and Lauer in the proposed inventory notice orders was inadvertent or purposeful, since the mere fact of omission was sufficient to require suppression under <span class="citation no-link">18 U. S. C. §2518</span> (10)(a).<footnotemark>10</footnotemark></p>
<p id="b572-5">We granted certiorari to resolve these issues, which concern the construction of a major federal statute, <span class="citation multiple-matches"><a href="/c/U.%20S./424/907/">424 U. S. 907</a></span>, and now reverse.</p>
<p id="b572-6">II</p>
<p id="b572-7">The United States contends that § 2518 (1) (b) (iv) requires that a wiretap application identify only the principal target of the interception, and that § 2518 (8) (d) does not require the Government to provide the issuing judge with a list of all identifiable persons who were overheard in the <page-number citation-index="1" label="423">*423</page-number>course of an authorized interception. We think neither contention is sound.</p>
<p id="b573-5">A</p>
<p id="b573-6">We turn first to the identification requirements of § 2518 (l)(b)(iv). That provision requires a wiretap application to specify “the identity of the person, if known, committing the offense and whose communications are to be intercepted.” In construing that language, this Court already has ruled that the Government is not required to identify an individual in the application unless it has probable cause to believe (i) that the individual is engaged in the criminal activity under investigation and (ii) that the individual’s conversations will be intercepted over the target telephone. <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S. 143</a></span> (1974). The question at issue here is whether the Government is required to name <em>all </em>such individuals.<footnotemark>11</footnotemark></p>
<p id="b574-4"><page-number citation-index="1" label="424">*424</page-number>The United States argues that the most reasonable interpretation of the plain language of the statute is that the application must identify only the principal target of the investigation, who “will almost always be the individual whose phone is to be monitored.” <footnotemark>12</footnotemark> Brief for United States 18. Under this interpretation, if the Government has reason to believe that an individual will use the target telephone to place or receive calls, and the Government has probable cause to believe that the individual is engaged in the criminal activity under investigation, the individual qualifies as a principal target and must be named in the wiretap application. On the other hand, an individual who uses a different telephone to place calls to or receive calls from the target telephone is not a principal target even if the Government has probable cause to believe that the individual is engaged in the criminal activity under investigation. In other words, whether one is a principal target of the investigation depends on whether one operates the target telephone to place or receive calls.<footnotemark>13</footnotemark></p>
<p id="b574-5">Whatever the merits of such a statutory scheme, we find little support for it in the language and structure of Title III or in the legislative history. The statutory language itself refers only to “the person, if known, committing the <page-number citation-index="1" label="425">*425</page-number>offense and whose communications are to be intercepted.” That description is as applicable to a suspect placing calls to the target telephone as it is to a suspect placing calls from that telephone. It is true, as the United States suggests, that when read in the context of the other subdivisions of §2518 (1) (b), an argument can be made that Congress focused in subdivision (iv) on the primary user of the target telephone. But it is also clear from other sections of the statute that Congress expected that wiretap applications would name more than one individual. For example, Title III requires that inventory notice be served upon “the <em>persons </em>named in the order or the application.” <span class="citation no-link">18 U. S. C. §2518</span> (8)(d) (emphasis added). And §2518 (1) (e) requires that an intercept application disclose all previous intercept applications “involving <em>any of the same persons . </em>. . specified in the application” (emphasis added). It may well be that Congress anticipated that a given application would cover more than one telephone or that several suspects would use one telephone, and that an application for those reasons alone would require identification of more than one individual. But nothing on the face of the statute suggests that Congress intended to remove from the identification requirement those suspects whose intercepted communications originated on a telephone other than that listed in the wiretap application.<footnotemark>14</footnotemark></p>
<p id="b576-4"><page-number citation-index="1" label="426">*426</page-number>Nor can we find support in the legislative history for the “principal target” interpretation. Title III originated as a combination of S. 675, the Federal Wire Interception Act, which was introduced by Senator McClellan several months prior to this Court’s decision in <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967), and S. 2050, the Electronic Surveillance Control Act of 1967, introduced by Senator Hruska a few days after the <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>decision. S. Rep. No. 1097, 90th Cong., 2d Sess., 66 (1968). Both bills required that wiretap applications include a full and complete statement of the facts and circumstances relied upon by the applicant and specification of the nature and location of the communication facilities involved. Although neither bill contained an express identification requirement such as that at issue-here, both bills required the application to include a “full and complete statement of the facts concerning all previous applications . . . <em>involving any person named in the application </em>as committing, having committed, or being about to commit an offense.” Hearings Before the Subcommittee on Criminal Laws and Procedures of the Senate Committee on the Judiciary on Controlling'Crime Through More Effective Law Enforcement, 90th Cong.'; 1st Sess., 77, §8 (a)(3), and 1006, §2518 (4)(a) (1967) (emphasis added). Thus, even at this early stage, it was recognized that an application could identify several individuals, and there is no indication that the identification would be limited to principal targets.</p>
<p id="b576-5">S. 917 combined the major provisions of S. 675 and S. 2050 and eventually was enacted. While it was pending before the Senate Judiciary Committee, this Court decided <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). S. 917 was then redrafted to conform to <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>as well as <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span>, </em>and the identification provision was added at that time. The Senate Report states that the requirements set forth in the vari<page-number citation-index="1" label="427">*427</page-number>ous subdivisions of § 2518 (l)(b), including the identification requirement at issue here, were intended to “reflect . . . the constitutional command of particularization.” S. Rep. No. 1097, <em>supra, </em>at 101, citing <em>Berger </em>v. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#58" aria-description="Citation for case: Berger v. New York"><em>New York, supra, </em>at 58-60</a></span>, and <em>Katz </em>v. <em>United States, supra, </em>at 354-356. The United States now contends that although it may be that Congress read <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>to require, as a constitutional matter, that the subject of the surveillance be named if known, Congress would hardly have read those cases as requiring the naming of all ^parties likely to be overheard.<footnotemark>15</footnotemark> Brief for United States 25-26. But to the extent that Congress thought it was meeting the constitutional commands of particularization established in <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>Congress may have read those cases as mandating a broad identification requirement. The statute that we confronted in <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>required identification of “the person or persons” whose communications were to be overheard. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#59" aria-description="Citation for case: Berger v. New York">388 U. S., at 59</a></span>. And we expressly noted that that provision “[did] no more than identify the person whose constitutionally protected area is to be invaded . . . .” <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Ibid.</a></span> </em>Given the statute at issue in <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and our comment upon it, Congress may have concluded that the Constitution required the naming, in a wiretap application, of all suspects rather than just the primary user.<footnotemark>16</footnotemark></p>
<p id="b578-4"><page-number citation-index="1" label="428">*428</page-number>In any event, for our present purposes it is unnecessary to speculate as to exactly how Congress interpreted <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>with respect to the identification issue. It is sufficient to note that in response to those decisions Congress included an identification requirement which on its face draws no distinction based on the telephone one uses, and the United States points to no evidence in the legislative history that supports such a distinction. Indeed, the legislative materials apparently contain no use of the term “principal target” or any discussion of a different treatment based on the telephone from which a suspect speaks.<footnotemark>17</footnotemark> We therefore conclude that a wiretap application must name an individual if the Government has probable cause to believe that the individual is engaged in the criminal activity under investigation and expects to intercept the individual’s conversations over the target telephone.</p>
<p id="b578-5">B</p>
<p id="b578-6">The other statutory provision at issue in this case is <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d), which provides that the judge shall cause to be served on the persons named in the order or application an inventory, which must give notice of the entry of the order or application, state the disposition of <page-number citation-index="1" label="429">*429</page-number>the application, and indicate whether communications were intercepted.<footnotemark>18</footnotemark> Although the statute mandates inventory notice only for persons named in the application or the order, the statute also provides that the judge may order similar notice to other parties to intercepted communications if he concludes that such action is in the interest of justice.<footnotemark>19</footnotemark> Observing that this notice provision does not expressly require law enforcement authorities routinely to supply the judge with specific information upon which to exercise his discretion, the .United States contends that it would be inappropriate to read such a requirement into the statute since the judge has the option of asking the law enforcement authorities for whatever information he requires.</p>
<p id="b579-5">Our reading of the legislative history of the discretionary notice provision in light of the purposes of Title III leads us to reject the Government’s interpretation.. As reported from the Judiciary Committee, § 2518 (8) (d) contained only a provision mandating notice to the persons named in the application or the order; the discretionary notice provision was added by amendment on the floor of the Senate. In introducing that amendment, Senator Hart explained its purpose:</p>
<blockquote id="b579-6">“The amendment would give the judge who issued the order discretion to require notice to be served on other parties to intercepted communications, even though such <page-number citation-index="1" label="430">*430</page-number>parties are not specifically named in the court order. The Berger and Katz decisions established that notice of surveillance is a constitutional requirement of any surveillance statute. It may be that the required notice must be served on all parties to intercepted communications. Since legitimate interests of privacy may make such notice to all parties undesirable, the amendment leaves the final determination to the judge.” 114 Cong. Rec. 14485-14486 (1968).<footnotemark>20</footnotemark></blockquote>
<p id="b580-5">In deciding whether legitimate privacy interests justify withholding inventory notice from parties to intercepted conversations, a judge is likely to require information and assistance beyond that contained in the application papers and the recordings of intercepted conversations made available by law enforcement authorities. No purpose is served by holding that those authorities have no routine duty to supply the judge with relevant information. The Court of Appeals for the Ninth Circuit recently confronted this problem of dual responsibility, and we adopt the balanced construction that court placed on § 2518 (8) (d):</p>
<blockquote id="b580-6">“To discharge this obligation the judicial officer must have, at a minimum, knowledge of the particular categories into which fall all the individuals whose conver<page-number citation-index="1" label="431">*431</page-number>sations have been intercepted. Thus, while precise identification of each party to an intercepted communication is not required, a description of the general class, or classes, which they comprise is essential to enable the judge to determine whether additional information is necessary for a proper evaluation of the interests of the various parties. Furthermore, although the judicial officer has the duty to cause the filing of the inventory [notice], it is abundantly clear that the prosecution has greater access to and familiarity with the intercepted communications. Therefore we feel justified in imposing upon the latter the duty to classify all those whose conversations have been intercepted, and to transmit this information to the judge. Should the judge desire more information regarding these classes in order to exercise his [statutory] § 2518 (8) (d) discretion, . . . the government is [also] required to furnish such information as is available to it.” <em>United States </em>v. <em>Chun, </em><span class="citation" data-id="321775"><a href="/opinion/321775/united-states-v-david-chun/#540" aria-description="Citation for case: United States v. David Chun">503 F. 2d 533, 540</a></span> (1974). (Footnote omitted.)</blockquote>
<p id="b581-5">We agree with the Ninth Circuit that this allocation of responsibility best serves the purposes of Title III.<footnotemark>21</footnotemark></p>
<p id="b581-6">Currently, the policy of the Justice Department is to provide the issuing judge with the name of every person who has been overheard as to whom there is any reasonable possibility of indictment. Brief for United States 39. Because it fails to assure that the necessary range of infor<page-number citation-index="1" label="432">*432</page-number>relation will be before the issuing judge, this policy does not meet the test set out in <em><span class="citation" data-id="321775"><a href="/opinion/321775/united-states-v-david-chun/" aria-description="Citation for case: United States v. David Chun">Chun</a></span>. </em>Moreover, where, as here, the Government chooses to supply the issuing judge with a list of all identifiable persons rather than a description of the classes into which those persons fall, the list must be complete. Applying these principles, we find that the Government did not comply adequately with §2518 (8)(d), since the names of respondents Merlo and Lauer were not included on the purportedly complete list of identifiable persons submitted to the issuing judge.</p>
<p id="b582-5">Ill</p>
<p id="b582-6">We turn now to the question whether the District Court properly suppressed evidence derived from the wiretaps at issue solely because of the failure of the law enforcement authorities to comply fully with the provisions of §§2518 (1) (b)(iv) and 2518 (8) (d). Section 2515 expressly prohibits the use at trial, and at certain other proceedings, of the contents of any intercepted wire communication or any evidence derived therefrom “if the disclosure of that information would be in violation of this chapter.” The circumstances that trigger suppression under § 2515 are in turn enumerated in § 2518 (10) (a) :</p>
<blockquote id="b582-7">“(i) the communication was unlawfully intercepted;</blockquote>
<blockquote id="A4az">“(ii) the order of authorization or approval under which it was intercepted is insufficient on its face; or</blockquote>
<blockquote id="A-c">“(iii) the interception was not made in conformity with the order of authorization or approval.”</blockquote>
<p id="b582-8">There is no basis on the facts of this case to suggest that the authorization orders are facially insufficient, or that the interception was not conducted in conformity with the orders. Thus, only § 2518 (10) (a) (i) is relevant: Were the communications “unlawfully intercepted” given the violations of §§ 2518 (1) (b) (iv) and 2518 (8) (d) ? <footnotemark>22</footnotemark></p>
<p id="b583-4"><page-number citation-index="1" label="433">*433</page-number>Resolution of that question must begin with <em>United States </em>v. <em>Giordano, </em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S. 505</a></span> (1974), and <em>United States </em>v. <em>Chavez, </em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">416 U. S. 562</a></span> (1974). Those cases hold that “[not] every failure to comply fully with any requirement provided in Title III would render the interception of wire or oral communications 'unlawful.5 55 <span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/#574" aria-description="Citation for case: United States v. Chavez"><em>Id., </em>at 574-575</a></span>. To the contrary, suppression is required only for a “failure to satisfy any of those statutory requirements that directly and substan<page-number citation-index="1" label="434">*434</page-number>tially implement the congressional intention to limit the use of intercept procedures to those, situations clearly calling for the employment of this extraordinary investigative device.” <em>United States </em>v. <span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/#527" aria-description="Citation for case: United States v. Giordano"><em>Giordano, supra, </em>at 527</a></span>.</p>
<p id="b584-5"><em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">Giordano</a></span> </em>concerned the provision in Title III requiring that an application for an intercept order be approved by the Attorney General or an Assistant Attorney General specially designated by the Attorney General. Concluding that Congress intended to condition the use of wiretap procedures on the judgment of senior officials in the Department of Justice, the Court required suppression for failure to comply with the approval provision. <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span> </em>concerned the statutory requirement that the application for an intercept order specify the identity of the official authorizing the application. The problem in <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span> </em>was one of <em>misidentification; </em>although the application had in fact been authorized by the Attorney General, the application erroneously identified an Assistant Attorney General as the official authorizing the application. The Court concluded that mere misidentification of the official authorizing the application did not make the application unlawful within the meaning of § 2518 (10) (a) (i) since that identification requirement did not play a “substantive role” in the regulatory system. 416 U. S., at 578.</p>
<p id="b584-6">In the instant case, the Court of Appeals concluded that both the identification requirement of § 2518 (l)(b)(iv) and the notice requirement of § 2518 (8) (d) played a “central role” in the statutory framework, and for that reason affirmed the District Court's order suppressing relevant evidence. Although both statutory requirements are undoubtedly important, we do not think that the failure to comply fully with those provisions renders unlawful an intercept order that in all other respects satisfies the statutory requirements.</p>
<p id="b585-4"><page-number citation-index="1" label="435">*435</page-number>A</p>
<p id="b585-5">.As to § 2518 (l)(b)(iv), the issue is whether the identification in an intercept application of all those likely to be overheard in incriminating conversations plays a “substantive role” with respect to judicial authorization of intercept orders and consequently imposes a limitation on the use of intercept procedures. The statute provides that the issuing judge may approve an intercept application if he determines that normal investigative techniques have failed or are unlikely to succeed and there is probable cause to believe that: (i) an individual is engaged in criminal activity; (ii) particular communications concerning the offense will be .obtained through interception; and (iii) the target facilities are being used in connection with the specified criminal activity. §§ 2518 (3)(a-d). That determination is based on the “full and complete statement” of relevant facts supplied by law enforcement authorities. If, after evaluating the statutorily enumerated factors in light of the information contained in the application, the judge concludes that the wiretap order should issue, the failure to identify additional persons who are likely to be overheard engaging in incriminating conversations could hardly invalidate an otherwise lawful judicial authorization. The intercept order may issue only if the issuing judge determines that the statutory factors are present, and the failure to name additional targets in no way detracts from the sufficiency of those factors.</p>
<p id="b585-6">This case is unlike <em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">Giordano</a></span>, </em>where failure to satisfy the statutory requirement of prior approval by specified Justice Department officials bypassed a congressionally imposed limitation on the use of the intercept procedure. The Court there noted that it was reasonable to believe that requiring prior approval from senior officials in the Justice Department “would inevitably foreclose resort to wiretapping in various situations where investigative personnel would otherwise seek intercept authority from the court <page-number citation-index="1" label="436">*436</page-number>and the court would very likely authorize its use.” 416 U. S., at 528. Here, however, the statutorily imposed preconditions to judicial authorization were satisfied, and the issuing judge was simply unaware that additional persons might be overheard engaging in incriminating conversations. In no meaningful sense can it be said that the presence of that information as to additional targets would have precluded judicial authorization of the intercept <footnotemark>23</footnotemark> Rather, this case resembles <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span>, </em>where we held that a wiretap was not unlawful simply because the issuing judge was incorrectly informed as to which designated official had authorized the application. The <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span> </em>intercept was lawful because the Justice Department had performed its task of prior approval, and the instant intercept is lawful because the application provided sufficient information to enable the issuing judge to determine that the statutory preconditions were satisfied.<footnotemark>24</footnotemark></p>
<p id="b587-4"><page-number citation-index="1" label="437">*437</page-number>Finally, we note that nothing in the legislative history suggests that Congress intended this broad identification requirement to play “a central, or even functional, role in guarding against unwarranted use of wiretapping or electronic surveillance.” <em>United States </em>v. <em>Chavez, </em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/#578" aria-description="Citation for case: United States v. Chavez">416 U. S., at 578</a></span>. Neither S. 675 nor S. 2050, the predecessor bills of S. 917, contained an identification provision. See <em>supra, </em>at 426. The only explanation given in the Senate Report for the inclusion of the broad identification provision was that it was intended to reflect what Congress perceived to be the constitutional command of particularization. This explanation was offered with respect to all the information required by § 2518 (l)(b) to be set out in an intercept application. No additional guidance can be. gleaned from the floor debates, since they contain no substantive discussion of the identification provision.<footnotemark>25</footnotemark></p>
<p id="b588-4"><page-number citation-index="1" label="438">*438</page-number>B</p>
<p id="b588-5">We reach the same conclusion with respect to the Government's duty to inform the judge of all identifiable persons whose conversations were intercepted. As noted earlier, the version of Title III that emerged from the Senate Judiciary Committee provided only for mandatory notice to the “persons named in the order or the application.'' The Senate Report detailed the purpose of that provision:</p>
<blockquote id="b588-6">“[T]he intent of the provision is that the principle of postuse notice will be retained. This provision alone should insure the community that the techniques are reasonably employed. Through its operation all authorized interceptions must eventually become known at least to the subject. He can then seek appropriate civil redress, for example, under section 2520 ... if he feels that his privacy has been unlawfully invaded.” S. Rep. No. 1097, 90th Cong., 2d Sess., 105 (1968).</blockquote>
<p id="b588-7">The floor discussion concerning the amendment adding the provision for discretionary notice merely indicates an intent to provide notice to such additional persons as may be constitutionally required.</p>
<p id="b588-8">Nothing in the structure of the Act or this legislative history suggests that incriminating conversations are “unlawfully intercepted” whenever parties to those conversations do not receive discretionary inventory notice as a result of the Government’s failure to inform the District Court of their identities. At the time inventory notice was served on the other identifiable persons, the intercept had been completed and the conversations had been “seized” under a valid intercept order. The fact that discretionary notice reached <page-number citation-index="1" label="439">*439</page-number>39 rather than 41 identifiable persons does not in itself mean that the conversations were unlawfully intercepted.<footnotemark>26</footnotemark></p>
<p id="b589-5">The legislative history indicates that postintercept notice was designed instead to assure the community that the wiretap technique is reasonably employed. But even recognizing that Congress placed considerable emphasis on that aspect of the overall statutory scheme, we do not think that postintercept notice was intended to serve as an independent restraint on resort to the wiretap procedure.</p>
<p id="b589-6">IV</p>
<p id="b589-7">Although the Government was required to identify respondents Donovan, Robbins, and Buzzacco in the December 26 application for an extension of the initial intercept, failure to do so in the circumstances here presented did not warrant suppression under § 2518 (10) (a) (i). Nor was suppression justified with respect to respondents Merlo and Lauer simply because the Government inadvertently omitted their names from the comprehensive list of all identifiable persons whose conversations had been overheard. We hold that this is the correct result under the provisions of Title III, but we re<page-number citation-index="1" label="440">*440</page-number>emphasize the suggestion we made in <em>United States </em>v. <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span>, </em>that “strict adherence by the Government to the provisions of Title III would nonetheless be more in keeping with the responsibilities Congress has imposed upon it when authority to engage in wiretapping or electronic surveillance is sought.” 416 U. S., at 580.</p>
<p id="b590-5">The judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b590-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b566-9"> The wiretap application procedure is set forth at <span class="citation no-link">18 U. S. C. § 2518</span> (1), which provides:</p>
<p id="b566-10">“(1) Each application for an order authorizing or approving the interception of a wire or oral communication shall be made in writing upon oath or affirmation to a judge of competent jurisdiction and shall state <page-number citation-index="1" label="417">*417</page-number>the applicant’s authority to make such application. Each application shall include the following information:</p>
<p id="AWp">“(a) the identity of the investigative or law enforcement officer making the application, and the officer authorizing the application;</p>
<p id="AJ0_">“ (b) a full and complete statement of the facts and circumstances relied upon by the applicant, to justify his belief that an order should be issued, including (i) details as to the particular offense that has been, is being, or is about to be committed, (ii) a particular description of the nature and location of the facilities from which or the place where the communication is to be intercepted, (iii) a particular description of the type of communications sought to be intercepted, (iv) the identity of the person, if known, committing the offense and whose communications are to be intercepted;</p>
<p id="Au9">“(c) a full and complete statement as to whether or not other investigative procedures have been tried and failed or why they reasonably appear to be unlikely to succeed if tried or to be-too dangerous;</p>
<p id="A7Y">“(d) a statement of the period of time for which the interception is required to be maintained. If the nature of the investigation is such that the authorization for interception should not automatically terminate when the described type of communication has been first obtained, a particular description of facts establishing probable cause to believe that additional communications of the same type will occur thereafter;</p>
<p id="AJx">“(e) a full and complete statement of the facts concerning all previous applications known to the individual authorizing and making the application, made to any judge for authorization to intercept, or for approval of interceptions of, wire or oral communications involving any of the same persons, facilities or places specified in the application, and the action taken by the judge on each such application; and</p>
<p id="A3K">“(f) where the application is for the extension of an order, a statement setting forth the results thus far obtained from the interception, or a reasonable explanation of the failure to obtain such results.”</p>
<p id="ABI">The issuing judge is free to require the applicant to furnish additional information. <span class="citation no-link">18 U. S. C. § 2518</span> (2).</p>
</footnote>
<footnote label="2">
<p id="b568-5"> The affidavit set forth extensive information indicating that the named individuals were conducting a gambling operation. This information was derived from physical surveillance by agents of the FBI, an examination of telephone company toll records, and the personal observations of six informants, whose past reliability also was detailed in the affidavit.</p>
</footnote>
<footnote label="3">
<p id="b568-6"> The District Court’s order was issued pursuant to <span class="citation no-link">18 U. S. C. §§ 2518</span> (3), (4), which provide in pertinent part:</p>
<p id="b568-7">“(3) Upon such application the judge may enter an ex parte order, as requested or as modified, authorizing or approving interception of wire or oral communications within the territorial jurisdiction of the court in which the judge is sitting, if the judge determines on the basis of the facts submitted by the applicant that—</p>
<p id="b568-8">“(a) there is probable cause for belief that an individual is committing, has committed, or is about to commit a particular offense enumerated in section 2516 of this chapter;</p>
<p id="b568-9">"(b) there is probable cause for belief that particular communications concerning that offense will be obtained through such interception;</p>
<p id="b568-10">"(c) normal investigative procedures have been tried and have failed or reasonably appear to be unlikely to succeed if tried or to be too dangerous;</p>
<p id="b568-11">“(d) there is probable cause for belief that the facilities from which, or the place where, the wire or oral communications are to be intercepted are being used, or are about to be used, in connection with the commission of such offense, or are leased to, listed in the name of, or commonly used by such person.</p>
<p id="b569-5"><page-number citation-index="1" label="419">*419</page-number>“(4) Each order authorizing or approving the interception of any wire or oral communication shall specify—</p>
<p id="Apq">“(a) the identity of the person, if known, whose communications are to be intercepted;</p>
<p id="A1k">“(b) the nature and location of the communications facilities as to which, or the place where, authority to intercept is granted;</p>
<p id="AWM">“(c) a particular description of the type of communication sought to be intercepted, and a statement of the particular offense to which it relates;</p>
<p id="AH2">“(d) the identity of the agency authorized to intercept the communications, and of the person authorizing the application; and</p>
<p id="Azs">“(e) the period of time during which such interception is authorized, including a statement as to whether or not the interception shall automatically terminate when the described communication has been first obtained.”</p>
</footnote>
<footnote label="4">
<p id="b569-10"> In addition to the December 26 application requesting an extension of the initial intercept order, the Government also filed on that date a separate application seeking authorization to monitor a third telephone discovered at the same North Olmstead address. Both applications were accompanied by another affidavit setting forth the results of the initial monitoring, the manner in which the third telephone was discovered, the facts, indicating that the newly discovered telephone was being used, to conduct a gambling business, and reasons why continued interception was necessary. A copy of the affidavit filed on November 28 was also attached to the December 26 applications. For the sake of clarity, the two applications filed on December 26 will be treated as a single application.</p>
</footnote>
<footnote label="5">
<p id="b569-11"> The United States conceded in the Court of Appeals that respondents Donovan and Robbins were “known” within the meaning of the statute at the time of the December 26 application, but challenged as <page-number citation-index="1" label="420">*420</page-number>clearly erroneous the District Court’s finding that respondent Buzzacco was “known” at that time. The Court of Appeals upheld the District Court’s finding, and the United States has not sought review of that disposition. Thus, for our purposes, all three respondents were “known” on December 26.</p>
</footnote>
<footnote label="6">
<p id="b570-11"> An inventory notice <em>must </em>be served within a designated period of time upon “the persons named in the order or the application.” <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d). The inventory must give notice of the entry of the intercept order or application, state the disposition of the application, and indicate whether communications were or were not intercepted. <em><span class="citation no-link">Ibid.</span> </em>Upon the filing of a motion, the judge has discretion to make available the intercepted communications, the applications, and the orders. <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b570-12">Title III also authorizes the District Court to cause an inventory notice to be served on “other parties to intercepted communications” if the judge determines that such notice is in the interest of justice. <em><span class="citation no-link">Ibid.</span> </em>Those other parties may also be given access to the intercepted communications, the applications, and the orders. <em><span class="citation no-link">Ibid.</span></em></p>
</footnote>
<footnote label="7">
<p id="b570-13"> Although respondents Merlo and Lauer were not served with inventory notice pursuant to §2518 (8) (d), the intercept orders, applications, <page-number citation-index="1" label="421">*421</page-number>and related papers were made available to all the defendants, including Merlo and Lauer, on November 26, 1973. Thus, the introduction into evidence at trial of the contents of the intercepted conversations and evidence derived therefrom would not be prohibited by <span class="citation no-link">18 U. S. C. §2518</span> (9).</p>
</footnote>
<footnote label="8">
<p id="b571-11"> The Government filed its appeal from the District Court’s order suppressing evidence under <span class="citation no-link">18 U. S. C. § 3731</span>, and there has been no trial on the charges with respect to the respondents.</p>
</footnote>
<footnote label="9">
<p id="b572-8"> See n. 6, <em>supra.</em></p>
</footnote>
<footnote label="10">
<p id="b572-9"><em> </em>Title <span class="citation no-link">18 U. S. C. § 2518</span> (10) (a) provides in pertinent part:</p>
<p id="b572-10">“(10) (a) Any aggrieved person in any trial, hearing, or proceeding in or before any court, department, officer, agency, regulatory body, or other authority of the United States, a State, or a political subdivision thereof, may move to suppress the. contents of any intercepted wire or oral communication, or evidence derived therefrom, on the grounds that—</p>
<p id="Ahz">“(i) the communication was unlawfully intercepted;</p>
<p id="b572-11">“(ii) the order of authorization or approval under which it was intercepted is insufficient on its face; or</p>
<p id="b572-12">“(iii) the interception was not made in conformity with the order of authorization or approval.”</p>
</footnote>
<footnote label="11">
<p id="b573-7"> Every Court of Appeals that has considered the issue has concluded that an individual whose conversations probably will be intercepted by a wiretap must be identified in the wiretap application if the law enforcement authorities have probable cause to believe the individual is committing the offense for which the wiretap is sought. <em>United States </em>v. <em>Chiarizio, </em><span class="citation" data-id="331054"><a href="/opinion/331054/united-states-v-michael-chiarizio/#292" aria-description="Citation for case: United States v. Michael Chiarizio">525 F. 2d 289, 292</a></span> (CA2 1975); <em>United States </em>v. <em>Bernstein, </em><span class="citation" data-id="324740"><a href="/opinion/324740/united-states-v-calman-bernstein/" aria-description="Citation for case: United States v. Calman Bernstein">509 F. 2d 996</a></span> (CA4 1975), cert. pending, No. 74-1486; <em>United States </em>v. <em>Doolittle, </em><span class="citation multiple-matches"><a href="/c/F.%202d/507/1368/">507 F. 2d 1368</a></span> (CA5), aff’d en banc, <span class="citation multiple-matches"><a href="/c/F.%202d/518/500/">518 F. 2d 500</a></span> (1975), cert. pending, Nos. 75-500, 75-509, 75-513; <em>United States </em>v. <em>Civella, </em><span class="citation" data-id="8898935"><a href="/opinion/8911188/united-states-v-civella/" aria-description="Citation for case: United States v. Civella">533 F. 2d 1395</a></span> (CA8 1976), cert. pending, Nos. 75-1813, 76-169; <em>United States </em>v. <em>Russo, </em><span class="citation" data-id="331942"><a href="/opinion/331942/united-states-v-anthony-r-russo/#1056" aria-description="Citation for case: United States v. Anthony R. Russo">527 F. 2d 1051, 1056</a></span> (CA10 1975), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./426/906/">426 U. S. 906</a></span> (1976). See also <em>United States </em>v. <em>Moore, </em>168 U. S. App. D. C. 227, 235-236, <span class="citation" data-id="326419"><a href="/opinion/326419/united-states-v-aaron-r-moore-jr-united-states-of-america-v-robert/#493" aria-description="Citation for case: United States v. Aaron R. Moore, Jr., United States of...">513 F. 2d 485, 493-494</a></span> (1975) (interpreting D. C. Code § 23-547 (a) (2) (D), which is almost identical to the provision at issue here).</p>
<p id="b573-8">A number of these courts have concluded, and respondents Donovan, Robbins, and Buzzacco argue, that our decision in <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S. 143</a></span> (1974), resolved this identification issue. See <em>United States </em>v. <em><span class="citation" data-id="331054"><a href="/opinion/331054/united-states-v-michael-chiarizio/" aria-description="Citation for case: United States v. Michael Chiarizio">Chiarizio, supra;</a></span> United States </em>v. <em><span class="citation" data-id="326419"><a href="/opinion/326419/united-states-v-aaron-r-moore-jr-united-states-of-america-v-robert/" aria-description="Citation for case: United States v. Aaron R. Moore, Jr., United States of...">Moore, supra.</a></span> </em>Although there is language in <em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">Kahn</a></span> </em>suggesting that wiretap applications must identify all such individuals, the identification question presented here was not before us in <em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">Kahn</a></span>. </em>The question in that case was whether a wiretap application had to identify a known user of the target telephone whose com<page-number citation-index="1" label="424">*424</page-number>plicity in the criminal activity under investigation was not known at the time of the application. <em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">Kahn</a></span> </em>is a relevant, though not controlling, precedent.</p>
</footnote>
<footnote label="12">
<p id="b574-7"> The United States does not suggest that regardless of the factual circumstances a wiretap application must identify only a single individual. To the contrary, it concedes that if two or more persons are using the target telephone “equally” to commit the offense, and thus are “equally” targets of the investigation, “all must be named.” Brief for United States 18 n. 13.</p>
</footnote>
<footnote label="13">
<p id="b574-8"> Counsel for the United States explained this position succinctly at oral argument: “The critical distinction ... is [one] between the users of the telephone that is being monitored on the one hand, and all other persons throughout the world who may converse from unmonitored phones on the other hand.” Tr. of Oral Arg. 13.</p>
</footnote>
<footnote label="14">
<p id="b575-5"> Indeed, the contrary conclusion is suggested by the fact that identification of an individual in an application for an intercept order triggers other statutory provisions. First, § 2518 (1) (e) requires an intercept application to disclose all previous applications “involving any of the same persons . . . specified in the application.” To the extent that Congress thought it necessary to provide the issuing judge with such information, there is no indication of congressional intent to require provision of such information only if a suspect operated from one end of a telephone line. Second, § 2518 (8) (d) mandates that an inventory notice be served upon “the persons named in the order or the application.” As with §2518 (1) (e), the congressional purpose would <page-number citation-index="1" label="426">*426</page-number>not be <em>served by </em>limiting that notice on the basis of the telephone from which one speaks.</p>
</footnote>
<footnote label="15">
<p id="b577-5"> At the time of the enactment of Title III, Congress did not have before it the view we expressed on this issue in <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S., at 155</a></span> n. 15. The Fourth Amendment requires specification of “the place to be searched, and the persons or things to be seized.” In the wiretap context, those requirements are satisfied by identification of the telephone line to be tapped and the particular conversations to be seized. It is not a constitutional requirement that all those likely to be overheard engaging in incriminating conversations be named. Specification of this sort “identifies] the person whose constitutionally protected area is to be invaded rather than ‘particularly describing’ the communications, conversations, or discussions to be seized.” <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#59" aria-description="Citation for case: Berger v. New York">388 U. S., at 59</a></span>.</p>
</footnote>
<footnote label="16">
<p id="b577-6"> That Congress may have so understood the constitutional require<page-number citation-index="1" label="428">*428</page-number>ment is also suggested by <em>the </em>portion of <em>the </em>Senate Report dealing with that provision of S. 917 that required the intercept <em>order </em>to “specify the identity, if known, of the individual whose communications are to be intercepted.” The Senate Report merely cites <em>West </em>v. <em>Cabell, </em><span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/" aria-description="Citation for case: West v. Cabell">153 U. S. 78</a></span> (1894), which concerns the need for proper identification of the subject of an arrest warrant. S. Rep. No. 1097, 90th Cong., 2d Sess., 102 (1968). To the extent that Congress may have considered <em><span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/" aria-description="Citation for case: West v. Cabell">West</a></span> </em>to apply to wiretap orders, we have no reason to believe that Congress considered its applicability to extend only to those suspects using the target telephone.</p>
</footnote>
<footnote label="17">
<p id="b578-8"> At least one Senator read the identification requirement in S. 917 to parallel the identification requirement contained in the statute at issue in <em>Berger </em>v. <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">New York</a></span>: </em>“Specificity is required as to the person or persons whose communications will be intercepted.” 114 Cong. Rec. 14763 (1968) (remarles of Sen. Percy).</p>
</footnote>
<footnote label="18">
<p id="b579-7"> The inventory notice must be served within a reasonable time but not later than 90 days after the date the application for an intercept order was filed. On an <em>ex parte </em>showing of good cause, service of the inventory may be postponed.</p>
</footnote>
<footnote label="19">
<p id="b579-8"> In addition to these provisions for mandatory and discretionary inventory notice, the Government is required to supply the issuing judge with recordings of the intercepted conversations, which are to be sealed according to his directions. <span class="citation no-link">18 U. S. C. § 2518</span> (8) (a). These notice and return provisions satisfy constitutional requirements. See <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#355" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 355-356</a></span>, and n. 16 (1967); <em>Berger </em>v. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#60" aria-description="Citation for case: Berger v. New York"><em>New York, supra, </em>at 60</a></span>.</p>
</footnote>
<footnote label="20">
<p id="b580-7"> It is worth noting that shortly before Senator Hart proposed this amendment to S. 917, Senator Long had read to the Senate portions of a report prepared by the Association of the Bar of the City of New York on federal wiretap legislation. That report commented that parties to intercepted conversations other than those named in the application or order probably should be served with inventory notice, but it also recognized that under some circumstances the provision of such notice could be harmful and gave the following example:</p>
<p id="b580-8"><em>“A, </em>a businessman, talks with his customers, and the latter are served with papers showing that A is being bugged .... [T]he damage to confidence in A and to A's reputation in general may damage A unjustly. In this case it would seem that the customers should not be served with the inventory..” 114 Cong. Rec. 14476 (1968).</p>
</footnote>
<footnote label="21">
<p id="b581-7"> At oral argument, counsel for the United States recognized the merit of the approach specified in <em>United States </em>v. <em><span class="citation" data-id="321775"><a href="/opinion/321775/united-states-v-david-chun/" aria-description="Citation for case: United States v. David Chun">Chun</a></span>:</em></p>
<p id="b581-8">“Perhaps the approach of the Court of Appeals for the Ninth Circuit, which suggested that rather than submitting specific names we should submit categories of persons who had been overheard, is a better policy, would be more helpful to the district court in exercising its discretion, and we would have no objection to following any reasonable policy that the district courts determine would be useful to them in this area.” Tr. of Oral Arg. 6-7.</p>
</footnote>
<footnote label="22">
<p id="b582-9"> The availability of the suppression remedy for these statutory, <page-number citation-index="1" label="433">*433</page-number>as opposed to constitutional, violations, see nn. 15 and 19, <em>supra, </em>turns on the provisions of Title III rather than the judicially fashioned exclusionary rule aimed at deterring violations of Fourth Amendment rights. <em>United States v. Giordano, </em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/#524" aria-description="Citation for case: United States v. Giordano">416 U. S. 505, 524</a></span> (1974).</p>
<p id="b583-6">The concurring opinion of The Cheep Justice contends that respondents Donovan, Robbins, and Buzzacco lack standing even to seek suppression. <em>Post, </em>at 440-441. This contention rests on the ground that Congress rejected an amendment proposed by Senators Long and Hart that would have added a fourth ground justifying suppression — namely, that the person against whom the Government sought to introduce the evidence was not named in the court order. Since these three respondents would have been entitled to suppression under the rejected amendment, the concurring opinion concludes they .cannot seek suppr&amp;sion here.</p>
<p id="b583-7">This view fails to recognize that § 2518 (10) (a) establishing the suppression remedy provides <em>alternative </em>grounds on which one can seek suppression of evidence derived from a wiretap. Thus, the mere fact that Congress chose not to add a fourth alternative could not mean that it intended to prevent persons who would have been covered by that alternative from seeking suppression on one of the other grounds. As the Justice Department commented, in the same statement cited in the concurring opinion: “The [Long and Hart] amendment is designed to limit the scope of electronic surveillance, but it accomplishes this purpose in an artificial manner. <em>So long as a court order is validly obtained, </em>evidence obtained under the order should be admissible against any person not merely against the person named in the order.” 114 Cong. Rec. 14718 (1968) (emphasis added). Here, respondents Donovan, Robbins, and Buzzacco challenge the validity of the court order, and nothing in either Congress’ rejection of the proposed amendment or the Justice Department’s comment thereon suggests that § 2518 (10) (a) (i) is unavailable to persons who might have had a remedy under a provision not enacted by Congress.</p>
</footnote>
<footnote label="23">
<p id="b586-5"> There is no suggestion in this case that the Government agents knowingly failed to identify respondents Donovan, Robbins, and Buzzacco for the purpose of keeping relevant information from the District Court that might have prompted the court to conclude that probable cause was lacking. If such a showing had been made, we would have a different case. Nor is there any suggestion that as a result of the failure to name these three respondents they were denied the mandatory inventory notice supplied to persons named in the application. <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d). Respondents Donovan, Robbins, and Buzzacco were <em>among the </em>37 persons served with the initial inventory.</p>
</footnote>
<footnote label="24">
<p id="b586-6"><em> </em>No one suggests that the failure to identify in a wiretap application individuals who are “unknown” within the meaning of the statute, see <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S. 143</a></span> (1974), requires suppression of intercepted conversations to which those individuals were parties. Though recognizing that the failure to identify such an “unknown” individual does not make unlawful an otherwise valid intercept order, respondents Donovan, Robbins, and Buzzacco suggest that the opposite is true with respect to the failure to identify in a wiretap application individuals who are “known” within the meaning of the statute. Counsel for these respondents suggested at oral argument that this difference in result is justified by analogy to warrantless searches or arrests. Tr. of Oral Arg. 40. Although law enforcement officials can often take action without a warrant when they have <page-number citation-index="1" label="437">*437</page-number>been unable to foresee the circumstances that eventually confronted them, they still must obtain a search or arrest warrant when their prior knowledge is sufficient to establish probable cause, and it is suggested that the same principle applies here. The major flaw' in that reasoning is that this case does not concern warrantless action. Here, the omission on the part of law enforcement authorities was not a failure to seek prior judicial authorization, but a failure to identify every individual who could be expected to be overheard engaging in incriminating conversations. That the complete absence of prior judicial authorization would make an intercept unlawful has no bearing on the lawfulness of an intercept order that fails to identify every target.</p>
</footnote>
<footnote label="25">
<p id="b587-6"> Even if we assume that Congress thought that a broad identification requirement was constitutionally mandated, it does not follow that Congress imposed <em>statutory </em>suppression under §§ 2515 and 2518 (10) (a) (i) as a sanction for noncompliance. In limiting use of the intercept procedure to “the most precise and discriminate circumstances,” S. Rep. No. 1097, 90th Cong., 2d Sess., 102 (1968), Congress required law enforcement authorities to convince a district court that probable cause existed to believe that a specific person was committing a specific offense using a specific telephone. This requirement was satisfied here when the application set forth sufficient information to indicate that the primary targets were conducting a gambling business over four particular telephones. Nothing <page-number citation-index="1" label="438">*438</page-number>in the legislative history indicates that Congress intended to declare an otherwise constitutional intercept order “unlawful” under § 2518 (10) (a) (i) — resulting in suppression under § 2515 — for failure to name additional targets.</p>
</footnote>
<footnote label="26">
<p id="b589-8"> Counsel for respondents Merlo and Lauer conceded at oral argument that the failure to name those respondents in the proposed inventory order was not intentional, Tr. of Oral Arg. 32, and we axe therefore not called upon to decide whether suppression would be an available remedy if the Government knowingly sought to prevent the District Court from serving inventory notice on particular parties. Nor does this case present an opportunity to comment upon the suggestion, recognized by the United States, Brief 49 n. 40, that suppression might be required if the agents knew before the interception that no inventory would be served.</p>
<p id="b589-9">Moreover, respondents Merlo and Lauer were not prejudiced by their failure to receive postintercept notice under either of the District Court's inventory orders. As noted earlier, the Government made available to all defendants the intercept orders, applications, and related papers. See n. 7, <em>supra. </em>And in response to pretrial discovery motions, the Government produced transcripts of the intercepted conversations.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Dunn.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Dunn"
type: case
citation: "480 U.S. 294 (1987)"
parallel_cite: "107 S. Ct. 1134; 94 L. Ed. 2d 326"
neutral_cite: 1987 U.S. LEXIS 1057
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-04-20
docket: 85-998
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-03-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Dunn
  varies_by_point: false
  scope_note: "Good law; the four-factor Dunn test remains the governing framework for determining the extent of a home's curtilage (applied in Jardines and Collins v. Virginia)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111833/united-states-v-dunn/"
  cluster_id: 111833
  opinion_id: 9430862
  identity_checked: true
homes:
  - page: "[[Curtilage]]"
    role: "Key — Anchor"
  - page: "[[Open Fields]]"
    role: "Key"
related: ["[[Oliver v. United States]]", "[[California v. Ciraolo]]", "[[Hester v. United States]]", "[[Florida v. Jardines]]", "[[Collins v. Virginia]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "curtilage", "open-fields", "home"]
holding: "Curtilage is determined by four factors — proximity to the home, whether the area is within an enclosure surrounding the home, the nature of its use, and steps taken to shield it from observation — all bearing on whether the area is so intimately tied to the home as to fall under the home's Fourth Amendment umbrella."
lake:
  record_id: United States v. Dunn
  status: verified
  projected_at: 2026-07-06
---

# United States v. Dunn

*480 U.S. 294 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal agents, investigating a drug-manufacturing operation, crossed perimeter fences onto Dunn's ranch and approached a barn standing about 50 yards beyond the fence surrounding the ranch house. Without entering the barn, agents stood outside it, smelled chemicals associated with drug manufacture, and shined a flashlight inside to observe a suspected drug lab. That observation supported a warrant; Dunn moved to suppress, arguing the barn was within the home's [[Curtilage|curtilage]] and thus protected.

## Issue
Whether the area near the barn — located approximately 50 yards from the fence surrounding the ranch house — was within the [[Curtilage|curtilage]] of the house for Fourth Amendment purposes, such that the agents' warrantless observation invaded a protected area.

## Rule
[[Curtilage]] is determined by reference to four factors: "curtilage questions should be resolved with particular reference to four factors: the proximity of the area claimed to be curtilage to the home, whether the area is included within an enclosure surrounding the home, the nature of the uses to which the area is put, and the steps taken by the resident to protect the area from observation by people passing by." — 480 U.S. at 301. ^pin-301

The factors are not a rigid formula but tools serving one question: "these factors are useful analytical tools only to the degree that, in any given case, they bear upon the centrally relevant consideration — whether the area in question is so intimately tied to the home itself that it should be placed under the home's 'umbrella' of Fourth Amendment protection." — *Id.* ^pin-301a

## Application
Applying the four factors to Dunn's barn: it sat 50 yards from the fence enclosing the house (not in close proximity); it stood outside that fence, so it was not within the enclosure surrounding the home; the agents had objective indications the barn was used to manufacture drugs rather than for intimate activities of the home; and Dunn had done little to shield the barn's interior from observation by anyone standing in the open fields. Together these showed the barn was not so intimately tied to the home as to fall within its [[Curtilage|curtilage]]. Because the barn lay in the open fields, the agents' observation from outside it was not a Fourth Amendment search.

## Conclusion
The barn and its surrounding area lay outside the [[Curtilage|curtilage]] of the ranch house, so the warrantless observation did not violate the Fourth Amendment; the Fifth Circuit was reversed. *Dunn* supplies the controlling four-factor [[Curtilage|curtilage]] test.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Dunn*'s four-factor test remains the governing [[Curtilage|curtilage]] analysis and is applied in later home-privacy cases, including [[Florida v. Jardines]] (front-porch [[Curtilage|curtilage]]) and [[Collins v. Virginia]] (driveway/[[Curtilage|curtilage]] and the automobile exception).

## Appears on
- [[Curtilage]] — *Key — Anchor*

## Sources
- *United States v. Dunn*, 480 U.S. 294 (1987) — https://www.courtlistener.com/opinion/111833/united-states-v-dunn/ — pinpoints: 301.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "151d855a0097e0b8", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "480 U.S. 294 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 1057", "official_citation_present": true, "parallel_cite": "107 S. Ct. 1134; 94 L. Ed. 2d 326", "title": "United States v. Dunn", "year": "1987"}}
{"assertion_id": "820a6203a48197c5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Curtilage is determined by four factors — proximity to the home, whether the area is within an enclosure surrounding the home, the nature of its use, and steps taken to shield it from observation — all bearing on whether the area is so intimately tied to the home as to fall under the home's Fourth Amendment umbrella.", "title": "United States v. Dunn"}}
{"assertion_id": "a54329f5d445019f", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Key — Anchor", "title": "United States v. Dunn"}}
{"assertion_id": "aaf78c40436223af", "dimension": "support", "kind": "home_role", "locator": {"home": "Open Fields"}, "payload": {"home": "Open Fields", "role": "Key", "title": "United States v. Dunn"}}
{"assertion_id": "049b9ca12db4bd01", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Dunn"}}
{"assertion_id": "d1530332e9ee338a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-03-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Dunn", "field_i_validity": "good_law", "scope_note": "Good law; the four-factor Dunn test remains the governing framework for determining the extent of a home's curtilage (applied in Jardines and Collins v. Virginia).", "title": "United States v. Dunn", "varies_by_point": "false"}}
```

### lake record — United States v. Dunn

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Dunn",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Dunn",
    "case_name_short": "Dunn",
    "case_name_full": "United States v. Dunn",
    "input_case_name": "United States v. Dunn",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-04-20",
    "year": 1987,
    "docket": "85-998",
    "cluster_id": 111833,
    "lead_opinion_id": 9430862,
    "sibling_ids": [
      111833,
      9430862,
      9430863,
      9430864
    ],
    "absolute_url": "/opinion/111833/united-states-v-dunn/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 294",
      "volume": "480",
      "reporter": "U.S.",
      "page": "294",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1134",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 326",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1057",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1057",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 294",
        "volume": "480",
        "reporter": "U.S.",
        "page": "294",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1134",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 326",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1057",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1057",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 294",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 294",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-301",
      "page": null,
      "quote": "--- # United States v. Dunn *480 U.S. 294 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal agents, investigating a drug-manufacturing operation, crossed perimeter fences onto Dunn's ranch and approached a barn standing about 50 yards beyond the fence surrounding the ranch house. Without entering the barn, agents stood outside it, smelled chemicals associated with drug manufacture, and shined a flashlight inside to observe a suspected drug lab. That observation supported a warrant; Dunn moved to suppress, arguing the barn was within the home's curtilage and thus protected. ## Issue Whether the area near the barn \u2014 located approximately 50 yards from the fence surrounding the ranch house \u2014 was within the curtilage of the house for Fourth Amendment purposes, such that the agents' warrantless observation invaded a protected area. ## Rule Curtilage is determined by reference to four factors:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-301a",
      "page": null,
      "quote": "these factors are useful analytical tools only to the degree that, in any given case, they bear upon the centrally relevant consideration \u2014 whether the area in question is so intimately tied to the home itself that it should be placed under the home's 'umbrella' of Fourth Amendment protection.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-03-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Dunn",
    "varies_by_point": false,
    "scope_note": "Good law; the four-factor Dunn test remains the governing framework for determining the extent of a home's curtilage (applied in Jardines and Collins v. Virginia).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Wittey",
          "cluster_id": 9404034,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sorenson",
          "cluster_id": 4806437,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Dobson",
          "cluster_id": 7174628,
          "cite": [
            "102 N.E.3d 1032",
            "92 Mass. App. Ct. 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri, Plaintiff/Respondent v. Timothy A. Pierce",
          "cluster_id": 4254135,
          "cite": [
            "504 S.W.3d 766",
            "2016 Mo. App. LEXIS 864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2792904,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2772730,
          "cite": [
            "367 N.C. 753",
            "767 S.E.2d 312",
            "2015 N.C. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 2736404,
          "cite": [
            "152 So. 3d 619",
            "2014 Fla. App. LEXIS 14965",
            "2014 WL 4723562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "STATE OF MISSOURI, Plaintiff-Respondent v. TENA D. CADY",
          "cluster_id": 2673768,
          "cite": [
            "425 S.W.3d 234",
            "2014 WL 1328278",
            "2014 Mo. App. LEXIS 372"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bond v. United States",
          "cluster_id": 118354,
          "cite": [
            "146 L. Ed. 2d 365",
            "120 S. Ct. 1462",
            "529 U.S. 334",
            "2000 U.S. LEXIS 2520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Pitman",
          "cluster_id": 2234418,
          "cite": [
            "813 N.E.2d 93",
            "211 Ill. 2d 502",
            "286 Ill. Dec. 36",
            "2004 Ill. LEXIS 989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate Robert Smith v. Marasco",
          "cluster_id": 3013435,
          "cite": [
            "318 F.3d 497"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Albert Lee Purcell, Shon Purcell",
          "cluster_id": 771684,
          "cite": [
            "236 F.3d 1274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "ESTATE OF",
          "cluster_id": 780724,
          "cite": [
            "318 F.3d 497",
            "2003 U.S. App. LEXIS 1432"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Coffin v. Stacy Brandau",
          "cluster_id": 3048939,
          "cite": [
            "642 F.3d 999",
            "2011 U.S. App. LEXIS 11353",
            "2011 WL 2162997"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Rogers v. M. L. Pendleton, Officer M. G. Vinyard, Officer",
          "cluster_id": 773125,
          "cite": [
            "249 F.3d 279",
            "2001 U.S. App. LEXIS 8157",
            "2001 WL 473736"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Pace, Anthony Besase, Christ Savides, Donald Smith, John Cialoni, and Robert Wilson",
          "cluster_id": 538544,
          "cite": [
            "898 F.2d 1218",
            "1990 U.S. App. LEXIS 3831"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin C. Reilly",
          "cluster_id": 713016,
          "cite": [
            "76 F.3d 1271",
            "1996 U.S. App. LEXIS 2078",
            "1996 WL 56684"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Elkins Carol Elkins, United States of America v. Carol Elkins James Elkins",
          "cluster_id": 778775,
          "cite": [
            "300 F.3d 638"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1275885,
          "cite": [
            "957 P.2d 681"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mierz",
          "cluster_id": 1255546,
          "cite": [
            "901 P.2d 286",
            "127 Wash. 2d 460"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan v. State",
          "cluster_id": 1666213,
          "cite": [
            "728 So. 2d 1088",
            "1998 WL 800121"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Basher",
          "cluster_id": 183144,
          "cite": [
            "629 F.3d 1161",
            "2011 U.S. App. LEXIS 1064",
            "2011 WL 167045"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 3152697,
          "cite": [
            "303 Kan. 11",
            "363 P.3d 875",
            "2015 Kan. LEXIS 929"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Talkington",
          "cluster_id": 2784485,
          "cite": [
            "301 Kan. 453",
            "345 P.3d 258",
            "2015 Kan. LEXIS 167",
            "2015 WL 968451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bullock",
          "cluster_id": 883585,
          "cite": [
            "901 P.2d 61",
            "272 Mont. 361",
            "52 State Rptr. 717",
            "1995 Mont. LEXIS 163"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perea-Rey",
          "cluster_id": 801335,
          "cite": [
            "680 F.3d 1179",
            "2012 U.S. App. LEXIS 10941",
            "2012 WL 1948973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzM0MTAyNDAwMDAwJnM9NjI3MTYyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111833+OR+9430862+OR+9430863+OR+9430864%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDImcz03NzM4NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111833+OR+9430862+OR+9430863+OR+9430864%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 0,
        "triage_snippet_classified": 40
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864)",
    "indexed_citing_opinions": 779,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111833,
        "count": 660,
        "count_source": "search"
      },
      {
        "opinion_id": 9430862,
        "count": 134,
        "count_source": "search"
      },
      {
        "opinion_id": 9430863,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430864,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1338,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-dunn.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNTc5MTcmcz0xMDMxMDQ5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111833+OR+9430862+OR+9430863+OR+9430864%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111833,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 111667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 232365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 237417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 238889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 263655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 270626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 358699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 388191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 402220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 404175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 421926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 454693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 463250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 464634,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1175600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1200960,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1227951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1246385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1263323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1271682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1287214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1326786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1366121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1391288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1507253,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1518631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1575755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1671337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1688103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 2123323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 2455959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 3839556,
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
    "date_created": "2026-07-05T23:42:59Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:43:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:43:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:49:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:43:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Dunn

```
<opinion type="majority">
<author id="b342-6">Justice White</author>
<p id="ARz">delivered the opinion of the Court.</p>
<p id="b342-7">We granted the Government’s petition for certiorari to decide whether the area near a barn, located approximately 50 yards from a fence surrounding a ranch house, is, for Fourth Amendment purposes, within the curtilage of the house. The Court of Appeals for the Fifth Circuit held that the barn lay within the house’s curtilage, and that the District Court should have suppressed certain evidence obtained as a result of law enforcement officials’ intrusion onto the area immediately surrounding the barn. <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d 1226</a></span> (1986). We conclude that the barn and the area around it lay outside the curtilage of the house, and accordingly reverse the judgment of the Court of Appeals.</p>
<p id="b342-8">I</p>
<p id="b342-9">Respondent Ronald Dale Dunn and a codefendant, Robert Lyle Carpenter, were convicted by a jury of conspiring to manufacture phenylacetone and amphetamine, and to possess amphetamine with intent to distribute, in violation of <span class="citation no-link">21 U. S. C. § 846</span>. Respondent was also convicted of manufacturing these two controlled substances and possessing amphetamine with intent to distribute. The events giving rise to respondent’s apprehension and conviction began in 1980 when agents from the Drug Enforcement Administration (DEA) discovered that Carpenter had purchased large quantities of chemicals and equipment used in the manufacture of amphetamine and phenylacetone. DEA agents obtained warrants from a Texas state judge authorizing installation of miniature electronic transmitter tracking devices, or “beepers,” in an electric hot plate stirrer, a drum of acetic anhy-dride, and a container holding phenylacetic acid, a precursor to phenylacetone. All of these items had been ordered by <page-number citation-index="1" label="297">*297</page-number>Carpenter. On September 3, 1980, Carpenter took possession of the electric hot plate stirrer, but the agents lost the signal from the “beeper” a few days later. The agents were able to track the “beeper” in the container of chemicals, however, from October 27, 1980, until November 5, 1980, on which date Carpenter’s pickup truck, which was carrying the container, arrived at respondent’s ranch. Aerial photographs of the ranch property showed Carpenter’s truck backed up to a barn behind the ranch house. The agents also began receiving transmission signals from the “beeper” in the hot plate stirrer that they had lost in early September and determined that the stirrer was on respondent’s ranch property.</p>
<p id="b343-5">Respondent’s ranch comprised approximately 198 acres and was completely encircled by a perimeter fence. The property also contained several interior fences, constructed mainly of posts and multiple strands of barbed wire. The ranch residence was situated 14 mile from a public road. A fence encircled the residence and a nearby small greenhouse. Two barns were located approximately 50 yards from this fence. The front of the larger of the two barns was enclosed by a wooden fence and had an open overhang. Locked, waist-high gates barred entry into the barn proper, and netting material stretched from the ceiling to the top of the wooden gates.</p>
<p id="b343-6">On the evening of November 5, 1980, law enforcement officials made a warrantless entry onto respondent’s ranch property. A DEA agent accompanied by an officer from the Houston Police Department crossed over the perimeter fence and one interior fence. Standing approximately midway between the residence and the barns, the DEA agent smelled what he believed to be phenylacetic acid, the odor coming from the direction of the barns. The officers approached the smaller of the barns — crossing over a barbed wire fence— and, looking into the bam, observed only empty boxes. The officers then proceeded to the larger barn, crossing another <page-number citation-index="1" label="298">*298</page-number>barbed wire fence as well as a wooden fence that enclosed the front portion of the barn. The officers walked under the barn’s overhang to the locked wooden gates and, shining a flashlight through the netting on top of the gates, peered into the barn. They observed what the DEA agent thought to be a phenylacetone laboratory. The officers did not enter the barn.<footnotemark>1</footnotemark> At this point the officers departed from respondent’s property, but entered it twice more on November 6 to confirm the presence of the phenylacetone laboratory.</p>
<p id="b344-5">On November 6, 1980, at 8:30 p.m., a Federal Magistrate issued a warrant authorizing a search of respondent’s ranch. DEA agents and state law enforcement officials executed the warrant on November 8, 1980.<footnotemark>2</footnotemark> The officers arrested re<page-number citation-index="1" label="299">*299</page-number>spondent and seized chemicals and equipment, as well as bags of amphetamines they discovered in a closet in the ranch house.</p>
<p id="b345-5">The District Court denied respondent’s motion to suppress all evidence seized pursuant to the warrant and respondent and Carpenter were convicted. In a decision rendered in 1982, the Court of Appeals reversed respondent’s conviction. <em>United States </em>v. <em>Dunn, </em><span class="citation" data-id="402220"><a href="/opinion/402220/united-states-v-ronald-dale-dunn-and-robert-lyle-carpenter/" aria-description="Citation for case: United States v. Ronald Dale Dunn and Robert Lyle Carpenter">674 F. 2d 1093</a></span>. The court concluded that the search warrant had been issued based on information obtained during the officers’ unlawful warrantless entry onto respondent’s ranch property and, therefore, all evidence seized pursuant to the warrant should have been suppressed. Underpinning this conclusion was the court’s reasoning that “the barn in question was within the curtilage of the residence and was within the protective ambit of the fourth amendment.” <span class="citation" data-id="402220"><a href="/opinion/402220/united-states-v-ronald-dale-dunn-and-robert-lyle-carpenter/#1100" aria-description="Citation for case: United States v. Ronald Dale Dunn and Robert Lyle Carpenter"><em>Id., </em>at 1100</a></span>. We granted the Government’s petition for certiorari, vacated the judgment of the Court of Appeals, and remanded the case for further consideration in fight of <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984). <span class="citation" data-id="9041426"><a href="/opinion/9048025/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">467 U. S. 1201</a></span> (1984). On remand, the Court of Appeals reaffirmed its judgment that the evidence seized pursuant to the warrant should have been suppressed, but altered the legal basis supporting this conclusion: the large barn was not within the curtilage of the house, but by standing outside the barn and peering into the structure, the officers nonetheless violated respondent’s “reasonable expectation of privacy in his barn and its contents.” <span class="citation" data-id="454693"><a href="/opinion/454693/united-states-v-ronald-dale-dunn/#886" aria-description="Citation for case: United States v. Ronald Dale Dunn">766 F. 2d 880, 886</a></span> (1985). The Government again filed a petition for certiorari. On January 17, 1986, before this Court acted on the petition, the Court of Appeals recalled and vacated its judgment issued on remand, stating that it would enter a new judgment in due course. <span class="citation multiple-matches"><a href="/c/F.%202d/781/52/">781 F. 2d 52</a></span>. On February 4, 1986, the Court of Appeals reinstated the original opinion rendered in 1982, asserting that “[u]pon studied reflection, we now conclude and hold that the barn was inside the protected curtilage.” <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/#1227" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d, at 1227</a></span>. The Government thereupon submitted a supplement to its petition for certiorari, revising the question pre<page-number citation-index="1" label="300">*300</page-number>sented to whether the barn lay within the curtilage of the house. We granted the petition, <span class="citation multiple-matches"><a href="/c/U.%20S./477/903/">477 U. S. 903</a></span>, and now reverse.</p>
<p id="b346-5">II</p>
<p id="b346-6">The curtilage concept originated at common law to extend to the area immediately surrounding a dwelling house the same protection under the law of burglary as was afforded the house itself. The concept plays a part, however, in interpreting the reach of the Fourth Amendment. <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924), held that the Fourth Amendment’s protection accorded “persons, houses, papers, and effects” did not extend to the open fields, the Court observing that the distinction between a person’s house and open fields “is as old as the common law. 4 Bl. Comm. 223, 225, 226.”<footnotemark>3</footnotemark></p>
<p id="b346-7">We reaffirmed the holding of <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span> </em>in <em>Oliver </em>v. <em>United States, supra. </em>There, we recognized that the Fourth Amendment protects the curtilage of a house and that the extent of the curtilage is determined by factors that bear upon whether an individual reasonably may expect that the area in question should be treated as the home itself. <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States">466 U. S., at 180</a></span>. We identified the central component of this inquiry as whether the area harbors the “intimate activity associated with the ‘sanctity of a man’s home and the privacies of life.’” <em>Ibid, </em>(quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886)).</p>
<p id="b347-3"><page-number citation-index="1" label="301">*301</page-number>Drawing upon the Court’s own cases and the cumulative experience of the lower courts that have grappled with the task of defining the extent of a home’s curtilage, we believe that curtilage questions should be resolved with particular reference to four factors: the proximity of the area claimed to be curtilage to the home, whether the area is included within an enclosure surrounding the home, the nature of the uses to which the area is put, and the steps taken by the resident to protect the area from observation by people passing by. See <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#221" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 221</a></span> (1986) (Powell, J., dissenting) (citing <em>Care </em>v. <em>United States, </em><span class="citation" data-id="238889"><a href="/opinion/238889/orval-care-v-united-states/#25" aria-description="Citation for case: Orval Care v. United States">231 F. 2d 22, 25</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./351/932/">351 U. S. 932</a></span> (1956); <em>United States </em>v. <em>Van Dyke, </em><span class="citation" data-id="388191"><a href="/opinion/388191/united-states-v-larry-g-van-dyke/#993" aria-description="Citation for case: United States v. Larry G. Van Dyke">643 F. 2d 992, 993-994</a></span> (CA4 1981)).<footnotemark>4</footnotemark> We do not suggest that combining these factors produces a finely tuned formula that, when mechanically applied, yields a “correct” answer to all extent-of-curtilage questions. Rather, these factors are useful analytical tools only to the degree that, in any given case, they bear upon the centrally relevant consideration — whether the area in question is so intimately tied to the home itself that it should be placed under the home’s “umbrella” of Fourth Amendment protection. Applying these factors to respondent’s barn and to the area immediately surrounding it, we have little difficulty in concluding that this area lay outside the curtilage of the ranch house.</p>
<p id="b348-4"><page-number citation-index="1" label="302">*302</page-number><em>First. </em>The record discloses that the barn was located 50 yards from the fence surrounding the house and 60 yards from the house itself. <span class="citation" data-id="454693"><a href="/opinion/454693/united-states-v-ronald-dale-dunn/#882" aria-description="Citation for case: United States v. Ronald Dale Dunn">766 F. 2d, at 882-883</a></span>; <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/#1228" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d, at 1228</a></span>. Standing in isolation, this substantial distance supports no inference that the barn should be treated as an adjunct of the house.</p>
<p id="b348-5"><em>Second. </em>It is also significant that respondent’s barn did not lie within the area surrounding the house that was enclosed by a fence. We noted in <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver, supra,</a></span> </em>that “for most homes, the boundaries of the curtilage will be clearly marked; and the conception defining the curtilage — as the area around the home to which the activity of home life extends —is a familiar one easily understood from our daily experience.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States">466 U. S., at 182, n. 12</a></span>. Viewing the physical layout of respondent’s ranch in its entirety, see <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/#1228" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d, at 1228</a></span>, it is plain that the fence surrounding the residence serves to demark a specific area of land immediately adjacent to the house that is readily identifiable as part and parcel of the house. Conversely, the barn — the front portion itself enclosed by a fence — and the area immediately surrounding it, stands out as a distinct portion of respondent’s ranch, quite separate from the residence.</p>
<p id="b348-6"><em>Third. </em>It is especially significant that the law enforcement officials possessed objective data indicating that the barn was not being used for intimate activities of the home. The aerial photographs showed that the truck Carpenter had been driving that contained the container of phenylacetic acid was backed up to the barn, “apparently,” in the words of the Court of Appeals, “for the unloading of its contents.” <span class="citation" data-id="402220"><a href="/opinion/402220/united-states-v-ronald-dale-dunn-and-robert-lyle-carpenter/#1096" aria-description="Citation for case: United States v. Ronald Dale Dunn and Robert Lyle Carpenter">674 F. 2d, at 1096</a></span>. When on respondent’s property, the officers’ suspicion was further directed toward the barn because of “a very strong odor” of phenylacetic acid. App. 15. As the DEA agent approached the barn, he “could hear a motor running, like a pump motor of some sort . . . .” <em>Id., at </em>17. Furthermore, the officers detected an “extremely strong” odor of phenylacetic acid coming from a small crack in the <page-number citation-index="1" label="303">*303</page-number>wall of the barn. <em>Ibid. </em>Finally, as the officers were standing in front of the barn, immediately prior to looking into its interior through the netting material, “the smell was very, very strong . . . [and the officers] could hear the motor running very loudly.” <em>Id., </em>at 18. When considered together, the above facts indicated to the officers that the use to which the barn was being put could not fairly be characterized as so associated with the activities and privacies of domestic life that the officers should have deemed the barn as part of respondent’s home.</p>
<p id="b349-6"><em>Fourth. </em>Respondent did little to protect the barn area from observation by those standing in the open fields. Nothing in the record suggests that the various interior fences on respondent’s property had any function other than that of the typical ranch fence; the fences were designed and constructed to corral livestock, not to prevent persons from observing what lay inside the enclosed areas.</p>
<p id="b349-7">l — l HH 1 — I</p>
<p id="b349-1">Respondent submits an alternative basis for affirming the judgment below, one that was presented to but ultimately not relied upon by the Court of Appeals. Respondent asserts that he possessed an expectation of privacy, independent from his home’s curtilage, in the barn and its contents, because the barn is an essential part of his business. Brief for Respondent 9. Respondent overlooks the significance of <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984).</p>
<p id="b349-2">We may accept, for the sake of argument, respondent’s submission that his barn enjoyed Fourth Amendment protection and could not be entered and its contents seized without a warrant. But it does not follow on the record before us that the officers’ conduct and the ensuing search and seizure violated the Constitution. <em>Oliver </em>reaffirmed the precept, established in <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>, </em>that an open field is neither a “house” nor an “effect,” and, therefore, “the government’s intrusion upon the open fields is not one of those ‘unreasonable searches’ <page-number citation-index="1" label="304">*304</page-number>proscribed by the text of the Fourth Amendment.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#177" aria-description="Citation for case: Oliver v. United States">466 U. S., at 177</a></span>. The Court expressly rejected the argument that the erection of fences on an open field — at least of the variety involved in those cases and in the present case — creates a constitutionally protected privacy interest. <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 182-183</a></span>. “[T]he term ‘open fields’ may include any unoccupied or undeveloped area outside of the curtilage. An open field need be neither ‘open’ nor a ‘field’ as those terms are used in common speech.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 180, n. 11</a></span>. It follows that no constitutional violation occurred here when the officers crossed over respondent’s ranch-style perimeter fence, and over several similarly constructed interior fences, prior to stopping at the locked front gate of the barn. As previously mentioned, the officers never entered the barn, nor did they enter any other structure on respondent’s premises. Once at their vantage point, they merely stood, outside the curti-lage of the house and in the open fields upon which the barn was constructed, and peered into the barn’s open front. And, standing as they were in the open fields, the Constitution did not forbid them to observe the phenylacetone laboratory located in respondent’s barn. This conclusion flows naturally from our previous decisions.</p>
<p id="b350-5">Under <em>Oliver </em>and <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>, </em>there is no constitutional difference between police observations conducted while in a public place and while standing in the open fields. Similarly, the fact that the objects observed by the officers lay within an area that we have assumed, but not decided, was protected by the Fourth Amendment does not affect our conclusion. Last Term, in <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986), we held that warrantless naked-eye aerial observation of a home’s curtilage did not violate the Fourth Amendment. We based our holding on the premise that the Fourth Amendment “has never been extended to require law enforcement officers to shield their eyes when passing by a home on public thoroughfares.” <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo"><em>Id., </em>at 213</a></span>. Importantly, we deemed it irrelevant that the police observation at issue <page-number citation-index="1" label="305">*305</page-number>was directed specifically at the identification of marijuana plants growing on an area protected by the Fourth Amendment. <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ibid.</a></span> </em>Finally, the plurality opinion in <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 739-740</a></span> (1983), notes that it is “beyond dispute” that the action of a police officer in shining his flashlight to illuminate the interior of a car, without probable cause to search the car, “trenched upon no right secured . . . by the Fourth Amendment.” The holding in <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span> (1927) is of similar import. Here, the officers’ use of the beam of a flashlight, directed through the essentially open front of respondent’s barn, did not transform their observations into an unreasonable search within the meaning of Fourth Amendment.</p>
<p id="b351-5">The officers lawfully viewed the interior of respondent’s barn, and their observations were properly considered by the Magistrate in issuing a search warrant for respondent’s premises. Accordingly, the judgment of the Court of Appeals is reversed.</p>
<p id="b351-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b344-6"> In denying respondent’s motion to suppress all evidence obtained as a result of the search warrant, the District Court Judge stated that the law enforcement officials, during their incursions onto respondent’s property, “did not invade the premises, that is, the houses or the barns . . . .” Tr. 216. The Court of Appeals did not disturb this finding. At the suppression hearing, the DEA agent described the officers’ approach to the large barn on November 5:</p>
<p id="b344-7">“A. We came back around, we crossed a small wooden type fence here, which put us right underneath a type of a tin overhang and in front of us was a wooden locked gate ....</p>
<p id="b344-8">“Q. How high was that gate?</p>
<p id="b344-9">“A. It probably came up to my waist, estimated.</p>
<p id="b344-10">“Q. Was that gate open or shut?</p>
<p id="b344-11">“A. It was shut and it was locked.</p>
<p id="b344-12">“Q. Was there anything above that gate?</p>
<p id="b344-13">“A. Yes, there was.</p>
<p id="b344-14">“Q. What was that?</p>
<p id="b344-15">“A. A fish netting, kind of a netting, that was hanging from the ceiling down to the gate.</p>
<p id="b344-16">“Q. Did you cross over that gate and go into the barn?</p>
<p id="b344-17">“A. No.</p>
<p id="b344-18">“Q. Did you stand outside the gate?</p>
<p id="b344-19">“A. We stood right at the gate.”</p>
<p id="b344-20">App. 17-18.</p>
</footnote>
<footnote label="2">
<p id="b344-21"> Prior to the actual search of the barn and ranch house, the agents entered the property for further observations.</p>
</footnote>
<footnote label="3">
<p id="b346-8"> In the section of Blaekstone’s Commentaries which the Court cited, Blackstone described the elements of common-law burglary, and elaborated on the element that a breaking occur in a mansion or dwelling house. In defining the terms “mansion or dwelling-house,” Blackstone wrote that “no distant barn, warehouse, or the like are under the same privileges, nor looked upon as a man’s castle of defence . . . .” 4 W. Blackstone, Commentaries *225. Blackstone observed, however, that “if the barn, stable, or warehouse, be parcel of the mansion-house, and within the same common fence, though not under the same roof or contiguous, a burglary may be committed therein; for the capital house protects and privileges all its branches and appurtenances, if within the curtilage or homestall.” <em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">Ibid.</a></span></em></p>
</footnote>
<footnote label="4">
<p id="b347-4"> We decline the Government’s invitation to adopt a “bright-line rule” that “the curtilage should extend no farther than the nearest fence surrounding a fenced house.” Brief for United States 14. Fencing configurations are important factors in defining the curtilage, see <em>infra, </em>at 302, but, as we emphasize above, the primary focus is whether the area in question harbors those intimate activities associated with domestic life and the privacies of the home. Application of the Government’s “first fence rule” might well lead to diminished Fourth Amendment protection in those cases where a structure lying outside a home’s enclosing fence was used for such domestic activities. And, in those cases where a house is situated on a large parcel of property and has no nearby enclosing fence, the Government’s rule would serve no utility; a court would still be required to assess the various factors outlined above to define the extent of the curtilage.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Garner.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Garner"
type: case
citation: "416 F.3d 1208 (2005)"
parallel_cite: ""
neutral_cite: "2005 U.S. App. LEXIS 15369; 2005 WL 1766377"
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 2005
date_decided: 2005-07-27
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2005-07-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Garner
  varies_by_point: false
  scope_note: "Good law; anchor for the persons-in-public caretaking strand. Caniglia v. Strom (2021) confined its no-freestanding-caretaking holding to the home and does not disturb a community-caretaking detention of a person in public."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/166206/united-states-v-garner/"
  cluster_id: 166206
  opinion_id: 166206
  identity_checked: true
homes:
  - page: "[[Community Caretaking]]"
    role: "Key — Anchor"
related: ["[[Cady v. Dombrowski]]", "[[United States v. Rideau]]", "[[Graham v. Barnette]]", "[[Caniglia v. Strom]]", "[[Terry v. Ohio]]"]
aliases: ["United States v. Garner (10th Cir. 2005)", "United States v. Mark James Garner"]
tags: ["case", "fourth-amendment", "community-caretaking", "investigative-detention", "persons-in-public", "tenth-circuit"]
holding: "A community-caretaking detention of a person is valid under a three-part test — (1) specific and articulable facts warranting the intrusion, (2) the government's caretaking interest outweighing the individual's liberty interest, and (3) scope and duration tailored to the caretaking purpose; once that purpose is satisfied, continued detention requires independent reasonable suspicion."
lake:
  record_id: United States v. Garner
  status: verified
  projected_at: 2026-07-09
---

# United States v. Garner

*416 F.3d 1208 (10th Cir. 2005)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Around 5:00 p.m., South Salt Lake City police received a report that a man had been seen in a field near an apartment complex for several hours, unconscious in a half-sitting, half-slumped-over position. Officer Boyd and the municipal fire department responded and found Garner lying in the field. As Officer Boyd approached, Garner walked away but was stopped by a stone wall; Boyd told him to come back and sit so the fire department could examine him. Garner appeared nervous and repeatedly moved his hands in and out of his pockets. After the fire department's examination, the officers continued the encounter, ran a warrant check, and Garner admitted recent drug use and outstanding warrants; he then fled, was tackled, and a search of his pockets revealed a handgun and burglary tools. He was charged as a felon in possession (18 U.S.C. § 922(g)(1)) and moved to suppress.

## Issue
Whether an officer exercising a community-caretaking function may detain a person without reasonable suspicion of a crime, and what standards govern such a caretaking detention of a person.

## Rule
A police officer exercising community-caretaking functions "may ... properly detain a person," subject to a three-part test. **First (articulable need):** "such a community caretaking detention must be based upon 'specific and articulable facts which ... reasonably warrant [an] intrusion' into the individual's liberty." — 416 F.3d at 1213. ^pin-1213

**Second (interest-balancing):** "the government's interest must outweigh the individual's interest in being free from arbitrary governmental interference." — *Id.* ^pin-1213a

**Third (tailoring):** "the detention must last no longer than is necessary to effectuate its purpose, and its scope must be carefully tailored to its underlying justification." — [*Id.*](https://www.courtlistener.com/opinion/166206/united-states-v-garner/#:~:text=the%20detention%20must%20last%20no) ^pin-1213b

Once the caretaking purpose is satisfied, any further detention needs an independent justification: "Once the officer has completed the inquiry necessary to satisfy the purpose of the initial detention, he or she must allow the person to proceed unless the officer has a reasonable suspicion of criminal conduct." — *Id.* ^pin-1213c

## Application
On these facts, Officer Boyd was acting in a community-caretaking role when he directed Garner — reported unconscious in a field for hours — to return so the fire department could examine him; that supplied the articulable facts of need, and the government's interest in protecting a man who "might well have needed medical assistance" outweighed Garner's liberty interest. When the medical examination ended, the detention did not become unlawful: Garner's continuing nervous, evasive behavior and hand movements furnished reasonable suspicion to extend the stop, and the limited questions (name, date of birth) and warrant check were reasonably tailored to the encounter's purpose. The caretaking detention and its continuation were therefore reasonable.

## Conclusion
The detention did not violate the Fourth Amendment; the Tenth Circuit affirmed the denial of Garner's motion to suppress the handgun and burglary tools.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Garner* is the Tenth Circuit anchor for the **persons-in-public** community-caretaking strand, applying [[Cady v. Dombrowski]]'s "community caretaking functions" to the detention of a person and citing [[United States v. Rideau]] (5th Cir.) for extending a caretaking detention based on an apparently impaired person's behavior.
- [[Caniglia v. Strom]] (2021) held there is no *freestanding* community-caretaking exception authorizing a warrantless entry into a **home**; that holding is confined to the home and does **not** disturb *Garner*'s rule for caretaking detentions of persons in public.

## Appears on
- [[Community Caretaking]] — *Key — Anchor*

## Sources
- *United States v. Garner*, 416 F.3d 1208 (10th Cir. 2005) — https://www.courtlistener.com/opinion/166206/united-states-v-garner/ — pinpoints: 1213.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e9391ea62e4a4b56", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "416 F.3d 1208 (2005)", "court": "U.S. Court of Appeals, 10th Circuit", "neutral_cite": "2005 U.S. App. LEXIS 15369; 2005 WL 1766377", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Garner", "year": "2005"}}
{"assertion_id": "38d0039e271d10c8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A community-caretaking detention of a person is valid under a three-part test — (1) specific and articulable facts warranting the intrusion, (2) the government's caretaking interest outweighing the individual's liberty interest, and (3) scope and duration tailored to the caretaking purpose; once that purpose is satisfied, continued detention requires independent reasonable suspicion.", "title": "United States v. Garner"}}
{"assertion_id": "3ae1ee44b5bd44c3", "dimension": "support", "kind": "home_role", "locator": {"home": "Community Caretaking"}, "payload": {"home": "Community Caretaking", "role": "Key — Anchor", "title": "United States v. Garner"}}
{"assertion_id": "0d0ea93f2c708259", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Garner"}}
{"assertion_id": "1ee51bbe93145445", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2005-07-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Garner", "field_i_validity": "good_law", "scope_note": "Good law; anchor for the persons-in-public caretaking strand. Caniglia v. Strom (2021) confined its no-freestanding-caretaking holding to the home and does not disturb a community-caretaking detention of a person in public.", "title": "United States v. Garner", "varies_by_point": "false"}}
```

### lake record — United States v. Garner

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Garner",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Garner",
    "case_name_short": "Garner",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Mark James GARNER, Defendant-Appellant",
    "input_case_name": "United States v. Garner",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2005-07-27",
    "year": 2005,
    "docket": null,
    "cluster_id": 166206,
    "lead_opinion_id": 166206,
    "sibling_ids": [
      166206
    ],
    "absolute_url": "/opinion/166206/united-states-v-garner/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "416 F.3d 1208",
      "volume": "416",
      "reporter": "F.3d",
      "page": "1208",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2005 U.S. App. LEXIS 15369",
        "volume": "2005",
        "reporter": "U.S. App. LEXIS",
        "page": "15369",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 WL 1766377",
        "volume": "2005",
        "reporter": "WL",
        "page": "1766377",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "416 F.3d 1208",
        "volume": "416",
        "reporter": "F.3d",
        "page": "1208",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 U.S. App. LEXIS 15369",
        "volume": "2005",
        "reporter": "U.S. App. LEXIS",
        "page": "15369",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 WL 1766377",
        "volume": "2005",
        "reporter": "WL",
        "page": "1766377",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "416 F.3d 1208",
    "official_selection": {
      "court_class": "coa",
      "selected": "416 F.3d 1208",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1213",
      "page": null,
      "quote": "--- # United States v. Garner *416 F.3d 1208 (10th Cir. 2005)* \u00b7 U.S. Court of Appeals, 10th Circuit \u00b7 **Binding in-circuit \u2014 10th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 5:00 p.m., South Salt Lake City police received a report that a man had been seen in a field near an apartment complex for several hours, unconscious in a half-sitting, half-slumped-over position. Officer Boyd and the municipal fire department responded and found Garner lying in the field. As Officer Boyd approached, Garner walked away but was stopped by a stone wall; Boyd told him to come back and sit so the fire department could examine him. Garner appeared nervous and repeatedly moved his hands in and out of his pockets. After the fire department's examination, the officers continued the encounter, ran a warrant check, and Garner admitted recent drug use and outstanding warrants; he then fled, was tackled, and a search of his pockets revealed a handgun and burglary tools. He was charged as a felon in possession (18 U.S.C. \u00a7 922(g)(1)) and moved to suppress. ## Issue Whether an officer exercising a community-caretaking function may detain a person without reasonable suspicion of a crime, and what standards govern such a caretaking detention of a person. ## Rule A police officer exercising community-caretaking functions",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1213a",
      "page": null,
      "quote": "the government's interest must outweigh the individual's interest in being free from arbitrary governmental interference.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1213b",
      "page": null,
      "quote": "the detention must last no longer than is necessary to effectuate its purpose, and its scope must be carefully tailored to its underlying justification.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 8961,
      "fragment": "#:~:text=the%20detention%20must%20last%20no",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1213c",
      "page": null,
      "quote": "Once the officer has completed the inquiry necessary to satisfy the purpose of the initial detention, he or she must allow the person to proceed unless the officer has a reasonable suspicion of criminal conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2005-07-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Garner",
    "varies_by_point": false,
    "scope_note": "Good law; anchor for the persons-in-public caretaking strand. Caniglia v. Strom (2021) confined its no-freestanding-caretaking holding to the home and does not disturb a community-caretaking detention of a person in public.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Storey v. Garcia",
          "cluster_id": 3062104,
          "cite": [
            "696 F.3d 987",
            "2012 WL 4478784",
            "2012 U.S. App. LEXIS 20471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lundstrom v. Romero",
          "cluster_id": 173471,
          "cite": [
            "616 F.3d 1108",
            "2010 U.S. App. LEXIS 17136",
            "2010 WL 3222048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Novitsky v. City of Aurora",
          "cluster_id": 169434,
          "cite": [
            "491 F.3d 1244",
            "2007 U.S. App. LEXIS 15959",
            "2007 WL 1935142"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Kenneth McCormick",
          "cluster_id": 3202373,
          "cite": [
            "494 S.W.3d 673",
            "2016 WL 2742841",
            "2016 Tenn. LEXIS 318"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Terry Lee Coffman",
          "cluster_id": 4509998,
          "cite": [
            "914 N.W.2d 240"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donahue v. Wihongi",
          "cluster_id": 4707601,
          "cite": [
            "948 F.3d 1177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "STATE of Tennessee v. James David MOATS",
          "cluster_id": 1043895,
          "cite": [
            "403 S.W.3d 170",
            "2013 WL 1181967",
            "2013 Tenn. LEXIS 311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. State",
          "cluster_id": 1886723,
          "cite": [
            "975 A.2d 877",
            "409 Md. 415",
            "2009 Md. LEXIS 277"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Samuels",
          "cluster_id": 169448,
          "cite": [
            "493 F.3d 1187",
            "2007 U.S. App. LEXIS 16194",
            "2007 WL 1969675"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maurice Trotter, A.K.A. Mo Mardell Trotter, A.K.A. Juice, A.K.A. Del",
          "cluster_id": 797493,
          "cite": [
            "483 F.3d 694",
            "2007 WL 1128851"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mitchell",
          "cluster_id": 166672,
          "cite": [
            "429 F.3d 952",
            "2005 U.S. App. LEXIS 25106",
            "2005 WL 3105700"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chavez",
          "cluster_id": 4848966,
          "cite": [
            "985 F.3d 1234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Neugin",
          "cluster_id": 4750564,
          "cite": [
            "958 F.3d 924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ozga v. Elliot",
          "cluster_id": 7317315,
          "cite": [
            "150 F. Supp. 3d 178",
            "2015 U.S. Dist. LEXIS 169812",
            "2015 WL 9286767"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schreiber v. Moe",
          "cluster_id": 2500057,
          "cite": [
            "445 F. Supp. 2d 799",
            "2006 U.S. Dist. LEXIS 55900",
            "2006 WL 2331175"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. State",
          "cluster_id": 1477450,
          "cite": [
            "932 A.2d 739",
            "176 Md. App. 7",
            "2007 Md. App. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gilmore",
          "cluster_id": 2770554,
          "cite": [
            "776 F.3d 765",
            "2015 WL 221619",
            "2015 U.S. App. LEXIS 696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America v. Philip Wetmore",
          "cluster_id": 10697026,
          "cite": [
            "560 F. Supp. 3d 591",
            "2021 DNH 091P"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 4587106,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Duffin Windham v. State",
          "cluster_id": 3109009,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Villagrana-Flores",
          "cluster_id": 168356,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(166206) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 1,
        "triage_snippet_classified": 6
      },
      "lane2_top_cited": {
        "query": "cites:(166206)",
        "reviewed": 22,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 21,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(166206)",
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
    "complete_query": "cites:(166206)",
    "indexed_citing_opinions": 22,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 166206,
        "count": 22,
        "count_source": "search"
      }
    ],
    "citation_count": 40,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-garner.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjE0ODExNDEmcz0yNTAwMDU3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28166206%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 166206,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 118352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 136990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 160815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 162075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 162579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 164194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 165035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 165216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 604813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 661539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 685190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 741171,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T00:00:03Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:01:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:01:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:05:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:01:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Garner

```
                                                                            F I L E D
                                                                      United States Court of Appeals
                                                                              Tenth Circuit
                                     PUBLISH
                                                                             July 27, 2005
                   UNITED STATES COURT OF APPEALS
                                                                        PATRICK FISHER
                                                                                  Clerk
                                TENTH CIRCUIT



    UNITED STATES OF AMERICA,

              Plaintiff-Appellee,


    v.                                                   No. 04-4111


    MARK JAMES GARNER,

              Defendant-Appellant.




         APPEAL FROM THE UNITED STATES DISTRICT COURT
                   FOR THE DISTRICT OF UTAH
                    (D.C. No. 2:03-CR-320-DKW)


Richard P. Mauro, Salt Lake City, Utah, for the Defendant-Appellant.

Paul M. Warner, United States Attorney, District of Utah, and Kevin L. Sundwall,
Assistant United States Attorney, District of Utah, for the Plaintiff-Appellee.


Before HENRY , MCCONNELL, and HARTZ , Circuit Judges.             *




HENRY, Circuit Judge.


*
  After examining the briefs and appellate record, this panel has determined
unanimously that oral argument would not materially assist the determination of
this appeal. See F ED . R. A PP . P. 34(a)(2); 10 TH C IR . R. 34.1(G). The case is
therefore ordered submitted without oral argument.
      After the district court denied his motion to suppress, Mark James Garner

entered a conditional guilty plea to possession of a firearm after conviction of a

felony, a violation of 18 U.S.C. § 922(g)(1). In this appeal, he argues that

because South Salt Lake City police officers lacked reasonable suspicion to detain

him, the district court erred in denying his motion to suppress. We are not

persuaded by Mr. Garner’s arguments and therefore affirm the district court’s

decision.



                                 I. BACKGROUND

      Around 5:00 p.m. on April 11, 2003, the South Salt Lake City Police

Department received information that a man had been seen in a field near an

apartment complex for several hours, unconscious in a half-sitting, half-slumped-

over position. Rec. vol. II, at 5 (Tr. of Oct. 23, 2003 Hr’g). Officer Tyrone

Boyd proceeded to the apartment complex, arriving at approximately the same

time as the municipal fire department. He found Mr. Garner lying in a field on

the north side of the complex.

      As Officer Boyd approached, Mr. Garner began to walk away. Mr. Garner

turned a corner around a building but was stopped by a stone wall. Officer Boyd

told Mr. Garner to come back and sit down so that the fire department personnel

                                         -2-
could examine him. Mr. Garner complied but, according to Officer Boyd, he

appeared nervous, “always looking around [and] saying everything was cool and

[that] he didn’t want any trouble” and moving his hands in and out of his pockets.

Id. at 8.

       After fire department personnel examined Mr. Garner, he began to walk

away. Officer Boyd told him to sit back down because he was not done with him

yet. He then asked Mr. Garner his name and his date of birth, and Mr. Garner

provided the information.

       About this time, Officer Robert Ransdell arrived. Officer Boyd informed

Officer Ransdell that Mr. Garner appeared nervous. Officer Ransdell instructed

Officer Boyd to ask the dispatcher to determine whether Mr. Garner had any

outstanding warrants.

       Officer Ransdell then approached Mr. Garner. Like Officer Boyd, he

noticed that Mr. Garner appeared nervous and was moving his hands in and out of

his pockets. Officer Ransdell asked Mr. Garner to keep his hands in view and

then inquired why Mr. Garner was at the apartment complex and why he was so

nervous. Mr. Garner responded that he did not know why he was there and that

he had passed out. Officer Ransdell then asked whether Mr. Garner had been

taking drugs. Mr. Garner replied that he had “smoked some dope prior that day”

and that he had “some warrants.” Id. at 44.



                                        -3-
      At that point, Officer Boyd informed Officer Ransdell of the results of his

background check: Mr. Garner did have some outstanding warrants. Officer

Ransdell told Mr. Garner, “you’ve got some warrants, no big deal,” id. at 45, but

also indicated that he would be detained until the officers could determine the

substance of those warrants. Officer Ransdell directed Mr. Garner to turn around

and put his hands behind his back.

      At that point, Mr. Garner began to comply but then ran away. The officers,

along with fire department personnel, chased and tackled him. Mr. Garner fought

with the officers, but they managed to place him in handcuffs. A search of Mr.

Garner’s pants pockets revealed a handgun and burglary tools.

      After the government charged Mr. Garner with possession of a firearm after

a felony conviction, a violation of 18 U.S.C. § 922(g)(1), Mr. Garner moved to

suppress the evidence found by the officers. In support of his motion to suppress,

Mr. Garner first argued that Officer Boyd lacked the necessary reasonable

suspicion to support the initial detention. He also argued that, once the fire

department completed its examination, the officers lacked reasonable suspicion to

continue the detention.

      After hearing testimony from Officers Boyd and Ransdell, the district court

rejected both arguments. As to the initial detention, the court reasoned that

Officer Boyd’s observation of Mr. Garner sitting in the field, combined with Mr.


                                         -4-
Garner’s nervous and evasive behavior, provided reasonable suspicion to warrant

detaining Mr. Garner to investigate a possible public intoxication offense and to

determine whether Mr. Garner was suffering from some medical problem. The

court further concluded that even after the fire department personnel completed

their examination, “Officer Boyd had a continuing and remaining need to assess

[Mr. Garner’s] condition to determine whether he was under the influence of

drugs or alcohol . . . and to assess whether [Mr. Garner] was a danger to himself

or others.” Rec. vol. I, doc. 21, at 10 (Memorandum Decision and Order Denying

Defendant’s Motion to Suppress, filed Jan. 8, 2004). Thus, according to the

district court, the officers did not violate Mr. Garner’s Fourth Amendment rights,

and suppression of the evidence discovered in his pockets was not justified.



                                 II. DISCUSSION

      Mr. Garner now argues that Officer Boyd lacked reasonable suspicion to

detain him. He notes that the Officer Boyd acted on an anonymous tip and

observes that, before allowing police officers to detain a suspect, the courts have

usually required some kind of corroboration of the information provided by the

tip. As in the district court proceedings, Mr. Garner also argues that Officers

Boyd and Ransdell lacked the reasonable suspicion required to continue the

detention once fire department personnel finished the physical examination.


                                        -5-
      When reviewing the district court’s denial of a motion to suppress, we view

the evidence in the light most favorable to the government and accept the district

court’s factual findings unless they are clearly erroneous. United States v.

Kimoana, 383 F.3d 1215, 1220 (10th Cir. 2004). The ultimate question of

reasonableness under the Fourth Amendment is a legal conclusion that we review

de novo. Id.



                              A. The Initial Detention

      We begin our inquiry with the initial contact between the police officers

and Mr. Garner—Officer Boyd’s directing Mr. Garner to come back and sit down

so that the fire department personnel could examine him. Although Mr. Garner

argues that Officer Boyd then lacked any evidence that a crime had been

committed, that argument does not fully describe the role in which Officer Boyd

was acting.

      This court has recognized that “‘[e]ncounters are initiated by the police for

a wide variety of purposes, some of which are wholly unrelated to the desire to

prosecute for crime.’” United States v. King, 990 F.2d 1552, 1560 (10th Cir.

1993) (quoting Terry v. Ohio, 392 U.S. 1, 13 (1968)); see also id. (stating that

“those aspects of police function that relate to minimizing the likelihood of

disorder . . . are equal in their importance to the police function in identifying


                                         -6-
and punishing wrongdoers”) (quoting 1 ABA S TANDARDS FOR C RIMINAL J USTICE

§ 1-1.1(c), at 18 (2d ed. 1986)). The Supreme Court has deemed these

responsibilities “community caretaking functions” and has observed that they are

“totally divorced from the detection, investigation, or acquisition of evidence

relating to the violation of a criminal statute.” Cady v. Dombrowski, 413 U.S.

433, 441 (1973).

      In some circumstances, a police officer who is exercising these functions

may properly detain a person. King, 990 F.2d at 1561. For example, in King, we

concluded that a police officer’s brief detention of a motorist to advise him of

hazardous conditions created by an accident and to direct him to stop honking his

horn constituted a proper exercise of the community caretaking function

“regardless of whether [the defendant’s] actions violated any traffic laws.” Id.

      Like an investigative detention for law enforcement purposes, such a

community caretaking detention must be based upon “‘specific and articulable

facts which . . . reasonably warrant [an] intrusion’ into the individual’s liberty.”

Id. at 1560 (quoting Terry, 392 U.S. at 21). Additionally, the government’s

interest must outweigh the individual’s interest in being free from arbitrary

governmental interference. Id. Finally, the detention must last no longer than is

necessary to effectuate its purpose, and its scope must be carefully tailored to its

underlying justification. See Florida v. Royer, 460 U.S. 491, 500 (1983). Once


                                         -7-
the officer has completed the inquiry necessary to satisfy the purpose of the initial

detention, he or she must allow the person to proceed unless the officer has a

reasonable suspicion of criminal conduct. United States v. Gonzalez-Lerma, 14

F.3d 1479, 1483 (10th Cir. 1994).

      We acknowledge that some statements in our subsequent cases appear

inconsistent with the application of the community caretaking doctrine in King.

For example, in United States v. Bute , 43 F.3d 531, 535 (10th Cir. 1994), we

stated that “the community caretaking exception to the warrant requirement is

applicable only in cases involving automobile searches.” We agreed with the

Seventh Circuit that “the plain import from the language of [   Cady ] is that the

Supreme Court did not intend to create a broad exception to the Fourth

Amendment warrant requirement to apply whenever the police are acting in an

‘investigative,’ rather than a ‘criminal’ function’” and that “[the Supreme] Court

intended to confine the holding to the automobile exception and to foreclose an

expansive construction of the decision allowing warrantless searches of private

homes or businesses.”    Id. (quoting United States v. Pichany , 687 F.2d 204, 209

(7th Cir. 1982)). Accordingly, we rejected the government’s argument that the

search of an industrial building based on an officer’s suspicion of burglary and

vandalism was justified under the community caretaking doctrine.




                                           -8-
       In several other decisions, we have cited   Bute for the proposition that “the

community caretaking exception to the warrant requirement is applicable only in

cases involving automobile searches.”      See United States v. Maddox , 388 F.3d

1356, 1366 n.5 (10th Cir. 2004) (rejecting the government’s argument that the

community caretaking doctrine supported the detention of a defendant who had

reached under the seat of a pick-up truck as he pulled up to a residence where

officers were serving a search warrant),    cert. denied , 125 S. Ct. 1689 (2005);

United States v. Thomson , 354 F.3d 1197, 1200 n.1 (10th Cir. 2003) (noting the

government’s concession that the community caretaking doctrine was inapplicable

to a case in which officers had responded to reports of the defendant’s threatening

remarks to coworkers and had opened a canvas bag after the defendant stated that

the bag contained a gun).   But see Gallegos v. City of Colorado Springs    , 114 F.3d

1024, 1029 n.4 (10th Cir. 1997) (concluding that police officers properly detained

a citizen pursuant to the community caretaking function when they observed “a

distraught [man] on a public sidewalk in the middle of the night [who] [n]ot only

smell[ed] of alcohol, but . . . was crying and walking down the street with his

hands over his face”).

       Nevertheless, for several reasons these statements do not foreclose the

officers’ exercise of the community caretaking function here. First,     Bute

involved the search of a building, not, as here, the brief detention of a citizen


                                            -9-
reasonably believed by the officers to be at risk to himself. Additionally, in

Maddox and Thomson , the police officers were acting in their investigative

capacity; there is no indication that in effecting the detentions at issue, they acted

for some purpose “ wholly unrelated to the desire to prosecute for crime.” Terry,

392 U.S. at 13. Moreover, neither Bute nor Maddox nor Thomson cites King , and

our application of the community caretaking doctrine in the earlier case thus

remains the law of the circuit.   See Rogers v. United States , 281 F.3d 1108, 1116

(10th Cir. 2002) (observing that “earlier decisions prevail in the case of an

intra-circuit conflict”).

       Here, upon review of the record, we conclude that Officer Boyd was

exercising a community caretaking function when he directed Mr. Garner to

return so that the fire department could examine him. Cf. Gallegos , 114 F.3d at

1029 n.4 (concluding that police officers properly detained a citizen pursuant to

the community caretaking function when they observed him on a public sidewalk

in the middle of the night smelling of alcohol, crying, and holding his hands over

his face); United States v. Rideau, 969 F.2d 1572, 1574 (5th Cir. 1992) (en banc)

(concluding that officers properly detained a defendant for his own safety and the

safety of others after observing him standing in the middle of the road at night,

dressed in dark clothes, and apparently intoxicated). Moreover, Officer Boyd’s

directive was based on “specific and articulable facts . . . reasonably warrant[ing]


                                          -10-
that intrusion.” Terry, 392 U.S. at 21. In particular, Officer Boyd had received a

report of “an man down, said to be unconscious in a half sitting, half slumped

over position for several hours.” Rec. vol. II, at 5. When he arrived at the scene,

Officer Boyd found Mr. Garner, and he thus had reasonable grounds to conclude

that Mr. Garner might be in need of medical assistance.

      Officer Boyd also had reasonable suspicion that Mr. Garner may have

violated the criminal law. See Gallegos, 114 F.3d at 1029 n.4 (concluding that

police officers’ “initial stop . . . was valid under both an investigatory and

noninvestigatory rationale”). A Utah statute provides that:

             A person is guilty of intoxication if he is under the
             influence of alcohol, a controlled substance, or any
             substance having the property of releasing toxic vapors, to
             a degree that the person may endanger himself or another,
             in a public place or in a private place where he
             unreasonably disturbs other persons.

U TAH C ODE A NN . § 76-9-701(1). The report of an unconscious man in the field

outside the apartment complex, combined with Officer Boyd’s discovery of Mr.

Garner, provided the officer with grounds to briefly detain him to investigate a

possible public intoxication offense.

      We are not persuaded by Mr. Garner’s argument that the anonymity of the

person who called the police invalidates the initial detention. To be sure, as a

general rule, when police officers investigate the possible commission of a crime,

“something more than an anonymous tip of illegal activity is required to provide

                                          -11-
reasonable suspicion.” United States v. Tucker, 305 F.3d 1193, 1201 (10th Cir.

2002); see also Florida v. J.L., 529 U.S. 266, 268 (2000) (holding that “an

anonymous tip that a person is carrying a gun,” “without more,” did not establish

reasonable suspicion). That “something more” may be corroboration of

information provided by the tip. See id. at 270 (stating that “there are situations

in which an anonymous tip, suitably corroborated, exhibits ‘sufficient indicia of

reliability to provide reasonable suspicion to make the investigatory stop’”)

(quoting Alabama v. White, 496 U.S. 325, 327 (1990)). However, when the only

information corroborated is readily available and does not itself indicate that a

crime has been committed, reasonable suspicion may be lacking. See United

States v. Tuter, 240 F.3d 1292, 1297 (10th Cir. 2001) (noting that “[a]lmost

anyone can describe the residents of, and vehicles at, a particular home without

having any special knowledge of what goes on inside the home”).

      Nevertheless, the decisions upon which Mr. Garner relies in challenging the

anonymous source are distinguishable. Unlike the anonymous tips in those cases,

the tip here did not assert that Mr. Garner was engaging in some hidden criminal

activity. See e.g., J.L., 529 U.S. at 272 (describing the issue as whether “the

tipster ha[d] knowledge of concealed criminal activity”) (emphasis added); cf. 4

W AYNE R. L A F AVE , S EARCH AND S EIZURE § 9.5(h), at 571 (4th ed. 2004) (stating

that “the central issue [in this line of cases] is whether the informant’s


                                         -12-
information is so reliable and complete that it makes past, present, or pending

criminal conduct sufficiently likely to justify a stopping of the designated person

for investigation”). Thus, when the officers personally observed a man in the

field near the apartment complex, they confirmed the key information that they

had received from the anonymous source. Because that source had not purported

to describe any hidden criminal activities, no further investigation was necessary

to adequately corroborate the tip so that Officer Boyd could briefly detain Mr.

Garner.

      Similarly, the fact that Officer Boyd could not confirm all the information

offered by the anonymous source (e.g., how long Mr. Garner had been in the field

and whether he had been unconscious) is not dispositive. To establish reasonable

suspicion, not every detail of an anonymous tip must be verified. See White, 496

U.S. at 331.

      We further conclude that the government’s interest in community

caretaking outweighed Mr. Garner’s interest in being free from arbitrary

interference. The anonymous source had reported that Mr. Garner had remained

in the field for several hours and appeared unconscious. In light of that

observation, Mr. Garner might well have needed medical assistance, and the

government had a substantial interest in protecting him. See Rideau, 969 F.2d at

1574 (noting that police officers “have long served the public welfare by



                                        -13-
removing intoxicated people from the public streets, where they pose a hazard to

themselves and others”). In contrast, the intrusion upon Mr. Garner’s liberty was

not extensive. Officer Boyd merely told Mr. Garner to return to the spot from

where he had come so that fire department personnel could conduct a brief

physical examination.

      Accordingly, we conclude that Officer Boyd’s initial seizure of Mr. Garner

comported with the Fourth Amendment.



                           B. The Continuing Detention

      Mr. Garner also challenges Officer Boyd’s actions after the fire department

personnel completed their medical examination. As we have noted, when Mr.

Garner attempted to walk away for a second time, Officer Boyd told him to sit

back down because the police were not done with him yet. Mr. Garner argues that

the officers had no grounds upon which to continue to detain him.

      We disagree. As the fire department examined Mr. Garner, Officer Boyd

had an opportunity to make further observations. He noted that Mr. Garner

appeared “really nervous” and that he was moving his hands in and out of his

pockets. Rec. vol. II, at 8. Moreover, even though the fire department concluded

the examination and apparently found no emergency medical problems, Officer

Boyd had reason to believe that Mr. Garner might still have been intoxicated or



                                       -14-
constituted a danger to himself or others and that Mr. Garner may have violated

the Utah public intoxication statute. Cf. Illinois v. Wardlow, 528 U.S. 119, 125

(2002) (concluding that even though “the conduct justifying [a] stop was

ambiguous and susceptible of an innocent explanation[,]” the officers could

“detain the individuals to resolve the ambiguity”); Rideau, 969 F.2d at 1574-75

(concluding that an apparently intoxicated suspect’s nervous behavior and

backing away from police officers warranted extending the detention).

      Moreover, the continuing detention of Mr. Garner was reasonable in scope.

Although Mr. Garner maintains that Officer Boyd’s request for identification was

unduly intrusive, the Supreme Court has held that “[a]n identity request has an

immediate relation to the Terry stop’s purpose, rationale, and practical demands.”

See Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt County, 124 S. Ct.

2451, 2459 (2004). Officer Boyd’s asking Mr. Garner his name was thus

reasonable. In light of the information that Mr. Garner had been sitting and lying

in the field for several hours (which suggested that he might be a risk to himself

or others and that he might have violated the Utah public intoxication statute),

Mr. Garner’s continuing nervous behavior, and his moving his hands in and out of

his pockets, the subsequent questioning by Officers Boyd and Ransdell was also

reasonably related to the purposes of the detention.




                                        -15-
                               III. CONCLUSION

      Accordingly, we AFFIRM the district court’s decision denying Mr.

Garner’s motion to suppress.




                                     -16-

```

---
