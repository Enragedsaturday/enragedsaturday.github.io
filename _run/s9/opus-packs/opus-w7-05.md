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

## GROUP: _overhaul2/lake/cases/Maryland v. Wilson.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Maryland v. Wilson"
type: case
citation: "519 U.S. 408 (1997)"
parallel_cite: "117 S. Ct. 882; 137 L. Ed. 2d 41"
neutral_cite: 1997 U.S. LEXIS 1271
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1997
date_decided: 1997-02-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1997-02-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Wilson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118086/maryland-v-wilson/"
  cluster_id: 118086
  opinion_id: 118086
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
related: ["[[Pennsylvania v. Mimms]]", "[[Brendlin v. California]]", "[[Arizona v. Johnson]]", "[[Rodriguez v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stops", "passengers", "officer-safety", "order-out"]
holding: "Mimms extends to passengers: an officer making a lawful traffic stop may order the passengers, as well as the driver, out of the car…"
lake:
  record_id: Maryland v. Wilson
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Wilson

*519 U.S. 408 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Maryland trooper stopped a speeding car with three occupants. While the driver produced his license, the front-seat passenger, Wilson, was sweating and nervous; when ordered out of the car, he dropped a quantity of crack cocaine. Wilson argued the order to exit was an unreasonable seizure because, unlike the driver in *[[Pennsylvania v. Mimms]]*, he was a mere passenger.

## Issue
Whether the rule of *[[Pennsylvania v. Mimms]]* — that an officer may order the driver out of a lawfully stopped vehicle — extends to passengers.

## Rule
Yes. "We therefore hold that an officer making a traffic stop may order passengers to get out of the car pending completion of the stop." — 519 U.S. at 415. ^pin-415

The danger to an officer is likely greater when there are passengers as well as a driver, and while the justification for ordering passengers out is not identical to that for the driver, the additional intrusion on a passenger already stopped is minimal.

## Application
The trooper had lawfully stopped the car for speeding, so Wilson was already lawfully detained by the stop. Ordering him, as a passenger, to step out pending completion of the stop was at most a minimal additional intrusion, justified by the heightened officer-safety concerns that the presence of passengers creates. The order to exit was therefore reasonable, and the cocaine Wilson dropped was lawfully obtained.

## Conclusion
Reversed: an officer making a lawful traffic stop may order passengers, as well as the driver, out of the vehicle for the duration of the stop.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Wilson* extends [[Pennsylvania v. Mimms]] from drivers to passengers and sits alongside later traffic-stop authority recognizing that passengers are seized by the stop ([[Brendlin v. California]]) and may be subject to safety measures ([[Arizona v. Johnson]]); it remains good law.

## Appears on
- [[Traffic Stops]] — *Key — Progeny / Refinement*

