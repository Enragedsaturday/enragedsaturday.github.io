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

## GROUP: _overhaul2/lake/cases/California v. Carney.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "California v. Carney"
type: case
citation: "471 U.S. 386 (1985)"
parallel_cite: "105 S. Ct. 2066; 85 L. Ed. 2d 406; 53 U.S.L.W. 4521"
neutral_cite: 1985 U.S. LEXIS 8
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-05-13
docket: 83-859
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-05-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Carney
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111423/california-v-carney/"
  cluster_id: 111423
  opinion_id: 9430011
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[United States v. Ross]]", "[[California v. Acevedo]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "motor-home", "mobility"]
holding: "The automobile exception applies to a motor home being used as a vehicle, and articulates the exception's TWO justifications: (1) ready…"
lake:
  record_id: California v. Carney
  status: verified
  projected_at: 2026-07-09
---

# California v. Carney

*471 U.S. 386 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on information that Carney was exchanging marijuana for sex inside his motor home, agents watched a youth enter and leave it, stopped the youth, and then — without a warrant, on probable cause — entered the motor home parked in a downtown lot and found marijuana. Carney argued his motor home was more like a home than a vehicle.

## Issue
Whether the automobile exception to the warrant requirement applies to a motor home that is readily mobile.

## Rule
The vehicle exception rests on two justifications: "the pervasive schemes of regulation, which necessarily lead to reduced expectations of privacy, and the exigencies attendant to ready mobility justify searches without prior recourse to the authority of a magistrate so long as the overriding standard of probable cause is met." — 471 U.S. at 392. ^pin-392

