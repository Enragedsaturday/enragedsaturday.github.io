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

## GROUP: content/cases/Carroll v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Carroll v. United States"
type: case
citation: "267 U.S. 132 (1925)"
parallel_cite: "45 S. Ct. 280; 69 L. Ed. 543"
neutral_cite: 1925 U.S. LEXIS 361
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1925
date_decided: 1925-11-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1925-03-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Carroll v. United States
  varies_by_point: false
  scope_note: "Origin of the automobile exception; repeatedly reaffirmed and refined (Chambers, Ross, Carney, Acevedo). Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/100567/carroll-v-united-states/"
  cluster_id: 100567
  opinion_id: 100567
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Anchor"
related: ["[[Chambers v. Maroney]]", "[[California v. Carney]]", "[[California v. Acevedo]]", "[[Collins v. Virginia]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "warrantless-search", "vehicle", "probable-cause"]
holding: "Origin of the automobile exception: a vehicle may be searched without a warrant on probable cause because, unlike a fixed structure, it…"
lake:
  record_id: Carroll v. United States
  status: verified
  projected_at: 2026-07-06
---

# Carroll v. United States

*267 U.S. 132 (1925)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During Prohibition, federal agents who had probable cause to believe Carroll and a companion were transporting bootleg liquor stopped their automobile on a highway between Detroit and Grand Rapids and searched it without a warrant, finding 68 bottles of liquor concealed behind the upholstery. Carroll was convicted of transporting intoxicating liquor and challenged the warrantless search.

## Issue
Whether officers with probable cause may search a moving vehicle for contraband without first obtaining a warrant.

## Rule
Yes. The Court distinguished fixed premises from vehicles: there is "a necessary difference between a search of a store, dwelling house, or other structure in respect of which a proper official warrant readily may be obtained and a search of a ship, motor boat, wagon, or automobile for contraband goods, where it is not practicable to secure a warrant, because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." — 267 U.S. 132, ¶ 37. ^pin-p37

The exception rests on probable cause plus the vehicle's ready mobility; a warrantless search of a vehicle on probable cause to believe it carries contraband is reasonable.

## Application
The officers had probable cause — built on prior dealings and recognition of the car and its occupants — to believe Carroll's automobile was carrying contraband liquor. Because the car was readily movable and a warrant could not practicably be obtained before it left the area, the warrantless search of the vehicle on these facts was reasonable under the Fourth Amendment.

## Conclusion
The warrantless search of the moving automobile on probable cause was lawful; the conviction was affirmed. *Carroll* is the origin of the automobile exception.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Carroll*'s rule has been repeatedly reaffirmed and elaborated — extended to delayed station-house searches in [[Chambers v. Maroney]], grounded in ready mobility and pervasive regulation in [[California v. Carney]], and unified for containers in [[California v. Acevedo]]; its reach was bounded at the home's [[Curtilage|curtilage]] in [[Collins v. Virginia]].

## Appears on
- [[Automobile Exception]] — *Key — Anchor*

## Sources
- *Carroll v. United States*, 267 U.S. 132 (1925) — https://www.courtlistener.com/opinion/100567/carroll-v-united-states/ — pinpoint given as CourtListener paragraph number (¶ 37); CL's text of this 1925 opinion is paragraph-numbered without U.S. Reports star pagination at the quoted passage.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fc6135da7b308086", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "267 U.S. 132 (1925)", "court": "U.S. Supreme Court", "neutral_cite": "1925 U.S. LEXIS 361", "official_citation_present": true, "parallel_cite": "45 S. Ct. 280; 69 L. Ed. 543", "title": "Carroll v. United States", "year": "1925"}}
{"assertion_id": "04fa4fdd0683a2c7", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Anchor", "title": "Carroll v. United States"}}
{"assertion_id": "2c4a0855a423ae66", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Origin of the automobile exception: a vehicle may be searched without a warrant on probable cause because, unlike a fixed structure, it…", "title": "Carroll v. United States"}}
{"assertion_id": "4de3466122c95174", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Carroll v. United States"}}
{"assertion_id": "c006b81509ae3319", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1925-03-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Carroll v. United States", "field_i_validity": "good_law", "scope_note": "Origin of the automobile exception; repeatedly reaffirmed and refined (Chambers, Ross, Carney, Acevedo). Good law.", "title": "Carroll v. United States", "varies_by_point": "false"}}
```

### lake record — Carroll v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carroll v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Carroll v. United States",
    "case_name_short": "Carroll",
    "case_name_full": "Carroll Et Al. v. United States",
    "input_case_name": "Carroll v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1925-11-26",
    "year": 1925,
    "docket": null,
    "cluster_id": 100567,
    "lead_opinion_id": 100567,
    "sibling_ids": [
      100567,
      9418540,
      9418541
    ],
    "absolute_url": "/opinion/100567/carroll-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "267 U.S. 132",
      "volume": "267",
      "reporter": "U.S.",
      "page": "132",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "45 S. Ct. 280",
        "volume": "45",
        "reporter": "S. Ct.",
        "page": "280",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 543",
        "volume": "69",
        "reporter": "L. Ed.",
        "page": "543",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1925 U.S. LEXIS 361",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "361",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "267 U.S. 132",
        "volume": "267",
        "reporter": "U.S.",
        "page": "132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 S. Ct. 280",
        "volume": "45",
        "reporter": "S. Ct.",
        "page": "280",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 543",
        "volume": "69",
        "reporter": "L. Ed.",
        "page": "543",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1925 U.S. LEXIS 361",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "361",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "267 U.S. 132",
    "official_selection": {
      "court_class": "scotus",
      "selected": "267 U.S. 132",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-p37",
      "page": null,
      "quote": "--- # Carroll v. United States *267 U.S. 132 (1925)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During Prohibition, federal agents who had probable cause to believe Carroll and a companion were transporting bootleg liquor stopped their automobile on a highway between Detroit and Grand Rapids and searched it without a warrant, finding 68 bottles of liquor concealed behind the upholstery. Carroll was convicted of transporting intoxicating liquor and challenged the warrantless search. ## Issue Whether officers with probable cause may search a moving vehicle for contraband without first obtaining a warrant. ## Rule Yes. The Court distinguished fixed premises from vehicles: there is",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1925-03-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Carroll v. United States",
    "varies_by_point": false,
    "scope_note": "Origin of the automobile exception; repeatedly reaffirmed and refined (Chambers, Ross, Carney, Acevedo). Good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Carroll v. United States:lane1_negative"
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
        "journal_ref": "Carroll v. United States:lane1_negative"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gall v. United States",
          "cluster_id": 145843,
          "cite": [
            "169 L. Ed. 2d 445",
            "128 S. Ct. 586",
            "552 U.S. 38",
            "2007 U.S. LEXIS 13083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brinegar v. United States",
          "cluster_id": 104716,
          "cite": [
            "93 L. Ed. 2d 1879",
            "69 S. Ct. 1302",
            "338 U.S. 160",
            "1949 U.S. LEXIS 2084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmelin v. Michigan",
          "cluster_id": 112646,
          "cite": [
            "115 L. Ed. 2d 836",
            "111 S. Ct. 2680",
            "501 U.S. 957",
            "1991 U.S. LEXIS 3816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(100567 OR 9418540 OR 9418541) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMyMDQ0ODAwMDAwJnM9NDUxODk5MyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28100567+OR+9418540+OR+9418541%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(100567 OR 9418540 OR 9418541)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDgwJnM9MTA0NzY5JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28100567+OR+9418540+OR+9418541%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(100567 OR 9418540 OR 9418541)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 1,
        "triage_snippet_classified": 76
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(100567 OR 9418540 OR 9418541)",
    "indexed_citing_opinions": 4916,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 100567,
        "count": 4498,
        "count_source": "search"
      },
      {
        "opinion_id": 9418540,
        "count": 536,
        "count_source": "search"
      },
      {
        "opinion_id": 9418541,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7455,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/carroll-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMjIxMTYmcz0xMDM4ODk1NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28100567+OR+9418540+OR+9418541%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 100567,
        "cited_id": 85007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 85059,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 85079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 85121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 86221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 87693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 90759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 95241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 100265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 5560847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 6236987,
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
    "date_created": "2026-07-04T23:40:51Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:41:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:41:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:43:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:41:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Carroll v. United States

```
<p class="case_cite"><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U.S. 132</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">45 S.Ct. 280</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">69 L.Ed. 543</a></span></p>
    <p class="parties">CARROLL et al.<br>v.<br>UNITED STATES.</p>
    <p class="docket">No. 15.</p>
    <p class="date">Reargued and Submitted March 14, 1924.</p>
    <p class="date">Decided March 2, 1925.</p>
    <div class="prelims">
      <p class="indent">[Syllabus and Statement of the Case from pages 132-136 intentionally omitted]</p>
      <p class="indent">Messrs. Thomas E. Atkinson and Clare J. Hall, both of Grand Rapids, Mich., for plaintiffs in error.</p>
      <p class="indent">[Argument of Counsel from pages 136-143 intentionally omitted]</p>
      <p class="indent">The Attorney General and Mr. James M. Beck, Sol. Gen., of Washington, D. C., for the United States.</p>
      <p class="indent">Mr. Chief Justice TAFT, after stating the case as above, delivered the opinion of the Court.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">The constitutional and statutory provisions involved in this case include the Fourth Amendment and the National Prohibition Act.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">The Fourth Amendment is in part as follows:</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">'The right of the people to be secure in their persons,      houses, papers and effects against unreasonable searches and      seizures shall not be violated, and no warrants shall issue      but upon probable cause, supported by oath or affirmation,      and particularly describing the place to be searched, and the      persons or things to be seized.'</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">Section 25, title 2, of the National Prohibition Act, c. 85, <span class="citation no-link">41 Stat. 305</span>, 315, passed to enforce the Eighteenth Amendment, makes it unlawful to have or possess any liquor intended for use in violating the act, or which has been so used, and provides that no property rights shall exist in such inquor. A search warrant may issue and such liquor, with the containers thereof, may be seized under the warrant and be ultimately destroyed. The section further provides:</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">'No search warrant shall issue to search any private dwelling      occupied as such unless it is being used for the unlawful      sale of intoxicating liquor, or unless it is in part used for      some business purpose such as a store, shop, saloon,      restaurant, hotel, or boaring house. The term 'private      dwelling' shall be construed to include the room or rooms      used and occupied not transiently but solely as a residence in an apartment house, hotel, or boarding house.'</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">Section 26, title 2, under which the seizure herein was made, provides in part as follows:</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">'When the commissioner, his assistants, inspectors, or any      officer of the law shall discover any person in the act of      transporting in violation of the law, intoxicating liquors in      any wagon, buggy, automobile, water or air craft, or other      vehicle, it shall be his duty to seize any and all      intoxicating liquors found therein being transported contrary      to law. Whenever intoxicating liquors transported or      possessed illegally shall be seized by an officer he shall      take possession of the vehicle and team or automobile, boat,      air or water craft, or any other conveyance, and shall arrest      any person in charge thereof.'</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">The section then provides that the court upon conviction of the person so arrested shall order the liquor destroyed, and except for good cause shown shall order a sale by public auction of the other property seized, and that the proceeds shall be paid into the Treasury of the United States.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">By section 6 of an act supplemental to the National Prohibition Act (<span class="citation no-link">42 Stat. 222</span>, 223, c. 134 [Comp. St. Ann. Supp. 1923, &#167; 10184a]) it is provided that if any officer or agent or employee of the United States engaged in the enforcement of the Prohibition Act or this Amendment, 'shall search any private dwelling,' as defined in that act, 'without a warrant directing such search,' or 'shall without a search warrant maliciously and without reasonable cause search any other building or property,' he shall be guilty of a misdemeanor and subject to fine or imprisonment or both.</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">In the passage of the supplemental act through the Senate, amendment No. 32, known as the Stanley Amendment, was adopted, the relevant part of which was as follows:</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">'Sec. 6. That any officer, agent or employee of the United      States engaged in the enforcement of this act or the National Prohibition Act, or any other law of the United      States, who shall search or attempt to search the property or      premises of any person without previously securing a search      warrant, as provided by law, shall be guilty of a misdemeanor      and upon conviction thereof shall be fined not to exceed      $1,000, or imprisoned not to exceed one year, or both so      fined and imprisoned in the discretion of the court.'</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">This amendment was objected to in the House, and the judiciary committee, to whom it was referred, reported to the House of Representatives the following as a substitute:</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">'Sec. 6. That no officer, agent or employee of the United      States, while engaged in the enforcement of this act, the      National Prohibition Act, or any law in reference to the      manufacture or taxation of, or traffic in, intoxicating      liquor, shall search any private dwelling without a warrant      directing such search, and no such warrant shall issue unless      there is reason to believe such dwelling is used as a place      in which liquor is manufactured for sale or sold. The term      'private dwelling' shall be construed to include the room or      rooms occupied not transiently, but solely as a residence in      an apartment house, hotel, or boarding house. Any violation      of any provision of this paragraph shall be punished by a      fine of not to exceed $1,000 or imprisonment not to exceed      one year, or both such fine and imprisonment, in the      discretion of the court.'</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">In its report the committee spoke in part as follows:</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">'It appeared to the committee that the effect of the Senate      amendment No. 32, if agreed to by the House, would greatly      cripple the enforcement of the National Prohibition Act and      would otherwise seriously interfere with the government in      the enforcement of many other laws, as its scope is not      limited to the prohibition law, but applies equally to all laws where prompt action is      necessary. There are on the statute books of the United      States a number of laws authorizing search without a search      warrant. Under the common law and agreeable to the      Constitution search may in many cases be legally made without      a warrant. The Constitution does not forbid search, as some      parties contend, but it does forbid unreasonable search. This      provision in regard to search is as a rule contained in the      various state Constitutions, but notwithstanding that fact      search without a warrant is permitted in many cases, and      especially is that true in the enforcement of liquor      legislation.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">'The Senate amendment prohibits all search or attempt to      search any property or premises without a search warrant. The      effect of that would necessarily be to prohibit all search,      as no search can take place if it is not on some property or      premises.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">'Not only does this amendment prohibit search of any lands      but it prohibits the search of all property. It will prevent      the search of the common bootlegger and his stock in trade,      though caught and arrested in the act of violating the law.      But what is perhaps more serious, it will make it impossible      to stop the rum-running automobiles engaged in like illegal      traffic. It would take from the officers the power that they      absolutely must have to be of any service, for if they cannot      search for liquor without a warrant they might as well be      discharged. It is impossible to get a warrant to stop an      automobile. Before a warrant could be secured the automobile      would be beyond the reach of the officer with its load of      illegal liquor disposed of.'</p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">The conference report resulted, so far as the difference between the two houses was concerned, in providing for the punishment of any officer, agent, or employee of the government who searches a 'private dwelling' without a warrant, and for the punishment of any such officer, etc., who searches any 'other building or property' where, and only where, he makes the search without a warrant 'maliciously and without probable cause.' In other words, it left the way open for searching an automobile or vehicle of transportation without a warrant, if the search was not malicious or without probable cause.</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">The intent of Congress to make a distinction between the necessity for a search warrant in the searching of private dwellings and in that of automobiles and other road vehicles in the enforcement of the Prohibition Act is thus clearly established by the legislative history of the Stanley Amendment. Is such a distinction consistent with the Fourth Amendment? We think that it is, The Fourth Amendment does not denounce all searches or seizures, but only such as are unreasonable.</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">The leading case on the subject of search and seizure is Boyd v. United States, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">6 S. Ct. 524</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">29 L. Ed. 746</a></span>. An Act of Congress of June 22, 1874 (<span class="citation no-link">18 Stat. 187</span>), authorized a court of the United States in revenue cases, on motion of the government attorney, to require the defendant to produce in court his private books, invoices, and papers on pain in case of refusal of having the allegations of the attorney in his motion taken as confessed. This was held to be unconstitutional and void as applied to suits for penalties or to establish a forfeiture of goods, on the ground that under the Fourth Amendment the compulsory production of invoices to furnish evidence for forfeiture of goods constituted an unreasonable search even where made upon a search warrant, and was also a violation of the Fifth Amendment, in that it compelled the defendant in a criminal case to produce evidence against himself or be in the attitude of confessing his guilt.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">In Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S. Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L. Ed. 652</a></span>, L. R. A. 1915B, 834, Ann. Cas. 1915C, 1177, it was held that a court in a criminal prosecution could not retain letters of the accused seized in his house, in his absence and without his authority, by a United States marshal holding no warrant for his arrest and none for the search of his premises, to be used as evidence against him, the accused having made timely application to the court for an order for the return of the letters.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">In Silverthorne Lumber Co. v. United States, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">40 S. Ct. 182</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">64 L. Ed. 319</a></span>, a writ of error was brought to reverse a judgment of contempt of the District Court, fining the company and imprisoning one Silverthorne, its president, until he should purge himself of contempt in not producing books and documents of the company before the grand jury to prove violation of the statutes of the United States by the company and Silverthorne. Silverthorne had been arrested, and while under arrest the marshal had gone to the office of the company without a warrant and made a clean sweep of all books, papers, and documents found there and had taken copies and photographs of the papers. The District Court ordered the return of the originals, but impounded the photographs and copies. This was held to be an unreasonable search of the property and possessions of the corporation and a violation of the Fourth Amendment and the judgment for contempt was reversed.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">In Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">41 S. Ct. 261</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L. Ed. 647</a></span>, the obtaining through stealth by a representative of the government from the office of one suspected of defrauding the government of a paper which had no pecuniary value in itself, but was only to be used as evidence against its owner, was held to be a violation of the Fourth Amendment. It was further held that when the paper was offered in evidence and duly objected to it must be ruled inadmissible because obtained through an unreasonable search and seizure and also in violation of the Fifth Amendment because working compulsory incrimination.</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">In Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S. Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L. Ed. 654</a></span>, it was held that where concealed liquor was found by government officers without a search warrant in the home of the defendant, in his absence, and after a demand made upon his wife, it was inadmissible as evidence against the defendant, because acquired by an unreasonable seizure.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">In none of the cases cited is there any ruling as to the validity under the Fourth Amendment of a seizure without a warrant of contraband goods in the course of transportation and subject to forfeiture or destruction.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">On reason and authority the true rule is that if the search and seizure without a warrant are made upon probable cause, that is, upon a belief, reasonably arising out of circumstaces known to the seizing officer, that an automobile or other vehicle contains that which by law is subject to seizure and destruction, the search and seizure are valid. The Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted, and in a manner which will conserve public interests as well as the interests and rights of individual citizens.</p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">In Boyd v. United States, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">6 S. Ct. 524</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">29 L. Ed. 746</a></span>, as already said, the decision did not turn on whether a reasonable search might be made without a warrant; but for the purpose of showing the principle on which the Fourth Amendment proceeds, and to avoid any misapprehension of what was decided, the court, speaking through Mr. Justice Bradley, used language which is of particular significance and applicability here. It was there said (page 623 [<span class="citation no-link">6 S. Ct. 528</span>]):</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">'The search for and seizure of stolen or forfeited goods, or      goods liable to duties and concealed to avoid the payment      thereof, are totally different things from a search for and      seizure of a man's private books and papers for the purpose      of obtaining information therein contained, or of using them      as evidence against him. The two things differ toto coelo. In      the one case, the government is entitled to the possession of      the property; in the other it is not. The seizure of stolen      goods is authorized by the common law; and the seizure of goods forfeited for a breach      of the revenue laws, or concealed to avoid the duties payable      on them, has been authorized by English statutes for at least      two centuries past; and the like seizures have been      authorized by our own revenue acts from the commencement of      the government. The first statute passed by Congress to      regulate the collection of duites, the Act of July 31, 1789,      <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. As this      act was passed by the same Congress which proposed for      adoption the original amendments to the Constitution, it is      clear that the members of that body did not regard searches      and seizures of this kind as 'unreasonable,' and they are not      embraced within the prohibition of the amendment. So, also,      the supervision authorized to be exercised by officers of the      revenue over the manufacture or custody of excisable      articles, and the entries thereof in books required by law to      be kept for their inspection, are necessarily excepted out of      the category of unreasonable searches and seizures. So, also,      the laws which provide for the search and seizure of articles      and things which it is unlawful for a person to have in his      possession for the purpose of issue or disposition, such as      counterfeit coin, lottery tickets, implements of gambling,      etc., are not within this category. Common-welath v. Dana, 2      Metc. (Mass.) 329. Many other things of this character might      be enumerated.'</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">It is noteworthy that the twenty-fourth section of the act of 1789 to which the court there refers provides:</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">'That every collector, naval officer and surveyor, or other      person specially appointed by either of them for that      purpose, shall have full power and authority, to enter any      ship or vessel, in which they shall have reason to suspect      any goods, wares or merchandise subject to duty shall be      concealed; and therein to search for, seize, and secure any      such goods, wares or merchandise; and if they shall have      cause to suspect a concealment thereof, in any particular dwelling house, store, building, or other place,      they or either of them shall, upon application on oath or      affirmation to any justice of the peace, be entitled to a      warrant to enter such house, store, or other place (in the      daytime only) and there to search for such goods, and if any      shall be found, to seize and secure the same for trial; and      all such goods, wares and merchandise, on which the duties      shall not have been paid or secured, shall be forfeited.' <span class="citation no-link">1      Stat. 43</span>.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">Like provisions were contained in the Act of August 4, 1790, c. 35, &#167;&#167; 48-51, <span class="citation no-link">1 Stat. 145</span>, 170; in section 27 of the Act of February 18, 1793, c. 8, <span class="citation no-link">1 Stat. 305</span>, 315; and in sections 68-71 of the Act of March 2, 1799, c. 22, <span class="citation no-link">1 Stat. 627</span>, 677, 678.</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">Thus contemporaneously with the adoption of the Fourth Amendment we find in the First Congress, and in the following Second and Fourth Congresses, a difference made as to the necessity for a search warrant between goods subject to forfeiture, when concealed in a dwelling house or similar place, and like goods in course of transportation and concealed in a movable vessel where they readily could be put out of reach of a search warrant. Compare Hester v. United States, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">44 S. Ct. 445</a></span>, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">68 L. Ed. 898</a></span>.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">Again, by the second section of the Act of March 3, 1815, <span class="citation no-link">3 Stat. 231</span>, 232, it was made lawful for customs officers, not only to board and search vessels within their own and adjoining districts, but also to stop, search, and examine any vehicle, beast, or person on which or whom they should suspect there was merchandise which was subject to duty or had been introduced into the United States in any manner contrary to law, whether by the person in charge of the vehicle or beast or otherwise, and if they should find any goods, wares or merchandise thereon, which they had probable cause to believe had been so unlawfully brought into the country, to seize and secure the same, and the vehicle or beast as well, for trial and forfeiture. This act was renewed April 27, 1816 (<span class="citation no-link">3 Stat. 315</span>), for a year and expired. The Act of February 28, 1865, revived section 2 of the Act of 1815, above described, <span class="citation no-link">13 Stat. 441</span>, c. 67. The substance of this section was re-enacted in the third section of the Act of July 18, 1866, c. 201, <span class="citation no-link">14 Stat. 178</span>, and was thereafter embodied in the Revised Statutes as section 3061 (Comp. St. &#167; 5763). Neither section 3061 nor any of its earlier counterparts has ever been attacked as unconstitutional. Indeed, that section was referred to and treated as operative by this court in Cotzhausen v. Nazro, <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/#219" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215, 219</a></span>, <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">2 S. Ct. 503</a></span>, <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">27 L. Ed. 540</a></span>. See, also, United States v. One Black Horse (D C.) <span class="citation" data-id="8754123"><a href="/opinion/8770588/united-states-v-one-black-horse/" aria-description="Citation for case: United States v. One Black Horse">129 F. 167</a></span>.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">Again by section 2140 of the Revised Statutes (Comp. St. &#167; 4141) any Indian agent, subagent or commander of a military post in the Indian country, having reason to suspect or being informed that any white person or Indian is about to introduce, or has introduced, any spirituous liquor or wine into the Indian country, in violation of law, may cause the boats, stores, packages, wagons, sleds and places of deposit of such person to be searched and if any liquor is found therein, then it, together with the vehicles, shall be seized and and proceeded against by libel in the proper court and forfeited. Section 2140 was the outgrowth of the Act of May 6, 1822, c. 58, <span class="citation no-link">3 Stat. 682</span>, authorizing Indian agents to cause the goods of traders in the Indian country to be searched upon suspicion or information that ardent spirits were being introduced into the Indian country to be seized and forfeited if found, and of the Act of June 30, 1834, &#167; 20, c. 161, <span class="citation no-link">4 Stat. 729</span>, 732, enabling an Indian agent having reason to suspect any person of having introduced or being about to introduce liquors into the Indian country to cause the boat, stores or places of deposit of such person to be searched and the liquor found forfeited. This court recognized the statute of 1822 as justifying such a search and seizure in American Fur Co. v. United States, <span class="citation" data-id="85637"><a href="/opinion/85637/sundry-goods-wares-merchandises-v-united-states/" aria-description="Citation for case: Sundry Goods, Wares &amp; Merchandises v. United States">2 Pet. 358</a></span>, <span class="citation" data-id="85637"><a href="/opinion/85637/sundry-goods-wares-merchandises-v-united-states/" aria-description="Citation for case: Sundry Goods, Wares &amp; Merchandises v. United States">7 L. Ed. 450</a></span>. By the Indian Appropriation Act of March 2, 1917, c. 146, <span class="citation no-link">39 Stat. 969</span>, 970, automobiles used in introducing or attempting to introduce intoxicants into the Indian territory may be seized, libeled, and forfeited as provided in the Revised Statutes, &#167; 2140.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">And again in Alaska, by section 174 of the Act of March 3, 1899, c. 429, <span class="citation no-link">30 Stat. 1253</span>, 1280, it is provided that collectors and deputy collectors or any person authorized by them in writing shall be given power to arrest persons and seize vessels and merchandise in Alaska liable to fine, penalties, or forfeiture under the act and to keep and deliver the same, and the Attorney General, in construing the act, advised the government:</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">'If your agents reasonably suspect that a violation of law      has occurred, in my opinion they have power to search any      vessel within the three-mile limit according to the practice      of customs officers when acting under section 3059 of the      Revised Statutes [Comp. St. &#167; 5761], and to seize such      vessels.' 26 Op. Attys. Gen. 243.</p>
    </div>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">We have made a somewhat extended reference to these statutes to show that the guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the government, as recognizing a necessary difference between a search of a store, dwelling house, or other structure in respect of which a proper official warrant readily may be obtained and a search of a ship, motor boat, wagon, or automobile for contraband goods, where it is not practicable to secure a warrant, because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">Having thus established that contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant, we come now to consider under what circumstances such search may be made. It would be intolerable and unreasonable if a prohibition agent were authorized to stop every automobile on the chance of finding liquor, and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. Travelers may be so stopped in crossing an international boundary because of national self-protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in. But those lawfully within the country, entitled to use the public highways, have a right to free passage without interruption or search unless there is known to a competent official, authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise. Section 26, title 2, of the National Prohibition Act, like the second section of the act of 1789, for the searching of vessels, like the provisions of the act of 1815, and section 3601, Revised Statutes, for searching vehicles for smuggled goods, and like the act of 1822, and that of 1834 and section 2140, R. S., and the act of 1917 for the search of vehicles and automobiles for liquor smuggled into the Indian country, was enacted primarily to accomplish the seizure and destruction of contraband goods; secondly, the automobile was to be forfeited; and, thirdly, the driver was to be arrested. Under section 29, title 2, of the act the latter might be punished by not more than $500 fine for the first offense, not more than $1,000 fine and 90 days' imprisonment for the second offense, and by a fine of $500 or more and by not more than 2 years' imprisonment for the third offense. Thus he is to be arrested for a misdemeanor for his first and second offenses, and for a felony if he offends the third time.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">The main purpose of the act obviously was to deal with the liquor and its transportation, and to destroy it. The mere manufacture of liquor can do little to defeat the policy of the Eighteenth Amendment and the Prohibition Act, unless the for bidden product can be distributed for illegal sale and use. Section 26 was intended to reach and destroy the forbidden liquor in transportation and the provisions for forfeiture of the vehicle and the arrest of the transporter were incidental. The rule for determining what may be required before a seizure may be made by a competent seizing official is not to be determined by the character of the penalty to which the transporter may be subjected. Under section 28, title 2, of the Prohibition Act, the Commissioner of Internal Revenue, his assistants, agents and inspectors are to have the power and protection in the enforcement of the act conferred by the existing laws relating to the manufacture or sale of intoxicating liquors. Officers who seize under section 26 of the Prohibition Act are therefore protected by section 970 of the Revised Statutes (Comp. St. &#167; 1611), providing that:</p>
    </div>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">'When, in any prosecution commenced on account of the seizure      of any vessel, goods, wares, or merchandise, made by any      collector or other officer, under any act of Congress      authorizing such seizure, judgment is rendered for the      claimant, but it appears to the court that there was      reasonable cause of seizure, the court shall cause a proper      certificate thereof to be entered, and the claimant shall      not, in such case, be entitled to costs, nor shall the person      who made the seizure, nor the prosecutor, be liable to suit      or judgment on account of such suit or prosecution: Provided,      that the vessel, goods, wares, or merchandise be, after      judgment, forthwith returned to such claimant or his agent.'</p>
    </div>
    <div class="num" id="p41">
      <span class="num">41</span>
      <p class="indent">It follows from this that, if an officer seizes an autombile or the liquor in it without a warrant, and the facts as subsequently developed do not justify a judgment of condemnation and forfeiture, the officer may escape costs or a suit for damages by a showing that he had reasonable or probable cause for the seizure. Stacey v. Emery, <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642</a></span>, <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">24 L. Ed. 1035</a></span>. The measure of legality of such a seizure is, therefore, that the seizing officer shall have reasonable or probable cause for believing that the antomobile which he stops and seizes has contraband liquor therein which is being illegally transported.</p>
    </div>
    <div class="num" id="p42">
      <span class="num">42</span>
      <p class="indent">We here find the line of distrinction between legal and illegal seizures of liquor in transport in vehicles. It is certainly a reasonable distinction. It gives the owner of an automobile or other vehicle seized under section 26, in absence of probable cause, a right to have restored to him the automobile, it protects him under the Weeks and Amos Cases from use of the liquor as evidence against him, and it subjects the officer making the seizures to damages. On the other hand, in a case showing probalbe cause, the government and its officials are given the opportunity which they should have, to make the investigation necessary to trace reasonably suspected contraband goods and to seize them.</p>
    </div>
    <div class="num" id="p43">
      <span class="num">43</span>
      <p class="indent">Such a rule fulfills the guaranty of the Fourth Amendment. In cases where the securing of a warrant is reasonably practicable, it must be used and when properly supported by affidavit and issued after judicial approval protects the seizing officer against a suit for damages. In cases where seizure is impossible except without warrant, the seizing officer acts unlawfully and at his peril unless he can show the court probable cause. United States v. Kaplan (D. C.) <span class="citation" data-id="8829037"><a href="/opinion/8843816/united-states-v-kaplan/#972" aria-description="Citation for case: United States v. Kaplan">286 F. 963, 972</a></span>.</p>
    </div>
    <div class="num" id="p44">
      <span class="num">44</span>
      <p class="indent">But we are pressed with the argument that if the search of the automobile discloses the presence of liquor and leads under the staute to the arrest of the person in charge of the automobile, the right of seizure should be limited by the common-law rule as to the circumstances justifying an arrest without a warrant for a misdemeanor. The usual rule is that a police officer may arrest without warrant one believed by the officer upon reasonable cause to have been guilty of a felony, and that he may only arrest without a warrant one guilty of a misdemeanor if committed in his presence. Kurtz v. Moffitt, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487</a></span>, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">6 S. Ct. 148</a></span>, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">29 L. Ed. 458</a></span>; John Bad Elk v. United States, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529</a></span>, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">20 S. Ct. 729</a></span>, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">44 L. Ed. 874</a></span>. The rule is sometimes expressed as follows:</p>
    </div>
    <div class="num" id="p45">
      <span class="num">45</span>
      <p class="indent">'In cases of misdemeanor, a peace officer like a private      person has at common law no power of arresting without a      warrant except when a breach of the peace has been committed      in his presence or there is reasonable ground for supposing      that a breach of peace is about to be committed or renewed in      his presence.' Halsbury's Laws of England, vol. 9, part. III,      612.</p>
    </div>
    <div class="num" id="p46">
      <span class="num">46</span>
      <p class="indent">The reason for arrest for misdemeanors without warrant at common law was promptly to suppress breaches of the peace (1 Stephen, History of Criminal Law, 193), while the reason for arrest without warrant on a reliable report of a felony was because the public safety and the due apprehension of criminals charged with heinous offenses required that such arrests should be made at once without warrant (Rohan v. Sawin, 5 Cush. [Mass.] 281). The argument for defendants is that, as the misdemeanor to justify arrest without warrant must be committed in the presence of the police officer, the offense is not committed in his presence unless he can by his senses detect that the liquor is being transported, no matter how reliable his previous information by which he can identify the automobile as loaded with it. Elrod v. Moss (C. C. A.) <span class="citation" data-id="8823999"><a href="/opinion/8838892/elrod-v-moss/" aria-description="Citation for case: Elrod v. Moss">278 F. 123</a></span>; Hughes v. State, <span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/" aria-description="Citation for case: Hughes v. State">145 Tenn. 544</a></span>, <span class="citation no-link">238 S. W. 588</span>, 20 A. L. R. 639.</p>
    </div>
    <div class="num" id="p47">
      <span class="num">47</span>
      <p class="indent">So it is that under the rule contended for by defendants the liquor if carried by one who has been already twice convicted of the same offense may be seized on information other than the senses, while if he has been only once convicted it may not be seized unless the presence of the liquor is detected by the senses as the automobile concealing it rushes by. This is certainly a very unsatisfactory line of difference when the main object of the section is to forfeit and suppress the liquor, the arrest of the individual being only incidental as shown by the lightness of the penalty. See Commonwealth v. Street, 3 Pa. Dist. and Co. Ct. Rep.783. In England at the common law the difference in punishment between felonies and misdemeanors was very great. Under our present federal statutes, it is much less important and Congress may exercise a relatively wide discretion in classing particular offenses as felonies or misdemeanors. As the main purpose of section 26 was seizure and forfeiture, it is not so much the owner as the property that offends. Agnew v. Haymes, <span class="citation" data-id="8758980"><a href="/opinion/8775358/agnew-v-haymes/#641" aria-description="Citation for case: Agnew v. Haymes">141 F. 631, 641</a></span>, <span class="citation" data-id="8758980"><a href="/opinion/8775358/agnew-v-haymes/" aria-description="Citation for case: Agnew v. Haymes">72 C. C. A. 325</a></span>. The language of the section provides for seizure when the officer of the law 'discovers' any one in the act of transporting the liquor by automobile or other vehicle. Certainly it is a very narrow and technical construction of this word which would limit it to what the officer sees, hears or smells as the automobile rolls by and excludes therefrom when he identifies the car the convincing information that he may previously have received as to the use being made of it.</p>
    </div>
    <div class="num" id="p48">
      <span class="num">48</span>
      <p class="indent">We do not think such a nice distinction is applicable in the present case. When a man is legally arrested for an offense, whatever is found upon his person or in his control which it is unlawful for him to have and which may be used to prove the offense may be seized and held as evidence in the prosecution. Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S. Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L. Ed. 652</a></span>, L. R. A. 1915B, 834, Ann. Cas. 1915C, 1177; Dillon v. O'Brien and Davis, 16 Cox, C. C. 245; Getchell v. Page, <span class="citation" data-id="4937159"><a href="/opinion/5118454/getchell-v-page/" aria-description="Citation for case: Getchell v. Page">103 Me. 387</a></span>, <span class="citation" data-id="4937159"><a href="/opinion/5118454/getchell-v-page/" aria-description="Citation for case: Getchell v. Page">69 A. 624</a></span>, 18 L. R. A. (N. S.) 253, <span class="citation no-link">125 Am. St. Rep. 307</span>; Kneeland v. Connally, <span class="citation" data-id="5560847"><a href="/opinion/5710842/kneeland-v-connally/" aria-description="Citation for case: Kneeland v. Connally">70 Ga. 424</a></span>; 1 Bishop, Criminal Procedure, &#167; 211; 1 Wharton, Criminal Procedure (10th Ed.) &#167; 97. The argument of defendants is based on the theory that the seizure in this case can only be thus justified. If their theory were sound, their conclusion would be. The validity of the seizure then would turn wholly on the validity of the arrest without a seizure. But the theory is unsound. The right to search and the validity of the seizure are not dependent on the right to arrest. They are dependent on the reasonable cause the seizing officer has for belief that the contents of the automobile offend against the law. The seizure in such a proceeding comes before the arrest as section 26 indicates. It is true that section 26, title 2, provides for immediate proceedings against the person arrested and that upon conviction the liquor is to be destroyed and the automobile or other vehicle is to be sold, with the saving of the interest of a lienor who does not know of its unlawful use; but it is evident that if the person arrested is ignorant of the contents of the vehicle, or if he escapes, proceedings can be had against the liquor for destruction or other disposition under section 25 of the same title. The character of the offense for which, after the contraband liquor is found and seized, the driver can be prosecuted does not affect the validity of the seizure.</p>
    </div>
    <div class="num" id="p49">
      <span class="num">49</span>
      <p class="indent">This conclusion is in keeping with the requirements of the Fourth Amendment and the principles of search and seizure of contraband forfeitable property; and it is a wise one because it leaves the rule one which is easily applied and understood and is uniform. Houck v. State, <span class="citation no-link">106 Ohio St. 195</span>, <span class="citation no-link">140 N. E. 112</span>, accords with this conclusion. Ash v. United States (C. C. A.) <span class="citation" data-id="9335932"><a href="/opinion/9340588/ash-v-states/" aria-description="Citation for case: Ash v. States">299 F. 277</a></span>, and Milam v. United States (C. C. A.) <span class="citation" data-id="8835196"><a href="/opinion/8849836/milam-v-united-states/" aria-description="Citation for case: Milam v. United States">296 F. 629</a></span>, decisions by the Circuit Court of Appeals for the Fourth Circuit take the same view. The Ash Case is very similar in its facts to the case at bar, and both were by the same court which decided Snyder v. United States (C. C. A.) <span class="citation" data-id="8828212"><a href="/opinion/8843002/snyder-v-united-states/" aria-description="Citation for case: Snyder v. United States">285 F. 1</a></span>, cited for the defendants. See, also, Park v. United States (1st C. C. A.) <span class="citation" data-id="8833538"><a href="/opinion/8848214/park-v-united-states/#783" aria-description="Citation for case: Park v. United States">294 F. 776, 783</a></span>, and Lambert v. United States (9th C. C. A.) <span class="citation" data-id="8826550"><a href="/opinion/8841368/lambert-v-united-states/" aria-description="Citation for case: Lambert v. United States">282 F. 413</a></span>.</p>
    </div>
    <div class="num" id="p50">
      <span class="num">50</span>
      <p class="indent">Finally, was there probable cause? In The Apollon, <span class="citation" data-id="85416"><a href="/opinion/85416/the-apollon/" aria-description="Citation for case: The Apollon.">9 Wheat. 362</a></span>, <span class="citation" data-id="85416"><a href="/opinion/85416/the-apollon/" aria-description="Citation for case: The Apollon.">6 L. Ed. 111</a></span>, the question was whether the seizure of a French vessel at a particular place was upon probable cause that she was there for the purpose of smuggling. In this discussion Mr. Justice Story, who delivered the judgment of the court, said (page 374):</p>
    </div>
    <div class="num" id="p51">
      <span class="num">51</span>
      <p class="indent">'It has been very justly observed at the bar that the court      is bound to take notice of public facts and geographical positions, and that this remote part of the country has been      infested, at different periods, by smugglers, is matter of      general notoriety, and may be gathered from the public      documents of the government.'</p>
    </div>
    <div class="num" id="p52">
      <span class="num">52</span>
      <p class="indent">We know in this way that Grand Rapids is about 152 miles from Detroit, and that Detroit and its neighborhood along the Detroit river, which is the international boundary, is one of the most active centers for introducing illegally into this country spirituous liquors for distribution into the interior. It is obvious from the evidence that the prohibition agents were engaged in a regular patrol along the important highways from Detroit to Grand Rapids to stop and seize liquor carried in automobiles. They knew or had convincing evidence to make them believe that the Carroll boys, as they called them, were so-called 'bootleggers' in Grand Rapids; i. e., that they were engaged in plying the unlawful trade of selling such liquor in that city. The officers had soon after noted their going from Grand Rapids half way to Detroit, and attempted to follow them to that city to see where they went, but they escaped observation. Two months later these officers suddenly met the same men on their way westward presumably from Detroit. The partners in the original combination to sell liquor in Grand Rapids were together in the same automobile they had been in the night when they tried to furnish the whisky to the officers, which was thus identified as part of the firm equipment. They were coming from the direction of the great source of supply for their stock to Grand Rapids, where they plied their trade. That the officers, when they saw the defendants, believed that they were carrying liquor, we can have no doubt, and we think it is equally clear that they had reasonable cause for thinking so. Emphasis is put by defendants' counsel on the statement made by one of the officers that they were not looking for defendants at the particular time when they appeared. We do not perceive that it has any weight. As soon as they did appear, the officers were entitled to use their reasoning faculties upon all the facts of which they had previous knowledge in respect to the defendants.</p>
    </div>
    <div class="num" id="p53">
      <span class="num">53</span>
      <p class="indent">The necessity for probable cause in justifying seizures on land or sea, in making arrests without warrant for past felonies, and in malicious prosecution and false imprisonment cases has led to frequent definition of the phrase. In Stacey v. Emery, <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span> (<span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">24 L. Ed. 1035</a></span>), a suit for damages for seizure by a collector, this court defined probable cause as follows:</p>
    </div>
    <div class="num" id="p54">
      <span class="num">54</span>
      <p class="indent">'If the facts and circumstances before the officer are such      as to warrant a man of prudence and caution in believing that      the offense has been committed, it is sufficient.'</p>
    </div>
    <div class="num" id="p55">
      <span class="num">55</span>
      <p class="indent">See Locke v. United States, <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">7 Cranch, 339</a></span>, <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">3 L. Ed. 364</a></span>; The George, <span class="citation" data-id="8631556"><a href="/opinion/8651731/the-george/" aria-description="Citation for case: The George">1 Mason, 24</a></span>, Fed. Cas. No. 5328; The Thompson, <span class="citation" data-id="87693"><a href="/opinion/87693/the-thompson/" aria-description="Citation for case: The Thompson">3 Wall. 155</a></span>, <span class="citation" data-id="87693"><a href="/opinion/87693/the-thompson/" aria-description="Citation for case: The Thompson">18 L. Ed. 55</a></span>.</p>
    </div>
    <div class="num" id="p56">
      <span class="num">56</span>
      <p class="indent">It was laid down by Chief Justice Shaw, in Commonwealth v. Carey, <span class="citation no-link">12 Cush. 246</span>, 251, that:</p>
    </div>
    <div class="num" id="p57">
      <span class="num">57</span>
      <p class="indent">'If a constable or other peace officer arrest a person      without a warrant, he is not bound to show in his      justification a felony actually committed, to render the      arrest lawful; but if he suspects one on his own knowledge of      facts, or on facts communicated to him by others, and      thereupon he has reasonable ground to believe that the      accused has been guilty of felony, the arrest is not      unlawful.' Commonwealth v. Phelps, <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">209 Mass. 396</a></span>, <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">95 N. E.      868</a></span>, Ann. Cas. 1912B, 566; Rohan v. Sawin, <span class="citation no-link">5 Cush. 281</span>, 285.</p>
    </div>
    <div class="num" id="p58">
      <span class="num">58</span>
      <p class="indent">In McCarthy v. De Armit, <span class="citation" data-id="6236987"><a href="/opinion/6368121/mccarthy-v-de-armit/" aria-description="Citation for case: McCarthy v. De Armit">99 Pa. 63</a></span>, the Supreme Court of Pennsylvania sums up the definition of probable cause in this way (page 69):</p>
    </div>
    <div class="num" id="p59">
      <span class="num">59</span>
      <p class="indent">'The substance of all the definitions is a reasonable ground      for belief of guilt.'</p>
    </div>
    <div class="num" id="p60">
      <span class="num">60</span>
      <p class="indent">In the case of the Director General v. Kastenbaum, <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">263 U. S. 25</a></span>, <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">44 S. Ct. 52</a></span>, <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">68 L. Ed. 146</a></span>, which was a suit for false imprisonment, it was said by this court (page 28 [<span class="citation no-link">44 S. Ct. 53</span>]):</p>
    </div>
    <div class="num" id="p61">
      <span class="num">61</span>
      <p class="indent">'But, as we have seen, good faith is not enough to constitute      probable cause. That faith must be grounded on facts within      knowledge of the Director General's agent, which in the judgment of the court would make his faith      reasonable.'</p>
    </div>
    <div class="num" id="p62">
      <span class="num">62</span>
      <p class="indent">See, also, Munn v. De Nemours, <span class="citation no-link">3 Wash. C. C. 37</span>, Fed. Cas. No. 9926.</p>
    </div>
    <div class="num" id="p63">
      <span class="num">63</span>
      <p class="indent">In the light of these authorities, and what is shown by this record, it is clear the officers here had justification for the search and seizure. This is to say that the facts and circumstances within their knowledge and of which they had reasonably trustworthy information were sufficient in themselves to warrant a man of reasonable caution in the belief that intoxicating liquor was being transported in the automobile which they stopped and searched.</p>
    </div>
    <div class="num" id="p64">
      <span class="num">64</span>
      <p class="indent">Counsel finally argue that the defendants should be permitted to escape the effect of the conviction because the court refused on motion to deliver them the liquor when, as they say, the evidence adduced on the motion was much less than that shown on the trial, and did not show probable cause. The record does not make it clear what evidence was produced in support of or against the motion. But, apart from this, we think the point is without substance here. If the evidence given on the trial was sufficient, as we think it was, to sustain the introduction of the liquor as evidence, it is immaterial that there was an inadequacy of evidence when application was made for its return. A conviction on adequate and admissible evidence should not be set aside on such a ground. The whole matter was gone into at the trial, so no right of the defendants was infringed.</p>
    </div>
    <div class="num" id="p65">
      <span class="num">65</span>
      <p class="indent">Counsel for the government contend that Kiro, the defendant who did not own the automobile, could not complain of the violation of the Fourth Amendment in the use of the liquor as evidence against him, whatever the view taken as to Carroll's rights. Our conclusion as to the whole case makes it unnecessary for us to discuss this aspect of it.</p>
    </div>
    <div class="num" id="p66">
      <span class="num">66</span>
      <p class="indent">The judgment is affirmed.</p>
    </div>
    <div class="num" id="p67">
      <span class="num">67</span>
      <p class="indent">Mr. Justice McKENNA, before his retirement, concurred in this opinion.</p>
    </div>
    <div class="num" id="p68">
      <span class="num">68</span>
      <p class="indent">The separate opinion of Mr. Justice McREYNOLDS.</p>
    </div>
    <div class="num" id="p69">
      <span class="num">69</span>
      <p class="indent">1. The damnable character of the 'bootlegger's' business should not close our eyes to the mischief which will surely follow any attempt to destroy it by unwarranted methods. 'To press forward to a great principle by breaking through every other great principle that stands in the way of its establishment; * * * in short, to procure an eminent good by means that are unlawful, is as little consonant to private morality as to public justice.' Sir William Scott, The Le Louis, 2 Dodson, 210, 257.</p>
    </div>
    <div class="num" id="p70">
      <span class="num">70</span>
      <p class="indent">While quietly driving an ordinary automobile along a much frequented public road, plaintiffs in error were arrested by federal officers without a warrant and upon mere suspicion ill-founded, as I think. The officers then searched the machine and discovered carefully secreted whisky, which was seized and thereafter used as evidence against plaintiffs in error when on trial for transporting intoxicating liquor contrary to the Volstead Act. <span class="citation no-link">41 Stat. 305</span>, c. 85. They maintain that both arrest and seizure were unlawful and that use of the liquor as evidence violated their constitutional rights.</p>
    </div>
    <div class="num" id="p71">
      <span class="num">71</span>
      <p class="indent">This is not a proceeding to forfeit seized goods; nor is it an action against the seizing officer for a tort. Cases like the following are not controlling: Crowell v. McFadon. <span class="citation" data-id="85059"><a href="/opinion/85059/crowell-and-others-v-mfadon/#98" aria-description="Citation for case: Crowell and Others v. M&#x27;fadon">8 Cranch, 94, 98</a></span>, <span class="citation" data-id="85059"><a href="/opinion/85059/crowell-and-others-v-mfadon/" aria-description="Citation for case: Crowell and Others v. M&#x27;fadon">3 L. Ed. 499</a></span>; United States v. 1960 Bags of Coffee, <span class="citation" data-id="9416272"><a href="/opinion/85079/united-states-v-1960-bags-of-coffee/#403" aria-description="Citation for case: United States v. 1960 Bags of Coffee">8 Cranch, 398, 403, 405</a></span>, <span class="citation" data-id="9416272"><a href="/opinion/85079/united-states-v-1960-bags-of-coffee/" aria-description="Citation for case: United States v. 1960 Bags of Coffee">3 L. Ed. 602</a></span>; Otis v. Watkins, <span class="citation" data-id="85121"><a href="/opinion/85121/otis-v-watkins/" aria-description="Citation for case: Otis v. Watkins">9 Cranch, 339</a></span>, <span class="citation" data-id="85121"><a href="/opinion/85121/otis-v-watkins/" aria-description="Citation for case: Otis v. Watkins">3 L. Ed. 752</a></span>; Gelston v. Hoyt, <span class="citation" data-id="8373743"><a href="/opinion/8403401/gelston-v-hoyt/#310" aria-description="Citation for case: Gelston v. Hoyt">3 Wheat. 246, 310, 318</a></span>, <span class="citation" data-id="8373743"><a href="/opinion/8403401/gelston-v-hoyt/" aria-description="Citation for case: Gelston v. Hoyt">4 L. Ed. 381</a></span>; Wood v. United States, <span class="citation" data-id="86221"><a href="/opinion/86221/wood-v-united-states/" aria-description="Citation for case: Wood v. United States">16 Pet. 342</a></span>, <span class="citation" data-id="86221"><a href="/opinion/86221/wood-v-united-states/" aria-description="Citation for case: Wood v. United States">10 L. Ed. 987</a></span>; Taylor v. United States, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/#205" aria-description="Citation for case: Taylor v. United States">3 How. 197, 205</a></span>, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">11 L. Ed. 559</a></span>. They turned upon express provisions of applicable acts of Congress; they did not involve the point now presented and afford little, if any, assistance toward its proper solution. The Volstead Act does not, in terms, authorize arrest or seizure upon mere suspicion.</p>
    </div>
    <div class="num" id="p72">
      <span class="num">72</span>
      <p class="indent">Whether the officers are shielded from prosecution or action by Rev. Stat. &#167; 970, is not important. That section does not undertake to deprive the citizen of any constitutional right or to permit the use of evidence unlawfully obtained. It does, however, indicate the clear understanding of Congress that probable cause is not always enough to justify a seizure.</p>
    </div>
    <div class="num" id="p73">
      <span class="num">73</span>
      <p class="indent">Nor are we now concerned with the question whether by apt words Congress might have authorized the arrest without a warrant. It has not attempted to do this. On the contrary, the whole history of the legislation indicates a fixed purpose not so to do. First and second violations are declared to be misdemeanors nothing more&#8212;and Congress, of course, understood the rule concerning arrests for such offenses. Whether different penalties should have been prescribed or other provisions added is not for us to inquire; nor do difficulties attending enforcement give us power to supplement the legislation.</p>
    </div>
    <div class="num" id="p74">
      <span class="num">74</span>
      <p class="indent">2. As the Volstead Act contains no definite grant of authority to arrest upon suspicion and without warrant for a first offense, we come to inquire whether such authority can be inferred from its provisions.</p>
    </div>
    <div class="num" id="p75">
      <span class="num">75</span>
      <p class="indent">Unless the statute which creates a misdemeanor contains some clear provision to the contrary, suspicion that it is being violated will not justify an arrest. Criminal statutes must be strictly construed and applied, in harmony with rules of the common law. United States v. Harris, <span class="citation" data-id="95241"><a href="/opinion/95241/united-states-v-harris/#310" aria-description="Citation for case: United States v. Harris">177 U. S. 305, 310</a></span>, <span class="citation" data-id="95241"><a href="/opinion/95241/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">20 S. Ct. 609</a></span>, <span class="citation" data-id="95241"><a href="/opinion/95241/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">44 L. Ed. 780</a></span>. And the well-settled doctrine is that an arrest for a misdemeanor may not be made without a warrant unless the offense is committed in the officer's presence.</p>
    </div>
    <div class="num" id="p76">
      <span class="num">76</span>
      <p class="indent">Kurtz v. Moffitt, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498</a></span>, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#152" aria-description="Citation for case: Kurtz v. Moffitt">6 S. Ct. 148, 152</a></span> (<span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">29 L. Ed. 458</a></span>):</p>
    </div>
    <div class="num" id="p77">
      <span class="num">77</span>
      <p class="indent">'By the common law of England, neither a civil officer nor a      private citizen had the right without a warrant to make an      arrest for a crime not committed in his presence, except in      the case of felony, and then only for the purpose of bringing the      offender before a civil magistrate.'</p>
    </div>
    <div class="num" id="p78">
      <span class="num">78</span>
      <p class="indent">John Bad Elk v. United States, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534</a></span>, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#731" aria-description="Citation for case: Bad Elk v. United States">20 S. Ct. 729, 731</a></span> (<span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">44 L. Ed. 874</a></span>):</p>
    </div>
    <div class="num" id="p79">
      <span class="num">79</span>
      <p class="indent">'An officer, at common law, was not authorized to make an      arrest without a warrant, for a mere misdemeanor not      committed in his presence.'</p>
    </div>
    <div class="num" id="p80">
      <span class="num">80</span>
      <p class="indent">Commonwealth v. Wright, <span class="citation" data-id="6424446"><a href="/opinion/6550711/commonwealth-v-wright/#158" aria-description="Citation for case: Commonwealth v. Wright">158 Mass. 149, 158</a></span>, <span class="citation" data-id="6424446"><a href="/opinion/6550711/commonwealth-v-wright/#85" aria-description="Citation for case: Commonwealth v. Wright">33 N. E. 82, 85</a></span> (19 L. R. A. 206, <span class="citation no-link">35 Am. St. Rep. 475</span>):</p>
    </div>
    <div class="num" id="p81">
      <span class="num">81</span>
      <p class="indent">'It is suggested that the statutory misdemeanor of having in      one's possession short lobsters with intent to sell them is a      continuing offence, which is being committed while such      possession continues, and that therefore an officer who sees      any person in possession of such lobsters with intent to sell      them can arrest such person without a warrant, as for a      misdemeanor committed in his presence. We are of opinion,      however, that for statutory misdemeanors of this kind, not      amounting to a breach of the peace, there is no authority in      an officer to arrest without a warrant, unless it is given by      statute. * * * The Legislature has often empowered officers      to arrest without a warrant for similar offenses, which      perhaps tends to show that, in its opinion, no such right      exists at common law.'</p>
    </div>
    <div class="num" id="p82">
      <span class="num">82</span>
      <p class="indent">Pinkerton v. Verberg, <span class="citation" data-id="7934479"><a href="/opinion/7981669/pinkerton-v-verberg/#584" aria-description="Citation for case: Pinkerton v. Verberg">78 Mich. 573, 584</a></span>, <span class="citation" data-id="7934479"><a href="/opinion/7981669/pinkerton-v-verberg/#582" aria-description="Citation for case: Pinkerton v. Verberg">44 N. W. 579, 582</a></span> (7 L. R. A. 507, <span class="citation no-link">18 Am. St. Rep. 473</span>):</p>
    </div>
    <div class="num" id="p83">
      <span class="num">83</span>
      <p class="indent">'Any law which would place the keeping and safe-conduct of      another in the hands of even a conservator of the peace,      unless for some breach of the peace committed in his      presence, or upon suspicion of felony, would be most      oppressive and unjust, and destroy all the rights which our      Constitution guarantees. These are rights which existed long      before our Constitution, and we have taken just pride in      their maintenance, making them a part of the fundamental law      of the land.' 'If persons can be restrained of their liberty,      and assaulted and imprisoned, under such circumstances,      without complaint or warrant, then there is no limit to the      power of a police officer.'</p>
    </div>
    <div class="num" id="p84">
      <span class="num">84</span>
      <p class="indent">3. The Volstead Act contains no provision which annuls the accepted common-law rule or discloses definite intent to authorize arrests without warrant for misdemeanors not committed in the officer's presence.</p>
    </div>
    <div class="num" id="p85">
      <span class="num">85</span>
      <p class="indent">To support the contrary view section 26 is relied upon.</p>
    </div>
    <div class="num" id="p86">
      <span class="num">86</span>
      <p class="indent">'When * * * any officer of the law shall discover any person      in the act of transporting in violation of the law,      intoxicating liquors in any wagon, buggy, automobile, water      or air craft, or other vehicle, it shall be his duty to seize      any and all intoxicating liquors found therein being      transported contrary to law. Whenever intoxicating liquors      transported or possessed illegally shall be seized by an      officer he shall take possession of the vehicle and team or      automobile, boat, air or water craft, or any other      conveyance, and shall arrest any person in charge thereof.'</p>
    </div>
    <div class="num" id="p87">
      <span class="num">87</span>
      <p class="indent">Let it be observed that this section has no special application to automobiles; it includes <i>any</i> vehicle&#8212;buggy, wagon, boat, or air craft. Certainly, in a criminal statute, always to be strictly construed, the words 'shall discover * * * in the act of transporting in violation of the law' cannot mean shall have reasonable cause to suspect or believe that such transportation is being carried on. To discover and to suspect are wholly different things. Since the beginning apt words have been used when Congress intended that arrests for misdemeanors or seizures might be made upon suspicion. It has studiously refrained from making a felony of the offense here charged; and it did not undertake by any apt words to enlarge the power to arrest. It was not ignorant of the established rule on the subject, and well understood how this could be abrogated, as plainly appears from statutes like the following:</p>
    </div>
    <div class="num" id="p88">
      <span class="num">88</span>
      <p class="indent">'An act to regulate the collection of duties on imports and      tonnage,' approved March 2, 1789, <span class="citation no-link">1 Stat. 627</span>, 677, 678, c.      22; 'An act to provide more effectually for the collection of      the duties imposed by law on goods, wares and merchandise      imported into the United States, and on the tonnage of ships or      vessels,' approved August 4, 1790, <span class="citation no-link">1 Stat. 145</span>, 170, c. 35;      'An act further to provide for the collection of duties on      imports and tonnage,' approved March 3, 1815, <span class="citation no-link">3 Stat. 231</span>,      232, c. 94.</p>
    </div>
    <div class="num" id="p89">
      <span class="num">89</span>
      <p class="indent">These and similar acts definitely empowered officers to seize upon suspicion and therein radically differ from the Volstead Act, which authorized no such thing.</p>
    </div>
    <div class="num" id="p90">
      <span class="num">90</span>
      <p class="indent">'An act supplemental to the National Prohibition Act,' approved November 23, 1921, <span class="citation no-link">42 Stat. 222</span>, 223, c. 134, provides:</p>
    </div>
    <div class="num" id="p91">
      <span class="num">91</span>
      <p class="indent">'That any officer, agent, or employee of the United States      engaged in the enforcement of this act, or the National      Prohibition Act, or any other law of the United States, who      shall search any private dwelling as defined in the National      Prohibition Act, and occupied as such dwelling, without a      warrant directing such search, or who while so engaged shall      without a search warrant maliciously and without reasonable      cause search any other building or property, shall be guilty      of a misdemeanor and upon conviction thereof shall be fined      for a first offense not more than $1,000, and for a      subsequent offense not more than $1,000 or imprisoned not      more than one year, or both such fine and imprisonment.'</p>
    </div>
    <div class="num" id="p92">
      <span class="num">92</span>
      <p class="indent">And it is argued that the words and history of this section indicate the intent of Congress to distinguish between the necessity for warrants in order to search private dwelling and the right to search automobiles without one. Evidently Congress regarded the searching of private dwellings as matter of much graver consequence than some other searches and distinguished between them by declaring the former criminal. But the connection between this distinction and the legality of plaintiffs in error's arrest is not apparent. Nor can I find reason for inquiring concerning the validity of the distinction under the Fourth Amendment. Of course, the distinction is valid, and so are some seizures. But what of it? The act made nothing legal which theretofore was unlawful, and to conclude that by declaring the unauthorized search of a private dwelling criminal Congress intended to remove ancient restrictions from other searches and from arrests as well, would seem impossible.</p>
    </div>
    <div class="num" id="p93">
      <span class="num">93</span>
      <p class="indent">While the Fourth Amendment denounces only unreasonable seizures unreasonableness often depends upon the means adopted. Here the seizure followed an unlawful arrest, and therefore became itself unlawful&#8212;as plainly unlawful as the seizure within the home so vigorously denounced in Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391, 392, 393</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S. Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L. Ed. 652</a></span>, L. R. A. 1915B, 834, Ann. Cas. 1915C, 1177.</p>
    </div>
    <div class="num" id="p94">
      <span class="num">94</span>
      <p class="indent">In Snyder v. United States, <span class="citation" data-id="8828212"><a href="/opinion/8843002/snyder-v-united-states/#2" aria-description="Citation for case: Snyder v. United States">285 F. 1, 2</a></span>, the Court of Appeals, Fourth Circuit, rejected evidence obtained by an unwarranted arrest, and clearly announced some very wholesome doctrine:</p>
    </div>
    <div class="num" id="p95">
      <span class="num">95</span>
      <p class="indent">'That an officer may not make an arrest for a misdemeanor not      committed in his presence, without a warrant, has been so      frequently decided as not to require citation of authority.      It is equally fundamental that a citizen may not be arrested      on suspicion of having committed a misdemeanor and have his      person searched by force, without a warrant of arrest. If,      therefore, the arresting officer in this case had no other      justification for the arrest than the mere suspicion that a      bottle, only the neck of which he could see protruding from      the pocket of defendant's coat, contained intoxicating      liquor, then it would seem to follow without much question      that the arrest and search, without first having secured a      warrant, were illegal. And that his only justification was      his suspicion is admitted by the evidence of the arresting      officer himself. If the bottle had been empty or if it had      contained any one of a dozen innoxious liquids, the act of      the officer would, admittedly, have been an unlawful invasion      of the personal liberty of the defendant. That it happened in      this instance to contain whisky, we think, neither justifies the assault nor condemns the principle      which makes such an act unlawful.'</p>
    </div>
    <div class="num" id="p96">
      <span class="num">96</span>
      <p class="indent">The validity of the seizure under consideration depends on the legality of the arrest. This did not follow the seizure, but the reverse is true. Plaintiffs in error were first brought within the officers' power, and, while therein, the seizure took place. If an officer, upon mere suspicion of a misdemeanor, may stop one on the public highway, take articles away from him and thereafter use them as evidence to convict him of crime, what becomes of the Fourth and Fifth Amendments?</p>
    </div>
    <div class="num" id="p97">
      <span class="num">97</span>
      <p class="indent">In Weeks v. United States, supra, through Mr. Justice Day, this court said:</p>
    </div>
    <div class="num" id="p98">
      <span class="num">98</span>
      <p class="indent">'The effect of the Fourth Amendment is to put the courts of      the United States and federal officials, in the exercise of      their power and authority, under limitations and restraints      as to the exercise of such power and authority, and to      forever secure the people, their persons, houses, papers and      effects against all unreasonable searches and seizures under      the guise of law. This protection reaches all alike, whether      accused of crime or not, and the duty of giving to it force      and effect is obligatory upon all entrusted under our federal      system with the enforcement of the laws. The tendency of      those who execute the criminal laws of the country to obtain      conviction by means of unlawful seizures and enforced      confessions, the latter often obtained after subjecting      accused persons to unwarranted practices destructive of      rights secured by the federal Constitution, should find no      sanction in the judgments of the courts which are charged at      all times with the support of the Constitution and to which      people of all conditions have a right to appeal for the      maintenance of such fundamental rights. * * * The efforts of      the courts and their officials to bring the guilty to      punishment, praiseworthy as they are, are not to be aided by      the sacrifice of those great principles established by years      of endeavor and suffering which have resulted in their embodiment in the fundamental law of the      land.'</p>
    </div>
    <div class="num" id="p99">
      <span class="num">99</span>
      <p class="indent">Silverthorne Lumber Co. v. United States, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 391</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">40 S. Ct. 182</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">64 L. Ed. 319</a></span>:</p>
    </div>
    <div class="num" id="p100">
      <span class="num">100</span>
      <p class="indent">'The proposition could not be presented more nakedly. It is      that although of course its seizure was an outrage which the      government now regrets, it may study the papers before it      returns them, copy them, and then may use the knowledge that      it has gained to call upon the owners in a more regular form      to produce them; that the protection of the Constitution      covers the physical possession but not any advantages that      the government can gain over the object of its pursuit by      doing the forbidden act. Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S.      383</a></span>, to be sure, had established that laying the papers      directly before the grand jury was unwarranted, but it is      taken to mean only that two steps are required instead of      one. In our opinion such is not the law. It reduces the      Fourth Amendment to a form of words. <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 393</a></span>. The      essence of a provision forbidling the acquisition of evidence      in a certain way is that not merely evidence so acquired      shall not be used before the court but that it shall not be      used at all. Of course this does not mean that the facts thus      obtained become sacred and inaccessible. If knowledge of them      is gained from an independent source they may be proved like      any others, but the knowledge gained by the government's own      wrong cannot be used by it in the way proposed.'</p>
    </div>
    <div class="num" id="p101">
      <span class="num">101</span>
      <p class="indent">Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">41 S. Ct. 261</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L. Ed. 647</a></span>, and Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S. Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L. Ed. 654</a></span>, distinctly point out that property procured by unlawful action of federal officers cannot be introduced as evidence.</p>
    </div>
    <div class="num" id="p102">
      <span class="num">102</span>
      <p class="indent">The arrest of plaintiffs in error was unauthorized, illegal, and violated the guaranty of due process given by the Fifth Amendment. The liquor offered in evidence was obtained by the search which followed this arrest and was therefore obtained in violation of their constitutional rights. Articles found upon or in the control of one lawfully arrested may be used as evidence for certain purposes, but not at all when secured by the unlawful action of a federal officer.</p>
    </div>
    <div class="num" id="p103">
      <span class="num">103</span>
      <p class="indent">4. The facts known by the officers who arrested plaintiffs in error were wholly insufficient to create a reasonable belief that they were transporting liquor contrary to law. These facts were detailed by Fred Cronenwett, chief prohibition officer. His entire testimony as given at the trial follows:</p>
    </div>
    <div class="num" id="p104">
      <span class="num">104</span>
      <p class="indent">'I am in charge of the federal prohibition department in this      district. I am acquainted with these two respondents, and      first saw them on September 29, 1921, in Mr. Scully's      apartment on Oakes street, Grand Rapids. There were three of      them that came to Mr. Scully's apartment, one by the name of      Kruska, George Krio, and John Carroll. I was introduced to      them under the name of Stafford, and told them I was working      for the Michigan Chair Company, and wanted to buy three cases      of whisky, and the price was agreed upon. After they thought      I was all right, they said they would be back in half or      three-quarters of an hour; that they had to go out to the      east end of Grand Rapids to get this liquor. They went away      and came back in a short time, and Mr. Kruska came upstairs      and said they couldn't get it that night; that a fellow by      the name of Irving, where they were going to get it, wasn't      in, but they were going to deliver it the next day, about      ten. They didn't deliver it the next day. I am not positive      about the price. It seems to me it was around $130 a case. It      might be $135. Both respondents took part in this      conversation. When they came to Mr. Scully's apartment they      had this same car. While it was dark and I wasn't able to get      a good look at this car, later, on the 6th day of October,      when I was out on the road with Mr. Scully, I was waiting on      the highway while he went to Reed's Lake to get a light lunch, and they drove by, and I had their license number and      the appearance of their car, and knowing the two boys, seeing      them on the 29th day of September, I was satisfied when I      seen the car on December 15th it was the same car I had seen      on the 6th day of October. On the 6th day of October it was      probably twenty minutes before Scully got back to where I      was. I told him the Carroll boys had just gone toward Detroit      and we were trying to catch up with them and see where they      were going. We did catch up with them somewhere along by Ada,      just before we got to Ada, and followed them to East Lansing.      We gave up the chase at East Lansing.</p>
    </div>
    <div class="num" id="p105">
      <span class="num">105</span>
      <p class="indent">'On the 15th of December, when Peterson and Scully and I      overhauled this car on the road, it was in the country, on      Pike 16, the road leading between Grand Rapids and Detroit.      When we passed the car we were going toward Ionia, or      Detroit, and the Kiro and Carroll boys were coming towards      Grand Rapids when Mr. Scully and I recognized them and said,      'There goes the Carroll brothers,' and we went on still      further in the same direction we were going and turned around      and went back to them&#8212;drove up to the side of them. Mr.      Scully was driving the car; I was sitting in the front seat,      and I stepped out on the running board and held out my hand      and said, 'Carroll, stop that car,' and they did stop it.      John Kiro was driving the car. After we got them stopped, we      asked them to get out of the car, which they did. Carroll      referred to me, and called me by the name of 'Fred,' just as      soon as I got up to him. Raised up the back part of the      roadster; didn't find any liquor there; then raised up the      cushion; then I struck at the lazyback of the seat and it was      hard. I then started to open it up, and I did tear the      cushion some, and Carroll said, 'Don't tear the cushion; we      have only got six cases in there;' and I took out two bottles      and found out it was liquor; satisfied it was liquor. Mr.      Peterson and a fellow by the name of Gerald Donker came in with the two Carroll boys and      the liquor and the car to Grand Rapids. They brought the two      defendants and the car and the liquor to Grand Rapids. I and      the other men besides Peterson stayed out on the road,      looking for other cars that we had information were coming      in. There was conversation between me and Carroll before      Peterson started for town with the defendants. Mr. Carroll      said, 'Take the liquor, and give us one more chance, and I      will make it right with you.' At the same time he reached in      one of his trousers pockets and pulled out money; the amount      of it I don't know. I wouldn't say it was a whole lot. I saw      a $10 bill and there was some other bills; I don't know how      much there was; it wasn't a large amount.</p>
    </div>
    <div class="num" id="p106">
      <span class="num">106</span>
      <p class="indent">'As I understand, Mr. Hanley helped carry the liquor from the      car. On the next day afterwards, we put this liquor in boxes,      steel boxes, and left it in the marshal's vault, and it is      still there now. Mr. Hanley and Chief Deputy Johnson, some of      the agents and myself were there. Mr. Peterson was there the      next day that the labels were signed by the different      officers; those two bottles, Exhibits A and B.</p>
    </div>
    <div class="num" id="p107">
      <span class="num">107</span>
      <p class="indent">'Q. Now, those two bottles, Exhibits A and B, were those the      two bottles you took out of the car out there, or were those      two bottles taken out of the liquor after it got up here? A.      We didn't label them out on the road; simply found it was      liquor and sent it in; and this liquor was in Mr. Hanley's      custody that evening and during the middle of the next day      when we checked it over to see the amount of liquor that was      there. Mr. Johnson and I sealed the bottles, and Mr.      Johnson's name is on the label that goes over the bottle with      mine, and this liquor was taken out of the case to-day. It      was taken out for the purpose of analyzation. The others were      not broken until to-day.</p>
    </div>
    <div class="num" id="p108">
      <span class="num">108</span>
      <p class="indent">'Q. And are you able to tell us, from the label and from           the bottles, whether it is part of the same liquor taken           out of that car? A. It has the appearance of it; yes,           sir. Those are the bottles that were in there that Mr.           Hanley said was gotten out of the Carroll car.'</p>
    </div>
    <p class="indent">Cross-examination:</p>
    <div class="num" id="p109">
      <span class="num">109</span>
      <p class="indent">'I think I was the first one to get back to the Carroll car      after it was stopped. I had a gun in my pocket; I didn't      present it. I was the first one to the car and raised up the      back of the car, but the others were there shortly afterward.      We assembled right around the car immediately.</p>
    </div>
    <div class="num" id="p110">
      <span class="num">110</span>
      <p class="indent">'Q. And whatever examination and what investigation you made      you went right ahead and did it in your own way? A. Yes, sir.</p>
    </div>
    <div class="num" id="p111">
      <span class="num">111</span>
      <p class="indent">'Q. And took possession of it, arrested them, and brought      them in? A. Yes, sir.</p>
    </div>
    <div class="num" id="p112">
      <span class="num">112</span>
      <p class="indent">'Q. And at that time, of course, you had no search warrant?      A. No, sir. We had no knowledge that this car was coming      through at that particular time.'</p>
    </div>
    <p class="indent">Redirect examination:</p>
    <div class="num" id="p113">
      <span class="num">113</span>
      <p class="indent">'The lazyback was awfully hard when I struck it with my fist.      It was harder than upholstery ordinarily is in those backs; a      great deal harder. It was practically solid. Sixty-nine      quarts of whisky in one lazyback.'</p>
    </div>
    <div class="num" id="p114">
      <span class="num">114</span>
      <p class="indent">The negotiation concerning three cases of whisky on September 29th was the only circumstance which could have subjected plaintiffs in error to any reasonable suspicion. No whisky was delivered, and it is not certain that they ever intended to deliver any. The arrest came 2 1/2 months after the negotiation. Every act in the meantime is consistent with complete innocence. Has it come about that merely because a man once agreed to deliver whisky, but did not, he may be arrested whenever thereafter he ventures to drive an automobile on the road to Detroit!</p>
    </div>
    <div class="num" id="p115">
      <span class="num">115</span>
      <p class="indent">5. When Congress has intended that seizures or arrests might be made upon suspicion it has been careful to say so. The history and terms of the Volstead Act are not consistent with the suggestion that it was the purpose of Congress to grant the power here claimed for enforcement officers. The facts known when the arrest occurred were wholly insufficient to engender reasonable belief that plaintiffs in error were committing a misdemeanor, and the legality of the arrest cannot be supported by facts ascertained through the search which followed.</p>
    </div>
    <div class="num" id="p116">
      <span class="num">116</span>
      <p class="indent">To me it seems clear enough that the judgment should be reversed.</p>
    </div>
    <div class="num" id="p117">
      <span class="num">117</span>
      <p class="indent">I am authorized to say that Mr. Justice SUTHERLAND concurs in this opinion.</p>
    </div>
    
```

---

## GROUP: content/cases/Carter v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: Carter v. United States
type: case
citation: "No. 23-CF-0388, slip op. (dc 2025)"
parallel_cite: ""
neutral_cite: ""
court: D.C. 2025
court_level: state
circuit: ""
year: 2025
date_decided: 2025-08-28
docket: 23-CF-0388
authority_weight: "Persuasive — state, illustrative"
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
  opinion_url: "https://www.courtlistener.com/opinion/10662535/carter-v-united-states/"
  cluster_id: 10662535
  opinion_id: null
  identity_checked: false
lake:
  record_id: Carter v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Seizure of the Person]]"
    role: Key
related:
  - "[[Seizure of the Person]]"
  - "[[Terry v. Ohio]]"
  - "[[Graham v. Connor]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - show-of-authority
  - free-to-leave
  - reasonable-suspicion
holding: "A man was seized under the Fourth Amendment when an officer, backed by a show of authority and after disbelieving his response, directed him to hike up his pants; on the objective free-to-terminate inquiry — which properly accounts for the reasonable apprehension of a Black man in a heavily policed encounter — that request occurred before reasonable suspicion arose, making the seizure and its fruits unlawful."
---

# Carter v. United States

No. 23-CF-0388, slip op. (D.C. Ct. App. Aug. 28, 2025) · District of Columbia Court of Appeals · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): slip-only record (no A.3d cite yet); identity cluster 10662535 → opinion 11129122, decided 2025-08-28; Rule quote string-matched to the CL opinion text 2026-07-07. Slip-cite render per S2 A3; S9 promotes. -->

## Background
A five-officer tactical unit approached a group of about ten men, including Mr. Carter, in public during the daytime. An officer asked how he was doing; Carter lifted his shirt to show his waistband. When the officer expressed disbelief and asked whether he had "nothing" on him, Carter lifted his shirt again. The officer then asked him to "hike" up his pants; officers observed a bulge, seized him, and recovered a firearm. The trial court held Carter was not seized until after he raised his pants — by which point officers had reasonable suspicion — and denied suppression.

## Issue
Whether Mr. Carter was seized within the meaning of the Fourth Amendment when the officer directed him to raise his pants, before the officers had reasonable suspicion.

## Rule
The D.C. Court of Appeals reversed, holding that the seizure occurred earlier — at the request to raise his pants — and that the objective free-to-terminate inquiry must account for the defendant's race under *Dozier v. United States*: "we hold that Mr. Carter was seized within the meaning of the Fourth Amendment when Officer DelBorrell requested that he raise his pants." — slip op. at 30. Because that seizure preceded any reasonable suspicion or probable cause, it was unreasonable, and the firearm and Carter's ensuing statement should have been suppressed.

## Application
The court weighed the officers' coercive show of authority — the number of officers, the accusatory and repetitive questioning, and the disbelief of Carter's initial cooperation — and, applying *Dozier*, considered how an objectively reasonable Black man in Carter's position would experience that pressure. On that record, a reasonable person would not have felt free to walk away when told to hike up his pants, so the seizure crystallized before the bulge that supplied suspicion.

## Conclusion
Carter's convictions were **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. McLeese, Associate Judge, concurred in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Carter* illustrates the objective "free to terminate the encounter" test for when a *[[Seizure of the Person|seizure of the person]]* occurs and applies the D.C. rule (*Dozier v. United States*) that a suspect's race is relevant to that objective inquiry — a development the Supreme Court has not addressed. It is a published decision of the District of Columbia Court of Appeals, cited here for its reasoning.

## Appears on
- [[Seizure of the Person]] — *Key*

## Sources
- [*Carter v. United States*, No. 23-CF-0388 (D.C. Aug. 28, 2025)](https://www.courtlistener.com/opinion/10662535/carter-v-united-states/) — pinpoint: slip op. at 30 (opinion of the court; III. Conclusion); Rule quote string-matched to the CL opinion text 2026-07-07. No A.3d reporter cite has issued; the slip form is per S2 A3.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a6bd65ef3adb11c6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 23-CF-0388, slip op. (dc 2025)", "court": "D.C. 2025", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Carter v. United States", "year": "2025"}}
{"assertion_id": "56eef20fc28ed07a", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Key", "title": "Carter v. United States"}}
{"assertion_id": "85dbbecaa76000e8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A man was seized under the Fourth Amendment when an officer, backed by a show of authority and after disbelieving his response, directed him to hike up his pants; on the objective free-to-terminate inquiry — which properly accounts for the reasonable apprehension of a Black man in a heavily policed encounter — that request occurred before reasonable suspicion arose, making the seizure and its fruits unlawful.", "title": "Carter v. United States"}}
{"assertion_id": "d57014c85f9ebe41", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "Carter v. United States"}}
{"assertion_id": "e27ad88e377fbf66", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Carter v. United States", "varies_by_point": "false"}}
```

### lake record — Carter v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carter v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Carter v. United States",
    "case_name_short": "Carter",
    "case_name_full": "",
    "input_case_name": "Carter v. United States",
    "court": "D.C. 2025",
    "court_id": "dc",
    "court_level": "state",
    "circuit": null,
    "state": "dc",
    "date_decided": "2025-08-28",
    "year": 2025,
    "docket": "23-CF-0388",
    "cluster_id": 10662535,
    "lead_opinion_id": 11129122,
    "sibling_ids": [],
    "absolute_url": "/opinion/10662535/carter-v-united-states/",
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
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "D.C. Court of Appeals slip No. 23-CF-0388, filed 2025-08-28; no A.3d volume/page. (A search-floated '341 A.3d 1067' could not be independently confirmed; treated as unverified.)",
      "legs": [
        {
          "source": "Justia",
          "url": "https://law.justia.com/cases/district-of-columbia/court-of-appeals/2025/23-cf-0388.html",
          "cite": "No. 23-CF-0388 (D.C. 2025-08-28)"
        },
        {
          "source": "Court PDF",
          "url": "https://www.dccourts.gov/sites/default/files/2025-08/Carter%20v.%20U.S.%20%2023-CF-0388.pdf",
          "cite": "slip No. 23-CF-0388"
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
    "date_created": "2026-07-06T05:44:26Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "carter-v-united-states--10662535",
      "to_record_id": "Carter v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Carter v. United States

```
Notice: This opinion is subject to formal revision before publication in the Atlantic
and Maryland Reporters. Users are requested to notify the Clerk of the Court of
any formal errors so that corrections may be made before the bound volumes go
to press.

             DISTRICT OF COLUMBIA COURT OF APPEALS

                                  No. 23-CF-0388

                          DONTE J. CARTER, APPELLANT,

                                         V.

                            UNITED STATES, APPELLEE.

                          Appeal from the Superior Court
                           of the District of Columbia
                               (2020-CF2-007280)

                        (Hon. Lynn Leibovitz, Trial Judge)

(Submitted April 18, 2024                                Decided August 28, 2025)

      Brian D. Shefferman was on the brief for appellant.

      Chrisellen R. Kolb, Assistant United States Attorney, with whom Matthew M.
Graves, United States Attorney at the time the brief was filed, and John P.
Mannarino, Benjamin Helfand, Jacqueline Yarbro, and Michael C. Lee, Assistant
United States Attorneys, were on the brief, for appellee.

      Before BECKWITH and MCLEESE, Associate Judges, and WASHINGTON, *
Senior Judge.

      Opinion for the court by Senior Judge WASHINGTON.



      *
        Senior Judge Fisher was originally assigned to this case. Following his
retirement on August 22, 2024, Judge Fisher was replaced by Senior Judge
Washington.
                                          2

      Concurring opinion by Associate Judge MCLEESE at page 31.


      WASHINGTON, Senior Judge: Appellant Donte Carter was conversing amongst

a group of ten Black men on a sunlit sidewalk in Ward Four of the District. Despite

not having raised any suspicion of engaging in criminal activity, the group was

approached by four members of the Metropolitan Police Department’s Gun

Recovery Unit (GRU). One of the officers approached Mr. Carter from behind and

asked whether he was carrying a firearm. Mr. Carter replied that he was not and

twice lifted his shirt to demonstrate that nothing was hidden underneath. The officer

then asked Mr. Carter to “hike” his pants up. In this appeal, we are asked to

determine whether Mr. Carter was seized at this moment within the meaning of the

Fourth Amendment. We hold that he was.


                                  I.     Background


      Our articulation of the facts is based on both the trial court’s extensive factual

findings and footage from body-cameras worn by the officers.             Neither party

disputes these facts.


      At some time between 3:00 and 4:00 pm on a sunny day in September 2020,

five officers of the GRU 1 drove two unmarked vehicles into Ward Four of the


      1
          The unit has since been renamed to the Violent Crime Impact Team (VCIT).
                                         3

District, an area that consists predominantly of Black Americans, 2 to conduct a

firearm interdiction. They went there because of “an uptick in shootings and sounds

of gunfire” in the area. The officers observed ten Black men conversing on a

sidewalk and parked along the road opposite them. The group was split between

three men “sitting and standing near some planters,” and another seven men about

fifteen feet away. Among the group of seven men was appellant Mr. Carter, leaned

up against a parked car and facing everyone else.


      Four officers, Officers Sanders, Guzman, DelBorrell, and Keleman, emerged

from the vehicles and approached the group. They wore tactical vests with “police”

written on the back as well as visible handcuffs, firearms, and other police

equipment. Officers Sanders and Guzman focused on the group of three and

announced that they were “checking for firearms.”       Almost immediately, and

without being prompted to, one of the men lifted his shirt to reveal his waistband

seemingly to demonstrate that nothing was hidden underneath. Upon checking the




      2
         Ward Four consists of approximately 44 percent Black Americans and 29
percent White Americans. 2020 Consensus Information & Data: Table 3, D.C.
Office of Plan., https://planning.dc.gov/publication/2020-census-information-and-
data; https://perma.cc/B6QF-C8YQ.
                                            4

man’s waistband and a small bag he was carrying, Officers Sanders and Guzman

continued toward the larger group.


      Meanwhile, Officers DelBorrell and Keleman focused on Mr. Carter’s group.

Officer Keleman approached two individuals standing a few feet to Mr. Carter’s left

while Officer DelBorrell looped around the vehicle Mr. Carter was leaning on to

approach him from behind. As Officer DelBorrell rounded the vehicle, another man

approximately a foot ahead of Mr. Carter and several feet ahead of the officer also

lifted his shirt to reveal his waistband. Within three to four feet of Mr. Carter, Officer

DelBorrell asked how he was “doing,” to which Mr. Carter briefly replied, “how are

you doing” or “what’s up” before turning away. Officer DelBorrell then moved

closer to Mr. Carter but before he could say anything else, Mr. Carter also lifted his

shirt to show his waistband and then lowered it. As Mr. Carter raised his shirt,

DelBorrell asked, “[h]ey [c]hamp, you not got nothing on you?” Mr. Carter

responded, “no” and lifted his shirt again. Unsatisfied, Officer DelBorrell requested,

“[d]o you mind hiking your pants for me real quick?” Mr. Carter complied. “[I]n a

single quick motion, [Mr. Carter] hiked his pants [up] by holding them at the

waistband with two hands.” He “then lifted his shirt [again] and put it back down.”


      While this was happening, Officer Guzman had begun to approach Mr. Carter

from the other group. When he was about six to ten feet away, he noticed a bulge in
                                          5

Mr. Carter’s groin area. When Mr. Carter raised his pants in response to Officer

DelBorrell’s question, Officer Guzman, from approximately three to five feet away,

saw that the bulge was an L-shape, which he believed to be a firearm. Officer

Guzman then instructed Mr. Carter to “[s]tand up . . . one more time.” Mr. Carter

stood. Guzman then remarked, “[r]ight there, brother, right there,” pointing to Mr.

Carter’s right groin area. Mr. Carter replied, “[t]his is my phone,” pulling a phone

from his right pocket. Officer Guzman subsequently frisked Mr. Carter and after a

brief struggle in which the other officers on the scene joined, the officers recovered

a firearm hidden in Mr. Carter’s pants.


      Based on this encounter, Mr. Carter was charged with eight offenses

connected to the firearm. He moved to suppress the firearm as well as a statement

he made following the incident on grounds that they were the result of an

unreasonable seizure in violation of the Fourth Amendment. The trial court denied

his motion. It rejected his argument that he was seized when Officer DelBorrell

asked him to raise his pants and held that Mr. Carter was seized only after he pulled

his pants up. The court held that by then, the officers had reasonable suspicion to

seize him based on Officer Guzman’s observation of an L-shaped bulge in his groin

area that he made only after Mr. Carter raised his pants. Accordingly, the court held

that the firearm and statement were not the product of an unreasonable seizure.
                                           6

      Mr. Carter was subsequently convicted on all eight counts following a trial on

stipulated facts. He timely appealed.


                                     II.   Analysis


      The Fourth Amendment to the United States Constitution protects against

unreasonable searches and seizures. U.S. Const. amend. IV. Under the Fourth

Amendment’s prohibition against unreasonable seizures, law enforcement officers

may not seize an individual unless they have reasonable suspicion or probable cause

to believe that the person is engaged in criminal activity. See Terry v. Ohio, 392

U.S. 1, 27 (1968); Robinson v. United States, 76 A.3d 329, 335 (D.C. 2013).


      Mr. Carter’s sole claim on appeal is that the trial court erroneously denied his

motion to suppress. Contrary to the court’s holding, he argues that the officers seized

him within the meaning of the Fourth Amendment when Officer DelBorrell

requested that he raise his pants. Because, according to Mr. Carter, the officers

lacked reasonable suspicion or probable cause, such conduct violated his Fourth

Amendment rights. Mr. Carter claims that the trial court therefore should have

suppressed the fruits of that seizure—the firearm and his subsequent statement. See

Smith v. United States, 283 A.3d 88, 98 (D.C. 2022) (explaining that a court must

generally suppress any evidence “obtained as a direct result of” or “found to be a
                                          7

derivative of” an illegal search or seizure (quoting Utah v. Strieff, 579 U.S. 232, 237

(2016))).


      For its part, the government admits that it lacked reasonable suspicion or

probable cause to seize Mr. Carter when Officer DelBorrell asked him to raise his

pants. It also concedes that if it did seize Mr. Carter at that moment, the firearm and

statement were products of an unreasonable seizure and should have been

suppressed. The government’s sole argument on appeal is that it did not seize Mr.

Carter until after Officer DelBorrell’s request that Mr. Carter “hike” his pants up,

when it did have reasonable suspicion to seize him. Mr. Carter does not deny that

the officers had reasonable suspicion after Officer DelBorrell’s question and simply

argues that the seizure began before then.


      Accordingly, the central question before us is whether Mr. Carter was seized

when Officer DelBorrell requested that he raise his pants. We review this question

de novo. Sharp v. United States, 132 A.3d 161, 166 (D.C. 2016) (holding that

whether a defendant was seized within the meaning of the Fourth Amendment is a

question of law, which we review de novo).


      To determine whether a defendant was seized within the meaning of the

Fourth Amendment, we ask whether in view of all the circumstances surrounding

the defendant’s encounter with law enforcement, an objective and reasonable person
                                          8

in the defendant’s shoes would have “felt free to terminate” the interaction and “go

about [their] business.” Jones v. United States, 154 A.3d 591, 592 (D.C. 2017); see

Graham v. Connor, 490 U.S. 386, 397 (1989) (explaining that the test for

reasonableness    under   the   Fourth   Amendment       is   an   “objective   one”).

“Circumstances that might signify a seizure include the ‘presence of several officers,

the display of a weapon by an officer, some physical touching of the [defendant], or

the use of language or tone of voice indicating that compliance with the officer[s’]

request[s] might [have been] compelled.’” T.W. v. United States, 292 A.3d 790, 795

(D.C. 2023) (quoting United States v. Mendenhall, 446 U.S. 544, 554 (1980)). To

that list, we have added factors such as whether (1) the officers asked the defendant

questions of such an accusatory nature that an objective and reasonable person in the

defendant’s position would have felt “apprehensive” in failing to reply, see Jones,

154 A.3d at 596; (2) the officers continued to press the defendant with such

questions “in the face of an initial denial,” signaling that they “‘refused to accept’

the answer given,” T.W., 292 A.3d at 795 (quoting Golden v. United States, 248 A.3d

925, 938 (D.C. 2021)); (3) the encounter took place at night or the defendant was

alone or secluded, see Dozier v. United States, 220 A.3d 933, 944 (D.C. 2019); and

(4) “the officers . . . blocked the [defendant’s] potential exit paths or ‘means of

egress’” so as to signal that the defendant was not free to leave, T.W., 292 A.3d at

795 (quoting Golden, 248 A.3d at 939). In addition, we also consider the defendant’s
                                          9

race and the role that it may have played in affecting their willingness to leave. See

Dozier, 220 A.3d at 944.


                                         A.


      At the outset, we acknowledge that this is a close case. Whereas several

aspects of Mr. Carter’s interaction with the officers strongly suggest that he was

seized, there are other features that sway us in the opposite direction.


      Beginning with the case that favors Mr. Carter, we recognize that this case is

not too dissimilar from Golden, in which we held that the defendant was seized. See

generally Golden, 248 A.3d 925. In that case, the defendant, Brandon Golden, was

walking alone along a sidewalk at night when four GRU officers in a pair of

unmarked SUVs approached him from behind. Id. at 931. One of the SUVs stopped

at a curb in front of Mr. Golden and the other parked several feet to the left. Id.

With his window rolled down and his police badge, tactical vest, and firearm clearly

visible, an officer in the first car, Officer Vaillancourt, asked Mr. Golden, “in a

conversational tone . . . whether he had any weapons on him.” Id. at 932. Mr.

Golden replied that he did not. Id. Officer Vaillancourt then asked, “[c]an you just

show me your waistband[?]” Id. (second alteration in original).            Mr. Golden

complied by pulling up the middle and left sides of his shirt but not the right. Id.

Suspecting that Mr. Golden was attempting to conceal something underneath the
                                          10

right part of his shirt, Officer Vaillancourt continued to probe Mr. Golden about what

he was hiding. Id. Eventually, Officer Vaillancourt exited the vehicle, frisked Mr.

Golden, and discovered a firearm. Id. Mr. Golden was subsequently charged with

various firearm-related offenses and sought to suppress the firearm on grounds that

the officers seized him without reasonable suspicion or probable cause and that the

firearm was a product of this unreasonable seizure. Id. at 931, 933. The trial court

denied his motion and Mr. Golden was convicted. Id. at 933.


      On appeal, we vacated Mr. Golden’s conviction and remanded. Id. at 949.

We held that the officers in the SUVs seized Mr. Golden the moment Officer

Vaillancourt requested to see his waistband. Id. at 936. Because the officers lacked

reasonable suspicion or probable cause at that point, the seizure was unreasonable.

Id. at 940. Accordingly, the trial court erred in failing to suppress the firearm. Id.


      We arrived at the conclusion that Mr. Golden was seized by first recognizing

that Mr. Golden’s encounter with the officers was not merely one between “equals,”

which an objective and reasonable person would feel free to terminate, but rather

“commenced with an impressive show of police authority.” Id. at 936 (quoting

Jones, 154 A.3d at 595). We observed that “[n]ot one but four police officers in two

unmarked vehicles simultaneously converged on and partially surrounded [Mr.
                                          11

Golden], with one of the vehicles blocking his path by stopping directly in front of

him[—]a visible signal that the police intended for him to stop.” Id.


      Second, we held that Officer Vaillancourt’s immediate questioning of Mr.

Golden as to whether he was carrying any weapons was of such an accusatory nature

that it could not be viewed as merely “a simple request for information.” Id. at 937;

cf. Florida v. Bostick, 501 U.S. 429, 434 (1991) (holding that an officer does not

seize someone merely by approaching them and “ask[ing] a few questions”). Rather,

it indicated to Mr. Golden that he had been “singled . . . out” because the police

“suspected him of being armed and committing a crime,” thereby contributing to a

“sense of powerlessness in an investigative confrontation by the police,” one which

he could relieve himself of only by demonstrating his innocence. Golden, 248 A.3d

at 937 (second alteration in original).


      Finally, we explained that Officer Vaillancourt’s request that Mr. Golden

reveal his waistband after Mr. Golden denied carrying a weapon took the interaction

“beyond mere questioning,” because it “implied” to Mr. Golden that the officers

would continue to view him with “heightened suspicion if he attempted to end the

encounter without first exposing his waist[band].” Id. We held that an objective

and reasonable person in Mr. Golden’s shoes “would not [have felt] free to frustrate
                                         12

the police inquiry” without first complying with Officer Vaillancourt’s request in

order to “allay [his] suspicions” and “get the confrontation over with.” Id.


      Here, Mr. Carter’s interaction with the officers bore many of the same features

that contributed to our finding that Mr. Golden was seized. First, like in Golden,

two police vehicles simultaneously approached Mr. Carter and others in his group.

Four officers then exited the vehicles and converged on the group, suggesting that

the men were not simply free to continue conversing amongst themselves as they

were previously. Officer DelBorrell also approached Mr. Carter from behind,

which—in our view—would make any objective and reasonable person feel uneasy

and intimidated, especially when faced with an openly visible firearm within close

proximity.


      Second, like Officer Vaillancourt, Officer DelBorrell immediately asked Mr.

Carter whether he possessed a firearm. As we did in Golden, we view this question

as one that suggested to Mr. Carter that he, alongside other members of the group,

had been singled out as being suspected of criminal activity. An objective and

reasonable person in his shoes would have felt apprehensive in refusing to respond

to the officer’s question. See, e.g., Mayo v. United States, 315 A.3d 606, 628-29

(D.C. 2024) (en banc) (explaining that such a question is intimidating in part due to

the “illegal[ity] [of] carry[ing] a gun in the District without proper licensure and
                                         13

registration”); T.W., 292 A.3d at 796-97 (explaining the coercive nature of a request

for a weapon). They may have felt fearful that refusing to answer such a question

would have suggested to “the suspicious officer[]” that they had “something to

hide.” Guadalupe v. United States, 585 A.2d 1348, 1360 (D.C. 1991).


      Finally, despite Mr. Carter both denying carrying a firearm and raising his

shirt not once but twice to reveal his waistband, Officer DelBorrell continued to

probe him by asking him to “hik[e] [his] pants up.” We see no appreciable difference

between this request and that in Golden as both required the defendants to continue

assuaging the officers’ suspicions despite initially denying any wrongdoing. Indeed,

both requests implied to the defendants that they would continue to be suspected of

criminal activity until the officers stopped asking questions, thereby leaving them

with little choice but to respond. See T.W., 292 A.3d at 798 (seeing no meaningful

difference between the officer’s offer to pat down the defendant and Officer

Vaillancourt’s request to view Mr. Golden’s waistband because both questions were

asked after the defendants denied carrying a weapon).


      While we recognize the similarities between this case and Golden, we also

acknowledge two key differences that prevent us from holding that Golden controls

the outcome here. Most notably, in Golden, we placed significant weight on the fact

that Mr. Golden was approached at night by four officers in a secluded setting where
                                          14

there were no bystanders to witness the interaction. See Golden, 248 A.3d at 936-37.

This not only resulted in a more intimidating atmosphere, but it also heightened Mr.

Golden’s concern that he was being singled out for criminal activity and would need

to comply to dispel that suspicion. Id. at 937. Here, in contrast, Mr. Carter was not

singled out on his own but rather as a member of a larger group. This likely

mitigated Mr. Carter’s concern that he alone was being targeted by the police.

Further, Mr. Carter was not outnumbered by four officers in a secluded setting at

night. Less intimidating, the interaction took place in broad daylight with nine

potential witnesses, all occupying the attention of just four officers.


      Second, whereas the officers in Golden exerted significant control over Mr.

Golden’s movement by partially surrounding him, thereby signaling that he was not

free to leave, the officers here did not restrict Mr. Carter’s movement. Rather, as the

trial court found in its suppression ruling, Mr. Carter “was not surrounded or

hemmed in by the police” and was “more surrounded by those he had been hanging

out with.” Indeed, unlike in Golden, any restriction on Mr. Carter’s movement was,

at least in part, self-imposed, namely by his decision to lean against a car in the

company of others. 3 See I.N.S. v. Delgado, 466 U.S. 210, 218 (1984) (holding that


      3
       We are unpersuaded by the government’s additional attempts to distinguish
Golden. Namely, the government argues that Officer DelBorrell’s conduct toward
Mr. Carter was less “intimidating” than Officer Vaillancourt’s actions toward Mr.
Golden. It points to Officer DelBorrell’s casual tone, the fact that Mr. Carter did not
                                          15




seem to be bothered, and that Officer Vaillancourt requested that Mr. Golden
“acquiesce in a public unveiling of part of his body” whereas Officer DelBorrell
merely asked Mr. Carter to raise his pants.

       We disagree with the government that Officer DelBorrell was less
intimidating than Officer Vaillancourt. To begin, as we recognized in Golden,
Officer Vaillancourt’s tone was also “conversational.” Id. at 932. Despite that, we
held that his questions were still intimidating due to their accusatory nature. Id. at
937. Indeed, we have previously discouraged courts from “attach[ing] undue weight
to a police officer’s ‘conversational’ tone in speaking to a suspect.” T.W., 292 A.3d
at 803 (quoting Golden, 248 A.3d at 935 n.26). “While a harsh and commanding
tone could certainly convey to a person that their compliance is non-optional, a polite
and conversational tone does little to dispel coercion that arises from the content of
officers’ inquiries, or in how they have approached the suspect.” Id. at 803; see also
Guadalupe, 585 A.2d at 1361 (explaining that police questioning does “not have to
assume an intensity marking a shift from polite conversation to harsh words to create
an intimidating atmosphere”). This is especially true when the officer’s inquiries
are accusatory in nature, as they were here.

       Second, we disagree with the government’s characterization of Mr. Carter as
being “[un]bothered.” Almost immediately after Officer DelBorrell began
questioning him, Mr. Carter raised his shirt up twice. If he were unbothered, we
think it far more likely that he would ignore the officer’s questions or at minimum
verbally deny possessing a firearm, let alone take the more drastic step of revealing
his waistband. In any case, we place little weight on Mr. Carter’s subjective response
to Officer DelBorrell’s conduct as the Fourth Amendment seizure inquiry is an
objective one—that is, whether an objective and reasonable person in Mr. Carter’s
shoes would feel free to terminate the encounter. See Jackson v. United States, 805
A.2d 979, 987 (D.C. 2002).

       Finally, that Officer DelBorrell requested that Mr. Carter raise his pants
whereas Officer Vaillancourt asked Mr. Golden to reveal his waistband is not legally
significant for present purposes. Setting aside the fact that Mr. Carter had already
raised his shirt twice before Officer DelBorrell called on him to raise his pants, our
main point here in Golden was not that Mr. Golden was subject to a highly intrusive
inquiry (though he was), it was that the officer indicated to him that he would not be
free to leave until he fully satisfied the officer that he did not possess any weapons.
See Golden, 248 A.3d at 937. Similarly here, by failing to take “‘no’ for an answer,”
                                          16

workers in a factory were not seized despite officers being stationed at the factory

doors because the workers had already voluntarily limited their movement to the

factory floor before the officers arrived).


                                          B.


      In addition to the differences between Golden and this case, we previously

concluded in two cases—Brown and Kelly—that defendants in circumstances also

not too dissimilar to those here were not seized within the meaning of the Fourth

Amendment. See generally Brown v. United States, 983 A.2d 1023 (D.C. 2009);

Kelly v. United States, 580 A.2d 1282 (D.C. 1990).           In Brown, two officers

approached a group of “five or six [people] standing on [a] sidewalk.” 983 A.2d at

1024-25. One of the officers approached the defendant, Valerie Brown, and asked

if she had “any guns, drugs, or narcotics on [her].” Id. at 1025. Ms. Brown replied

that she was “not doing anything” and that she was just “counting [her] money.” Id.

The officer repeated her question and Ms. Brown “reached into her purse and handed

the officer a brown pill bottle,” which later tested positive for cocaine. Id.


      We held that Ms. Brown was not seized despite the fact that the officer asked

the same accusatory question twice. Id. at 1026. We relied on the fact that the



Officer DelBorrell gave Mr. Carter the impression that he would have to respond to
all his questions before being let go. Id. (alterations in original).
                                         17

officers were outnumbered by the group Ms. Brown was a part of, the fact that she

was approached by only one officer while the other was further away speaking to

two other individuals, that the officers did not engage in behavior, “such as

threatening gestures, orders, or intimidation, which might have caused the encounter

to lose its consensual nature,” and that other members of the group walked away

unimpeded, suggesting that an objective and reasonable person in Ms. Brown’s

shoes would have felt free to leave. Id. at 1025-26. That the officer asked an

accusatory question and that she repeated her question were insufficient to overcome

the non-coercive nature of the other aspects of the interaction. See id.


      In Kelly, two officers approached the defendant, James Kelly, at Union

Station. Kelly, 580 A.2d at 1284. Both officers were in plain clothes and neither

was visibly carrying a firearm or displaying their badge. Id. One of the officers

asked Mr. Kelly if he “could speak with him” and Mr. Kelly replied, “yes.” Id.

Meanwhile, the other officer stood “about four feet in front of Kelly.” Id. The

questioning officer inquired about where Mr. Kelly was arriving from, where he

lived, and how long he had lived there. Id. The officer then introduced himself as a

member of the Narcotics Branch of the police department and asked if Mr. Kelly

was “carrying any drugs.” Id. Mr. Kelly replied, “no.” Id. The officer then asked

to search Mr. Kelly’s bag, which Mr. Kelly permitted. Id.
                                          18

      Like in Brown, we held that Mr. Kelly was not seized despite being repeatedly

asked an accusatory question. Id. at 1288. We explained that the officer “made no

demands” of Mr. Kelly, never produced a weapon, and never touched Mr. Kelly. Id.

at 1286. Further, we rejected Mr. Kelly’s argument that the non-questioning officer

was impeding his movement as the officer was four feet away, did not brandish a

weapon, or make any threatening gestures. Id. Finally, we emphasized that the

questioning officer asked Mr. Kelly if he could speak with him, thereby implying to

Mr. Kelly that he did not have to comply. Id.


      Brown and Kelly suggest that we should similarly overlook the fact that Mr.

Carter was repeatedly asked accusatory questions as the other aspects of the

encounter were just as non-coercive as in those two cases. Like in Brown, Mr.

Carter’s group far outnumbered the officers who approached them. In fact, the

number of non-officers to officers was approximately the same in both cases (five

to two). Further, like in Brown, Mr. Carter was initially approached by one officer,

Officer DelBorrell, while the others focused elsewhere. Indeed, at the time Officer

DelBorrell requested that Mr. Carter raise his pants, Officer DelBorrell was the only

officer in Mr. Carter’s immediate vicinity. Officer Guzman, the next closest officer,

was still several feet away. Finally, like in Brown and Kelly, the officers here did not

make any threatening gestures or orders, nor did they touch Mr. Carter, so as to

suggest that compliance was mandatory.
                                         19

      The government goes so far as to argue that considering the similarities,

Brown and Kelly control the outcome in this case. While we certainly place

analytical weight on both cases, we reject the government’s claim that they are

controlling. Brown is distinguishable for two reasons. First, unlike in Brown, no

member of Mr. Carter’s group left once the police arrived. To the contrary, not only

did members of the group comply with the officers’ requests, but some went further

by raising their shirts before they were even asked. Accordingly, unlike in Brown,

the behavior of others surrounding Mr. Carter suggest that an objective and

reasonable person in his shoes would not have felt free to leave. Second, what made

the repetitive questioning less coercive in Brown was that Ms. Brown’s first answer

was non-responsive to the officer’s question. The officer asked whether she was

carrying any contraband, and rather than replying “yes” or “no,” Ms. Brown

answered that she was simply counting her money. Brown, 983 A.2d at 1025. Thus,

it was “entirely reasonable for the officer to ask her question again.” Gordon v.

United States, 120 A.3d 73, 82 (D.C. 2015) (differentiating Brown on grounds that

the repetitive questioning in Brown was simply to seek clarification to a non-

responsive initial answer); T.W., 292 A.3d at 801 (same). Here, in contrast, Mr.

Carter explicitly denied carrying a weapon and raised his shirt twice when Officer

DelBorrell questioned him. In the face of this denial, unlike in Brown, Officer

DelBorrell implied that he was unsatisfied by asking Mr. Carter to raise his pants.
                                         20

      Kelly is also distinguishable. Namely, the officer there requested Mr. Kelly’s

permission to speak with him before questioning him, thereby indicating that

cooperation was only optional. Kelly, 580 A.2d at 1284. An acknowledgement that

an individual need not comply significantly reduces the coercive nature of a police

encounter as it dispels doubt in an individual’s mind that they must cooperate to

terminate the interaction. Whereas the officer in Kelly effectively informed Mr.

Kelly of his right to walk away by asking him if he could speak, the officers did not

do so here. Officer DelBorrell simply approached Mr. Carter from behind and began

asking if he was carrying any weapons.


                                   *     *      *


      In light of the similarities between this case and those in which we both found

that the defendant was seized (Golden), and not seized (Brown and Kelly), we must

look beyond the mere conduct of the officers to objectively determine whether Mr.

Carter was seized. To do so, we examine the impact of the defendant’s race. Dozier,

220 A.3d at 944.     Indeed, in its suppression ruling, the trial court implicitly

recognized the relevance of race to its Fourth Amendment seizure inquiry. It

acknowledged that “in certain neighborhoods among certain demographics that are

highly policed[,] the behavior of police can convey to a reasonable . . . person that

they are compelled to allay [the] officers’ suspicion by acceding to their wishes.”
                                         21

The court went no further, however, and instead focused its analysis solely on the

coercive nature of the officers’ conduct. It did not delve further into how the

officers’ conduct might have uniquely impacted an objective and reasonable person

sharing Mr. Carter’s racial status as a Black man. Accordingly, in this next part, we

conduct a more thorough inquiry.


                                        C.


      Dozier requires that in addition to considering the coercive nature of the

officers’ conduct in a Fourth Amendment seizure analysis, we must also take into

account the defendant’s race. Id. More specifically, we are to consider whether an

objective and reasonable person sharing the defendant’s generalized lived

experiences arising out of their racial status would have felt free to terminate the

police encounter. See id. at 944-45. Our consideration of the defendant’s race

recognizes that a Fourth Amendment seizure inquiry would be incomplete, and

indeed, incongruent with the objective reality that people of color face during

interactions with law enforcement. Id. For people of color, and as relevant here,

Black men, feel “especially apprehensive” around the police such that conduct that
                                              22

may not rise to the level of a seizure without consideration of race, may do so once

the defendant’s race and lived experiences are accounted for. Id. at 944. 4


         To inform our analysis as to the role that Mr. Carter’s status as a Black man

may have played here, it is first important to understand why Black men, generally

speaking, are especially cautious around and more likely to comply with the

demands of law enforcement. There are two central reasons. First, “[i]t is no secret”

that Black Americans are disproportionately likely to be victims of violence at the

hands of police officers, particularly during suspicionless investigatory inquiries like

the one here. Bloom, supra at note 4, at 7 (quoting Strieff, 579 U.S. at 254 (2016)

(Sotomayor, J., dissenting)).       In recent years, nationally, police officers have

threatened or used non-fatal force in roughly three percent of encounters they

initiated or which resulted from a traffic accident. Nazgol Ghandnoosh & Celeste

Barry,       One   in   Five:   Disparities   in   Crime   and   Policing   9   (2023),




        For a more thorough discussion as to why considering the defendant’s race
         4

is consistent with the objective nature of the Fourth Amendment seizure inquiry, see,
e.g., Daniel S. Harawa, Coloring in the Fourth Amendment, 137 Harv. L. Rev. 1533
(2024); Aliza H. Bloom, Objective Enough: Race is Relevant to the Reasonable
Person in Criminal Procedure, 19 Stan. J. C.R. & C.L. 1 (2023); Lindsey Webb,
Legal Consciousness as Race Consciousness: Expansion of the Fourth Amendment
Seizure Analysis Through Objective Knowledge of Police Impunity, 48 Seton Hall
L. Rev. 403 (2018); Devon W. Carbado, (E)Racing the Fourth Amendment, 100
Mich. L. Rev. 946 (2002); Tracey Maclin, “Black and Blue Encounters”—Some
Preliminary Thoughts About Fourth Amendment Seizures: Should Race Matter, 26
Val. U. L. Rev. 243 (1991).
                                         23

https://www.sentencingproject.org/app/uploads/2023/11/One-in-Five-Disparities-

in-Crime-and-Policing.pdf;     https://perma.cc/J367-HYVL.           During     these

interactions, Black individuals were over twice as likely to be subject to force or

threatened force as White individuals. Id. And with regard to fatal force, Black

Americans were over twice as likely to be shot and killed by police officers as White

Americans. Id. Twenty-one percent of Black adults have reported being victims of

police violence on account of their race (compared to three percent of white adults)

and nearly half have stated that they were at some point fearful for their life around

law enforcement (compared to sixteen percent of white adults). Craig Palosky, Poll:

7 in 10 Black Americans Say They Have Experienced Incidents of Discrimination or

Police Mistreatment in their Lifetime, Including Nearly Half Who Felt Their Lives

Were in Danger, KFF (June 18, 2020), https://www.kff.org/racial-equity-and-

health-policy/press-release/poll-7-in-10-black-americans-say-they-have-

experienced-incidents-of-discrimination-or-police-mistreatment-in-lifetime-

including-nearly-half-who-felt-lives-were-in-danger/;        https://perma.cc/RR22-

LDNJ.


      Naturally, this statistical reality has led to the perception among Black

Americans, and Black men in particular, that they are unsafe around law

enforcement and that they must engage in “particular kinds of performances” around

the police to “preempt” and mitigate the risks of “law enforcement discipline.”
                                         24

Carbado, supra at note 4, at 966. Indeed, the inundation of countless stories of young

and unarmed Black men being killed by police for their failure to comply and

generations-worth of experience in dealing with the police within the Black

community have led Black parents to give their children “‘the talk’—instructing

them to never run down the street; always keep [their] hands where they can be seen;

[and to never] even think of talking back to . . . stranger[s]—all out of fear of how

an officer with a gun will react to them.” Strieff, 579 U.S. at 254 (Sotomayor, J.,

dissenting); see Rod K. Brunson, “Police Don’t Like Black People”: African-

American Young Men’s Accumulated Police Experiences, 6 Crim. & Pub. Pol’y 71,

88 (2007) (finding that “violence at the hands of the police . . . happened enough to

convince [Black youth] that it was a real possibility during any encounter with police

officers”); Rayan Succar et al., Understanding the Role of Media in the Formation

of Public Sentiment Towards the Police, Commc’ns Psych (2024) (describing the

influential role of individual media stories of police brutality on perceptions about

the police). Having been raised in this environment, and “being more vulnerable to

police violence” than other demographic groups, Black men are more likely to

comply with police demands rather than exercise their constitutional right to

terminate a suspicionless police encounter. Dozier, 220 A.3d at 945.


      Second, even setting aside the risk of provoking violence, Black Americans

are especially distrustful of law enforcement and are thus less likely to terminate a
                                          25

police encounter due to skepticism that any attempt to exercise their constitutional

rights will be respected. From slave patrols during the antebellum era to Black

Codes post-Reconstruction to disparate charging and sentencing practices today, the

criminal legal system has historically been used as a tool to undermine rather than

uphold the freedom and dignity of Black Americans. See Daniel S. Harawa,

Whitewashing the Fourth Amendment, 111 Geo. L.J. 923, 940 (2023); see generally

Michelle Alexander, The New Jim Crow (2010). Modern-day policing reflects this

history with Black communities disproportionately subject to adverse police

interactions. See Radley Balko, There’s Overwhelming Evidence that the Criminal

Justice System is Racist: Here’s the Proof, Wash. Post (June 10, 2020),

https://perma.cc/ND2K-SUGV (cataloging studies of racial bias in the criminal

justice system, including 46 peer-reviewed studies demonstrating racial bias in

policing and profiling over the prior five years). Black Americans are more likely

to be subject to suspicionless stops and are more likely to be searched and detained

during these stops. Bloom, supra at note 4, at 7, 13 (citing U.S. Dep’t Justice,

Investigation    of    the     Ferguson        Police    Department     4    (2015),

https://www.justice.gov/sites/default/files/opa/press-

releases/attachments/2015/03/04/ferguson_police_department_report.pdf;

https://perma.cc/ZBT9-7BJP (concluding that Black drivers were “more than twice

as likely as white drivers to be searched during vehicle stops even after controlling
                                         26

for non-race variables”)). Black men in particular also tend to be questioned more

accusatorily and aggressively—a product of both historical tension between law

enforcement and the Black community and, as social science research suggests,

stereotyping of Black men as being dangerous and criminally predisposed. Carbado,

supra at note 4, at 982; Graham Cronogue, Race and the Fourth Amendment: Why

the Reasonable Person Analysis Should Include Race as a Factor, 20 Tex. J. C.L &

C.R. 61 (2015). That is, whereas a police officer’s objective in questioning a White

individual will be to simply “check things out,” they will often “need more time with

and more information from the” Black individual given their perception that the

Black individual is more likely to engage in criminal activity. Carbado, supra at

note 4, at 982.


      It should therefore come as “no surprise” that Black Americans “often

perceive their interactions with law enforcement differently than other

demographics.” State v. Spears, 839 S.E.2d 450, 463 (S.C. 2020) (Beatty, C.J.,

dissenting). Eighty-four percent of Black adults have said that in dealing with the

police, Black Americans are generally treated less fairly than other demographic

groups. Drew DeSilver et al., 10 Things we Know About Race and Policing in the

U.S., Pew Rsch. Ctr. (June 3, 2020), https://www.pewresearch.org/short-

reads/2020/06/03/10-things-we-know-about-race-and-policing-in-the-u-s/;

https://perma.cc/RH4E-D3UA. Eighty-seven percent have said that the criminal
                                          27

legal system as a whole treats Black Americans less fairly. Id. Such distrust, sown

both historically through the use of the criminal legal system to subjugate Black

Americans and via biased modern police practices, has produced an objective reality

in which Black Americans lack confidence that the police will respect the exercise

of their rights. Maclin, supra at note 4, at 254. Rather, to avoid suffering physical

abuse and criminal consequences during suspicionless police interactions, Black

Americans, and Black men in particular, are often left with no other choice but to

remain “calm” and “congenial” and comply with the requests of law enforcement.

Id. at 278.


      Applying this understanding as to why Black men are especially apprehensive

around police, it is clear that many of the historical features of blue-on-black

interaction that have led to this perception were present in Mr. Carter’s encounter.

First, Mr. Carter was confronted in a predominantly Black area in a group consisting

entirely of Black men by GRU officers who were wearing tactical gear and who

were visibly displaying their firearms. This alone was likely sufficient to trigger the

elevated fear that Black men experience around law enforcement not only because

the officers were carrying openly visible firearms but also because their selective

targeting reflected a pervasive understanding that the police target Black men and

treat them unfairly. Moreover, the GRU (now the VCIT) has a “reputation for

[aggression].” Mayo, 315 A.3d at 631; Robinson, 76 A.3d at 331-32, 339 (noting
                                           28

GRU’s acknowledged “technique” of confronting people on the street, “ask[ing]

people if they have a gun,” and then “looking for a reaction,” including people’s

“movements” in response to the question (internal quotation marks omitted)); United

States v. Gibson, 366 F. Supp. 3d 14, 21 (D.D.C. 2018) (describing how the GRU

“trawl[s]” certain “neighborhoods asking occupants who fit a certain statistical

profile—mostly males in their late teens to early forties—if they possess contraband[

] [d]espite lacking any semblance of particularized suspicion when the initial contact

is made” (quoting United States v. Gross, 784 F.3d 784, 789 (D.C. Cir. 2015)

(Brown, J., concurring))). It is also known to selectively target Black individuals.

See Michael G. Tobin, Metropolitan Police Department Narcotics and Specialized

Investigations          Division           5,          20,          26,          (2020),

https://policecomplaints.dc.gov/sites/default/files/dc/sites/office%20of%20police%

20complaints/publication/attachments/National%20Police%20Foundation%20MP

D%20NSID%20Report%20September%202020%20Final.pdf;

https://perma.cc/S29N-PMF7 (reporting that between August 1, 2019 and January

31, 2020, Black individuals were the subject of over 87% of GRU stops, 91% of

arrests, and 100% of use-of-force incidents). Given this background, it should not

come as a shock that several of the men in Mr. Carter’s group immediately

capitulated to the police presence, including Mr. Carter, by raising their shirts despite

not being asked to. Indeed, whereas any reasonable person would be fearful of
                                           29

failing to cooperate under these circumstances, a Black man would be especially

cautious here so as to avoid potential physical retaliation. 5


      Second, compounding the already racially charged and coercive environment

in which Mr. Carter’s interaction with the police took place, Officer DelBorrell

accusatorily and repetitively questioned him regarding whether he possessed a

firearm. As explained above, Black men already widely believe that police officers

disrespect their rights. We view it as likely that Officer DelBorrell’s failure to accept

Mr. Carter’s initial denial triggered a fear that Officer DelBorrell would not permit

Mr. Carter to terminate the encounter without first dispelling his suspicions. To

avoid prolonging the suspicion, Mr. Carter felt compelled to comply rather than

attempt to exercise his constitutional rights.




      5
         The VCIT and similar police tactical units that engage in large-scale
suspicionless investigations are generally distinguishable from those police units
that are engaged in what many refer to as community policing activities. Generally
speaking, community policing promotes the systematic use of partnerships and
problem-solving techniques to proactively address the conditions that give rise to
public safety issues. U.S. Dep’t Justice, Community Policing Defined 1 (2014),
https://portal.cops.usdoj.gov/resourcecenter/content.ashx/cops-p157-pub.pdf;
https://perma.cc/9GU6-CNH7. Typically, police officers are assigned to particular
communities where they get to know and work with community leaders and others
to address the immediate conditions that give rise to public safety issues.
                                          30

                                   III.   Conclusion


      Accordingly, taking into account the coercive nature of the officers’ conduct

and factoring in the elevated effect that this would have had on an objective and

reasonable Black man in Mr. Carter’s shoes, we hold that Mr. Carter was seized

within the meaning of the Fourth Amendment when Officer DelBorrell requested

that he raise his pants. The combination of the impressive show of authority

reflected in the officers’ initial approach and the accusatory and repetitive nature of

Officer DelBorrell’s questioning already resembled a scenario in which we held a

seizure took place. Compounding the compulsive effect of the police tactics here

was that they were used against a man for whom, by virtue of his race and lived

experiences, it would have been objectively reasonable to be apprehensive around

police officers. Given the facts of this case, we believe that such apprehension would

have led an objective and reasonable Black man in Mr. Carter’s shoes to feel as

though he had to comply with the officers’ demands rather than terminating the

encounter. For this reason, we are satisfied that Mr. Carter was seized when Officer

Delborrell disbelieved his initial response, and further requested that he raise his

pants. Because this seizure was not based on reasonable suspicion or probable cause,

it was unreasonable and violated the Fourth Amendment. The trial court thus erred

in failing to suppress the fruits of the seizure—the firearm and Mr. Carter’s later

statement.
                                          31

      For the foregoing reasons, we vacate Mr. Carter’s convictions and remand for

further proceedings.


                                                            So ordered.


      MCLEESE, Associate Judge, concurring in the judgment: The opinion for the

court holds that Mr. Carter was unlawfully seized. Ante at 30. I respectfully concur

in the judgment.


      As the opinion for the court notes, the key facts are undisputed: (1) in public

and during the daytime, a group of five officers approached a group of ten men that

included Mr. Carter; (2) one of the officers asked Mr. Carter how he was doing;

(3) Mr. Carter lifted his shirt to show his waistband; (4) the officer asked if Mr.

Carter had “nothing” on him; (5) Mr. Carter responded no and lifted his shirt again;

and (6) the officer asked if Mr. Carter “mind[ed] hiking [his] pants for me real

quick?” Ante at 2-4.


      Describing the case as “close,” ante at 9, the opinion for the court appears to

give dispositive weight to an additional consideration: that Mr. Carter as a Black

man would reasonably be “especially apprehensive around police” and “especially

distrustful of law enforcement,” ante at 24, 27, and therefore would reasonably have

felt obliged to comply with the officer’s request to hike up his pants, ante at 30.
                                         32

      In support of the conclusion that Mr. Carter’s race is properly considered in

determining whether Mr. Carter was seized, the opinion for the court relies on this

court’s decision in Dozier v. United States, 220 A.3d 933 (D.C. 2019). I concurred

in the judgment in Dozier. Id. at 948-51 (McLeese, J., concurring in the judgment).

Among other things, I expressed uncertainty as to whether the race of a suspect can

permissibly be considered in assessing whether police conduct constitutes a seizure.

Id. at 950-51 (citing conflicting authority on issue). The opinion for the court in

Dozier held, however, that Mr. Dozier’s race should be so considered. Id. at 943-45.

That holding is binding on me. E.g., M.A.P. v. Ryan, 285 A.2d 310, 312 (D.C. 1971).


      Taking as a given that Mr. Carter’s race may properly be considered, I agree

with the conclusion of the opinion for the court that, although this is a close case,

Mr. Carter was seized. Ante at 9, 30. I therefore respectfully concur in the judgment.

```

---

## GROUP: content/cases/Case v. Montana.md  (`case`, 4 assertions)

### content_page

```
---
title: "Case v. Montana"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2026
date_decided: 2026-01-14
docket: 24-624
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2026-01-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Case v. Montana
  varies_by_point: false
  scope_note: "Decided January 14, 2026 (slip opinion; final U.S. Reports pagination pending). Kagan, J., for a unanimous Court; Sotomayor, J., and Gorsuch, J., concurring. Current good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10774335/case-v-montana/"
  cluster_id: 10774335
  opinion_id: 11240920
  identity_checked: false
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brigham City v. Stuart]]", "[[Caniglia v. Strom]]", "[[Michigan v. Fisher]]", "[[Mincey v. Arizona]]", "[[Ohio v. Robinette]]"]
aliases: []
tags: ["case", "fourth-amendment", "emergency-aid", "exigent-circumstances", "objectively-reasonable", "suicide", "mental-health"]
holding: "Brigham City's objective-reasonableness standard for warrantless home entries to render emergency aid applies without further gloss — it is neither lowered to Terry reasonable suspicion nor raised to probable cause — and asks only whether an officer had an objectively reasonable basis for believing entry was needed to prevent or deal with serious harm."
lake:
  record_id: Case v. Montana
  status: under_review
  projected_at: 2026-07-06
---

# Case v. Montana

*607 U.S. ___ (2026)* (No. 24-624) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Montana officers responded to the home of William Trevor Case after his ex-girlfriend called 911 to report that Case — whom the officers knew had mental-health and alcohol problems and had spoken of suicide — was threatening suicide, had spoken of a suicide note, and may have cocked or shot a gun before the call cut off. Officers knocked and yelled into an open window with no response; through the windows they saw empty beer cans, an empty handgun holster, and a notepad. After roughly 40 minutes, they entered to render [[Emergency Aid|emergency aid]]. When an officer approached a closet where Case was hiding, Case threw open the curtain holding what looked like a gun, and the officer shot and injured him; a handgun was found where he had stood. Charged with assaulting an officer, Case moved to suppress, arguing the warrantless entry was unlawful. The Montana Supreme Court upheld the entry under the State's "community caretaker" doctrine.

## Issue
Whether the warrantless home entry to render [[Emergency Aid|emergency aid]] satisfied the Fourth Amendment, and what standard governs such an entry — Brigham City's objective reasonableness, a lower reasonable-suspicion test, or a higher probable-cause test.

## Rule
Brigham City's standard governs, and it applies without further gloss. The Court declined to lower it to reasonable suspicion: "Brigham City did not adopt *Terry*'s reasonable-suspicion standard for home entries. . . . Rather, Brigham City formulated its own standard for dealing with household emergencies — again, whether an officer has 'an objectively reasonable basis for believing' that an occupant is seriously injured or imminently threatened with such harm." — slip op. at 7 (quoting *Brigham City*, 547 U.S. at 400). ^pin-slip7

And it declined to raise it to probable cause: "We decline Case's invitation to put a new probable-cause spin onto Brigham City. . . . So Brigham City adopted a different approach. Rather than strain to relate probable-cause decisions to emergency-aid situations, we asked simply whether an officer had 'an objectively reasonable basis for believing' that his entry was direly needed to prevent or deal with serious harm." — slip op. at 8. ^pin-slip8

The entry is also scope-limited: "an emergency-aid entry provides no basis to search the premises beyond what is reasonably needed to deal with the emergency while maintaining the officers' safety. But we assess the reasonableness of that limited entry on its own terms, rather than through the lens generally used to consider investigative activity." — slip op. at 9. ^pin-slip9

The bottom line: "We repeat today what we have held before: An officer may enter a home without a warrant if he has 'an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened with such injury.' . . . The officers' entry satisfied that test." — slip op. at 10–11. ^pin-slip10

## Application
Judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], the officers had an objectively reasonable basis to believe Case needed [[Emergency Aid|emergency aid]]: they knew of his mental-health and alcohol problems and prior suicide talk; they learned he had threatened suicide, spoke of a suicide note, and possibly fired a gun before the call ended; and they saw empty beer cans, an empty holster, and a notepad through the windows, with no response to urgent knocking. Whether Case had already shot himself (needing care) or had not (acute suicide risk), entry to prevent that result was reasonable — and the Fourth Amendment did not require officers to "leave him to his fate." The Court rejected Case's "suicide-by-cop" theory that the entry itself created the only danger.

## Conclusion
Affirmed (the judgment, though not all the reasoning, of the Montana Supreme Court). *Brigham City*'s objective-reasonableness test for emergency-aid home entries applies on its own terms and was satisfied here.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Kagan, J., unanimous; Sotomayor, J., and Gorsuch, J., concurring).
- *Case* reaffirms and clarifies [[Brigham City v. Stuart]], rejecting both a *[[Terry v. Ohio|Terry]]*-style reasonable-suspicion gloss and a probable-cause gloss on the emergency-aid standard. It is consistent with [[Caniglia v. Strom]] (no freestanding community-caretaking home entry — welfare entries must route through [[Emergency Aid|emergency aid]]) and applies the totality-of-the-circumstances approach reaffirmed in [[Ohio v. Robinette]].

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*

## Sources
- *Case v. Montana*, 607 U.S. ___ (2026) (No. 24-624) — https://www.courtlistener.com/opinion/10774335/case-v-montana/ — pinpoints: slip op. at 7, 8, 9, 10–11. Below: *State v. Case*, 417 Mont. 354, 553 P.3d 985 (2024), affirmed.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "23bdfc1c0677f95c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Brigham City's objective-reasonableness standard for warrantless home entries to render emergency aid applies without further gloss — it is neither lowered to Terry reasonable suspicion nor raised to probable cause — and asks only whether an officer had an objectively reasonable basis for believing entry was needed to prevent or deal with serious harm.", "title": "Case v. Montana"}}
{"assertion_id": "b9ebd3b65a251454", "dimension": "support", "kind": "home_role", "locator": {"home": "Emergency Aid"}, "payload": {"home": "Emergency Aid", "role": "Key — Progeny / Refinement", "title": "Case v. Montana"}}
{"assertion_id": "0f934c4da50f7717", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2026-01-14", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Case v. Montana", "field_i_validity": "good_law", "scope_note": "Decided January 14, 2026 (slip opinion; final U.S. Reports pagination pending). Kagan, J., for a unanimous Court; Sotomayor, J., and Gorsuch, J., concurring. Current good law.", "title": "Case v. Montana", "varies_by_point": "false"}}
{"assertion_id": "3cd3eb7474c8185d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Case v. Montana"}}
```

### lake record — Case v. Montana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Case v. Montana",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Case v. Montana",
    "case_name_short": "Case",
    "case_name_full": "",
    "input_case_name": "Case v. Montana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2026-01-14",
    "year": 2026,
    "docket": "24-624",
    "cluster_id": 10774335,
    "lead_opinion_id": 11240920,
    "sibling_ids": [
      11240920
    ],
    "absolute_url": "/opinion/10774335/case-v-montana/",
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
      "id": "pin-slip7",
      "page": null,
      "quote": "doctrine. ## Issue Whether the warrantless home entry to render emergency aid satisfied the Fourth Amendment, and what standard governs such an entry \u2014 Brigham City's objective reasonableness, a lower reasonable-suspicion test, or a higher probable-cause test. ## Rule Brigham City's standard governs, and it applies without further gloss. The Court declined to lower it to reasonable suspicion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-slip8",
      "page": null,
      "quote": "We decline Case's invitation to put a new probable-cause spin onto Brigham City. . . . So Brigham City adopted a different approach. Rather than strain to relate probable-cause decisions to emergency-aid situations, we asked simply whether an officer had 'an objectively reasonable basis for believing' that his entry was direly needed to prevent or deal with serious harm.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-slip9",
      "page": null,
      "quote": "an emergency-aid entry provides no basis to search the premises beyond what is reasonably needed to deal with the emergency while maintaining the officers' safety. But we assess the reasonableness of that limited entry on its own terms, rather than through the lens generally used to consider investigative activity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-slip10",
      "page": null,
      "quote": "We repeat today what we have held before: An officer may enter a home without a warrant if he has 'an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened with such injury.' . . . The officers' entry satisfied that test.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-01-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Case v. Montana",
    "varies_by_point": false,
    "scope_note": "Decided January 14, 2026 (slip opinion; final U.S. Reports pagination pending). Kagan, J., for a unanimous Court; Sotomayor, J., and Gorsuch, J., concurring. Current good law.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11240920) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
      },
      "lane2_top_cited": {
        "query": "cites:(11240920)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11240920)",
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
    "complete_query": "cites:(11240920)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11240920,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/case-v-montana.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11240920,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 171142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 1184823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 2381644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 2764455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4227836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4248565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4677033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4687473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4697833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 5432529,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 6585877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9413217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9416513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9421885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9427279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9429232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9430773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9430897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9431609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9431641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9433390,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9837829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9888304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 10499459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 11051434,
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
    "date_created": "2026-07-04T23:43:23Z",
    "date_modified": "2026-07-06T13:36:09Z",
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
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:43:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:43:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:36:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:43:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Case v. Montana

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

                            CASE v. MONTANA

       CERTIORARI TO THE SUPREME COURT OF MONTANA

   No. 24–624.      Argued October 15, 2025—Decided January 14, 2026


In Brigham City v. Stuart, 547 U. S. 398, 400, the Court held that the
  Fourth Amendment allows police officers to enter a home without a
  warrant if they have an “objectively reasonable basis for believing”
  that someone inside needs emergency assistance. In this case, Mon-
  tana police officers responded to the home of petitioner William Case
  after his ex-girlfriend called 9–1–1 to report that he was threatening
  suicide and may have shot himself. The officers knocked on the doors
  and yelled into an open window, but got no response. They could see
  an empty handgun holster and something that looked like a suicide
  note inside, and they ultimately decided to enter the home to render
  emergency aid. When one officer approached a bedroom closet in
  which Case was hiding, Case threw open the closet curtain while hold-
  ing an object that looked like a gun. Fearing that he was about to be
  shot, the officer shot and injured Case. An ambulance was called to
  take Case to the hospital, and officers found a handgun next to where
  Case had stood.
     Case was charged with assaulting a police officer. Case moved to
  suppress all evidence obtained from the home entry, arguing that the
  police violated the Fourth Amendment by entering without a warrant.
  The trial court denied the motion, and a jury found Case guilty. A
  divided Montana Supreme Court upheld the officers’ entry as lawful
  under Montana’s caretaker doctrine, rejecting the contention that an
  officer must have probable cause to believe that an occupant needs
  emergency aid.
Held: Brigham City’s objective reasonableness standard for warrantless
 home entries to render emergency aid applies without further gloss
 and was satisfied in this case. Pp. 5–11.
2                           CASE v. MONTANA

                                  Syllabus

       (a) “[S]earches and seizures inside a home without a warrant are
    presumptively unreasonable” under the Fourth Amendment. Brigham
    City, 547 U. S., at 403. But the “warrant requirement is subject to
    certain exceptions,” Lange v. California, 594 U. S. 295, 301, including
    the need to render emergency assistance. The Court first approved a
    warrantless home entry to render emergency assistance in Brigham
    City, holding that officers may enter when they have “an objectively
    reasonable basis for believing that an occupant is seriously injured or
    imminently threatened with such injury.” 547 U. S., at 400.
       The Montana Supreme Court’s opinion below strayed from that rule.
    Most important, the emergency-aid test incorporated in Montana’s
    caretaker doctrine evokes the Fourth Amendment standard of “reason-
    able suspicion” that applies to relatively non-invasive street stops. But
    Brigham City adopted a different standard for home entries.
       Case now urges the Court to understand Brigham City as sounding
    in probable cause, but the Court declines to put a new probable-cause
    spin onto the emergency-aid standard. Probable cause is “peculiarly
    related to criminal investigations,” Treasury Employees v. Von Raab,
    489 U. S. 656, 667, and that body of law would fit awkwardly, if at all,
    in the non-criminal, non-investigatory setting at issue here. Rather
    than strain to relate probable-cause decisions to emergency-aid situa-
    tions, Brigham City asked simply whether an officer had “an objec-
    tively reasonable basis for believing” that entry was direly needed to
    prevent or deal with serious harm. 547 U. S., at 400. Courts should
    assess the reasonableness of an emergency-aid entry on its own terms,
    rather than through the lens generally used to consider investigative
    activity. Pp. 5–9.
       (b) The officers here had an “objectively reasonable basis for believ-
    ing” that their entry was needed to prevent Case from ending his life.
    The information the officers obtained from Case’s ex-girlfriend, com-
    bined with their observations at the scene, suggested that Case may
    already have shot himself or would do so absent intervention. The of-
    ficers’ decision to enter his home to prevent that result was reasonable.
    Accordingly, the Court affirms the judgment (even though not all the
    reasoning) of the Montana Supreme Court. Pp. 9–11.
417 Mont. 354, 553 P. 3d 985, affirmed.

   KAGAN, J., delivered the opinion for a unanimous Court. SOTOMAYOR,
J., and GORSUCH, J., filed concurring opinions.
                        Cite as: 607 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 24–624
                                   _________________


WILLIAM TREVOR CASE, PETITIONER v. MONTANA
      ON WRIT OF CERTIORARI TO THE SUPREME COURT
                      OF MONTANA
                               [January 14, 2026]

   JUSTICE KAGAN delivered the opinion of the Court.
   In Brigham City v. Stuart, 547 U. S. 398, 400 (2006), this
Court held that police officers may enter a home without a
warrant if they have an “objectively reasonable basis for be-
lieving” that someone inside needs emergency assistance.
The question presented is whether that standard means
that officers must have “probable cause” for the intrusion,
as they typically would when investigating a crime. We
hold it does not. The probable-cause requirement is rooted
in, and derives its meaning from, the criminal context, and
we decline to transplant it to this different one. Brigham
City’s reasonableness standard means just what it says,
with no further gloss. And here it was satisfied because the
police had “an objectively reasonable basis for believing”
that a homeowner intended to take his own life and, indeed,
may already have shot himself.
                              I
   This case began with an alarming phone call—from peti-
tioner William Case to his ex-girlfriend J. H., both residents
of a small town in Montana. Case told J. H. on the call that
“he was going to kill himself.” App. 67 (testimony of J. H.).
Because Case sounded “erratic,” J. H. assumed he had been
2                     CASE v. MONTANA

                      Opinion of the Court

drinking. Ibid. She tried to talk Case out of committing
suicide, but “couldn’t reel him back”: With each passing mo-
ment, Case “became more methodical about what he was
going to do.” Id., at 68. Case said that he was “going to get
a note”—presumably meaning a suicide note, for J. H. or
others to find. Ibid. And then J. H. heard a “clicking”
sound, like the “cock[ing of] a gun.” Ibid. J. H. told Case
she was going to call the police, but that seemed only to an-
tagonize him: Case replied “he would shoot them all too.”
Id., at 69. Finally, J. H. heard “a pop” followed by “noth-
ing”—“just dead air.” Ibid. She “yelled [Case’s] name a few
times,” but got no response, leading her to think he had
“pulled the trigger.” Ibid. So she called 9–1–1 to report the
incident and drove as fast as she could to Case’s home.
   Three police officers, dispatched to do “a welfare check on
a suicidal male,” met J. H. outside the house. Id., at 104
(testimony of officer). They decided the situation was “very
serious,” based both on what J. H. told them about the call
and on what they already knew about Case. Id., at 75, 157.
The officers were aware that Case had a history of alcohol
abuse and mental-health issues; that he had previously
threatened suicide at the school where he worked; and that
he had once seemed to attempt “suicide-by-cop,” by con-
fronting the police in a way that was likely to provoke a le-
thal response. So the three officers requested that the chief
of police come to the scene. While waiting for him, they cir-
cled the house looking for signs of injury or danger. They
knocked on the doors and yelled into an open window, but
got no response. Shining their flashlights inside, they could
make out empty beer cans, an empty handgun holster, and
a notepad with writing on it, which they took to be the sui-
cide note Case had mentioned to J. H. At that point, how-
ever, they saw no sign of Case.
   Once the chief came, the officers conferred and decided to
enter the house “to render emergency aid.” Id., at 198. In
the best-case scenario, they hoped to “talk [Case] down” and
                  Cite as: 607 U. S. ____ (2026)              3

                      Opinion of the Court

prevent any injury. Id., at 174. But given J. H.’s account,
the officers considered as well another possibility—that
Case had already shot himself and might be “in there bleed-
ing.” Id., at 85. At the same time, they worried that if Case
remained unharmed, their entry could spark a confronta-
tion. See id., at 174, 192–193. So they equipped themselves
with long-barrel guns and a ballistic shield before going in.
   The officers entered the house through the front door,
about 40 minutes after they first arrived. They announced
themselves loudly, and continued to call out as they walked
through the home. Case did not answer; he was hiding in
the closet of a bedroom upstairs. When one of the officers
entered that room, Case threw open the closet curtain and
appeared from behind it, holding “a black object” which
looked like a gun. Id., at 194. Fearing that he was about
to be shot, the officer fired his own rifle. The bullet hit Case
in the abdomen, and another officer rushed to administer
first aid. An ambulance was called to take Case to the near-
est hospital (where he recovered). Meanwhile, one of the
officers found a handgun in a laundry basket next to the
place where Case had stood.
   The county attorney charged Case with assaulting a po-
lice officer. Case moved to suppress all evidence obtained
as a result of the home entry, arguing that the police had
violated the Fourth Amendment by coming into his house
without a warrant. The trial court denied the motion on the
ground that the police officers were responding legitimately
to an “emergency.” App. to Pet. for Cert. 42a. A Montana
jury then found Case guilty of the crime charged.
   On appeal, a divided Montana Supreme Court upheld the
trial court’s ruling that the officers’ entry was lawful. The
majority analyzed the issue under its “community care-
taker doctrine.” 553 P. 3d 985, 990 (Mont. 2024). It noted
that a recent Fourth Amendment decision of this Court,
Caniglia v. Strom, 593 U. S. 194, 198 (2021), had rejected a
“community caretaking rule” allowing a warrantless home
4                        CASE v. MONTANA

                          Opinion of the Court

entry even absent a “need to render emergency assistance”
to an occupant. But the Montana court thought its commu-
nity-caretaker doctrine survived that holding because it de-
manded such an emergency. Under that doctrine, the court
explained, police could enter a home to do a “welfare check”
only when “objective, specific and articulable facts” would
lead an “experienced officer [to] suspect” that a person in-
side “is in need of help or is in peril.” 553 P. 3d, at 990, 991.
And the court found that facts meeting that description ex-
isted here because of the likelihood of suicide. See id., at
994. The court rejected Case’s alternative standard: that a
police officer must have “probable cause to believe” the oc-
cupant in need of emergency aid. Id., at 992. The “probable
cause” locution, the court suggested, applies only when the
police are “engaged in a criminal investigation.” Ibid. The
dissenting justices, by contrast, favored the proposed prob-
able-cause rule, which they concluded the officers here did
not satisfy. See id., at 996, 998 (opinion of McKinnon, J.).
In the dissent’s view, the court’s different approach resem-
bled the “mere reasonable suspicion” standard applicable to
comparatively non-invasive street stops. Id., at 999. That
standard, the dissent thought, was too easily met to support
a warrantless entry into a home. See id., at 996, 999.
   We granted certiorari, 605 U. S. 968 (2025), because
courts have differed on whether police officers entering a
home to provide emergency aid need “probable cause” to be-
lieve that an occupant is in peril.* We conclude that stand-
ard, borrowed from the criminal context, is inapt. We in-
stead hold just what we have held before: that the officers
——————
  *Compare, e.g., Estate of Chamberlain v. White Plains, 960 F. 3d 100,
105 (CA2 2020) (requiring probable cause); United States v. Cooks, 920
F. 3d 735, 742 (CA11 2019) (same); Corrigan v. District of Columbia, 841
F. 3d 1022, 1030 (CADC 2016) (same), with, e.g., Hill v. Walsh, 884 F. 3d
16, 23 (CA1 2018) (not requiring probable cause); United States v. Quar-
terman, 877 F. 3d 794, 800 (CA8 2017) (same); United States v. Gambino-
Zavala, 539 F. 3d 1221, 1225 (CA10 2008) (same).
                 Cite as: 607 U. S. ____ (2026)             5

                     Opinion of the Court

may enter if, but only if, they have an “objectively reasona-
ble basis for believing” that an occupant faces serious dan-
ger. Brigham City, 547 U. S., at 400.
                               II
   The Fourth Amendment provides that “[t]he right of the
people to be secure in their persons, houses, papers, and ef-
fects, against unreasonable searches and seizures, shall not
be violated.” At the “very core” of that guarantee, as this
Court has often stated, “stands the right of a man to retreat
into his own home and there be free from unreasonable gov-
ernmental intrusion.” Caniglia, 593 U. S., at 198 (quoting
Florida v. Jardines, 569 U. S. 1, 6 (2013)). When the intru-
sion is into that most private place, “reasonableness” usu-
ally means having a warrant. Brigham City, 547 U. S., at
403 (“It is a basic principle of Fourth Amendment law that
searches and seizures inside a home without a warrant are
presumptively unreasonable”). “But not always: The war-
rant requirement is subject to certain exceptions.” Lange v.
California, 594 U. S. 295, 301 (2021). And among those is
one pertinent here, involving the need to provide an occu-
pant with emergency aid.
   This Court first approved a warrantless home entry to
render emergency assistance in Brigham City. There, po-
lice officers responding to a noise complaint observed
through a kitchen window a physical altercation between
an adolescent and several adults. As they watched, the
teenager punched one of the adults in the face, “sending
[him] to the sink spitting blood.” 547 U. S., at 406. The
officers immediately entered the home through a nearby
screen door and, announcing their presence, caused the
fight to cease. We unanimously approved the warrantless
entry as “reasonable under the circumstances.” Ibid. And
we explained what made it so: The officers had “an objec-
tively reasonable basis for believing that an occupant [was]
6                    CASE v. MONTANA

                     Opinion of the Court

seriously injured or imminently threatened with such in-
jury.” Id., at 400.
   Three years later, in Michigan v. Fisher, we reiterated
what we had said in Brigham City about the “emergency
aid exception.” 558 U. S. 45, 47 (2009) (per curiam). The
police in Fisher, also responding to a neighbor’s report,
found a scene redolent of violence and danger. Three win-
dows were broken, with the glass strewn on the ground out-
side; blood was smeared on one of the doors, as well as on
the smashed-in hood of a pickup truck in the driveway; and,
visible through a window, a man inside the house was
“screaming and throwing things” at an unseen target. Id.,
at 48. We held that the officers’ entry in those circum-
stances was “reasonable under the Fourth Amendment,”
just as it had been in Brigham City. 558 U. S., at 48. Using
the same standard articulated there, we concluded that the
officers had “an objectively reasonable basis for believing”
that an occupant of the home needed immediate aid. Id., at
47 (quoting Brigham City, 547 U. S., at 406).
   Finally, in Caniglia, we reaffirmed Brigham City even as
we rejected a broader “community caretaking” justification
for warrantless home entries. The police had gone to Ed-
ward Caniglia’s home after his wife reported that he was
suicidal. Caniglia spoke with the officers on his front porch
and agreed to go to a hospital for psychiatric testing. Then,
once he had left, the officers went inside and took away two
handguns he owned. The lower courts approved the entry
on the ground that the officers were performing “commu-
nity caretaking functions.” 593 U. S., at 196. But we de-
clined to recognize such an “open-ended license” for law en-
forcement officers to enter private homes. Id., at 199.
Citing Brigham City, we readily acknowledged that officers
may enter a home to “render emergency assistance to an
injured occupant or to protect an occupant from imminent
injury.” 593 U. S., at 198. But such emergency conditions
                  Cite as: 607 U. S. ____ (2026)            7

                      Opinion of the Court

were indeed necessary and, given the facts, the officers had
never tried to defend their entry on that basis.
   The Montana Supreme Court’s opinion strayed from the
Fourth Amendment rule that trio of decisions sets out. To
begin with, the court’s use of “community caretaker” doc-
trine was ill-advised, given that Caniglia contrasted “com-
munity caretaking” with “render[ing] emergency assis-
tance” and concluded that the former cannot alone justify a
warrantless home entry. Ibid. The Montana court, to be
sure, tried to reconcile its approach with Caniglia by depict-
ing its community-caretaker rule as allowing home entries
only in emergencies. See 553 P. 3d, at 991. But using ter-
minology that this Court has held misplaced in home-entry
cases could serve only to confuse the issue. And yet more
fundamental, the emergency-aid test incorporated in Mon-
tana’s caretaker doctrine is different from the one adopted
in Brigham City. As noted above, Montana’s test finds a
home entry “reasonable” when an officer has “specific and
articulable facts” from which to “suspect” that someone
needs help. 553 P. 3d, at 991; see supra, at 4. That test’s
language, as the dissenting justices noted, evokes the
Fourth Amendment standard applying to brief, investiga-
tive street stops: “reasonable suspicion” based on “specific
and articulable facts.” United States v. Sokolow, 490 U. S.
1, 7 (1989); Terry v. Ohio, 392 U. S. 1, 21 (1968); 553 P. 3d,
at 999 (McKinnon, J.). But Brigham City did not adopt
Terry’s reasonable-suspicion standard for home entries, as
both the State of Montana and the United States as amicus
curiae acknowledge. See Tr. of Oral Arg. 56, 68–69, 80. Ra-
ther, Brigham City formulated its own standard for dealing
with household emergencies—again, whether an officer has
“an objectively reasonable basis for believing” that an occu-
pant is seriously injured or imminently threatened with
such harm. 547 U. S., at 400.
   Case, however, wants something more. He recognizes
that the Brigham City test applies here, and that it has had
8                     CASE v. MONTANA

                      Opinion of the Court

but one formulation: In describing and applying that stand-
ard, we have never used any different terms. See Brief for
Case 24. But still, Case urges us now to understand the
Brigham City test as “sound[ing] in probable cause.” Brief
for Case 15, 24. What the test really requires, Case con-
tends, is that police officers “have probable cause to believe
[an occupant is] seriously injured or imminently threatened
with such injury.” Id., at 2. Case reaches that conclusion
based mainly on the Fourth Amendment’s recognition of the
“sanctity of the home.” Id., at 29. Given that special status,
he argues, a home entry’s aid-giving, “noninvestigatory
purpose” should make no difference: The same probable-
cause principles used in deciding whether “criminal activity
[is] afoot” should apply as well in “assessing the risk and
gravity of an emergency.” Reply Brief 1–2, 8, 16.
   We decline Case’s invitation to put a new probable-cause
spin onto Brigham City. “[T]he probable-cause standard,”
this Court has often stated, “is peculiarly related to crimi-
nal investigations.” Treasury Employees v. Von Raab, 489
U. S. 656, 667 (1989) (quoting Colorado v. Bertine, 479 U. S.
367, 371 (1987)). The standard’s history is “rooted” in the
“criminal investigatory context.” O’Connor v. Ortega, 480
U. S. 709, 723 (1987) (plurality opinion); see Henry v.
United States, 361 U. S. 98, 100–102 (1959). And the stand-
ard has acquired meaning over time by virtue of that con-
text, as judges have assessed, in case after case, the requi-
site likelihood of finding criminal contraband or evidence.
See, e.g., Illinois v. Gates, 462 U. S. 213, 238–239 (1983).
The resulting body of law would fit awkwardly, if at all, in
the non-criminal, non-investigatory setting at issue here.
So Brigham City adopted a different approach. Rather than
strain to relate probable-cause decisions to emergency-aid
situations, we asked simply whether an officer had “an ob-
jectively reasonable basis for believing” that his entry was
direly needed to prevent or deal with serious harm. 547
U. S., at 400. In adhering to that question, we respect as
                 Cite as: 607 U. S. ____ (2026)            9

                     Opinion of the Court

ever the “first among equals” status the Fourth Amend-
ment affords the home. Jardines, 569 U. S., at 6; see
Caniglia, 593 U. S., at 198–199. And in that vein, we note
that an emergency-aid entry provides no basis to search the
premises beyond what is reasonably needed to deal with the
emergency while maintaining the officers’ safety. But we
assess the reasonableness of that limited entry on its own
terms, rather than through the lens generally used to con-
sider investigative activity.
   Doing so here yields a ready conclusion: The officers had,
as Brigham City requires, an “objectively reasonable basis
for believing” that their intervention was needed to prevent
serious harm. As earlier described, the officers knew first-
hand that Case suffered from mental-health and alcohol-
abuse problems, and that he had previously talked about
committing suicide. See supra, at 2. When they reached
Case’s house, they learned about J. H. and Case’s just-
concluded phone call—that Case, in an apparently inebri-
ated state, threatened to kill himself, spoke of preparing a
suicide note, and quite possibly cocked or even shot a gun
before the line went dead. The concerns that call raised
were heightened by what the officers could see through the
windows—empty beer cans, an empty holster, and a note-
pad—as well as by Case’s failure to respond to their urgent
knocking. If Case had already shot himself, he could have
been severely injured and in need of immediate medical
care. And if he had not, the risk of suicide remained acute,
given all the facts then known to the officers. It was thus
objectively reasonable for the police to believe that Case
needed emergency aid.
   Case counters that only the police entry itself created a
“likely danger.” Brief for Case 45. His argument turns on
the prospect of suicide-by-cop. As noted earlier, Case had
once before acted in a way seemingly designed to provoke a
lethal police response, as the officers knew. See supra, at
2. And J. H. told the officers that Case had threatened to
10                    CASE v. MONTANA

                      Opinion of the Court

“shoot them all too” if they came to the scene. Ibid. So the
“main risk the officers objectively faced,” Case posits, was
that “their very entry would induce” a shoot-out, leading to
a “suicide-by-cop.” Brief for Case 18. And indeed, Case con-
tends, the officers knew that: Why else would they have
“waited roughly 40 minutes after their arrival” before en-
tering his home? Id., at 43. Case concludes that if the of-
ficers had only left well enough alone, nothing would have
happened.
   But Case much oversimplifies a complex situation. The
objective reasonableness of an officer’s conduct under
Brigham City, as in other Fourth Amendment contexts, is
evaluated by looking at the “totality of the circumstances.”
E.g., Barnes v. Felix, 605 U. S. 73, 80 (2025); Ohio v. Robi-
nette, 519 U. S. 33, 39 (1996). One of those circumstances
was no doubt that Case could provoke a confrontation. As
noted earlier, that was partly why the officers called the po-
lice chief to the scene and why they carefully considered
protective measures—leading to some delay in their entry.
See supra, at 2. But there is no basis for thinking that the
officers would have gone into Case’s home just so he could
instigate a gunfight. The circumstances making their entry
reasonable, as just stated, were those suggesting that Case
may already have shot himself or would do so absent inter-
vention. The statements Case made to J. H. plus the visual
evidence corroborating them indicated that Case wanted to
end his life. The decision of the officers to enter his home
to prevent that result—even at some significant risk to
themselves—was (at the least) reasonable. The Fourth
Amendment did not require them, as Case now argues, to
leave him to his fate.
                        *    *     *
  We repeat today what we have held before: An officer may
enter a home without a warrant if he has “an objectively
reasonable basis for believing that an occupant is seriously
                  Cite as: 607 U. S. ____ (2026)                 11

                      Opinion of the Court

injured or imminently threatened with such injury.”
Brigham City, 547 U. S., at 400. The officers’ entry satisfied
that test. Accordingly, we affirm the judgment (even
though not all the reasoning) of the Montana Supreme
Court.
                                                   It is so ordered.
                  Cite as: 607 U. S. ____ (2026)             1

                   SOTOMAYOR, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–624
                          _________________


WILLIAM TREVOR CASE, PETITIONER v. MONTANA
     ON WRIT OF CERTIORARI TO THE SUPREME COURT
                     OF MONTANA
                       [January 14, 2026]

   JUSTICE SOTOMAYOR, concurring.
   I join the Court’s opinion, which holds that police officers
may enter a home without a warrant if they have an “ ‘ob-
jectively reasonable basis for believing’ ” that an occupant is
seriously injured or imminently threatened with such
harm. Ante, at 5, 7, 10. Although the Montana Supreme
Court’s opinion appeared, erroneously, to apply a lower
standard akin to reasonable suspicion, I agree that the of-
ficers here had an “ ‘objectively reasonable basis for believ-
ing’ ” that Case needed emergency assistance because he
may have already shot himself or was imminently going to
do so. Ante, at 7–10.
   I write separately to underscore the unique considera-
tions that law enforcement and courts should bear in mind
when assessing whether there is an “objectively reasonable
basis to believe” that a person experiencing a mental-health
crisis needs law enforcement to “render emergency assis-
tance.” Brigham City v. Stuart, 547 U. S. 398, 403 (2006).
As Brigham City explained, the “ ‘justification for what
would be otherwise’ ” an illegal warrantless entry of a home
in this context is “ ‘[t]he need to protect or preserve life or
avoid serious injury.’ ” Ibid. (quoting Mincey v. Arizona, 437
U. S. 385, 392 (1978)). The officers in Brigham City, for in-
stance, needed to enter the house to break up an ongoing
fight to protect a person whom they saw through a window
being struck in the face and to prevent further violence. 547
2                        CASE v. MONTANA

                      SOTOMAYOR, J., concurring

U. S., at 406. When an officer is called to respond to a per-
son at risk of suicide, however, entering the house may not
always be the objectively reasonable course of action to
“ ‘preserve life or avoid serious injury.’ ” Id., at 403 (quoting
Mincey, 437 U. S., at 392).
   In these kinds of circumstances, the presence of law en-
forcement at times can escalate the situation rather that
ameliorate it, putting both the occupant and the officers in
danger. See, e.g., Chamberlain v. White Plains, 960 F. 3d
100, 101–104, 108 (CA2 2020) (officers repeatedly at-
tempted entry of the home of a person with a known “his-
tory of mental illness,” eventually shooting and killing the
occupant after he repeatedly said he was “ ‘okay’ ” and offic-
ers saw he did not need medical attention); Bailey v. Ken-
nedy, 349 F. 3d 731, 734–736, 744 (CA4 2003) (officers at-
tempted to enter house based on a neighbor’s report of
suicide, eventually kicking and striking occupant to arrest
him, despite occupant telling the officers that he was not
suicidal and that they should leave). The risk of escalation
is also heightened by the prevalence of firearms in nearly
half of American households.1 Police may employ more
forceful tactics when they know a firearm is in the house,
and an occupant who is experiencing an acute mental-
health crisis may react more unpredictably in response.
See, e.g., Corrigan v. District of Columbia, 841 F. 3d 1022,
1025–1028 (CADC 2016) (despite occupant voluntarily
meeting the police outside and disclaiming any intention to
harm himself, the officers triggered occupant’s post-
traumatic stress disorder after kicking his door and search-
ing his house, based on report that he was suicidal and
owned firearms); Frazier v. Miller, 404 Mont. 1, 484 P. 3d
912, 916 (2021) (occupant initially told police he was “ ‘fine’ ”
and to “go away” but drew pistol to his own head when the
——————
 1 In 2025, 42% of Americans reported living in a gun-owning household.

Gallup, Guns, https://news.gallup.com/poll/1645/guns.aspx.
                     Cite as: 607 U. S. ____ (2026)                   3

                      SOTOMAYOR, J., concurring

officer continued to attempt entry, leading the officer to
draw his gun in response and eventually shoot the occu-
pant).
   Studies show that individuals with serious mental-health
conditions are disproportionately likely to be injured and
seven times more likely to be killed during police interac-
tions compared to the general population.2 One report
showed that over a 2-year period, “calls for help resulted in
law enforcement officers shooting and killing the very peo-
ple they were called on to assist” in 178 cases.3 Another
study found that police shooting incidents involving behav-
ioral health concerns (suicidal behavior, substance use, or
serious mental illness) were 2.1 times more likely to result
in fatal injury than other police shooting incidents.4 Fur-
ther, individuals with a mental illness were “2.8 times more
likely” to “be killed in their own homes” compared to those
without a mental illness.5
   Given these risks, in some circumstances it may be more
reasonable for officers to try different means of de-escala-
tion before entering the home of a person experiencing a
mental-health crisis. Officers could, for example, attempt
to speak with the occupant from a distance or over the
phone; contact family, friends, or neighbors to help inter-
vene; call in specialized police units, such as negotiators or

——————
  2 See H. Jun, J. DeVylder, & L. Fedina, Police Violence Among Adults

Diagnosed With Mental Disorders, 45 Health & Soc. Work 81 (May
2020); A. Saleh, P. Applebaum, X. Liu, T. Stroup, & M. Wall, Deaths of
People with Mental Illness During Interactions With Law Enforcement,
58 Int’l J. L. & Psychiatry 110, 114 (May-June 2018) (Saleh).
  3 J. Gerberg & A. Li, When a Call to the Police for Help Turns Deadly,

Washington Post, June 22, 2022, https://www.washingtonpost.com/
investigations/interactive/2022/police-shootings-mental-health-calls/.
  4 J. Ward et al., National Burden of Injury and Deaths From Shootings

by Police in the United States, 2015–2020, 4 Am. J. Pub. Health 387,
391–392 (2024).
  5 Saleh 114.
4                          CASE v. MONTANA

                        SOTOMAYOR, J., concurring

officers trained in crisis intervention;6 or otherwise work
with mental-health professionals to approach the occu-
pant.7 Officers called to respond to these kinds of situations
should carefully investigate and assess the nature of the po-
tential crisis and determine whether there is an objectively
reasonable basis to believe that the occupant needs emer-
gency aid inside before entering without a warrant. Once
the decision is made to enter, moreover, the “manner” of the
officers’ entry and their subsequent conduct inside must
also be “reasonable.” Brigham City, 547 U. S., at 406.
    This case highlights the very complexities that will often
attend emergency-aid interventions involving reported
mental-health crises. Multiple facts suggested that Case
did not need emergency aid but was instead waiting inside
for the officers in order to provoke a confrontation that
would result in “suicide-by-cop.”
    Case had told his girlfriend, J. H., on the phone that he
would “shoot them all” if she called the police to his house.
App. 69. Once J. H. arrived at the house, she told the offic-
ers that Case threatened to “shoot it out” with the police.
Id., at 70–74. The officers also knew that in a prior incident
in which police were called to respond to a suicide attempt
by Case, Case had confronted the police in a way that sug-
gested he was attempting suicide-by-cop. Then, while sur-
veying the house, the officers discussed how Case had
“ ‘tried suicide by cop before’ ” and that it was likely Case
——————
   6 See id., at 114–115; Brief for American Psychiatric Association et al.

as Amici Curiae 18–25 (describing programs that involve sending teams
of specially trained police to respond to calls about mental-health crises).
   7 Many jurisdictions around the country have introduced programs in

which police officers and mental-health professionals jointly respond to
calls about mental-health crises. See Policy Research, Inc. & National
League of Cities, A. Krider, R. Huerter, K. Gaherty, & A. Moore, Re-
sponding to Individuals in Behavioral Health Crisis Via Co-responder
Models (Jan. 2020), https://www.theiacp.org/sites/default/files/SJC
Responding%20to%20Individuals.pdf (describing “co-responder” pro-
grams).
                     Cite as: 607 U. S. ____ (2026)                    5

                       SOTOMAYOR, J., concurring

was “ ‘going to pull a gun on us’ ” once they “ ‘go in the
house.’ ” 417 Mont. 354, 373, 553 P. 3d 985, 998 (2024).
   These facts, taken together, suggested that Case was nei-
ther already injured nor about to injure himself, but rather
that the primary danger he faced would arise only if the
officers entered his house. In other words, these facts
tended to undermine the officers’ basis to believe that he
needed emergency assistance inside.
   The officers’ warrantless entry ultimately did not violate
the Fourth Amendment, however, because there were suf-
ficient facts on the other side of the ledger supporting an
objectively reasonable basis to believe that Case had shot
himself. Critically, Case had told J. H. he had a “loaded
gun” and J. H. heard a “clicking” sound like the “cock[ing]”
of “a gun,” a “pop,” and then “just dead air” despite J. H.
yelling Case’s name multiple times over the phone. App.
68–69; 417 Mont., at 357, 553 P. 3d, at 988. Case also told
J. H. that he was “going to get a note” and “kill himself.”
App. 67–68. When the officers arrived, they saw an empty
handgun holster and notepad with writing inside Case’s
house, and Case did not respond when they shouted his
name into an open window. Considered together, those
facts gave rise to an objectively reasonable basis for the of-
ficers to believe that Case was already injured and in need
of emergency medical assistance, and was not necessarily
waiting inside for the officers seeking to provoke an escala-
tion leading to suicide-by-cop. As a result, the officers did
not violate the Fourth Amendment when they entered
Case’s home.8
   That conclusion, on the facts of this case, does not mean
it will always be objectively reasonable for officers respond-
ing to a mental-health crisis to make a warrantless entry.
——————
  8 Case has not challenged the reasonableness of the officers’ manner of

entry or their conduct inside his house after entry. As a result, neither
the decision below nor this Court had occasion to consider the reasona-
bleness of that conduct.
6                     CASE v. MONTANA

                   SOTOMAYOR, J., concurring

A different mix of information might have led to the conclu-
sion that the officers’ entry itself would put the occupant
(and officers) at a greater risk of escalation and serious in-
jury. Because the “objectively reasonable basis” test, as re-
affirmed by the Court today, demands careful attention to
the case-specific risks that attend mental-health crises, and
requires officers to act reasonably in response, I join the
Court’s opinion in full.
                  Cite as: 607 U. S. ____ (2026)            1

                    GORSUCH, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–624
                          _________________


WILLIAM TREVOR CASE, PETITIONER v. MONTANA
     ON WRIT OF CERTIORARI TO THE SUPREME COURT
                     OF MONTANA
                       [January 14, 2026]

   JUSTICE GORSUCH, concurring.
   Today’s case, like another before it, holds that police of-
ficers generally do not violate a person’s Fourth Amend-
ment rights when they enter his house without a warrant,
but with an “ ‘objectively reasonable basis’ ” for believing
someone inside is in physical danger and in need of imme-
diate aid. Ante, at 7 (quoting Brigham City v. Stuart, 547
U. S. 398, 400 (2006)). Importantly, the Court observes,
this exception to the warrant requirement permits entry
only to the extent reasonably necessary to address the ap-
parent emergency and does not authorize officers to search
a home more broadly. See ante, at 9. With all that, I agree.
   But to me, a question lingers: Why? Does the Fourth
Amendment tolerate this limited emergency aid exception
to the warrant requirement just because five or more Jus-
tices of this Court happen to believe that such entries are
“reasonable”? Or is this exception more directly “tied to the
law”? Carpenter v. United States, 585 U. S. 296, 397 (2018)
(GORSUCH, J., dissenting). The answer, I believe, is the lat-
ter.
   From before the founding through the present day, the
common law has generally permitted a private citizen to en-
ter another’s house and property in order to avert serious
physical harm. In those circumstances, and many others,
courts have historically held that property rights give way
to concern for human safety. See, e.g., 37 Hen. 6, pl. 26;
2                          CASE v. MONTANA

                         GORSUCH, J., concurring

Mouse’s Case, 12 Co. Rep. 63, 77 Eng. Rep. 1341 (K. B.
1608); Respublica v. Sparhawk, 1 Dall. 357, 363 (Pa. 1788);
Ploof v. Putnam, 81 Vt. 471, 474–475, 71 A. 188, 189 (1908).
Courts have long described property-law necessity defenses
like these as turning, too, on the adequacy of the defend-
ant’s judgment, not a post-hoc assessment of necessity in
fact. See, e.g., Mitchell v. Harmony, 13 How. 115, 134–135
(1852); Stone v. Mayor of City of New York, 25 Wend. 157,
176 (N. Y. 1840) (opinion of Verplanck, Sen.); Surocco v.
Geary, 3 Cal. 69, 72 (1853).*
   The common-law emergency rule is now often summa-
rized this way: “One is privileged to enter or remain on land
in the possession of another if it is or reasonably appears to
be necessary to prevent serious harm to . . . the actor[,] . . .
the other[,] or a third person . . . unless the actor knows or
has reason to know that the one for whose benefit he enters
is unwilling that he shall take such action.” Restatement
(Second) of Torts §197(1) (1963–1964). But, of course, this
privilege comes with its logical limitations. So, for example,
a private citizen who enters a home to render emergency
aid lacks license to do so in a manner “which a reasonable
man would not regard as necessary to” address the appar-
ent emergency. Id., §214, and Comment a; see also id., §197,
Comment a; Des Moines v. Webster, 861 N. W. 2d 878, 883–
885 (Iowa App. 2014); State v. Lukus, 149 Mont. 45, 50–51,
423 P. 2d 49, 52–53 (1967).
——————
   *Contrary to Mr. Case’s argument, King v. Coate, Lofft. 73, 98 Eng.
Rep. 539 (K. B. 1772), does not establish that the common law demanded
an exacting showing of actual necessity to defeat a claim for trespass.
True, Lord Mansfield explained that any necessity defense in that case
would need to “stand the strictest test,” with the “necessity manifestly
proved.” Id., at 75, 98 Eng. Rep., at 540. But Coate involved an effort to
involuntarily “confin[e] a person in a madhouse” for two months, not a
claim over a home entry. Id., at 74, 98 Eng. Rep., at 539. And it is hardly
surprising that the common law would demand a good deal more to jus-
tify a serious deprivation of liberty than to excuse an invasion of property
rights aimed at protecting human safety.
                   Cite as: 607 U. S. ____ (2026)              3

                     GORSUCH, J., concurring

   Today’s decision echoes both the common-law emergency
aid rule and its limitations. It does so, to be sure, in the con-
text of a law enforcement officer, not a private citizen, who
sought to enter another’s home. But on this point as well the
common law has spoken, long providing that officers gener-
ally enjoy the same legal privileges as private citizens. See,
e.g., Entick v. Carrington, 19 How. St. Tr. 1029, 1066 (C. P.
1765); 1 J. Chitty, Criminal Law 36 (1819); 2 M. Hale, His-
toria Placitorum Coronae 91 (1736). And, reflecting the
common law here again, this Court has held that the Fourth
Amendment usually permits officers lacking a valid war-
rant to “take actions that any private citizen might do with-
out fear of liability.” Caniglia v. Strom, 593 U. S. 194, 198
(2021) (internal quotation marks omitted). But they nor-
mally may do “no more” than that. Kentucky v. King, 563
U. S. 452, 469 (2011); see also Entick, 19 How. St. Tr., at
1066.
   It should come as no surprise that our decision today
might accord with the accumulated learning of the common
law—just as it should come as no surprise that our applica-
tion of the Fourth Amendment ought to be informed by the
common law’s lessons rather than mere intuition. For a pe-
riod, to be sure, the miasma created by this Court’s Katz era
led some to think the scope of the rights guaranteed by the
Fourth Amendment depend on nothing more than current
judicial instincts about “reasonable expectations of pri-
vacy.” See Carpenter, 585 U. S., at 394–395, 405–406
(GORSUCH, J., dissenting). But that confusion cannot last
forever, for no one should think the rights of Americans
hang on so thin a thread. Instead, and as Justice Story rec-
ognized, the Fourth Amendment is made of sturdier stuff,
representing “the affirmance of a great constitutional doc-
trine of the common law.” 3 Commentaries on the Consti-
tution of the United States 748 (1833).

```

---

## GROUP: content/cases/Chambers v. Florida.md  (`case`, 5 assertions)

### content_page

```
---
title: "Chambers v. Florida"
type: case
citation: "309 U.S. 227 (1940)"
parallel_cite: "60 S. Ct. 472; 84 L. Ed. 716"
neutral_cite: 1940 U.S. LEXIS 911
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1940
date_decided: 1940-02-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1940-02-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chambers v. Florida
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103301/chambers-v-florida/"
  cluster_id: 103301
  opinion_id: 103301
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Ashcraft v. Tennessee]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "fifth-amendment", "due-process", "confessions", "voluntariness", "coercion"]
holding: "Confessions extracted through prolonged, incommunicado interrogation of helpless prisoners were the product of compulsion and their use…"
lake:
  record_id: Chambers v. Florida
  status: verified
  projected_at: 2026-07-09
---

# Chambers v. Florida

*309 U.S. 227 (1940)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Four Black tenant farmers were arrested without warrants after a robbery-murder and held incommunicado, without counsel, friends, or formal charges. Over five days they were subjected to protracted, repeated interrogation — culminating in an all-night session — amid an atmosphere of mob hostility, until they confessed. The confessions were the basis of their death sentences, affirmed by the Florida courts.

## Issue
Whether confessions extracted by sustained, coercive incommunicado interrogation may be used to convict consistent with the Due Process Clause of the Fourteenth Amendment.

## Rule
No. The confessions were the product of compulsion, not free will, and their use violates due process: "To permit human lives to be forfeited upon confessions thus obtained would make of the constitutional requirement of due process of law a meaningless symbol." — 309 U.S. 227, 240. ^pin-240

"Under our constitutional system, courts stand against any winds that blow as havens of refuge for those who might otherwise suffer because they are helpless, weak, outnumbered, or because they are non-conforming victims of prejudice and public excitement." — [*Id.* at 241](https://www.courtlistener.com/opinion/103301/chambers-v-florida/#:~:text=Under%20our%20constitutional%20system%2C%20courts). ^pin-241

## Application
For five days these petitioners were held without charges, isolated, and interrogated under circumstances "calculated to break the strongest nerves and the stoutest resistance," with the fear of mob violence surrounding them. On those facts the confessions were compelled rather than freely given, and using them to send the petitioners to death denied due process.

## Conclusion
The coerced confessions could not support the convictions; the judgments of the Supreme Court of Florida were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chambers* applies the due-process voluntariness rule of [[Brown v. Mississippi]] to psychological/incommunicado coercion, a line later extended in [[Ashcraft v. Tennessee]] and cabined to require state coercion in [[Colorado v. Connelly]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Chambers v. Florida*, 309 U.S. 227 (1940) — https://www.courtlistener.com/opinion/103301/chambers-v-florida/ — pinpoints: 240, 241.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ba701a05d5ad7534", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "309 U.S. 227 (1940)", "court": "U.S. Supreme Court", "neutral_cite": "1940 U.S. LEXIS 911", "official_citation_present": true, "parallel_cite": "60 S. Ct. 472; 84 L. Ed. 716", "title": "Chambers v. Florida", "year": "1940"}}
{"assertion_id": "a8a1731068eb2253", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Chambers v. Florida"}}
{"assertion_id": "f8feef6fbb50dd73", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Confessions extracted through prolonged, incommunicado interrogation of helpless prisoners were the product of compulsion and their use…", "title": "Chambers v. Florida"}}
{"assertion_id": "229de859e109f4a3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1940-02-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Chambers v. Florida", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Chambers v. Florida", "varies_by_point": "false"}}
{"assertion_id": "b5b6ad87b0d500ce", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chambers v. Florida"}}
```

### lake record — Chambers v. Florida

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chambers v. Florida",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chambers v. Florida",
    "case_name_short": "Chambers",
    "case_name_full": "CHAMBERS Et Al. v. FLORIDA",
    "input_case_name": "Chambers v. Florida",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1940-02-12",
    "year": 1940,
    "docket": null,
    "cluster_id": 103301,
    "lead_opinion_id": 103301,
    "sibling_ids": [
      103301
    ],
    "absolute_url": "/opinion/103301/chambers-v-florida/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "309 U.S. 227",
      "volume": "309",
      "reporter": "U.S.",
      "page": "227",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "60 S. Ct. 472",
        "volume": "60",
        "reporter": "S. Ct.",
        "page": "472",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 716",
        "volume": "84",
        "reporter": "L. Ed.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1940 U.S. LEXIS 911",
        "volume": "1940",
        "reporter": "U.S. LEXIS",
        "page": "911",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "309 U.S. 227",
        "volume": "309",
        "reporter": "U.S.",
        "page": "227",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 S. Ct. 472",
        "volume": "60",
        "reporter": "S. Ct.",
        "page": "472",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 716",
        "volume": "84",
        "reporter": "L. Ed.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1940 U.S. LEXIS 911",
        "volume": "1940",
        "reporter": "U.S. LEXIS",
        "page": "911",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "309 U.S. 227",
    "official_selection": {
      "court_class": "scotus",
      "selected": "309 U.S. 227",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-240",
      "page": null,
      "quote": "--- # Chambers v. Florida *309 U.S. 227 (1940)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Four Black tenant farmers were arrested without warrants after a robbery-murder and held incommunicado, without counsel, friends, or formal charges. Over five days they were subjected to protracted, repeated interrogation \u2014 culminating in an all-night session \u2014 amid an atmosphere of mob hostility, until they confessed. The confessions were the basis of their death sentences, affirmed by the Florida courts. ## Issue Whether confessions extracted by sustained, coercive incommunicado interrogation may be used to convict consistent with the Due Process Clause of the Fourteenth Amendment. ## Rule No. The confessions were the product of compulsion, not free will, and their use violates due process:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-241",
      "page": null,
      "quote": "Under our constitutional system, courts stand against any winds that blow as havens of refuge for those who might otherwise suffer because they are helpless, weak, outnumbered, or because they are non-conforming victims of prejudice and public excitement.",
      "star_marker": "241",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 18800,
      "fragment": "#:~:text=Under%20our%20constitutional%20system%2C%20courts",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1940-02-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chambers v. Florida",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Singleton",
          "cluster_id": 9506618,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Phipps",
          "cluster_id": 9440775,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael E. HARRIS, Petitioner-Appellant, v. Robert WRIGHT, Superintendent, Clallam Bay Correction Center, Respondent-Appellee",
          "cluster_id": 724945,
          "cite": [
            "93 F.3d 581",
            "96 Cal. Daily Op. Serv. 6150",
            "96 Daily Journal DAR 10051",
            "1996 U.S. App. LEXIS 20643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Avendano-Lopez",
          "cluster_id": 1387134,
          "cite": [
            "904 P.2d 324",
            "79 Wash. App. 706"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Luther Wilkins, Jr. v. James A. May",
          "cluster_id": 521076,
          "cite": [
            "872 F.2d 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leroy Mitchell",
          "cluster_id": 483891,
          "cite": [
            "812 F.2d 1250",
            "1987 U.S. App. LEXIS 3549"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Walter McKinley Harris v. John D. Rees, Superintendent, Kentucky State Reformatory",
          "cluster_id": 472621,
          "cite": [
            "794 F.2d 1168",
            "1986 U.S. App. LEXIS 27282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerry Lane Jurek v. W. J. Estelle, Jr., Director, Texas Department of Corrections, Respondent",
          "cluster_id": 379222,
          "cite": [
            "623 F.2d 929",
            "1980 U.S. App. LEXIS 14967"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maria Irma Navia-Duran v. Immigration and Naturalization Service",
          "cluster_id": 352273,
          "cite": [
            "568 F.2d 803",
            "1977 U.S. App. LEXIS 5395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Pearce",
          "cluster_id": 107978,
          "cite": [
            "23 L. Ed. 2d 656",
            "89 S. Ct. 2072",
            "395 U.S. 711",
            "1969 U.S. LEXIS 1165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brady v. United States",
          "cluster_id": 108137,
          "cite": [
            "25 L. Ed. 2d 747",
            "90 S. Ct. 1463",
            "397 U.S. 742",
            "1970 U.S. LEXIS 45"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McMann v. Richardson",
          "cluster_id": 108138,
          "cite": [
            "25 L. Ed. 2d 763",
            "90 S. Ct. 1441",
            "397 U.S. 759",
            "1970 U.S. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griswold v. Connecticut",
          "cluster_id": 107082,
          "cite": [
            "14 L. Ed. 2d 510",
            "85 S. Ct. 1678",
            "381 U.S. 479",
            "1965 U.S. LEXIS 2282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashe v. Swenson",
          "cluster_id": 108114,
          "cite": [
            "25 L. Ed. 2d 469",
            "90 S. Ct. 1189",
            "397 U.S. 436",
            "1970 U.S. LEXIS 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Illinois",
          "cluster_id": 105382,
          "cite": [
            "100 L. Ed. 2d 891",
            "76 S. Ct. 585",
            "351 U.S. 12",
            "1956 U.S. LEXIS 1059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rochin v. California",
          "cluster_id": 104943,
          "cite": [
            "96 L. Ed. 2d 183",
            "72 S. Ct. 205",
            "342 U.S. 165",
            "1952 U.S. LEXIS 2576",
            "25 A.L.R. 2d 1396",
            "96 L. Ed. 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Elstad",
          "cluster_id": 111364,
          "cite": [
            "84 L. Ed. 2d 222",
            "105 S. Ct. 1285",
            "470 U.S. 298",
            "1985 U.S. LEXIS 60",
            "53 U.S.L.W. 4244"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. New York",
          "cluster_id": 104681,
          "cite": [
            "93 L. Ed. 2d 1337",
            "69 S. Ct. 1079",
            "337 U.S. 241",
            "1949 U.S. LEXIS 2308",
            "93 L. Ed. 1337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheppard v. Maxwell",
          "cluster_id": 107247,
          "cite": [
            "16 L. Ed. 2d 600",
            "86 S. Ct. 1507",
            "384 U.S. 333",
            "1966 U.S. LEXIS 1413",
            "1 Media L. Rep. (BNA) 1220",
            "6 Ohio Misc. 231",
            "35 Ohio Op. 2d 431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Allen",
          "cluster_id": 105074,
          "cite": [
            "97 L. Ed. 2d 469",
            "73 S. Ct. 397",
            "344 U.S. 443",
            "1953 U.S. LEXIS 2391",
            "97 L. Ed. 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. California",
          "cluster_id": 106451,
          "cite": [
            "8 L. Ed. 2d 758",
            "82 S. Ct. 1417",
            "370 U.S. 660",
            "1962 U.S. LEXIS 850"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kennedy v. Mendoza-Martinez",
          "cluster_id": 106534,
          "cite": [
            "9 L. Ed. 2d 644",
            "83 S. Ct. 554",
            "372 U.S. 144",
            "1963 U.S. LEXIS 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Oliver",
          "cluster_id": 104521,
          "cite": [
            "92 L. Ed. 2d 682",
            "68 S. Ct. 499",
            "333 U.S. 257",
            "1948 U.S. LEXIS 2452",
            "92 L. Ed. 682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNabb v. United States",
          "cluster_id": 103791,
          "cite": [
            "318 U.S. 332",
            "63 S. Ct. 608",
            "87 L. Ed. 819",
            "1943 U.S. LEXIS 1280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Screws v. United States",
          "cluster_id": 104135,
          "cite": [
            "325 U.S. 91",
            "65 S. Ct. 1031",
            "89 L. Ed. 1495",
            "1945 U.S. LEXIS 2096",
            "162 A.L.R. 1330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shelley v. Kraemer",
          "cluster_id": 104545,
          "cite": [
            "92 L. Ed. 2d 1161",
            "68 S. Ct. 836",
            "334 U.S. 1",
            "1948 U.S. LEXIS 2764",
            "3 A.L.R. 2d 441",
            "92 L. Ed. 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103301) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MDM1MjAwMDAwMCZzPTE0MTg4NjEmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103301%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(103301)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTY0JnM9MTA1OTE3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28103301%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103301)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 2,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(103301)",
    "indexed_citing_opinions": 540,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103301,
        "count": 540,
        "count_source": "search"
      }
    ],
    "citation_count": 844,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chambers-v-florida.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3NDcyOTkmcz00NDY5MTQ5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103301%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103301,
        "cited_id": 89446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 92743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 93324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 95204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 103162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3267432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3381494,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3382712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3383257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3390304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3390887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3396558,
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
    "date_created": "2026-07-04T23:44:10Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:44:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:44:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:47:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:44:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chambers v. Florida

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b297-13">
  Mr. Justice Black
 </author>
<p id="AkAq">
  delivered' the opinion of the Court.
 </p>
<p id="b297-14">
  The grave question presented by the petition for cer-tiorari, granted in forma pauperis,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  is whether proceedings in which confessions, were utilized, and which culminated in sentences of death upon four young negro men in the State of Florida, failed to afford the safeguard of that due process of law guaranteed by the Fourteenth Amendment.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b298-3">
<span citation-index="1" class="star-pagination" label="228"> 
   *228
   </span>
<em>
   First.
  </em>
  The State of Florida challenges our jurisdiction to look behind the judgments below claiming that the issues of fact upon which petitioners base their claim that due process was denied them have been finally determined because passed upon by a jury. 'However, use by a State of an improperly obtained confession may constitute a denial of due process of law as guaranteed in the Fourteenth Amendment.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Since petitioners have seasonably asserted the right under the federal Constitution to have (their guilt or innocence of a capital crime determined without reliance upon confessions obtained by means
  <span citation-index="1" class="star-pagination" label="229"> 
   *229
   </span>
  proscribed by the due process clause of the Fourteenth' Amendment, we must determine independently whether petitioners’ confessions were so obtained, by review of the facts upon which that issue necessarily turns.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b299-4">
<em>
   Second.
  </em>
  The record shows—
 </p>
<p id="b299-5">
  About nine o’clock on the night of Saturday, May 13, 1933, Robert Darsey, an elderly white man, was robbed and murdered in Ppmpano, Florida, a small town in Broward County about twelve miles from Fort Lauderdale, the County seat. The opinion of the Supreme Court of Florida affirming petitioners’ conviction for this crime stated that “It was one of those crimes that induced* an enraged community . . .”
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  And, as the dissenting judge pointed out, “The murder and robbery of the elderly Mr. Darsey . . . was a most dastardly and atrocious crime. It naturally aroused great and well justified public indignation.”
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b299-6">
  Between 9:30 and 10 o’clock after the murder, petitioner Charlie Davis was arrested, and within the next twenty-four hours from twenty-five to forty negroes living in the community, including petitioners Williamson, Chambers, and Woodward, were arrested without warrants and confined in the Broward County jail, at Fort Lauderdale. On the night of the crime, attempts to trail the murderers by bloodhounds brought J. T. Williams, a convict guard, into the proceedings. From then until confessions were obtained and petitioners were sentenced, he took a prominent part. About 11 P. M. on the following Monday, May 15, the sheriff and Williams took several of the imprisoned' negroes, including Williamson and Chambers, to the Dade County jail at Miami. The
  <span citation-index="1" class="star-pagination" label="230"> 
   *230
   </span>
  sheriff testified that they were taken there because he felt a possibility of mob violence and “wanted to give protection to every prisoner ... in jail.” Evidence of petitioners was that on the way to Miami a motorcycle patrolman drew up to the car in which the men were riding and the sheriff “told the cop that he had some negroes that he — [was] taking down to Miami to escape a mob.” This statement was not denied by the sheriff in his testimony and Williams did not testify at all; Williams apparently has now disappeared. Upon order of Williams, petitioner Williamson was kept in the death cell of the Dade County jail. The prisoners thus spirited to Miami were returned to the Fort Lauderdale jail the next day, Tuesday.
 </p>
<p id="b300-4">
  It is clear from the evidence of both the State and petitioners that from Sunday, May 14, to Saturday, May 20, the thirty to forty negro suspects were subjected to questioning and cross questioning (with the exception that several of the suspects were in Dade County jail over one night). From the afternoon of Saturday, May 20, until sunrise of the 21st, petitioners and possibly one or two others underwent persistent and repeated questioning. The Supreme Court of .Florida said the questioning “was in progress several days and all night before the confessions were secured” and referred to the last night as an “all night vigil.” The sheriff who supervised the procedure of continued interrogation testified that he questioned the prisoners “in the day time all the week,” but did not question them during any night before the all night vigil' of Saturday, May 20, because after having “questioned them all day . . . [he] was tired.” Other evidence of the State was “that the officers of Broward County were in that jail almost ■ continually during the whole week questioning these boys, and other boys, in connection with this” case.
 </p>
<p id="b301-5">
<span citation-index="1" class="star-pagination" label="231"> 
   *231
   </span>
  The process of repeated questioning took place in the jailer’s quarters on the fourth floor of the jail. During the week following their arrest and until their confessions were finally acceptable to the State’s Attorney in the early' dawn of Sunday, May 21st, petitioners and their fellow prisoners were led one at a -time from their cells to the questioning room, quizzed, and returned to their cells to await another turn. So'far as appears, the prisoners at no time during the week were permitted to see or confer with counsel or a single friend or relative. When carried singly from his cell and subjected to questioning, each found himself, a single prisoner, surrounded in a fourth floor jail room by four to ten men, the county sheriff, his deputies; a convict guard, and other white officers and citizens of the community.
 </p>
<p id="b301-6">
  The testimony is in conflict as to whether all four petitioners were continually threatened and physically mistreated until they finally, in hopeless desperation and fear of their lives, agreed to confess on Sunday morning just after daylight. Be that as it may, it is certain that by Saturday, May 20th, five days of continued questioning had elicited no confession. Admittedly, a concentration of effort — directed against a small number of prisoners including petitioners — on the part of the questioners, principally the sheriff and Williams, the convict guard, began about 3: 30 that Saturday afternoon. From that hour on, with only short intervals for food and rest for the questioners — “They all stayed up all night.” “They bring one of them at a time backwards and forwards . . . until they confessed.” And Williams was present and participating that night, during the whole' of which the jail cook served coffee and sandwiches to the men who “grilled” the prisoners.
 </p>
<p id="b301-7">
  Sometime in the early hours of Sunday, the 21st, probably about 2:30 A. M., Woodward apparently “broke” — '
  <span citation-index="1" class="star-pagination" label="232"> 
   *232
   </span>
  as one of the state’s witnesses put it — after a fifteen or twenty minute period of questioning by Williams, the sheriff and the constable “one right after the other.” The State’s Attorney was awakened at his home, and called to the jail. He came, but was dissatisfied with the confession of-Woodward which he took down in writing at that time, and said something like “tear this paper up, that isn’t what I want, when you get something worth while call me.”
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  This same State’s Attorney conducted the state’s case in the circuit court below and also made himself a witness, but did not testify as to. why Woodward’s
  <span citation-index="1" class="star-pagination" label="233"> 
   *233
   </span>
  first alleged confession was unsatisfactory to him. The sheriff did, however:
 </p>
<blockquote id="b303-4">
  “A. No, it wasn’t false, part of it was true and part of it wasn’t; Mr. Maire [the State’s Attorney] said there wasn’t enough. It wasn’t clear enough.
 </blockquote>
<blockquote id="b303-7">
<em>
   " ...
  </em>
</blockquote>
<blockquote id="b303-8">
  “Q. . . . Was that voluntarily made at that time?
 </blockquote>
<blockquote id="ABK">
  “A. Yes, sir.
 </blockquote>
<blockquote id="b303-9">
  “Q. It was voluntarily made that time'?
 </blockquote>
<blockquote id="b303-10">
  “A. Yes, sir..
 </blockquote>
<blockquote id="b304-3">
<span citation-index="1" class="star-pagination" label="234"> 
   *234
   </span>
  “Q. You didn’t consider it sufficient?
 </blockquote>
<blockquote id="A8P">
  “A. Mr. Maire.
 </blockquote>
<blockquote id="b304-5">
  “Q. Mr.' Maire told you that it wasn’t sufficient, so you kept on questioning him until the time you got him to make a free and voluntary confession of other matters that he hadn’t included in the first?
 </blockquote>
<blockquote id="b304-6">
  “A. .No, sir, we questioned him there and we caught him in lies..
 </blockquote>
<blockquote id="b304-7">
  “Q. Caught all of them telling lies?
 </blockquote>
<blockquote id="b304-8">
  “A. Caught every one of them lying to us that night, yes, sir.
 </blockquote>
<blockquote id="b304-9">
  “Q. Did you tell them they were lying?
 </blockquote>
<blockquote id="b304-10">
  “A. Yes, sir.
 </blockquote>
<blockquote id="b304-11">
  “Q. Just how would you tell them that?
 </blockquote>
<blockquote id="b304-12">
  “A. Just like I am talking to you.
 </blockquote>
<blockquote id="b305-5">
<span citation-index="1" class="star-pagination" label="235"> 
   *235
   </span>
  “Q. You said ‘Jack, you told me a lie’?
 </blockquote>
<blockquote id="b305-6">
  “A. Yes, sir.”
 </blockquote>
<p id="b305-7">
  After one week’s constant denial of all guilt, petitioner “broke.”
 </p>
<p id="b305-8">
  Just before sunrise, the state officials got something “worthwhile” from petitioners which the State’s Attorney would “want”; again he was called; he came;- in the presence of'those who had carried on and witnessed the all-night questioning, he caused his questions and petitioners’ answers to be stenographically reported. These are the confessions utilized by the State to obtain the judgments upon which petitioners were sentenced' to death. No formal charges had been brought before the confessions. Two days thereafter, petitioners-were indicted, were arraigned and Williamson and Woodward pleaded guilty; Chambers and Davis pleaded not guilty. Later the sheriff, accompanied by Williams, informed an-attorney who presumably had been appointed to defend Davis that Davis wanted his plea of not guilty withdrawn. This was done, and Davis then pleaded guilty. When Chambers was tried, his conviction rested upon his confession and testimony of the other three confessors. The convict guard and the sheriff “were in the Court room sitting down in a seat.” And from arrest until sentenced to death, petitioners were never — either in jail or in court— wholly removed from the constant observation, influence, custody and control of those whose persistent pressure brought about the' sunrise confessions.
 </p>
<p id="b305-9">
<em>
   Third.
  </em>
  The scope and operation of the Fourteenth Amendment have been fruitful sources of controversy in our constitutional history.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  However, in view of its his-
  <span citation-index="1" class="star-pagination" label="236"> 
   *236
   </span>
  torieal setting and the wrongs which called it into being, the due process provision of the Fourteenth Amendment — just as that in the Fifth — has led few to doubt that it was intended to guarantee procedural standards adequate and appropriate, then and thereafter,
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  to protect, at all times, people charged with or suspected of crime by those holding positions of power and authority. Tyrannical governments had immemorially utilized dictatorial criminal procedure and punishment to make scapegoats of the weak, or of helpless political, religious, or racial minorities and those who differed, who would not conform and who resisted tyranny. ■ The instruments of such governments were, in the main, two. Conduct, innocent when engaged in, was subsequently made by fiat criminally punishable without legislation. And a liberty loving people won the principle that criminal punishments could not be inflicted save for that which proper legislative action had already by “the law of the land” forbidden when done. But even more was needed. From the popular hatred and abhorrence of illegal confinement, torture and extortion of confessions of violations of the “law of the land” evolved the fundamental idea that no man’s life, liberty or property be forfeited as criminal punishment for violation of that law until there had been a charge fairly made and fairly tried in a pub-
  <span citation-index="1" class="star-pagination" label="237"> 
   *237
   </span>
  lie tribunal free of prejudice, passion, excitement, and tyrannical power. Thus, as assurance against ancient evils, our country, in order to preserve “the blessings of liberty,” wrote into its basic law the requirement, among others, that the forfeiture of the lives, liberties or property of people accused of crime can only follow if procedural safeguards of due process have been obeyed.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
</p>
<p id="b307-6">
  The determination to preserve an accused’s right to procedural due process sprang in large part from knowledge of the historical truth that the rights and liberties of people accused of crime could not be safely entrusted to secret inquisitorial processes. The testimony of centuries, in governments of varying kinds over populations of different races and beliefs, stood as proof that physical and mental torture and coercion had brought about the tragically unjust sacrifices of some who were the noblest and most useful of their generations. The rack, the thumbscrew, the wheel, solitary confinement, protracted questioning and cross questioning, and other ingenious forms.of entrapment of the helpless or unpopular had .left their wake of mutilated bodies and shattered minds along the way to the cross, the guillotine, the stake and
  <span citation-index="1" class="star-pagination" label="238"> 
   *238
   </span>
  the hangman's noose. And they who have suffered most from -secret and dictatorial proceedings have almost always been the poor, the ignorant, the numerically weak, the friendless, and the powerless.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b308-4">
  This requirement — of conforming to fundamental standards of procedure in criminal trials — was made operative against the States by the Fourteenth Amendment. Where one of several accused had limped into the trial court as a result of admitted physical mistreatment inflicted to obtain confessions upon which a jury had returned a verdict of guilty of murder, this Court recently declared,
  <em>
   Brown
  </em>
  v. Mississippi, that “It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process.”
  <a class="footnote" href="#fn12" id="fn12_ref">
<em>
    12
   </em>
</a>
</p>
<p id="b308-5">
  Here, the record develops a sharp conflict upon the issue of physical, violence and mistreatment, but shows, without conflict, the dragnet methods of arrest on suspicion without warrant, and the protracted questioning and cross questioning of these ignorant young colored tenant farmers by state officers and other white citizens, in a fourth floor jail room, where as prisoners they were without friends, advisers or counselors, and under circumstances calculated to break the strongest nerves and
  <span citation-index="1" class="star-pagination" label="239"> 
   *239
   </span>
  the stoutest resistance. Just as our decision in
  <em>
   Brown
  </em>
  v.
  <em>
   Mississippi
  </em>
  was based upon the fact that the confessions were the result of compulsion, so in the present case, the admitted practices were such as to justify the statement that “The undisputed facts showed that compulsion was applied.”'
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
</p>
<p id="b309-4">
  For five days petitioners were subjected to interrogations culminating in Saturday’s (May 20th) all night examination. Over a period of five days they steadily refused to confess and disclaimed any guilt. The very circumstances surrounding their confinement and their questioning' without any formal charges having been brought, were such as to fill petitioners with terror and frightful misgivings.
  <a class="footnote" href="#fn14" id="fn14_ref">
   14
  </a>
  Some were practical strangers in
  <span citation-index="1" class="star-pagination" label="240"> 
   *240
   </span>
  the community; three were arrested in a one-room farm tenant house which was their home; the haunting fear of mob violence was around them in an atmosphere charged with excitement and public indignation. From virtually the moment of their arrest until their eventual confessions, they never knew just when any one would be called back to the fourth floor room, and there, surrounded by his accusers and others, interrogated by men who held their very lives — so far as these ignorant petitioners could know — in the balance. The rejection of petitioner Woodward’s first “confession,” given in the early hours of Sunday morning, because it was found wanting, demonstrates the relentless tenacity which “broke” petitioners’ will and rendered them helpless to resist their accusers further. To permit human lives to be forfeited upon confessions thus obtained would make of the constitutional requirement of due process of law a meaningless symbol.
 </p>
<p id="b310-5">
  We are not impressed by the argument that law enforcement methods such as those under review are necessary to uphold our laws.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
  The Constitution proscribes
  <span citation-index="1" class="star-pagination" label="241"> 
   *241
   </span>
  such lawless means irrespective of the end. And this argument flouts the basic principle that all people must stand on an equalit-y before the bar of justice in every American court. Today, as in ages past, we are not without tragic proof that the exalted power of some governments to punish manufactured crime dictatorially is the handmaid of tyranny. Under our constitutional system, courts stand against any winds that blow as havens of refuge for those who might otherwise suffer because they are helpless, weak, outnumbered, or because they are non-conforming victims of prejudice and public excitement. Due process of law, preserved for all by our Constitution, commands that no such practice as that disclosed by this record shall send any accused to his death. No higher duty, no more solemn responsibility, rests upon this Court, than that of translating into living law and maintaining this constitutional shield deliberately planned and inscribed for the benefit of every human being subject to our Constitution — of whatever race, creed or persuasion.
 </p>
<p id="b312-3">
<span citation-index="1" class="star-pagination" label="242"> 
   *242
   </span>
  The Supreme Court of .Florida was in' error and' its judgment is
 </p>
<p id="b312-4">
<em>
   Reversed.
  </em>
</p>
<judges id="b312-5">
  Mr. Justice Murphy took no part in the consideration or decision of- this case.
 </judges>















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b297-15">
   <span class="citation multiple-matches"><a href="/c/U.%20S./308/541/">308 U. S. 541</a></span>.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b297-16">
   Petitioners Williamson, Woodward and Davis pleaded guilty of murder and petitioner Chambers was found guilty by a jury; all
   <span citation-index="1" class="star-pagination" label="228"> 
    *228
    </span>
   were sentenced to death, and the Supreme Court of Florida affirmed. <span class="citation" data-id="3393132"><a href="/opinion/3399600/chambers-v-state/" aria-description="Citation for case: Chambers v. State">111 Fla. 707</a></span>, <span class="citation" data-id="3393132"><a href="/opinion/3399600/chambers-v-state/" aria-description="Citation for case: Chambers v. State">151 So. 499</a></span>; <span class="citation" data-id="3383257"><a href="/opinion/3390999/chambers-v-state/" aria-description="Citation for case: Chambers v. State">152 So. 437</a></span>. Upon the allegation that, unknown to the trial judge, the confessions on which the judgments and sentences of death were based were not voluntary and had been obtained by coercion and. duress, the State Supreme Court granted leave to present a petition for writ of error eoram nobis to the Broward County Circuit Court, <span class="citation" data-id="3393132"><a href="/opinion/3399600/chambers-v-state/" aria-description="Citation for case: Chambers v. State">111 Fla. 707</a></span>; <span class="citation" data-id="3383257"><a href="/opinion/3390999/chambers-v-state/" aria-description="Citation for case: Chambers v. State">152 So. 437</a></span>. The Circuit Court denied the petition without trial of the issues raised by it and the State Supreme Court reversed and ordered the issues submitted to a jury. <span class="citation" data-id="3382712"><a href="/opinion/3390517/chambers-v-state/" aria-description="Citation for case: Chambers v. State">117 Fla. 642</a></span>; <span class="citation" data-id="3382712"><a href="/opinion/3390517/chambers-v-state/" aria-description="Citation for case: Chambers v. State">158 So. 153</a></span>. Upon a verdict adverse to petitioners, the Circuit Court re-affirmed the original judgments and sentences. Again, the State Supreme Court reversed, holding that the issue of force, fear of personal violence and duress had been properly submitted to the jury, but the issue raised by the assignment of error alleging "that the confessions and pleas “were not in fact freely and voluntarily made” had not been clearly submitted to the jury. <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#737" aria-description="Citation for case: Chambers v. State">123 Fla. 734, 737</a></span>; <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#700" aria-description="Citation for case: Chambers v. State">167 So. 697, 700</a></span>. A change of venue, to Palm Beach County, was granted, a jury again found against petitioners and the Broward Circuit Court once more reaffirmed the júdgments and sentences of death. The. Supreme Court of Florida, one judge dissenting, affirmed, <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/" aria-description="Citation for case: Chambers v. State">136 Fla. 568</a></span>; <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/" aria-description="Citation for case: Chambers v. State">187 So. 156</a></span>. While the petition thus seeks review of the judgments and sentences of death rendered in the Broward Circuit Court and reaffirmed in the Palm Beach Circuit Court, the evidence before us consists solely of the transcript of proceedings (on writ of error cpram nobis) in Palm- Beach County Court wherein the circumstances surrounding the obtaining of petitioners’ alleged confessions were passed on by a jury.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b298-5">
<em>
    Brown
   </em>
   v.
   <em>
    Mississippi,
   </em>
   <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b299-7">
<em>
    Pierre
   </em>
   v.
   <em>
    Louisiana,
   </em>
   <span class="citation" data-id="103162"><a href="/opinion/103162/pierre-v-louisiana/#358" aria-description="Citation for case: Pierre v. Louisiana">306 U. S. 354, 358</a></span>;
   <em>
    Norris
   </em>
   v.
   <em>
    Alabama,
   </em>
   <span class="citation" data-id="102407"><a href="/opinion/102407/norris-v-alabama/#590" aria-description="Citation for case: Norris v. Alabama">294 U. S. 587, 590</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b299-8">
   <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#572" aria-description="Citation for case: Chambers v. State">136 Fla. 568, 572</a></span>; <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#157" aria-description="Citation for case: Chambers v. State">187 So. 156, 157</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b299-9">
<span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#574" aria-description="Citation for case: Chambers v. State"><em>
    Id.,
   </em>
   574</a></span>.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b302-4">
   A constable of the community, testifying about this particular incident, said in part:
  </p>
<blockquote id="b302-5">
   “Q. Were you there when Mr. Maire [State’s Attorney] talked to Walter Woodward the first time he came over there?
  </blockquote>
<blockquote id="b302-6">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b302-7">
   “Q. Take his confession down in writing?
  </blockquote>
<blockquote id="b302-8">
   “A. Yes.
  </blockquote>
<blockquote id="b302-9">
   “Q. If he made a confession why did you all keep on questioning him about it. As a matter of fact, what he said that time wasn’t what you. wanted him to say, was it ?
  </blockquote>
<blockquote id="b302-10">
   “A. It wasn’t what he said the last time.
  </blockquote>
<blockquote id="b302-11">
   “Q. It wasn’t what you wanted him to say, was it?
  </blockquote>
<blockquote id="b302-12">
   “A. We didn’t think it was all correct.
  </blockquote>
<blockquote id="b302-13">
   “ Q. What part of it did you think wasn’t correct. Would you say what he told you there at that time was freely and voluntarily made?
  </blockquote>
<blockquote id="b302-14">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b302-15">
   “Q. What he freely and voluntarily told you in the way of a confession at that time, it wasn’t what you wanted?
  </blockquote>
<blockquote id="b302-16">
   “A. It didn’t make up like it should.
  </blockquote>
<blockquote id="b302-17">
   “Q. What matter didn’t make up ?
  </blockquote>
<blockquote id="b302-18">
   “A. There was some things he told us that couldn’t possible be true.
  </blockquote>
<blockquote id="b302-19">
   “Q. What did'Mr. Maire say about it at that time; did you hear Mr. Maire say at this time 'tear this paper up, that isn’t what I want,
   <span citation-index="1" class="star-pagination" label="233"> 
    *233
    </span>
   when you get something worth while call me,’ or words to that,effect?
  </blockquote>
<blockquote id="ALWq">
   “A. Something similar to that.
  </blockquote>
<blockquote id="b303-12">
   “Q. That did happen that night?
  </blockquote>
<blockquote id="b303-13">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b303-14">
   “Q. That was in the presence of Walter Woodward?
  </blockquote>
<blockquote id="b303-15">
   “A. Yes, sir.”
  </blockquote>
<p id="b303-16">
   And petitioner Woodward testified on this subject as follows:
  </p>
<blockquote id="b303-17">
   “A. ... I was taken out several times on the night of the 20th ... So I still denied it. . . .
  </blockquote>
<blockquote id="b303-18">
   “A. He- said I had told lies and kept him sitting up all the week and he was tired and if I didn't come across I would never see the sun rise.
  </blockquote>
<blockquote id="b303-19">
   “A. . . . then I was taken back to the private cell. . . . and shortly after that they come back, shortly after that, twenty or twenty-five minutes, and bring me out. ... I [told Williams] if he would send for the State Attorney he could take down what I said, I said send for him and I will tell him what I know. So he sent for Mr. Maire some time during Saturday night, must have been around one or two o’clock in the night, it was after midnight, and so he sent for Mr. Maire, I didn’t know Mr. Maire then, but I know him now by his face.
  </blockquote>
<blockquote id="b303-20">
   “A. Well he come in and said 'this boy got something to tell mo’- and Captain Williams says ‘yes, he is ready to tell you.’ ....
  </blockquote>
<blockquote id="b303-21">
   “. . . Mr.'Maire had a pen and a book to take down what I told him, which he said had to be on the typewriter, but I didn’t see any typewriter, I saw him with a pen and book, so whether it was short
   <span citation-index="1" class="star-pagination" label="234"> 
    *234
    </span>
   hand or regular writing I don’t know, but he took it down with pen. After I told him my story he said it was no good, and he tore it up. . . .
  </blockquote>
<blockquote id="b304-14">
   “Q. What was it Mr. Maire said?
  </blockquote>
<blockquote id="b304-15">
   “A. He told them it wasn’t no good, when they got something out of me he would be back. It was late he had to go back and go to bed.
  </blockquote>
<blockquote id="b304-16">
   “A. ... I wasn’t in the cell long before they come back. . . .
  </blockquote>
<blockquote id="b304-17">
   “Q. How long was that from the time you was brought into that room until Mr. Maire left there?
  </blockquote>
<blockquote id="b304-18">
   “A. Something like two or three hours, I guess, because it was around sunrise when I went into the room.
  </blockquote>
<blockquote id="b304-19">
   “Q. Had you slept any that night, Walter?
  </blockquote>
<blockquote id="b304-20">
<em>
    “A.
   </em>
   No, sir. I was wálked all night, not continually, but I didn’t have no time R- sleep except in short spaces of the night.
  </blockquote>
<blockquote id="b304-21">
   "Q. When Mr. Maire got there it was after daylight?
  </blockquote>
<blockquote id="b304-22">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b304-23">
   “Q. Why did you say to them that morning anything after you were brought into the room?
  </blockquote>
<blockquote id="b304-24">
<em>
    “A.
   </em>
   Because I was scared, ...
  </blockquote>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b305-10">
   There have been long-continued and constantly recurring differences of opinion as -to whether general 1-gislative acts regulating the use of property could be invalidated as violating the-due process clause of the Fourteenth Amendment.
   <em>
    Munn
   </em>
   v.
   <em>
    Illinois,
   </em>
   <span class="citation" data-id="9417073"><a href="/opinion/89446/munn-v-illinois/#125" aria-description="Citation for case: Munn v. Illinois">94 U. S. 113, 125</a></span>, dissent 136-154;
   <em>
    Chicago M. &amp; St. P. R. Co.
   </em>
   v. Minnesota,
   <span citation-index="1" class="star-pagination" label="236"> 
    *236
    </span>
   <span class="citation" data-id="9841772"><a href="/opinion/92743/chicago-milwaukee-st-paul-railway-co-v-minnesota/" aria-description="Citation for case: Chicago, Milwaukee &amp; St. Paul Railway Co. v. Minnesota">134 U. S. 418</a></span>, dissent 461-466. And there has been a current of opinion — which this court has declined to adopt in many previous cases — that the Fourteenth Amendment was intended to make secure against state invasion all the rights, privileges and immunities protected from federal violation by the Bill of Rights (Amendments I to VIII). See, e. g.,
   <em>
    Twining
   </em>
   v.
   <em>
    New Jersey,
   </em>
   <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#98" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78, 98-9</a></span>, Mr. Justice Harlan, dissenting, 114;
   <em>
    Maxwell
   </em>
   v.
   <em>
    Dow,
   </em>
   <span class="citation" data-id="9417812"><a href="/opinion/95204/maxwell-v-dow/" aria-description="Citation for case: Maxwell v. Dow">176 U. S. 581</a></span>, dissent 606;
   <em>
    O’Neil
   </em>
   v.
   <em>
    Vermont,
   </em>
   <span class="citation" data-id="9841791"><a href="/opinion/93324/oneil-v-vermont/" aria-description="Citation for case: O&#x27;Neil v. Vermont">144 U. S. 323</a></span>, dissent 361;
   <em>
    Palko
   </em>
   v.
   <em>
    Connecticut,
   </em>
   <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325, 326</a></span>;
   <em>
    Hague
   </em>
   v.
   <em>
    C. I. O.,
   </em>
   <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U. S. 496</a></span>.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b306-7">
   Cf.
   <em>
    Weems
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/#372" aria-description="Citation for case: Weems v. United States">217 U. S. 349, 372, 373</a></span>, and dissent setting out (p. 396) argument of Patrick Henry, 3 Elliot, Debates 447.
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b307-7">
   As adopted, the Constitution provided, “The Privilege of the Writ of Habeas Corpus shall not be suspended, unless when in Cases of Rebellion or Invasion the public Safety may require it.” (Art. I, § 9.) “No Bill of Attainder or ex post facto Law shall be passed”
   <em>
    (Id.),
   </em>
   “No State shall . .. pass any Bill of Attainder, or ex post facto Law. .
   <em>
    .(Id.,
   </em>
   § 10), and “No Person shall be convicted of Treason unless on the Testimony of two Witnesses to the same overt Act, or on Confession in open Court” (Art. III, § 3). The Bill of Rights (Amend. I to VIII). Cf. Magna Carta, 1297 (<span class="citation no-link">25 Edw. 1</span>); The Petition of Right, 1627 (3 Car. 1, c. 1.); The Habeas Corpus Act, 1640 (16 Car. 1, c. 10.), An Act for [the Regulating] the Privie Councell and for taking away the Court commonly called the Star Chamber; Stat. (1661) 13 Car. 2, Stat. 1, C. 1 (Treason); The Bill of Rights (1688) (1 Will. &amp; Mar. sess. 2, c. 2.); all collected in “Halsbury’s Stat. of Eng.” (1929) Vol. 3.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b308-6">
   “In-all third degree cases, it is remarkable to note that the confessions were taken from ‘men of humble station in life and of a comparatively low degree of intelligence, and most of them apparently too poor to employ counsel and too friendless to have any one advise them of their rights.’” Filamor, “Third Degree Confession,” 13 Bombay L. J., 339, 346. “That the third degree is especially used against the poor and uninfluential is asserted by several writers, and confirmed by official informants and judicial decisions.” IV National Commission On Law Observance and Enforcement, Reports, (1931) Ch. 3, p. 159. Cf.
   <em>
    Morrison
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="102188"><a href="/opinion/102188/morrison-v-california/#95" aria-description="Citation for case: Morrison v. California">291 U. S. 82, 95</a></span>.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b308-7">
   <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#286" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 286</a></span>.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b309-5">
   See
   <em>
    Ziang Sung Wan
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#16" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S. 1, 16</a></span>. The dissenting Judge below noted, <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#576" aria-description="Citation for case: Chambers v. State">136 Fla. 568, 576</a></span>; <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#159" aria-description="Citation for case: Chambers v. State">187 So. 156, 159</a></span>, that, in a prior appeal of this same case, the Supreme Court of Florida had said: “Even if the jury totally disbelieved the testimony of the petitioners, the testimony of Sheriff Walter Clark, and one or two of the other witnesses introduced by the State, was sufficient to show that these confessions were only made after such' constantly repeated and persistent questioning and cross-questioning on the part of the officers and one J. T. Williams, a convict guard, at frequent intervals while they were in jail, over a period of about a week, and culminating in an all-night questioning of the petitioners separately in succession, throughout practically all of Saturday night, until confessions had been obtained from all of them, when they were all brought into a room in the jailer’s quarters at 6:30 on Sunday morning and made their confessions before the state attorney, the officers, said J. T. Williams, and several disinterested outsiders, the confessions, in the form of questions and answers, being taken down by the court reporter, and then typewritten.
  </p>
<blockquote id="b309-6">
   “Under the principles laid down in Nickels
   <em>
    v.
   </em>
   State, <span class="citation" data-id="3381494"><a href="/opinion/3389464/nickels-v-state/" aria-description="Citation for case: Nickels v. State">90 Fla. 659</a></span>, <span class="citation" data-id="3381494"><a href="/opinion/3389464/nickels-v-state/" aria-description="Citation for case: Nickels v. State">106 So. 479</a></span>; Davis
   <em>
    v.
   </em>
   State, <span class="citation" data-id="4921824"><a href="/opinion/5103863/davis-v-state/" aria-description="Citation for case: Davis v. State">90 Fla. 317</a></span>, <span class="citation" data-id="3390887"><a href="/opinion/3397624/daviss-v-state/" aria-description="Citation for case: Daviss. v. State">105 So. 843</a></span>; Deiterle
   <em>
    v.
   </em>
   State <span class="citation" data-id="3396558"><a href="/opinion/3402562/deiterle-v-state/" aria-description="Citation for case: Deiterle v. State">98 Fla. 739</a></span>, <span class="citation" data-id="3396558"><a href="/opinion/3402562/deiterle-v-state/" aria-description="Citation for case: Deiterle v. State">124 So. 47</a></span>; Mathieu
   <em>
    v.
   </em>
   State, <span class="citation" data-id="3390304"><a href="/opinion/3397120/mathieu-v-state/" aria-description="Citation for case: Mathieu v. State">101 Fla. 94</a></span>, <span class="citation" data-id="3390304"><a href="/opinion/3397120/mathieu-v-state/" aria-description="Citation for case: Mathieu v. State">133 So. 550</a></span>, these confessions were not legally obtained.” <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#741" aria-description="Citation for case: Chambers v. State">123 Fla. 734, 741</a></span>; <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#700" aria-description="Citation for case: Chambers v. State">167 So. 697, 700</a></span>.
  </blockquote>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b309-7">
   Cf. the statement of the Supreme Court of Arkansas,
   <em>
    Bell
   </em>
   v.
   <em>
    State,
   </em>
   <span class="citation" data-id="3267432"><a href="/opinion/3265128/bell-v-state/#89" aria-description="Citation for case: Bell v. State">180 Ark. 79, 89</a></span>; <span class="citation" data-id="3267432"><a href="/opinion/3265128/bell-v-state/" aria-description="Citation for case: Bell v. State">20 S. W. 2d 618</a></span>, 622: “This negro boy was
   <span citation-index="1" class="star-pagination" label="240"> 
    *240
    </span>
   taken, on the day after the discovery of the homicide while he was at his usual work, and placed in jail. He had heard them whipping Swain in the jail; he was taken from the jail to the penitentiary at Little Rock and turned over to the warden, Captain Todhunter, who was requested by the sheriff to question him. This Todhunter proceeded to do, day after day, an hour at a time. There Bell was, an ignorant country boy surrounded by all of those things that strike terror to the negro heart; . . ." See Münsterberg, On the Witness Stand, (1927) 137
   <em>
    et seq.
   </em>
</p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b310-7">
   The police practices here examined are to some degree widespread throughout our country. See Report of Comm. on Lawless Enforcement of the Law (Amer. Bar Ass’n) 1 Amer. Journ. of Pol. Sci., 575; Note 43 H. L. R. 617; IV National Commission On Law Observance And Enforcement,
   <em>
    supra,
   </em>
   Ch. 2, § 4. Yet our national record for crime detection and criminal law enforcement compares poorly with that of Great Britain where secret interrogation of an
   <span citation-index="1" class="star-pagination" label="241"> 
    *241
    </span>
   accused or suspect is not tolerated. See, Report of Comm. on Lawless Enforcement of the Law,
   <em>
    supra,
   </em>
   588; 43 H. L. <span class="citation" data-id="9841772"><a href="/opinion/92743/chicago-milwaukee-st-paul-railway-co-v-minnesota/#618" aria-description="Citation for case: Chicago, Milwaukee &amp; St. Paul Railway Co. v. Minnesota">R.,
   <em>
    supra,
   </em>
   618</a></span>. It has even been suggested that the use of the “third degree” has lowered the esteem in which administration of justice is held by the public and has engendered an attitude of hostility to and unwillingness to cooperate with the police on the part of many people. See, IV National Commission, etc.,
   <em>
    supra,
   </em>
   p. 190. And, after scholarly investigation, the conclusion has been reached “that such methods, aside from their brutality, tend in the long run to defeat their ówn purpose; they encourage inefficiency on the part of the police.” Glueck, Crime and Justice, (1936) 76. See IV National Commission, etc.,
   <em>
    supra,
   </em>
   5; cf. 4 Wigmore, Evidence, (2d ed.) § 2251. The requirement that an accused be brought promptly before a magistrate has been sought by some as a solution to the problem of fostering law enforcement without sacrificing the liberties and procedural rights of the individual. 2 Wig.,
   <em>
    supra,
   </em>
   § 851, IV National Commission, etc.,
   <em>
    supra,
   </em>
   5.
  </p>
</div></div></opinion>
```

---
