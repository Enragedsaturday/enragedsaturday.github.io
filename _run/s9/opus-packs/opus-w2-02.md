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

## GROUP: _overhaul2/lake/cases/Brigham City v. Stuart.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Brigham City v. Stuart"
type: case
citation: "547 U.S. 398 (2006)"
parallel_cite: "126 S. Ct. 1943; 164 L. Ed. 2d 650"
neutral_cite: 2006 U.S. LEXIS 4155
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-05-22
docket: 05-502
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-05-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brigham City v. Stuart
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145654/brigham-city-v-stuart/"
  cluster_id: 145654
  opinion_id: 145654
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Anchor"
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Fisher]]", "[[Mincey v. Arizona]]", "[[Caniglia v. Strom]]"]
aliases: []
tags: ["case", "fourth-amendment", "emergency-aid", "exigent-circumstances", "warrantless-entry"]
holding: "Emergency aid exception: police may enter a home without a warrant when they have an objectively reasonable basis to believe an occupant…"
lake:
  record_id: Brigham City v. Stuart
  status: verified
  projected_at: 2026-07-06
---

# Brigham City v. Stuart

*547 U.S. 398 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At about 3 a.m. officers responded to a loud-party call. From the yard they saw, through a screen door and windows, an altercation in the kitchen in which a juvenile broke free and punched an adult hard enough to draw blood. An officer announced his presence and entered to stop the fight; the occupants were charged with offenses including disorderly conduct and intoxication.

## Issue
Whether police may make a warrantless entry into a home under the emergency-aid exception even if their subjective motivation may have been to make arrests.

## Rule
Police "may enter a home without a warrant when they have an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened with such injury." — 547 U.S. at 400. ^pin-400

The standard is purely objective: "An action is 'reasonable' under the Fourth Amendment, regardless of the individual officer's state of mind, 'as long as the circumstances, viewed objectively, justify [the] action.' . . . The officer's subjective motivation is irrelevant." — *Id.* at 404. ^pin-404

## Application
The officers watched a juvenile strike an adult in the kitchen, an ongoing assault that supplied an objectively reasonable basis to believe an occupant was injured or about to be. Because the test is objective, any arrest motive did not defeat the entry; the warrantless entry and the officer's announcement were reasonable on these facts.

## Conclusion
The warrantless entry was reasonable; the Utah Supreme Court's suppression was reversed, and subjective intent is irrelevant to an objectively justified emergency-aid entry.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Followed by** [[Michigan v. Fisher]] (per curiam) — objective basis judged at the moment of entry; no ironclad proof of injury required.
- [[Caniglia v. Strom]] (no *freestanding* community-caretaking entry into a home) leaves *Brigham City*'s emergency-aid rule undisturbed.

## Appears on
- [[Emergency Aid]] — *Key — Anchor*
- [[Exigent Circumstances and Hot Pursuit]] — *Related (cross-doctrine)*

