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

## GROUP: _overhaul2/lake/cases/Texas v. Brown.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Texas v. Brown"
type: case
citation: "460 U.S. 730 (1983)"
parallel_cite: "103 S. Ct. 1535; 75 L. Ed. 2d 502; 51 U.S.L.W. 4361"
neutral_cite: 1983 U.S. LEXIS 143
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-04-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-04-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Texas v. Brown
  varies_by_point: false
  scope_note: "Plurality opinion; its 'immediately apparent = probable cause' reading is settled and was confirmed for plain view in Arizona v. Hicks and Horton v. California."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110901/texas-v-brown/"
  cluster_id: 110901
  opinion_id: 9429131
  identity_checked: false
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
related: ["[[Coolidge v. New Hampshire]]", "[[Arizona v. Hicks]]", "[[Horton v. California]]", "[[Minnesota v. Dickerson]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view"]
holding: "'Immediately apparent' means probable cause, not certainty ('an unhappy choice of words'); shining a flashlight into a car interior is not a search."
lake:
  record_id: Texas v. Brown
  status: under_review
  projected_at: 2026-07-06
---

# Texas v. Brown

*460 U.S. 730 (1983) (plurality)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At a routine driver's-license checkpoint an officer asked Brown for his license and, at the same time, shined a flashlight into the car. He saw Brown withdraw his hand from his pocket holding an opaque, knotted green party balloon — a packaging he knew from experience to be used for narcotics — and saw plastic vials, loose white powder, and an open bag of balloons in the glove compartment. The balloon held heroin.

## Issue
Whether seizure of the balloon was justified under the [[Plain View Doctrine|plain-view doctrine]] — in particular, what "immediately apparent" requires — and whether using a flashlight to look into the car's interior was itself a search.

## Rule
Illuminating a car's interior is not a search: the officer's "action in shining his flashlight to illuminate the interior of Brown's car trenched upon no right secured to the latter by the Fourth Amendment." — 460 U.S. at 739–40. ^pin-739

"Immediately apparent" does not mean certainty. The plurality explained that "the use of the phrase 'immediately apparent' was very likely an unhappy choice of words, since it can be taken to imply that an unduly high degree of certainty as to the incriminatory character of evidence is necessary for an application of the 'plain view' doctrine." — *Id.* at 741. ^pin-741

The standard is probable cause: the doctrine "does not demand any showing that such a belief be correct or more likely true than false. A 'practical, nontechnical' probability that incriminating evidence is involved is all that is required." — *Id.* at 742. ^pin-742

## Application
On these facts the officer had a lawful vantage point at the lawful checkpoint, used a flashlight (no search) to see into the car, and — drawing on his experience that knotted party balloons are used to carry narcotics, reinforced by the vials, powder, and bag of balloons in plain view — had probable cause to believe the balloon contained contraband. That practical probability satisfied "immediately apparent," so the warrantless seizure of the balloon was justified under the [[Plain View Doctrine|plain-view doctrine]].

## Conclusion
The seizure of the balloon was lawful; the Texas court's suppression was reversed. The "immediately apparent" element of plain view requires only probable cause, and shining a flashlight into a car is not a search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality).
- The probable-cause reading of "immediately apparent" was confirmed in [[Arizona v. Hicks]] (plain view requires probable cause) and the three-element plain-view test was restated in [[Horton v. California]]; the "immediately apparent" / probable-cause logic also governs the plain-feel rule of [[Minnesota v. Dickerson]].

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*

