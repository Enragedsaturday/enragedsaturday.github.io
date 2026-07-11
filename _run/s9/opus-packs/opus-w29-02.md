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

## GROUP: content/cases/Chambers v. Maroney.md  (`case`, 5 assertions)

### content_page

```
---
title: "Chambers v. Maroney"
type: case
citation: "399 U.S. 42 (1970)"
parallel_cite: "90 S. Ct. 1975; 26 L. Ed. 2d 419"
neutral_cite: 1970 U.S. LEXIS 19
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-10-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1970-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chambers v. Maroney
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108184/chambers-v-maroney/"
  cluster_id: 108184
  opinion_id: 9424320
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Acevedo]]", "[[California v. Carney]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "warrantless-search", "vehicle", "station-house"]
holding: "Where there was PC and mobility at the scene, officers may search the vehicle without a warrant later at the station house; immediate…"
lake:
  record_id: Chambers v. Maroney
  status: verified
  projected_at: 2026-07-06
---

# Chambers v. Maroney

*399 U.S. 42 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police, acting on probable cause from witness descriptions, stopped a station wagon shortly after an armed service-station robbery, arrested the occupants, and drove the car to the police station, where they searched it without a warrant and found weapons and evidence of the robbery. Chambers challenged the warrantless station-house search.

## Issue
Whether police who had probable cause and a lawfully stopped vehicle at the scene may instead search it without a warrant later at the station house.

## Rule
Yes. Given probable cause to search a vehicle that was mobile when stopped, a warrantless search at the station house is reasonable: "For constitutional purposes, we see no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. Given probable cause to search, either course is reasonable under the Fourth Amendment." — 399 U.S. 42, 52. ^pin-52

## Application
The officers had probable cause to search the station wagon and could lawfully have searched it on the spot, where it was a "fleeting target." Because both the probable cause and the car's mobility persisted, searching it without a warrant after it had been taken to the station house was, on these facts, no less reasonable than an immediate roadside search.

## Conclusion
The warrantless station-house search was reasonable; the conviction was upheld. *Chambers* extends the [[Carroll v. United States]] automobile exception to a later search away from the scene.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chambers* elaborates the [[Carroll v. United States]] rule and is part of the line later unified for containers in [[California v. Acevedo]] and grounded in the exception's two justifications in [[California v. Carney]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Chambers v. Maroney*, 399 U.S. 42 (1970) — https://www.courtlistener.com/opinion/108184/chambers-v-maroney/ — pinpoint: 52.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1ef65060210513f1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "399 U.S. 42 (1970)", "court": "U.S. Supreme Court", "neutral_cite": "1970 U.S. LEXIS 19", "official_citation_present": true, "parallel_cite": "90 S. Ct. 1975; 26 L. Ed. 2d 419", "title": "Chambers v. Maroney", "year": "1970"}}
{"assertion_id": "7e6efbe7f9c0294f", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "Chambers v. Maroney"}}
{"assertion_id": "a7a585a668bdacc7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where there was PC and mobility at the scene, officers may search the vehicle without a warrant later at the station house; immediate…", "title": "Chambers v. Maroney"}}
{"assertion_id": "270340d350971c50", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chambers v. Maroney"}}
{"assertion_id": "ac4d3efbf5b499ce", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1970-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Chambers v. Maroney", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Chambers v. Maroney", "varies_by_point": "false"}}
```