## Sources
- *Maryland v. Wilson*, 519 U.S. 408 (1997) — https://www.courtlistener.com/opinion/118086/maryland-v-wilson/ — pinpoint: 415.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9ebd8f5cf5eaccff", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. Wilson"}, "payload": {"all": [{"cite": "519 U.S. 408", "page": "408", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "519"}, {"cite": "117 S. Ct. 882", "page": "882", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "117"}, {"cite": "137 L. Ed. 2d 41", "page": "41", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "1997 U.S. LEXIS 1271", "page": "1271", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1997"}], "display": "519 U.S. 408", "official": {"cite": "519 U.S. 408", "page": "408", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "519"}, "official_selection_present": true, "record_id": "Maryland v. Wilson"}}
{"assertion_id": "8bdcf9716f7fc70a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-415", "record_id": "Maryland v. Wilson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-415", "pinpoint_status": "slip-only", "quote": "--- # Maryland v. Wilson *519 U.S. 408 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Maryland trooper stopped a speeding car with three occupants. While the driver produced his license, the front-seat passenger, Wilson, was sweating and nervous; when ordered out of the car, he dropped a quantity of crack cocaine. Wilson argued the order to exit was an unreasonable seizure because, unlike the driver in *Pennsylvania v. Mimms*, he was a mere passenger. ## Issue Whether the rule of *Pennsylvania v. Mimms* — that an officer may order the driver out of a lawfully stopped vehicle — extends to passengers. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Maryland v. Wilson", "star_marker": null}}
{"assertion_id": "6eda12838d514d3f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. Wilson"}, "payload": {"as_of_content": "1997-02-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. Wilson", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Maryland v. Wilson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Wilson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Wilson",
    "case_name_short": "Wilson",
    "case_name_full": "Maryland v. Wilson",
    "input_case_name": "Maryland v. Wilson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-02-19",
    "year": 1997,
    "docket": null,
    "cluster_id": 118086,
    "lead_opinion_id": 118086,
    "sibling_ids": [
      118086,
      9433418,
      9433419,
      9433420
    ],
    "absolute_url": "/opinion/118086/maryland-v-wilson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "519 U.S. 408",
      "volume": "519",
      "reporter": "U.S.",
      "page": "408",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 882",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "882",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 41",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "41",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 1271",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "1271",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "519 U.S. 408",
        "volume": "519",
        "reporter": "U.S.",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 882",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "882",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 41",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "41",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 1271",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "1271",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "519 U.S. 408",
    "official_selection": {
      "court_class": "scotus",
      "selected": "519 U.S. 408",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-415",
      "page": null,
      "quote": "--- # Maryland v. Wilson *519 U.S. 408 (1997)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Maryland trooper stopped a speeding car with three occupants. While the driver produced his license, the front-seat passenger, Wilson, was sweating and nervous; when ordered out of the car, he dropped a quantity of crack cocaine. Wilson argued the order to exit was an unreasonable seizure because, unlike the driver in *Pennsylvania v. Mimms*, he was a mere passenger. ## Issue Whether the rule of *Pennsylvania v. Mimms* \u2014 that an officer may order the driver out of a lawfully stopped vehicle \u2014 extends to passengers. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1997-02-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Wilson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4786330,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lerma v. State",
          "cluster_id": 6241263,
          "cite": [
            "543 S.W.3d 184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Amado",
          "cluster_id": 3195514,
          "cite": [
            "474 Mass. 147",
            "48 N.E.3d 414"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane1_negative"
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
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
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
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muehler v. Mena",
          "cluster_id": 142878,
          "cite": [
            "161 L. Ed. 2d 299",
            "125 S. Ct. 1465",
            "544 U.S. 93",
            "2005 U.S. LEXIS 2755"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mendoza Tello",
          "cluster_id": 1375527,
          "cite": [
            "15 Cal. 4th 264",
            "62 Cal. Rptr. 2d 437",
            "933 P.2d 1134",
            "97 Cal. Daily Op. Serv. 2823",
            "97 Daily Journal DAR 4991",
            "1997 Cal. LEXIS 1567"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez-Barragan",
          "cluster_id": 4260741,
          "cite": [
            "2016 CO 66",
            "379 P.3d 330",
            "2016 WL 5375502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
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
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bryan v. MacPherson",
          "cluster_id": 148934,
          "cite": [
            "630 F.3d 805"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chapo",
          "cluster_id": 2197767,
          "cite": [
            "770 N.W.2d 68",
            "283 Mich. App. 360"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Bennett v. City of Eastpointe",
          "cluster_id": 790530,
          "cite": [
            "410 F.3d 810",
            "2005 U.S. App. LEXIS 10587",
            "2005 WL 1384366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez Ex Rel. Gonzalez v. City of Anaheim",
          "cluster_id": 2658912,
          "cite": [
            "747 F.3d 789",
            "2014 WL 1274551",
            "2014 U.S. App. LEXIS 5895"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Harmon",
          "cluster_id": 4670342,
          "cite": [
            "2019 COA 156"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. City of Shreveport",
          "cluster_id": 37439,
          "cite": [
            "397 F.3d 287",
            "2005 U.S. App. LEXIS 589",
            "2005 WL 67028"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corbin v. State",
          "cluster_id": 1588733,
          "cite": [
            "85 S.W.3d 272",
            "2002 Tex. Crim. App. LEXIS 116",
            "2002 WL 1174569"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Dayton Holt",
          "cluster_id": 774866,
          "cite": [
            "264 F.3d 1215",
            "2001 Colo. J. C.A.R. 4452",
            "2001 U.S. App. LEXIS 19759",
            "2001 WL 1013251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lomax",
          "cluster_id": 2512057,
          "cite": [
            "234 P.3d 377",
            "49 Cal. 4th 530",
            "112 Cal. Rptr. 3d 96",
            "2010 Cal. LEXIS 6017"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derrick Newman v. James Guedry",
          "cluster_id": 3071815,
          "cite": [
            "703 F.3d 757",
            "2012 U.S. App. LEXIS 26205",
            "2012 WL 6634975"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Reppert",
          "cluster_id": 2258199,
          "cite": [
            "814 A.2d 1196",
            "2002 Pa. Super. 383",
            "2002 Pa. Super. LEXIS 3779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
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
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ferreira",
          "cluster_id": 1196184,
          "cite": [
            "988 P.2d 700",
            "133 Idaho 474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Acosta-Colon",
          "cluster_id": 198134,
          "cite": [
            "157 F.3d 9",
            "1998 U.S. App. LEXIS 24862",
            "1998 WL 671324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Wilson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118086 OR 9433418 OR 9433419 OR 9433420) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDM0MzI2NDAwMDAwJnM9NDI3MDA4MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118086+OR+9433418+OR+9433419+OR+9433420%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118086 OR 9433418 OR 9433419 OR 9433420)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkmcz0yNTIxNDUzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118086+OR+9433418+OR+9433419+OR+9433420%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118086 OR 9433418 OR 9433419 OR 9433420)",
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
    "complete_query": "cites:(118086 OR 9433418 OR 9433419 OR 9433420)",
    "indexed_citing_opinions": 892,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118086,
        "count": 720,
        "count_source": "search"
      },
      {
        "opinion_id": 9433418,
        "count": 183,
        "count_source": "search"
      },
      {
        "opinion_id": 9433419,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433420,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1557,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-wilson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMjIyNzUmcz0xMDY4MDU5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118086+OR+9433418+OR+9433419+OR+9433420%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118086,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 111471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118086,
        "cited_id": 118036,
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
    "date_created": "2026-07-05T12:16:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:17:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:17:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:20:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:17:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Wilson

```
<div>
<center><b><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">519 U.S. 408</a></span> (1997)</b></center>
<center><h1>MARYLAND<br>
v.<br>
WILSON</h1></center>
<center>No. 95-1268.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued December 11, 1996.</center>
<center>Decided February 19, 1997.</center>
CERTIORARI TO THE COURT OF SPECIAL APPEALS OF MARYLAND
<p><span class="star-pagination">*409</span> Rehnquist, C. J., delivered the opinion of the Court, in which O'Connor, Scalia, Souter, Thomas, Ginsburg, and Breyer, JJ., joined. Stevens, J., filed a dissenting opinion, in which Kennedy, J., joined, <i>post,</i>  p. 415. Kennedy, J., filed a dissenting opinion, <i>post,</i> p. 422.</p>
<p><i>J. Joseph Curran, Jr.,</i> Attorney General of Maryland, argued the cause for petitioner. With him on the briefs were <i>Gary E. Bair, Mary Ellen Barbera,</i> and <i>Kathryn Grill Graeff,</i> Assistant Attorneys General.</p>
<p><i>Byron L. Warnken,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./519/804/">519 U. S. 804</a></span> (1996), argued the cause and filed a brief for respondent.</p>
<p><i>Attorney General Reno</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Acting Solicitor General Dellinger, Acting Assistant Attorney General Keeney, Deputy Solicitor General Dreeben, David C. Frederick,</i> and <i>Nina Goodman.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*410</span> Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>In this case we consider whether the rule of <i>Pennsylvania</i>  v.<i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106</a></span> (1977) <i>(per curiam)</i><i>,</i> that a police officer may as a matter of course order the driver of a lawfully stopped car to exit his vehicle, extends to passengers as well. We hold that it does.</p>
<p>At about 7:30 p.m. on a June evening, Maryland state trooper David Hughes observed a passenger car driving southbound on I-95 in Baltimore County at a speed of 64 miles per hour. The posted speed limit was 55 miles per hour, and the car had no regular license tag; there was a torn piece of paper reading "Enterprise Rent-A-Car" dangling from its rear. Hughes activated his lights and sirens, signaling the car to pull over, but it continued driving for another mile and a half until it finally did so.</p>
<p>During the pursuit, Hughes noticed that there were three occupants in the car and that the two passengers turned to look at him several times, repeatedly ducking below sight level and then reappearing. As Hughes approached the car on foot, the driver alighted and met him halfway. The driver was trembling and appeared extremely nervous, but nonetheless produced a valid Connecticut driver's license. Hughes instructed him to return to the car and retrieve the rental documents, and he complied. During this encounter, Hughes noticed that the front-seat passenger, respondent Jerry Lee Wilson, was sweating and also appeared extremely <span class="star-pagination">*411</span> nervous. While the driver was sitting in the driver's seat looking for the rental papers, Hughes ordered Wilson out of the car.</p>
<p>When Wilson exited the car, a quantity of crack cocaine fell to the ground. Wilson was then arrested and charged with possession of cocaine with intent to distribute. Before trial, Wilson moved to suppress the evidence, arguing that Hughes' ordering him out of the car constituted an unreasonable seizure under the Fourth Amendment. The Circuit Court for Baltimore County agreed, and granted respondent's motion to suppress. On appeal, the Court of Special Appeals of Maryland affirmed, <span class="citation" data-id="7926611"><a href="/opinion/7974104/state-v-wilson/" aria-description="Citation for case: State v. Wilson">106 Md. App. 24</a></span>, <span class="citation" data-id="7926611"><a href="/opinion/7974104/state-v-wilson/" aria-description="Citation for case: State v. Wilson">664 A. 2d 1</a></span> (1995), ruling that <i>Pennsylvania</i> v. <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span></i> does not apply to passengers. The Court of Appeals of Maryland denied certiorari. <span class="citation no-link">340 Md. 502</span>, <span class="citation no-link">667 A. 2d 342</span> (1995). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./518/1003/">518 U. S. 1003</a></span> (1996), and now reverse.</p>
<p>In <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>,</i> we considered a traffic stop much like the one before us today. There, Mimms had been stopped for driving with an expired license plate, and the officer asked him to step out of his car. When Mimms did so, the officer noticed a bulge in his jacket that proved to be a .38-caliber revolver, whereupon Mimms was arrested for carrying a concealed deadly weapon. Mimms, like Wilson, urged the suppression of the evidence on the ground that the officer's ordering him out of the car was an unreasonable seizure, and the Pennsylvania Supreme Court, like the Court of Special Appeals of Maryland, agreed.</p>
<p>We reversed, explaining that "[t]he touchstone of our analysis under the Fourth Amendment is always `the reasonableness in all the circumstances of the particular governmental invasion of a citizen's personal security,' " 434 U. S., at 108 109 (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968)), and that reasonableness "depends `on a balance between the public interest and the individual's right to personal security free from arbitrary interference by law officers,' " <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S., at 109</a></span> (quoting <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, <span class="star-pagination">*412</span> 878 (1975)). On the public interest side ofthe balance, we noted that the State "freely concede[d]" that there had been nothing unusual or suspicious to justify ordering Mimms out of the car, but that it was the officer's "practice to order all drivers [stopped in traffic stops] out of their vehicles as a matter of course" as a "precautionary measure" to protect the officer's safety. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S., at 109-110</a></span>. We thought it "too plain for argument" that this justificationofficer safetywas "both legitimate and weighty." <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Id.,</i> at 110</a></span>. In addition, we observed that the danger to the officer of standing by the driver's door and in the path of oncoming traffic might also be "appreciable." <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#111" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Id.,</i> at 111</a></span>.</p>
<p>On the other side of the balance, we considered the intrusion into the driver's liberty occasioned by the officer's ordering him out of the car. Noting that the driver's car was already validly stopped for a traffic infraction, we deemed the additional intrusion of asking him to step outside his car "<i>de minimis.</i> " <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Ibid.</a></span></i> Accordingly, we concluded that "once a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment's proscription of unreasonable seizures." <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Id.,</a></span></i> at111, n. 6.</p>
<p>Respondent urges, and the lower courts agreed, that this <i>per se</i> rule does not apply to Wilson because he was a passenger, not the driver. Maryland, in turn, argues that we have already implicitly decided this question by our statement in <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), that "[i]n [<span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Mimms</i></a></span> ], we held that police may order <i>persons</i> out of an automobile during astop for a traffic violation," <i>id.,</i> at 1047-1048 (emphasis added), and by Justice Powell's statement in <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978), that "this Court determined in [<span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Mimms</i></a></span> ] that <i>passengers</i> in automobiles have no Fourth Amendment right not to be ordered from their vehicle, once a proper stop is made," <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#155" aria-description="Citation for case: Pennsylvania v. Mimms"><i>id.,</i> at 155, n. 4</a></span> (Powell, J., joined by Burger, C. J., concurring) (emphasis added). We agree with respondent that the former statement was dictum, and the <span class="star-pagination">*413</span> latter was contained in a concurrence, so that neither constitutes binding precedent.</p>
<p>We must therefore now decide whether the rule of <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span></i>  applies to passengers as well as to drivers.<sup>[1]</sup> On the public interest side of the balance, the same weighty interest in officer safety is present regardless of whether the occupant of the stopped car is a driver or passenger. Regrettably, traffic stops may be dangerous encounters. In 1994 alone, there were 5,762 officer assaults and 11 officers killed during traffic pursuits and stops. Federal Bureau of Investigation, Uniform Crime Reports: Law Enforcement Officers Killed and Assaulted 71, 33 (1994). In the case of passengers, the danger of the officer's standing in the path of oncoming traffic would not be present except in the case of a passenger in the left rear seat, but the fact that there is more than one occupant of the vehicle increases the possible sources of harm to the officer.<sup>[2]</sup></p>
<p>On the personal liberty side of the balance, the case for the passengers is in one sense stronger than that for the driver. There is probable cause to believe that the driver has committed a minor vehicular offense, but there is no such reason to stop or detain the passengers. But as a practical <span class="star-pagination">*414</span> matter, the passengers are already stopped by virtue of the stop of the vehicle. The only change in their circumstances which will result from ordering them out of the car is that they will be outside of, rather than inside of, the stopped car. Outside the car, the passengers will be denied access to any possible weapon that might be concealed in the interior of the passenger compartment. It would seem that the possibility of a violent encounter stems not from the ordinary reaction ofa motorist stopped for a speeding violation, but from the fact that evidence of a more serious crime might be uncovered during the stop. And the motivation of a passenger to employ violence to prevent apprehension of such a crime is every bit as great as that of the driver.</p>
<p>We think that our opinion in <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692</a></span> (1981), offers guidance by analogy here. There the police had obtained a search warrant for contraband thought to be located in a residence, but when they arrived to execute the warrant they found Summers coming down the front steps. The question in the case depended "upon a determination whether the officers had the authority to require him to re-enter the house and toremain there while they conducted their search." <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Id.,</a></span></i> at695. In holding as it did, the Court said:</p>
<blockquote>"Although no special danger to the police is suggested by the evidence in this record, the execution of a warrant to search for narcotics is the kind of transaction that may give rise to sudden violence or frantic efforts to conceal or destroy evidence. The risk of harm to both the police and the occupants is minimized if the officers routinely exercise unquestioned command of the situation." <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><i>Id.,</i> at 702-703</a></span> (footnote omitted).</blockquote>
<p>In summary, danger to an officer from a traffic stop is likely to be greater when there are passengers in addition to the driver in the stopped car. While there is not the same basis for ordering the passengers out of the car as there is <span class="star-pagination">*415</span> for ordering the driver out, the additional intrusion on the passenger is minimal. We therefore hold that an officer making a traffic stop may order passengers to get out of the car pending completion of the stop.<sup>[3]</sup></p>
<p>The judgment of the Court of Special Appeals of Maryland is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Stevens, with whom Justice Kennedy joins, dissenting.</p>
<p>In <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106</a></span> (1977) <i>(per curiam)</i><i>,</i> the Court answered the "narrow question" whether an "incremental intrusion" on the liberty of a person who had been lawfully seized was reasonable. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Id.,</i> at 109</a></span>. This case, in contrast, raises a separate and significant question concerning the power of the State to make an initial seizure of persons who are not even suspected of having violated the law.</p>
<p>My concern is not with the ultimate disposition of this particular case, but rather with the literally millions of other cases that will be affected by the rule the Court announces. Though the question is not before us, I am satisfied that under the rationale of <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968)if a police officer conducting a traffic stop has an articulable suspicion of possible danger, the officer may order passengers to exit the vehicle as a defensive tactic without running afoul of the Fourth Amendment. Accordingly, I assume that the facts recited in the majority's opinion provided a valid justification <span class="star-pagination">*416</span> for this officer's order commanding the passengers to get out of thisvehicle.<sup>[1]</sup> But the Court's ruling goes much further. It applies equally to traffic stops in which there is not even a scintilla of evidence of any potential risk to the police officer. In those cases, I firmly believe that the Fourth Amendment prohibits routine and arbitrary seizures of obviously innocent citizens.</p>
<p></p>
<h2>I</h2>
<p>The majority suggests that the personal liberty interest at stake here, which is admittedly "stronger" than that at issue in <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>,</i> is outweighed by the need to ensure officer safety. <i>Ante,</i> at 413, 414-415. The Court correctly observes that "traffic stops may be dangerous encounters." <i>Ante,</i> at 413. The magnitude of the danger to police officers is reflected in the statistic that, in 1994 alone, "there were 5,762 officer assaults and 11 officers killed during traffic pursuits and stops." <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Ibid.</a></span></i> There is, unquestionably, a strong public interest in minimizing the number of such assaults and fatalities. The Court's statistics, however, provide no support for the conclusion that its ruling will have any such effect.</p>
<p>Those statistics do not tell us how many of the incidents involved passengers. Assuming that many of the assaults were committed by passengers, we do not know how many occurred after the passenger got out of the vehicle, how many took place while the passenger remained in the vehicle, or indeed, whether any of them could have been prevented <span class="star-pagination">*417</span> by an order commanding the passengers to exit.<sup>[2]</sup> There is no indication that the number of assaults was smaller in jurisdictions where officers may order passengers to exit the vehicle without any suspicion than in jurisdictions where they were then prohibited from doing so. Indeed, there is no indication that any of the assaults occurred when there was a complete absence of any articulable basis for concern about the officer's safetythe only condition under which I would hold that the Fourth Amendment prohibits an order commanding passengers to exit a vehicle. In short, the statistics are as consistent with the hypothesis that ordering passengers to get out of a vehicle increases the danger of assault as with the hypothesis that it reduces that risk.</p>
<p>Furthermore, any limited additional risk to police officers must be weighed against the unnecessary invasion that will be imposed on innocent citizens under the majority's rule in the tremendous number of routine stops that occur each day. We have long recognized that "[b]ecause of the extensive regulation of motor vehicles and traffic . . . the extent of police-citizen contact involving automobiles will be substantially greater than police-citizen contact in a home or office." <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441</a></span> (1973).<sup>[3]</sup> Most traffic <span class="star-pagination">*418</span> stops involve otherwise law-abiding citizens who have committed minor traffic offenses. A strong interest in arriving at a destinationto deliver a patient to a hospital, to witness a kickoff, or to get to work on timewill often explain a traffic violation without justifying it. In the aggregate, these stops amount to significant law enforcement activity.</p>
<p>Indeed, the number of stops in which an officer is actually at risk is dwarfed by the far greater number of routine stops. If Maryland's share of the national total is about average, the State probably experiences about 100 officer assaults each year during traffic stops and pursuits. Making the unlikely assumption that passengers are responsible for onefourth of the total assaults, it appears that the Court's new rule would provide a potential benefit to Maryland officers in only roughly 25 stops a year.<sup>[4]</sup> These stops represent a minuscule portion of the total. In Maryland alone, there are something on the order of one million traffic stops each year.<sup>[5]</sup> Assuming that there are passengers in about half of the cars stopped, the majority's rule is of some possible advantage to police in only about one out of every twenty thousand traffic stops in which there is a passenger in the car. And, any benefit is extremely marginal. In the overwhelming majority of cases posing a real threat, the officer would almost <span class="star-pagination">*419</span> certainly have some ground to suspect danger that would justify ordering passengers out of the car.</p>
<p>In contrast, the potential daily burden on thousands of innocent citizens is obvious. That burden may well be "minimal" in individual cases. <i>Ante,</i> at 415. But countless citizens who cherish individual liberty and are offended, embarrassed, and sometimes provoked by arbitrary official commands may well consider the burden to be significant.<sup>[6]</sup> In all events, the aggregation of thousands upon thousands of petty indignities has an impact on freedom that I would characterize as substantial, and which in my view clearly outweighs the evanescent safety concerns pressed by the majority.</p>
<p></p>
<h2>II</h2>
<p>The Court concludes today that the balance of convenience and danger that supported its holding in <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span></i> applies to passengers of lawfully stopped cars as well as drivers. In <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span></i> itself, however, the Court emphasized the fact that the intrusion into the driver's liberty at stake was "occasioned not by the initial stop of the vehicle, which was admittedly justified, but by the order to get out of the car." <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#111" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S., at 111</a></span>. The conclusion that "this additional intrusion can only be described as <i>de minimis</i> " rested on the premise that the "police have already lawfully decided that the driver shall be briefly detained." <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Ibid.</a></span></i><sup>[7]</sup></p>
<p><span class="star-pagination">*420</span> In this case as well, the intrusion on the passengers' liberty occasioned by the initial stop of the vehicle is not challenged. That intrusion was a necessary by-product of the lawful detention of the driver. But the passengers had not yet been seized at the time the car was pulled over, any more than a traffic jam caused by construction or other stateimposed delay not directed at a particular individual constitutes a seizure of that person. The question iswhether a passenger in a lawfully stopped car may beseized, by an order to get out of the vehicle, without any evidence whatsoever that he or she poses a threat to the officer or has committed an offense.<sup>[8]</sup></p>
<p>To order passengers about during the course of a traffic stop, insisting that they exit and remain outside the car, can hardly be classified as a <i>de minimis</i> intrusion. The traffic violation sufficiently justifies subjecting the driver to detention and some police control forthe time necessary to conclude the business of the stop. The restraint on the liberty of blameless passengers that the majority permits is, in contrast, entirely arbitrary.<sup>[9]</sup></p>
<p>In my view, wholly innocent passengers in a taxi, bus, or private car have a constitutionally protected right to decide whether to remain comfortably seated within the vehicle rather than exposing themselves to the elements and the observation of curious bystanders. The Constitution should not be read to permit law enforcement officers to order innocent passengers about simply because they have the misfortune <span class="star-pagination">*421</span> to be seated in a car whose driver has committed a minor traffic offense.</p>
<p>Unfortunately, the effect of the Court's new rule on the law may turn out to be far more significant than its immediate impact on individual liberty. Throughout most of our history the Fourth Amendment embodied a general rule requiring that official searches and seizures be authorized by a warrant, issued "upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."<sup>[10]</sup> During the prohibition era, the exceptions for warrantless searches supported by probable cause started to replace the general rule.<sup>[11]</sup> In 1968, in the landmark "stop and frisk" case <i>Terry</i>  v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court placed its stamp of approval on seizures supported by specific and articulable facts that did not establish probable cause. The Court crafted <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> as a narrow exception to the general rule that "the police must, whenever practicable, obtain advance judicial approval of searches and seizures through the warrant procedure." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 20</a></span>. The intended scope of the Court's major departure from prior practice was reflected in its statement that the "demand for specificity in the information upon which police action ispredicated is the central teaching of this Court's Fourth Amendment jurisprudence." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 21, n. 18</a></span>; see also <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 27</a></span>. In the 1970's, the Court twice rejected attempts to justify suspicionless seizures that caused only "modest" intrusions on the liberty of passengers in automobiles. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#879" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 879-880</a></span> (1975); <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span>, 662-663 <span class="star-pagination">*422</span> (1979).<sup>[12]</sup> Today, however, the Court takes the unprecedented step of authorizing seizures that are unsupported by any individualized suspicion whatsoever.</p>
<p>The Court's conclusion seems to rest on the assumption that the constitutional protection against "unreasonable" seizures requires nothing more than a hypothetically rational basis for intrusions on individual liberty. How far this ground-breaking decision will take us, I do not venture to predict. I fear, however, that it may pose a more serious threat to individual liberty than the Court realizes.</p>
<p>I respectfully dissent.</p>
<p>Justice Kennedy, dissenting.</p>
<p>I join in the dissent by Justice Stevens and add these few observations.</p>
<p>The distinguishing feature of our criminal justice system is its insistence on principled, accountable decisionmaking in individual cases. If a person is to be seized, a satisfactory explanation for the invasive action ought to be established by an officer who exercises reasoned judgment under all the circumstances of the case. This principle can be accommodated even where officers must make immediate decisions to ensure their own safety.</p>
<p>Traffic stops, even for minor violations, can take upwards of 30 minutes. When an officer commands passengers innocent of any violation to leave the vehicle and stand by the side of the road in full view of the public, the seizure is serious, not trivial. As Justice Stevens concludes, the command to exit ought not to be given unless there are objective circumstances making it reasonable for the officer to issue the order. (We do not have before us the separate question whether passengers, who, after all, are in the car by choice, <span class="star-pagination">*423</span> can be ordered to remain there for a reasonable time while the police conduct their business.)</p>
<p>The requisite showing for commanding passengers to exit need be no more than the existence of any circumstance justifying the order in the interests of the officer's safety or to facilitate a lawful search or investigation. As we have acknowledged for decades, special latitude is given to the police in effecting searches and seizures involving vehicles and their occupants. See, <i>e. g., </i><i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970); <i>New York</i> v. <i>Class,</i> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/" aria-description="Citation for case: New York v. Class">475 U. S. 106</a></span> (1986); <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981). Just last Term we adhered to a rule permitting vehicle stops if there is some objective indication that a violation has been committed, regardless of the officer's real motives. See <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996). We could discern no other, workable rule. Even so, we insisted on a reasoned explanation for the stop.</p>
<p>The practical effect of our holding in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>,</i> of course, is to allow the police to stop vehicles in almost countless circumstances. When <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> is coupled with today's holding, the Court puts tens of millions of passengers at risk of arbitrary control by the police. If the command to exit were to become commonplace, the Constitution would be diminished in a most public way. As the standards suggested in dissent are adequate to protect the safety of the police, we ought not to suffer so great a loss.</p>
<p>Since a myriad of circumstances will give a cautious officer reasonable grounds for commanding passengers to leave the vehicle, it might be thought the rule the Court adopts today will be little different in its operation than the rule offered in dissent. It does no disservice to police officers, however, to insist upon exercise of reasoned judgment. Adherence to neutral principles is the very premise of the rule of law the police themselves defend with such courage and dedication.</p>
<p>Most officers, it might be said, will exercise their new power with discretion and restraint; and no doubt this often <span class="star-pagination">*424</span> will be the case. It might also be said that if some jurisdictions use today's ruling to require passengers to exit as a matter of routine in every stop, citizen complaints and political intervention will call for an end to the practice. These arguments, however, would miss the point. Liberty comes not from officials by grace but from the Constitution by right.</p>
<p>For these reasons, and with all respect for the opinion of the Court, I dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Ohio et al. by <i>Betty D. Montgomery,</i> Attorney General of Ohio, <i>Jeffrey S. Sutton,</i> State Solicitor, and <i>Simon B. Karas</i> and <i>Stuart A. Cole,</i> Assistant Attorneys General, joined by the Attorneys General for their respective jurisdictions as follows: <i>Jeff Sessions</i> of Alabama, <i>Grant Woods</i> of Arizona, <i>Winston Bryant</i> of Arkansas, <i>Daniel E. Lungren</i> of California, <i>Gale A. Norton</i> of Colorado, <i>Richard Blumenthal</i> of Connecticut, <i>M. Jane Brady</i>  of Delaware, <i>Robert Butterworth</i> of Florida, <i>James E. Ryan</i> of Illinois, <i>Tom Miller</i> of Iowa, <i>Carla J. Stovall</i> of Kansas, <i>A. B. Chandler III</i> of Kentucky, <i>Richard P. Ieyoub</i> of Louisiana, <i>Scott Harshbarger</i> of Massachusetts, <i>Frank J. Kelley</i> of Michigan, <i>Hubert Humphrey III</i> of Minnesota, <i>Mike Moore</i> of Mississippi, <i>Joseph P. Mazurek</i> of Montana, <i>Don Stenberg</i>  of Nebraska, <i>Frankie Sue Del Papa</i> of Nevada, <i>Jeffrey R. Howard</i> of New Hampshire, <i>Tom Udall</i> of New Mexico, <i>Dennis C. Vacco</i> of New York, <i>Michael F. Easley</i> of North Carolina, <i>Heidi Heitkamp</i> of North Dakota, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Theodore Kulongoski</i> of Oregon, <i>Thomas Corbett, Jr.,</i> of Pennsylvania, <i>Jeffrey B. Pine</i> of Rhode Island, <i>Charles Condon</i> of South Carolina, <i>Mark W. Barnett</i> of South Dakota, <i>Charles W. Burson</i> of Tennessee, <i>Jan Graham</i> of Utah, <i>Jeffrey L. Amestoy</i>  of Vermont, <i>Julio A. Brady</i> of the U. S. Virgin Islands, <i>Christine O. Gregoire</i> of Washington, <i>Darrell McGraw, Jr.,</i> of West Virginia, and <i>James E. Doyle</i> of Wisconsin; for Americans for Effective Law Enforcement, Inc., et al. by <i>Fred E. Inbau, Wayne W. Schmidt, Robert Wennerholm, James P. Manek, John Kaye, Richard M. Weintraub,</i> and <i>Bernard J. Farber;</i> for the National Association of Police Organizations, Inc., by <i>William J. Johnson;</i> and for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i>  and <i>Charles L. Hobson.</i> </p>
<p>[1]  Respondent argues that, because we have generally eschewed brightline rules in the Fourth Amendment context, see, <i>e. g., Ohio</i> v. <i>Robinette, ante,</i> p. 33, we should not here conclude that passengers may constitutionally be ordered out of lawfully stopped vehicles.But, that we typically avoid <i>per se</i> rules concerningsearches and seizures does not mean that we have always done so; <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span></i> itself drew a bright line, and we believe the principles that underlay that decision apply to passengers as well.</p>
<p>[2]  Justice Stevens' dissenting opinion points out, <i>post,</i> at 416, that these statistics are not further broken down as to assaults by passengers and assaults by drivers.It is, indeed, regrettable that the empirical data on a subject such as this are sparse, but we need not ignore the data which do exist simply because further refinement would be even more helpful. Justice Stevens agrees that there is "a strong public interest in minimizing" the number of assaults on law officers, <i>ibid.,</i> and we believe that our holding today is more likely to accomplish that result than would be the case if his views were to prevail.</p>
<p>[3]  Maryland urges us to go further and hold that an officer may forcibly detaina passenger for theentire duration ofthe stop. But respondent was subjected to no detention based on the stopping of the caronce he had left it; his arrest was based on probable cause to believe that he was guiltyof possession of cocaine with intentto distribute. The question which Maryland wishes answered, therefore, is not presented by this case, and we express no opinion upon it.</p>
<p>[1]  The Maryland Court of Special Appeals held, <i>inter alia,</i> that the State had not properly preserved this claimduring the suppression hearing. See App. to Pet. for Cert. 4a.The State similarly fails to press the point here. Pet.for Cert. 4,n. 1; Brief forPetitioner 4,n. 1. The issue is therefore not before us,and Iam not free to concur inthe Court's judgment on this alternative ground. See <i>Caldwell</i> v. <i>Mississippi,</i> <span class="citation" data-id="111471"><a href="/opinion/111471/caldwell-v-mississippi/#327" aria-description="Citation for case: Caldwell v. Mississippi">472 U. S. 320, 327</a></span> (1985); this Court's Rule 14.1(a).</p>
<p>[2]  Iam assuming that in the typical case the officer would not order passengers out of a vehicle until after he had stopped his own car, exited, and arrived at a position where he could converse with the driver. The only way to avoid all risk to the officer, I suppose, would be to adopt a routine practice of always issuing an order through an amplified speaker commanding everyone to get out of the stopped car before the officer exposed himself to the possibility of a shot from a hidden weapon. Given the predicate for the Court's rulingthat an articulable basis for suspecting danger to the officer provides insufficient protection against the possibility of a surprise assaultwe must assume that every passenger, no matter how feeble or infirm, must be prepared to accept the "petty indignity" of obeying an arbitrary and sometimes demeaning command issued over a loud speaker.</p>
<p>[3]  See also <i>New York</i> v. <i>Class,</i> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#113" aria-description="Citation for case: New York v. Class">475 U. S. 106, 113</a></span> (1986); <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976); cf. <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#810" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 810, 818</a></span> (1996).</p>
<p>[4]  This figure may in fact be smaller. The majority's data aggregate assaults committed during "[t]raffic [p]ursuits and [s]tops." Federal Bureau of Investigation, Uniform Crime Reports: Law Enforcement Officers Killed and Assaulted 71 (1994). In those assaults that occur during the <i>pursuit</i> of a moving vehicle, it would obviously be impossible for an officer to order a passenger out of the car.</p>
<p>[5]  Maryland had well over one million nontort motor vehicle cases during a 1-year period between 1994 and 1995. Annual Report of the Maryland Judiciary 80 (1994-1995). Though the State does not maintain a count of the number of stops performed each year, this figure is probably a fair rough proxy. The bulk of these cases likely represent a traffic stop, and this total does not include those stops in which the police officer simply gave the driver an informal reprimand. I presume that these figures are representative of present circumstances.</p>
<p>[6]  The number of cases in which the command actually protects the officer from harm may well be a good deal smaller than the number in which a passenger isharmed by exposure to inclement weather, as wellas the number in which an ill-advisedcommand is improperly enforced. Consider,forexample, the harm caused toa passenger by an inadequately trained officer after a command was issued to exit the vehicle in <i>Board of Comm'rs of Bryan Cty.</i> v. <i>Brown,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/67/1174/">67 F. 3d 1174</a></span> (CA5 1995), cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./517/1154/">517 U. S. 1154</a></span> (1996).</p>
<p>[7]  Dissenting in <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>,</i> I criticized the Court's reasoning and, indeed, predicted the result that the majority reaches today. 434 U. S.,at 122-123.</p>
<p>[8]  The ordertothe passenger isunquestionably a "seizure" within the meaning ofthe Fourth Amendment. As we held in<i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975): "The Fourth Amendment appliesto allseizuresofthe person, including seizures that involve only a brief detention short of traditional arrest.<i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968)."</p>
<p>[9]  Cf. <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#91" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85, 91</a></span> (1979) ("`[A] person's mere propinquity to others independently suspected of criminal activity does not, without more, give rise to probable cause to search that person' " (citing <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#62" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 62-63</a></span> (1968))).</p>
<p>[10]  See,<i>e. g., </i><i>Amos</i> v.<i>United States,</i> 255U. S.313, 315(1921);<i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span> (1914).</p>
<p>[11]  See, <i>e. g., </i><i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span> (1925) (automobile search). We had also recognized earlier in dictum the now wellestablished doctrine permitting warrantless searches incident to a valid arrest. See <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>,</i> 232 U. S.,at 392; seealso J. Landynski, Search and Seizure and the Supreme Court 87 (1966).</p>
<p>[12]  Dissenting in <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979), then-Justice Rehnquist characterized the motorist's interest in freedom from random stops as "only the most diaphanous of citizen interests." <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#666" aria-description="Citation for case: Delaware v. Prouse"><i>Id.,</i> at 666</a></span>.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Massachusetts v. Sheppard.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Massachusetts v. Sheppard"
type: case
citation: "468 U.S. 981 (1984)"
parallel_cite: "104 S. Ct. 3424; 82 L. Ed. 2d 737; 52 U.S.L.W. 5177"
neutral_cite: 1984 U.S. LEXIS 154
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-07-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Massachusetts v. Sheppard
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111263/massachusetts-v-sheppard/"
  cluster_id: 111263
  opinion_id: 111263
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Illinois v. Krull]]", "[[Herring v. United States]]", "[[Davis v. United States (2011)|Davis v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith", "warrant-defect", "leon"]
holding: "Companion to Leon: where a warrant was technically/clerically defective in form (wrong pre-printed form) but officers reasonably relied…"
lake:
  record_id: Massachusetts v. Sheppard
  status: verified
  projected_at: 2026-07-06
---

# Massachusetts v. Sheppard

*468 U.S. 981 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A detective prepared an affidavit establishing probable cause for a murder investigation but, unable to find a proper form, used a warrant form for controlled substances. He told the judge the form needed changing; the judge said he would make the necessary changes, made some alterations, and signed it. The warrant as issued still described the wrong items (controlled substances). The officers searched and found evidence of the murder, which the defendant sought to suppress because the warrant did not particularly describe the things to be seized.

## Issue
Whether the exclusionary rule bars evidence seized under a warrant that was technically defective in form, where the officers reasonably relied on the issuing judge's assurance that the warrant authorized the requested search.

## Rule
The [[The Good-Faith Exception|good-faith exception]] applies; suppression is not required. "we refuse to rule that an officer is required to disbelieve a judge who has just advised him, by word and by action, that the warrant he possesses authorizes him to conduct the search he has requested." — 468 U.S. at 989–990. ^pin-989

Where the only defect is the judge's failure to make the clerical corrections he assured the officer he would make, the officers' reliance on the warrant was objectively reasonable.

## Application
The detective did everything that could be expected: he established probable cause, brought the form's defect to the judge's attention, and was assured by word and action that the judge would make the warrant conform to the requested search. The sole error — the judge's failure to amend the form's description — was the judge's, not the officers'. Because a reasonable officer would have concluded the warrant authorized the search, the officers' reliance was objectively reasonable, and excluding the evidence would not serve the deterrent purpose of the rule.

## Conclusion
The evidence was admissible under the [[The Good-Faith Exception|good-faith exception]]; suppression was not required for a judge's clerical error on which the officers reasonably relied.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Sheppard* is the companion to [[United States v. Leon]], applying the [[The Good-Faith Exception|good-faith exception]] where the warrant defect is the issuing judge's clerical error. It belongs with the line extending good faith to reliance on a statute ([[Illinois v. Krull]]), on negligent recordkeeping ([[Herring v. United States]]), and on binding precedent ([[Davis v. United States (2011)|Davis v. United States]]).

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Massachusetts v. Sheppard*, 468 U.S. 981 (1984) — https://www.courtlistener.com/opinion/111263/massachusetts-v-sheppard/ — pinpoint: 989–990.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "31a803ac25ea472c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Massachusetts v. Sheppard"}, "payload": {"all": [{"cite": "468 U.S. 981", "page": "981", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "468"}, {"cite": "104 S. Ct. 3424", "page": "3424", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "82 L. Ed. 2d 737", "page": "737", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "82"}, {"cite": "1984 U.S. LEXIS 154", "page": "154", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 5177", "page": "5177", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "468 U.S. 981", "official": {"cite": "468 U.S. 981", "page": "981", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "468"}, "official_selection_present": true, "record_id": "Massachusetts v. Sheppard"}}
{"assertion_id": "81e0fb6dc19df0e3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-989", "record_id": "Massachusetts v. Sheppard"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-989", "pinpoint_status": "slip-only", "quote": "--- # Massachusetts v. Sheppard *468 U.S. 981 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A detective prepared an affidavit establishing probable cause for a murder investigation but, unable to find a proper form, used a warrant form for controlled substances. He told the judge the form needed changing; the judge said he would make the necessary changes, made some alterations, and signed it. The warrant as issued still described the wrong items (controlled substances). The officers searched and found evidence of the murder, which the defendant sought to suppress because the warrant did not particularly describe the things to be seized. ## Issue Whether the exclusionary rule bars evidence seized under a warrant that was technically defective in form, where the officers reasonably relied on the issuing judge's assurance that the warrant authorized the requested search. ## Rule The good-faith exception applies; suppression is not required.", "quote_fidelity": "mismatch", "record_id": "Massachusetts v. Sheppard", "star_marker": null}}
{"assertion_id": "3ee3fbbd5af86582", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Massachusetts v. Sheppard"}, "payload": {"as_of_content": "1984-07-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Massachusetts v. Sheppard", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Massachusetts v. Sheppard

```json
{
  "schema_version": "s2.v1",
  "record_id": "Massachusetts v. Sheppard",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Massachusetts v. Sheppard",
    "case_name_short": "Sheppard",
    "case_name_full": "Massachusetts v. Sheppard",
    "input_case_name": "Massachusetts v. Sheppard",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-05",
    "year": 1984,
    "docket": null,
    "cluster_id": 111263,
    "lead_opinion_id": 111263,
    "sibling_ids": [
      111263
    ],
    "absolute_url": "/opinion/111263/massachusetts-v-sheppard/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9287468,
        "score": 20,
        "case_name": "Massachusetts v. Sheppard"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 981",
      "volume": "468",
      "reporter": "U.S.",
      "page": "981",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3424",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 737",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5177",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5177",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 154",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 981",
        "volume": "468",
        "reporter": "U.S.",
        "page": "981",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3424",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 737",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 154",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5177",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5177",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 981",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 981",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-989",
      "page": null,
      "quote": "--- # Massachusetts v. Sheppard *468 U.S. 981 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A detective prepared an affidavit establishing probable cause for a murder investigation but, unable to find a proper form, used a warrant form for controlled substances. He told the judge the form needed changing; the judge said he would make the necessary changes, made some alterations, and signed it. The warrant as issued still described the wrong items (controlled substances). The officers searched and found evidence of the murder, which the defendant sought to suppress because the warrant did not particularly describe the things to be seized. ## Issue Whether the exclusionary rule bars evidence seized under a warrant that was technically defective in form, where the officers reasonably relied on the issuing judge's assurance that the warrant authorized the requested search. ## Rule The good-faith exception applies; suppression is not required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Massachusetts v. Sheppard",
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
        "journal_ref": "Massachusetts v. Sheppard:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rush",
          "cluster_id": 3164356,
          "cite": [
            "808 F.3d 1007",
            "2015 U.S. App. LEXIS 22212",
            "2015 WL 9269763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kamal Qazah",
          "cluster_id": 3155406,
          "cite": [
            "810 F.3d 879"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Wright",
          "cluster_id": 2777610,
          "cite": [
            "777 F.3d 635",
            "2015 WL 507169",
            "2015 U.S. App. LEXIS 1939"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rose",
          "cluster_id": 2981732,
          "cite": [
            "714 F.3d 362",
            "2013 WL 1664697",
            "2013 U.S. App. LEXIS 7764"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jay Todd Hessman",
          "cluster_id": 786373,
          "cite": [
            "369 F.3d 1016",
            "2004 U.S. App. LEXIS 10612",
            "2004 WL 1191037"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane1_negative"
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
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
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
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Evans",
          "cluster_id": 117905,
          "cite": [
            "131 L. Ed. 2d 34",
            "115 S. Ct. 1185",
            "514 U.S. 1",
            "1995 U.S. LEXIS 1806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bigelow",
          "cluster_id": 5687958,
          "cite": [
            "66 N.Y.2d 417",
            "497 N.Y.S.2d 630",
            "488 N.E.2d 451",
            "1985 N.Y. LEXIS 17919"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Edmunds",
          "cluster_id": 2316698,
          "cite": [
            "586 A.2d 887",
            "526 Pa. 374",
            "1991 Pa. LEXIS 28"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Rodriguez",
          "cluster_id": 111280,
          "cite": [
            "83 L. Ed. 2d 165",
            "105 S. Ct. 308",
            "469 U.S. 1",
            "1984 U.S. LEXIS 159",
            "53 U.S.L.W. 3359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Grubbs",
          "cluster_id": 145670,
          "cite": [
            "164 L. Ed. 2d 195",
            "126 S. Ct. 1494",
            "547 U.S. 90",
            "2006 U.S. LEXIS 2496"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Upton",
          "cluster_id": 2028985,
          "cite": [
            "476 N.E.2d 548",
            "394 Mass. 363",
            "1985 Mass. LEXIS 1398"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Novembrino",
          "cluster_id": 1516571,
          "cite": [
            "519 A.2d 820",
            "105 N.J. 95",
            "1987 N.J. LEXIS 265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
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
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Frazier",
          "cluster_id": 791897,
          "cite": [
            "423 F.3d 526",
            "2005 U.S. App. LEXIS 19190",
            "2005 WL 2123792"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard J. Leary, and F.L. Kleinberg & Co.",
          "cluster_id": 505922,
          "cite": [
            "846 F.2d 592",
            "1988 U.S. App. LEXIS 5755",
            "1988 WL 39811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Eason",
          "cluster_id": 1863783,
          "cite": [
            "2001 WI 98",
            "629 N.W.2d 625",
            "245 Wis. 2d 206",
            "2001 Wisc. LEXIS 443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Torres",
          "cluster_id": 5689682,
          "cite": [
            "74 N.Y.2d 224",
            "544 N.Y.S.2d 796",
            "543 N.E.2d 61",
            "1989 N.Y. LEXIS 886"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marsala",
          "cluster_id": 7894150,
          "cite": [
            "216 Conn. 150",
            "579 A.2d 58",
            "1990 Conn. LEXIS 308"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dracy Lamont McKneely Andrew Ellis, and Alandis Bennett, Also Known as Torjano Akines",
          "cluster_id": 654640,
          "cite": [
            "6 F.3d 1447",
            "1993 U.S. App. LEXIS 26177",
            "1993 WL 403544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell R. George, AKA Rusty, and Pamela A. Johnson-Sherman, Francis R. Lajoice",
          "cluster_id": 590903,
          "cite": [
            "975 F.2d 72",
            "1992 U.S. App. LEXIS 22728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Howard Laughton",
          "cluster_id": 790424,
          "cite": [
            "409 F.3d 744",
            "2005 U.S. App. LEXIS 8683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Carter",
          "cluster_id": 1294313,
          "cite": [
            "370 S.E.2d 553",
            "322 N.C. 709",
            "1988 N.C. LEXIS 477"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Barbara Fama",
          "cluster_id": 450379,
          "cite": [
            "758 F.2d 834",
            "1985 U.S. App. LEXIS 30301"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massachusetts v. Sheppard:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111263) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDEwMTAyNDAwMDAwJnM9MjA3NzcxMiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111263%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111263)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjAmcz0yOTY4Nzg4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111263%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111263)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 1,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111263)",
    "indexed_citing_opinions": 572,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111263,
        "count": 572,
        "count_source": "search"
      }
    ],
    "citation_count": 854,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/massachusetts-v-sheppard.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjczMTU2MTgmcz00ODk2NDI5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111263%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111263,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 288501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 336439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 339106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 350518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 388826,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 402242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 405042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 409379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 2037706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 2058560,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111263,
        "cited_id": 2242345,
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
    "date_created": "2026-07-05T12:20:02Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:20:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:20:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:23:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:20:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Massachusetts v. Sheppard

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1025-4">
<span citation-index="1" class="star-pagination" label="983"> 
   *983
   </span>
  Justice White
 </author>
<p id="ANT">
  delivered the opinion of the Court.
 </p>
<p id="b1025-5">
  This case involves the application of the rules articulated today in
  <em>
   United States
  </em>
  v.
  <em>
   Leon, ante,
  </em>
  p. 897, to a situation in
  <span citation-index="1" class="star-pagination" label="984"> 
   *984
   </span>
  which police officers seize items pursuant to a warrant subsequently invalidated because of a technical error on the part of the issuing judge.
 </p>
<p id="b1026-5">
  I
 </p>
<p id="b1026-6">
  The badly burned body of Sandra Boulware was discovered in a vacant lot in the Roxbury section of Boston at approximately 5 a. m., Saturday, May 5,1979. An autopsy revealed that Boulware had died of multiple compound skull fractures caused by blows to the head. After a brief investigation, the police decided to question one of the victim’s boyfriends, Osborne Sheppard. Sheppard told the police that he had last seen the victim on Tuesday night and that he had been at a local gaming house (where card games were played) from 9 p. m. Friday until 5 a. m. Saturday. He identified several people who would be willing to substantiate the latter claim.
 </p>
<p id="b1026-7">
  By interviewing the people Sheppard had said were at the gaming house on Friday night, the police learned that although Sheppard was at the gaming house that night, he had borrowed an automobile at about 3 o’clock Saturday morning in order to give two men a ride home. Even though the trip normally took only 15 minutes, Sheppard did not return with the car until nearly 5 a. m.
 </p>
<p id="b1026-8">
  On Sunday morning, police officers visited the owner of the car Sheppard had borrowed. He consented to an inspection of the vehicle. Bloodstains and pieces of hair were found on the rear bumper and within the trunk compartment. In addition, the officers noticed strands of wire in the trunk similar to wire strands found on and near the body of the victim. The owner of the car told the officers that when he last used the car on Friday night, shortly before Sheppard borrowed it, he had placed articles in the trunk and had not noticed any stains on the bumper or in the trunk.
 </p>
<p id="b1026-9">
  On the basis of the evidence gathered thus far in the investigation, Detective Peter O’Malley drafted an affidavit designed to support an application for an arrest warrant and a search warrant authorizing a search of Sheppard’s residence.
  <span citation-index="1" class="star-pagination" label="985"> 
   *985
   </span>
  The affidavit set forth the results of the investigation and stated that the police wished to search for
 </p>
<blockquote id="b1027-5">
  “[a] fifth bottle of amaretto liquor, 2 nickel bags of marijuana, a woman’s jacket that has been described as black-grey (charcoal) possessions of Sandra D. Boulware, similar type wire and rope that match those on the body of Sandra D. Boulware, or in the above [TJhunderbird. Blunt instrument that might have been used on the victim. Men’s or women’s clothing that may have blood, gasoline, burns on them. Items that may have fingerprints of the victim.”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</blockquote>
<p id="b1027-6">
  Detective O’Malley showed the affidavit to the District Attorney, the District Attorney’s first assistant, and a sergeant, who all concluded that it set forth probable cause for the search and the arrest. <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#492" aria-description="Citation for case: Commonwealth v. Sheppard">387 Mass. 488, 492</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#727" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d 725, 727</a></span> (1982).
 </p>
<p id="b1027-7">
  Because it was Sunday, the local court was closed, and the police had a difficult time finding a warrant application form. Detective O’Malley finally found a warrant form previously in use in the Dorchester District. The form was entitled “Search Warrant — Controlled Substance G. L. c. 276 §§1 through 3A.” Realizing that some changes had to be made before the form could be used to authorize the search requested in the affidavit, Detective O’Malley deleted the subtitle “controlled substance” with a typewriter. He also substituted “Roxbury” for the printed “Dorchester” and typed Sheppard’s name and address into blank spaces provided for that information. However, the reference to “controlled substance” was not deleted in the portion of the form that constituted the warrant application and that, when signed, would constitute the warrant itself.
 </p>
<p id="b1028-4">
<span citation-index="1" class="star-pagination" label="986"> 
   *986
   </span>
  Detective O’Malley then took the affidavit and the warrant form to the residence of a judge who had consented to consider the warrant application. The judge examined the affidavit and stated that he would authorize the search as requested. Detective O’Malley offered the warrant form and stated that he knew the form as presented dealt with controlled substances. He showed the judge where he had crossed out the subtitles. After unsuccessfully searching for a more suitable form, the judge informed O’Malley that he would make the necessary changes so as to provide a proper search warrant. The judge then took the form, made some changes on it, and dated and signed the warrant. However, he did not change the substantive portion of the warrant, which continued to authorize a search for controlled substances;
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  nor did he alter the form so as to incorporate the affidavit. The judge returned the affidavit and the warrant to O’Malley, informing him that the warrant was sufficient authority in form and content to carry out the search as requested.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  O’Malley took the two documents and, accompanied by other officers, proceeded to Sheppard’s residence.
  <span citation-index="1" class="star-pagination" label="987"> 
   *987
   </span>
  The scope of the ensuing search was limited to the items listed in the affidavit, and several incriminating pieces of evidence were discovered.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Sheppard was then charged with first-degree murder.
 </p>
<p id="b1029-7">
  At a pretrial suppression hearing, the trial judge concluded that the warrant failed to conform to the commands of the Fourth Amendment because it did not particularly describe the items to be seized. The judge ruled, however, that the evidence could be admitted notwithstanding the defect in the warrant because the police had acted in good faith in executing what they reasonably thought was a valid warrant. App. 35a. At the subsequent trial, Sheppard was convicted.
 </p>
<p id="b1029-8">
  On appeal, Sheppard argued that the evidence obtained pursuant to the defective warrant should have been suppressed. The Supreme Judicial Court of Massachusetts agreed. A plurality of the justices concluded that although “the police conducted the search in a good faith belief, reasonably held, that the search was lawful and authorized by the warrant issued by the judge,” <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#503" aria-description="Citation for case: Commonwealth v. Sheppard">387 Mass., at 503</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#733" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d, at 733</a></span>, the evidence had to be excluded because this Court had not recognized a good-faith exception to the exclusionary rule. Two justices combined in a separate concurrence to stress their rejection of the good-faith exception, and one justice dissented, contending that since exclusion of the evidence in this case would not serve to deter any police misconduct, the evidence should be admitted. We granted certiorari and set the case for argument in conjunction with
  <em>
   United States
  </em>
  v.
  <em>
   Leon, ante,
  </em>
  p. 897. <span class="citation multiple-matches"><a href="/c/U.%20S./463/1205/">463 U. S. 1205</a></span> (1983).
 </p>
<p id="b1029-9">
  II
 </p>
<p id="b1029-3">
  Having already decided that the exclusionary rule should not be applied when the officer conducting the search acted in
  <span citation-index="1" class="star-pagination" label="988"> 
   *988
   </span>
  objectively reasonable reliance on a warrant issued by a detached and neutral magistrate that subsequently is determined to be invalid,
  <em>
   ante,
  </em>
  at 922-923, the sole issue before us in this case is whether the officers reasonably believed that the search they conducted was authorized by a valid warrant.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  There is no dispute that the officers believed that the warrant authorized the search that they conducted. Thus, the only question is whether there was an objectively reasonable basis for the officers’ mistaken belief. Both the trial court, App. 35a, and a majority of the Supreme Judicial Court, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#503" aria-description="Citation for case: Commonwealth v. Sheppard">387 Mass., at 503</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#733" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d, at 733</a></span>;
  <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#524" aria-description="Citation for case: Commonwealth v. Sheppard"><em>
   id.,
  </em>
  at 524-525</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#745" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d, at 745</a></span> (Lynch, J., dissenting), concluded that there was. We agree.
 </p>
<p id="b1031-4">
<span citation-index="1" class="star-pagination" label="989"> 
   *989
   </span>
  The officers in this case took every step that could reasonably be expected of them. Detective O’Malley prepared an affidavit which was reviewed and approved by the District Attorney. He presented that affidavit to a neutral judge. The judge concluded that the affidavit established probable cause to search Sheppard’s residence, App. 26a, and informed O’Malley that he would authorize the search as requested. O’Malley then produced the warrant form and informed the judge that it might need to be changed. He was told by the judge that the necessary changes would be made. He then observed the judge make some changes and received the warrant and the affidavit. At this point, a reasonable police officer would have concluded, as O’Malley did, that the warrant authorized a search for the materials outlined in the affidavit.
 </p>
<p id="b1031-5">
  Sheppard contends that since O’Malley knew the warrant form was defective, he should have examined it to make sure that the necessary changes had been made. However, that argument is based on the premise that O’Malley had a duty to disregard the judge’s assurances that the requested search would be authorized and the necessary changes would be made. Whatever an officer may be required to do when he executes a warrant without knowing beforehand what items are to be seized,
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  we refuse to rule that an officer is required
  <span citation-index="1" class="star-pagination" label="990"> 
   *990
   </span>
  to disbelieve a judge who has just advised him, by word and by action, that the warrant he possesses authorizes him to conduct the search he has requested. In Massachusetts, as in most jurisdictions, the determinations of a judge acting within his jurisdiction, even if erroneous, are valid and binding until they are set aside under some recognized procedure.
  <em>
   Streeter
  </em>
  v.
  <em>
   City of Worcester,
  </em>
  <span class="citation" data-id="2037706"><a href="/opinion/2037706/streeter-v-city-of-worcester/#472" aria-description="Citation for case: Streeter v. City of Worcester">336 Mass. 469, 472</a></span>, <span class="citation" data-id="2037706"><a href="/opinion/2037706/streeter-v-city-of-worcester/#517" aria-description="Citation for case: Streeter v. City of Worcester">146 N. E. 2d 514, 517</a></span> (1957);
  <em>
   Moll
  </em>
  v.
  <em>
   Township of Wakefield,
  </em>
  <span class="citation" data-id="6439840"><a href="/opinion/6566090/moll-v-town-of-wakefield/#507" aria-description="Citation for case: Moll v. Town of Wakefield">274 Mass. 505, 507</a></span>, <span class="citation" data-id="6439840"><a href="/opinion/6566090/moll-v-town-of-wakefield/#82" aria-description="Citation for case: Moll v. Town of Wakefield">175 N. E. 81, 82</a></span> (1931). If an officer is required to accept at face value the judge’s conclusion that a warrant form is invalid, there is little reason why he should be expected to disregard assurances that everything is all right, especially when he has alerted the judge to the potential problems.
 </p>
<p id="b1032-5">
  In sum, the police conduct in this case clearly was objectively reasonable and largely error-free. An error of constitutional dimensions may have been committed with respect to the issuance of the warrant, but it was the judge, not the police officers, who made the critical mistake. “[T]he exclusionary rule was adopted to deter unlawful searches by police, not to punish the errors of magistrates and judges.”
  <em>
   Illinois
  </em>
  v.
  <em>
   Gates,
  </em>
  <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#263" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 263</a></span> (1983) (White, J., concurring in judgment).
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  Suppressing evidence because the
  <span citation-index="1" class="star-pagination" label="991"> 
   *991
   </span>
  judge failed to make all the necessary clerical corrections despite his assurances that such changes would be made will not serve the deterrent function that the exclusionary rule was designed to achieve. Accordingly, federal law does not require the exclusion of the disputed evidence in this case. The judgment of the Supreme Judicial Court is therefore reversed, and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b1033-5">
<em>
   It is so ordered.
  </em>
</p>
<p id="b1033-6">
  [For opinion of Justice Stevens concurring in the judgment, see
  <em>
   ante,
  </em>
  p. 960.]
 </p>
<p id="b1033-7">
  [For dissenting opinion of Justice Brennan, see
  <em>
   ante,
  </em>
  p. 928.]
 </p>







<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1027-8">
   The liquor and marihuana were included in the request because Sheppard had told the officers that when he was last with the victim, the two had purchased two bags of marihuana and a fifth of amaretto before going to his residence.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b1028-5">
   The warrant directed the officers to “search for any controlled substance, article, implement or other paraphernalia used in, for, or in connection with the unlawful possession or use of any controlled substance, and to seize and securely keep the same until final action . . . .”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b1028-6">
   Sheppard contends that there is no evidence in the record that the judge spoke to O’Malley after he made the changes. Brief for Respondent 11, n. 4. However, the trial judge expressly found that the judge “informed Detective O’Malley that the warrant as delivered over was sufficient authority in form and content to carry out the search as requested,” App. 27a, and a plurality of the Supreme Judicial Court noted that finding without any apparent disapproval. <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#497" aria-description="Citation for case: Commonwealth v. Sheppard">387 Mass. 488, 497</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#730" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d 725, 730</a></span> (1982). Since it would have been reasonable for O’Malley to infer that the warrant was valid when the judge made some changes after assuring him that the form would be corrected, an express assurance that the warrant was adequate would add little to the reasonableness of O’Malley’s belief that the necessary changes had been made. Therefore, nothing would be served by combing the record to determine whether there is sufficient evidence to support the trial court’s finding that the judge spoke to O'Malley after signing the warrant.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b1029-4">
   The police found a pair of bloodstained boots, bloodstains on the concrete floor, a woman’s earring with bloodstains on it, a bloodstained envelope, a pair of men’s jockey shorts and women’s leotards with blood on them, three types of wire, and a woman’s hairpiece, subsequently identified as the victim’s.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b1030-5">
   Both the trial court, App. 32a, and a majority of the Supreme Judicial Court, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#500" aria-description="Citation for case: Commonwealth v. Sheppard">387 Mass., at 500-501</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#731" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d, at 731-732</a></span>;
   <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#510" aria-description="Citation for case: Commonwealth v. Sheppard"><em>
    id.,
   </em>
   at 510</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#737" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d, at 737</a></span> (Liacos, J., joined by Abrams, J., concurring), concluded that the warrant was constitutionally defective because the description in the warrant was completely inaccurate and the warrant did not incorporate the description contained in the affidavit. Petitioner does not dispute this conclusion.
  </p>
<p id="b1030-6">
   Petitioner does argue, however, that even though the warrant was invalid, the search was constitutional because it was reasonable within the meaning of the Fourth Amendment. Brief for Petitioner 28-32. The uniformly applied rule is that a search conducted pursuant to a warrant that fails to conform to the particularity requirement of the Fourth Amendment is unconstitutional.
   <em>
    Stanford
   </em>
   v.
   <em>
    Texas,
   </em>
   <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span> (1965);
   <em>
    United States
   </em>
   v.
   <em>
    Cardwell,
   </em>
   <span class="citation" data-id="405042"><a href="/opinion/405042/united-states-v-james-b-cardwell-united-states-of-america-v-marvin/#77" aria-description="Citation for case: United States v. James B. Cardwell, United States of...">680 F. 2d 75, 77-78</a></span> (CA9 1982);
   <em>
    United States
   </em>
   v.
   <em>
    Crozier,
   </em>
   <span class="citation" data-id="402242"><a href="/opinion/402242/united-states-v-clarence-jay-crozier-manuel-isadore-pine-alan-terry/#1299" aria-description="Citation for case: United States v. Clarence Jay Crozier, Manuel Isadore...">674 F. 2d 1293, 1299</a></span> (CA9 1982);
   <em>
    United States
   </em>
   v.
   <em>
    Klein,
   </em>
   <span class="citation" data-id="9464268"><a href="/opinion/350518/united-states-v-allan-michael-klein/#185" aria-description="Citation for case: United States v. Allan Michael Klein">565 F. 2d 183, 185</a></span> (CA1 1977);
   <em>
    United States
   </em>
   v.
   <em>
    Gardner,
   </em>
   <span class="citation" data-id="336439"><a href="/opinion/336439/united-states-v-norman-eugene-gardner/#862" aria-description="Citation for case: United States v. Norman Eugene Gardner">537 F. 2d 861, 862</a></span> (CA6 1976);
   <em>
    United States
   </em>
   v.
   <em>
    Marti,
   </em>
   <span class="citation" data-id="288501"><a href="/opinion/288501/united-states-v-luis-marti-and-lou-saks/#1268" aria-description="Citation for case: United States v. Luis Marti and Lou Saks">421 F. 2d 1263, 1268-1269</a></span> (CA2 1970). That rule is in keeping with the well-established principle that “except in certain carefully defined classes of cases, a search of private property without proper consent is ‘unreasonable’ unless it has been authorized by a valid search warrant.”
   <em>
    Camara
   </em>
   v.
   <em>
    Municipal Court,
   </em>
   <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967). See
   <em>
    Steagald
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U. S. 204, 211-212</a></span> (1981);
   <em>
    Jones
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958). Whether the present case fits into one of those carefully defined classes is a fact-bound issue of little importance since similar situations are unlikely to arise with any regularity.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b1031-6">
   Normally, when an officer who has not been involved in the application stage receives a warrant, he will read it in order to determine the object of the search. In this case, Detective O’Malley, the officer who directed the search, knew what items were listed in the affidavit presented to the judge, and he had good reason to believe that the warrant authorized the seizure of those items. Whether an officer who is less familiar with the warrant application or who has unalleviated concerns about the proper scope of the search would be justified in failing to notice a defect like the one in the warrant in this case is an issue we need not decide. We hold only that it was not unreasonable for the police in this case to rely on the judge’s assurances that the warrant authorized the search they had requested.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b1032-6">
   This is not an instance in which “it is plainly evident that a magistrate or judge had no business issuing a warrant.”
   <em>
    Illinois
   </em>
   v.
   <em>
    Gates,
   </em>
   <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#264" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 264</a></span> (White, J., concurring in judgment). The judge’s error was not in concluding that a warrant should issue but in failing to make the necessary changes on the form. Indeed, Sheppard admits that if the judge had crossed out the reference to controlled substances, written “see attached affidavit” on the form, and attached the affidavit to the warrant, the warrant would have been valid. Tr. of Oral Arg. 27, 50. See
   <em>
    United States
   </em>
   v.
   <em>
    Johnson,
   </em>
   <span class="citation" data-id="9469774"><a href="/opinion/409379/united-states-of-america-in-81-2838-v-howard-u-johnson-in-81-2839/#64" aria-description="Citation for case: United States of America, in 81-2838 v. Howard U....">690 F. 2d 60, 64-65</a></span> (CA3 1982), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./459/1214/">459 U. S. 1214</a></span> (1983);
   <em>
    In re Property Belonging to Talk of the Town Bookstore, Inc.,
   </em>
   <span class="citation" data-id="388826"><a href="/opinion/388826/in-the-matter-of-seizure-of-property-belonging-to-talk-of-the-town/#1318" aria-description="Citation for case: In The Matter Of Seizure Of Property Belonging To Talk Of...">644 F. 2d 1317, 1318-1319</a></span> (CA9 1981);
   <em>
    United States
   </em>
   v.
   <em>
    Johnson,
   </em>
   <span class="citation" data-id="339106"><a href="/opinion/339106/united-states-v-john-d-johnson/#1315" aria-description="Citation for case: United States v. John D. Johnson">541 F. 2d 1311, 1315-1316</a></span> (CA8 1976);
   <em>
    United States
   </em>
   v.
   <em>
    Womack,
   </em>
   166 U. S. App. D. C. 35, 49, <span class="citation" data-id="324545"><a href="/opinion/324545/united-states-v-herman-l-womack-united-states-of-america-v-potomac-news/#382" aria-description="Citation for case: United States v. Herman L. Womack, United States of...">509 F. 2d 368, 382</a></span> (1974);
   <em>
    Commonwealth
   </em>
   v.
   <em>
    Todisco,
   </em>
   <span class="citation" data-id="2242345"><a href="/opinion/2242345/commonwealth-v-todisco/#450" aria-description="Citation for case: Commonwealth v. Todisco">363 Mass. 445, 450</a></span>, <span class="citation" data-id="2242345"><a href="/opinion/2242345/commonwealth-v-todisco/#864" aria-description="Citation for case: Commonwealth v. Todisco">294 N. E. 2d 860, 864</a></span> (1973).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Massiah v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Massiah v. United States"
type: case
citation: "377 U.S. 201 (1964)"
parallel_cite: "84 S. Ct. 1199; 12 L. Ed. 2d 246"
neutral_cite: 1964 U.S. LEXIS 1277
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-05-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-05-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Massiah v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106822/massiah-v-united-states/"
  cluster_id: 106822
  opinion_id: 106822
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Anchor"
related: ["[[Maine v. Moulton]]", "[[Kuhlmann v. Wilson]]", "[[Brewer v. Williams]]", "[[United States v. Henry]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "deliberate-elicitation", "post-indictment"]
holding: "Once adversary proceedings have begun (here, post-indictment), the government violates the Sixth Amendment when it deliberately elicits…"
lake:
  record_id: Massiah v. United States
  status: verified
  projected_at: 2026-07-06
---

# Massiah v. United States

*377 U.S. 201 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Massiah was indicted on federal narcotics charges, retained counsel, and was released on bail. A codefendant, Colson, agreed to cooperate with federal agents and let them install a radio transmitter in his car. Colson then drew Massiah into an incriminating conversation, which an agent overheard by radio. The statements were used against Massiah at trial.

## Issue
Whether the government may use against a defendant at trial his own incriminating statements, deliberately elicited by government agents after indictment and outside the presence of his counsel.

## Rule
No — such deliberate post-indictment elicitation violates the Sixth Amendment. "We hold that the petitioner was denied the basic protections of that guarantee when there was used against him at his trial evidence of his own incriminating words, which federal agents had deliberately elicited from him after he had been indicted and in the absence of his counsel." — 377 U.S. at 206. ^pin-206

The rule reaches indirect and surreptitious interrogations, not just questioning in a police station.

## Application
By the time of the recorded conversation, Massiah had been indicted and had retained counsel, so his Sixth Amendment right had attached. The federal agents, acting through the cooperating codefendant and the hidden transmitter, deliberately elicited incriminating statements from him without counsel present — indeed, without his even knowing he was being interrogated. Using those statements against him at trial denied him the assistance of counsel the Sixth Amendment guarantees.

## Conclusion
Reversed: incriminating statements deliberately elicited from an indicted, represented defendant outside the presence of counsel cannot be used against him at trial.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Massiah* is the foundation of the Sixth Amendment "deliberate elicitation" doctrine, later refined by [[Maine v. Moulton]] (knowing exploitation) and [[Kuhlmann v. Wilson]] (action beyond mere listening), and applied in [[Brewer v. Williams]] and [[United States v. Henry]]. It remains good law.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Anchor*

## Sources
- *Massiah v. United States*, 377 U.S. 201 (1964) — https://www.courtlistener.com/opinion/106822/massiah-v-united-states/ — pinpoint: 206.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e209d54ad852784f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Massiah v. United States"}, "payload": {"all": [{"cite": "377 U.S. 201", "page": "201", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "377"}, {"cite": "84 S. Ct. 1199", "page": "1199", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "12 L. Ed. 2d 246", "page": "246", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "12"}, {"cite": "1964 U.S. LEXIS 1277", "page": "1277", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1964"}], "display": "377 U.S. 201", "official": {"cite": "377 U.S. 201", "page": "201", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "377"}, "official_selection_present": true, "record_id": "Massiah v. United States"}}
{"assertion_id": "dbc72c01ac66feb9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-206", "record_id": "Massiah v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-206", "pinpoint_status": "slip-only", "quote": "--- # Massiah v. United States *377 U.S. 201 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Massiah was indicted on federal narcotics charges, retained counsel, and was released on bail. A codefendant, Colson, agreed to cooperate with federal agents and let them install a radio transmitter in his car. Colson then drew Massiah into an incriminating conversation, which an agent overheard by radio. The statements were used against Massiah at trial. ## Issue Whether the government may use against a defendant at trial his own incriminating statements, deliberately elicited by government agents after indictment and outside the presence of his counsel. ## Rule No — such deliberate post-indictment elicitation violates the Sixth Amendment.", "quote_fidelity": "mismatch", "record_id": "Massiah v. United States", "star_marker": null}}
{"assertion_id": "078a76788f4a6dc9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Massiah v. United States"}, "payload": {"as_of_content": "1964-05-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Massiah v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Massiah v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Massiah v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Massiah v. United States",
    "case_name_short": "Massiah",
    "case_name_full": "Massiah v. United States",
    "input_case_name": "Massiah v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-05-18",
    "year": 1964,
    "docket": null,
    "cluster_id": 106822,
    "lead_opinion_id": 106822,
    "sibling_ids": [
      106822,
      9422796,
      9422797
    ],
    "absolute_url": "/opinion/106822/massiah-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "377 U.S. 201",
      "volume": "377",
      "reporter": "U.S.",
      "page": "201",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1199",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 246",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 1277",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1277",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "377 U.S. 201",
        "volume": "377",
        "reporter": "U.S.",
        "page": "201",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1199",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 246",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 1277",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1277",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "377 U.S. 201",
    "official_selection": {
      "court_class": "scotus",
      "selected": "377 U.S. 201",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-206",
      "page": null,
      "quote": "--- # Massiah v. United States *377 U.S. 201 (1964)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Massiah was indicted on federal narcotics charges, retained counsel, and was released on bail. A codefendant, Colson, agreed to cooperate with federal agents and let them install a radio transmitter in his car. Colson then drew Massiah into an incriminating conversation, which an agent overheard by radio. The statements were used against Massiah at trial. ## Issue Whether the government may use against a defendant at trial his own incriminating statements, deliberately elicited by government agents after indictment and outside the presence of his counsel. ## Rule No \u2014 such deliberate post-indictment elicitation violates the Sixth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-05-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Massiah v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Bateman",
          "cluster_id": 9413757,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Benton",
          "cluster_id": 10134904,
          "cite": [
            "317 Or. App. 384",
            "505 P.3d 975"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
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
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Justin Barrett Blakeney v. State of Mississippi",
          "cluster_id": 4442047,
          "cite": [
            "236 So. 3d 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4348984,
          "cite": [
            "848 F.3d 767",
            "2017 FED App. 0034P",
            "2017 WL 603848",
            "2017 U.S. App. LEXIS 2629"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zackary Stewart v. Karl Wagner",
          "cluster_id": 4255669,
          "cite": [
            "836 F.3d 978",
            "2016 U.S. App. LEXIS 16642",
            "2016 WL 4728039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended September 20, 2016 State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 4472001,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 3218790,
          "cite": [
            "882 N.W.2d 68",
            "2016 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
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
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 2806802,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fischer v. Smith",
          "cluster_id": 8442138,
          "cite": [
            "780 F.3d 556",
            "2015 U.S. App. LEXIS 4195",
            "2015 WL 1186845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
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
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wade",
          "cluster_id": 107486,
          "cite": [
            "18 L. Ed. 2d 1149",
            "87 S. Ct. 1926",
            "388 U.S. 218",
            "1967 U.S. LEXIS 1085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhode Island v. Innis",
          "cluster_id": 110254,
          "cite": [
            "64 L. Ed. 2d 297",
            "100 S. Ct. 1682",
            "446 U.S. 291",
            "1980 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Escobedo v. Illinois",
          "cluster_id": 106883,
          "cite": [
            "12 L. Ed. 2d 977",
            "84 S. Ct. 1758",
            "378 U.S. 478",
            "1964 U.S. LEXIS 827",
            "4 Ohio Misc. 197",
            "32 Ohio Op. 2d 31"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCleskey v. Zant",
          "cluster_id": 112573,
          "cite": [
            "113 L. Ed. 2d 517",
            "111 S. Ct. 1454",
            "499 U.S. 467",
            "1991 U.S. LEXIS 2218",
            "59 U.S.L.W. 4288",
            "91 Cal. Daily Op. Serv. 2680",
            "91 Daily Journal DAR 4340"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesbrook v. State",
          "cluster_id": 1473130,
          "cite": [
            "29 S.W.3d 103",
            "2000 Tex. Crim. App. LEXIS 86",
            "2000 WL 1346901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffa v. United States",
          "cluster_id": 107318,
          "cite": [
            "17 L. Ed. 2d 374",
            "87 S. Ct. 408",
            "385 U.S. 293",
            "1966 U.S. LEXIS 2778"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Moulton",
          "cluster_id": 111546,
          "cite": [
            "88 L. Ed. 2d 481",
            "106 S. Ct. 477",
            "474 U.S. 159",
            "1985 U.S. LEXIS 147",
            "54 U.S.L.W. 4039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kuhlmann v. Wilson",
          "cluster_id": 111726,
          "cite": [
            "91 L. Ed. 2d 364",
            "106 S. Ct. 2616",
            "477 U.S. 436",
            "1986 U.S. LEXIS 65",
            "54 U.S.L.W. 4809"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rushen v. Spain",
          "cluster_id": 111051,
          "cite": [
            "78 L. Ed. 2d 267",
            "104 S. Ct. 453",
            "464 U.S. 114",
            "1983 U.S. LEXIS 11",
            "52 U.S.L.W. 3452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106822 OR 9422796 OR 9422797) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzA2MjgxNjAwMDAwJnM9MjcwNjU3NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106822+OR+9422796+OR+9422797%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106822 OR 9422796 OR 9422797)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTAmcz00ODAzNjAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106822+OR+9422796+OR+9422797%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106822 OR 9422796 OR 9422797)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 1,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106822 OR 9422796 OR 9422797)",
    "indexed_citing_opinions": 2146,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106822,
        "count": 1988,
        "count_source": "search"
      },
      {
        "opinion_id": 9422796,
        "count": 206,
        "count_source": "search"
      },
      {
        "opinion_id": 9422797,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3189,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/massiah-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzMDk1NiZzPTk0MDYyOTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28106822+OR+9422796+OR+9422797%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106822,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 100989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 104079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 258052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 262616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 1236300,
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
    "date_created": "2026-07-05T12:23:22Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:23:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:23:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:26:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:23:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Massiah v. United States

```
<div>
<center><b><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U.S. 201</a></span> (1964)</b></center>
<center><h1>MASSIAH<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 199.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 3, 1964.</center>
<center>Decided May 18, 1964.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Robert J. Carluccio</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Solicitor General Cox</i> argued the cause for the United States. With him on the brief were <i>Assistant Attorney General Miller</i> and <i>Jerome Nelson.</i></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioner was indicted for violating the federal narcotics laws. He retained a lawyer, pleaded not guilty, and was released on bail. While he was free on bail a federal agent succeeded by surreptitious means in listening to incriminating statements made by him. Evidence of these statements was introduced against the petitioner at his trial over his objection. He was convicted, and the Court of Appeals affirmed.<sup>[1]</sup> We granted certiorari to <span class="star-pagination">*202</span> consider whether, under the circumstances here presented, the prosecution's use at the trial of evidence of the petitioner's own incriminating statements deprived him of any right secured to him under the Federal Constitution. <span class="citation multiple-matches"><a href="/c/U.%20S./374/805/">374 U. S. 805</a></span>.</p>
<p>The petitioner, a merchant seaman, was in 1958 a member of the crew of the S. S. <i>Santa Maria.</i> In April of that year federal customs officials in New York received information that he was going to transport a quantity of narcotics aboard that ship from South America to the United States. As a result of this and other information, the agents searched the <i>Santa Maria</i> upon its arrival in New York and found in the afterpeak of the vessel five packages containing about three and a half pounds of cocaine. They also learned of circumstances, not here relevant, tending to connect the petitioner with the cocaine. He was arrested, promptly arraigned, and subsequently indicted for possession of narcotics aboard a United States vessel.<sup>[2]</sup> In July a superseding indictment was returned, charging the petitioner and a man named Colson with the same substantive offense, and in separate counts charging the petitioner, Colson, and others with having conspired to possess narcotics aboard a United States vessel, and to import, conceal, and facilitate the sale of narcotics.<sup>[3]</sup> The petitioner, who had retained a lawyer, pleaded not guilty and was released on bail, along with Colson.</p>
<p>A few days later, and quite without the petitioner's knowledge, Colson decided to cooperate with the government agents in their continuing investigation of the narcotics activities in which the petitioner, Colson, and others had allegedly been engaged. Colson permitted an agent named Murphy to install a Schmidt radio transmitter <span class="star-pagination">*203</span> under the front seat of Colson's automobile, by means of which Murphy, equipped with an appropriate receiving device, could overhear from some distance away conversations carried on in Colson's car.</p>
<p>On the evening of November 19, 1959, Colson and the petitioner held a lengthy conversation while sitting in Colson's automobile, parked on a New York street. By prearrangement with Colson, and totally unbeknown to the petitioner, the agent Murphy sat in a car parked out of sight down the street and listened over the radio to the entire conversation. The petitioner made several incriminating statements during the course of this conversation. At the petitioner's trial these incriminating statements were brought before the jury through Murphy's testimony, despite the insistent objection of defense counsel. The jury convicted the petitioner of several related narcotics offenses, and the convictions were affirmed by the Court of Appeals.<sup>[4]</sup></p>
<p>The petitioner argues that it was an error of constitutional dimensions to permit the agent Murphy at the trial to testify to the petitioner's incriminating statements which Murphy had overheard under the circumstances disclosed by this record. This argument is based upon two distinct and independent grounds. First, we are told that Murphy's use of the radio equipment violated the petitioner's rights under the Fourth Amendment, and, consequently, that all evidence which Murphy thereby obtained was, under the rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, inadmissible against the petitioner at the trial. Secondly, it is said that the petitioner's <span class="star-pagination">*204</span> Fifth and Sixth Amendment rights were violated by the use in evidence against him of incriminating statements which government agents had deliberately elicited from him after he had been indicted and in the absence of his retained counsel. Because of the way we dispose of the case, we do not reach the Fourth Amendment issue.</p>
<p>In <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>, this Court reversed a state criminal conviction because a confession had been wrongly admitted into evidence against the defendant at his trial. In that case the defendant had already been indicted for first-degree murder at the time he confessed. The Court held that the defendant's conviction could not stand under the Fourteenth Amendment. While the Court's opinion relied upon the totality of the circumstances under which the confession had been obtained, four concurring Justices pointed out that the Constitution required reversal of the conviction upon the sole and specific ground that the confession had been deliberately elicited by the police after the defendant had been indicted, and therefore at a time when he was clearly entitled to a lawyer's help. It was pointed out that under our system of justice the most elemental concepts of due process of law contemplate that an indictment be followed by a trial, "in an orderly courtroom, presided over by a judge, open to the public, and protected by all the procedural safeguards of the law." <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#327" aria-description="Citation for case: Spano v. New York">360 U. S., at 327</a></span> (STEWART, J., concurring). It was said that a Constitution which guarantees a defendant the aid of counsel at such a trial could surely vouchsafe no less to an indicted defendant under interrogation by the police in a completely extrajudicial proceeding. Anything less, it was said, might deny a defendant "effective representation by counsel at the only stage when legal aid and advice would help him." <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York">360 U. S., at 326</a></span> (DOUGLAS, J., concurring).</p>
<p>Ever since this Court's decision in the <i><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span></i> case, the New York courts have unequivocally followed this constitutional <span class="star-pagination">*205</span> rule. "Any secret interrogation of the defendant, from and after the finding of the indictment, without the protection afforded by the presence of counsel, contravenes the basic dictates of fairness in the conduct of criminal causes and the fundamental rights of persons charged with crime." <i>People</i> v. <i>Waterman,</i> 9 N. Y. 2d 561, 565, <span class="citation" data-id="5519137"><a href="/opinion/5671829/people-v-waterman/#448" aria-description="Citation for case: People v. Waterman">175 N. E. 2d 445, 448</a></span>.<sup>[5]</sup></p>
<p>This view no more than reflects a constitutional principle established as long ago as <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, where the Court noted that ". . . during perhaps the most critical period of the proceedings . . . that is to say, from the time of their arraignment until the beginning of their trial, when consultation, thoroughgoing investigation and preparation [are] vitally important, the defendants . . . [are] as much entitled to such aid [of counsel] during that period as at the trial itself." <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama"><i>Id.,</i> at 57</a></span>. And since the <i><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span></i> decision the same basic constitutional principle has been broadly reaffirmed by this Court. <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>. See <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>.</p>
<p>Here we deal not with a state court conviction, but with a federal case, where the specific guarantee of the Sixth Amendment directly applies.<sup>[6]</sup><i>Johnson</i> v. <i>Zerbst,</i> 304 <span class="star-pagination">*206</span> U. S. 458. We hold that the petitioner was denied the basic protections of that guarantee when there was used against him at his trial evidence of his own incriminating words, which federal agents had deliberately elicited from him after he had been indicted and in the absence of his counsel. It is true that in the <i><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span></i> case the defendant was interrogated in a police station, while here the damaging testimony was elicited from the defendant without his knowledge while he was free on bail. But, as Judge Hays pointed out in his dissent in the Court of Appeals, "if such a rule is to have any efficacy it must apply to indirect and surreptitious interrogations as well as those conducted in the jailhouse. In this case, Massiah was more seriously imposed upon . . . because he did not even know that he was under interrogation by a government agent." 307 F. 2d, at 72-73.</p>
<p>The Solicitor General, in his brief and oral argument, has strenuously contended that the federal law enforcement agents had the right, if not indeed the duty, to continue their investigation of the petitioner and his alleged criminal associates even though the petitioner had been indicted. He points out that the Government was continuing its investigation in order to uncover not only the source of narcotics found on the S. S. <i>Santa Maria,</i> but also their intended buyer. He says that the quantity of narcotics involved was such as to suggest that the petitioner was part of a large and well-organized ring, and indeed that the continuing investigation confirmed this suspicion, since it resulted in criminal charges against many defendants. Under these circumstances the Solicitor General concludes that the government agents were completely "justified in making use of Colson's cooperation by having Colson continue his normal associations and by surveilling them."</p>
<p>We may accept and, at least for present purposes, completely approve all that this argument implies, Fourth <span class="star-pagination">*207</span> Amendment problems to one side. We do not question that in this case, as in many cases, it was entirely proper to continue an investigation of the suspected criminal activities of the defendant and his alleged confederates, even though the defendant had already been indicted. All that we hold is that the defendant's own incriminating statements, obtained by federal agents under the circumstances here disclosed, could not constitutionally be used by the prosecution as evidence against <i>him</i> at his trial.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE CLARK and MR. JUSTICE HARLAN join, dissenting.</p>
<p>The current incidence of serious violations of the law represents not only an appalling waste of the potentially happy and useful lives of those who engage in such conduct but also an overhanging, dangerous threat to those unidentified and innocent people who will be the victims of crime today and tomorrow. This is a festering problem for which no adequate cures have yet been devised. At the very least there is much room for discontent with remedial measures so far undertaken. And admittedly there remains much to be settled concerning the disposition to be made of those who violate the law.</p>
<p>But dissatisfaction with preventive programs aimed at eliminating crime and profound dispute about whether we should punish, deter, rehabilitate or cure cannot excuse concealing one of our most menacing problems until the millennium has arrived. In my view, a civilized society must maintain its capacity to discover transgressions of the law and to identify those who flout it. This much is necessary even to know the scope of the problem, much less to formulate intelligent countermeasures. It will just not do to sweep these disagreeable matters under the rug or to pretend they are not there at all.</p>
<p><span class="star-pagination">*208</span> It is therefore a rather portentous occasion when a constitutional rule is established barring the use of evidence which is relevant, reliable and highly probative of the issue which the trial court has before itwhether the accused committed the act with which he is charged. Without the evidence, the quest for truth may be seriously impeded and in many cases the trial court, although aware of proof showing defendant's guilt, must nevertheless release him because the crucial evidence is deemed inadmissible. This result is entirely justified in some circumstances because exclusion serves other policies of overriding importance, as where evidence seized in an illegal search is excluded, not because of the quality of the proof, but to secure meaningful enforcement of the Fourth Amendment. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>; <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. But this only emphasizes that the soundest of reasons is necessary to warrant the exclusion of evidence otherwise admissible and the creation of another area of privileged testimony. With all due deference, I am not at all convinced that the additional barriers to the pursuit of truth which the Court today erects rest on anything like the solid foundations which decisions of this gravity should require.</p>
<p>The importance of the matter should not be underestimated, for today's rule promises to have wide application well beyond the facts of this case. The reason given for the result herethe admissions were obtained in the absence of counselwould seem equally pertinent to statements obtained at any time after the right to counsel attaches, whether there has been an indictment or not; to admissions made prior to arraignment, at least where the defendant has counsel or asks for it; to the fruits of admissions improperly obtained under the new rule; to criminal proceedings in state courts; and to defendants long since convicted upon evidence <span class="star-pagination">*209</span> including such admissions. The new rule will immediately do service in a great many cases.</p>
<p>Whatever the content or scope of the rule may prove to be, I am unable to see how this case presents an unconstitutional interference with Massiah's right to counsel. Massiah was not prevented from consulting with counsel as often as he wished. No meetings with counsel were disturbed or spied upon. Preparation for trial was in no way obstructed. It is only a sterile syllogisman unsound one, besidesto say that because Massiah had a right to counsel's aid before and during the trial, his out-of-court conversations and admissions must be excluded if obtained without counsel's consent or presence. The right to counsel has never meant as much before, <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>; <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, and its extension in this case requires some further explanation, so far unarticulated by the Court.</p>
<p>Since the new rule would exclude all admissions made to the police, no matter how voluntary and reliable, the requirement of counsel's presence or approval would seem to rest upon the probability that counsel would foreclose any admissions at all. This is nothing more than a thinly disguised constitutional policy of minimizing or entirely prohibiting the use in evidence of voluntary out-of-court admissions and confessions made by the accused. Carried as far as blind logic may compel some to go, the notion that statements from the mouth of the defendant should not be used in evidence would have a severe and unfortunate impact upon the great bulk of criminal cases.</p>
<p>Viewed in this light, the Court's newly fashioned exclusionary principle goes far beyond the constitutional privilege against self-incrimination, which neither requires nor suggests the barring of voluntary pretrial admissions. The Fifth Amendment states that no person "shall be compelled in any criminal case to be a witness against <span class="star-pagination">*210</span> himself . . . ." The defendant may thus not be compelled to testify at his trial, but he may if he wishes. Likewise he may not be compelled or coerced into saying anything before trial; but until today he could if he wished to, and if he did, it could be used against him. Whether as a matter of self-incrimination or of due process, the proscription is against compulsioncoerced incrimination. Under the prior law, announced in countless cases in this Court, the defendant's pretrial statements were admissible evidence if voluntarily made; inadmissible if not the product of his free will. Hardly any constitutional area has been more carefully patrolled by this Court, and until now the Court has expressly rejected the argument that admissions are to be deemed involuntary if made outside the presence of counsel. <i>Cicenia</i> v. <i><span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">Lagay, supra</a></span></i><i>; </i><i>Crooker</i> v. <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">California, supra</a></span></i><i>.</i><sup>[*]</sup></p>
<p>The Court presents no facts, no objective evidence, no reasons to warrant scrapping the voluntary-involuntary test for admissibility in this area. Without such evidence I would retain it in its present form.</p>
<p>This case cannot be analogized to the American Bar Association's rule forbidding an attorney to talk to the opposing party litigant outside the presence of his counsel. Aside from the fact that the Association's canons are not of constitutional dimensions, the specific canon argued is inapposite because it deals with the conduct <span class="star-pagination">*211</span> of lawyers and not with the conduct of investigators. Lawyers are forbidden to interview the opposing party because of the supposed imbalance of legal skill and acumen between the lawyer and the party litigant; the reason for the rule does not apply to nonlawyers and certainly not to Colson, Massiah's codefendant.</p>
<p>Applying the new exclusionary rule is peculiarly inappropriate in this case. At the time of the conversation in question, petitioner was not in custody but free on bail. He was not questioned in what anyone could call an atmosphere of official coercion. What he said was said to his partner in crime who had also been indicted. There was no suggestion or any possibility of coercion. What petitioner did not know was that Colson had decided to report the conversation to the police. Had there been no prior arrangements between Colson and the police, had Colson simply gone to the police after the conversation had occurred, his testimony relating Massiah's statements would be readily admissible at the trial, as would a recording which he might have made of the conversation. In such event, it would simply be said that Massiah risked talking to a friend who decided to disclose what he knew of Massiah's criminal activities. But if, as occurred here, Colson had been cooperating with the police prior to his meeting with Massiah, both his evidence and the recorded conversation are somehow transformed into inadmissible evidence despite the fact that the hazard to Massiah remains precisely the same the defection of a confederate in crime.</p>
<p>Reporting criminal behavior is expected or even demanded of the ordinary citizen. Friends may be subpoenaed to testify about friends, relatives about relatives and partners about partners. I therefore question the soundness of insulating Massiah from the apostasy of his partner in crime and of furnishing constitutional sanctions for the strict secrecy and discipline of criminal organizations. <span class="star-pagination">*212</span> Neither the ordinary citizen nor the confessed criminal should be discouraged from reporting what he knows to the authorities and from lending his aid to secure evidence of crime. Certainly after this case the Colsons will be few and far between; and the Massiahs can breathe much more easily, secure in the knowledge that the Constitution furnishes an important measure of protection against faithless compatriots and guarantees sporting treatment for sporting peddlers of narcotics.</p>
<p>Meanwhile, of course, the public will again be the loser and law enforcement will be presented with another serious dilemma. The general issue lurking in the background of the Court's opinion is the legitimacy of penetrating or obtaining confederates in criminal organizations. For the law enforcement agency, the answer for the time being can only be in the form of a prediction about the future application of today's new constitutional doctrine. More narrowly, and posed by the precise situation involved here, the question is this: when the police have arrested and released on bail one member of a criminal ring and another member, a confederate, is cooperating with the police, can the confederate be allowed to continue his association with the ring or must he somehow be withdrawn to avoid challenge to trial evidence on the ground that it was acquired after rather than before the arrest, after rather than before the indictment?</p>
<p>Defendants who are out on bail have been known to continue their illicit operations. See <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="262616"><a href="/opinion/262616/robert-lowell-rogers-v-united-states/" aria-description="Citation for case: Robert Lowell Rogers v. United States">325 F. 2d 485</a></span> (C. A. 10th Cir.). That an attorney is advising them should not constitutionally immunize their statements made in furtherance of these operations and relevant to the question of their guilt at the pending prosecution. In this very case there is evidence that after indictment defendant Aiken tried to <span class="star-pagination">*213</span> persuade Agent Murphy to go into the narcotics business with him. Under today's decision, Murphy may neither testify as to the content of this conversation nor seize for introduction in evidence any narcotics whose location Aiken may have made known.</p>
<p>Undoubtedly, the evidence excluded in this case would not have been available but for the conduct of Colson in cooperation with Agent Murphy, but is it this kind of conduct which should be forbidden to those charged with law enforcement? It is one thing to establish safeguards against procedures fraught with the potentiality of coercion and to outlaw "easy but self-defeating ways in which brutality is substituted for brains as an instrument of crime detection." <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#344" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 344</a></span>. But here there was no substitution of brutality for brains, no inherent danger of police coercion justifying the prophylactic effect of another exclusionary rule. Massiah was not being interrogated in a police station, was not surrounded by numerous officers or questioned in relays, and was not forbidden access to others. Law enforcement may have the elements of a contest about it, but it is not a game. <i>McGuire</i> v. <i>United States,</i> <span class="citation" data-id="100989"><a href="/opinion/100989/mcguire-v-united-states/#99" aria-description="Citation for case: McGuire v. United States">273 U. S. 95, 99</a></span>. Massiah and those like him receive ample protection from the long line of precedents in this Court holding that confessions may not be introduced unless they are voluntary. In making these determinations the courts must consider the absence of counsel as one of several factors by which voluntariness is to be judged. See <i>House</i> v. <i>Mayo,</i> <span class="citation" data-id="104079"><a href="/opinion/104079/house-v-mayo/#45" aria-description="Citation for case: House v. Mayo">324 U. S. 42, 45-46</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#567" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 567</a></span>; <i>Cicenia</i> v. <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/#509" aria-description="Citation for case: Cicenia v. Lagay"><i>Lagay, supra,</i> at 509</a></span>. This is a wiser rule than the automatic rule announced by the Court, which requires courts and juries to disregard voluntary admissions which they might well find to be the best possible evidence in discharging their responsibility for ascertaining truth.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,...">307 F. 2d 62</a></span>.</p>
<p>[2]  21 U. S. C. § 184a.</p>
<p>[3]  <span class="citation no-link">21 U. S. C. §§ 173</span>, 174.</p>
<p>[4]  The petitioner's trial was upon a second superseding indictment which had been returned on March 3, 1961, and which included additional counts against him and other defendants. The Court of Appeals reversed his conviction upon a conspiracy count, one judge dissenting, but affirmed his convictions upon three substantive counts, one judge dissenting. <span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,...">307 F. 2d 62</a></span>.</p>
<p>[5]  See also <i>People</i> v. <i>Davis,</i> 13 N. Y. 2d 690, <span class="citation" data-id="5520812"><a href="/opinion/5673349/people-v-davis/" aria-description="Citation for case: People v. Davis">191 N. E. 2d 674</a></span>, 241 N. Y. S. 2d 172 (1963); <i>People</i> v. <i>Rodriguez,</i> 11 N. Y. 2d 279, <span class="citation" data-id="5519859"><a href="/opinion/5672480/people-v-rodriguez/" aria-description="Citation for case: People v. Rodriguez">183 N. E. 2d 651</a></span>, 229 N. Y. S. 2d 353 (1962); <i>People</i> v. <i>Meyer,</i> 11 N. Y. 2d 162, <span class="citation" data-id="5519835"><a href="/opinion/5672465/people-v-meyer/" aria-description="Citation for case: People v. Meyer">182 N. E. 2d 103</a></span>, 227 N. Y. S. 2d 427 (1962); <i>People</i> v. <i>Di Biasi,</i> 7 N. Y. 2d 544, <span class="citation" data-id="5518161"><a href="/opinion/5670925/people-v-di-biasi/" aria-description="Citation for case: People v. Di Biasi">166 N. E. 2d 825</a></span>, 200 N. Y. S. 2d 21 (1960); <i>People</i> v. <i>Swanson,</i> 18 App. Div. 2d 832, 237 N. Y. S. 2d 400 (2d Dept. 1963); <i>People</i> v. <i>Price,</i> 18 App. Div. 2d 739, 235 N. Y. S. 2d 390 (3d Dept. 1962); <i>People</i> v. <i>Wallace,</i> 17 App. Div. 2d 981, 234 N. Y. S. 2d 579 (2d Dept. 1962); <i>People</i> v. <i>Karmel,</i> 17 App. Div. 2d 659, 230 N. Y. S. 2d 413 (2d Dept. 1962); <i>People</i> v. <i>Robinson,</i> 16 App. Div. 2d 184, 224 N. Y. S. 2d 705 (4th Dept. 1962).</p>
<p>[6]  "In all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence."</p>
<p>[*]  Today's rule picks up where the Fifth Amendment ends and bars wholly voluntary admissions. I would assume, although one cannot be sure, that the new rule would not have a similar supplemental role in connection with the Fourth Amendment. While the Fifth Amendment bars only compelled incrimination, the Fourth Amendment bars only unreasonable searches. It could be argued, fruitlessly I would hope, that if the police must stay away from the defendant they must also stay away from his house once the right to counsel has attached and that a court must exclude the products of a reasonable search made pursuant to a properly issued warrant but without the consent or presence of the accused's counsel.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Mathews v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Mathews v. United States"
type: case
citation: "485 U.S. 58 (1988)"
parallel_cite: "108 S. Ct. 883; 99 L. Ed. 2d 54"
neutral_cite: 1988 U.S. LEXIS 943
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mathews v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112012/mathews-v-united-states/"
  cluster_id: 112012
  opinion_id: 112012
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Progeny / Refinement"
related: ["[[Sorrells v. United States]]", "[[Hampton v. United States]]", "[[Jacobson v. United States]]"]
aliases: []
tags: ["case", "entrapment", "affirmative-defense", "jury-instruction"]
holding: "A defendant who denies one or more elements of the charged crime is nonetheless entitled to an entrapment instruction whenever there is…"
lake:
  record_id: Mathews v. United States
  status: verified
  projected_at: 2026-07-06
---

# Mathews v. United States

*485 U.S. 58 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Mathews, an employee of the Small Business Administration, was charged with accepting a gratuity after taking a loan from a program participant who was cooperating with the FBI. Before trial he sought to raise an entrapment defense, but the District Court ruled entrapment unavailable because he would not admit all the elements (including the requisite mental state) of the offense. The Seventh Circuit affirmed.

## Issue
Whether a defendant who denies one or more elements of the charged crime may nonetheless obtain a jury instruction on entrapment where the evidence would support it.

## Rule
Yes. "We hold that even if the defendant denies one or more elements of the crime, he is entitled to an entrapment instruction whenever there is sufficient evidence from which a reasonable jury could find entrapment." — 485 U.S. at 62. ^pin-62

Denying the offense and requesting an entrapment instruction are not mutually exclusive; the instruction follows from the evidence, not from any concession of guilt.

## Application
The trial court refused to instruct on entrapment solely because Mathews would not admit the intent element of accepting the loan. Because a defendant may both deny an element and obtain an entrapment instruction where the evidence supports it, that refusal was error; the trial court's observation that the entrapment evidence was "shaky at best" went to what the jury could find, not to the availability of the instruction.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]; a defendant's refusal to admit the elements of the crime does not by itself bar an entrapment instruction.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mathews* remains the governing rule on the availability of the entrapment instruction to a defendant who denies the offense.

## Appears on
- [[Entrapment]] — *Key — Progeny / Refinement*

## Sources
- *Mathews v. United States*, 485 U.S. 58 (1988) — https://www.courtlistener.com/opinion/112012/mathews-v-united-states/ — pinpoint: 62.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1c6f589b83eea359", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Mathews v. United States"}, "payload": {"all": [{"cite": "485 U.S. 58", "page": "58", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "485"}, {"cite": "108 S. Ct. 883", "page": "883", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "99 L. Ed. 2d 54", "page": "54", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "1988 U.S. LEXIS 943", "page": "943", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}], "display": "485 U.S. 58", "official": {"cite": "485 U.S. 58", "page": "58", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "485"}, "official_selection_present": true, "record_id": "Mathews v. United States"}}
{"assertion_id": "7a0ca345ad126335", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-62", "record_id": "Mathews v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-62", "pinpoint_status": "slip-only", "quote": "--- # Mathews v. United States *485 U.S. 58 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mathews, an employee of the Small Business Administration, was charged with accepting a gratuity after taking a loan from a program participant who was cooperating with the FBI. Before trial he sought to raise an entrapment defense, but the District Court ruled entrapment unavailable because he would not admit all the elements (including the requisite mental state) of the offense. The Seventh Circuit affirmed. ## Issue Whether a defendant who denies one or more elements of the charged crime may nonetheless obtain a jury instruction on entrapment where the evidence would support it. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Mathews v. United States", "star_marker": null}}
{"assertion_id": "a9c6b5fc08793648", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Mathews v. United States"}, "payload": {"as_of_content": "1988-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Mathews v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Mathews v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mathews v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mathews v. United States",
    "case_name_short": "Mathews",
    "case_name_full": "Mathews v. United States",
    "input_case_name": "Mathews v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-02-24",
    "year": 1988,
    "docket": null,
    "cluster_id": 112012,
    "lead_opinion_id": 112012,
    "sibling_ids": [
      112012,
      9431220,
      9431221,
      9431222,
      9431223
    ],
    "absolute_url": "/opinion/112012/mathews-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9079219,
        "score": 20,
        "case_name": "Mathews v. United States"
      },
      {
        "cluster_id": 9079218,
        "score": 20,
        "case_name": "Mathews v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "485 U.S. 58",
      "volume": "485",
      "reporter": "U.S.",
      "page": "58",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 883",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "883",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 L. Ed. 2d 54",
        "volume": "99",
        "reporter": "L. Ed. 2d",
        "page": "54",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 943",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "943",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "485 U.S. 58",
        "volume": "485",
        "reporter": "U.S.",
        "page": "58",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 883",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "883",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 L. Ed. 2d 54",
        "volume": "99",
        "reporter": "L. Ed. 2d",
        "page": "54",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 943",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "943",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "485 U.S. 58",
    "official_selection": {
      "court_class": "scotus",
      "selected": "485 U.S. 58",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-62",
      "page": null,
      "quote": "--- # Mathews v. United States *485 U.S. 58 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mathews, an employee of the Small Business Administration, was charged with accepting a gratuity after taking a loan from a program participant who was cooperating with the FBI. Before trial he sought to raise an entrapment defense, but the District Court ruled entrapment unavailable because he would not admit all the elements (including the requisite mental state) of the offense. The Seventh Circuit affirmed. ## Issue Whether a defendant who denies one or more elements of the charged crime may nonetheless obtain a jury instruction on entrapment where the evidence would support it. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mathews v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Mathews v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Kaeppeler",
          "cluster_id": 3166351,
          "cite": [
            "473 Mass. 396",
            "42 N.E.3d 1090"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nwoye",
          "cluster_id": 2720438,
          "cite": [
            "60 F. Supp. 3d 225",
            "2014 U.S. Dist. LEXIS 117714",
            "2014 WL 4179119"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nelson",
          "cluster_id": 2659864,
          "cite": [
            "979 F. Supp. 2d 123",
            "2013 WL 5778318",
            "2013 U.S. Dist. LEXIS 153420"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Nelson, Jr.",
          "cluster_id": 1085188,
          "cite": [
            "732 F.3d 504",
            "2013 WL 5612057",
            "2013 U.S. App. LEXIS 20752"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Singleton",
          "cluster_id": 1540031,
          "cite": [
            "974 A.2d 679",
            "292 Conn. 734",
            "2009 Conn. LEXIS 214"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Estelle v. McGuire",
          "cluster_id": 112660,
          "cite": [
            "116 L. Ed. 2d 385",
            "112 S. Ct. 475",
            "502 U.S. 62",
            "1991 U.S. LEXIS 7060"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Old Chief v. United States",
          "cluster_id": 118074,
          "cite": [
            "136 L. Ed. 2d 574",
            "117 S. Ct. 644",
            "519 U.S. 172",
            "1997 U.S. LEXIS 298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LaRock",
          "cluster_id": 1201619,
          "cite": [
            "470 S.E.2d 613",
            "196 W. Va. 294",
            "1996 W. Va. LEXIS 25"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
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
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. VanderVliet",
          "cluster_id": 1804994,
          "cite": [
            "508 N.W.2d 114",
            "444 Mich. 52"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Abilez",
          "cluster_id": 2599854,
          "cite": [
            "161 P.3d 58",
            "61 Cal. Rptr. 3d 526",
            "41 Cal. 4th 472",
            "2007 Cal. LEXIS 6758"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Perruquet v. Kenneth R. Briley",
          "cluster_id": 788465,
          "cite": [
            "390 F.3d 505",
            "2004 U.S. App. LEXIS 23949",
            "2004 WL 2600589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferrel v. State",
          "cluster_id": 2336099,
          "cite": [
            "55 S.W.3d 586",
            "2001 Tex. Crim. App. LEXIS 68",
            "2001 WL 1043247"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William D. Davis, United States of America v. Curry James Williams",
          "cluster_id": 679513,
          "cite": [
            "36 F.3d 1424",
            "94 Daily Journal DAR 13648",
            "1994 U.S. App. LEXIS 27168",
            "1994 WL 525969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Walter v. Cross, A/K/A Bobo Walter v. Cross, United States of America v. Jules C. Melograne",
          "cluster_id": 779563,
          "cite": [
            "308 F.3d 308",
            "2002 U.S. App. LEXIS 22068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Evans",
          "cluster_id": 2025348,
          "cite": [
            "530 N.E.2d 1360",
            "125 Ill. 2d 50",
            "125 Ill. Dec. 790",
            "1988 Ill. LEXIS 137"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Salas",
          "cluster_id": 2510587,
          "cite": [
            "127 P.3d 40",
            "38 Cal. Rptr. 3d 624",
            "37 Cal. 4th 967"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
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
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mitchell",
          "cluster_id": 2037652,
          "cite": [
            "604 N.E.2d 877",
            "152 Ill. 2d 274",
            "178 Ill. Dec. 354",
            "1992 Ill. LEXIS 152"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Markman",
          "cluster_id": 1978964,
          "cite": [
            "916 A.2d 586",
            "591 Pa. 249",
            "2007 Pa. LEXIS 387"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brad Eugene Branch, Kevin Whitecliff, Jaime Castillo, Renos Lenny Avraam, Paul Fatta and Graeme Leonard Craddock",
          "cluster_id": 723782,
          "cite": [
            "91 F.3d 699"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Everette",
          "cluster_id": 2091114,
          "cite": [
            "565 N.E.2d 1295",
            "141 Ill. 2d 147",
            "152 Ill. Dec. 377",
            "1991 Ill. LEXIS 7"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brand",
          "cluster_id": 8439509,
          "cite": [
            "467 F.3d 179",
            "71 Fed. R. Serv. 672",
            "2006 U.S. App. LEXIS 25887",
            "2006 WL 2981524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kojo Sababu, Jaime Delgado, and Dora Garcia",
          "cluster_id": 533826,
          "cite": [
            "891 F.2d 1308",
            "1989 U.S. App. LEXIS 19420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Wakefield",
          "cluster_id": 4480090,
          "cite": [
            "2018 COA 37",
            "428 P.3d 639"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maseratti",
          "cluster_id": 5861,
          "cite": [
            "1 F.3d 330",
            "1993 WL 326573"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gardner",
          "cluster_id": 839169,
          "cite": [
            "753 N.W.2d 78",
            "482 Mich. 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmen Denise Heredia",
          "cluster_id": 797504,
          "cite": [
            "483 F.3d 913",
            "2007 U.S. App. LEXIS 9911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathews v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112012 OR 9431220 OR 9431221 OR 9431222 OR 9431223) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTY5NjgzMjAwMDAwJnM9MzAwMDIxOCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112012+OR+9431220+OR+9431221+OR+9431222+OR+9431223%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(112012 OR 9431220 OR 9431221 OR 9431222 OR 9431223)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgmcz01MTI1NzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112012+OR+9431220+OR+9431221+OR+9431222+OR+9431223%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112012 OR 9431220 OR 9431221 OR 9431222 OR 9431223)",
        "reviewed": 28,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 28,
        "triage_read": 0,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112012 OR 9431220 OR 9431221 OR 9431222 OR 9431223)",
    "indexed_citing_opinions": 753,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112012,
        "count": 653,
        "count_source": "search"
      },
      {
        "opinion_id": 9431220,
        "count": 107,
        "count_source": "search"
      },
      {
        "opinion_id": 9431221,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431222,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431223,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1244,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mathews-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0MTImcz05NDIyMDM4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112012+OR+9431220+OR+9431221+OR+9431222+OR+9431223%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112012,
        "cited_id": 94425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 107009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 108308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 108412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 108799,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 109437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 111603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 251729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 257213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 265540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 290218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 330367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 382671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 392820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 416916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 435958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 445051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 448198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 449562,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 456043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 464967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 470999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112012,
        "cited_id": 478010,
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
    "date_created": "2026-07-05T12:26:18Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:26:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:26:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:53:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:26:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mathews v. United States

```
<div>
<center><b><span class="citation" data-id="9431220"><a href="/opinion/112012/mathews-v-united-states/" aria-description="Citation for case: Mathews v. United States">485 U.S. 58</a></span> (1988)</b></center>
<center><h1>MATHEWS<br>
v.<br>
UNITED STATES</h1></center>
<center>No. 86-6109.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 2, 1987</center>
<center>Decided February 24, 1988</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT
<p><span class="star-pagination">*59</span> <i>Franklyn M. Gimbel,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./481/1046/">481 U. S. 1046</a></span>, argued the cause for petitioner. With him on the briefs were <i>Jeffrey A. Kaufman</i> and <i>Marna M. Tess-Mattner.</i></p>
<p><i>Charles A. Rothfeld</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Fried, Assistant Attorney General Weld,</i> and <i>Deputy Solicitor General Bryson.</i></p>
<p>CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>This case requires the Court to decide whether a defendant in a federal criminal prosecution who denies commission of the crime may nonetheless have the jury instructed, where the evidence warrants, on the affirmative defense of entrapment. The United States Court of Appeals for the Seventh Circuit upheld the ruling of the District Court, which had refused to instruct the jury as to entrapment because petitioner would not admit committing all of the elements of the crime of accepting a bribe. <span class="citation" data-id="478010"><a href="/opinion/478010/united-states-v-frederick-mathews/" aria-description="Citation for case: United States v. Frederick Mathews">803 F. 2d 325</a></span> (1986). This holding conflicts with decisions of other Courts of Appeals, which have taken a variety of approaches to the question.<sup>[1]</sup> We <span class="star-pagination">*60</span> granted certiorari to resolve this conflict, and we now reverse.</p>
<p>Petitioner was employed by the Small Business Administration (SBA) in Milwaukee, Wisconsin, and was responsible for the SBA's "8A Program," which provided aid to certain small businesses. Under the program, the SBA obtained Government contracts and subcontracted them to program participants. The SBA would then assist the participants in performing the contracts. Midwest Knitting Mills, whose president was James DeShazer, was one of the participants in the 8A Program. DeShazer's principal contact at the SBA was petitioner.</p>
<p>In October 1984, DeShazer complained to a Government customer that petitioner had repeatedly asked for loans. DeShazer believed that petitioner was not providing Midwest with certain 8A Program benefits because DeShazer had not made the requested loans. In early 1985, the Federal Bureau of Investigation (FBI) arranged for DeShazer to assist in the investigation resulting from his complaint. Under FBI surveillance, DeShazer offered petitioner a loan that, according to DeShazer, petitioner had previously requested. <span class="star-pagination">*61</span> Petitioner agreed to accept the loan, and two months later, DeShazer met petitioner at a restaurant and gave him the money. Petitioner was immediately arrested and charged with accepting a gratuity in exchange for an official act. <span class="citation no-link">18 U. S. C. § 201</span>(g).</p>
<p>Before trial petitioner filed a motion <i>in limine</i> seeking to raise an entrapment defense. The District Court denied the motion, ruling that entrapment was not available to petitioner because he would not admit all of the elements (including the requisite mental state) of the offense charged. The District Court did, however, allow petitioner to argue as his first line of defense that his acts "were procurred <i>[sic]</i> by the overt acts of the principle <i>[sic]</i> witness of the Government, Mr. DeShazer."<sup>[2]</sup> App. 131.</p>
<p>At trial, the Government argued that petitioner had accepted the loan in return for cooperation in SBA matters. The Government called DeShazer, who testified both that petitioner had repeatedly asked for loans and that he and petitioner had agreed that the loan at issue would result in SBA-provided benefits for Midwest. The Government also played tape recordings of conversations between DeShazer and petitioner in which they discussed the loan. Petitioner testified in his own defense that although he had accepted the loan, he believed it was a personal loan unrelated to his duties at the SBA. Petitioner stated that he and DeShazer were friends and that he had accepted a personal loan from DeShazer previously. According to petitioner, he was in dire financial straits when DeShazer broached the possibility of providing a loan. Petitioner also testified that DeShazer had stated that he needed quickly to get rid of the money that he was offering to petitioner because he had been hiding the money from his wife and was concerned that she would be upset if she discovered this secret; DeShazer had also stated <span class="star-pagination">*62</span> at one point that if petitioner did not take the money soon, DeShazer would be tempted to spend it.</p>
<p>At the close of the trial, petitioner moved for a "mistrial" because of the District Court's refusal to instruct the jury as to entrapment. The District Court noted that the evidence of entrapment was "shaky at best," <i>ibid.,</i> but rather than premise its denial of petitioner's motion on that ground, the court reaffirmed its earlier ruling that, as a matter of law, petitioner was not entitled to an entrapment instruction because he would not admit committing all elements of the crime charged. The jury subsequently found petitioner guilty.</p>
<p>The United States Court of Appeals for the Seventh Circuit affirmed the District Court's refusal to allow petitioner to argue entrapment:</p>
<blockquote>"When a defendant pleads entrapment, he is asserting that, although he had criminal intent, it was 'the Government's deception [that implanted] the criminal design in the mind of the defendant.' <i>United States</i> v. <i>Russell,</i> <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/" aria-description="Citation for case: United States v. Russell">411 U. S. 423</a></span>, 436 . . . (1973); <i>United States</i> v. <i>Rodgers,</i> <span class="citation" data-id="448198"><a href="/opinion/448198/united-states-v-cleveland-r-rodgers/#550" aria-description="Citation for case: United States v. Cleveland R. Rodgers">755 F. 2d 533, 550</a></span> (7th Cir. 1985). We find this to be inconsistent <i>per se</i> with the defense that the defendant never had the requisite criminal intent. We see no reason to allow [petitioner] or any other defendant to plead these defenses simultaneously." <span class="citation" data-id="478010"><a href="/opinion/478010/united-states-v-frederick-mathews/#327" aria-description="Citation for case: United States v. Frederick Mathews">803 F. 2d, at 327</a></span>.</blockquote>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./480/945/">480 U. S. 945</a></span> (1987), to consider under what circumstances a defendant is entitled to an entrapment instruction. We hold that even if the defendant denies one or more elements of the crime, he is entitled to an entrapment instruction whenever there is sufficient evidence from which a reasonable jury could find entrapment.</p>
<p>Because the parties agree as to the basics of the affirmative defense of entrapment as developed by this Court, there is little reason to chronicle its history in detail. Suffice it to say that the Court has consistently adhered to the view, first enunciated in <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932), <span class="star-pagination">*63</span> that a valid entrapment defense has two related elements: government inducement of the crime, and a lack of predisposition on the part of the defendant to engage in the criminal conduct. See <i>Sherman</i> v. <i>United States,</i> <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#376" aria-description="Citation for case: Sherman v. United States">356 U. S. 369, 376-378</a></span> (1958); <i>United States</i> v. <i>Russell,</i> <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 435-436</a></span> (1973); <i>Hampton</i> v. <i>United States,</i> <span class="citation" data-id="9426380"><a href="/opinion/109437/hampton-v-united-states/#489" aria-description="Citation for case: Hampton v. United States">425 U. S. 484, 489</a></span> (1976). Predisposition, "the principal element in the defense of entrapment," <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#433" aria-description="Citation for case: United States v. Russell"><i>Russell, supra,</i> at 433</a></span>, focuses upon whether the defendant was an "unwary innocent" or, instead, an "unwary criminal" who readily availed himself of the opportunity to perpetrate the crime. <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States"><i>Sherman, supra,</i> at 372</a></span>; <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#436" aria-description="Citation for case: United States v. Russell"><i>Russell, supra,</i> at 436</a></span>. The question of entrapment is generally one for the jury, rather than for the court. <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#377" aria-description="Citation for case: Sherman v. United States"><i>Sherman, supra,</i> at 377</a></span>.</p>
<p>The Government insists that a defendant should not be allowed both to deny the offense and to rely on the affirmative defense of entrapment. Because entrapment presupposes the commission of a crime, <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell"><i>Russell, supra,</i> at 435</a></span>, a jury could not logically conclude that the defendant had both failed to commit the elements of the offense <i>and</i> been entrapped. According to the Government, petitioner is asking to "clai[m] the right to swear that he had no criminal intent and in the same breath to argue that he had one that did not originate with him." <i>United States</i> v. <i>Henry,</i> <span class="citation" data-id="9472863"><a href="/opinion/445051/united-states-v-harold-donald-henry/#214" aria-description="Citation for case: United States v. Harold Donald Henry">749 F. 2d 203, 214</a></span> (CA5 1984) (en banc) (Gee, J., dissenting).</p>
<p>As a general proposition a defendant is entitled to an instruction as to any recognized defense for which there exists evidence sufficient for a reasonable jury to find in his favor. <i>Stevenson</i> v. <i>United States,</i> <span class="citation" data-id="94425"><a href="/opinion/94425/stevenson-v-united-states/" aria-description="Citation for case: Stevenson v. United States">162 U. S. 313</a></span> (1896); 4 C. Torcia, Wharton's Criminal Procedure § 538, p. 11 (12th ed. 1976) (hereinafter Wharton). A parallel rule has been applied in the context of a lesser included offense instruction, see Fed. Rule Crim. Proc. 31(c); <i>Keeble</i> v. <i>United States,</i> <span class="citation" data-id="9425312"><a href="/opinion/108799/keeble-v-united-states/#208" aria-description="Citation for case: Keeble v. United States">412 U. S. 205, 208</a></span> (1973); <i>Sansone</i> v. <i>United States,</i> <span class="citation" data-id="107009"><a href="/opinion/107009/sansone-v-united-states/#349" aria-description="Citation for case: Sansone v. United States">380 U. S. 343, 349</a></span> (1965). In <i><span class="citation" data-id="94425"><a href="/opinion/94425/stevenson-v-united-states/" aria-description="Citation for case: Stevenson v. United States">Stevenson</a></span>,</i> this Court reversed a murder conviction arising out of a gunfight in the Indian Territory. The <span class="star-pagination">*64</span> principal holding of the Court was that the evidence was sufficient to entitle the defendant to a manslaughter instruction, but the Court also decided that the defendant was entitled as well to have the jury instructed on self-defense. The affirmative defense of self-defense is, of course, inconsistent with the claim that the defendant killed in the heat of passion.</p>
<p>Federal appellate cases also permit the raising of inconsistent defenses. See <i>Johnson</i> v. <i>United States,</i> 138 U. S. App. D. C. 174, 179, <span class="citation" data-id="290218"><a href="/opinion/290218/barrington-joseph-johnson-v-united-states/#656" aria-description="Citation for case: Barrington Joseph Johnson v. United States">426 F. 2d 651, 656</a></span> (1970) (the defense in a rape case was permitted to argue that the act did not take place and that the victim consented), cert. dism'd, <span class="citation" data-id="9424523"><a href="/opinion/108308/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">401 U. S. 846</a></span> (1971); see also <i>Womack</i> v. <i>United States,</i> 119 U. S. App. D. C. 40, <span class="citation" data-id="265540"><a href="/opinion/265540/spencer-womack-v-united-states/" aria-description="Citation for case: Spencer Womack v. United States">336 F. 2d 959</a></span> (1964). And state cases support the proposition that a homicide defendant may be entitled to an instruction on both accident and self-defense, two inconsistent affirmative defenses. 4 Wharton § 545, p. 32.</p>
<p>The Government points out that inconsistent pleading is specifically authorized under the Federal Rules of Civil Procedure, but that there is no parallel authorization under the Federal Rules of Criminal Procedure. Rule 8(e)(2) of the Federal Rules of Civil Procedure provides in relevant part:</p>
<blockquote>"A party may set forth two or more statements of a claim or defense alternately or hypothetically, either in one count or defense or in separate counts or defenses. . . . <i>A party may also state as many separate claims or defenses as he has regardless of consistency</i> and whether based on legal, equitable or maritime grounds. All statements shall be made subject to the obligations set forth in Rule 11." (Emphasis added.)</blockquote>
<p>The absence of a cognate provision affecting criminal trials, we think, is not because the Rules intended to more severely restrict criminal defendants than civil parties, but because of the much less elaborate system of pleadings  particularly with respect to the defendant  in a criminal case. The issues of fact in a criminal trial are usually developed by the evidence adduced and the court's instructions to the jury. A <span class="star-pagination">*65</span> simple plea of not guilty, Fed. Rule Crim. Proc. 11, puts the prosecution to its proof as to all elements of the crime charged, and raises the defense of entrapment. <i>Sorrells,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#452" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 452</a></span>. The only matters required to be specially pleaded by a defendant are notice of alibi, Fed. Rule Crim. Proc. 12.1, or of intent to rely on insanity as a defense, Fed. Rule Crim. Proc. 12.2.</p>
<p>The Government argues that allowing a defendant to rely on inconsistent defenses will encourage perjury, lead to jury confusion, and subvert the truth-finding function of the trial. These same concerns are, however, present in the civil context, yet inconsistency is expressly allowed under the Federal Rules of Civil Procedure. We do not think that allowing inconsistency necessarily sanctions perjury. Here petitioner wished to testify that he had no intent to commit the crime, and have his attorney argue to the jury that if it concluded otherwise, then it should consider whether that intent was the result of Government inducement. The jury would have considered inconsistent defenses, but petitioner would not have necessarily testified untruthfully.</p>
<p>We would not go so far as to say that charges on inconsistent defenses may not on occasion increase the risk of perjury, but particularly in the case of entrapment we think the practical consequences will be less burdensome than the Government fears. The Court of Appeals in <i>United States</i> v. <i>Demma,</i> <span class="citation" data-id="9462183"><a href="/opinion/330367/united-states-v-anthony-j-demma-united-states-of-america-v-henry-brulay/#985" aria-description="Citation for case: United States v. Anthony J. Demma, United States of...">523 F. 2d 981, 985</a></span> (CA9 1975) (en banc), observed:</p>
<blockquote>"Of course, it is very unlikely that the defendant will be able to prove entrapment without testifying and, in the course of testifying, without admitting that he did the acts charged. . . . When he takes the stand, the defendant forfeits his right to remain silent, subjects himself to all the rigors of cross-examination, including impeachment, and exposes himself to prosecution for perjury. Inconsistent testimony by the defendant seriously impairs and potentially destroys his credibility. While we hold that a defendant may both deny the acts <span class="star-pagination">*66</span> and other elements necessary to constitute the crime charged and at the same time claim entrapment, the high risks to him make it unlikely as a strategic matter that he will choose to do so."</blockquote>
<p>The Government finally contends that since the entrapment defense is not of "constitutional dimension," <i>Russell,</i> <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#433" aria-description="Citation for case: United States v. Russell">411 U. S., at 433</a></span>, and that since it is "relatively limited," <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell"><i>id.,</i> at 435</a></span>, Congress would be free to make the entrapment defense available on whatever conditions and to whatever category of defendants it believed appropriate. Congress, of course, has never spoken on the subject, and so the decision is left to the courts. We are simply not persuaded by the Government's arguments that we should make the availability of an instruction on entrapment where the evidence justifies it subject to a requirement of consistency to which no other such defense is subject.</p>
<p>The Government contends as an alternative basis for affirming the judgment below that the evidence at trial was insufficient to support an instruction on the defense of entrapment. Of course evidence that Government agents merely afforded an opportunity or facilities for the commission of the crime would be insufficient to warrant such an instruction. But this question was pretermitted by the Court of Appeals, and it will be open for consideration by that court on remand.</p>
<p><i>Reversed and remanded.</i></p>
<p>JUSTICE KENNEDY took no part in the consideration or decision of this case.</p>
<p>JUSTICE BRENNAN, concurring.</p>
<p>I join the Court's opinion. I write separately only because I have previously joined or written four opinions dissenting from this Court's holdings that the defendant's predisposition is relevant to the entrapment defense. <i>Hampton</i> v. <i>United States,</i> <span class="citation" data-id="9426380"><a href="/opinion/109437/hampton-v-united-states/#495" aria-description="Citation for case: Hampton v. United States">425 U. S. 484, 495</a></span> (1976) (BRENNAN, J., dissenting); <span class="star-pagination">*67</span> <i>United States</i> v. <i>Russell,</i> <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#436" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 436</a></span> (1973) (Douglas, J., dissenting); <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#439" aria-description="Citation for case: United States v. Russell"><i>id.,</i> at 439</a></span> (Stewart, J., dissenting); <i>Sherman</i> v. <i>United States,</i> <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#378" aria-description="Citation for case: Sherman v. United States">356 U. S. 369, 378</a></span> (1958) (Frankfurter, J., concurring in judgment). See also <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#453" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435, 453</a></span> (1932) (Roberts, J., concurring in judgment). Although some governmental misconduct might be sufficiently egregious to violate due process, <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#431" aria-description="Citation for case: United States v. Russell"><i>Russell, supra,</i> at 431-432</a></span>, my differences with the Court have been based on statutory interpretation and federal common law, not on the Constitution. Were I judging on a clean slate, I would still be inclined to adopt the view that the entrapment defense should focus exclusively on the Government's conduct. But I am not writing on a clean slate; the Court has spoken definitively on this point. Therefore I bow to <i>stare decisis,</i> and today join the judgment and reasoning of the Court.</p>
<p>JUSTICE SCALIA, concurring in the judgment.</p>
<p>I concur in the judgment of the Court because in my view the defense of entrapment will rarely be genuinely inconsistent with the defense on the merits, and when genuine inconsistency exists its effect in destroying the defendant's credibility will suffice to protect the interests of justice.</p>
<p>The typical case presenting the issue before us here is one in which the defendant introduces evidence to the effect that he did not commit the unlawful acts, or did not commit them with the requisite unlawful intent, and also introduces evidence to show his lack of predisposition and inordinate government inducement. There is nothing inconsistent in these showings. The inconsistency alleged by the government is a purely formal one, which arises only if entrapment is defined to require not only (1) inordinate government inducement to commit a crime, (2) directed at a person not predisposed to commit the crime, but also (3) causing that person to commit the crime. If the third element is added to the definition, counsel's argument to the jury cannot claim entrapment without admitting the crime. But I see no reason why the third <span class="star-pagination">*68</span> element is essential, unless it is for the very purpose of rendering the defense unavailable without admission of the crime. Surely it does not add anything of substance to the findings the jury must make, since findings of (1) inordinate inducement plus (2) lack of predisposition will almost inevitably produce a conclusion of (3) causality. To be sure, entrapment cannot be available as a defense unless a crime by the object of the entrapment is established, since if there is no crime there is nothing to defend against; but in that sense all affirmative defenses assume commission of the crime.</p>
<p>My point is not that entrapment must be defined to exclude element (3). Whether it is or not, since that element seems to me unnecessary to achieve the social policy fostered by the defense I am not willing to declare the defense unavailable when it produces the formal inconsistency of the defendant's simultaneously denying the crime and asserting entrapment which assumes commission of the crime. I would not necessarily accept such formal inconsistency for other defenses, where the element contradicted is a functionally essential element of the defense.</p>
<p>Of course in the entrapment context, as elsewhere, the defendant's case may involve genuine, <i>non</i>formal inconsistency. The defendant might testify, for example, that he was not in the motel room where the illegal drugs changed hands, and that the drugs were pressed upon him in the motel room by agents of the government. But that kind of genuine inconsistency here, as elsewhere, is self-penalizing. There is nothing distinctive about entrapment that justifies a special prophylactic rule.</p>
<p>JUSTICE WHITE, with whom JUSTICE BLACKMUN joins, dissenting.</p>
<p>At his criminal trial, petitioner took the stand and flatly denied accepting a loan "for or because of any official act." App. 128-130; <span class="citation no-link">18 U. S. C. § 201</span>(g). Petitioner later moved for a mistrial because the District Court would not permit <span class="star-pagination">*69</span> him to rely on that testimony while he simultaneously argued that, in fact, he <i>had</i> accepted a loan for an official act, but only at the Government's instigation. Today, the Court holds that this rather sensible ruling on the part of the District Court constitutes reversible error. The reasons the Court offers for reaching this conclusion are not at all persuasive, and I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>The Court properly recognizes that its result is not compelled by the Constitution. As the Court acknowledges, petitioner has no Fifth or Sixth Amendment right to conduct the inconsistent entrapment defense that he wished to mount at trial. <i>Ante,</i> at 66. And yet, if the Constitution does not compel reversal of the decision below, then what does?</p>
<p>Certainly not any Act of Congress, or the Federal Rules of Criminal Procedure. As the majority candidly admits, "Congress . . . has never spoken on the subject [at issue here], and so the decision is left to the courts." <i><span class="citation no-link">Ibid.</span></i> Moreover, the Court also frankly notes that while the Federal Rules of Civil Procedure contain a provision expressly authorizing inconsistent defenses, Fed. Rule Civ. Proc. 8(e)(2), the Federal Criminal Rules are without any such authorization. <i>Ante,</i> at 64. Indeed, the rather scant authority the majority cites in support of its view that inconsistent defenses are generally permitted in criminal trials, <i>ibid.,</i> is strongly suggestive of just how extraordinary such pleadings are in the criminal context.<sup>[1]</sup></p>
<p><span class="star-pagination">*70</span> Nor is the result the Court reaches urged by a predominance of authority in the lower courts. As the Court recognizes, only two Circuits have held, as the Court does today, that a criminal defendant may deny committing the elements of a crime, and then contend that the Government entrapped him into the offense. The remaining Circuits are far more restrained in their allowance of such inconsistent defenses, divided along the lines the majority discusses in its opinion. <i>Ante,</i> at 59-60, n. 1.</p>
<p>Thus, neither the Constitution, nor a statute, nor the Criminal Rules, nor the bulk of authority compels us to reverse petitioner's conviction. Nor does the Court claim support from any of these sources for its decision. Instead, the majority rests almost exclusively on an application of the "general proposition [that] a defendant is entitled to an instruction as to any legally sufficient defense for which there exists evidence sufficient for a reasonable jury to find in his favor." <i>Ante,</i> at 63. There are several reasons, however, why this "general proposition" is inapposite here.</p>
<p></p>
<h2>II</h2>
<p>First, there is the unique nature of the entrapment defense. There is a valuable purpose served by having civil litigants plead alternative defenses which may be legally inconsistent. Allowing a tort defendant to claim both that he owed no duty of care to the plaintiff, but that if he did, he met that duty, preserves possible alternative defenses under which the defendant is entitled to relief. It prevents formalities of pleadings, or rigid application of legal doctrines, from standing in the way of the equitable resolution of a civil dispute. See generally 2A J. Moore, J. Lucas, &amp; G. Grotheer, Moore's Federal Practice ¶ 8.32, pp. 8-224  8-229 (2d ed. 1987). The same may be true for <i>some</i> criminal defenses <span class="star-pagination">*71</span> (such as "self-defense" or "provocation") where a defendant may truthfully testify as to the facts of the crime, leaving it to his counsel to argue that these facts make out, as a matter of law, several possible defenses.</p>
<p>But the entrapment defense, by contrast, "is a relatively limited defense"; it is only available to "a defendant who has committed all the elements of a proscribed offense." <i>United States</i> v. <i>Russell,</i> <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 435</a></span> (1973). Thus, when a defendant (as petitioner did here) testifies that he did not commit the elements of the offense he is charged with, the defense of entrapment is <i>not</i> a plausible alternative legal theory of the case; rather, it is a proper defense <i>only</i> if the accused is lying. We have rejected before the notion that a defendant has a right to lie at trial, or a right to solicit his attorney's aid in executing such a defense strategy. See <i>Nix</i> v. <i>Whiteside,</i> <span class="citation" data-id="9430360"><a href="/opinion/111603/nix-v-whiteside/#173" aria-description="Citation for case: Nix v. Whiteside">475 U. S. 157, 173</a></span> (1986). And there is respectable authority for concluding that no legitimate end of the criminal justice system is served by requiring a trial court to entertain such tactics, in the form of an entrapment defense which is at odds with the defendant's own testimony.<sup>[2]</sup></p>
<p>Allowing such inconsistency in defense tactics invites the scourge of an effective criminal justice system: perjury. In the past, we have taken extraordinary steps to combat perjury in criminal trials; these steps have even included permitting the admission of otherwise inadmissible evidence to prevent a defendant from procuring an acquittal via false testimony. See, <i>e. g., </i><i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#720" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 720-723</a></span> (1975); <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York">401 U. S. 222, 225-226</a></span> (1971). Yet today, the Court reaches a result which it concedes "may . . . on occasion" increase the risk of perjury. <i>Ante,</i> at 65. This is reason enough to reject the Court's result. Worse still, the majority's prognostication may well <span class="star-pagination">*72</span> be an understatement. Even if  as the Court suggests, <i><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">ibid.</a></span></i>  inconsistent defenses do not measurably increase the frequency of perjury in civil trials, the risk of perjury in a criminal trial is always greater than in a civil setting because the stakes are so much higher. See <i>Britt</i> v. <i>North Carolina,</i> <span class="citation" data-id="9424695"><a href="/opinion/108412/britt-v-north-carolina/#238" aria-description="Citation for case: Britt v. North Carolina">404 U. S. 226, 238</a></span> (1971) (Douglas, J., dissenting). Absent some constitutional or statutory mandate to conduct criminal trials in a particular way, we should be taking steps to minimize, not increase, the danger of perjured testimony.</p>
<p>After all, a criminal trial is not a game or a sport. "[T]he very nature of a trial [i]s a search for truth." <i>Nix</i> v. <span class="citation" data-id="9430360"><a href="/opinion/111603/nix-v-whiteside/#166" aria-description="Citation for case: Nix v. Whiteside"><i>Whiteside, supra,</i> at 166</a></span>. This observation is particularly applicable to criminal trials, which are the means by which we affix our most serious judgments of individual guilt or innocence. It is fundamentally inconsistent with this understanding of criminal justice to permit a defendant to win acquittal on a rationale which he states, under oath, to be false. "Permitting a defendant to argue two defenses that cannot both be true is equivalent to sanctioning perjury by the defendant." See Note, Entrapment and Denial of the Crime: A Defense of the Inconsistency Rule, 1986 Duke L. J. 866, 883-884.</p>
<p>Finally, even if the Court's decision does not result in increased perjury at criminal trials, it will  at the very least  result in increased confusion among criminal juries.<sup>[3]</sup> The lower courts have rightly warned that jury confusion is likely to result from allowing a defendant to say "I did not do it" <span class="star-pagination">*73</span> while his lawyer argues "he did it, but the government tricked him into it." See, <i>e. g., </i><i>United States</i> v. <i>Dorta,</i> <span class="citation" data-id="8938495"><a href="/opinion/8947819/united-states-v-dorta/#1182" aria-description="Citation for case: United States v. Dorta">783 F. 2d 1179, 1182</a></span> (CA4 1986). Creating such confusion may enable some defendants to win acquittal on the entrapment defense, but only under the peculiar circumstances where a jury rejects the defendant's own stated view of the facts. We have not previously endorsed defense efforts to prevail at trial by playing such "shell games" with the jury; rather, we have written that "[a] defendant has no entitlement to the luck of a lawless decisionmaker." <i>Strickland</i> v. <i>Washington,</i> <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#695" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668, 695</a></span> (1984). Nor, it should be added, is there any entitlement to a baffled decisionmaker.</p>
<p></p>
<h2>III</h2>
<p>Ultimately, only petitioner knows whether he accepted a loan in exchange for an official act, or whether he obtained it as a personal favor. Today, the Court holds that petitioner has a right to take the stand and claim the latter, while having his attorney argue that he was entrapped into doing the former. Nothing counsels such a result  let alone compels it. Hence this dissent.</p>
<h2>NOTES</h2>
<p>[1]  Two other Circuits have adopted the approach taken by the Seventh Circuit. See <i>United States</i> v. <i>Hill,</i> <span class="citation" data-id="9468206"><a href="/opinion/392820/united-states-v-paul-hill/#514" aria-description="Citation for case: United States v. Paul Hill">655 F. 2d 512, 514</a></span> (CA3 1981); <i>United States</i> v. <i>Whitley,</i> <span class="citation" data-id="435958"><a href="/opinion/435958/united-states-v-whitley/#1139" aria-description="Citation for case: United States v. Whitley">734 F. 2d 1129, 1139</a></span> (CA6 1984). Four Circuits have ruled that a defendant may not affirmatively deny committing the elements of the crime if he desires an entrapment instruction. <i>United States</i> v. <i>Annese,</i> <span class="citation" data-id="382671"><a href="/opinion/382671/united-states-v-jerald-annese-united-states-of-america-v-nicholas-tavano/#1046" aria-description="Citation for case: United States v. Jerald Annese, United States of America...">631 F. 2d 1041, 1046-1047</a></span> (CA1 1980); <i>United States</i> v. <i>Mayo,</i> <span class="citation" data-id="416916"><a href="/opinion/416916/united-states-v-harold-f-mayo-jr-and-mark-a-mcgarghan/#72" aria-description="Citation for case: United States v. Harold F. Mayo, Jr. And Mark A. McGarghan">705 F. 2d 62, 72-73</a></span> (CA2 1983); <i>United States</i> v. <i>Dorta,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/783/1179/">783 F. 2d 1179</a></span>, 1181 (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./477/905/">477 U. S. 905</a></span> (1986); <i>United States</i> v. <i>Mora,</i> <span class="citation" data-id="456043"><a href="/opinion/456043/united-states-v-richard-mora/#1198" aria-description="Citation for case: United States v. Richard Mora">768 F. 2d 1197, 1198-1199</a></span> (CA10 1985), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./474/1083/">474 U. S. 1083</a></span> (1986). One Circuit has declared that a defendant denying the elements of the crime may rely on entrapment if the issue is raised by the Government's evidence. <i>United States</i> v. <i>Smith,</i> <span class="citation" data-id="9473276"><a href="/opinion/449562/united-states-v-timothy-rand-smith/#1169" aria-description="Citation for case: United States v. Timothy Rand Smith">757 F. 2d 1161, 1169</a></span> (CA11 1985). Another Circuit has developed a hybrid rule allowing a testifying defendant to contest the intent element of the offense charged, but not the acts, while arguing entrapment. <i>United States</i> v. <i>Henry,</i> <span class="citation" data-id="9472863"><a href="/opinion/445051/united-states-v-harold-donald-henry/" aria-description="Citation for case: United States v. Harold Donald Henry">749 F. 2d 203</a></span> (CA5 1984) (en banc); two Circuits have ruled that a defendant is entitled to an entrapment instruction even if he testifies and denies all elements of the offense. <i>United States</i> v. <i>Demma,</i> <span class="citation" data-id="9462183"><a href="/opinion/330367/united-states-v-anthony-j-demma-united-states-of-america-v-henry-brulay/" aria-description="Citation for case: United States v. Anthony J. Demma, United States of...">523 F. 2d 981</a></span> (CA9 1975) (en banc); <i>Hansford</i> v. <i>United States,</i> 112 U. S. App. D. C. 359, <span class="citation" data-id="257213"><a href="/opinion/257213/david-louis-hansford-v-united-states/" aria-description="Citation for case: David Louis Hansford v. United States">303 F. 2d 219</a></span> (1962). We note also that even within the Circuits, the decisions have been contradictory and inconsistent.</p>
<p>[2]  In pursuing this line of defense, petitioner apparently introduced the same evidence that he planned to adduce in support of his entrapment claim.</p>
<p>[1]  While some cases have explicitly permitted inconsistent criminal defenses outside of the entrapment area, <i>e. g., </i><i>Whittaker</i> v. <i>United States,</i> 108 U. S. App. D. C. 268, 269, <span class="citation" data-id="251729"><a href="/opinion/251729/james-allen-whittaker-v-united-states/#632" aria-description="Citation for case: James Allen Whittaker v. United States">281 F. 2d 631, 632</a></span> (1960), others have been less receptive to this defense strategy, see, <i>e. g., </i><i>United States</i> v. <i>Ervin,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/436/1331/">436 F. 2d 1331</a></span>, 1334 (CA5 1971); <i>Blunt</i> v. <i>United States,</i> 131 U. S. App. D. C. 306, 312, n. 12, <span class="citation" data-id="282808"><a href="/opinion/282808/thomas-e-blunt-v-united-states/#1289" aria-description="Citation for case: Thomas E. Blunt v. United States">404 F. 2d 1283, 1289, n. 12</a></span> (1968). Given the rarity of reported federal cases on this question, drawing any conclusion about the prevailing practice in the federal courts is difficult. See Note, Entrapment and Denial of the Crime: A Defense of the Inconsistency Rule, 1986 Duke L. J. 866, 878-879, and n. 127.</p>
<p>[2]  See, <i>e. g., </i><i>United States</i> v. <i>Dorta,</i> <span class="citation" data-id="8938495"><a href="/opinion/8947819/united-states-v-dorta/#1181" aria-description="Citation for case: United States v. Dorta">783 F. 2d 1179, 1181-1182</a></span> (CA4 1986); <i>United States</i> v. <i>Smith,</i> <span class="citation" data-id="9473276"><a href="/opinion/449562/united-states-v-timothy-rand-smith/#1167" aria-description="Citation for case: United States v. Timothy Rand Smith">757 F. 2d 1161, 1167-1168</a></span> (CA11 1985); <i>United States</i> v. <i>Henry,</i> <span class="citation" data-id="9472863"><a href="/opinion/445051/united-states-v-harold-donald-henry/#214" aria-description="Citation for case: United States v. Harold Donald Henry">749 F. 2d 203, 214-216</a></span> (CA5 1984) (en banc) (Gee, J., dissenting).</p>
<p>[3]  Again, the fact that the system endures the jury confusion caused by inconsistent civil defenses is no support for the Court's conclusion here. For one thing, reliability is obviously a more important concern in criminal cases than in civil.
</p>
<p>Moreover, in civil cases, the trial court has the option of ordering the jury to complete a special verdict form, thus minimizing any errors in judgment which may result from inconsistent defenses. See Fed. Rule Civ. Proc. 49(a). The Criminal Rules contain no similar provision, cf. Fed. Rule Crim. Proc. 31, and "as a general rule special verdicts are disfavored in criminal cases," see <i>United States</i> v. <i>Buishas,</i> <span class="citation" data-id="470999"><a href="/opinion/470999/united-states-v-john-m-buishas-charles-r-gies-and-william-j-michael/#1317" aria-description="Citation for case: United States v. John M. Buishas, Charles R. Gies and...">791 F. 2d 1310, 1317</a></span> (CA7 1986).</p>

</div>
```

---
