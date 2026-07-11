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

## GROUP: _overhaul2/lake/cases/Delaware v. Prouse.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Delaware v. Prouse"
type: case
citation: "440 U.S. 648 (1979)"
parallel_cite: "99 S. Ct. 1391; 59 L. Ed. 2d 660"
neutral_cite: 1979 U.S. LEXIS 80
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-03-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-03-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Delaware v. Prouse
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110045/delaware-v-prouse/"
  cluster_id: 110045
  opinion_id: 110045
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Related (cross-doctrine)"
related: ["[[Heien v. North Carolina]]", "[[City of Indianapolis v. Edmond]]", "[[Whren v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "reasonable-suspicion", "random-stop", "license-check"]
holding: "Random, suspicionless stops of motorists to check license and registration are unreasonable under the Fourth Amendment; an officer needs…"
lake:
  record_id: Delaware v. Prouse
  status: verified
  projected_at: 2026-07-06
---

# Delaware v. Prouse

*440 U.S. 648 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A patrolman, acting on no observed violation or articulable suspicion, stopped Prouse's car solely to check his license and registration; he smelled and then saw marijuana in plain view, leading to charges. Prouse moved to suppress, and the Delaware courts held the random, suspicionless stop unconstitutional.

## Issue
Whether police may stop a motorist to check his driver's license and registration without any articulable and reasonable suspicion of wrongdoing.

## Rule
No. "[W]e hold that except in those situations in which there is at least articulable and reasonable suspicion that a motorist is unlicensed or that an automobile is not registered, or that either the vehicle or an occupant is otherwise subject to seizure for violation of law, stopping an automobile and detaining the driver in order to check his driver's license and the registration of the automobile are unreasonable under the Fourth Amendment." — 440 U.S. 648, 663. ^pin-663

The Court left open less-intrusive, non-discretionary alternatives such as questioning all traffic at fixed roadblock-type checkpoints.

## Application
The officer stopped Prouse without observing any traffic or equipment violation and without any reasonable suspicion that he was unlicensed, the car unregistered, or anyone subject to seizure — the stop was admittedly random and at the officer's unbridled discretion. Because such a discretionary, suspicionless spot check is unreasonable, the stop was unconstitutional and the marijuana it produced should have been suppressed.

## Conclusion
The random, suspicionless license-check stop violated the Fourth Amendment; the suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Prouse* requires individualized suspicion for discretionary traffic stops while preserving non-discretionary checkpoints — a line developed in [[City of Indianapolis v. Edmond]] and complemented by the reasonable-mistake rule of [[Heien v. North Carolina]].

## Appears on
- [[Traffic Stops]] — *Key — Progeny / Refinement*

## Sources
- *Delaware v. Prouse*, 440 U.S. 648 (1979) — https://www.courtlistener.com/opinion/110045/delaware-v-prouse/ — pinpoint: 663.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1e3cdfa0bca0dd67", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Delaware v. Prouse"}, "payload": {"all": [{"cite": "440 U.S. 648", "page": "648", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "440"}, {"cite": "99 S. Ct. 1391", "page": "1391", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "59 L. Ed. 2d 660", "page": "660", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "59"}, {"cite": "1979 U.S. LEXIS 80", "page": "80", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "440 U.S. 648", "official": {"cite": "440 U.S. 648", "page": "648", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "440"}, "official_selection_present": true, "record_id": "Delaware v. Prouse"}}
{"assertion_id": "c00227f191e56c39", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-663", "record_id": "Delaware v. Prouse"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-663", "pinpoint_status": "slip-only", "quote": "--- # Delaware v. Prouse *440 U.S. 648 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A patrolman, acting on no observed violation or articulable suspicion, stopped Prouse's car solely to check his license and registration; he smelled and then saw marijuana in plain view, leading to charges. Prouse moved to suppress, and the Delaware courts held the random, suspicionless stop unconstitutional. ## Issue Whether police may stop a motorist to check his driver's license and registration without any articulable and reasonable suspicion of wrongdoing. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Delaware v. Prouse", "star_marker": null}}
{"assertion_id": "1d2c7b7194ee874b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Delaware v. Prouse"}, "payload": {"as_of_content": "1979-03-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Delaware v. Prouse", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Delaware v. Prouse

```json
{
  "schema_version": "s2.v1",
  "record_id": "Delaware v. Prouse",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Delaware v. Prouse",
    "case_name_short": "Prouse",
    "case_name_full": "Delaware v. Prouse",
    "input_case_name": "Delaware v. Prouse",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-03-27",
    "year": 1979,
    "docket": null,
    "cluster_id": 110045,
    "lead_opinion_id": 110045,
    "sibling_ids": [
      110045,
      9427509,
      9427510,
      9427511
    ],
    "absolute_url": "/opinion/110045/delaware-v-prouse/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "440 U.S. 648",
      "volume": "440",
      "reporter": "U.S.",
      "page": "648",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1391",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 660",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "660",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 80",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "80",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "440 U.S. 648",
        "volume": "440",
        "reporter": "U.S.",
        "page": "648",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1391",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 660",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "660",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 80",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "80",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "440 U.S. 648",
    "official_selection": {
      "court_class": "scotus",
      "selected": "440 U.S. 648",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-663",
      "page": null,
      "quote": "--- # Delaware v. Prouse *440 U.S. 648 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A patrolman, acting on no observed violation or articulable suspicion, stopped Prouse's car solely to check his license and registration; he smelled and then saw marijuana in plain view, leading to charges. Prouse moved to suppress, and the Delaware courts held the random, suspicionless stop unconstitutional. ## Issue Whether police may stop a motorist to check his driver's license and registration without any articulable and reasonable suspicion of wrongdoing. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-03-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Delaware v. Prouse",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane1_negative"
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
        "journal_ref": "Delaware v. Prouse:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 9352626,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 6466320,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane1_negative"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. McCollan",
          "cluster_id": 110132,
          "cite": [
            "61 L. Ed. 2d 433",
            "99 S. Ct. 2689",
            "443 U.S. 137",
            "1979 U.S. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Railway Labor Executives' Assn.",
          "cluster_id": 112219,
          "cite": [
            "103 L. Ed. 2d 639",
            "109 S. Ct. 1402",
            "489 U.S. 602",
            "1989 U.S. LEXIS 1568",
            "4 I.E.R. Cas. (BNA) 224",
            "1989 CCH OSHD 28,476",
            "57 U.S.L.W. 4324",
            "13 OSHC (BNA) 2065",
            "130 L.R.R.M. (BNA) 2857",
            "49 Empl. Prac. Dec. (CCH) 38,791"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Kennedy",
          "cluster_id": 110714,
          "cite": [
            "72 L. Ed. 2d 416",
            "102 S. Ct. 2083",
            "456 U.S. 667",
            "1982 U.S. LEXIS 111",
            "50 U.S.L.W. 4544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkxNTc0NDAwMDAwJnM9NDc2MDAwMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110045+OR+9427509+OR+9427510+OR+9427511%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05ODUmcz0xNDU2NDAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110045+OR+9427509+OR+9427510+OR+9427511%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511)",
        "reviewed": 109,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 109,
        "triage_read": 2,
        "triage_snippet_classified": 107
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511)",
    "indexed_citing_opinions": 3221,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110045,
        "count": 2856,
        "count_source": "search"
      },
      {
        "opinion_id": 9427509,
        "count": 435,
        "count_source": "search"
      },
      {
        "opinion_id": 9427510,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427511,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5550,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/delaware-v-prouse.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMzEyODUmcz0xMDQ2MjY1NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110045+OR+9427509+OR+9427510+OR+9427511%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110045,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 102505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 274285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 299088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 321729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 332182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 348709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1087989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1190270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1332651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1367261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1442373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1471204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1500552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1518042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1701839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1778812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1893463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 2170567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 2354841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 2378216,
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
    "date_created": "2026-07-05T02:20:37Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:20:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:20:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:20:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Delaware v. Prouse

```
<div>
<center><b><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648</a></span> (1979)</b></center>
<center><h1>DELAWARE<br>
v.<br>
PROUSE.</h1></center>
<center>No. 77-1571.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 17, 1979.</center>
<center>Decided March 27, 1979.</center>
CERTIORARI TO THE SUPREME COURT OF DELAWARE.
<p><span class="star-pagination">*649</span> <i>Charles M. Oberly III</i> argued the cause for petitioner. With him on the brief were <i>Richard R. Wier, Jr.,</i> Attorney General of Delaware, and <i>Carolyn Berger, Fred S. Silverman,</i> and <i>Kathleen Molyneux,</i> Deputy Attorneys General.</p>
<p><i>David M. Lukoff</i> argued the cause for respondent. With him on the brief were <i>Richard M. Baumeister, Frank Askin,</i> and <i>Eric Neisser.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*650</span> MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>The question is whether it is an unreasonable seizure under the Fourth and Fourteenth Amendments to stop an automobile, being driven on a public highway, for the purpose of checking the driving license of the operator and the registration of the car, where there is neither probable cause to believe nor reasonable suspicion that the car is being driven contrary to the laws governing the operation of motor vehicles or that either the car or any of its occupants is subject to seizure or detention in connection with the violation of any other applicable law.</p>
<p></p>
<h2>I</h2>
<p>At 7:20 p. m. on November 30, 1976, a New Castle County, Del., patrolman in a police cruiser stopped the automobile occupied by respondent.<sup>[1]</sup> The patrolman smelled marihuana smoke as he was walking toward the stopped vehicle, and he seized marihuana in plain view on the car floor. Respondent was subsequently indicted for illegal possession of a controlled substance. At a hearing on respondent's motion to suppress the marihuana seized as a result of the stop, the patrolman testified that prior to stopping the vehicle he had observed neither traffic or equipment violations nor any suspicious activity, and that he made the stop only in order to check the driver's license and registration. The patrolman was not acting pursuant to any standards, guidelines, or procedures pertaining to document spot checks, promulgated by either his department or the State Attorney General. Characterizing the stop as "routine," the patrolman explained, "I saw the car <span class="star-pagination">*651</span> in the area and wasn't answering any complaints, so I decided to pull them off." App. A9. The trial court granted the motion to suppress, finding the stop and detention to have been wholly capricious and therefore violative of the Fourth Amendment.</p>
<p>The Delaware Supreme Court affirmed, noting first that "[t]he issue of the legal validity of systematic, roadblock-type stops of a number of vehicles for license and vehicle registration check is <i>not</i> now before the Court," <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1362" aria-description="Citation for case: State v. Prouse">382 A. 2d 1359, 1362</a></span> (1978) (emphasis in original). The court held that "a random stop of a motorist in the absence of specific articulable facts which justify the stop by indicating a reasonable suspicion that a violation of the law has occurred is constitutionally impermissible and violative of the Fourth and Fourteenth Amendments to the United States Constitution." <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1364" aria-description="Citation for case: State v. Prouse"><i>Id.,</i> at 1364</a></span>. We granted certiorari to resolve the conflict between this decision, which is in accord with decisions in five other jurisdictions,<sup>[2]</sup> and the contrary determination in six jurisdictions<sup>[3]</sup> that the Fourth Amendment does not prohibit the kind of automobile stop that occurred here. <span class="citation multiple-matches"><a href="/c/U.%20S./439/816/">439 U. S. 816</a></span> (1978).</p>
<p></p>
<h2>II</h2>
<p>Because the Delaware Supreme Court held that the stop at issue not only violated the Federal Constitution but also <span class="star-pagination">*652</span> was impermissible under Art. I, § 6, of the Delaware Constitution, it is urged that the judgment below was based on an independent and adequate state ground and that we therefore have no jurisdiction in this case. <i>Fox Film Corp.</i> v. <i>Muller,</i> <span class="citation" data-id="102505"><a href="/opinion/102505/fox-film-corp-v-muller/#210" aria-description="Citation for case: Fox Film Corp. v. Muller">296 U. S. 207, 210</a></span> (1935). At least, it is suggested, the matter is sufficiently uncertain that we should remand for clarification as to the ground upon which the judgment rested. <i>California</i> v. <i>Krivda,</i> <span class="citation" data-id="108622"><a href="/opinion/108622/california-v-krivda/#35" aria-description="Citation for case: California v. Krivda">409 U. S. 33, 35</a></span> (1972). Based on our reading of the opinion, however, we are satisfied that even if the State Constitution would have provided an adequate basis for the judgment, the Delaware Supreme Court did not intend to rest its decision independently on the State Constitution and that we have jurisdiction of this case.</p>
<p>As we understand the opinion below, Art I, § 6, of the Delaware Constitution will automatically be interpreted at least as broadly as the Fourth Amendment;<sup>[4]</sup> that is, every police practice authoritatively determined to be contrary to the Fourth and Fourteenth Amendments will, without further analysis, be held to be contrary to Art. I, § 6. This approach, which is consistent with previous opinions of the Delaware Supreme Court,<sup>[5]</sup> was followed in this case. The court analyzed <span class="star-pagination">*653</span> the various decisions interpreting the Federal Constitution, concluded that the Fourth Amendment foreclosed spot checks of automobiles, and summarily held that the State Constitution was therefore also infringed. This is one of those cases where "at the very least, the [state] court felt compelled by what it understood to be federal constitutional considerations to construe . . . its own law in the manner it did." <i>Zacchini</i> v. <i>Scripps-Howard Broadcasting Co.,</i> <span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/#568" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">433 U. S. 562, 568</a></span> (1977). Had state law not been mentioned at all, there would be no question about our jurisdiction, even though the State Constitution might have provided an independent and adequate state ground. <i><span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">Ibid.</a></span></i> The same result should follow here where the state constitutional holding depended upon the state court's view of the reach of the Fourth and Fourteenth Amendments. If the state court misapprehended federal law, "[i]t should be freed to decide . . . these suits according to its own local law." <i>Missouri ex rel. Southern R. Co.</i> v. <i>Mayfield,</i> <span class="citation" data-id="9527085"><a href="/opinion/1087989/missouri-ex-rel-southern-railway-co-v-mayfield/#5" aria-description="Citation for case: Missouri Ex Rel. Southern Railway Co. v. Mayfield">340 U. S. 1, 5</a></span> (1950).</p>
<p></p>
<h2>III</h2>
<p>The Fourth and Fourteenth Amendments are implicated in this case because stopping an automobile and detaining its occupants constitute a "seizure" within the meaning of those Amendments, even though the purpose of the stop is limited and the resulting detention quite brief. <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556-558</a></span> (1976); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); cf. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16</a></span> (1968). The essential purpose of the proscriptions in the Fourth Amendment is to impose a standard <span class="star-pagination">*654</span> of "reasonableness"<sup>[6]</sup> upon the exercise of discretion by government officials, including law enforcement agents, in order " `to safeguard the privacy and security of individuals against arbitrary invasions. . . .' " <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312</a></span> (1978), quoting <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967).<sup>[7]</sup> Thus, the permissibility of a particular law enforcement practice is judged by balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate governmental interests.<sup>[8]</sup> Implemented in this manner, the reasonableness standard usually requires, at a minimum, that the facts upon which an intrusion is based be capable of measurement against "an objective standard,"<sup>[9]</sup> whether this be probable cause<sup>[10]</sup> or a less stringent test.<sup>[11]</sup> In those situations in which the balance of interests precludes insistence upon "some quantum <span class="star-pagination">*655</span> of individualized suspicion,"<sup>[12]</sup> other safeguards are generally relied upon to assure that the individual's reasonable expectation of privacy is not "subject to the discretion of the official in the field," <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>. See <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>id.,</i> at 534-535</a></span>; <i>Marshall</i> v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#320" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>Barlow's, Inc., supra,</i> at 320-321</a></span>; <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#322" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 322-323</a></span> (1972) (requiring warrants).</p>
<p>In this case, however, the State of Delaware urges that patrol officers be subject to no constraints in deciding which automobiles shall be stopped for a license and registration check because the State's interest in discretionary spot checks as a means of ensuring the safety of its roadways outweighs the resulting intrusion on the privacy and security of the persons detained.</p>
<p></p>
<h2>IV</h2>
<p>We have only recently considered the legality of investigative stops of automobiles where the officers making the stop have neither probable cause to believe nor reasonable suspicion that either the automobile or its occupants are subject to seizure under the applicable criminal laws. In <i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce, supra</a></span></i><i>,</i> Border Patrol agents conducting roving patrols in areas near the international border asserted statutory authority to stop at random any vehicle in order to determine whether it contained illegal aliens or was involved in smuggling operations. The practice was held to violate the Fourth Amendment, but the Court did not invalidate all warrantless automobile stops upon less than probable cause. Given "the importance of the governmental interest at stake, the minimal intrusion of a brief stop, and the absence of practical alternatives for policing the border," <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 881</a></span>, the Court analogized the roving-patrol stop to the on-the-street encounter addressed in <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> and held:</p>
<blockquote>"Except at the border and its functional equivalents, officers on roving patrol may stop vehicles only if they are <span class="star-pagination">*656</span> aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion that the vehicles contain aliens who may be illegally in the country." <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 884</a></span> (footnote omitted).</blockquote>
<p>Because "the nature of illegal alien traffic and the characteristics of smuggling operations tend to generate articulable grounds for identifying violators," <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>id.,</i> at 883</a></span>, "a requirement of reasonable suspicion for stops allows the Government adequate means of guarding the public interest and also protects residents of the border areas from indiscriminate official interference." <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Ibid.</a></span></i></p>
<p>The constitutionality of stops by Border Patrol agents was again before the Court in <i>United States</i> v. <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra</a></span></i><i>,</i> in which we addressed the permissibility of checkpoint operations. This practice involved slowing all oncoming traffic "to a virtual, if not a complete, halt," <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#546" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 546</a></span>, at a highway roadblock, and referring vehicles chosen at the discretion of Border Patrol agents to an area for secondary inspection. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#546" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>id.,</i> at 546, 558</a></span>. Recognizing that the governmental interest involved was the same as that furthered by roving-patrol stops, the Court nonetheless sustained the constitutionality of the Border Patrol's checkpoint operations. The crucial distinction was the lesser intrusion upon the motorist's Fourth Amendment interests:</p>
<blockquote>"[The] objective intrusionthe stop itself, the questioning, and the visual inspectionalso existed in roving-patrol stops. But we view checkpoint stops in a different light because the subjective intrusionthe generating of concern or even fright on the part of lawful travelersis appreciably less in the case of a checkpoint stop." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 558</a></span>.</blockquote>
<p>Although not dispositive,<sup>[13]</sup> these decisions undoubtedly provide <span class="star-pagination">*657</span> guidance in balancing the public interest against the individual's Fourth Amendment interests implicated by the practice of spot checks such as occurred in this case. We cannot agree that stopping or detaining a vehicle on an ordinary city street is less intrusive than a roving-patrol stop on a major highway and that it bears greater resemblance to a permissible stop and secondary detention at a checkpoint near the border. In this regard, we note that <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> was not limited to roving-patrol stops on limited-access roads, but applied to any roving-patrol stop by Border Patrol agents on any type of roadway on less than reasonable suspicion. See <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 882-883</a></span>; <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#894" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 894</a></span> (1975). We cannot assume that the physical and psychological intrusion visited upon the occupants of a vehicle by a random stop to check documents is of any less moment than that occasioned by a stop by border agents on roving patrol. Both of these stops generally entail law enforcement officers signaling a moving automobile to pull over to the side of the roadway, by means of a possibly unsettling show of authority. Both interfere with freedom of movement, are inconvenient, and consume time. Both may create substantial anxiety. For Fourth Amendment purposes, we also see insufficient resemblance between sporadic and random stops of individual vehicles making their way through city traffic and those stops occasioned by roadblocks where all vehicles are brought to a halt or to a near halt, and all are subjected to a show of the police power of the community. "At traffic checkpoints the motorist can see that other vehicles are being stopped, he can see visible signs of the officers' authority, and he is much less likely to be frightened or annoyed by the intrusion." <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#894" aria-description="Citation for case: United States v. Ortiz"><i>Id.,</i> at 894-895</a></span>, quoted in <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 558</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*658</span> V</h2>
<p>But the State of Delaware urges that even if discretionary spot checks such as occurred in this case intrude upon motorists as much as or more than do the roving patrols held impermissible in <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> these stops are reasonable under the Fourth Amendment because the State's interest in the practice as a means of promoting public safety upon its roads more than outweighs the intrusion entailed. Although the record discloses no statistics concerning the extent of the problem of lack of highway safety, in Delaware or in the Nation as a whole, we are aware of the danger to life<sup>[14]</sup> and property posed by vehicular traffic and of the difficulties that even a cautious and an experienced driver may encounter. We agree that the States have a vital interest in ensuring that only those qualified to do so are permitted to operate motor vehicles, that these vehicles are fit for safe operation, and hence that licensing, registration, and vehicle inspection requirements are being observed. Automobile licenses are issued periodically to evidence that the drivers holding them are sufficiently familiar with the rules of the road and are physically qualified to operate a motor vehicle.<sup>[15]</sup> The registration requirement and, more pointedly, the related annual inspection requirement in Delaware<sup>[16]</sup> are designed to keep dangerous automobiles off the road. Unquestionably, these provisions, properly administered, are essential elements in a highway safety program. Furthermore, we note that the State of Delaware requires a minimum amount of insurance <span class="star-pagination">*659</span> coverage as a condition to automobile registration,<sup>[17]</sup> implementing its legitimate interest in seeing to it that its citizens have protection when involved in a motor vehicle accident.<sup>[18]</sup></p>
<p>The question remains, however, whether in the service of these important ends the discretionary spot check is a sufficiently productive mechanism to justify the intrusion upon Fourth Amendment interests which such stops entail. On the record before us, that question must be answered in the negative. Given the alternative mechanisms available, both those in use and those that might be adopted, we are unconvinced that the incremental contribution to highway safety of the random spot check justifies the practice under the Fourth Amendment.</p>
<p>The foremost method of enforcing traffic and vehicle safety regulations, it must be recalled, is acting upon observed violations. Vehicle stops for traffic violations occur countless times each day; and on these occasions, licenses and registration papers are subject to inspection and drivers without them will be ascertained. Furthermore, drivers without licenses are presumably the less safe drivers whose propensities may well exhibit themselves.<sup>[19]</sup> Absent some empirical data to the contrary, it must be assumed that finding an unlicensed driver among those who commit traffic violations is a much more likely event than finding an unlicensed driver by choosing randomly from the entire universe of drivers. If this were not so, licensing of drivers would hardly be an effective means of promoting roadway safety. It seems common sense that the <span class="star-pagination">*660</span> percentage of all drivers on the road who are driving without a license is very small and that the number of licensed drivers who will be stopped in order to find one unlicensed operator will be large indeed. The contribution to highway safety made by discretionary stops selected from among drivers generally will therefore be marginal at best. Furthermore, and again absent something more than mere assertion to the contrary, we find it difficult to believe that the unlicensed driver would not be deterred by the possibility of being involved in a traffic violation or having some other experience calling for proof of his entitlement to drive but that he would be deterred by the possibility that he would be one of those chosen for a spot check. In terms of actually discovering unlicensed drivers or deterring them from driving, the spot check does not appear sufficiently productive to qualify as a reasonable law enforcement practice under the Fourth Amendment.</p>
<p>Much the same can be said about the safety aspects of automobiles as distinguished from drivers. Many violations of minimum vehicle-safety requirements are observable, and something can be done about them by the observing officer, directly and immediately. Furthermore, in Delaware, as elsewhere, vehicles must carry and display current license plates,<sup>[20]</sup> which themselves evidence that the vehicle is properly registered;<sup>[21]</sup> and, under Delaware law, to qualify for annual registration a vehicle must pass the annual safety inspection<sup>[22]</sup> and be properly insured.<sup>[23]</sup> It does not appear, therefore, that a stop of a Delaware-registered vehicle is necessary in order to ascertain compliance with the State's registration requirements; and, because there is nothing to <span class="star-pagination">*661</span> show that a significant percentage of automobiles from other States do not also require license plates indicating current registration, there is no basis for concluding that stopping even out-of-state cars for document checks substantially promotes the State's interest.</p>
<p>The marginal contribution to roadway safety possibly resulting from a system of spot checks cannot justify subjecting every occupant of every vehicle on the roads to a seizure limited in magnitude compared to other intrusions but nonetheless constitutionally cognizableat the unbridled discretion of law enforcement officials. To insist neither upon an appropriate factual basis for suspicion directed at a particular automobile nor upon some other substantial and objective standard or rule to govern the exercise of discretion "would invite intrusions upon constitutionally guaranteed rights based on nothing more substantial than inarticulate hunches . . . ." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. By hypothesis, stopping apparently safe drivers is necessary only because the danger presented by some drivers is not observable at the time of the stop. When there is not probable cause to believe that a driver is violating any one of the multitude of applicable traffic and equipment regulations<sup>[24]</sup>or other articulable basis amounting to reasonable suspicion that the driver is unlicensed or his vehicle unregisteredwe cannot conceive of any legitimate basis upon which a patrolman could decide that stopping a particular driver for a spot check would be more productive than stopping any other driver. This kind of standardless and unconstrained discretion is the evil the Court has discerned when in previous cases it has insisted that the discretion of the official in the field be circumscribed, at least to some extent. <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#270" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 270</a></span> (1973); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532-533</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*662</span> VI</h2>
<p>The "grave danger" of abuse of discretion, <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#559" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 559</a></span>, does not disappear simply because the automobile is subject to state regulation resulting in numerous instances of police-citizen contact, <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441</a></span> (1973). Only last Term we pointed out that "if the government intrudes . . . the privacy interest suffers whether the government's motivation is to investigate violations of criminal laws or breaches of other statutory or regulatory standards." <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 312-313</a></span>. There are certain "relatively unique circumstances," <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>id.,</i> at 313</a></span>, in which consent to regulatory restrictions is presumptively concurrent with participation in the regulated enterprise. See <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972) (federal regulation of firearms); <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970) (federal regulation of liquor). Otherwise, regulatory inspections unaccompanied by any quantum of individualized, articulable suspicion must be undertaken pursuant to previously specified "neutral criteria." <i>Marshall</i> v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>Barlow's, Inc., supra,</i> at 323</a></span>.</p>
<p>An individual operating or traveling in an automobile does not lose all reasonable expectation of privacy simply because the automobile and its use are subject to government regulation.<sup>[25]</sup> Automobile travel is a basic, pervasive, and often necessary mode of transportation to and from one's home, workplace, and leisure activities. Many people spend more hours each day traveling in cars than walking on the streets. Undoubtedly, many find a greater sense of security and privacy in traveling in an automobile than they do in exposing themselves by pedestrian or other modes of travel. Were the <span class="star-pagination">*663</span> individual subject to unfettered governmental intrusion every time he entered an automobile, the security guaranteed by the Fourth Amendment would be seriously circumscribed. As <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> recognized, people are not shorn of all Fourth Amendment protection when they step from their homes onto the public sidewalks. Nor are they shorn of those interests when they step from the sidewalks into their automobiles. See <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972).</p>
<p></p>
<h2>VII</h2>
<p>Accordingly, we hold that except in those situations in which there is at least articulable and reasonable suspicion that a motorist is unlicensed or that an automobile is not registered, or that either the vehicle or an occupant is otherwise subject to seizure for violation of law, stopping an automobile and detaining the driver in order to check his driver's license and the registration of the automobile are unreasonable under the Fourth Amendment. This holding does not preclude the State of Delaware or other States from developing methods for spot checks that involve less intrusion or that do not involve the unconstrained exercise of discretion.<sup>[26]</sup> Questioning of all oncoming traffic at roadblock-type stops is one possible alternative. We hold only that persons in automobiles on public roadways may not for that reason alone have their travel and privacy interfered with at the unbridled discretion of police officers. The judgment below is affirmed.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE BLACKMUN, with whom MR. JUSTICE POWELL joins, concurring.</p>
<p>The Court, <i>ante,</i> this page, carefully protects from the reach of its decision other less intrusive spot checks "that do not involve <span class="star-pagination">*664</span> the unconstrained exercise of discretion." The roadblock stop for all traffic is given as an example. I necessarily assume that the Court's reservation also includes other not purely random stops (such as every 10th car to pass a given point) that equate with, but are less intrusive than, a 100% roadblock stop. And I would not regard the present case as a precedent that throws any constitutional shadow upon the necessarily somewhat individualized and perhaps largely random examinations by game wardens in the performance of their duties. In a situation of that type, it seems to me, the Court's balancing process, and the value factors under consideration, would be quite different.</p>
<p>With this understanding, I join the Court's opinion and its judgment.</p>
<p>MR. JUSTICE REHNQUIST, dissenting.</p>
<p>The Court holds, in successive sentences, that absent an articulable, reasonable suspicion of unlawful conduct, a motorist may not be subjected to a random license check, but that the States are free to develop "methods for spot checks that . . . do not involve the unconstrained exercise of discretion," such as "[q]uestioning . . . all oncoming traffic at road-block-type stops . . . ." <i>Ante,</i> at 663. Because motorists, apparently like sheep, are much less likely to be "frightened" or "annoyed" when stopped en masse, a highway patrolman needs neither probable cause nor articulable suspicion to stop <i>all</i> motorists on a particular thoroughfare, but he cannot without articulable suspicion stop <i>less</i> than all motorists. The Court thus elevates the adage "misery loves company" to a novel role in Fourth Amendment jurisprudence. The rule becomes "curiouser and curiouser" as one attempts to follow the Court's explanation for it.</p>
<p>As the Court correctly points out, people are not shorn of their Fourth Amendment protection when they step from their homes onto the public sidewalks or from the sidewalks into <span class="star-pagination">*665</span> their automobiles. But a random license check of a motorist operating a vehicle on highways owned and maintained by the State is quite different from a random stop designed to uncover violations of laws that have nothing to do with motor vehicles.<sup>[*]</sup> No one questions that the State may require the licensing of those who drive on its highways and the registration of vehicles which are driven on those highways. If it may insist on these requirements, it obviously may take steps necessary to enforce compliance. The reasonableness of the enforcement measure chosen by the State is tested by weighing its intrusion on the motorists' Fourth Amendment interests against its promotion of the State's legitimate interests. <i>E. g., </i><i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975).</p>
<p>In executing this balancing process, the Court concludes that given the alternative mechanisms available, discretionary spot checks are not a "sufficiently productive mechanism" to safeguard the State's admittedly "vital interest in ensuring that only those qualified to do so are permitted to operate motor vehicles, that these vehicles are fit for safe operation, and hence that licensing, registration, and vehicle inspection requirements are being observed." <i>Ante,</i> at 659, 658. Foremost among the alternative methods of enforcing traffic and vehicle <span class="star-pagination">*666</span> safety regulations, according to the Court, is acting upon observed violations, for "drivers without licenses are presumably the less safe drivers whose propensities may well exhibit themselves." <i>Ante,</i> at 659. Noting that "finding an unlicensed driver among those who commit traffic violations is a much more likely event than finding an unlicensed driver by choosing randomly from the entire universe of drivers," <i>ibid.,</i> the Court concludes that the contribution to highway safety made by random stops would be marginal at best. The State's primary interest, however, is in traffic safety, not in apprehending unlicensed motorists for the sake of apprehending unlicensed motorists. The whole point of enforcing motor vehicle safety regulations is to remove from the road the unlicensed driver before he demonstrates why he is unlicensed. The Court would apparently prefer that the State check licenses and vehicle registrations as the wreckage is being towed away.</p>
<p>Nor is the Court impressed with the deterrence rationale, finding it inconceivable that an unlicensed driver who is not deterred by the prospect of being involved in a traffic violation or other incident requiring him to produce a license would be deterred by the possibility of being subjected to a spot check. The Court arrives at its conclusion without the benefit of a shred of empirical data in this record suggesting that a system of random spot checks would fail to deter violators. In the absence of such evidence, the State's determination that random stops would serve a deterrence function should stand.</p>
<p>On the other side of the balance, the Court advances only the most diaphanous of citizen interests. Indeed, the Court does not say that these interests can never be infringed by the State, just that the State must infringe them en masse rather than citizen by citizen. To comply with the Fourth Amendment, the State need only subject <i>all</i> citizens to the same "anxiety" and "inconvenien[ce]" to which it now subjects only a few.</p>
<p><span class="star-pagination">*667</span> For constitutional purposes, the action of an individual law enforcement officer is the action of the State itself, <i>e. g., </i><i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 346-347</a></span> (1880), and state acts are accompanied by a presumption of validity until shown otherwise. See, <i>e. g., </i><i>McDonald</i> v. <i>Board of Election,</i> <span class="citation" data-id="107917"><a href="/opinion/107917/mcdonald-v-board-of-election-commrs-of-chicago/" aria-description="Citation for case: McDonald v. Board of Election Comm&#x27;rs of Chicago">394 U. S. 802</a></span> (1969). Although a system of discretionary stops could conceivably be abused, the record before us contains no showing that such abuse is probable or even likely. Nor is there evidence in the record that a system of random license checks would fail adequately to further the State's interest in deterring and apprehending violators. Nevertheless, the Court concludes "[o]n the record before us" that the random spot check is not "a sufficiently productive mechanism to justify the intrusion upon Fourth Amendment interests which such stops entail." <i>Ante,</i> at 659. I think that the Court's approach reverses the presumption of constitutionality accorded acts of the States. The burden is not upon the State to demonstrate that its procedures are consistent with the Fourth Amendment, but upon respondent to demonstrate that they are not. "On this record" respondent has failed to make such a demonstration.</p>
<p>Neither the Court's opinion, nor the opinion of the Supreme Court of Delaware, suggests that the random stop made in this case was carried out in a manner inconsistent with the Equal Protection Clause of the Fourteenth Amendment. Absent an equal protection violation, the fact that random stops may entail "a possibly unsettling show of authority," <i>ante,</i> at 657, and "may create substantial anxiety," <i>ibid.,</i> seems an insufficient basis to distinguish for Fourth Amendment purposes between a roadblock stopping all cars and the random stop at issue here. Accordingly, I would reverse the judgment of the Supreme Court of Delaware.</p>
<h2>NOTES</h2>
<p>[*]  <i>Frank Carrington, Wayne W. Schmidt, Glen R. Murphy,</i> and <i>James P. Costello</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  In its opinion, the Delaware Supreme Court referred to respondent as the operator of the vehicle, see <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1361" aria-description="Citation for case: State v. Prouse">382 A. 2d 1359, 1361</a></span> (1978). However, the arresting officer testified: "I don't believe [respondent] was the driver. . . . As I recall, he was in the back seat . . . ," App. A12; and the trial court in its ruling on the motion to suppress referred to respondent as one of the four "occupants" of the vehicle, <i><span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/" aria-description="Citation for case: State v. Prouse">id.,</a></span></i> at A17. The vehicle was registered to respondent. <i><span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/" aria-description="Citation for case: State v. Prouse">Id.,</a></span></i> at A10.</p>
<p>[2]  <i>United States</i> v. <i>Montgomery,</i> 182 U. S. App. D. C. 426, <span class="citation" data-id="9464098"><a href="/opinion/348709/united-states-v-kevin-l-montgomery/" aria-description="Citation for case: United States v. Kevin L. Montgomery">561 F. 2d 875</a></span> (1977); <i>People</i> v. <i>Ingle,</i> 36 N. Y. 2d 413, <span class="citation" data-id="5529536"><a href="/opinion/5681169/people-v-ingle/" aria-description="Citation for case: People v. Ingle">330 N. E. 2d 39</a></span> (1975); <i>State</i> v. <i>Ochoa,</i> <span class="citation" data-id="9553424"><a href="/opinion/1190270/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">23 Ariz. App. 510</a></span>, <span class="citation" data-id="9553424"><a href="/opinion/1190270/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">534 P. 2d 441</a></span> (1975), rev'd on other grounds, <span class="citation" data-id="9604044"><a href="/opinion/1367261/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">112 Ariz. 582</a></span>, <span class="citation" data-id="9604044"><a href="/opinion/1367261/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">544 P. 2d 1097</a></span> (1976); <i>Commonwealth</i> v. <i>Swanger,</i> <span class="citation" data-id="1518042"><a href="/opinion/1518042/commonwealth-v-swanger/" aria-description="Citation for case: Commonwealth v. Swanger">453 Pa. 107</a></span>, <span class="citation" data-id="1518042"><a href="/opinion/1518042/commonwealth-v-swanger/" aria-description="Citation for case: Commonwealth v. Swanger">307 A. 2d 875</a></span> (1973); <i>United States</i> v. <i>Nicholas,</i> <span class="citation" data-id="299088"><a href="/opinion/299088/united-states-v-george-willie-nicholas-jr/" aria-description="Citation for case: United States v. George Willie Nicholas, Jr.">448 F. 2d 622</a></span> (CA8 1971). See also <i>United States</i> v. <i>Cupps,</i> <span class="citation" data-id="321729"><a href="/opinion/321729/united-states-v-hoyt-cupps-jr/" aria-description="Citation for case: United States v. Hoyt Cupps, Jr.">503 F. 2d 277</a></span> (CA6 1974).</p>
<p>[3]  <i>State</i> v. <i>Holmberg,</i> <span class="citation" data-id="9670456"><a href="/opinion/1701839/state-v-holmberg/" aria-description="Citation for case: State v. Holmberg">194 Neb. 337</a></span>, <span class="citation" data-id="9670456"><a href="/opinion/1701839/state-v-holmberg/" aria-description="Citation for case: State v. Holmberg">231 N. W. 2d 672</a></span> (1975); <i>State</i> v. <i>Allen,</i> <span class="citation" data-id="1332651"><a href="/opinion/1332651/state-v-allen/" aria-description="Citation for case: State v. Allen">282 N. C. 503</a></span>, <span class="citation" data-id="1332651"><a href="/opinion/1332651/state-v-allen/" aria-description="Citation for case: State v. Allen">194 S. E. 2d 9</a></span> (1973); <i>Palmore</i> v. <i>United States,</i> <span class="citation" data-id="2378216"><a href="/opinion/2378216/palmore-v-united-states/" aria-description="Citation for case: Palmore v. United States">290 A. 2d 573</a></span> (D. C. App. 1972), aff'd on jurisdictional grounds only, <span class="citation" data-id="9425255"><a href="/opinion/108767/palmore-v-united-states/" aria-description="Citation for case: Palmore v. United States">411 U. S. 389</a></span> (1973); <i>Leonard</i> v. <i>State,</i> <span class="citation" data-id="1778812"><a href="/opinion/1778812/leonard-v-state-of-texas/" aria-description="Citation for case: Leonard v. State of Texas">496 S. W. 2d 576</a></span> (Tex. Crim. App. 1973); <i>United States</i> v. <i>Jenkins,</i> <span class="citation" data-id="332182"><a href="/opinion/332182/united-states-v-james-jenkins-jr/" aria-description="Citation for case: United States v. James Jenkins, Jr.">528 F. 2d 713</a></span> (CA10 1975); <i>Myricks</i> v. <i>United States,</i> <span class="citation" data-id="274285"><a href="/opinion/274285/charles-james-myricks-v-united-states/" aria-description="Citation for case: Charles James Myricks v. United States">370 F. 2d 901</a></span> (CA5), cert. dismissed, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1015/">386 U. S. 1015</a></span> (1967).</p>
<p>[4]  The court stated:
</p>
<p>"The Delaware Constitution Article I, § 6 is substantially similar to the Fourth Amendment and a violation of the latter is necessarily a violation of the former." <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1362" aria-description="Citation for case: State v. Prouse">382 A. 2d, at 1362</a></span>, citing <i>State</i> v. <i>Moore,</i> <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">55 Del. 356</a></span>, <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">187 A. 2d 807</a></span> (1963).</p>
<p><i>Moore</i> was decided less than two years after <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), applied to the States the limitations previously imposed only on the Federal Government. In setting forth the approach reiterated in the opinion below, <i><span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">Moore</a></span></i> noted not only the common purposes and wording of the Fourth Amendment and the state constitutional provision, but also the overriding effect of the former. See <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/#362" aria-description="Citation for case: State v. Moore">55 Del., at 362-363</a></span>, <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/#810" aria-description="Citation for case: State v. Moore">187 A. 2d, at 810-811</a></span>.</p>
<p>[5]  We have found only one case decided after <i>State</i> v. <i><span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">Moore, supra</a></span></i><i>,</i> in which the court relied solely on state law in upholding the validity of a search or seizure, and that case involved not only Del. Const. Art. I, § 6, but also state statutory requirements for issuance of a search warrant. <i>Rossitto</i> v. <i>State,</i> <span class="citation" data-id="2170567"><a href="/opinion/2170567/rossitto-v-state/" aria-description="Citation for case: Rossitto v. State">234 A. 2d 438</a></span> (1967). Moreover, every case holding a search or seizure to be contrary to the state constitutional provision relies on cases interpreting the Fourth Amendment and simultaneously concludes that the search or seizure is contrary to that provision. See, <i>e. g., </i><i>Young</i> v. <i>State,</i> <span class="citation" data-id="1893463"><a href="/opinion/1893463/young-v-state/" aria-description="Citation for case: Young v. State">339 A. 2d 723</a></span> (1975); <i>Freeman</i> v. <i>State,</i> <span class="citation" data-id="1500552"><a href="/opinion/1500552/freeman-v-state/" aria-description="Citation for case: Freeman v. State">317 A. 2d 540</a></span> (1974); cf. <i>Bertomeu</i> v. <i>State,</i> <span class="citation" data-id="1471204"><a href="/opinion/1471204/bertomeu-v-state/" aria-description="Citation for case: Bertomeu v. State">310 A. 2d 865</a></span> (1973).</p>
<p>[6]  See <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#315" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 315</a></span> (1978); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 439</a></span> (1973); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 539</a></span> (1967).</p>
<p>[7]  See also <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span> (1976); <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 895</a></span> (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#270" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 270</a></span> (1973); <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#97" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 97</a></span> (1964); <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455-456</a></span> (1948).</p>
<p>[8]  See, <i>e. g., </i><i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616-619</a></span> (1977); <i>United States</i> v. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 555</a></span>; cases cited in n. 6, <i>supra.</i></p>
<p>[9]  <i>Terry</i> v. <i>Ohio, supra,</i> at 21. See also <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#137" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 137</a></span> (1978); <i>Beck</i> v. <i>Ohio, supra,</i> at 96-97.</p>
<p>[10]  See, <i>e. g., </i><i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span> (1976); <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963) (warrantless arrests requiring probable cause); <i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra</a></span></i><i>; </i><i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925) (warrantless searches requiring probable cause). See also <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975).</p>
<p>[11]  See <i>Terry</i> v. <i>Ohio, supra</i><i>; </i><i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce, supra</a></span></i><i>.</i>
</p>
<p>In addition, the Warrant Clause of the Fourth Amendment generally requires that prior to a search a neutral and detached magistrate ascertain that the requisite standard is met, see, <i>e. g., </i><i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978).</p>
<p>[12]  <i>United States</i> v. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 560</a></span>.</p>
<p>[13]  In addressing the constitutionality of Border Patrol practices, we reserved the question of the permissibility of state and local officials stopping motorists for document questioning in a manner similar to checkpoint detention, see <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span> n. 14, or roving-patrol operations, see <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 883</a></span> n. 8.</p>
<p>[14]  In 1977, 47,671 persons died in motor vehicle accidents in this country. U. S. Dept. of Transportation, Highway Safety A-9 (1977).</p>
<p>[15]  See, <i>e. g.,</i> Del. Code Ann., Tit. 21, §§ 2701, 2707 (1974 and Supp. 1977); § 2713 (1974) (Department of Public Safety "shall examine the applicant as to his physical and mental qualifications to operate a motor vehicle in such manner as not to jeopardize the safety of persons or property . . .").</p>
<p>[16]  § 2143 (a) (1974).</p>
<p>[17]  § 2118 (Supp. 1977); State of Delaware, Department of Public Safety, Division of Motor Vehicles, Driver's Manual 60 (1976).</p>
<p>[18]  It has been urged that additional state interests are the apprehension of stolen motor vehicles and of drivers under the influence of alcohol or narcotics. The latter interest is subsumed by the interest in roadway safety, as may be the former interest to some extent. The remaining governmental interest in controlling automobile thefts is not distinguishable from the general interest in crime control.</p>
<p>[19]  Cf. <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 883</a></span>.</p>
<p>[20]  Del. Code Ann., Tit. 21, § 2126 (1974).</p>
<p>[21]  §§ 2121 (b), (d) (1974).</p>
<p>[22]  See n. 16, <i>supra;</i> § 2109 (1974).</p>
<p>[23]  See n. 17, <i>supra;</i> § 2109 (1974).</p>
<p>[24]  See, <i>e. g.,</i> §§ 4101-4199B (1974 and Supp. 1977).</p>
<p>[25]  Cf. <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978) (warrant required for federal inspection under interstate commerce power of health and safety of workplace); <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967) (warrant required for inspection of warehouse for municipal fire code violations); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967) (warrant required for inspection of residence for municipal fire code violations).</p>
<p>[26]  Nor does our holding today cast doubt on the permissibility of roadside truck weigh-stations and inspection checkpoints, at which some vehicles may be subject to further detention for safety and regulatory inspection than are others.</p>
<p>[*]  Indeed, this distinction was expressly recognized in <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, 883 n. 8 (1975):
</p>
<p>"Our decision in this case takes into account the special function of the Border Patrol, the importance of the governmental interests in policing the border area, the character of roving-patrol stops, and the availability of alternatives to random stops unsupported by reasonable suspicion. Border Patrol agents have no part in enforcing laws that regulate highway use, and their activities have nothing to do with an inquiry whether motorists and their vehicles are entitled, by virtue of compliance with laws governing highway usage, to be upon the public highways. Our decision thus does not imply that state and local enforcement agencies are without power to conduct such limited stops as are necessary to enforce laws regarding drivers' licenses, vehicle registration, truck weights, and similar matters."</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Devenpeck v. Alford.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Devenpeck v. Alford"
type: case
citation: "543 U.S. 146 (2004)"
parallel_cite: "125 S. Ct. 588; 160 L. Ed. 2d 537"
neutral_cite: 2004 U.S. LEXIS 8272
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-12-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-12-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Devenpeck v. Alford
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137733/devenpeck-v-alford/"
  cluster_id: 137733
  opinion_id: 137733
  identity_checked: true