Both come into play for a readily mobile vehicle: "First, the vehicle is obviously readily mobile by the turn of an ignition key, if not actually moving. Second, there is a reduced expectation of privacy stemming from its use as a licensed motor vehicle subject to a range of police regulation inapplicable to a fixed dwelling." — [*Id.* at 393](https://www.courtlistener.com/opinion/111423/california-v-carney/#:~:text=First%2C%20the%20vehicle%20is%20obviously). ^pin-393

## Application
Carney's motor home was readily mobile — licensed, on the public roads, and parked in a lot rather than set up as a residence — and was subject to the pervasive regulation that reduces privacy expectations in vehicles. Both justifications applied, so the warrantless search on probable cause fell within the automobile exception despite the vehicle's homelike attributes.

## Conclusion
The automobile exception applied to the motor home; the judgment suppressing the marijuana was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Carney* states the modern two-justification rationale for the automobile exception rooted in [[Carroll v. United States]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *California v. Carney*, 471 U.S. 386 (1985) — https://www.courtlistener.com/opinion/111423/california-v-carney/ — pinpoints: 392, 393.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "02ad54d38db6cdd2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "California v. Carney"}, "payload": {"all": [{"cite": "471 U.S. 386", "page": "386", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "471"}, {"cite": "105 S. Ct. 2066", "page": "2066", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "85 L. Ed. 2d 406", "page": "406", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "85"}, {"cite": "1985 U.S. LEXIS 8", "page": "8", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4521", "page": "4521", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "471 U.S. 386", "official": {"cite": "471 U.S. 386", "page": "386", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "471"}, "official_selection_present": true, "record_id": "California v. Carney"}}
{"assertion_id": "7fdc5e66ac7038ef", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-392", "record_id": "California v. Carney"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-392", "pinpoint_status": "slip-only", "quote": "--- # California v. Carney *471 U.S. 386 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on information that Carney was exchanging marijuana for sex inside his motor home, agents watched a youth enter and leave it, stopped the youth, and then — without a warrant, on probable cause — entered the motor home parked in a downtown lot and found marijuana. Carney argued his motor home was more like a home than a vehicle. ## Issue Whether the automobile exception to the warrant requirement applies to a motor home that is readily mobile. ## Rule The vehicle exception rests on two justifications:", "quote_fidelity": "mismatch", "record_id": "California v. Carney", "star_marker": null}}
{"assertion_id": "843f1d0f3bbb0eb4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-393", "record_id": "California v. Carney"}, "payload": {"fragment": "#:~:text=First%2C%20the%20vehicle%20is%20obviously", "page": null, "pin_id": "pin-393", "pinpoint_status": "star-verified", "quote": "First, the vehicle is obviously readily mobile by the turn of an ignition key, if not actually moving. Second, there is a reduced expectation of privacy stemming from its use as a licensed motor vehicle subject to a range of police regulation inapplicable to a fixed dwelling.", "quote_fidelity": "matched", "record_id": "California v. Carney", "star_marker": "393"}}
{"assertion_id": "4a2c620265b30090", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "California v. Carney"}, "payload": {"as_of_content": "1985-05-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "California v. Carney", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — California v. Carney

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Carney",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "California v. Carney",
    "case_name_short": "Carney",
    "case_name_full": "California v. Carney",
    "input_case_name": "California v. Carney",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-05-13",
    "year": 1985,
    "docket": "83-859",
    "cluster_id": 111423,
    "lead_opinion_id": 9430011,
    "sibling_ids": [
      111423,
      9430011,
      9430012
    ],
    "absolute_url": "/opinion/111423/california-v-carney/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "471 U.S. 386",
      "volume": "471",
      "reporter": "U.S.",
      "page": "386",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 2066",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "2066",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 2d 406",
        "volume": "85",
        "reporter": "L. Ed. 2d",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4521",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4521",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 8",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "8",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "471 U.S. 386",
        "volume": "471",
        "reporter": "U.S.",
        "page": "386",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 2066",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "2066",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 2d 406",
        "volume": "85",
        "reporter": "L. Ed. 2d",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 8",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "8",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4521",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4521",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "471 U.S. 386",
    "official_selection": {
      "court_class": "scotus",
      "selected": "471 U.S. 386",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-392",
      "page": null,
      "quote": "--- # California v. Carney *471 U.S. 386 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on information that Carney was exchanging marijuana for sex inside his motor home, agents watched a youth enter and leave it, stopped the youth, and then \u2014 without a warrant, on probable cause \u2014 entered the motor home parked in a downtown lot and found marijuana. Carney argued his motor home was more like a home than a vehicle. ## Issue Whether the automobile exception to the warrant requirement applies to a motor home that is readily mobile. ## Rule The vehicle exception rests on two justifications:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-393",
      "page": null,
      "quote": "First, the vehicle is obviously readily mobile by the turn of an ignition key, if not actually moving. Second, there is a reduced expectation of privacy stemming from its use as a licensed motor vehicle subject to a range of police regulation inapplicable to a fixed dwelling.",
      "star_marker": "393",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 16130,
      "fragment": "#:~:text=First%2C%20the%20vehicle%20is%20obviously",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-05-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Carney",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Davenport",
          "cluster_id": 4743495,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sanborn",
          "cluster_id": 4404766,
          "cite": [
            "477 Mass. 393",
            "77 N.E.3d 274"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane1_negative"
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
        "journal_ref": "California v. Carney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Waxler",
          "cluster_id": 2656340,
          "cite": [
            "224 Cal. App. 4th 712",
            "168 Cal. Rptr. 3d 822",
            "2014 WL 935470",
            "2014 Cal. App. LEXIS 227"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Superintendent, Mass. Correctional Institution at Walpole v. Hill",
          "cluster_id": 111476,
          "cite": [
            "86 L. Ed. 2d 356",
            "105 S. Ct. 2768",
            "472 U.S. 445",
            "1985 U.S. LEXIS 109",
            "53 U.S.L.W. 4778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Fensterer",
          "cluster_id": 111535,
          "cite": [
            "88 L. Ed. 2d 15",
            "106 S. Ct. 292",
            "474 U.S. 15",
            "1985 U.S. LEXIS 137",
            "54 U.S.L.W. 3301"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Claytor",
          "cluster_id": 3951703,
          "cite": [
            "620 N.E.2d 906",
            "85 Ohio App. 3d 623",
            "1993 Ohio App. LEXIS 1930"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Dyson",
          "cluster_id": 2621047,
          "cite": [
            "144 L. Ed. 2d 442",
            "119 S. Ct. 2013",
            "527 U.S. 465",
            "1999 U.S. LEXIS 4200"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gomez",
          "cluster_id": 2613548,
          "cite": [
            "932 P.2d 1",
            "122 N.M. 777",
            "1997 NMSC 006"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Koedatich",
          "cluster_id": 2159212,
          "cite": [
            "548 A.2d 939",
            "112 N.J. 225",
            "1988 N.J. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hubert v. State",
          "cluster_id": 1464366,
          "cite": [
            "312 S.W.3d 554",
            "2010 Tex. Crim. App. LEXIS 636",
            "2010 WL 2077166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. William L. Witt(074468)",
          "cluster_id": 2993869,
          "cite": [
            "223 N.J. 409",
            "126 A.3d 850",
            "2015 N.J. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carlo Scott Bagley",
          "cluster_id": 457913,
          "cite": [
            "772 F.2d 482",
            "19 Fed. R. Serv. 222",
            "1985 U.S. App. LEXIS 23309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
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
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keehn v. State",
          "cluster_id": 2341745,
          "cite": [
            "279 S.W.3d 330",
            "2009 Tex. Crim. App. LEXIS 425",
            "2009 WL 774854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randy Graham",
          "cluster_id": 775981,
          "cite": [
            "275 F.3d 490",
            "2001 U.S. App. LEXIS 26685",
            "2001 WL 1636805"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Klein v. City of San Clemente",
          "cluster_id": 1435788,
          "cite": [
            "584 F.3d 1196",
            "2009 U.S. App. LEXIS 21642",
            "2009 WL 3152381"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Carney:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111423 OR 9430011 OR 9430012) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzQ0NDcwNDAwMDAwJnM9MzA5MzgwMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111423+OR+9430011+OR+9430012%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(111423 OR 9430011 OR 9430012)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTAmcz00MzI2OTI5JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111423+OR+9430011+OR+9430012%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111423 OR 9430011 OR 9430012)",
        "reviewed": 49,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 49,
        "triage_read": 0,
        "triage_snippet_classified": 49
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111423 OR 9430011 OR 9430012)",
    "indexed_citing_opinions": 793,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111423,
        "count": 671,
        "count_source": "search"
      },
      {
        "opinion_id": 9430011,
        "count": 139,
        "count_source": "search"
      },
      {
        "opinion_id": 9430012,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1277,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-carney.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNzE1NDImcz0xMDMxNTIzMiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111423+OR+9430011+OR+9430012%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111423,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 110466,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 110951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111339,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 303550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 308034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 326862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 337764,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 347602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 361203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 377893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 382242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 396356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 414134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 1132273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 1204049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 1278177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 1290893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 1719125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 1997533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 2111273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 2128583,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 2163745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 2181717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111423,
        "cited_id": 2615223,
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
    "date_created": "2026-07-04T21:26:11Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:29:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Carney

```
<opinion type="majority">
<author id="b457-12">Chief Justice Burger</author>
<p id="AT-">delivered the opinion of the Court.</p>
<p id="b457-13">We granted certiorari to decide whether law enforcement agents violated the Fourth Amendment when they conducted a warrantless search, based on probable cause, of a fully mobile “motor home” located in a public place.</p>
<p id="b457-14">H-I</p>
<p id="b457-3">On May 31, 1979, Drug Enforcement Agency Agent Robert Williams watched respondent, Charles Carney, ap<page-number citation-index="1" label="388">*388</page-number>proach a youth in downtown San Diego. The youth accompanied Carney to a Dodge Mini Motor Home parked in a nearby lot. Carney and the youth closed the window shades in the motor home, including one across the front window. Agent Williams had previously received uncorroborated information that the same motor home was used by another person who was exchanging marihuana for sex. Williams, with assistance from other agents, kept the motor home under surveillance for the entire one and one-quarter hours that Carney and the youth remained inside. When the youth left the motor home, the agents followed and stopped him. The youth told the agents that he had received marihuana in return for allowing Carney sexual contacts.</p>
<p id="b458-4">At the agents’ request, the youth returned to the motor home and knocked on its door; Carney stepped out. The agents identified themselves as law enforcement officers. Without a warrant or consent, one agent entered the motor home and observed marihuana, plastic bags, and a scale of the kind used in weighing drugs on a table. Agent Williams took Carney into custody and took possession of the motor home. A subsequent search of the motor home at the police station revealed additional marihuana in the cupboards and refrigerator.</p>
<p id="b458-5">Respondent was charged with possession of marihuana for sale. At a preliminary hearing, he moved to suppress the evidence discovered in the motor home. The Magistrate denied the motion, upholding the initial search as a justifiable search for other persons, and the subsequent search as a routine inventory search.</p>
<p id="b458-6">Respondent renewed his suppression motion in the Superior Court. The Superior Court also rejected the claim, holding that there was probable cause to arrest respondent, that the search of the motor home was authorized under the automobile exception to the Fourth Amendment’s warrant requirement, and that the motor home itself could be seized without a warrant as an instrumentality of the crime. Re<page-number citation-index="1" label="389">*389</page-number>spondent then pleaded <em>nolo contendere </em>to the charges against him, and was placed on probation for three years.</p>
<p id="b459-5">Respondent appealed from the order placing him on probation. The California Court of Appeal affirmed, reasoning that the vehicle exception applied to respondent’s motor home. <span class="citation no-link">117 Cal. App. 3d 36</span>, <span class="citation no-link">172 Cal. Rptr. 430</span> (1981).</p>
<p id="b459-6">The California Supreme Court reversed the conviction. <span class="citation" data-id="9793378"><a href="/opinion/2615223/people-v-carney/" aria-description="Citation for case: People v. Carney">34 Cal. 3d 597</a></span>, <span class="citation" data-id="9793378"><a href="/opinion/2615223/people-v-carney/" aria-description="Citation for case: People v. Carney">668 P. 2d 807</a></span> (1983). The Supreme Court did not disagree with the conclusion of the trial court that the agents had probable cause to arrest respondent and to believe that the vehicle contained evidence of a crime; however, the court held that the search was unreasonable because no warrant was obtained, rejecting the State’s argument that the vehicle exception to the warrant requirement should apply.<footnotemark>1</footnotemark> That court reached its decision by concluding that the mobility of a vehicle “is no longer the prime justification for the automobile exception; rather, ‘the answer lies in the diminished expectation of privacy which surrounds the automobile.’” <span class="citation" data-id="9793378"><a href="/opinion/2615223/people-v-carney/#605" aria-description="Citation for case: People v. Carney"><em>Id., </em>at 605</a></span>, <span class="citation" data-id="9793378"><a href="/opinion/2615223/people-v-carney/#811" aria-description="Citation for case: People v. Carney">668 P. 2d, at 811</a></span>. The California Supreme Court held that the expectations of privacy in a motor home are more like those in a dwelling than in an automobile because the primary function of motor homes is not to provide transportation but to “provide the occupant with living quarters.” <span class="citation" data-id="9793378"><a href="/opinion/2615223/people-v-carney/#606" aria-description="Citation for case: People v. Carney"><em>Id., </em>at 606</a></span>, <span class="citation" data-id="9793378"><a href="/opinion/2615223/people-v-carney/#812" aria-description="Citation for case: People v. Carney">668 P. 2d, at 812</a></span>.</p>
<p id="b459-7">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./465/1098/">465 U. S. 1098</a></span> (1984). We reverse.</p>
<p id="b460-7"><page-number citation-index="1" label="390">*390</page-number>1 — 1 I — I</p>
<p id="b460-3">The Fourth Amendment protects the right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” This fundamental right is preserved by a requirement that searches be conducted pursuant to a warrant issued by an independent judicial officer. There are, of course, exceptions to the general rule that a warrant must be secured before a search is undertaken; one is the so-called “automobile exception” at issue in this case. This exception to the warrant requirement was first set forth by the Court 60 years ago in <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). There, the Court recognized that the privacy interests in an automobile are constitutionally protected; however, it held that the ready mobility of the automobile justifies a lesser degree of protection of those interests. The Court rested this exception on a long-recognized distinction between stationary structures and vehicles:</p>
<blockquote id="b460-4">“[T]he guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant because the vehicle can be <em>quickly moved </em>out of the locality or jurisdiction in which the warrant must be sought.” <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><em>Id., </em>at 153</a></span> (emphasis added).</blockquote>
<p id="b460-5">The capacity to be “quickly moved” was clearly the basis of the holding in <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>, </em>and our cases have consistently recognized ready mobility as one of the principal bases of the automobile exception. See, <em>e. g., Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#59" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 59</a></span> (1967); <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52</a></span> (1970); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#442" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 442</a></span> (1973); <page-number citation-index="1" label="391">*391</page-number><em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#588" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 588</a></span> (1974); <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367</a></span> (1976). In <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>, </em>for example, commenting on the rationale for the vehicle exception, we noted that “the opportunity to search is fleeting since a car is readily movable.” <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 51</a></span>. More recently, in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#806" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 806</a></span> (1982), we once again emphasized that “an immediate intrusion is necessary” because of “the nature of an automobile in transit. . . .” The mobility of automobiles, we have observed, “creates circumstances of such exigency that, as a practical necessity, rigorous enforcement of the warrant requirement is impossible.” <em>South Dakota </em>v. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 367</a></span>.</p>
<p id="b461-5">However, although ready mobility alone was perhaps the original justification for the vehicle exception, our later cases have made clear that ready mobility is not the only basis for the exception. The reasons for the vehicle exception, we have said, are twofold. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 367</a></span>. “Besides the element of mobility, less rigorous warrant requirements govern because the expectation of privacy with respect to one’s automobile is significantly less than that relating to one’s home or office.” <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Ibid.</a></span></em></p>
<p id="b461-6">Even in cases where an automobile was not immediately mobile, the lesser expectation of privacy resulting from its use as a readily mobile vehicle justified application of the vehicular exception. See, <em>e. g., Cady </em>v. <em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski, supra.</a></span> </em>In some cases, the configuration of the vehicle contributed to the lower expectations of privacy; for example, we held in <em>Cardwell </em>v. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis"><em>Lewis, supra, </em>at 590</a></span>, that, because the passenger compartment of a standard automobile is relatively open to plain view, there are lesser expectations of privacy. But even when enclosed “repository” areas have been involved, we have concluded that the lesser expectations of privacy warrant application of the exception. We have applied the exception in the context of a locked car trunk, <em>Cady </em>v. <em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski, supra,</a></span> </em>a sealed package in a car trunk, <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross, supra,</a></span> </em>a closed compartment under the dashboard, <em>Cham</em><page-number citation-index="1" label="392">*392</page-number><em>bers </em>v. <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra,</a></span> </em>the interior of a vehicle’s upholstery, <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span> </em>or sealed packages inside a covered pickup truck, <em>United States </em>v. <em>Johns, </em><span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/" aria-description="Citation for case: United States v. Johns">469 U. S. 478</a></span> (1985).</p>
<p id="b462-4">These reduced expectations of privacy derive not from the fact that the area to be searched is in plain view, but from the pervasive regulation of vehicles capable of traveling on the public highways. <em>Cady </em>v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#440" aria-description="Citation for case: Cady v. Dombrowski"><em>Dombrowski, supra, </em>at 440-441</a></span>. As we explained in <em>South Dakota </em>v. <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>, </em>an inventory search case:</p>
<blockquote id="b462-5">“Automobiles, unlike homes, are subjected to pervasive and continuing governmental regulation and controls, including periodic inspection and licensing requirements. As an everyday occurrence, police stop and examine vehicles when license plates or inspection stickers have expired, or if other violations, such as exhaust fumes or excessive noise, are noted, or if headlights or other safety equipment are not in proper working order.” <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 368</a></span>.</blockquote>
<p id="b462-6">The public is fully aware that it is accorded less privacy in its automobiles because of this compelling governmental need for regulation. Historically, “individuals always [have] been on notice that movable vessels may be stopped and searched on facts giving rise to probable cause that the vehicle contains contraband, without the protection afforded by a magistrate’s prior evaluation of those facts.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#806" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em>at 806, n. 8</a></span>. In short, the pervasive schemes of regulation, which necessarily lead to reduced expectations of privacy, and the exigencies attendant to ready mobility justify searches without prior recourse to the authority of a magistrate so long as the overriding standard of probable cause is met.</p>
<p id="b462-7">When a vehicle is being used on the highways, or if it is readily capable of such use and is found stationary in a place not regularly used for residential purposes — temporary or otherwise — the two justifications for the vehicle exception <page-number citation-index="1" label="393">*393</page-number>come into play.<footnotemark>2</footnotemark> First, the vehicle is obviously readily mobile by the turn of an ignition key, if not actually moving. Second, there is a reduced expectation of privacy stemming from its use as a licensed motor vehicle subject to a range of police regulation inapplicable to a fixed dwelling. At least in these circumstances, the overriding societal interests in effective law enforcement justify an immediate search before the vehicle and its occupants become unavailable.</p>
<p id="b463-5">While it is true that respondent’s vehicle possessed some, if not many of the attributes of a home, it is equally clear that the vehicle falls clearly within the scope of the exception laid down in <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>and applied in succeeding cases. Like the automobile in <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>, </em>respondent’s motor home was readily mobile. Absent the prompt search and seizure, it could readily have been moved beyond the reach of the police. Furthermore, the vehicle was licensed to “operate on public streets; [was] serviced in public places;. . . and [was] subject to extensive regulation and inspection.” <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#154" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 154, n. 2</a></span> (1978) (Powell, J., concurring). And the vehicle was so situated that an objective observer would conclude that it was being used not as a residence, but as a vehicle.</p>
<p id="b463-6">Respondent urges us to distinguish his vehicle from other vehicles within the exception because it was <em>capable of functioning as a home. </em>In our increasingly mobile society, many vehicles used for transportation can be and are being used not only for transportation but for shelter, <em>i. e., </em>as a “home” or “residence.” To distinguish between respondent’s motor home and an ordinary sedan for purposes of the vehicle exception would require that we apply the exception depending upon the size of the vehicle and the quality of its appointments. Moreover, to fail to apply the exception to vehicles <page-number citation-index="1" label="394">*394</page-number>such as a motor home ignores the fact that a motor home lends itself easily to use as an instrument of illicit drug traffic and other illegal activity. In <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross">456 U. S., at 822</a></span>, we declined to distinguish between “worthy” and “unworthy” containers, noting that “the central purpose of the Fourth Amendment forecloses such a distinction. ” We decline today to distinguish between “worthy” and “unworthy” vehicles which are either on the public roads and highways, or situated such that it is reasonable to conclude that the vehicle is not being used as a residence.</p>
<p id="b464-7">Our application of the vehicle exception has never turned on the other uses to which a vehicle might be put. The exception has historically turned on the ready mobility of the vehicle, and on the presence of the vehicle in a setting that objectively indicates that the vehicle is being used for transportation.<footnotemark>3</footnotemark> These two requirements for application of the exception ensure that law enforcement officials are not unnecessarily hamstrung in their efforts to detect and prosecute criminal activity, and that the legitimate privacy interests of the public are protected. Applyingthe vehicle exception in these circumstances allows the essential purposes served by the exception to be fulfilled, while assuring that the exception will acknowledge legitimate privacy interests.</p>
<p id="b464-3">III</p>
<p id="Azh">The question remains whether, apart from the lack of a warrant, this search was unreasonable. Under the vehicle exception to the warrant requirement, “[ojnly the prior approval of the magistrate is waived; the search otherwise [must be such] as the magistrate could authorize.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em>at 823</a></span>.</p>
<p id="b465-4"><page-number citation-index="1" label="395">*395</page-number>This search was not unreasonable; it was plainly one that the magistrate could authorize if presented with these facts. The DEA agents had fresh, direct, uncontradicted evidence that the respondent was distributing a controlled substance from the vehicle, apart from evidence of other possible offenses. The agents thus had abundant probable cause to enter and search the vehicle for evidence of a crime notwithstanding its possible use as a dwelling place.</p>
<p id="b465-5">The judgment of the California Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b465-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b459-8"> Respondent contends that the state-court decision rests on an adequate and independent state ground, because the opinion refers to the State as well as the Federal Constitution. Respondent’s argument is clearly foreclosed by our opinion in <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040-1041</a></span> (1983), in which we held, “when... a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so.” We read the opinion as resting on federal law.</p>
</footnote>
<footnote label="2">
<p id="b463-7"> With few exceptions, the courts have not hesitated to apply the vehicle exception to vehicles other than automobiles. See, <em>e. g., United States </em>v. <em>Rollins, </em><span class="citation" data-id="414134"><a href="/opinion/414134/united-states-v-dennis-albert-rollins-junior-n-enfinger-and-john-d/" aria-description="Citation for case: United States v. Dennis Albert Rollins, Junior N....">699 F. 2d 530</a></span> (CA11) (airplane), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/933/">464 U. S. 933</a></span> (1983).</p>
</footnote>
<footnote label="3">
<p id="b464-4"> We need not pass on the application of the vehicle exception to a motor home that is situated in a way or place that objectively indicates that it is being used as a residence. Among the factors that might be relevant in determining whether a warrant would be required in such a circumstance is its location, whether the vehicle is readily mobile or instead, for instance, elevated on blocks, whether the vehicle is licensed, whether it is connected to utilities, and whether it has convenient access to a public road.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/California v. Ciraolo.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "California v. Ciraolo"
type: case
citation: "476 U.S. 207 (1986)"
parallel_cite: "106 S. Ct. 1809; 90 L. Ed. 2d 210"
neutral_cite: 1986 U.S. LEXIS 154
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-06-30
docket: 84-1513
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-05-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Ciraolo
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111666/california-v-ciraolo/"
  cluster_id: 111666
  opinion_id: 9430502
  identity_checked: true
homes:
  - page: "[[Aerial and Enhanced Surveillance]]"
    role: "Key — Anchor"
related: ["[[Florida v. Riley]]", "[[California v. Greenwood]]", "[[Kyllo v. United States]]", "[[Florida v. Jardines]]"]
aliases: []
tags: ["case", "fourth-amendment", "curtilage", "aerial-surveillance", "expectation-of-privacy"]
holding: "Warrantless naked-eye aerial observation of a fenced curtilage from navigable airspace (1,000 ft) is not a search — no reasonable expectation of privacy from the air."
lake:
  record_id: California v. Ciraolo
  status: verified
  projected_at: 2026-07-06
---

# California v. Ciraolo

*476 U.S. 207 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on an anonymous tip that marijuana was growing in Ciraolo's backyard, officers who could not see over his two fences flew a private plane over the property at 1,000 feet and identified marijuana plants in the fenced yard with the naked eye. They used those observations to obtain a search warrant.

## Issue
Whether warrantless, naked-eye aerial observation of a fenced backyard within the [[Curtilage|curtilage]], from public navigable airspace, is a search under the Fourth Amendment.

## Rule
"In an age where private and commercial flight in the public airways is routine, it is unreasonable for respondent to expect that his marijuana plants were constitutionally protected from being observed with the naked eye from an altitude of 1,000 feet. The Fourth Amendment simply does not require the police traveling in the public airways at this altitude to obtain a warrant in order to observe what is visible to the naked eye." — 476 U.S. at 215. ^pin-215

## Application
Although Ciraolo's yard was within the [[Curtilage|curtilage]] and shielded by fences from ground-level view, the plants were knowingly exposed to anyone flying overhead in lawful navigable airspace. The officers' naked-eye observation from 1,000 feet was therefore not a search, and the warrant obtained from those observations was valid.

## Conclusion
The aerial observation was not a Fourth Amendment search; the judgment suppressing the evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ciraolo* was **followed** by [[Florida v. Riley]] (helicopter at 400 feet) and is **distinguished** from sense-enhancing-technology cases such as [[Kyllo v. United States]] and the physical-intrusion analysis of [[Florida v. Jardines]].

## Appears on
- [[Aerial and Enhanced Surveillance]] — *Key — Anchor*

## Sources
- *California v. Ciraolo*, 476 U.S. 207 (1986) — https://www.courtlistener.com/opinion/111666/california-v-ciraolo/ — pinpoint: 215.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f6233c0c9164a3b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "California v. Ciraolo"}, "payload": {"all": [{"cite": "476 U.S. 207", "page": "207", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "476"}, {"cite": "106 S. Ct. 1809", "page": "1809", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "106"}, {"cite": "90 L. Ed. 2d 210", "page": "210", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "1986 U.S. LEXIS 154", "page": "154", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}], "display": "476 U.S. 207", "official": {"cite": "476 U.S. 207", "page": "207", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "476"}, "official_selection_present": true, "record_id": "California v. Ciraolo"}}
{"assertion_id": "f94131b17f2a574d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-215", "record_id": "California v. Ciraolo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-215", "pinpoint_status": "slip-only", "quote": "--- # California v. Ciraolo *476 U.S. 207 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on an anonymous tip that marijuana was growing in Ciraolo's backyard, officers who could not see over his two fences flew a private plane over the property at 1,000 feet and identified marijuana plants in the fenced yard with the naked eye. They used those observations to obtain a search warrant. ## Issue Whether warrantless, naked-eye aerial observation of a fenced backyard within the curtilage, from public navigable airspace, is a search under the Fourth Amendment. ## Rule", "quote_fidelity": "mismatch", "record_id": "California v. Ciraolo", "star_marker": null}}
{"assertion_id": "fafff916c44ec794", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "California v. Ciraolo"}, "payload": {"as_of_content": "1986-05-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "California v. Ciraolo", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — California v. Ciraolo

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Ciraolo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "California v. Ciraolo",
    "case_name_short": "Ciraolo",
    "case_name_full": "California v. Ciraolo",
    "input_case_name": "California v. Ciraolo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-06-30",
    "year": 1986,
    "docket": "84-1513",
    "cluster_id": 111666,
    "lead_opinion_id": 9430502,
    "sibling_ids": [
      111666,
      9430502,
      9430503
    ],
    "absolute_url": "/opinion/111666/california-v-ciraolo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "476 U.S. 207",
      "volume": "476",
      "reporter": "U.S.",
      "page": "207",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1809",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1809",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 L. Ed. 2d 210",
        "volume": "90",
        "reporter": "L. Ed. 2d",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 154",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "476 U.S. 207",
        "volume": "476",
        "reporter": "U.S.",
        "page": "207",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1809",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1809",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 L. Ed. 2d 210",
        "volume": "90",
        "reporter": "L. Ed. 2d",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 154",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "476 U.S. 207",
    "official_selection": {
      "court_class": "scotus",
      "selected": "476 U.S. 207",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-215",
      "page": null,
      "quote": "--- # California v. Ciraolo *476 U.S. 207 (1986)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on an anonymous tip that marijuana was growing in Ciraolo's backyard, officers who could not see over his two fences flew a private plane over the property at 1,000 feet and identified marijuana plants in the fenced yard with the naked eye. They used those observations to obtain a search warrant. ## Issue Whether warrantless, naked-eye aerial observation of a fenced backyard within the curtilage, from public navigable airspace, is a search under the Fourth Amendment. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-05-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Ciraolo",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. O'Donnell",
          "cluster_id": 4427767,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rigel",
          "cluster_id": 4426623,
          "cite": [
            "2017 Ohio 7640",
            "97 N.E.3d 825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Villagran",
          "cluster_id": 4422358,
          "cite": [
            "477 Mass. 711",
            "81 N.E.3d 310"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christopher Covey v. Assessor of Ohio County",
          "cluster_id": 2773276,
          "cite": [
            "777 F.3d 186",
            "2015 WL 309598",
            "2015 U.S. App. LEXIS 1113"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
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
        "journal_ref": "California v. Ciraolo:lane1_negative"
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
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Knutson",
          "cluster_id": 2718239,
          "cite": [
            "288 Neb. 823"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Maury",
          "cluster_id": 2598797,
          "cite": [
            "68 P.3d 1",
            "133 Cal. Rptr. 2d 561",
            "30 Cal. 4th 342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bowers v. Hardwick",
          "cluster_id": 111738,
          "cite": [
            "92 L. Ed. 2d 140",
            "106 S. Ct. 2841",
            "478 U.S. 186",
            "1986 U.S. LEXIS 123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Claytor",
          "cluster_id": 3951703,
          "cite": [
            "620 N.E.2d 906",
            "85 Ohio App. 3d 623",
            "1993 Ohio App. LEXIS 1930"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Harris",
          "cluster_id": 112413,
          "cite": [
            "109 L. Ed. 2d 13",
            "110 S. Ct. 1640",
            "495 U.S. 14",
            "1990 U.S. LEXIS 2037",
            "58 U.S.L.W. 4457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warshak",
          "cluster_id": 181032,
          "cite": [
            "631 F.3d 266",
            "2010 U.S. App. LEXIS 25415",
            "2010 WL 5071766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reedy v. Evanson",
          "cluster_id": 152023,
          "cite": [
            "615 F.3d 197",
            "2010 U.S. App. LEXIS 15974",
            "2010 WL 2991378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heller v. District of Columbia",
          "cluster_id": 614652,
          "cite": [
            "670 F.3d 1244",
            "399 U.S. App. D.C. 314",
            "2011 U.S. App. LEXIS 20130",
            "2011 WL 4551558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
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
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tyrell J.",
          "cluster_id": 1258965,
          "cite": [
            "876 P.2d 519",
            "8 Cal. 4th 68",
            "32 Cal. Rptr. 2d 33",
            "94 Cal. Daily Op. Serv. 5846",
            "94 Daily Journal DAR 10633",
            "1994 Cal. LEXIS 3897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 5607956,
          "cite": [
            "23 Cal. 4th 789",
            "3 P.3d 311",
            "2000 Daily Journal DAR 7789",
            "97 Cal. Rptr. 2d 914",
            "2000 Cal. Daily Op. Serv. 5894",
            "2000 Cal. LEXIS 5217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Fields Christopher Crawley",
          "cluster_id": 740479,
          "cite": [
            "113 F.3d 313",
            "1997 U.S. App. LEXIS 10728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Ciraolo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111666 OR 9430502 OR 9430503) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzY2MTU2ODAwMDAwJnM9Mjk0ODMxNyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111666+OR+9430502+OR+9430503%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(111666 OR 9430502 OR 9430503)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDUmcz04MDEzMzUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111666+OR+9430502+OR+9430503%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111666 OR 9430502 OR 9430503)",
        "reviewed": 53,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 53,
        "triage_read": 1,
        "triage_snippet_classified": 52
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111666 OR 9430502 OR 9430503)",
    "indexed_citing_opinions": 724,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111666,
        "count": 597,
        "count_source": "search"
      },
      {
        "opinion_id": 9430502,
        "count": 142,
        "count_source": "search"
      },
      {
        "opinion_id": 9430503,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1256,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-ciraolo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNjI4NTUmcz0xMDI2NTcxNSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111666+OR+9430502+OR+9430503%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111666,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 358699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 388191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 2176782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111666,
        "cited_id": 2443377,
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
    "date_created": "2026-07-04T21:29:45Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:30:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:30:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:34:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:30:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Ciraolo

```
<opinion type="majority">
<author id="b273-4"><page-number citation-index="1" label="209">*209</page-number>Chief Justice Burger</author>
<p id="Ab6">delivered the opinion of the Court.</p>
<p id="b273-5">We granted certiorari to determine whether the Fourth Amendment is violated by aerial observation without a warrant from an altitude of 1,000 feet of a fenced-in backyard within the curtilage of a home.</p>
<p id="b273-6">I</p>
<p id="b273-7">On September 2, 1982, Santa Clara Police received an anonymous telephone tip that marijuana was growing in respondent’s backyard. Police were unable to observe the contents of respondent’s yard from ground level because of a 6-foot outer fence and a 10-foot inner fence completely enclosing the yard. Later that day, Officer Shutz, who was assigned to investigate, secured a private plane and flew over respondent’s house at an altitude of 1,000 feet, within navigable airspace; he was accompanied by Officer Rodriguez. Both officers were trained in marijuana identification. From the overflight, the officers readily identified marijuana plants 8 feet to 10 feet in height growing in a 15- by 25-foot plot in respondent’s yard; they photographed the area with a standard 35mm camera.</p>
<p id="b273-8">On September 8, 1982, Officer Shutz obtained a search warrant on the basis of an affidavit describing the anonymous tip and their observations; a photograph depicting respondent’s house, the backyard, and neighboring homes was attached to the affidavit as an exhibit. The warrant was <page-number citation-index="1" label="210">*210</page-number>executed the next day and 73 plants were seized; it is not disputed that these were marijuana.</p>
<p id="AJz">After the trial court denied respondent’s motion to suppress the evidence of the search, respondent pleaded guilty to a charge of cultivation of marijuana. The California Court of Appeal reversed, however, on the ground that the warrantless aerial <em>observation </em>of respondent’s yard which led to the issuance of the warrant violated the Fourth Amendment. <span class="citation" data-id="2176782"><a href="/opinion/2176782/people-v-ciraolo/" aria-description="Citation for case: People v. Ciraolo">161 Cal. App. 3d 1081</a></span>, <span class="citation" data-id="2176782"><a href="/opinion/2176782/people-v-ciraolo/" aria-description="Citation for case: People v. Ciraolo">208 Cal. Rptr. 93</a></span> (1984). That court held first that respondent’s backyard marijuana garden was within the “curtilage” of his home, under <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984). The court emphasized that the height and existence of the two fences constituted “objective criteria from which we may conclude he manifested a reasonable expectation of privacy by any standard.” <span class="citation" data-id="2176782"><a href="/opinion/2176782/people-v-ciraolo/#1089" aria-description="Citation for case: People v. Ciraolo">161 Cal. App. 3d, at 1089</a></span>, <span class="citation" data-id="2176782"><a href="/opinion/2176782/people-v-ciraolo/#97" aria-description="Citation for case: People v. Ciraolo">208 Cal. Rptr., at 97</a></span>.</p>
<p id="b274-7">Examining the particular method of surveillance undertaken, the court then found it “significant” that the flyover “was not the result of a routine patrol conducted for any other legitimate law enforcement or public safety objective, but was undertaken for the specific purpose of observing this particular enclosure within [respondent’s] curtilage.” <em><span class="citation" data-id="2176782"><a href="/opinion/2176782/people-v-ciraolo/" aria-description="Citation for case: People v. Ciraolo">Ibid.</a></span> </em>It held this focused observation was “a direct and unauthorized intrusion into the sanctity of the home” which violated respondent’s reasonable expectation of privacy. <span class="citation" data-id="2176782"><a href="/opinion/2176782/people-v-ciraolo/#1089" aria-description="Citation for case: People v. Ciraolo"><em>Id., </em>at 1089-1090</a></span>, <span class="citation" data-id="2176782"><a href="/opinion/2176782/people-v-ciraolo/#98" aria-description="Citation for case: People v. Ciraolo">208 Cal. Rptr., at 98</a></span> (footnote omitted). The California Supreme Court denied the State’s petition for review.</p>
<p id="b274-8">We granted the State’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./471/1134/">471 U. S. 1134</a></span> (1985). We reverse.</p>
<p id="b274-9">The State argues that respondent has “knowingly exposed” his backyard to aerial observation, because all that was seen was visible to the naked eye from any aircraft flying overhead. The State analogizes its mode of observation to a knothole or opening in a fence: if there is an opening, the police may look.</p>
<p id="b275-4"><page-number citation-index="1" label="211">*211</page-number>The California Court of Appeal, as we noted earlier, accepted the analysis that unlike the casual observation of a private person flying overhead, this flight was focused specifically on a small suburban yard, and was not the result of any routine patrol overflight. Respondent contends he has done all that can reasonably be expected to tell the world he wishes to maintain the privacy of his garden within the curtilage without covering his yard. Such covering, he argues, would defeat its purpose as an outside living area; he asserts he has not “knowingly” exposed himself to aerial views.</p>
<p id="b275-5">II</p>
<p id="b275-6">The touchstone of Fourth Amendment analysis is whether a person has a “constitutionally protected reasonable expectation of privacy.” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360</a></span> (1967) (Harlan, J., concurring). <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>posits a two-part inquiry: first, has the individual manifested a subjective expectation of privacy in the object of the challenged search? Second, is society willing to recognize that expectation as reasonable? See <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 740</a></span> (1979).</p>
<p id="b275-7">Clearly — and understandably — respondent has met the test of manifesting his own subjective intent and desire to maintain privacy as to his unlawful agricultural pursuits. However, we need not address that issue, for the State has not challenged the finding of the California Court of Appeal that respondent had such an expectation. It can reasonably be assumed that the 10-foot fence was placed to conceal the marijuana crop from at least street-level views. So far as the normal sidewalk traffic was concerned, this fence served that purpose, because respondent “took normal precautions to maintain his privacy.” <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#105" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 105</a></span> (1980).</p>
<p id="b275-8">Yet a 10-foot fence might not shield these plants from the eyes of a citizen or a policeman perched on the top of a truck or a two-level bus. Whether respondent therefore manifested <page-number citation-index="1" label="212">*212</page-number>a subjective expectation of privacy from <em>all </em>observations of his backyard, or whether instead he manifested merely a hope that no one would observe his unlawful gardening pursuits, is not entirely clear in these circumstances. Respondent appears to challenge the authority of government to observe his activity from any vantage point or place if the viewing is motivated by a law enforcement purpose, and not the result of a casual, accidental observation.</p>
<p id="b276-4">We turn, therefore, to the second inquiry under <em>Katz, i. e., </em>whether that expectation is reasonable. In pursuing this inquiry, we must keep in mind that “[t]he test of legitimacy is not whether the individual chooses to conceal assertedly ‘private’ activity,” but instead “whether the government’s intrusion infringes upon the personal and societal values protected by the Fourth Amendment.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#181" aria-description="Citation for case: Oliver v. United States"><em>Oliver, supra, </em>at 181-183</a></span>.</p>
<p id="b276-5">Respondent argues that because his yard was in the curtilage of his home, no governmental aerial observation is permissible under the Fourth Amendment without a warrant.<footnotemark>1</footnotemark> The history and genesis of the curtilage doctrine are instructive. “At common law, the curtilage is the area to which extends the intimate activity associated with the ‘sanctity of a man’s home and the privacies of life.’” <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver, supra,</a></span> </em>at 180 (quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886)). See 4 Blackstone, Commentaries *225. The <page-number citation-index="1" label="213">*213</page-number>protection afforded the curtilage is essentially a protection of families and personal privacy in an area intimately linked to the home, both physically and psychologically, where privacy expectations are most heightened. The claimed area here was immediately adjacent to a suburban home, surrounded by high double fences. This close nexus to the home would appear to encompass this small area within the curtilage. Accepting, as the State does, that this yard and its crop fall within the curtilage, the question remains whether naked-eye observation of the curtilage by police from an aircraft lawfully operating at an altitude of 1,000 feet violates an expectation of privacy that is reasonable.</p>
<p id="b277-5">That the area is within the curtilage does not itself bar all police observation. The Fourth Amendment protection of the home has never been extended to require law enforcement officers to shield their eyes when passing by a home on public thoroughfares. Nor does the mere fact that an individual has taken measures to restrict some views of his activities preclude an officer’s observations from a public vantage point where he has a right to be and which renders the activities clearly visible. <em>E. g., United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#282" aria-description="Citation for case: United States v. Knotts">460 U. S. 276, 282</a></span> (1983). “What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 351</a></span>.</p>
<p id="b277-6">The observations by Officers Shutz and Rodriguez in this case took place within public navigable airspace, see 49 U. S. C. App. §1304, in a physically nonintrusive manner; from this point they were able to observe plants readily discernible to the naked eye as marijuana. That the observation from aircraft was directed at identifying the plants and the officers were trained to recognize marijuana is irrelevant. Such observation is precisely what a judicial officer needs to provide a basis for a warrant. Any member of the public flying in this airspace who glanced down could have seen <page-number citation-index="1" label="214">*214</page-number>everything that these officers observed. On this record, we readily conclude that respondent’s expectation that his garden was protected from such observation is unreasonable and is not an expectation that society is prepared to honor.<footnotemark>2</footnotemark></p>
<p id="b278-5">The dissent contends that the Court ignores Justice Harlan’s warning in his concurrence in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361-362</a></span>, that the Fourth Amendment should not be limited to proscribing only physical intrusions onto private property. <em>Post, </em>at 215-216. But Justice Harlan’s observations about future electronic developments and the potential for electronic interference with private communications, see <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#362" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 362</a></span>, were plainly not aimed at simple visual observations from a public place. Indeed, since <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>the Court has required warrants for electronic surveillance aimed at intercepting private conversations. See <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297</a></span> (1972).</p>
<p id="b278-6">Justice Harlan made it crystal clear that he was resting on the reality that one who enters a telephone booth is entitled to assume that his conversation. is not being intercepted. This does not translate readily into a rule of constitutional dimensions that one who grows illicit drugs in his backyard is “entitled to assume” his unlawful conduct will not be ob<page-number citation-index="1" label="215">*215</page-number>served by a passing aircraft — or by a power company repair mechanic on a pole overlooking the yard. As Justice Harlan emphasized,</p>
<blockquote id="b279-5">“a man’s home is, for most purposes, a place where he expects privacy, but objects, activities, or statements that he exposes to the ‘plain view’ of outsiders are not ‘protected’ because no intention to keep them to himself has been exhibited. On the other hand, conversations in the open would not be protected against being overheard, for the expectation of privacy under the circumstances would be unreasonable.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 361</a></span>.</blockquote>
<p id="b279-6">One can reasonably doubt that in 1967 Justice Harlan considered an aircraft within the category of future “electronic” developments that could stealthily intrude upon an individual’s privacy. In an age where private and commercial flight in the public airways is routine, it is unreasonable for respondent to expect that his marijuana plants were constitutionally protected from being observed with the naked eye from an altitude of 1,000 feet. The Fourth Amendment simply does not require the police traveling in the public airways at this altitude to obtain a warrant in order to observe what is visible to the naked eye.<footnotemark>3</footnotemark></p>
<p id="b279-7">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b276-6"> Because the parties framed the issue in the California courts below and in this Court as concerning only the reasonableness of aerial observation generally, see Pet. for Cert, i, without raising any distinct issue as to the photograph attached as an exhibit to the affidavit in support of the search warrant, our analysis is similarly circumscribed. It was the officer’s observation, not the photograph, that supported the warrant. Officer Shutz testified that the photograph did not identify the marijuana as such because it failed to reveal a “true representation” of the color of the plants: “you have to see it with the naked eye.” App. 36.</p>
</footnote>
<footnote label="2">
<p id="b278-7"> The California Court of Appeal recognized that police have the right to use navigable airspace, but made a pointed distinction between police aircraft focusing on a particular home and police aircraft engaged in a “routine patrol.” It concluded that the officers’ “focused” observations violated respondent’s reasonable expectations of privacy. In short, that court concluded that a regular police patrol plane identifying respondent’s marijuana would lead to a different result. Whether this is a rational distinction is hardly relevant, although we find difficulty understanding exactly how respondent’s expectations of privacy from aerial observation might differ when two airplanes pass overhead at identical altitudes, simply for different purposes. We are cited to no authority for this novel analysis or the conclusion it begat. The fact that a ground-level observation by police “focused” on a particular place is not different from a “focused” aerial observation under the Fourth Amendment.</p>
</footnote>
<footnote label="3">
<p id="b279-10"> In <em>Dow Chemical Co. </em>v. <em>United States, post, </em>p. 227, decided today, we hold that the use of an aerial mapping camera to photograph an industrial manufacturing complex from navigable airspace similarly does not require a warrant under the Fourth Amendment. The State acknowledges that “[ajerial observation of curtilage may become invasive, either due to physical intrusiveness or through modern technology which discloses to the senses those intimate associations, objects or activities otherwise imperceptible to police or fellow citizens.” Brief for Petitioner 14-15.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/California v. Greenwood.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "California v. Greenwood"
type: case
citation: "486 U.S. 35 (1988)"
parallel_cite: "108 S. Ct. 1625; 100 L. Ed. 2d 30; 56 U.S.L.W. 4409"
neutral_cite: 1988 U.S. LEXIS 2279
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-05-16
docket: 86-684
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-05-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Greenwood
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112067/california-v-greenwood/"
  cluster_id: 112067
  opinion_id: 9431296
  identity_checked: true
homes:
  - page: "[[Abandonment]]"
    role: "Key — Progeny / Refinement"
related: ["[[Abel v. United States]]", "[[Katz v. United States]]", "[[California v. Ciraolo]]"]
aliases: []
tags: ["case", "fourth-amendment", "abandonment", "garbage", "expectation-of-privacy"]
holding: "No reasonable expectation of privacy in garbage bags left for collection at the curb, outside the curtilage; warrantless search/seizure of curbside trash does not violate the 4A."
lake:
  record_id: California v. Greenwood
  status: verified
  projected_at: 2026-07-06
---

# California v. Greenwood

*486 U.S. 35 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on information that Greenwood might be dealing drugs, police asked his regular trash collector to set aside the opaque garbage bags Greenwood left at the curb for pickup. Searching the bags, officers found evidence of narcotics use, which they used to obtain warrants to search the house.

## Issue
Whether the warrantless search and seizure of garbage left for collection at the curb, outside the home's [[Curtilage|curtilage]], violates the Fourth Amendment.

## Rule
"Here, we conclude that respondents exposed their garbage to the public sufficiently to defeat their claim to Fourth Amendment protection." — 486 U.S. at 40. ^pin-40

"It is common knowledge that plastic garbage bags left on or at the side of a public street are readily accessible to animals, children, scavengers, snoops, and other members of the public." — *Id.* ^pin-40b

## Application
Greenwood placed his garbage in opaque bags at the curb for collection by a third party — exposing it to animals, scavengers, the public, and the trash collector who could have sorted through it or handed it to police. He thus had no objectively [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the discarded items, and the warrantless search of the bags did not violate the Fourth Amendment.

## Conclusion
There was no Fourth Amendment violation; the judgment suppressing the evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Greenwood* applies the exposure/abandonment principle alongside [[Abel v. United States]] and the knowing-exposure logic of [[Katz v. United States]].

## Appears on
- [[Abandonment]] — *Key — Progeny / Refinement*

## Sources
- *California v. Greenwood*, 486 U.S. 35 (1988) — https://www.courtlistener.com/opinion/112067/california-v-greenwood/ — pinpoint: 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b794342502bd849d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "California v. Greenwood"}, "payload": {"all": [{"cite": "486 U.S. 35", "page": "35", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "486"}, {"cite": "108 S. Ct. 1625", "page": "1625", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "100 L. Ed. 2d 30", "page": "30", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "1988 U.S. LEXIS 2279", "page": "2279", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}, {"cite": "56 U.S.L.W. 4409", "page": "4409", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "56"}], "display": "486 U.S. 35", "official": {"cite": "486 U.S. 35", "page": "35", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "486"}, "official_selection_present": true, "record_id": "California v. Greenwood"}}
{"assertion_id": "5490edf947711f23", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-40b", "record_id": "California v. Greenwood"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-40b", "pinpoint_status": "slip-only", "quote": "It is common knowledge that plastic garbage bags left on or at the side of a public street are readily accessible to animals, children, scavengers, snoops, and other members of the public.", "quote_fidelity": "mismatch", "record_id": "California v. Greenwood", "star_marker": null}}
{"assertion_id": "b09bab66d8478845", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-40", "record_id": "California v. Greenwood"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-40", "pinpoint_status": "slip-only", "quote": "--- # California v. Greenwood *486 U.S. 35 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on information that Greenwood might be dealing drugs, police asked his regular trash collector to set aside the opaque garbage bags Greenwood left at the curb for pickup. Searching the bags, officers found evidence of narcotics use, which they used to obtain warrants to search the house. ## Issue Whether the warrantless search and seizure of garbage left for collection at the curb, outside the home's curtilage, violates the Fourth Amendment. ## Rule", "quote_fidelity": "mismatch", "record_id": "California v. Greenwood", "star_marker": null}}
{"assertion_id": "8fdf3ef77733e4c1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "California v. Greenwood"}, "payload": {"as_of_content": "1988-05-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "California v. Greenwood", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — California v. Greenwood

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Greenwood",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "California v. Greenwood",
    "case_name_short": "Greenwood",
    "case_name_full": "CALIFORNIA v. GREENWOOD Et Al.",
    "input_case_name": "California v. Greenwood",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-05-16",
    "year": 1988,
    "docket": "86-684",
    "cluster_id": 112067,
    "lead_opinion_id": 9431296,
    "sibling_ids": [
      112067,
      9431296,
      9431297
    ],
    "absolute_url": "/opinion/112067/california-v-greenwood/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9074833,
        "score": 10,
        "case_name": "California v. Greenwood"
      },
      {
        "cluster_id": 9074832,
        "score": 10,
        "case_name": "California v. Greenwood"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "486 U.S. 35",
      "volume": "486",
      "reporter": "U.S.",
      "page": "35",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 1625",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "1625",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 30",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4409",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4409",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2279",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2279",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "486 U.S. 35",
        "volume": "486",
        "reporter": "U.S.",
        "page": "35",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 1625",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "1625",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 30",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2279",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2279",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4409",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4409",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "486 U.S. 35",
    "official_selection": {
      "court_class": "scotus",
      "selected": "486 U.S. 35",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-40",
      "page": null,
      "quote": "--- # California v. Greenwood *486 U.S. 35 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on information that Greenwood might be dealing drugs, police asked his regular trash collector to set aside the opaque garbage bags Greenwood left at the curb for pickup. Searching the bags, officers found evidence of narcotics use, which they used to obtain warrants to search the house. ## Issue Whether the warrantless search and seizure of garbage left for collection at the curb, outside the home's curtilage, violates the Fourth Amendment. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-40b",
      "page": null,
      "quote": "It is common knowledge that plastic garbage bags left on or at the side of a public street are readily accessible to animals, children, scavengers, snoops, and other members of the public.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-05-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Greenwood",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rieves",
          "cluster_id": 4477518,
          "cite": [
            "2018 Ohio 955",
            "109 N.E.3d 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Knutson",
          "cluster_id": 2718239,
          "cite": [
            "288 Neb. 823"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pinon, Araceli Sanchez",
          "cluster_id": 3099362,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tony Lavan v. City of Los Angeles",
          "cluster_id": 807915,
          "cite": [
            "693 F.3d 1022",
            "2012 WL 3834659",
            "2012 U.S. App. LEXIS 18639"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Friedman v. Boucher",
          "cluster_id": 3064806,
          "cite": [
            "580 F.3d 847",
            "2009 WL 2857199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Friedman v. Boucher",
          "cluster_id": 1459727,
          "cite": [
            "568 F.3d 1119",
            "2009 U.S. App. LEXIS 13440",
            "2009 WL 1758366"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Funk",
          "cluster_id": 4002857,
          "cite": [
            "896 N.E.2d 203",
            "177 Ohio App. 3d 814",
            "2008 Ohio 4086"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane1_negative"
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
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
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
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 2411822,
          "cite": [
            "839 S.W.2d 54",
            "1992 Tenn. LEXIS 348"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
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
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 2629957,
          "cite": [
            "117 P.3d 476",
            "32 Cal. Rptr. 3d 759",
            "36 Cal. 4th 1114",
            "2005 Cal. Daily Op. Serv. 7196",
            "2005 Daily Journal DAR 9801",
            "2005 Cal. LEXIS 8908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Black",
          "cluster_id": 2461340,
          "cite": [
            "815 S.W.2d 166",
            "1991 Tenn. LEXIS 322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
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
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez-Portoreal",
          "cluster_id": 2033638,
          "cite": [
            "666 N.E.2d 207",
            "88 N.Y.2d 99",
            "643 N.Y.S.2d 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anita Christensen and Robert Alty v. County of Boone, Illinois, and Edward Krieger",
          "cluster_id": 797469,
          "cite": [
            "483 F.3d 454"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hardy",
          "cluster_id": 1494781,
          "cite": [
            "963 S.W.2d 516",
            "1997 WL 716775"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 2274111,
          "cite": [
            "319 S.W.3d 697",
            "2010 Tex. Crim. App. LEXIS 618",
            "2010 WL 1979437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Boland",
          "cluster_id": 2612515,
          "cite": [
            "800 P.2d 1112",
            "115 Wash. 2d 571",
            "1990 Wash. LEXIS 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Eugene Wright",
          "cluster_id": 663707,
          "cite": [
            "16 F.3d 1429",
            "1994 U.S. App. LEXIS 2361",
            "1994 WL 38983"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hempele",
          "cluster_id": 1435469,
          "cite": [
            "576 A.2d 793",
            "120 N.J. 182",
            "1990 N.J. LEXIS 92"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph N. Basinski",
          "cluster_id": 770429,
          "cite": [
            "226 F.3d 829",
            "2000 U.S. App. LEXIS 22481",
            "2000 WL 1246554"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Greenwood:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112067 OR 9431296 OR 9431297) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU2MjA0ODAwMDAwJnM9MjU5NDAyMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112067+OR+9431296+OR+9431297%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 60,
        "triage_read": 3,
        "triage_snippet_classified": 57
      },
      "lane2_top_cited": {
        "query": "cites:(112067 OR 9431296 OR 9431297)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTImcz0zMTUyNjk3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112067+OR+9431296+OR+9431297%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112067 OR 9431296 OR 9431297)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 0,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112067 OR 9431296 OR 9431297)",
    "indexed_citing_opinions": 637,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112067,
        "count": 541,
        "count_source": "search"
      },
      {
        "opinion_id": 9431296,
        "count": 113,
        "count_source": "search"
      },
      {
        "opinion_id": 9431297,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1059,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-greenwood.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NTU5MTUmcz05NDQ3NTgxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112067+OR+9431296+OR+9431297%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112067,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 108622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 110231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 110829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 111943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 296077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 306735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 335974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 360868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 370180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 389953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 415483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 421191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 430929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 442968,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 460221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 463553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1116935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1125153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1174400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1174758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1207494,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1210219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1216270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1383117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1421847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1463256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1641820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1664437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1709358,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1714935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 1893678,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 2038836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 2067887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 2109062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 2149977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112067,
        "cited_id": 3735259,
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
    "date_created": "2026-07-04T21:34:14Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:34:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:34:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:18:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:34:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Greenwood

```
<opinion type="majority">
<author id="b95-8"><page-number citation-index="1" label="37">*37</page-number>Justice White</author>
<p id="Adr">delivered the opinion of the Court.</p>
<p id="b95-9">The issue here is whether the Fourth Amendment prohibits the warrantless search and seizure of garbage left for collection outside the curtilage of a home. We conclude, in accordance with the vast majority of lower courts that have addressed the issue, that it does not.</p>
<p id="b95-10">h — 1</p>
<p id="b95-3">In early 1984, Investigator Jenny Stracner of the Laguna Beach Police Department received information indicating that respondent Greenwood might be engaged in narcotics trafficking. Stracner learned that a criminal suspect had informed a federal drug enforcement agent in February 1984 that a truck filled with illegal drugs was en route to the Laguna Beach address at which Greenwood resided. In addition, a neighbor complained of heavy vehicular traffic late at night in front of Greenwood’s single-family home. The neighbor reported that the vehicles remained at Greenwood’s house for only a few minutes.</p>
<p id="b95-4">Stracner sought to investigate this information by conducting a surveillance of Greenwood’s home. She observed several vehicles make brief stops at the house during the late-night and early morning hours, and she followed a truck from the house to a residence that had previously been under investigation as a narcotics-trafficking location.</p>
<p id="b95-5">On April 6, 1984, Stracner asked the neighborhood’s regular trash collector to pick up the plastic garbage bags that Greenwood had left on the curb in front of his house and to turn the bags over to her without mixing their contents with garbage from other houses. The trash collector cleaned his truck bin of other refuse, collected the garbage bags from the street in front of Greenwood’s house, and turned the bags over to Stracner. The officer searched through the rubbish <page-number citation-index="1" label="38">*38</page-number>and found items indicative of narcotics use. She recited the information that she had gleaned from the trash search in an affidavit in support of a warrant to search Greenwood’s home.</p>
<p id="b96-4">Police officers encountered both respondents at the house later that day when they arrived to execute the warrant. The police discovered quantities of cocaine and hashish during their search of the house. Respondents were arrested on felony narcotics charges. They subsequently posted bail.</p>
<p id="b96-5">The police continued to receive reports of many late-night visitors to the Greenwood house. On May 4, Investigator Robert Rahaeuser obtained Greenwood’s garbage from the regular trash collector in the same manner as had Stracner. The garbage again contained evidence of narcotics use.</p>
<p id="b96-6">Rahaeuser secured another search warrant for Greenwood’s home based on the information from the second trash search. The police found more narcotics and evidence of narcotics trafficking when they executed the warrant. Greenwood was again arrested.</p>
<p id="b96-7">The Superior Court dismissed the charges against respondents on the authority of <em>People </em>v. Krivda, <span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">5 Cal. 3d 357</a></span>, <span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">486 P. 2d 1262</a></span> (1971), which held that warrantless trash searches violate the Fourth Amendment and the California Constitution. The court found that the police would not have had probable cause to search the Greenwood home without the evidence obtained from the trash searches.</p>
<p id="b96-8">The Court of Appeal affirmed. <span class="citation" data-id="2149977"><a href="/opinion/2149977/people-v-greenwood/" aria-description="Citation for case: People v. Greenwood">182 Cal. App. 3d 729</a></span>, <span class="citation" data-id="2149977"><a href="/opinion/2149977/people-v-greenwood/" aria-description="Citation for case: People v. Greenwood">227 Cal. Rptr. 539</a></span> (1986). The court noted at the outset that the fruits of warrantless trash searches could no longer be suppressed if <em><span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">Krivda</a></span> </em>were based only on the California Constitution, because since 1982 the State has barred the suppression of evidence seized in violation of California law but not federal law. See Cal. Const., Art. I, § 28(d); <em>In re Lance W., </em><span class="citation" data-id="9626292"><a href="/opinion/1421847/people-v-lance-w/" aria-description="Citation for case: People v. Lance W.">37 Cal. 3d 873</a></span>, <span class="citation" data-id="9626292"><a href="/opinion/1421847/people-v-lance-w/" aria-description="Citation for case: People v. Lance W.">694 P. 2d 744</a></span> (1985). But <em><span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">Krivda</a></span>, </em>a decision binding on the Court of Appeal, also held that the fruits of warrantless trash searches were to be excluded under federal <page-number citation-index="1" label="39">*39</page-number>law. Hence, the Superior Court was correct in dismissing the charges against respondents. <span class="citation" data-id="2149977"><a href="/opinion/2149977/people-v-greenwood/#735" aria-description="Citation for case: People v. Greenwood">182 Cal. App. 3d, at 735</a></span>, 227 Cal. Rptr, at 542.<footnotemark>1</footnotemark></p>
<p id="b97-9">The California Supreme Court denied the State’s petition for review of the Court of Appeal’s decision. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./483/1019/">483 U. S. 1019</a></span>, and now reverse.</p>
<p id="b97-10">) — I I — C</p>
<p id="b97-3">The warrantless search and seizure of the garbage bags left at the curb outside the Greenwood house would violate the Fourth Amendment only if respondents manifested a subjective expectation of privacy in their garbage that society accepts as objectively reasonable. <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#715" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 715</a></span> (1987); <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 211</a></span> (1986); <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#177" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 177</a></span> (1984); <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). Respondents do not disagree with this standard.</p>
<p id="b97-4">They assert, however, that they had, and exhibited, an expectation of privacy with respect to the trash that was searched by the police: The trash, which was placed on the street for collection at a fixed time, was contained in opaque plastic bags, which the garbage collector was expected to pick up, mingle with the trash of others, and deposit at the garbage dump. The trash was only temporarily on the street, and there was little likelihood that it would be inspected by anyone.</p>
<p id="b97-5">It may well be that respondents did not expect that the contents of their garbage bags would become known to the police or other members of the public. An expectation of privacy does not give rise to Fourth Amendment protection, <page-number citation-index="1" label="40">*40</page-number>however, unless society is prepared to accept that expectation as objectively reasonable.</p>
<p id="b98-5">Here, we conclude that respondents exposed their garbage to the public sufficiently to defeat their claim to Fourth Amendment protection. It is common knowledge that plastic garbage bags left on or at the side of a public street are readily accessible to animals,<footnotemark>2</footnotemark> children, scavengers,<footnotemark>3</footnotemark> snoops,<footnotemark>4</footnotemark> and other members of the public. See <span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/#367" aria-description="Citation for case: People v. Krivda"><em>Krivda, supra, </em>at 367</a></span>, <span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/#1269" aria-description="Citation for case: People v. Krivda">486 P. 2d, at 1269</a></span>. Moreover, respondents placed their refuse at the curb for the express purpose of conveying it to a third party, the trash collector, who might himself have sorted through respondents’ trash or permitted others, such as the police, to do so. Accordingly, having deposited their garbage “in an area particularly suited for <page-number citation-index="1" label="41">*41</page-number>public inspection and, in a manner of speaking, public consumption, for the express purpose of having strangers take it,” <em>United States </em>v. <em>Reicherter, </em><span class="citation" data-id="389953"><a href="/opinion/389953/united-states-v-george-charles-reicherter-george-c-reicherter/#399" aria-description="Citation for case: United States v. George Charles Reicherter, George C....">647 F. 2d 397, 399</a></span> (CA3 1981), respondents could have had no reasonable expectation of privacy in the inculpatory items that they discarded.</p>
<p id="b99-5">Furthermore, as we have held, the police cannot reasonably be expected to avert their eyes from evidence of criminal activity that could have been observed by any member of the public. Hence, “[w]hat a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection.” <em>Katz </em>v. <em>United States, supra, </em>at 351. We held in <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979), for example, that the police did not violate the Fourth Amendment by causing a pen register to be installed at the telephone company’s offices to record the telephone numbers dialed by a criminal suspect. An individual has no legitimate expectation of privacy in the numbers dialed on his telephone, we reasoned, because he voluntarily conveys those numbers to the telephone company when he uses the telephone. Again, we observed that “a person has no legitimate expectation of privacy in information he voluntarily turns over to third parties.” <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#743" aria-description="Citation for case: Smith v. Maryland"><em>Id., </em>at 743-744</a></span>.</p>
<p id="b99-6">Similarly, we held in <em>California </em>v. <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo, supra,</a></span> </em>that the police were not required by the Fourth Amendment to obtain a warrant before conducting surveillance of the respondent’s fenced backyard from a private plane flying at an altitude of 1,000 feet. We concluded that the respondent’s expectation that his yard was protected from such surveillance was unreasonable because “[a]ny member of the public flying in this airspace who glanced down could have seen everything that these officers observed.” <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo"><em>Id., </em>at 213-214</a></span>.</p>
<p id="b99-7">Our conclusion that society would not accept as reasonable respondents’ claim to an expectation of privacy in trash left for collection in an area accessible to the public is reinforced by the unanimous rejection of similar claims by the Federal Courts of Appeals. See <em>United States </em>v. <em>Dela Espriella, </em><page-number citation-index="1" label="42">*42</page-number><span class="citation" data-id="8937749"><a href="/opinion/8947105/united-states-v-dela-espriella/#1437" aria-description="Citation for case: United States v. Dela Espriella">781 F. 2d 1432, 1437</a></span> (CA9 1986); <em>United States </em>v. <em>O’Bryant, </em><span class="citation" data-id="460221"><a href="/opinion/460221/united-states-v-john-dillard-obryant/#1533" aria-description="Citation for case: United States v. John Dillard O&#x27;Bryant">775 F. 2d 1528, 1533-1534</a></span> (CA11 1985); <em>United States </em>v. <em>Michaels, </em><span class="citation" data-id="430929"><a href="/opinion/430929/united-states-v-james-anthony-michaels-iii/#1312" aria-description="Citation for case: United States v. James Anthony Michaels, III">726 F. 2d 1307, 1312-1313</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./469/820/">469 U. S. 820</a></span> (1984); <em>United States </em>v. <em>Kramer, </em><span class="citation" data-id="421191"><a href="/opinion/421191/united-states-v-john-a-kramer/#791" aria-description="Citation for case: United States v. John A. Kramer">711 F. 2d 789, 791-794</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/962/">464 U. S. 962</a></span> (1983); <em>United States </em>v. <em>Terry, </em><span class="citation multiple-matches"><a href="/c/F.%202d/702/299/">702 F. 2d 299</a></span>, 308-309 (CA2), cert. denied <em>sub nom. Williams </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/U.%20S./461/931/">461 U. S. 931</a></span> (1983); <em>United States </em>v. <span class="citation" data-id="389953"><a href="/opinion/389953/united-states-v-george-charles-reicherter-george-c-reicherter/#399" aria-description="Citation for case: United States v. George Charles Reicherter, George C...."><em>Reicherter, supra, </em>at 399</a></span>; <em>United States </em>v. <em>Vahalik, </em><span class="citation" data-id="370180"><a href="/opinion/370180/united-states-v-floyd-a-vahalik/#100" aria-description="Citation for case: United States v. Floyd A. Vahalik">606 F. 2d 99, 100-101</a></span> (CA5 1979) <em>(per curiam), </em>cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/1081/">444 U. S. 1081</a></span> (1980); <em>United States </em>v. <em>Crowell, </em><span class="citation" data-id="8908006"><a href="/opinion/8919452/united-states-v-crowell/#1025" aria-description="Citation for case: United States v. Crowell">586 F. 2d 1020, 1025</a></span> (CA4 1978), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./440/959/">440 U. S. 959</a></span> (1979); <em>Magda </em>v. <em>Benson, </em><span class="citation" data-id="335974"><a href="/opinion/335974/john-george-magda-v-c-l-benson-warden/#112" aria-description="Citation for case: John George Magda v. C. L. Benson, Warden">536 F. 2d 111, 112-113</a></span> (CA6 1976) <em>(per curiam); United States </em>v. <em>Mustone, </em><span class="citation" data-id="306735"><a href="/opinion/306735/united-states-v-christopher-mustone-united-states-of-america-v-michael/#972" aria-description="Citation for case: United States v. Christopher Mustone, United States of...">469 F. 2d 970, 972-974</a></span> (CA1 1972). In <em>United States </em>v. <em>Thornton, </em>241 U. S. App. D. C. 46, 56, and n. 11, <span class="citation" data-id="442968"><a href="/opinion/442968/united-states-v-benjamin-t-thornton/#49" aria-description="Citation for case: United States v. Benjamin T. Thornton">746 F. 2d 39, 49</a></span>, and n. 11 (1984), the court observed that “the overwhelming weight of authority rejects the proposition that a reasonable expectation of privacy exists with respect to trash discarded outside the home and the curtilege <em>[sic] </em>thereof.” In addition, of those state appellate courts that have considered the issue, the vast majority have held that the police may conduct war-rantless searches and seizures of garbage discarded in public areas. See <em>Commonwealth </em>v. <em>Chappee, </em><span class="citation" data-id="2067887"><a href="/opinion/2067887/commonwealth-v-chappee/#512" aria-description="Citation for case: Commonwealth v. Chappee">397 Mass. 508, 512-513</a></span>, <span class="citation" data-id="2067887"><a href="/opinion/2067887/commonwealth-v-chappee/#721" aria-description="Citation for case: Commonwealth v. Chappee">492 N. E. 2d 719, 721-722</a></span> (1986); <em>Cooks </em>v. <em>State, </em><span class="citation" data-id="1174758"><a href="/opinion/1174758/cooks-v-state/#656" aria-description="Citation for case: Cooks v. State">699 P. 2d 653, 656</a></span> (Okla. Crim.), cert, denied, <span class="citation multiple-matches"><a href="/c/U.%20S./474/935/">474 U. S. 935</a></span> (1985); <em>State </em>v. <em>Stevens, </em><span class="citation" data-id="9666272"><a href="/opinion/1664437/state-v-stevens/#314" aria-description="Citation for case: State v. Stevens">123 Wis. 2d 303, 314-317</a></span>, <span class="citation" data-id="9666272"><a href="/opinion/1664437/state-v-stevens/#794" aria-description="Citation for case: State v. Stevens">367 N. W. 2d 788, 794-797</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./474/852/">474 U. S. 852</a></span> (1985); <em>State </em>v. <span class="citation" data-id="1893678"><a href="/opinion/1893678/state-v-ronngren/#228" aria-description="Citation for case: State v. Ronngren"><em>Ronngren, 361 </em>N. W. 2d 224, 228-230</a></span> (N. D. 1985); <em>State </em>v. <em>Brown, </em><span class="citation" data-id="3735259"><a href="/opinion/3983080/state-v-brown/#37" aria-description="Citation for case: State v. Brown">20 Ohio App. 3d 36, 37-38</a></span>, <span class="citation" data-id="3735259"><a href="/opinion/3983080/state-v-brown/#217" aria-description="Citation for case: State v. Brown">484 N. E. 2d 215, 217-218</a></span> (1984); <em>State </em>v. <em>Oquist, </em><span class="citation" data-id="1709358"><a href="/opinion/1709358/state-v-oquist/" aria-description="Citation for case: State v. Oquist">327 N. W. 2d 587</a></span> (Minn. 1982); <em>People </em>v. <em>Whotte, </em><span class="citation" data-id="9663228"><a href="/opinion/1641820/people-v-whotte/" aria-description="Citation for case: People v. Whotte">113 Mich. App. 12</a></span>, <span class="citation" data-id="9663228"><a href="/opinion/1641820/people-v-whotte/" aria-description="Citation for case: People v. Whotte">317 N. W. 2d 266</a></span> (1982); <em>Commonwealth </em>v. <em>Minton, </em><span class="citation" data-id="1463256"><a href="/opinion/1463256/commonwealth-v-minton/#391" aria-description="Citation for case: Commonwealth v. Minton">288 Pa. Super. 381, 391</a></span>, <span class="citation" data-id="1463256"><a href="/opinion/1463256/commonwealth-v-minton/#217" aria-description="Citation for case: Commonwealth v. Minton">432 A. 2d 212, 217</a></span> (1981); <em>State </em>v. <em>Schultz, </em><span class="citation" data-id="1125153"><a href="/opinion/1125153/state-v-schultz/" aria-description="Citation for case: State v. Schultz">388 So. 2d 1326</a></span> (Fla. App. 1980); <em>People </em>v. <em>Huddleston, </em><span class="citation" data-id="9526722"><a href="/opinion/2038836/people-v-huddleston/" aria-description="Citation for case: People v. Huddleston">38 Ill. App. 3d 277</a></span>, <span class="citation" data-id="9526722"><a href="/opinion/2038836/people-v-huddleston/" aria-description="Citation for case: People v. Huddleston">347 N. E. 2d 76</a></span> (1976); <em>Willis </em>v. <em>State, </em><span class="citation" data-id="1714935"><a href="/opinion/1714935/willis-v-state/#249" aria-description="Citation for case: Willis v. State">518 S. W. 2d 247, 249</a></span> (Tex. Crim. App. 1975); <em>Smith </em>v. <em>State, </em><span class="citation" data-id="9528966"><a href="/opinion/1116935/smith-v-state/" aria-description="Citation for case: Smith v. State">510 P. 2d 793</a></span> (Alaska), cert. denied, <page-number citation-index="1" label="43">*43</page-number><span class="citation multiple-matches"><a href="/c/U.%20S./414/1086/">414 U. S. 1086</a></span> (1973); <em>State </em>v. <em>Fassler, </em><span class="citation" data-id="9563410"><a href="/opinion/1210219/state-v-fassler/#592" aria-description="Citation for case: State v. Fassler">108 Ariz. 586, 592-593</a></span>, <span class="citation" data-id="9563410"><a href="/opinion/1210219/state-v-fassler/#813" aria-description="Citation for case: State v. Fassler">503 P. 2d 807, 813-814</a></span> (1972); <em>Croker </em>v. <em>State, </em><span class="citation" data-id="1174400"><a href="/opinion/1174400/croker-v-state/#125" aria-description="Citation for case: Croker v. State">477 P. 2d 122, 125-126</a></span> (Wyo. 1970); <em>State </em>v. <em>Purvis, </em><span class="citation" data-id="9562213"><a href="/opinion/1207494/state-v-purvis/#411" aria-description="Citation for case: State v. Purvis">249 Ore. 404, 411</a></span>, <span class="citation" data-id="9562213"><a href="/opinion/1207494/state-v-purvis/#1005" aria-description="Citation for case: State v. Purvis">438 P. 2d 1002, 1005</a></span> (1968). But see <em>State </em>v. <em>Tanaka, </em><span class="citation" data-id="1216270"><a href="/opinion/1216270/state-v-tanaka/" aria-description="Citation for case: State v. Tanaka">67 Haw. 658</a></span>, <span class="citation" data-id="1216270"><a href="/opinion/1216270/state-v-tanaka/" aria-description="Citation for case: State v. Tanaka">701 P. 2d 1274</a></span> (1985); <em>People </em>v. <em>Krivda, </em><span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">5 Cal. 3d 357</a></span>, <span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">486 P. 2d 1262</a></span> (1971).<footnotemark>5</footnotemark></p>
<p id="b101-5">Ill</p>
<p id="b101-6">We reject respondent Greenwood’s alternative argument for affirmance: that his expectation of privacy in his garbage should be deemed reasonable as a matter of federal constitutional law because the warrantless search and seizure of his garbage was impermissible as a matter of California law. He urges that the state-law right of Californians to privacy in their garbage, announced by the California Supreme Court in <em><span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">Krivda, supra,</a></span> </em>survived the subsequent state constitutional amendment eliminating the suppression remedy as a means of enforcing that right. See <em>In re Lance W., </em><span class="citation" data-id="9626292"><a href="/opinion/1421847/people-v-lance-w/#886" aria-description="Citation for case: People v. Lance W.">37 Cal. 3d, at 886-887</a></span>, <span class="citation" data-id="9626292"><a href="/opinion/1421847/people-v-lance-w/#752" aria-description="Citation for case: People v. Lance W.">694 P. 2d, at 752-753</a></span>. Hence, he argues that the Fourth Amendment should itself vindicate that right.</p>
<p id="b101-7">Individual States may surely construe their own constitutions as imposing more stringent constraints on police conduct than does the Federal Constitution. We have never intimated, however, that whether or not a search is reasonable within the meaning of the Fourth Amendment depends on the law of the particular State in which the search occurs. We have emphasized instead that the Fourth Amendment analysis must turn on such factors as “our <em>societal </em>understanding that certain areas deserve the most scrupulous protection from government invasion.” <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States">466 U. S., at 178</a></span> (emphasis added). See also <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143-144, n. 12</a></span> (1978). We have already concluded that society as a whole possesses no such under<page-number citation-index="1" label="44">*44</page-number>standing with regard to garbage left for collection at the side of a public street. Respondent’s argument is no less than a suggestion that concepts of privacy under the laws of each State are to determine the reach of the Fourth Amendment. We do not accept this submission.</p>
<p id="b102-8"><em>&gt; </em>h — I</p>
<p id="b102-3">Greenwood finally urges as an additional ground for affirmance that the California constitutional amendment eliminating the exclusionary rule for evidence seized in violation of state but not federal law violates the Due Process Clause of the Fourteenth Amendment. In his view, having recognized a state-law right to be free from warrantless searches of garbage, California may not under the Due Process Clause deprive its citizens of what he describes as “the only effective deterrent” to violations of this right. Greenwood concedes that no direct support for his position can be found in the decisions of this Court. He relies instead on cases holding that individuals are entitled to certain procedural protections before they can be deprived of a liberty or property interest created by state law. See <em>Hewitt </em>v. <em>Helms, </em><span class="citation" data-id="9429000"><a href="/opinion/110829/hewitt-v-helms/" aria-description="Citation for case: Hewitt v. Helms">459 U. S. 460</a></span> (1983); <em>Vitek </em>v. <em>Jones, </em><span class="citation" data-id="9427841"><a href="/opinion/110231/vitek-v-jones/" aria-description="Citation for case: Vitek v. Jones">445 U. S. 480</a></span> (1980).</p>
<p id="b102-4">We see no merit in Greenwood’s position. California could amend its Constitution to negate the holding in <em><span class="citation" data-id="9611834"><a href="/opinion/1383117/people-v-krivda/" aria-description="Citation for case: People v. Krivda">Krivda</a></span> </em>that state law forbids warrantless searches of trash. We are convinced that the State may likewise eliminate the exclusionary rule as a remedy for violations of that right. At the federal level, we have not required that evidence obtained in violation of the Fourth Amendment be suppressed in all circumstances. See, <em>e. g., United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984); <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). Rather, our decisions concerning the scope of the Fourth Amendment exclusionary rule have balanced the benefits of détérring police misconduct against the costs of excluding reliable evidence of criminal activity. See <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#908" aria-description="Citation for case: United States v. Leon">468 U. S., at 908-913</a></span>. We <page-number citation-index="1" label="45">*45</page-number>have declined to apply the exclusionary rule indiscriminately “when law enforcement officers have acted in objective good faith or their transgressions have been minor,” because “the magnitude of the benefit conferred on . . . guilty defendants [in such circumstances] offends basic concepts of the criminal justice system.” <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Id.,</a></span> </em>at 908 (citing <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 490</a></span> (1976)).</p>
<p id="b103-5">The States are not foreclosed by the Due Process Clause from using a similar balancing approach to delineate the scope of their own exclusionary rules. Hence, the people of California could permissibly conclude that the benefits of excluding relevant evidence of criminal activity do not outweigh the costs when the police conduct at issue does not violate federal law.</p>
<p id="b103-6">V</p>
<p id="b103-7">The judgment of the California Court of Appeal is therefore reversed, and this case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b103-8">
<em>It is so ordered.</em>
</p>
<p id="b103-9">Justice Kennedy took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b97-6"> The Court of Appeal also held that respondent Van Houten had standing to seek the suppression of evidence discovered during the April 4 search of Greenwood’s home. <span class="citation" data-id="2149977"><a href="/opinion/2149977/people-v-greenwood/#735" aria-description="Citation for case: People v. Greenwood">182 Cal. App. 3d, at 735</a></span>, <span class="citation" data-id="2149977"><a href="/opinion/2149977/people-v-greenwood/#542" aria-description="Citation for case: People v. Greenwood">227 Cal. Rptr., at 542-543</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b98-6"> For example, <em>State </em>v. <em>Ronngren, </em><span class="citation" data-id="1893678"><a href="/opinion/1893678/state-v-ronngren/" aria-description="Citation for case: State v. Ronngren">361 N. W. 2d 224</a></span> (N. D. 1985), involved the search of a garbage bag that a dog, acting “at the behest of no one,” <span class="citation" data-id="1893678"><a href="/opinion/1893678/state-v-ronngren/#228" aria-description="Citation for case: State v. Ronngren"><em>id., </em>at 228</a></span>, had dragged from the defendants’ yard into the yard of a neighbor. The neighbor deposited the bag in his own trash can, which he later permitted the police to search. The North Dakota Supreme Court held that the search of the garbage bag did not violate the defendants’ Fourth Amendment rights.</p>
</footnote>
<footnote label="3">
<p id="b98-7"> It is not only the homeless of the Nation’s cities^ who make use of others’ refuse. For example, a nationally syndicated consumer columnist has suggested that apartment dwellers obtain cents-off coupons by “mak[ing] friends with the fellow who handles the trash” in their buildings, and has recounted the tale of “the ‘Rich lady’ from Westmont who once a week puts on rubber gloves and hip boots and wades into the town garbage dump looking for labels and other proofs of purchase” needed to obtain manufacturers’ refunds. M. Sloane, “The Supermarket Shopper’s” 1980 Guide to Coupons and Refunds 74, 161 (1980).</p>
</footnote>
<footnote label="4">
<p id="b98-8"> Even the refuse of prominent Americans has not been invulnerable. In 1975, for example, a reporter for a weekly tabloid seized five bags of garbage from the sidewalk outside the home of Secretary of State Henry Kissinger. Washington Post, July 9, 1975, p. Al, col. 8. A newspaper editorial criticizing this journalistic “trash-picking” observed that “[e]vi-dently . . . ‘everybody does it.’” Washington Post, July 10, 1975, p. A18, col. 1. We of course do not, as the dissent implies, “bas[e] [our] conclusion” that individuals have no reasonable expectation of privacy in their garbage on this “sole incident.” <em>Post, </em>at 51.</p>
</footnote>
<footnote label="5">
<p id="b101-8"> Given that the dissenters are among the tiny minority of judges whose views are contrary to ours, we are distinctly unimpressed with the dissent’s prediction that “society will be shocked to learn” of today’s decision. <em>Post, </em>at 46.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/California v. Hodari D..json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "California v. Hodari D."
type: case
citation: "499 U.S. 621 (1991)"
parallel_cite: "111 S. Ct. 1547; 113 L. Ed. 2d 690; 59 U.S.L.W. 4335; 91 Daily Journal DAR 4665"
neutral_cite: "1991 U.S. LEXIS 2397; 91 Cal. Daily Op. Serv. 2893"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-04-23
docket: 89-1632
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Hodari D.
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112579/california-v-hodari-d/"
  cluster_id: 112579
  opinion_id: 112579
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[United States v. Mendenhall]]", "[[Brendlin v. California]]"]
aliases: ["California v. Hodari D", "Hodari D."]
tags: ["case", "fourth-amendment", "seizure", "show-of-authority", "flight"]
holding: "A show-of-authority seizure is not complete until the suspect submits; contraband discarded while still fleeing is not the fruit of a seizure."
lake:
  record_id: California v. Hodari D.
  status: verified
  projected_at: 2026-07-06
---

# California v. Hodari D.

*499 U.S. 621 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A group of youths fled at the approach of an unmarked police car. An officer chased Hodari on foot. Just before the officer caught and tackled him, Hodari tossed away a small rock of crack cocaine. Hodari argued he had been "seized" the moment he saw the officer giving chase, so the discarded cocaine was the fruit of an unlawful seizure.

## Issue
Whether a suspect who does not yield to a police show of authority is "seized" under the Fourth Amendment before any physical force is applied.

## Rule
"The narrow question before us is whether, with respect to a show of authority as with respect to application of physical force, a seizure occurs even though the subject does not yield. We hold that it does not." — 499 U.S. at 626. ^pin-626

"An arrest requires either physical force (as described above) or, where that is absent, submission to the assertion of authority." — *Id.* ^pin-626b

## Application
Hodari was not touched until after he had thrown away the cocaine, and he had not submitted to the chasing officer's show of authority before then. Because neither physical force nor submission had occurred at the moment he discarded the cocaine, he was not yet seized, and the cocaine was not the fruit of a seizure.

## Conclusion
No seizure had occurred when Hodari abandoned the cocaine; the judgment suppressing it was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hodari D.* refines the seizure framework of [[Terry v. Ohio]] and [[United States v. Mendenhall]] by adding the submission requirement for show-of-authority seizures.

## Appears on
- [[Seizure of the Person]] — *Key — Progeny / Refinement*

## Sources
- *California v. Hodari D.*, 499 U.S. 621 (1991) — https://www.courtlistener.com/opinion/112579/california-v-hodari-d/ — pinpoint: 626.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "612913d1698b7bc0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "California v. Hodari D."}, "payload": {"all": [{"cite": "499 U.S. 621", "page": "621", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "499"}, {"cite": "111 S. Ct. 1547", "page": "1547", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "111"}, {"cite": "113 L. Ed. 2d 690", "page": "690", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "113"}, {"cite": "1991 U.S. LEXIS 2397", "page": "2397", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1991"}, {"cite": "91 Cal. Daily Op. Serv. 2893", "page": "2893", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "91"}, {"cite": "59 U.S.L.W. 4335", "page": "4335", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "59"}, {"cite": "91 Daily Journal DAR 4665", "page": "4665", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "91"}], "display": "499 U.S. 621", "official": {"cite": "499 U.S. 621", "page": "621", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "499"}, "official_selection_present": true, "record_id": "California v. Hodari D."}}
{"assertion_id": "573ee065ee152818", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-626b", "record_id": "California v. Hodari D."}, "payload": {"fragment": null, "page": null, "pin_id": "pin-626b", "pinpoint_status": "slip-only", "quote": "An arrest requires either physical force (as described above) or, where that is absent, submission to the assertion of authority.", "quote_fidelity": "mismatch", "record_id": "California v. Hodari D.", "star_marker": null}}
{"assertion_id": "fe526808aa3bd8ba", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-626", "record_id": "California v. Hodari D."}, "payload": {"fragment": null, "page": null, "pin_id": "pin-626", "pinpoint_status": "slip-only", "quote": "under the Fourth Amendment before any physical force is applied. ## Rule", "quote_fidelity": "mismatch", "record_id": "California v. Hodari D.", "star_marker": null}}
{"assertion_id": "def6a35ce5300a59", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "California v. Hodari D."}, "payload": {"as_of_content": "1991-04-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "California v. Hodari D.", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — California v. Hodari D.

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Hodari D.",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "California v. Hodari D.",
    "case_name_short": "",
    "case_name_full": "California v. Hodari D.",
    "input_case_name": "California v. Hodari D.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-04-23",
    "year": 1991,
    "docket": "89-1632",
    "cluster_id": 112579,
    "lead_opinion_id": 112579,
    "sibling_ids": [
      112579,
      9432255,
      9432256
    ],
    "absolute_url": "/opinion/112579/california-v-hodari-d/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "499 U.S. 621",
      "volume": "499",
      "reporter": "U.S.",
      "page": "621",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 1547",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1547",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 690",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 U.S.L.W. 4335",
        "volume": "59",
        "reporter": "U.S.L.W.",
        "page": "4335",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Daily Journal DAR 4665",
        "volume": "91",
        "reporter": "Daily Journal DAR",
        "page": "4665",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 2397",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2397",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Cal. Daily Op. Serv. 2893",
        "volume": "91",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "2893",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "499 U.S. 621",
        "volume": "499",
        "reporter": "U.S.",
        "page": "621",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 1547",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1547",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 690",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 2397",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2397",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Cal. Daily Op. Serv. 2893",
        "volume": "91",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "2893",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 U.S.L.W. 4335",
        "volume": "59",
        "reporter": "U.S.L.W.",
        "page": "4335",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Daily Journal DAR 4665",
        "volume": "91",
        "reporter": "Daily Journal DAR",
        "page": "4665",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "499 U.S. 621",
    "official_selection": {
      "court_class": "scotus",
      "selected": "499 U.S. 621",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-626",
      "page": null,
      "quote": "under the Fourth Amendment before any physical force is applied. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-626b",
      "page": null,
      "quote": "An arrest requires either physical force (as described above) or, where that is absent, submission to the assertion of authority.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Hodari D.",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Dorado",
          "cluster_id": 10133856,
          "cite": [
            "307 Or. App. 641",
            "477 P.3d 1209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Matta",
          "cluster_id": 4671437,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane1_negative"
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
        "journal_ref": "California v. Hodari D.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Drayton",
          "cluster_id": 121153,
          "cite": [
            "153 L. Ed. 2d 242",
            "122 S. Ct. 2105",
            "536 U.S. 194",
            "2002 U.S. LEXIS 4420"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel v. City of Joliet",
          "cluster_id": 4376986,
          "cite": [
            "580 U.S. 357",
            "137 S. Ct. 911",
            "197 L. Ed. 2d 312",
            "2017 U.S. LEXIS 2021",
            "26 Fla. L. Weekly Fed. S 476",
            "85 U.S.L.W. 4130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Arkansas",
          "cluster_id": 117936,
          "cite": [
            "131 L. Ed. 2d 976",
            "115 S. Ct. 1914",
            "514 U.S. 927",
            "1995 U.S. LEXIS 3464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. Commonwealth",
          "cluster_id": 1067400,
          "cite": [
            "487 S.E.2d 259",
            "25 Va. App. 193",
            "1997 Va. App. LEXIS 444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Garcia-Cantu",
          "cluster_id": 1769810,
          "cite": [
            "253 S.W.3d 236",
            "2008 Tex. Crim. App. LEXIS 581",
            "2008 WL 1958956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hollman",
          "cluster_id": 5690698,
          "cite": [
            "79 N.Y.2d 181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crain v. State",
          "cluster_id": 2353970,
          "cite": [
            "315 S.W.3d 43",
            "2010 Tex. Crim. App. LEXIS 794",
            "2010 WL 2595077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ehly",
          "cluster_id": 1448102,
          "cite": [
            "854 P.2d 421",
            "317 Or. 66",
            "1993 Ore. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bora",
          "cluster_id": 2243377,
          "cite": [
            "634 N.E.2d 168",
            "83 N.Y.2d 531",
            "611 N.Y.S.2d 796",
            "1994 N.Y. LEXIS 703"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl James v. Wilkes Barre City",
          "cluster_id": 812864,
          "cite": [
            "700 F.3d 675",
            "2012 U.S. App. LEXIS 24592",
            "2012 WL 5954632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gene Autrey Adams v. Paul Metiva",
          "cluster_id": 675736,
          "cite": [
            "31 F.3d 375",
            "1994 U.S. App. LEXIS 19686",
            "1994 WL 394087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katherine Gardenhire and Walter Gardenhire v. Donald Schubert, in His Individual and Official Capacity as Chief of Police",
          "cluster_id": 767858,
          "cite": [
            "205 F.3d 303",
            "2000 U.S. App. LEXIS 3126",
            "2000 WL 232311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez-Llamas v. Oregon",
          "cluster_id": 145628,
          "cite": [
            "165 L. Ed. 2d 557",
            "126 S. Ct. 2669",
            "548 U.S. 331",
            "2006 U.S. LEXIS 5177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112579 OR 9432255 OR 9432256) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTA3MTYxNjAwMDAwJnM9NDQzMjY0MyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112579+OR+9432255+OR+9432256%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112579 OR 9432255 OR 9432256)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzAmcz0xMDU3MTU1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112579+OR+9432255+OR+9432256%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112579 OR 9432255 OR 9432256)",
        "reviewed": 82,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 82,
        "triage_read": 0,
        "triage_snippet_classified": 82
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112579 OR 9432255 OR 9432256)",
    "indexed_citing_opinions": 2003,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112579,
        "count": 1741,
        "count_source": "search"
      },
      {
        "opinion_id": 9432255,
        "count": 286,
        "count_source": "search"
      },
      {
        "opinion_id": 9432256,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3675,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-hodari-d.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzMzMDEmcz0xMDM2MjU3NiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112579+OR+9432255+OR+9432256%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112579,
        "cited_id": 85464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 88142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 88824,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 94447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 112218,
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
    "date_created": "2026-07-04T23:18:53Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:19:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:19:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:22:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:19:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Hodari D.

```
<div>
<center><b><span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">499 U.S. 621</a></span> (1991)</b></center>
<center><h1>CALIFORNIA<br>
v.<br>
HODARI D.</h1></center>
<center>No. 89-1632.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 14, 1991.</center>
<center>Decided April 23, 1991.</center>
CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA, FIRST APPELLATE DISTRICT
<p><span class="star-pagination">*622</span> <i>Ronald E. Niver,</i> Deputy Attorney General of California, argued the cause for petitioner. With him on the briefs were <i>John K. Van de Kamp,</i> Attorney General, <i>Richard B. Iglehart,</i> Chief Assistant Attorney General, <i>John H. Sugiyama,</i> Senior Assistant Attorney General, and <i>Clifford K. Thompson, Jr.,</i> and <i>Morris Beatus,</i> Deputy Attorneys General.</p>
<p><i>Clifford M. Sloan</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Solicitor General Starr, Assistant Attorney General Mueller, Deputy Solicitor General Bryson,</i> and <i>Paul J. Larkin, Jr.</i></p>
<p><i>James L. Lozenski,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./498/935/">498 U. S. 935</a></span>, argued the cause for respondent. With him on the brief was <i>J. Bradley O'Connell.</i><sup>[*]</sup></p>
<p>JUSTICE SCALIA delivered the opinion of the Court.</p>
<p>Late one evening in April 1988, Officers Brian McColgin and Jerry Pertoso were on patrol in a high-crime area of Oakland, California. They were dressed in street clothes but wearing jackets with "Police" embossed on both front and back. Their unmarked car proceeded west on Foothill Boulevard, and turned south onto 63rd Avenue. As they rounded the corner, they saw four or five youths huddled around a small red car parked at the curb. When the youths <span class="star-pagination">*623</span> saw the officers' car approaching they apparently panicked, and took flight. The respondent here, Hodari D., and one companion ran west through an alley; the others fled south. The red car also headed south, at a high rate of speed.</p>
<p>The officers were suspicious and gave chase. McColgin remained in the car and continued south on 63rd Avenue; Pertoso left the car, ran back north along 63rd, then west on Foothill Boulevard, and turned south on 62nd Avenue. Hodari, meanwhile, emerged from the alley onto 62nd and ran north. Looking behind as he ran, he did not turn and see Pertoso until the officer was almost upon him, whereupon he tossed away what appeared to be a small rock. A moment later, Pertoso tackled Hodari, handcuffed him, and radioed for assistance. Hodari was found to be carrying $130 in cash and a pager; and the rock he had discarded was found to be crack cocaine.</p>
<p>In the juvenile proceeding brought against him, Hodari moved to suppress the evidence relating to the cocaine. The court denied the motion without opinion. The California Court of Appeal reversed, holding that Hodari had been "seized" when he saw Officer Pertoso running towards him, that this seizure was unreasonable under the Fourth Amendment, and that the evidence of cocaine had to be suppressed as the fruit of that illegal seizure. The California Supreme Court denied the State's application for review. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./498/807/">498 U. S. 807</a></span> (1990).</p>
<p>As this case comes to us, the only issue presented is whether, at the time he dropped the drugs, Hodari had been "seized" within the meaning of the Fourth Amendment.<sup>[1]</sup> If <span class="star-pagination">*624</span> so, respondent argues, the drugs were the fruit of that seizure and the evidence concerning them was properly excluded. If not, the drugs were abandoned by Hodari and lawfully recovered by the police, and the evidence should have been admitted. (In addition, of course, Pertoso's seeing the rock of cocaine, at least if he recognized it as such, would provide reasonable suspicion for the unquestioned seizure that occurred when he tackled Hodari. Cf. <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960).)</p>
<p>We have long understood that the Fourth Amendment's protection against "unreasonable . . . seizures" includes seizure of the person, see <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span> (1959). From the time of the founding to the present, the word "seizure" has meant a "taking possession," 2 N. Webster, An American Dictionary of the English Language 67 (1828); 2 J. Bouvier, A Law Dictionary 510 (6th ed. 1856); Webster's Third New International Dictionary 2057 (1981). For most purposes at common law, the word connoted not merely grasping, or applying physical force to, the animate or inanimate object in question, but actually bringing it within physical control. A ship still fleeing, even though under attack, would not be considered to have been seized as a war prize. Cf. <i>The Josefa Segunda,</i> <span class="citation" data-id="85464"><a href="/opinion/85464/the-josefa-segunda/#325" aria-description="Citation for case: The Josefa Segunda">10 Wheat. 312, 325-326</a></span> (1825). A res capable of manual delivery was not seized until "tak[en] into custody." <i>Pelham</i> v. <i>Rose,</i> <span class="citation" data-id="88142"><a href="/opinion/88142/pelham-v-rose/#106" aria-description="Citation for case: Pelham v. Rose">9 Wall. 103, 106</a></span> (1870). To constitute an arrest, howeverthe quintessential "seizure of the person" under our Fourth Amendment jurisprudencethe mere grasping or application of physical force with lawful authority, whether or not it succeeded in subduing the arrestee, was sufficient. See, <i>e. g., </i><i>Whitehead</i> v. <i>Keyes,</i> <span class="citation" data-id="6413260"><a href="/opinion/6539539/whithead-v-keyes/#501" aria-description="Citation for case: Whithead v. Keyes">85 Mass. 495, 501</a></span> (1862) ("[A]n officer effects an arrest of a person whom he has authority to arrest, by laying his hand on him for the purpose of arresting him, though he may not succeed in stopping and holding him"); 1 <span class="star-pagination">*625</span> Restatement of Torts § 41, Comment <i>h</i> (1934). As one commentator has described it:</p>
<blockquote>"There can be constructive detention, which will constitute an arrest, although the party is never actually brought within the physical control of the party making an arrest. This is accomplished by merely touching, however slightly, the body of the accused, by the party making the arrest and for that purpose, although he does not succeed in stopping or holding him even for an instant; as where the bailiff had tried to arrest one who fought him off by a fork, the court said, `If the bailiff had touched him, that had been an arrest . . . .'" A. Cornelius, Search and Seizure 163-164 (2d ed. 1930) (footnote omitted).</blockquote>
<p>To say that an arrest is effected by the slightest application of physical force, despite the arrestee's escape, is not to say that for Fourth Amendment purposes there is a <i>continuing</i> arrest during the period of fugitivity. If, for example, Pertoso had laid his hands upon Hodari to arrest him, but Hodari had broken away and had <i>then</i> cast away the cocaine, it would hardly be realistic to say that that disclosure had been made during the course of an arrest. Cf. <i>Thompson</i> v. <i>Whitman,</i> <span class="citation" data-id="88824"><a href="/opinion/88824/thompson-v-whitman/#471" aria-description="Citation for case: Thompson v. Whitman">18 Wall. 457, 471</a></span> (1874) ("A seizure is a single act, and not a continuous fact"). The present case, however, is even one step further removed. It does not involve the application of any physical force; Hodari was untouched by Officer Pertoso at the time he discarded the cocaine. His defense relies instead upon the proposition that a seizure occurs "when the officer, by means of physical force <i>or show of authority,</i> has in some way restrained the liberty of a citizen." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19, n. 16</a></span> (1968) (emphasis added). Hodari contends (and we accept as true for purposes of this decision) that Pertoso's pursuit qualified as a "show of authority" <span class="star-pagination">*626</span> calling upon Hodari to halt. The narrow question before us is whether, with respect to a show of authority as with respect to application of physical force, a seizure occurs even though the subject does not yield. We hold that it does not.</p>
<p>The language of the Fourth Amendment, of course, cannot sustain respondent's contention. The word "seizure" readily bears the meaning of a laying on of hands or application of physical force to restrain movement, even when it is ultimately unsuccessful. ("She seized the purse-snatcher, but he broke out of her grasp.") It does not remotely apply, however, to the prospect of a policeman yelling "Stop, in the name of the law!" at a fleeing form that continues to flee. That is no seizure.<sup>[2]</sup> Nor can the result respondent wishes to achieve be producedindirectly, as it wereby suggesting that Pertoso's uncomplied-with show of authority was a common-law arrest, and then appealing to the principle that all common-law arrests are seizures. An arrest requires <i>either</i> physical force (as described above) <i>or,</i> where that is absent, <i>submission</i> to the assertion of authority.</p>
<blockquote>"Mere words will not constitute an arrest, while, on the other hand, no actual, physical touching is essential. The apparent inconsistency in the two parts of this statement is explained by the fact that an assertion of authority and purpose to arrest followed by submission of the arrestee constitutes an arrest. There can be no arrest <span class="star-pagination">*627</span> without either touching or submission." Perkins, The Law of Arrest, <span class="citation no-link">25 Iowa L. Rev. 201</span>, 206 (1940) (footnotes omitted).</blockquote>
<p>We do not think it desirable, even as a policy matter, to stretch the Fourth Amendment beyond its words and beyond the meaning of arrest, as respondent urges.<sup>[3]</sup> Street pursuits always place the public at some risk, and compliance with police orders to stop should therefore be encouraged. Only a few of those orders, we must presume, will be without adequate basis, and since the addressee has no ready means of identifying the deficient ones it almost invariably is the responsible course to comply. Unlawful orders will not be deterred, moreover, by sanctioning through the exclusionary rule those of them that are <i>not</i> obeyed. Since policemen do not command "Stop!" expecting to be ignored, or give chase hoping to be outrun, it fully suffices to apply the deterrent to their genuine, successful seizures.</p>
<p>Respondent contends that his position is sustained by the so-called <i>Mendenhall</i> test, formulated by Justice Stewart's opinion in <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span> (1980), and adopted by the Court in later cases, see <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 573</a></span> (1988); <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984): "[A] person has been `seized' within the <span class="star-pagination">*628</span> meaning of the Fourth Amendment only if, in view of all the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 554</a></span>. See also <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (opinion of WHITE, J.). In seeking to rely upon that test here, respondent fails to read it carefully. It says that a person has been seized "only if," not that he has been seized "whenever"; it states a <i>necessary,</i> but not a <i>sufficient,</i> condition for seizureor, more precisely, for seizure effected through a "show of authority." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> establishes that the test for existence of a "show of authority" is an objective one: not whether the citizen perceived that he was being ordered to restrict his movement, but whether the officer's words and actions would have conveyed that to a reasonable person. Application of this objective test was the basis for our decision in the other case principally relied upon by respondent, <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut, supra,</a></span></i> where we concluded that the police cruiser's slow following of the defendant did not convey the message that he was not free to disregard the police and go about his business. We did not address in <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut</a></span>,</i> however, the question whether, if the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> test was metif the message that the defendant was not free to leave <i>had</i> been conveyeda Fourth Amendment seizure would have occurred. See <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#577" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 577</a></span> (KENNEDY, J., concurring).</p>
<p>Quite relevant to the present case, however, was our decision in <i>Brower</i> v. <i>Inyo County,</i> <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596</a></span> (1989). In that case, police cars with flashing lights had chased the decedent for 20 milessurely an adequate "show of authority"but he did not stop until his fatal crash into a police-erected blockade. The issue was whether his death could be held to be the consequence of an unreasonable seizure in violation of the Fourth Amendment. We did not even consider the possibility that a seizure could have occurred during the course of the chase because, as we explained, that "show of authority" did not produce his stop. <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#597" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo"><i>Id.,</i> at 597</a></span>. And we discussed, <span class="star-pagination">*629</span> <i>ibid.,</i> an opinion of Justice Holmes, involving a situation not much different from the present case, where revenue agents had picked up containers dropped by moonshiners whom they were pursuing without adequate warrant. The containers were not excluded as the product of an unlawful seizure because "[t]he defendant's own acts, and those of his associates, disclosed the jug, the jar and the bottleand there was no seizure in the sense of the law when the officers examined the contents of each after they had been abandoned." <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#58" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 58</a></span> (1924). The same is true here.</p>
<p>In sum, assuming that Pertoso's pursuit in the present case constituted a "show of authority" enjoining Hodari to halt, since Hodari did not comply with that injunction he was not seized until he was tackled. The cocaine abandoned while he was running was in this case not the fruit of a seizure, and his motion to exclude evidence of it was properly denied. We reverse the decision of the California Court of Appeal, and remand for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE STEVENS, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>The Court's narrow construction of the word "seizure" represents a significant, and in my view, unfortunate, departure from prior case law construing the Fourth Amendment.<sup>[1]</sup> Almost a quarter of a century ago, in two landmark cases one broadening the protection of individual privacy,<sup>[2]</sup> and the other broadening the powers of law enforcement officers<sup>[3]</sup> we rejected the method of Fourth Amendment analysis that <span class="star-pagination">*630</span> today's majority endorses. In particular, the Court now adopts a definition of "seizure" that is unfaithful to a long line of Fourth Amendment cases. Even if the Court were defining seizure for the first time, which it is not, the definition that it chooses today is profoundly unwise. In its decision, the Court assumes, without acknowledging, that a police officer may now fire his weapon at an innocent citizen and not implicate the Fourth Amendmentas long as he misses his target.</p>
<p>For the purposes of decision, the following propositions are not in dispute. First, when Officer Pertoso began his pursuit of respondent,<sup>[4]</sup> the officer did not have a lawful basis for either stopping or arresting respondent. See App. 138-140; <i>ante,</i> at 623, n. 1. Second, the officer's chase amounted to a "show of authority" as soon as respondent saw the officer nearly upon him. See <i>ante,</i> at 625-626, 629. Third, the act of discarding the rock of cocaine was the direct consequence of the show of authority. See Pet. for Cert. 48-49, 52. Fourth, as the Court correctly demonstrates, no common-law arrest occurred until the officer tackled respondent. See <i>ante,</i> at 624-625. Thus, the Court is quite right in concluding that the abandonment of the rock was not the fruit of a common-law arrest.</p>
<p>It is equally clear, however, that if the officer had succeeded in touching respondent before he dropped the rock <span class="star-pagination">*631</span> even if he did not subdue himan arrest would have occurred.<sup>[5]</sup> See <i>ante,</i> at 624-625, 626. In that event (assuming the touching precipitated the abandonment), the evidence would have been the fruit of an unlawful common-law arrest. The distinction between the actual case and the hypothetical case is the same as the distinction between the common-law torts of assault and batterya touching converts the former into the latter.<sup>[6]</sup> Although the distinction between assault and battery was important for pleading purposes, see 2 J. Chitty, Pleading *372-*376, the distinction should not take on constitutional dimensions. The Court mistakenly allows this common-law distinction to define its interpretation of the Fourth Amendment.</p>
<p>At the same time, the Court fails to recognize the existence of another, more telling, common-law distinctionthe distinction between an arrest and an attempted arrest. As the Court teaches us, the distinction between battery and assault was critical to a correct understanding of the common law of arrest. See <i>ante,</i> at 626 ("An arrest requires <i>either</i> physical force . . . <i>or,</i> where that is absent, <i>submission</i> to the assertion of authority"). However, the facts of this case do not describe an actual arrest, but rather an unlawful <i>attempt</i> to take a presumptively innocent person into custody. Such an <span class="star-pagination">*632</span> attempt was unlawful at common law.<sup>[7]</sup> Thus, if the Court wants to define the scope of the Fourth Amendment based on the common law, it should look, not to the common law of arrest, but to the common law of attempted arrest, according to the facts of this case.</p>
<p>The first question, then, is whether the common law should define the scope of the outer boundaries of the constitutional protection against unreasonable seizures. Even if, contrary to settled precedent, traditional common-law analysis were controlling, it would still be necessary to decide whether the unlawful attempt to make an arrest should be considered a seizure within the meaning of the Fourth Amendment, and whether the exclusionary rule should apply to unlawful attempts.</p>
<p></p>
<h2>I</h2>
<p>The Court today takes a narrow view of "seizure," which is at odds with the broader view adopted by this Court almost 25 years ago. In <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the Court considered whether electronic surveillance conducted "without any trespass and without the seizure of any material object fell outside the ambit of the Constitution." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353</a></span>. Over Justice Black's powerful dissent, we rejected that "narrow view" of the Fourth Amendment and held that electronic eavesdropping is a "search and seizure" within the meaning of the Amendment. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353-354</a></span>. We thus endorsed the position expounded by two of the dissenting Justices in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928):</p>
<blockquote>
<span class="star-pagination">*633</span> "Time and again, this Court in giving effect to the principle underlying the Fourth Amendment, has refused to place an unduly literal construction upon it." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#476" aria-description="Citation for case: Olmstead v. United States"><i>Id.,</i> at 476</a></span> (Brandeis, J., dissenting).</blockquote>
<blockquote>"The direct operation or literal meaning of the words used do not measure the purpose or scope of its provisions. Under the principles established and applied by this Court, the Fourth Amendment safeguards against all evils that are like and equivalent to those embraced within the ordinary meaning of its words." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#488" aria-description="Citation for case: Olmstead v. United States"><i>Id.,</i> at 488</a></span> (Butler, J., dissenting).</blockquote>
<p>Writing for the Court in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> Justice Stewart explained:</p>
<blockquote>"Thus, although a closely divided Court supposed in <i><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span></i> that surveillance without any trespass and without the seizure of any material object fell outside the ambit of the Constitution, we have since departed from the narrow view on which that decision rested. Indeed, we have expressly held that the Fourth Amendment governs not only the seizure of tangible items, but extends as well to the recording of oral statements, overheard without any `technical trespass under . . . local property law.' <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span>. Once this much is acknowledged, and once it is recognized that the Fourth Amendment protects peopleand not simply `areas'against unreasonable searches and seizures, it becomes clear that the reach of that Amendment cannot turn upon the presence or absence of a physical intrusion into any given enclosure.</blockquote>
<blockquote>"We conclude that the underpinnings of <i><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span></i> and <i>Goldman</i> have been so eroded by our subsequent decisions that the `trespass' doctrine there enunciated can no longer be regarded as controlling. The Government's activities in electronically listening to and recording the petitioner's words violated the privacy upon which he justifiably relied while using the telephone <span class="star-pagination">*634</span> booth and thus constituted a `search and seizure' within the meaning of the Fourth Amendment. The fact that the electronic device employed to achieve that end did not happen to penetrate the wall of the booth can have no constitutional significance.</blockquote>
<blockquote>"The question remaining for decision, then, is whether the search and seizure conducted in this case complied with constitutional standards." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353-354</a></span>.</blockquote>
<p>Significantly, in the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> opinion, the Court repeatedly used the word "seizure" to describe the process of recording sounds that could not possibly have been the subject of a common-law seizure. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 356, 357</a></span>.</p>
<p>Justice Black's reasoning, which was rejected by the Court in 1967, is remarkably similar to the reasoning adopted by the Court today. After criticizing "language-stretching judges," <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#366" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 366</a></span>, Justice Black wrote:</p>
<blockquote>"I do not deny that common sense requires and that this Court often has said that the Bill of Rights' safeguards should be given a liberal construction. This principle, however, does not justify construing the search and seizure amendment as applying to eavesdropping or the `seizure' of conversations." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#366" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 366-367</a></span>.</blockquote>
<blockquote>"Since I see no way in which the words of the Fourth Amendment can be construed to apply to eavesdropping, that closes the matter for me. In interpreting the Bill of Rights, I willingly go as far as a liberal construction of the language takes me, but I simply cannot in good conscience give a meaning to words which they have never before been thought to have and which they certainly do not have in common ordinary usage. I will not distort the words of the Amendment in order to `keep the Constitution up to date' or `to bring it into harmony with the times.' It was never meant that this Court have such power, which in effect would make us a continuously functioning constitutional convention." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#373" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 373</a></span>.</blockquote>
<p><span class="star-pagination">*635</span> The expansive construction of the word "seizure" in the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> case provided an appropriate predicate for the Court's holding in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the following year.<sup>[8]</sup> Prior to <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the Fourth Amendment proscribed any seizure of the person that was not supported by the same probable-cause showing that would justify a custodial arrest.<sup>[9]</sup> See <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 207-209</a></span> (1979). Given the fact that street encounters between citizens and police officers "are incredibly rich in diversity," <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#13" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 13</a></span>, the Court recognized the need for flexibility and held that "reasonable" suspiciona quantum of proof less demanding than probable causewas adequate to justify a stop for investigatory purposes. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 21-22</a></span>. As a corollary to the lesser justification for the stop, the Court necessarily concluded that the word "seizure" in the Fourth Amendment encompasses official restraints on individual freedom that fall short of a common-law arrest. Thus, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> broadened the range of encounters between the police and the citizen encompassed within the term "seizure," while at the same time, lowering the standard of proof necessary to justify a "stop" in the newly expanded category of seizures <span class="star-pagination">*636</span> now covered by the Fourth Amendment.<sup>[10]</sup> The Court explained:</p>
<blockquote>"Our first task is to establish at what point in this encounter the Fourth Amendment becomes relevant. That is, we must decide whether and when Officer McFadden `seized' Terry and whether and when he conducted a `search.' There is some suggestion in the use of such terms as `stop' and `frisk' that such police conduct is outside the purview of the Fourth Amendment because neither action rises to the level of a `search' or `seizure' within the meaning of the Constitution. We emphatically reject this notion. It is quite plain that the Fourth Amendment governs `seizures' of the person which do not eventuate in a trip to the station house and prosecution for crime`arrests' in traditional terminology. It must be recognized that whenever a police officer accosts an individual and restrains his freedom to walk away, he has `seized' that person." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 16</a></span> (footnote omitted).</blockquote>
<blockquote>"The distinctions of classical `stop-and-frisk' theory thus serve to divert attention from the central inquiry under the Fourth Amendmentthe reasonableness in all the circumstances of the particular governmental invasion of a citizen's personal security. `Search' and `seizure' are not talismans. We therefore reject the notions that the Fourth Amendment does not come into play at all as a limitation upon police conduct if the officers stop short of something called a `technical arrest' or a `full-blown search.'" <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 19</a></span>.</blockquote>
<p><span class="star-pagination">*637</span> The decisions in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> unequivocally reject the notion that the common law of arrest defines the limits of the term "seizure" in the Fourth Amendment. In <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> the Court abandoned the narrow view that would have limited a seizure to a material object, and, instead, held that the Fourth Amendment extended to the recording of oral statements. And in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the Court abandoned its traditional view that a seizure under the Fourth Amendment required probable cause, and, instead, expanded the definition of a seizure to include an investigative stop made on less than probable cause. Thus, the major premise underpinning the majority's entire analysis todaythat the common law of arrest should define the term "seizure" for Fourth Amendment purposes, see <i>ante,</i> at 624-625is seriously flawed. The Court mistakenly hearkens back to common law, while ignoring the expansive approach that the Court has taken in Fourth Amendment analysis since <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i><sup>[11]</sup></p>
<p></p>
<h2>II</h2>
<p>The Court fares no better when it tries to explain why the proper definition of the term "seizure" has been an open question until today. In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> in addition to stating that a seizure occurs "whenever a police officer accosts an individual and restrains his freedom to walk away," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16</a></span>, the Court noted that a seizure occurs "when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen. . . ." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 19, n. 16</a></span>. The touchstone of a seizure is the restraint of an individual's personal liberty <i>"in some way." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></i> (emphasis added).<sup>[12]</sup> Today the Court's reaction to respondent's reliance on <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> <span class="star-pagination">*638</span> is to demonstrate that in "show of force" cases no common-law arrest occurs unless the arrestee <i>submits.</i> See <i>ante,</i> at 626-627. That answer, however, is plainly insufficient given the holding in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> that the Fourth Amendment applies to stops that need not be justified by probable cause in the absence of a full-blown arrest.</p>
<p>In <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980), the Court "adhere[d] to the view that a person is `seized' only when, by means of physical force or a show of authority, his freedom of movement is restrained." <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#553" aria-description="Citation for case: United States v. Mendenhall"><i>Id.,</i> at 553</a></span>. The Court looked to whether the citizen who is questioned "remains free to disregard the questions and walk away," and if he or she is able to do so, then "there has been no intrusion upon that person's liberty or privacy" that would require some "particularized and objective justification" under the Constitution. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Id.,</i> at 554</a></span>. The test for a "seizure," as formulated by the Court in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>,</i> was whether, "in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Ibid.</a></span></i> Examples of seizures include "the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer's request might be compelled." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Ibid.</a></span></i> The Court's unwillingness today to adhere to the "reasonable person" standard, as formulated by Justice Stewart in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>,</i> marks an unnecessary departure from Fourth Amendment case law.</p>
<p>The Court today draws the novel conclusion that even though no seizure can occur <i>unless</i> the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> reasonable person standard is met, see <i>ante,</i> at 628, the fact that the standard has been met does not necessarily mean that a seizure has occurred. See <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">ibid.</a></span> (Mendenhall</i> "states a <i>necessary,</i> but not a <i>sufficient</i> condition for seizure . . . effected <span class="star-pagination">*639</span> through a `show of authority'"). If it were true that a seizure requires more than whether a reasonable person felt free to leave, then the following passage from the Court's opinion in <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984), is at best, seriously misleading:</p>
<blockquote>"As we have noted elsewhere: `Obviously, not all personal intercourse between policemen and citizens involves "seizures" of persons. Only when the officer, by means of physical force or show of authority, has restrained the liberty of a citizen may we conclude that a "seizure" has occurred.' <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 19, n. 16</a></span>. While applying such a test is relatively straightforward in a situation resembling a traditional arrest, see <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 212-216</a></span> (1979), the protection against unreasonable seizures also extends to `seizures that involve only a brief detention short of traditional arrest.' <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975). What has evolved from our cases is a determination that an initially consensual encounter between a police officer and a citizen can be transformed into a seizure or detention within the meaning of the Fourth Amendment, `if, in view of all the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.' <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Mendenhall, supra,</i> at 554</a></span> (footnote omitted); see <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (plurality opinion)." <i>Id.,</i> at 215.</blockquote>
<p>More importantly, in <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), a plurality of the Court adopted Justice Stewart's formulation in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> as the appropriate standard for determining when police questioning crosses the threshold from a consensual encounter to a forcible stop. In <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>,</i> the Court held that an illegal seizure had occurred. As a <span class="star-pagination">*640</span> predicate for that holding, JUSTICE WHITE, in his opinion for the plurality, explained that the citizen "may not be detained <i>even momentarily</i> without reasonable, objective grounds for doing so; and his refusal to listen or answer does not, without more, furnish those grounds. <i>United States</i> v. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#556" aria-description="Citation for case: United States v. Mendenhall"><i>Mendenhall, supra,</i> at 556</a></span> (opinion of Stewart, J.)." <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer">460 U. S., at 498</a></span> (emphasis added). The rule looks, not to the subjective perceptions of the person questioned, but rather, to the objective characteristics of the encounter that may suggest whether a reasonable person would have felt free to leave.</p>
<p>Even though momentary, a seizure occurs whenever an objective evaluation of a police officer's show of force conveys the message that the citizen is not entirely free to leavein other words, that his or her liberty is being restrained in a significant way. That the Court understood the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> definition as both necessary and sufficient to describe a Fourth Amendment seizure is evident from this passage in our opinion in <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109</a></span> (1984):</p>
<blockquote>"A `seizure' of property occurs when there is some meaningful interference with an individual's possessory interests in that property.5</blockquote>
<p>5 "See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983); <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#716" aria-description="Citation for case: United States v. Place"><i>id.,</i> at 716</a></span> (BRENNAN, J., concurring in result); <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 747-748</a></span> (1983) (STEVENS, J., concurring in judgment); see also <i>United States v. Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 13-14, n. 8</a></span> (1977); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906). While the concept of a `seizure' of property is not much discussed in our cases, this definition follows from our oftrepeated definition of the `seizure' of a person within the meaning of the Fourth Amendmentmeaningful interference, however brief, with an individual's freedom of movement. See <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#696" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 696</a></span> (1981); <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438, 440</a></span>, n. (1980) <i>(per curiam); </i><i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#551" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 551-554</a></span> (1980) (opinion of Stewart, J.); <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 50</a></span> (1979); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <i>Davis</i> v. <i>Mississippi,</i> <span class="star-pagination">*641</span> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16, 19, n. 16</a></span>." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#113" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 113</a></span>, and n. 5.</p>
<p>Finally, it is noteworthy that in <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567</a></span> (1988), the State asked us to repudiate the reasonable person standard developed in <i>Terry, Mendenhall, Delgado,</i> and <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>.</i><sup>[13]</sup> We decided, however, to "adhere to our traditional contextual approach," <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 573</a></span>. In our opinion, we described Justice Stewart's analysis in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> as "a test to be applied in determining whether `a person has been "seized" within the meaning of the Fourth Amendment'" and noted that "[t]he Court has since embraced this test." <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 573</a></span>. Moreover, in commenting on the virtues of the test, we explained that it focused on the police officer's conduct:</p>
<blockquote>"The test's objective standardlooking to the reasonable man's interpretation of the conduct in questionallows the police to determine in advance whether the conduct contemplated will implicate the Fourth Amendment." <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#574" aria-description="Citation for case: Michigan v. Chesternut"><i>Id.,</i> at 574</a></span>.</blockquote>
<p>Expressing his approval of the Court's rejection of Michigan's argument in <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut</a></span>,</i> Professor LaFave observed:</p>
<blockquote>"The `free to leave' concept, in other words, has nothing to do with a particular suspect's choice to flee rather than submit or with his assessment of the probability of successful flight. Were it otherwise, police would be encouraged to utilize a very threatening but sufficiently slow chase as an evidence-gathering technique whenever they lack even the reasonable suspicion needed for a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop." 3 W. LaFave, Search and Seizure § 9.2, p. 61 (2d ed. 1987, Supp. 1991).</blockquote>
<p><span class="star-pagination">*642</span> Whatever else one may think of today's decision, it unquestionably represents a departure from earlier Fourth Amendment case law. The notion that our prior cases contemplated a distinction between seizures effected by a touching on the one hand, and those effected by a show of force on the other hand, and that all of our repeated descriptions of the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> test stated only a necessary, but not a sufficient, condition for finding seizures in the latter category, is nothing if not creative lawmaking. Moreover, by narrowing the definition of the term seizure, instead of enlarging the scope of reasonable justifications for seizures, the Court has significantly limited the protection provided to the ordinary citizen by the Fourth Amendment. As we explained in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>:</i></p>
<blockquote>"The danger in the logic which proceeds upon distinctions between a `stop' and an `arrest,' or `seizure' of the person, and between a `frisk' and a `search' is twofold. It seeks to isolate from constitutional scrutiny the initial stages of the contact between the policeman and the citizen. And by suggesting a rigid all-or-nothing model of justification and regulation under the Amendment, it obscures the utility of limitations upon the scope, as well as the initiation, of police action as a means of constitutional regulation." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#17" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 17</a></span>.</blockquote>
<p></p>
<h2>III</h2>
<p>In this case the officer's show of forcetaking the form of a head-on chaseadequately conveyed the message that respondent was not free to leave.<sup>[14]</sup> Whereas in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>,</i> there was "nothing in the record [to] sugges[t] that the respondent <span class="star-pagination">*643</span> had any objective reason to believe that she was not free to end the conversation in the concourse and proceed on her way," <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#555" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 555</a></span>, here, respondent attempted to end "the conversation" before it began and soon found himself literally "not free to leave" when confronted by an officer running toward him head-on who eventually tackled him to the ground. There was an interval of time between the moment that respondent saw the officer fast approaching and the moment when he was tackled, and thus brought under the control of the officer. The question is whether the Fourth Amendment was implicated at the earlier or the later moment.</p>
<p>Because the facts of this case are somewhat unusual, it is appropriate to note that the same issue would arise if the show of force took the form of a command to "freeze," a warning shot, or the sound of sirens accompanied by a patrol car's flashing lights. In any of these situations, there may be a significant time interval between the initiation of the officer's show of force and the complete submission by the citizen. At least on the facts of this case, the Court concludes that the timing of the seizure is governed by the citizen's reaction, rather than by the officer's conduct. See <i>ante,</i> at 626-627. One consequence of this conclusion is that the point at which the interaction between citizen and police officer becomes a seizure occurs, not when a reasonable citizen believes he or she is no longer free to go, but, rather, only after the officer exercises control over the citizen.</p>
<p>In my view, our interests in effective law enforcement and in personal liberty<sup>[15]</sup> would be better served by adhering to a standard that "allows the police to determine in advance whether the conduct contemplated will implicate the Fourth <span class="star-pagination">*644</span> Amendment." <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#574" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 574</a></span>. The range of possible responses to a police show of force, and the multitude of problems that may arise in determining whether, and at which moment, there has been "submission," can only create uncertainty and generate litigation.</p>
<p>In some cases, of course, it is immediately apparent at which moment the suspect submitted to an officer's show of force. For example, if the victim is killed by an officer's gunshot,<sup>[16]</sup> as in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 11</a></span> (1985) ("A police officer may not seize an unarmed, nondangerous suspect by shooting him dead"),<sup>[17]</sup> or by a hidden roadblock, as in <i>Brower</i> v. <i>Inyo County,</i> <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593</a></span> (1989), the submission is unquestionably complete. But what if, for example, William James Caldwell (Brower) had just been wounded before being apprehended? Would it be correct to say that no seizure had occurred and therefore the Fourth Amendment was not implicated even if the pursuing officer had no justification whatsoever for initiating the chase? The Court's opinion in <i><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">Brower</a></span></i> suggests that the officer's responsibility should not depend on the character of the victim's evasive action. The Court wrote:</p>
<blockquote>"Brower's independent decision to continue the chase can no more eliminate respondents' responsibility for the termination of his movement effected by the roadblock than Garner's independent decision to flee eliminated the Memphis police officer's responsibility for the termination of his movement effected by the bullet." <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#595" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo"><i>Id.,</i> at 595</a></span>.</blockquote>
<p><span class="star-pagination">*645</span> It seems equally clear to me that the constitutionality of a police officer's show of force should be measured by the conditions that exist at the time of the officer's action. A search must be justified on the basis of the facts available at the time it is initiated; the subsequent discovery of evidence does not retroactively validate an unconstitutional search. The same approach should apply to seizures; the character of the citizen's response should not govern the constitutionality of the officer's conduct.</p>
<p>If an officer effects an arrest by touching a citizen, apparently the Court would accept the fact that a seizure occurred, even if the arrestee should thereafter break loose and flee. In such a case, the constitutionality of the seizure would be evaluated as of the time the officer acted. That category of seizures would then be analyzed in the same way as searches, namely, was the police action justified when it took place? It is anomalous, at best, to fashion a different rule for the subcategory of "show of force" arrests.</p>
<p>In cases within this new subcategory, there will be a period of time during which the citizen's liberty has been restrained, but he or she has not yet completely submitted to the show of force. A motorist pulled over by a highway patrol car cannot come to an immediate stop, even if the motorist intends to obey the patrol car's signal. If an officer decides to make the kind of random stop forbidden by <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979), and, after flashing his lights, but before the vehicle comes to a complete stop, sees that the license plate has expired, can he justify his action on the ground that the seizure became lawful after it was initiated but before it was completed? In an airport setting, may a drug enforcement agent now approach a group of passengers with his gun drawn, announce a "baggage search," and rely on the passengers' reactions to justify his investigative stops? The holding of today's majority fails to recognize the coercive and intimidating nature of such behavior and creates a rule that may allow such behavior to go unchecked.</p>
<p><span class="star-pagination">*646</span> The deterrent purposes of the exclusionary rule focus on the conduct of law enforcement officers and on discouraging improper behavior on their part,<sup>[18]</sup> and not on the reaction of the citizen to the show of force. In the present case, if Officer Pertoso had succeeded in tackling respondent before he dropped the rock of cocaine, the rock unquestionably would have been excluded as the fruit of the officer's unlawful seizure. Instead, under the Court's logic-chopping analysis, the exclusionary rule has no application because an attempt to make an unconstitutional seizure is beyond the coverage of the Fourth Amendment, no matter how outrageous or unreasonable the officer's conduct may be.</p>
<p>It is too early to know the consequences of the Court's holding. If carried to its logical conclusion, it will encourage unlawful displays of force that will frighten countless innocent citizens into surrendering whatever privacy rights they <span class="star-pagination">*647</span> may still have. It is not too soon, however, to note the irony in the fact that the Court's own justification for its result is its analysis of the rules of the common law of arrest that antedated our decisions in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i> Yet, even in those days the common law provided the citizen with protection against an attempt to make an unlawful arrest. See nn. 5 and 7, <i>supra.</i> The central message of <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> was that the protection the Fourth Amendment provides to the average citizen is not rigidly confined by ancient common-law precept. The message that today's literal-minded majority conveys is that the common law, rather than our understanding of the Fourth Amendment as it has developed over the last quarter of a century, defines, and limits, the scope of a seizure. The Court today defines a seizure as commencing, not with egregious police conduct, but rather with submission by the citizen. Thus, it both delays the point at which "the Fourth Amendment becomes relevant"<sup>[19]</sup> to an encounter and limits the range of encounters that will come under the heading of "seizure." Today's qualification of the Fourth Amendment means that innocent citizens may remain "secure in their persons . . . against unreasonable searches and seizures" only at the discretion of the police.<sup>[20]</sup></p>
<p>Some sacrifice of freedom always accompanies an expansion in the Executive's unreviewable<sup>[21]</sup> law enforcement powers. <span class="star-pagination">*648</span> A court more sensitive to the purposes of the Fourth Amendment would insist on greater rewards to society before decreeing the sacrifice it makes today. Alexander Bickel presciently wrote that "many actions of government have two aspects: their immediate, necessarily intended, practical effects, and their perhaps unintended or unappreciated bearing on values we hold to have more general and permanent interest."<sup>[22]</sup> The Court's immediate concern with containing criminal activity poses a substantial, though unintended, threat to values that are fundamental and enduring.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the Wayne County Prosecuting Attorney by <i>John D. O'Hair, pro se,</i> and <i>Timothy A. Baughman.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the California Attorneys for Criminal Justice by <i>Paul L. Gabbert;</i> and for the National Association of Criminal Defense Lawyers by <i>Paul Morris.</i></p>
<p>Briefs of <i>amici curiae</i> were filed for the Appellate Committee of the California District Attorneys Association by <i>Ira Reiner</i> and <i>Harry B. Sondheim;</i> and for <i>Marvin Cahn, pro se.</i></p>
<p>[1]  California conceded below that Officer Pertoso did not have the "reasonable suspicion" required to justify stopping Hodari, see <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). That it would be unreasonable to stop, for brief inquiry, young men who scatter in panic upon the mere sighting of the police is not self-evident, and arguably contradicts proverbial common sense. See Proverbs 28:1 ("The wicked flee when no man pursueth"). We do not decide that point here, but rely entirely upon the State's concession.</p>
<p>[2]  For this simple reasonwhich involves neither "logic-chopping," <i>post,</i> at 646, nor any arcane knowledge of legal historyit is irrelevant that English law proscribed "an unlawful <i>attempt</i> to take a presumptively innocent person into custody." <i>Post,</i> at 631. We have consulted the common law to explain the meaning of seizureand, contrary to the dissent's portrayal, to expand rather than contract that meaning (since one would not normally think that the mere touching of a person would suffice). But neither usage nor common-law tradition makes an <i>attempted</i> seizure a seizure. The common law may have made an attempted seizure unlawful in certain circumstances; but it made many things unlawful, very few of which were elevated to constitutional proscriptions.</p>
<p>[3]  Nor have we ever done so. The dissent is wrong in saying that <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), "broadened the range of encounters . . . encompassed within the term `seizure,'" <i>post,</i> at 635. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> unquestionably involved conduct that would constitute a common-law seizure; its novelty (if any) was in expanding the acceptable <i>justification</i> for such a seizure, beyond probable cause. The dissent is correct that <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), "unequivocally reject[s] the notion that the common law of arrest defines the limits of the term `seizure' in the Fourth Amendment," <i>post,</i> at 637. But we do not assert that it defines the limits of the term "seizure"; only that it defines the limits of a <i>seizure of the person.</i> What <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> stands for is the proposition that items which could not be subject to seizure at common law (<i>e. g.,</i> telephone conversations) can be seized under the Fourth Amendment. That is quite different from saying that what constitutes an arrest (a seizure of the person) has changed.</p>
<p>[1]  The Fourth Amendment to the Constitution protects "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . ."</p>
<p>[2]  <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967).</p>
<p>[3]  <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968).</p>
<p>[4]  The Court's gratuitous quotation from Proverbs 28:1, see <i>ante,</i> at 623, n. 1, mistakenly assumes that innocent residents have no reason to fear the sudden approach of strangers. We have previously considered, and rejected, this ivory-towered analysis of the real world for it fails to describe the experience of many residents, particularly if they are members of a minority. See generally Johnson, Race and the Decision To Detain a Suspect, 93 Yale L. J. 214 (1983). It has long been "a matter of common knowledge that men who are entirely innocent do sometimes fly from the scene of a crime through fear of being apprehended as the guilty parties, or from an unwillingness to appear as witnesses. Nor is it true as an accepted axiom of criminal law that `the wicked flee when no man pursueth, but the righteous are as bold as a lion.'" <i>Alberty</i> v. <i>United States,</i> <span class="citation" data-id="94447"><a href="/opinion/94447/alberty-v-united-states/#511" aria-description="Citation for case: Alberty v. United States">162 U. S. 499, 511</a></span> (1896).</p>
<p>[5]  "[I]f the officer pronounces words of arrest without an actual touching and the other immediately runs away, there is no escape (in the technical sense) because there was no arrest. It would be otherwise had the officer touched the arrestee for the purpose of apprehending him, because touching for the manifested purpose of arrest by one having lawful authority completes the apprehension, `although he does not succeed in stopping or holding him even for an instant.'" Perkins, The Law of Arrest, <span class="citation no-link">25 Iowa L. Rev. 201</span>, 206 (1940) (footnotes omitted).</p>
<p>[6]  "One who undertakes to make an arrest without lawful authority, or who attempts to do so in an unlawful manner, is guilty of an assault if the other is ordered to submit to the asserted authority, is guilty of battery if he lays hands on the other for this unlawful purpose . . . ." <span class="citation no-link"><i>Id.,</i> at 263</span> (footnotes omitted).</p>
<p>[7]  "[E]ven without touching the other, the officer may subject himself to liability if he undertakes to make an arrest without being privileged by law to do so.3
</p>
<p>"3 For example, an officer might be guilty of an assault because of an attempted arrest, without privilege, even if he did not succeed in touching the other. Furthermore, if the other submitted to such an arrest without physical contact, the officer is liable for false imprisonment. Gold v. Bissell, <span class="citation" data-id="5512913"><a href="/opinion/5665934/gold-v-bissell/" aria-description="Citation for case: Gold v. Bissell">1 Wend. 210</a></span> (N. Y. Sup. Ct. 1828)." <i>Id.,</i> at 201.</p>
<p>[8]  "We have recently held that `the Fourth Amendment protects people, not places,' <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), and wherever an individual may harbor a reasonable `expectation of privacy,' <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 361</a></span> (MR. JUSTICE HARLAN, concurring), he is entitled to be free from unreasonable governmental intrusion. Of course, the specific content and incidents of this right must be shaped by the context in which it is asserted. For `what the Constitution forbids is not all searches and seizures, but unreasonable searches and seizures.' <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960)." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 9</a></span>.</p>
<p>[9]  <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), the case on which the majority largely relies, was decided over 40 years before <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i> In that case, the defendant did not even argue that there was a seizure of his person. The Court's holding in <i><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span></i> that the abandoned moonshine whiskey had not been seized simply did not address the question whether it would have been the fruit of a constitutional violation if there had been a seizure of the person before the whiskey was abandoned.</p>
<p>[10]  The Court applied this principle in <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979):
</p>
<p>"We have recognized that in some circumstances an officer may detain a suspect briefly for questioning, although he does not have `probable cause' to believe that the suspect is involved in criminal activity, as is required for a traditional arrest. However, we have required the officers to have a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity." <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 51</a></span> (citations omitted).</p>
<p>[11]  It is noteworthy that the Court has relied so heavily on cases and commentary that antedated <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i></p>
<p>[12]  "The essential teaching of the Court's decision in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>that an individual's right to personal security and freedom must be respected even in encounters with the police that fall short of full arresthas been consistently reaffirmed." <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#227" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 227</a></span> (1984) (Brennan, J., concurring in part and dissenting in part).</p>
<p>[13]  "Petitioner argues that the Fourth Amendment is never implicated until an individual stops in response to the police's show of authority. Thus, petitioner would have us rule that a lack of objective and particularized suspicion would not poison police conduct, no matter how coercive, as long as the police did not succeed in actually apprehending the individual." <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#572" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 572</a></span>.</p>
<p>[14]  The California Court of Appeal noted:
</p>
<p>"This case involves more than a pursuit, as Officer Pertoso did not pursue [respondent], but ran in such a fashion as to cut him off and confront him head on. Under the rationale of <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut</a></span>,</i> this action is reasonably perceived as an intrusion upon one's freedom of movement and as a maneuver intended to block or `otherwise control the direction or speed' of one's movement." App. A to Pet. for Cert. 9.</p>
<p>[15]  "To determine the constitutionality of a seizure `[w]e must balance the nature and quality of the intrusion on the individual's Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion.'" <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 8</a></span> (1985) (citation omitted).</p>
<p>[16]  Even under the common law, "If an officer shoots at an arrestee when he is not privileged to do so, he is guilty of an aggravated assault. And if death results from an arrest, or attempted arrest, which was not authorized at all, . . . the arrester is guilty of manslaughter or, in extreme cases, of murder." Perkins, 25 Iowa L. Rev., at 263-264.</p>
<p>[17]  In <i>Tennessee</i> v. <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i><i>,</i> even the dissent agreed with the majority that the police officer who shot at a fleeing suspect had "`seized' [the suspect] by shooting him." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#25" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 25</a></span> (O'CONNOR, J., dissenting).</p>
<p>[18]  The purpose of the Fourth Amendment is "`to prevent arbitrary and oppressive interference by enforcement officials with the privacy and personal security of individuals.'" <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 215</a></span> (quoting <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span> (1976)); see <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#553" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 553-554</a></span> (same); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 12</a></span> ("Ever since its inception, the rule excluding evidence seized in violation of the Fourth Amendment has been recognized as a principal mode of discouraging lawless police conduct"); 4 W. LaFave, Search and Seizure § 11.4(j), pp. 459-460 (2d ed. 1987) ("Incriminating admissions and attempts to dispose of incriminating evidence are common and predictable consequences of illegal arrests and searches, and thus to admit such evidence would encourage such Fourth Amendment violations in future cases").
</p>
<p>Justice Brandeis wrote eloquently about the overarching purpose of the Fourth Amendment:</p>
<p>"The makers of our Constitution . . . sought to protect Americans in their beliefs, their thoughts, their emotions and their sensations. They conferred, as against the Government, the right to be let alonethe most comprehensive of rights and the right most valued by civilized men. To protect that right, every unjustifiable intrusion by the Government upon the privacy of the individual, whatever the means employed, must be deemed a violation of the Fourth Amendment." <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 478</a></span> (1928) (dissenting opinion).</p>
<p>Today's opinion has lost sight of these purposes.</p>
<p>[19]  <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16</a></span>.</p>
<p>[20]  Justice Jackson presaged this development when he wrote:
</p>
<p>"[A]n illegal search and seizure usually is a single incident, perpetrated by surprise, conducted in haste, kept purposely beyond the court's supervision and limited only by the judgment and moderation of officers whose own interests and records are often at stake in the search . . . . The citizen's choice is quietly to submit to whatever the officers undertake or to resist at risk of arrest or immediate violence." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#182" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 182</a></span> (1949) (dissenting opinion).</p>
<p>[21]  "[T]he right to be secure against searches and seizures is one of the most difficult to protect. Since the officers are themselves the chief invaders, there is no enforcement outside of court . . . . There may be, and I am convinced that there are, many unlawful searches of homes and automobiles of innocent people which turn up nothing incriminating, in which no arrest is made, about which courts do nothing, and about which we never hear." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#181" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 181</a></span> (Jackson, J., dissenting).</p>
<p>[22]  The Least Dangerous Branch 24 (1962).</p>

</div>
```

---