## Sources
- *Texas v. Brown*, 460 U.S. 730 (1983) (plurality) — https://www.courtlistener.com/opinion/110901/texas-v-brown/ — pinpoints: 739–40, 741, 742.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0b82f5672b8d1c2f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Texas v. Brown"}, "payload": {"all": [{"cite": "460 U.S. 730", "page": "730", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "460"}, {"cite": "103 S. Ct. 1535", "page": "1535", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "75 L. Ed. 2d 502", "page": "502", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "75"}, {"cite": "1983 U.S. LEXIS 143", "page": "143", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4361", "page": "4361", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "460 U.S. 730", "official": {"cite": "460 U.S. 730", "page": "730", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "460"}, "official_selection_present": true, "record_id": "Texas v. Brown"}}
{"assertion_id": "2793ea107116c52e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-741", "record_id": "Texas v. Brown"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-741", "pinpoint_status": "slip-only", "quote": "Immediately apparent", "quote_fidelity": "mismatch", "record_id": "Texas v. Brown", "star_marker": null}}
{"assertion_id": "427d3d834a16d4ed", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-739", "record_id": "Texas v. Brown"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-739", "pinpoint_status": "slip-only", "quote": "requires — and whether using a flashlight to look into the car's interior was itself a search. ## Rule Illuminating a car's interior is not a search: the officer's", "quote_fidelity": "mismatch", "record_id": "Texas v. Brown", "star_marker": null}}
{"assertion_id": "fff45aacfa2dd1b8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-742", "record_id": "Texas v. Brown"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-742", "pinpoint_status": "slip-only", "quote": "does not demand any showing that such a belief be correct or more likely true than false. A 'practical, nontechnical' probability that incriminating evidence is involved is all that is required.", "quote_fidelity": "mismatch", "record_id": "Texas v. Brown", "star_marker": null}}
{"assertion_id": "0011db442f4a4df0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Texas v. Brown"}, "payload": {"as_of_content": "1983-04-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Texas v. Brown", "scope_note": "Plurality opinion; its 'immediately apparent = probable cause' reading is settled and was confirmed for plain view in Arizona v. Hicks and Horton v. California.", "varies_by_point": false}}
```

### lake record — Texas v. Brown

```json
{
  "schema_version": "s2.v1",
  "record_id": "Texas v. Brown",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Texas v. Brown",
    "case_name_short": "Brown",
    "case_name_full": "Texas v. Brown",
    "input_case_name": "Texas v. Brown",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-04-19",
    "year": 1983,
    "docket": null,
    "cluster_id": 110901,
    "lead_opinion_id": 9429131,
    "sibling_ids": [
      110901,
      9429131,
      9429132,
      9429133,
      9429134
    ],
    "absolute_url": "/opinion/110901/texas-v-brown/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "460 U.S. 730",
      "volume": "460",
      "reporter": "U.S.",
      "page": "730",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1535",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 502",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "502",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4361",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4361",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 143",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "460 U.S. 730",
        "volume": "460",
        "reporter": "U.S.",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1535",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 502",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "502",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 143",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4361",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4361",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "460 U.S. 730",
    "official_selection": {
      "court_class": "scotus",
      "selected": "460 U.S. 730",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-739",
      "page": null,
      "quote": "requires \u2014 and whether using a flashlight to look into the car's interior was itself a search. ## Rule Illuminating a car's interior is not a search: the officer's",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-741",
      "page": null,
      "quote": "Immediately apparent",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-742",
      "page": null,
      "quote": "does not demand any showing that such a belief be correct or more likely true than false. A 'practical, nontechnical' probability that incriminating evidence is involved is all that is required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-04-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Texas v. Brown",
    "varies_by_point": false,
    "scope_note": "Plurality opinion; its 'immediately apparent = probable cause' reading is settled and was confirmed for plain view in Arizona v. Hicks and Horton v. California.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The State of Texas v. Christian Bruce Gonzales",
          "cluster_id": 9433471,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tanguay",
          "cluster_id": 4598184,
          "cite": [
            "918 F.3d 1"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532255,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4409778,
          "cite": [
            "2017 COA 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunn",
          "cluster_id": 111833,
          "cite": [
            "94 L. Ed. 2d 326",
            "107 S. Ct. 1134",
            "480 U.S. 294",
            "1987 U.S. LEXIS 1057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Georgia v. Randolph",
          "cluster_id": 145669,
          "cite": [
            "164 L. Ed. 2d 208",
            "126 S. Ct. 1515",
            "547 U.S. 103",
            "2006 U.S. LEXIS 2498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saldano v. State",
          "cluster_id": 1591817,
          "cite": [
            "70 S.W.3d 873",
            "2002 Tex. Crim. App. LEXIS 49",
            "2002 WL 385848"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Harris",
          "cluster_id": 820744,
          "cite": [
            "185 L. Ed. 2d 61",
            "133 S. Ct. 1050",
            "568 U.S. 237",
            "2013 U.S. LEXIS 1121"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Square",
          "cluster_id": 1827528,
          "cite": [
            "433 So. 2d 104"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Altria Group, Inc. v. Good",
          "cluster_id": 145925,
          "cite": [
            "172 L. Ed. 2d 398",
            "129 S. Ct. 538",
            "555 U.S. 70",
            "2008 U.S. LEXIS 9127",
            "77 U.S.L.W. 4021"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chaplaincy of Full Gospel Churches v. England",
          "cluster_id": 186744,
          "cite": [
            "454 F.3d 290",
            "372 U.S. App. D.C. 94",
            "65 Fed. R. Serv. 3d 808",
            "2006 U.S. App. LEXIS 16952",
            "103 Fair Empl. Prac. Cas. (BNA) 171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY5NTc3NjAwMDAwJnM9NDI0MTkyNSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110901+OR+9429131+OR+9429132+OR+9429133+OR+9429134%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTEmcz01NjcyMTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110901+OR+9429131+OR+9429132+OR+9429133+OR+9429134%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134)",
        "reviewed": 83,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 83,
        "triage_read": 2,
        "triage_snippet_classified": 81
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134)",
    "indexed_citing_opinions": 1905,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110901,
        "count": 1645,
        "count_source": "search"
      },
      {
        "opinion_id": 9429131,
        "count": 303,
        "count_source": "search"
      },
      {
        "opinion_id": 9429132,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429133,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429134,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3147,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/texas-v-brown.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzE3Nzkmcz0xMDM2MjY3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110901+OR+9429131+OR+9429132+OR+9429133+OR+9429134%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110901,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 102505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 296598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 303966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 313647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 316481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 328010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 329736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 329973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 330213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 338727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 359737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 374770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 391014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 399010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 401019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 403902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1193476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1208933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1239224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1362880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1526891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1631203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1687759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1710492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1739285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1774097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 2222769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 2418802,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 2448737,
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
    "date_created": "2026-07-05T21:24:55Z",
    "date_modified": "2026-07-06T08:56:23Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:25:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:25:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:25:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Texas v. Brown

```
<opinion type="majority">
<author id="b794-9">Justice Rehnquist</author>
<p id="A7s">announced the judgment of the Court and delivered an opinion, in which The Chief Justice, Justice White, and Justice O’Connor joined.</p>
<p id="b794-10">Respondent Clifford James Brown was convicted in the District Court of Tarrant County, Tex., for possession of heroin in violation of state law. The Texas Court of Criminal Appeals reversed his conviction, holding that certain evidence should have been suppressed because it was obtained in violation of the Fourth Amendment to the United States Constitution.<footnotemark>1</footnotemark> <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/" aria-description="Citation for case: Brown v. State">617 S. W. 2d 196</a></span>. That court rejected the <page-number citation-index="1" label="733">*733</page-number>State’s contention that the so-called “plain view” doctrine justified the police seizure. Because of apparent uncertainty concerning the scope and applicability of this doctrine, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1116/">457 U. S. 1116</a></span>, and now reverse the judgment of the Court of Criminal Appeals.</p>
<p id="b795-5">On a summer evening in June 1979, Tom Maples, an officer of the Fort Worth police force, assisted in setting up a routine driver’s license checkpoint on East Allen Street in that city. Shortly before midnight Maples stopped an automobile driven by respondent Brown, who was alone. Standing alongside the driver’s window of Brown’s car, Maples asked him for his driver’s license. At roughly the same time, Maples shined his flashlight into the car and saw Brown withdraw his right hand from his right pants pocket. Caught between the two middle fingers of the hand was an opaque, green party balloon, knotted about one-half inch from the tip. Brown let the balloon fall to the seat beside his leg, and then reached across the passenger seat and opened the glove compartment.</p>
<p id="b796-4"><page-number citation-index="1" label="734">*734</page-number>Because of his previous experience in arrests for drug offenses, Maples testified that he was aware that narcotics frequently were packaged in balloons like the one in Brown’s hand. When he saw the balloon, Maples shifted his position in order to obtain a better view of the interior of the glove compartment. He noticed that it contained several small plastic vials, quantities of loose white powder, and an open bag of party balloons. After rummaging briefly through the glove compartment, Brown told Maples that he had no driver’s license in his possession. Maples then instructed him to get out of the car and stand at its rear. Brown complied, and, before following him to the rear of the car, Maples reached into the car and picked up the green balloon; there seemed to be a sort of powdery substance within the tied-off portion of the balloon.</p>
<p id="b796-5">Maples then displayed the balloon to a fellow officer who indicated that he “understood the situation.” The two officers then advised Brown that he was under arrest.<footnotemark>2</footnotemark> They <page-number citation-index="1" label="735">*735</page-number>also conducted an on-the-scene inventory of Brown’s car, discovering several plastic bags containing a green leafy substance and a large bottle of milk sugar. These items, like the balloon, were seized by the officers. At the suppression hearing conducted by the District Court, a police department chemist testified that he had examined the substance in the balloon seized by Maples and determined that it was heroin. He also testified that narcotics frequently were packaged in ordinary party balloons.</p>
<p id="b797-5">The Court of Criminal Appeals, discussing the Fourth Amendment issue, observed that “ ‘plain view <em>alone </em>is never enough to justify the warrantless seizure of evidence.’ ” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span>, quoting <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 468</a></span> (1971) (opinion of Stewart, J., joined by Douglas, Brennan, and Marshall, JJ.) It further concluded that “Officer Maples had to <em>know </em>that ‘incriminatory evidence was before him when he seized the balloon.’” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span> (emphasis supplied), quoting <em>DeLao </em>v. <em>State, </em><span class="citation" data-id="9769560"><a href="/opinion/2418802/delao-v-state/#291" aria-description="Citation for case: DeLao v. State">550 S. W. 2d 289, 291</a></span> (Tex. Crim. App. 1977). On the State’s petition for rehearing, three judges dissented, stating their view that “[t]he issue turns on whether an officer, relying on years of practical experience and knowledge commonly accepted, has probable cause to seize the balloon in plain view.” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#201" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 201</a></span>.</p>
<p id="b797-6">Because the “plain view” doctrine generally is invoked in conjunction with other Fourth Amendment principles, such as those relating to warrants, probable cause, and search incident to arrest, we rehearse briefly these better understood principles of Fourth Amendment law. That Amendment secures the persons, houses, papers, and effects of the people against unreasonable searches and seizures, and requires the existence of probable cause before a warrant shall issue. Our cases hold that procedure by way of a warrant is preferred, although in a wide range of diverse situations we have recognized flexible, common-sense exceptions to this requirement. See, <em>e. g., Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) <page-number citation-index="1" label="736">*736</page-number>(hot pursuit); <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51-52</a></span> (1951) (exigent circumstances); <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982) (automobile search); <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), and <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981) (search of person and surrounding area incident to arrest); <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973) (search at border or “functional equivalent”); <em>Zap </em>v. <em>United States, </em><span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#630" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 630</a></span> (1946) (consent). We have also held to be permissible intrusions less severe than full-scale searches or seizures without the necessity of a warrant. See, <em>e. g., Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968) (stop and frisk); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975) (seizure for questioning); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979) (roadblock). One frequently mentioned “exception to the warrant requirement,” <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#456" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 456</a></span>, is the so-called “plain view” doctrine, relied upon by the State in this case.</p>
<p id="b798-5">While conceding that the green balloon seized by Officer Maples was clearly visible to him, the Court of Criminal Appeals held that the State might not avail itself of the “plain view” doctrine. That court said:</p>
<blockquote id="b798-6">“For the plain view doctrine to apply, not only must the officer be legitimately in a position to view the object, but it must be immediately apparent to the police that they have evidence before them. This ‘immediately apparent’ aspect is central to the plain view exception and is here relied upon by appellant. [Citation omitted.] In this case then, Officer Maples had to know that ‘incriminatory evidence was before him when he seized the balloon.’” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span>.</blockquote>
<p id="b798-7">The Court of Criminal Appeals based its conclusion primarily on the plurality portion of the opinion of this Court in <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra.</a></span> </em>In the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality’s view, the “plain view” doctrine permits the warrantless seizure by police of private possessions where three require<page-number citation-index="1" label="737">*737</page-number>ments are satisfied.<footnotemark>3</footnotemark> First, the police officer must lawfully make an “initial intrusion” or otherwise properly be in a position from which he can view a particular area. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 465-468</a></span>. Second, the officer must discover incriminating evidence “inadvertently,” which is to say, he may not “know in advance the location of [certain] evidence and intend to seize it,” relying on the plain-view doctrine only as a pretext. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#470" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 470</a></span>. Finally, it must be “immediately apparent” to the police that the items they observe may be evidence of a crime, contraband, or otherwise subject to seizure. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#466" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 466</a></span>. While the lower courts generally have applied the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality’s discussion of “plain view,” it has never been expressly adopted by a majority of this Court. On the contrary, the plurality’s formulation was sharply criticized at the time, see, <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#506" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 506</a></span> (Black, J., dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#516" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 516-521</a></span> (White, J., dissenting). While not a binding precedent, as the considered opinion of four Members of this Court it should obviously be the point of reference for further discussion of the issue.</p>
<p id="b799-5">The <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality observed: “it is important to keep in mind that, in the vast majority of cases, <em>any </em>evidence seized by the police will be in plain view, at least at the moment of seizure,” simply as “the normal concomitant of any search, legal or illegal.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 465</a></span>. The question whether property in plain view of the police may be seized therefore must turn on the legality of the intrusion that enables them to perceive and physically seize the property in question. The <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality, while following this approach to “plain <page-number citation-index="1" label="738">*738</page-number>view,” characterized it as an independent exception to the warrant requirement. At least from an analytical perspective, this description may be somewhat inaccurate. We recognized in <em>Payton </em>v. <em>New, York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980), the well-settled rule that “objects such as weapons or contraband found in a public place may be seized by the police without a warrant. The seizure of property in plain view involves no invasion of privacy and is presumptively reasonable, assuming that there is probable cause to associate the property with criminal activity.” A different situation is presented, however, when the property in open view is “‘situated on private premises to which access is not otherwise available for the seizing officer.’” <em>Ibid., </em>quoting <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#354" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 354</a></span> (1977). As these cases indicate, “plain view” provides grounds for seizure of an item when an officer’s access to an object has some prior justification under the Fourth Amendment.<footnotemark>4</footnotemark> “Plain view” is perhaps better understood, therefore, not as an independent “exception” to the Warrant <page-number citation-index="1" label="739">*739</page-number>Clause, but simply as an extension of whatever the prior justification for an officer’s “access to an object” may be.</p>
<p id="b801-5">The principle is grounded on the recognition that when a police officer has observed an object in “plain view,” the owner’s remaining interests in the object are merely those of possession and ownership, see <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#515" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 515</a></span> (White, J., dissenting). Likewise, it reflects the fact that requiring police to obtain a warrant once they have obtained a first-hand perception of contraband, stolen property, or incriminating evidence generally would be a “needless inconvenience,” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 468</a></span>, that might involve danger to the police and public. <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Ibid.</a></span> </em>We have said previously that “the permissibility of a particular law enforcement practice is judged by balancing its intrusion on . . . Fourth Amendment interests against its promotion of legitimate governmental interests.” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 654</a></span>. In light of the private and governmental interests just outlined, our decisions have come to reflect the rule that if, while lawfully engaged in an activity in a particular place, police officers perceive a suspicious object, they may seize it immediately. See <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927); <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span> (1931); <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465</a></span> (1932); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968); <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969). This rule merely reflects an application of the Fourth Amendment’s central requirement of reasonableness to the law governing seizures of property.</p>
<p id="b801-6">Applying these principles, we conclude that Officer Maples properly seized the green balloon from Brown’s automobile. The Court of Criminal Appeals stated that it did not “question . . . the validity of the officer’s initial stop of appellant’s vehicle as a part of a license check,” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span>, and we agree. <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 654-655</a></span>. It is likewise beyond dispute that Maples’ action in shining his <page-number citation-index="1" label="740">*740</page-number>flashlight to illuminate the interior of Brown’s car trenched upon no right secured to the latter by the Fourth Amendment. The Court said in <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span> (1927): “[The] use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution.” Numerous other courts have agreed that the use of artificial means to illuminate a darkened area simply does not constitute a search, and thus triggers no Fourth Amendment protection.<footnotemark>5</footnotemark></p>
<p id="b802-5">Likewise, the fact that Maples “changed [his] position” and “bent down at an angle so [he] could see what was inside” Brown’s car, App. 16, is irrelevant to Fourth Amendment analysis. The general public could peer into the interior of Brown’s automobile from any number of angles; there is no reason Maples should be precluded from observing as an officer what would be entirely visible to him as a private citizen. There is no legitimate expectation of privacy, <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring); <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#739" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 739-745</a></span> (1979), shielding that portion of the interior of an automobile which may be viewed from outside the vehicle by either inquisitive passersby or diligent police officers. In short, the conduct that enabled Maples to observe the interior of Brown’s car and of his open glove compartment was not a search within the meaning of the Fourth Amendment.</p>
<p id="b803-4"><page-number citation-index="1" label="741">*741</page-number>Thus there can be no dispute here as to the presence of the first of the three requirements held necessary by the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality to invoke the “plain view” doctrine.<footnotemark>6</footnotemark> But the Court of Criminal Appeals, as we have noted, felt the State’s case ran aground on the requirement that the incriminating nature of the items be “immediately apparent” to the police officer. To the Court of Criminal Appeals, this apparently meant that the officer must be possessed of near certainty as to the seizable nature of the items. Decisions by this Court since <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>indicate that the use of the phrase “immediately apparent” was very likely an unhappy choice of words, since it can be taken to imply that an unduly high degree of certainty as to the incriminatory character of evidence is necessary for an application of the “plain view” doctrine.</p>
<p id="b803-5">In <em>Colorado </em>v. <em>Bannister, </em><span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#3" aria-description="Citation for case: Colorado v. Bannister">449 U. S. 1, 3-4</a></span> (1980), we applied what was in substance the plain-view doctrine to an officer’s seizure of evidence from an automobile. <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#4" aria-description="Citation for case: Colorado v. Bannister"><em>Id., </em>at 4, n. 4</a></span>. The officer noticed that the occupants of the automobile matched a description of persons suspected of a theft and that auto parts in the open glove compartment of the car similarly resembled ones reported stolen. The Court held that these facts supplied the officer with “probable cause,” <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#4" aria-description="Citation for case: Colorado v. Bannister"><em>id., </em>at 4</a></span>, and therefore, that he could seize the incriminating items from the car without a warrant. Plainly, the Court did not view the “immediately apparent” language of <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>as establishing any requirement that a police officer “know” that certain items are contraband or evidence of a crime. Indeed, <em>Colorado </em>v. <em><span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">Bannister, supra,</a></span> </em>was merely an application of the rule, set forth in <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), that “[t]he seizure of property in plain view involves no invasion of privacy and <em>is presumptively reasonable, assuming that there is probable cause to associate the property </em><page-number citation-index="1" label="742">*742</page-number><em>with criminal activity.” Id., </em>at 587 (emphasis added). We think this statement of the rule from <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton, supra,</a></span> </em>requiring probable cause for seizure in the ordinary case,<footnotemark>7</footnotemark> is consistent with the Fourth Amendment and we reaffirm it here.</p>
<p id="b804-4">As the Court frequently has remarked, probable cause is a flexible, common-sense standard. It merely requires that the facts available to the officer would “warrant a man of reasonable caution in the belief,” <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/#162" aria-description="Citation for case: Work v. United States Ex Rel. Rives">267 U. S. 182, 162</a></span> (1925), that certain items may be contraband or stolen property or useful as evidence of a crime; it does not demand any showing that such a belief be correct or more likely true than false. A “practical, nontechnical” probability that incriminating evidence is involved is all that is required. <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). Moreover, our observation in <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981), regarding “particularized suspicion,” is equally applicable to the probable-cause requirement:</p>
<blockquote id="b804-5">“The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain common-sense conclusions about human behavior; jurors as factfinders are permitted to do the same — and so are law enforcement officers. Finally, the evidence thus collected must be seen and weighed not in terms of library analysis by scholars, but as understood by those versed in the field of law enforcement.”</blockquote>
<p id="b804-6">With these considerations in mind it is plain that Officer Maples possessed probable cause to believe that the balloon in Brown’s hand contained an illicit substance. Maples testified that he was aware, both from his participation in previous narcotics arrests and from discussions with other officers,</p>
<p id="b805-4"><page-number citation-index="1" label="743">*743</page-number>that balloons tied in the manner of the one possessed by Brown were frequently used to carry narcotics. This testimony was corroborated by that of a police department chemist who noted that it was “common” for balloons to be used in packaging narcotics. In addition, Maples was able to observe the contents of the glove compartment of Brown’s car, which revealed further suggestions that Brown was engaged in activities that might involve possession of illicit substances. The fact that Maples could not see through the opaque fabric of the balloon is all but irrelevant: the distinctive character of the balloon itself spoke volumes as to its contents — particularly to the trained eye of the officer.</p>
<p id="b805-5">In addition to its statement that for seizure of objects in plain view to be justified the basis upon which they might be seized had to be “immediately apparent,” and the requirement that the initial intrusion be lawful, both of which requirements we hold were satisfied here, the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality also stated that the police must discover incriminating evidence “inadvertently,” which is to say, they may not “know in advance the location of [certain] evidence and intend to seize it,” relying on the plain-view doctrine only as a pretense. 430 U. S., at 470. Whatever may be the final disposition of the “inadvertence” element of “plain view,”<footnotemark>8</footnotemark> it clearly was no bar to the seizure here. The circumstances of this meeting between Maples and Brown give no suggestion that the roadblock was a pretext whereby evidence of narcotics violation might be uncovered in “plain view” in the course of a check for driver’s licenses. Here, although the officers no doubt had an expectation that some of the cars they halted on East Allen Street — which was part of a “medium” area of narcotics traffic, App. 33 — would contain narcotics or para<page-number citation-index="1" label="744">*744</page-number>phernalia, there is no indication in the record that they had anything beyond this generalized expectation. Likewise, there is no indication that Maples had any reason to believe that any particular object would be in Brown’s glove compartment or elsewhere in his automobile. The “inadvertence” requirement of “plain view,” properly understood, was no bar to the seizure here.</p>
<p id="b806-5">Maples lawfully viewed the green balloon in the interior of Brown’s car, and had probable cause to believe that it was subject to seizure under the Fourth Amendment. The judgment of the Texas Court of Criminal Appeals is accordingly reversed, and the case is remanded for further proceedings.</p>
<p id="b806-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b794-12"> Brown argues that the decision below rested on an independent and adequate state ground, and therefore that this Court lacks jurisdiction. <em>Fox Film Corp. </em>v. <em>Muller, </em><span class="citation" data-id="102505"><a href="/opinion/102505/fox-film-corp-v-muller/#210" aria-description="Citation for case: Fox Film Corp. v. Muller">296 U. S. 207, 210</a></span> (1935). The position is untenable. The opinion of the Texas Court of Criminal Appeals rests squarely on the interpretation of the Fourth Amendment to the United States Constitution in <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), and on Texas cases interpreting that decision, <em>e. g., Howard </em>v. <em>State, </em><span class="citation" data-id="9661682"><a href="/opinion/1631203/howard-v-state/" aria-description="Citation for case: Howard v. State">599 S. W. 2d 597</a></span> (Tex. Crim. App. 1979); <em>DeLao </em>v. <em>State, </em><span class="citation" data-id="9769560"><a href="/opinion/2418802/delao-v-state/" aria-description="Citation for case: DeLao v. State">550 S. W. 2d 289</a></span> (Tex. Crim. App. 1977); <em>Duncan </em>v. <em>State, </em><span class="citation" data-id="9647768"><a href="/opinion/1526891/duncan-v-state/" aria-description="Citation for case: Duncan v. State">549 S. W. 2d 730</a></span> (Tex. Crim. App. 1977); and <em>Nicholas </em>v. <em>State, </em><span class="citation" data-id="9775167"><a href="/opinion/2448737/nicholas-v-state/" aria-description="Citation for case: Nicholas v. State">502 S. W. 2d 169</a></span> (Tex. Crim. App. 1973). The only men<page-number citation-index="1" label="733">*733</page-number>tion of the Texas Constitution occurs in a summary of Brown’s contentions at the outset of the lower court’s opinion.</p>
<p id="b795-7">Brown relies principally on <em>Howard </em>v. <em>State, supra, </em>and <em>Duncan </em>v. <em>State, supra. </em>Neither decision supports the proposition that the Texas Court of Criminal Appeals based its decision upon state law. In <em>Howard, </em>the State argued that the plain-view doctrine justified the seizure of a closed translucent medicine jar from an automobile. The Court of Criminal Appeals rejected the claim, relying on <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra,</a></span> </em>and stating that the State’s arguments “cannot be squared with the Supreme Court’s interpretation of the plain view doctrine.” <span class="citation" data-id="9661682"><a href="/opinion/1631203/howard-v-state/#602" aria-description="Citation for case: Howard v. State">599 S. W. 2d, at 602</a></span>. The court also relied on <em>Thomas </em>v. <em>State, </em><span class="citation" data-id="9680885"><a href="/opinion/1774097/thomas-v-state/" aria-description="Citation for case: Thomas v. State">572 S. W. 2d 507</a></span> (Tex. Crim. App. 1976), which it characterized as “[fjollowing the teachings of <em>Coolidge </em>v. <em>New Hampshire.” </em><span class="citation" data-id="9661682"><a href="/opinion/1631203/howard-v-state/#602" aria-description="Citation for case: Howard v. State">599 S. W. 2d, at 602</a></span>. An additional opinion of the court on the State’s motion for rehearing merely elaborated upon the application of the plain-view doctrine set forth in the court’s original opinion. Similarly, in <em><span class="citation" data-id="9647768"><a href="/opinion/1526891/duncan-v-state/" aria-description="Citation for case: Duncan v. State">Duncan</a></span>, </em>the Court of Criminal Appeals rejected the State’s reliance on the plain-view theory, citing to <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>for a statement of the applicable law, as well as to <em>Nicholas </em>v. <em>State, supra. </em>Like the court’s other decisions in the area, <em><span class="citation" data-id="9775167"><a href="/opinion/2448737/nicholas-v-state/" aria-description="Citation for case: Nicholas v. State">Nicholas</a></span> </em>relied only on <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>.</em></p>
</footnote>
<footnote label="2">
<p id="b796-6"> It is not clear on the record before us when Brown was arrested. The Court of Criminal Appeals stated, at one point in its opinion, that it did not question “the propriety of the arrest since appellant failed to produce a driver’s license.” ■ <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d 196,200</a></span>. This statement might be read to suggest that Brown was arrested upon his failure to produce a license, instead of at some point following seizure of the balloon from the car. The transcript of the suppression hearing, however, indicates rather clearly that Brown was not formally arrested until after seizure of the balloon. App. 28-31. In the face of such indications, we decline to interpret the above-quoted clause from the Court of Criminal Appeals’ opinion as evidencing a belief that an arrest occurred prior to seizure of the balloon. Rather, we think it likely that the court was simply reasoning that Brown’s arrest, whenever it may have taken place, was justified because of his failure to produce a driver’s license.</p>
<p id="b796-7">We do not address the argument that seizure of the balloon would have been justified under <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), which permits warrantless searches of the passenger compartment of an automobile incident to an arrest, because of the absence of clear factual findings regarding the time at which, and the reason for which, Brown was arrested and because the lower court was not able to consider that decision.</p>
</footnote>
<footnote label="3">
<p id="b799-6"> The plurality also remarked that “plain view <em>alone </em>is never enough to justify the warrantless seizure of evidence.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 468</a></span>. The court below appeared to understand this phrase to impose an independent limitation upon the scope of the plain-view doctrine articulated in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>. </em>The context in which the plurality used the phrase, however, indicates that it was merely a rephrasing of its conclusion, discussed below, that in order for the plain-view doctrine to apply, a police officer must be engaged in a lawful intrusion or must otherwise legitimately occupy the position affording him a “plain view.”</p>
</footnote>
<footnote label="4">
<p id="b800-5"> Thus, police may perceive an object while executing a search warrant, or they may come across an item while acting pursuant to some exception to the Warrant Clause, <em>e. g., Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). Alternatively, police may need no justification under the Fourth Amendment for their access to an item, such as when property is left in a public place, see <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980).</p>
<p id="b800-6">It is important to distinguish “plain view,” as used in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>to justify <em>seizure </em>of an object, from an officer’s mere observation of an item left in plain view. Whereas the latter generally involves no Fourth Amendment search, see <em>infra, </em>at 740; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the former generally does implicate the Amendment’s limitations upon seizures of personal property. The information obtained as a result of observation of an object in plain sight may be the basis for probable cause or reasonable suspicion of illegal activity. In turn, these levels of suspicion may, in some cases, see, <em>e. g., Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra;</a></span> United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), justify police conduct affording them access to a particular item.</p>
</footnote>
<footnote label="5">
<p id="b802-6"><em> E. g., United States </em>v. <em>Chesher, </em><span class="citation" data-id="9469232"><a href="/opinion/403902/united-states-v-lawrence-gilbert-chesher/#1356" aria-description="Citation for case: United States v. Lawrence Gilbert Chesher">678 F. 2d 1353, 1356-1357, n. 2</a></span> (CA9 1982); <em>United States </em>v. <em>Ocampo, </em><span class="citation" data-id="391014"><a href="/opinion/391014/united-states-v-daniel-ocampo-theodoro-hernandez-jose-otero-and/#427" aria-description="Citation for case: United States v. Daniel Ocampo, Theodoro Hernandez, Jose...">650 F. 2d 421, 427</a></span> (CA2 1981); <em>United States </em>v. <em>Pugh, </em><span class="citation" data-id="350948"><a href="/opinion/350948/united-states-v-larry-wayne-pugh/#627" aria-description="Citation for case: United States v. Larry Wayne Pugh">566 F. 2d 626, 627, n. 2</a></span> (CA8 1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/1010/">435 U. S. 1010</a></span> (1978); <em>United States </em>v. <em>Coplen, </em><span class="citation" data-id="338727"><a href="/opinion/338727/united-states-v-tommy-joe-coplen-united-states-of-america-v-henry/" aria-description="Citation for case: United States v. Tommy Joe Coplen, United States of...">541 F. 2d 211</a></span> (CA9 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1073/">429 U. S. 1073</a></span> (1977); <em>United States </em>v. <em>Lara, </em><span class="citation" data-id="328010"><a href="/opinion/328010/united-states-v-ruben-garza-lara/" aria-description="Citation for case: United States v. Ruben Garza Lara">517 F. 2d 209</a></span> (CA5 1975); <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9461232"><a href="/opinion/323153/united-states-v-kenneth-wayne-johnson-united-states-of-america-v-derrick/" aria-description="Citation for case: United States v. Kenneth Wayne Johnson, United States of...">506 F. 2d 674</a></span> (CA8 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./421/917/">421 U. S. 917</a></span> (1975); <em>United States </em>v. <em>Booker, </em><span class="citation" data-id="9458318"><a href="/opinion/303966/united-states-v-robert-lee-booker/#992" aria-description="Citation for case: United States v. Robert Lee Booker">461 F. 2d 990, 992</a></span> (CA6 1972); <em>United States </em>v. <em>Hanahan, </em><span class="citation" data-id="296598"><a href="/opinion/296598/united-states-v-robert-michael-hanahan/" aria-description="Citation for case: United States v. Robert Michael Hanahan">442 F. 2d 649</a></span> (CA7 1971); <em>People </em>v. <em>Waits, </em><span class="citation" data-id="9557787"><a href="/opinion/1193476/people-v-waits/" aria-description="Citation for case: People v. Waits">196 Colo. 35</a></span>, <span class="citation" data-id="9557787"><a href="/opinion/1193476/people-v-waits/" aria-description="Citation for case: People v. Waits">580 P. 2d 391</a></span> (1978); <em>Redd </em>v. <em>State, </em><span class="citation" data-id="5596513"><a href="/opinion/5744734/redd-v-state/" aria-description="Citation for case: Redd v. State">240 Ga. 753</a></span>, <span class="citation" data-id="5596513"><a href="/opinion/5744734/redd-v-state/" aria-description="Citation for case: Redd v. State">243 S. E. 2d 16</a></span> (1978); <em>State </em>v. <em>Chattley, </em><span class="citation" data-id="2332441"><a href="/opinion/2332441/state-v-chattley/" aria-description="Citation for case: State v. Chattley">390 A. 2d 472</a></span> (Me. 1978); <em>State </em>v. <em>Vohnoutka, </em><span class="citation" data-id="2222769"><a href="/opinion/2222769/state-v-vohnoutka/" aria-description="Citation for case: State v. Vohnoutka">292 N. W. 2d 756</a></span> (Minn. 1980); <em>Dick </em>v. <em>State, </em><span class="citation" data-id="1362880"><a href="/opinion/1362880/dick-v-state/" aria-description="Citation for case: Dick v. State">596 P. 2d 1265</a></span> (Okla. Crim. App. 1979); <em>State </em>v. <em>Miller, </em><span class="citation" data-id="1208933"><a href="/opinion/1208933/state-v-miller/" aria-description="Citation for case: State v. Miller">45 Ore. App. 407</a></span>, <span class="citation" data-id="1208933"><a href="/opinion/1208933/state-v-miller/" aria-description="Citation for case: State v. Miller">608 P. 2d 595</a></span> (1980); <em>Albo </em>v. <em>State, </em><span class="citation" data-id="1687759"><a href="/opinion/1687759/albo-v-state/" aria-description="Citation for case: Albo v. State">379 So. 2d 648</a></span> (Fla. 1980).</p>
</footnote>
<footnote label="6">
<p id="b803-6"> While seizure of the balloon required a warrantless, physical intrusion into Brown’s automobile, this was proper, assuming that the remaining requirements of the plain-view doctrine were satisfied. <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982).</p>
</footnote>
<footnote label="7">
<p id="b804-7"> We need not address whether, in some circumstances, a degree of suspicion lower than probable cause would be sufficient basis for a seizure in certain cases.</p>
</footnote>
<footnote label="8">
<p id="b805-6"> See <em>State </em>v. <em>King, </em><span class="citation" data-id="9671244"><a href="/opinion/1710492/state-v-king/#655" aria-description="Citation for case: State v. King">191 N. W. 2d 650, 655</a></span> (Iowa 1971); <em>United States </em>v. <em>Santana, </em><span class="citation" data-id="313647"><a href="/opinion/313647/united-states-v-gilberto-santana/#369" aria-description="Citation for case: United States v. Gilberto Santana">485 F. 2d 365, 369-370</a></span> (CA2 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/931/">415 U. S. 931</a></span> (1974); <em>United States </em>v. <em>Bradshaw, </em><span class="citation" data-id="9460223"><a href="/opinion/316481/united-states-v-william-garland-bradshaw/#1101" aria-description="Citation for case: United States v. William Garland Bradshaw">490 F. 2d 1097, 1101, n. 3</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/895/">419 U. S. 895</a></span> (1974); <em>North </em>v. <em>Superior Court, </em><span class="citation" data-id="9577161"><a href="/opinion/1239224/north-v-superior-court/#306" aria-description="Citation for case: North v. Superior Court">8 Cal. 3d 301, 306-307</a></span>, <span class="citation" data-id="9577161"><a href="/opinion/1239224/north-v-superior-court/#1308" aria-description="Citation for case: North v. Superior Court">502 P. 2d 1305, 1308</a></span> (1972).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Texas v. Cobb.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Texas v. Cobb"
type: case
citation: "532 U.S. 162 (2001)"
parallel_cite: "121 S. Ct. 1335; 149 L. Ed. 2d 321"
neutral_cite: 2001 U.S. LEXIS 2696
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-04-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-04-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Texas v. Cobb
  varies_by_point: false
  scope_note: "Good law; defines the scope of the Sixth Amendment right by the Blockburger same-elements test."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118417/texas-v-cobb/"
  cluster_id: 118417
  opinion_id: 9434063
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[McNeil v. Wisconsin]]", "[[Massiah v. United States]]", "[[Brewer v. Williams]]", "[[Montejo v. Louisiana]]", "[[Maine v. Moulton]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel"]
holding: "The Sixth Amendment right to counsel is offense-specific; it attaches only to the charged offense and does not extend to other,…"
lake:
  record_id: Texas v. Cobb
  status: verified
  projected_at: 2026-07-06
---

# Texas v. Cobb

*532 U.S. 162 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Cobb was indicted for burglary of a home and was appointed counsel on that charge. A woman and her infant daughter had disappeared from the home. While free on bond and represented on the burglary, Cobb later confessed to his father, who told police; after [[Miranda and Custodial Interrogation|Miranda warnings]] and a waiver, Cobb confessed to murdering the woman and child. He argued the murder confession was taken in violation of his Sixth Amendment right to counsel, which had attached on the factually related burglary.

## Issue
Whether the Sixth Amendment right to counsel, once it has attached to a charged offense, also extends to other uncharged offenses that are factually related to the charged one.

## Rule
The right to counsel is charge-specific: "the Sixth Amendment right is 'offense specific.'" — 532 U.S. at 164. ^pin-164

It therefore does not automatically reach other, uncharged offenses merely because they are factually intertwined with the charged crime. The scope of an "offense" is fixed by the *Blockburger* same-elements test: "where the same act or transaction constitutes a violation of two distinct statutory provisions, the test to be applied to determine whether there are two offenses or only one, is whether each provision requires proof of a fact which the other does not." — *Id.* at 173. ^pin-173

## Application
Because Cobb had been charged only with burglary, his Sixth Amendment right had attached to that offense alone. Capital murder and burglary each require proof of an element the other does not, so under *Blockburger* they are separate offenses; the murder was not the "same offense" as the charged burglary. The right to counsel on the burglary therefore did not bar police from questioning Cobb about the uncharged murders, and his Miranda-waived confession was admissible.

## Conclusion
The Sixth Amendment right to counsel did not extend to the uncharged murders; the Texas court's reversal was itself reversed. A defendant's attachment of counsel on one charge does not insulate him from interrogation on distinct, uncharged offenses.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Cobb* applies and confines the offense-specific rule of [[McNeil v. Wisconsin]]; it is read alongside [[Massiah v. United States]] and [[Brewer v. Williams]] (deliberate elicitation after attachment) and [[Montejo v. Louisiana]] (waiver of the attached right).

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Texas v. Cobb*, 532 U.S. 162 (2001) — https://www.courtlistener.com/opinion/118417/texas-v-cobb/ — pinpoints: 164, 173.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d31544984e9e01e8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Texas v. Cobb"}, "payload": {"all": [{"cite": "532 U.S. 162", "page": "162", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "532"}, {"cite": "121 S. Ct. 1335", "page": "1335", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "149 L. Ed. 2d 321", "page": "321", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "149"}, {"cite": "2001 U.S. LEXIS 2696", "page": "2696", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}], "display": "532 U.S. 162", "official": {"cite": "532 U.S. 162", "page": "162", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "532"}, "official_selection_present": true, "record_id": "Texas v. Cobb"}}
{"assertion_id": "a4ccc337de484991", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-173", "record_id": "Texas v. Cobb"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-173", "pinpoint_status": "slip-only", "quote": "is fixed by the *Blockburger* same-elements test:", "quote_fidelity": "mismatch", "record_id": "Texas v. Cobb", "star_marker": null}}
{"assertion_id": "b8c581809b82fad4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-164", "record_id": "Texas v. Cobb"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-164", "pinpoint_status": "slip-only", "quote": "--- # Texas v. Cobb *532 U.S. 162 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Cobb was indicted for burglary of a home and was appointed counsel on that charge. A woman and her infant daughter had disappeared from the home. While free on bond and represented on the burglary, Cobb later confessed to his father, who told police; after Miranda warnings and a waiver, Cobb confessed to murdering the woman and child. He argued the murder confession was taken in violation of his Sixth Amendment right to counsel, which had attached on the factually related burglary. ## Issue Whether the Sixth Amendment right to counsel, once it has attached to a charged offense, also extends to other uncharged offenses that are factually related to the charged one. ## Rule The right to counsel is charge-specific:", "quote_fidelity": "mismatch", "record_id": "Texas v. Cobb", "star_marker": null}}
{"assertion_id": "693f47b49ffac9c1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Texas v. Cobb"}, "payload": {"as_of_content": "2001-04-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Texas v. Cobb", "scope_note": "Good law; defines the scope of the Sixth Amendment right by the Blockburger same-elements test.", "varies_by_point": false}}
```

### lake record — Texas v. Cobb

```json
{
  "schema_version": "s2.v1",
  "record_id": "Texas v. Cobb",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Texas v. Cobb",
    "case_name_short": "Cobb",
    "case_name_full": "Texas v. Cobb",
    "input_case_name": "Texas v. Cobb",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-04-17",
    "year": 2001,
    "docket": null,
    "cluster_id": 118417,
    "lead_opinion_id": 9434063,
    "sibling_ids": [
      118417,
      9434063,
      9434064,
      9434065
    ],
    "absolute_url": "/opinion/118417/texas-v-cobb/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "532 U.S. 162",
      "volume": "532",
      "reporter": "U.S.",
      "page": "162",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 1335",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1335",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 321",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 2696",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "2696",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "532 U.S. 162",
        "volume": "532",
        "reporter": "U.S.",
        "page": "162",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1335",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1335",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 321",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 2696",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "2696",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "532 U.S. 162",
    "official_selection": {
      "court_class": "scotus",
      "selected": "532 U.S. 162",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-164",
      "page": null,
      "quote": "--- # Texas v. Cobb *532 U.S. 162 (2001)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Cobb was indicted for burglary of a home and was appointed counsel on that charge. A woman and her infant daughter had disappeared from the home. While free on bond and represented on the burglary, Cobb later confessed to his father, who told police; after Miranda warnings and a waiver, Cobb confessed to murdering the woman and child. He argued the murder confession was taken in violation of his Sixth Amendment right to counsel, which had attached on the factually related burglary. ## Issue Whether the Sixth Amendment right to counsel, once it has attached to a charged offense, also extends to other uncharged offenses that are factually related to the charged one. ## Rule The right to counsel is charge-specific:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-173",
      "page": null,
      "quote": "is fixed by the *Blockburger* same-elements test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-04-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Texas v. Cobb",
    "varies_by_point": false,
    "scope_note": "Good law; defines the scope of the Sixth Amendment right by the Blockburger same-elements test.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Fernandes",
          "cluster_id": 9414986,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Handa",
          "cluster_id": 4505766,
          "cite": [
            "892 F.3d 95"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "DUTTON v. CITY OF MIDWEST CITY",
          "cluster_id": 2813680,
          "cite": [
            "2015 OK 51",
            "353 P.3d 532",
            "2015 Okla. LEXIS 75",
            "2015 WL 3998977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in Re Mark Athans, Omar Martinez and Prestige Surgical Assistants, LLC",
          "cluster_id": 2980932,
          "cite": [
            "458 S.W.3d 675",
            "2015 Tex. App. LEXIS 1499",
            "2015 WL 673416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Taylor",
          "cluster_id": 7306221,
          "cite": [
            "17 F. Supp. 3d 162",
            "2014 WL 1653194",
            "2014 U.S. Dist. LEXIS 57397"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basciano",
          "cluster_id": 2470094,
          "cite": [
            "763 F. Supp. 2d 303",
            "2011 U.S. Dist. LEXIS 2901",
            "2011 WL 114865"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tlasek",
          "cluster_id": 6589376,
          "cite": [
            "77 Mass. App. Ct. 298",
            "930 N.E.2d 170",
            "2010 Mass. App. LEXIS 999"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Samuel Constanza Alvarado",
          "cluster_id": 793566,
          "cite": [
            "440 F.3d 191",
            "2006 U.S. App. LEXIS 6055",
            "2006 WL 598152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ronald R. Scarberry v. State of Iowa",
          "cluster_id": 792613,
          "cite": [
            "430 F.3d 956",
            "2005 U.S. App. LEXIS 25648",
            "2005 WL 3159221"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Padilla v. Kentucky",
          "cluster_id": 1723,
          "cite": [
            "176 L. Ed. 2d 284",
            "130 S. Ct. 1473",
            "559 U.S. 356",
            "2010 U.S. LEXIS 2928"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 1476684,
          "cite": [
            "859 A.2d 364",
            "181 N.J. 391",
            "2004 N.J. LEXIS 1080"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": [
            "173 L. Ed. 2d 955",
            "129 S. Ct. 2079",
            "556 U.S. 778",
            "2009 U.S. LEXIS 3973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quiroz",
          "cluster_id": 4282819,
          "cite": [
            "55 M.J. 334",
            "2001 CAAF LEXIS 1020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lotter",
          "cluster_id": 8285182,
          "cite": [
            "917 N.W.2d 850",
            "301 Neb. 125"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 8437415,
          "cite": [
            "327 F.3d 56"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gregory",
          "cluster_id": 2621432,
          "cite": [
            "147 P.3d 1201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. DePriest",
          "cluster_id": 2517841,
          "cite": [
            "163 P.3d 896",
            "63 Cal. Rptr. 3d 896",
            "42 Cal. 4th 1",
            "2007 Cal. LEXIS 8291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thornton",
          "cluster_id": 2552553,
          "cite": [
            "161 P.3d 3",
            "61 Cal. Rptr. 3d 461",
            "41 Cal. 4th 391",
            "2007 Cal. LEXIS 6759"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tommie T. Childs",
          "cluster_id": 776249,
          "cite": [
            "277 F.3d 947",
            "2002 U.S. App. LEXIS 760",
            "2002 WL 63798"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Fayed",
          "cluster_id": 4741522,
          "cite": [
            "9 Cal. 5th 147",
            "260 Cal. Rptr. 3d 761",
            "460 P.3d 1149"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaemmerling v. Lappin",
          "cluster_id": 187263,
          "cite": [
            "553 F.3d 669",
            "384 U.S. App. D.C. 240",
            "2008 U.S. App. LEXIS 26507",
            "2008 WL 5396823"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hitt",
          "cluster_id": 47622,
          "cite": [
            "473 F.3d 146",
            "2006 WL 3616560"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson, Ex Parte Ronald",
          "cluster_id": 2949202,
          "cite": [
            "442 S.W.3d 325",
            "2014 Tex. Crim. App. LEXIS 969",
            "2014 WL 4627231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sapp",
          "cluster_id": 2689898,
          "cite": [
            "2004 Ohio 7008",
            "105 Ohio St. 3d 104",
            "822 N.E.2d 1239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cobb v. State",
          "cluster_id": 1588789,
          "cite": [
            "85 S.W.3d 258",
            "2002 Tex. Crim. App. LEXIS 111",
            "2002 WL 1059741"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warner v. State",
          "cluster_id": 2586068,
          "cite": [
            "2006 OK CR 40",
            "144 P.3d 838",
            "2006 WL 2788641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Trujillo",
          "cluster_id": 2588337,
          "cite": [
            "146 P.3d 1259",
            "51 Cal. Rptr. 3d 718",
            "40 Cal. 4th 165",
            "2006 Daily Journal DAR 16081",
            "2006 Cal. Daily Op. Serv. 11289",
            "2006 Cal. LEXIS 14358"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Toles",
          "cluster_id": 162347,
          "cite": [
            "297 F.3d 959",
            "2002 U.S. App. LEXIS 12481",
            "2002 WL 1365590"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Vasquez",
          "cluster_id": 2484061,
          "cite": [
            "456 Mass. 350",
            "923 N.E.2d 524",
            "2010 Mass. LEXIS 120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pecina, Alfredo Leyva",
          "cluster_id": 2947167,
          "cite": [
            "361 S.W.3d 68",
            "2012 WL 204293",
            "2012 Tex. Crim. App. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mayes",
          "cluster_id": 1440035,
          "cite": [
            "63 S.W.3d 615",
            "2001 Mo. LEXIS 99",
            "2001 WL 1609093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDc2NTQ0MDAwMDAwJnM9Nzg0NDYyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118417+OR+9434063+OR+9434064+OR+9434065%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MCZzPTMwMTM0NzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118417+OR+9434063+OR+9434064+OR+9434065%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 1,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065)",
    "indexed_citing_opinions": 305,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118417,
        "count": 268,
        "count_source": "search"
      },
      {
        "opinion_id": 9434063,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9434064,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434065,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 504,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/texas-v-cobb.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyNzExMTEmcz00ODg3NTY2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118417+OR+9434063+OR+9434064+OR+9434065%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118417,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 108114,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 108987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 109695,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 112622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 112906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 606691,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 734234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 746894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 752877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 1778701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 1960321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2009182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2025446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2239111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2278126,
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
    "date_created": "2026-07-05T21:28:38Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:28:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:28:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:33:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:28:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Texas v. Cobb

```
<opinion type="majority">
<author id="b258-6">Chief Justice Rehnquist</author>
<p id="Aij">delivered the opinion of the Court.</p>
<p id="b258-7">The Texas Court of Criminal Appeals held that a criminal defendant's Sixth Amendment right to counsel attaches not only to the offense with which he is charged, but to other offenses “closely related factually” to the charged offense. We hold that our decision in <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S. 171</a></span> (1991), meant what it said, and that the Sixth Amendment right is “offense specific.”</p>
<p id="b258-8">In December 1993, Lindsey Owings reported to the Walker County, Texas, Sheriff’s Office that the home he <page-number citation-index="1" label="165">*165</page-number>shared with his wife, Margaret, and their 16-month-old daughter, Kori Rae, had been burglarized. He also informed police that his wife and daughter were missing. Respondent Raymond Levi Cobb lived across the street from the Owings. Acting on an anonymous tip that respondent was involved in the burglary, Walker County investigators questioned him about the events. He denied involvement. In July 1994, while under arrest for an unrelated offense, respondent was again questioned about the incident. Respondent then gave a written statement confessing to the burglary, but he denied knowledge relating to the disappearances. Respondent was subsequently indicted for the burglary, and Hal Ridley was appointed in August 1994 to represent respondent on that charge.</p>
<p id="b259-5">Shortly after Ridley’s appointment, investigators asked and received his permission to question respondent about the disappearances. Respondent continued to deny involvement. Investigators repeated this process in September 1995, again with Ridley’s permission and again with the same result.</p>
<p id="b259-6">In November 1995, respondent, free on bond in the burglary ease, was living with his father in Odessa, Texas. At that time, respondent’s father contacted the Walker County Sheriff’s Office to report that respondent had confessed to him that he killed Margaret Owings in the course of the burglary. Walker County investigators directed respondent’s father to the Odessa police station, where he gave a statement. Odessa police then faxed the statement to Walker County, where investigators secured a warrant for respondent’s arrest and faxed it back to Odessa. Shortly thereafter, Odessa police took respondent into custody and administered warnings pursuant to <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span> (1966). Respondent waived these rights.</p>
<p id="b259-7">After a short time, respondent confessed to murdering both Margaret and Kori Rae. Respondent explained that when Margaret confronted him as he was attempting to re<page-number citation-index="1" label="166">*166</page-number>move the Qwings’ stereo, he stabbed her in the stomach with a knife he was carrying. Respondent told police that he dragged her body to a wooded area a few hundred yards from the house. Respondent then stated:</p>
<blockquote id="b260-5">“ ‘I went back to her house and I saw the baby laying on its bed. I took the baby out there and it was sleeping the whole time. I laid the baby down on the ground four or five feet away from its mother. I went back to my house and got a flat edge shovel. That’s all I could find. Then I went back over to where they were and I started digging a hole between them. After I got the hole dug, the baby was awake. It started going toward its mom and it fell in the hole. I put the lady in the hole and I covered them up. I remember stabbing a different knife I had in the ground where they were. I was crying right then.’ ” App. to Pet. for Cert. A-9 to A-10.</blockquote>
<p id="b260-6">Respondent later led police to the location where he had buried the victims’ bodies.</p>
<p id="b260-7">Respondent was convicted of capital murder for murdering more than one person in the course of a single criminal transaction. See <span class="citation no-link">Tex. Penal Code Ann. § 19.03</span>(a)(7)(A) (1994). He was sentenced to death. On appeal to the Court of Criminal Appeals of Texas, respondent argued, <em>inter alia, </em>that his confession should have been suppressed because it was obtained in violation of his Sixth Amendment right to counsel. Relying on <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), respondent contended that his right to counsel had attached when Ridley was appointed in the burglary case and that Odessa police were therefore required to secure Ridley’s permission before proceeding with the interrogation.</p>
<p id="b260-8">The Court of Criminal Appeals reversed respondent’s conviction by a divided vote and remanded for a new trial. The court held that “once the right to counsel attaches to <page-number citation-index="1" label="167">*167</page-number>the offense charged, it also attaches to any other offense that is very closely related factually to the offense charged.” <span class="citation" data-id="9692380"><a href="/opinion/1891478/cobb-v-state/#3" aria-description="Citation for case: Cobb v. State">2000 WL 275644, *3</a></span> (2000) (citations omitted). Finding the capital murder charge to be “factually interwoven with the burglary,” the court concluded that respondent’s Sixth Amendment right to counsel had attached on the capital murder charge even though respondent had not yet been charged with that offense. <em>Id., </em>at *4. The court further found that respondent had asserted that right by accepting Ridley’s appointment in the burglary case. See <em>ibid. </em>Accordingly, it deemed the confession inadmissible and found that its introduction had not been harmless error. See <em>id., </em>at *4-*5. Three judges dissented, finding <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>to be distinguishable and concluding that respondent had made a valid unilateral waiver of his right to counsel before confessing. See 2000 WL, at *5-*13 (opinion of McCormick, P. J.).</p>
<p id="b261-5">The State sought review in this Court, and we granted certiorari to consider first whether the Sixth Amendment right to counsel extends to crimes that are “factually related” to those that have actually been charged, and second whether respondent made a valid unilateral waiver of that right in this case. <span class="citation multiple-matches"><a href="/c/U.%20S./530/1260/">530 U. S. 1260</a></span> (2000). Because we answer the first question in the negative, we do not reach the second.</p>
<p id="b261-6">The Sixth Amendment provides that “[i]n all criminal prosecutions, the aeeused shall enjoy the right... to have the Assistance, of Counsel for his defence.” In <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S. 171</a></span> (1991), we explained when this right arises:</p>
<blockquote id="b261-7">“The Sixth Amendment right [to counsel]... is offense specific. It cannot be invoked once for all future prosecutions, for it does not attach until a prosecution is commenced, that is, at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, in<page-number citation-index="1" label="168">*168</page-number>formation, or arraignment.” <span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#175" aria-description="Citation for case: McNeil v. Wisconsin"><em>Id., </em>at 175</a></span> (citations and internal quotation marks omitted).</blockquote>
<p id="b262-5">Accordingly, we held that a defendant’s statements regarding offenses for which he had not been charged were admissible notwithstanding the attachment of his Sixth Amendment right to counsel on other charged offenses. See <span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#176" aria-description="Citation for case: McNeil v. Wisconsin"><em>id., </em>at 176</a></span>.</p>
<p id="b262-6">Some state courts and Federal Courts of Appeals, however, have read into <em>McNeil’s </em>offense-specific definition an exception for crimes that aré “factually related” to a charged offense.<footnotemark>1</footnotemark> Several of these courts have interpreted <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U.S. 387</a></span> (1977), and <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U.S. 159</a></span> (1985)—both of which were decided well before <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span></em>—to support this view, which respondent now invites us to approve. We decline to do so.</p>
<p id="b262-7">In <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Brewer</a></span>, </em>a suspect in the abduction and murder of a 10-year-old girl had fled from the scene of the erime in Des Moines, Iowa, some 160 miles east to Davenport, Iowa, where he surrendered to police. An arrest warrant was issued in Des Moines on a charge of abduction, and the suspect was arraigned on that warrant before a Davenport judge. Des Moines police traveled to Davenport, took the man into custody, and began the drive back to Des Moines. Along the way, one of the officers persuaded the suspect to lead police to the victim’s body. The suspect ultimately was convicted of the girl’s murder. This Court upheld the federal habeas court’s conclusion that police had violated the suspect’s Sixth Amendment right to counsel. We held that the officer’s comments to the suspect constituted in<page-number citation-index="1" label="169">*169</page-number>terrogation and that the suspect had not validly waived his right to counsel by responding to the officer. See <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#405" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 405-406</a></span>.</p>
<p id="b263-5">Respondent suggests that <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Brewer</a></span> </em>implicitly held that the right to counsel attached to the factually related murder when the suspect was arraigned on the abduction charge. See Brief for Respondent 4. The Court’s opinion, however, simply did not address the significance of the fact that the suspect had been arraigned only on the abduction charge, nor did the parties in any way argue this question. Constitutional rights are not defined by inferences from opinions which did not address the question at issue. Cf. <em>Hagans </em>v. <em>Lavine, </em><span class="citation" data-id="9425636"><a href="/opinion/108987/hagans-v-lavine/#535" aria-description="Citation for case: Hagans v. Lavine">415 U.S. 528, 535, n. 5</a></span> (1974) (“[W]hen questions of jurisdiction have been passed on in prior decisions <em>sub silentio, </em>this Court has never considered itself bound when a subsequent case finally brings the jurisdictional issue before us”).</p>
<p id="b263-6"><em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton</a></span> </em>is similarly unhelpful to respondent. That case involved two individuals indicted for a series of thefts, one of whom had secretly agreed to cooperate with the police investigation of his codefendant, Moulton. At the suggestion of police, the informant recorded several telephone calls and one face-to-face conversation he had with Moulton during which the two discussed their criminal exploits and possible alibis. In the course of those conversations, Moul-ton made various incriminating statements regarding both the thefts for which he had been charged and additional crimes. In a superseding indictment, Moulton was charged with the original crimes as well as burglary, arson, and three additional thefts. At trial, the State introduced portions of the recorded face-to-face conversation, and Moulton ultimately was convicted of three of the originally charged thefts plus one count of burglary. Moulton appealed his convictions to the Supreme Judicial Court of Maine, arguing that introduction of the recorded conversation violated <page-number citation-index="1" label="170">*170</page-number>his Sixth Amendment right to counsel. That court agreed, holding;</p>
<blockquote id="b264-5">“‘Those statements may be admissible in the investigation or prosecution of charges for which, at the time the recordings were made, adversary proceedings had not yet commenced. But as to the charges for which Moul-ton’s right to counsel had already attached, his incriminating statements should have been ruled inadmissible at trial, given the circumstances in which they were acquired.’ ” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 168</a></span> (quoting <em>State </em>v. Moulton, <span class="citation" data-id="2009182"><a href="/opinion/2009182/state-v-moulton/#161" aria-description="Citation for case: State v. Moulton">481 A. 2d 155, 161</a></span> (1984)).</blockquote>
<p id="b264-6">We affirmed.</p>
<p id="b264-7">Respondent contends that, in affirming reversal of both the theft and burglary charges, the <em>Moulton </em>Court must have concluded that Moulton’s Sixth Amendment right to counsel attached to the burglary charge. See Brief for Respondent 13-14; see also Brief for the National Association of Criminal Defense Lawyers et al. as <em>Amici Curiae </em>22-23. But the <em>Moulton </em>Court did not address the question now before us, and to the extent <em>Moulton </em>spoke to the matter at all, it expressly referred to the offense-specific nature of the Sixth Amendment right to counsel:</p>
<blockquote id="b264-8">“The police have an interest in the thorough investigation of crimes for which <em>formal charges </em>have already been filed. They also have an interest in investigating new or additional crimes. Investigations of either type of crime may require surveillance of individuals already under indictment. Moreover, law enforcement officials investigating an individual suspected of committing one crime and <em>formally charged </em>with having committed another crime obviously seek to discover evidence useful at a trial of either crime. In seeking evidence pertaining to <em>'pending charges, </em>however, the Government’s investigative powers are limited by the Sixth Amendment rights of the accused.... On the other hand, to exclude <page-number citation-index="1" label="171">*171</page-number>evidence pertaining to charges as to which the Sixth Amendment right to counsel had not attached at the time the evidence was obtained, simply because other charges were pending at that time, would unnecessarily frustrate the public’s interest in the investigation of criminal activities'.” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#179" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 179-180</a></span> (emphasis added; footnote omitted).</blockquote>
<p id="b265-5">See also <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#168" aria-description="Citation for case: Maine v. Moulton"><em>id., </em>at 168</a></span> (“[T]he purpose of their meeting was to discuss the <em>pending charges”); id., </em>at 177 (“[T]he police knew... that Moulton and [the informant] were meeting for the express purpose of discussing the <em>pending charges </em>...” (emphasis added)). Thus, respondent’s reliance on <em>Moulton </em>is misplaced and, in light of the language employed there and subsequently in <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span>, </em>puzzling.</p>
<p id="b265-6">Respondent predicts that the offense-specific rule will prove “disastrous” to suspects’ constitutional rights and will “permit law enforcement officers almost complete and total license to conduct unwanted and uncounseled interrogations.” Brief for Respondent 8-9. Besides offering no evidence that such a parade of horribles has occurred in those jurisdictions that have not enlarged upon <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span>, </em>he fails to appreciate the significance of two critical considerations. First, there can be no doubt that a suspect must be apprised of his rights against compulsory self-incrimination and to consult with an attorney before authorities may conduct custodial interrogation. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>; <em>Dickerson </em>v. <em>United States, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States">530 U.S. 428, 435</a></span> (2000) (quoting Miranda.). In the present ease, police scrupulously followed <em>Miranda’s, </em>dictates when questioning respondent.<footnotemark>2</footnotemark> Second, it is critical to recognize that the Con<page-number citation-index="1" label="172">*172</page-number>stitution does not negate society’s interest in the ability of police to talk to witnesses and suspects, even those who have been charged with other offenses.</p>
<blockquote id="b266-5">“Since the ready ability to obtain uncoereed confessions is not an evil but an unmitigated good, society would be the loser. Admissions of guilt resulting from valid <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waivers ‘are more than merely “desirable”; they are essential to society’s compelling interest in finding, convicting, and punishing those who violate the law.’ ” <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span>, </em>501U. S., at 181 (quoting <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 426</a></span> (1986)).</blockquote>
<p id="b266-6">See also <em>Moulton, supra, </em>at 180 (“[T]o exclude evidence pertaining to charges as to which the Sixth Amendment right to counsel had not attached at the time the evidence was obtained, simply because other charges were pending at that time, would unnecessarily frustrate the public’s interest in the investigation of criminal activities”).</p>
<p id="b266-7">Although it is clear that the Sixth Amendment right to counsel attaches only to charged offenses, we have reeog-<page-number citation-index="1" label="173">*173</page-number>nized in other contexts that the definition of an “offense” is not necessarily limited to the four corners of a charging instrument. In <em>Blockburger </em>v. <em>United States, </em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">284 U. S. 299</a></span> (1932), we explained that “where the same act or transaction constitutes a violation of two distinct statutory provisions, the test to be applied to determine whether there are two offenses or only one, is whether each provision requires proof of a fact which the other does not.” <span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/#304" aria-description="Citation for case: Blockburger v. United States"><em>Id., </em>at 304</a></span>. We have since applied the <em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">Blockburger</a></span> </em>test to delineate the scope of the Fifth Amendment’s Double Jeopardy Clause, which prevents multiple or successive prosecutions for the “same offence.” See, <em>e. g., Brown </em>v. <em>Ohio, </em><span class="citation" data-id="9426874"><a href="/opinion/109695/brown-v-ohio/#164" aria-description="Citation for case: Brown v. Ohio">432 U. S. 161, 164-166</a></span> (1977). We see no constitutional difference between the meaning of the term “offense” in the contexts of double jeopardy and of the right to counsel. Accordingly, we hold that when the Sixth Amendment right to counsel attaches, it does encompass offenses that, even if not formally charged, would be considered the same offense under the <em>Block-burger </em>test.<footnotemark>3</footnotemark></p>
<p id="b267-5">While simultaneously conceding that its own test “lacks the precision for which police officers may hope,” <em>post, </em>at 186, the dissent suggests that adopting Blockburger’s definition of “offense” will prove difficult to administer. But it is the dissent’s vague iterations of the “ ‘closely related to’ ” or “‘inextricably intertwined with’” test, <em>post, </em>at 186, that would defy simple application. The dissent seems to presuppose that officers will possess complete knowledge of the circumstances surrounding an incident, such that the officers will be able to tailor their investigation to avoid addressing factually related offenses. Such an assumption, however, ignores the reality that police often are not yet aware of the <page-number citation-index="1" label="174">*174</page-number>exact sequence and scope of events they are investigating— indeed, that is why police must investigate in the first place. Deterred by the possibility of violating the Sixth Amendment, police likely would refrain from questioning certain defendants altogether.</p>
<p id="b268-5">It remains only to apply these principles to the facts at hand. At the time he confessed to Odessa police, respondent had been indicted for burglary of the Owings residence, but he had not been charged in the murders of Margaret and Kori Rae. As defined by Texas law, burglary and capital murder are not the same offense under <em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">Blockburger</a></span>. </em>Compare <span class="citation no-link">Tex. Penal Code Ann. § 30.02</span>(a) (1994) (requiring entry into or continued concealment in a habitation or building) with § 19.03(a)(7)(A) (requiring murder of more than one person during a single criminal transaction). Accordingly, the Sixth Amendment right to counsel did not bar police from interrogating respondent regarding the murders, and respondent’s confession was therefore admissible.</p>
<p id="b268-6">The judgment of the Court of Criminal Appeals of Texas is reversed.</p>
<p id="b268-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b262-8"> See, <em>e.g., United States </em>v. <em>Covarrubias, 179 </em>F. 3d 1219, 1223-1224 (CA9 1999); <em>United States </em>v. <em>Melgar, </em><span class="citation" data-id="752877"><a href="/opinion/752877/united-states-v-jose-aldalberto-melgar-aka-jose-aldalberto/#1013" aria-description="Citation for case: United States v. Jose Aldalberto Melgar, A/K/A Jose...">139 F. 3d 1005, 1013</a></span> (CA4 1998); <em>United States </em>v. <em>Doherty, </em><span class="citation" data-id="9490677"><a href="/opinion/746894/united-states-v-ross-allen-doherty/#776" aria-description="Citation for case: United States v. Ross Allen Doherty">126 F. 3d 769, 776</a></span> (CA6 1997); <em>United States </em>v. <em>Arnold, </em><span class="citation" data-id="9489990"><a href="/opinion/734234/united-states-v-dean-martin-arnold/#41" aria-description="Citation for case: United States v. Dean Martin Arnold">106 F. 3d 37, 41</a></span> (CA3 1997); <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="606691"><a href="/opinion/606691/united-states-v-frankie-b-williams/#457" aria-description="Citation for case: United States v. Frankie B. Williams">993 F. 2d 451, 457</a></span> (CA5 1993); <em>Commonwealth </em>v. <em>Rainwater, </em><span class="citation" data-id="6451287"><a href="/opinion/6577408/commonwealth-v-rainwater/#556" aria-description="Citation for case: Commonwealth v. Rainwater">425 Mass. 540,556</a></span>, <span class="citation" data-id="6451287"><a href="/opinion/6577408/commonwealth-v-rainwater/#1229" aria-description="Citation for case: Commonwealth v. Rainwater">681 N. E. 2d 1218, 1229</a></span> (1997); <em>In re Pack, </em><span class="citation" data-id="2278126"><a href="/opinion/2278126/in-re-the-interest-of-pack/#354" aria-description="Citation for case: In Re the Interest of Pack">420 Pa. Super. 347, 354-356</a></span>, <span class="citation" data-id="2278126"><a href="/opinion/2278126/in-re-the-interest-of-pack/#1010" aria-description="Citation for case: In Re the Interest of Pack">616 A. 2d 1006,1010-1011</a></span> (1992).</p>
</footnote>
<footnote label="2">
<p id="b265-7"> Curiously, while predicting disastrous consequences for the core values underlying the Sixth Amendment, see <em>post, </em>at 179-183 (opinion of Breyek, J.), the dissenters give short shrift to the Fifth Amendment’s role (as expressed in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em>Dickerson) </em>in protecting a defendant’s right to consult with counsel before talking to police. Even though the Sixth Amendment right to counsel has not attached to uncharged offenses, <page-number citation-index="1" label="172">*172</page-number>defendants retain the ability under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to refuse any police questioning, and, indeed, charged defendants presumably have met with counsel and have had the opportunity to discuss whether it is advisable to invoke those Fifth Amendment rights. Thus, in all but the rarest of cases, the Court’s decision today will have no impact whatsoever upon a defendant’s ability to protect his Sixth Amendment right.</p>
<p id="b266-9">It is also worth noting that, contrary to the dissent’s suggestion, see <em>post, </em>at 177-178, 179, there is no “background principle” of our Sixth Amendment jurisprudence establishing that there may be no contact between a defendant and police without counsel present. The dissent would expand the Sixth Amendment right to the assistance of counsel in a criminal prosecution into a rule which “‘exists to prevent lawyers from taking advantage of uncounseled laypersons and to preserve the integrity of the lawyer-client relationship.’ ” <em>Post, </em>at 181 (quoting ABA Aim. Model Rule of Profesional Conduct 4.2 (4th ed. 1999)). Every profession is competent to define the standards of conduct for its members, but such standards are obviously not controlling in interpretation of constitutional provisions. The Sixth Amendment right to counsel is personal to the defendant and specific to the offense.</p>
</footnote>
<footnote label="3">
<p id="b267-6"> In this sense, we could just as easily describe the Sixth Amendment as “prosecution specific,” insofar as it prevents discussion of charged offenses as well as offenses that, under <em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">Blockburger</a></span>, </em>could not be the subject of a later prosecution. And, indeed, the text of the Sixth Amendment confines its scope to “all criminal <em>prosecutions.”</em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/The GEO Group, Inc. v. Menocal.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: "The GEO Group, Inc. v. Menocal"
type: case
citation: "No. 24-758, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 24-758
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
  opinion_url: "https://www.courtlistener.com/opinion/10800194/geo-group-inc-v-menocal/"
  cluster_id: 10800194
  opinion_id: null
  identity_checked: false
lake:
  record_id: "The GEO Group, Inc. v. Menocal"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - federal-contractor
  - yearsley
  - collateral-order
  - appellate-jurisdiction
  - derivative-immunity
  - supreme-court
holding: "Because the Yearsley doctrine gives a federal contractor a potential merits defense rather than an immunity from suit, a district court order denying Yearsley protection is not immediately appealable under the collateral-order doctrine; it neither resolves an issue separate from the merits nor is effectively unreviewable after final judgment."
aliases:
  - "The GEO Group, Inc. v. Menocal"
  - "GEO Group, Inc. v. Menocal"
  - GEO Group v. Menocal
---

# The GEO Group, Inc. v. Menocal

*No. 24-758, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10800194 → majority opinion 11266870 (No. 24-758, decided Feb. 25, 2026). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (current-Term slip opinion, no reporter cite assigned — S2 A3). S9 promotes. -->

## Background
GEO Group operates a private immigration-detention facility in Aurora, Colorado, under contract with U.S. Immigration and Customs Enforcement (ICE). Former detainee Alejandro Menocal brought a class action alleging GEO's detainee work policies violated a federal forced-labor bar and Colorado's unjust-enrichment law. GEO argued the suit was barred by *Yearsley v. W.A. Ross Construction Co.*, which shields a federal contractor from liability for conduct the Government lawfully "authorized and directed." The district court held the contract did not direct the challenged policies and that a trial was necessary; the Tenth Circuit dismissed GEO's immediate appeal for lack of jurisdiction.

## Issue
Whether a district court order denying a federal contractor's *Yearsley* defense is immediately appealable under the collateral-order doctrine.

## Rule
The courts of appeals may hear appeals only from "final decisions," 28 U.S.C. § 1291, subject to a narrow collateral-order exception for rulings that (1) conclusively determine the disputed question, (2) resolve an important issue completely separate from the merits, and (3) are effectively unreviewable on appeal from a final judgment. The Court held: "Because *Yearsley* provides federal contractors a potential merits defense rather than an immunity from suit, a pretrial order denying *Yearsley* protection is not immediately appealable." — slip op. at 1. ^pin-slip1

## Application
Unlike qualified or sovereign immunity — which confer a right *not to stand trial* and so justify immediate review — *Yearsley* supplies only a defense to liability on the merits. An order rejecting it therefore does not resolve a question "completely separate from the merits," and any error can be corrected on appeal from final judgment; the ruling flunks the collateral-order test. The interest in avoiding piecemeal appeals controls.

## Conclusion
**Affirmed.** Justice Kagan wrote for a unanimous Court (9–0); the Tenth Circuit's dismissal for lack of jurisdiction was upheld.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *GEO Group* sharpens the line between an "immunity from suit" (immediately appealable, like [[Qualified Immunity|qualified immunity]] in § 1983 litigation) and a mere "merits defense" (not appealable until final judgment), classifying *Yearsley* federal-contractor protection as the latter.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Geo Group, Inc. v. Menocal*, No. 24-758, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10800194/geo-group-inc-v-menocal/) — pinpoint: slip op. at 1 (Yearsley is a merits defense, not an appealable immunity). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c4dc5fa2a0d3f540", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "The GEO Group, Inc. v. Menocal"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "The GEO Group, Inc. v. Menocal", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — The GEO Group, Inc. v. Menocal

```json
{
  "schema_version": "s2.v1",
  "record_id": "The GEO Group, Inc. v. Menocal",
  "status": "under_review",
  "identity": {
    "case_name": "Geo Group, Inc. v. Menocal",
    "case_name_short": "Menocal",
    "case_name_full": "",
    "input_case_name": "The GEO Group, Inc. v. Menocal",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "24-758",
    "cluster_id": 10800194,
    "lead_opinion_id": 11266870,
    "sibling_ids": [],
    "absolute_url": "/opinion/10800194/geo-group-inc-v-menocal/",
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
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "SCOTUS No. 24-758, decided 2026-02-25 (607 U.S. ___; Kagan, 9-0). No S. Ct. page yet.",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/24-758",
          "cite": "No. 24-758, decided 2026-02-25"
        },
        {
          "source": "Justia",
          "url": "https://supreme.justia.com/cases/federal/us/607/24-758/",
          "cite": "607 U.S. ___ (2026) placeholder"
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
    "date_created": "2026-07-06T12:13:28Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "the-geo-group-inc-v-menocal--10800194",
      "to_record_id": "The GEO Group, Inc. v. Menocal",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — The GEO Group, Inc. v. Menocal

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

             GEO GROUP, INC. v. MENOCAL ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE TENTH CIRCUIT

 No. 24–758.      Argued November 10, 2025—Decided February 25, 2026


Petitioner GEO Group operates a private detention facility in Aurora,
  Colorado, under a contract with U. S. Immigration and Customs En-
  forcement (ICE). Respondent Alejandro Menocal, a former detainee at
  the Aurora facility, initiated this class action, alleging GEO’s work pol-
  icies for detainees violate a federal bar on forced labor and Colorado’s
  prohibition on unjust enrichment. GEO responded that the suit must
  be dismissed under Yearsley v. W. A. Ross Constr. Co., 309 U. S. 18,
  which held that a federal contractor cannot be held liable for conduct
  that the Government has lawfully “authorized and directed” the con-
  tractor to perform. Id., at 20–21. GEO argued that ICE had author-
  ized and directed it to carry out the challenged labor policies. But the
  District Court did not read GEO’s contract with the Government to
  instruct GEO to adopt those policies. The District Court thus con-
  cluded that the Yearsley doctrine did not relieve GEO of legal respon-
  sibility and a trial would be necessary. GEO immediately filed an ap-
  peal, which the Court of Appeals for the Tenth Circuit dismissed for
  lack of jurisdiction, holding that an order denying Yearsley protection
  does not qualify for interlocutory review under Cohen v. Beneficial In-
  dustrial Loan Corp., 337 U. S. 541.
Held: Because Yearsley provides federal contractors a potential merits
 defense rather than an immunity from suit, a pretrial order denying
 Yearsley protection is not immediately appealable. Pp. 3–12.
    (a) The courts of appeals have jurisdiction over appeals from “final
 decisions of the district courts.” 28 U. S. C. §1291. A decision gener-
 ally is “final” only when it “resolves the entire case”—when it “ends the
 litigation” on the merits or otherwise. Ritzen Group, Inc. v. Jackson
2                     GEO GROUP, INC. v. MENOCAL

                                    Syllabus

    Masonry, LLC, 589 U. S. 35, 37–38. That final-judgment rule, by pre-
    venting piecemeal appeals, “promotes the efficient administration of
    justice” and “preserves the proper balance between trial and appellate
    courts.” Microsoft Corp. v. Baker, 582 U. S. 23, 36–37.
       Under the collateral-order doctrine, however, a “small class” of deci-
    sions are treated as “final”—and thus immediately appealable—even
    though they do not end a case. Cohen, 337 U. S., at 546. To get imme-
    diate review, a prejudgment order must satisfy the three conditions
    this Court has “distilled” from Cohen. Will v. Hallock, 546 U. S. 345,
    349. The order must “(1) conclusively determine the disputed question,
    (2) resolve an important issue completely separate from the merits of
    the action, and (3) be effectively unreviewable on appeal from a final
    judgment.” Van Cauwenberghe v. Biard, 486 U. S. 517, 522.
       Whether the denial of a pretrial request to dismiss a case like the
    one here can satisfy Cohen’s third condition will generally turn on
    whether the defendant has asserted a defense to liability or instead an
    immunity from suit. A party asserting a merits defense advances some
    reason why his conduct was not unlawful and he should not be found
    liable. But a party asserting an immunity need not challenge the mer-
    its of the charge against him: his claim of immunity does not turn on
    his conduct’s legality. That difference entails another. Because it en-
    sures a defendant need not “answer for his conduct” in court at all, an
    immunity is in its “essence” an “entitlement not to stand trial.” Mitch-
    ell v. Forsyth, 472 U. S. 511, 525–526. A liability defense, by contrast,
    does not allow the defendant to escape legal proceedings, because it is
    through them that the asserted defense is addressed and liability fi-
    nally determined. And that divergence matters for Cohen’s third con-
    dition, which requires that the order involve a right that “would be
    irretrievably lost absent an immediate appeal.” Van Cauwenberghe,
    486 U. S., at 524. The right not to stand trial is irretrievably lost once
    trial occurs, but the right to a finding of non-liability can be effectively
    vindicated after trial, through reversal of an adverse final judgment.
    So, if a defendant asserts a liability defense, Cohen is likely to block an
    immediate appeal; if he asserts an immunity, Cohen will likely allow
    it. Pp. 3–7.
       (b) Does Yearsley offer federal contractors a merits defense or in-
    stead an immunity? Menocal says a defense, because Yearsley gives
    contractors only a way to show that their conduct complied with the
    law. GEO says an immunity—more specifically, “derivative sovereign
    immunity”—where the Government’s own immunity extends to con-
    tractors who meet specified conditions. Brief for GEO 15.
       Yearsley provides a potential defense to liability, not an immunity
    from suit. In Yearsley, the Court held that a contractor that had
    flooded the Yearsleys’ property while performing work “authorized and
                       Cite as: 607 U. S. ___ (2026)                       3

                                 Syllabus

  directed by the Government” was not liable to the landowner. 309
  U.S., at 20. The Court explained that a contractor acting as an agent
  of the Government could be held liable for injurious conduct in only
  two circumstances: when “he exceeded his authority” or when that au-
  thority “was not validly conferred.” Id., at 21. The Court found neither
  circumstance obtained in Yearsley, because the contractor received a
  lawful authorization and stayed within the bounds of the authority
  given. That reasoning describes a defense, not an immunity: Years-
  ley’s protection runs out when the contractor may have violated the
  law—when the contractor either acted under an illegal authorization
  or exceeded the scope of a legal one. Yearsley thus ensures that it will
  never shield unlawful conduct, in the way that all immunities do.
     GEO’s contrary view—that it enjoys “derivative sovereign immun-
  ity”—would put Yearsley in conflict with the general rule that sover-
  eign immunity is not transferrable to government agents. The Court
  has repeatedly held that the Government’s immunity from suit “does
  not extend to those that act[ ] in its name,” Sloan Shipyards Corp. v.
  United States Shipping Bd. Emergency Fleet Corporation, 258 U. S.
  549, 568, or do its work, Keifer & Keifer v. Reconstruction Finance Cor-
  poration, 306 U. S. 381, 388, including by “reason of a contract” with
  the Government, Brady v. Roosevelt S. S. Co., 317 U. S. 575, 583; see
  also Hopkins v. Clemson, 221 U. S. 636, 642–643. The whole thrust of
  those decisions is to deny that government agents can assert—whether
  always or sometimes—a “derived” form of sovereign immunity. In-
  stead, sovereign immunity belongs alone to the Government. Pp. 7–
  11.
     (c) Once Yearsley is properly understood as a merits defense, the
  question before the Court almost answers itself. Like the denial of
  other defenses, a district court’s denial of Yearsley protection is not im-
  mediately appealable under §1291. Such a ruling is not, as Cohen’s
  third condition demands, “effectively unreviewable on appeal from a
  final judgment.” Van Cauwenberghe, 486 U. S., at 522. The right that
  a merits defense affords is to a finding of non-liability. And that
  right—unlike the right not to stand trial—is fully vindicable on appeal
  from a final judgment. Accordingly, the finality rule of §1291 precludes
  interlocutory review of a Yearsley denial. Pp. 11–12.
Affirmed and remanded.

KAGAN, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SOTOMAYOR, GORSUCH, KAVANAUGH, BARRETT, and JACKSON, JJ.,
joined, and in which THOMAS, J., joined as to Parts I and III. THOMAS, J.,
filed an opinion concurring in part and concurring in the judgment.
ALITO, J., filed an opinion concurring in the judgment.
                        Cite as: 607 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 24–758
                                   _________________


THE GEO GROUP, INC., PETITIONER v. ALEJANDRO
             MENOCAL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                              [February 25, 2026]

  JUSTICE KAGAN delivered the opinion of the Court.
  In Yearsley v. W. A. Ross Constr. Co., 309 U. S. 18, 20
(1940), this Court held that a federal contractor cannot be
held liable for conduct that the Government has lawfully
“authorized and directed” the contractor to perform. Ra-
ther, liability may attach only if the authorization was un-
lawful or if the contractor acted outside its scope. See id.,
at 20–21.
  The question here is whether a contractor may take an
immediate appeal of a district court’s pretrial order denying
Yearsley protection. The answer is no. Because Yearsley
provides a defense to liability, not an immunity from suit,
an order denying its protection can be effectively reviewed
after a final judgment. So appellate review of such an or-
der, as of most pretrial rulings, must await completion of
the district court’s proceedings.
                            I
   Petitioner GEO Group operates a private detention facil-
ity in Aurora, Colorado, under a contract with U. S. Immi-
gration and Customs Enforcement (ICE). The facility holds
individuals whose immigration proceedings are pending.
2               GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

Respondent Alejandro Menocal was detained there in 2014.
Soon afterward, he initiated this class action on behalf of
the Aurora facility’s detainees.
   The suit challenges two policies GEO used to put the de-
tainees to work, thereby reducing its own labor costs. First,
the so-called Sanitation Policy required detainees to clean,
without any pay, all the facility’s common areas. A de-
tainee’s failure to perform his assigned tasks led to escalat-
ing sanctions, up to 72 hours in solitary confinement. Sec-
ond, the so-called Voluntary Work Program offered $1 per
day to detainees for other kinds of needed work, such as
preparing food and doing laundry. Menocal’s complaint al-
leged that the former policy violated a federal bar on forced
labor and that the latter breached Colorado’s prohibition on
unjust enrichment.
   Following discovery, the District Court addressed GEO’s
contention that Yearsley required the suit’s dismissal. That
was so, the argument ran, because ICE had by contract “au-
thorized and directed” GEO to carry out the two challenged
policies. Defendant’s Cross-Motion for Summary Judgt. in
No. 14–2887 (D Colo., June 25, 2020), ECF Doc. 284, p. 17.
But the District Court did not read the government contract
that way. Nothing in its terms, the court found, instructed
GEO to adopt the work rules at issue. Rather, in “inde-
pendently develop[ing] and implement[ing]” those rules,
GEO “far exceeded its contractual obligations.”           635
F. Supp. 3d 1151, 1173 (Colo. 2022). So the Yearsley doc-
trine, the District Court concluded, did not relieve GEO of
legal responsibility. Instead, a trial would be necessary to
address whether GEO’s policies violated the referenced
bans on forced labor or unjust enrichment.
   GEO immediately filed an appeal, but the Court of Ap-
peals for the Tenth Circuit dismissed it for lack of jurisdic-
tion. See 2024 WL 4544184 (Oct. 22, 2024). Appellate ju-
risdiction, the court explained, seldom extends to an order
that does not terminate the litigation at issue. Such an
                  Cite as: 607 U. S. ____ (2026)             3

                      Opinion of the Court

order qualifies for interlocutory review only if it satisfies
three conditions deriving from this Court’s decision in Co-
hen v. Beneficial Industrial Loan Corp., 337 U. S. 541
(1949). And an order denying Yearsley protection, the
Tenth Circuit held, does not do so. The court saw no need
to address the first or third Cohen conditions because it con-
cluded that a Yearsley denial flunked the second: Such a
ruling is not (as Cohen demands) “completely separate from
the merits” of the suit. 2024 WL 4544184, *7. That is be-
cause, the court reasoned, an inquiry into what the Govern-
ment instructed the contractor to do is relevant to both
Yearsley’s application and the “lawfulness of the contrac-
tor’s challenged actions.” Id., at *8.
  We granted certiorari, 605 U. S. 968 (2025), to resolve
whether a pretrial order denying Yearsley protection to a
government contractor is immediately appealable. Like the
Tenth Circuit, we hold that it is not. But unlike the Tenth
Circuit, we focus on the third Cohen condition, which re-
quires an order to be effectively unreviewable on appeal
from a final judgment.
                               II
   “Finality as a condition of review is an historic character-
istic of federal appellate procedure.” Cobbledick v. United
States, 309 U. S. 323, 324 (1940). Originating in the First
Judiciary Act of 1789, the finality requirement is now codi-
fied in 28 U. S. C. §1291. The courts of appeals, that section
provides, have jurisdiction over appeals from “final deci-
sions of the district courts.” And a decision generally is “fi-
nal” under §1291 only when it “resolves the entire case”—
when it “ends the litigation” (on the merits or otherwise)
and “leaves nothing for the court to do but execute the judg-
ment.” Ritzen Group, Inc. v. Jackson Masonry, LLC, 589
U. S. 35, 37–38 (2020). That final-judgment rule, by pre-
venting piecemeal appeals, “promotes the efficient admin-
istration of justice” and “preserves the proper balance
4               GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

between trial and appellate courts.” Microsoft Corp. v.
Baker, 582 U. S. 23, 36–37 (2017).
   For a “small class” of decisions, however, the finality rule
gives ground and allows interlocutory appeals. Cohen, 337
U. S., at 546. Section 1291, we have often explained, re-
quires a “practical rather than a technical construction,”
and thus may treat as “final” certain decisions that do not
end a case. Mohawk Industries, Inc. v. Carpenter, 558 U. S.
100, 106 (2009) (quoting Cohen, 337 U. S., at 546). We iden-
tify those decisions by category, not case-specific circum-
stances. See Mohawk, 558 U. S., at 107. And we erect a
high bar. A non-terminal order may be appealed, Cohen
held, only if it “finally determine[s] claims of right separa-
ble from, and collateral to, rights asserted in the action, too
important to be denied review and too independent of the
cause itself to require that appellate consideration be de-
ferred.” 337 U. S., at 546. That so-called collateral-order
doctrine, we have since underscored, is “narrow,” “strin-
gent,” and of “modest scope.” Digital Equipment Corp. v.
Desktop Direct, Inc., 511 U. S. 863, 868 (1994); Will v. Hal-
lock, 546 U. S. 345, 350 (2006).
   To keep it that way, this Court has “distilled” the Cohen
ruling into three non-negotiable conditions. Will, 546 U. S.,
at 349. A pre-judgment order, to get immediate review,
must “(1) conclusively determine the disputed question, (2)
resolve an important issue completely separate from the
merits of the action, and (3) be effectively unreviewable on
appeal from a final judgment.” Van Cauwenberghe v.
Biard, 486 U. S. 517, 522 (1988). Failure on any component
of that three-part test is fatal.
   When, as here, an order denies a pretrial request to dis-
miss, appealability under Cohen will generally turn on
whether the defendant has asserted a defense to liability or
instead an immunity from suit. See Mitchell v. Forsyth, 472
U. S. 511, 526–527 (1985). If a defense, Cohen is likely to
block an immediate appeal; if an immunity, Cohen will
                      Cite as: 607 U. S. ____ (2026)                     5

                          Opinion of the Court

likely allow it. To show why, we describe below the differ-
ence between a merits defense and an immunity; what that
difference entails for the right to avoid trial; and how that
right matters in applying the third Cohen condition. Once
that is done, it becomes clear why, as later described, the
parties here mainly contest whether Yearsley offers an im-
munity or just a merits defense. See infra, at 7–8.1
   To start, a party asserting a merits defense in a lawsuit
makes a fundamentally different kind of argument than a
party asserting an immunity. The former advances some
reason why his conduct was not unlawful—or said other-
wise, why under the law he did nothing wrong. And so, that
defendant says, he should not be found liable: Because he
obeyed the law, he should not, for example, have to pay
damages. By contrast, a party asserting an immunity
“makes no challenge” to “the merits of the charge against
him.” Abney v. United States, 431 U. S. 651, 659 (1977).
That defendant need never say he followed the law, because
his claim of immunity does not turn on his conduct’s legal-
ity. “[A]n immunity frees one who enjoys it from a lawsuit
whether or not he acted wrongly.” Richardson v. McKnight,
521 U. S. 399, 403 (1997). A classic example is sovereign
immunity: It shields the Government from suit (absent a
waiver) regardless whether the Government violated the
law. See, e.g., FDIC v. Meyer, 510 U. S. 471, 475 (1994).2
——————
  1 Note that one category of cases exists outside this dichotomy: a non-

merits-based defense that also is not an immunity. On occasion, this
Court has decided that a defense, although barring suit irrespective of
the merits, still fails to qualify as an immunity because it does not serve
sufficiently “weighty public objective[s].” Will v. Hallock, 546 U. S. 345,
353 (2006) (so holding with respect to the Federal Tort Claims Act’s judg-
ment bar). That “public interest” wrinkle, however, never arises if the
defense is on the merits—which, as we will explain, is the case here.
  2 Qualified immunity is, in the respect relevant here, the same. That

doctrine shields a defendant even when the claim against him “in fact
has merit”—or otherwise said, even when he violated the law—so long
as the law at that time was not “clearly established.” Camreta v. Greene,
6                 GEO GROUP, INC. v. MENOCAL

                         Opinion of the Court

   That difference between a merits defense and an immun-
ity entails another: The latter, but not the former, is in its
“essence” an “entitlement not to stand trial.” Mitchell, 472
U. S., at 525. Because an immunity applies irrespective of
the merits, the protection it offers is not a simple finding of
non-liability. Rather, the immunity ensures that the de-
fendant need not “answer for his conduct” in court at all—
that he avoids, in addition to liability, all the usual “bur-
dens of litigation,” including a trial. Id., at 525–526. And
so we typically describe the protection in just that way: as
an immunity “from suit.” Id., at 526 (emphasis in original);
see, e.g., Thacker v. TVA, 587 U. S. 218, 221 (2019); Jam v.
International Finance Corp., 586 U. S. 199, 202 (2019). A
“mere defense” to liability, as we have noted, offers some-
thing different, and of lesser value. Mitchell, 472 U. S., at
526. Because it establishes that the defendant acted law-
fully, a valid defense leads to a judgment of non-liability.
But it does not allow the defendant to escape the varied ri-
gors and costs of legal proceedings. Indeed, it is in and
through those proceedings that the asserted defense is ad-
dressed and liability finally determined.
   And that divergence—in whether the defendant pos-
sesses a right not to stand trial—matters for the third Co-
hen condition. Again, that condition states that a non-ter-
minal order may be appealed when issued only if it is
“effectively unreviewable on appeal from a final judgment.”
Van Cauwenberghe, 486 U. S., at 522; see supra, at 4. For
that to be true, we have explained, the order must involve
a right that “would be irretrievably lost absent an immedi-
ate appeal.” Van Cauwenberghe, 486 U. S., at 524. The
right to avoid trial fits that description. It is irretrievably
lost once trial occurs, even supposing the defendant were to

——————
563 U. S. 692, 705 (2011). “Like other forms of immunity,” then, quali-
fied immunity offers protection “even when [the defendant] acts unlaw-
fully.” Brief for United States as Amicus Curiae 23.
                      Cite as: 607 U. S. ____ (2026)                        7

                           Opinion of the Court

prevail on the merits. And so, in the ordinary case, the de-
nial of an immunity is immediately appealable. See ibid.;
Abney, 431 U. S., at 659–660. But the right to a finding of
non-liability stands on a different footing: It can be effec-
tively vindicated after a trial has occurred, through the re-
versal of an adverse final judgment. And so the denial of a
merits defense is generally appealable only once trial-court
proceedings have ended. See Van Cauwenberghe, 486 U. S.,
at 524; Mitchell, 472 U. S., at 526.
   In short, then, distinguishing between a merits defense
and an immunity from suit, in the way described above, of-
fers a ready way of determining whether the denial of a re-
quest to dismiss a case can satisfy Cohen’s third condition
for interlocutory review.3
                           III
 For just that reason, the parties here mainly dispute
whether our Yearsley decision offers federal contractors a
——————
   3 By the same token, that distinction is likely to determine whether the

other two Cohen conditions are met, though we need not here address
the reasons in any detail. See Puerto Rico Aqueduct and Sewer Authority
v. Metcalf & Eddy, Inc., 506 U. S. 139, 144 (1993) (“Once it is established
that” a State is “immune from suit in federal court, it follows that the
elements of the Cohen collateral order doctrine are satisfied”). Recall
that Cohen’s second condition, on which the Court of Appeals relied, de-
mands that the order “resolve an important issue completely separate
from the merits of the action.” Van Cauwenberghe v. Biard, 486 U. S.
517, 522 (1988); see supra, at 4. A decision on a defense, addressing the
legality of the defendant’s conduct, goes directly to the suit’s merits—
whereas a decision on an immunity, applying regardless of that conduct’s
legality, does not. Similarly for the first condition, which is that the or-
der “conclusively determine the disputed question.” Van Cauwenberghe,
486 U. S., at 522. When a defense turns on contested facts, as is often
true, a pretrial order denying it functions only to defer its resolution until
trial. By contrast, we have held, a pretrial denial of an immunity always
acts as a “fully consummated decision” because nothing can then happen
to avert “the trial the defendant maintains is barred.” Mitchell v. For-
syth, 472 U. S. 511, 527 (1985) (quoting Abney v. United States, 431 U. S.
651, 659 (1977)).
8               GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

merits defense or instead an immunity. Menocal (sup-
ported by the United States as amicus curiae) says a de-
fense, because Yearsley gives contractors only a way to show
that their conduct complied with the law. GEO says an im-
munity—more specifically, “derivative sovereign immun-
ity.” Brief for GEO 15. Under Yearsley, GEO contends, the
Government’s own immunity extends to contractors who
meet specified conditions, thereby giving them the “right
not to stand trial.” Brief for GEO 15. So which is it—a de-
fense or an immunity?
   Yearsley involved a suit by landowners against a federal
contractor for flooding their property. The Government had
hired the contractor to redirect the Missouri River in order
to improve its navigation. The construction company, as
specified in the contract, built dikes in a part of the river
near where the Yearsleys owned a farm. The result, as ex-
pected, was to wash away almost 100 acres of their land.
The Yearsleys did not dispute that the contractor’s work
was “all authorized and directed by the Government.” 309
U. S., at 20. Nonetheless, they sued the contractor for
money damages.
   This Court held that there was “no liability on the part of
the contractor.” Id., at 21. Drawing from multiple prece-
dents involving agency law, the Court explained that a con-
tractor acting as an agent of the Government could be held
liable for injurious conduct in only two circumstances: when
“he exceeded his authority” or when that authority “was not
validly conferred.” Ibid. Here, neither circumstance ob-
tained. As to the second, the Court explained that the Gov-
ernment had “validly” authorized the company to flood the
Yearsleys’ land, because the Government itself possessed
that legal right and had properly delegated it by contract.
Id., at 21–22. And as to the first, the Court concluded that
all the company’s work had stayed within the bounds of the
authority given: The Government had provided instruc-
tions, and the contractor had merely “execut[ed] its will.”
                 Cite as: 607 U. S. ____ (2026)            9

                     Opinion of the Court

Id., at 20–21. Given both those facts—the Government’s
lawful authorization and the contractor’s compliance with
it—the Court could see “no ground for holding [the contrac-
tor] liable.” Id., at 22.
   That reasoning describes a defense, not an immunity.
Yearsley provides protection to a contractor when it has re-
ceived a lawful authorization and acted according to its
terms—meaning, when the contractor has acted within le-
gal bounds. So in invoking Yearsley, the contractor is mak-
ing the argument of a merits defense—that it is not liable
because it has complied with the law. See supra, at 5. Con-
versely, Yearsley’s protection runs out when the contractor
may have violated the law—when the contractor either
acted under an illegal authorization or exceeded the scope
of a legal one. By drawing the line there, Yearsley ensures
that it will never shield unlawful conduct, in the way that
all immunities do. See supra, at 5. In short, because Years-
ley protects a contractor only when—and only because—it
has acted lawfully, Yearsley operates as a defense to liabil-
ity on the merits. And that is consistent with all Yearsley’s
language. The decision never refers to an “immunity,” or
otherwise suggests that the defendant receives a pass from
legal proceedings; it asks only whether the contractor may
be found “liable.” 309 U. S., at 21–22.
   Still more, GEO’s contrary view would put Yearsley in
conflict with the general rule that sovereign immunity is
not transferrable to agents, including contractors, of a gov-
ernment. As Justice Holmes once explained, the Federal
Government’s immunity from a suit (absent a statute
providing otherwise) “does not extend to those that act[ ] in
its name.” Sloan Shipyards Corp. v. United States Ship-
ping Bd. Emergency Fleet Corporation, 258 U. S. 549, 568
(1922). The Court repeated that precept in the Term just
before Yearsley: “[T]he government does not become the
conduit of its immunity in suits against its agents” just be-
cause “they do [the government’s] work.” Keifer & Keifer v.
10              GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

Reconstruction Finance Corporation, 306 U. S. 381, 388
(1939). Rather, the “exceptional freedom from legal respon-
sibility” that sovereign immunity offers is “confined” to the
sovereign entity itself. Ibid. Or again, a few Terms after
Yearsley: A private contractor cannot obtain “[i]mmunity
from suit” by “reason of a contract” it made with the Gov-
ernment. Brady v. Roosevelt S. S. Co., 317 U. S. 575, 583
(1943). GEO tries to bypass those holdings by arguing that
they preclude a contractor from asserting only “uncondi-
tional” sovereign immunity, not the (supposed) “derivative
sovereign immunity” Yearsley offers, which is conditioned
on compliance with the Government’s lawful directives. Re-
ply Brief 6–7. But the proposed distinction is strained. The
whole thrust of the decisions is to deny that government
agents can assert—whether always or sometimes—a “de-
rived” form of sovereign immunity. Rather, the Court in-
sisted, sovereign immunity belongs alone to the Govern-
ment.
   And another, pre-Yearsley decision proves the point, by
relegating a state agent that had asserted sovereign im-
munity to a merits defense, whose contours anticipated
what Yearsley would offer. See Hopkins v. Clemson, 221
U. S. 636 (1911). Oddly enough, the suit challenged the
same kind of conduct involved in Yearsley: The government
agent had flooded a person’s land. The State itself, the
Court noted, would have had “immunity from [a] suit”
based on such conduct. 221 U. S., at 642. But an agent
working on the State’s behalf could not “avail itself ” of that
special “exemption” from “judicial process.” Id., at 642, 645.
“[I]mmunity from suit,” the Court explained, “is a high at-
tribute of sovereignty—a prerogative of the State itself ”—
which cannot be invoked by the State’s agents. Id., at 642–
643. Yet all was not lost: The agent got something. Alt-
hough the agent was “not exempt from suit,” it could “suc-
cessfully defend” against the charges by showing the “law-
ful authority under which [it] acted.” Id., at 643. Those
                      Cite as: 607 U. S. ____ (2026)                    11

                          Opinion of the Court

terms evoke the ones Yearsley used later. See 309 U. S., at
22 (precluding liability for a contractor “acting under” “val-
idly conferred” authority); supra, at 8. And they function
not, as GEO posits, to condition the transfer of sovereign
immunity, but to describe something different—as the
Court made explicit, a merits “defen[se].” Hopkins, 221
U. S., at 643.4
   Once Yearsley is understood in that way—as a merits de-
fense—the question before us almost answers itself: No, a
district court’s denial of Yearsley protection is not immedi-
ately appealable under §1291. Like the denial of other de-
fenses, such a ruling is not, as Cohen’s third condition de-
mands, “effectively unreviewable on appeal from a final
judgment.” Van Cauwenberghe, 486 U. S., at 522. The
right that a merits defense affords is to a finding of non-
liability. And that right—unlike the right not to stand
trial—is fully vindicable on appeal from a final judgment.
See Swint v. Chambers County Comm’n, 514 U. S. 35, 43
(1995); supra, at 6. All an appellate court need do at that

——————
  4 GEO counters that two of our decisions refer to Yearsley as offering

“immunity,” see Brief for GEO 17, 23, but that argument makes far too
much of one piece of loose language. The first cited case, Brady v. Roo-
sevelt S. S. Co., 317 U. S. 575 (1943), mainly cuts against GEO. As noted
above, the Court there rejected the view that a government contractor
obtains “[i]mmunity from suit” by virtue of its contractual relation. Id.,
at 583; see supra, at 10. The Court then turned to Yearsley, finding it
not to apply because the suit alleged negligent conduct, outside what the
Government had authorized. In that half-paragraph, the decision once
refers to Yearsley as providing a “certain immunity.” 317 U. S., at 583.
But it apparently used that term in a colloquial sense, as something of a
synonym for “protection.” The Court’s fuller description of Yearsley ex-
plains that it relieves the contractor of “liability,” without suggesting
that it also offers a pass from litigation. 317 U. S., at 583. And the sec-
ond cited case, Campbell-Ewald Co. v. Gomez, 577 U. S. 153 (2016), gives
GEO even less to work with. That decision merely quotes the imprecise
phrase in Brady on the way to rejecting another contractor’s claim (even
more expansive than GEO’s) to share in the Government’s sovereign im-
munity. 577 U. S., at 166.
12                 GEO GROUP, INC. v. MENOCAL

                          Opinion of the Court

point is reverse the erroneous liability finding. So the final-
ity rule of §1291 precludes interlocutory review of a Years-
ley denial.5
   For those reasons, we hold that the Court of Appeals
lacked jurisdiction over GEO’s appeal. If eventually found
liable, GEO may of course appeal the District Court’s rejec-
tion of its asserted Yearsley defense. But GEO must wait
until then. A Yearsley denial is not appealable before the
trial court’s proceedings have ended.
   We therefore affirm the judgment of the Court of Appeals
and remand the case for further proceedings consistent
with this opinion.
                                                      It is so ordered.




——————
   5 This holding still allows review of a given Yearsley denial by means

of §1292(b)’s separate appeal-certification process. Under that provision,
a district court may find that the special difficulty and importance of an
otherwise unappealable order counsels in favor of immediate review, and
an appellate court may accept that determination. Here, though, the
District Court saw no reason to act under §1292(b).
                  Cite as: 607 U. S. ____ (2026)              1

                      Opinion of THOMAS, J.

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–758
                          _________________


THE GEO GROUP, INC., PETITIONER v. ALEJANDRO
             MENOCAL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                       [February 25, 2026]

   JUSTICE THOMAS, concurring in part and concurring in
the judgment.
   I concur in Parts I and III of the Court’s opinion and in
its judgment. I agree with the Court that Yearsley v. W. A.
Ross Constr. Co., 309 U. S. 18 (1940), and similar decisions
establish a defense from liability and not an immunity from
suit. See ante, at 8–9. Orders rejecting Yearsley defenses
are therefore unlike the orders denying immunities that
this Court has already held to be immediately appealable.
Because no other statute or rule authorized an interlocu-
tory appeal here, the Court correctly affirms the Tenth Cir-
cuit’s dismissal. I do not join Part II because “[w]e need not,
and in my view should not, further justify our holding by
applying” the collateral-order doctrine established by Co-
hen v. Beneficial Industrial Loan Corp., 337 U. S. 541
(1949). Mohawk Industries, Inc. v. Carpenter, 558 U. S.
100, 115 (2009) (THOMAS, J., concurring in part and concur-
ring in judgment). I remain of the view that we should not
expand the Cohen collateral order doctrine beyond orders
that our precedents have already held to be immediately
appealable.
   The Cohen collateral-order doctrine, which allows federal
courts to exercise appellate jurisdiction over certain inter-
locutory orders, conflicts with Congress’s authority over
federal appellate jurisdiction. U. S. Const., Art. I, §8, cl. 9;
2               GEO GROUP, INC. v. MENOCAL

                     Opinion of THOMAS, J.

Art. III, §1. By statute, parties generally cannot appeal be-
fore final judgment. See 28 U. S. C. §1291; ante, at 3–4.
Congress has established certain exceptions to that final-
judgment rule that allow parties to appeal some interlocu-
tory orders immediately. E.g., §1292(a)(1). It has also au-
thorized this Court to create further exceptions through
rulemaking. §1292(e). Cohen’s collateral-order doctrine al-
lows judges to create additional exceptions by judicial opin-
ion, which bypasses “ ‘Congress’s designation of the rule-
making process as the way to define or refine when a
district court ruling is “final” and when an interlocutory or-
der is appealable.’ ” Mohawk Industries, 558 U. S., at 114–
115 (opinion of THOMAS, J.) (quoting Swint v. Chambers
County Comm’n, 514 U. S. 35, 48 (1995)). For that reason,
if an interlocutory order “is not on all fours with orders we
previously have held to be appealable under the collateral
order doctrine,” it should not be immediately appealable.
Mohawk Industries, 558 U. S., at 115 (opinion of THOMAS,
J.).
                  Cite as: 607 U. S. ____ (2026)             1

                ALITO, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–758
                          _________________


THE GEO GROUP, INC., PETITIONER v. ALEJANDRO
             MENOCAL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                      [February 25, 2026]

   JUSTICE ALITO, concurring in the judgment.
   I agree with the Court that the defense conferred by
Yearsley v. W. A. Ross Constr. Co., 309 U. S. 18 (1940), is
not an “immunity from suit.” I therefore agree that an or-
der denying a Yearsley defense is not a “collateral order”
subject to immediate appeal. But I would not rest these
conclusions solely on the fact that Yearsley’s applicability
“turn[s] on [the defendant’s] conduct’s legality.” Ante, at 5.
Under the collateral-order doctrine, defendants may some-
times appeal the denial of a defense immediately when do-
ing so is necessary to vindicate important constitutional or
public-policy interests. And this rule holds true even if the
defense at issue turns on the legality of the defendant’s con-
duct. Thus, I cannot join the opinion of the Court, but I
concur in the judgment because deferring appellate review
of Yearsley rulings until final judgment does not imperil im-
portant constitutional or public-policy interests.
                                I
   Since 1789, Congress has generally limited the universe
of appealable orders to “final decrees and judgments.” Act
of Sept. 24, 1789, 1 Stat. 84. Today, this “final-judgment
rule” limits the jurisdiction of federal courts of appeals. See
28 U. S. C. §1291. The Court has long given this limit a
“practical rather than a technical construction.” Cohen v.
2               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

Beneficial Industrial Loan Corp., 337 U. S. 541, 546 (1949).
Consistent with that approach, our decision in Cohen held
that certain interlocutory orders—now known as collateral
orders—are sufficiently “final” that a party may appeal
them before litigation reaches final judgment. Id., at 546–
547.
  Our collateral-order doctrine establishes three criteria
that an order must satisfy to qualify for immediate appeal.
The order must (1) “conclusively determine [a] disputed
question,” (2) resolve an issue “separate from the merits of
the action,” and (3) be “effectively unreviewable on appeal
from a final judgment.” Coopers & Lybrand v. Livesay, 437
U. S. 463, 468 (1978). Whether a given order satisfies these
criteria does not turn on the “facts of a particular case.”
Carroll v. United States, 354 U. S. 394, 405 (1957). Rather,
the criteria must be satisfied for the “entire category” of or-
ders. Digital Equipment Corp. v. Desktop Direct, Inc., 511
U. S. 863, 868 (1994).
                               A
   Initially, this Court applied the “effectively unreviewa-
ble” requirement to capture orders that would become moot
by the time of final judgment. See Cohen, 337 U. S., at 546.
For those orders, a strict application of the final-judgment
rule “would practically defeat the right to any review at all.”
Cobbledick v. United States, 309 U. S. 323, 324–325 (1940).
We first applied this reasoning in Cohen, which involved a
district-court order that excused the plaintiffs from a litiga-
tion-bond requirement. 337 U. S., at 544–547. Applicable
state law required the plaintiffs to post such a bond to se-
cure their obligation to pay the defendant’s litigation ex-
penses and attorney’s fees if their claims failed. Cohen held
that the order excusing the plaintiffs from posting that
bond was immediately appealable because it would “not be
merged in final judgment.” Id., at 546. Regardless of who
prevailed at final judgment, the question whether the
                  Cite as: 607 U. S. ____ (2026)             3

                ALITO, J., concurring in judgment

plaintiffs had to post a bond would be moot. If the defend-
ant prevailed, an appeal would not relieve it from the plain-
tiffs’ failure to post a bond. And if the plaintiffs prevailed,
the defendant would not be entitled to recover its legal
costs. Thus, if orders denying requests for litigation bonds
were not subject to immediate appeal, those orders would
never receive appellate review.
   This conception of the collateral-order doctrine’s “effec-
tively unreviewable” requirement informed our decision in
Swift & Co. Packers v. Compania Colombiana Del Caribe,
S. A., 339 U. S. 684 (1950). There, we held that the Fifth
Circuit had appellate jurisdiction over a lower court’s order
vacating the attachment of a foreign vessel. Id., at 685–
689. That vessel, which the libelants attached while it
passed through U. S.-controlled waters, served as security
for their claims against the foreign defendant. In this re-
spect, the vessel resembled the bond in Cohen. As was the
case with the bond order, an immediate appeal was the only
means for appellate review of the order vacating the attach-
ment of the vessel. If the libelants in Swift did not prevail
at final judgment, the court’s vacatur of the attachment or-
der would become moot. And if the libelants did prevail,
any appellate review of the attachment issue would be an
“empty rite,” as the vessel would have likely departed U. S.
jurisdiction. 339 U. S., at 689.
   The same reasoning explains our jurisdictional holding in
Stack v. Boyle, 342 U. S. 1 (1951), which extended Cohen to
an order denying a criminal defendant’s motion to modify
his pretrial bail-bond amount. 342 U. S., at 3. Once a court
renders final judgment in a criminal case, the conditions
governing the defendant’s pretrial release become moot. By
that juncture, the defendant has either been released from
custody or begun a sentence of incarceration. Thus, if there
were to be any appellate review of bail, it would need to oc-
cur before final judgment.
4               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

   In sum, our early collateral-order cases applied the “ef-
fectively unreviewable” requirement narrowly. It captured
those orders that would be unreviewable on appeal from a
final judgment on account of mootness.
                               B
   Over the ensuing decades, the Court expanded its appli-
cation of the “effectively unreviewable” requirement to in-
clude orders that undoubtedly would not become moot by
final judgment. For example, in Abney v. United States, 431
U. S. 651 (1977), and Helstoski v. Meanor, 442 U. S. 500
(1979), the Court held that denials of defenses under the
Double Jeopardy Clause and Speech or Debate Clause sat-
isfied Cohen even though these protections could be “vindi-
cated on an appeal following final judgment.” Abney, 431
U. S., at 660. Like most criminal-law defenses, double-jeop-
ardy and speech-or-debate issues merge into the final judg-
ment, and a reviewing court can grant meaningful relief on
these grounds by reversing a defendant’s conviction. Abney
and Helstoski nevertheless held that denials of relief under
these two Clauses were collateral orders.
   Our holdings in these cases relied on the premise that
those two protections were not merely shields from criminal
liability. They were instead “guarantee[s] against being . . .
put to trial” at all. Abney, 431 U. S., at 661; accord, Hel-
stoski, 442 U. S., at 508 (“[T]he Speech or Debate Clause
was designed to protect Congressmen . . . from the burden
of defending themselves” (internal quotation marks omit-
ted)). Thus, although a court could review these defenses
on appeal from a final judgment, a court could not fully vin-
dicate their protections at that time. By the time of final
judgment, the defendant would have already been exposed
to trial, thereby suffering the very harm that these defenses
exist to prevent. This line of reasoning sufficed to render
the orders in Abney and Helstoski “effectively
                 Cite as: 607 U. S. ____ (2026)            5

                ALITO, J., concurring in judgment

unreviewable” on appeal from a final judgment. See Abney,
431 U. S., at 662.
   This doctrinal development had important implications
for our collateral-order jurisprudence. Under Abney and
Helstoski’s logic, once a court designates a defense as an
“immunity from suit,” that defense satisfies the third col-
lateral-order criterion. Digital Equipment, 511 U. S., at
870. We have likewise recognized that an order denying an
immunity from suit will also satisfy the other two collat-
eral-order requirements. See ante, at 7, n. 1. The denial of
an immunity satisfies the first criterion because it “conclu-
sively determine[s]” that a defendant may go to trial. Coop-
ers & Lybrand, 437 U. S., at 468. See Helstoski, 442 U. S.,
at 507 (“Once a motion to dismiss is denied, there is nothing
the Member can do under the [Speech or Debate] Clause . . .
to prevent the trial”). And a “claim of immunity is concep-
tually distinct from the merits,” so an order denying an im-
munity claim satisfies the second requirement. Mitchell v.
Forsyth, 472 U. S. 511, 527 (1985). For these reasons, fed-
eral courts have consistently held that denials of an immun-
ity are collateral orders subject to immediate appeal. See,
e.g., Nixon v. Fitzgerald, 457 U. S. 731, 742 (1982) (Presi-
dential civil immunity); Mitchell, 472 U. S., at 530 (quali-
fied immunity); Puerto Rico Aqueduct and Sewer Authority
v. Metcalf & Eddy, Inc., 506 U. S. 139, 143 (1993) (state and
territorial sovereign immunity); Kilburn v. Socialist Peo-
ple’s Libyan Arab Jamahiriya, 376 F. 3d 1123, 1126 (CADC
2004) (foreign sovereign immunity).
   Given that the designation of a defense as an immunity
is dispositive under the collateral-order doctrine, our Court
has stringently guarded the designation. See Midland As-
phalt Corp. v. United States, 489 U. S. 794, 801 (1989). Af-
ter all, “virtually every right that could be enforced appro-
priately by pretrial dismissal” could be loosely described as
an immunity from suit. Digital Equipment, 511 U. S., at
873. But treating every such right as an immunity would
6               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

permit the “narrow” collateral-order doctrine to “swallow”
the final judgment rule in “virtually every case.” Id., at 868,
873 (internal quotation marks omitted). Our Court has
therefore recognized the need to distinguish “between a
right not to be tried and a right whose remedy requires the
dismissal of charges.” United States v. Hollywood Motor
Car Co., 458 U. S. 263, 269 (1982) (per curiam). And we
have explained that determining whether a defense consti-
tutes an immunity requires an evaluation of “the value of
the interests” that an immediate appeal would advance.
Digital Equipment, 511 U. S., at 878–879. Specifically, we
explained in Will v. Hallock, 546 U. S. 345 (2006), that a
defense “should be treated as an immunity demanding the
protection of a collateral order appeal” only if wrongly al-
lowing a suit to proceed would “imperil a substantial public
interest.” Id., at 353; see also Lauro Lines s.r.l. v. Chasser,
490 U. S. 495, 502 (1989) (Scalia, J., concurring) (“The rea-
son” that a right fails the third requirement of the collat-
eral-order doctrine “is, quite simply, that the law does not
deem the right important enough”).
   Our collateral-order decisions reflect this approach. We
have applied the immunity label to defenses when allowing
an immediate appeal was necessary to preserve “some par-
ticular value of a high order,” such as “honoring the separa-
tion of powers, preserving the efficiency of government and
the initiative of its officials, respecting a State’s dignitary
interests, and mitigating the government’s advantage” over
individual defendants in high-stakes matters. Will, 546
U. S., at 352–353; see, e.g., Nixon, 457 U. S., at 742–743,
749, 758 (citing separation-of-powers concerns when allow-
ing an appeal of an order denying Presidential immunity);
Mitchell, 472 U. S., at 526 (explaining that the avoidance of
distraction, overdeterrence, and timidity in Government
service justified immediate appeals of orders denying qual-
ified immunity); Puerto Rico Aqueduct and Sewer Author-
ity, 506 U. S., at 146 (allowing an appeal of an order
                  Cite as: 607 U. S. ____ (2026)            7

                ALITO, J., concurring in judgment

denying sovereign immunity to “ ‘prevent the indignity of
subjecting a State to the coercive process of judicial tribu-
nals’ ”). In contrast, we have declined to designate defenses
as immunities when postponing appellate review to final
judgment would not imperil important interests. See, e.g.,
Will, 546 U. S., at 353 (holding that the interest in shorten-
ing troublesome litigation is insufficient to treat a defense
as an immunity); Mohawk Industries, Inc. v. Carpenter, 558
U. S. 100, 108–113 (2009) (acknowledging that the attor-
ney-client privilege serves important public interests but
declining to designate it as an immunity because deferring
appeals would not meaningfully harm those interests).
  As these decisions illustrate, we have been cautious in re-
cent years about expanding the collateral-order doctrine,
but we have not closed the book on Cohen. Just two Terms
ago, we designated another defense as an immunity and
evaluated it in an interlocutory posture. See Trump v.
United States, 603 U. S. 593, 635 (2024) (citing Mitchell,
472 U. S., at 524–530); 603 U. S., at 654–655 (BARRETT, J.,
concurring in part). The test for determining whether a de-
fense constitutes an immunity therefore remains keyed to
the interests that an immediate appeal would vindicate. If
postponing review of a wrongly denied defense would un-
dermine important constitutional or policy interests, that
defense constitutes an immunity.
                             II
  Under this framework, the Yearsley doctrine is not an im-
munity from suit. Permitting immediate appeals of orders
denying Yearsley defenses is not necessary to vindicate any
sufficiently important constitutional or public-policy inter-
ests.
                            A
  As the majority correctly explains, Yearsley shields de-
fendants from damages actions for conduct that federal law
8               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

authorized. See Campbell-Ewald Co. v. Gomez, 577 U. S.
153, 166–167 (2016). Although this protection is important
for a range of Government operations, it does not meet the
threshold to be designated an immunity.
   First, postponing appellate review of Yearsley’s applica-
bility until final judgment would not create significant sep-
aration-of-powers problems. To be sure, the possibility that
courts might impose liability for conduct that Congress au-
thorized presents some conflict between those two branches
of Government. Likewise, incorrect contractor-liability ad-
judications can interfere with Executive Branch operations.
But these risks of error arise anytime a court misapplies a
federal statute or entertains an action involving a Govern-
ment contractor. Moreover, these risks pale in comparison
to the separation-of-powers concerns that motivated the ap-
plication of the collateral-order doctrine in other immunity
contexts. See, e.g., Helstoski, 442 U. S., at 502 (concerning
a Congressman who was exposed to criminal liability based
on his decision to introduce a bill in the House of Represent-
atives).
   Yearsley does not implicate sovereign-dignity interests,
either. Although GEO Group describes Yearsley as confer-
ring “derivative sovereign immunity” on contractors, Brief
for Petitioner 10, this label is a poor fit. Sovereign immun-
ity protects governments from the indignity of being sub-
jected to a court’s jurisdiction. Puerto Rico Aqueduct and
Sewer Authority, 506 U. S., at 146. We have never de-
scribed the Yearsley doctrine in those terms, nor have we
suggested that it limits courts’ jurisdiction over contractors.
Cf. Yearsley, 309 U. S., at 19 (noting without disagreement
that the lower court exercised jurisdiction over the case);
Campbell-Ewald Co., 577 U. S., at 165–166 (concluding
that the lower court had jurisdiction over a case before de-
termining whether Yearsley applied). Rather, Yearsley
merely shields contractors from exposure for conduct that
federal law authorized. I therefore agree with the majority
                     Cite as: 607 U. S. ____ (2026)                   9

                   ALITO, J., concurring in judgment

that the Yearsley doctrine “derives” from the Government’s
lawmaking authority, not its sovereign immunity. See
ante, at 9–10; cf. Campbell-Ewald Co., 577 U. S., at 166–
167; Sloan Shipyards Corp. v. United States Shipping Bd.
Emergency Fleet Corporation, 258 U. S. 549, 566–567
(1922).
   Last, unlike with qualified immunity, allowing immedi-
ate appeals of Yearsley denials is not necessary to prevent
overdeterrence, timidity, and distraction in Government
service. That is not to say that these concerns are entirely
absent when plaintiffs bring damages actions against Gov-
ernment contractors. As this Court recognized in Filarsky
v. Delia, 566 U. S. 377 (2012), the public has an interest in
preventing overdeterrence, timidity, and distraction in
Government functions no matter the “nature of [the defend-
ant’s] particular relationship with the government.” Id., at
389–392. But our doctrine already accommodates these
concerns by allowing contractors to invoke qualified im-
munity. Ibid.; Campbell-Ewald Co., 577 U. S., at 167. In-
deed, qualified immunity provides a greater protection to
contractors than Yearsley does. Whereas Yearsley shields
only those contractors who act within the bounds of their
legal authorization, qualified immunity protects “all but the
plainly incompetent or those who knowingly violate the
law.” Malley v. Briggs, 475 U. S. 335, 341 (1986). And as
the defense’s name indicates, contractors may immediately
appeal denials of qualified immunity. Mitchell, 472 U. S.,
at 530. Because qualified immunity already vindicates the
public interest in avoiding overdeterrence, timidity, and
distraction among contractors, there is no overriding inter-
est in also allowing immediate appeals of orders denying
Yearsley’s more modest protections.*           Cf. Mohawk
——————
 *Although Government contractors may generally assert qualified im-
munity, this Court has held that “private prison guards” may not in Rev.
10                 GEO GROUP, INC. v. MENOCAL

                    ALITO, J., concurring in judgment

Industries, Inc., 558 U. S., at 109–112 (declining to treat the
attorney-client privilege as an immunity because other “es-
tablished mechanisms for appellate review” were availa-
ble).
  In sum, allowing immediate appeals of orders denying
Yearsley defenses is not necessary to vindicate any im-
portant constitutional or public-policy interests. Accord-
ingly, the Yearsley doctrine is not an immunity from suit.
And because Yearsley issues can be reviewed on an appeal
from a final judgment, these orders do not otherwise satisfy
the third collateral-order requirement.
                               B
   Rather than conducting the public-interest inquiry that
our immunity case law employs, the majority trains most of
its analysis on a single question: Whether the Yearsley doc-
trine “turn[s] on [the defendant’s] conduct’s legality.” Ante,
at 5. Because the Yearsley doctrine does, the majority con-
cludes that it fails to satisfy the third collateral-order re-
quirement. That analysis is oversimplified.
   Of course, whether a defense turns on the legality of a
defendant’s conduct can be relevant to the collateral-order
analysis. For example, the degree of overlap between a
——————
Stat. §1979, 42 U. S. C. §1983 cases. See Richardson v. McKnight, 521
U. S. 399, 412 (1997). Separately, this Court has not decided whether
corporate-contractor defendants like GEO Group may invoke qualified
immunity. But see United Pet Supply, Inc. v. Chattanooga, 768 F. 3d
464, 484, n. 3 (CA6 2014) (noting that the Sixth Circuit has entertained
corporate defendants’ assertions of qualified immunity). Perhaps the
public interest would be well-served by allowing appeals of orders deny-
ing Yearsley defenses to those defendants who cannot invoke qualified
immunity. Even so, our doctrine requires us to decide whether Yearsley
denials are collateral orders as a category, not “as applied” to particular
defendants. If, however, most defendants who invoke Yearsley could not
invoke qualified immunity, the collateral-order analysis might be differ-
ent. For example, if corporate contractors could never invoke qualified
immunity, then there would be a stronger argument that denials of
Yearsley defenses should be immediately appealable.
                  Cite as: 607 U. S. ____ (2026)             11

                 ALITO, J., concurring in judgment

defense and a defendant’s conduct can bear on whether an
order is “ ‘separate from the merits of the action.’ ” Ante, at
7, n. 1; but see Mitchell, 472 U. S., at 527. It is also true
that certain “immunities from suit” are jurisdictional bars
that shield a defendant from judicial process regardless of
whether it acted lawfully. See, e.g., 28 U. S. C. § 1604 (cod-
ifying foreign sovereign immunity as a jurisdictional bar);
Seminole Tribe of Fla. v. Florida, 517 U. S. 44, 72–73 (1996)
(treating state sovereign immunity as a jurisdictional
limit).
   Nonetheless, the majority’s rule cannot fully explain our
collateral-order case law. For instance, qualified immunity
is an immunity from suit, yet its applicability can and often
does turn on whether a defendant violated the law. See
District of Columbia v. Wesby, 583 U. S. 48, 62–63 (2018).
Indeed, before this Court decided Pearson v. Callahan, 555
U. S. 223 (2009), a court evaluating a qualified-immunity
defense had to resolve the legality of the defendant’s alleged
conduct. Id., at 232; see, e.g., Scott v. Harris, 550 U. S. 372,
377 (2007). We nevertheless treated (and continue to treat)
denials of qualified immunity as collateral orders.
   On the other side of the ledger, we have held that several
defenses are not immunities even though they do not turn
on the legality of the defendant’s conduct. For instance, this
Court has held that neither the Federal Tort Claims Act’s
judgment bar nor a criminal defendant’s right against vin-
dictive prosecution qualifies as an immunity from suit, even
though neither defense concerns a defendant’s challenged
conduct. See Will, 546 U. S., at 353–355; Hollywood Motor
Car Co., 458 U. S., at 267–270; see also Digital Equipment
Corp., 511 U. S., at 884 (holding that a lower court’s refusal
to enforce a settlement agreement against a plaintiff ’s
claims was not a collateral order).
   In short, although the majority’s focus—whether a de-
fense turns on the legality of the defendant’s conduct—can
12              GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

be relevant in the collateral-order analysis, it is not dispos-
itive of whether a defense constitutes an immunity.
                          *    *      *
   Because postponing appellate review of Yearsley issues
until final judgment would not imperil important constitu-
tional or public-policy interests, I concur in the judgment of
the Court.

```

---

## GROUP: _overhaul2/lake/cases/Thompson v. Clark.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Thompson v. Clark
type: case
citation: "596 U.S. 36 (2022)"
parallel_cite: 142 S. Ct. 1332
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2022
date_decided: ""
docket: 20-659
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
  opinion_url: "https://www.courtlistener.com/opinion/6457347/thompson-v-clark/"
  cluster_id: 6457347
  opinion_id: 6329458
  identity_checked: true
lake:
  record_id: Thompson v. Clark
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Malicious Prosecution under the Fourth Amendment]]"
    role: Key
related:
  - "[[Chiaverini v. City of Napoleon]]"
  - "[[Heck v. Humphrey]]"
  - "[[Malicious Prosecution under the Fourth Amendment]]"
tags:
  - case
  - fourth-amendment
  - malicious-prosecution
  - section-1983
  - favorable-termination
holding: "To show a favorable termination for a Fourth Amendment § 1983 malicious-prosecution claim, a plaintiff need only show that the criminal prosecution ended without a conviction — not that it ended with some affirmative indication of innocence."
---

# Thompson v. Clark

*596 U.S. 36 (2022)* (No. 20-659) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 6457347 → opinion 6329458; quote string-matched to the CL opinion text 2026-07-07 (CL carries the slip opinion, 596 U.S. ___; pin cited slip-style per S2 A3). S9 promotes. -->

## Background
Larry Thompson's sister-in-law, who lived with his family in Brooklyn, called authorities to report suspected child abuse of his newborn daughter; the marks were later shown to be a normal diaper rash. When EMTs and police arrived, Thompson refused to let them enter without a warrant. Officers entered anyway, and Thompson was arrested and charged with obstructing governmental administration and resisting arrest. He was held two days; the charges were later dismissed on the prosecution's motion, without any explanation. Thompson sued the officers under 42 U.S.C. § 1983, advancing a Fourth Amendment malicious-prosecution claim. Under Second Circuit precedent (*Lanning*), a plaintiff had to show that the prosecution ended not merely without a conviction but with some affirmative indication of innocence — a showing Thompson could not make — so the courts below dismissed the claim.

## Issue
What a plaintiff must show to establish the "favorable termination" element of a Fourth Amendment malicious-prosecution claim under § 1983: is it enough that the prosecution ended without a conviction, or must it also have ended with an affirmative indication of innocence?

## Rule
A Fourth Amendment claim under § 1983 for malicious prosecution borrows the elements of the most analogous common-law tort — malicious prosecution — as it stood in 1871, requiring the plaintiff to show a favorable termination of the underlying criminal case. Because the American tort-law consensus of 1871 treated the favorable-termination element as satisfied whenever the prosecution ended without a conviction, the Court held: "To demonstrate a favorable termination of a criminal prosecution for purposes of the Fourth Amendment claim under §1983 for malicious prosecution, a plaintiff need only show that his prosecution ended without a conviction." — 596 U.S. 36 (slip op., at 2). ^pin-2

## Application
Thompson's charges were dismissed before trial without any explanation, which is enough to satisfy the favorable-termination requirement as the Court defined it. Requiring an affirmative indication of innocence, the Court reasoned, would be inconsistent with the 1871 tort consensus, would be hard to apply to the many prosecutions that end in unexplained dismissals, and would leave plaintiffs unable to sue simply because a busy prosecutor gave no reasons. Because Thompson's prosecution ended without a conviction, he satisfied that element and his claim could proceed.

## Conclusion
The judgment of the Second Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Kavanaugh, J., delivered the opinion of the Court; Alito, J., joined by Thomas, Gorsuch, and Barrett, JJ., dissented, disputing that the Fourth Amendment houses a malicious-prosecution claim at all.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Thompson* supplies the favorable-termination rule for Fourth Amendment malicious-prosecution claims; the Court applied and built on it in *[[Chiaverini v. City of Napoleon]]* (2024), which held that such claims are assessed charge by charge.

## Appears on
- [[Malicious Prosecution under the Fourth Amendment]] — *Key*

## Sources
- [*Thompson v. Clark*, 596 U.S. 36 (2022)](https://www.courtlistener.com/opinion/6457347/thompson-v-clark/) — pinpoint: slip op., at 2 (Opinion of the Court, holding); quote string-matched to the CL slip-opinion text 2026-07-07.
- [*Chiaverini v. City of Napoleon*, 602 U.S. 556 (2024)](https://www.courtlistener.com/opinion/10600074/chiaverini-v-city-of-napoleon/) — applying *Thompson*'s framework charge by charge.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a7037882b4905275", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Thompson v. Clark"}, "payload": {"all": [{"cite": "596 U.S. 36", "page": "36", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "596"}, {"cite": "142 S. Ct. 1332", "page": "1332", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "142"}], "display": "596 U.S. 36", "official": {"cite": "596 U.S. 36", "page": "36", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "596"}, "official_selection_present": true, "record_id": "Thompson v. Clark"}}
{"assertion_id": "0dc72b8bb24057ad", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Thompson v. Clark"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Thompson v. Clark", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Thompson v. Clark

```json
{
  "schema_version": "s2.v1",
  "record_id": "Thompson v. Clark",
  "status": "under_review",
  "identity": {
    "case_name": "Thompson v. Clark",
    "case_name_short": "Thompson",
    "case_name_full": "",
    "input_case_name": "Thompson v. Clark",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2022,
    "docket": "20-659",
    "cluster_id": 6457347,
    "lead_opinion_id": 6329458,
    "sibling_ids": [],
    "absolute_url": "/opinion/6457347/thompson-v-clark/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "596 U.S. 36",
      "volume": "596",
      "reporter": "U.S.",
      "page": "36",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "142 S. Ct. 1332",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "1332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "596 U.S. 36",
        "volume": "596",
        "reporter": "U.S.",
        "page": "36",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 1332",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "1332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "596 U.S. 36",
    "official_selection": {
      "court_class": "scotus",
      "selected": "596 U.S. 36",
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
    "date_created": "2026-07-06T12:11:00Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "thompson-v-clark--6457347",
      "to_record_id": "Thompson v. Clark",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Thompson v. Clark

```
(Slip Opinion)              OCTOBER TERM, 2021                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                     THOMPSON v. CLARK ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE SECOND CIRCUIT

      No. 20–659.     Argued October 12, 2021—Decided April 4, 2022
In January 2014, petitioner Larry Thompson was living with his fiancée
  (now wife) and their newborn baby in an apartment in Brooklyn, New
  York. Thompson’s sister-in-law, who apparently suffered from a men-
  tal illness, called 911 to report that Thompson was sexually abusing
  the baby. When Emergency Medical Technicians arrived, Thompson
  denied that anyone had called 911. When the EMTs returned with
  four police officers, Thompson told them that they could not enter with-
  out a warrant. The police nonetheless entered and handcuffed Thomp-
  son. EMTs took the baby to the hospital where medical professionals
  examined her and found no signs of abuse. Meanwhile, Thompson was
  arrested and charged with obstructing governmental administration
  and resisting arrest. He was detained for two days before being re-
  leased. The charges against Thompson were dismissed before trial
  without any explanation by the prosecutor or judge. After the dismis-
  sal, Thompson filed suit under 42 U. S. C. §1983, alleging several con-
  stitutional violations, including a Fourth Amendment claim for mali-
  cious prosecution. To maintain that Fourth Amendment claim under
  §1983, a plaintiff such as Thompson must demonstrate, among other
  things, that he obtained a favorable termination of the underlying
  criminal prosecution. To meet that requirement, Second Circuit prec-
  edent required Thompson to show that his criminal prosecution ended
  not merely without a conviction, but also with some affirmative indi-
  cation of his innocence. See Lanning v. Glens Falls, 908 F. 3d 19, 22.
  The District Court, bound by Lanning, held that Thompson’s criminal
  case had not ended in a way that affirmatively indicated his innocence
  because Thompson could not offer any substantial evidence to explain
  why his case was dismissed. The Second Circuit affirmed the dismis-
  sal of Thompson’s claim. This Court granted certiorari to resolve a
2                        THOMPSON v. CLARK

                                 Syllabus

    split among the Courts of Appeals over how to apply the favorable ter-
    mination requirement of the Fourth Amendment claim under §1983
    for malicious prosecution.
Held: To demonstrate a favorable termination of a criminal prosecution
 for purposes of the Fourth Amendment claim under §1983 for mali-
 cious prosecution, a plaintiff need not show that the criminal prosecu-
 tion ended with some affirmative indication of innocence. A plaintiff
 need only show that his prosecution ended without a conviction.
 Thompson has satisfied that requirement here. Pp. 4–12.
    (a) To determine the elements of a constitutional claim under §1983,
 this Court’s practice is to first look to the elements of the most analo-
 gous tort as of 1871 when §1983 was enacted, so long as doing so is
 consistent with “the values and purposes of the constitutional right at
 issue.” Manuel v. Joliet, 580 U. S. 357, 370. Here, as most of the
 Courts of Appeals to consider the question have determined, the most
 analogous tort to this Fourth Amendment claim is malicious prosecu-
 tion. Pp. 4–7.
    (b) In accord with the elements of the malicious prosecution tort, a
 Fourth Amendment claim under §1983 for malicious prosecution re-
 quires the plaintiff to show a favorable termination of the underlying
 criminal case against him. The parties to this case, as well as the lower
 courts, disagree about what a favorable termination entails, i.e., is it
 sufficient to show that Thompson’s prosecution ended without a con-
 viction or must he also show that his prosecution ended with some af-
 firmative indication of innocence? To resolve that disagreement, the
 Court looks to American malicious prosecution tort law as of 1871. At
 that time, most American courts agreed that the favorable termination
 element of a malicious prosecution claim was satisfied so long as the
 prosecution ended without a conviction. A plaintiff could maintain a
 malicious prosecution claim when, for example, the prosecutor aban-
 doned the criminal case or the court dismissed the case without provid-
 ing a reason.
    The American tort-law consensus as of 1871 did not require a plain-
 tiff in a malicious prosecution suit to show that his prosecution ended
 with an affirmative indication of innocence, and this Court similarly
 construes Thompson’s Fourth Amendment claim under §1983 for ma-
 licious prosecution. Doing so is consistent with “the values and pur-
 poses” of the Fourth Amendment. Manuel, 580 U. S., at 370. Ques-
 tions concerning whether a criminal defendant was wrongly charged,
 or whether an individual may seek redress for a wrongful prosecution,
 cannot reasonably depend on whether the prosecutor or court hap-
 pened to explain why charges were dismissed. And requiring a plain-
 tiff to show that his prosecution ended with an affirmative indication
 of innocence is not necessary to protect officers from unwarranted civil
                     Cite as: 596 U. S. ____ (2022)                      3

                                Syllabus

  suits, as officers are still protected by the requirement that the plain-
  tiff show the absence of probable cause and by qualified immunity.
  Pp. 7–11.
794 Fed. Appx. 140, reversed and remanded.

   KAVANAUGH, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and BREYER, SOTOMAYOR, KAGAN, and BARRETT, JJ., joined. ALITO,
J., filed a dissenting opinion, in which THOMAS and GORSUCH, JJ., joined.
                        Cite as: 596 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 20–659
                                    _________________


            LARRY THOMPSON, PETITIONER v.
                 PAGIEL CLARK, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                                   [April 4, 2022]

   JUSTICE KAVANAUGH delivered the opinion of the Court.
   Larry Thompson was charged and detained in state crim-
inal proceedings, but the charges were dismissed before
trial without any explanation by the prosecutor or judge.
After the dismissal, Thompson alleged that the police offic-
ers who initiated the criminal proceedings had “maliciously
prosecuted” him without probable cause. App. 33–34.
Thompson sued and sought money damages from those of-
ficers in federal court. As relevant here, he advanced a
Fourth Amendment claim under 42 U. S. C. §1983 for ma-
licious prosecution.
   To maintain that Fourth Amendment claim under §1983,
a plaintiff such as Thompson must demonstrate, among
other things, that he obtained a favorable termination of the
underlying criminal prosecution. Cf. Heck v. Humphrey,
512 U. S. 477, 484, and n. 4 (1994). This case requires us to
flesh out what a favorable termination entails. Does it suf-
fice for a plaintiff to show that his criminal prosecution
ended without a conviction? Or must the plaintiff also
demonstrate that the prosecution ended with some affirm-
ative indication of his innocence, such as an acquittal or a
2                   THOMPSON v. CLARK

                     Opinion of the Court

dismissal accompanied by a statement from the judge that
the evidence was insufficient?
   We conclude as follows: To demonstrate a favorable ter-
mination of a criminal prosecution for purposes of the
Fourth Amendment claim under §1983 for malicious prose-
cution, a plaintiff need only show that his prosecution
ended without a conviction. Thompson satisfied that re-
quirement in this case. We therefore reverse the judgment
of the U. S. Court of Appeals for the Second Circuit and re-
mand for further proceedings consistent with this opinion.
                              I
  Larry Thompson lived with his fiancée (now wife) and
their newborn baby girl in an apartment in Brooklyn, New
York. In January 2014, Thompson’s sister-in-law was also
staying there. The sister-in-law apparently suffered from a
mental illness. One day that January, the sister-in-law
called 911 and claimed that Thompson was sexually abus-
ing his one-week-old baby daughter. Two Emergency Med-
ical Technicians promptly responded. When the EMTs ar-
rived at the family’s apartment, Thompson asked the EMTs
why they were there and denied that anyone had called 911.
The EMTs left and informed the police of the situation.
  The EMTs and four police officers then returned to the
apartment. When they arrived, Thompson told them that
they could not come in without a warrant. The police offic-
ers nonetheless entered and, after a brief scuffle, hand-
cuffed Thompson. The EMTs followed the officers into the
apartment and examined the baby. After finding red marks
on the baby’s body, the EMTs took the baby to the hospital
for evaluation. The marks turned out to be a case of diaper
rash. The medical professionals found no signs of abuse.
  Meanwhile, the police officers arrested Thompson for re-
sisting their entry into the apartment. Thompson was
taken to a local hospital and then to jail. While Thompson
was in custody, one of the police officers prepared and filed
                 Cite as: 596 U. S. ____ (2022)           3

                     Opinion of the Court

a criminal complaint charging Thompson with obstructing
governmental administration and resisting arrest. Thomp-
son remained in custody for two days. A judge then re-
leased him on his own recognizance.
  Before trial, the prosecution moved to dismiss the
charges, and the trial judge in turn dismissed the case. The
prosecutor did not explain why she sought to dismiss the
charges, nor did the trial judge explain why he dismissed
the case.
  After the criminal prosecution ended, Thompson brought
suit for damages under 42 U. S. C. §1983 against the police
officers who had arrested and charged him. Thompson al-
leged several constitutional violations, including a Fourth
Amendment claim for “malicious prosecution.” App. 33.
Thompson asserted that the officers “maliciously prose-
cuted” him and “subjected him to an unlawful, illegal and
excessive detention” in violation of his Fourth Amendment
rights. Id., at 34.
   To prevail on that claim under Second Circuit precedent,
Thompson had to show that his criminal prosecution ended
not merely without a conviction, but also with some affirm-
ative indication of his innocence. See Lanning v. Glens
Falls, 908 F. 3d 19, 22 (2018). Thompson could not put forth
any substantial evidence that would explain why the pros-
ecutor had moved to dismiss the charges or why the trial
court had dismissed the charges. Therefore, the District
Court ruled that Thompson’s criminal case had not ended
in a way that affirmatively indicated his innocence. The
District Court granted judgment to the defendant officers
on that Fourth Amendment claim. Notably, the District
Court also opined that the relevant Second Circuit prece-
dent “can and should be changed” to say that a favorable
termination occurs so long as the prosecution ends without
a conviction. 364 F. Supp. 3d 178, 181, 196–197 (EDNY
2019). On appeal, however, the U. S. Court of Appeals for
the Second Circuit adhered to its precedent in Lanning and
4                    THOMPSON v. CLARK

                      Opinion of the Court

affirmed the dismissal of Thompson’s Fourth Amendment
claim. 794 Fed. Appx. 140 (2020).
   The Courts of Appeals have split over how to apply the
favorable termination requirement of the Fourth Amend-
ment claim under §1983 for malicious prosecution. In ad-
dition to the Second Circuit, some other Courts of Appeals
have held that a favorable termination requires some af-
firmative indication of innocence. See, e.g., Kossler v.
Crisanti, 564 F. 3d 181, 187 (CA3 2009) (en banc); Cordova
v. Albuquerque, 816 F. 3d 645, 649 (CA10 2016). By con-
trast, the Eleventh Circuit has held that a favorable termi-
nation occurs so long as the criminal prosecution ends with-
out a conviction. See Laskar v. Hurd, 972 F. 3d 1278, 1282
(2020). This Court granted certiorari to resolve the split.
592 U. S. ___ (2021).
                               II
                               A
   In 1871, Congress passed and President Grant signed the
Civil Rights Act of 1871. Section 1 of that Act, now codified
at 42 U. S. C. §1983, created a species of federal tort liabil-
ity for individuals to sue state and local officers for depriva-
tions of constitutional rights.
   In this case, Thompson sued several police officers under
§1983, alleging that he was “maliciously prosecuted” with-
out probable cause and that he was seized as a result. App.
33–34. He brought a Fourth Amendment claim under
§1983 for malicious prosecution, sometimes referred to as a
claim for unreasonable seizure pursuant to legal process.
This Court’s precedents recognize such a claim. See Manuel
v. Joliet, 580 U. S. 357, 363–364, 367–368 (2017); Albright
v. Oliver, 510 U. S. 266, 271 (1994) (plurality opinion); see
also id., at 290–291 (Souter, J., concurring in judgment).
And following this Court’s precedents, the District Courts
and Courts of Appeals have decided numerous cases involv-
ing Fourth Amendment claims under §1983 for malicious
                      Cite as: 596 U. S. ____ (2022)                     5

                          Opinion of the Court

prosecution. See, e.g., Pitt v. District of Columbia, 491 F. 3d
494, 510–511 (CADC 2007) (“[N]early every other Circuit
has held that malicious prosecution is actionable under the
Fourth Amendment to the extent that the defendant’s ac-
tions cause the plaintiff to be ‘seized’ without probable
cause”); Kossler, 564 F. 3d, at 186–187; Sykes v. Anderson,
625 F. 3d 294, 308–309 (CA6 2010); Durham v. Horner, 690
F. 3d 183, 188 (CA4 2012); Myers v. Koopman, 738 F. 3d
1190, 1194 (CA10 2013); Winfrey v. Rogers, 901 F. 3d 483,
491–493 (CA5 2018); Lanning, 908 F. 3d, at 28; Jordan v.
Waldoboro, 943 F. 3d 532, 545 (CA1 2019); Williams v.
Aguirre, 965 F. 3d 1147, 1157 (CA11 2020).1
   The narrow dispute in this case concerns one element of
the Fourth Amendment claim under §1983 for malicious
prosecution. To determine the elements of a constitutional
claim under §1983, this Court’s practice is to first look to
the elements of the most analogous tort as of 1871 when
§1983 was enacted, so long as doing so is consistent with
“the values and purposes of the constitutional right at is-
sue.” Manuel, 580 U. S., at 370; see also Nieves v. Bartlett,
587 U. S. ___, ___ (2019) (slip op., at 12); Heck, 512 U. S., at
483.2
   Here, as most of the Courts of Appeals to consider the

——————
   1 Thompson also brought a Fourth Amendment claim for unreasonable

seizure (labeled a false arrest claim), based on his initial arrest before
charges were filed against him. But the jury ruled against him on the
merits of that claim. That claim is not before us, and we therefore do not
consider it.
   2 Because this claim is housed in the Fourth Amendment, the plaintiff

also has to prove that the malicious prosecution resulted in a seizure of
the plaintiff. See Manuel v. Joliet, 580 U. S. 357, 365–366 (2017). It has
been argued that the Due Process Clause could be an appropriate ana-
lytical home for a malicious prosecution claim under §1983. See Albright
v. Oliver, 510 U. S. 266, 281, 286 (1994) (Kennedy, J., concurring in judg-
ment). If so, the plaintiff presumably would not have to prove that he
was seized as a result of the malicious prosecution. But we have no oc-
casion to consider such an argument here.
6                      THOMPSON v. CLARK

                        Opinion of the Court

question have determined, the most analogous tort to this
Fourth Amendment claim is malicious prosecution. See
Kossler, 564 F. 3d, at 186; Sykes, 625 F. 3d, at 308–309;
Durham, 690 F. 3d, at 188; Myers, 738 F. 3d, at 1194; Lan-
ning, 908 F. 3d, at 28; Jordan, 943 F. 3d, at 545. That is
because the gravamen of the Fourth Amendment claim for
malicious prosecution, as this Court has recognized it, is the
wrongful initiation of charges without probable cause. And
the wrongful initiation of charges without probable cause is
likewise the gravamen of the tort of malicious prosecution.
   In American courts as of 1871, the malicious prosecution
tort generally allowed recovery against an individual who
had initiated or caused the initiation of criminal proceed-
ings despite having “no good reason to believe” that crimi-
nal charges were “justified by the facts and the law.” T.
Cooley, Law of Torts 180 (1880) (Cooley); see also 1 F. Hil-
liard, The Law of Torts or Private Wrongs 412–414 (1866)
(Hilliard). The malicious prosecution tort protected against
“injury to the person, as connected with false imprison-
ment” and against “a wrong to character or reputation.” Id.,
at 412 (emphasis deleted).
   American courts described the elements of the malicious
prosecution tort as follows: (i) the suit or proceeding was
“instituted without any probable cause”; (ii) the “motive in
instituting” the suit “was malicious,” which was often de-
fined in this context as without probable cause and for a
purpose other than bringing the defendant to justice; and
(iii) the prosecution “terminated in the acquittal or dis-
charge of the accused.” Cooley 181.3
   That third requirement—a favorable termination of the
underlying criminal prosecution—is the focus of the parties’
dispute in this case.

——————
  3 We need not decide whether a plaintiff bringing a Fourth Amend-

ment claim under §1983 for malicious prosecution must establish malice
(or some other mens rea) in addition to the absence of probable cause.
                  Cite as: 596 U. S. ____ (2022)            7

                      Opinion of the Court

                                B
   In accord with the elements of the malicious prosecution
tort, a Fourth Amendment claim under §1983 for malicious
prosecution requires the plaintiff to show a favorable termi-
nation of the underlying criminal case against him. The
favorable termination requirement serves multiple pur-
poses: (i) it avoids parallel litigation in civil and criminal
proceedings over the issues of probable cause and guilt;
(ii) it precludes inconsistent civil and criminal judgments
where a claimant could succeed in the tort action after hav-
ing been convicted in the criminal case; and (iii) it prevents
civil suits from being improperly used as collateral attacks
on criminal proceedings. Cf. Heck, 512 U. S., at 484–485;
see also McDonough v. Smith, 588 U. S. ___, ___ (2019) (slip
op., at 7).
   The parties to this case disagree about what a favorable
termination entails. In particular, does it suffice for a
plaintiff to show that his prosecution ended without a con-
viction? Or must the plaintiff also show that his prosecu-
tion ended with some affirmative indication of innocence,
such as an acquittal or a dismissal accompanied by a state-
ment from the judge that the evidence was insufficient?
   To resolve that disagreement, we must look to American
malicious prosecution tort law as of 1871. See Nieves, 587
U. S., at ___ (slip op., at 12). In most American courts that
had considered the question as of 1871, the favorable ter-
mination element of a malicious prosecution claim was sat-
isfied so long as the prosecution ended without a conviction.
As one influential New York decision explained, when the
individual was “convicted in the suit or proceeding com-
plained of,” he could not maintain an action for malicious
prosecution. Clark v. Cleveland, 6 Hill 344, 346, n. a (1844).
But when the individual was not convicted, the “question
is, whether the prosecution instituted by the defendant can
be said to have been terminated, disposed of, or, as the
books usually say, at an end.” Id., at 346. The “technical
8                   THOMPSON v. CLARK

                      Opinion of the Court

prerequisite is only that the particular prosecution be dis-
posed of in such a manner” that it “cannot be revived.” Id.,
at 347; Bacon v. Waters, 84 Mass. 400, 401–402 (1861); M.
Newell, Law of Malicious Prosecution 327–328 (1892)
(Newell).
   On that point, American courts as of 1871 were largely in
agreement. To take one example, the Supreme Court of In-
diana ruled that a dismissal satisfied the favorable termi-
nation requirement because it marked “an end to further
proceedings against the defendant” on the charges. Chap-
man v. Woods, 6 Blackf. 504, 505–506 (1843). Similarly, the
Supreme Court of Tennessee concluded that a suit was
proper when “the prosecution was at an end.” Pharis v.
Lambert, 33 Tenn. 228, 232 (1853).
   For that reason, a plaintiff could maintain a malicious
prosecution claim when, for example, the prosecutor aban-
doned the criminal case or the court dismissed the case
without providing a reason. See, e.g., Fay v. O’Neill, 36
N. Y. 11, 13 (1867); Murray v. Lackey, 6 N. C. 368, 368–369
(1818); Driggs v. Burton, 44 Vt. 124, 143–144 (1871); Brown
v. Randall, 36 Conn. 56, 61–63 (1869); Chapman, 6 Blackf.,
at 505–506; Sayles v. Briggs, 45 Mass. 421, 425–426 (1842);
Yocum v. Polly, 40 Ky. 358, 359 (1841); Burhans v. Sanford,
19 Wend. 417, 418 (N. Y. 1838); Cotton v. Wilson, Minor 203
(Ala. 1824).
   Several courts explicitly added, moreover, that a favora-
ble termination did not require an acquittal or a dismissal
accompanied by some affirmative indication of innocence.
In the words of one court, it “is not to be understood, that
an action, for a malicious prosecution, will not lie, unless
the party has been acquitted by a jury on trial.” Thomas v.
DeGraffenreid, 11 S. C. L. 143, 144–145 (1819). “On the
contrary, a person may have his action after a bill rejected
by the grand jury, or even where no bill has been preferred,
if there is a final end of the prosecution, and the party dis-
charged.” Id., at 145; see also Chapman, 6 Blackf., at 505–
                  Cite as: 596 U. S. ____ (2022)            9

                      Opinion of the Court

506.
   The treatises of that era agreed that a favorable termina-
tion occurred so long as the prosecution ended without con-
viction. Cooley’s tort-law treatise stated, for example, that
“the reasonable rule seems to be, that the technical prereq-
uisite is only that the particular prosecution be disposed of
in such a manner that this cannot be revived, and the pros-
ecutor, if he proceeds further, will be put to a new one.”
Cooley 186; see also Newell 343 (expressing approval of the
rule); Hilliard 453, and n. 5 (recognizing the rule).
   The parties to this case have identified only one court
that required something more, such as an acquittal or a dis-
missal accompanied by some affirmative indication of inno-
cence. In 1863, the Rhode Island Supreme Court concluded,
“with reluctance,” that “ ‘the termination must be such as to
furnish prima facie evidence that the action was without
foundation.’ ” Rounds v. Humes, 7 R. I. 535, 537 (1863). But
Rhode Island stood as an outlier on that question. The
other American courts to consider the issue did not require
some affirmative indication of innocence in order for a ma-
licious prosecution tort claim to proceed. The courts simply
required that the prosecution ended in the defendant’s fa-
vor. As Chief Judge Pryor explained in his comprehensive
opinion for the Eleventh Circuit in Laskar v. Hurd, 972
F. 3d, at 1287: “The clear majority of American courts did
not limit favorable terminations to those that suggested the
accused’s innocence.”
   Against that body of precedent and historical practice, re-
spondent Clark contends that American courts as of 1871
had not settled on any particular favorable termination
rule. But the cases and treatises that respondent latches
onto addressed a separate issue—not whether the prosecu-
tion had terminated in the defendant’s favor, but whether
the prosecution had terminated at all. In particular, courts
divided over whether a prosecutor’s dismissal without dis-
charge by a judge in fact terminated a prosecution. Some
10                  THOMPSON v. CLARK

                     Opinion of the Court

courts concluded that a prosecution ended when the prose-
cutor dismissed the case, even if the court had not yet taken
action. See, e.g., Woodman v. Prescott, 66 N. H. 375, 376–
377 (1890); see also 1 F. Hilliard, The Law of Torts or Pri-
vate Wrongs 475 (1874); Newell 327–328; Cooley 186.
Other courts said that a prosecution did not end until a
judge discharged, or formally released, the defendant from
the case. See, e.g., DeGraffenreid, 11 S. C. L., at 145; Pau-
kett v. Livermore, 5 Iowa 277, 282 (1857).
   But those cases did not purport to alter the basic favora-
ble termination principle—namely, that a malicious prose-
cution claim could proceed when the prosecution termi-
nated without a conviction.
   Respondent also seizes on a comment in the American
Law Institute’s 1976 Second Restatement of Torts (as have
most of the Courts of Appeals that have sided with respond-
ent’s position on this issue). See Jordan, 943 F. 3d, at 545–
546; Lanning, 908 F. 3d, at 26; Salley v. Myers, 971 F. 3d
308, 312–313 (CA4 2020); Jones v. Clark Cty., 959 F. 3d
748, 763–765 (CA6 2020); Cordova, 816 F. 3d, at 651. The
comment in the Second Restatement opined that, for pur-
poses of a malicious prosecution claim, a criminal case ter-
minates “in favor of the accused” when the prosecution ends
in a way “as to indicate the innocence of the accused.” Re-
statement (Second) of Torts §660, and Comment a (1976).
   But respondent’s reliance on the 1976 Restatement is
flawed because the Restatement did not purport to describe
the consensus of American law as of 1871, at least on that
question. The status of American law as of 1871 is the rel-
evant inquiry for our purposes. See Manuel, 580 U. S., at
370; Nieves, 587 U. S., at ___ (slip op., at 12); Laskar, 972
F. 3d, at 1286. And in the overwhelming majority of Amer-
ican jurisdictions that had considered the issue as of 1871,
a plaintiff alleging malicious prosecution did not need to
show that his prosecution had ended with some affirmative
indication of innocence.
                 Cite as: 596 U. S. ____ (2022)           11

                     Opinion of the Court

   Because the American tort-law consensus as of 1871 did
not require a plaintiff in a malicious prosecution suit to
show that his prosecution ended with an affirmative indi-
cation of innocence, we similarly construe the Fourth
Amendment claim under §1983 for malicious prosecution.
Doing so is consistent, moreover, with “the values and pur-
poses” of the Fourth Amendment. Manuel, 580 U. S., at
370. The question of whether a criminal defendant was
wrongly charged does not logically depend on whether the
prosecutor or court explained why the prosecution was dis-
missed. And the individual’s ability to seek redress for a
wrongful prosecution cannot reasonably turn on the fortu-
ity of whether the prosecutor or court happened to explain
why the charges were dismissed. In addition, requiring the
plaintiff to show that his prosecution ended with an affirm-
ative indication of innocence would paradoxically foreclose
a §1983 claim when the government’s case was weaker and
dismissed without explanation before trial, but allow a
claim when the government’s evidence was substantial
enough to proceed to trial. That would make little sense.
Finally, requiring a plaintiff to show that his prosecution
ended with an affirmative indication of innocence is not nec-
essary to protect officers from unwarranted civil suits—
among other things, officers are still protected by the re-
quirement that the plaintiff show the absence of probable
cause and by qualified immunity.
                         *    *    *
   In sum, we hold that a Fourth Amendment claim under
§1983 for malicious prosecution does not require the plain-
tiff to show that the criminal prosecution ended with some
affirmative indication of innocence. A plaintiff need only
show that the criminal prosecution ended without a convic-
tion. Thompson has satisfied that requirement here. We
express no view, however, on additional questions that may
be relevant on remand, including whether Thompson was
12                  THOMPSON v. CLARK

                     Opinion of the Court

ever seized as a result of the alleged malicious prosecution,
whether he was charged without probable cause, and
whether respondent is entitled to qualified immunity. On
remand, the Second Circuit or the District Court as appro-
priate may consider those and other pertinent questions.
We reverse the judgment of the U. S. Court of Appeals for
the Second Circuit and remand for further proceedings con-
sistent with this opinion.

                                             It is so ordered.
                 Cite as: 596 U. S. ____ (2022)            1

                      LITO, J., concurring
                     ALITO      dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 20–659
                         _________________


          LARRY THOMPSON, PETITIONER v.
               PAGIEL CLARK, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                        [April 4, 2022]

   JUSTICE ALITO, with whom JUSTICE THOMAS and
JUSTICE GORSUCH join, dissenting.
   Homer described the mythical chimera as a “grim mon-
ster” made of “all lion in front, all snake behind, all goat
between.” The Iliad p. 201 (R. Fagles trans. 1990). Today,
the Court creates a chimera of a constitutional tort by
stitching together elements taken from two very different
claims: a Fourth Amendment unreasonable seizure claim
and a common-law malicious-prosecution claim.
   The Court justifies this creation on the ground that mali-
cious prosecution is the common-law tort that is most anal-
ogous to an unreasonable seizure claim. And because a
common-law malicious-prosecution claim demanded proof
of a favorable termination, the Court holds that its new cre-
ation includes that element. But this Court has never held
that the Fourth Amendment houses a malicious-prosecu-
tion claim, and the Court defends its analogy with just two
sentences of independent analysis and a reference to a body
of lower court cases.
   I cannot agree with that approach. The Court’s independ-
ent analysis of this important question is far too cursory,
and its reliance on lower court cases is particularly ill-ad-
vised here because that body of case law appears to have
been heavily influenced by a mistaken reading of the plu-
rality opinion in Albright v. Oliver, 510 U. S. 266 (1994).
2                    THOMPSON v. CLARK

                      ALITO, J., dissenting

   What the Court has done is to recognize a novel hybrid
claim of uncertain scope that has no basis in the Constitu-
tion and is almost certain to lead to confusion.
                            I
  The Court asserts that malicious prosecution is the com-
mon-law tort that is most analogous to petitioner’s Fourth
Amendment claim, ante, at 5, but in fact the Fourth Amend-
ment and malicious prosecution have almost nothing in
common.
                                A
   The Fourth Amendment prohibits “unreasonable
searches and seizures.” And a Fourth Amendment claim
based on an unreasonable seizure has two indispensable
elements: (i) there must have been a “seizure,” i.e., an arrest
or some other use of “ ‘physical force’ or a ‘show of authority’
that ‘in some way restrain[s] the liberty’ of [a] person,”
Torres v. Madrid, 592 U. S. ___, ___ (2021) (slip op., at 3),
and (ii) the seizure must have been “unreasonable,” which
means, in the case of a full-blown arrest, that the officers
making the arrest must have lacked probable cause. Dis-
trict of Columbia v. Wesby, 583 U. S. ___, ___ (2018) (slip
op., at 7).
   Malicious prosecution, on the other hand, requires proof
that “(i) the suit or proceeding was ‘instituted without any
probable cause;’ (ii) the ‘motive in instituting’ the suit ‘was
malicious . . . ; and (iii) the prosecution ‘terminated in the
acquittal or discharge of the accused.’ ” Ante, at 6 (quoting
T. Cooley, Law of Torts 180 (1880) (Cooley)); see also Ma-
nuel v. Joliet, 580 U. S. 357, 378 (2017) (ALITO, J., dissent-
ing).
   A comparison of the elements of the malicious-prosecution
tort with the elements of a Fourth Amendment unreasona-
ble-seizure claim shows that there is no overlap. That is, a
plaintiff suing for unreasonable seizure need not prove any
                  Cite as: 596 U. S. ____ (2022)              3

                       ALITO, J., dissenting

of the elements of common-law malicious prosecution, and
a plaintiff suing for common-law malicious prosecution
need not prove any of the elements required to establish an
unreasonable seizure.
   Start with the elements of an unreasonable-seizure
claim. Such a claim does not require proof that there was a
“prosecution”—i.e., a criminal proceeding that is initiated
by the filing of charges in the form of a criminal complaint,
information, or indictment—while a malicious-prosecution
claim obviously requires a prosecution. See, e.g., 1 F. Hilli-
ard, The Law of Torts or Private Wrongs §2, pp. 413–414
(1866) (Hilliard) (“The general principle is laid down, that
an action lies for maliciously causing one to be indicted,
whereby he is damnified, either in person, reputation, or
property” (emphasis added)); Cooley 180 (“[I]t is a duty
which every man owes to every other not to institute pro-
ceedings maliciously, which he has no good reason to believe
are justified by the facts and the law” (emphasis added));
M. Newell, Law of Malicious Prosecution, False Imprison-
ment, and Abuse of Process §1, p. 3 (1892) (Newell) (same);
see also W. Prosser, Law of Torts 860 (1941) (“The interest
in freedom from unjustifiable litigation is protected by an
action for malicious prosecution” (boldface deleted and em-
phasis added)). A person who is arrested without probable
cause may have a viable unreasonable-seizure claim even if
he or she is released before any charges are filed.
   An unreasonable-seizure claim also does not require
“malice.” The Court has “almost uniformly rejected invita-
tions to probe subjective intent” in Fourth Amendment
cases. Ashcroft v. al-Kidd, 563 U. S. 731, 737 (2011). If a
law enforcement officer makes an arrest without probable
cause, the arrest is unreasonable and therefore unconstitu-
tional even if the officer harbors no ill will for the arrestee.
Likewise, if an officer makes an arrest with probable cause,
there is no Fourth Amendment violation regardless of the
“actual motivations of the individual officers involved.”
4                   THOMPSON v. CLARK

                      ALITO, J., dissenting

Whren v. United States, 517 U. S. 806, 813 (1996); see also
Cordova v. Albuquerque, 816 F. 3d 645, 664 (CA10 2016)
(Gorsuch, J., concurring in judgment).
   Finally, the validity of an unreasonable-seizure claim is
not dependent on the outcome of any prosecution that hap-
pens to follow a seizure. A person who is arrested without
probable cause but then convicted based on evidence discov-
ered after the arrest is not barred from recovering simply
because he or she cannot show a favorable termination to
the proceeding. See Wallace v. Kato, 549 U. S. 384, 389–
392 (2007); cf. Heck v. Humphrey, 512 U. S. 477, 487, n. 7
(1994) (a person may bring “a suit for damages attributable
to an allegedly unreasonable search” even if he or she was
convicted). Thus, an unreasonable-seizure claim may be
shown without proving any of the elements of a common-
law malicious-prosecution claim.
   Turning now to the elements of malicious prosecution, we
see that all of those may be established without proving ei-
ther of the two elements that the constitutional text and our
precedents require in order to establish an unreasonable
seizure.
   First, the tort of malicious prosecution does not require a
seizure within the meaning of the Fourth Amendment.
There are cases in which defendants charged with non-
violent crimes agree to appear for arraignment and are then
released pending trial on their own recognizance. These de-
fendants are prosecuted, and they may bring a common-law
suit for malicious prosecution if the other elements of that
tort can be shown, but they are not seized. See, e.g., 1 Hil-
liard §1, at 412 (noting that malicious prosecution may in-
volve “injury to the person, as connected with false impris-
onment,” but is “primarily . . . a wrong to character or
reputation”); 3 D. Dobbs, The Law of Torts §586, p. 388
(2011) (the “prosecution does not necessarily involve any
detention of the plaintiff at all”). The term seizure would
have to be given a novel and extravagant interpretation in
                 Cite as: 596 U. S. ____ (2022)            5

                     ALITO, J., dissenting

order to reach a “defendant awaiting trial on his own recog-
nizance” or one who simply receives a “summons to appear
at trial.” Cordova, 816 F. 3d, at 663 (opinion of Gorsuch,
J.).
  Second, since a malicious-prosecution claim does not re-
quire a seizure, it obviously does not require proof that the
person bringing suit was seized without probable cause.
The claim does demand proof that the person bringing suit
was prosecuted without probable cause, but probable cause
at the time of arrest is a different question from probable
cause at the time at which a prosecution is initiated.
  In light of the differences between these two claims, it is
apparent that a Fourth Amendment unreasonable-seizure
claim is not analogous to a claim for malicious prosecution.
Much more analogous are the common-law torts of false ar-
rest and false imprisonment, which protect against “[e]very
confinement of the person,” including one effected by “forci-
bly detaining [someone] in the public streets.” Wallace, 549
U. S., at 388–389 (internal quotation marks omitted); see
also Dobbs, Law of Torts §41 (describing elements of false
imprisonment and false arrest); Restatement (Second) of
Torts §35 (1964) (same).
                            B
  The Court does not make a serious effort to justify its
analogy between unreasonable seizure and malicious pros-
ecution. Instead, the Court largely relies on the fact that
“most of the Courts of Appeals to consider the question”
have drawn that analogy, ante, at 6, but the Court ignores
contrary lower court authority. See, e.g., Manuel v. Joliet,
903 F. 3d 667, 670 (CA7 2018); Jones v. Clark County, 959
F. 3d 748, 776–777 (CA6 2020) (Murphy, J., concurring in
part); Pagan-Gonzalez v. Moreno, 919 F. 3d 582, 608–617
(CA1 2019) (Barron, J., concurring). But in any event, we
should not decide this important question without inde-
pendent analysis, and the Court’s own cursory analysis is
6                    THOMPSON v. CLARK

                      ALITO, J., dissenting

erroneous.
   The Court claims that the “gravamen” of petitioner’s
Fourth Amendment claim is the same as that of a mali-
cious-prosecution claim: the “wrongful initiation of charges
without probable cause.” Ante, at 6. But what the Court
describes is not a Fourth Amendment violation at all. As
explained, that Amendment protects against “unreasonable
searches and seizures”—not the unreasonable “initiation of
charges.” In fact, “the specific provisions of the Bill of
Rights neither impose a standard for the initiation of a
prosecution” nor “require a pretrial hearing to weigh evi-
dence according to a given standard.” Albright, 510 U. S.,
at 282 (Kennedy, J., concurring in judgment); see also 4 W.
LaFave, J. Israel, N. King, & O. Kerr, Criminal Procedure
§14.2(a), pp. 329, 331 (4th ed. 2015) (noting that the Con-
stitution does not require “screening” of the decision to pros-
ecute “by some neutral body” to ensure “some minimal evi-
dence supporting the charge,” and “the sole constitutional
protection” is “what the Fourth Amendment requires to jus-
tify physical restraints”).
   The Court also says that the initiation of charges must be
“wrongful,” but it is not clear what that means. If that term
simply refers to the lack of probable cause, then the Court
has failed to capture the “gravamen” of malicious prosecu-
tion because that tort requires not just that the defendant
initiated charges “without probable cause” but also—as the
name of the tort suggests—that this was done with “mal-
ice.” See 1 Hilliard §4, at 416 (“want of probable cause” is
not enough “without malice”); 1 Newell §6, at 7 (“The plain-
tiff must show that the defendant acted from malicious mo-
tives in prosecuting him”). Cf. ante, at 6, n. 5 (claiming to
reserve the question whether the claim requires malice).
   If, on the other hand, the Court uses the term “wrongful”
to require “malice,” then the claim it has endorsed is even
more incompatible with the Fourth Amendment, which al-
                 Cite as: 596 U. S. ____ (2022)            7

                     ALITO, J., dissenting

most always imposes a purely objective standard. See su-
pra, at 4.
                            II
   The Court’s recognition of a Fourth Amendment mali-
cious-prosecution claim has no basis in our precedents.
                              A
   The Court relies on certain lower court decisions that ac-
cepted the strange concept of a Fourth Amendment mali-
cious-prosecution claim, but that line of cases developed in
large part because of a misunderstanding of the tersely
worded plurality opinion in Albright, 510 U. S. 266. See
Hernandez-Cuevas v. Taylor, 723 F. 3d 91, 99 (CA1 2013)
(noting that “dicta” in Albright led many jurisdictions to
“recogniz[e] a Fourth Amendment malicious prosecution
claim”). Instead of simply accepting that misreading, we
should explain what Albright actually decided and what the
plurality said.
   In that case, Kevin Albright was arrested and bound over
for trial without probable cause. The prosecution was dis-
missed before trial, and Albright then sued under 42
U. S. C. §1983. The District Court dismissed his suit; the
Court of Appeals affirmed the dismissal; and when the case
was argued in this Court, the only claim that Albright
pressed was that his prosecution without probable cause vi-
olated substantive due process. 510 U. S., at 268 (plurality
opinion). He did not advance either a Fourth Amendment
claim or a malicious-prosecution claim.
   This Court affirmed the dismissal of Albright’s substan-
tive due process claim, and while no opinion gained major-
ity approval, both the four Justices who joined the plurality
opinion and the three justices who concurred in the judg-
ment agreed that substantive due process does not include
the right to be free from prosecution without probable
8                    THOMPSON v. CLARK

                      ALITO, J., dissenting

cause. Id., at 268, 275 (plurality opinion); id., at 282 (opin-
ion of Kennedy, J.); id., at 286 (Souter, J., concurring in
judgment). That is all that Albright actually decided.
   The terse plurality opinion did make comments about the
Fourth Amendment and malicious prosecution, and those
comments have led to confusion in the lower courts. But a
careful reading of the plurality opinion shows that it in no
way suggested that the Fourth Amendment protects
against malicious prosecution.
   When the plurality commented on the Fourth Amend-
ment, it was addressing Albright’s prosecution-without-
probable-cause claim, not malicious prosecution. And in
connection with the prosecution-without-probable-cause
claim, the plurality made the following two points. First,
the plurality noted that “[w]here a particular Amendment
‘provides an explicit textual source of constitutional protec-
tion’ against a particular sort of government behavior, ‘that
Amendment, not the more generalized notion of “substan-
tive due process,” must be the guide for analyzing [the]
claims.’ ” Id., at 273. Second, the plurality observed that
the Fourth Amendment is the constitutional provision that
deals with “pretrial deprivations of liberty.” Id., at 274.
   What this discussion suggested was that if any provision
of the Constitution provided a home for Albright’s prosecu-
tion-without-probable-cause claim, the Fourth Amendment
was a better bet than the Fourteenth Amendment’s Due
Process Clause. But the plurality did not conclude or even
suggest that a prosecution-without-probable-cause claim
could be brought under the Fourth Amendment. See id., at
274–275 (expressly declining to express a view on the ques-
tion). Indeed, the plurality expressly reiterated that “the
accused is not ‘entitled to judicial oversight or review of the
decision to prosecute,’ ” suggesting instead that the harm to
Albright—if any—was that he was “not merely charged”
but also “submitted himself to arrest.” Id., at 274 (quoting
Gerstein v. Pugh, 420 U. S. 103, 114 (1975)).
                      Cite as: 596 U. S. ____ (2022)                     9

                          ALITO, J., dissenting

   As for malicious prosecution, the plurality did not even
hint that such a claim could be brought under the Fourth
Amendment. The plurality’s only two references to mali-
cious prosecution appeared in the portion of the opinion
that set out what had occurred in the lower courts. Foot-
note 3 recounted that Albright’s complaint contained a com-
mon-law malicious-prosecution claim but that this claim
had been dismissed without prejudice and that this issue
was not before the Court. 510 U. S., at 269, n. 3. Footnote
4 then observed that there was an “ ‘embarrassing diversity
of judicial opinion’ ” in the lower courts as to whether a ma-
licious-prosecution claim was actionable under §1983, and
the footnote added that substantive due process did not
“furnish the constitutional peg on which to hang such a
‘tort.’ ” Id., at 270–271, n. 4. But the plurality opinion did
not suggest that the Fourth Amendment could provide such
a “peg,” and neither did any other Justice who concurred in
the judgment.*
                             B
  Manuel v. Joliet, 580 U. S. 357, also provides no support
for a Fourth Amendment malicious-prosecution claim.
There, petitioner Elijah Manuel brought suit under the
Fourth Amendment, alleging that he was arrested without


——————
   *Justice Scalia’s concurring opinion made no mention of malicious
prosecution. Justice Ginsburg mentioned malicious prosecution only
when describing Albright’s claims, see 510 U. S., at 277, n. 1, and to note
that it was “anomalous” that Albright sought to hold a police officer (ra-
ther than a prosecutor) liable under a malicious-prosecution theory, id.,
at 279, n. 5. Justice Kennedy, joined by JUSTICE THOMAS, filed an opinion
concurring in the judgment and argued that “if a State did not provide a
tort remedy for malicious prosecution, there would be force to the argu-
ment that the malicious initiation of a baseless criminal prosecution in-
fringes an interest protected by the Due Process Clause.” Id., at 286.
But he did not suggest that a malicious-prosecution claim could be
brought under the Fourth Amendment.
10                  THOMPSON v. CLARK

                      ALITO, J., dissenting

probable cause and then held for seven weeks without prob-
able cause after a judge ordered him detained. Id., at 359–
360. The Court reasoned that the Fourth Amendment pro-
hibits “government officials from detaining a person in the
absence of probable cause.” Id., at 367. A violation of that
prohibition, the Court continued, may occur both “before
the formal onset of a criminal proceeding” and “when legal
process itself goes wrong—when, for example, a judge’s
probable-cause determination is predicated solely on a po-
lice officer’s false statements.” Ibid. Accordingly, the Court
concluded that the plaintiff in that case could state a Fourth
Amendment claim because the “judge’s order holding [him]
for trial” was not supported by probable cause. Id., at 368.
   Although the majority asserts that Manuel authorized
Fourth Amendment malicious-prosecution claims, see ante,
at 4, Manuel did no such thing. That decision expressly de-
clined to determine “whether (and, if so, how) [petitioner’s
Fourth Amendment claim] should resemble the malicious
prosecution tort.” Id., at 372, n. 10. Indeed, the majority’s
analysis here is incompatible with the analysis in Manuel,
where the gravamen of the wrong was that petitioner was
“detain[ed] . . . in the absence of probable cause.” Id., at
367. Manuel thus provides no support for the Court’s sug-
gestion that the Fourth Amendment prohibits the “initia-
tion of charges without probable cause.” Ante, at 6.
                               III
  Instead of clarifying the law regarding §1983 malicious-
prosecution claims, today’s decision, I fear, will sow more
confusion. The Court endorses a Fourth Amendment claim
for malicious prosecution that appears to have the following
elements: (1) the defendant “initiat[ed]” charges against the
plaintiff in a way that was “wrongful” and “without proba-
ble cause,” (2) the “malicious prosecution resulted in a sei-
zure of the plaintiff,” and (3) the prosecution must not have
ended in conviction. Ante, at 5–6, and n. 2. This tort has
                  Cite as: 596 U. S. ____ (2022)           11

                      ALITO, J., dissenting

no precedent in Fourth Amendment law. It is markedly dif-
ferent from the common-law tort of malicious prosecution,
and its dimensions are uncertain.
  First, it is not clear why this tort requires both a seizure
and a prosecution. As noted, the two do not always go to-
gether, and if the aim is to permit the victims of malicious
prosecution to sue under §1983, it is not clear why detention
should be required. While pretrial detention certainly in-
creases the harm inflicted by a malicious prosecution, such
a prosecution can be very damaging even if the victim is
never detained. See, e.g., M. Bigelow, The Law of Torts 204
(1875) (a plaintiff may show damage to “his person by im-
prisonment, his reputation by the scandal, or . . . his prop-
erty by the expense”). The majority’s only answer to the
question why the claim requires a seizure is that it is
“housed in the Fourth Amendment,” ante, at 5, n. 2, but
that response begs the antecedent question whether the
Fourth Amendment houses a malicious-prosecution suit at
all.
  Second, where the person bringing suit under §1983 is
arrested and then prosecuted, it is not clear whether both
the arrest and the prosecution must have been done with-
out probable cause and without a legitimate law enforce-
ment purpose. An arrest made without probable cause may
be followed by a prosecution based on new evidence that
clearly establishes probable cause. And by the same token,
the evidence that establishes probable cause at the time of
arrest may be thoroughly discredited at some point well be-
fore the termination of a prosecution.
  Third and most important, it is not clear what the Court
means when it says that the “gravamen” of the claim is
“wrongful initiation of charges without probable cause.”
Ante, at 6. Since the Court refers repeatedly to “malicious
prosecution,” one might think that this requires a guilty
mental state, but in a footnote, the Court raises the possi-
bility that the constitutional tort it recognizes may require
12                   THOMPSON v. CLARK

                       ALITO, J., dissenting

nothing more than the absence of probable cause. See ibid.,
n. 3.
   If that turns out to be so, it is hard to see even the slight-
est connection between the Court’s new tort and common-
law malicious prosecution. Malice is the hallmark of a
malicious-prosecution claim. Even if a prosecution is
brought and maintained without probable cause, a
malicious-prosecution claim cannot succeed without proof
of malice. See supra, at 6. And if the Court’s new tort has
nothing to do with malicious prosecution, what possible rea-
son can there be for borrowing that tort’s favorable-termi-
nation element?
                              IV
   Instead of creating a new hybrid claim, we should simply
hold that a malicious-prosecution claim may not be brought
under the Fourth Amendment. Such a holding would not
leave a person in petitioner’s situation without legal protec-
tion. Petitioner brought Fourth Amendment claims against
respondents for false arrest, excessive force, and unlawful
entry, but after trial a jury ruled against him on all those
claims. See App. 142–146. Petitioner could have also
sought relief under state law. See, e.g., Cordova, 816 F. 3d,
at 662 (opinion of Gorsuch, J.). New York law appears to
recognize a malicious-prosecution tort with an element very
much like the favorable-termination element that the Court
adopts today, see Lanning v. Glens Falls, 908 F. 3d 19, 24–
25 (CA2 2018), but petitioner chose not to bring such a
claim. See Tr. of Oral Arg. 40–41.
   For these reasons, I would affirm the judgment below,
and I therefore respectfully dissent.

```

---