homes:
  - page: "[[Arrest and Arrest Warrants]]"
    role: "Key — offense-of-arrest flexibility (objective standard; motive irrelevant)"
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
related: ["[[Whren v. United States]]", "[[District of Columbia v. Wesby]]", "[[Brinegar v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "arrest", "objective-standard", "closely-related-offense"]
holding: "An arrest is lawful so long as the known facts give probable cause for SOME criminal offense; the offense need not be the one the…"
lake:
  record_id: Devenpeck v. Alford
  status: verified
  projected_at: 2026-07-06
---

# Devenpeck v. Alford

*543 U.S. 146 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers arrested Alford, citing a state privacy-act offense for recording his roadside conversation with them; that offense turned out not to be a crime. Alford sued under § 1983 for unlawful arrest. The Ninth Circuit held probable cause could be assessed only on offenses "closely related" to the one the officer invoked. The State sought review of that limitation.

## Issue
Whether a warrantless arrest is lawful only if there is probable cause for an offense closely related to the one the arresting officer announced.

## Rule
No; the inquiry is objective and offense-agnostic. "Our cases make clear that an arresting officer's state of mind (except for the facts that he knows) is irrelevant to the existence of probable cause. . . . [T]hat is to say, his subjective reason for making the arrest need not be the criminal offense as to which the known facts provide probable cause." — 543 U.S. 146, 153. ^pin-153

An arrest is lawful so long as the facts known to the officer establish probable cause for some criminal offense, whether or not that offense is the one the officer cited or one "closely related" to it.

## Application
Whether the privacy-act offense the officers named was valid or "closely related" to anything did not control; the question was whether the facts they knew amounted to probable cause for any offense. Because the "closely related offense" rule has no basis in precedent or reason, the Ninth Circuit erred in applying it, and the lawfulness of Alford's arrest had to be assessed under the objective probable-cause standard [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
The "closely related offense" requirement was rejected; the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]] for assessment of probable cause under the objective standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Devenpeck* extends the objective-cause logic of [[Whren v. United States]] to the offense of arrest and feeds the totality-of-the-circumstances analysis reaffirmed in [[District of Columbia v. Wesby]].