### lake record — Chambers v. Maroney

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chambers v. Maroney",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chambers v. Maroney",
    "case_name_short": "Chambers",
    "case_name_full": "Chambers v. Maroney, Correctional Superintendent",
    "input_case_name": "Chambers v. Maroney",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-10-12",
    "year": 1970,
    "docket": null,
    "cluster_id": 108184,
    "lead_opinion_id": 9424320,
    "sibling_ids": [
      108184,
      9424320,
      9424321,
      9424322
    ],
    "absolute_url": "/opinion/108184/chambers-v-maroney/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8978955,
        "score": 20,
        "case_name": "Chambers v. Maroney"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "399 U.S. 42",
      "volume": "399",
      "reporter": "U.S.",
      "page": "42",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 1975",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 419",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 19",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "19",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "399 U.S. 42",
        "volume": "399",
        "reporter": "U.S.",
        "page": "42",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1975",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 419",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 19",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "19",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "399 U.S. 42",
    "official_selection": {
      "court_class": "scotus",
      "selected": "399 U.S. 42",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-52",
      "page": null,
      "quote": "--- # Chambers v. Maroney *399 U.S. 42 (1970)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police, acting on probable cause from witness descriptions, stopped a station wagon shortly after an armed service-station robbery, arrested the occupants, and drove the car to the police station, where they searched it without a warrant and found weapons and evidence of the robbery. Chambers challenged the warrantless station-house search. ## Issue Whether police who had probable cause and a lawfully stopped vehicle at the scene may instead search it without a warrant later at the station house. ## Rule Yes. Given probable cause to search a vehicle that was mobile when stopped, a warrantless search at the station house is reasonable:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1970-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chambers v. Maroney",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Podrazo",
          "cluster_id": 2645492,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Williams v. State",
          "cluster_id": 2542111,
          "cite": [
            "356 S.W.3d 508",
            "2011 WL 5220350"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Curtis Leo Williams v. State",
          "cluster_id": 3089627,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dahlem v. State",
          "cluster_id": 2274819,
          "cite": [
            "322 S.W.3d 685",
            "2010 WL 1854413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cronic",
          "cluster_id": 111169,
          "cite": [
            "80 L. Ed. 2d 657",
            "104 S. Ct. 2039",
            "466 U.S. 648",
            "1984 U.S. LEXIS 78",
            "52 U.S.L.W. 4560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": [
            "58 L. Ed. 2d 387",
            "99 S. Ct. 421",
            "439 U.S. 128",
            "1978 U.S. LEXIS 2452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Clark",
          "cluster_id": 111750,
          "cite": [
            "92 L. Ed. 2d 460",
            "106 S. Ct. 3101",
            "478 U.S. 570",
            "1986 U.S. LEXIS 135",
            "54 U.S.L.W. 5023"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. Slappy",
          "cluster_id": 110914,
          "cite": [
            "75 L. Ed. 2d 610",
            "103 S. Ct. 1610",
            "461 U.S. 1",
            "1983 U.S. LEXIS 5",
            "51 U.S.L.W. 4399"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiteley v. Warden, Wyoming State Penitentiary",
          "cluster_id": 108297,
          "cite": [
            "28 L. Ed. 2d 306",
            "91 S. Ct. 1031",
            "401 U.S. 560",
            "1971 U.S. LEXIS 65",
            "58 Ohio Op. 2d 434"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Wilson",
          "cluster_id": 118086,
          "cite": [
            "137 L. Ed. 2d 41",
            "117 S. Ct. 882",
            "519 U.S. 408",
            "1997 U.S. LEXIS 1271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Barlow's, Inc.",
          "cluster_id": 109866,
          "cite": [
            "56 L. Ed. 2d 305",
            "98 S. Ct. 1816",
            "436 U.S. 307",
            "1978 U.S. LEXIS 26",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "6 OSHC (BNA) 1571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjEzNjYwODAwMDAwJnM9MjMzNTE5NSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108184+OR+9424320+OR+9424321+OR+9424322%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MDMmcz0xMTA1NTgmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108184+OR+9424320+OR+9424321+OR+9424322%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322)",
        "reviewed": 31,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 31,
        "triage_read": 0,
        "triage_snippet_classified": 31
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322)",
    "indexed_citing_opinions": 2970,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108184,
        "count": 2726,
        "count_source": "search"
      },
      {
        "opinion_id": 9424320,
        "count": 358,
        "count_source": "search"
      },
      {
        "opinion_id": 9424321,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424322,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4392,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chambers-v-maroney.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MTM2Mjgmcz05NDM5ODM1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108184+OR+9424320+OR+9424321+OR+9424322%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108184,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 103272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 284134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 286933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
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
    "date_created": "2026-07-04T23:47:16Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:47:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:47:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:50:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:47:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chambers v. Maroney

```
<opinion type="majority">
<author id="b79-13">Mr. Justice White</author>
<p id="AG1">delivered the opinion of the Court.</p>
<p id="A5B">The principal question in this case concerns the admissibility of evidence seized from an automobile, in which petitioner was riding at the time of his arrest, after the automobile was taken to a police station and was there thoroughly searched without a warrant. The Court of Appeals for the Third Circuit found no violation of petitioner’s Fourth Amendment rights. We affirm.</p>
<p id="b80-5"><page-number citation-index="1" label="44">*44</page-number>I</p>
<p id="b80-6">During the night of May 20, 1963, a Gulf service station in North Braddock, Pennsylvania, was robbed by two men, each of whom carried and displayed a gun. The robbers took the currency from the cash register; the service station attendant, one Stephen Kovacich, was directed to place the coins in his right-hand glove, which was then taken by the robbers. Two teen-agers, who had earlier noticed a blue compact station wagon circling the block in the vicinity of the Gulf station, then saw the station wagon speed away from a parking lot close to the Gulf station. About the same time, they learned that the Gulf station had been robbed. They reported to police, who arrived immediately, that four men were in the station wagon and one was wearing a green sweater. Kova-cich told the police that one of the men who robbed him was wearing a green sweater and the other was wearing a trench coat. A description of the car and the two robbers was broadcast over the police radio. Within an hour, a light blue compact station wagon answering the description and carrying four men was stopped by the police about two miles from the Gulf station. Petitioner was one of the men in the station wagon. He was wearing a green sweater and there was a trench coat in the car. The occupants were arrested and the car was driven to the police station. In the course of a thorough search of the car at the station, the police found concealed in a compartment under the dashboard two .38-caliber revolvers (one loaded with dumdum bullets), a right-hand glove containing small change, and certain cards bearing the name of Raymond Havicon, the attendant at a Boron service station in McKeesport, Pennsylvania, who had been robbed at gunpoint on May 13, 1963. In the course of a warrant-authorized search of petitioner’s home the day after petitioner’s arrest, police found and <page-number citation-index="1" label="45">*45</page-number>seized certain .38-caliber ammunition, including some dumdum bullets similar' to those found in one of the guns taken from the station wagon.</p>
<p id="b81-5">Petitioner was indicted for both robberies.<footnotemark>1</footnotemark> His first trial ended in a mistrial but he was convicted of both robberies at the second trial. Both Kovacieh and Hav-icon identified petitioner as one of the robbers.<footnotemark>2</footnotemark> The materials taken from the station wagon were introduced into evidence, Kovacieh identifying his glove and Hav-icon the cards taken in the May 13 robbery. The bullets seized at petitioner’s house were also introduced over objections of petitioner’s counsel.<footnotemark>3</footnotemark> Petitioner was sentenced to a term of four to eight years’ imprisonment for the May 13 robbery and to a term of two to seven years’ imprisonment for the May 20 robbery, the sentences to run consecutively.<footnotemark>4</footnotemark> Petitioner did not take a direct appeal from these convictions. In 1965, petitioner sought a writ of habeas corpus in the state court, which denied the writ after a brief evidentiary hearing; the denial of <page-number citation-index="1" label="46">*46</page-number>the writ was affirmed on appeal in the Pennsylvania appellate courts. Habeas corpus proceedings were then commenced in the United States District Court for the Western District of Pennsylvania. An order to show cause was issued. Based on the State’s response and the state court record, the petition for habeas corpus was denied without a hearing. The Court of Appeals for the Third Circuit affirmed, <span class="citation" data-id="284134"><a href="/opinion/284134/united-states-of-america-ex-rel-frank-chambers-v-james-f-maroney/" aria-description="Citation for case: United States of America Ex Rel. Frank Chambers v. James...">408 F. 2d 1186</a></span>, and we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./396/900/">396 U. S. 900</a></span> (1969).<footnotemark>5</footnotemark></p>
<p id="b82-6">II</p>
<p id="b82-7">We pass quickly the claim that the search of the automobile was the fruit of an unlawful arrest. Both the courts below thought the arresting officers had probable cause to make the arrest. We agree. Having talked to the teen-age observers and to the victim Kova-cich, the police had ample cause to stop a light blue compact station wagon carrying four men and to arrest the occupants, one of whom was wearing a green sweater <page-number citation-index="1" label="47">*47</page-number>and one of whom had a trench coat with him in the car.<footnotemark>6</footnotemark></p>
<p id="b83-4">Even so, the search that produced the incriminating evidence was made at the police station some time after the arrest and cannot be justified as a search incident to an arrest: “Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest.” <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). <em>Dyke </em>v. <em>Taylor Implement Mfg. Co., </em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> (1968), is to the same effect; the reasons that have been thought sufficient to justify warrantless searches carried out in connection with an. arrest no longer obtain when the accused is safely in custody at the station house.</p>
<p id="b83-5">There are, however, alternative grounds arguably justifying the search of the car in this case. In <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston, supra,</a></span> </em>the arrest was for vagrancy; it was apparent that the officers had no cause to believe that evidence of crime was concealed in the auto. In <em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">Dyke, supra,</a></span> </em>the Court expressly rejected the suggestion that there was probable cause to search the car, <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#221" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S., at 221-222</a></span>. Here the situation is different, for the police had probable cause to believe that the robbers, carrying guns and the fruits of the crime, had fled the scene in a light blue compact station wagon which would be carrying four men, one wearing a green sweater and another wearing a trench coat. As the state courts correctly held, there was probable cause to arrest the occupants of the station wagon that the officers stopped; just as obviously was <page-number citation-index="1" label="48">*48</page-number>there probable cause to search the car for guns and stolen money.</p>
<p id="b84-4">In terms of the circumstances justifying a warrantless search, the Court has long distinguished between an automobile and a home or office. In <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), the issue was the admissibility in evidence of contraband liquor seized in a war-rantless search of a car on the highway. After surveying the law from the time of the adoption of the Fourth Amendment onward, the Court held that automobiles and other conveyances may be searched without a warrant in circumstances that would not justify the search without a warrant of a house or an office, provided that there is probable cause to believe that the car contains articles that the officers are entitled to seize. The Court expressed its holding as follows:</p>
<blockquote id="b84-5">“We have made a somewhat extended reference to these statutes to show that the guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.</blockquote>
<blockquote id="b84-6">“Having thus established that contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant, we come now to consider under what circumstances such search may be made. . . . [T]hose lawfully within the country, entitled to use <page-number citation-index="1" label="49">*49</page-number>the public highways, have a right to free passage without interruption or search unless there is known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise. . . .</blockquote>
<blockquote id="b85-5">“The measure of legality of such a seizure is, therefore, that the seizing officer shall have reasonable or probable cause for believing that the automobile which he stops and seizes has contraband liquor therein which is being illegally transported.” <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153-154, 155-156</a></span>.</blockquote>
<p id="b85-6">The Court also noted that the search of an auto on probable cause proceeds on a theory wholly different from that justifying the search incident to an arrest:</p>
<blockquote id="b85-7">“The right to search and the validity of the seizure are not dependent on the right to arrest. They are dependent on the reasonable cause the seizing officer has for belief that the contents of the automobile offend against the law.” <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158-159</a></span>.</blockquote>
<p id="b85-8">Finding that there was probable cause for the search and seizure at issue before it, the Court affirmed the convictions.</p>
<p id="b85-9"><em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>was followed and applied in <em>Husty </em>v. <em>United States, </em><span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931), and <em>Scher </em>v. <em>United States, </em><span class="citation" data-id="103100"><a href="/opinion/103100/scher-v-united-states/" aria-description="Citation for case: Scher v. United States">305 U. S. 251</a></span> (1938). It was reaffirmed and followed in <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). In 1964, the opinion in <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston, supra,</a></span> </em>cited both <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>and <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>with approval, <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#366" aria-description="Citation for case: Preston v. United States">376 U. S., at 366-367</a></span>. In <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967),<footnotemark>7</footnotemark> <page-number citation-index="1" label="50">*50</page-number>the Court read <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>as dealing primarily with a search incident to arrest and cited that case for the proposition that the mobility of a car may make the search of a car without a warrant reasonable “although the result might be the opposite in a search of a home, a store, or other fixed piece of property.” <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#59" aria-description="Citation for case: Cooper v. California">386 U. S., at 59</a></span>. The Court’s opinion in <em>Dyke, </em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#221" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S., at 221</a></span>, recognized that “[a]utomobiles, because of their mobility, may be searched without a warrant upon facts not justifying a warrantless search of a residence or office,” citing <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>and <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra.</a></span> </em>However, because there was insufficient reason to search the car involved in the <em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">Dyke</a></span> </em>case, the Court did not reach the question of whether those cases “extend to a warrant-less search, based upon probable cause, of an automobile which, having been stopped originally on a highway, is parked outside a courthouse.” <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#222" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S., at 222</a></span>.<footnotemark>8</footnotemark></p>
<p id="AKg">Neither <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span> </em>nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords. But the circumstances that <page-number citation-index="1" label="51">*51</page-number>furnish probable cause to search a particular auto for particular articles are most often unforeseeable; moreover, the opportunity to search is fleeting since a car is readily movable. Where this is true, as in <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>and the case before us now, if an effective search is to be made at any time, either the search must be made immediately without a warrant or the car itself must be seized and held without a warrant for whatever period is necessary to obtain a warrant for the search.<footnotemark>9</footnotemark></p>
<p id="b87-5">In enforcing the Fourth Amendment’s prohibition against unreasonable searches and seizures, the Court has insisted upon probable cause as a minimum requirement for a reasonable search permitted by the Constitution. As a general rule, it has also required the judgment of a magistrate on the probable-cause issue and the issuance of a warrant before a search is made. Only in exigent circumstances will the judgment of the police as to probable cause serve as a sufficient authorization for a search. <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span> </em>holds a search warrant unnecessary where there is probable cause to search an automobile stopped on the highway; the car is movable, the occupants are alerted, and the car’s contents may never be found again if a warrant must be obtained. Hence an immediate search is constitutionally permissible.</p>
<p id="b87-6">Arguably, because of the preference for a magistrate’s judgment, only the immobilization of the car should be permitted until a search warrant is obtained; arguably, only the “lesser” intrusion is permissible until the magistrate authorizes the “greater.” But which is the “greater” and which the “lesser” intrusion is itself a debatable question and the answer may depend on a variety <page-number citation-index="1" label="52">*52</page-number>of circumstances. For constitutional purposes, we see no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. Given probable cause to search, either course is reasonable under the Fourth Amendment.</p>
<p id="b88-5">On the facts before us, the blue station wagon could have been searched on the spot when it was stopped since there was probable cause to search and it was a fleeting target for a search. The probable-cause factor still obtained at the station house and so did the mobility of the car unless the Fourth Amendment permits a warrantless seizure of the car and the denial of its use to anyone until a warrant is secured. In that event there is little to choose in terms of practical consequences between an immediate search without a warrant and the car’s immobilization until a warrant i's obtained.<footnotemark>10</footnotemark> The same consequences may not follow where there is unforeseeable cause to search a house. Compare <em>Vale </em>v. <em>Louisiana, ante, </em>p. 30. But as <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span> </em>held, for the purposes of the Fourth Amendment there is a constitutional difference between houses and cars.</p>
<p id="b88-6">Ill</p>
<p id="b88-7">Neither of petitioner’s remaining contentions warrants reversal of the judgment of the Court of Appeals. One of them challenges the admissibility at trial of the .38-caliber ammunition seized in the course of a search of petitioner’s house. The circumstances relevant to this <page-number citation-index="1" label="53">*53</page-number>issue are somewhat confused, involving as they do questions of probable cause, a lost search warrant, and the Pennsylvania procedure for challenging the admissibility of evidence seized. Both the District Court and the Court of Appeals, however, after careful examination of the record, found that if there was error in admitting the ammunition, the error was harmless beyond a reasonable doubt. Having ourselves studied this record, we are not prepared to differ with the two courts below. See <em>Harrington </em>v. <em>California, </em><span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969).</p>
<p id="b89-5">The final claim is that petitioner was not afforded the effective assistance of counsel. The facts pertinent to this claim are these: The Legal Aid Society of Allegheny County was appointed to represent petitioner prior to his first trial. A representative of the society conferred with petitioner, and a member of its staff, Mr. Middleman, appeared for petitioner at the first trial. There is no claim that petitioner was not then adequately represented by fully prepared counsel. The difficulty arises out of the second trial. Apparently no one from the Legal Aid Society again conferred with petitioner until a few minutes before the second trial began. The attorney who then appeared to represent petitioner was not Mr. Middleman but Mr. Tamburo, another Legal Aid Society attorney. No charge is made that Mr. Tamburo was incompetent or inexperienced; rather the claim is that his appearance for petitioner was so belated that he could not have furnished effective legal assistance at the second trial. Without granting an evidentiary hearing, the District Court rejected petitioner’s claim. The Court of Appeals dealt with the matter in an extensive opinion. After carefully examining the state court record, which it had before it, the court found ample grounds for holding that the appearance of a different attorney at the second trial had not resulted in prejudice to petitioner. The claim that Mr. Tamburo <page-number citation-index="1" label="54">*54</page-number>was unprepared centered around his allegedly inadequate efforts to have the guns and ammunition excluded from evidence. But the Court of Appeals found harmless any error in the admission of the bullets and ruled that the guns and other materials seized from the car were admissible evidence. Hence the claim of prejudice from the substitution of counsel was without substantial basis.<footnotemark>11</footnotemark> In this posture of the case we are not inclined to disturb the judgment of the Court of Appeals as to what the state record shows with respect to the adequacy of counsel. Unquestionably, the courts should make every effort to effect early appointments of counsel in all cases. But we are not disposed to fashion a <em>per se </em>rule requiring reversal of every conviction following tardy appointment of counsel or to hold that, whenever a habeas corpus petition alleges a belated appointment, an evidentiary hearing must be held to determine whether the defendant has been denied his constitutional right to counsel. The Court of Appeals reached the right result in denying a hearing in this case.</p>
<p id="b90-4">
<em>Affirmed.</em>
</p>
<judges id="b90-5">Mr. Justice Blackmun took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b81-6"> Petitioner was indicted separately for each robbery. One of the other three men was similarly indicted and the other two were indicted only for the Gulf robbery. All indictments and all defendants were tried together. In a second trial following a mistrial, the jury found all defendants guilty as charged.</p>
</footnote>
<footnote label="2">
<p id="b81-7"> Kovacieh identified petitioner at a pretrial stage of the proceedings, and so testified, but could not identify him at the trial. Havieon identified petitioner both before trial and at trial.</p>
</footnote>
<footnote label="3">
<p id="b81-8"> The bullets were apparently excluded at the first trial. The grounds for the exclusion do not clearly appear from the record now before us.</p>
</footnote>
<footnote label="4">
<p id="b81-9"> The four-to-eight-year sentence was to be served concurrently with another sentence, for an unrelated armed robbery offense, imposed earlier but vacated subsequent to imposition of sentence in this case. The two-to-seven-year term was to be consecutive to the other sentences. It appears that the offenses here at issue caused revocation of petitioner’s parole in connection with a prior conviction. Apparently petitioner has now begun to serve the first of the two sentences imposed for the convictions here challenged.</p>
</footnote>
<footnote label="5">
<p id="b82-8"> Since <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), the federal courts have regularly entertained and ruled on petitions for habeas corpus filed by state prisoners alleging that unconstitutionally seized evidence was admitted at their trials. See, <em>e. g., Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968); <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967). As for federal prisoners, a divided Court held that relief under <span class="citation no-link">28 U. S. C. § 2255</span> was available to vindicate Fourth Amendment rights. <em>Kaufman </em>v. <em>United States, </em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969). Right-to-counsel claims of course have regularly been pressed and entertained in federal habeas corpus proceedings.</p>
<p id="b82-9">It is relevant to note here that petitioner Chambers at trial made no objection to the introduction of the items seized from the car; however his Fourth Amendment claims with respect to the auto search were raised and passed on by the Pennsylvania courts in the state habeas corpus proceeding. His objection to the search of his house was raised at his trial and rejected both on the merits and because he had not filed a motion to suppress; similar treatment was given the point in the state collateral proceedings, which took <page-number citation-index="1" label="47">*47</page-number>place before the same judge who had tried the criminal case. The counsel claim was not presented at trial but was raised and rejected in the state collateral proceedings.</p>
</footnote>
<footnote label="6">
<p id="b83-9"> In any event, as we point out below, the validity of an arrest is not necessarily determinative of the right to search a car if there is probable cause to make the search. Here, as will be true in many cases, the circumstances justifying the arrest are also those furnishing probable cause for the search.</p>
</footnote>
<footnote label="7">
<p id="b85-10"> <em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span> </em>involved the warrantless search of a car held for forfeiture under state law. Evidence seized from the car in that search was held admissible. In the case before us no claim is made that state law authorized that the station wagon be held as <page-number citation-index="1" label="50">*50</page-number>evidence or as an instrumentality of the crime; nor was the station wagon an abandoned or stolen vehicle. The question here is whether probable cause justifies a warrantless search in. the circumstances presented.</p>
</footnote>
<footnote label="8">
<p id="b86-7"> Nothing said last term in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), purported to modify or affect the rationale of <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>. </em>As the Court noted:</p>
<blockquote id="b86-8">“Our holding today is of course entirely consistent with the recognized principle that, assuming the existence of probable cause, automobiles and other vehicles may be searched without warrants 'where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.’ <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span>; see <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span>.” 395 U. S., at 764 n. 9.</blockquote>
</footnote>
<footnote label="9">
<p id="b87-7"> Following the car until a warrant can be obtained seems an impractical alternative since, among other things, the car may be taken out of the jurisdiction. Tracing the car and searching it hours or days later would of course permit instruments or fruits of crime to be removed from the car before the search.</p>
</footnote>
<footnote label="10">
<p id="b88-8"> It was not unreasonable in this case to take the car to the station house. All occupants in the car were arrested in a dark parking lot in the middle of the night. A careful search at that point was impractical and perhaps not safe for the officers, and it would serve the owner’s convenience and the safety of his car to have the vehicle and the keys together at the station house.</p>
</footnote>
<footnote label="11">
<p id="b90-8"> It is pertinent to note that each of the four defendants was represented by separate counsel. The attorney for Lawson, who was the car owner and who was the only defendant to take the stand, appears to have been the lead counsel. As far as the record before us reveals, no counsel made any objection at the trial to the admission of the items taken from the car. Petitioner’s counsel objected to the introduction of the bullets seized from petitioner’s house.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Chandler v. Miller.md  (`case`, 5 assertions)

### content_page

```
---
title: "Chandler v. Miller"
type: case
citation: "520 U.S. 305 (1997)"
parallel_cite: "117 S. Ct. 1295; 137 L. Ed. 2d 513"
neutral_cite: 1997 U.S. LEXIS 2505
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1997
date_decided: 1997-04-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1997-04-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chandler v. Miller
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118100/chandler-v-miller/"
  cluster_id: 118100
  opinion_id: 9433438
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[City of Indianapolis v. Edmond]]", "[[Ferguson v. City of Charleston]]", "[[Board of Education v. Earls]]"]
aliases: []
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "suspicionless-search"]
holding: "Georgia's suspicionless drug-testing requirement for candidates for state office is unconstitutional — there was no concrete, special…"
lake:
  record_id: Chandler v. Miller
  status: verified
  projected_at: 2026-07-06
---

# Chandler v. Miller

*520 U.S. 305 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Georgia required candidates for designated state offices to certify they had passed a urinalysis drug test within 30 days of qualifying for the ballot. Two Libertarian Party candidates challenged the requirement as an unreasonable suspicionless search under the Fourth Amendment.

## Issue
Whether a State's suspicionless drug-testing requirement for candidates for elective office fits the special-needs exception to the Fourth Amendment's individualized-suspicion baseline.

## Rule
No, absent a genuine, concrete danger the testing is designed to meet. Where public safety is substantial and real, suspicionless searches calibrated to the risk may be reasonable; "[b]ut where, as in this case, public safety is not genuinely in jeopardy, the Fourth Amendment precludes the suspicionless search, no matter how conveniently arranged." — 520 U.S. 305, 323. ^pin-323

"However well meant, the candidate drug test Georgia has devised diminishes personal privacy for a symbol's sake. The Fourth Amendment shields society against that state action." — *Id.* at 322. ^pin-322

## Application
Georgia identified no concrete drug problem among its officeholders and the certification scheme was not designed to detect actual use (candidates chose their own test date and could abstain beforehand). Because the State showed no special need substantial enough to override the individualized-suspicion requirement, the suspicionless testing requirement was unconstitutional on these facts.

## Conclusion
Georgia's candidate drug-testing statute violated the Fourth Amendment; the judgment upholding it was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chandler* marks the outer limit of the special-needs doctrine, distinguishing the safety-justified testing upheld in earlier cases and foreshadowing the law-enforcement-purpose limits of [[Ferguson v. City of Charleston]] and [[City of Indianapolis v. Edmond]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Chandler v. Miller*, 520 U.S. 305 (1997) — https://www.courtlistener.com/opinion/118100/chandler-v-miller/ — pinpoints: 322, 323.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "243e39b447438a61", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "520 U.S. 305 (1997)", "court": "U.S. Supreme Court", "neutral_cite": "1997 U.S. LEXIS 2505", "official_citation_present": true, "parallel_cite": "117 S. Ct. 1295; 137 L. Ed. 2d 513", "title": "Chandler v. Miller", "year": "1997"}}
{"assertion_id": "111929f9af51ce10", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "Chandler v. Miller"}}
{"assertion_id": "91ed0b70e0d131e9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Georgia's suspicionless drug-testing requirement for candidates for state office is unconstitutional — there was no concrete, special…", "title": "Chandler v. Miller"}}
{"assertion_id": "637b9b2a6fa77aee", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1997-04-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Chandler v. Miller", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Chandler v. Miller", "varies_by_point": "false"}}
{"assertion_id": "7ba1d647bef58712", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chandler v. Miller"}}
```

### lake record — Chandler v. Miller

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chandler v. Miller",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chandler v. Miller",
    "case_name_short": "",
    "case_name_full": "CHANDLER Et Al. v. MILLER, GOVERNOR OF GEORGIA, Et Al.",
    "input_case_name": "Chandler v. Miller",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-04-15",
    "year": 1997,
    "docket": null,
    "cluster_id": 118100,
    "lead_opinion_id": 9433438,
    "sibling_ids": [
      118100,
      9433438,
      9433439
    ],
    "absolute_url": "/opinion/118100/chandler-v-miller/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "520 U.S. 305",
      "volume": "520",
      "reporter": "U.S.",
      "page": "305",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 1295",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 513",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "513",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 2505",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2505",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "520 U.S. 305",
        "volume": "520",
        "reporter": "U.S.",
        "page": "305",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 1295",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 513",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "513",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 2505",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2505",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "520 U.S. 305",
    "official_selection": {
      "court_class": "scotus",
      "selected": "520 U.S. 305",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-323",
      "page": null,
      "quote": "--- # Chandler v. Miller *520 U.S. 305 (1997)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Georgia required candidates for designated state offices to certify they had passed a urinalysis drug test within 30 days of qualifying for the ballot. Two Libertarian Party candidates challenged the requirement as an unreasonable suspicionless search under the Fourth Amendment. ## Issue Whether a State's suspicionless drug-testing requirement for candidates for elective office fits the special-needs exception to the Fourth Amendment's individualized-suspicion baseline. ## Rule No, absent a genuine, concrete danger the testing is designed to meet. Where public safety is substantial and real, suspicionless searches calibrated to the risk may be reasonable;",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-322",
      "page": null,
      "quote": "However well meant, the candidate drug test Georgia has devised diminishes personal privacy for a symbol's sake. The Fourth Amendment shields society against that state action.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1997-04-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chandler v. Miller",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. King",
          "cluster_id": 8441539,
          "cite": [
            "736 F.3d 805",
            "2013 WL 4516751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marcel King",
          "cluster_id": 854814,
          "cite": [
            "711 F.3d 986",
            "2013 WL 886161",
            "2013 U.S. App. LEXIS 4730"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 2967360,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schenekl v. State",
          "cluster_id": 1472762,
          "cite": [
            "996 S.W.2d 305",
            "1999 WL 374216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane1_negative"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
          "cluster_id": 121171,
          "cite": [
            "153 L. Ed. 2d 735",
            "122 S. Ct. 2559",
            "536 U.S. 822",
            "2002 U.S. LEXIS 4882",
            "2002 Cal. Daily Op. Serv. 5761",
            "2002 Daily Journal DAR 7275",
            "70 U.S.L.W. 4737",
            "15 Fla. L. Weekly Fed. S 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segundo v. State",
          "cluster_id": 1590541,
          "cite": [
            "270 S.W.3d 79",
            "2008 Tex. Crim. App. LEXIS 1505",
            "2008 WL 4724093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolfson v. Brammer",
          "cluster_id": 153018,
          "cite": [
            "616 F.3d 1045",
            "2010 U.S. App. LEXIS 16766",
            "2010 WL 3191159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Comite De Jornaleros De Redondo Beach v. City of Redondo Beach",
          "cluster_id": 613771,
          "cite": [
            "657 F.3d 936",
            "2011 WL 4336667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jacoby, T., Aplt.",
          "cluster_id": 4429713,
          "cite": [
            "170 A.3d 1065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pierce v. Smith",
          "cluster_id": 12443,
          "cite": [
            "117 F.3d 866",
            "13 I.E.R. Cas. (BNA) 8",
            "1997 U.S. App. LEXIS 17907",
            "1997 WL 395259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "American Civil Liberties Union v. United States Conference of Catholic Bishops",
          "cluster_id": 815386,
          "cite": [
            "705 F.3d 44",
            "2013 WL 150321",
            "2013 U.S. App. LEXIS 976"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marcavage v. City of New York",
          "cluster_id": 805786,
          "cite": [
            "689 F.3d 98",
            "2012 WL 3125225",
            "2012 U.S. App. LEXIS 16081"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re the United States",
          "cluster_id": 8441402,
          "cite": [
            "724 F.3d 600",
            "58 Communications Reg. (P&F) 1292",
            "2013 WL 3914484",
            "2013 U.S. App. LEXIS 15510"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Los Angeles v. Patel",
          "cluster_id": 2810524,
          "cite": [
            "576 U.S. 409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brandon Michael Lifshitz",
          "cluster_id": 786321,
          "cite": [
            "369 F.3d 173",
            "2004 WL 1043468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Lee Scott",
          "cluster_id": 794629,
          "cite": [
            "450 F.3d 863",
            "2006 U.S. App. LEXIS 14182"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wiedeman",
          "cluster_id": 1033708,
          "cite": [
            "286 Neb. 193",
            "835 N.W.2d 698"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118100 OR 9433438 OR 9433439) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MjI4Mzg0MDAwMDAmcz0zMDIyMjc2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118100+OR+9433438+OR+9433439%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118100 OR 9433438 OR 9433439)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OSZzPTEyNzM0NTgmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118100+OR+9433438+OR+9433439%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118100 OR 9433438 OR 9433439)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118100 OR 9433438 OR 9433439)",
    "indexed_citing_opinions": 321,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118100,
        "count": 290,
        "count_source": "search"
      },
      {
        "opinion_id": 9433438,
        "count": 38,
        "count_source": "search"
      },
      {
        "opinion_id": 9433439,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 525,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chandler-v-miller.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY4NDg3OTkmcz00NzY3NjMyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118100+OR+9433438+OR+9433439%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118100,
        "cited_id": 101887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 107301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 108902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 109831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112632,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 355692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 422035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 486563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 711061,
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
    "date_created": "2026-07-04T23:50:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:53:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chandler v. Miller

```
<opinion type="majority">
<author id="b400-5">Justice Ginsburg</author>
<p id="A5R">delivered the opinion of the Court.</p>
<p id="b400-6">The Fourth Amendment requires government to respect “[t]he right of the people to be secure in their persons . . . against unreasonable searches and seizures.” This restraint on government conduct generally bars officials from undertaking a search or seizure absent individualized suspicion. Searches conducted without grounds for suspicion of particular individuals have been upheld, however, in “certain limited circumstances.” See <em>Treasury Employees </em>v. <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 668</a></span> (1989). These circumstances include brief stops for questioning or observation at a fixed Border Patrol checkpoint, <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#545" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 545-550, 566-567</a></span> (1976), or at a sobriety checkpoint, <em>Michigan Dept. of State Police </em>v. <em>Sitz, </em><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444, 447, 455</a></span> (1990), and administrative inspections in “closely regulated” businesses, <em>New York </em>v. <em>Burger, </em><span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#703" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 703-704</a></span> (1987).</p>
<p id="b400-7">Georgia requires candidates for designated state offices to certify that they have taken a drug test and that the test result was negative. <span class="citation no-link">Ga. Code Ann. §21-2-140</span> (1993) (hereinafter §21-2-140). We confront in this case the question whether that requirement ranks among the limited circumstances in which suspicionless searches are warranted. Relying on this Court's precedents sustaining drug-testing <page-number citation-index="1" label="309">*309</page-number>programs for student athletes, customs employees, and railway employees, see <em>Vernonia School Dist. 47J </em>v. <em>Acton, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#650" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 650, 665-666</a></span> (1995) (random drug testing of students who participate in interscholastic sports); <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#659" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 659</a></span> (drug tests for United States Customs Service employees who seek transfer or promotion to certain positions); <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#608" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 608-613</a></span> (1989) (drug and alcohol tests for railway employees involved in train accidents and for those who violate particular safety rules), the United States Court of Appeals for the Eleventh Circuit judged Georgia’s law constitutional. We reverse that judgment. Georgia’s requirement that candidates for state office pass a drug test, we hold, does not fit within the closely guarded category of constitutionally permissible suspicionless searches.</p>
<p id="AOqb">I</p>
<p id="b401-3">The prescription at issue, approved by the Georgia Legislature in 1990, orders that “[ejach candidate seeking to qualify for nomination or election to a state office shall as a condition of such qualification be required to certify that such candidate has tested negative for illegal drugs.” §21 — 2— 140(b). Georgia was the first, and apparently remains the only, State to condition candidacy for state office on a drug test.</p>
<p id="b401-4">Under the Georgia statute, to qualify for a place on the ballot, a candidate must present a certificate from a state-approved laboratory, in a form approved by the Secretary of State, reporting that the candidate submitted to a urinalysis drug test within 30 days prior to qualifying for nomination or election and that the results were negative. § 21 — 2— 140(c). The statute lists as “[ijllegal drug[s]”: marijuana, cocaine, opiates, amphetamines, and phencyclidines. § 21-2-140(a)(3). The designated state offices are: “the Governor, Lieutenant Governor, Secretary of State, Attorney General, State School Superintendent, Commissioner of Insurance, <page-number citation-index="1" label="310">*310</page-number>Commissioner of Agriculture, Commissioner of Labor, Justices of the Supreme Court, Judges of the Court of Appeals, judges of the superior courts, district attorneys, members of the General Assembly, and members of the Public Service Commission.” § 21-2-140(a)(4).</p>
<p id="b402-5">Candidate drug tests are to be administered in a manner consistent with the United States Department of Health and Human Services Guidelines, <span class="citation no-link">53 Fed. Reg. 11979</span>-11989 (1988), or other professionally valid procedures approved by Georgia’s Commissioner of Human Resources. See § 21-2-140(a)(2). A candidate may provide the test specimen at a laboratory approved by the State, or at the office of the candidate’s personal physician, see App. 4-5 (Joint Statement of Undisputed Facts). Once a urine sample is obtained, an approved laboratory determines whether any of the five specified illegal drugs are present, <em>id., </em>at 5; §21-2-140(c), and prepares a certificate reporting the test results to the candidate.</p>
<p id="b402-6">Petitioners were Libertarian Party nominees in 1994 for state offices subject to the requirements of §21-2-140. The Party nominated Walker L. Chandler for the office of Lieutenant Governor, Sharon T. Harris for the office of Commissioner of Agriculture, and James D. Walker for the office of member of the General Assembly. In May 1994, about one month before the deadline for submission of the certificates required by §21-2-140, petitioners Chandler, Harris, and Walker filed this action in the United States District Court for the Northern District of Georgia. They asserted, <em>inter alia, </em>that the drug tests required by §21-2-140 violated their rights under the First, Fourth, and Fourteenth Amendments to the United States Constitution. Naming as defendants Governor Zell D. Miller and two other state officials involved in the administration of §21-2-140, petitioners requested declaratory and injunctive relief barring enforcement of the statute.</p>
<p id="b403-4"><page-number citation-index="1" label="311">*311</page-number>In June 1994, the District Court denied petitioners’ motion for a preliminary injunction. Stressing the importance of the state offices sought and the relative unintrusiveness of the testing procedure, the court found it unlikely that petitioners would prevail on the merits of their claims. App. to Pet. for Cert. 5B. Petitioners apparently submitted to the drug tests, obtained the certificates required by § 21-2-140, and appeared on the ballot. See Tr. of Oral Arg. 5. After the 1994 election, the parties jointly moved for the entry of final judgment on stipulated facts. In January 1995, the District Court entered final judgment for respondents.</p>
<p id="b403-5">A divided Eleventh Circuit panel affirmed. <span class="citation multiple-matches"><a href="/c/F.%203d/73/1543/">73 F. 3d 1543</a></span> (1996). It is settled law, the court accepted, that the drug tests required by the statute rank as searches. But, as was true of the drug-testing programs at issue in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>and <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>the court reasoned, §21-2-140 serves “special needs,” interests other than the ordinary needs of law enforcement. The court therefore endeavored to “ ‘balance the individual’s privacy expectations against the Government’s interests to determine whether it [was] impractical to require a warrant or some level of individualized suspicion in the particular context.’” 73 F. 3d, at 1545 (quoting <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 665-666</a></span>).</p>
<p id="b403-6">Examining the state interests involved, the court acknowledged the absence of any record of drug abuse by elected officials in Georgia. Nonetheless, the court observed, “[t]he people of Georgia place in the trust of their elected officials ... their liberty, their safety, their economic well-being, [and] ultimate responsibility for law enforcement.” 73 F. 3d, at 1546. Consequently, “those vested with the highest executive authority to make public policy in general and frequently to supervise Georgia’s drug interdiction efforts in particular must be persons appreciative of the perils of drug use.” <em>Ibid. </em>The court further noted that “[t]he nature of high public office in itself demands the highest levels of honesty, clear-sightedness, and clear-thinking.” <em>Ibid. </em>Re<page-number citation-index="1" label="312">*312</page-number>citing responsibilities of the offices petitioners sought, the Court of Appeals perceived those “positions [as] particularly susceptible to the ‘risks of bribery and blackmail against which the Government is entitled to guard.’ ” <em>Ibid, </em>(quoting <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 674</a></span>).</p>
<p id="b404-5">Turning to petitioners’ privacy interests, the Eleventh Circuit emphasized that the tests could be conducted in the office of the candidate’s private physician, making the “intrusion here . . . even less than that approved in <em>Von Raab." </em>73 F. 3d, at 1547. The court also noted the statute’s reference to federally approved drug-testing guidelines. <em>Ibid. </em>The drug test itself would reveal only the presence or absence of indicia <em>of </em>the use of particular drugs, and not any other information about the health of the candidate. Furthermore, the candidate would control release of the test results: Should the candidate test positive, he or she could forfeit the opportunity to run for office, and in that event, nothing would be divulged to law enforcement officials. <em>Ibid. </em>Another consideration, the court said, is the reality that “candidates for high office must expect the voters to demand some disclosures about their physical, emotional, and mental fitness for the position.” <em>Ibid. </em>Concluding that the State’s interests outweighed the privacy intrusion caused by the required certification, the court held the statute, as applied to petitioners, not inconsistent' with the Fourth and Fourteenth Amendments. <em>Ibid.</em><footnotemark><em>1</em></footnotemark></p>
<p id="b404-6">Judge Barkett dissented. In her view, a balance of the State’s and candidates’ interests was not appropriate, for the State had failed to establish a special governmental need for the regime. “There is nothing so special or immediate about the generalized governmental interests involved here,” she observed, “as to warrant suspension of the Fourth <page-number citation-index="1" label="313">*313</page-number>Amendment’s requirement of individualized suspicion for searches and seizures.” <em>Id., </em>at 1551.</p>
<p id="b405-5">We granted the petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./518/1057/">518 U. S. 1057</a></span> (1996), and now reverse.<footnotemark>2</footnotemark></p>
<p id="b405-6">II</p>
<p id="b405-7">We begin our discussion of this case with an uncontested point: Georgia’s drug-testing requirement, imposed by law and enforced by state officials, effects a search within the meaning of the Fourth and Fourteenth Amendments. See <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#617" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 617</a></span>; Tr. of Oral Arg. 36; Brief for United States as <em>Amicus Curiae </em>Í0 (collection and testing of urine to meet Georgia’s certification statute “constitutes a search subject to the demands of the Fourth Amendment” (internal quotation marks omitted)). As explained in <em>Sjkin-ner, </em>government-ordered “collection and testing of urine intrudes upon expectations of privacy that society has long recognized as reasonable.” 489 U. S., at 617. Because “these intrusions [are] searches under the Fourth Amendment,” <em>ibid., </em>we focus on the question: Are the searches reasonable?</p>
<p id="b405-8">To be reasonable under the Fourth Amendment, a search ordinarily must be based on individualized suspicion of wrongdoing. See <em>Vernonia, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 652-653</a></span>. But particularized exceptions to the main rule are sometimes warranted based on “special needs, beyond the normal need for law enforcement.” <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 619</a></span> (internal <page-number citation-index="1" label="314">*314</page-number>quotation marks omitted). When such “special needs”— concerns other than crime detection — are alleged in justification of a Fourth Amendment intrusion, courts must undertake a context-specific inquiry, examining closely the competing private and public interests advanced by the parties. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 665-666</a></span>; see also <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 668</a></span>. As <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>stated: “In limited circumstances, where the privacy interests implicated by the search are minimal, and where an important governmental interest furthered by the intrusion would be placed in jeopardy by a requirement of individualized suspicion, a search may be reasonable despite the absence of such suspicion.” 489 U. S., at 624.</p>
<p id="b406-5">In evaluating Georgia’s ballot-access, drug-testing statute — a measure plainly not tied to individualized suspicion— the Eleventh Circuit sought to “ ‘balance the individual’s privacy expectations against the [State’s] interests,’ ” 73 F. 3d, at 1545 (quoting <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 665</a></span>), in line with our precedents most immediately in point: <em>Skinner, Von Raab, </em>and <em>Vernonia. </em>We review those decisions before inspecting Georgia’s law.</p>
<p id="b406-6">A</p>
<p id="b406-7"><em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>concerned Federal Railroad Administration (FRA) regulations that required blood and urine tests of rail employees involved in train accidents; the regulations also authorized railroads to administer breath and urine tests to employees who violated certain safety rules. 489 U. S., at 608-612. The FRA adopted the drug-testing program in response to evidence of drug and alcohol abuse by some railroad employees, the obvious safety hazards posed by such abuse, and the documented link between drug- and alcohol-impaired employees and the incidence of train accidents. <em>Id., </em>at 607-608. Recognizing that the urinalysis tests, most conspicuously, raised evident privacy concerns, the Court noted two offsetting considerations: First, the regulations reduced the intrusiveness of the collection process, <em>id., </em>at 626; <page-number citation-index="1" label="315">*315</page-number>and, more important, railway employees, “by reason of their participation in an industry that is regulated pervasively to ensure safety,” had diminished expectations of privacy, <em>id., </em>at 627.</p>
<p id="b407-5">“[Surpassing safety interests,” the Court concluded, warranted the FRA testing program. <em>Id., </em>at 634. The drug tests could deter illegal drug use by railroad employees, workers positioned to “cause great human loss before any signs of impairment become noticeable to supervisors.” <em>Id., </em>at 628. The program also helped railroads to obtain invaluable information about the causes of major train accidents. See <em>id., </em>at 630. Testing without a showing of individualized suspicion was essential, the Court explained, if these vital interests were to be served. See <em>id., </em>at 628. Employees could not forecast the timing of an accident or a safety violation, events that would trigger testing. The employee’s inability to avoid detection simply by staying drug free at a prescribed test time significantly enhanced the deterrent effect of the program. See <em>ibid. </em>Furthermore, imposing an individualized suspicion requirement for a drug test in the chaotic aftermath of a train accident would seriously impede an employer’s ability to discern the cause of the accident; indeed, waiting until suspect individuals could be identified “likely would result in the loss or deterioration of the evidence furnished by the tests.” <em>Id., </em>at 631.</p>
<p id="b407-6">In <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>the Court sustained a United States Customs Service program that made drug tests a condition of promotion or transfer to positions directly involving drug interdiction or requiring the employee to carry a firearm. 489 U. S., at 660-661, 667-677.<footnotemark>3</footnotemark> While the Service’s regime was <page-number citation-index="1" label="316">*316</page-number>not prompted by a demonstrated drug abuse problem, <em>id., </em>at 660, it was developed for an agency with an “almost unique mission,” <em>id., </em>at 674, as the “first line of defense” against the smuggling of illicit drugs into the United States, <em>id., </em>at 668. Work directly involving drug interdiction and posts that require the employee to carry a firearm pose grave safety threats to employees who hold those positions, and also expose them to large amounts of illegal narcotics and to persons engaged in crime; illicit drug users in such high-risk positions might be unsympathetic to the Service’s mission, tempted by bribes, or even threatened with blackmail. See <em>id., </em>at 668-671. The Court held that the Government had a “compelling” interest in assuring that employees placed in these positions would not include drug users. See <em>id., </em>at 670-671. Individualized suspicion would not work in this setting, the Court determined, because it was “not feasible to subject [these] employees and their work product to the kind of day-to-day scrutiny that is the norm in more traditional office environments.” <em>Id., </em>at 674.</p>
<p id="b408-5">Finally, in <em>Vernonia, </em>the Court sustained a random drug-testing program for-high school students engaged in interscholastic athletic competitions. The program’s context was critical, for a local government bears large “responsibilities, under a public school system, as guardian and tutor of children entrusted to its care.” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#665" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 665</a></span>. An “immediate crisis,” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>id., </em>at 663</a></span>, caused by “a sharp increase in drug use” in the school district, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#648" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>id., </em>at 648</a></span>, sparked installation of the program. District Court findings established that student athletes were not only “among the drug users,” they were “leaders of the drug culture.” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>Id., </em>at 649</a></span>. Our decision noted that “‘students within the school environment have a lesser expectation of privacy than members of the population generally.’ ” <em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">Id.,</a></span> </em>at 657 (quoting <em>New Jersey </em>v. <page-number citation-index="1" label="317">*317</page-number><em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#348" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 348</a></span> (1985) (Powell, J., concurring)). We emphasized the importance of deterring drug use by schoolchildren and the risk of injury a drug-using student athlete east on himself and those engaged with him on the playing field. See <em>Vernonia, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662</a></span>.</p>
<p id="b409-5">B</p>
<p id="b409-6">Respondents urge that the precedents just examined are not the sole guides for assessing the constitutional validity of the Georgia statute. The “special needs” analysis, they contend, must be viewed through a different lens because § 21-2-140 implicates Georgia’s sovereign power, reserved to it under the Tenth Amendment, to establish qualifications for those who seek state office. Respondents rely on <em>Gregory </em>v. <em>Ashcroft, </em><span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/" aria-description="Citation for case: Gregory v. Ashcroft">501 U. S. 452</a></span> (1991), which upheld against federal statutory and Equal Protection Clause challenges Missouri’s mandatory retirement age of 70 for state judges. The Court found this age classification reasonable and not barred by the federal legislation. See <span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/#473" aria-description="Citation for case: Gregory v. Ashcroft"><em>id., </em>at 473</a></span>. States, <em><span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/" aria-description="Citation for case: Gregory v. Ashcroft">Gregory</a></span> </em>reaffirmed, enjoy wide latitude to establish conditions of candidacy for state office, but in setting such conditions, they may not disregard basic constitutional protections. See <span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/#463" aria-description="Citation for case: Gregory v. Ashcroft"><em>id., </em>at 463</a></span>; <em>McDaniel </em>v. <em>Paty, </em><span class="citation" data-id="9427133"><a href="/opinion/109831/mcdaniel-v-paty/" aria-description="Citation for case: McDaniel v. Paty">435 U. S. 618</a></span> (1978) (invalidating state provision prohibiting members of clergy from serving as delegates to state constitutional convention); <em>Communist Party of Ind. </em>v. <em>Whitcomb, </em><span class="citation" data-id="9425495"><a href="/opinion/108902/communist-party-of-indiana-v-whitcomb/" aria-description="Citation for case: Communist Party of Indiana v. Whitcomb">414 U. S. 441</a></span> (1974) (voiding loyalty oath as a condition of ballot access); <em>Bond </em>v. <em>Floyd, </em><span class="citation" data-id="107301"><a href="/opinion/107301/bond-v-floyd/" aria-description="Citation for case: Bond v. Floyd">385 U. S. 116</a></span> (1966) (Georgia Legislature could not exclude elected representative on ground that his antiwar statements cast doubt on his ability to take an oath). We are aware of no precedent suggesting that a State’s power to establish qualifications for state offices — any more than its sovereign power to prosecute crime — diminishes the constraints on state action imposed by the Fourth Amendment. We therefore reject respondents’ invitation to apply in this case a framework extraordinarily deferential to state meas<page-number citation-index="1" label="318">*318</page-number>ures setting conditions of candidacy for state office. Our guides remain <em>Skinner, Von Raab, </em>and <em>Vernonia.</em></p>
<p id="b410-5">Turning to those guides, we note, first, that the testing method the Georgia statute describes is relatively noninvasive; therefore, if the “special needs” showing had been made, the State could not be faulted for excessive intrusion. Georgia’s statute invokes the drug-testing guidelines applicable to the federal programs upheld in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>and <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>. </em>See Brief for United States as <em>Amicus Curiae </em>20-21; <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#661" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 661-662, n. 1</a></span>. The State permits a candidate to provide the urine specimen in the office of his or her private physician; and the results of the test are given first to the candidate, who controls further dissemination of the report. Because the State has effectively limited the invasiveness of the testing procedure, we concentrate on the core issue: Is the certification requirement warranted by a special need?</p>
<p id="b410-6">Our precedents establish that the proffered special need for drug testing must be substantial — important enough to override the individual’s acknowledged privacy interest, sufficiently vital to suppress the Fourth Amendment’s normal requirement of individualized suspicion. See <em>supra, </em>at 313-317 and this page. Georgia has failed to show, in justification of § 21-2-140, a special need of that kind.</p>
<p id="b410-7">Respondents’ defense of the statute rests primarily on the incompatibility of unlawful drug use with holding high state office. The statute is justified, respondents contend, because the use of illegal drugs draws into question an official’s judgment and integrity; jeopardizes the discharge of public functions, including antidrug law enforcement efforts; and undermines public confidence and trust in elected officials. Brief for Respondents 11-18. The statute, according to respondents, serves to deter unlawful drug users from becoming candidates and thus stops them from attaining high state office. <em>Id., </em>at 17-18. Notably lacking in respondents’ pres<page-number citation-index="1" label="319">*319</page-number>entation is any indication of a concrete danger demanding departure from the Fourth Amendment’s main rule.</p>
<p id="b411-5">Nothing in the record hints that the hazards respondents broadly describe are real and not simply hypothetical for Georgia’s polity. The statute was not enacted, as counsel for respondents readily acknowledged at oral argument, in response to any fear or suspicion of drug use by state officials:</p>
<blockquote id="b411-6">“QUESTION: Is there any indication anywhere in this record that Georgia has a particular problem here with State officeholders being drug abusers?</blockquote>
<blockquote id="b411-7">“[COUNSEL FOR RESPONDENTS]: No, there is no such evidence, [and] to be frank, there is no such problem as we sit here today.” Tr. of Oral Arg. 32.</blockquote>
<p id="b411-8">See also <em>id., </em>at 31 (counsel for respondents affirms absence of evidence that state officeholders in Georgia have drug problems). A demonstrated problem of drug abuse, while not in all cases necessary to the validity of a testing regime, see <em>Von </em>Raab, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#673" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 673-675</a></span>, would shore up an assertion of special need for a suspicionless general search program. Proof of unlawful drug use may help to clarify — and to substantiate — the precise hazards posed by such use. Thus, the evidence of drug and alcohol use by railway employees engaged in safety-sensitive tasks in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>, </em>see 489 U. S., at 606-608, and the immediate crisis prompted by a sharp rise in students’ use of unlawful drugs in <em>Vernonia, </em>see <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662-663</a></span>, bolstered the Government’s and school officials’ arguments that drug-testing programs were warranted and appropriate.</p>
<p id="b411-9">In contrast to the effective testing regimes upheld in <em>Skinner, Von Raab, </em>and <em>Vernonia, </em>Georgia’s certification requirement is not well designed to identify candidates who violate antidrug laws. Nor is the scheme a credible means to deter illicit drug users from seeking election to state office. The test date — to be scheduled by the candidate anytime within <page-number citation-index="1" label="320">*320</page-number>30 days prior to qualifying for a place on the ballot — is no secret. As counsel for respondents acknowledged at oral argument, users of illegal drugs, save for those prohibitively addicted, could abstain for a pretest period sufficient to avoid detection. See Tr. of Oral Arg. 44-46.<footnotemark>4</footnotemark> Even if we indulged respondents’ argument that one purpose of §21-2-140 might be to detect those unable so to abstain, see <em>id., </em>at 46, respondents have not shown or argued that such persons are likely to be candidates for public office in Georgia. Moreover, respondents have offered no reason why ordinary law enforcement methods would not suffice to apprehend such addicted individuals, should they appear in the limelight of a public stage. Section 21-2-140, in short, is not needed and cannot work to ferret out lawbreakers, and respondents barely attempt to support the statute on that ground.</p>
<p id="b412-5">Respondents and the United States as <em>amicus curiae </em>rely most heavily on our decision in <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>which sustained a drug-testing program for Customs Service officers prior to promotion or transfer to certain high-risk positions, despite the absence of any documented drug abuse problem among Service employees. 489 U. S., at 660; see Brief for Respondents 12-14; Brief for United States as <em>Amicus Curiae </em>18; see also 73 F. 3d, at 1646. The posts in question in <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span> </em>directly involved drug interdiction or otherwise required the Service member to carry a firearm. See 489 U. S., at 670 (“Government has a compelling interest in ensuring that front-line interdiction personnel are physically fit, and have unimpeachable integrity and judgment.”); <em>id., </em>at 670-671 (“[T]he public should not bear the risk that employees who may suffer from impaired perception and judgment will be promoted to positions where they may need to employ deadly force.”).</p>
<p id="b413-4"><page-number citation-index="1" label="321">*321</page-number>Hardly a decision opening broad vistas for suspicionless searches, <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span> </em>must be read in its unique context. As the Customs Service reported in announcing the testing program: “Customs employees, more than any other Federal workers, are routinely exposed to the vast network of organized crime that is inextricably tied to illegal drug use.” <em>National Treasury Employees Union </em>v. <em>Von Raab, </em><span class="citation" data-id="486563"><a href="/opinion/486563/national-treasury-employees-union-and-argent-acosta-president-chapter/#173" aria-description="Citation for case: National Treasury Employees Union and Argent Acosta,...">816 F. 2d 170, 173</a></span> (CA5 1987) (internal quotation marks omitted), aff’d in part, vacated in part, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989). We stressed that “[d]rug interdiction ha[d] become the agency’s primary enforcement mission,” <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#660" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 660</a></span>, and that the employees in question would have “access to vast sources of valuable contraband,” <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#669" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 669</a></span>. Furthermore, Customs officers “ha[dj been the targets of bribery by drug smugglers on numerous occasions,” and several had succumbed to the temptation. <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Ibid.</a></span></em></p>
<p id="b413-5">Respondents overlook a telling difference between <em>Von Raab </em>and Georgia’s candidate drug-testing program. In <em>Von Raab </em>it was “not feasible to subject employees [required to carry firearms or concerned with interdiction of controlled substances] and their work product to the kind of day-to-day scrutiny that is the norm in more traditional office environments.” <em>Id., </em>at 674. Candidates for public office, in contrast, are subject to relentless scrutiny — by their peers, the public, and the press. Their day-to-day conduct attracts attention notably beyond the norm in ordinary work environments.</p>
<p id="b413-6">What is left, after close review of Georgia’s scheme, is the image the State seeks to project. By requiring candidates for public office to submit to drug testing, Georgia displays its commitment to the struggle against drug abuse. The suspicionless tests, according to respondents, signify that candidates, if elected, will be fit to serve their constituents free from the influence of illegal drugs. But Georgia asserts no evidence of a drug problem among the State’s elected officials, those officials typically do not perform high-risk, <page-number citation-index="1" label="322">*322</page-number>safety-sensitive tasks, and the required certification immediately aids no interdiction effort. The need revealed, in short, is symbolic, not “special,” as that term draws meaning from our case law.</p>
<p id="b414-5">In <em>Von Raab, </em>the Customs Service had defended its officer drug-testing program in part as a way to demonstrate the agency’s commitment to enforcement of the law. See Brief for United States in <em>Treasury Employees </em>v. <em>Von Raab, </em>O. T. 1988, No. 86-1879, pp. 35-36. The <em>Von Raab </em>Court, however, did not rely on that justification. Indeed, if a need of the “set a good example” genre were sufficient to overwhelm a Fourth Amendment objection, then the care this Court took to explain why the needs in <em>Skinner, Von Raab, </em>and <em>Vernonia </em>ranked as “special” wasted many words in entirely unnecessary, perhaps even misleading, elaborations.</p>
<p id="b414-6">In a pathmarking dissenting opinion, Justice Brandéis recognized the importance of teaching by example: “Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example.” <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928). Justice Brandéis explained in <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span> </em>why the Government set a bad example when it introduced in a criminal proceeding evidence obtained through an unlawful Government wiretap:</p>
<blockquote id="b414-7">“[I]t is . . . immaterial that the intrusion was in aid of law enforcement. Experience should teach us to be most on our guard to protect liberty when the Government’s purposes are beneficent. Men born to freedom are naturally alert to repel invasion of their liberty by evil-minded rulers. The greatest dangers to liberty lurk in insidious encroachment by men of zeal, well-meaning but without understanding.” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#479" aria-description="Citation for case: Olmstead v. United States"><em>Id., </em>at 479</a></span>.</blockquote>
<p id="b414-8">However well meant, the candidate drug test Georgia has devised diminishes personal privacy <em>for </em>a symbol’s sake. The Fourth Amendment shields society against that state action.</p>
<p id="Am"><page-number citation-index="1" label="323">*323</page-number>III</p>
<p id="b415-3">We note, finally, matters this opinion does not treat. Georgia’s singular drug test for candidates is not part of a medical examination designed to provide certification of a candidate’s general health, and we express no opinion on such examinations. Nor do we touch on financial disclosure requirements, which implicate different concerns and procedures. See, <em>e. g., Barry </em>v. <em>City of New York, </em><span class="citation" data-id="8917405"><a href="/opinion/8927506/barry-v-city-of-new-york/" aria-description="Citation for case: Barry v. City of New York">712 F. 2d 1554</a></span> (CA2 1983) (upholding city’s financial disclosure law for elected and appointed officials, candidates for city office, and certain city employees); <em>Plante </em>v. <em>Gonzalez, </em><span class="citation" data-id="355692"><a href="/opinion/355692/kenneth-a-plante-v-larry-gonzalez-etc-jon-c-thomas-v-larry-gonzalez/" aria-description="Citation for case: Kenneth A. Plante v. Larry Gonzalez, Etc., Jon C. Thomas...">575 F. 2d 1119</a></span> (CA5 1978) (upholding Florida’s financial disclosure requirements for certain public officers, candidates, and employees). And we do not speak to drug testing in the private sector, a domain unguarded by Fourth Amendment constraints. See <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984).</p>
<p id="b415-4">We reiterate, too, that where the risk to public safety is substantial and real, blanket suspicionless searches calibrated to the risk may rank as “reasonable” — for example, searches now routine at airports and at entrances to courts and other official buildings. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 674-676</a></span>, and n. 3. But where, as in this case, public safety is not genuinely in jeopardy, the Fourth Amendment precludes the suspicionless search, no matter how conveniently arranged.</p>
<p id="b415-5">* * *</p>
<p id="b415-6">For the reasons stated, the judgment of the Court of Appeals for the Eleventh Circuit is</p>
<p id="b415-7">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b404-7"> The court also rejected equal protection and free speech pleas made by petitioners. 73 F. 3d, at 1547-1549. We hold § 21-2-140 incompatible with the Fourth and Fourteenth Amendments, and do not reach petitioners’ further pleas.</p>
</footnote>
<footnote label="2">
<p id="b405-9"> The United States, as <em>amicus curiae </em>in support of respondents, suggests that this case may have become moot because there is no continuing controversy regarding the now-completed 1994 election, and petitioners, who did not sue on behalf of a class, failed to assert in the courts below that they intended to run for a covered state office in a future election. See Brief for United States as <em>Amicus Curiae </em>9-10, n. 4. We reject the suggestion of mootness. Petitioner Chandler represented, as an officer of this Court, that he plans to run again, and counsel for the State does not contest that representation. See Tr. of Oral Arg. 4-6, 27; see also <span class="citation no-link">28 U. S. C. § 1653</span> (defective allegations of jurisdiction curable by amendment at trial or in appellate stages).</p>
</footnote>
<footnote label="3">
<p id="b407-7"> The Service’s program also required tests for individuals promoted or transferred to positions in which they would handle “classified” material. 489 U. S., at 661. The Court agreed that the Government “ha[d] a compelling interest in protecting truly sensitive information.” <em>Id,., </em>at 677. However, we did not rule on this aspect of the program, see <em>id., </em>at 677-678, <page-number citation-index="1" label="316">*316</page-number>because the record did not clarify “whether the category defined by the [regulation] encompassed] only those Customs employees likely to gain access to sensitive information," <em>id., </em>at 678.</p>
</footnote>
<footnote label="4">
<p id="b412-6"> In <em>Treasury Employees v. Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989), the applicant for promotion or transfer could not know precisely when action would be taken on the application. In contrast, the potential candidate knows from the start the timing of all relevant events.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Chapman v. United States (1961).md  (`case`, 5 assertions)

### content_page

```
---
title: "Chapman v. United States (1961)"
type: case
citation: "365 U.S. 610 (1961)"
parallel_cite: "81 S. Ct. 776; 5 L. Ed. 2d 828"
neutral_cite: 1961 U.S. LEXIS 1396
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-04-03
docket: 175
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1961-04-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Chapman v. United States (1961)"
  varies_by_point: false
  scope_note: "Landlord-cannot-consent rule remains good law; consistent with the later common-authority consent framework (Matlock) and reaffirmed in spirit by Stoner v. California and Georgia v. Randolph."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106197/chapman-v-united-states/"
  cluster_id: 106197
  opinion_id: 106197
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Progeny (third-party consent)"
related: ["[[Stoner v. California]]"]
aliases: ["Chapman v. United States"]
tags: ["case", "fourth-amendment", "consent", "third-party-consent", "landlord-tenant", "home"]
holding: "A landlord cannot give valid third-party consent to a search of premises currently leased to a tenant; a warrantless entry of the tenant's home on the landlord's authority alone violates the Fourth Amendment."
lake:
  record_id: "Chapman v. United States (1961)"
  status: verified
  projected_at: 2026-07-06
---

# Chapman v. United States (1961)

*365 U.S. 610 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Disambiguation:** This is *Chapman v. United States*, 365 U.S. 610 (1961) (landlord consent). Not to be confused with the unrelated *Chapman v. United States*, 500 U.S. 453 (1991) (LSD carrier-weight sentencing), which is not part of this corpus. A bare `[[Chapman v. United States]]` link resolves here.

## Background
Georgia officers, acting without a warrant but with the consent of the petitioner's landlord, forced open an unlocked window and searched the petitioner's rented house in his absence, finding an unregistered distillery and 1,300 gallons of mash. The landlord, on a social visit, had smelled mash and called police; before the entry he had not exercised any statutory option to forfeit the tenancy. Chapman was convicted of federal liquor-law violations on the seized evidence.

## Issue
Whether a landlord's consent can authorize a warrantless search of premises leased to and occupied by a tenant, rendering the search reasonable under the Fourth Amendment.

## Rule
No. A landlord has no right, absent an express covenant, "forcibly to enter the demised premises without the consent of the tenant," and cannot delegate such a right to police. To uphold a warrantless entry, search, and seizure on the landlord's authority "would reduce the [Fourth] Amendment to a nullity and leave [tenants'] homes secure only in the discretion of [landlords]." — 365 U.S. at 616–617 (quoting *Johnson v. United States*, 333 U.S. at 14). ^pin-617

"It follows that this search was unlawful, and since evidence obtained through that search was admitted at the trial, the judgment of the Court of Appeals must be [reversed]." — *Id.* at 618. ^pin-618

## Application
The landlord had merely entered to "view waste," but the entry was forcible (a window was forced) and its purpose was to search for distilling equipment, not to view waste; the landlord had not forfeited the tenancy and a nuisance abatement could proceed only on the solicitor-general's information. He therefore had no authority to enter or to consent, and his permission could not substitute for a warrant covering the tenant's home. The seizure was unlawful.

## Conclusion
The warrantless search authorized only by the landlord's consent violated the Fourth Amendment; the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chapman*'s rule that a landlord cannot consent to a search of the tenant's occupied premises remains good law and is consistent with the later common-authority consent doctrine (*[[United States v. Matlock]]*) and reaffirmed in principle by [[Stoner v. California]] (hotel clerk) and *[[Georgia v. Randolph]]*.

## Appears on
- [[Consent Searches]] — *Progeny ([[Consent Searches|third-party consent]])*

## Sources
- *Chapman v. United States*, 365 U.S. 610 (1961) — https://www.courtlistener.com/opinion/106197/chapman-v-united-states/ — pinpoints: 616–617, 618.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "888974599c009969", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "365 U.S. 610 (1961)", "court": "U.S. Supreme Court", "neutral_cite": "1961 U.S. LEXIS 1396", "official_citation_present": true, "parallel_cite": "81 S. Ct. 776; 5 L. Ed. 2d 828", "title": "Chapman v. United States (1961)", "year": "1961"}}
{"assertion_id": "31db59a22c88974b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A landlord cannot give valid third-party consent to a search of premises currently leased to a tenant; a warrantless entry of the tenant's home on the landlord's authority alone violates the Fourth Amendment.", "title": "Chapman v. United States (1961)"}}
{"assertion_id": "715b07579c79a7f6", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Progeny (third-party consent)", "title": "Chapman v. United States (1961)"}}
{"assertion_id": "1b790a391e19efbc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chapman v. United States (1961)"}}
{"assertion_id": "9809a925783dca64", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1961-04-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Chapman v. United States (1961)", "field_i_validity": "good_law", "scope_note": "Landlord-cannot-consent rule remains good law; consistent with the later common-authority consent framework (Matlock) and reaffirmed in spirit by Stoner v. California and Georgia v. Randolph.", "title": "Chapman v. United States (1961)", "varies_by_point": "false"}}
```

### lake record — Chapman v. United States (1961)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chapman v. United States (1961)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chapman v. United States",
    "case_name_short": "Chapman",
    "case_name_full": "Chapman v. United States",
    "input_case_name": "Chapman v. United States (1961)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-04-03",
    "year": 1961,
    "docket": "175",
    "cluster_id": 106197,
    "lead_opinion_id": 106197,
    "sibling_ids": [
      106197,
      9422156,
      9422157,
      9422158
    ],
    "absolute_url": "/opinion/106197/chapman-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 106282,
        "score": 20,
        "case_name": "Poe v. Ullman"
      },
      {
        "cluster_id": 106195,
        "score": 20,
        "case_name": "Ferguson v. Georgia"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "365 U.S. 610",
      "volume": "365",
      "reporter": "U.S.",
      "page": "610",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 776",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "776",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 828",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1396",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "365 U.S. 610",
        "volume": "365",
        "reporter": "U.S.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 776",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "776",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 828",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1396",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "365 U.S. 610",
    "official_selection": {
      "court_class": "scotus",
      "selected": "365 U.S. 610",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-617",
      "page": null,
      "quote": "--- # Chapman v. United States (1961) *365 U.S. 610 (1961)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> > **Disambiguation:** This is *Chapman v. United States*, 365 U.S. 610 (1961) (landlord consent). Not to be confused with the unrelated *Chapman v. United States*, 500 U.S. 453 (1991) (LSD carrier-weight sentencing), which is not part of this corpus. A bare `[[Chapman v. United States]]` link resolves here. ## Background Georgia officers, acting without a warrant but with the consent of the petitioner's landlord, forced open an unlocked window and searched the petitioner's rented house in his absence, finding an unregistered distillery and 1,300 gallons of mash. The landlord, on a social visit, had smelled mash and called police; before the entry he had not exercised any statutory option to forfeit the tenancy. Chapman was convicted of federal liquor-law violations on the seized evidence. ## Issue Whether a landlord's consent can authorize a warrantless search of premises leased to and occupied by a tenant, rendering the search reasonable under the Fourth Amendment. ## Rule No. A landlord has no right, absent an express covenant,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-618",
      "page": null,
      "quote": "It follows that this search was unlawful, and since evidence obtained through that search was admitted at the trial, the judgment of the Court of Appeals must be [reversed].",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1961-04-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chapman v. United States (1961)",
    "varies_by_point": false,
    "scope_note": "Landlord-cannot-consent rule remains good law; consistent with the later common-authority consent framework (Matlock) and reaffirmed in spirit by Stoner v. California and Georgia v. Randolph.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
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
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
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
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adrian Biera v. State",
          "cluster_id": 3096517,
          "cite": [
            "391 S.W.3d 204",
            "2012 WL 5199374",
            "2012 Tex. App. LEXIS 8782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. M. Santulli, LLC",
          "cluster_id": 5630495,
          "cite": [
            "29 Misc. 3d 37"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gibson",
          "cluster_id": 3975410,
          "cite": [
            "164 Ohio App. 3d 558",
            "2005 Ohio 6380",
            "843 N.E.2d 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barocio v. State",
          "cluster_id": 1426797,
          "cite": [
            "117 S.W.3d 19",
            "2003 WL 21402504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barocio, Xavier Hernandez v. State",
          "cluster_id": 2928784,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Edward Wilhelm v. John A. Boggs, Deputy, and Joseph Tanner, Deputy",
          "cluster_id": 777694,
          "cite": [
            "290 F.3d 822",
            "2002 U.S. App. LEXIS 9590",
            "2002 WL 1021362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Richardson v. State",
          "cluster_id": 2446882,
          "cite": [
            "865 S.W.2d 944",
            "1993 Tex. Crim. App. LEXIS 167",
            "1993 WL 431499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Woodberry v. State",
          "cluster_id": 1510666,
          "cite": [
            "856 S.W.2d 453",
            "1993 Tex. App. LEXIS 1887",
            "1993 WL 117161"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Broge",
          "cluster_id": 2062103,
          "cite": [
            "511 N.E.2d 1321",
            "159 Ill. App. 3d 127",
            "111 Ill. Dec. 26",
            "1987 Ill. App. LEXIS 2947"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sonja Yvette Osunegbu",
          "cluster_id": 490555,
          "cite": [
            "822 F.2d 472",
            "1987 U.S. App. LEXIS 9851"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stoner v. California",
          "cluster_id": 106777,
          "cite": [
            "11 L. Ed. 2d 856",
            "84 S. Ct. 889",
            "376 U.S. 483",
            "1964 U.S. LEXIS 1579"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Poe v. Ullman",
          "cluster_id": 106282,
          "cite": [
            "6 L. Ed. 2d 989",
            "81 S. Ct. 1752",
            "367 U.S. 497",
            "1961 U.S. LEXIS 1953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. White",
          "cluster_id": 108304,
          "cite": [
            "28 L. Ed. 2d 453",
            "91 S. Ct. 1122",
            "401 U.S. 745",
            "1971 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxwell v. State",
          "cluster_id": 2105782,
          "cite": [
            "73 S.W.3d 278",
            "2002 Tex. Crim. App. LEXIS 84",
            "2002 WL 562264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold B. Dorman v. United States",
          "cluster_id": 293653,
          "cite": [
            "435 F.2d 385",
            "140 U.S. App. D.C. 313",
            "1970 U.S. App. LEXIS 9785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODY0NjcyMDAwMDAmcz0yMzI1MzI1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106197+OR+9422156+OR+9422157+OR+9422158%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 14,
        "triage_snippet_classified": 186
      },
      "lane2_top_cited": {
        "query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODImcz0xMTIwNjI0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106197+OR+9422156+OR+9422157+OR+9422158%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158)",
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
    "complete_query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158)",
    "indexed_citing_opinions": 576,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106197,
        "count": 549,
        "count_source": "search"
      },
      {
        "opinion_id": 9422156,
        "count": 36,
        "count_source": "search"
      },
      {
        "opinion_id": 9422157,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422158,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 891,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chapman-v-united-states-1961.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU1OTA1OTMmcz00NDM0NDU4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106197+OR+9422156+OR+9422157+OR+9422158%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106197,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 249324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 3400993,
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
    "date_created": "2026-07-04T23:53:11Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:53:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:53:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:57:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:53:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chapman v. United States (1961)

```
<div>
<center><b><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U.S. 610</a></span> (1961)</b></center>
<center><h1>CHAPMAN<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 175.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 23, 1961.</center>
<center>Decided April 3, 1961.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT.
<p><i>J. Sewell Elliott</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Robert S. Erdahl</i> argued the cause for the United States. On the brief were <i>Solicitor General Rankin, Assistant Attorney General Wilkey, Beatrice Rosenberg</i> and <i>Kirby W. Patterson.</i></p>
<p>MR. JUSTICE WHITTAKER delivered the opinion of the Court.</p>
<p>Acting without a warrant but with the consent of the petitioner's landlord, Georgia law enforcement officers enteredthrough an unlocked windowand searched petitioner's rented house, in his absence, and there found and seized an unregistered "distillery" and 1,300 gallons of "mash." Soon afterward petitioner was indicted in <span class="star-pagination">*611</span> the District Court for the Middle District of Georgia for violations of the federal liquor laws.<sup>[1]</sup> He promptly moved the court for an order suppressing the use of the seized items as evidence at his impending criminal trial on the ground that they were obtained by an unlawful search and seizure. After hearing evidence, the court held that the search and seizure were lawful under federal standards and denied the motion.</p>
<p>At the subsequent trial, the evidence sought to be suppressed was offered and received, over petitioner's renewed objections. Upon that evidence, the jury found petitioner guilty, and the court sentenced him to imprisonment for a year and a day. On appeal, the Court of Appeals for the Fifth Circuit affirmed. <span class="citation" data-id="249324"><a href="/opinion/249324/elmer-samuel-chapman-v-united-states/" aria-description="Citation for case: Elmer Samuel Chapman v. United States">272 F. 2d 70</a></span>. To examine petitioner's claim that the courts below violated the standards governing admissibility of timely challenged evidence in federal courts, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./363/836/">363 U. S. 836</a></span>.</p>
<p>The relevant evidence is not controverted. It shows the following: One Bridgaman, and another, owned a dwelling house in a wooded area near the Macon, Georgia, airport, which they commonly rented through a rental agency. Understanding that the house had been rented to a new tenant, Bridgaman, on Sunday, February 16, 1958, went to the house for the purpose of inviting the tenants to attend church. Upon arrival he noted a strong "odor of mash" about the house. There was no response to his knock, and, although he tried to do so, he was unable to see into the house. He then returned to his home and, by telephone, advised the local police department of his observations. Soon afterward two local police officers, Harbin and Chance, arrived at Bridgaman's home, and the three then went to the rented <span class="star-pagination">*612</span> house. They noticed a strong odor of "whiskey mash" coming from the house. After their knock at the door failed to produce a response, they walked around the house and tried to look into it but were unable to do so because the shades were down. They found that all of the windows were locked, save one in the bathroom. The officers testified that Bridgaman told them "to go in the window and see what['s] what in there." Bridgaman's version of what he said was: "If it's what I think it is, what it smells like, yes, you can have my permission to go in." Thereupon they opened the bathroom window and, with the assistance of Bridgaman and Chance, Harbin entered the house through that opening. Upon entering the house he saw a complete and sizable distillery and 1,300 gallons of mash located in the living room. Apart from some accessories, containers and firewood, there was nothing else in the house. Harbin then called to Chance that he had found a large still and asked him "to go get some help." Chance immediately leftdropping Bridgaman at his hometo call the federal officers. While the federal officers were en route to the house, petitioner drove up, unlocked the front door, entered the house and was immediately arrested by Harbin. The federal officers soon arrived and took custody of petitioner. They also saved samples of the mash, took various pictures of the scene and then destroyed the still and its contents. Neither the state nor the federal officers had any warrant of any kind.</p>
<p>Although the decisions below were rendered prior to this Court's decision in <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>, the doctrine of that case is not here involved, as the lower courts explicitly rested their determinations on the ground that the search and seizure, though made by state officers, were valid under federal standards. Hence, the only question here is whether those determinations were correct. We believe that they were not.</p>
<p><span class="star-pagination">*613</span> The Fourth Amendment to the United States Constitution provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>Until <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>, this Court had never directly decided, but had always assumed, "that one's house cannot lawfully be searched without a search warrant, except as an incident to a lawful arrest therein" (<span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#32" aria-description="Citation for case: Agnello v. United States"><i>id.,</i> at 32</a></span>), but that case explicitly decided that "Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are . . . unlawful notwithstanding facts unquestionably showing probable cause." <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States"><i>Id.,</i> at 33</a></span>.</p>
<p>At least two decisions of this Court are closely relevant. <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>, and <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>. In the <i><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></i> case, Federal agents had received "complaints" respecting activities at a certain garage in Baltimore and decided to "investigate." As they "approached the garage they got the odor of whiskey coming from within." Looking through a small opening, they saw a number of cardboard cases. Although they had no warrant of any kind, they "broke the fastening upon a door, entered and found one hundred twenty-two cases of whiskey. No one was within the place and there was no reason to think otherwise. While the search progressed, Taylor came from his house and was put under arrest. The search and seizure were undertaken with the hope of securing evidence upon which to indict and convict him." <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#5" aria-description="Citation for case: Taylor v. United States"><i>Id.,</i> at 5</a></span>.</p>
<p><span class="star-pagination">*614</span> In condemning that search and seizure, this Court said that the officers "had abundant opportunity [to obtain a warrant] and to proceed in an orderly way even after the odor had emphasized their suspicions; there was no probability of material change in the situation during the time necessary to secure such warrant. Moreover, a short period of watching would have prevented any such possibility. . . . Prohibition officers may rely on a distinctive odor as a physical fact indicative of possible crime; but its presence alone does not strip the owner of a building of constitutional guarantees against unreasonable search." The Court concluded that "in any view, the action of the agents was inexcusable and the seizure unreasonable. The evidence was obtained unlawfully and should have been suppressed." <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States"><i>Id.,</i> at 6</a></span>.</p>
<p>In the <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> case, state narcotic agents, while in the hallway of a hotel, recognized a strong odor of burning opium coming from a particular room. Without knowing who was occupying the room, they knocked and, after some delay, the door was opened. The agents then entered the room and told the occupant "to consider [herself] under arrest because we are going to search the room." The search produced incriminating opium and smoking apparatus which was warm from recent use. The District Court refused to suppress that evidence and admitted it over defendant's objection at the trial and she was convicted. In reversing, this Court said:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. <span class="star-pagination">*615</span> Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. . . . The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.</blockquote>
<blockquote>"There are exceptional circumstances in which, on balancing the need for effective law enforcement against the right of privacy, it may be contended that a magistrate's warrant for search may be dispensed with. But this is not such a case." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S., at 13-15</a></span>.</blockquote>
<p>Here, as in that case, "No reason is offered for not obtaining a search warrant except the inconvenience to the officers and some slight delay necessary to prepare papers and present the evidence to a magistrate. These are never very convincing reasons and, in these circumstances, certainly are not enough to by-pass the constitutional requirement. No suspect was fleeing or likely to take flight. The search was of permanent premises, not of a movable vehicle. No evidence or contraband was threatened with removal or destruction, except perhaps the fumes which we suppose in time would disappear." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S., at 15</a></span>.</p>
<p>We think it must be concluded here, as it was in <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span>,</i> that "If the officers in this case were excused from the constitutional duty of presenting their evidence to a magistrate, <span class="star-pagination">*616</span> it is difficult to think of a case in which it should be required." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S., at 15</a></span>. See also <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span>; <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">357 U. S. 493</a></span>.</p>
<p>Actually, the Government does not contend in this Court that this search and seizure, as such, met the standards of the Fourth Amendment. Instead, it says: "Our position is that when the landlord, paying a social call, found good reason to believe that the leased premises were being wasted and used for criminal purposes, he had authority to enter as a matter of right and to bring officers with him for this purpose." It says that, under the common law, a landlord has an absolute right to enter the demised premises "to view waste," and that he should be able to exercise that right through law enforcement officers to whom he has delegated his authority. But it cites no Georgia or other case holding that a landlord, in the absence of an express covenant so permitting, has a right forcibly to enter the demised premises without the consent of the tenant "to view waste." And, so far as our research discloses, no Georgia case so holds.</p>
<p>The only relevant authority cited by the Government is a statement from Tiffany, Landlord and Tenant (1910 ed.), § 3. b. (2), p. 9, that "It has also been said that [the landlord] may enter to `view waste,' that is, to determine whether waste has been committed, <i>provided at least that this does not involve the breaking of windows or doors</i> . . . ."<sup>[2]</sup> (Emphasis added.) There are several answers to this contention. First, here the landlord and the officers forced open a window to gain entry to the premises. Second, "their purpose in entering was [not to view waste but] to search for distilling equipment . . . ." <i>Jones</i> v. <i>United States, supra,</i> at 500. Third, to uphold <span class="star-pagination">*617</span> such an entry, search and seizure "without a warrant would reduce the [Fourth] Amendment to a nullity and leave [tenants'] homes secure only in the discretion of [landlords]." <i>Johnson</i> v. <i>United States, supra,</i> at 14. Moreover, "it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical. . . . [W]e ought not to bow to them in the fair administration of the criminal law. To do so would not comport with our justly proud claim of the procedural protections accorded to those charged with crime." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266-267</a></span>.</p>
<p>After pointing to the fact that a Georgia statute (Title 58 Ga. Code § 106) provides that the unlawful manufacture of distilled liquor on rented premises shall work a forfeiture of the rights of the tenant, at the option of the landlord, and that another (Title 58 Ga. Code § 109) provides that use of a structure for that purpose constitutes a nuisance, the Government argues that, inasmuch as he used the demised premises for the illicit manufacture of distilled liquor, petitioner had forfeited all rights in the premises, and the landlord thus acquired the right forcibly to enter to abate the nuisance, and that he could and did delegate that right to the officers. But it is clear that, before the officers made the forcible entry, the landlord did not know that the premises were being used for the manufacture of liquor, nor had he exercised his statutory option to forfeit the tenancy for such a cause. And the Supreme Court of Georgia has held that a proceeding to abate a nuisance under § 109 "must proceed for the public on information filed by the solicitor-general of the circuit." <i>Kilgore</i> v. <i>Paschall,</i> <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/#417" aria-description="Citation for case: Kilgore v. Paschall">202 Ga. 416, 417</a></span>, <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/#521" aria-description="Citation for case: Kilgore v. Paschall">43 S. E. 2d 520, 521</a></span>.</p>
<p><span class="star-pagination">*618</span> It follows that this search was unlawful, and since evidence obtained through that search was admitted at the trial, the judgment of the Court of Appeals must be</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE BLACK concurs in the result.</p>
<p>MR. JUSTICE FRANKFURTER, concurring in the judgment.</p>
<p>Since searches and seizures play such a frequent role in federal criminal trials, it is most important that the law on searches and seizures by which prosecutors and trial judges are to be guided should be as clear and unconfusing as the nature of the subject matter permits. The course of true law pertaining to searches and seizures, as enunciated here, has notto put it mildlyrun smooth. The Court's opinion in this case is hardly calculated, I regret to say, to contribute to clarification. The reasoning by which the Court reaches its result would be warranted were <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948), still law. While the Court does not explicitly rely on it, underlying the present decision is the approach of <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>.</i> That decision was a short-lived deviation from the course of decisions preceding it and it was specifically overruled by <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span> (1950). Since the <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> case expresses the prevailing view, the decision in this case runs counter to it. The Court does rely on <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, although that case was seriously impaired by <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 66</a></span>, dissenting opinion, at 85.</p>
<p>Surely it is fair to say that the lower courts and prosecutors have a right to proceed on the assumption, on the basis of controlling decisions, that whether or not a search is "unreasonable" turns on the circumstances presented by a particular situation, as a matter of substantive determination. On that test, I find it very difficult to conclude that a police officer may not deem adequate <span class="star-pagination">*619</span> the authorization of a landlord to enter his house without a search warrant where he has solid ground for believing that his lessee is utilizing the house as an illegal distillery. It seems to me that it is not at all "unreasonable" not to charge a local police officer with knowledge of the law of Georgia regarding the power of a landlord to abate a nuisance in his house. Apart from charging a policeman with knowledge of the local law relating to landlord and tenant, he certainly would not acquire that knowledge by reading the only Georgia case to which the Court's opinion refers, <i>Kilgore</i> v. <i>Paschall,</i> <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">202 Ga. 416</a></span>, <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">43 S. E. 2d 520</a></span>, a case which deals with the procedure of a solicitor general of a Georgia circuit in abating a nuisance by an injunction and tells nothing about the remedy of self-help by a landlord.</p>
<p>In joining the Court's judgment, I do so on the basis of the views set forth in my dissents in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#594" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 594</a></span>; <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#630" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 630</a></span>; <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#155" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 155</a></span>; <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#68" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 68</a></span>. As these opinions elucidate, the Fourth Amendment incorporates a guiding history that gives meaning to the phrase "unreasonable searches and seizures" contained within it far beyond the meaning of the phrase in isolation and taken from the context of that history and its gloss upon the Fourth Amendment. The Amendment in its entirety in the setting of that history decidedly does not leave the phrase "unreasonable searches and seizures" at large.</p>
<p>MR. JUSTICE CLARK, dissenting.</p>
<p>The Constitution condemns only an <i>unreasonable</i> search. As my Brother FRANKFURTER says, that determination "turns on the circumstances presented by a particular situation."<sup>[1]</sup></p>
<p><span class="star-pagination">*620</span> As I read the record, Bridgaman had rented a house to Chapman. On a Sunday morning he called at the house to invite Chapman to church services. However, Bridgaman found Chapman gone, the house locked up and an "awful scent" of whiskey mash all over the place, including an open but empty cellar. He reported these facts to state officers and, at his suggestion, two officers accompanied him to the house. They too smelled, as the Court says, "a strong odor of `whiskey mash' coming from the house."</p>
<p>Under Georgia law, the use of premises for the manufacture or the keeping of liquor for disposition works "a forfeiture of the rights of any lessee or tenant under any lease or contract for rent . . . ."<sup>[2]</sup> Bridgaman advised the officers he was the owner of the house, had it leased out, and "instructed" officer Harbin to enter it and "see what['s] what in there." The officers found a bathroom window unlocked. Bridgaman "told" the officers "to go in the window" and assisted in "boosting" officer Harbin into the window and on into the house. Inside, the officer found a still set up for operation and 1,300 gallons of whiskey mash in the vats. There was neither household furniture nor other evidence of residential occupancy.</p>
<p>The Court sets aside Chapman's conviction on the ground that this search without a warrant was "unreasonable." For the life of me I cannot see why this is true. I agree with a unanimous Court of Appeals that "under the circumstances of the search here made by the State officers, no illegality was shown."</p>
<p>The "reasonableness" of the search hinges on the rights of the landlord under Georgia law in such a situation. <span class="star-pagination">*621</span> This Court refuses to honor the clear language of § 106, apparently because the Government "cites no Georgia or other case" holding that a landlord may, under the circumstances here, enter on his premises. Instead, it bases its reversal on <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>, and <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, involving entry by officers, unaccompanied by the landlord, into a <i>home</i> without a search warrant when there was ample time to secure one. This doctrine, established by <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948), was repudiated and specifically overruled only two years later in <i>united States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, at 66</a></span>. Furthermore, none of the cases cited by the Court involve the landlord-tenant circumstance controlling here.</p>
<p>As to Georgia law, the Court itself finds that "no Georgia case" holds that landlords have a right of entry as was exercised by Bridgaman here. It says that, first, the window was forced, second, the entry was for purposes of search and, third, affirmance would " `leave [tenants'] homes secure only in the discretion of [landlords]' " (quoting from <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson, supra</a></span></i>). The obvious answer to that is: "Chapman was a tenant no more!" The statute provided for the forfeiture of his lease at his lessor's option when he began making whiskey on the premises. And Bridgaman so elected when he directed the officers to enter the house. It was Chapman who was the trespasser, not Bridgaman. The latter was merely repossessing his property, not abating a nuisance. Therefore, § 109 of the Georgia Code, cited by the Court, has no bearing here for that statute merely provides that the Attorney General "may" abate such a nuisance. It has no reference to landlords <i>qua</i> landlords. Indeed, the officers here could have abated the nuisance without judicial help by destroying the still and all of its paraphernalia under authority of 58 Ga. Code Ann. (Cum. <span class="star-pagination">*622</span> Supp. 1958) § 207.<sup>[3]</sup> Likewise, <i>Kilgore</i> v. <i>Paschall,</i> <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">202 Ga. 416</a></span>, <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">43 S. E. 2d 520</a></span>, also cited by the Court, is entirely inapposite. That case merely holds that the special statutory authorization, under an entirely different provision of the Georgia Code, § 110, to close up "blind tigers," <i>i. e.,</i> public places of disrepute where gambling, drinking, etc., are carried on, must be brought by the Solicitor of the county wherein they are located. But even if it did hold that actions under § 109 must be brought by the Solicitor, that ruling would have no effect here, precisely because the present factual situation does not come under § 109 but under § 106 and § 207, <i>supra.</i></p>
<p>Furthermore, there was ample reason for not getting a warrant here. It was Sunday afternoon and, as the Georgia officer testified, he had "never got one on Sunday." "I don't think you can." And this was buttressed by his further statements: "Well, I didn't feel no call to get one." "The man that owned the house, he was there and he told us to go in the window and see what['s] what in there, so we went on in." This shows a complete reliance by the officers on Bridgaman's direction to enter the house. This, I say, made the search entirely reasonable and therefore valid under the Fourth Amendment.</p>
<p>Every moment of every day, somewhere in the United States, a law enforcement officer is faced with the problem of search and seizure. He is anxious to obey the rules that circumscribe his conduct in this field. It is the duty of this Court to lay down those rules with such clarity and understanding that he may be able to follow them. For some years now the field has been muddy, but today the Court makes it a quagmire. It fashions a novel rule, supporting it with an old theory long since overruled. <span class="star-pagination">*623</span> If <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> is no longer law the Court should say so. It is disastrous to law enforcement to leave at large the inconsistent rules laid down in these cases. It turns the wellsprings of democracylaw and orderinto a slough of frustration. It turns crime detection into a game of "cops and robbers." We hear much these days of an increasing crime rate and a breakdown in law enforcement. Some place the blame on police officers. I say there are others that must shoulder much of that responsibility.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation no-link">26 U. S. C. §§ 5601</span>, 5606.</p>
<p>[2]  Only ancient English cases are cited in support of the text.</p>
<p>[1]  I join in his opinion except for the last paragraph in which he concurs in the judgment of the Court.</p>
<p>[2]  58 Ga. Code Ann., § 106. Aside from eviction, there are no statutory procedural requirements as to forfeiture, the forfeit operating by virtue of § 106 at the option of the landlord.</p>
<p>[3]  Section 207 provides in pertinent part:
</p>
<p>"[W]henever said apparatus [for making liquor is] . . . found or discovered by any sheriff, . . . the same shall be summarily destroyed and rendered useless by him without any formal order of the court."</p>

</div>
```

---

## GROUP: content/cases/Chatrie v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Chatrie v. United States"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2026
date_decided: 2026-06-29
docket: 25-112
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2026-06-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chatrie v. United States
  varies_by_point: false
  scope_note: "New Binding — SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-verified 2026-07-02 (cluster 10881683 → lead opinion 11349205)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/"
  cluster_id: 10881683
  opinion_id: 11349205
  identity_checked: false
homes:
  - page: "[[Reverse-Keyword and Geofence Warrants]]"
    role: "Key — Anchor (geofence exposition home)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — geofence (cross-ref)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carpenter v. United States]]", "[[United States v. Jones]]", "[[Katz v. United States]]", "[[Smith v. Maryland]]", "[[The Warrant Requirement]]", "[[Standing to Challenge a Search]]", "[[The Exclusionary Rule]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "digital-privacy", "geofence", "location-history", "third-party-doctrine"]
holding: "Acquiring a cell-phone user's Google Location History (geofence) data is a Fourth Amendment search — there is a reasonable expectation of privacy in the record of one's phone's location, even for a short period and even when the data is held by a third party; the Court did not decide whether geofence warrants satisfy probable cause and particularity, vacating and remanding."
lake:
  record_id: Chatrie v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Chatrie v. United States

*609 U.S. ___ (2026)* (No. 25-112) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-02: cluster 10881683 → lead opinion 11349205 — see frontmatter/Sources. -->

## Background
Investigating a 2019 armed robbery of a Midlothian, Virginia credit union, police obtained a **geofence warrant** directing Google to disclose **Location History** for every device within a 150-meter radius of the bank during a roughly one-hour window around the robbery. That "reverse-location" process ultimately identified Okello Chatrie. He moved to suppress, arguing that compelling Google to produce his Location History was a warrantless Fourth Amendment search. The Fourth Circuit — on rehearing **[[Reading and Citing Cases#en-banc|en banc]]**, splitting 7–7 on whether a search occurred — affirmed the denial of suppression (136 F.4th 100), teeing up the threshold question for the Supreme Court.

## Issue
Whether the government conducts a Fourth Amendment "search" when it acquires a person's Google Location History (geofence) data — records of a cell phone's location — held by a third-party provider.

## Rule
Yes. Acquiring a cell-phone user's **Google Location History is a Fourth Amendment search**. In the Court's words: "An individual has a reasonable expectation of privacy in records about his cell phone's location, and police intrude on that constitutionally protected interest when they demand the information—even though for only a limited time, and from a third-party tech company." The protection holds **even for a limited time** and **even though a third party holds the records**. The Court rejected the argument that Location History (off by default / opt-in) is "voluntarily shared" and thus stripped of protection by the third-party doctrine, **applying and extending *[[Carpenter v. United States|Carpenter]]*** to bulk reverse-location data. *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) (slip op.). ^pin-op

Critically, the Court **did not** hold geofence warrants categorically unconstitutional. It **expressly declined** to decide whether *this* geofence warrant satisfied the Fourth Amendment's **probable-cause and [[Particularity|particularity]]** requirements, leaving that question for remand.

## Application
Police compelled Google to produce Location History for all devices in a geographic area and time window — an "all-encompassing" record of individuals' movements generated automatically and held by a third party. Under *[[Carpenter v. United States|Carpenter]]*'s logic, that acquisition invaded a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and was therefore a search; the third-party/opt-in rationale the Fourth Circuit panel had relied on did not defeat that protection.

## Conclusion
Acquiring geofence Location History is a Fourth Amendment search. The judgment was **[[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]]** for the lower courts to decide the **probable-cause and [[Particularity|particularity]]** of the geofence warrant — the question the Court left open. **Kagan, J.**, delivered the opinion of the Court, joined by Roberts, C.J., and Sotomayor, Kavanaugh, and Jackson, JJ.; Jackson, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]], joined by Sotomayor, J.; Gorsuch, J., concurred in the judgment (making the judgment **6–3**); Alito, J., dissented, joined by Thomas, J., as to Part I and by Barrett, J., as to Parts II–B, II–C–1, and II–C–2; Barrett, J., filed a separate [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** anchor on the geofence search-threshold question.
- **Doctrinal effect:** **RESOLVES** the former circuit split on whether acquiring geofence Location History is a *search* (5th Cir. *[[United States v. Smith (2024)|Smith]]* = yes; 4th Cir. [[Reading and Citing Cases#en-banc|en banc]] *Chatrie* = fractured) — **it is a search**. *[[Smith v. Maryland|Smith]]*'s further holding that geofence warrants are "modern-day general warrants" and **categorically unconstitutional** was **not** adopted; it is now the persuasive minority position feeding the **[[Reading and Citing Cases#on-remand|remanded]]** probable-cause/[[Particularity|particularity]] question — the new live frontier.
- **CL-confirm: VERIFIED (2026-07-02).** CourtListener **cluster** `10881683` **is** the genuine SCOTUS *Chatrie* (`scotus / 25-112 / 2026-06-29`); its lead opinion is `11349205`, against which the Rule quote above was matched verbatim. The earlier "corrupted object" warning was a cluster-vs-opinion ID mix-up: `10881683` is a *cluster* id, and fetching it from the `/opinions/` endpoint returns an unrelated case — use `/clusters/10881683/` or opinion `11349205` instead. See Sources.

## Appears on
- [[Reverse-Keyword and Geofence Warrants]] — *Key — Anchor (geofence exposition home)*
- [[Reasonable Expectation of Privacy]] — *Key — geofence (cross-ref)*
- [[Third-Party Doctrine & CSLI]] — *Key — Progeny / Refinement*

## Sources
- *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) — **slip opinion (PRIMARY):** https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf — decided June 29, 2026.
- SCOTUSblog case page — https://www.scotusblog.com/cases/chatrie-v-united-states/
- Justia, *Chatrie v. United States*, 609 U.S. ___ (2026) — https://supreme.justia.com/cases/federal/us/609/25-112/
- Cornell LII (Supreme Court text, No. 25-112) — https://www.law.cornell.edu/supremecourt/text/25-112
- Decision below: *United States v. Chatrie*, 136 F.4th 100 (4th Cir. 2025) (en banc) — https://www.courtlistener.com/opinion/10443725/united-states-v-okello-chatrie/
- CourtListener: *Chatrie v. United States* — https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/ — **verified 2026-07-02** (cluster 10881683 → lead opinion 11349205; case name, docket 25-112, and decision date 2026-06-29 confirmed against the cluster record and opinion text). The earlier "corrupted object" warning was a cluster-vs-opinion ID confusion: `10881683` is the **cluster** id and must not be fetched from the `/opinions/` endpoint (that resolves to an unrelated case); the lead **opinion** id is `11349205`.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "10c345d127d67f58", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Acquiring a cell-phone user's Google Location History (geofence) data is a Fourth Amendment search — there is a reasonable expectation of privacy in the record of one's phone's location, even for a short period and even when the data is held by a third party; the Court did not decide whether geofence warrants satisfy probable cause and particularity, vacating and remanding.", "title": "Chatrie v. United States"}}
{"assertion_id": "2cfed47a0d37ea98", "dimension": "support", "kind": "home_role", "locator": {"home": "Reverse-Keyword and Geofence Warrants"}, "payload": {"home": "Reverse-Keyword and Geofence Warrants", "role": "Key — Anchor (geofence exposition home)", "title": "Chatrie v. United States"}}
{"assertion_id": "6fa09fdcbedd076f", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Key — geofence (cross-ref)", "title": "Chatrie v. United States"}}
{"assertion_id": "8e30a33a27b0549b", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Key — Progeny / Refinement", "title": "Chatrie v. United States"}}
{"assertion_id": "450e558b4c99fb67", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chatrie v. United States"}}
{"assertion_id": "6cf24f81cfc9d4c8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2026-06-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Chatrie v. United States", "field_i_validity": "good_law", "scope_note": "New Binding — SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-verified 2026-07-02 (cluster 10881683 → lead opinion 11349205).", "title": "Chatrie v. United States", "varies_by_point": "false"}}
```

### lake record — Chatrie v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chatrie v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Chatrie v. United States",
    "case_name_short": "Chatrie",
    "case_name_full": "",
    "input_case_name": "Chatrie v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2026-06-29",
    "year": 2026,
    "docket": "25-112",
    "cluster_id": 10881683,
    "lead_opinion_id": 11349205,
    "sibling_ids": [
      11349205
    ],
    "absolute_url": "/opinion/10881683/chatrie-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
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
    }
  },
  "pinpoints": [
    {
      "id": "pin-op",
      "page": null,
      "quote": "when it acquires a person's Google Location History (geofence) data \u2014 records of a cell phone's location \u2014 held by a third-party provider. ## Rule Yes. Acquiring a cell-phone user's **Google Location History is a Fourth Amendment search**. In the Court's words:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-06-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chatrie v. United States",
    "varies_by_point": false,
    "scope_note": "New Binding \u2014 SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-verified 2026-07-02 (cluster 10881683 \u2192 lead opinion 11349205).",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11349205) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "audit_marker": null,
        "proposed_negative_events": 0
      },
      "lane2_top_cited": {
        "query": "cites:(11349205)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "audit_marker": null,
        "proposed_negative_events": 0
      },
      "lane3_recency": {
        "query": "cites:(11349205)",
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
    "complete_query": "cites:(11349205)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11349205,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/private/tmp/cssi-lake-s2-live-smoke-20260704/progeny/chatrie-v-united-states.jsonl"
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T14:23:50Z",
    "date_modified": "2026-07-06T13:36:12Z",
    "warnings": [
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T14:24:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T14:24:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:36:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T14:24:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chatrie v. United States (truncated)

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

                    CHATRIE v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE FOURTH CIRCUIT

       No. 25–112.     Argued April 27, 2026—Decided June 29, 2026
On May 20, 2019, a man robbed a credit union in Midlothian, Virginia.
 Local police officers learned from witness interviews and surveillance
 footage that the robber had approached the credit union from a corner
 of an adjacent church while appearing to talk on a cell phone, but they
 could not find out anything more, and the robber remained at large.
 On June 14, the police officers applied to a Virginia magistrate for a
 geofence warrant directed to Google, which would require Google to
 hand over data about the cell phones located within a 150-meter radius
 of the credit union—the so-called “geofence”—near the time of the
 crime. The application described the cell-phone location data Google
 collects through a service called Location History, which records the
 location of a user’s cell phone every two minutes or so. The application
 also explained how that cell-phone location data could help identify the
 robber, possible accomplices, or additional witnesses. The warrant de-
 scribed a three-step process that the police would follow: at step one,
 Google would produce anonymized location data for all cell phones
 within the geofence 30 minutes before to 30 minutes after the robbery;
 at step two, officers would attempt to narrow the list, and Google would
 provide additional anonymized data for that narrowed list, consisting
 of cell-phone locations both inside and outside the geofence during a
 two-hour period surrounding the robbery; and at step three, officers
 would further narrow the list, and Google would turn over identifying
 information, including names and phone numbers, for users on the fi-
 nal list. The magistrate issued the warrant, and through this process,
 Google ultimately produced three cell-phone users’ identifying infor-
 mation, including petitioner Okello Chatrie, whose location data
 showed that he entered the geofence about ten minutes before the rob-
 bery and headed toward a residential area immediately after leaving
2                     CHATRIE v. UNITED STATES

                                  Syllabus

    the bank.
       Following further police work, a federal grand jury charged Chatrie
    with robbery and related firearms offenses, and he moved to suppress
    the information the police obtained from Google. According to Chatrie,
    the officers had acquired that data through a Fourth Amendment
    search, and the warrant ostensibly authorizing that search was inva-
    lid. The District Court found that the geofence warrant “plainly vio-
    lates the rights enshrined in [the Fourth] Amendment” but denied the
    motion based on the good-faith exception to the exclusionary rule. 590
    F. Supp. 3d 901, 905, 937–938. A divided panel of the Fourth Circuit
    affirmed on different reasoning, holding that no search occurred be-
    cause Chatrie “did not have a reasonable expectation of privacy in two
    hours’ worth of Location History data voluntarily exposed to Google.”
    107 F. 4th 319, 325. The Fourth Circuit granted rehearing en banc
    and affirmed in a one-sentence per curiam, with the court dividing
    evenly on whether a Fourth Amendment search had occurred. This
    Court granted certiorari solely on the question whether the police vio-
    lated the Fourth Amendment in obtaining Chatrie’s location data.
Held: Police officers conducted a Fourth Amendment search when they
 acquired Chatrie’s location data from Google because an individual has
 a reasonable expectation of privacy in his cell-phone location infor-
 mation. Pp. 10–33.
    (a) The Fourth Amendment protects individuals’ reasonable expec-
 tations of privacy, and governmental “intrusion into that private
 sphere generally qualifies as a search.” Carpenter v. United States,
 585 U. S. 296, 304. The Amendment’s “basic purpose” is “to safeguard
 the privacy and security of individuals against arbitrary invasions by
 governmental officials,” id., at 303, and it was designed “to place ob-
 stacles in the way of a too permeating police surveillance,” United
 States v. Di Re, 332 U. S. 581, 595. Pp. 10–29.
      (1) In Carpenter, this Court held that accessing cell-site location
 information (CSLI) constitutes a Fourth Amendment search because
 “individuals have a reasonable expectation of privacy in the whole of
 their physical movements,” 585 U. S., at 310. The Court reasoned that
 CSLI provides a “detailed” and “encyclopedic” portrait of a person’s
 whereabouts, id., at 309, and, with that, “an intimate window into a
 person’s life,” id., at 311. Because people “compulsively carry” their
 cell phones “all the time,” the Court explained, a cell phone “tracks
 nearly exactly the movements of its owner,” and thus “faithfully fol-
 lows” him not only through “public thoroughfares [but] into private
 residences, doctor’s offices, political headquarters, and other poten-
 tially revealing locales.” Ibid. The Court further observed that the
 “newfound tracking capacity” that CSLI gives the police “runs against
 everyone”—not just those “under investigation”—and “travel[s] back
                     Cite as: 609 U. S. ___ (2026)                      3

                               Syllabus

in time,” making possible a form of surveillance that would have been
unknown prior to the digital age, id., at 311–312. Carpenter accord-
ingly held that “[a]llowing government access to cell-site records con-
travenes” expectations of privacy. Id., at 311. Pp. 13–15.
     (2) Everything Carpenter relied on to find that law enforcement
officers conducted a Fourth Amendment search when they accessed
CSLI records applies as well or better to the police’s accessing of Loca-
tion History data. First, Location History provides an even more fine-
tuned picture of a person’s movements, pinpointing location within
around twenty meters rather than within sectors of one-eighth to four
square miles; it records location every two minutes or so for a daily
average of 720 chartings rather than 101; and it can estimate elevation
to reveal which floor of a building a phone is on. Second, Location His-
tory allows police to reconstruct “retrospective[ly],” and with no real
effort, people’s comings and goings in any area, enabling “tireless and
absolute surveillance” of any number of people in any number of
places. Carpenter, 585 U. S., at 312. And third, Location History im-
plicates personal privacy interests even more than CSLI, because Lo-
cation History is more the cell-phone user’s own. Most cell-phone users
have no awareness of CSLI records, and would never try to retrieve
them; by contrast, Google users regularly employ Location History as
a personal journal. In that way, Location History resembles other pri-
vate materials—e.g., emails, documents, photographs, or calendars—
that even if stored on Google’s servers, a user reasonably views as his
own and expects to be shielded from the “inquisitive eyes” of the gov-
ernment. Id., at 305. Pp. 16–18.
     (3) The Government’s argument that accessing only a short
amount of cell-phone location information does not count as a Fourth
Amendment search fails. “[E]ven short-term monitoring” can provide
“a wealth of detail about [a person’s] familial, political, professional,
religious, and sexual associations,” United States v. Jones, 565 U. S.
400, 415, and this Court has never understood Fourth Amendment
protections as kicking in only once an intrusion “goes too far,” Pennsyl-
vania Coal Co. v. Mahon, 260 U. S. 393, 415. Where the Fourth
Amendment applies, it applies regardless of “the quality or quantity of
information” the government obtains. Kyllo v. United States, 533 U. S.
27, 37. That approach makes all the more sense when, as with Loca-
tion History, law enforcement officials can select the time-limited set
of materials they want from an all-encompassing database. Pp. 18–23.
     (4) The Government argues that the so-called third-party doctrine
precludes Chatrie from invoking the Fourth Amendment’s protections.
The idea is that in “authoriz[ing] Google to collect, retain, and use” his
location information, Chatrie lost his legitimate expectation of privacy,
and therefore his right to complain of a search. Brief for United States
4                     CHATRIE v. UNITED STATES

                                  Syllabus

    15. But Carpenter refused to apply the third-party doctrine to CSLI,
    and no good reason exists to reach a different result for Location His-
    tory. In Carpenter, the Court rejected application of the third-party
    doctrine to CSLI because such information is “qualitatively different”
    from “telephone numbers and bank records,” 585 U. S., at 309—it is
    incomparably “revealing” and is “not truly ‘shared’ as one normally un-
    derstands the term” given that cell phones are “indispensable to par-
    ticipation in modern society,” id., at 315. Both differentiating features
    apply equally or better to Location History, which is even more “re-
    vealing” than CSLI and is “not truly shared” in the normal sense of
    wanting a third party to see or use it. Id., at 315. The exposure of that
    information to Google is merely what happens when a user avails him-
    self of one of the services on his cell phone. The Government’s argu-
    ment that generating Location History, unlike producing CSLI, is a
    voluntary choice is meritless. That argument ignores how and why
    Google users turn on Location History: Google repeatedly prompts us-
    ers to turn on the service, often warning that devices will not “work
    correctly” otherwise, 2 App. 140–141, while not disclosing in that
    prompt how frequently users’ location information would be recorded,
    how precise it would be, or how it might be given to the government.
    More generally, an app-by-app, feature-by-feature method of granting
    Fourth Amendment protection misapprehends the nature of modern
    cell-phone use, where nearly everything requires some kind of “affirm-
    ative act” beyond “powering up” a given app or service. The Govern-
    ment wishes to disconnect the activities people do on their cell phones
    from the mere act of carrying a turned-on cell phone (the thing that
    generates CSLI), with only the latter receiving assured Fourth Amend-
    ment protection. But the point of carrying smartphones is to use what
    is on them—as Carpenter said, to use the apps and “services they pro-
    vide.” 585 U. S., at 315. Accordingly, a cell-phone user is not to be
    viewed as sharing private information with third parties—which then
    can be freely passed on to the government—just by doing the ordinary
    things cell-phone users do. Pp. 24–29.
       (b) The conclusion that a Fourth Amendment search occurred does
    not resolve this case, because the Fourth Amendment prohibits only
    searches that are “unreasonable.” When law enforcement officials un-
    dertake a search to discover evidence of a crime, the reasonableness
    standard generally requires that they seek a warrant from “a neutral
    and detached magistrate,” Johnson v. United States, 333 U. S. 10, 14,
    who may issue a warrant only when “probable cause is properly estab-
    lished and the scope of the authorized search is set out with particu-
    larity,” Kentucky v. King, 563 U. S. 452, 459. The warrant issued here,
    as described earlier, was an uncommon, multi-step one, and the par-
    ties have contested the legality of each stage of the search process it
                      Cite as: 609 U. S. ___ (2026)                      5

                                Syllabus

  authorized. The Fourth Circuit did not address the questions that un-
  usual warrant raises. Because this is “a court of review, not of first
  view,” Cutter v. Wilkinson, 544 U. S. 709, 718, n. 7, the Court leaves it
  up to the Court of Appeals to decide whether, at each step of the search
  process, the warrant satisfied the Fourth Amendment’s requirements
  of particularity and probable cause. Pp. 29–32.
136 F. 4th 100, vacated and remanded.

   KAGAN, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SOTOMAYOR, KAVANAUGH, and JACKSON, JJ., joined. JACKSON, J.,
filed a concurring opinion, in which SOTOMAYOR, J., joined. GORSUCH, J.,
filed an opinion concurring in the judgment. ALITO, J., filed a dissenting
opinion, in which THOMAS, J., joined as to Part I, and in which BARRETT,
J., joined as to Parts II–B, II–C–1, and II–C–2. BARRETT, J., filed a dis-
senting opinion.
                        Cite as: 609 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 25–112
                                   _________________


           OKELLO T. CHATRIE, PETITIONER v.
                   UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                                 [June 29, 2026]

   JUSTICE KAGAN delivered the opinion of the Court.
   In recent years, law enforcement officers have employed
so-called geofence warrants to obtain information that tech-
nology companies collect about their users’ cell-phone loca-
tions. Suppose that investigators know a crime was com-
mitted at a particular place and time, but do not have a
suspect. They may draw a “geofence”—a virtual perime-
ter—around the crime scene and get a warrant compelling
a company to hand over data about the cell phones located
in that area near the time of the crime. Following a process
specified in the warrant, the company will turn over the
cell-phone data and eventually identify by name one or
more of the users thus disclosed.
   The geofence warrant at issue here was directed to
Google, and used to solve a bank robbery. Hundreds of mil-
lions of Google users have activated a service called Loca-
tion History, which records the location of a user’s cell
phone every two minutes or so. Through a geofence war-
rant, police officers required Google to turn over Location
History data revealing cell phones within the vicinity of a
bank at around the time it was robbed. At the end of the
multi-step process described in the warrant, Google gave
2               CHATRIE v. UNITED STATES

                     Opinion of the Court

the police three names. The Federal Government soon
charged one of the individuals thus identified, petitioner
Okello Chatrie, with committing the crime.
   Today, we consider how the Fourth Amendment applies
to that use of a geofence warrant. Answering that question
in full would mean deciding whether the police conducted a
Fourth Amendment “search” when they acquired the cell-
phone data leading to Chatrie’s arrest and, if so, whether
that search was reasonable given the features of the war-
rant they employed. We decide the first part of that inquiry
today, concluding that the police conducted a search when
they gained access to Location History data. An individual
has a reasonable expectation of privacy in records about his
cell phone’s location, and police intrude on that constitu-
tionally protected interest when they demand the infor-
mation—even though for only a limited time, and from a
third-party tech company. We leave to the Court of Appeals
the further question whether, given the warrant issued, the
search here was reasonable, meaning that each of its steps
was properly described with particularity and found to be
supported by probable cause.
                            I
                            A
  Modern cell phones, we observed a dozen years ago, are
“such a pervasive and insistent part of daily life that the
proverbial visitor from Mars might conclude they were an
important feature of human anatomy.” Riley v. California,
573 U. S. 373, 385 (2014). Since then, the percentage of
Americans who own smartphones has only increased. To-
day, more than nine in ten Americans own a smartphone.
See W. Bishop, Pew Research Center, Mobile Fact Sheet
(Nov. 20, 2025) (91%); compare A. Smith, Pew Research
Center, Smartphone Ownership—2013 Update (June 5,
2013) (56%). That means they are likely addicted to apps
and other services, many of which collect and store
                    Cite as: 609 U. S. ____ (2026)                   3

                         Opinion of the Court

“detailed information about all aspects of a person’s life.”
Riley, 573 U. S., at 396.
  Among that information is a single fact most pertinent
here: where the user’s cell phone is located at a given time.
Apps of many kinds rely on that datum. Your maps app
wants to help you navigate from Point A (where you are) to
Point B (where you are going). Ride-sharing apps of course
track your location when you are using them, and often do
so even when you are not. Weather apps want to tell you
about local conditions. Fast-food apps want to identify the
closest burger and pizza joints. Fitness apps want to track
your running routes. And so on.
  This case concerns a form of cell-phone location data
called “Location History,” which Google apps collect and
store.1 Location History is what it sounds like—a time-
stamped record of every place a cell phone has been. Every
two minutes or so, Location History draws from an array of
sources to log a cell phone’s location. Those sources include
nearby Wi-Fi networks, Bluetooth beacons, and cell sites,
as well as GPS and IP address information. When com-
bined, the signals tracked can determine a cell phone’s lo-
cation within 20 meters. They can also ascertain a phone’s
elevation, and thus reveal which floor within a building the
phone is on. By all accounts, those features make Location
History “the most sweeping, granular, and comprehensive
tool” existing today for collecting and storing location data.
590 F. Supp. 3d 901, 907 (ED Va. 2022).
  Google repeatedly prompts users to enable Location His-
tory, and over 500 million users worldwide have done so.
The first prompt comes when a user initially establishes a
Google account. If that spur is ignored, another will arrive
when a user sets up a Google app—like Google Assistant,
——————
  1 Throughout this opinion, we describe how Location History worked at

the time the warrant at issue was executed. As noted below, Google has
since then instituted a significant change, which apparently insulates
Location History data from geofence warrants. See infra, at 4, n. 2.
4                  CHATRIE v. UNITED STATES

                         Opinion of the Court

Google Maps, or Google Photos—on his phone or other de-
vice. Android (though not iPhone) users are specifically
warned that their devices will not “work correctly” unless
they turn on Location History. 2 App. 140–141. And once
a user does so, the service runs—and runs constantly—in
the background. Regardless whether the user has a Google
app open—or whether he is using his phone at all—Loca-
tion History remains active. Indeed, it continues to work
even if the user deletes the app through which he first
turned it on. Location History stops only if a user affirma-
tively stops it. Sans that intervention, it tracks and tracks
and tracks a user’s cell phone (and other devices).
   Google stores all Location History data in the cloud, ra-
ther than on a user’s device—though that choice makes no
real difference to the user. “Cloud computing” refers to “the
capacity of Internet-connected devices to display data
stored on remote servers rather than on the device itself.”
Riley, 573 U. S., at 397. Because it exists, Google can store
information on its own servers, while the user can view it
as if stored on his cell phone. Such remote storage, we have
explained, is common: “Cell phone users often may not
know whether particular information is stored on the device
or in the cloud, and it generally makes little difference.”
Ibid. So, for example, Google usually stores users’ emails,
documents, and photographs on company servers instead of
on individual devices. See Brief for Google LLC as Amicus
Curiae 3, 37–38. And the same is true of the information
generated by Location History, which is stored in a single
central repository on Google’s servers.2 That data exists
someplace remote, but a user sees it—and the content
——————
   2 Except that in July 2025, years after the geofence warrant used in

this case, Google made a change: It now stores Location History data on
individual users’ devices rather than on its own servers. See Brief for
Google LLC as Amicus Curiae 2. Google represents that, as a result, it
is no longer capable of responding to geofence warrants that seek Loca-
tion History data. See ibid.
                 Cite as: 609 U. S. ____ (2026)            5

                     Opinion of the Court

Google creates from it—in the palm of his hand. The user
thus can access a “Timeline” showing where he has traveled
when; receive real-time updates about his daily commute;
and take advantage of maps and recommendations based
on his usual movements.
                              B
   In the last decade, Google’s Location History data has
also served another function, though this one unknown to
most users: That data, as obtained through a geofence war-
rant, can enable law enforcement officers to solve hard-to-
solve crimes. Such a warrant, as earlier described, seeks
information about the cell phones located in the vicinity of
a crime scene at around the time the crime was committed.
See supra, at 1. The goal, put simply, is to find out who was
there and so who might have done it. (There are usually
better ways to investigate an already-known suspect—like
seeking only his location data.) And the mechanism is to
use the offender’s cell phone as an identifying device. The
warrant specifies a timeframe and maps an area (with the
geofence as its perimeter), and demands information about
the cell phones—and their users—present within it. There
is some uncertainty about how often the technique in fact
works. See Brief for Orin S. Kerr as Amicus Curiae 14 (Kerr
Brief ). But its use among law enforcement officers has
flourished. Google received its first geofence warrant in
2016. See 590 F. Supp. 3d, at 914. Two years later, it re-
ceived 982; and two years after that, more than 11,000. See
Google, Supplemental Information on Geofence Warrants
in The United States (Aug. 2021), https://services.google.
com/fh/files/misc/supplemental_information_geofence_war-
rants_united_states.pdf (archived at https://perma.cc/
LN4P-KQJA). Though the details vary, each has made the
6                   CHATRIE v. UNITED STATES

                          Opinion of the Court

same essential demand: Tell us, through cell-phone location
data, who was there when a crime happened.3
   As those demands began to proliferate, Google worked
with law enforcement officials to develop a three-step pro-
tocol to govern geofence warrants. At the first step, Google
produces anonymized (i.e., no names attached) location
data for all cell phones (or other devices) within the
geofence—typically, a circle with a designated radius sur-
rounding a latitude/longitude coordinate—during a speci-
fied timeframe. That data generally includes each phone’s
latitude/longitude       coordinate    and      corresponding
timestamp; an estimate of that information’s accuracy; and
a description of the information’s source (e.g., a Wi-Fi net-
work, a cell site, or some other). The data at this stage
shows each user’s location, every two minutes or so, within
the geofence. At the second step of the process, officials re-
view the data produced and typically ask Google to provide
additional information for a subset of still-anonymized us-
ers. That new data is usually for a longer timeframe than
first specified; it also shows the user’s location outside, as
well as inside, the geofence. Finally, at the third step, offi-
cials demand the identities of a further subset of users—
their names, email addresses, and phone numbers. Thus,
the geofence warrant is designed to eventually produce a
select number of identified users suspected of committing
the crime under investigation.
                             C
  On May 20, 2019, at about 4:50 p.m., a man robbed a
credit union in Midlothian, Virginia. The robber presented
a teller with a handwritten note demanding $100,000,
——————
  3 Google is not the only tech company that has received geofence war-

rants; so have Apple, Lyft, Snapchat, and Uber, among others. See 136
F. 4th 100, 102, n. 1 (CA4 2025) (en banc) (Diaz, C. J., concurring). But
Google is the “most common recipient and the only one known to re-
spond.” Ibid.
                 Cite as: 609 U. S. ____ (2026)            7

                     Opinion of the Court

threatening to hurt her and her family if she did not com-
ply, and warning her that he had “boys on the lookout out
side.” 590 F. Supp. 3d, at 905–906. When the teller replied
that she did not have access to that amount of money, the
robber brandished a firearm. He ordered everyone in the
bank to the ground, and forced the bank’s manager to open
a safe and put $195,000 into a bag. The robber then left on
foot with the money.
   Local police officers responded to the scene and began an
investigation. They learned, from witness interviews and
surveillance-camera footage, that the robber had ap-
proached the credit union from a corner of an adjacent
church, while appearing to talk on a cell phone. But they
could not find out anything more, and the robber remained
at large.
   On June 14, the police officers thus applied to a Virginia
magistrate for a geofence warrant directed to Google. The
application described the cell-phone location data Google
collects, and explained how that data could lead to identify-
ing the robber, his possible accomplices, or additional wit-
nesses to the crime. Success was particularly likely here,
the application stated, because the robber appeared to be
using his phone when he entered the credit union, and may
even have been speaking with an accomplice. The officers’
proposed geofence was a circle with a radius of 150 meters
surrounding the credit union.
   The warrant application went on to describe the three-
step process that the police would follow to obtain the loca-
tion information sought. At step one, Google would produce
anonymized location data for all cell phones within the
geofence in the hour between 4:20 and 5:20 p.m. (30
minutes before to 30 minutes after the robbery). At step
two, police officers would “attempt to narrow down the list
[of devices] by reviewing the time stamped location coordi-
nates for each [device] and comparing that against the
known time and location information that is specific to this
8                CHATRIE v. UNITED STATES

                      Opinion of the Court

crime.” 2 App. 136. For that narrowed list, Google would
provide additional (but still anonymized) data—cell-phone
locations both inside and outside the geofence during a two-
hour period (so now from 3:50 to 5:50 p.m.). Finally, at step
three, police would again “attempt to narrow down the list
by comparing this additional information regarding travel
and time against the known time and location information
that is specific to this crime.” Id., at 137. And Google would
then turn over identifying information for each user on the
final list, including his name and phone number.
   The magistrate issued the warrant, and officers executed
it in the manner prescribed. At the first stage of the pro-
cess, Google gave up anonymized data for 19 users found
within the geofence during the hour within which the rob-
bery occurred. At the second stage, the officers winnowed
the list to nine users. And Google produced anonymized
data showing their movements both inside and outside the
geofence for the extended two-hour period. At the third and
last step, the police again narrowed the list, this time to
three users. Google responded with their identifying infor-
mation. One of the three was Chatrie. The location data
showed that he entered the geofenced area about ten
minutes before the robbery, and headed toward a residen-
tial area of town immediately after leaving the bank.
   Following further police work, a federal grand jury
charged Chatrie with robbery and related firearms of-
fenses. He moved to suppress the information that the po-
lice had obtained from Google. According to Chatrie, the
officers had acquired that data through a Fourth Amend-
ment search, and the warrant ostensibly authorizing that
search was invalid.
   The District Court mainly agreed with Chatrie’s Fourth
Amendment analysis, but still denied the motion to exclude
the Location History evidence. Even though “this particu-
lar geofence warrant plainly violates the rights enshrined
in [the Fourth] Amendment,” the court stated, the officers’
                  Cite as: 609 U. S. ____ (2026)             9

                      Opinion of the Court

reliance on it was not “objectively unreasonable.” 590
F. Supp. 3d, at 905, 938. And because that was so, the court
concluded, the good-faith exception to the exclusionary rule
permitted admission of the location data. See id., at 937–
938; United States v. Leon, 468 U. S. 897, 922–923 (1984)
(establishing good-faith exception).
   A divided panel of the Court of Appeals of the Fourth Cir-
cuit affirmed, but on different reasoning. The majority held
that the government did not conduct a search and therefore
did not need a warrant. That was so, the majority reasoned,
because Chatrie “did not have a reasonable expectation of
privacy in two hours’ worth of Location History data volun-
tarily exposed to Google.” 107 F. 4th 319, 325 (2024). Judge
Wynn dissented, arguing that “the police intrusion into
Chatrie’s Location History data” was “a search that trig-
gered the Fourth Amendment’s protections,” and that the
warrant issued was “so lacking in particularity and proba-
ble cause that it was invalid.” Id., at 339, 362, and n. 12.
   After granting rehearing en banc, the Fourth Circuit af-
firmed in a one-sentence per curiam. See 136 F. 4th 100,
101 (2025) (“The judgment of the district court is
AFFIRMED”). In multiple accompanying writings, the
court divided evenly (7 to 7) on whether a Fourth Amend-
ment search had occurred. Of the seven judges who thought
it had, most believed the geofence warrant defective. But
most also thought the exclusionary rule’s good-faith excep-
tion applied, so ruled against Chatrie anyway.
   We granted certiorari solely on the question whether the
police violated the Fourth Amendment in obtaining Cha-
trie’s location data, thus declining to consider the exclusion-
ary rule issue. See 607 U. S. 1148 (2026). The disputed
Fourth Amendment question divides into two parts. First,
did law enforcement officials conduct a search under the
Fourth Amendment when they acquired Chatrie’s location
data from Google? We hold that they did because an indi-
vidual has a legitimate expectation of privacy in his cell-
10                   CHATRIE v. UNITED STATES

                           Opinion of the Court

phone location data. Second, did the multi-step geofence
warrant issued here make that search reasonable? We
leave that question—which requires deciding whether the
warrant satisfied the Fourth Amendment’s probable cause
and particularity requirements at each stage of the search
process—to the Court of Appeals to address in the first in-
stance.4
                            II
  The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” The “basic
purpose” of that Amendment, our precedents say, is “to
——————
   4 In line with our grant of certiorari, we do not address whether the

good-faith exception to the exclusionary rule still allows the admission of
the Location History data in this case. That question remains for the
Fourth Circuit to consider anew, gleaning anything it thinks relevant
from our decision on the substantive Fourth Amendment issues.
   The principal dissent seeks to rehash our limited grant of certiorari,
but we see no reason to doubt it. We have Article III jurisdiction in this
case, as even the dissent concedes. See post, at 4, n. 2 (ALITO, J.). That
is because the Fourth Circuit is free to revisit the exclusionary rule issue
in light of our opinion and to provide Chatrie with relief. See Chafin v.
Chafin, 568 U. S. 165, 172 (2013) (Article III jurisdiction disappears only
when it becomes “impossible for the court to grant any effectual relief
whatever to the prevailing party”). So what does the dissent mean when
it continually labels this opinion “advisory” (post, at 1, 2, 4, 5, 6, 7)—a
term customarily used to describe opinions lacking a jurisdictional basis?
Apparently, the dissent’s objection is that we today decide a question in-
volving the Fourth Amendment when the odds are strong (so says the
dissent) that the Fourth Circuit will eventually, as it did before, resolve
this case on exclusionary rule grounds. But to repeat, the Fourth Circuit
may now consider anew, after review of our opinion, how the good-faith
exception applies here. And the very decision establishing that exception
held that courts should feel free to “resolv[e] the Fourth Amendment is-
sue” before the good-faith issue, either to better assess good faith or “to
guide future action by law enforcement officers and magistrates.” United
States v. Leon, 468 U. S. 897, 925 (1984). So contra the dissent, there is
nothing advisory (or otherwise improper) in today deciding the Fourth
Amendment issue on which we previously granted certiorari.
                      Cite as: 609 U. S. ____ (2026)                    11

                          Opinion of the Court

safeguard the privacy and security of individuals against
arbitrary invasions by governmental officials.” Carpenter
v. United States, 585 U. S. 296, 303 (2018) (quoting Camara
v. Municipal Court of City and County of San Francisco, 387
U. S. 523, 528 (1967)).
   That purpose is central to decisions about whether a
Fourth Amendment “search” has occurred. Our early
search doctrine focused on whether law enforcement offi-
cials “obtain[ed] information by physically intruding”—that
is, trespassing—on private property. United States v.
Jones, 565 U. S. 400, 406–407, n. 3 (2012); see id., at 404–
405. But the Court in Katz v. United States, 389 U. S. 347,
351 (1967), recognized that “the Fourth Amendment pro-
tects people, not places.” And so we have long held that
“property rights are not the sole measure” of a constitu-
tional violation; the Fourth Amendment “protect[s] certain
expectations of privacy as well.” Soldal v. Cook County, 506
U. S. 56, 64 (1992); Carpenter, 585 U. S., at 304. “When an
individual seeks to preserve something as private and his
expectation of privacy is one that society is prepared to rec-
ognize as reasonable,” then governmental “intrusion into
that private sphere generally qualifies as a search.” Ibid.5
——————
   5 The dissent suggests that this Court has tried to curtail Katz ever

since deciding it, see post, at 10–11 (ALITO, J.); more energetically, the
concurrence advocates overthrowing Katz and reverting to a solely prop-
erty-based approach, see post, at 1–2, 4 (GORSUCH, J., concurring in judg-
ment). But this Court has faithfully applied Katz for some 60 years. Our
decision in Carpenter v. United States, 585 U. S. 296 (2018), responded
to the same arguments made today (see, e.g., id., at 391–397 (GORSUCH,
J., dissenting)) by reaffirming that Katz had “discredited the premise
that property interests control” and that “privacy interests do not rise or
fall with property rights.” 585 U. S., at 304, n. 1. And in saying as much,
Carpenter had plenty of other decisions to cite. See, e.g., United States
v. Jones, 565 U. S. 400, 411 (2012) (refusing to “make trespass the exclu-
sive test”); Kyllo v. United States, 533 U. S. 27, 32 (2001) (stating that
the Court has “decoupled violation[s] of a person’s Fourth Amendment
rights from trespassory violation of his property”). Of course, sometimes
the privacy and property approaches will “align,” and an opinion
12                  CHATRIE v. UNITED STATES

                          Opinion of the Court

   Whether an expectation of privacy counts as legitimate is
less the result of any fixed set of rules than of “guideposts”
stretching back to the Fourth Amendment’s beginnings.
Id., at 305. From the founding onward, we have explained,
the Fourth Amendment has sought to secure the “privacies
of life” against the exercise of “arbitrary power.” Boyd v.
United States, 116 U. S. 616, 630 (1886); see Carpenter, 585
U. S., at 305. So too we have recognized, and repeatedly,
that the Amendment was designed “to place obstacles in the
way of a too permeating police surveillance.” United States
v. Di Re, 332 U. S. 581, 595 (1948); Carpenter, 585 U. S., at
305. Whatever the form of an attempted incursion, the
Fourth Amendment protects Americans’ long-held convic-
tion that no government official should have free access to
the most closely kept aspects of their lives.
   In recent decades, this Court has often confronted the
challenge of adhering to those principles in the face of new
technologies. “[I]nnovations in surveillance tools” have “en-
hanced the Government’s capacity to encroach upon areas
normally guarded from inquisitive eyes.” Ibid. The Court,
in response, has sought to “assure[ ] preservation of that de-
gree of privacy against government that existed when the
Fourth Amendment was adopted.” Kyllo v. United States,
533 U. S. 27, 34 (2001). So in one decision, we rejected a
“mechanical interpretation” of the Fourth Amendment to
hold that the use of a thermal imager to detect heat coming
——————
adopting the one will resemble, in whole or part, an opinion adopting the
other. Florida v. Jardines, 569 U. S. 1, 13 (2013) (KAGAN, J., concurring).
That is not because the privacy-based approach is groping toward the
more “coheren[t]” property-based one, as the concurrence suggests. Post,
at 8 (GORSUCH, J.). It is simply because property law “naturally enough
influence[s]” our “shared societal expectations” of what places and things
count as private and should be free from governmental intrusion. Geor-
gia v. Randolph, 547 U. S. 103, 111 (2006); see Carpenter, 585 U. S., at
304, n. 1 (“[P]roperty rights are often informative” in “determining which
expectations of privacy are legitimate”). And when such an alignment of
the two approaches occurs, then all the better.
                 Cite as: 609 U. S. ____ (2026)           13

                     Opinion of the Court

from a person’s home was a search in the constitutional
sense. Id., at 35. And in another, we held that the search
of a cell phone incident to arrest could not proceed without
a warrant (even though the search of a handbag could) be-
cause of the phone’s “vast quantities of personal infor-
mation.” Riley, 573 U. S., at 386. Most recently, in Carpen-
ter v. United States, this Court held that accessing a form
of cell-phone location information other than Location His-
tory is a Fourth Amendment search given individuals’ rea-
sonable expectations of privacy. See 585 U. S., at 310–313.
   We begin with Carpenter in considering the Govern-
ment’s front-line position here: that no warrant was needed
to get Location History data from Google (although the po-
lice “prophylactically secured” one) because no Fourth
Amendment search ever took place. See Brief for United
States 14. We then explain why the result we reached in
Carpenter once again follows. Contrary to the Govern-
ment’s view, an individual has a legitimate expectation of
privacy in the information Location History collects about
his cell phone’s—meaning his own—movements. The police
invade that expectation, and thus conduct a search, when
they acquire that information, even though for only a lim-
ited period of time and even though via a third-party tech
company.
                              A
  The question presented in Carpenter was “whether the
Government conducts a search under the Fourth Amend-
ment when it accesses historical cell phone records that pro-
vide a comprehensive chronicle of the user’s past move-
ments.” 585 U. S., at 300. The cell-phone records at issue
were what is known as cell-site location information (CSLI).
As we explained, CSLI is a “time-stamped record” gener-
ated each time a cell phone connects to a cell site. Id., at
301. Wireless carriers collect and store that information for
their own business purposes (such as finding weak spots in
14                 CHATRIE v. UNITED STATES

                         Opinion of the Court

their networks). But CSLI can also benefit law enforce-
ment, because it identifies an individual’s approximate lo-
cation every time his phone makes a connection. In Car-
penter, police officers investigating a string of Radio Shack
robberies ordered a wireless carrier of a known suspect to
turn over his CSLI records for a seven-day period (without
first getting a warrant). Those records showed, as the Gov-
ernment later put it, that the suspect, Timothy Carpenter,
was “right where the . . . robbery was at the exact time of
the robbery.” Id., at 303. Carpenter moved to exclude the
CSLI records, arguing that the Government acquired them
through an unconstitutional search.
   The Court began its analysis by reviewing what it had
said about a different way of tracking “physical location and
movements”: the use of a GPS device to monitor a vehicle.
Id., at 306. In United States v. Jones, 565 U. S. 400, five
Justices had agreed that such tracking counts as a Fourth
Amendment search because “individuals have a reasonable
expectation of privacy in the whole of their physical move-
ments.” Carpenter, 585 U. S., at 310; see Jones, 565 U. S.,
at 430 (ALITO, J., concurring in judgment); id., at 415
(SOTOMAYOR, J., concurring).6 That made sense, the Car-
penter Court thought, even though the movements occurred
in public. Prior to the digital age, pursuing a suspect “for
any extended period of time was difficult and costly and
therefore rarely undertaken.” 585 U. S., at 310 (quoting
Jones, 565 U. S., at 429 (opinion of ALITO, J.)). As a result,
“society’s expectation has been that law enforcement agents
and others would not—and indeed, in the main, simply
could not—secretly monitor and catalogue every single
movement of an individual’s car.” Carpenter, 585 U. S., at
310 (quoting Jones, 565 U. S., at 430 (opinion of ALITO, J.)).

——————
  6 An overlapping set of five Justices decided the case on a different

ground, based on the Government’s physical trespass of the vehicle. See
Jones, 565 U. S., at 404–405.
                      Cite as: 609 U. S. ____ (2026)                     15

                           Opinion of the Court

A new technology should not transform what individuals
had reasonably thought they could withhold from the Gov-
ernment.
   It followed a fortiori, Carpenter held, that “[a]llowing gov-
ernment access to cell-site records contravenes” expecta-
tions of privacy. 585 U. S., at 311. To an even greater de-
gree than GPS monitoring, CSLI can provide a full “record
of the holder’s whereabouts” and, with that, “an intimate
window into a person’s life.” Ibid. People, after all, “regu-
larly leave their vehicles,” but they “compulsively carry”
their cell phones “all the time.” Ibid. A cell phone thus
“tracks nearly exactly the movements of its owner”: It
“faithfully follows” him not only through “public thorough-
fares [but] into private residences, doctor’s offices, political
headquarters, and other potentially revealing locales.”
Ibid. What is more, the “newfound tracking capacity” that
CSLI gives the police “runs against everyone”—not just
those “under investigation”—and “travel[s] back in time.”
Id., at 312. Police officers need not decide in advance (as
they do with GPS devices) who they want to follow and
when. Instead, they can easily and cheaply—with “just the
click of a button”—reconstruct any person’s movements
“retrospective[ly].” Id., at 311–312. What in the past was
“unknowable” suddenly becomes open to view, presenting
formerly unimaginable “privacy concerns.” Ibid. The Court
thus concluded: “[W]hen the Government accessed CSLI
from the wireless carriers”—thereby obtaining a “detailed
log” of where Carpenter had gone for seven days—“it in-
vaded Carpenter’s reasonable expectation of privacy in the
whole of his physical movements.” Id., at 312–313.7
——————
  7 A significant fraction of the dissent is devoted to relitigating Carpen-

ter, from which its author dissented. See post, at 1, 8–10, 13–14, 19–21
(ALITO, J.). Carpenter, the dissent complains today, “extended the Fourth
Amendment’s warrant requirement to encompass a category of govern-
ment investigations that it had never previously covered”: The decision
“thus reflected a stark departure from both traditional Fourth
16                  CHATRIE v. UNITED STATES

                          Opinion of the Court

                               B
  The resemblances between CSLI and Location History, in
their relationship to personal privacy, practically leap off
the page. Everything Carpenter relied on to find that law
enforcement officers conducted a Fourth Amendment
search when they accessed wireless carriers’ CSLI records
applies as well or better to the police’s accessing of Google’s
Location History data.
  First, Location History provides an even more fine-tuned
picture of a person’s movements than CSLI. Carpenter
noted that through CSLI records, police could “achieve[ ]
near perfect surveillance” of an individual holding a cell
phone. Id., at 311–312. But Location History is nearer per-
fect still. Here is one way of comparing the two: At any
given time, CSLI placed Carpenter within a “sector ranging
from one-eighth to four square miles,” whereas Location
History pinpointed Chatrie’s location within around twenty
meters, which is less than two percent of a mile. Id., at 312;
see 1 App. 45, 3 id., at 173–174. Or here is another
——————
Amendment principles and this Court’s 20th-century doctrine.” Post, at
13. In leveling that charge, the dissent re-ups arguments, point-for-
point, that Carpenter specifically rejected. Compare post, at 8, 13 (main-
taining that compelled document-production orders are never searches),
with 585 U. S., at 317–318 (rejecting that view); compare also post, at 9,
13 (contending that the Fourth Amendment never protects documents
held by third parties), with 585 U. S., at 313–316 (likewise rejecting that
view). In light of that outlook, it is perhaps not so surprising that the
dissent criticizes today’s decision as “rely[ing] primarily” on Carpenter,
rather than on earlier Fourth Amendment decisions. Post, at 13. But on
that supposed offense, we plead guilty as charged. Carpenter is the most
recent decision of this Court to consider the Fourth Amendment’s appli-
cation to new surveillance technologies—indeed, to law enforcement’s
use of those technologies to create a “chronicle of [a cell-phone] user’s
past movements.” 585 U. S., at 300. What would be grounds for com-
plaint is if this decision did not “rely primarily” on Carpenter. Post, at
13. And as the next section of this opinion shows, the more one delves
into the technologies at issue, the closer the parallels become. See infra
this page and 17–18.
                   Cite as: 609 U. S. ____ (2026)             17

                       Opinion of the Court

measure: CSLI logged Carpenter’s location an average of
101 times a day, whereas Location History commonly rec-
ords a person’s location every two minutes, for a daily aver-
age of 720 chartings. See Carpenter, 585 U. S., at 302; 136
F. 4th, at 151 (Berner, J., concurring). Or finally, a third:
Unlike CSLI, Location History can estimate a phone’s ele-
vation—so, for example, can tell whether someone has gone
into a doctor’s office on the first floor of a multi-story build-
ing, or a private apartment on the tenth. Of course, the
accuracy of each of the two techniques may vary in different
places and at different times. But across the board Location
History is the far more precise measure. When the Carpen-
ter Court said that CSLI provides a “detailed” and “encyclo-
pedic” portrait of a person’s whereabouts, it did not know
what further technology was on the horizon. 585 U. S., at
309.
   And next, Location History also allows police officers to
reconstruct “retrospective[ly],” and with no real effort, peo-
ple’s comings and goings in any area. Id., at 312. As with
CSLI, the Government need not decide in advance the kind
of surveillance it should undertake, whether of a person or
a site. “Whoever the suspect turns out to be,” Carpenter
said of CSLI, “he has effectively been tailed every moment
of every day.” Ibid. Likewise, as this case shows, wherever
a location of interest turns out to be (whether a crime scene
or a protest march or even a private home), it has effectively
been surveilled for the same boundless time. Google’s Lo-
cation History will be available to chart the movements of
many individuals—or a few or one—within the vicinity,
again at the “click of a button.” Id., at 311. Recall that in
Jones, it was thought notable that law enforcement officials
of an earlier age usually could not monitor every movement
of an individual’s car, as a GPS device does. See supra, at
14–15; 565 U. S., at 430 (opinion of ALITO, J.); see also Car-
penter, 585 U. S., at 312 (“In the past, attempts to recon-
struct a person’s [prior] movements were limited”). Far less
18               CHATRIE v. UNITED STATES

                      Opinion of the Court

could those officials ever perform the “tireless and absolute
surveillance” of any number of people in any number of
places, public and private, that Location History can accom-
plish. Ibid. If the one kind of intrusion clashes with “soci-
ety’s expectation[s]” of what counts as private, so must the
other. Jones, 565 U. S., at 430 (opinion of ALITO, J.).
   Indeed, Location History records implicate those privacy
interests still more than CSLI data because the former is
more the individual’s own. Most cell-phone users have no
awareness of CSLI records, and anyway would never try to
retrieve them. The records are instead the province of wire-
less carriers, which maintain them for an array of business
functions. See Carpenter, 585 U. S., at 301; supra, at 13–
14. Location History information is different. No doubt,
Google itself uses those records to improve the quality of its
apps. But Google users, too, regularly employ Location His-
tory—for example, “to remind themselves of a restaurant
they ate at two weeks ago, the time they were last at a
friend’s home, the sites they saw on vacation, or the dis-
tance they walked on a particular day.” Brief for Google
LLC as Amicus Curiae 8. The records thus serve as a per-
sonal journal of a user’s movements, which that user con-
sults (and even can edit) for his own purposes. See id., at
10. In that way, Location History resembles other private
materials—think of emails, documents, photographs, or
calendars—that even if stored on Google’s servers, a user
reasonably views as his own. And as a result, that he rea-
sonably expects to be shielded from the “inquisitive eyes” of
the government. Carpenter, 585 U. S., at 305.
                            C
  The Government, not much contesting any of the above,
principally argues on a different ground: that accessing
only a short amount of cell-phone location information
(whether Location History or CSLI) does not count as a
Fourth Amendment search. (The dissent likewise contends
                      Cite as: 609 U. S. ____ (2026)                    19

                          Opinion of the Court

that the “duration” of data obtained here is too brief for a
search to have happened. Post, at 14 (ALITO, J.); see post,
at 15–16.) Recall that Carpenter involved seven days’ worth
of location data. See supra, at 14–15. And in deciding that
case, this Court reserved the issue whether there was a
more “limited period for which the Government may obtain”
such data “free from Fourth Amendment scrutiny.” 585
U. S., at 310, n. 3.8 The Government now claims that the
answer is yes, and that the two hours’ worth of Location
History acquired here falls within the Constitution-free
zone. In the Government’s view, a person has no reasonable
expectation of privacy in “that short a time window” of lo-
cation data, because his “short-term” movements will “re-
veal[ ] little about the details of [his] personal life.” Brief for
United States 12, 20; see id., at 20 (“A single stop at a doc-
tor’s office, for example, does not in itself identify the reason
for the visit”). The Government cites in support United
States v. Knotts, 460 U. S. 276, 282 (1983), in which the
Court held that police officers’ use of a beeper to assist an
hours-long tail of a car did not bring the Fourth Amend-
ment into play. The lesson the Government draws is that
law enforcement officials accessing Location History should
receive a Fourth Amendment grace period of some number
of hours.
——————
   8 In comparing Carpenter and this case, the dissent sometimes treats

the former as involving not 7 days but instead 127 days of location data.
See post, at 13, 14, 15 (ALITO, J.). But there is no basis for doing so. To
be sure, one of the two wireless carriers involved in the case had turned
over 127 days of data, as the Court noted. See 585 U. S., at 302. But the
other was ordered to turn over only 7 days, and the Court could not have
been clearer that its holding applied whenever the Government accessed
a week or more of CSLI data (with everything below that amount re-
served). See id., at 310, n. 3 (“It is sufficient for our purposes today to
hold that accessing seven days of CSLI constitutes a Fourth Amendment
search”). The dissent acknowledges that fact (post, at 15, n. 4), even as
it repeatedly invokes the 127-day figure to make its comparative argu-
ment sound stronger.
20               CHATRIE v. UNITED STATES

                      Opinion of the Court

   But to begin, the Government is wrong about the inca-
pacity of short-term location information to reveal private
matters. “[R]epeated patterns,” in the Government’s phras-
ing, are not all that individuals wish to, and reasonably ex-
pect to, keep to themselves. Brief for United States 20. Re-
turn here to another of Jones’s insights: “[E]ven short-term
monitoring” of a person’s physical movements can provide
“a wealth of detail about [his] familial, political, profes-
sional, religious, and sexual associations.” 565 U. S., at 415
(opinion of SOTOMAYOR, J.). Consider just a few trips that
a person is apt to think “indisputably private”: to “the psy-
chiatrist, the plastic surgeon, the abortion clinic, the AIDS
treatment center, the strip club, the criminal defense attor-
ney, [or] the by-the-hour motel.” Ibid. And unlike a GPS
device, Location History enables police officers to focus on
precisely those sites—to see, in a given time block, who
shows up. Similarly, Location History—even two hours of
it—allows officers to target one-off events of potential inter-
est: a gun show, say, or a political rally.
   Still more fundamentally, we have never understood
Fourth Amendment protections as kicking in only once an
intrusion “goes too far.” Pennsylvania Coal Co. v. Mahon,
260 U. S. 393, 415 (1922) (adopting that approach for regu-
latory takings). Where the Fourth Amendment applies, it
applies—regardless of “the quality or quantity of infor-
mation” the government obtains. Kyllo, 533 U. S., at 37.
So, for example, this Court held that thermal imaging qual-
ified as a search even though it did not, and was not likely
to, detect “private activities” or “intimate details.” Ibid.
The Amendment, we analogized, makes “no exception” for
the officer “who barely cracks open the front door and sees
nothing but the nonintimate rug on the vestibule floor.”
Ibid. And likewise, the Amendment does not give agents a
pass if their wiretap is of limited duration and thus less
likely to intrude on private matters. Indeed, in our seminal
                     Cite as: 609 U. S. ____ (2026)                    21

                          Opinion of the Court

wiretap case, the police obtained only 18 minutes of record-
ings. See Katz, 389 U. S., at 354, n. 14.
   That approach makes all the more sense when, as with
Location History, officials can select the time-limited set of
materials they want from an all-encompassing database.
Then, the durational bounds on the data actually acquired
do little to address the Fourth Amendment’s concern about
“a too permeating police surveillance.” Di Re, 332 U. S., at
595; see supra, at 12. What creates that concern is that the
government can access all of a cell-phone user’s movements,
in both public and private places—that it possesses a vir-
tual panopticon with which to scrutinize its citizens’ activi-
ties. The sweep of the official invasion is not made less be-
cause the government, with the benefit of hindsight, can
pinpoint exactly which few hours of movements it wants to
review. That feature of accessing location data is, indeed,
more a practical benefit to the government than a limit on
its intrusive powers.9
   And contra the Government, Knotts does not support the
view that accessing two hours of Location History is not a
search. There, police officers put a beeper in a car to help
them follow it from Minnesota to Wisconsin. The Court de-
cided that the beeper did not turn the tail into a search, but
was explicit in keeping its holding cabined to that rudimen-
tary technology. The defendant had argued that a ruling
against him would enable officials to conduct “surveillance
——————
  9 The Government’s grace-period approach to Fourth Amendment pro-

tection would also create a host of line-drawing questions. At what point,
exactly, would a non-search become a search? In two hours, or six hours,
or one day, or six days? And how often would the clock reset? If, say, the
limit was six hours, could an officer request location data from 6 a.m. to
noon, and then again from 12:30 to 6:30 p.m.? And if there were concur-
rent federal and state investigations of a crime, as there could have been
here, would law enforcement access to Location History data double?
The approach the Government offers would “keep defendants and judges
guessing for years to come.” Riley v. California, 573 U. S. 373, 401
(2014).
22                   CHATRIE v. UNITED STATES

                           Opinion of the Court

of any citizen of this country” free from the strictures of the
Fourth Amendment. 460 U. S., at 283. The Court took the
concern seriously, stating that if technology progressed so
as to allow more sophisticated surveillance, “different con-
stitutional principles” could well apply. Id., at 284. And
three decades later, five Justices in two opinions found that
they did. When faced in Jones with a GPS device—which
unlike the beeper allowed remote monitoring—they de-
cided, notwithstanding Knotts, that privacy was implicated
and a search had occurred. See supra, at 14–15. Yet even
that was not all. When six years further on, the Carpenter
Court held that accessing CSLI was a search, it recounted
the Knotts-to-Jones progression to explain why Knotts did
not stand in its way. See 585 U. S., at 306–307 (Knotts “was
careful to distinguish between the rudimentary tracking fa-
cilitated by the beeper and more sweeping modes of surveil-
lance”). For the third time, we reach the same conclusion
today.
   And still another feature of Knotts makes it inapt here:
that the surveillance there was confined to public roads.
That fact was crucial to the Court’s decision: “A person trav-
eling in an automobile on public thoroughfares has no rea-
sonable expectation of privacy,” Knotts explained, because
the car is always “in plain view.” 460 U. S., at 281. By con-
trast, the movements that Location History reveals are not
limited to public streets. Recall what Carpenter observed:
A “cell phone faithfully follows its owner beyond public
thoroughfares and into private residences, doctor’s offices,
[and] political headquarters.” 585 U. S., at 311; see supra,
at 15.10 In one of those places—a private residence—this
——————
   10 The dissent replies that the “limited geofence procedure” authorized

by the warrant here distinguishes this case from Carpenter because “the
geofence’s boundaries” centered on “a public place.” Post, at 16 (ALITO,
J.). But as an initial matter, those boundaries were defined by a warrant.
If accessing Location History does not count as a Fourth Amendment
search, as the dissent generally suggests (see, e.g., post, at 12, 17), there
                     Cite as: 609 U. S. ____ (2026)                    23

                          Opinion of the Court

Court has held even beeper technology to count as a search
because it could reveal “whether a particular article—or a
person, for that matter” was in the home “at a particular
time.” United States v. Karo, 468 U. S. 705, 716 (1984). If
that is so, accessing Location History must also be a
search—even if for only two hours—because that data can
far more reliably show someone within a home (indeed, on
a specific floor). The Government replies with an odd argu-
ment. It thinks that “tracking [someone] into a private res-
idence”—yes, even for two hours—would “probably” be a
search, but tells us not to worry because Chatrie did not go
home. Tr. of Oral Arg. 98, 134. That approach, however, is
foreign to the way the Fourth Amendment works. Whether
something is a search does not depend on what it finds. See
Di Re, 332 U. S., at 595 (“[A] search is not to be made legal
by what it turns up. In law it is good or bad when it starts”).
An officer, after all, cannot know the fruits of a given sur-
veillance in advance. The surveillance must be either a
search or not regardless. The Government’s concession
thus gives away its argument that, for purposes of the
Fourth Amendment, two hours of cell-phone location data
is not enough.


——————
will not be a warrant (or any other means) to limit the scope of what law
enforcement can demand. And even putting that aside, the dissent’s ar-
gument is wrong because it ignores how this geofence warrant actually
worked. The geofence was not limited to the bank; it also included a
nearby church. 590 F. Supp. 3d 901, 918 (ED Va. 2022); cf. Brief for
Google LLC as Amicus Curiae 12 (noting that, in Google’s experience, it
is “common for a geofence to cover private homes, apartment buildings,
. . . hotels, [and] places of worship”). And regardless, the Location His-
tory data the police obtained at the second stage of the search process
was not constrained by the geofence. In fact, it showed individuals’ trips
to private residences, a school, and a hospital. See 590 F. Supp. 3d, at
923–924. So the geofence’s boundaries do not somehow turn Location
History into a public-movements-only technology or ensure a less “com-
prehensive” log than in Carpenter. Post, at 16.
24               CHATRIE v. UNITED STATES

                      Opinion of the Court

                               D
  The Government has an additional argument, which in
Carpenter was its “primary” one—that the so-called third-
party doctrine precludes Chatrie from invoking the Fourth
Amendment’s protections. 585 U. S., at 313. (Here too the
dissent reiterates the Government’s view. See post, at 11–
12, 17 (ALITO, J.).) The idea is that in “authoriz[ing] Google
to collect, retain, and use” his location information, Chatrie
lost his legitimate expectation of privacy, and therefore his
right to complain of a search—regardless whether it was for
two hours, two weeks, or two years. Brief for United States
15. The problem for the Government—and presumably the
reason that its primary assertion in Carpenter has here be-
come a secondary one—is that Carpenter refused to apply
the third-party doctrine to CSLI, and no good reason exists
to reach a different result for Location History.
  The third-party doctrine traces to two cases involving in-
formation provided by customers to a bank and telephone
company, and then turned over to law enforcement officials.
In United States v. Miller, 425 U. S. 435 (1976), this Court
held that a bank depositor had no reasonable expectation of
privacy in canceled checks and deposit slips in his bank’s
possession, because the records were “voluntarily conveyed
to the bank[ ] and exposed to [its] employees in the ordinary
course of business.” Id., at 442. The depositor, the Court
explained, had “take[n] the risk, in revealing his affairs to
another,” that the third party would in turn provide that
information to the government. Id., at 443. A few years
later, the Court in Smith v. Maryland, 442 U. S. 735 (1979),
applied that principle to hold that a (landline) telephone
subscriber lacked a legitimate expectation of privacy in the
phone numbers he dialed. Once again, the Court reasoned
that the subscriber had “voluntarily conveyed [the dialed
numbers] to the telephone company,” and so relinquished
his Fourth Amendment right. Id., at 744.
                  Cite as: 609 U. S. ____ (2026)           25

                      Opinion of the Court

   In Carpenter, however, the Court rejected the Govern-
ment’s contention that the third-party doctrine likewise
governed the acquisition of CSLI. The Court acknowledged
that a cell-phone user “continuously reveals his location” to
a third-party wireless carrier. 585 U. S., at 309. But it held
that cell-phone location information is “qualitatively differ-
ent” from “telephone numbers and bank records.” Ibid.
Those differences fell along two axes. First, the Court ex-
plained, the “nature” of CSLI is incomparably “revealing.”
Id., at 314. There is “a world of difference” between the “ex-
haustive chronicle of location information casually collected
by wireless carriers” and “the limited types of personal in-
formation addressed in Smith and Miller.” Ibid. The for-
mer thus “implicates privacy concerns far beyond” the lat-
ter. Id., at 315. And second, the Court continued, “[c]ell
phone location information is not truly ‘shared’ as one nor-
mally understands the term.” Ibid. Because “cell phones
and the services they provide” are “such a pervasive and
insistent part of daily life”—“indispensable to participation
in modern society”—a person can hardly help but generate
a “trail of location data.” Ibid. “[I]n no meaningful sense,”
the Court thought, does that mean a person “voluntar[il]y
expos[es]” to any third party a “comprehensive dossier of
his physical movements.” Ibid.
   Both differentiating features highlighted in Carpenter
apply equally or better to Location History. As noted above,
Location History is even more “revealing” than CSLI, be-
cause it provides a yet more precise record of an individual’s
movements. See supra, at 16–17. Access to that record en-
ables officials to undertake nearly perfect, retrospective
surveillance of countless persons and places. See supra, at
17–18. And for Location History, that surveillance is based
on information that a user reasonably understands as his
own, even though stored on Google’s servers—much like his
emails, photos, and calendar entries. See supra, at 18.
Likewise, the information is “not truly shared,” in the
26               CHATRIE v. UNITED STATES

                     Opinion of the Court

normal sense of wanting a third party to see or use it. Car-
penter, 585 U. S., at 315. The exposure of that information
to Google is merely what happens when a user avails him-
self of one of the services on his cell phone. Or said a bit
differently, it is the automatic price of conventional cell-
phone usage—which, just as Carpenter noted, is a “perva-
sive and insistent part of daily life.” Ibid. So just as the
third-party doctrine did not apply in Carpenter, it does not
apply here.
   The Government contests that conclusion on Carpenter’s
second axis alone: It claims that generating Location His-
tory, unlike producing CSLI, is a voluntary choice on the
user’s part. Although carrying a cell phone may be indis-
pensable in modern society, the Government argues, using
Location History is not. Rather, Location History is an “op-
tional add-on,” which a user must enable by an “affirmative
act” beyond “powering up” a phone. Brief for United States
13, 22 (quoting Carpenter, 585 U. S., at 315). In support,
the Government emphasizes that only around one-third of
current Google accountholders have activated the service.
See Brief for United States 22; see 1 App. 45. That goes to
show, says the Government, that people can “live[ ] without”
Location History. Brief for United States 22; see Tr. of Oral
Arg. 92. And if that is true (the Government says), people
who do use the feature have indeed “voluntar[il]y expos[ed]”
all of their movements. Carpenter, 585 U. S., at 315.
   But as an initial matter, that argument ignores some per-
tinent facts about how and why Google users turn on Loca-
tion History. As described earlier, Google prompts a user,
and repeatedly, to turn on the service—when he sets up a
Google account, when he sets up an Android phone, and
when he sets up a Google app. See supra, at 3–4. The
prompt often informs him that his device will not “work cor-
rectly” unless he does so. 2 App. 140–141. By contrast, it
does not tell him quite what he is signing up for: “how fre-
quently Google would record [his] location”; “how precise
                  Cite as: 609 U. S. ____ (2026)           27

                      Opinion of the Court

Location History can be”; or how Google might give all that
minute-by-minute location information to the government.
590 F. Supp. 3d, at 936; 136 F. 4th, at 128 (Wynn, J., con-
curring in judgment). In those circumstances, it is hard to
see how any user is, in the normal sense, “sharing” with
third parties a comprehensive catalog of his physical move-
ments. Carpenter, 585 U. S., at 314. And that is so regard-
less of how many others ignore Google’s entreaties. The
Government’s estimation of that number is almost surely
overstated: It appears to include, for example, the many
millions of Google accountholders in foreign countries like
China where collecting Location History is illegal. See 4
Joint App. in No. 22–4489 (CA4), pp. 845, 848. But in any
event, the raw user totals for Location History—one-third,
two-thirds, or someplace in between—are not the most apt
measure of whether that service’s enlistees have, as the
Government claims, self-consciously “assumed the risk of
sharing” all their movements with others. Brief for United
States 12.
  More generally, the Government’s approach to Fourth
Amendment protection would raise a host of workability is-
sues. At the top of the list: What percentage of users would
have to sign up for a service to make doing so non-volun-
tary? The Government posited at argument that if 80 per-
cent of active Google accountholders had enabled Location
History, the case would be “much closer.” Tr. of Oral. Arg.
92. After all, the Government candidly noted, even pos-
sessing a cell phone is not truly “indispensable” (to use Car-
penter’s word): “[S]omething like 90 percent of people have
[them].” Tr. of Oral. Arg. 92. So where to draw the line?
And after that, the questions only multiply. Would a user
lose Fourth Amendment protection if a highly popular cell-
phone feature became less so over time? What if the use of
a given feature is ubiquitous among (but only among) a sub-
set of the population (say, an age cohort), and an individual
defendant is a member of that class? Would it be enough if
28               CHATRIE v. UNITED STATES

                      Opinion of the Court

the lion’s share of cell-phone users enabled a feature similar
to the one at issue—so, for example, any location-tracking
service, whether Google’s or some other company’s? And
finally, a more basic inquiry: In such a world, how is any-
one—whether a cell-phone user or a police officer—to know
in advance (which is when the knowledge is useful) whether
enrollees in a given service will be found to have Fourth
Amendment protection in the information that service col-
lects? To ask all these questions about the Government’s
approach is to know that it is on the wrong track.
   And there is yet a deeper problem: The Government’s
app-by-app, feature-by-feature method of granting Fourth
Amendment protection misapprehends the very nature of
modern cell-phone use. Pretty much everything a person
does on a smartphone requires some kind of opt-in—an “af-
firmative act” beyond “powering up” to utilize a given app
or service. Carpenter, 585 U. S., at 315. Consider sending
an email on Gmail, uploading a photo to Google Photos, or
adding a calendar entry to Google Calendar. None happens
solely by dint of the phone’s operation; each requires, as Lo-
cation History does, an “optional add-on.” Brief for United
States 13. And each activity, like using Location History,
results in sharing information with a third-party tech com-
pany—turning over private materials to live on that com-
pany’s servers. The Government wishes to disconnect all
those uses from the mere act of carrying a turned-on cell
phone (the thing that generates CSLI), with only the latter
receiving assured Fourth Amendment protection. But that
is to imagine that all of us are living in dumb flip-phone
days. The point of carrying smartphones is to use what is
on them—as Carpenter said, to use the apps and “services
they provide.” 585 U. S., at 315. That is what has become
a “pervasive and insistent”—even “indispensable”—“part of
daily life.” Ibid.; Riley, 573 U. S., at 385. And so that is
what Carpenter insulated from the third-party doctrine. A
cell-phone user is not to be viewed as sharing private
                     Cite as: 609 U. S. ____ (2026)                    29

                          Opinion of the Court

information with third parties—which then can be freely
passed on to the government—just by doing the ordinary
things cell-phone users do.
                        *     *    *
  For all those reasons, we hold that police officers invade
a cell-phone user’s reasonable expectation of privacy when
they access his Location History. It does not matter if the
time period scrutinized was only two hours. Nor does it
matter that the materials obtained were handed over by a
third-party tech company. When the government “accesses
historical cell phone” location information—Location His-
tory as much as CSLI—it “conducts a search under the
Fourth Amendment.” Carpenter, 585 U. S., at 300.
                              III
   That conclusion does not resolve this case, because the
Fourth Amendment prohibits only searches that are “un-
reasonable.” When law enforcement officials undertake a
search to discover evidence of a crime, the reasonableness
standard generally requires that they seek a warrant from
“a neutral and detached magistrate.” Johnson v. United
States, 333 U. S. 10, 14 (1948); see Vernonia School Dist.
47J v. Acton, 515 U. S. 646, 653 (1995).11 That requirement
subjects the officials’ assessment of a search’s propriety to
the “deliberate, impartial judgment of a judicial officer.”
United States v. Grubbs, 547 U. S. 90, 99 (2006). The mag-
istrate, in turn, may issue a warrant only when “probable
cause is properly established and the scope of the author-
ized search is set out with particularity.” Kentucky v. King,
563 U. S. 452, 459 (2011).
——————
  11 Our precedents recognize exceptions to that rule—most prominently,

“when the exigencies of the situation make the needs of law enforcement
so compelling that [a] warrantless search is objectively reasonable.” Car-
penter, 585 U. S., at 319. Today’s decision does not call into doubt, in
such circumstances, a warrantless geofence search. See id., at 320 (not-
ing the same for “warrantless access to CSLI”).
30               CHATRIE v. UNITED STATES

                      Opinion of the Court

   When officers have obtained a warrant, as they did here,
a search’s legality will thus depend on whether a magis-
trate has properly found probable cause to support a partic-
ularly described search. “[P]robable cause is a fluid con-
cept—turning on the assessment of probabilities in
particular factual contexts—not readily, or even usefully,
reduced to a neat set of legal rules.” Illinois v. Gates, 462
U. S. 213, 232 (1983). But a magistrate must always deter-
mine that there is a “fair probability that contraband or ev-
idence of a crime will be found” in the place searched. Id.,
at 238. That means determining, to the requisite “fair prob-
ability,” both that the place searched will have the materi-
als sought and that those materials will contain evidence
“aid[ing]” in a criminal’s “apprehension or conviction.” Mes-
serschmidt v. Millender, 565 U. S. 535, 551, 552, n. 7 (2012);
see Zurcher v. Stanford Daily, 436 U. S. 547, 556 (1978)
(“The critical element” is whether there is the requisite
“cause to believe that the specific ‘things’ to be searched for
and seized are located” in the targeted place). The particu-
larity requirement, for its part, ensures that the search will
be of an appropriate scope—that it is “carefully tailored to
its justifications, and will not take on the character of the
wide-ranging exploratory searches the Framers intended to
prohibit.” Maryland v. Garrison, 480 U. S. 79, 84 (1987).
That requirement typically looks to such matters as the ge-
ographic and durational expanse of the search. See id., at
84–85; Karo, 468 U. S., at 718. And it too must take account
of “particular factual contexts,” including in surveillance
cases the nature of the technology to be used. Gates, 462
U. S., at 232; see, e.g., Karo, 468 U. S., at 718; see generally
Kerr Brief 17–20.
   The warrant issued here, as described earlier, was an un-
common, multi-step one. See supra, at 7–8. The first step
it laid out authorized police officers to obtain location data
for all cell phones inside the designated geofence within a
one-hour timeframe. The second step entitled the officers
                 Cite as: 609 U. S. ____ (2026)           31

                     Opinion of the Court

to obtain additional data (two hours, both inside and out-
side the geofence) for a subset of those phones—of the offic-
ers’ own choosing. And the third step enabled them to ob-
tain personal identifying information (including names,
email addresses, and phone numbers) for a further subset—
again of their selection. As to how the officers would make
their choices at the second and third steps—how they would
pick the users subject to more intense scrutiny—the war-
rant said very little. In toto: They would “attempt to narrow
down the list by reviewing the time stamped location coor-
dinates for each [device] and comparing that against the
known time and location information that is specific to this
crime.” 2 App. 136; see id., at 137; supra, at 7–8.
   The parties have contested the legality of each stage of
that process. Chatrie analogizes the first step to an “uncon-
stitutional general warrant,” and argues that in any event
the search at that step was both insufficiently described by
the warrant and lacking in probable cause. Brief for Cha-
trie 12; see id., at 13. As to steps two and three, Chatrie
contends that the warrant left too much authority to police
officers—and too little to the magistrate—to define the
search’s scope and determine whether cause for it existed.
See id., at 13–14. The Government, for its part, defends the
warrant at every step as seeking “particularized infor-
mation from Google’s database” based on “probable cause to
believe that Google had information” that would help solve
a crime. Brief for United States 14. And the Government
urges that the discretion given to the officers at steps two
and three fell within the bounds of reasonableness. See id.,
at 46.
   We leave all of those questions to the Court of Appeals to
decide in the first instance. Because the Fourth Circuit
panel concluded that no search had occurred, it did not ad-
dress whether the geofence warrant issued here validly au-
thorized each stage of the search process. Nor did the en
banc court’s one-sentence per curiam opinion speak to that
32               CHATRIE v. UNITED STATES

                     Opinion of the Court

issue. We are, as we have said many times before, “a court
of review, not of first view.” Cutter v. Wilkinson, 544 U. S.
709, 718, n. 7 (2005). It is therefore now up to the Court of
Appeals to decide whether, at each step of the search pro-
cess, the warrant satisfied the Fourth Amendment’s re-
quirements of particularity and probable cause.
                              IV
   In his famed and vindicated dissent, Justice Brandeis ex-
plained why a wiretap was a search, subject to Fourth
Amendment requirements. See Olmstead v. United States,
277 U. S. 438, 471 (1928). Those who drafted the Amend-
ment could not have imagined such a technology. But they
understood, Justice Brandeis wrote, a matter of more trans-
cendent importance: that Americans had “as against the
Government, the right to be let alone” and that the Fourth
Amendment must protect against “every unjustifiable in-
trusion by the Government upon the privacy of the individ-
ual, whatever the means employed.” Id., at 478.
   Far more recently, this Court in Carpenter invoked Jus-
tice Brandeis’s opinion in explaining why law enforcement
officials could not have “unrestricted access to a wireless
carrier’s database of physical location information.” 585
U. S., at 320. Said Carpenter: “[T]he Court is obligated—as
‘[s]ubtler and more far-reaching means of invading privacy
have become available to the Government’—to ensure that
the ‘progress of science’ does not erode Fourth Amendment
protections.” Ibid. (quoting 277 U. S., at 473–474 (dissent-
ing opinion)). For new technological tools, the Court con-
tinued, may “risk[ ] Government encroachment of the sort
the Framers, after consulting the lessons of history, drafted
the Fourth Amendment to prevent.” 585 U. S., at 320.
   Today’s decision follows from the same judicial obliga-
tion, to guard against the same risk of undue encroach-
ment. The Fourth Amendment applies, too, when officials
tap into Google’s “database of physical location
                  Cite as: 609 U. S. ____ (2026)                 33

                      Opinion of the Court

information.” Ibid. That database is new, but the principle
covering it is not: That principle is instead the one our his-
tory has given. The Fourth Amendment must, as ever, pro-
tect against unjustified governmental intrusion on the pri-
vacy of the individual.
  For the reasons stated, we vacate the judgment of the
Court of Appeals and remand the case for further proceed-
ings consistent with this opinion.
                                                   It is so ordered.
                 Cite as: 609 U. S. ____ (2026)           1

                    JACKSON, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 25–112
                         _________________


         OKELLO T. CHATRIE, PETITIONER v.
                 UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                        [June 29, 2026]

  JUSTICE JACKSON, with whom JUSTICE SOTOMAYOR joins,
concurring.
  I agree with the Court that law enforcement officers con-
ducted a search when they accessed petitioner Chatrie’s Lo-
cation History. I write separately because I would have
gone further to explain that this search violated the Fourth
Amendment. As the Court observes, “[w]hen officers have
obtained a warrant,” the validity of a search turns on
“whether a magistrate has properly found probable cause to
support a particularly described search.” Ante, at 30. In
my view, it is clear that at a minimum the second and third
stages of the search process here did not satisfy this foun-
dational requirement.
  At step two, the warrant authorized officers to access an
additional hour’s worth of Location History, unbounded by
the geofence’s perimeter. Though the warrant stated that
officers would “attempt to narrow down the list” of devices
subject to this step, there was no explicit requirement that
they do so. 2 App. 136 (emphasis added). Nor did the war-
rant set forth any criteria that officers would use in their
narrowing efforts. Ibid.
  The same infirmities carried over to step three. At this
step, the warrant authorized officers to access “identifying
account information,” including the username, date of
birth, account number, and any email addresses or
2                CHATRIE v. UNITED STATES

                    JACKSON, J., concurring

telephone numbers associated with the account. Id., at 137.
Once again, the warrant stated only that officers would “at-
tempt to narrow down the list,” without setting forth any
criteria for doing so. Ibid. (emphasis added).
   This “uncommon, multi-step” process, ante, at 30, meant
that officers conducted key portions of the search outside
the supervision of “a neutral and detached magistrate,”
Johnson v. United States, 333 U. S. 10, 14 (1948). Put dif-
ferently, officers could obtain additional, sensitive infor-
mation at steps two and three without having to convince a
magistrate that there was probable cause to believe this
particular information would uncover evidence related to
the crime. In this way, the warrant left “too much to the
discretion of the officer[s] executing the order,” giving them
a “roving commission” to collect more data absent any jus-
tification to a magistrate. Berger v. New York, 388 U. S. 41,
59 (1967).
   The facts of this case illustrate why the lack of magiste-
rial oversight is dangerous. When executing steps two and
three, law enforcement initially sought unbounded data
and account information from all 19 devices identified at
step one. See 590 F. Supp. 3d 901, 921 (ED Va. 2022).
Nothing in the warrant prevented officers from obtaining
this broad set of data; they narrowed the list only because
Google insisted on it. The officers eventually settled on re-
questing data from nine devices at step two, but even this
shorter list may have been overbroad. For three of the nine
devices, the location data showed the users’ movements to
and from sensitive spaces—namely, residences, a school,
and a hospital. See id., at 923. Given how it was written,
the warrant itself provided no “judicial check” on law en-
forcement’s determination that probable cause justified this
intrusion. Steagald v. United States, 451 U. S. 204, 220
(1981).
                  Cite as: 609 U. S. ____ (2026)            3

                     JACKSON, J., concurring

                         *     *    *
  The Court correctly observes that allowing the Govern-
ment to “access all of a cell-phone user’s movements” with-
out limit essentially arms it with “a virtual panopticon with
which to scrutinize its citizens’ activities.” Ante, at 21. It
is for this reason that law enforcement and courts must
carefully abide by the Fourth Amendment’s instruction that
“no Warrants shall issue, but upon probable cause, sup-
ported by Oath or affirmation, and particularly describing
the place to be searched, and the persons or things to be
seized.” The Fourth Circuit should keep this instruction in
mind on remand when evaluating the constitutionality of
the multi-step search that occurred here, especially at steps
two and three.
                  Cite as: 609 U. S. ____ (2026)              1

               GORSUCH, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 25–112
                          _________________


         OKELLO T. CHATRIE, PETITIONER v.
                 UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                         [June 29, 2026]

  JUSTICE GORSUCH, concurring in the judgment.
  I agree with the Court’s judgment that the government’s
examination of Okello Chatrie’s Location History data
amounted to a search for purposes of the Fourth Amend-
ment. But respectfully, I would reach that conclusion by a
different route.
                              I
  To decide whether a Fourth Amendment search took
place in this case, the Court once again invokes a test first
advanced in a solo concurrence in Katz v. United States, 389
U. S. 347 (1967). Under that test, a search occurs when the
government intrudes on an “expectation of privacy” that
“society is prepared to recognize as ‘reasonable.’ ” Id., at 361
(Harlan, J., concurring).
  If Katz has become a familiar feature of our law, it seems
to me no more persuasive for it. Consider just a few of its
problems, beginning with this: It has no basis in the Con-
stitution’s text or history. The Fourth Amendment’s pro-
tections do not depend on “the breach of some abstract ‘ex-
pectation of privacy’ whose contours are left to the judicial
imagination.” Carpenter v. United States, 585 U. S. 296,
391 (2018) (GORSUCH, J., dissenting). Instead, the Fourth
Amendment speaks in more concrete terms, protecting an
individual’s person, house, papers, and effects from
2                CHATRIE v. UNITED STATES

               GORSUCH, J., concurring in judgment

unreasonable searches and seizures. Ibid. No surprise,
then, that it’s hard to find anything like the Katz test in the
law leading up to the Fourth Amendment’s adoption—or
anything much like it in this Court’s jurisprudence before
the 1960s.       See Carpenter, 585 U. S., at 391–392
(GORSUCH, J., dissenting).
   Even if I could overlook that problem with Katz, I still
wouldn’t know how to apply it. As the Court has candidly
admitted, it has never been able to identify a “single rubric”
that might “definitively resolv[e] which expectations of pri-
vacy are entitled to protection.” Carpenter, 585 U. S., at 304
(majority opinion). Maybe Katz poses an empirical ques-
tion, tagging reasonable expectations of privacy to those
privacy expectations “people actually have.” Carpenter, 585
U. S., at 392 (GORSUCH, J., dissenting). Or maybe the ques-
tion is a normative one, asking what expectations reasona-
ble people “should . . . have.” Ibid. In truth, nobody knows
and, either way, this Court is the wrong body for the task.
We aren’t equipped to make empirical assessments about
what most Americans think. Nor is it our job to enforce our
own normative judgments, as opposed to those embodied in
the Constitution and laws. Id., at 392–394.
   If this weren’t trouble enough, we’ve also adorned Katz
with an equally indefensible qualification called the third
party doctrine. Under its terms, the Court has held, an in-
dividual maintains no “reasonable expectation of privacy”
in information he shares with others. Accordingly, the gov-
ernment may freely search a person’s papers and effects
without triggering any Fourth Amendment scrutiny so long
as they are entrusted to the care of someone else. See Smith
v. Maryland, 442 U. S. 735, 743–744 (1979); United States
v. Miller, 425 U. S. 435, 442–443 (1976).
   Much as with Katz itself, this Court has never offered a
persuasive justification for its offshoot. Carpenter, 585
U. S., at 389–390 (GORSUCH, J., dissenting). Nor do I see
how it might. Do we seriously mean to suggest that most
                  Cite as: 609 U. S. ____ (2026)             3

               GORSUCH, J., concurring in judgment

Americans think they have no “reasonable expectation of
privacy” in records held for them by their banks or pharma-
cists or doctors or technology companies? If not, on what
authority might we rule that the American people should
not reasonably expect privacy in materials like those? Re-
ally, the third party doctrine amounts to little more than a
“doubtful application of Katz that lets the government
search almost whatever it wants whenever it wants.” Id.,
at 391.
   As it did eight years ago in Carpenter, the Court today
largely ignores these problems. It simply declares that Mr.
Chatrie enjoyed a reasonable expectation of privacy in his
Location History because authorities could have used it to
create “a virtual panopticon.” Ante, at 21. And it tells us
that the third party doctrine does not apply to this case be-
cause Mr. Chatrie did “ ‘not truly shar[e]’ ” his Location His-
tory with Google. Ante, at 25–26 (quoting Carpenter, 585
U. S., at 315 (majority opinion)).
   Count me unpersuaded. Why does tracking Mr. Chatrie’s
movements digitally over an hour or two invade his reason-
able expectation of privacy when an officer tailing him for
the same length of time would not? See United States v.
Knotts, 460 U. S. 276, 281–283 (1983). Why is Location His-
tory data Mr. Chatrie voluntarily shared with Google not
“truly shared” when a person’s bank records are? See Mil-
ler, 425 U. S., at 440–443. Does the Court just mean to give
Katz’s third party doctrine a quiet burial by suggesting to-
day that any information shared over “smartphones” using
“apps and services” falls outside its reach? Ante, at 28 (in-
ternal quotation marks omitted). And what does any of this
have to do with the Fourth Amendment’s terms anyway?
Even if Katz and its battered third party doctrine may
straggle on today, they leave our Fourth Amendment juris-
prudence about where the Court’s obscenity doctrine stood
in the 1960s: We know a “reasonable expectation of
4                CHATRIE v. UNITED STATES

               GORSUCH, J., concurring in judgment

privacy” (and an exception to the third party doctrine) when
we see it.
                               II
   Rather than employ Katz and its third party doctrine, I
would take a different approach. To decide whether the
Fourth Amendment is in play, I would consult its terms,
asking first whether Location History qualifies as one of
Mr. Chatrie’s papers or effects, and then asking whether
the government searched those papers or effects. This tra-
ditional approach remains very much part of our law. See
Byrd v. United States, 584 U. S. 395, 403 (2018). Indeed,
we have expressly recognized that Katz and its progeny
“supplemen[t] rather than displac[e]” traditional Fourth
Amendment principles. Carpenter, 585 U. S., at 403 (ma-
jority opinion); see also Soldal v. Cook County, 506 U. S. 56,
64–65 (1992); United States v. Jones, 565 U. S. 400, 406–
407 (2012); Florida v. Jardines, 569 U. S. 1, 11 (2013).
   Thanks to Katz’s prominence today, of course, litigants
sometimes fail to press more traditional Fourth Amend-
ment arguments. See, e.g., Carpenter, 585 U. S., at 406
(GORSUCH, J., dissenting). But whatever his faults (possi-
bly including bank robbery), Mr. Chatrie has not forfeited
that line of attack in this case. In fact, he begins his brief
before us by contending that the Fourth Amendment is im-
plicated here precisely because the government enlisted
Google to search his “papers and effects.” See Brief for Pe-
titioner 15, 33.
   I agree with that assessment. Set aside whether Location
History data qualifies as among Mr. Chatrie’s “papers,” and
consider whether it at least constitutes one of his “effects.”
Based on the evidence the parties have put before us, it ap-
pears the word “effects” was understood at the time of the
Fourth Amendment’s adoption to embrace most any kind of
personal property. See, e.g., M. Brady, The Lost “Effects”
of the Fourth Amendment: Giving Personal Property Due
                  Cite as: 609 U. S. ____ (2026)            5

               GORSUCH, J., concurring in judgment

Protection, 125 Yale L. J. 946, 985–987 (2016) (“[E]arly
sources indicate that the term ‘effects’ meant ‘personal
property’ in common and colloquial usage”); L. Donohue,
The Original Fourth Amendment, 83 U. Chi. L. Rev. 1181,
1301 (2016) (effects meant “personal property or posses-
sions,” including “commercial items and goods”); Brief for
United States 32 (suggesting that “effects” excludes certain
real property like so-called open fields (citing Oliver v.
United States, 466 U. S. 170 (1984))).
   As I see it, Mr. Chatrie’s Location History data qualifies
as his personal property. To appreciate why, start with
this. As Google puts it, and no one seriously disputes, Lo-
cation History serves as a “diary” or map “of a person’s trav-
els.” Brief for Google LLC as Amicus Curiae 3–4. At the
time of the events in question, Mr. Chatrie’s agreement
with Google referred to Location History as “your” (mean-
ing, the user’s) “information.” 1 App. 72 (emphasis added).
Under the parties’ agreement, too, Mr. Chatrie was free to
“review” and “edit” his location data. Id., at 19. He was
even free to export or delete that data “from Google’s serv-
ers at will.” Ibid. Beyond all that, Google promised to pro-
tect his information against “unauthorized access, altera-
tion, disclosure, or destruction.” Id., at 71. Put simply, Mr.
Chatrie had the rights to enjoy, manage, alter, dispose, and
exclude others from what amounted to an electronic diary
or map of his travels. And as someone who held that many
“sticks in the bundle of rights . . . commonly characterized
as property”—including the “most treasured” and “essen-
tial” right to exclude—he has a strong claim that the Loca-
tion History data was his personal property. Cedar Point
Nursery v. Hassid, 594 U. S. 139, 149–150 (2021) (internal
quotation marks omitted).
   Next, notice what statutory and case law have to say on
the subject. The investigation of Mr. Chatrie unfolded in
Virginia. That State’s Computer Crimes Act expressly de-
scribes “computer data” as a form of “[p]roperty.” Va. Code
6                 CHATRIE v. UNITED STATES

               GORSUCH, J., concurring in judgment

Ann. §18.2–152.2 (2021). Altering or making an unauthor-
ized copy of computer data can constitute the crime of “com-
puter trespass” (another property law concept). §§18.2–
152.4(A)(3), (6). And the State provides a right to sue for
anyone “whose property or person is injured” by violations
of the Act (again suggesting a right to exclude). §18.2–
152.12(A).
   Nor is Virginia some outlier. In Texas, “computer . . .
data” can constitute “[p]roperty.” Tex. Penal Code Ann.
§33.01(16) (West Cum. Supp. 2025). State law likewise
criminalizes “knowingly access[ing] . . . a computer, com-
puter network, or computer system . . . with the intent to
obtain or use a file, data, or proprietary information” for a
prohibited purpose. §33.02(b–1)(2)(C) (West 2016). Once
more, as well, those whose “property has been injured” by
certain computer crimes may bring a “civil cause of action.”
Tex. Civ. Prac. & Rem. Code Ann. §143.001 (West 2019).
Georgia has a similar regime. See Ga. Code Ann. §§16–9–
93(b), (g) (2018) (criminalizing “[c]omputer [t]respass” and
providing a private right of action for such violations). And,
it appears, so do many other States. See Brief for Cato In-
stitute as Amicus Curiae 14–15, and n. 5 (“Today, more
than half of states . . . treat digital records and data as per-
sonal property,” and “[m]any” of them “make it illegal for
private actors to access or convert another person’s digital
data”); see also, e.g., People v. Seymour, 536 P. 3d 1260,
1273 (Colo. 2023) (finding that “law enforcement’s copying
of [the defendant’s] search history meaningfully interfered
with his possessory interest in that data”); Integrated Direct
Marketing, LLC v. May, 2016 Ark. 281, p. 6, 495 S. W. 3d
73, 76 (“[U]nder Arkansas law, intangible property, such as
electronic data, . . . can be converted”); cf. Thyroff v. Nation-
wide Mut. Ins. Co., 8 N. Y. 3d 283, 292–293, 864 N. E. 2d
1272, 1278 (2007) (holding that “electronic records that
were stored on a computer and were indistinguishable from
printed documents” are “subject to a claim of conversion”).
                   Cite as: 609 U. S. ____ (2026)              7

               GORSUCH, J., concurring in judgment

   To be sure, pursuant to its agreement with Mr. Chatrie,
Google stored his Location History data on its servers and
was free to use it for certain purposes. Brief for United
States 34–36. But an individual need not have “complete
ownership or exclusive control” before he can assert a
Fourth Amendment challenge against the search of real
property. Carpenter, 585 U. S., at 401 (GORSUCH, J., dis-
senting). Instead, we have long recognized, a “tenan[t] [or]
resident family membe[r]” who does not enjoy “fee simple
title” in a house has a sufficient interest in it to give rise to
a Fourth Amendment right. Ibid. And I fail to see why the
law should differ markedly when it comes to personal prop-
erty. If you “[t]oss your keys to a valet at a restaurant” or
“[a]sk your neighbor to look after your dog while you travel,”
you may entrust your personal property to another and li-
cense him to do certain things with it, much as Mr. Chatrie
did with his Location History data. Id., at 399. But that
hardly means that property is no longer yours. Ibid.
   Nor does it matter that those who wrote the Fourth
Amendment might not have imagined an electronic diary or
map of one’s travels. As with other laws, the terms found
in the Fourth Amendment carry their original public mean-
ing and can bear more applications than its drafters might
have expected or intended. See id., at 400. So just as the
First Amendment protects speech over the internet today
no less than it did speech delivered in the town square in
1791, it should hardly come as a surprise that the Fourth
Amendment might protect as personal “effects” electronic
diaries of one’s travels as it always has more traditional
ones. See Kyllo v. United States, 533 U. S. 27, 40 (2001)
(observing that a “search” of a home can take place not just
by physical entry but also by the external use of thermal-
imaging devices).
   Because Mr. Chatrie’s Location History data is his effect,
it is subject to the Fourth Amendment’s restrictions when
the government searches it. So, was there a search? The
8                CHATRIE v. UNITED STATES

              GORSUCH, J., concurring in judgment

government conducts a search when it “ ‘look[s] over or
through for the purpose of finding something.’ ” Id., at 32,
n. 1 (quoting N. Webster, An American Dictionary of the
English Language 66 (1828) (reprint 6th ed. 1989)). Under
our precedents, none of which the government asks us to
overrule, a search equally transpires when government of-
ficials enlist private parties in that task. See Skinner v.
Railway Labor Executives’ Assn., 489 U. S. 602, 614 (1989)
(Fourth Amendment “protects against” searches “effected”
by a private party “if the private party acted as an instru-
ment or agent of the Government”). And that’s exactly
what occurred here: The government conducted a search
both when it compelled Google to rummage through Mr.
Chatrie’s data at “step one,” and when it later examined
that data for itself and demanded more data yet from
Google at “step two.” See ante, at 7–8 (describing the step-
wise process in which the searches were conducted in this
case).
                             *
  I might have hoped that the Court would have pursued a
more traditional approach to the Fourth Amendment today.
But look carefully and you will see hints of it at work even
in the Court’s opinion. Why is the Court so protective of
Location History data, email, and electronically stored pho-
tos and calendars? See ante, at 25–26. Because, it turns
out, “a user reasonably understands” all those things “as
his own.” Ante, at 25. Put another way, they are his effects.
And why does the Court hold Mr. Chatrie’s effects protected
by the Fourth Amendment even though a third party stores
them? Because, the Court says, those effects remain his
“even though [they are] stored on Google’s servers.” Ibid.
Put another way, entrusting your effects to a third party for
certain agreed purposes doesn’t mean they are no longer
yours. While more work may lie ahead to bring coherence
                Cite as: 609 U. S. ____ (2026)         9

             GORSUCH, J., concurring in judgment

to our Fourth Amendment jurisprudence, perhaps this is a
start.
                  Cite as: 609 U. S. ____ (2026)            1

                      ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 25–112
                          _________________


         OKELLO T. CHATRIE, PETITIONER v.
                 UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                         [June 29, 2026]

   JUSTICE ALITO, with whom JUSTICE THOMAS joins as to
Part I and with whom JUSTICE BARRETT joins as to Parts
II–B, II–C–1, and II–C–2, dissenting.
   Eight years ago, I warned that this Court’s decision in
Carpenter v. United States, 585 U. S. 296 (2018), would pro-
duce one of two outcomes. Either the Court would need to
clarify Carpenter’s limits in a future decision, or Carpenter
would usher in “revolutionary developments” in our doc-
trine by giving criminal suspects a “protected Fourth
Amendment interest in any sensitive personal information
about them that is collected and owned by third parties.”
Id., at 385 (ALITO, J., dissenting). Today, the Court takes
the country down the latter path. In doing so, the Court
sheds Carpenter’s self-imposed boundaries and further de-
stabilizes longstanding Fourth Amendment jurisprudence.
   To make matters worse, the majority does all this in an
advisory opinion. Although today’s decision will send seis-
mic waves through our Fourth Amendment doctrine, not
one iota of the majority opinion will affect the outcome of
this case. The Court knows this and does not claim other-
wise. Indeed, by refusing to review the one question that
could have at least theoretically given Chatrie some hope of
relief, the Court carefully set the stage for its planned per-
formance: striking a pose as a great champion of privacy in
2                CHATRIE v. UNITED STATES

                      ALITO, J., dissenting

the digital age. I cannot support this irresponsible esca-
pade.
                               I
  The Court should not have granted certiorari in this case,
and under any faithful application of our precedents, it
should now either dismiss this petition or affirm the deci-
sion below based on the “good-faith exception” to the exclu-
sionary rule. Instead, the Court issues an advisory opinion
concerning a now-obsolete “geofence” procedure. Last
Term, the Court worried out loud about rushing in to judge
“new technologies with transformative capabilities” that we
barely understand. TikTok Inc. v. Garland, 604 U. S. 56,
62 (2025) (per curiam). In cases involving such technology,
the Court proclaimed, we should take care not to “ ‘embar-
rass the future.’ ” Ibid. (quoting Northwest Airlines, Inc. v.
Minnesota, 322 U. S. 292, 300 (1944)). Today, the Court ex-
hibits no such modesty.
                             A
  It has long been established that federal courts may not
issue “advisory opinions” that do not bear on the rights of
the litigants before them. Lewis v. Continental Bank Corp.,
494 U. S. 472, 477 (1990). At the appellate stage, this prin-
ciple means that courts should resolve only those questions
on which a favorable ruling would provide a litigant redress
from the judgment below. See Food Marketing Institute v.
Argus Leader Media, 588 U. S. 427, 432–433 (2019). The
question on which the Court granted certiorari in this case
cannot satisfy this requirement under any colorable view of
the law. The Court should therefore decline to answer it.
  Okello Chatrie’s ongoing stake in this case stems from his
conviction for robbing a bank and brandishing a firearm.
On appeal, Chatrie challenged those convictions on only one
ground. He argued that the District Court erred in denying
his motion to suppress the fruits of the geofence procedure
                     Cite as: 609 U. S. ____ (2026)                    3

                          ALITO, J., dissenting

that led to his identification as the bank robber.1 So, unless
he can show that this evidence should be suppressed, he
cannot obtain any relief. And his chances of making the
showing needed to justify suppression are virtually zero.
  The police obtained information about Chatrie’s location
at the time of the robbery pursuant to a warrant issued by
a neutral magistrate. And when evidence is obtained under
such a warrant, a defendant seeking suppression must
overcome the good-faith exception to the exclusionary rule.
United States v. Leon, 468 U. S. 897, 923 (1984). A majority
of the Court of Appeals for the Fourth Circuit, sitting en
banc, held that Chatrie could not do so. 136 F. 4th 100, 101
(2025) (Diaz, C. J., concurring); id., at 114 (Niemeyer, J.,
concurring); id., at 115 (King, J., concurring); id., at 115,
n. 1 (Winn, J., concurring in judgment); id., at 142 (Hey-
tens, J., concurring). That holding suffices to affirm the
District Court’s admission of the geofence evidence and
thus independently supports the Fourth Circuit’s judg-
ment. Accordingly, any review by this Court should concern
an issue that could at least plausibly disturb that good-faith
holding. Cf. Stewart v. IHT Ins. Agcy. Group, LLC, 990
F. 3d 455, 457 (CA6 2021).
  On this score, today’s decision fails. The majority does
not dispute the Fourth Circuit’s good-faith analysis, and
nothing in its opinion casts a shred of doubt on that holding.
See ante, at 10, n. 4. To overcome the good-faith exception,
Chatrie would need to show that either (1) the affidavit sup-
porting the geofence warrant was knowingly or recklessly

——————
  1 The majority characterizes the issue as whether the Government may

introduce the location information that the police obtained through the
geofence procedure. But Chatrie also sought to suppress all the fruits of
that location information, and these could potentially include a firearm
matching one used in the crime, nearly $100,000 of currency in bands
bearing the bank teller’s signature, and his confession to the crime. See
Defendant’s Motion to Suppress in No. 3:19–cr–00130 (ED Va.), ECF
Doc. 29; Statement of Facts, ECF Doc. 229, p. 3.
4                     CHATRIE v. UNITED STATES

                             ALITO, J., dissenting

false, (2) the magistrate rubber-stamped the warrant appli-
cation, (3) the affidavit was “ ‘bare bones,’ ” or (4) the war-
rant application was so facially deficient that no reasonable
officer would rely on it. Leon, 468 U. S., at 923, and n. 24.
Yet nothing in the majority opinion touches on any of these
matters. Thus, nothing in today’s decision bears on the
Fourth Circuit’s good-faith holding. And because that hold-
ing independently supports the judgment below, the Court’s
opinion is advisory.2
   This outcome was guaranteed as soon as this Court
granted certiorari. When seeking review in this Court,
Chatrie recognized that dislodging the Fourth Circuit’s
judgment required that he prevail on the good-faith issue,
so his petition asked us to alter the good-faith exception.
See Pet. for Cert. i, 34–37 (asking the Court to create a
carve-out to the good-faith exception). Yet the Court ex-
cluded the good-faith issue from its grant of certiorari, 607
U. S. 1148 (2026), ensuring that any opinion would be advi-
sory. Indeed, even if the Court were to decide that the

——————
   2 I do not contend that the Court lacks Article III jurisdiction over this

case as a formal matter. Chatrie’s conviction suffices to render this liti-
gation a “case or controversy,” regardless of the question on which the
Court granted certiorari. The majority opinion is nonetheless advisory—
not because I think “the odds are strong” that Chatrie will lose on re-
mand, contra, ante, at 10, n. 4., but because the majority opinion does
not disturb the basis for the Fourth Circuit’s judgment and thus Cha-
trie’s conviction. This Court’s longstanding policy against issuing advi-
sory opinions on constitutional issues is not limited to cases where we
lack jurisdiction. See, e.g., Rescue Army v. Municipal Court of Los Ange-
les, 331 U. S. 549, 568 (1947) (holding that the Court possessed jurisdic-
tion over a case but nonetheless declining to exercise it because the
Court’s policy against issuing gratuitous constitutional opinions “has not
been limited to jurisdictional determinations”); Liverpool, New York &
Philadelphia S. S. Co. v. Commissioners of Emigration, 113 U. S. 33, 39
(1885) (“In the exercise of [its] jurisdiction, [this Court] is bound . . . never
to anticipate a question of constitutional law in advance of the necessity
of deciding it”). An opinion composed exclusively of dicta is no less advi-
sory simply because the Court has jurisdiction to pronounce such dicta.
                  Cite as: 609 U. S. ____ (2026)            5

                      ALITO, J., dissenting

warrant in this case was deficient, there would be no color-
able argument on remand that all reasonable officers would
have correctly predicted that outcome. See Leon, 468 U. S.,
at 923. After all, this Court has never provided guidance
on how to apply the Warrant Clause when the police re-
quest geolocation data from a third party. See Carpenter,
585 U. S., at 316–320 (noting only that such a warrant re-
quires probable cause). Accordingly, it would be nearly im-
possible for Chatrie to prove that the police here (and, by
extension, every other officer who ever relied on this type of
geofence warrant) acted in bad faith. See Davis v. United
States, 564 U. S. 229, 240 (2011) (Fourth Amendment vio-
lations “trigger the harsh sanction of exclusion only when
they are deliberate . . . and culpable”). In sum, no resolu-
tion of the question on which the Court granted certiorari
could have disturbed the Fourth Circuit’s good-faith hold-
ing and, thus, its judgment.
   The Court therefore erred by granting certiorari, and we
should now dismiss this petition as improvidently granted.
See Conway v. California Adult Authority, 396 U. S. 107,
110 (1969) (per curiam) (dismissing when resolving the is-
sue addressed in the petition would produce an advisory
opinion). Alternatively, this Court could affirm the decision
below on good-faith grounds. Although the Court did not
grant certiorari on this question, we may affirm a judgment
on any ground supported by the record, and we would not
be the court of “first view” on the good-faith issue. Upper
Skagit Tribe v. Lundgren, 584 U. S. 554, 560–561 (2018).
The Government properly presented this issue below, the
District Court admitted the contested evidence on good-
faith grounds, a majority of the en banc Fourth Circuit
voted to affirm on that basis, and the Government contin-
ued to press good faith at the petition and merits stages in
this Court. See Government’s Response in Opposition to
Defendant’s Motion for Suppression, ECF Doc. 41, p. 21;
590 F. Supp. 3d 901, 937 (ED Va. 2022); Brief in Opposition
6                CHATRIE v. UNITED STATES

                      ALITO, J., dissenting

13; Brief for United States 47–48. This Court therefore has
every reason to affirm on that ground.
  Instead, the Court charges forward to decide the question
presented, even though the majority cannot discern any im-
pact that its decision has on the Fourth Circuit’s judgment.
See ante, at 10, n. 4. The majority thus issues a plainly ad-
visory opinion, violating this Court’s “oldest and most con-
sistent” justiciability rule. Flast v. Cohen, 392 U. S. 83, 96
(1968) (internal quotation marks omitted).
                               B
   Advisory-opinion concerns aside, our prudential certio-
rari considerations further counseled against granting cer-
tiorari. Writs of certiorari are discretionary, and we reserve
them for “compelling” cases in which the court below “has
decided an important question of federal law.” This Court’s
Rule 10. The question in this case does not qualify.
   Chatrie’s petition asked whether the geofence procedure
that the police used here comports with the Fourth Amend-
ment. The answer to this question has scarcely any ongoing
significance. Google, the Government, and the majority all
agree that Google has modified its Location History service
in a manner that forecloses future use of this geofence pro-
cedure. Ante, at 4, n. 2; Brief for Google LLC as Amicus
Curiae 2; Brief for United States 42, n. 3. Chatrie does not
offer any evidence to the contrary. See Tr. of Oral Arg. 17–
18; Brief for Petitioner 5; Pet. for Cert. 10–11. As a result,
Fourth Amendment challenges to this geofence procedure
will likely pass into obscurity soon.
   This Court has long been averse to granting certiorari on
questions “that time [will] soon bury.” Darr v. Burford, 339
U. S. 200, 227 (1950) (Frankfurter, J., dissenting). This
aversion applies with special force here given this case’s
subject matter. The Fourth Amendment’s application to
surveillance technology turns on the “unique nature” of the
technology involved and the way in which the police use it
                  Cite as: 609 U. S. ____ (2026)             7

                      ALITO, J., dissenting

to collect information. Carpenter, 585 U. S., at 309. For
instance, when determining whether law enforcement’s use
of a technology requires a warrant or is otherwise “unrea-
sonable,” this Court has considered the technology’s capa-
bilities, prevalence, costliness, conspicuousness, intrusive-
ness, precision, accuracy, security, and comprehensiveness.
See, e.g., Kyllo v. United States, 533 U. S. 27, 34–35 (2001);
United States v. Jones, 565 U. S. 400, 429–431 (2012)
(ALITO, J., concurring in judgment); Maryland v. King, 569
U. S. 435, 446–465 (2013); Birchfield v. North Dakota, 579
U. S. 438, 461–464 (2016); Carpenter, 585 U. S., at 310–313.
Because these qualities vary from one technology to the
next, the specific application of the Fourth Amendment
does as well. Such variability renders this case all the less
suitable for our review. Whatever one’s jurisprudential
views about the Fourth Amendment in the digital age, a
case concerning a now-obsolete geofence procedure is an
odd vehicle for pronouncin

[...TRUNCATED 29626 of 149626 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