## Sources
- *Brigham City v. Stuart*, 547 U.S. 398 (2006) — https://www.courtlistener.com/opinion/145654/brigham-city-v-stuart/ — pinpoints: 400, 404.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b2011975b1fc0656", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brigham City v. Stuart"}, "payload": {"all": [{"cite": "547 U.S. 398", "page": "398", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "547"}, {"cite": "126 S. Ct. 1943", "page": "1943", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "126"}, {"cite": "164 L. Ed. 2d 650", "page": "650", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "164"}, {"cite": "2006 U.S. LEXIS 4155", "page": "4155", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2006"}], "display": "547 U.S. 398", "official": {"cite": "547 U.S. 398", "page": "398", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "547"}, "official_selection_present": true, "record_id": "Brigham City v. Stuart"}}
{"assertion_id": "9f814fda7fa33a44", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-400", "record_id": "Brigham City v. Stuart"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-400", "pinpoint_status": "slip-only", "quote": "--- # Brigham City v. Stuart *547 U.S. 398 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At about 3 a.m. officers responded to a loud-party call. From the yard they saw, through a screen door and windows, an altercation in the kitchen in which a juvenile broke free and punched an adult hard enough to draw blood. An officer announced his presence and entered to stop the fight; the occupants were charged with offenses including disorderly conduct and intoxication. ## Issue Whether police may make a warrantless entry into a home under the emergency-aid exception even if their subjective motivation may have been to make arrests. ## Rule Police", "quote_fidelity": "mismatch", "record_id": "Brigham City v. Stuart", "star_marker": null}}
{"assertion_id": "a608fc0595312b27", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-404", "record_id": "Brigham City v. Stuart"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-404", "pinpoint_status": "slip-only", "quote": "An action is 'reasonable' under the Fourth Amendment, regardless of the individual officer's state of mind, 'as long as the circumstances, viewed objectively, justify [the] action.' . . . The officer's subjective motivation is irrelevant.", "quote_fidelity": "mismatch", "record_id": "Brigham City v. Stuart", "star_marker": null}}
{"assertion_id": "2c4be1373a3ace6d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brigham City v. Stuart"}, "payload": {"as_of_content": "2006-05-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brigham City v. Stuart", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Brigham City v. Stuart

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brigham City v. Stuart",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brigham City v. Stuart",
    "case_name_short": "Stuart",
    "case_name_full": "BRIGHAM CITY, UTAH v. STUART Et Al.",
    "input_case_name": "Brigham City v. Stuart",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-05-22",
    "year": 2006,
    "docket": "05-502",
    "cluster_id": 145654,
    "lead_opinion_id": 145654,
    "sibling_ids": [
      145654,
      9434949,
      9434950
    ],
    "absolute_url": "/opinion/145654/brigham-city-v-stuart/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9256378,
        "score": 10,
        "case_name": "Brigham City v. Stuart"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 398",
      "volume": "547",
      "reporter": "U.S.",
      "page": "398",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 1943",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1943",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 650",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "650",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 4155",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4155",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 398",
        "volume": "547",
        "reporter": "U.S.",
        "page": "398",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 1943",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1943",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 650",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "650",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 4155",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4155",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 398",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 398",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-400",
      "page": null,
      "quote": "--- # Brigham City v. Stuart *547 U.S. 398 (2006)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At about 3 a.m. officers responded to a loud-party call. From the yard they saw, through a screen door and windows, an altercation in the kitchen in which a juvenile broke free and punched an adult hard enough to draw blood. An officer announced his presence and entered to stop the fight; the occupants were charged with offenses including disorderly conduct and intoxication. ## Issue Whether police may make a warrantless entry into a home under the emergency-aid exception even if their subjective motivation may have been to make arrests. ## Rule Police",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-404",
      "page": null,
      "quote": "An action is 'reasonable' under the Fourth Amendment, regardless of the individual officer's state of mind, 'as long as the circumstances, viewed objectively, justify [the] action.' . . . The officer's subjective motivation is irrelevant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-05-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brigham City v. Stuart",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Mickel",
          "cluster_id": 10680424,
          "cite": [
            "321 Ga. 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane1_negative"
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
        "journal_ref": "Brigham City v. Stuart:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Heller",
          "cluster_id": 145777,
          "cite": [
            "171 L. Ed. 2d 637",
            "128 S. Ct. 2783",
            "554 U.S. 570",
            "2008 U.S. LEXIS 5268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ziglar v. Abbasi",
          "cluster_id": 4403804,
          "cite": [
            "582 U.S. 120",
            "2017 U.S. LEXIS 3874",
            "137 S. Ct. 1843",
            "198 L. Ed. 2d 290",
            "26 Fla. L. Weekly Fed. S 655",
            "85 U.S.L.W. 4360",
            "2017 WL 2621317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
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
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
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
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
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
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
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
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City and County of San Francisco v. Sheehan",
          "cluster_id": 2801435,
          "cite": [
            "575 U.S. 600",
            "135 S. Ct. 1765",
            "191 L. Ed. 2d 856",
            "2015 U.S. LEXIS 3200",
            "83 U.S.L.W. 4303",
            "25 Fla. L. Weekly Fed. S 254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
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
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
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
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jose Chavez v. James Ziglar",
          "cluster_id": 802689,
          "cite": [
            "683 F.3d 1102",
            "2012 WL 2334124",
            "2012 U.S. App. LEXIS 12555"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Fisher",
          "cluster_id": 1755,
          "cite": [
            "175 L. Ed. 2d 410",
            "130 S. Ct. 546",
            "558 U.S. 45",
            "2009 U.S. LEXIS 8773"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
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
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nunez v. Duncan",
          "cluster_id": 1463726,
          "cite": [
            "591 F.3d 1217",
            "2010 U.S. App. LEXIS 517",
            "2010 WL 60089"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Thompson",
          "cluster_id": 4858089,
          "cite": [
            "2021 CO 15"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jasper Black",
          "cluster_id": 797418,
          "cite": [
            "482 F.3d 1035",
            "2007 U.S. App. LEXIS 8182"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of L. A. v. Patel",
          "cluster_id": 2811846,
          "cite": [
            "576 U.S. 409",
            "135 S. Ct. 2443",
            "192 L. Ed. 2d 435",
            "2015 U.S. LEXIS 4065",
            "83 U.S.L.W. 4520",
            "25 Fla. L. Weekly Fed. S 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brigham City v. Stuart:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145654 OR 9434949 OR 9434950) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjEzNDMzNjAwMDAwJnM9NDg1NjYzMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145654+OR+9434949+OR+9434950%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145654 OR 9434949 OR 9434950)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjcmcz01NjQyMjg3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145654+OR+9434949+OR+9434950%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145654 OR 9434949 OR 9434950)",
        "reviewed": 134,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 134,
        "triage_read": 2,
        "triage_snippet_classified": 132
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145654 OR 9434949 OR 9434950)",
    "indexed_citing_opinions": 1122,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145654,
        "count": 857,
        "count_source": "search"
      },
      {
        "opinion_id": 9434949,
        "count": 290,
        "count_source": "search"
      },
      {
        "opinion_id": 9434950,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2239,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brigham-city-v-stuart.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MTU2Njgmcz0xMDY2MzEyOCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145654+OR+9434949+OR+9434950%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145654,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 184651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 260805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 769576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 1316088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 1854815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 2310659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 2576420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145654,
        "cited_id": 2602480,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T20:31:27Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:31:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:31:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:35:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:31:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brigham City v. Stuart

```
(Slip Opinion)              OCTOBER TERM, 2005                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

            BRIGHAM CITY, UTAH v. STUART ET AL.

           CERTIORARI TO THE SUPREME COURT OF UTAH

       No. 05–502.      Argued April 24, 2006—Decided May 22, 2006
Responding to a 3 a.m. call about a loud party, police arrived at the
  house in question, heard shouting inside, proceeded down the drive
  way, and saw two juveniles drinking beer in the backyard. Entering
  the yard, they saw through a screen door and windows an altercation
  in the kitchen between four adults and a juvenile, who punched one
  of the adults, causing him to spit blood in a sink. An officer opened
  the screen door and announced the officers’ presence. Unnoticed
  amid the tumult, the officer entered the kitchen and again cried out,
  whereupon the altercation gradually subsided. The officers arrested
  respondents and charged them with contributing to the delinquency
  of a minor and related offenses. The trial court granted their motion
  to suppress all evidence obtained after the officers entered the home
  on the ground that the warrantless entry violated the Fourth
  Amendment, and the Utah Court of Appeals affirmed. Affirming, the
  State Supreme Court held that the injury caused by the juvenile’s
  punch was insufficient to trigger the “emergency aid doctrine” be
  cause it did not give rise to an objectively reasonable belief that an
  unconscious, semiconscious, or missing person feared injured or dead
  was in the home. Furthermore, the court suggested the doctrine was
  inapplicable because the officers had not sought to assist the injured
  adult but had acted exclusively in a law enforcement capacity. The
  court also held that the entry did not fall within the exigent circum
  stances exception to the warrant requirement.
Held: Police may enter a home without a warrant when they have an
 objectively reasonable basis for believing that an occupant is seri
 ously injured or imminently threatened with such injury.
    Because the Fourth Amendment’s ultimate touchstone is “reason
  ableness,” the warrant requirement is subject to certain exceptions.
  For example, one exigency obviating the requirement is the need to
2                      BRIGHAM CITY v. STUART

                                  Syllabus

    render emergency assistance to occupants of private property who are
    seriously injured or threatened with such injury. Mincey v. Arizona,
    437 U. S. 385, 392. This Court has repeatedly rejected respondents’
    contention that, in assessing the reasonableness of an entry, consid
    eration should be given to the subjective motivations of individual of
    ficers. Because the officers’ subjective motivation is irrelevant, Bond
    v. United States, 529 U. S. 334, 338, n. 2, it does not matter here
    whether they entered the kitchen to arrest respondents and gather
    evidence or to assist the injured and prevent further violence. Indi
    anapolis v. Edmond, 531 U. S. 32, 46, and Florida v. Wells, 495 U. S.
    1, 4, distinguished. Relying on this Court’s holding in Welsh v. Wis
    consin, 466 U. S. 740, 753, that “an important factor to be considered
    when determining whether any exigency exists is the gravity of the
    underlying offense for which the arrest is being made,” respondents
    further contend that their conduct was not serious enough to justify
    the officers’ intrusion into the home. This contention is misplaced.
    In Welsh, the “only potential emergency” confronting the officers was
    the need to preserve evidence of the suspect’s blood-alcohol level, an
    exigency the Court held insufficient under the circumstances to jus
    tify a warrantless entry into the suspect’s home. Ibid. Here, the offi
    cers were confronted with ongoing violence occurring within the
    home, a situation Welsh did not address.
       The officers’ entry here was plainly reasonable under the circum
    stances. Given the tumult at the house when they arrived, it was ob
    vious that knocking on the front door would have been futile. More
    over, in light of the fracas they observed in the kitchen, the officers
    had an objectively reasonable basis for believing both that the injured
    adult might need help and that the violence was just beginning.
    Nothing in the Fourth Amendment required them to wait until an
    other blow rendered someone unconscious, semiconscious, or worse
    before entering. The manner of their entry was also reasonable, since
    nobody heard the first announcement of their presence, and it was
    only after the announcing officer stepped into the kitchen and an
    nounced himself again that the tumult subsided. That announce
    ment was at least equivalent to a knock on the screen door and, un
    der the circumstances, there was no violation of the Fourth
    Amendment’s knock-and-announce rule. Furthermore, once the an
    nouncement was made, the officers were free to enter; it would serve
    no purpose to make them stand dumbly at the door awaiting a re
    sponse while those within brawled on, oblivious to their presence.
    Pp. 3–7.
2005 UT 13, 122 P. 3d 506, reversed and remanded.
    ROBERTS, C. J., delivered the opinion for a unanimous Court. STE
VENS, J.,filed a concurring opinion.
                        Cite as: 547 U. S. ____ (2006)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 05–502
                                   _________________


BRIGHAM CITY, UTAH, PETITIONER v. CHARLES W.
               STUART ET AL.
 ON WRIT OF CERTIORARI TO THE SUPREME COURT OF UTAH
                                 [May 22, 2006]

  CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
  In this case we consider whether police may enter a
home without a warrant when they have an objectively
reasonable basis for believing that an occupant is seriously
injured or imminently threatened with such injury. We
conclude that they may.
                              I
  This case arises out of a melee that occurred in a Brig-
ham City, Utah, home in the early morning hours of July
23, 2000. At about 3 a.m., four police officers responded to
a call regarding a loud party at a residence. Upon arriving
at the house, they heard shouting from inside, and pro
ceeded down the driveway to investigate. There, they
observed two juveniles drinking beer in the backyard.
They entered the backyard, and saw—through a screen
door and windows—an altercation taking place in the
kitchen of the home. According to the testimony of one of
the officers, four adults were attempting, with some diffi
culty, to restrain a juvenile. The juvenile eventually
“broke free, swung a fist and struck one of the adults in
the face.” 2005 UT 13, ¶2, 122 P. 3d 506, 508. The officer
2                 BRIGHAM CITY v. STUART

                     Opinion of the Court

testified that he observed the victim of the blow spitting
blood into a nearby sink. App. 40. The other adults con
tinued to try to restrain the juvenile, pressing him up
against a refrigerator with such force that the refrigerator
began moving across the floor. At this point, an officer
opened the screen door and announced the officers’ pres
ence. Amid the tumult, nobody noticed. The officer en
tered the kitchen and again cried out, and as the occu
pants slowly became aware that the police were on the
scene, the altercation ceased.
   The officers subsequently arrested respondents and
charged them with contributing to the delinquency of a
minor, disorderly conduct, and intoxication. In the trial
court, respondents filed a motion to suppress all evidence
obtained after the officers entered the home, arguing that
the warrantless entry violated the Fourth Amendment.
The court granted the motion, and the Utah Court of
Appeals affirmed.
   Before the Supreme Court of Utah, Brigham City ar
gued that although the officers lacked a warrant, their
entry was nevertheless reasonable on either of two
grounds. The court rejected both contentions and, over
two dissenters, affirmed. First, the court held that the
injury caused by the juvenile’s punch was insufficient to
trigger the so-called “emergency aid doctrine” because it
did not give rise to an “ objectively reasonable belief that
an unconscious, semi-conscious, or missing person feared
injured or dead [was] in the home.” 122 P. 3d, at 513
(internal quotation marks omitted). Furthermore, the
court suggested that the doctrine was inapplicable because
the officers had not sought to assist the injured adult, but
instead had acted “exclusively in their law enforcement
capacity.” Ibid.
   The court also held that the entry did not fall within the
exigent circumstances exception to the warrant require
ment. This exception applies, the court explained, where
                 Cite as: 547 U. S. ____ (2006)            3

                     Opinion of the Court

police have probable cause and where “a reasonable per
son [would] believe that the entry was necessary to pre
vent physical harm to the officers or other persons.” Id.,
at 514 (internal quotation marks omitted). Under this
standard, the court stated, the potential harm need not be
as serious as that required to invoke the emergency aid
exception. Although it found the case “a close and difficult
call,” the court nevertheless concluded that the officers’
entry was not justified by exigent circumstances. Id., at
515.
   We granted certiorari, 546 U. S. ___ (2006), in light of
differences among state courts and the Courts of Appeals
concerning the appropriate Fourth Amendment standard
governing warrantless entry by law enforcement in an
emergency situation. Compare In re Sealed Case 96–3167,
153 F. 3d 759, 766 (CADC 1998) (“[T]he standard for
exigent circumstances is an objective one”) and People v.
Hebert, 46 P. 3d 473, 480 (Colo. 2002) (en banc) (consider
ing the circumstances as they “would have been objec
tively examined by a prudent and trained police officer”),
with United States v. Cervantes, 219 F. 3d 882, 890 (CA9
2000) (“[U]nder the emergency doctrine, ‘[a] search must
not be primarily motivated by intent to arrest and seize
evidence’ ” (quoting People v. Mitchell, 39 N. Y. 2d 173,
177, 347 N. E. 2d 607, 609 (1976)) and State v. Mountford,
171 Vt. 487, 492, 769 A. 2d 639, 645 (2000) (Mitchell test
“requir[es] courts to find that the primary subjective moti
vation behind such searches was to provide emergency
aid”).
                                II
  It is a “ ‘ basic principle of Fourth Amendment law that
searches and seizures inside a home without a warrant
are presumptively unreasonable.’ ” Groh v. Ramirez, 540
U. S. 551, 559 (2004) (quoting Payton v. New York, 445 U. S.
573, 586 (1980) (some internal quotation marks omitted)).
4                 BRIGHAM CITY v. STUART

                      Opinion of the Court

Nevertheless, because the ultimate touchstone of the
Fourth Amendment is “reasonableness,” the warrant
requirement is subject to certain exceptions. Flippo v.
West Virginia, 528 U. S. 11, 13 (1999) (per curiam); Katz v.
United States, 389 U. S. 347, 357 (1967). We have held, for
example, that law enforcement officers may make a war
rantless entry onto private property to fight a fire and
investigate its cause, Michigan v. Tyler, 436 U. S. 499, 509
(1978), to prevent the imminent destruction of evidence,
Ker v. California, 374 U. S. 23, 40 (1963), or to engage in
“hot pursuit” of a fleeing suspect, United States v. Santana,
427 U. S. 38, 42–43 (1976). “[W]arrants are generally re
quired to search a person’s home or his person unless ‘the
exigencies of the situation’ make the needs of law enforce
ment so compelling that the warrantless search is objec
tively reasonable under the Fourth Amendment.” Mincey v.
Arizona, 437 U. S. 385, 393–394 (1978).
   One exigency obviating the requirement of a warrant is
the need to assist persons who are seriously injured or
threatened with such injury. “ ‘The need to protect or
preserve life or avoid serious injury is justification for
what would be otherwise illegal absent an exigency or
emergency.’ ” Id., at 392 (quoting Wayne v. United States,
318 F. 2d 205, 212 (CADC 1963) (Burger, J.)); see also
Tyler, supra, at 509. Accordingly, law enforcement officers
may enter a home without a warrant to render emergency
assistance to an injured occupant or to protect an occupant
from imminent injury. Mincey, supra, at 392; see also
Georgia v. Randolph, 547 U. S. ___, ___ (2006) (slip op., at
13–14) (“[I]t would be silly to suggest that the police would
commit a tort by entering . . . to determine whether vio
lence (or threat of violence) has just occurred or is about to
(or soon will) occur”).
   Respondents do not take issue with these principles, but
instead advance two reasons why the officers’ entry here
was unreasonable. First, they argue that the officers were
                  Cite as: 547 U. S. ____ (2006)            5

                      Opinion of the Court

more interested in making arrests than quelling violence.
They urge us to consider, in assessing the reasonableness
of the entry, whether the officers were “indeed motivated
primarily by a desire to save lives and property.” Brief for
Respondents 3; see also Brief for National Association of
Criminal Defense Lawyers as Amicus Curiae 6 (entry to
render emergency assistance justifies a search “only when
the searching officer is acting outside his traditional law-
enforcement capacity”). The Utah Supreme Court also
considered the officers’ subjective motivations relevant.
See 122 P. 3d, at 513 (search under the “emergency aid
doctrine” may not be “primarily motivated by intent to
arrest and seize evidence” (internal quotation marks
omitted)).
   Our cases have repeatedly rejected this approach. An
action is “reasonable” under the Fourth Amendment,
regardless of the individual officer’s state of mind, “as long
as the circumstances, viewed objectively, justify [the]
action.” Scott v. United States, 436 U. S. 128, 138 (1978)
(emphasis added). The officer’s subjective motivation is
irrelevant. See Bond v. United States, 529 U. S. 334, 338,
n. 2 (2000) (“The parties properly agree that the subjective
intent of the law enforcement officer is irrelevant in deter
mining whether that officer’s actions violate the Fourth
Amendment . . . ; the issue is not his state of mind, but the
objective effect of his actions”); Whren v. United States, 517
U. S. 806, 813 (1996) (“[W]e have been unwilling to enter
tain Fourth Amendment challenges based on the actual
motivations of individual officers”); Graham v. Connor, 490
U. S. 386, 397 (1989) (“[O]ur prior cases make clear” that
“the subjective motivations of the individual officers . . .
ha[ve] no bearing on whether a particular seizure is ‘unrea
sonable’ under the Fourth Amendment”). It therefore does
not matter here—even if their subjective motives could be
so neatly unraveled—whether the officers entered the
kitchen to arrest respondents and gather evidence against
6                BRIGHAM CITY v. STUART

                     Opinion of the Court

them or to assist the injured and prevent further violence.
   As respondents note, we have held in the context of
programmatic searches conducted without individualized
suspicion—such as checkpoints to combat drunk driving or
drug trafficking—that “an inquiry into programmatic
purpose” is sometimes appropriate. Indianapolis v. Ed
mond, 531 U. S. 32, 46 (2000) (emphasis added); see also
Florida v. Wells, 495 U. S. 1, 4 (1990) (an inventory search
must be regulated by “standardized criteria” or “established
routine” so as not to “be a ruse for a general rummaging in
order to discover incriminating evidence”). But this inquiry
is directed at ensuring that the purpose behind the pro
gram is not “ultimately indistinguishable from the general
interest in crime control.” Edmond, 531 U. S., at 44. It
has nothing to do with discerning what is in the mind of
the individual officer conducting the search. Id., at 48.
   Respondents further contend that their conduct was not
serious enough to justify the officers’ intrusion into the
home. They rely on Welsh v. Wisconsin, 466 U. S. 740, 753
(1984), in which we held that “an important factor to be
considered when determining whether any exigency exists
is the gravity of the underlying offense for which the
arrest is being made.” This contention, too, is misplaced.
Welsh involved a warrantless entry by officers to arrest a
suspect for driving while intoxicated. There, the “only
potential emergency” confronting the officers was the need
to preserve evidence (i.e., the suspect’s blood-alcohol
level)—an exigency that we held insufficient under the
circumstances to justify entry into the suspect’s home.
Ibid. Here, the officers were confronted with ongoing
violence occurring within the home. Welsh did not address
such a situation.
   We think the officers’ entry here was plainly reasonable
under the circumstances. The officers were responding, at
3 o’clock in the morning, to complaints about a loud party.
As they approached the house, they could hear from
                 Cite as: 547 U. S. ____ (2006)            7

                     Opinion of the Court

within “an altercation occurring, some kind of a fight.”
App. 29. “It was loud and it was tumultuous.” Id., at 33.
The officers heard “thumping and crashing” and people
yelling “stop, stop” and “get off me.” Id., at 28, 29. As the
trial court found, “it was obvious that . . . knocking on the
front door” would have been futile. Id., at 92. The noise
seemed to be coming from the back of the house; after
looking in the front window and seeing nothing, the offi
cers proceeded around back to investigate further. They
found two juveniles drinking beer in the backyard. From
there, they could see that a fracas was taking place inside
the kitchen. A juvenile, fists clenched, was being held
back by several adults. As the officers watch, he breaks
free and strikes one of the adults in the face, sending the
adult to the sink spitting blood.
   In these circumstances, the officers had an objectively
reasonable basis for believing both that the injured adult
might need help and that the violence in the kitchen was
just beginning. Nothing in the Fourth Amendment re
quired them to wait until another blow rendered someone
“unconscious” or “semi-conscious” or worse before enter
ing. The role of a peace officer includes preventing vio
lence and restoring order, not simply rendering first aid to
casualties; an officer is not like a boxing (or hockey) refe
ree, poised to stop a bout only if it becomes too one-sided.
   The manner of the officers’ entry was also reasonable.
After witnessing the punch, one of the officers opened the
screen door and “yelled in police.” Id., at 40. When no
body heard him, he stepped into the kitchen and an
nounced himself again. Only then did the tumult subside.
The officer’s announcement of his presence was at least
equivalent to a knock on the screen door. Indeed, it was
probably the only option that had even a chance of rising
above the din. Under these circumstances, there was no
violation of the Fourth Amendment’s knock-and-announce
rule. Furthermore, once the announcement was made, the
8                BRIGHAM CITY v. STUART

                     Opinion of the Court

officers were free to enter; it would serve no purpose to
require them to stand dumbly at the door awaiting a
response while those within brawled on, oblivious to their
presence.
  Accordingly, we reverse the judgment of the Supreme
Court of Utah, and remand the case for further proceed
ings not inconsistent with this opinion.
                                           It is so ordered.
                 Cite as: 547 U. S. ____ (2006)            1

                    STEVENS, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 05–502
                         _________________


BRIGHAM CITY, UTAH, PETITIONER v. CHARLES W.
               STUART ET AL.
 ON WRIT OF CERTIORARI TO THE SUPREME COURT OF UTAH
                        [May 22, 2006]

   JUSTICE STEVENS, concurring.
   This is an odd flyspeck of a case. The charges that have
been pending against respondents for the past six years
are minor offenses—intoxication, contributing to the de
linquency of a minor, and disorderly conduct—two of
which could have been proved by evidence that was gath
ered by the responding officers before they entered the
home. The maximum punishment for these crimes ranges
between 90 days and 6 months in jail. And the Court’s
unanimous opinion restating well-settled rules of federal
law is so clearly persuasive that it is hard to imagine the
outcome was ever in doubt.
   Under these circumstances, the only difficult question is
which of the following is the most peculiar: (1) that the
Utah trial judge, the intermediate state appellate court,
and the Utah Supreme Court all found a Fourth Amend
ment violation on these facts; (2) that the prosecution
chose to pursue this matter all the way to the United
States Supreme Court; or (3) that this Court voted to
grant the petition for a writ of certiorari.
   A possible explanation for the first is that the suppres
sion ruling was correct as a matter of Utah law, and nei
ther trial counsel nor the trial judge bothered to identify
the Utah Constitution as an independent basis for the
decision because they did not expect the prosecution to
2                    BRIGHAM CITY v. STUART

                        STEVENS, J., concurring

appeal.* The most plausible explanation for the latter two
decisions is that they were made so police officers in Utah
may enter a home without a warrant when they see ongo
ing violence—we are, of course, reversing the Utah Su
preme Court’s conclusion to the contrary. But that pur
pose, laudable though it may be, cannot be achieved in
this case. Our holding today addresses only the limita
tions placed by the Federal Constitution on the search at
issue; we have no authority to decide whether the police in
this case violated the Utah Constitution.
   The Utah Supreme Court, however, has made clear that
the Utah Constitution provides greater protection to the
privacy of the home than does the Fourth Amendment.
See State v. Debooy, 2000 UT 32, ¶12, 996 P. 2d 546, 549.
And it complained in this case of respondents’ failure to
raise or adequately brief a state constitutional challenge,
thus preventing the state courts from deciding the case on
anything other than Fourth Amendment grounds. See
2005 UT 13, ¶12, 122 P. 3d 506, 510. “[S]urpris[ed]” by
“[t]he reluctance of litigants to take up and develop a state
constitutional analysis,” ibid., the court expressly invited
future litigants to bring challenges under the Utah Consti
tution to enable it to fulfill its “responsibility as guardians
of the individual liberty of our citizens” and “undertak[e] a
principled exploration of the interplay between federal and
state protections of individual rights,” id., at 511. The fact
that this admonishment and request came from the Utah
Supreme Court in this very case not only demonstrates
that the prosecution selected the wrong case for establish
ing the rule it wants, but indicates that the Utah Supreme
Court would probably adopt the same rule as a matter of
state constitutional law that we reject today under the
——————
  * Indeed, it was the prosecution that prepared the trial court’s order
granting respondents’ motion to suppress. See 2002 UT App. 317, ¶4,
57 P. 3d 1111, 1112.
                 Cite as: 547 U. S. ____ (2006)            3

                    STEVENS, J., concurring

Federal Constitution.
   Whether or not that forecast is accurate, I can see no
reason for this Court to cause the Utah courts to redecide
the question as a matter of state law. Federal interests
are not offended when a single State elects to provide
greater protection for its citizens than the Federal Consti
tution requires. Indeed, I continue to believe “that a policy
of judicial restraint—one that allows other decisional
bodies to have the last word in legal interpretation until it
is truly necessary for this Court to intervene—enables this
Court to make its most effective contribution to our federal
system of government.” Michigan v. Long, 463 U. S. 1032,
1067 (1983) (STEVENS, J., dissenting). Thus, while I join the
Court’s opinion, I remain persuaded that my vote to deny
the State’s petition for certiorari was correct.

```

---

## GROUP: _overhaul2/lake/cases/Brinegar v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Brinegar v. United States"
type: case
citation: "338 U.S. 160 (1949)"
parallel_cite: "69 S. Ct. 1302; 93 L. Ed. 2d 1879"
neutral_cite: 1949 U.S. LEXIS 2084
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1949
date_decided: 1949-10-10
docket: 23
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1949-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brinegar v. United States
  varies_by_point: false
  scope_note: "Classic probable-cause standard; bedrock and good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/104716/brinegar-v-united-states/"
  cluster_id: 104716
  opinion_id: 104716
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Anchor"
  - page: "[[The Proof Ladder]]"
    role: "Key — rung anchor"
related: ["[[Carroll v. United States]]", "[[Illinois v. Gates]]", "[[Maryland v. Pringle]]"]
aliases: ["Brinegar v. US"]
tags: ["case", "fourth-amendment", "probable-cause"]
holding: "Classic probable-cause standard: practical, non-technical probabilities on which reasonable people act."
lake:
  record_id: Brinegar v. United States
  status: verified
  projected_at: 2026-07-06
---

# Brinegar v. United States

*338 U.S. 160 (1949)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal agents who knew Brinegar as a frequent hauler of illegal liquor saw him driving a heavily loaded car toward a "dry" state. They stopped and searched the car, found liquor, and he was convicted of importing it. He challenged whether the agents had probable cause to stop and search.

## Issue
What quantum and kind of proof the Fourth Amendment requires to establish probable cause.

## Rule
"In dealing with probable cause, however, as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act." — 338 U.S. at 175. ^pin-175

Probable cause exists "where 'the facts and circumstances within their [the officers'] knowledge and of which they had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the belief that' an offense has been or is being committed." — *Id.* at 175-176. ^pin-176

## Application
The agents' prior knowledge that Brinegar was a known liquor-runner, combined with their observation of his heavily loaded car heading toward a dry state, were practical, everyday probabilities sufficient to warrant a reasonable officer's belief that he was transporting liquor unlawfully. That belief furnished probable cause for the stop and search.

## Conclusion
Probable cause supported the search; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Brinegar*'s "reasonable and prudent" formulation remains the bedrock statement of probable cause, carried forward through [[Illinois v. Gates]] and applied in cases such as [[Maryland v. Pringle]].

## Appears on
- [[Probable Cause]] — *Key — Anchor*
- [[The Proof Ladder]] — *Key — rung anchor*

## Sources
- *Brinegar v. United States*, 338 U.S. 160 (1949) — https://www.courtlistener.com/opinion/104716/brinegar-v-united-states/ — pinpoints: 175, 176.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1fb740f5ee67c842", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brinegar v. United States"}, "payload": {"all": [{"cite": "338 U.S. 160", "page": "160", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "338"}, {"cite": "69 S. Ct. 1302", "page": "1302", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "93 L. Ed. 2d 1879", "page": "1879", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "1949 U.S. LEXIS 2084", "page": "2084", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1949"}], "display": "338 U.S. 160", "official": {"cite": "338 U.S. 160", "page": "160", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "338"}, "official_selection_present": true, "record_id": "Brinegar v. United States"}}
{"assertion_id": "381eb55746dfeba4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-175", "record_id": "Brinegar v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-175", "pinpoint_status": "slip-only", "quote": "state. They stopped and searched the car, found liquor, and he was convicted of importing it. He challenged whether the agents had probable cause to stop and search. ## Issue What quantum and kind of proof the Fourth Amendment requires to establish probable cause. ## Rule", "quote_fidelity": "mismatch", "record_id": "Brinegar v. United States", "star_marker": null}}
{"assertion_id": "c886a2db17a729ed", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-176", "record_id": "Brinegar v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-176", "pinpoint_status": "slip-only", "quote": "where 'the facts and circumstances within their [the officers'] knowledge and of which they had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the belief that' an offense has been or is being committed.", "quote_fidelity": "mismatch", "record_id": "Brinegar v. United States", "star_marker": null}}
{"assertion_id": "777d03c1c6fd167f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brinegar v. United States"}, "payload": {"as_of_content": "1949-06-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brinegar v. United States", "scope_note": "Classic probable-cause standard; bedrock and good law.", "varies_by_point": false}}
```

### lake record — Brinegar v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brinegar v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brinegar v. United States",
    "case_name_short": "Brinegar",
    "case_name_full": "Brinegar v. United States",
    "input_case_name": "Brinegar v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1949-10-10",
    "year": 1949,
    "docket": "23",
    "cluster_id": 104716,
    "lead_opinion_id": 104716,
    "sibling_ids": [
      104716,
      9420390,
      9420391,
      9420392
    ],
    "absolute_url": "/opinion/104716/brinegar-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8204634,
        "score": 10,
        "case_name": "Brinegar v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "338 U.S. 160",
      "volume": "338",
      "reporter": "U.S.",
      "page": "160",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "69 S. Ct. 1302",
        "volume": "69",
        "reporter": "S. Ct.",
        "page": "1302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 1879",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "1879",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1949 U.S. LEXIS 2084",
        "volume": "1949",
        "reporter": "U.S. LEXIS",
        "page": "2084",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "338 U.S. 160",
        "volume": "338",
        "reporter": "U.S.",
        "page": "160",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 S. Ct. 1302",
        "volume": "69",
        "reporter": "S. Ct.",
        "page": "1302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 1879",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "1879",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1949 U.S. LEXIS 2084",
        "volume": "1949",
        "reporter": "U.S. LEXIS",
        "page": "2084",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "338 U.S. 160",
    "official_selection": {
      "court_class": "scotus",
      "selected": "338 U.S. 160",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-175",
      "page": null,
      "quote": "state. They stopped and searched the car, found liquor, and he was convicted of importing it. He challenged whether the agents had probable cause to stop and search. ## Issue What quantum and kind of proof the Fourth Amendment requires to establish probable cause. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-176",
      "page": null,
      "quote": "where 'the facts and circumstances within their [the officers'] knowledge and of which they had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the belief that' an offense has been or is being committed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1949-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brinegar v. United States",
    "varies_by_point": false,
    "scope_note": "Classic probable-cause standard; bedrock and good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "In re B.A.T.",
          "cluster_id": 9430894,
          "cite": [
            "2023 Ohio 3366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Robin Pena",
          "cluster_id": 4807354,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Guastucci",
          "cluster_id": 4796647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
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
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re WINSHIP",
          "cluster_id": 108111,
          "cite": [
            "25 L. Ed. 2d 368",
            "90 S. Ct. 1068",
            "397 U.S. 358",
            "1970 U.S. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
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
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coolidge v. New Hampshire",
          "cluster_id": 108377,
          "cite": [
            "29 L. Ed. 2d 564",
            "91 S. Ct. 2022",
            "403 U.S. 443",
            "1971 U.S. LEXIS 25"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilar v. Texas",
          "cluster_id": 106865,
          "cite": [
            "12 L. Ed. 2d 723",
            "84 S. Ct. 1509",
            "378 U.S. 108",
            "1964 U.S. LEXIS 994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
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
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
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
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guzman v. State",
          "cluster_id": 2449770,
          "cite": [
            "955 S.W.2d 85",
            "1997 Tex. Crim. App. LEXIS 72",
            "1997 WL 587024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 106022,
          "cite": [
            "4 L. Ed. 2d 697",
            "80 S. Ct. 725",
            "362 U.S. 257",
            "1960 U.S. LEXIS 1413",
            "78 A.L.R. 2d 233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
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
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
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
        "journal_ref": "Brinegar v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(104716 OR 9420390 OR 9420391 OR 9420392) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTU5MTc0NDAwMDAwJnM9NDYyNTE5MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28104716+OR+9420390+OR+9420391+OR+9420392%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(104716 OR 9420390 OR 9420391 OR 9420392)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDY2JnM9MTA4ODUwJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28104716+OR+9420390+OR+9420391+OR+9420392%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(104716 OR 9420390 OR 9420391 OR 9420392)",
        "reviewed": 106,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 106,
        "triage_read": 1,
        "triage_snippet_classified": 105
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(104716 OR 9420390 OR 9420391 OR 9420392)",
    "indexed_citing_opinions": 4049,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 104716,
        "count": 3676,
        "count_source": "search"
      },
      {
        "opinion_id": 9420390,
        "count": 464,
        "count_source": "search"
      },
      {
        "opinion_id": 9420391,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9420392,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6015,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brinegar-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MjYzMDYmcz0xMDYyMTc4OCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28104716+OR+9420390+OR+9420391+OR+9420392%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 104716,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 99080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 100685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 104570,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 104607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1475726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1479874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1488414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1499078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1507600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1509096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1512100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1565995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1735465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104716,
        "cited_id": 1876453,
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
    "date_created": "2026-07-04T20:35:08Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:35:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:35:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:37:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:35:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brinegar v. United States

```
<div>
<center><b><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U.S. 160</a></span> (1949)</b></center>
<center><h1>BRINEGAR<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 12.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 18-19, 1948.</center>
<center>Decided June 27, 1949.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE TENTH CIRCUIT.
<p><span class="star-pagination">*161</span> <i>Irving E. Ungerman</i> argued the cause for petitioner. With him on the brief was <i>Leslie L. Conner.</i></p>
<p><i>Stanley M. Silverberg</i> argued the cause for the United States. <i>Solicitor General Perlman, Assistant Attorney General Campbell, Robert S. Erdahl</i> and <i>Beatrice Rosenberg</i> were on the brief.</p>
<p>MR. JUSTICE RUTLEDGE delivered the opinion of the Court.</p>
<p>Brinegar was convicted of importing intoxicating liquor into Oklahoma from Missouri in violation of the federal statute which forbids such importation contrary to the laws of any state.<sup>[1]</sup> His conviction was based in <span class="star-pagination">*162</span> part on the use in evidence against him of liquor seized from his automobile in the course of the alleged unlawful importation.</p>
<p>Prior to the trial Brinegar moved to suppress this evidence as having been secured through an unlawful search and seizure.<sup>[2]</sup> The motion was denied, as was a renewal of the objection at the trial.</p>
<p>The Court of Appeals affirmed the conviction, <span class="citation" data-id="9641361"><a href="/opinion/1499078/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">165 F. 2d 512</a></span>, and certiorari was sought solely on the ground that the search and seizure contravened the Fourth Amendment and therefore the use of the liquor in evidence vitiated the conviction. We granted the writ to determine this question. <span class="citation multiple-matches"><a href="/c/U.%20S./333/841/">333 U. S. 841</a></span>.</p>
<p>The facts are substantially undisputed. At about six o'clock on the evening of March 3, 1947, Malsed, an investigator of the Alcohol Tax Unit, and Creehan, a special investigator, were parked in a car beside a highway near the Quapaw Bridge in northeastern Oklahoma. The point was about five miles west of the Missouri-Oklahoma line. Brinegar drove past headed west in his Ford coupe. Malsed had arrested him about five months earlier for illegally transporting liquor; had seen him loading liquor into a car or truck in Joplin, Missouri, on at least two occasions during the preceding six months; and knew him to have a reputation for hauling liquor. As Brinegar passed, Malsed recognized both him and the Ford. He told Creehan, who was driving the officers' car, that <span class="star-pagination">*163</span> Brinegar was the driver of the passing car. Both agents later testified that the car, but not especially its rear end, appeared to be "heavily loaded" and "weighted with something." Brinegar increased his speed as he passed the officers. They gave chase. After pursuing him for about a mile at top speed, they gained on him as his car skidded on a curve, sounded their siren, overtook him, and crowded his car to the side of the road by pulling across in front of it. The highway was one leading from Joplin, Missouri, toward Vinita, Oklahoma, Brinegar's home.</p>
<p>As the agents got out of their car and walked back toward petitioner, Malsed said, "Hello, Brinegar, how much liquor have you got in the car?" or "How much liquor have you got in the car this time?" Petitioner replied, "Not too much," or "Not so much." After further questioning he admitted that he had twelve cases in the car. Malsed testified that one case, which was on the front seat, was visible from outside the car, but petitioner testified that it was covered by a lap robe. Twelve more cases were found under and behind the front seat. The agents then placed Brinegar under arrest and seized the liquor.</p>
<p>The district judge, after a hearing on the motion to suppress at which the facts stated above appeared in evidence, was of the opinion that "the mere fact that the agents knew that this defendant was engaged in hauling whiskey, even coupled with the statement that the car appeared to be weighted, would not be probable cause for the search of this car." Therefore, he thought, there was no probable cause when the agents began the chase. He held, however, that the voluntary admission made by petitioner after his car had been stopped constituted probable cause for a search, regardless of the legality of the arrest and detention, and that therefore the evidence was admissible. At the trial, as has been said, the court overruled petitioner's renewal of the objection.</p>
<p><span class="star-pagination">*164</span> The Court of Appeals, one judge dissenting, took essentially the view held by the District Court. The dissenting judge thought that the search was unlawful and therefore statements made during its course could not justify the search.</p>
<p>The crucial question is whether there was probable cause for Brinegar's arrest, in the light of prior adjudications on this problem, more particularly <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, which on its face most closely approximates the situation presented here.<sup>[3]</sup></p>
<p>The <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> decision held that, under the Fourth Amendment, a valid search of a vehicle moving on a public highway may be had without a warrant, but only if probable cause for the search exists.<sup>[4]</sup> The Court then went on to rule that the facts presented amounted to probable cause for the search of the automobile there involved. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#160" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 160</a></span>.</p>
<p>In the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case three federal prohibition agents and a state officer stopped and searched the defendants' car on a highway leading from Detroit to Grand Rapids, Michigan, and seized a quantity of liquor discovered in the search. About three months before the search, the two defendants and another man called on two of the agents at an apartment in Grand Rapids and, unaware that they were dealing with federal agents, agreed to sell one of the agents three cases of liquor. Both agents noticed the Oldsmobile roadster in which the three men came to the <span class="star-pagination">*165</span> apartment and its license number. Presumably because the official capacity of the proposed purchaser was suspected by the defendants, the liquor was never delivered.</p>
<p>About a week later the same two agents, while patrolling the road between Grand Rapids and Detroit on the lookout for violations of the National Prohibition Act, were passed by the defendants, who were proceeding in a direction from Grand Rapids toward Detroit in the same Oldsmobile roadster. The agents followed the defendants for some distance but lost trace of them. Still later, on the occasion of the search, while the officers were patrolling the same highway, they met and passed the defendants, who were in the same roadster, going in a direction from Detroit toward Grand Rapids. Recognizing the defendants, the agents turned around, pursued them, stopped them about sixteen miles outside Grand Rapids, searched their car and seized the liquor it carried.</p>
<p>This Court ruled that the information held by the agents, together with the judicially noticed fact that Detroit was "one of the most active centers for introducing illegally into this country spirituous liquors for distribution into the interior" (<span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#160" aria-description="Citation for case: Carroll v. United States">267 U. S. at 160</a></span>), constituted probable cause for the search.</p>
<p></p>
<h2>I.</h2>
<p>Obviously the basic facts held to constitute probable cause in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case were very similar to the basic facts here. In each case the search was of an automobile moving on a public highway and was made without a warrant by federal officers charged with enforcing federal statutes outlawing the transportation of intoxicating liquors (except under conditions not complied with).<sup>[5]</sup><span class="star-pagination">*166</span> In each instance the officers were patrolling the highway in the discharge of their duty. And in each before stopping the car or starting to pursue it they recognized both the driver and the car, from recent personal contact and observation, as having been lately engaged in illicit liquor dealings.<sup>[6]</sup> Finally, each driver was proceeding in his identified car in a direction from a known source of liquor supply toward a probable illegal market, under circumstances indicating no other probable purpose than to carry on his illegal adventure.<sup>[7]</sup></p>
<p>These are the ultimate facts. Necessarily the concrete, subordinate facts on which they were grounded in the two cases differed somewhat in detail. The more important of the variations in details of the proof are as follows:</p>
<p>In <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> the agent's knowledge of the primary and ultimate fact that the accused were engaged in liquor running was derived from the defendants' offer to sell liquor to the agents some three months prior to the search, while here that knowledge was derived largely from Malsed's personal observation, reinforced by hearsay; the officers when they bargained for the liquor in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> saw the number of the defendants' car, whereas no such fact is shown in this record; and in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> the Court took judicial notice that Detroit was on the international boundary and an active center for illegal importation <span class="star-pagination">*167</span> of spirituous liquors for distribution into the interior, while in this case the facts that Joplin, Missouri, was a ready source of supply for liquor and Oklahoma a place of likely illegal market were known to the agent Malsed from his personal observation and experience as well as from facts of common knowledge.</p>
<p>Treating first the two latter and less important matters, in view of the positive and undisputed evidence concerning Malsed's identification of Brinegar's Ford, we think no significance whatever attaches, for purposes of distinguishing the cases, to the fact that in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case the officers saw and recalled the license number of the offending car while this record discloses no like recollection.</p>
<p>Likewise it is impossible to distinguish the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case with reference to the proof relating to the source of supply, the place of probable destination and illegal market, and consequently the probability that the known liquor operators were using the connecting highway for the purposes of their unlawful business.</p>
<p>There were of course some legal as well as some factual differences in the two situations. Under the statute in review in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> the whole nation was legally dry. Not only the manufacture, but the importation, transportation and sale of intoxicating liquors were prohibited throughout the country. Under the statute now in question only the importation of such liquors contrary to the law of the state into which they are brought and in which they were seized is forbidden.</p>
<p>In the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case the Court judicially noticed that Detroit was located on the international boundary with Canada and had become an active center for illegally bringing liquor into the country for distribution into the interior. This was pertinent in connection with other circumstances, for showing the probability under which the agents acted that use of the highway connecting <span class="star-pagination">*168</span> Detroit and Grand Rapids by the known operators in liquor was for the purpose of carrying on their unlawful traffic.</p>
<p>In this case, the record shows that Brinegar had used Joplin, Missouri, to Malsed's personal knowledge derived from direct observation, not merely from hearsay as seems to be suggested, as a source of supply on other occasions within the preceding six months. It also discloses that Brinegar's home was in Vinita, Oklahoma, and that Brinegar when apprehended was traveling in a direction leading from Joplin to Vinita, at a point about four or five miles west of the Missouri-Oklahoma line.</p>
<p>Joplin, like Detroit in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, was a ready source of supply. But unlike Detroit it was not an illegal source. So far as appears, Brinegar's purchases there were entirely legal. And so, we may assume for present purposes, was his transportation of the liquor in Missouri, until he reached and crossed the state line into Oklahoma.</p>
<p>This difference, however, is insubstantial. For the important thing here is not whether Joplin was an illegal source of supply; it is rather that Joplin was a ready, convenient and probable one for persons disposed to violate the Oklahoma and federal statutes. That fact was demonstrated fully, not only by the geographic facts, but by Malsed's direct and undisputed testimony of his personal observation of Brinegar's use of liquor-dispensing establishments in Joplin for procuring his whiskey. Such direct evidence was lacking in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> as to Detroit, and for that reason the Court resorted to judicial notice of the commonly known facts to supply that deficiency. Malsed's direct testimony, based on his personal observation, dispensed with that necessity in this case.</p>
<p>The situation relating to the probable place of market, as bearing on the probability of unlawful importation, is somewhat different. Broadly on the facts this may well have been taken to be the State of Oklahoma as a <span class="star-pagination">*169</span> whole or its populous northeastern region. From the facts of record we know, as the agents knew, that Oklahoma was a "dry" state. At the time of the search, its law forbade the importation of intoxicating liquors from other states, except under a permit not generally procurable<sup>[8]</sup> and which there is no pretense Brinegar had secured or attempted to secure. This fact, taken in connection with the known "wet" status of Missouri and the location of Joplin close to the Oklahoma line, affords a very natural situation for persons inclined to violate the Oklahoma and federal statutes to ply their trade. The proof therefore concerning the source of supply, the place of probable destination and illegal market, and hence the probability that Brinegar was using the highway for the forbidden transportation, was certainly no less strong than the showing in these respects in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case.<sup>[9]</sup></p>
<p>Finally, as for the most important potential distinction, namely, that concerning the primary and ultimate fact that the petitioner was engaging in liquor running, Malsed's personal observation of Brinegar's recent activities established that he was so engaged quite as effectively as did the agent's prior bargaining with the defendants in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case. He saw Brinegar loading liquor, in <span class="star-pagination">*170</span> larger quantities than would be normal for personal consumption, into a car or a truck in Joplin on other occasions during the six months prior to the search. He saw the car Brinegar was using in this case in use by him at least once in Joplin within that period and followed it. And several months prior to the search he had arrested Brinegar for unlawful transportation of liquor and this arrest had resulted in an indictment which was pending at the time of this trial. Moreover Malsed instantly recognized Brinegar's Ford coupe and Brinegar as the driver when he passed the parked police car. And at that time Brinegar was moving in a direction from Joplin toward Vinita only a short distance inside Oklahoma from the state line.</p>
<p>All these facts are undisputed. Wholly apart from Malsed's knowledge that Brinegar bore the general reputation of being engaged in liquor running, they constitute positive and convincing evidence that Brinegar was engaged in that activity, no less convincing than the evidence in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> that the defendants had offered to sell liquor to the officers. The evidence here is undisputed, is admissible on the issue of probable cause, and clearly establishes that the agent had good ground for believing that Brinegar was engaged regularly throughout the period in illicit liquor running and dealing.</p>
<p>Notwithstanding the variations in detail, therefore, we think the proof in this case furnishes support quite as strong as that made in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, indeed stronger in some respects, to sustain the ultimate facts there held in the aggregate to constitute probable cause for a search identical in all substantial and material respects with the one made here. Nothing in the variations of detail affords a substantial basis for undermining here any of the ultimate facts held to be sufficient in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> or for distinguishing the cases. Each of the ultimate facts found in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> to constitute probable cause, when taken together, <span class="star-pagination">*171</span> is present in this case and is fully substantiated by the proof. Accordingly the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> decision must be taken to control this situation, unless it is now to be overruled.</p>
<p>This is true, although the trial court and the Court of Appeals, including the dissenting judge, were of the opinion, as stated by the latter court, "that the facts within the knowledge of the investigators and of which they had reasonable trustworthy information prior to the time the incriminating statements were made by Brinegar were not sufficient to lead a reasonably discreet and prudent man to believe that intoxicating liquor was being transported in the coupe, and did not constitute probable cause for a search." <span class="citation" data-id="9641361"><a href="/opinion/1499078/brinegar-v-united-states/#514" aria-description="Citation for case: Brinegar v. United States">165 F. 2d at 514</a></span>. If, as we think, the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case is indistinguishable from this one on the material facts, and that decision is to continue in force, it necessarily follows that the quoted "finding" or "conclusion" was erroneous.<sup>[10]</sup> In the absence of any significant difference in the facts, it cannot be that the Fourth Amendment's incidence turns on whether different trial judges draw general conclusions that the facts are sufficient or insufficient to constitute probable cause.</p>
<p></p>
<h2>II.</h2>
<p>It remains to consider one further asserted difference between this case and the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, having to do with the admissibility or inadmissibility at the trial of the evidence on which the agents acted in making the search, particularly the evidence concerning their knowledge that the defendants were engaging in illicit liquor running.</p>
<p><span class="star-pagination">*172</span> It is argued first that this case can be distinguished from <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> because Malsed's knowledge of this primary and ultimate fact rested wholly or largely on surmise or hearsay. This argument is disproved by the facts of record which we have set forth above. There was hearsay, but there was much more. Indeed, as we have emphasized, the facts derived from Malsed's personal observations were sufficient in themselves, without the hearsay concerning general reputation, to sustain his conclusion concerning the illegal character of Brinegar's operations.</p>
<p>But a further distinction based upon inadmissibility of the evidence is asserted. It is said that, while in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> the defendants' offer to sell liquor to the agents was admissible and was admitted at the trial, here the evidence that Malsed had arrested Brinegar for illegal transportation of liquor several months before the search, though admitted on the hearing on the motion to suppress, was excluded at the trial. Cf. <i>Michelson</i> v. <i>United States,</i> <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">335 U. S. 469</a></span>. The inference seems to be that the evidence concerning the prior arrest should not have been received at the hearing on the motion. In any event, the conclusion is drawn that the factors relating to inadmissibility of the evidence here, for purposes of proving guilt at the trial, deprive the evidence as a whole of sufficiency to show probable cause for the search and therefore distinguish this case from the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case.</p>
<p>Apart from its failure to take account of the facts disclosed by Malsed's direct and personal observation, even if his testimony concerning the prior arrest were excluded, the so-called distinction places a wholly unwarranted emphasis upon the criterion of admissibility in evidence, to prove the accused's guilt, of the facts relied upon to show probable cause. That emphasis, we think, goes much too far in confusing and disregarding <span class="star-pagination">*173</span> the difference between what is required to prove guilt in a criminal case and what is required to show probable cause for arrest or search. It approaches requiring (if it does not in practical effect require) proof sufficient to establish guilt in order to substantiate the existence of probable cause. There is a large difference between the two things to be proved, as well as between the tribunals which determine them, and therefore a like difference in the <i>quanta</i> and modes of proof required to establish them.</p>
<p>For a variety of reasons relating not only to probative value and trustworthiness, but also to possible prejudicial effect upon a trial jury and the absence of opportunity for cross-examination, the generally accepted rules of evidence throw many exclusionary protections about one who is charged with and standing trial for crime. Much evidence of real and substantial probative value goes out on considerations irrelevant to its probative weight but relevant to possible misunderstanding or misuse by the jury.</p>
<p>Thus, in this case, the trial court properly excluded from the record at the trial, cf. <i>Michelson</i> v. <i>United States,</i> <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">335 U. S. 469</a></span>, Malsed's testimony that he had arrested Brinegar several months earlier for illegal transportation of liquor and that the resulting indictment was pending in another court at the time of the trial of this case. This certainly was not done on the basis that the testimony concerning arrest, or perhaps even the indictment, was surmise or hearsay or that it was without probative value. Yet the same court admitted the testimony at the hearing on the motion to suppress the evidence seized in the search, where the issue was not guilt but probable cause and was determined by the court without a jury.<sup>[11]</sup></p>
<p><span class="star-pagination">*174</span> The court's rulings, one admitting, the other excluding the identical testimony, were neither inconsistent nor improper. They illustrate the difference in standards and latitude allowed in passing upon the distinct issues of probable cause and guilt. Guilt in a criminal case must be proved beyond a reasonable doubt and by evidence confined to that which long experience in the common-law tradition, to some extent embodied in the Constitution, has crystallized into rules of evidence consistent with that standard. These rules are historically grounded rights of our system, developed to safeguard men from dubious and unjust convictions, with resulting forfeitures of life, liberty and property.</p>
<p>However, if those standards were to be made applicable in determining probable cause for an arrest or for search and seizure, more especially in cases such as this involving moving vehicles used in the commission of crime, few indeed would be the situations in which an officer, charged with protecting the public interest by enforcing the law, could take effective action toward that end.<sup>[12]</sup> Those standards have seldom been so applied.<sup>[13]</sup></p>
<p><span class="star-pagination">*175</span> In dealing with probable cause, however, as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act. The standard of proof is accordingly correlative to what must be proved.</p>
<p>"The substance of all the definitions" of probable cause "is a reasonable ground for belief of guilt." <i>McCarthy</i> v. <i>De Armit,</i> 99 Pa. St. 63, 69, quoted with approval in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> opinion. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#161" aria-description="Citation for case: Carroll v. United States">267 U. S. at 161</a></span>. And this "means less than evidence which would justify condemnation" or conviction, as Marshall, C. J., said for the Court more than a century ago in <i>Locke</i> v. <i>United States,</i> <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span>. Since Marshall's time, at any rate,<sup>[14]</sup> it has come to mean more than bare suspicion: Probable cause exists where "the facts and circumstances within their [the officers'] knowledge and of which they had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the <span class="star-pagination">*176</span> belief that" an offense has been or is being committed. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span>.<sup>[15]</sup></p>
<p>These long-prevailing standards seek to safeguard citizens from rash and unreasonable interferences with privacy and from unfounded charges of crime. They also seek to give fair leeway for enforcing the law in the community's protection. Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability. The rule of probable cause is a practical, nontechnical conception affording the best compromise that has been found for accommodating these often opposing interests. Requiring more would unduly hamper law enforcement. To allow less would be to leave law-abiding citizens at the mercy of the officers' whim or caprice.</p>
<p>The troublesome line posed by the facts in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case and this case is one between mere suspicion and probable cause. That line necessarily must be drawn by an act of judgment formed in the light of the particular situation and with account taken of all the circumstances. No problem of searching the home or any other place of privacy was presented either in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> or here. Both cases involve freedom to use public highways in swiftly moving vehicles for dealing in contraband, and to be unmolested <span class="star-pagination">*177</span> by investigation and search in those movements. In such a case the citizen who has given no good cause for believing he is engaged in that sort of activity is entitled to proceed on his way without interference.<sup>[16]</sup> But one who recently and repeatedly has given substantial ground for believing that he is engaging in the forbidden transportation in the area of his usual operations has no such immunity, if the officer who intercepts him in that region knows that fact at the time he makes the interception and the circumstances under which it is made are not such as to indicate the suspect is going about legitimate affairs.</p>
<p>This does not mean, as seems to be assumed, that every traveler along the public highways may be stopped and searched at the officers' whim, caprice or mere suspicion.<sup>[17]</sup> The question presented in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case lay on the border between suspicion and probable cause. But the Court carefully considered that problem and resolved it by concluding that the facts within the officers' knowledge when they intercepted the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> defendants amounted to more than mere suspicion and constituted probable cause for their action. We cannot say this conclusion was wrong, or was so lacking in reason and consistency with the Fourth Amendment's purposes that it <span class="star-pagination">*178</span> should now be overridden. Nor, as we have said, can we find in the present facts any substantial basis for distinguishing this case from the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case.</p>
<p>Accordingly the judgment is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BURTON, concurring.</p>
<p>I join in the opinion of the Court that there was probable cause for the search within the standards established in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>.</p>
<p>Whether or not the necessary probable cause for a search of the petitioner's car existed <i>before</i> the government agents caught up with him and said to him, "How much liquor have you got in the car this time?" and he replied, "Not too much," it is clear, and each of the lower courts found, that, under all of the circumstances of this case, the necessary probable cause for the search of the petitioner's car <i>then</i> existed. If probable cause for the search existed at that point, the search which then was begun was lawful without a search warrant as is demonstrated in the opinion of the Court. That search disclosed that a crime was in the course of its commission in the presence of the arresting officers, precisely as those officers had good reason to believe was the fact. The ensuing arrest of the petitioner was lawful and the subsequent denial of his motion to suppress the evidence obtained by the search was properly sustained.</p>
<p>It is my view that it is not necessary, for the purposes of this case, to establish probable cause for the search at any point earlier than that of the above colloquy. The earlier events, recited in the opinion of the Court, disclose at least ample grounds to justify the chase and official interrogation of the petitioner by the government agents in the manner adopted. This interrogation quickly disclosed indisputable probable cause for the search and for the arrest. In my view, these earlier events not only justified the steps taken by the government <span class="star-pagination">*179</span> agents but those events imposed upon the government agents a positive duty to investigate further, in some such manner as they adopted. It is only by alertness to proper occasions for prompt inquiries and investigations that effective prevention of crime and enforcement of law is possible. Government agents are commissioned to represent the interests of the public in the enforcement of the law and this requires affirmative action not only when there is reasonable ground for an arrest or probable cause for a search but when there is reasonable ground for an investigation. This is increasingly true when the facts point directly to a crime in the course of commission in the presence of the agent. Prompt investigation may then not only discover but, what is still more important, may interrupt the crime and prevent some or all of its damaging consequences.</p>
<p>In the present case, from the moment that the agents saw this petitioner driving his heavily laden car in Oklahoma, evidently en route from Missouri, the events justifying and calling for an interrogation of him rapidly gained cumulative force. Nothing occurred that even tended to lessen the reasonableness of the original basis for the suspicion of the agents that a crime within their particular line of duty was being committed in their presence. Nothing occurred to make it unlawful for them, in line of duty, to make the interrogation which suggested itself to them. When their interrogation of the petitioner led to his voluntary response as quoted above, that response demonstrated ample probable cause for an immediate search of the petitioner's car for the contraband liquor which he had indicated might be found there. The interrogation of the petitioner, thus made by the agents in their justifiable investigation of a crime reasonably suspected by them to be in the course of commission in their presence, cannot now be resorted to by the petitioner in support of a motion to suppress the evidence of that crime. Government agents have duties of crime <span class="star-pagination">*180</span> prevention and crime detection as well as the duty of arresting offenders caught in the commission of a crime or later identified as having committed a crime. The performance of the first duties are as important as the performance of the last. In this case the performance of the first halted the commission of the crime and also resulted in the arrest of the offender.</p>
<p>MR. JUSTICE JACKSON, dissenting.</p>
<p>When this Court recently has promulgated a philosophy that some rights derived from the Constitution are entitled to "a preferred position," <i>Murdock</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9419338"><a href="/opinion/103831/murdock-v-pennsylvania/#115" aria-description="Citation for case: Murdock v. Pennsylvania">319 U. S. 105, 115</a></span>, dissent at p. 166; <i>Saia</i> v. <i>New York,</i> <span class="citation" data-id="9420191"><a href="/opinion/104570/saia-v-new-york/#562" aria-description="Citation for case: Saia v. New York">334 U. S. 558, 562</a></span>, I have not agreed. We cannot give some constitutional rights a preferred position without relegating others to a deferred position; we can establish no firsts without thereby establishing seconds. Indications are not wanting that Fourth Amendment freedoms are tacitly marked as secondary rights, to be relegated to a deferred position.</p>
<p>The Fourth Amendment states: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>These, I protest, are not mere second-class rights but belong in the catalog of indispensable freedoms. Among deprivations of rights, none is so effective in cowing a population, crushing the spirit of the individual and putting terror in every heart. Uncontrolled search and seizure is one of the first and most effective weapons in the arsenal of every arbitrary government. And one need only briefly to have dwelt and worked among a people possessed of many admirable qualities but deprived of these rights to know that the human personality <span class="star-pagination">*181</span> deteriorates and dignity and self-reliance disappear where homes, persons and possessions are subject at any hour to unheralded search and seizure by the police.</p>
<p>But the right to be secure against searches and seizures is one of the most difficult to protect. Since the officers are themselves the chief invaders, there is no enforcement outside of court.</p>
<p>Only occasional and more flagrant abuses come to the attention of the courts, and then only those where the search and seizure yields incriminating evidence and the defendant is at least sufficiently compromised to be indicted. If the officers raid a home, an office, or stop and search an automobile but find nothing incriminating, this invasion of the personal liberty of the innocent too often finds no practical redress. There may be, and I am convinced that there are, many unlawful searches of homes and automobiles of innocent people which turn up nothing incriminating, in which no arrest is made, about which courts do nothing, and about which we never hear.</p>
<p>Courts can protect the innocent against such invasions only indirectly and through the medium of excluding evidence obtained against those who frequently are guilty. Federal courts have used this method of enforcement of the Amendment, in spite of its unfortunate consequences on law enforcement, although many state courts do not. This inconsistency does not disturb me, for local excesses or invasions of liberty are more amenable to political correction, the Amendment was directed only against the new and centralized government, and any really dangerous threat to the general liberties of the people can come only from this source. We must therefore look upon the exclusion of evidence in federal prosecutions, if obtained in violation of the Amendment, as a means of extending protection against the central government's agencies. So a search against Brinegar's car must be regarded as a search of the car of Everyman.</p>
<p><span class="star-pagination">*182</span> We must remember that the extent of any privilege of search and seizure without warrant which we sustain, the officers interpret and apply themselves and will push to the limit. We must remember, too, that freedom from unreasonable search differs from some of the other rights of the Constitution in that there is no way in which the innocent citizen can invoke advance protection. For example, any effective interference with freedom of the press, or free speech, or religion, usually requires a course of suppressions against which the citizen can and often does go to the court and obtain an injunction. Other rights, such as that to an impartial jury or the aid of counsel, are within the supervisory power of the courts themselves. Such a right as just compensation for the taking of private property may be vindicated after the act in terms of money.</p>
<p>But an illegal search and seizure usually is a single incident, perpetrated by surprise, conducted in haste, kept purposely beyond the court's supervision and limited only by the judgment and moderation of officers whose own interests and records are often at stake in the search. There is no opportunity for injunction or appeal to disinterested intervention. The citizen's choice is quietly to submit to whatever the officers undertake or to resist at risk of arrest or immediate violence.</p>
<p>And we must remember that the authority which we concede to conduct searches and seizures without warrant may be exercised by the most unfit and ruthless officers as well as by the fit and responsible, and resorted to in case of petty misdemeanors as well as in the case of the gravest felonies.</p>
<p>With this prologue I come to the case of Brinegar. His automobile was one of his "effects" and hence within the express protection of the Fourth Amendment. Undoubtedly the automobile presents peculiar problems for enforcement agencies, is frequently a facility for the perpetration of crime and an aid in the escape of criminals. <span class="star-pagination">*183</span> But if we are to make judicial exceptions to the Fourth Amendment for these reasons, it seems to me they should depend somewhat upon the gravity of the offense. If we assume, for example, that a child is kidnaped and the officers throw a roadblock about the neighborhood and search every outgoing car, it would be a drastic and undiscriminating use of the search. The officers might be unable to show probable cause for searching any particular car. However, I should candidly strive hard to sustain such an action, executed fairly and in good faith, because it might be reasonable to subject travelers to that indignity if it was the only way to save a threatened life and detect a vicious crime. But I should not strain to sustain such a roadblock and universal search to salvage a few bottles of bourbon and catch a bootlegger.</p>
<p>The Court sustains this search as an application of <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>. I dissent because I regard it as an extension of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, which already has been too much taken by enforcement officers as blanket authority to stop and search cars on suspicion. I shall confine this opinion to showing the several ways in which this decision seems to expand the already expansive right to stop and search automobiles.</p>
<p>In the first place, national prohibition legislation was found in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case to have put congressional authority back of the search without warrant of cars suspected of its violation. No such congressional authority exists in this case. The Court is voluntarily dispensing with warrant in this case as matter of judicial policy, while in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case the Court could have required a warrant only by holding an Act of Congress unconstitutional.<sup>[1]</sup></p>
<p><span class="star-pagination">*184</span> A second and important distinction is that in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case the lower court had found that the evidence showed probable cause for that search, while in this case two courts below have held that (except for evidence turned up after the search, which we consider later) there was not probable cause. If we assume the facts to be indistinguishable, this important distinction emerges from the decisions: <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> held only that these facts <i>permitted</i> a District Court, if so convinced, to find probable cause from them. The Court now holds these facts <i>require</i> a finding of probable cause. This shift from a permissive to a mandatory basis is a shift of no inconsiderable significance.</p>
<p>While the Court sustained the search without warrant in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, it emphatically declined to dispense with the necessity for evidence of probable cause for making such a search. It said: "It would be intolerable and unreasonable if a prohibition agent were authorized to <span class="star-pagination">*185</span> stop every automobile on the chance of finding liquor and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in. But those lawfully within the country, entitled to use the public highways, have a right to free passage without interruption or search unless there is known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132 at 153</a></span>.</p>
<p>Analysis of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> facts shows that while several facts are common to the two cases, the settings from which those facts take color and meaning differ in essential respects.</p>
<p>In the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, the primary and the ultimate fact that the accused was engaged in liquor running was not surmise or hearsay, as it is here. Carroll and his companion, some time before their arrest, had come to meet the two arresting officers, not then known as officials, upon the understanding that they were customers wanting liquor. Carroll promised to sell and deliver them three cases at $130 a case. For some reason there was a failure to deliver, but when the officers arrested them they had this positive and personal knowledge that these men were trafficking in liquor. Also, it is to be noted that the officers, when bargaining for liquor, saw and learned the number of the car these bootleggers were using in the business and, at the time of the arrest, recognized it as the same car.</p>
<p>Then this Court took judicial notice that the place whence Carroll, when stopped, was coming, on the international boundary, "is one of the most active centers <span class="star-pagination">*186</span> for introducing illegally into this country spirituous liquors for distribution into the interior." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#160" aria-description="Citation for case: Carroll v. United States">267 U. S. at 160</a></span>. These facts provided the very foundation of the opinion of this Court on the subject of probable cause, which it summed up as follows:</p>
<p>"The partners in the original combination to sell liquor in Grand Rapids were together in the same automobile they had been in the night when they tried to furnish the whiskey to the officers which was thus identified as part of the firm equipment. They were coming from the direction of the great source of supply for their stock to Grand Rapids where they plied their trade. That the officers when they saw the defendants believed that they were carrying liquor we can have no doubt, and we think it is equally clear that they had reasonable cause for thinking so." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#160" aria-description="Citation for case: Carroll v. United States">267 U. S. at 160</a></span>.</p>
<p>Not only did the Court rely almost exclusively on information gained in personal negotiations of the officers to buy liquor from defendants to show probable cause, but the dissenting members asserted it to be the only circumstance which could have subjected the accused to any reasonable suspicion. And that is the sort of direct evidence on personal knowledge that is lacking here.</p>
<p>In contrast, the proof that Brinegar was trafficking in illegal liquor rests on inferences from two circumstances, neither one of which would be allowed to be proved at a trial: One, it appears that the same officers previously had arrested Brinegar on the same charge. But there had been no conviction and it does not appear whether the circumstances of the former arrest indicated any strong probability of it. In any event, this evidence of a prior arrest of the accused would not even be admissible in a trial to prove his guilt on this occasion.</p>
<p>As a second basis for inference, the officers also say that Brinegar had the reputation of being a liquor runner. The weakness of this hearsay evidence is revealed by contrasting <span class="star-pagination">*187</span> it with the personal negotiations which proved that Carroll was one. The officers' testimony of reputation would not be admissible in a trial of defendant unless he was unwise enough to open the subject himself by offering character testimony. See <i>Greer</i> v. <i>United States,</i> <span class="citation" data-id="99080"><a href="/opinion/99080/greer-v-united-states/#560" aria-description="Citation for case: Greer v. United States">245 U. S. 559, 560</a></span>.</p>
<p>I do not say that no evidence which would be inadmissible to prove guilt at a trial may be considered in weighing probable cause, but I am surprised that the Court is ready to rule that inadmissible evidence alone, as to vital facts without which other facts give little indication of guilt, establish probable cause as matter of law. The only other fact is that officer Malsed stated that twice, on September 23 and on September 30, about six months before this arrest, he saw Brinegar in a Missouri town, where liquor is lawful, loading liquor into a truck, not the car in this case. That is all. The Court from that draws the inference which the courts below, familiar we presume with the local conditions, refused to draw, <i>viz.,</i> that to be seen loading liquor into a truck where it is lawful is proof that defendant is unlawfully trafficking in liquor some distance away. There is not, as in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, evidence that he was offering liquor for sale to anybody at any time. In the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, the offer to sell liquor to the officers would itself have been a law violation. It seems rather foggy reasoning to say that the courts are obliged to draw the same conclusion from legal conduct as from illegal conduct.</p>
<p>I think we cannot say the lower courts were wrong as matter of law in holding that there was no probable cause up to the time the car was put off the road and stopped, and that we cannot say it was proper to consider the deficiency supplied by what followed. When these officers engaged in a chase at speeds dangerous to those who participated, and to other lawful wayfarers, and ditched the defendant's car, they were either taking the <span class="star-pagination">*188</span> initial steps in arrest, search and seizure, or they were committing a completely lawless and unjustifiable act. That they intended to set out on a search is unquestioned, and there seems no reason to doubt that in their own minds they thought there was cause and right to search. They have done exactly what they would have done, and done rightfully, if they had been executing a warrant. At all events, whatever it may have lacked technically of arrest, search and seizure, it was a form of coercion and duress under color of official authorityand a very formidable type of duress at that.</p>
<p>I do not, of course, contend that officials may never stop a car on the highway without the halting being considered an arrest or a search. Regulations of traffic, identifications where proper, traffic census, quarantine regulations, and many other causes give occasion to stop cars in circumstances which do not imply arrest or charge of crime. And to trail or pursue a suspected car to its destination, to observe it and keep it under surveillance, is not in itself an arrest nor a search. But when a car is forced off the road, summoned to stop by a siren, and brought to a halt under such circumstances as are here disclosed, we think the officers are then in the position of one who has entered a home: the search at its commencement must be valid and cannot be saved by what it turns up. <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; and see <i>Nueslein</i> v. <i>District of Columbia,</i> 73 App. D. C. 85, <span class="citation" data-id="1512100"><a href="/opinion/1512100/nueslein-v-district-of-columbia/" aria-description="Citation for case: Nueslein v. District of Columbia">115 F. 2d 690</a></span>.</p>
<p>The findings of the two courts below make it clear that this search began and proceeded through critical and coercive phases without the justification of probable cause. What it yielded cannot save it. I would reverse the judgment.</p>
<p>MR. JUSTICE FRANKFURTER and MR. JUSTICE MURPHY join in this opinion.</p>
<h2>NOTES</h2>
<p>[1]  Section 3 (a) of the Liquor Enforcement Act of 1936, <span class="citation no-link">49 Stat. 1928</span>, <span class="citation no-link">27 U. S. C. § 223</span>, provides: "Whoever shall import, bring, or transport any intoxicating liquor into any State in which all sales (except for scientific, sacramental, medicinal, or mechanical purposes) of intoxicating liquor containing more than 4 per centum of alcohol by volume are prohibited, otherwise than in the course of continuous interstate transportation through such State, or attempt so to do, or assist in so doing, shall: (1) If such liquor is not accompanied by such permit or permits, license or licenses therefor as are now or hereafter required by the laws of such State; or (2) if all importation, bringing, or transportation of intoxicating liquor into such State is prohibited by the laws thereof; be guilty of a misdemeanor and shall be fined not more than $1,000 or imprisoned not more than one year, or both." Okla. Sess. Laws, 1939, c. 16, Art. 1, § 1, in effect at the time of petitioner's arrest, made it unlawful to import or cause to be imported into that state, without a permit, any intoxicating liquor containing more than 4 per cent of alcohol by volume.</p>
<p>[2]  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." U. S. Const. Amend. IV.</p>
<p>[3]  Neither the opinion of the Court of Appeals nor the unpublished opinion of the trial court refers to the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case.</p>
<p>[4]  "The Fourth Amendment does not denounce all searches or seizures, but only such as are unreasonable. . . . On reason and authority the true rule is that if the search and seizure without a warrant are made upon probable cause, that is, upon a belief, reasonably arising out of circumstances known to the seizing officer, that an automobile or other vehicle contains that which by law is subject to seizure and destruction, the search and seizure are valid." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#147" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 147, 149</a></span>.</p>
<p>[5]  The substantive offense charged in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> was violation of the National Prohibition Act, <span class="citation no-link">41 Stat. 305</span>; here, violation of the Liquor Enforcement Act of 1936.</p>
<p>[6]  In this case identification of the car as having been previously used by Brinegar in his liquor-running activities was inferential, although identification of its use by him in Joplin, Mo., his source of supply, was direct and undisputed.</p>
<p>[7]  The Government also stresses the fact, not present in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, of flight by Brinegar after he realized he was being pursued. We find it is unnecessary to take account of this factor in deciding this case. As to the factor of flight, see <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span>; <i>Talley</i> v. <i>United States,</i> <span class="citation" data-id="6894747"><a href="/opinion/6995964/talley-v-united-states/" aria-description="Citation for case: Talley v. United States">159 F. 2d 703</a></span>; <i>United States</i> v. <i>Heitner,</i> <span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/#107" aria-description="Citation for case: United States v. Heitner">149 F. 2d 105, 107</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="6885646"><a href="/opinion/6987410/jones-v-united-states/#541" aria-description="Citation for case: Jones v. United States">131 F. 2d 539, 541</a></span>; <i>Levine</i> v. <i>United States,</i> <span class="citation" data-id="6887471"><a href="/opinion/6989120/levine-v-united-states/#629" aria-description="Citation for case: Levine v. United States">138 F. 2d 627, 629</a></span>.</p>
<p>[8]  It was unlawful to import into Oklahoma, without a permit, any intoxicating liquor, as defined by the laws of that state, containing more than four per cent of alcohol by volume. See note 1 <i>supra.</i> Manufacture, sale, furnishing or transportation of intoxicating liquor was forbidden in Oklahoma. 37 Okla. Stat. § 1 (1941).</p>
<p>[9]  Indeed the showing here was stronger because there was no necessity, as there was in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, for resorting to judicial notice to establish either the probable source of supply or that it was illegal. On the present record judicial notice is hardly needed to give us cognizance of the differing laws of Missouri and Oklahoma, or of Joplin's proximity to the state line, and its ready convenience to one living as near by as Vinita who might be disposed to use it as a base of supply for importing liquor into Oklahoma in violation of the state and federal statutes.</p>
<p>[10]  As has been noted above, the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case is neither cited nor referred to in any of the opinions filed in the trial court and the Court of Appeals. Nor is there anything in the record before us showing that the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> decision was considered in any of the rulings made in the hearing on the motion to suppress, at the trial, or in the Court of Appeals.</p>
<p>[11]  The court however thought that, even with the fact of the arrest before it, the evidence was insufficient to show probable cause at the time Brinegar passed the police car.</p>
<p>[12]  The inappropriateness of applying the rules of evidence as a criterion to determine probable cause is apparent in the case of an application for a warrant before a magistrate, the context in which the issue of probable cause most frequently arises. The ordinary rules of evidence are generally not applied in <i>ex parte</i> proceedings, "partly because there is no opponent to invoke them, partly because the judge's determination is usually discretionary, partly because it is seldom final, but mainly because the system of Evidence rules was devised for the special control of trials by jury." 1 Wigmore, Evidence (3d ed., 1940) 19. See also Note, <span class="citation no-link">46 Harv. L. Rev. 1307</span>, 1310-1311.</p>
<p>[13]  But see, e. g., <i>Grau</i> v. <i>United States,</i> <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/#128" aria-description="Citation for case: Grau v. United States">287 U. S. 124, 128</a></span>, in which it was said by way of <i>dictum</i> that "A search warrant may issue only upon evidence which would be competent in the trial of the offense before a jury (<i>Giles</i> v. <i>United States,</i> <span class="citation" data-id="8827755"><a href="/opinion/8842552/giles-v-united-states/" aria-description="Citation for case: Giles v. United States">284 Fed. 208</a></span>; <i>Wagner</i> v. <i>United States,</i> 8 F. (2d) 581 . . . ." For this proposition there was no authority in the decisions of this Court. It was stated in a case in which the evidence adduced to prove probable cause was not incompetent, but was insufficient to support the inference necessary to the existence of probable cause. The statement has not been repeated by this Court.
</p>
<p>The <i>Wagner</i> case relies solely upon <i><span class="citation" data-id="8827755"><a href="/opinion/8842552/giles-v-united-states/" aria-description="Citation for case: Giles v. United States">Giles</a></span>,</i> the other case cited in <i><span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">Grau</a></span>,</i> and holds a warrant bad which issued on the basis of "hearsay and conclusions." The <i><span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">Grau</a></span></i> dictum occasionally has been applied or stated as dictum by the courts of appeals and district courts: <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="1479874"><a href="/opinion/1479874/simmons-v-united-states/#88" aria-description="Citation for case: Simmons v. United States">18 F. 2d 85, 88</a></span>; <i>Worthington</i> v. <i>United States,</i> <span class="citation" data-id="1475726"><a href="/opinion/1475726/worthington-v-united-states/#564" aria-description="Citation for case: Worthington v. United States">166 F. 2d 557, 564-565</a></span>; see also <i>Reeve</i> v. <i>Howe,</i> <span class="citation" data-id="1735465"><a href="/opinion/1735465/reeve-v-howe/#622" aria-description="Citation for case: Reeve v. Howe">33 F. Supp. 619, 622</a></span>; <i>United States</i> v. <i>Novero,</i> <span class="citation" data-id="1876453"><a href="/opinion/1876453/united-states-v-novero/#279" aria-description="Citation for case: United States v. Novero">58 F. Supp. 275, 279</a></span>. Cf. <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="1488414"><a href="/opinion/1488414/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">35 F. 2d 957</a></span>. See Note, <span class="citation no-link">46 Harv. L. Rev. 1307</span>, 1310-1311, for a criticism of the <i><span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">Grau</a></span></i> dictum. And see note 15, <i>infra,</i> and text.</p>
<p>[14]  Marshall's full statement in <i>Locke</i> v. <i>United States</i> was: "It may be added, that the term `probable cause,' according to its usual acceptation, means less than evidence which would justify condemnation; and, in all cases of seizure, has a fixed and well known meaning. It imports a seizure made under circumstances which warrant suspicion." <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span>.</p>
<p>[15]  To the same effect are: <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span>; <i>Dumbra</i> v. <i>United States,</i> <span class="citation" data-id="100685"><a href="/opinion/100685/dumbra-v-united-states/#441" aria-description="Citation for case: Dumbra v. United States">268 U. S. 435, 441</a></span>; <i>Steele</i> v. <i>United States No. 1,</i> <span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/#504" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498, 504-505</a></span>; <i>Stacey</i> v. <i>Emery,</i> <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span>.
</p>
<p>The <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> opinion also quotes with approval the following statement: "If the facts and circumstances before the officer are such as to warrant a man of prudence and caution in believing that the offense has been committed, it is sufficient." P. 161. Ascription of the statement to <i>Locke</i> v. <i>United States,</i> <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">7 Cranch 339</a></span>, appears to be an error in citation.</p>
<p>[16]  See the discussion of exceptions in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> opinion, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, 149 ff.</p>
<p>[17]  "It would be intolerable and unreasonable if a prohibition agent were authorized to stop every automobile on the chance of finding liquor and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in. But those lawfully within the country, entitled to use the public highways, have a right to free passage without interruption or search unless there is known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153-154</a></span>.</p>
<p>[1]  The <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case was based on the National Prohibition Act, <span class="citation no-link">41 Stat. 305</span>. Section 26 of that statute provided that when an officer discovered any person transporting liquor in violation of the law, in any vehicle, it was the officer's duty to seize the liquor, take possession of the vehicle, and arrest any person found in charge thereof. The officer was required to proceed at once against any such person but, if no one was found claiming the vehicle, it was to be sold after appropriate notice and the proceeds paid into the Treasury. Section 25 of the Act authorized search warrants for private dwellings but only if they were being used in the illicit liquor business.
</p>
<p>It had been proposed to amend the statute to forbid search of an automobile without warrant. After disagreement between the House and the Senate, that restriction was finally rejected. In the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case, the legislative history of this proposed (Stanley) amendment was considered at length. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 144</a></span>-146. The Court then concluded, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 147</a></span>, that, without the amendment, the Act "left the way open for searching an automobile . . . without a warrant, if the search was not malicious or without probable cause." And it stated the issue thus: "The intent of Congress to make a distinction between the necessity for a search warrant in the searching of private dwellings and in that of automobiles and other road vehicles is [<i>sic</i>] the enforcement of the Prohibition Act is thus clearly established by the legislative history of the Stanley Amendment. Is such a distinction consistent with the Fourth Amendment? . . ."</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Briscoe v. LaHue.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Briscoe v. LaHue
type: case
citation: "460 U.S. 325 (1983)"
parallel_cite: "103 S. Ct. 1108; 75 L. Ed. 2d 96; 51 U.S.L.W. 4247"
neutral_cite: 1983 U.S. LEXIS 146
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-03-07
docket: No. 81-1407
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
  opinion_url: "https://www.courtlistener.com/opinion/110885/briscoe-v-lahue/"
  cluster_id: 110885
  opinion_id: null
  identity_checked: true
lake:
  record_id: Briscoe v. LaHue
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Absolute Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Rehberg v. Paulk]]"
  - "[[Imbler v. Pachtman]]"
tags:
  - case
  - section-1983
  - witness-immunity
  - absolute-immunity
  - perjury
  - police-testimony
holding: "Police officers, like all other witnesses, are absolutely immune from § 1983 damages liability for testimony they give in a judicial proceeding, even if the testimony is alleged to be perjured, because at common law all participants integral to the judicial process enjoyed such immunity and § 1983 did not abrogate it."
aliases:
  - Briscoe v. LaHue
  - "Briscoe v. LaHue (1983)"
---

# Briscoe v. LaHue

*460 U.S. 325 (1983)* (No. 81-1407) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110885 → combined opinion 110885 (Stevens, J.; 460 U.S. 325, decided Mar. 7, 1983). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*336` follows the quoted sentence, placing it at 335). S9 promotes. -->

## Background
Several convicted defendants brought § 1983 damages suits against police officers who had testified against them at their criminal trials, alleging that the officers gave perjured testimony that helped secure the convictions. The Federal Magistrate and District Court dismissed the suits, and the Seventh Circuit affirmed on the ground that all witnesses — police officers as well as lay witnesses — are absolutely immune from civil liability for their testimony in judicial proceedings. Because the courts of appeals had divided on the question, the Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether a police officer who allegedly gives perjured testimony at a criminal trial may be sued for damages under § 1983 by the person convicted.

## Rule
The Court grounded the answer in the common-law immunity that shielded every participant in the judicial process, which Congress is presumed not to have silently abolished in enacting § 1983: "In short, the common law provided absolute immunity from subsequent damages liability for all persons — governmental or otherwise — who were integral parts of the judicial process." — 460 U.S. at 335. ^pin-335

## Application
A testifying police officer is either an ordinary witness — with the strong claim to witness immunity that any witness has — or an official performing a critical role in the proceeding, entitled to the same protection as other governmental participants. Either way, subjecting officers to § 1983 suits for their testimony would deter candid testimony, divert their energies from law enforcement, and let convicted defendants relitigate their trials as damages actions for perjury. The common-law immunity therefore covers police-officer witnesses no less than lay witnesses.

## Conclusion
The judgment was **affirmed**. Stevens, J., delivered the opinion of the Court; Marshall, J. (joined by Brennan and Blackmun, JJ.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Briscoe*'s trial-witness immunity was later extended to **grand jury** testimony — including that of a complaining or investigating officer — in *[[Rehberg v. Paulk]]* (2012). Teach its boundary carefully: the immunity attaches to *testimony*, not to a witness's separate, non-testimonial acts such as fabricating evidence (compare *[[Imbler v. Pachtman|Imbler]]* and *[[Buckley v. Fitzsimmons]]*, where investigative fabrication drew only [[Qualified Immunity|qualified immunity]]).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Briscoe v. LaHue*, 460 U.S. 325 (1983)](https://www.courtlistener.com/opinion/110885/briscoe-v-lahue/) — pinpoint: 335 (Stevens, J., for the Court; the CL opinion text places the reporter star `*336` immediately after the quoted sentence, fixing it on 335). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "40c1b8c9a5edb6a9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Briscoe v. LaHue"}, "payload": {"all": [{"cite": "460 U.S. 325", "page": "325", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "460"}, {"cite": "103 S. Ct. 1108", "page": "1108", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "75 L. Ed. 2d 96", "page": "96", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "75"}, {"cite": "1983 U.S. LEXIS 146", "page": "146", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4247", "page": "4247", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "460 U.S. 325", "official": {"cite": "460 U.S. 325", "page": "325", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "460"}, "official_selection_present": true, "record_id": "Briscoe v. LaHue"}}
{"assertion_id": "99024949c9ce43fe", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Briscoe v. LaHue"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Briscoe v. LaHue", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Briscoe v. LaHue

```json
{
  "schema_version": "s2.v1",
  "record_id": "Briscoe v. LaHue",
  "status": "under_review",
  "identity": {
    "case_name": "Briscoe v. LaHue",
    "case_name_short": "Briscoe",
    "case_name_full": "BRISCOE Et Al. v. LaHUE Et Al.",
    "input_case_name": "Briscoe v. LaHue",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-03-07",
    "year": 1983,
    "docket": "No. 81-1407",
    "cluster_id": 110885,
    "lead_opinion_id": 9429107,
    "sibling_ids": [],
    "absolute_url": "/opinion/110885/briscoe-v-lahue/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "460 U.S. 325",
      "volume": "460",
      "reporter": "U.S.",
      "page": "325",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1108",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1108",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 96",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "96",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4247",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4247",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 146",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "146",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "460 U.S. 325",
        "volume": "460",
        "reporter": "U.S.",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1108",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1108",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 96",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "96",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 146",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "146",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4247",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4247",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "460 U.S. 325",
    "official_selection": {
      "court_class": "scotus",
      "selected": "460 U.S. 325",
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
    "date_created": "2026-07-06T13:47:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "briscoe-v-lahue--110885",
      "to_record_id": "Briscoe v. LaHue",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Briscoe v. LaHue

```
<opinion type="majority">
<author id="b388-10">Justice Stevens</author>
<p id="A1K">delivered the opinion of the Court.</p>
<p id="b388-11">This case presents a question of statutory construction: whether <span class="citation no-link">42 U. S. C. §1983</span> (1976 ed., Supp. V) authorizes a convicted person to assert a claim for damages against a police officer for giving perjured testimony at his criminal trial. The Court of Appeals for the Seventh Circuit held that witnesses are absolutely immune from damages liability based on their testimony, and rejected the petitioners’ contention that government officials who testify about the performance of their official duties may be held liable under § 1983 even if other witnesses may not. We agree with that conclusion.</p>
<p id="b388-12">The Court of Appeals heard argument in three separate cases raising the absolute immunity issue and decided them in a single opinion. Two of these cases are before us on a writ of certiorari. Petitioner Briscoe was convicted in state court of burglarizing a house trailer. He then filed a § 1983 complaint against respondent LaHue, a member of the Bloo-mington, Indiana, police force, alleging that LaHue had violated his constitutional right to due process by committing perjury in the criminal proceedings leading to his conviction.<footnotemark>1</footnotemark> <page-number citation-index="1" label="327">*327</page-number>LaHue had testified that in his opinion Briscoe was one of no more than 50 to 100 people in Bloomington whose prints would match a partial thumbprint on a piece of glass found at the scene of the crime. According to Briscoe, the testimony was false because the Federal Bureau of Investigation and the state police considered the partial print too incomplete to be of value, and without the print there was no evidence identifying him as the burglar. He sought $100,000 in damages. The District Court granted LaHue’s motion for summary judgment on four separate grounds: (1) the facts alleged in the complaint did not suggest that LaHue had testified falsely; (2) allegations of perjury alone are insufficient to state a constitutional claim; (3) LaHue had not testified “under color of law”; and (4) Briscoe’s claim was collaterally estopped by his criminal conviction.</p>
<p id="b389-5">Petitioners Vickers and Ballard were jointly tried and convicted of sexual assault in state court. They subsequently brought a civil action under § 1983 against respondent Hun-ley, a member of the Cedar Lake, Indiana, police force, alleging that he had deprived them of their constitutional rights to due process and a fair trial. They alleged that, by giving false testimony suggesting that they had been able to harmonize their stories before making exculpatory statements to police, he had prejudicially diminished the credibility of those statements. Each plaintiff sought $150,000 in compensatory and $50,000 in punitive damages. The Federal Magistrate granted a motion to dismiss the complaint on alternative grounds: (1) Hunley had not testified “under color of law”; (2) he was entitled to absolute witness immunity; and (3) peti- - tioners had failed to state a claim under § 1983 because they did not allege that the prosecutor had knowingly used false testimony. The District Court affirmed the dismissal on the first ground. Both cases were appealed to the United States Court of Appeals for the Seventh Circuit.<footnotemark>2</footnotemark></p>
<p id="b390-4"><page-number citation-index="1" label="328">*328</page-number>Although other issues were argued in the Court of Appeals, its holding in both cases was predicated squarely on the ground that, in litigation brought under <span class="citation no-link">42 U. S. C. §1983</span> (1976 ed., Supp. V), all witnesses — police officers as well as lay witnesses — are absolutely immune from civil liability based on their testimony in judicial proceedings. <span class="citation multiple-matches"><a href="/c/F.%202d/663/713/">663 F. 2d 713</a></span> (1981).<footnotemark>3</footnotemark> Because of the importance of the immunity question, which has given rise to divergent conclusions in the Courts of Appeals,<footnotemark>4</footnotemark> we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./455/1016/">455 U. S. 1016</a></span> (1982).<footnotemark>5</footnotemark></p>
<p id="b391-4"><page-number citation-index="1" label="329">*329</page-number>Before confronting the precise question that this case presents — whether § 1983 creates a damages remedy against police officers for their testimony as witnesses — we begin by considering the potential liability of lay witnesses on the one hand, and of judges and prosecutors who perform integral functions in judicial proceedings on the other hand. The unavailability of a damages remedy against both of these categories sheds considerable light on petitioners’ claim that Congress intended police officer witnesses to be treated differently.</p>
<p id="b391-5">I</p>
<p id="b391-6">There are two reasons why § 1983 does not allow recovery of damages against a private party for testimony in a judicial proceeding. First, § 1983 does not create a remedy for all conduct that may result in violation of “rights, privileges, or immunities secured by the Constitution and laws.” Its reach is limited to actions taken “under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory . . . .”<footnotemark>6</footnotemark> It is beyond question that, when a private <page-number citation-index="1" label="330">*330</page-number>party gives testimony in open court in a criminal trial, that act is not performed “under color of law.”<footnotemark>7</footnotemark></p>
<p id="b392-5">Second, since 1951, when this Court decided <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367</a></span>, it has been settled that the all-encompassing language of § 1983, referring to “[e]very person” who, under color of law, deprives another of federal constitutional or statutory rights, is not to be taken literally.<footnotemark>8</footnotemark></p>
<blockquote id="b392-6">“It is by now well settled that the tort liability created by § 1983 cannot be understood in a historical vacuum. . . . One important assumption underlying the Court’s decisions in this area is that members of the 42d Congress were familiar with common-law principles, including defenses previously recognized in ordinary tort litigation, and that they likely intended these common-law principles to obtain, absent specific provisions to the contrary.” <em>City of Newport </em>v. <em>Fact Concerts, Inc., </em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/#258" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247, 258</a></span> (1981).</blockquote>
<p id="b392-7">See <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 554</a></span> (1967).</p>
<p id="b392-8">The immunity of parties and witnesses from subsequent damages liability for their testimony in judicial proceedings<footnotemark>9</footnotemark> <page-number citation-index="1" label="331">*331</page-number>was well established in English common law. <em>Cutler </em>v. <em>Dixon, 4 </em>Co. Rep. 14b, 76 Eng. Rep. 886 (Q. B. 1585); <em>Anfield </em>v. <em>Feverhill, </em>2 Bulst. 269, 80 Eng. Rep. 1113 (K. B. 1614); <em>Henderson </em>v. <em>Broomhead, </em>4 H. &amp; N. 569, 578, 157 Eng. Rep. 964, 968 (Ex. 1859);<footnotemark>10</footnotemark> see <em>Dawkins </em>v. <em>Lord Rokeby, </em>4 F. &amp; F. 806, 833-834, 176 Eng. Rep. 800, 812 (C. P. 1866). Some American decisions required a showing that the witness’ allegedly defamatory statements were relevant to the judicial proceeding, but once this threshold showing had been made, the witness had an absolute privilege.<footnotemark>11</footnotemark> The <page-number citation-index="1" label="332">*332</page-number>plaintiff could not recover even if the witness knew the statements were false and made them with malice.<footnotemark>12</footnotemark></p>
<p id="b394-5">In the words of one 19th-century court, in damages suits against witnesses, “the claims of the individual must yield to <page-number citation-index="1" label="333">*333</page-number>the dictates of public policy, which requires that the paths which lead to the ascertainment of truth should be left as free and unobstructed as possible.” <em>Calkins </em>v. <em>Sumner, </em><span class="citation" data-id="6598323"><a href="/opinion/6717522/calkins-v-sumner/#197" aria-description="Citation for case: Calkins v. Sumner">13 Wis. 193, 197</a></span> (1860). A witness’ apprehension of subsequent damages liability might induce two forms of self-censorship. First, witnesses might be reluctant to come forward to testify. See <em>Henderson </em>v. <em>Broomhead, supra, </em>at 578-579, 157 Eng. Rep., at 968. And once a witness is on the stand, his testimony might be distorted by the fear of subsequent liability. See <em>Barnes </em>v. <em>McCrate, </em><span class="citation" data-id="4928856"><a href="/opinion/5110328/barnes-v-mccrate/#446" aria-description="Citation for case: Barnes v. McCrate">32 Me. 442, 446-447</a></span> (1851). Even within the constraints of the witness’ oath there may be various ways to give an account or to state an opinion. These alternatives may be more or less detailed and may differ in emphasis and certainty. A witness who knows that he might be forced to defend a subsequent lawsuit, and perhaps to pay damages, might be inclined to shade his testimony in favor of the potential plaintiff, to magnify uncertainties, and thus to deprive the finder of fact of candid, objective, and undistorted evidence. See Veeder, Absolute Immunity in Defamation: Judicial Proceedings, <span class="citation no-link">9 Colum. L. Rev. 463</span>, 470 (1909).<footnotemark>13</footnotemark> But the truthfinding process is better <page-number citation-index="1" label="334">*334</page-number>served if the witness’ testimony is submitted to “the crucible of the judicial process so that the factfinder may consider it, after cross-examination, together with the other evidence in the case to determine where the truth lies.” <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#440" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 440</a></span> (1976) (White, J., concurring in judgment).<footnotemark>14</footnotemark></p>
<p id="b396-5">At least with respect to private witnesses, it is clear that §1983 did not abrogate the absolute immunity existing at common law, and petitioners do not contend otherwise. Like the immunity for legislators at issue in <em>Tenney </em>v. <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Brandhove</a></span>, </em>the common law’s protection for witnesses is “a tradition so well grounded in history and reason” that we cannot believe that Congress impinged on it “by covert inclusion in the general language before us.” <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S., at 376</a></span>.</p>
<p id="b396-6">II</p>
<p id="b396-7">The Court has already addressed the question whether § 1983 permits damages recoveries from judges, prosecutors, and other persons acting “under color of law” who perform official functions in the judicial process. Again, we have found that, in light of common-law immunity principles, § 1983 did not impose liability on these officials. We have held that state judges are absolutely immune from liability for their judicial acts, <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967); <em>Stump </em>v. <em>Sparkman, </em><span class="citation" data-id="9427113"><a href="/opinion/109820/stump-v-sparkman/" aria-description="Citation for case: Stump v. Sparkman">435 U. S. 349</a></span> (1978), and that state prosecutors have absolute immunity from liability for their actions in initiating prosecutions, <em>Imbler </em>v. <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Pachtman, supra.</a></span></em></p>
<p id="b396-8">The central focus of our analysis has been the nature of the judicial proceeding itself. Thus, in his opinion concurring in the judgment in <em>Imbler </em>v. <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Pachtman, supra,</a></span> </em>Justice White explained that the absolute immunity of public prosecutors was “based on the policy of protecting the judicial process.” <page-number citation-index="1" label="335">*335</page-number><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#439" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 439</a></span>. He explained that this protection extended equally to other participants, including counsel and witnesses.</p>
<blockquote id="b397-5">“The reasons for this rule are also substantial. It is precisely the function of a judicial proceeding to determine where the truth lies. The ability of courts, under carefully developed procedures, to separate truth from falsity, and the importance of accurately resolving factual disputes in criminal (and civil) cases are such that those involved in judicial proceedings should be ‘given every encouragement to make a full disclosure of all pertinent information within their knowledge.’” <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Ibid.</a></span></em></blockquote>
<p id="b397-6">The common law’s protection for judges and prosecutors formed part of a “cluster of immunities protecting the various participants in judge-supervised trials,” which stemmed “from the characteristics of the judicial process.” <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#512" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 512</a></span> (1978); cf. <em>King </em>v. <em>Skinner, </em>Lofft 54, 56, 98 Eng. Rep. 529 (K. B. 1772) (“[NJeither party, witness, counsel, jury, or judge can be put to answer, civilly or criminally, for words spoken in office”). The common law recognized that</p>
<blockquote id="b397-7">“controversies sufficiently intense to erupt in litigation are not easily capped by a judicial decree. The loser in one forum will frequently seek another .... Absolute immunity is thus necessary to assure that judges, advocates, and witnesses can perform their respective functions without harassment or intimidation.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#512" aria-description="Citation for case: Butz v. Economou"><em>Butz, supra, </em>at 512</a></span>.</blockquote>
<p id="b397-8">In short, the common law provided absolute immunity from subsequent damages liability for all persons — governmental or otherwise — who were integral parts of the judicial process. It is equally clear that § 1983 does not authorize a damages claim against private witnesses on the one hand, or against judges or prosecutors in the performance of their respective duties on the other. When a police officer appears as a witness, he may reasonably be viewed as acting like any <page-number citation-index="1" label="336">*336</page-number>other witness sworn to tell the truth — in which event he can make a strong claim to witness immunity;<footnotemark>16</footnotemark> alternatively, he may be regarded as an official performing a critical role in the judicial process, in which event he may seek the benefit afforded to other governmental participants in the same proceeding. Nothing in the language of the statute suggests that such a witness belongs in a narrow, special category lacking protection against damages suits. We must ask, however, whether anything in the legislative history of § 1983 points to a different conclusion.</p>
<p id="b398-9">I — I HH h-H</p>
<p id="b398-3">Petitioners point to a number of references throughout the debates on the 1871 Act to widespread perjury by Ku Klux Klan witnesses in state criminal trials.<footnotemark>15</footnotemark> They urge that, because perjury was one of the specific evils with which Congress was concerned, recognizing an absolute immunity for witnesses would conflict with congressional intent. We find this argument unpersuasive. The Act consisted of several sections establishing different remedies for disorder and violence in the Southern States.<footnotemark>17</footnotemark> The legislative history and statutory language indicate that Congress intended perjury <page-number citation-index="1" label="337">*337</page-number>leading to unjust acquittals of Klan conspirators to be prohibited by §2, the civil and criminal conspiracy section of the statute, now codified in relevant part at <span class="citation no-link">42 U. S. C. § 1985</span>(3) (1976 ed., Supp. V) and <span class="citation no-link">18 U. S. C. §241</span>. But the language of §1 — now codified as §1983 — differs from that of §2 in essential respects, and we find no evidence that Congress intended to abrogate the traditional common-law witness immunity in §1983 actions.</p>
<p id="b399-5">The Ku Klux Act, <span class="citation no-link">17 Stat. 13</span>, was enacted on April 20, 1871, less than a month after President Grant sent a dramatic message to Congress describing the breakdown of law and order in the Southern States. Cong. Globe, 42d Cong., 1st Sess., 236, 244 (1871). During the debates, supporters of the bill repeatedly described the reign of terror imposed by the Klan upon black citizens and their white sympathizers in the Southern States. Hours of oratory were devoted to the details of Klan outrages — arson, robbery, whippings, shootings, murders, and other forms of violence and intimidation— often committed in disguise and under cover of night. These acts of lawlessness went unpunished, legislators asserted, because Klan members and sympathizers controlled or influenced the administration of state criminal justice. In particular, it was alleged that Klan members were obligated, by virtue of membership in the organization, to protect fellow members who were charged with criminal activity. They had a duty to offer themselves for service on grand and petit juries, and to violate their jurors’ oaths by refusing to indict or to convict regardless of the strength of the evidence. They also were bound to appear as witnesses, and again to violate their oaths by committing perjury, if necessary, to exculpate their Klan colleagues.<footnotemark>18</footnotemark> Perjury was thus one of the <page-number citation-index="1" label="338">*338</page-number>means by which the Klan prevented state courts from gaining convictions of Klan members for crimes against blacks and Republicans.</p>
<p id="b400-5">It is clear from the legislative debates that, in the view of the Act’s sponsors, the victims of Klan outrages were deprived of “equal protection of the laws” if the perpetrators systematically went unpunished.<footnotemark>19</footnotemark> Proponents of the measure repeatedly argued that, given the ineffectiveness of state law enforcement and the individual’s federal right to “equal protection of the laws,” an independent federal remedy was necessary and Congress had the power to provide it.<footnotemark>20</footnotemark> See <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#174" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167, 174</a></span> (1961).</p>
<p id="b400-6">Section 2 was designed specifically to provide criminal and civil remedies in federal court for the conspiratorial activities of the Klan. Indeed the provision singles out those who “go in disguise upon the public highway.” Earlier versions of the section enumerated precisely the activities that had been attributed to the Klan — murder, manslaughter, mayhem, robbery, assault and battery, perjury, subornation of perjury, criminal obstruction of legal process or resistance of of-<page-number citation-index="1" label="339">*339</page-number>fleers in discharge of official duty, arson, or larceny. Cong. Globe, <em>supra, </em>at 317. The more general language in the final version of § 2 was also intended to apply to the abuses that had been described repeatedly in congressional debate.<footnotemark>21</footnotemark> Part of the provision is particularly well tailored to reach conspiracies to commit perjury in order to prevent punishment of fellow Klansmen. It provides penalties whenever two or more persons shall</p>
<blockquote id="b401-5">“conspire together ... for the purpose of preventing or hindering the constituted authorities of any State from giving or securing to all persons within such State the equal protection of the laws, or shall conspire together for the purpose of in any manner impeding, hindering, obstructing, or defeating the due course of justice in any State or Territory, with intent to deny to any citizen of the United States the due and equal protection of the laws <em>. . . ,”</em><footnotemark><em>22</em></footnotemark></blockquote>
<p id="b401-6">This evidence does not, however, tend to show that Congress intended to abrogate witness immunity in civil actions under § 1, which applied to wrongs committed “under color of . . . law.” The bill’s proponents were exclusively concerned with perjury resulting in unjust <em>acquittals </em>— perjury likely to be committed by private parties acting in furtherance of a conspiracy — and not with perjury committed “under color of <page-number citation-index="1" label="340">*340</page-number>law” that might lead to unjust <em>convictions. </em>In hundreds of pages of debate there is no reference to the type of alleged constitutional deprivation at issue in this case: perjury by a <em>government official </em>leading to an unjust conviction. Indeed, the legislative history is virtually silent even with regard to perjury by <em>private </em>persons leading to convictions of innocent defendants.<footnotemark>23</footnotemark> There is a simple enough reason for this lacuna: the Klan had other, more direct, means of dealing with its victims. A “reign of terrorism and bloodshed” did not require the formal processes of law; at most, drumhead tribunals were convened at dead of night.<footnotemark>24</footnotemark> Even when the organization’s intended victims had been taken into custody and charged with crimes, the evidence before Congress suggested that the Klan resorted to vigilante justice rather than courtroom perjury.<footnotemark>25</footnotemark></p>
<p id="b402-5">In summary, the legislative history supports criminal punishment under §2 for a witness who conspired to give perjured testimony favorable to a defendant, with the effect of preventing effective enforcement of the laws, and liability in a civil suit against the perjured witness by the defendant’s victim. But these are not the issues before us today. We are asked to extrapolate from pro-defendant perjury to pro-prosecution perjury, and if willing to make that step, we are further invited to apply legislative history relating to § 2 — a section specifically directed toward private conspiracies — to § 1 — a section designed to provide remedies for abuses under <page-number citation-index="1" label="341">*341</page-number>color of law. We decline the invitation. The debates of the 42d Congress do not support petitioners’ contention that Congress intended to provide a § 1 damages remedy against police officers or any other witnesses.<footnotemark>26</footnotemark></p>
<p id="b403-9">I — I C</p>
<p id="b403-3">Petitioners, finally, urge that we should carve out an exception to the general rule of immunity in cases of alleged perjury by police officer witnesses.<footnotemark>27</footnotemark> They assert that the reasons supporting common-law immunity — the need to <page-number citation-index="1" label="342">*342</page-number>avoid intimidation and self-censorship — apply with diminished force to police officers. Policemen often have a duty to testify about the products of their investigations, and they have a professional interest in obtaining convictions which would assertedly counterbalance any tendency to shade testimony in favor of potentially vindictive defendants. In addition, they are subject to § 1983 lawsuits for the performance of their other duties, as to which they have only qualified immunity, and their defense is generally undertaken by their governmental employers. Further, petitioners urge that perjured testimony by police officers is likely to be more damaging to constitutional rights than such testimony by ordinary citizens, because the policeman in uniform carries special credibility in the eyes of jurors. And, in the case of police officers, who cooperate regularly with prosecutors in the enforcement of criminal law, prosecution for perjury is alleged to be so unlikely that it is not an effective substitute for civil damages.</p>
<p id="b404-5">These contentions have some force. But our cases clearly indicate that immunity analysis rests on functional categories, not on the status of the defendant.<footnotemark>28</footnotemark> A police officer on the witness stand performs the same functions as any other witness; he is subject to compulsory process, takes an oath, responds to questions on direct examination and cross-examination, and may be prosecuted subsequently for perjury.</p>
<p id="b404-6">Moreover, to the extent that traditional reasons for witness immunity are less applicable to governmental witnesses, <page-number citation-index="1" label="343">*343</page-number>other considerations of public policy support absolute immunity more emphatically for such persons than for ordinary witnesses. Subjecting government officials, such as police officers, to damages liability under § 1983 for their testimony might undermine not only their contribution to the judicial process but also the effective performance of their other public duties.</p>
<p id="b405-5">Section 1983 lawsuits against police officer witnesses, like lawsuits against prosecutors, “could be expected with some frequency.” Cf. <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#425" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 425</a></span>. Police officers testify in scores of cases every year, and defendants often will transform resentment at being convicted into allegations of perjury by the State’s official witnesses. As the files in this case show, even the processing of a complaint that is dismissed before trial consumes a considerable amount of time and resources.<footnotemark>29</footnotemark></p>
<p id="b405-6">This category of § 1983 litigation might well impose significant burdens on the judicial system and on law enforcement resources. As this Court noted when it recognized absolute immunity for prosecutors in <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span>, </em>if the defendant official “could be made to answer in court each time [a disgruntled defendant] charged him with wrongdoing, his energy and at<page-number citation-index="1" label="344">*344</page-number>tention would be diverted from the pressing duty of enforcing the criminal law.” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#425" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 425</a></span>. To some degree the individual’s burden might be alleviated by the government’s provision of counsel, but a case that goes to trial always imposes significant emotional and other costs on every party litigant.</p>
<p id="b406-5">It is not sufficient to assert that the burdens on defendants and the courts could be alleviated by limiting the cause of action to those former criminal defendants who have already vindicated themselves in another forum, either on appeal or by collateral attack. We rejected a similar contention in <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span>. </em>Petitioner contended that “his suit should be allowed, even if others would not be, because the District Court’s issuance of the writ of habeas corpus shows that his suit has substance.” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#428" aria-description="Citation for case: Imbler v. Pachtman"><em>Id., </em>at 428, n. 27</a></span>. We declined to carve out such an exception to prosecutorial immunity, noting that petitioner’s success in a collateral proceeding did not necessarily establish the merits of his civil rights action. Moreover, we noted that “using the habeas proceeding as a ‘door-opener’ for a subsequent civil rights action would create the risk of injecting extraneous concerns into that proceeding.” <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Ibid.</a></span> </em>We emphasized that, in determining whether to grant postconviction relief, the tribunal should focus solely on whether there was a fair trial under law. “This focus should not be blurred by even the subconscious knowledge that a post-trial decision in favor of the accused might result in the prosecutor’s being called upon to respond in damages for his error or mistaken judgment.” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#427" aria-description="Citation for case: Imbler v. Pachtman"><em>Id., </em>at 427</a></span>. The same danger exists in the case of potential liability for police officer witnesses.<footnotemark>30</footnotemark></p>
<p id="b407-4"><page-number citation-index="1" label="345">*345</page-number>There is, of course, the possibility that, despite the truth-finding safeguards of the judicial process, some defendants might indeed be unjustly convicted on the basis of knowingly false testimony by police officers.<footnotemark>31</footnotemark> The absolute immunity for prosecutors recognized in <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span> </em>bars one possible avenue of redress for such defendants. Similarly, in this case, the absolute witness immunity bars another possible path to recovery for these defendants. But we have recognized, again and again, that in some situations, the alternative of limiting the official’s immunity would disserve the broader public interest. As Judge Learned Hand wrote years ago:</p>
<blockquote id="b407-5">“As is so often the case, the answer must be found in a balance between the evils inevitable in either alternative. In this instance it has been thought in the end better to leave unredressed the wrongs done by dishonest officers than to subject those who try to do their duty to the constant dread of retaliation.” <em>Gregoire </em>v. <span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/#581" aria-description="Citation for case: Gregoire v. Biddle"><em>Biddle, 177 </em>F. 2d 579, 581</a></span> (CA2 1949), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./339/949/">339 U. S. 949</a></span> (1950).<footnotemark>32</footnotemark></blockquote>
<p id="b407-6">In short, the rationale of our prior absolute immunity cases governs the disposition of this case. In 1871, common-law immunity for witnesses was well settled. The principles set forth in <em>Pierson </em>v. <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Ray</a></span> </em>to protect judges and in <em>Imbler </em>v. <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Pachtman</a></span> </em>to protect prosecutors also apply to witnesses, who perform a somewhat different function in the trial process but whose participation in bringing the litigation to a <page-number citation-index="1" label="346">*346</page-number>just — or possibly unjust — conclusion is equally indispensable. The decision of the Court of Appeals is affirmed.</p>
<p id="b408-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b388-13"> The Court has held that the prosecutor’s knowing use of perjured testimony violates due process, but has not held that the false testimony of a police officer in itself violates constitutional rights. See <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 103</a></span>, and nn. 8, 9 (1976) (citing cases).</p>
</footnote>
<footnote label="2">
<p id="b389-6"> At the time of the Court of Appeals’ decision, petitioner Briscoe’s conviction had been set aside by the Indiana Court of Appeals on the ground that the evidence was insufficient to prove Briscoe’s guilt beyond a reason<page-number citation-index="1" label="328">*328</page-number>able doubt. The opinion did not question the veracity of LaHue’s testimony, but found that the State’s evidence, including testimony that Briscoe was one of 50 to 100 persons who might have robbed the trailer, did not meet the State’s burden of proof. <em>Briscoe </em>v. <em>State, </em><span class="citation" data-id="2069769"><a href="/opinion/2069769/briscoe-v-state/#460" aria-description="Citation for case: Briscoe v. State">180 Ind. App. 450, 460</a></span>, <span class="citation" data-id="2069769"><a href="/opinion/2069769/briscoe-v-state/#644" aria-description="Citation for case: Briscoe v. State">388 N. E. 2d 638, 644</a></span> (1979). Petitioners Vickers and Ballard were still serving their sentences when the Court of Appeals affirmed the dismissal of their complaint.</p>
</footnote>
<footnote label="3">
<p id="b390-7"> On review of pretrial orders dismissing petitioners’ complaints, the Court of Appeals assumed that the complaints’ factual allegations of perjury were true. It also assumed that petitioners had alleged a constitutional violation — that they had been deprived of their liberty without due process of law by respondents’ perjury in the judicial proceedings that resulted in their convictions. Because we granted certiorari to review the Court of Appeals’ holding, we make the same assumptions for purposes of deciding this case, without implying that they are valid. In light of its resolution of the immunity question the Court of Appeals did not determine whether the respondents had acted “under color of law,” though it suggested that it might have answered in the affirmative. 663 F. 2d, at 721, n. 4.</p>
</footnote>
<footnote label="4">
<p id="b390-8"><em> A </em>rule of absolute witness immunity has been adopted by the majority of Courts of Appeals. <em>Brawer </em>v. <em>Horowitz, </em><span class="citation" data-id="8899121"><a href="/opinion/8911357/brawer-v-horowitz/#836" aria-description="Citation for case: Brawer v. Horowitz">535 F. 2d 830, 836-837</a></span> (CA3 1976) (lay witness in federal court; <em>Bivens </em>action); <em>Burke </em>v. <em>Miller, </em><span class="citation" data-id="9464949"><a href="/opinion/358165/herman-k-burke-v-jerry-miller-md/" aria-description="Citation for case: Herman K. Burke v. Jerry Miller, M.D.">580 F. 2d 108</a></span> (CA4 1978) (state medical examiner; § 1983 action), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./440/930/">440 U. S. 930</a></span> (1979); <em>Charles </em>v. <em>Wade, </em><span class="citation" data-id="9468664"><a href="/opinion/397403/earl-charles-v-f-w-wade-leo-b-ryan-and-city-of-savannah-georgia/" aria-description="Citation for case: Earl Charles v. F. W. Wade, Leo B. Ryan and City of...">665 F. 2d 661</a></span> (CA5 1982) (police officer victim; § 1983 suit), cert. pending, No. 81-1881; <em>Myers </em>v. <em>Bull, </em><span class="citation" data-id="366607"><a href="/opinion/366607/philip-d-myers-v-clyde-harold-bull/#866" aria-description="Citation for case: Philip D. Myers v. Clyde Harold Bull">599 F. 2d 863, 866</a></span> (CA8) (police officer witness; § 1983 suit), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/901/">444 U. S. 901</a></span> (1979); <em>Blevins </em>v. <em>Ford, </em><span class="citation" data-id="354155"><a href="/opinion/354155/robert-lee-blevins-v-john-ford-iii-and-john-mitchell-robert-lee-blevins/" aria-description="Citation for case: Robert Lee Blevins v. John Ford, III and John Mitchell,...">572 F. 2d 1336</a></span> (CA9 1978) (private witnesses and former Assistant U. S. Attorney; action under § 1983 and the Fifth Amendment). But see <em>Briggs </em>v. <em>Goodwin, </em>186 U. S. App. D. C. 179, <span class="citation multiple-matches"><a href="/c/F.%202d/569/10/">569 F. 2d 10</a></span> (1977) (dicta rejecting absolute immunity for government <page-number citation-index="1" label="329">*329</page-number>official witness; <em>Bivens </em>action), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./437/904/">437 U. S. 904</a></span> (1978); <em>Hilliard </em>v. <em>Williams, </em><span class="citation" data-id="327967"><a href="/opinion/327967/lilly-mae-onie-lee-whitelaw-hilliard-v-john-l-williams-and-donn-clark/#1350" aria-description="Citation for case: Lilly Mae Onie Lee Whitelaw Hilliard v. John L. Williams...">516 F. 2d 1344, 1350</a></span> (CA6 1975) (rejecting absolute immunity for agent of state bureau of investigation; § 1983 action), cert. denied <em>sub nom. Clark </em>v. <em>Hilliard, </em><span class="citation" data-id="8998975"><a href="/opinion/9006257/clark-v-hilliard/" aria-description="Citation for case: Clark v. Hilliard">423 U. S. 1066</a></span> (1976).</p>
</footnote>
<footnote label="5">
<p id="b391-11"> The petition for writ of certiorari presents the following question: “Whether a police officer who commits perjury during a state court criminal trial should be granted absolute immunity from civil liability under <span class="citation no-link">42 U. S. C. § 1983</span>.” Pet. for Cert. i. The petition does not raise the question of immunity for testimony at pretrial proceedings such as probable-cause hearings, nor does petitioners’ brief discuss whether the same immunity considerations that apply to trial testimony also apply to testimony at probable-cause hearings. We therefore do not decide whether respondent LaHue is entitled to absolute immunity for allegedly false testimony at two probable-cause hearings regarding petitioner Briscoe.</p>
</footnote>
<footnote label="6">
<p id="b391-12"> Thus, even though the defective performance of defense counsel may cause the trial process to deprive an accused person of his liberty in an unconstitutional manner, <em>Cuyler </em>v. <em>Sullivan, </em><span class="citation" data-id="9427906"><a href="/opinion/110256/cuyler-v-sullivan/#342" aria-description="Citation for case: Cuyler v. Sullivan">446 U. S. 335, 342-345</a></span> (1980), the lawyer who may be responsible for the unconstitutional state action <page-number citation-index="1" label="330">*330</page-number>does not himself act under color of state law within the meaning of § 1983. <em>Polk County </em>v. <em>Dodson, </em><span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/" aria-description="Citation for case: Polk County v. Dodson">454 U. S. 312</a></span> (1981). This conclusion is compelled by the character of the office performed by defense counsel. See <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/#317" aria-description="Citation for case: Polk County v. Dodson"><em>id., </em>at 317-319</a></span>; <em>Ferri </em>v. <em>Ackerman, </em><span class="citation" data-id="110162"><a href="/opinion/110162/ferri-v-ackerman/#204" aria-description="Citation for case: Ferri v. Ackerman">444 U. S. 193, 204</a></span> (1979). It is equally clear that the office of the lay witness who merely discharges his duty to testify truthfully is not performed under color of law within the meaning of § 1983.</p>
</footnote>
<footnote label="7">
<p id="b392-15"> It is conceivable, however, that nongovernmental witnesses could act “under color of law” by conspiring with the prosecutor or other state officials. See <em>Dennis </em>v. <em>Sparks, </em><span class="citation" data-id="110353"><a href="/opinion/110353/dennis-v-sparks/#27" aria-description="Citation for case: Dennis v. Sparks">449 U. S. 24, 27-29</a></span> (1980); <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#152" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 152</a></span> (1970). It is therefore necessary to go beyond the “color of law” analysis to consider whether private witnesses may ever be held liable for damages under § 1983.</p>
</footnote>
<footnote label="8">
<p id="b392-16"> Nor is this the only piece of 19th-century legislation in which the word “every” may not be given a literal reading. See <em>National Society of Professional Engineers </em>v. <em>United States, </em><span class="citation" data-id="9427139"><a href="/opinion/109833/national-society-of-professional-engineers-v-united-states/#687" aria-description="Citation for case: National Society of Professional Engineers v. United States">435 U. S. 679, 687-688</a></span> (1978).</p>
</footnote>
<footnote label="9">
<p id="b392-17"> The availability of a common-law action for false accusations of crime, see <em>post, </em>at 350-351, is inapposite because petitioners present only the <page-number citation-index="1" label="331">*331</page-number>question of § 1983 liability for false testimony during a state-court criminal trial. See n. 5, <em>supra.</em></p>
</footnote>
<footnote label="10">
<p id="b393-6"> “We have therefore a large collection of cases where from time to time parties have attempted to get damages in cases like the present, but in no one instance has the action ever been held to be maintainable. If for centuries many persons have attempted to get a remedy for injuries like the present, and there is an entire absence of authority that such remedy exists, it shews the unanimous opinion of those who have held the place which we do now, that such an action is not maintainable.” <em>Henderson </em>v. <em>Broomhead, </em>4 H. &amp; N., at 578, 157 Eng. Rep., at 968.</p>
</footnote>
<footnote label="11">
<p id="b393-7"> See generally M. Newell, Law of Defamation, Libel and Slander 425, 450-459 (1890); J. Townshend, A Treatise on the Wrongs Called Slander and Libel 353-354 (2d ed. 1872). See, <em>e. g., Lawson </em>v. <em>Hicks, </em><span class="citation" data-id="6507029"><a href="/opinion/6630579/lawson-v-hicks/#285" aria-description="Citation for case: Lawson v. Hicks">38 Ala. 279, 285-288</a></span> (1862); <em>Myers </em>v. <em>Hodges, </em><span class="citation" data-id="4916813"><a href="/opinion/5099272/myers-v-hodges/#208" aria-description="Citation for case: Myers v. Hodges">53 Fla. 197, 208-210</a></span>, <span class="citation no-link">44 So. 357</span>, 361 (1907); <em>Smith </em>v. <em>Howard, </em><span class="citation" data-id="7094409"><a href="/opinion/7183828/smith-v-howard/#56" aria-description="Citation for case: Smith v. Howard">28 Iowa 51, 56-57</a></span> (1869); <em>Gardemal </em>v. <em>McWilliams, </em><span class="citation" data-id="7195200"><a href="/opinion/7278574/gardemal-v-mcwilliams/#457" aria-description="Citation for case: Gardemal v. McWilliams">43 La. Ann. 454, 457-458</a></span>, <span class="citation no-link">9 So. 106</span>,108 (1891); <em>Burke </em>v. <em>Ryan, </em><span class="citation" data-id="7193408"><a href="/opinion/7277096/burke-v-ryan/#951" aria-description="Citation for case: Burke v. Ryan">36 La. Ann. 951, 951-952</a></span> (1884); <em>McLaughlin </em>v. <em>Cowley, </em><span class="citation" data-id="6419701"><a href="/opinion/6545970/mclaughlin-v-cowley/#319" aria-description="Citation for case: McLaughlin v. Cowley">127 Mass. 316, 319-320</a></span> (1879); <em>Barnes </em>v. <em>McCrate, </em><span class="citation" data-id="4928856"><a href="/opinion/5110328/barnes-v-mccrate/#446" aria-description="Citation for case: Barnes v. McCrate">32 Me. 442, 446-447</a></span> (1851); <em>Cooper </em>v. <em>Phipps, </em><span class="citation" data-id="6896396"><a href="/opinion/6997472/cooper-v-phipps/#363" aria-description="Citation for case: Cooper v. Phipps">24 Ore. 357, 363-364</a></span>, <span class="citation" data-id="6896396"><a href="/opinion/6997472/cooper-v-phipps/#986" aria-description="Citation for case: Cooper v. Phipps">33 P. 985, 986-987</a></span> (1893); <em>Shadden </em>v. <em>McElwee, </em><span class="citation" data-id="8298131"><a href="/opinion/8330232/shadden-v-mcelwee/#149" aria-description="Citation for case: Shadden v. McElwee">86 Tenn. 146, 149-154</a></span>, <span class="citation no-link">5 S. W. 602</span>, 603-605 (1887); <em>Cooley </em>v. <em>Galyon, </em><span class="citation" data-id="8299944"><a href="/opinion/8331975/cooley-v-galyon/#13" aria-description="Citation for case: Cooley v. Galyon">109 Tenn. 1, 13-14</a></span>, <span class="citation no-link">70 S. W. 607</span>, 610 (1902); cf. <em>Hoar </em>v. <em>Wood, </em><span class="citation" data-id="6407880"><a href="/opinion/6534162/hoar-v-wood/#197" aria-description="Citation for case: Hoar v. Wood">44 Mass. 193, 197-198</a></span> (1841) (statements by counsel); <em>Marsh </em>v. <em>Ellsworth, </em><span class="citation" data-id="3576468"><a href="/opinion/3595375/marsh-v-ellsworth/#312" aria-description="Citation for case: Marsh v. . Ellsworth">50 N. Y. 309, 312-313</a></span> (1872) (same). Other courts appear to have taken a position closer to the English rule, which did not require any showing of pertinency or materiality. See, <em>e. g., Chambliss </em>v. <em>Blau, </em><span class="citation" data-id="6518689"><a href="/opinion/6642021/chambliss-v-blau/#89" aria-description="Citation for case: Chambliss v. Blau">127 Ala. 86, 89-90</a></span>, <span class="citation no-link">28 So. 602</span>, 603 (1899); cf. <em>Calkins </em>v. <em>Sumner, </em><span class="citation" data-id="6598323"><a href="/opinion/6717522/calkins-v-sumner/#197" aria-description="Citation for case: Calkins v. Sumner">13 Wis. 193, 197-198</a></span> (1860) (in absence of objection and ruling by court, lack of pertinency of responses to questions does not remove immunity, because witnesses are not in a position to know what statements are pertinent to the case).</p>
<p id="b393-8">Although some cases used the words “good faith,” see, <em>e. g., White </em>v. <em>Carroll, </em><span class="citation" data-id="3593942"><a href="/opinion/3611879/white-v-carroll/#166" aria-description="Citation for case: White v. . Carroll">42 N. Y. 161, 166</a></span> (1870); <em>Shadden </em>v. <span class="citation" data-id="8298131"><a href="/opinion/8330232/shadden-v-mcelwee/#149" aria-description="Citation for case: Shadden v. McElwee"><em>McElwee, supra, </em>at 149-150</a></span>, <page-number citation-index="1" label="332">*332</page-number>5 S. W., at 603, good faith was established as a matter of law if the statements were pertinent and material to the judicial proceeding and given in response to questions. Indeed, even if the testimony was not pertinent, the plaintiff had the burden of proving bad faith. The testimony by respondents in this case would have received absolute protection at common law, because it was directly relevant to the criminal charges against petitioners. If the testimony had not been relevant, it is unlikely that petitioners would have stated a claim that their constitutional rights had been violated. Therefore, for purposes of § 1983 analysis, there is no material difference between the English rule and the American rule.</p>
</footnote>
<footnote label="12">
<p id="b394-13"> Justice Marshall’s dissent relies heavily on an opinion rendered by this Court, <em>White </em>v. <em>Nicholls, </em><span class="citation" data-id="86319"><a href="/opinion/86319/white-v-nicholls/#286" aria-description="Citation for case: White v. Nicholls">3 How. 266, 286-288</a></span> (1845). The Court’s discussion of privileged statements in judicial proceedings was purely dictum. The plaintiff sought damages for defendants’ allegedly defamatory assertions in a petition to the President of the United States requesting the plaintiff’s removal from office as a customs collector, a statement entitled at most to a qualified privilege. <em>White </em>v. <em><span class="citation" data-id="86319"><a href="/opinion/86319/white-v-nicholls/" aria-description="Citation for case: White v. Nicholls">Nicholls</a></span> </em>cannot be considered authoritative. In 1909 a leading commentator stated:</p>
<blockquote id="b394-14">“[T]he demands of public policy on which the rule [of absolute immunity] is based are so controlling that there is only one considered case in the English or American reports in which the existence of the general doctrine of absolute immunity under the common law has ever been questioned. Strangely enough this isolated instance was a decision of the Supreme Court of the United States, in the course of which Mr. Justice Daniel, speaking for the court, denied both the rule and its policy; but this expression of opinion was <em>obiter, </em>since the case in issue was one of qualified immunity.” Veeder, Absolute Immunity in Defamation: Judicial Proceedings, <span class="citation no-link">9 Colum. L. Rev. 463</span>, 465-466 (footnotes omitted).</blockquote>
<p id="b394-15">In 1860, a New York court asserted that “the reasoning of Judge Daniel’s opinion, and the propositions which he deduces where he goes beyond the case in hand, are clearly unsustained by principle or authority.” <em>Perkins </em>v. <em>Mitchell, </em><span class="citation" data-id="5459837"><a href="/opinion/5615126/perkins-v-mitchell/#468" aria-description="Citation for case: Perkins v. Mitchell">31 Barb. 461, 468</a></span> (N. Y. Sup. Ct.). In 1878, the West Virginia Supreme Court severely criticized <em>White </em>v. <em><span class="citation" data-id="86319"><a href="/opinion/86319/white-v-nicholls/" aria-description="Citation for case: White v. Nicholls">Nicholls</a></span>, </em>stating: “We have reviewed all the authorities, cited by Justice Daniel, and have seen, that none of them are in conflict with the position, that express malice may be shielded by its being expressed in judicial proceedings in certain forms. . . . And the review of the American authorities will show, that the overwhelming weight of authority is opposed to Justice Daniel’s idea, that <page-number citation-index="1" label="333">*333</page-number>there is no case, in which an action of slander or libel will not lie for libelous matter, spoken or written in the course of regular judicial proceedings. . . . The authorities, both English and American, fully establish the position, that there is a class of absolutely privileged communications . . . .” <em>Johnson </em>v. <em>Brown, </em>13 W. Ya. 71, 128-129. See also <em>McGehee </em>v. <em>Insurance Co. of North America, </em><span class="citation" data-id="8746034"><a href="/opinion/8762636/mcgehee-v-insurance-co-of-north-america/" aria-description="Citation for case: McGehee v. Insurance Co. of North America">112 F. 853</a></span> (CA5 1902) (declining to follow <em>White </em>v. Nicholls); <em>Shelfer </em>v. <em>Gooding, </em><span class="citation" data-id="3670154"><a href="/opinion/3923607/shelfer-v-gooding/#181" aria-description="Citation for case: Shelfer v. . Gooding">47 N. C. 175, 181-182</a></span> (1855) (suggesting that Justice Daniel miscited <em>Hodgson </em>v. <em>Scarlett, </em>1 Barn. <em>&amp; </em>Aid. 232, 106 Eng. Rep. 86 (K. B. 1818)). In short, <em>White </em>v. <em><span class="citation" data-id="86319"><a href="/opinion/86319/white-v-nicholls/" aria-description="Citation for case: White v. Nicholls">Nicholls</a></span> </em>was not even a reliable statement of the common law; still less was it “the most salient feature in the landscape of the common law at the time Congress acted” in 1871.</p>
</footnote>
<footnote label="13">
<p id="b395-6"> In addition, some courts expressed concern that, in the absence of a privilege, honest witnesses might erroneously be subjected to liability because they would have difficulty proving the truth of their statements. This result seemed inappropriate in light of the witness’ duty to testify. <em>E. g., Calkins </em>v. <em>Sumner, </em><span class="citation" data-id="6598323"><a href="/opinion/6717522/calkins-v-sumner/#198" aria-description="Citation for case: Calkins v. Sumner">13 Wis., at 198</a></span>; <em>Barnes </em>v. <em>McCrate, 32 </em>Me., at 446-447; <em>Chambliss </em>v. <em>Blau, </em><span class="citation" data-id="6518689"><a href="/opinion/6642021/chambliss-v-blau/#89" aria-description="Citation for case: Chambliss v. Blau">127 Ala., at 89</a></span>, 28 So., at 603.</p>
</footnote>
<footnote label="14">
<p id="b396-9"> Cf. <em>Marsh </em>v. <em>Ellsworth, </em>60 N. Y., at 312 (importance of placing all relevant evidence before court and jury “to enable them to arrive at the truth”); <em>Hoar </em>v. <em>Wood, </em><span class="citation" data-id="6407880"><a href="/opinion/6534162/hoar-v-wood/#197" aria-description="Citation for case: Hoar v. Wood">44 Mass., at 197</a></span> (stressing impartiality of judge as sufficient antidote to inaccuracies and exaggerations by adversaries).</p>
</footnote>
<footnote label="15">
<p id="b398-4"> The common-law immunity that protected witnesses as well as other participants in the judicial process drew no distinction between public officials and private citizens. See Veeder, <em>supra </em>n. 12, at 468-469. The general purposes underlying witness immunity at common law applied equally to official and private witnesses. Both types of witness took the stand and testified under oath in response to the questions of counsel. Both might be deterred by the prospect of subsequent, vexatious litigation.</p>
</footnote>
<footnote label="16">
<p id="b398-5"> Brief for Petitioners 19-20, citing 1 B. Schwartz, Statutory History of the United States: Civil Rights 599-606, 625 (1970).</p>
</footnote>
<footnote label="17">
<p id="b398-6"> In addition to § 1, codified as § 1983, and § 2, discussed in text m/m, the Act permitted the President to use armed force in response to insurrection and domestic violence (§ 3), authorized the suspension of habeas corpus if the President deemed it necessary (§ 4), required grand and petit jurors to take a test oath (§ 5), and provided a civil penalty against persons who knew of and failed to prevent § 2 violations. <span class="citation no-link">17 Stat. 13</span>.</p>
</footnote>
<footnote label="18">
<p id="b399-6"> Supporters of the bill repeatedly quoted the testimony before an investigating committee of two former Klan members, who described a Klan oath binding its members to commit perjury. Cong. Globe, 42d Cong., 1st Sess., 152, 158, 173, 201, 320-321, 322, 340, 437, 439, 443-444, 457, 458, 503, 516, 518, 653, 654, 687 (1871).</p>
</footnote>
<footnote label="19">
<p id="b400-7"> See <span class="citation no-link"><em>id., </em>at 322</span> (remarks of Rep. Stoughton); 334 (remarks of Rep. Hoar); 375 (remarks of Rep. Lowe); 428 (remarks of Rep. Beatty); 458, 459 (remarks of Rep. Cobum); 481-482 (remarks of Rep. Wilson); 486 (remarks of Rep. Cook); 501 (remarks of Sen. Frelinghuysen); 506 (remarks of Sen. Pratt); 608 (remarks of Sen. Pool); 697 (remarks of Sen. Edmunds).</p>
</footnote>
<footnote label="20">
<p id="b400-8"> As Representative Coburn stated:</p>
<blockquote id="b400-9">“The United States courts are further above mere local influence than the county courts; their judges can act with more independence, cannot be put under terror, as local judges can; their sympathies are not so nearly identified with those of the vicinage; the jurors are taken from the State, and not the neighborhood; they will be able to rise above prejudices and bad passions or terror more easily. The marshal, clothed with more power than the sheriff, can make arrests with certainty, and, with the aid of the General Government, can seize offenders in spite of any banded and combined resistance such as may be expected.” <span class="citation no-link"><em>Id., </em>at 460</span>.</blockquote>
<p id="b400-10">See <span class="citation no-link"><em>id., </em>at 334</span> (remarks of Rep. Hoar); 374 (remarks of Rep. Lowe); 428 (remarks of Rep. Beatty); 459-460 (remarks of Rep. Coburn); 486 (remarks of Rep. Cook); 501 (remarks of Sen. Frelinghuysen); 514 (remarks of Rep. Poland).</p>
</footnote>
<footnote label="21">
<p id="b401-7"> Compare <span class="citation no-link"><em>id., </em>at 317</span> (original version introduced by Rep. Shellabarger) with <span class="citation no-link"><em>id., </em>at 477-478</span> (more general language in amended version); see <span class="citation no-link"><em>id., </em>at 567, 702</span> (Senate amendment adding language punishing conspiracy for obstructing the due course of justice).</p>
</footnote>
<footnote label="22">
<p id="b401-8"> It is noteworthy that the imposition of criminal liability on persons for conspiracy to give false evidence was not in derogation of the common law as it existed in 1871. Witnesses were traditionally subject to a prosecution for perjury committed in the course of their evidence, “or for conspiracy in case of a combination of two or more to give false evidence.” Newell, <em>supra </em>n. 11, at 450, § 44. The offense of perjury had been shaped in English law during the 16th and 17th centuries by Parliament, the Court of Star Chamber, and common-law judges. 4 W. Holdsworth, A History of English Law 515-519 (1924); S. Milsom, Historical Foundations of the Common Law 418 (2d ed. 1981).</p>
</footnote>
<footnote label="23">
<p id="b402-6"> In several hundred pages of small triple-columned print, only one Senator — not a member of the Committee that reported the bill — referred to the possibility that perjury was being used to convict the innocent. See Cong. Globe, 42d Cong., 1st Sess., 653 (1871) (remarks of Sen. Osborn). His comments were made in connection with a proposal to retain a test oath for grand and petit jurors.</p>
</footnote>
<footnote label="24">
<p id="b402-7"> The debates describe nocturnal Klan meetings passing decrees condemning political enemies. See <em>id., </em>at 157, 209, 320, 321, 504.</p>
</footnote>
<footnote label="25">
<p id="b402-8"> For references to lynch mobs attacking suspects held in custody, see <em>id., </em>at 156. 157. 166. 200. 321. 444. 446. 447.</p>
</footnote>
<footnote label="26">
<p id="b403-4"> The legislative history of the Civil Rights Act of 1866, discussed at length by Justice MARSHALL’S dissent, simply does not speak to the question whether Congress intended witnesses — private parties or public officials — to be civilly liable for false testimony resulting in an unjust criminal conviction. It makes clear that judges and other “state officials integral to the judicial process” are subject to <em>criminal </em>liability for violating the constitutional rights of individuals. But we have never questioned that proposition, and we do not do so now. Moreover, witnesses enjoyed no common-law immunity from criminal prosecution for perjury. See n. 22, <em>supra. </em>Therefore the <em>criminal </em>provisions of the 1866 Act and its successors apply to official witnesses. See n. 32, <em>infra. </em>But the 1866 legislative history, to the extent that it sheds any light on the meaning of the 1871 Act, does not support <em>civil </em>liability for such witnesses, because it does not show the requisite congressional intent to override the clearly established common-law immunity of witnesses from civil liability. With respect to witnesses, the legislative history of the 1866 Act is simply silent, and we are unwilling to assume that, whenever legislators referred to “state judicial officials” or to “the judicial power of the State,” they were describing witnesses as well as judges, sheriffs, and marshals.</p>
<p id="b403-5">Moreover, our decisions recognizing absolute immunity for judges and prosecutors from civil liability under the 1871 Act implicitly reject the position that the legislative history of the 1866 Act defines the scope of immunity for purposes of the 1871 Act. See <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967); <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976).</p>
</footnote>
<footnote label="27">
<p id="b403-6"> The contours of the proposed exception are not clear. Similar considerations would presumably apply to other government officials and experts, including coroners, medical examiners, psychiatric experts, and social workers.</p>
</footnote>
<footnote label="28">
<p id="b404-7"> See <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#513" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 513-514</a></span> (1978) (administrative law judges enjoy absolute judicial immunity even though they are in the Executive Branch); <em>Imbler </em>v. <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman"><em>Pachtman, supra, </em>at 430-431</a></span> (reserving the question whether a prosecutor, who is absolutely immune for decisions to initiate a prosecution or put witnesses on the stand, has similar immunity for administrative or investigative tasks); cf. <em>Hampton </em>v. <em>City of Chicago, </em><span class="citation" data-id="8890918"><a href="/opinion/8903845/hampton-v-city-of-chicago/#608" aria-description="Citation for case: Hampton v. City of Chicago">484 F. 2d 602, 608</a></span> (CA7 1973) (prosecutor’s immunity ceases when he acts in a capacity other than his quasi-judicial role), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/917/">415 U. S. 917</a></span> (1974).</p>
</footnote>
<footnote label="29">
<p id="b405-7"> Moreover, lawsuits alleging perjury on the stand in violation of the defendant’s due process rights often raise material questions of fact, inappropriate for disposition at the summary judgment stage. The plaintiff’s complaint puts in issue the falsity and materiality of the allegedly perjured statements, and the defendant witness’ knowledge and state of mind at the time he testified. Sometimes collateral-estoppel principles will permit dismissal at the pretrial stage. But if the truth of the allegedly perjured statement was not necessarily decided in the previous criminal verdict, if there is newly discovered evidence of falsity, or if the defendant concedes that the testimony was inaccurate, the central issue will be the defendant’s state of mind. Summary judgment is usually not feasible under these circumstances. C. Wright, Law of Federal Courts 493 (3d ed. 1976). If summary judgment is denied, the case must proceed to trial and must traverse much of the same ground as the original criminal trial.</p>
</footnote>
<footnote label="30">
<p id="b406-6"> We are not writing on a clean slate, and it is not for us to craft a new rule designed to enable trial judges to dismiss meritless claims before trial but to allow recovery in cases of demonstrated injustice, when an innocent plaintiff has already obtained postconviction relief. The States remain free to grant relief in such cases and, of course, Congress has the power to fashion an appropriate remedy if it perceives the need for one.</p>
</footnote>
<footnote label="31">
<p id="b407-7"> There is no reason to believe, however, that this risk is any greater than, or indeed as great as, the risk of an unjust conviction resulting from a misidentification or other unintentional mistake. There is no federal damages remedy for such innocent persons, or for those who are acquitted after undergoing the burdens of a criminal trial.</p>
</footnote>
<footnote label="32">
<p id="b407-8"> Finally, in those cases in which the judicial process fails, the public is not powerless to punish misconduct. Like prosecutors and judges, official witnesses may be punished criminally for willful deprivations of constitutional rights under <span class="citation no-link">18 U. S. C. § 242</span>.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Brosseau v. Haugen.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "Brosseau v. Haugen"
type: case
citation: "543 U.S. 194 (2004)"
parallel_cite: "125 S. Ct. 596; 160 L. Ed. 2d 583"
neutral_cite: 2004 U.S. LEXIS 8275
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-12-13
docket: 03-1261
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-12-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brosseau v. Haugen
  varies_by_point: false
  scope_note: "Good law (per curiam). The leading specificity case for qualified immunity in the use-of-force setting: Graham and Garner are 'cast at a high level of generality' and rarely clearly establish the answer in a particular shooting; repeatedly reaffirmed (e.g. Mullenix v. Luna, Kisela v. Hughes)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137736/brosseau-v-haugen/"
  cluster_id: 137736
  opinion_id: 137736
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Tennessee v. Garner]]", "[[Graham v. Connor]]", "[[Mullenix v. Luna]]", "[[Kisela v. Hughes]]", "[[Plumhoff v. Rickard]]"]
aliases: []
tags: ["case", "use-of-force", "deadly-force", "qualified-immunity", "section-1983", "clearly-established-law", "fleeing-suspect"]
holding: "Officer Brosseau was entitled to qualified immunity for shooting a fleeing suspect in a vehicle: Garner and Graham are cast at too high a level of generality to clearly establish that the shooting was unlawful, and the handful of relevant fact-specific cases placed her conduct in the 'hazy border between excessive and acceptable force.'"
lake:
  record_id: Brosseau v. Haugen
  status: verified
  projected_at: 2026-07-06
---

# Brosseau v. Haugen

*543 U.S. 194 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Rochelle Brosseau of the Puyallup, Washington, police responded to a report of a fight at Kenneth Haugen's mother's house; Haugen had a felony no-bail warrant. After a foot search, Haugen jumped into his Jeep, locked the door, and ignored Brosseau's commands to get out. Brosseau broke the driver's window with her handgun and struck him, but Haugen started the Jeep. As it began to move — with another officer on foot, occupied vehicles nearby, and a girlfriend and child in a car in the driveway — Brosseau fired one shot through the rear window, hitting Haugen in the back. He survived, pleaded guilty to felony "eluding," and sued under § 1983 for excessive force.

## Issue
Whether Officer Brosseau was entitled to [[Qualified Immunity|qualified immunity]] on the excessive-force claim — i.e., whether it was clearly established that shooting a fleeing suspect in these circumstances violated the Fourth Amendment.

## Rule
[[Qualified Immunity|Qualified immunity]] protects an officer who reasonably misjudges an unsettled legal question. "Qualified immunity shields an officer from suit when she makes a decision that, even if constitutionally deficient, reasonably misapprehends the law governing the circumstances she confronted." — 543 U.S. at 198. ^pin-198

The clearly-established inquiry must be particularized, not abstract. "*Graham* and *Garner*, following the lead of the Fourth Amendment's text, are cast at a high level of generality." — 543 U.S. at 199. ^pin-199

Those general standards "clearly establish" the answer only "in an obvious case … even without a body of relevant case law." — *Id.*

The fact-specific precedent did not place the question beyond debate. The relevant cases "taken together undoubtedly show that this area is one in which the result depends very much on the facts of each case. None of them squarely governs the case here; they do suggest that Brosseau's actions fell in the '"hazy border between excessive and acceptable force."'" — 543 U.S. at 201. ^pin-201

Accordingly, "[t]he cases by no means 'clearly establish' that Brosseau's conduct violated the Fourth Amendment." — *Id.* ^pin-201b

## Application
The Court took the facts in the light most favorable to Haugen and expressed no view on whether the shooting actually violated the Fourth Amendment; it resolved the case on the second, qualified-immunity step alone. Measured at the proper level of specificity — whether to shoot "a disturbed felon, set on avoiding capture through vehicular flight, when persons in the immediate area are at risk from that flight" — only a "handful" of lower-court decisions spoke to the situation, and they pointed in different directions (*Cole v. Bone* and *Smith v. Freland* finding no violation; *Estate of Starks v. Enyart* finding a jury question). Because that body of law did not give Brosseau fair notice that her single shot was unlawful, her conduct fell in the hazy border the doctrine protects, and she was entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
Reversed. The Ninth Circuit erred on [[Qualified Immunity|qualified immunity]]; Brosseau was entitled to it because the law did not clearly establish that her shooting of the fleeing Haugen violated the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- *Brosseau* is the foundational reminder that excessive-force [[Qualified Immunity|qualified immunity]] is judged at a high level of specificity: the general reasonableness tests of [[Graham v. Connor]] and [[Tennessee v. Garner]] rarely "clearly establish" the answer in a particular shooting. The Court has reaffirmed and applied it repeatedly — [[Mullenix v. Luna]] and [[Kisela v. Hughes]] both rely on *Brosseau*, and [[Plumhoff v. Rickard]] cited it for the proposition that no clearly established law forbade the officers' conduct. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Brosseau v. Haugen*, 543 U.S. 194 (2004) (per curiam) — https://www.courtlistener.com/opinion/137736/brosseau-v-haugen/ — pinpoints: 198, 199, 201.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0ff8fb3811222318", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brosseau v. Haugen"}, "payload": {"all": [{"cite": "543 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "543"}, {"cite": "125 S. Ct. 596", "page": "596", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "125"}, {"cite": "160 L. Ed. 2d 583", "page": "583", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "160"}, {"cite": "2004 U.S. LEXIS 8275", "page": "8275", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}], "display": "543 U.S. 194", "official": {"cite": "543 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "543"}, "official_selection_present": true, "record_id": "Brosseau v. Haugen"}}
{"assertion_id": "0375e2351727818a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-201", "record_id": "Brosseau v. Haugen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-201", "pinpoint_status": "slip-only", "quote": "— *Id.* The fact-specific precedent did not place the question beyond debate. The relevant cases", "quote_fidelity": "mismatch", "record_id": "Brosseau v. Haugen", "star_marker": null}}
{"assertion_id": "29ddcd072ed3dc0f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-201b", "record_id": "Brosseau v. Haugen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-201b", "pinpoint_status": "slip-only", "quote": "[t]he cases by no means 'clearly establish' that Brosseau's conduct violated the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "Brosseau v. Haugen", "star_marker": null}}
{"assertion_id": "a60eff08d746b42f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-198", "record_id": "Brosseau v. Haugen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-198", "pinpoint_status": "slip-only", "quote": "and sued under § 1983 for excessive force. ## Issue Whether Officer Brosseau was entitled to qualified immunity on the excessive-force claim — i.e., whether it was clearly established that shooting a fleeing suspect in these circumstances violated the Fourth Amendment. ## Rule Qualified immunity protects an officer who reasonably misjudges an unsettled legal question.", "quote_fidelity": "mismatch", "record_id": "Brosseau v. Haugen", "star_marker": null}}
{"assertion_id": "e71dd9bc683ba3bc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-199", "record_id": "Brosseau v. Haugen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-199", "pinpoint_status": "slip-only", "quote": "*Graham* and *Garner*, following the lead of the Fourth Amendment's text, are cast at a high level of generality.", "quote_fidelity": "mismatch", "record_id": "Brosseau v. Haugen", "star_marker": null}}
{"assertion_id": "fa792afe337dfb1e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brosseau v. Haugen"}, "payload": {"as_of_content": "2004-12-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brosseau v. Haugen", "scope_note": "Good law (per curiam). The leading specificity case for qualified immunity in the use-of-force setting: Graham and Garner are 'cast at a high level of generality' and rarely clearly establish the answer in a particular shooting; repeatedly reaffirmed (e.g. Mullenix v. Luna, Kisela v. Hughes).", "varies_by_point": false}}
```

### lake record — Brosseau v. Haugen

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brosseau v. Haugen",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brosseau v. Haugen",
    "case_name_short": "Brosseau",
    "case_name_full": "Brosseau v. Haugen",
    "input_case_name": "Brosseau v. Haugen",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-12-13",
    "year": 2004,
    "docket": "03-1261",
    "cluster_id": 137736,
    "lead_opinion_id": 137736,
    "sibling_ids": [
      137736,
      9434715,
      9434716,
      9434717
    ],
    "absolute_url": "/opinion/137736/brosseau-v-haugen/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "543 U.S. 194",
      "volume": "543",
      "reporter": "U.S.",
      "page": "194",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "125 S. Ct. 596",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 583",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "583",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 8275",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "8275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "543 U.S. 194",
        "volume": "543",
        "reporter": "U.S.",
        "page": "194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 S. Ct. 596",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 583",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "583",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 8275",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "8275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "543 U.S. 194",
    "official_selection": {
      "court_class": "scotus",
      "selected": "543 U.S. 194",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-198",
      "page": null,
      "quote": "and sued under \u00a7 1983 for excessive force. ## Issue Whether Officer Brosseau was entitled to qualified immunity on the excessive-force claim \u2014 i.e., whether it was clearly established that shooting a fleeing suspect in these circumstances violated the Fourth Amendment. ## Rule Qualified immunity protects an officer who reasonably misjudges an unsettled legal question.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-199",
      "page": null,
      "quote": "*Graham* and *Garner*, following the lead of the Fourth Amendment's text, are cast at a high level of generality.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-201",
      "page": null,
      "quote": "\u2014 *Id.* The fact-specific precedent did not place the question beyond debate. The relevant cases",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-201b",
      "page": null,
      "quote": "[t]he cases by no means 'clearly establish' that Brosseau's conduct violated the Fourth Amendment.",
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
    "composite_basis_ref": "Brosseau v. Haugen",
    "varies_by_point": false,
    "scope_note": "Good law (per curiam). The leading specificity case for qualified immunity in the use-of-force setting: Graham and Garner are 'cast at a high level of generality' and rarely clearly establish the answer in a particular shooting; repeatedly reaffirmed (e.g. Mullenix v. Luna, Kisela v. Hughes).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tolan v. Cotton",
          "cluster_id": 2672535,
          "cite": [
            "188 L. Ed. 2d 895",
            "134 S. Ct. 1861",
            "2014 U.S. LEXIS 3112",
            "82 U.S.L.W. 4358",
            "572 U.S. 650",
            "88 Fed. R. Serv. 3d 765",
            "24 Fla. L. Weekly Fed. S 731",
            "2014 WL 1757856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reichle v. Howards",
          "cluster_id": 801500,
          "cite": [
            "182 L. Ed. 2d 985",
            "132 S. Ct. 2088",
            "566 U.S. 658",
            "2012 U.S. LEXIS 4132"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Pauly",
          "cluster_id": 4374579,
          "cite": [
            "580 U.S. 73",
            "196 L. Ed. 2d 463",
            "2017 U.S. LEXIS 5",
            "137 S. Ct. 548",
            "26 Fla. L. Weekly Fed. S 409",
            "85 U.S.L.W. 4027",
            "2017 WL 69170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisela v. Hughes",
          "cluster_id": 4482892,
          "cite": [
            "584 U.S. 100",
            "138 S. Ct. 1148",
            "200 L. Ed. 2d 449",
            "2018 U.S. LEXIS 2066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crawford v. Metropolitan Government of Nashville and Davidson Cty.",
          "cluster_id": 145915,
          "cite": [
            "172 L. Ed. 2d 650",
            "129 S. Ct. 846",
            "555 U.S. 271",
            "2009 U.S. LEXIS 870",
            "21 Fla. L. Weekly Fed. S 609",
            "77 U.S.L.W. 4093",
            "91 Empl. Prac. Dec. (CCH) 43,434",
            "105 Fair Empl. Prac. Cas. (BNA) 353"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goebert v. Lee County",
          "cluster_id": 77881,
          "cite": [
            "510 F.3d 1312",
            "2007 U.S. App. LEXIS 29513",
            "2007 WL 4458122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laura Skop v. City of Atlanta, Georgia",
          "cluster_id": 77695,
          "cite": [
            "485 F.3d 1130",
            "2007 U.S. App. LEXIS 10341",
            "2007 WL 1288012"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkie v. Robbins",
          "cluster_id": 145705,
          "cite": [
            "168 L. Ed. 2d 389",
            "127 S. Ct. 2588",
            "551 U.S. 537",
            "2007 U.S. LEXIS 8513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick Booker v. South Carolina Department of Corrections",
          "cluster_id": 4387227,
          "cite": [
            "855 F.3d 533",
            "2017 WL 1531576",
            "2017 U.S. App. LEXIS 7563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Deville v. Marcantel",
          "cluster_id": 65780,
          "cite": [
            "567 F.3d 156",
            "2009 U.S. App. LEXIS 9403",
            "2009 WL 1162586"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morgan v. Swanson",
          "cluster_id": 8441074,
          "cite": [
            "659 F.3d 359",
            "2011 U.S. App. LEXIS 19656",
            "2011 WL 4470233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iqbal v. Hasty",
          "cluster_id": 2716,
          "cite": [
            "490 F.3d 143"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ellen Keates v. Michael Koile",
          "cluster_id": 4474827,
          "cite": [
            "883 F.3d 1228"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Elyea",
          "cluster_id": 183790,
          "cite": [
            "631 F.3d 843",
            "78 Fed. R. Serv. 3d 874",
            "2011 U.S. App. LEXIS 1781",
            "2011 WL 256978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maldonado v. Fontanes",
          "cluster_id": 203857,
          "cite": [
            "568 F.3d 263",
            "2009 U.S. App. LEXIS 12716",
            "2009 WL 1547737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Victoria Zetwick v. County of Yolo",
          "cluster_id": 4370725,
          "cite": [
            "850 F.3d 436",
            "2017 WL 710476",
            "2017 U.S. App. LEXIS 3260",
            "101 Empl. Prac. Dec. (CCH) 45,744",
            "129 Fair Empl. Prac. Cas. (BNA) 1657"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk3MzYzMjAwMDAwJnM9NDc3NTMxOCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137736+OR+9434715+OR+9434716+OR+9434717%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      },
      "lane2_top_cited": {
        "query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNjUmcz0yMDkyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28137736+OR+9434715+OR+9434716+OR+9434717%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717)",
        "reviewed": 105,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 105,
        "triage_read": 0,
        "triage_snippet_classified": 105
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717)",
    "indexed_citing_opinions": 1039,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137736,
        "count": 743,
        "count_source": "search"
      },
      {
        "opinion_id": 9434715,
        "count": 312,
        "count_source": "search"
      },
      {
        "opinion_id": 9434716,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434717,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2766,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brosseau-v-haugen.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyOTAwNjYmcz0xMDM3MzA2NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28137736+OR+9434715+OR+9434716+OR+9434717%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137736,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 112594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 136067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 541812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 576267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 607163,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 652953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 765106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 765160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 767897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 776968,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 783116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 784483,
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
    "date_created": "2026-07-04T20:37:54Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:38:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:38:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:38:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brosseau v. Haugen

```
<div>
<center><b><span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/" aria-description="Citation for case: Brosseau v. Haugen">543 U.S. 194</a></span> (2004)</b></center>
<center><h1>BROSSEAU<br>
v.<br>
HAUGEN</h1></center>
<center>No. 03-1261.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Decided December 13, 2004.</center>
ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p>PER CURIAM.</p>
<p>Officer Rochelle Brosseau, a member of the Puyallup, Washington, Police Department, shot Kenneth Haugen in the back as he attempted to flee from law enforcement authorities in his vehicle. Haugen subsequently filed this action in the United States District Court for the Western District of <span class="star-pagination">*195</span> Washington pursuant to Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>. He alleged that the shot fired by Brosseau constituted excessive force and violated his federal constitutional rights.<sup>[1]</sup> The District Court granted summary judgment to Brosseau after finding she was entitled to qualified immunity. The Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police...">339 F. 3d 857</a></span> (2003). Following the two-step process set out in <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span> (2001), the Court of Appeals found, first, that Brosseau had violated Haugen's Fourth Amendment right to be free from excessive force and, second, that the right violated was clearly established and thus Brosseau was not entitled to qualified immunity. Brosseau then petitioned for writ of certiorari, requesting that we review both of the Court of Appeals' determinations. We grant the petition on the second, qualified immunity question and reverse.</p>
<p>The material facts, construed in a light most favorable to Haugen, are as follows.<sup>[2]</sup> On the day before the fracas, Glen Tamburello went to the police station and reported to Brosseau that Haugen, a former crime partner of his, had stolen tools from his shop. Brosseau later learned that there was a felony no-bail warrant out for Haugen's arrest on drug and other offenses. The next morning, Haugen was spray painting his Jeep Cherokee in his mother's driveway. Tamburello learned of Haugen's whereabouts, and he and cohort Matt Atwood drove a pickup truck to Haugen's mother's house to pay Haugen a visit. A fight ensued, which was witnessed by a neighbor who called 911.</p>
<p>Brosseau heard a report that the men were fighting in Haugen's mother's yard and responded. When she arrived, Tamburello and Atwood were attempting to get Haugen into <span class="star-pagination">*196</span> Tamburello's pickup. Brosseau's arrival created a distraction, which provided Haugen the opportunity to get away. Haugen ran through his mother's yard and hid in the neighborhood. Brosseau requested assistance, and, shortly thereafter, two officers arrived with a K-9 to help track Haugen down. During the search, which lasted about 30 to 45 minutes, officers instructed Tamburello and Atwood to remain in Tamburello's pickup. They instructed Deanna Nocera, Haugen's girlfriend who was also present with her 3-year-old daughter, to remain in her small car with her daughter. Tamburello's pickup was parked in the street in front of the driveway; Nocera's small car was parked in the driveway in front of and facing the Jeep; and the Jeep was in the driveway facing Nocera's car and angled somewhat to the left. The Jeep was parked about 4 feet away from Nocera's car and 20 to 30 feet away from Tamburello's pickup.</p>
<p>An officer radioed from down the street that a neighbor had seen a man in her backyard. Brosseau ran in that direction, and Haugen appeared. He ran past the front of his mother's house and then turned and ran into the driveway. With Brosseau still in pursuit, he jumped into the driver's side of the Jeep and closed and locked the door. Brosseau believed that he was running to the Jeep to retrieve a weapon.</p>
<p>Brosseau arrived at the Jeep, pointed her gun at Haugen, and ordered him to get out of the vehicle. Haugen ignored her command and continued to look for the keys so he could get the Jeep started. Brosseau repeated her commands and hit the driver's side window several times with her handgun, which failed to deter Haugen. On the third or fourth try, the window shattered. Brosseau unsuccessfully attempted to grab the keys and struck Haugen on the head with the barrel and butt of her gun. Haugen, still undeterred, succeeded in starting the Jeep. As the Jeep started or shortly after it began to move, Brosseau jumped back and to the left. She fired one shot through the rear driver's side window <span class="star-pagination">*197</span> at a forward angle, hitting Haugen in the back. She later explained that she shot Haugen because she was "`fearful for the other officers on foot who [she] believed were in the immediate area, [and] for the occupied vehicles in [Haugen's] path and for any other citizens who might be in the area.'" <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/#865" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police...">339 F. 3d, at 865</a></span>.</p>
<p>Despite being hit, Haugen, in his words, "`st[ood] on the gas'"; navigated the "`small, tight space'" to avoid the other vehicles; swerved across the neighbor's lawn; and continued down the street. <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/#882" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police..."><i>Id.,</i> at 882</a></span>. After about a half block, Haugen realized that he had been shot and brought the Jeep to a halt. He suffered a collapsed lung and was airlifted to a hospital. He survived the shooting and subsequently pleaded guilty to the felony of "eluding." <span class="citation no-link">Wash. Rev. Code § 46.61.024</span> (1994). By so pleading, he admitted that he drove his Jeep in a manner indicating "a wanton or wilful disregard for the lives . . . of others." <i><span class="citation no-link">Ibid.</span></i> He subsequently brought this § 1983 action against Brosseau.</p>
<p></p>
<h2>*  *  *</h2>
<p>When confronted with a claim of qualified immunity, a court must ask first the following question: "Taken in the light most favorable to the party asserting the injury, do the facts alleged show the officer's conduct violated a constitutional right?" <i>Saucier</i> v. <i>Katz,</i> 533 U. S., at 201. As the Court of Appeals recognized, the constitutional question in this case is governed by the principles enunciated in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), and <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989). These cases establish that claims of excessive force are to be judged under the Fourth Amendment's "`objective reasonableness'" standard. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#388" aria-description="Citation for case: Graham v. Connor"><i>Id.,</i> at 388</a></span>. Specifically with regard to deadly force, we explained in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> that it is unreasonable for an officer to "seize an unarmed, nondangerous suspect by shooting him dead." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 11</a></span>. But "[w]here the officer has probable cause to believe that the suspect poses a threat of serious physical <span class="star-pagination">*198</span> harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force." <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Ibid.</a></span></i></p>
<p>We express no view as to the correctness of the Court of Appeals' decision on the constitutional question itself. We believe that, however that question is decided, the Court of Appeals was wrong on the issue of qualified immunity.<sup>[3]</sup></p>
<p>Qualified immunity shields an officer from suit when she makes a decision that, even if constitutionally deficient, reasonably misapprehends the law governing the circumstances she confronted. <i>Saucier</i> v. <i>Katz,</i> 533 U.S., at 206 (qualified immunity operates "to protect officers from the sometimes `hazy border between excessive and acceptable force'"). Because the focus is on whether the officer had fair notice that her conduct was unlawful, reasonableness is judged against the backdrop of the law at the time of the conduct. If the law at that time did not clearly establish that the officer's conduct would violate the Constitution, the officer should not be subject to liability or, indeed, even the burdens of litigation.</p>
<p>It is important to emphasize that this inquiry "must be undertaken in light of the specific context of the case, not as a broad general proposition." <i>Id.,</i> at 201. As we previously said in this very context:</p>
<blockquote>"[T]here is no doubt that <i>Graham</i> v. <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Connor, supra</a></span></i><i>,</i> clearly establishes the general proposition that use of force is contrary to the Fourth Amendment if it is excessive under objective standards of reasonableness. Yet that is not enough. Rather, we emphasized in <i>Anderson</i> [v. <i>Creighton</i>] `that the right the official is alleged to have violated must have been "clearly established" in <span class="star-pagination">*199</span> a more particularized, and hence more relevant, sense: The contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right.' 483 U.S. [635,] 640 [(1987)]. The relevant, dispositive inquiry in determining whether a right is clearly established is whether it would be clear to a reasonable officer that his conduct was unlawful in the situation he confronted." <i>Id.,</i> at 201-202.</blockquote>
<p>The Court of Appeals acknowledged this statement of law, but then proceeded to find fair warning in the general tests set out in <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> and <i>Garner.</i> <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/#873" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police...">339 F.3d, at 873-874</a></span>. In so doing, it was mistaken. <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> and <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>,</i> following the lead of the Fourth Amendment's text, are cast at a high level of generality. See <i>Graham</i> v. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor"><i>Connor, supra,</i> at 396</a></span> ("`[T]he test of reasonableness under the Fourth Amendment is not capable of precise definition or mechanical application'"). Of course, in an obvious case, these standards can "clearly establish" the answer, even without a body of relevant case law. See <i>Hope</i> v. <i>Pelzer,</i> <span class="citation" data-id="9434318"><a href="/opinion/121169/hope-v-pelzer/#738" aria-description="Citation for case: Hope v. Pelzer">536 U.S. 730, 738</a></span> (2002) (noting in a case where the Eighth Amendment violation was "obvious" that there need not be a materially similar case for the right to be clearly established). See also <i>Pace</i> v. <i>Capobianco,</i> <span class="citation" data-id="7009807"><a href="/opinion/7103965/pace-v-capobianco/#1283" aria-description="Citation for case: Pace v. Capobianco">283 F.3d 1275, 1283</a></span> (CA11 2002) (explaining in a Fourth Amendment case involving an officer shooting a fleeing suspect in a vehicle that, "when we look at decisions such as <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> and <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>,</i> we see some tests to guide us in determining the law in many different kinds of circumstances; but we do not see the kind of clear law (clear answers) that would apply" to the situation at hand). The present case is far from the obvious one where <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> and <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> alone offer a basis for decision.</p>
<p>We therefore turn to ask whether, at the time of Brosseau's actions, it was "`"clearly established"'" in this more "`particularized'" sense that she was violating Haugen's Fourth Amendment right. <i>Saucier</i> v. <i>Katz,</i> 533 U.S., at <span class="star-pagination">*200</span> 202. The parties point us to only a handful of cases relevant to the "situation [Brosseau] confronted": whether to shoot a disturbed felon, set on avoiding capture through vehicular flight, when persons in the immediate area are at risk from that flight.<sup>[4]</sup><i>Ibid.</i> Specifically, Brosseau points us to <i>Cole</i> v. <i>Bone,</i> <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/" aria-description="Citation for case: Cole v. Bone">993 F. 2d 1328</a></span> (CA8 1993), and <i>Smith</i> v. <i>Freland,</i> <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">954 F. 2d 343</a></span> (CA6 1992).</p>
<p>In these cases, the courts found no Fourth Amendment violation when an officer shot a fleeing suspect who presented a risk to others. <i>Cole</i> v. <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/#1333" aria-description="Citation for case: Cole v. Bone"><i>Bone, supra,</i> at 1333</a></span> (holding the officer "had probable cause to believe that the truck posed an imminent threat of serious physical harm to innocent motorists as well as to the officers themselves"); <i>Smith</i> v. <i>Freland,</i> <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/#347" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">954 F. 2d, at 347</a></span> (noting "a car can be a deadly weapon" and holding the officer's decision to stop the car from possibly injuring others was reasonable). <i><span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">Smith</a></span></i> is closer to this case. There, the officer and suspect engaged in a car chase, which appeared to be at an end when the officer cornered the suspect at the back of a dead-end residential street. The suspect, however, freed his car and began speeding down the street. At this point, the officer fired a shot, which killed the suspect. The court held the officer's decision was reasonable and thus did not violate the Fourth Amendment. It noted that the suspect, like Haugen here, "had proven he would do almost anything to avoid capture" and that he posed a major threat to, among others, the officers at the end of the street. <i><span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">Ibid.</a></span></i></p>
<p><span class="star-pagination">*201</span> Haugen points us to <i>Estate of Starks</i> v. <i>Enyart,</i> <span class="citation" data-id="6928206"><a href="/opinion/7026598/estate-of-starks-v-enyart/" aria-description="Citation for case: Estate of Starks v. Enyart">5 F. 3d 230</a></span> (CA7 1993), where the court found summary judgment inappropriate on a Fourth Amendment claim involving a fleeing suspect. There, the court concluded that the threat created by the fleeing suspect's failure to brake when an officer suddenly stepped in front of his just-started car was not a sufficiently grave threat to justify the use of deadly force. <span class="citation" data-id="6928206"><a href="/opinion/7026598/estate-of-starks-v-enyart/#234" aria-description="Citation for case: Estate of Starks v. Enyart"><i>Id.,</i> at 234</a></span>.</p>
<p>These three cases taken together undoubtedly show that this area is one in which the result depends very much on the facts of each case. None of them squarely governs the case here; they do suggest that Brosseau's actions fell in the "`hazy border between excessive and acceptable force.'" <i>Saucier</i> v. <i>Katz, supra,</i> at 206. The cases by no means "clearly establish" that Brosseau's conduct violated the Fourth Amendment.</p>
<p>The judgment of the United States Court of Appeals for the Ninth Circuit is therefore reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BREYER, with whom JUSTICE SCALIA and JUSTICE GINSBURG join, concurring.</p>
<p>I join the Court's opinion but write separately to express my concern about the matter to which the Court refers in footnote 3, namely, the way in which lower courts are required to evaluate claims of qualified immunity under the Court's decision in <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.S./533/194/">533 U.S. 194</a></span>, 201 (2001). As the Court notes, <i>ante,</i> at 198, n. 3, <i>Saucier</i> requires lower courts to decide (1) the constitutional question prior to deciding (2) the qualified immunity question. I am concerned that the current rule rigidly requires courts unnecessarily to decide difficult constitutional questions when there is available an easier basis for the decision (<i>e. g.,</i> qualified immunity) that will satisfactorily resolve the case before the court. Indeed when courts' dockets are crowded, a rigid "order of <span class="star-pagination">*202</span> battle" makes little administrative sense and can sometimes lead to a constitutional decision that is effectively insulated from review, see <i>Bunting</i> v. <i>Mellen,</i> <span class="citation" data-id="9434630"><a href="/opinion/136067/bunting-v-mellen/#1025" aria-description="Citation for case: Bunting v. Mellen">541 U. S. 1019, 1025</a></span> (2004) (SCALIA, J., dissenting from denial of certiorari). For these reasons, I think we should reconsider this issue.</p>
<p>JUSTICE STEVENS, dissenting.</p>
<p>In my judgment, the answer to the constitutional question presented by this case is clear: Under the Fourth Amendment, it was objectively unreasonable for Officer Brosseau to use deadly force against Kenneth Haugen in an attempt to prevent his escape. What is not clear is whether Brosseau is nonetheless entitled to qualified immunity because it might not have been apparent to a reasonably well-trained officer in Brosseau's shoes that killing Haugen to prevent his escape was unconstitutional. In my opinion that question should be answered by a jury.</p>
<p></p>
<h2>I</h2>
<p>Law enforcement officers should never be subject to damages liability for failing to anticipate novel developments in constitutional law. Accordingly, whenever a suit against an officer is based on the alleged violation of a constitutional right that has not been clearly established, the qualified immunity defense is available. <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982). Prompt dismissal of such actions protects officers from unnecessary litigation and accords with this Court's wise "policy of avoiding the unnecessary adjudication of constitutional questions." <i>County of Sacramento</i> v. <i>Lewis,</i> <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#859" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833, 859</a></span> (1998) (STEVENS, J., concurring in judgment). When, however, the applicable constitutional rule is well settled, "we should address the constitutional question at the outset." <i>Ibid.;</i> see also <i>Siegert</i> v. <i>Gilley,</i> <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/" aria-description="Citation for case: Siegert v. Gilley">500 U. S. 226</a></span> (1991). The constitutional limits on the use of deadly force have been clearly established for almost two decades.</p>
<p><span class="star-pagination">*203</span> In 1985, we held that the killing of an unarmed burglar to prevent his escape was an unconstitutional seizure. <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span>. We considered, and rejected, the State's contention that the Fourth Amendment's prohibition against unreasonable seizures should be construed in light of the common-law rule, which allowed the use of whatever force was necessary to effectuate the arrest of a fleeing felon. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#12" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 12-13</a></span>. We recognized that the common-law rule had been fashioned "when virtually all felonies were punishable by death" and long before guns were available to the police, and noted that modern police departments in a majority of large cities allowed the firing of a weapon only when a felon presented a threat of death or serious bodily harm. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#13" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 13-19</a></span>. We concluded that "changes in the legal and technological context" had made the old rule obsolete. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#15" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 15</a></span>.</p>
<p>Unlike most "excessive force" cases in which the degree of permissible force varies widely from case to case, the only issue in a "deadly force" case is whether the facts apparent to the officer justify a decision to kill a suspect in order to prevent his escape.</p>
<p>In <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> we stated the governing rule:</p>
<blockquote>"The use of deadly force to prevent the escape of all felony suspects, whatever the circumstances, is constitutionally unreasonable. It is not better that all felony suspects die than that they escape. Where the suspect poses no immediate threat to the officer and no threat to others, the harm resulting from failing to apprehend him does not justify the use of deadly force to do so.... A police officer may not seize an unarmed, nondangerous suspect by shooting him dead....</blockquote>
<blockquote>"Where the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force. Thus, if the suspect threatens the officer with a weapon or <span class="star-pagination">*204</span> there is probable cause to believe that he has committed a crime involving the infliction or threatened infliction of serious physical harm, deadly force may be used if necessary to prevent escape, and if, where feasible, some warning has been given." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 11-12</a></span>.</blockquote>
<p>The most common justifications for the use of deadly force are plainly inapplicable to this case. Respondent Haugen had not threatened anyone with a weapon, and petitioner Brosseau did not shoot in order to defend herself.<sup>[1]</sup> Haugen was not a person who had committed a violent crime; nor was there any reason to believe he would do so if permitted to escape. Indeed, there is nothing in the record to suggest he intended to harm anyone.<sup>[2]</sup> The "threat of serious physical harm, either to the officer or to others," <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 11</a></span>, that provides the sole justification for Brosseau's use of deadly force was the risk that while fleeing in his vehicle Haugen would accidentally collide with a pedestrian or another vehicle. Whether Brosseau's shot enhanced or minimized that risk is debatable, but the risk of such an accident surely did <span class="star-pagination">*205</span> not justify an attempt to kill the fugitive.<sup>[3]</sup> Thus, I have no difficulty in endorsing the Court's assumption that Brosseau's conduct violated the Constitution.</p>
<p></p>
<h2>II</h2>
<p>An officer is entitled to qualified immunity, despite having engaged in constitutionally deficient conduct, if, in doing so, she did not violate "clearly established statutory or constitutional rights of which a reasonable person would have known." <i>Harlow,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>. The requirement that the law be clearly established is designed to ensure that officers have fair notice of what conduct is proscribed. See <i>Hope</i> v. <i>Pelzer,</i> <span class="citation" data-id="9434318"><a href="/opinion/121169/hope-v-pelzer/#739" aria-description="Citation for case: Hope v. Pelzer">536 U. S. 730, 739</a></span> (2002). Accordingly, we have recognized that "general statements of the law are not inherently incapable of giving fair and clear warning," <i>United States</i> v. <i>Lanier,</i> <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#271" aria-description="Citation for case: United States v. Lanier">520 U. S. 259, 271</a></span> (1997), and have firmly rejected the notion that "an official action is protected by qualified immunity unless the very action in question has previously been held unlawful," <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 640</a></span> (1987).</p>
<p>Thus, the Court's search for relevant case law applying the <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> standard to materially similar facts is both unnecessary and ill advised. See <i>Hope,</i> <span class="citation" data-id="9434318"><a href="/opinion/121169/hope-v-pelzer/#741" aria-description="Citation for case: Hope v. Pelzer">536 U. S., at 741</a></span> ("Although earlier cases involving `fundamentally similar' facts can provide especially strong support for a conclusion that the law is clearly established, they are not necessary to such a finding"); see also <i>Lanier,</i> <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#269" aria-description="Citation for case: United States v. Lanier">520 U. S., at 269</a></span>. Indeed, the cases the majority relies on are inapposite and, in fact, only serve <span class="star-pagination">*206</span> to illuminate the patent unreasonableness of Brosseau's actions.<sup>[4]</sup></p>
<p>Rather than uncertainty about the law, it is uncertainty about the likely consequences of Haugen's flight  or, more precisely, uncertainty about how a reasonable officer making the split-second decision to use deadly force would have assessed the foreseeability of a serious accident  that prevents me from answering the question of qualified immunity that this case presents. This is a quintessentially "fact-specific" question, not a question that judges should try to answer "as a matter of law." Cf. <i>Anderson,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 641</a></span>. Although it is preferable to resolve the qualified immunity question at the earliest possible stage of litigation, this preference does not give judges license to take inherently factual questions away from the jury. See <i>Hunter</i> v. <i>Bryant,</i> <span class="citation" data-id="9432435"><a href="/opinion/112671/hunter-v-bryant/#229" aria-description="Citation for case: Hunter v. Bryant">502 U. S. 224, 229</a></span> (1991) <i>(per curiam)</i> (SCALIA, J., concurring in judgment); <span class="citation" data-id="9432435"><a href="/opinion/112671/hunter-v-bryant/#233" aria-description="Citation for case: Hunter v. Bryant"><i>id.,</i> at 233</a></span> (STEVENS, J., dissenting) ("`Whether <span class="star-pagination">*207</span> a reasonable officer could have believed he had probable cause is a question for the trier of fact, and summary judgment or a directed verdict in a § 1983 action based on [the] lack of probable cause is proper only if there is only one reasonable conclusion a jury could reach'" (quoting <i>Bryant</i> v. <i>U. S. Treasury Dept., Secret Service,</i> <span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#721" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury...">903 F. 2d 717, 721</a></span> (CA9 1990))). The bizarre scenario described in the record of this case convinces me that reasonable jurors could well disagree about the answer to the qualified immunity issue. My conclusion is strongly reinforced by the differing opinions expressed by the Circuit Judges who have reviewed the record.</p>
<p></p>
<h2>III</h2>
<p>The Court's attempt to justify its decision to reverse the Court of Appeals without giving the parties an opportunity to provide full briefing and oral argument is woefully unpersuasive. If Brosseau had deliberately shot Haugen in the head and killed him, the legal issues would have been the same as those resulting from the nonfatal wound. I seriously doubt that my colleagues would be so confident about the result as to decide the case without the benefit of briefs or argument on such facts.<sup>[5]</sup> At a minimum, the Ninth Circuit's decision was not clearly erroneous, and the extraordinary remedy of summary reversal is not warranted on these facts. See R. Stern, E. Gressman, &amp; S. Shapiro, Supreme Court Practice 281 (6th ed. 1986).</p>
<p>In sum, the constitutional limits on an officer's use of deadly force have been well settled in this Court's jurisprudence for nearly two decades, and, in this case, Officer Brosseau acted outside of those clearly delineated bounds. <span class="star-pagination">*208</span> Nonetheless, in my judgment, there is a genuine factual question as to whether a reasonably well-trained officer standing in Brosseau's shoes could have concluded otherwise, and that question plainly falls with the purview of the jury.</p>
<p>For these reasons, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  Haugen also asserted pendent state-law claims and claims against the city and police department. These claims are not presently before us.</p>
<p>[2]  Because this case arises in the posture of a motion for summary judgment, we are required to view all facts and draw all reasonable inferences in favor of the nonmoving party, Haugen. See <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201 (2001).</p>
<p>[3]  We have no occasion in this case to reconsider our instruction in <i>Saucier</i> v. <i>Katz, supra</i><i>,</i> that lower courts decide the constitutional question prior to deciding the qualified immunity question. We exercise our summary reversal procedure here simply to correct a clear misapprehension of the qualified immunity standard.</p>
<p>[4]  The parties point us to a number of other cases in this vein that postdate the conduct in question, <i>i. e.,</i> Brosseau's February 21, 1999, shooting of Haugen. See <i>Cowan ex rel. Estate of Cooper</i> v. <i>Breen,</i> <span class="citation" data-id="784483"><a href="/opinion/784483/margaret-cowan-administratrix-of-the-estate-of-victoria-cooper-v-michael/#763" aria-description="Citation for case: Margaret Cowan, Administratrix of the Estate of Victoria...">352 F. 3d 756, 763</a></span> (CA2 2003); <i>Pace</i> v. <i>Capobianco,</i> <span class="citation" data-id="7009807"><a href="/opinion/7103965/pace-v-capobianco/#1281" aria-description="Citation for case: Pace v. Capobianco">283 F. 3d 1275, 1281-1282</a></span> (CA11 2002); <i>Scott</i> v. <i>Clay County,</i> <span class="citation" data-id="9492855"><a href="/opinion/767897/patricia-scott-v-clay-county-tennessee-chinn-anderson-billy-pierce/#877" aria-description="Citation for case: Patricia Scott v. Clay County, Tennessee Chinn Anderson...">205 F. 3d 867, 877</a></span> (CA6 2000); <i>McCaslin</i> v. <i>Wilkins,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/183/775/">183 F. 3d 775</a></span>, 778-779 (CA8 1999); <i>Abraham</i> v. <i>Raso,</i> <span class="citation" data-id="765106"><a href="/opinion/765106/vanessa-abraham-in-her-own-right-and-as-administratrix-of-the-estate-of/#288" aria-description="Citation for case: Vanessa Abraham, in Her Own Right and as Administratrix...">183 F. 3d 279, 288-296</a></span> (CA3 1999). These decisions, of course, could not have given fair notice to Brosseau and are of no use in the clearly established inquiry.</p>
<p>[1]  Although Brosseau attested that she believed Haugen may have been attempting to retrieve a weapon from the floorboard of his vehicle sometime during the struggle, a fact which Haugen hotly contests, there is no evidence in the record to suggest that, at the time the shot was fired, Brosseau believed, or any reasonable officer would have thought, that Haugen had access to a weapon at that moment.</p>
<p>[2]  At the time of the shooting, Brosseau had the following facts at her disposal. Haugen had a felony no-bail warrant for a nonviolent drug offense, was suspected in a nonviolent burglary, and had been fleeing from law enforcement on foot for approximately 30 to 45 minutes without incident. At the behest of Brosseau, the private individuals on the scene were inside their respective vehicles. Haugen's girlfriend and her daughter were in a small car approximately four feet in front and slightly to the right of Haugen's Jeep; Glen Tamburello and Matt Atwood were inside a pickup truck on the street blocking the driveway, approximately 20 to 30 feet from Haugen's Jeep. The only two police officers on foot at the scene were last seen in a neighbor's backyard, two houses down and to the right of the driveway.</p>
<p>[3]  The evidence supporting Haugen's allegation that Brosseau did "willfully fire her weapon with the intent to murder me," 1 Record, Doc. No. 1, includes a statement by a defense expert that Brosseau had "clearly articulated her intention to use deadly force," <i><span class="citation" data-id="765106"><a href="/opinion/765106/vanessa-abraham-in-her-own-right-and-as-administratrix-of-the-estate-of/" aria-description="Citation for case: Vanessa Abraham, in Her Own Right and as Administratrix...">id.,</a></span></i> Doc. No. 24. Moreover, the report of the Puyallup, Washington, Police Department Firearms Review Board stated that Brosseau "chose to use deadly force to stop Haugen." 2 <i><span class="citation" data-id="765106"><a href="/opinion/765106/vanessa-abraham-in-her-own-right-and-as-administratrix-of-the-estate-of/" aria-description="Citation for case: Vanessa Abraham, in Her Own Right and as Administratrix...">id.,</a></span></i> Doc. No. 27, Exh. H.</p>
<p>[4]  In <i>Cole</i> v. <i>Bone,</i> <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/" aria-description="Citation for case: Cole v. Bone">993 F. 2d 1328</a></span> (CA8 1993), an 18-wheel tractor-trailer sped through a tollbooth and engaged the police in a high-speed pursuit in excess of 90 miles per hour on a high-traffic interstate during the holiday season. During the course of the pursuit, the driver passed traffic on both shoulders of the interstate, repeatedly attempted to ram several police cars, drove more than 100 passenger vehicles off the road, ran through several roadblocks, and continued driving after the officer shot out the wheels of the fugitive's truck. <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/#1330" aria-description="Citation for case: Cole v. Bone"><i>Id.,</i> at 1330-1331</a></span>. Only then did the officer finally resort to deadly force to disable the driver. Similarly, in <i>Smith</i> v. <i>Freland,</i> <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">954 F. 2d 343</a></span> (CA6 1992), the suspect led a police officer on a high-speed chase, reaching speeds in excess of 90 miles per hour. When the officer initially cornered the suspect in a field, the driver repeatedly swerved directly toward the police car, forcing the officer to move out of the way and allowing the suspect to continue the chase. <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/#344" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the..."><i>Id.,</i> at 344</a></span>. Only after additional officers cornered the suspect for a second time, and after the suspect smashed directly into an unoccupied police car and began to flee again, did the officer finally shoot the driver. <i><span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">Ibid.</a></span></i>
</p>
<p>In stark contrast, at the time Brosseau shot Haugen, the Jeep was immobile, or at best, had just started moving. Haugen had not driven at excess speeds; nor had he rammed, or attempted to ram, nearby police cars or passenger vehicles. In sum, there was no ongoing or prior high-speed car chase to inform the probable-cause analysis.</p>
<p>[5]  The Court's recitation of the facts that led up to the shooting obscures the undisputed point that no one contends Haugen was the kind of dangerous person  perhaps a terrorist or an escaped convict on a crime spree  who would have been a danger to the community if he had been allowed to escape. The factual issues relate only to the danger that he posed while in the act of escaping.</p>

</div>
```

---