## Appears on
- [[Arrest and Arrest Warrants]] — *Key*
- [[Probable Cause]] — *Key — Progeny / Refinement*

## Sources
- *Devenpeck v. Alford*, 543 U.S. 146 (2004) — https://www.courtlistener.com/opinion/137733/devenpeck-v-alford/ — pinpoint: 153 (verbatim passage confirmed on CourtListener; reporter page per the verified 543 U.S. 153–55 cite).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a0f694382a865f9c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Devenpeck v. Alford"}, "payload": {"all": [{"cite": "543 U.S. 146", "page": "146", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "543"}, {"cite": "125 S. Ct. 588", "page": "588", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "125"}, {"cite": "160 L. Ed. 2d 537", "page": "537", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "160"}, {"cite": "2004 U.S. LEXIS 8272", "page": "8272", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}], "display": "543 U.S. 146", "official": {"cite": "543 U.S. 146", "page": "146", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "543"}, "official_selection_present": true, "record_id": "Devenpeck v. Alford"}}
{"assertion_id": "e03775a681cd49f0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-153", "record_id": "Devenpeck v. Alford"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-153", "pinpoint_status": "slip-only", "quote": "to the one the officer invoked. The State sought review of that limitation. ## Issue Whether a warrantless arrest is lawful only if there is probable cause for an offense closely related to the one the arresting officer announced. ## Rule No; the inquiry is objective and offense-agnostic.", "quote_fidelity": "mismatch", "record_id": "Devenpeck v. Alford", "star_marker": null}}
{"assertion_id": "1504b1db3abfd7c4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Devenpeck v. Alford"}, "payload": {"as_of_content": "2004-12-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Devenpeck v. Alford", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Devenpeck v. Alford

```json
{
  "schema_version": "s2.v1",
  "record_id": "Devenpeck v. Alford",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Devenpeck v. Alford",
    "case_name_short": "Devenpeck",
    "case_name_full": "DEVENPECK Et Al. v. ALFORD",
    "input_case_name": "Devenpeck v. Alford",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-12-13",
    "year": 2004,
    "docket": null,
    "cluster_id": 137733,
    "lead_opinion_id": 137733,
    "sibling_ids": [
      137733
    ],
    "absolute_url": "/opinion/137733/devenpeck-v-alford/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 139725,
        "score": 20,
        "case_name": "Devenpeck v. Alford"
      },
      {
        "cluster_id": 137710,
        "score": 20,
        "case_name": "Devenpeck v. Alford"
      },
      {
        "cluster_id": 9223394,
        "score": 20,
        "case_name": "Devenpeck v. Alford"
      },
      {
        "cluster_id": 9223393,
        "score": 20,
        "case_name": "Devenpeck v. Alford"
      },
      {
        "cluster_id": 135641,
        "score": 20,
        "case_name": "Devenpeck v. Alford"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "543 U.S. 146",
      "volume": "543",
      "reporter": "U.S.",
      "page": "146",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "125 S. Ct. 588",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "588",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 537",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "537",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 8272",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "8272",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "543 U.S. 146",
        "volume": "543",
        "reporter": "U.S.",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 S. Ct. 588",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "588",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 537",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "537",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 8272",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "8272",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "543 U.S. 146",
    "official_selection": {
      "court_class": "scotus",
      "selected": "543 U.S. 146",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-153",
      "page": null,
      "quote": "to the one the officer invoked. The State sought review of that limitation. ## Issue Whether a warrantless arrest is lawful only if there is probable cause for an offense closely related to the one the arresting officer announced. ## Rule No; the inquiry is objective and offense-agnostic.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-12-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Devenpeck v. Alford",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Darrell Mark Babcock",
          "cluster_id": 4623035,
          "cite": [
            "924 F.3d 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lionel Alexander v. City of Round Rock",
          "cluster_id": 4384027,
          "cite": [
            "854 F.3d 298",
            "2017 U.S. App. LEXIS 6692",
            "2017 WL 1393702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rife v. Oklahoma Department of Public Safety",
          "cluster_id": 4340429,
          "cite": [
            "846 F.3d 1119",
            "2017 WL 280700",
            "2017 U.S. App. LEXIS 1117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Pegg v. Grant Herrnberger",
          "cluster_id": 4335908,
          "cite": [
            "845 F.3d 112",
            "2017 WL 35722",
            "2017 U.S. App. LEXIS 109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Demilia",
          "cluster_id": 2746456,
          "cite": [
            "771 F.3d 1051",
            "2014 U.S. App. LEXIS 20684",
            "2014 WL 5462413"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
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
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
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
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laurie Tsao v. Desert Palace, Inc.",
          "cluster_id": 810771,
          "cite": [
            "698 F.3d 1128",
            "2012 WL 5200336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fogarty v. Gallegos",
          "cluster_id": 170599,
          "cite": [
            "523 F.3d 1147",
            "2008 U.S. App. LEXIS 8587",
            "2008 WL 1765018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gary Blankenhorn v. City of Orange Andy Romero Dung Nguyen Garrett Ross Tamara South Gray, Sergeant Montano, Officer Kayano, Officer Roman, Officer",
          "cluster_id": 797658,
          "cite": [
            "485 F.3d 463",
            "2007 U.S. App. LEXIS 10856",
            "2007 D.A.R. 6484"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
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
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heien v. North Carolina",
          "cluster_id": 2760668,
          "cite": [
            "190 L. Ed. 2d 475",
            "135 S. Ct. 530",
            "2014 U.S. LEXIS 8306",
            "83 U.S.L.W. 4021",
            "25 Fla. L. Weekly Fed. S 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracey White v. Thomas Jackson",
          "cluster_id": 4414209,
          "cite": [
            "865 F.3d 1064",
            "2017 WL 3254496",
            "2017 U.S. App. LEXIS 13926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Halsey v. Frank Pfeiffer",
          "cluster_id": 2671183,
          "cite": [
            "750 F.3d 273",
            "2014 WL 1622769",
            "2014 U.S. App. LEXIS 7696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fabrikant v. French",
          "cluster_id": 806776,
          "cite": [
            "691 F.3d 193",
            "2012 U.S. App. LEXIS 17254",
            "2012 WL 3518527"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Jaegly, Jr. v. Matthew Couch, Bernard Santandria, Paula Breen and City of Albany, Docket No. 05-2191-Cv",
          "cluster_id": 793434,
          "cite": [
            "439 F.3d 149",
            "2006 U.S. App. LEXIS 4533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zellner v. Summerlin",
          "cluster_id": 2707,
          "cite": [
            "494 F.3d 344",
            "2007 U.S. App. LEXIS 17272",
            "2007 WL 2067932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brian Ulrich v. Pope County",
          "cluster_id": 868496,
          "cite": [
            "715 F.3d 1054",
            "2013 U.S. App. LEXIS 10157",
            "2013 WL 2157812"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
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
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmichael v. Village of Palatine, Ill.",
          "cluster_id": 146911,
          "cite": [
            "605 F.3d 451",
            "2010 U.S. App. LEXIS 10378",
            "2010 WL 2011509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freeman v. Gore",
          "cluster_id": 48719,
          "cite": [
            "483 F.3d 404",
            "2007 WL 968131"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Figueroa v. Mazza",
          "cluster_id": 3209159,
          "cite": [
            "825 F.3d 89",
            "2016 U.S. App. LEXIS 10152",
            "2016 WL 3126772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fayer v. Vaughn",
          "cluster_id": 216101,
          "cite": [
            "649 F.3d 1061",
            "2011 U.S. App. LEXIS 9103",
            "2011 WL 1663595"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson Ex Rel. Davison v. Napolitano",
          "cluster_id": 146453,
          "cite": [
            "604 F.3d 732",
            "2010 U.S. App. LEXIS 9887",
            "2010 WL 1931683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Revell v. Port Authority of New York & New Jersey",
          "cluster_id": 423,
          "cite": [
            "598 F.3d 128",
            "2010 U.S. App. LEXIS 5803",
            "2010 WL 1006651"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Devenpeck v. Alford:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137733) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDA4NjY1NjAwMDAwJnM9MzE0OTI4NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137733%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(137733)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTUmcz0xMzAzNzEwJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28137733%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137733)",
        "reviewed": 54,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 54,
        "triage_read": 0,
        "triage_snippet_classified": 54
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137733)",
    "indexed_citing_opinions": 689,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137733,
        "count": 689,
        "count_source": "search"
      }
    ],
    "citation_count": 1834,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/devenpeck-v-alford.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMjA3NzQmcz0xMDEzMTc2MyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28137733%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137733,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 112585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 131150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 198626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 411158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 516197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 782475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 1202122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137733,
        "cited_id": 2620699,
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
    "date_created": "2026-07-05T02:24:44Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:25:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:25:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:29:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:25:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Devenpeck v. Alford

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b352-4">
<span citation-index="1" class="star-pagination" label="148"> 
   *148
   </span>
  Justice Scalia
 </author>
<p id="ApqC">
  delivered the opinion of the Court.
 </p>
<p id="b352-5">
  This case presents the question whether an arrest is lawful under the Fourth Amendment when the criminal offense for which there is probable cause to arrest is not “closely related” to the offense stated by the arresting officer at the time of arrest.
 </p>
<p id="b352-6">
  I
 </p>
<p id="b352-7">
  A
 </p>
<p id="b352-8">
  On the night of November 22,1997, a disabled automobile and its passengers were stranded on the shoulder of State Route 16, a divided highway, in Pierce County, Washington.
  <em>
   Alford
  </em>
  v.
  <em>
   Haner,
  </em>
  <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#974" aria-description="Citation for case: Alford v. Haner">333 F. 3d 972, 974</a></span> (CA9 2003); App. 94, 98. Respondent Jerome Alford pulled his car off the road behind the disabled vehicle, activating his “wig-wag” headlights (which flash the left and right lights alternately). As he pulled off the road, Officer Joi Haner of the Washington State Patrol, one of the two petitioners here, passed the disabled car from the opposite direction. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#974" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 974</a></span>. He turned around to check on the motorists at the first opportunity, and when he arrived, respondent, who had begun helping the motorists change a flat tire, hurried back to his car and drove away.
  <em>
   <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/" aria-description="Citation for case: Alford v. Haner">Ibid.</a></span>
  </em>
  The stranded motorists asked Haner if respondent was a “cop”; they said that respondent’s statements, and his flashing, wig-wag headlights, had given them that impression.
  <em>
   Ibid.;
  </em>
  App. 96. They also informed Haner that as respondent hurried off he left his flashlight behind.
  <em>
   Id.,
  </em>
  at 97.
 </p>
<p id="b352-9">
  On the basis of this information, Haner radioed his supervisor, Sergeant Gerald Devenpeck, the other petitioner here, that he was concerned respondent was an “impersonator”
  <span citation-index="1" class="star-pagination" label="149"> 
   *149
   </span>
  or “wannabe cop.”
  <em>
   Id.,
  </em>
  at 97-98. He pursued respondent’s vehicle and pulled it over. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>. Through the passenger-side window, Haner observed that respondent was listening to the Kitsap County Sheriff’s Office police frequency on a special radio, and that handcuffs and a hand-held police scanner were in the car.
  <em>
   <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/" aria-description="Citation for case: Alford v. Haner">Ibid.</a></span>
  </em>
  These facts bolstered Haner’s suspicion that respondent was impersonating a police officer. App. 106, 107. Haner thought, moreover, that respondent seemed untruthful and evasive: He told Haner that he had worked previously for the “State Patrol,” but under further questioning, claimed instead to have worked in law enforcement in Texas and at a shipyard.
  <em>
   <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/" aria-description="Citation for case: Alford v. Haner">Ibid.</a></span>
  </em>
  He claimed that his flashing headlights were part of a recently installed car-alarm system, and acted as though he was unable to trigger the system; but during these feigned efforts Haner noticed that respondent avoided pushing a button near his knee, which Haner suspected (correctly) to be the switch for the lights. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>; App. 108.
 </p>
<p id="b353-5">
  Sergeant Devenpeck arrived on the scene a short time later. After Haner informed Devenpeck of the basis for his belief that respondent had been impersonating a pólice officer,
  <em>
   id.,
  </em>
  at 110, Devenpeck approached respondent’s vehicle and inquired about the wig-wag headlights, <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>. As before, respondent said that the headlights were part of his alarm system and that he did not know how to activate them. App. 52, 138-139. Like Haner, Devenpeck was skeptical of respondent’s answers. In the course of his questioning, Devenpeck noticed a tape recorder on the passenger seat of respondent’s car, with the play and record buttons depressed. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>. He ordered Haner to remove respondent from the car, played the recorded tape, and found that respondent had been recording his conversations with the officers. Devenpeck informed respondent that he was under arrest for a violation of the Washington Privacy Act, <span class="citation no-link">Wash. Rev. Code §9.73.030</span> (1994). <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>; App. 144-145. Respondent protested that a State Court-of-
  <span citation-index="1" class="star-pagination" label="150"> 
   *150
   </span>
  Appeals decision, a copy of which he claimed was in his glove compartment, permitted him to record roadside conversations with police officers. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>; App. 42, 67-68. Devenpeck returned to his car, reviewed the language of the Privacy Act, and attempted unsuccessfully to reach a prosecutor to confirm that the arrest was lawful.
  <em>
   Id.,
  </em>
  at 151-154. Believing that the text of the Privacy Act confirmed that respondent’s recording was unlawful,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  he directed Officer Haner to take respondent to jail.
  <em>
   Id.,
  </em>
  at 154.
 </p>
<p id="b354-5">
  A short time later; Devenpeck reached by phone Mark Lindquist, a deputy county prosecutor, to whom he recounted the events leading to • respondent’s arrest. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>. The two discussed a series of possible criminal offenses, including violation of the Privacy Act, impersonating a police officer, and making a false representation to an officer. App. 177-178. Lindquist advised that there was “clearly probable cause,”
  <em>
   id.,
  </em>
  at 179, and suggested that respondent also be charged with “obstructing a public servant” “based on the runaround [he] gave [Devenpeck],”
  <em>
   id.,
  </em>
  at 157. Devenpeck rejected this suggestion, explaining that the State Patrol does not, as a matter of policy, “stack charges” against an arrestee.
  <em>
   Id.,
  </em>
  at 157-158.
 </p>
<p id="b354-6">
  At booking, Haner charged respondent with violating the State Privacy Act,
  <em>
   id.,
  </em>
  at 32-33, and issued a ticket to respondent for his flashing headlights under <span class="citation no-link">Wash. Rev. Code §46.37.280</span>(3) (1994), App. 24-25. Under state law, respondent could be detained on the latter offense only for the period of time “reasonably necessary” to issue a citation.
  <span citation-index="1" class="star-pagination" label="151"> 
   *151
   </span>
  §46.64.015. The state trial court subsequently dismissed both charges. App. 10, 29.
 </p>
<p id="b355-5">
  B
 </p>
<p id="b355-6">
  Respondent filed suit against petitioners in Federal District Court. He asserted a federal cause of action under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, and a state cause of action for unlawful arrest and imprisonment, both claims resting upon the allegation that petitioners arrested him without probable cause in violation of the Fourth and Fourteenth Amendments. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>. The District Court denied petitioners’ motion for summary judgment on grounds of qualified immunity, and the case proceeded to trial.
  <em>
   Alford
  </em>
  v.
  <em>
   Washington State Police,
  </em>
  Case No. C99-5586RJB (WD Wash., Nov. 30, 2000), App. to Pet. for Cert. 40a. The jury was instructed that, for respondent to prevail on either his federal- or state-law claim, he must demonstrate that petitioners arrested him without probable cause, App. 199-201; and that probable cause exists “if the facts and circumstances within the arresting officer’s knowledge are sufficient to warrant a prudent person to conclude that the suspect has committed, is committing, or was about to commit a crime,”
  <em>
   id.,
  </em>
  at 201. The jury was also instructed that, at the time of respondent’s arrest, a State Court-of-Appeals decision,
  <em>
   State
  </em>
  v.
  <em>
   Flora,
  </em>
  <span class="citation" data-id="1202122"><a href="/opinion/1202122/state-v-flora/" aria-description="Citation for case: State v. Flora">68 Wash. App. 802</a></span>, <span class="citation" data-id="1202122"><a href="/opinion/1202122/state-v-flora/" aria-description="Citation for case: State v. Flora">845 P. 2d 1355</a></span> (1992), had clearly established that respondent’s taping of petitioners was not a crime, App. 202. And the jury was directed that it must find for petitioners if a reasonable officer in the same circumstances would have believed respondent’s detention was lawful.
  <em>
   Id.,
  </em>
  at 200. Respondent did not object to any of these instructions. The jury returned a unanimous verdict in favor of petitioners. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>. The District Court denied respondent’s motion for judgment as a matter of law or, in the alternative, a new trial, and respondent appealed.
  <em>
   Ibid.;
  </em>
  App. to Pet. for Cert. 25a.
 </p>
<p id="b356-4">
<span citation-index="1" class="star-pagination" label="152"> 
   *152
   </span>
  A divided panel of the Court of Appeals for the Ninth Circuit reversed, finding “no evidence to support the jury’s verdict,” <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#975" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 975</a></span>. The majority concluded that petitioners could not have had probable cause to arrest because they cited only the Privacy Act charge and “[t]ape recording officers conducting a traffic stop is not a crime in Washington.”
  <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#976" aria-description="Citation for case: Alford v. Haner"><em>
   Id.,
  </em>
  at 976</a></span>. The majority rejected petitioners’ claim that probable cause existed to arrest respondent for the offenses of impersonating a law-enforcement officer, Wash. Rev. Code § 9A.60.040(3) (1994), and obstructing a law-enforcement officer, §9A.76.020, because, it said, those offenses were not “closely related” to the offense invoked by Devenpeck as he took respondent into custody, <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#976" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 976-977</a></span>. The majority also held that there was no evidence to support petitioners’ claim of qualified immunity, since, given the Washington Court of Appeals’ decision in
  <em>
   <span class="citation" data-id="1202122"><a href="/opinion/1202122/state-v-flora/" aria-description="Citation for case: State v. Flora">Flora</a></span>,
  </em>
  “no objectively.reasonable officer could have concluded that arresting [respondent] for taping the traffic stop was permissible,” <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#979" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 979</a></span>. Judge Gould dissented on the ground that it was objectively reasonable for petitioners to believe that respondent had violated the Privacy Act. See
  <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#980" aria-description="Citation for case: Alford v. Haner"><em>
   id.,
  </em>
  at 980</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./541/987/">541 U. S. 987</a></span> (2004).
 </p>
<p id="b356-5">
  HH HH
 </p>
<p id="b356-1">
  The Fourth Amendment protects [t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” In conformity with the rule at common law, a warrantless arrest by a law officer is reasonable under the Fourth Amendment where there is probable cause to believe that a criminal offense has been or is being committed. See
  <em>
   United States
  </em>
  v.
  <em>
   Watson,
  </em>
  <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#417" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 417-424</a></span> (1976);
  <em>
   Brinegar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-176</a></span> (1949). Whether probable cause exists depends upon the reasonable conclusion to be drawn from the facts known to the arresting officer at the time of the arrest.
  <em>
   Maryland
  </em>
  v.
  <em>
   Pringle,
  </em>
  <span class="citation" data-id="131150"><a href="/opinion/131150/maryland-v-pringle/#371" aria-description="Citation for case: Maryland v. Pringle">540 U. S. 366, 371</a></span> (2003). In
  <span citation-index="1" class="star-pagination" label="153"> 
   *153
   </span>
  this case, the Court of Appeals held that the probable-cause inquiry is further confined to the known facts bearing upon the offense actually invoked at the time of arrest, and that (in addition) the offense supported by these known facts must be “closely related” to the offense that the officer invoked. <span class="citation" data-id="8407953"><a href="/opinion/8437549/alford-v-haner/#976" aria-description="Citation for case: Alford v. Haner">333 F. 3d, at 976</a></span>. We find no basis in precedent or reason for this limitation.
 </p>
<p id="b357-4">
  Our cases make clear that an arresting officer’s state of mind (except for the facts that he knows) is irrelevant to the existence of probable cause. See
  <em>
   Whren
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 812-813</a></span> (1996) (reviewing cases);
  <em>
   Arkansas
  </em>
  v.
  <em>
   Sullivan,
  </em>
  <span class="citation" data-id="9795082"><a href="/opinion/2620699/arkansas-v-sullivan/" aria-description="Citation for case: Arkansas v. Sullivan">532 U. S. 769</a></span> (2001)
  <em>
   (per curiam).
  </em>
  That is to say, his subjective reason for making the arrest need not be the criminal offense as to which the known facts provide probable cause. As we have repeatedly explained, “ ‘the fact that the officer does not have the state of mind which is hypothe-cated by the reasons which provide the legal justification for the officer’s action does not invalidate the action taken as long as the circumstances, viewed objectively, justify that action.’”
  <em>
   <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren, supra,</a></span>
  </em>
  at 813 (quoting
  <em>
   Scott
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 138</a></span> (1978)). “[T]he Fourth Amendment’s concern with ‘reasonableness’ allows certain actions to be taken in certain circumstances,
  <em>
   whatever
  </em>
  the subjective intent.”
  <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#814" aria-description="Citation for case: Whren v. United States"><em>
   Whren, supra,
  </em>
  at 814</a></span>. “[E]venhanded law enforcement is best achieved by the application of objective standards of conduct, rather than standards that depend upon the subjective state of mind of the officer.”
  <em>
   Horton
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#138" aria-description="Citation for case: Horton v. California">496 U. S. 128, 138</a></span> (1990).
 </p>
<p id="b357-5">
  The rule that the. offense establishing probable cause must be “closely related” to, and based on the same conduct as, the offense identified by the arresting officer at the time of arrest is inconsistent with this precedent.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Such a rule
  <span citation-index="1" class="star-pagination" label="154"> 
   *154
   </span>
  makes the lawfulness of an arrest turn upon the motivation of the arresting officer — eliminating, as validating probable cause, facts that played no part in the officer’s expressed subjective reason for making the arrest, and offenses that are not “closely related” to that subjective reason. See,
  <em>
   e. g., Sheehy
  </em>
  v.
  <em>
   Plymouth,
  </em>
  <span class="citation" data-id="198626"><a href="/opinion/198626/sheehy-v-town-of-plymouth/#20" aria-description="Citation for case: Sheehy v. Town of Plymouth">191 F. 3d 15, 20</a></span> (CA1 1999);
  <em>
   Trejo
  </em>
  v.
  <em>
   Perez,
  </em>
  <span class="citation" data-id="411158"><a href="/opinion/411158/eduardo-trejo-v-ivan-perez/#485" aria-description="Citation for case: Eduardo Trejo v. Ivan Perez">693 F. 2d 482, 485-486</a></span> (CA5 1982). This means that the constitutionality of an arrest under a given set of known facts will “vary from place to place and from time to time,”
  <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#815" aria-description="Citation for case: Whren v. United States"><em>
   Whren, supra,
  </em>
  at 815</a></span>, depending on whether the arresting officer states the reason for the detention and, if so, whether he correctly identifies a general class of offense for which, probable cause exists. An arrest made by a knowledgeable, veteran officer would be valid, whereas an arrest made by a rookie
  <em>
   in precisely the same circumstances
  </em>
  would not. We see no reason to ascribe to the Fourth Amendment such arbitrarily variable protection.
 </p>
<p id="b358-5">
  Those who support the “closely related offense” rule say that, although it is aimed at rooting out the subjective vice of arrests made for the wrong reason, it does so by objective means — that is, by reference to the arresting officer’s statement of his reason. The same argument was made in
  <em>
   <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren, supra,</a></span>
  </em>
  in defense of the proposed rule that a traffic stop can be declared invalid for malicious motivation when it is justified only by an offense which standard police practice does not make the basis for a stop. That rule, it was said, “attempt[s] to root out subjective vices through objective means,”
  <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#814" aria-description="Citation for case: Whren v. United States"><em>
   id.,
  </em>
  at 814</a></span>. We rejected the argument there, and we reject it again here. Subjective intent of the arresting officer,
  <em>
   however
  </em>
  it is determined (and of course subjective intent is
  <em>
   always
  </em>
  determined by objective means), is simply
  <span citation-index="1" class="star-pagination" label="155"> 
   *155
   </span>
  no basis for invalidating an arrest. Those are lawfully arrested whom the facts known to the arresting officers give probable cause to arrest.
 </p>
<p id="b359-5">
  Finally, the “closely related offense” rule is condemned by its perverse consequences. While it is assuredly good police practice to inform a person of the reason for his arrest at the time he is taken into custody, we have never held that to be constitutionally required.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Hence, the predictable consequence of a rule limiting the probable-cause inquiry to offenses closely related to (and supported by the same facts as) those identified by the arresting officer is not, as respondent contends, that officers will cease making sham arrests on the hope that such arrests will later be validated, but rather that officers will cease providing reasons for arrest. And even if this option were to be foreclosed by adoption of a statutory or constitutional requirement, officers would simply give every reason for which probable cause could conceivably exist.
 </p>
<p id="b359-6">
  The facts of this case exemplify the arbitrary consequences of a “closely related offense” rule. Officer Haner’s initial stop of respondent was motivated entirely by the suspicion that he was impersonating a police officer. App. 106. Before pulling respondent over, Haner indicated by radio that this was his concern; during the stop, Haner asked respondent whether he was actively employed in law enforcement and why his car had wig-wag headlights; and when Sergeant Devenpeck arrived, Haner told him why he thought respondent was a “wannabe cop,”
  <em>
   id.,
  </em>
  at 98. In addition, in the course of interrogating respondent, both officers became convinced that he was not answering their questions truthfully and, with respect to the wig-wag headlights, that he
  <span citation-index="1" class="star-pagination" label="156"> 
   *156
   </span>
  was affirmatively trying to mislead them. Only after these suspicions had developed did Devenpeck discover the taping, place respondent under arrest, and offer the Privacy Act as the reason. Because of the “closely related offense” rule, Devenpeck’s actions render irrelevant both Haner’s developed suspicions that respondent was impersonating a police officer and the officers’ shared belief that respondent obstructed their investigation. The outcome under the “closely related offense” rule might well have been different if Haner, rather than Devenpeck, had made the arrest, on the stated basis of
  <em>
   his
  </em>
  suspicions; if Devenpeck had not abided the county’s policy against stacking charges; or if either officer had made the arrest without stating the grounds. We have consistently rejected a conception of the Fourth Amendment that would produce such haphazard results. See
  <em>
   Whren,
  </em>
  <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#815" aria-description="Citation for case: Whren v. United States">517 U. S., at 815</a></span>.
 </p>
<p id="b360-4">
  * * *
 </p>
<p id="b360-5">
  Respondent contended below that petitioners lacked probable cause to arrest him for obstructing a law-enforcement officer or for impersonating a law-enforcement officer. Because the Court of Appeals held that those offenses were legally irrelevant, it did not decide the question. We decline to engage in this inquiry for the first time here. Accordingly, we reverse the judgment of the Ninth Circuit and remand the case for further proceedings consistent with this opinion.
 </p>
<p id="b360-6">
<em>
   It is so ordered.
  </em>
</p>
<judges id="b360-7">
  The Chief Justice took no part in the decision of this case.
 </judges>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b354-7">
   The relevant provision of the Washington Privacy Act states:
  </p>
<blockquote id="b354-8">
   “Except as otherwise provided in this chapter, it shall be unlawful for any individual, partnership, corporation, association, or the state of Washington, its agencies, and political subdivisions to intercept, or record any . . . [p]rivate conversation, by any device electronic or otherwise designed to record or transmit such conversation regardless how the device is powered or actuated without first obtaining the consent of all the persons engaged in the conversation.” <span class="citation no-link">Wash. Rev. Code § 9.78.030</span>(1)(b) (1994).
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b357-6">
   At least one Court of Appeals has adopted a variation of the “closely related offense” rule which looks not to the offense stated by the officer at the time of arrest, but to the offense given by the officer at booking. See
   <em>
    Gassner
   </em>
   v.
   <em>
    Garland,
   </em>
   <span class="citation" data-id="516197"><a href="/opinion/516197/jules-gassner-v-city-of-garland-texas-ml-bates/#398" aria-description="Citation for case: Jules Gassner v. City of Garland, Texas, M.L. Bates">864 F. 2d 394, 398</a></span> (CA5 1989); but see
   <em>
    Sheehy
   </em>
   v.
   <span citation-index="1" class="star-pagination" label="154"> 
    *154
    </span>
<em>
    Plymouth,
   </em>
   <span class="citation" data-id="198626"><a href="/opinion/198626/sheehy-v-town-of-plymouth/#20" aria-description="Citation for case: Sheehy v. Town of Plymouth">191 F. 3d 15, 20</a></span> (CA1 1999) (holding that an arrest
   <em>
    cannot
   </em>
   be justified by an offense given at booking when the offense asserted by the officer at the time of arrest was not closely related). Most of our discussion in this opinion, and our conclusion of invalidity, applies to this variation as well.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b359-7">
   Even absent a requirement that an individual be informed of the reason for arrest when he is taken into custody, he will not be left to wonder for long. “[Pjersons arrested without a warrant must promptly be brought before a neutral magistrate for a judicial determination of probable cause.”
   <em>
    County of Riverside
   </em>
   v.
   <em>
    McLaughlin,
   </em>
   <span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/#53" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U. S. 44, 53</a></span> (1991).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Dickerson v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Dickerson v. United States"
type: case
citation: "530 U.S. 428 (2000)"
parallel_cite: "120 S. Ct. 2326; 147 L. Ed. 2d 405"
neutral_cite: 2000 U.S. LEXIS 4305
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-06-26
docket: 99-5525
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Dickerson v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118380/dickerson-v-united-states/"
  cluster_id: 118380
  opinion_id: 118380
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Berkemer v. McCarty]]", "[[Berghuis v. Thompkins]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "constitutional-rule", "section-3501", "stare-decisis"]
holding: "Miranda is a constitutional rule that Congress may not supersede by statute; § 3501 is unconstitutional and Miranda governs the…"
lake:
  record_id: Dickerson v. United States
  status: verified
  projected_at: 2026-07-06
---

# Dickerson v. United States

*530 U.S. 428 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Dickerson, charged with bank robbery, moved to suppress a statement made without complete *[[Miranda v. Arizona|Miranda]]* warnings. The Government invoked 18 U.S.C. § 3501, a statute enacted after *[[Miranda v. Arizona|Miranda]]* that made the admissibility of confessions turn solely on voluntariness. The Fourth Circuit held § 3501 governed and displaced *[[Miranda v. Arizona|Miranda]]*; the Supreme Court took the case to decide whether Congress could do so.

## Issue
Whether Congress may legislatively supersede *[[Miranda v. Arizona]]* and replace its warning requirement with a pure voluntariness test under § 3501.

## Rule
No; *[[Miranda v. Arizona|Miranda]]* is a constitutional rule beyond Congress's power to overrule by statute. "[W]e conclude that *Miranda* announced a constitutional rule that Congress may not supersede legislatively. Following the rule of *stare decisis*, we decline to overrule *Miranda* ourselves." — 530 U.S. 428, 444. ^pin-444

Because § 3501 sought to reinstate a voluntariness-only standard in place of *[[Miranda v. Arizona|Miranda]]*'s warnings, it could not govern the admissibility of statements obtained in custodial interrogation.

## Application
Section 3501 was Congress's attempt to substitute a voluntariness test for *[[Miranda v. Arizona|Miranda]]*'s warning requirement. Because *[[Miranda v. Arizona|Miranda]]* is constitutionally based, that statute could not displace it, and *[[Miranda v. Arizona|Miranda]]* — not § 3501 — governed the admissibility of Dickerson's statement; the Fourth Circuit's contrary holding was reversed.

## Conclusion
*[[Miranda v. Arizona|Miranda]]* is a constitutional decision that Congress cannot legislatively overrule; § 3501 could not displace it. The judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Dickerson* reaffirms the constitutional status of [[Miranda v. Arizona]]; later cases such as [[Berghuis v. Thompkins]] continue to apply the *[[Miranda v. Arizona|Miranda]]* framework it preserved.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Dickerson v. United States*, 530 U.S. 428 (2000) — https://www.courtlistener.com/opinion/118380/dickerson-v-united-states/ — pinpoint: 444.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f108a8eb5c5442e5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Dickerson v. United States"}, "payload": {"all": [{"cite": "530 U.S. 428", "page": "428", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "530"}, {"cite": "120 S. Ct. 2326", "page": "2326", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "120"}, {"cite": "147 L. Ed. 2d 405", "page": "405", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "147"}, {"cite": "2000 U.S. LEXIS 4305", "page": "4305", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}], "display": "530 U.S. 428", "official": {"cite": "530 U.S. 428", "page": "428", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "530"}, "official_selection_present": true, "record_id": "Dickerson v. United States"}}
{"assertion_id": "fb8cd52680639190", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-444", "record_id": "Dickerson v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-444", "pinpoint_status": "slip-only", "quote": "--- # Dickerson v. United States *530 U.S. 428 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Dickerson, charged with bank robbery, moved to suppress a statement made without complete *Miranda* warnings. The Government invoked 18 U.S.C. § 3501, a statute enacted after *Miranda* that made the admissibility of confessions turn solely on voluntariness. The Fourth Circuit held § 3501 governed and displaced *Miranda*; the Supreme Court took the case to decide whether Congress could do so. ## Issue Whether Congress may legislatively supersede *Miranda v. Arizona* and replace its warning requirement with a pure voluntariness test under § 3501. ## Rule No; *Miranda* is a constitutional rule beyond Congress's power to overrule by statute.", "quote_fidelity": "mismatch", "record_id": "Dickerson v. United States", "star_marker": null}}
{"assertion_id": "6e123130df8dc817", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Dickerson v. United States"}, "payload": {"as_of_content": "2000-06-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Dickerson v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Dickerson v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Dickerson v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Dickerson v. United States",
    "case_name_short": "Dickerson",
    "case_name_full": "Dickerson v. United States",
    "input_case_name": "Dickerson v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-06-26",
    "year": 2000,
    "docket": "99-5525",
    "cluster_id": 118380,
    "lead_opinion_id": 118380,
    "sibling_ids": [
      118380,
      9433984,
      9433985
    ],
    "absolute_url": "/opinion/118380/dickerson-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9261445,
        "score": 20,
        "case_name": "Dickerson v. United States"
      },
      {
        "cluster_id": 9190515,
        "score": 20,
        "case_name": "Dickerson v. United States"
      },
      {
        "cluster_id": 9190514,
        "score": 20,
        "case_name": "Dickerson v. United States"
      },
      {
        "cluster_id": 9263817,
        "score": 20,
        "case_name": "Dickerson v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "530 U.S. 428",
      "volume": "530",
      "reporter": "U.S.",
      "page": "428",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "120 S. Ct. 2326",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "2326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "147 L. Ed. 2d 405",
        "volume": "147",
        "reporter": "L. Ed. 2d",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. LEXIS 4305",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "4305",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "530 U.S. 428",
        "volume": "530",
        "reporter": "U.S.",
        "page": "428",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "120 S. Ct. 2326",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "2326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "147 L. Ed. 2d 405",
        "volume": "147",
        "reporter": "L. Ed. 2d",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. LEXIS 4305",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "4305",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "530 U.S. 428",
    "official_selection": {
      "court_class": "scotus",
      "selected": "530 U.S. 428",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-444",
      "page": null,
      "quote": "--- # Dickerson v. United States *530 U.S. 428 (2000)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Dickerson, charged with bank robbery, moved to suppress a statement made without complete *Miranda* warnings. The Government invoked 18 U.S.C. \u00a7 3501, a statute enacted after *Miranda* that made the admissibility of confessions turn solely on voluntariness. The Fourth Circuit held \u00a7 3501 governed and displaced *Miranda*; the Supreme Court took the case to decide whether Congress could do so. ## Issue Whether Congress may legislatively supersede *Miranda v. Arizona* and replace its warning requirement with a pure voluntariness test under \u00a7 3501. ## Rule No; *Miranda* is a constitutional rule beyond Congress's power to overrule by statute.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Dickerson v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gideon",
          "cluster_id": 4632199,
          "cite": [
            "2019 Ohio 2482",
            "130 N.E.3d 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nader Abdallah",
          "cluster_id": 4574399,
          "cite": [
            "911 F.3d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Alleyne v. United States",
          "cluster_id": 903985,
          "cite": [
            "186 L. Ed. 2d 314",
            "133 S. Ct. 2151",
            "2013 U.S. LEXIS 4543",
            "570 U.S. 99",
            "81 U.S.L.W. 4444",
            "24 Fla. L. Weekly Fed. S 310",
            "2013 WL 2922116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Washington",
          "cluster_id": 145641,
          "cite": [
            "165 L. Ed. 2d 224",
            "126 S. Ct. 2266",
            "547 U.S. 813",
            "2006 U.S. LEXIS 4886"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimbrough v. United States",
          "cluster_id": 145841,
          "cite": [
            "169 L. Ed. 2d 481",
            "128 S. Ct. 558",
            "552 U.S. 85",
            "2007 U.S. LEXIS 13082"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
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
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Citizens United v. Federal Election Commission",
          "cluster_id": 1741,
          "cite": [
            "175 L. Ed. 2d 753",
            "130 S. Ct. 876",
            "558 U.S. 310",
            "2010 U.S. LEXIS 766",
            "22 Fla. L. Weekly Fed. S 73",
            "78 U.S.L.W. 4078",
            "187 L.R.R.M. (BNA) 2961",
            "159 Lab. Cas. (CCH) 10,166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
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
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. California",
          "cluster_id": 799972,
          "cite": [
            "162 L. Ed. 2d 129",
            "125 S. Ct. 2410",
            "545 U.S. 162",
            "2005 U.S. LEXIS 4842",
            "8 A.L.R. Fed. 2d 849"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKune v. Lile",
          "cluster_id": 121146,
          "cite": [
            "153 L. Ed. 2d 47",
            "122 S. Ct. 2017",
            "536 U.S. 24",
            "2002 U.S. LEXIS 4206"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. Flowers",
          "cluster_id": 145663,
          "cite": [
            "164 L. Ed. 2d 415",
            "126 S. Ct. 1708",
            "547 U.S. 220",
            "2006 U.S. LEXIS 3451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paulson v. State",
          "cluster_id": 1754997,
          "cite": [
            "28 S.W.3d 570",
            "2000 Tex. Crim. App. LEXIS 89",
            "2000 WL 1468423"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District Attorney's Office for the Third Judicial District v. Osborne",
          "cluster_id": 145860,
          "cite": [
            "174 L. Ed. 2d 38",
            "129 S. Ct. 2308",
            "557 U.S. 52",
            "2009 U.S. LEXIS 4536",
            "21 Fla. L. Weekly Fed. S 945",
            "77 U.S.L.W. 4498"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holloman Ex Rel. Holloman v. Harland",
          "cluster_id": 76571,
          "cite": [
            "370 F.3d 1252",
            "2004 WL 1178465"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Federal Election Commission v. Wisconsin Right to Life, Inc.",
          "cluster_id": 145706,
          "cite": [
            "168 L. Ed. 2d 329",
            "127 S. Ct. 2652",
            "551 U.S. 449",
            "2007 U.S. LEXIS 8515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Marko",
          "cluster_id": 3008904,
          "cite": [
            "2015 COA 139",
            "434 P.3d 618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Windsor",
          "cluster_id": 945737,
          "cite": [
            "186 L. Ed. 2d 808",
            "133 S. Ct. 2675",
            "2013 U.S. LEXIS 4921",
            "570 U.S. 744",
            "24 Fla. L. Weekly Fed. S 445",
            "81 U.S.L.W. 4633",
            "57 Employee Benefits Cas. (BNA) 1577",
            "2013 WL 3196928",
            "111 A.F.T.R.2d (RIA) 2385",
            "118 Fair Empl. Prac. Cas. (BNA) 1417"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
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
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Morrow v. Barry Balaski",
          "cluster_id": 891221,
          "cite": [
            "719 F.3d 160",
            "98 A.L.R. 6th 777",
            "2013 WL 2466892",
            "2013 U.S. App. LEXIS 11246"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dickerson v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118380 OR 9433984 OR 9433985) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI4MjQzMjAwMDAwJnM9NDUwNDQwNyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118380+OR+9433984+OR+9433985%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118380 OR 9433984 OR 9433985)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NDkmcz0yNjM4NDM0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118380+OR+9433984+OR+9433985%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118380 OR 9433984 OR 9433985)",
        "reviewed": 73,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 73,
        "triage_read": 1,
        "triage_snippet_classified": 72
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118380 OR 9433984 OR 9433985)",
    "indexed_citing_opinions": 1204,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118380,
        "count": 998,
        "count_source": "search"
      },
      {
        "opinion_id": 9433984,
        "count": 237,
        "count_source": "search"
      },
      {
        "opinion_id": 9433985,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1934,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/dickerson-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyODM5Njgmcz0xMDM2ODk5MiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118380+OR+9433984+OR+9433985%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118380,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 97552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 102164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 105072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 105920,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 106129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 106761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 106987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 107423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 107978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 108794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 109091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 109491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 110783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 111865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 117982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 118021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 118038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 118133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 118140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 118149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 118278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 118332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 521076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 761256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118380,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T02:29:37Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:30:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:30:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:34:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:30:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Dickerson v. United States (truncated)

```
<div>
<center><b><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U.S. 428</a></span> (2000)</b></center>
<center><h1>DICKERSON<br>
v.<br>
UNITED STATES</h1></center>
<center>No. 99-5525.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued April 19, 2000.</center>
<center>Decided June 26, 2000.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FOURTH CIRCUIT
<p><span class="star-pagination">*430</span> <span class="star-pagination">*430</span> Rehnquist, C. J., delivered the opinion of the Court, in which Stevens, O'Connor, Kennedy, Souter, Ginsburg, and Breyer, JJ., joined. Scalia, J., filed a dissenting opinion, in which Thomas, J., joined, <i>post,</i>  p. 444.</p>
<p><i>James W. Hundley,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./528/1072/">528 U. S. 1072</a></span>, argued the cause for petitioner. With him on the briefs were <i>Carter G. Phillips, Jeffrey T. Green,</i> and <i>Kurt H. Jacobs.</i> </p>
<p><i>Solicitor General Waxman</i> argued the cause for the United States. With him on the briefs were <i>Attorney General Reno, Assistant Attorney General Robinson, Deputy Solicitor General Dreeben, James A. Feldman,</i> and <i>Lisa S. Blatt.</i> </p>
<p><i>Paul G. Cassell,</i> by invitation of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./528/1045/">528 U. S. 1045</a></span>, argued the cause as <i>amicus curiae</i> urging affirmance. With him on the brief were <i>Daniel J. Popeo</i> and <i>Paul D. Kamenar.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*431</span> Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), we held that certain warnings must be given before a suspect's statement made during custodial interrogation could be admitted in <span class="star-pagination">*432</span> evidence. In the wake of that decision, Congress enacted <span class="citation no-link">18 U. S. C. § 3501</span>, which in essence laid down a rule that the admissibility of such statements should turn only on whether or not they were voluntarily made. We hold that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i>  being a constitutional decision of this Court, may not be in effect overruled by an Act of Congress, and we decline to overrule <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> ourselves. We therefore hold that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and its progeny in this Court govern the admissibility of statements made during custodial interrogation in both state and federal courts.</p>
<p>Petitioner Dickerson was indicted for bank robbery, conspiracy to commit bank robbery, and using a firearm in the course of committing a crime of violence, all in violation of the applicable provisions of Title 18 of the United States Code. Before trial, Dickerson moved to suppress a statement he had made at a Federal Bureau of Investigation field office, on the grounds that he had not received "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>  warnings" before being interrogated. The District Court granted his motion to suppress, and the Government took an interlocutory appeal to the United States Court of Appeals for the Fourth Circuit. That court, by a divided vote, reversed the District Court's suppression order. It agreed with the District Court's conclusion that petitioner had not received <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before making his statement. But it went on to hold that § 3501, which in effect makes the admissibility of statements such as Dickerson's turn solely on whether they were made voluntarily, was satisfied in this case. It then concluded that our decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  was not a constitutional holding, and that, therefore, Congress could by statute have the final say on the question of admissibility. <span class="citation" data-id="9491840"><a href="/opinion/761256/united-states-v-charles-thomas-dickerson-washington-legal-foundation-safe/" aria-description="Citation for case: United States v. Charles Thomas Dickerson, Washington...">166 F. 3d 667</a></span> (1999).</p>
<p>Because of the importance of the questions raised by the Court of Appeals' decision, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./528/1045/">528 U. S. 1045</a></span> (1999), and now reverse.</p>
<p>We begin with a brief historical account of the law governing the admission of confessions. Prior to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> we <span class="star-pagination">*433</span> evaluated the admissibility of a suspect's confession under a voluntariness test. The roots of this test developed in the common law, as the courts of England and then the United States recognized that coerced confessions are inherently untrustworthy. See, <i>e. g., </i><i>King</i> v. <i>Rudd,</i> 1 Leach 115, 117-118, 122-123, 168 Eng. Rep. 160, 161, 164 (K. B. 1783) (Lord Mansfield, C. J.) (stating that the English courts excluded confessions obtained by threats and promises); <i>King</i> v. <i>Warickshall,</i> 1 Leach 262, 263-264, 168 Eng. Rep. 234, 235 (K. B. 1783) ("A free and voluntary confession is deserving of the highest credit, because it is presumed to flow from the strongest sense of guilt . . . but a confession forced from the mind by the flattery of hope, or by the torture of fear, comes in so questionable a shape . . . that no credit ought to be given to it; and therefore it is rejected"); <i>King</i> v. <i>Parratt,</i> 4 Car. &amp; P. 570, 172 Eng. Rep. 829 (N. P. 1831); <i>Queen</i> v. <i>Garner,</i>  <span class="citation" data-id="6142254"><a href="/opinion/6274346/sherman-v-garfield/" aria-description="Citation for case: Sherman v. Garfield">1 Den. 329</a></span>, 169 Eng. Rep. 267 (Ct. Crim. App. 1848); <i>Queen</i>  v. <i>Baldry,</i> <span class="citation" data-id="5465219"><a href="/opinion/5620246/church-v-bull/" aria-description="Citation for case: Church v. Bull">2 Den. 430</a></span>, 169 Eng. Rep. 568 (Ct. Crim. App. 1852); <i>Hopt</i> v. <i>Territory of Utah,</i> <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/" aria-description="Citation for case: Hopt v. People of Territory of Utah">110 U. S. 574</a></span> (1884); <i>Pierce</i>  v. <i>United States,</i> <span class="citation" data-id="94327"><a href="/opinion/94327/pierce-v-united-states/#357" aria-description="Citation for case: Pierce v. United States">160 U. S. 355, 357</a></span> (1896). Over time, our cases recognized two constitutional bases for the requirement that a confession be voluntary to be admitted into evidence: the Fifth Amendment right against self-incrimination and the Due Process Clause of the Fourteenth Amendment. See, <i>e. g., </i><i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542</a></span> (1897) (stating that the voluntariness test "is controlled by that portion of the Fifth Amendment . . . commanding that no person `shall be compelled in any criminal case to be a witness against himself' "); <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936) (reversing a criminal conviction under the Due Process Clause because it was based on a confession obtained by physical coercion).</p>
<p>While <i><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span></i> was decided before <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i> and its progeny, for the middle third of the 20th century our cases based the rule against admitting coerced confessions primarily, if not exclusively, on notions of due process. We applied the <span class="star-pagination">*434</span> due process voluntariness test in "some 30 different cases decided during the era that intervened between <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i>  and <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> [(1964)]." <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#223" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 223</a></span> (1973). See, <i>e. g., </i><i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963); <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944); <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940). Those cases refined the test into an inquiry that examines "whether a defendant's will was overborne" by the circumstances surrounding the giving of a confession. <i>Schneckloth,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 226</a></span>. The due process test takes into consideration "the totality of all the surrounding circumstancesboth the characteristics of the accused and the details of the interrogation." <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Ibid.</a></span></i> See also <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#513" aria-description="Citation for case: Haynes v. Washington"><i>Haynes, supra,</i> at 513</a></span>; <i>Gallegos</i> v. <i>Colorado,</i> <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/#55" aria-description="Citation for case: Gallegos v. Colorado">370 U. S. 49, 55</a></span> (1962); <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 440</a></span> (1961) ("[A]ll the circumstances attendant upon the confession must be taken into account"); <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#404" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 404</a></span> (1945) ("If all the attendant circumstances indicate that the confession was coerced or compelled, it may not be used to convict a defendant"). The determination "depend[s] upon a weighing of the circumstances of pressure against the power of resistance of the person confessing." <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/#185" aria-description="Citation for case: Stein v. New York">346 U. S. 156, 185</a></span> (1953).</p>
<p>We have never abandoned this due process jurisprudence, and thus continue to exclude confessions that were obtained involuntarily. But our decisions in <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), and <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> changed the focus of much of the inquiry in determining the admissibility of suspects' incriminating statements. In <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span>,</i> we held that the Fifth Amendment's Self-Incrimination Clause is incorporated in the Due Process Clause of the Fourteenth Amendment and thus applies to the States. 378 U. S., at 6-11. We decided <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> on the heels of <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span>.</i> </p>
<p>In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> we noted that the advent of modern custodial police interrogation brought with it an increased concern <span class="star-pagination">*435</span> about confessions obtained by coercion.<sup>[1]</sup> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 445-458</a></span>. Because custodial police interrogation, by its very nature, isolates and pressures the individual, we stated that "[e]ven without employing brutality, the `third degree' or [other] specific stratagems, . . . custodial interrogation exacts a heavy toll on individual liberty and trades on the weakness of individuals." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#455" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 455</a></span>. We concluded that the coercion inherent in custodial interrogation blurs the line between voluntary and involuntary statements, and thus heightens the risk that an individual will not be "accorded his privilege under the Fifth Amendment . . . not to be compelled to incriminate himself." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#439" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 439</a></span>. Accordingly, we laid down "concrete constitutional guidelines for law enforcement agencies and courts to follow." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#442" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 442</a></span>. Those guidelines established that the admissibility in evidence of any statement given during custodial interrogation of a suspect would depend on whether the police provided the suspect with four warnings. These warnings (which have come to be known colloquially as "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> rights") are: a suspect "has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 479</a></span>.</p>
<p>Two years after <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was decided, Congress enacted § 3501. That section provides, in relevant part:</p>
<blockquote>"(a) In any criminal prosecution brought by the United States or by the District of Columbia, a confession . . . shall be admissible in evidence if it is voluntarily given. Before such confession is received in evidence, the trial <span class="star-pagination">*436</span> judge shall, out of the presence of the jury, determine any issue as to voluntariness. If the trial judge determines that the confession was voluntarily made it shall be admitted in evidence and the trial judge shall permit the jury to hear relevant evidence on the issue of voluntariness and shall instruct the jury to give such weight to the confession as the jury feels it deserves under all the circumstances. "(b) The trial judge in determining the issue of voluntariness shall take into consideration all the circumstances surrounding the giving of the confession, including (1) the time elapsing between arrest and arraignment of the defendant making the confession, if it was made after arrest and before arraignment, (2) whether such defendant knew the nature of the offense with which he was charged or of which he was suspected at the time of making the confession, (3) whether or not such defendant was advised or knew that he was not required to make any statement and that any such statement could be used against him, (4) whether or not such defendant had been advised prior to questioning of his right to the assistance of counsel; and (5) whether or not such defendant was without the assistance of counsel when questioned and when giving such confession. "The presence or absence of any of the abovementioned factors to be taken into consideration by the judge need not be conclusive on the issue of voluntariness of the confession." Given § 3501's express designation of voluntariness as the touchstone of admissibility, its omission of any warning requirement, and the instruction for trial courts to consider a nonexclusive list of factors relevant to the circumstances of a confession, we agree with the Court of Appeals that Congress intended by its enactment to overrule <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i>  See also <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#464" aria-description="Citation for case: Davis v. United States">512 U. S. 452, 464</a></span> (1994) (Scalia, J.,concurring) (stating that, prior to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i>  <span class="star-pagination">*437</span> "voluntariness <i>vel non</i> was the touchstone of admissibility of confessions"). Because of the obvious conflict between our decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and § 3501, we must address whether Congress has constitutional authority to thus supersede <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> If Congress has such authority, § 3501's totalityof-the-circumstances approach must prevail over <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s requirement of warnings; if not, that section must yield to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s more specific requirements.</blockquote>
<p>The law in this area is clear. This Court has supervisory authority over the federal courts, and we may use that authority to prescribe rules of evidence and procedure that are binding in those tribunals. <i>Carlisle</i> v. <i>United States,</i>  <span class="citation" data-id="9433281"><a href="/opinion/118021/carlisle-v-united-states/#426" aria-description="Citation for case: Carlisle v. United States">517 U. S. 416, 426</a></span> (1996). However, the power to judicially create and enforce nonconstitutional "rules of procedure and evidence for the federal courts exists only in the absence of a relevant Act of Congress." <i>Palermo</i> v. <i>United States,</i> <span class="citation" data-id="9421845"><a href="/opinion/105920/palermo-v-united-states/#353" aria-description="Citation for case: Palermo v. United States">360 U. S. 343, 353, n. 11</a></span> (1959) (citing <i>Funk</i> v. <i>United States,</i> <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/#382" aria-description="Citation for case: Funk v. United States">290 U. S. 371, 382</a></span> (1933), and <i>Gordon</i> v. <i>United States,</i>  <span class="citation" data-id="105072"><a href="/opinion/105072/gordon-v-united-states/#418" aria-description="Citation for case: Gordon v. United States">344 U. S. 414, 418</a></span> (1953)). Congress retains the ultimate authority to modify or set aside any judicially created rules of evidence and procedure that are not required by the Constitution. <span class="citation" data-id="9421845"><a href="/opinion/105920/palermo-v-united-states/#345" aria-description="Citation for case: Palermo v. United States"><i>Palermo, supra,</i> at 345-348</a></span>; <span class="citation" data-id="9433281"><a href="/opinion/118021/carlisle-v-united-states/#426" aria-description="Citation for case: Carlisle v. United States"><i>Carlisle, supra,</i> at 426</a></span>; <i>Vance</i> v. <i>Terrazas,</i> <span class="citation" data-id="9427734"><a href="/opinion/110168/vance-v-terrazas/#265" aria-description="Citation for case: Vance v. Terrazas">444 U. S. 252, 265</a></span> (1980).</p>
<p>But Congress may not legislatively supersede our decisions interpreting and applying the Constitution. See, <i>e. g., </i><i>City of Boerne</i> v. <i>Flores,</i> <span class="citation" data-id="9433509"><a href="/opinion/118140/city-of-boerne-v-flores/#517" aria-description="Citation for case: City of Boerne v. Flores">521 U. S. 507, 517-521</a></span> (1997). This case therefore turns on whether the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> Court announced a constitutional rule or merely exercised its supervisory authority to regulate evidence in the absence of congressional direction. Recognizing this point, the Court of Appeals surveyed <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and its progeny to determine the constitutional status of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision. <span class="citation" data-id="9491840"><a href="/opinion/761256/united-states-v-charles-thomas-dickerson-washington-legal-foundation-safe/#687" aria-description="Citation for case: United States v. Charles Thomas Dickerson, Washington...">166 F. 3d, at 687-692</a></span>. Relying on the fact that we have created several exceptions to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s warnings requirement and that we have repeatedly referred to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings as "prophylactic," <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span>, 653 <span class="star-pagination">*438</span> (1984), and "not themselves rights protected by the Constitution," <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974),<sup>[2]</sup> the Court of Appeals concluded that the protections announced in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are not constitutionally required. <span class="citation" data-id="9491840"><a href="/opinion/761256/united-states-v-charles-thomas-dickerson-washington-legal-foundation-safe/#687" aria-description="Citation for case: United States v. Charles Thomas Dickerson, Washington...">166 F. 3d, at 687-690</a></span>.</p>
<p>We disagree with the Court of Appeals' conclusion, although we concede that there is language in some of our opinions that supports the view taken by that court. But first and foremost of the factors on the other sidethat <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is a constitutional decisionis that both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  and two of its companion cases applied the rule to proceedings in state courtsto wit, Arizona, California, and New York. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#491" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 491-494, 497-499</a></span>. Since that time, we have consistently applied <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s rule to prosecutions arising in state courts. See, <i>e. g., </i><i>Stansbury</i> v. <i>California,</i>  <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">511 U. S. 318</a></span> (1994) <i>(per curiam)</i><i>; </i><i>Minnick</i> v. <i>Mississippi,</i> <span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U. S. 146</a></span> (1990); <i>Arizona</i> v. <i>Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988); <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#481" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 481-482</a></span> (1981). It is beyond dispute that we do not hold a supervisory power over the courts of the several States. <i>Smith</i> v. <i>Phillips,</i> <span class="citation" data-id="9428656"><a href="/opinion/110645/smith-v-phillips/#221" aria-description="Citation for case: Smith v. Phillips">455 U. S. 209, 221</a></span> (1982) ("Federal courts hold no supervisory authority over state judicial proceedings and may intervene only to correct wrongs of constitutional dimension"); <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/#508" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504, 508-509</a></span> (1958). With respect to proceedings in state courts, our "authority is limited to enforcing the commands of the United States Constitution." <i>Mu'Min</i> v. <i>Virginia,</i> <span class="citation" data-id="9432296"><a href="/opinion/112604/mumin-v-virginia/#422" aria-description="Citation for case: Mu&#x27;Min v. Virginia">500 U. S. 415, 422</a></span> (1991). See also <i>Harris</i> v. <i>Rivera,</i> <span class="citation" data-id="9428554"><a href="/opinion/110590/harris-v-rivera/#344" aria-description="Citation for case: Harris v. Rivera">454 U. S. 339, 344-345</a></span> (1981) <i>(per curiam)</i>  (stating that "[f]ederal judges . . . may not require the observance <span class="star-pagination">*439</span> of any special procedures" in state courts "except when necessary to assure compliance with the dictates of the Federal Constitution").<sup>[3]</sup></p>
<p>The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion itself begins by stating that the Court granted certiorari "to explore some facets of the problems . . . of applying the privilege against self-incrimination to in-custody interrogation, <i>and to give concrete constitutional guidelines for law enforcement agencies and courts to follow.</i> " <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#441" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 441-442</a></span> (emphasis added). In fact, the majority opinion is replete with statements indicating that the majority thought it was announcing a constitutional rule.<sup>[4]</sup> Indeed, the Court's ultimate conclusion was that the <span class="star-pagination">*440</span> unwarned confessions obtained in the four cases before the Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> "were obtained from the defendant under circumstances that did not meet constitutional standards for protection of the privilege."<sup>[5]</sup><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#491" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 491</a></span>.</p>
<p>Additional support for our conclusion that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is constitutionally based is found in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> Court's invitation for legislative action to protect the constitutional right against coerced self-incrimination. After discussing the "compelling pressures" inherent in custodial police interrogation, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> Court concluded that, "[i]n order to combat these pressures and to permit a full opportunity to exercise the privilege against self-incrimination, the accused must be adequately and effectively apprised of his rights and the exercise of those rights must be fully honored." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 467</a></span>. However, the Court emphasized that it could not foresee "the potential alternatives for protecting the privilege which might be devised by Congress or the States," and it accordingly opined that the Constitution would not preclude legislative solutions that differed from the prescribed <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings but which were "at least as effective in apprising accused persons of their right of silence and in assuring a continuous opportunity to exercise it."<sup>[6]</sup><i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> </p>
<p><span class="star-pagination">*441</span> The Court of Appeals also relied on the fact that we have, after our <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision, made exceptions from its rule in cases such as <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984), and <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971). See <span class="citation" data-id="9491840"><a href="/opinion/761256/united-states-v-charles-thomas-dickerson-washington-legal-foundation-safe/#672" aria-description="Citation for case: United States v. Charles Thomas Dickerson, Washington...">166 F. 3d, at 672, 689-691</a></span>. But we have also broadened the application of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> doctrine in cases such as <i>Doyle</i> v. <i>Ohio,</i> <span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">426 U. S. 610</a></span> (1976), and <i>Arizona</i> v. <i>Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988). These decisions illustrate the principlenot that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is not a constitutional rulebut that no constitutional rule is immutable. No court laying down a general rule can possibly foresee the various circumstances in which counsel will seek to apply it, and the sort of modifications represented by these cases are as much a normal part of constitutional law as the original decision.</p>
<p>The Court of Appeals also noted that in <i>Oregon</i> v. <i>Elstad,</i>  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), we stated that "`[t]he <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> exclusionary rule . . . serves the Fifth Amendment and sweeps more broadly than the Fifth Amendment itself.' " <span class="citation" data-id="9491840"><a href="/opinion/761256/united-states-v-charles-thomas-dickerson-washington-legal-foundation-safe/" aria-description="Citation for case: United States v. Charles Thomas Dickerson, Washington...">166 F. 3d, at 690</a></span> (quoting <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 306</a></span>). Our decision in that caserefusing to apply the traditional "fruits" doctrine developed in Fourth Amendment casesdoes not prove that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is a nonconstitutional decision, but simply recognizes the fact that unreasonable searches under the Fourth Amendment are different from unwarned interrogation under the Fifth Amendment.</p>
<p>As an alternative argument for sustaining the Court of Appeals' decision, the court-invited <i>amicus curiae</i><sup>[7]</sup> contends that the section complies with the requirement that a legislative alternative to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> be equally as effective in preventing coerced confessions. See Brief for Paul G. Cassell <span class="star-pagination">*442</span> as <i>Amicus Curiae</i> 28-39. We agree with the <i>amicus</i> ` contention that there are more remedies available for abusive police conduct than there were at the time <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was decided, see, <i>e. g., </i><i>Wilkins</i> v. <i>May,</i> <span class="citation" data-id="521076"><a href="/opinion/521076/luther-wilkins-jr-v-james-a-may/#194" aria-description="Citation for case: Luther Wilkins, Jr. v. James A. May">872 F. 2d 190, 194</a></span> (CA7 1989) (applying <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i>  <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971), to hold that a suspect may bring a federal cause of action under the Due Process Clause for police misconduct during custodial interrogation). But we do not agree that these additional measures supplement § 3501's protections sufficiently to meet the constitutional minimum. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires procedures that will warn a suspect in custody of his right to remain silent and which will assure the suspect that the exercise of that right will be honored. See, <i>e. g.,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. As discussed above, § 3501 explicitly eschews a requirement of preinterrogation warnings in favor of an approach that looks to the administration of such warnings as only one factor in determining the voluntariness of a suspect's confession. The additional remedies cited by <i>amicus</i> do not, in our view, render them, together with § 3501, an adequate substitute for the warnings required by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> </p>
<p>The dissent argues that it is judicial overreaching for this Court to hold § 3501 unconstitutional unless we hold that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are required by the Constitution, in the sense that nothing else will suffice to satisfy constitutional requirements. <i>Post,</i> at 453-454, 465 (opinion of Scalia, J.). But we need not go further than <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to decide this case. In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court noted that reliance on the traditional totality-of-the-circumstances test raised a risk of overlooking an involuntary custodial confession, 384 U. S, at 457, a risk that the Court found unacceptably great when the confession is offered in the case in chief to prove guilt. The Court therefore concluded that something more than the totality test was necessary. See <i>ibid.;</i> see also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467, 490-491</a></span>. As discussed above, § 3501 reinstates the totality test as <span class="star-pagination">*443</span> sufficient. Section 3501 therefore cannot be sustained if <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is to remain the law.</p>
<p>Whether or not we would agree with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s reasoning and its resulting rule, were we addressing the issue in the first instance, the principles of <i>stare decisis</i> weigh heavily against overruling it now. See, <i>e. g., </i><i>Rhode Island</i> v. <i>Innis,</i>  <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#304" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 304</a></span> (1980) (Burger, C. J., concurring in judgment) ("The meaning of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> has become reasonably clear and law enforcement practices have adjusted to its strictures; I would neither overrule <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> disparage it, nor extend it at this late date"). While "`<i>stare decisis</i> is not an inexorable command,' " <i>State Oil Co.</i> v. <i>Khan,</i> <span class="citation" data-id="118149"><a href="/opinion/118149/state-oil-co-v-khan/#20" aria-description="Citation for case: State Oil Co. v. Khan">522 U. S. 3, 20</a></span> (1997) (quoting <i>Payne</i> v. <i>Tennessee,</i> <span class="citation" data-id="9432389"><a href="/opinion/112643/payne-v-tennessee/#828" aria-description="Citation for case: Payne v. Tennessee">501 U. S. 808, 828</a></span> (1991)), particularly when we are interpreting the Constitution, <i>Agostini</i> v. <i>Felton,</i> <span class="citation" data-id="9433491"><a href="/opinion/118133/agostini-v-felton/#235" aria-description="Citation for case: Agostini v. Felton">521 U. S. 203, 235</a></span> (1997), "even in constitutional cases, the doctrine carries such persuasive force that we have always required a departure from precedent to be supported by some `special justification.' " <i>United States</i> v. <i>International Business Machines Corp.,</i>  <span class="citation" data-id="9433314"><a href="/opinion/118038/united-states-v-international-business-machines-corp/#856" aria-description="Citation for case: United States v. International Business MacHines Corp.">517 U. S. 843, 856</a></span> (1996) (quoting <span class="citation" data-id="9432389"><a href="/opinion/112643/payne-v-tennessee/#842" aria-description="Citation for case: Payne v. Tennessee"><i>Payne, supra,</i> at 842</a></span> (Souter, J., concurring), in turn quoting <i>Arizona</i> v. <i>Rumsey,</i> <span class="citation" data-id="9842058"><a href="/opinion/111194/arizona-v-rumsey/#212" aria-description="Citation for case: Arizona v. Rumsey">467 U. S. 203, 212</a></span> (1984)).</p>
<p>We do not think there is such justification for overruling <i>Miranda. Miranda</i> has become embedded in routine police practice to the point where the warnings have become part of our national culture. See <i>Mitchell</i> v. <i>United States,</i> <span class="citation" data-id="9433785"><a href="/opinion/118278/mitchell-v-united-states/#331" aria-description="Citation for case: Mitchell v. United States">526 U. S. 314, 331-332</a></span> (1999) (Scalia, J., dissenting) (stating that the fact that a rule has found "`wide acceptance in the legal culture' " is "adequate reason not to overrule" it). While we have overruled our precedents when subsequent cases have undermined their doctrinal underpinnings, see, <i>e. g., </i><i>Patterson</i> v. <i>McLean Credit Union,</i> <span class="citation" data-id="9431745"><a href="/opinion/112296/patterson-v-mclean-credit-union/#173" aria-description="Citation for case: Patterson v. McLean Credit Union">491 U. S. 164, 173</a></span> (1989), we do not believe that this has happened to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision. If anything, our subsequent cases have reduced the impact of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule on legitimate law enforcement while reaffirming the decision's core ruling that unwarned <span class="star-pagination">*444</span> statements may not be used as evidence in the prosecution's case in chief.</p>
<p>The disadvantage of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule is that statements which may be by no means involuntary, made by a defendant who is aware of his "rights," may nonetheless be excluded and a guilty defendant go free as a result. But experience suggests that the totality-of-the-circumstances test which § 3501 seeks to revive is more difficult than <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> for law enforcement officers to conform to, and for courts to apply in a consistent manner. See, <i>e. g., </i><i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S., at 515</a></span> ("The line between proper and permissible police conduct and techniques and methods offensive to due process is, at best, a difficult one to draw"). The requirement that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings be given does not, of course, dispense with the voluntariness inquiry. But as we said in <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420</a></span> (1984), "[c]ases in which a defendant can make a colorable argument that a self-incriminating statement was `compelled' despite the fact that the law enforcement authorities adhered to the dictates of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are rare." <i>Id.,</i> at 433, n. 20.</p>
<p>In sum, we conclude that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> announced a constitutional rule that Congress may not supersede legislatively. Following the rule of <i>stare decisis,</i> we decline to overrule <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> ourselves.<sup>[8]</sup> The judgment of the Court of Appeals is therefore</p>
<blockquote>
<i>Reversed.</i>  Justice Scalia, with whom Justice Thomas joins, dissenting.</blockquote>
<p>Those to whom judicial decisions are an unconnected series of judgments that produce either favored or disfavored <span class="star-pagination">*445</span> results will doubtless greet today's decision as a paragon of moderation, since it declines to overrule <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Those who understand the judicial process will appreciate that today's decision is not a reaffirmation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> but a radical revision of the most significant element of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> (as of all cases): the rationale that gives it a permanent place in our jurisprudence.</p>
<p><i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137</a></span> (1803), held that an Act of Congress will not be enforced by the courts if what it prescribes violates the Constitution of the United States. That was the basis on which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was decided. One will search today's opinion in vain, however, for a statement (surely simple enough to make) that what <span class="citation no-link">18 U. S. C. § 3501</span> prescribesthe use at trial of a voluntary confession, even when a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning or its equivalent has failed to be givenviolates the Constitution. The reason the statement does not appear is not only (and perhaps not so much) that it would be absurd, inasmuch as § 3501 excludes from trial precisely what the Constitution excludes from trial, viz., compelled confessions; but also that Justices whose votes are needed to compose today's majority are on record as believing that a violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is <i>not</i> a violation of the Constitution. See <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#457" aria-description="Citation for case: Davis v. United States">512 U. S. 452, 457-458</a></span> (1994) (opinion of the Court, in which Kennedy, J., joined); <i>Duckworth</i> v. <i>Eagan,</i> <span class="citation" data-id="9431819"><a href="/opinion/112322/duckworth-v-eagan/#203" aria-description="Citation for case: Duckworth v. Eagan">492 U. S. 195, 203</a></span> (1989) (opinion of the Court, in which Kennedy, J., joined); <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985) (opinion of the Court by O'Connor, J.); <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984) (opinion of the Court by Rehnquist, J.). And so, to justify today's agreed-upon result, the Court must adopt a significant <i>new,</i>  if not entirely comprehensible, principle of constitutional law. As the Court chooses to describe that principle, statutes of Congress can be disregarded, not only when what they prescribe violates the Constitution, but when what they prescribe contradicts a decision of this Court that "announced a constitutional rule," <i>ante,</i> at 437. As I shall discuss in some <span class="star-pagination">*446</span> detail, the only thing that can possibly mean in the context of this case is that this Court has the power, not merely to apply the Constitution but to expand it, imposing what it regards as useful "prophylactic" restrictions upon Congress and the States. That is an immense and frightening antidemocratic power, and it does not exist.</p>
<p>It takes only a small step to bring today's opinion out of the realm of power-judging and into the mainstream of legal reasoning: The Court need only go beyond its carefully couched iterations that "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> is a constitutional decision," <i>ante,</i> at 438, that "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> is constitutionally based," <i>ante,</i> at 440, that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> has "constitutional underpinnings," <i>ante,</i> at 440, n. 5, and come out and say quite clearly: "We reaffirm today that custodial interrogation that is not preceded by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings or their equivalent violates the Constitution of the United States." It cannot say that, because a majority of the Court does not believe it. The Court therefore acts in plain violation of the Constitution when it denies effect to this Act of Congress.</p>
<p></p>
<h2>I</h2>
<p>Early in this Nation's history, this Court established the sound proposition that constitutional government in a system of separated powers requires judges to regard as inoperative any legislative Act, even of Congress itself, that is "repugnant to the Constitution."</p>
<blockquote>"So if a law be in opposition to the constitution; if both the law and the constitution apply to a particular case, so that the court must either decide that case conformably to the law, disregarding the constitution; or conformably to the constitution, disregarding the law; the court must determine which of these conflicting rules governs the case." <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/#178" aria-description="Citation for case: Marbury v. Madison"><i>Marbury, supra,</i> at 178</a></span>. The power we recognized in <i><span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">Marbury</a></span></i> will thus permit us, indeed require us, to "disregar[d]" § 3501, a duly enacted <span class="star-pagination">*447</span> statute governing the admissibility of evidence in the federal courts, only if it "be in opposition to the constitution"here, assertedly, the dictates of the Fifth Amendment.</blockquote>
<p>It was once possible to characterize the so-called <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  rule as resting (however implausibly) upon the proposition that what the statute here before us permitsthe admission at trial of un-<i>Mirandized</i> confessionsviolates the Constitution. That is the fairest reading of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case itself. The Court began by announcing that the Fifth Amendment privilege against self-incrimination applied in the context of extrajudicial custodial interrogation, see 384 U. S., at 460 467itself a doubtful proposition as a matter both of history and precedent, see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#510" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 510-511</a></span> (Harlan, J., dissenting) (characterizing the Court's conclusion that the Fifth Amendment privilege, rather than the Due Process Clause, governed station house confessions as a "<i>trompe l'oeil</i> "). Having extended the privilege into the confines of the station house, the Court liberally sprinkled throughout its sprawling 60-page opinion suggestions that, because of the compulsion inherent in custodial interrogation, the privilege was violated by any statement thus obtained that did not conform to the rules set forth in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> or some functional equivalent. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 458</a></span> ("Unless adequate protective devices are employed to dispel the compulsion <i>inherent</i> in custodial surroundings, <i>no</i> statement obtained from the defendant can truly be the product of his free choice" (emphases added)); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 461</a></span> ("An individual swept from familiar surroundings into police custody, surrounded by antagonistic forces, and subjected to the techniques of persuasion described above cannot be otherwise than under compulsion to speak"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i>  at 467</a></span> ("We have concluded that without proper safeguards the process of in-custody interrogation . . . contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 457, n. 26</a></span> (noting <span class="star-pagination">*448</span> the "absurdity of denying that a confession obtained under these circumstances is compelled").</p>
<p>The dissenters, for their part, also understood <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s holding to be based on the "premise . . . that pressure on the suspect must be eliminated though it be only the subtle influence of the atmosphere and surroundings." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#512" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 512</a></span> (Harlan, J., dissenting). See also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#535" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 535</a></span> (White, J., dissenting) ("[I]t has never been suggested, until today, that such questioning was so coercive and accused persons so lacking in hardihood that the very first response to the very first question following the commencement of custody must be conclusively presumed to be the product of an overborne will"). And at least one case decided shortly after <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  explicitly confirmed the view. See <i>Orozco</i> v. <i>Texas,</i> <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/#326" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324, 326</a></span> (1969) ("[T]he use of these admissions obtained in the absence of the required warnings was a flat violation of the Self-Incrimination Clause of the Fifth Amendment as construed in <i>Miranda</i> ").</p>
<p>So understood, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was objectionable for innumerable reasons, not least the fact that cases spanning more than 70 years had rejected its core premise that, absent the warnings and an effective waiver of the right to remain silent and of the (thitherto unknown) right to have an attorney present, a statement obtained pursuant to custodial interrogation was necessarily the product of compulsion. See <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span> (1958) (confession not involuntary despite denial of access to counsel); <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span> (1958) (same); <i>Powers</i> v. <i>United States,</i> <span class="citation" data-id="97552"><a href="/opinion/97552/powers-v-united-states/" aria-description="Citation for case: Powers v. United States">223 U. S. 303</a></span> (1912) (lack of warnings and counsel did not render statement before United States Commissioner involuntary); <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">162 U. S. 613</a></span> (1896) (same). Moreover, history and precedent aside, the decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> if read as an explication of what the Constitution <i>requires,</i> is preposterous. There is, for example, simply no basis in reason for concluding that a response to the very first question asked, by a suspect who already <i>knows</i> all of the rights described <span class="star-pagination">*449</span> in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning, is anything other than a volitional act. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#533" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 533-534</a></span> (White, J., dissenting). And even if one assumes that the elimination of compulsion absolutely requires informing even the most knowledgeable suspect of his right to remain silent, it cannot conceivably require the right to have <i>counsel</i> present. There is a world of difference, which the Court recognized under the traditional voluntariness test but ignored in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> between compelling a suspect to incriminate himself and preventing him from foolishly doing so of his own accord. Only the latter (which is <i>not</i> required by the Constitution) could explain the Court's inclusion of a right to counsel and the requirement that it, too, be knowingly and intelligently waived. Counsel's presence is not required to tell the suspect that he <i>need</i> not speak; the interrogators can do that. The only good reason for having counsel there is that he can be counted on to advise the suspect that he <i>should</i> not speak. See <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#59" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 59</a></span> (1949) (Jackson, J., concurring in result in part and dissenting in part) ("[A]ny lawyer worth his salt will tell the suspect in no uncertain terms to make no statement to police under any circumstances").</p>
<p>Preventing foolish (rather than compelled) confessions is likewise the only conceivable basis for the rules (suggested in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444-445, 473-474</a></span>), that courts must exclude any confession elicited by questioning conducted, without interruption, after the suspect has indicated a desire to stand on his right to remain silent, see <i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#105" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 105-106</a></span> (1975), or initiated by police after the suspect has expressed a desire to have counsel present, see <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span>, 484 485 (1981). Nonthreatening attempts to persuade the suspect to reconsider that initial decision are not, without more, enough to render a change of heart the product of anything other than the suspect's free will. Thus, what is most remarkable about the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decisionand what <span class="star-pagination">*450</span> made it unacceptable as a matter of straightforward constitutional interpretation in the <i><span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">Marbury</a></span></i> traditionis its palpable hostility toward the act of confession <i>per se,</i> rather than toward what the Constitution abhors, <i>compelled</i> confession. See <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977) ("[F]ar from being prohibited by the Constitution, admissions of guilt by wrongdoers, if not coerced, are inherently desirable"). The Constitution is not, unlike the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> majority, offended by a criminal's commendable qualm of conscience or fortunate fit of stupidity. Cf. <i>Minnick</i> v. <i>Mississippi,</i> <span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/#166" aria-description="Citation for case: Minnick v. Mississippi">498 U. S. 146, 166-167</a></span> (1990) (Scalia, J., dissenting).</p>
<p>For these reasons, and others more than adequately developed in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> dissents and in the subsequent works of the decision's many critics, any conclusion that a violation of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rules <i>necessarily</i> amounts to a violation of the privilege against compelled self-incrimination can claim no support in history, precedent, or common sense, and as a result would at least presumptively be worth reconsidering even at this late date. But that is unnecessary, since the Court has (thankfully) long since abandoned the notion that failure to comply with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s rules is itself a violation of the Constitution.</p>
<p></p>
<h2>II</h2>
<p>As the Court today acknowledges, since <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> we have explicitly, and repeatedly, interpreted that decision as having announced, not the circumstances in which custodial interrogation runs afoul of the Fifth or Fourteenth Amendment, but rather only "prophylactic" rules that go beyond the right against compelled self-incrimination. Of course the seeds of this "prophylactic" interpretation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> were present in the decision itself. See <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#439" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 439</a></span> (discussing the "necessity for procedures which assure that the [suspect] is accorded his privilege"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#447" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 447</a></span> ("[u]nless a proper limitation upon custodial interrogation is achieved such as these decisions will advancethere can be no assurance <span class="star-pagination">*451</span> that practices of this nature will be eradicated"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i>  at 457</a></span> ("[i]n these cases, we might not find the defendants' statements to have been involuntary in traditional terms"); <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span></i> (noting "concern for adequate safeguards to protect precious Fifth Amendment rights" and the "potentiality for compulsion" in Ernesto Miranda's interrogation). In subsequent cases, the seeds have sprouted and borne fruit: The Court has squarely concluded that it is possibleindeed not uncommonfor the police to violate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> without also violating the Constitution.</p>
<p><i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974), an opinion for the Court written by then-Justice Rehnquist, rejected the true-to-<span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison"><i>Marbury,</i></a></span> failure-to-warn-as-constitutional-violation interpretation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> It held that exclusion of the "fruits" of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violationthe statement of a witness whose identity the defendant had revealed while in custodywas not required. The opinion explained that the question whether the "police conduct complained of directly infringed upon respondent's right against compulsory selfincrimination" was a "separate question" from "whether it instead violated only the prophylactic rules developed to protect that right." <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#439" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 439</a></span>. The "procedural safeguards" adopted in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court said, "were not themselves rights protected by the Constitution but were instead measures to insure that the right against compulsory self-incrimination was protected," and to "provide practical reinforcement for the right," <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 444</a></span>. Comparing the particular facts of the custodial interrogation with the "historical circumstances underlying the privilege," <i>ibid.,</i>  the Court concluded, unequivocally, that the defendant's statement could not be termed "involuntary as that term has been defined in the decisions of this Court," <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker"><i>id.,</i> at 445</a></span>, and thus that there had been no constitutional violation, notwithstanding the clear violation of the "procedural rules later established in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> " <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span></i> Lest there be any confusion on the point, the Court reiterated that the "police conduct at <span class="star-pagination">*452</span> issue here did not abridge respondent's constitutional privilege against compulsory self-incrimination, but departed only from the prophylactic standards later laid down by this Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to safeguard that privilege." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#446" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 446</a></span>. It is clear from our cases, of course, that if the statement in <i>Tucker had</i> been obtained in violation of the Fifth Amendment, the statement and its fruits would have been excluded. See <i>Nix</i> v. <i>Williams,</i> <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#442" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 442</a></span> (1984).</p>
<p>The next year, in <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975), the Court held that a defendant's statement taken in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that was nonetheless <i>voluntary</i> could be used at trial for impeachment purposes. This holding turned upon the recognition that violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is not unconstitutional compulsion, since statements obtained in actual violation of the privilege against compelled self-incrimination, "as opposed to . . . taken in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> " quite simply "may not be put to any testimonial use whatever against [the defendant] in a criminal trial," including as impeachment evidence. <i>New Jersey</i> v. <i>Portash,</i> <span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 459</a></span> (1979). See also <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span>, 397 398 (1978) (holding that while statements obtained in violation of <i>Miranda</i> may be used for impeachment if otherwise trustworthy, the Constitution prohibits "<i>any</i> criminal trial use against a defendant of his <i>involuntary</i> statement").</p>
<p>Nearly a decade later, in <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984), the Court relied upon the fact that "[t]he prophylactic <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings . . . are `not themselves rights protected by the Constitution,' " <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span></i> at 654 (quoting <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 444</a></span>), to create a "public safety" exception. In that case, police apprehended, after a chase in a grocery store, a rape suspect known to be carrying a gun. After handcuffing and searching him (and finding no gun)but before reading him his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warningsthe police demanded to know where the gun was. The defendant nodded in the direction of some empty cartons and responded that "the gun is over there." The Court held that both the unwarned <span class="star-pagination">*453</span> statement"the gun is over there"and the recovered weapon were admissible in the prosecution's case in chief under a "public safety exception" to the "prophylactic rules enunciated in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> " 467 U. S., at 653. It explicitly acknowledged that if the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were an imperative of the Fifth Amendment itself, such an exigency exception would be impossible, since the Fifth Amendment's bar on compelled self-incrimination is absolute, and its "`strictures, unlike the Fourth's are not removed by showing reasonableness,' " 467 U. S., at 653, n. 3. (For the latter reason, the Court found it necessary to note that respondent did not "claim that [his] statements were actually compelled by police conduct which overcame his will to resist," <i>id.,</i> at 654.)</p>
<p>The next year, the Court again declined to apply the "fruit of the poisonous tree" doctrine to a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation, this time allowing the admission of a suspect's properly warned statement even though it had been preceded (and, arguably, induced) by an earlier inculpatory statement taken in violation of <i>Miranda. Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985). As in <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span>,</i> the Court distinguished the case from those holding that a confession obtained as a result of an unconstitutional search is inadmissible, on the ground that the violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not involve an "actual infringement of the suspect's constitutional rights," <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 308</a></span>. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court explained, "sweeps more broadly than the Fifth Amendment itself," and <i>"Miranda</i> `s preventive medicine provides a remedy even to the defendant who has suffered no identifiable constitutional harm." <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 306-307</a></span>. "[E]rrors [that] are made by law enforcement officers in administering the prophylactic <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> procedures . . . should not breed the same irremediable consequences as police infringement of the Fifth Amendment itself." <i>Id.,</i> at 308-309.</p>
<p>In light of these cases, and our statements to the same effect in others, see, <i>e. g., </i><i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#457" aria-description="Citation for case: Davis v. United States">512 U. S., at 457-458</a></span>; <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#690" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 690-691</a></span> (1993); <span class="star-pagination">*454</span> <i>Eagan,</i> <span class="citation" data-id="9431819"><a href="/opinion/112322/duckworth-v-eagan/#203" aria-description="Citation for case: Duckworth v. Eagan">492 U. S., at 203</a></span>, it is simply no longer possible for the Court to conclude, even if it wanted to, that a violation of <i>Miranda'</i> s rules is a violation of the Constitution. But as I explained at the outset, that is what is required before the Court may disregard a law of Congress governing the admissibility of evidence in federal court. The Court today insists that the <i>decision</i> in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is a "constitutional" one, <i>ante,</i>  at 432, 438; that it has "constitutional underpinnings," <i>ante,</i>  at 440, n. 5; a "constitutional basis" and a "constitutional origin," <i>ante,</i> at 439, n. 3; that it was "constitutionally based," <i>ante,</i> at 440; and that it announced a "constitutional rule," <i>ante,</i> at 437, 439, 441, 444. It is fine to play these word games; but what makes a decision "constitutional" in the only sense relevant herein the sense that renders it impervious to supersession by congressional legislation such as § 3501 is the determination that the Constitution <i>requires</i> the result that the decision announces and the statute ignores. By disregarding congressional action that concededly does not violate the Constitution, the Court flagrantly offends fundamental principles of separation of powers, and arrogates to itself prerogatives reserved to the representatives of the people.</p>
<p>The Court seeks to avoid this conclusion in two ways: First, by misdescribing these post-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> cases as mere dicta. The Court concedes only "that there is language in some of our opinions that supports the view" that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s protections are not "constitutionally required." <i>Ante,</i> at 438. It is not a matter of <i>language;</i> it is a matter of <i>holdings.</i> The proposition that failure to comply with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s rules does not establish a constitutional violation was central to the <i>holdings</i> of <i>Tucker, Hass, Quarles,</i> and <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>.</i> </p>
<p>The second way the Court seeks to avoid the impact of these cases is simply to disclaim responsibility for reasoned decisionmaking. It says:</p>
<blockquote>"These decisions illustrate the principlenot that <i>Mi-</i>  <i>randa</i> is not a constitutional rulebut that no constitutional rule is immutable. No court laying down a general <span class="star-pagination">*455</span> rule can possibly foresee the various circumstances in which counsel will seek to apply it, and the sort of modifications represented by these cases are as much a normal part of constitutional law as the original decision." <i>Ante,</i> at 441. The issue, however, is not whether court rules are "mutable"; they assuredly are. It is not whether, in the light of "various circumstances," they can be "modifi[ed]"; they assuredly can. The issue is whether, <i>as mutated and modified,</i> they must <i>make sense.</i> The requirement that they do so is the only thing that prevents this Court from being some sort of nine-headed Caesar, giving thumbs-up or thumbs-down to whatever outcome, case by case, suits or offends its collective fancy. And if confessions procured in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  are confessions "compelled" in violation of the Constitution, the post-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> decisions I have discussed do not make sense. The only reasoned basis for their outcome was that a violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is <i>not</i> a violation of the Constitution. If, for example, as the Court acknowledges was the holding of <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,</i> "the traditional `fruits' doctrine developed in Fourth Amendment cases" (that the fruits of evidence obtained unconstitutionally must be excluded from trial) does <i>not</i> apply to the fruits of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violations, <i>ante,</i> at 441; and if the reason for the difference is <i>not</i> that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violations are not constitutional violations (which is plainly and flatly what <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span></i> said); then the Court must come up with some <i>other</i> explanation for the difference. (That will take quite a bit of doing, by the way, since it is <i>not</i> clear on the face of the Fourth Amendment that evidence obtained in violation of that guarantee must be excluded from trial, whereas it <i>is</i> clear on the face of the Fifth Amendment that unconstitutionally compelled confessions cannot be used.) To say simply that "unreasonable searches under the Fourth Amendment are different from unwarned interrogation under the Fifth Amendment," <i>ante,</i> at 441, is true but supremely unhelpful.</blockquote>
<p><span class="star-pagination">*456</span> Finally, the Court asserts that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> must be a "constitutional decision" announcing a "constitutional rule," and thus immune to congressional modification, because we have since its inception applied it to the States. If this argument is meant as an invocation of <i>stare decisis,</i> it fails because, though it is true that our cases applying <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> against the States must be reconsidered if <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is not required by the Constitution, it is likewise true that our cases (discussed above) based on the principle that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is <i>not</i>  required by the Constitution will have to be reconsidered if it <i>is.</i> So the <i>stare decisis</i> argument is a wash. If, on the other hand, the argument is meant as an appeal to logic rather than <i>stare decisis,</i> it is a classic example of begging the question: Congress's attempt to set aside <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> since it represents an assertion that violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is not a violation of the Constitution, <i>also</i> represents an assertion that the Court has no power to impose <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> on the States. To answer this assertionnot by showing why violation of <i>Miranda is</i> a violation of the Constitutionbut by asserting that <i>Miranda does</i> apply against the States, is to assume precisely the point at issue. In my view, our continued application of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> code to the States despite our consistent statements that running afoul of its dictates does not necessarilyor even usuallyresult in an actual constitutional violation, represents not the source of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s salvation but rather evidence of its ultimate illegitimacy. See generally J. Grano, Confessions, Truth, and the Law 173-198 (1993); Grano, Prophylactic Rules in Criminal Procedure: A Question of Article III Legitimacy, <span class="citation no-link">80 Nw. U. L. Rev. 100</span> (1985). As Justice Stevens has elsewhere explained: "This Court's power to require state courts to exclude probative self-incriminatory statements rests entirely on the premise that the use of such evidence violates the Federal Constitution. . . . If the Court does not accept that premise, it must regard the holding in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case itself, as well as all of the federal jurisprudence that has <span class="star-pagination">*457</span> evolved from that decision, as nothing more than an illegitimate exercise of raw judicial power." <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#370" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 370</a></span> (dissenting opinion). Quite so.</p>
<p></p>
<h2>III</h2>
<p>There was available to the Court a means of reconciling the established proposition that a violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not itself offend the Fifth Amendment with the Court's assertion of a right to ignore the present statute. That means of reconciliation was argued strenuously by both petitioner and the United States, who were evidently more concerned than the Court is with maintaining the coherence of our jurisprudence. It is not mentioned in the Court's opinion because, I assume, a majority of the Justices intent on reversing believes that incoherence is the lesser evil. They may be right.</p>
<p>Petitioner and the United States contend that there is nothing at all exceptional, much less unconstitutional, about the Court's adopting prophylactic rules to buttress constitutional rights, and enforcing them against Congress and the States. Indeed, the United States argues that "[p]rophylactic rules are now and have been for many years a feature of this Court's constitutional adjudication." Brief for United States 47. That statement is not wholly inaccurate, if by "many years" one means since the mid-1960's. However, in their zeal to validate what is in my view a lawless practice, the United States and petitioner greatly overstate the frequency with which we have engaged in it. For instance, petitioner cites several cases in which the Court quite simply exercised its traditional judicial power to define the scope of constitutional protections and, relatedly, the circumstances in which they are violated. See <i>Loretto</i> v. <i>Teleprompter Manhattan CATV Corp.,</i> <span class="citation" data-id="9428911"><a href="/opinion/110783/loretto-v-teleprompter-manhattan-catv-corp/#436" aria-description="Citation for case: Loretto v. Teleprompter Manhattan CATV Corp.">458 U. S. 419, 436-437</a></span> (1982) (holding that a permanent physical occupation constitutes a <i>per se</i> taking); <i>Maine</i> v. <i>Moulton,</i> <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 176</a></span> (1985) (holding that the Sixth Amendment right to the assistance <span class="star-pagination">*458</span> of counsel is <i>actually</i> "violated when the State obtains incriminating statements by knowingly circumventing the accused's right to have counsel present in a confrontation between the accused and a state agent").</p>
<p>Similarly unsupportive of the supposed practice is <i>Bruton</i>  v. <i>United States,</i> <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U. S. 123</a></span> (1968), where we concluded that the Confrontation Clause of the Sixth Amendment forbids the admission of a nontestifying codefendant's facially incriminating confession in a joint trial, even where the jury has been given a limiting instruction. That decision was based, not upon the theory that this was desirable protection "beyond" what the Confrontation Clause technically required; but rather upon the self-evident proposition that the inability to cross-examine an available witness whose damaging out-of-court testimony is introduced violates the Confrontation Clause, combined with the conclusion that in these circumstances a mere jury instruction can never be relied upon to prevent the testimony from being damaging, see <i>Richardson</i> v. <i>Marsh,</i> <span class="citation" data-id="9430922"><a href="/opinion/111865/richardson-v-marsh/#207" aria-description="Citation for case: Richardson v. Marsh">481 U. S. 200, 207-208</a></span> (1987).</p>
<p>The United States also relies on our cases involving the question whether a State's procedure for appointed counsel's withdrawal of representation on appeal satisfies the State's constitutional obligation to "`affor[d] adequate and effective appellate review to indigent defendants.' " <i>Smith</i> v. <i>Robbins,</i> <span class="citation" data-id="9433893"><a href="/opinion/118332/smith-v-robbins/#276" aria-description="Citation for case: Smith v. Robbins">528 U. S. 259, 276</a></span> (2000) (quoting <i>Griffin</i> v. <i>Illinois,</i> <span class="citation" data-id="9421263"><a href="/opinion/105382/griffin-v-illinois/#20" aria-description="Citation for case: Griffin v. Illinois">351 U. S. 12, 20</a></span> (1956)). In <i>Anders</i> v. <i>California,</i> <span class="citation" data-id="9423399"><a href="/opinion/107423/anders-v-california/" aria-description="Citation for case: Anders v. California">386 U. S. 738</a></span> (1967), we concluded that California's procedure governing withdrawal fell short of the constitutional minimum, and we outlined a procedure that <i>would</i> meet that standard. But as we made clear earlier this Term in <i>Smith,</i> which upheld a procedure <i>different</i> from the one <i><span class="citation" data-id="9423399"><a href="/opinion/107423/anders-v-california/" aria-description="Citation for case: Anders v. California">Anders</a></span></i> suggested, the benchmark of constitutionality is the constitutional requirement of adequate representation, and not some excrescence upon that requirement decreed, for safety's sake, by this Court.</p>
<p><span class="star-pagination">*459</span> In a footnote, the United States directs our attention to certain overprotective First Amendment rules that we have adopted to ensure "breathing space" for expression. See <i>Gertz</i> v. <i>Robert Welch, Inc.,</i> <span class="citation" data-id="9425816"><a href="/opinion/109091/gertz-v-robert-welch-inc/#340" aria-description="Citation for case: Gertz v. Robert Welch, Inc.">418 U. S. 323, 340, 342</a></span> (1974) (recognizing that in <i>New York Times Co.</i> v. <i>Sullivan,</i> <span class="citation" data-id="9422744"><a href="/opinion/106761/new-york-times-co-v-sullivan/" aria-description="Citation for case: New York Times Co. v. Sullivan">376 U. S. 254</a></span> (1964), we "extended a measure of strategic protection to defamatory falsehood" of public officials); <i>Freedman</i> v. <i>Maryland,</i> <span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/#58" aria-description="Citation for case: Freedman v. Maryland">380 U. S. 51, 58</a></span> (1965) (setting forth "procedural safeguards designed to obviate the dangers of a censorship system" with respect to motion picture obscenity). In these cases, and others involving the First Amendment, the Court has acknowledged that in order to guarantee that protected speech is not "chilled" and thus forgone, it is in some instances necessary to incorporate in our substantive rules a "measure of strategic protection." But that is because the Court has viewed the importation of "chill" as <i>itself</i> a violation of the First Amendmentnot because the Court thought it could go beyond what the First Amendment <i>demanded</i> in order to provide some prophylaxis.</p>
<p>Petitioner and the United States are right on target, however, in characterizing the Court's actions in a case decided within a few years of <i>Miranda, North Carolina</i> v. <i>Pearce,</i>  <span class="citation" data-id="9424091"><a href="/opinion/107978/north-carolina-v-pearce/" aria-description="Citation for case: North Carolina v. Pearce">395 U. S. 711</a></span> (1969). There, the Court concluded that due process would be offended were a judge vindictively to resentence with added severity a defendant who had successfully appealed his original conviction. Rather than simply announce that vindictive sentencing violates the Due Process Clause, the Court went on to hold that "[i]n order to assure the absence of such a [vindictive] motivation, . . . the reasons for [imposing the increased sentence] must affirmatively appear" and must "be based upon objective information concerning identifiable conduct on the part of the defendant occurring after the time of the original sentencing proceeding." <span class="citation" data-id="9424091"><a href="/opinion/107978/north-carolina-v-pearce/#726" aria-description="Citation for case: North Carolina v. Pearce"><i>Id.,</i> at 726</a></span>. The Court later explicitly acknowledged <i><span class="citation" data-id="9424091"><a href="/opinion/107978/north-carolina-v-pearce/" aria-description="Citation for case: North Carolina v. Pearce">Pearce</a></span></i> `s prophylactic character, see <i>Michigan</i> v. <i>Payne,</i> <span class="citation" data-id="8985601"><a href="/opinion/8993355/michigan-v-payne/#53" aria-description="Citation for case: Michigan v. Payne">412 U. S. 47, 53</a></span> (1973). It is true, therefore, that the <span class="star-pagination">*460</span> case exhibits the same fundamental flaw as does <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  when deprived (as it has been) of its original (implausible) pretension to announcement of what the Constitution itself required. That is, although the Due Process Clause may well prohibit punishment based on judicial vindictiveness, the Constitution by no means vests in the courts "any general power to prescribe particular devices `in order to assure the absence of such a motivation,' " <span class="citation" data-id="9424091"><a href="/opinion/107978/north-carolina-v-pearce/#741" aria-description="Citation for case: North Carolina v. Pearce">395 U. S., at 741</a></span> (Black, J., dissenting). Justice Black surely had the right idea when he derided the Court's requirement as "pure legislation if there ever was legislation," <i>ibid.,</i> although in truth <i><span class="citation" data-id="9424091"><a href="/opinion/107978/north-carolina-v-pearce/" aria-description="Citation for case: North Carolina v. Pearce">Pearce</a></span></i> `s rule pales as a legislative achievement when compared to the detailed code promulgated in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i><sup>[1]</sup></p>
<p>The foregoing demonstrates that, petitioner's and the United States' suggestions to the contrary notwithstanding, what the Court did in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> (assuming, as later cases hold, that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> went beyond what the Constitution actually requires) is in fact extraordinary. That the Court has, on rare and recent occasion, repeated the mistake does not transform error into truth, but illustrates the potential for future mischief that the error entails. Where the Constitution has wished to lodge in one of the branches of the Federal Government some limited power to supplement its guarantees, it has said so. See Amdt. 14, § 5 ("The Congress shall have power to enforce, by appropriate legislation, the provisions of this article"). The power with which the Court would endow itself under a "prophylactic" justification for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> goes far beyond what it has permitted Congress to do under authority of that text. Whereas we have insisted <span class="star-pagination">*461</span> that congressional action under § 5 of the Fourteenth Amendment must be "congruent" with, and "proportional" to, a <i>constitutional violation,</i> see <i>City of Boerne</i> v. <i>Flores,</i>  <span class="citation" data-id="9433509"><a href="/opinion/118140/city-of-boerne-v-flores/#520" aria-description="Citation for case: City of Boerne v. Flores">521 U. S. 507, 520</a></span> (1997), the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> nontextual power to embellish confers authority to prescribe preventive measures against not only constitutionally prohibited compelled confessions, but also (as discussed earlier) foolhardy ones.</p>
<p>I applaud, therefore, the refusal of the Justices in the majority to enunciate this boundless doctrine of judicial empowerment as a means of rendering today's decision rational. In nonetheless joining the Court's judgment, however, they overlook two truisms: that actions speak louder than silence, and that (in judge-made law at least) logic will out. Since there is in fact no other principle that can reconcile today's judgment with the post-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> cases that the Court refuses to abandon, what today's decision will stand for, whether the Justices can bring themselves to say it or not, is the power of the Supreme Court to write a prophylactic, extra constitutional Constitution, binding on Congress and the States.</p>
<p></p>
<h2>IV</h2>
<p>Thus, while I agree with the Court that § 3501 cannot be upheld without also concluding that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> represents an illegitimate exercise of our authority to review state-court judgments, I do not share the Court's hesitation in reaching that conclusion. For while the Court is also correct that the doctrine of <i>stare decisis</i> demands some "special justification" for a departure from longstanding precedenteven precedent of the constitutional varietythat criterion is more than met here. To repeat Justice Stevens' cogent observation, it is "[o]bviou[s]" that "the Court's power to reverse Miranda's conviction rested <i>entirely</i> on the determination that a violation of the Federal Constitution had occurred." <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#367" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 367, n. 9</a></span> (dissenting opinion) (emphasis added). Despite the Court's Orwellian assertion to the contrary, it is undeniable that later cases (discussed <span class="star-pagination">*462</span> above) have "undermined [<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> `s] doctrinal underpinnings," <i>ante,</i> at 443, denying constitutional violation and thus stripping the holding of its only constitutionally legitimate support. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s critics and supporters alike have long made this point. See Office of Legal Policy, U. S. Dept. of Justice, Report to Attorney General on Law of Pre-Trial Interrogation 97 (Feb. 12, 1986) ("The current Court has repudiated the premises on which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was based, but has drawn back from recognizing the full implications of its decisions"); <i>id.,</i> at 78 ("<i>Michigan</i> v. <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span></i> accordingly repudiated the doctrinal basis of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision"); Sonenshein, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and the Burger Court: Trends and Countertrends, 13 Loyola U. Chi. L. J. 405, 407-408 (1982) ("Although the Burger Court has not overruled <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court has consistently undermined the rationales, assumptions, and values which gave <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> life"); <i>id.,</i> at 425-426 ("Seemingly, the Court [in <i>Michigan</i> v. <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span></i> ] utterly destroyed both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s rationale and its holding"); Stone, The Miranda Doctrine in the Burger Court, 1977 S. Ct. Rev. 99, 118 ("Mr. Justice Rehnquist's conclusion that there is a violation of the Self-Incrimination Clause only if a confession is involuntary . . . is an outright rejection of the core premises of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> ").</p>
<p>The Court cites <i>Patterson</i> v. <i>McLean Credit Union,</i> <span class="citation" data-id="9431745"><a href="/opinion/112296/patterson-v-mclean-credit-union/#173" aria-description="Citation for case: Patterson v. McLean Credit Union">491 U. S. 164, 173</a></span> (1989), as accurately reflecting our standard for overruling, see <i>ante,</i> at 443which I am pleased to accept, even though <i><span class="citation" data-id="9431745"><a href="/opinion/112296/patterson-v-mclean-credit-union/" aria-description="Citation for case: Patterson v. McLean Credit Union">Patterson</a></span></i> was speaking of overruling statutory cases and the standard for constitutional decisions is somewhat more lenient. What is set forth there reads as though it was written precisely with the current status of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in mind:</p>
<blockquote>"In cases where statutory precedents have been overruled, the primary reason for the Court's shift in position has been the intervening development of the law, through either the growth of judicial doctrine or further action taken by Congress. Where such changes have <span class="star-pagination">*463</span> removed or weakened the conceptual underpinnings from the prior decision, . . . or where the later law has rendered the decision irreconcilable with competing legal doctrines or policies, . . . the Court has not hesitated to overrule an earlier decision." <span class="citation" data-id="9431745"><a href="/opinion/112296/patterson-v-mclean-credit-union/#173" aria-description="Citation for case: Patterson v. McLean Credit Union">491 U. S., at 173</a></span>. Neither am I persuaded by the argument for retaining <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that touts its supposed workability as compared with the totality-of-the-circumstances test it purported to replace. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `s proponents cite <i>ad nauseam</i> the fact that the Court was called upon to make difficult and subtle distinctions in applying the "voluntariness" test in some 30-odd due process "coerced confessions" cases in the 30 years between <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), and <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> It is not immediately apparent, however, that the judicial burden has been eased by the "bright-line" rules adopted in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> In fact, in the 34 years since <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was decided, this Court has been called upon to decide nearly <i>60</i> cases involving a host of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> issues, most of them predicted with remarkable prescience by Justice White in his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> dissent. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#545" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 545</a></span>.</blockquote>
<p>Moreover, it is not clear why the Court thinks that the "totality-of-the-circumstances test . . . is more difficult than <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> for law enforcement officers to conform to, and for courts to apply in a consistent manner." <i>Ante,</i> at 444. Indeed, I find myself persuaded by Justice O'Connor's rejection of this same argument in her opinion in <i>Williams,</i>  <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#711" aria-description="Citation for case: Withrow v. Williams">507 U. S., at 711-712</a></span> (O'Connor, J., joined by Rehnquist, C. J., concurring in part and dissenting in part):</p>
<blockquote>"<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda,</i></a></span> for all its alleged brightness, is not without its difficulties; and voluntariness is not without its strengths. . . . ". . . <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> creates as many close questions as it resolves. The task of determining whether a defendant is in `custody' has proved to be `a slippery one.' And the supposedly `bright' lines that separate interrogation <span class="star-pagination">*464</span> from spontaneous declaration, the exercise of a right from waiver, and the adequate warning from the inadequate, likewise have turned out to be rather dim and ill defined. . . . "The totality-of-the-circumstances approach, on the other hand, permits each fact to be taken into account without resort to formal and dispositive labels. By dispensing with the difficulty of producing a yes-or-no answer to questions that are often better answered in shades and degrees, <i>the voluntariness inquiry often can</i>  <i>make judicial decisionmaking easier rather than more</i>  <i>onerous.</i> " (Emphasis added; citations omitted.) But even were I to agree that the old totality-of-thecircumstances test was more cumbersome, it is simply not true that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> has banished it from the law and replaced it with a new test. Under the current regime, which the Court today retains in its entirety, courts are frequently called upon to undertake <i>both</i> inquiries. That is because, as explained earlier, voluntariness remains the <i>constitutional</i>  standard, and as such continues to govern the admissibility for impeachment purposes of statements taken in violation of <i><span class="citation" data-id="9423233"><a h

[...TRUNCATED 19162 of 139162 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/District of Columbia v. R.W..json  (`lake-record`, 1 assertions)

### content_page

```
---
title: District of Columbia v. R.W.
type: case
citation: "No. 25-248, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 25-248
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
  opinion_url: "https://www.courtlistener.com/opinion/10845431/district-of-columbia-v-rw/"
  cluster_id: 10845431
  opinion_id: 11312795
  identity_checked: false
lake:
  record_id: District of Columbia v. R.W.
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Recent development
related:
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[Kansas v. Glover]]"
  - "[[Whren v. United States]]"
  - "[[Terry v. Ohio]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - terry-stop
  - reasonable-suspicion
  - totality-of-the-circumstances
  - supreme-court
holding: "Reasonable suspicion for an investigatory stop is measured against the totality of the circumstances, an inquiry that forbids evaluating and rejecting each supporting factor in isolation; because Officer Vanterpool confronted a pre-dawn suspicious-vehicle dispatch, two occupants who fled the car the instant he arrived, and a vehicle backing out with a door still open, he had reasonable suspicion to stop R.W., and the District of Columbia Court of Appeals' contrary decision was reversed."
aliases:
  - District of Columbia v. R.W.
  - "District of Columbia v. R.W. (2026)"
---

# District of Columbia v. R.W.

*No. 25-248, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10845431 → per curiam opinion 11312795 (608 U.S. ___, decided Apr. 20, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (current-Term slip opinion, no reporter star-pagination — S2 A3). S9 promotes. -->

## Background
Around 2:00 a.m. on a winter morning, District of Columbia Metropolitan Police Officer Clifford Vanterpool answered a radio dispatch directing him to check a suspicious vehicle at a specific apartment address. As he turned his marked cruiser into the parking lot, two people immediately fled the car "unprovoked," leaving at least one door open, and the driver — R.W., then a minor — began backing out of the space with the rear door still open. Vanterpool parked behind the car, ordered R.W. to raise his hands, and drew his weapon. Evidence found after the stop led to delinquency adjudications for unauthorized use of a vehicle and related offenses. The District of Columbia Court of Appeals held the stop violated the Fourth Amendment because, after "excising" the dispatch call and the companions' flight, the remaining facts did not amount to reasonable suspicion.

## Issue
Whether the facts available to Officer Vanterpool before he ordered R.W. to raise his hands supplied reasonable suspicion to justify the investigatory stop.

## Rule
Reasonable suspicion is assessed under the "totality of the circumstances," a standard that reviewing courts may not satisfy or defeat by isolating each factor; it "depends on the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act," and permits officers to draw "commonsense judgments and inferences about human behavior." Reaffirming *[[United States v. Arvizu|Arvizu]]*, the Court held that a reviewing court must look at the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] of each case — "an analysis that precludes the 'evaluation and rejection' of 'factors in isolation from each other.'" — slip op. at 2. ^pin-slip2

## Application
The District of Columbia Court of Appeals committed the very error the totality standard forbids: it "excised" the dispatch call and the two companions' unprovoked flight from the analysis, then found the residue — the late hour and the car's movement — insufficient. Taken together, however, the pre-dawn hour, a suspicious-vehicle report, occupants fleeing the moment a marked cruiser appeared, and a car backing out with a door hanging open gave Vanterpool a particularized and objective basis to suspect wrongdoing. The Court found the presence of reasonable suspicion clear on the combined facts.

## Conclusion
**Reversed.** [[Common Legal Terms#per-curiam|Per curiam]]. Because the court below departed from those principles and Officer Vanterpool clearly had reasonable suspicion to stop R.W., the Supreme Court summarily reversed the suppression ruling.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *R.W.* is a recent, error-correcting [[Common Legal Terms#per-curiam|per curiam]] reaffirming that the reasonable-suspicion inquiry is holistic — a rebuke of "divide-and-conquer" review that recurs whenever a lower court discounts individually innocent factors (compare *[[Kansas v. Glover]]* and the totality method of *[[Terry v. Ohio|Terry]]*).

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Recent development*

## Sources
- [*District of Columbia v. R.W.*, No. 25-248, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10845431/district-of-columbia-v-rw/) — pinpoint: slip op. at 2 (totality-of-the-circumstances rule; no divide-and-conquer). Rule quote string-matched to the CL opinion text 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "758e848d5e9c11f8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "District of Columbia v. R.W."}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "District of Columbia v. R.W.", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — District of Columbia v. R.W.

```json
{
  "schema_version": "s2.v1",
  "record_id": "District of Columbia v. R.W.",
  "status": "under_review",
  "identity": {
    "case_name": "District of Columbia v. R.W.",
    "case_name_short": "R.W.",
    "case_name_full": "",
    "input_case_name": "District of Columbia v. R.W.",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "25-248",
    "cluster_id": 10845431,
    "lead_opinion_id": 11312795,
    "sibling_ids": [],
    "absolute_url": "/opinion/10845431/district-of-columbia-v-rw/",
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
      "note": "SCOTUS per curiam No. 25-248, decided 2026-04-20 (608 U.S. ___; reasonable-suspicion vehicle stop). No S. Ct. page yet.",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/25-248",
          "cite": "No. 25-248, per curiam 2026-04-20"
        },
        {
          "source": "Justia",
          "url": "https://supreme.justia.com/cases/federal/us/608/25-248/",
          "cite": "608 U.S. ___ (2026) placeholder"
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
    "date_created": "2026-07-06T12:13:53Z",
    "date_modified": "2026-07-09T05:52:34Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:14:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:14:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "district-of-columbia-v-r-w--10845431",
      "to_record_id": "District of Columbia v. R.W.",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — District of Columbia v. R.W.

```
                   Cite as: 608 U. S. ____ (2026)              1

                             Per Curiam

SUPREME COURT OF THE UNITED STATES
            DISTRICT OF COLUMBIA v. R.W.
ON PETITION FOR WRIT OF CERTIORARI TO THE DISTRICT OF
             COLUMBIA COURT OF APPEALS
               No. 25–248.    Decided April 20, 2026

   PER CURIAM.
   In the wee hours of a winter morning in Washington,
D. C., District of Columbia Metropolitan Police Officer
Clifford Vanterpool received a radio dispatch call directing
him to check out a suspicious vehicle at a specific address.
Officer Vanterpool reached the apartment building at that
address around 2:00 a.m. As he turned his marked police
vehicle into the parking lot, he saw two people immediately
flee from a car, “unprovoked,” after “[p]olice had not done
anything other than simply pull up.” App. to Pet. for Cert.
48a. The runners left open at least one of the car doors.
The driver then began to back out of the parking space, rear
door still open. Officer Vanterpool decided to investigate.
He parked directly behind the car, left his own vehicle, or-
dered the driver, R. W., to put his hands up, and drew his
service weapon.
   R. W. raised a “single argument” on appeal—that Officer
Vanterpool lacked reasonable articulable suspicion suffi-
cient to justify the seizure. In re R.W., 334 A. 3d 593, 599
(D. C. 2025). The District of Columbia Court of Appeals
held that Officer Vanterpool, by stopping R. W. without rea-
sonable suspicion, violated the Fourth Amendment. We
disagree.
   When an officer makes a “brief investigatory stop[ ] of per-
sons or vehicles that fall[s] short of [a] traditional arrest,”
the Fourth Amendment “is satisfied if the officer’s action is
supported by reasonable suspicion to believe that criminal
activity ‘ “may be afoot.” ’ ” United States v. Arvizu, 534 U. S.
266, 273 (2002) (quoting United States v. Sokolow, 490 U. S.
2                 DISTRICT OF COLUMBIA v. R.W.

                              Per Curiam

1, 7 (1989)). In assessing whether an officer had reasonable
suspicion, a reviewing court must “look at the ‘totality of the
circumstances’ of each case”—an analysis that precludes
the “evaluation and rejection” of “factors in isolation from
each other.” Arvizu, 534 U. S., at 273–274. Because the
D. C. Court of Appeals departed from these principles—and
because Officer Vanterpool clearly had reasonable suspi-
cion to stop R. W.—we reverse.
                               I
   Largely based on evidence found after Officer Vanterpool
told R. W. to put his hands up, the District of Columbia
charged R. W. (a minor at the time) with unauthorized use
of a motor vehicle, felony receipt of stolen property, unlaw-
ful entry of a motor vehicle, and operating a vehicle in the
District of Columbia without a permit. Before trial, R. W.
moved to suppress the evidence obtained after he was
stopped. Following a suppression hearing, the trial court
denied R. W.’s motion, relying on four facts to conclude that
the officer had reasonable suspicion to stop R. W.: (1) the
officer had received a radio dispatch call regarding a suspi-
cious vehicle at a specified address, (2) the officer saw “ ‘two
persons fleeing from a vehicle’ ” upon his arrival, (3) “ ‘[i]t
was almost 2 a.m.,’ ” and (4) as the officer approached the
car, it began “ ‘backing out of the parking space . . . while
the rear driver’s side door [was] still open.’ ” 334 A. 3d, at
599. After a bench trial, the trial court adjudicated R. W.
delinquent on all counts and assigned R. W. to one year of
probation with conditions.
   On appeal, the D. C. Court of Appeals reversed the denial
of the motion to suppress and vacated the delinquency ad-
judication.* The court “first assess[ed] the legitimacy and
——————
  *The District of Columbia conceded that “Officer Vanterpool seized
R. W. when he first asked R. W. to put his hands up,” so the D. C. Court
of Appeals decided only “whether the facts then known by Officer
                      Cite as: 608 U. S. ____ (2026)                     3

                               Per Curiam

weight of each of the factors bearing on reasonable suspi-
cion” before “weigh[ing] that information all together.” Id.,
at 600 (internal quotation marks omitted). In the first step
of this analysis, it held that the trial court had erred by con-
sidering two factors: the radio dispatch call and the flight
of R. W.’s companions. It “excis[ed]” those factors from the
analysis. Id., at 597. It then concluded that, without more,
the remaining facts—the late hour and the car’s move-
ment—did not give rise to reasonable suspicion. After the
D. C. Court of Appeals ruled, the District of Columbia
sought certiorari.
                              II
   The question is whether the facts available to Officer
Vanterpool—before he ordered R. W. to put his hands up—
warranted the stop. In other words, we ask whether Officer
Vanterpool had a reasonable suspicion that R. W. was en-
gaged in criminal wrongdoing. Sokolow, 490 U. S., at 7–8.
Such reasonable suspicion arises when, based on the “ ‘to-
tality of the circumstances,’ ” the detaining officer had a
“ ‘particularized and objective basis’ ” for suspecting crimi-
nal wrongdoing. Arvizu, 534 U. S., at 273 (quoting United
States v. Cortez, 449 U. S. 411, 417 (1981)). Reasonable sus-
picion “ ‘depends on the factual and practical considerations
of everyday life on which reasonable and prudent men, not
legal technicians, act.’ ” Kansas v. Glover, 589 U. S. 376,
380 (2020) (quoting Prado Navarette v. California, 572 U. S.
393, 402 (2014)). It permits officers to make “ ‘commonsense
judgments and inferences about human behavior.’ ” Glover,
589 U. S., at 380–381 (quoting Illinois v. Wardlow, 528
U. S. 119, 125 (2000)).
   On the facts of this case, Officer Vanterpool clearly had
reasonable suspicion to stop R. W. Already on alert from
——————
Vanterpool created an objectively reasonable suspicion that criminal ac-
tivity was afoot.” 334 A. 3d, at 599 (citing Terry v. Ohio, 392 U. S. 1, 21
(1968)).
4               DISTRICT OF COLUMBIA v. R.W.

                          Per Curiam

the late-night dispatch call about a suspicious vehicle, the
officer observed every person in R. W.’s car respond
strangely to an approaching police car. Two people took off
running. We have observed that “unprovoked flight upon
noticing the police . . . . is certainly suggestive” of wrongdo-
ing. Id., at 124. The driver, R. W., did not run from the car,
but his companions’ flight cast his presence in a suspicious
light. After all, we have observed that “ ‘a car passenger . . .
will often be engaged in a common enterprise with the
driver, and have the same interest in concealing the fruits
or the evidence of their wrongdoing.’ ” Maryland v. Pringle,
540 U. S. 366, 373 (2003) (quoting Wyoming v. Houghton,
526 U. S. 295, 304–305 (1999)).
   We need not determine whether that connection alone
supported reasonable suspicion because R. W. was in the
driver’s seat and—after the passengers fled from the car—
began backing out of the parking space, ignoring the car’s
open back door. For most drivers, it would be a surprising
event for their back-seat passengers to exit the car and run
headlong away from them. But we doubt that most would
respond by putting their car into reverse and attempting to
drive away without at least checking whether the doors
were closed. R. W.’s own actions—combined with the pan-
icked flight of his companions—strongly suggested that he
was (like them) engaged in unlawful conduct he wished to
hide from police. See Sibron v. New York, 392 U. S. 40, 66
(1968) (recognizing that “deliberately furtive actions and
flight at the approach of . . . law officers are strong indicia
of mens rea”).
                              III
  The D. C. Court of Appeals reached a different conclusion
by “excis[ing]” the radio dispatch and the conduct of R. W.’s
companions from the analysis, and considering only “the
lateness of the hour and the slight movement of the car.”
334 A. 3d, at 597. The totality-of-the-circumstances test,
                 Cite as: 608 U. S. ____ (2026)            5

                          Per Curiam

however, “precludes this sort of divide-and-conquer analy-
sis.” Arvizu, 534 U. S., at 274. As our precedents have rec-
ognized, “the whole is often greater than the sum of its
parts—especially when the parts are viewed in isolation.”
District of Columbia v. Wesby, 583 U. S. 48, 60–61 (2018).
   Indeed, this case reveals the perils of reviewing facts
piecemeal and without context. Take the passengers’ flight
from the car. We have little doubt that, in some circum-
stances, an officer could not reasonably attribute his suspi-
cion of a fleeing individual to bystanders milling nearby.
Cf. Ybarra v. Illinois, 444 U. S. 85, 91 (1979) (recognizing
that “a person’s mere propinquity to others independently
suspected of criminal activity does not, without more, give
rise to probable cause to search that person”). But the
“whole picture” here tells a different story. Cortez, 449
U. S., at 417.
   After watching two people flee from a suspicious car, a
reasonable officer surely would question the driver’s next
move. Why would the driver hurriedly back up the car
without even closing a car door left open by his fleeing com-
panions? Perhaps one could imagine an innocent explana-
tion for such unusual behavior—the court below, for exam-
ple, surmised that R. W. “may not even have noticed that
his companions left the door open.” 334 A. 3d, at 605. “But
we have consistently recognized that reasonable suspicion
‘need not rule out the possibility of innocent conduct.’ ”
Navarette, 572 U. S., at 403 (quoting Arvizu, 534 U. S., at
277). Based on everything the officer observed on the night
in question, he drew the “commonsense inference” that all
three people in the car—including the driver—were trying
to hide wrongdoing from the police. Glover, 589 U. S., at
381.
   “[T]he Fourth Amendment requires . . . that a court ‘slosh
[its] way through’ a ‘factbound morass.’ ” Barnes v. Felix,
605 U. S. 73, 80 (2025) (quoting Scott v. Harris, 550 U. S.
372, 383 (2007)). There may be no “ ‘easy-to-apply legal
6               DISTRICT OF COLUMBIA v. R.W.

                           Per Curiam

test’ ” or “ ‘on/off switch’ ” in this context, Barnes, 605 U. S.,
at 80 (quoting Scott, 550 U. S., at 382–383), but one thing
is clear: “The ‘totality of the circumstances’ requires courts
to consider ‘the whole picture,’ ” Wesby, 583 U. S., at 60
(quoting Cortez, 449 U. S., at 417). The D. C. Court of Ap-
peals expressly declined to do that. 334 A. 3d, at 599. It
instead considered only the observations that “(1) it was
2:00 a.m. and (2) R. W. reversed a few feet in a parking spot
while the vehicle’s rear door was open.” Id., at 605. Ex-
pressly “excis[ed]” from its analysis was, for example, the
compelling fact that two individuals fled the vehicle as soon
as they spotted the police car. Pretending that the most
revealing aspect of the encounter did not happen is incom-
patible with the totality-of-the-circumstances approach re-
quired by our precedents.
                        *     *    *
  The petition for certiorari and R. W.’s motion to proceed
in forma pauperis are granted, the judgment of the District
of Columbia Court of Appeals is reversed, and the case is
remanded for further proceedings not inconsistent with this
opinion.
                                                It is so ordered.

  JUSTICE SOTOMAYOR would deny the petition for a writ of
certiorari.
                  Cite as: 608 U. S. ____ (2026)             1

                     JACKSON, J., dissenting

SUPREME COURT OF THE UNITED STATES
            DISTRICT OF COLUMBIA v. R.W.
ON PETITION FOR WRIT OF CERTIORARI TO THE DISTRICT OF
             COLUMBIA COURT OF APPEALS
               No. 25–248.   Decided April 20, 2026

   JUSTICE JACKSON, dissenting.
   The Fourth Amendment may require courts to “slosh . . .
through a factbound morass.” Ante, at 5 (internal quotation
marks omitted). It does not require readers of judicial opin-
ions to do the same. Any readable analysis will, of neces-
sity, tick through factors, finding some weighty, others less
so, and still others not at all, before piling them on a scale
and assessing the result. That is what the court below did
here, and it was right to do so. Announcing a conclusion
without providing reasoning along the way is not helpful to
the parties, the public, or the development of the law.
   To its credit, the Court applies a similar, factor-by-factor
approach here. That the Court’s analysis is comprehensible
shows as much. Like the court below, the per curiam takes
account of the facts in turn: a “late-night dispatch call about
a suspicious vehicle”; R. W.’s companions’ “unprovoked
flight”; R. W.’s shift into reverse with a car door still ajar.
Ante, at 4 (internal quotation marks omitted). And like the
court below, the per curiam explains how much weight it
assigns to each. Unprovoked flight, the Court says, is “cer-
tainly suggestive” of wrongdoing. Ibid. (internal quotation
marks omitted). “[C]ombined” with the flight, the Court
continues, R. W.’s abrupt reversal “strongly suggested”
wrongdoing. Ibid. This is how courts write opinions.
   So I am not sure why our Court sees fit to intervene in
this case, let alone to do so summarily. If the intervention
reflects a worry that the District of Columbia Court of Ap-
peals (DCCA) misunderstands the Fourth Amendment’s to-
tality-of-the-circumstances analysis, that worry seems
2               DISTRICT OF COLUMBIA v. R.W.

                      JACKSON, J., dissenting

unfounded. The DCCA has grasped the correct inquiry. Its
precedents rightly observe that “[t]he issue is not whether
any one factor individually justifies a stop, but rather
whether ‘collectively’ the totality of the circumstances sup-
ports a determination that the officers had reasonable sus-
picion for an investigatory stop.” Parker v. United States,
333 A. 3d 1162, 1175 (2025) (citing Mayo v. United States,
315 A. 3d 606, 637 (2024) (en banc)); see also, e.g., Maye v.
United States, 260 A. 3d 638, 647 (2021); Golden v. United
States, 248 A. 3d 925, 941 (2021).
   If today’s decision instead reflects dissatisfaction with the
DCCA’s comment that it “ ‘excis[ed]’ ” certain factors from
its analysis, ante, at 4–5, I do not contest that this was poor
word choice, see United States v. Arvizu, 534 U. S. 266, 274
(2002) (rejecting a “divide-and-conquer analysis”). But I do
not think that word choice reflects a methodological error.
Courts excise facts from their analyses every day. Opinion-
writing is an exercise in culling the irrelevant; in applica-
tion, no “totality-of-the-circumstances” test really lives up
to its name. Indeed, today’s per curiam necessarily omits a
number of facts the Court finds insignificant—e.g., the
make and model of the car, the precise location of the stop,
the color of R. W.’s friends’ clothing. Though it does not say
so, the Court “excises” those facts, too. It does not thereby
misapply the Fourth Amendment.
   If, finally, the Court’s decision to intervene reflects disap-
proval of the DCCA’s assessment of which particular facts
to weigh and to what extent, I cannot fathom why that kind
of factbound determination warranted correction by this
Court. The DCCA assigned no weight to two facts—the dis-
patch call and the unprovoked flight. The Court does not
seem to take issue with the first. For good reason: The
DCCA reasonably applied our decisions explaining that an
officer may not obtain reasonable suspicion by relying on
the unsupported hunch of a fellow officer. See Whiteley v.
Warden, Wyo. State Penitentiary, 401 U. S. 560, 568 (1971);
                 Cite as: 608 U. S. ____ (2026)           3

                    JACKSON, J., dissenting

United States v. Hensley, 469 U. S. 221, 232 (1985). The
Court may be right that the second—the unprovoked
flight—should have borne some rather than no weight. But
if this context-specific adjustment is all the per curiam
seeks to achieve, it does not merit the use of our summary
discretion.
   Even if I would have assigned more heft to a particular
fact in my own first-instance assessment, I would not word-
smith a lower court in this fashion. In my view, this is not
a worthy accomplishment for the unusual step of summary
reversal. Therefore, I respectfully dissent.

```

---
