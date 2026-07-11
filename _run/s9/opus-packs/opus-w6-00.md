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

## GROUP: _overhaul2/lake/cases/Illinois v. Lafayette.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Illinois v. Lafayette"
type: case
citation: "462 U.S. 640 (1983)"
parallel_cite: "103 S. Ct. 2605; 77 L. Ed. 2d 65"
neutral_cite: 1983 U.S. LEXIS 71
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-06-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Lafayette
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110976/illinois-v-lafayette/"
  cluster_id: 110976
  opinion_id: 9429258
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[South Dakota v. Opperman]]", "[[Colorado v. Bertine]]", "[[Florida v. Wells]]", "[[Chimel v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "inventory-search", "booking", "search-incident-to-arrest"]
holding: "As part of the routine booking/incarceration process (a stationhouse inventory), police may search any container or article in an…"
lake:
  record_id: Illinois v. Lafayette
  status: verified
  projected_at: 2026-07-06
---

# Illinois v. Lafayette

*462 U.S. 640 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Lafayette was arrested for disturbing the peace and taken to the police station. During booking, an officer removed the contents of the shoulder bag Lafayette had been carrying and found amphetamine pills. The Illinois courts suppressed the pills, reasoning the search of the bag was neither a valid [[Search Incident to Arrest|search incident to arrest]] nor a valid inventory.

## Issue
Whether, consistent with the Fourth Amendment, police may search the personal effects of a person under lawful arrest as part of the routine administrative procedure incident to booking and jailing the suspect.

## Rule
Yes. As part of the routine stationhouse booking process, police may search and inventory an arrestee's effects without a warrant or probable cause: "we hold that it is not 'unreasonable' for police, as part of the routine procedure incident to incarcerating an arrested person, to search any container or article in his possession, in accordance with established inventory procedures." — 462 U.S. at 648. ^pin-648

The justification for such a search does not rest on probable cause, so the absence of a warrant is immaterial to its reasonableness.

## Application
Lafayette's shoulder bag was searched at the station as part of the routine procedure for booking and jailing him after a lawful arrest. Because such a stationhouse inventory of an arrestee's possessions is reasonable to protect property, deter false claims, and keep weapons and contraband out of the jail, the officer needed neither a warrant nor probable cause, and the amphetamine pills were lawfully discovered.

## Conclusion
The stationhouse search of the shoulder bag was reasonable; the suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lafayette* applies the inventory-search rationale of [[South Dakota v. Opperman]] to the booking of an arrested person, alongside [[Colorado v. Bertine]] and [[Florida v. Wells]] on inventory searches generally.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Illinois v. Lafayette*, 462 U.S. 640 (1983) — https://www.courtlistener.com/opinion/110976/illinois-v-lafayette/ — pinpoint: 648.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3ea31f14306cc039", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Lafayette"}, "payload": {"all": [{"cite": "462 U.S. 640", "page": "640", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "462"}, {"cite": "103 S. Ct. 2605", "page": "2605", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "77 L. Ed. 2d 65", "page": "65", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "77"}, {"cite": "1983 U.S. LEXIS 71", "page": "71", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}], "display": "462 U.S. 640", "official": {"cite": "462 U.S. 640", "page": "640", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "462"}, "official_selection_present": true, "record_id": "Illinois v. Lafayette"}}
{"assertion_id": "ec1a8c57846e3c8d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-648", "record_id": "Illinois v. Lafayette"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-648", "pinpoint_status": "slip-only", "quote": "--- # Illinois v. Lafayette *462 U.S. 640 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Lafayette was arrested for disturbing the peace and taken to the police station. During booking, an officer removed the contents of the shoulder bag Lafayette had been carrying and found amphetamine pills. The Illinois courts suppressed the pills, reasoning the search of the bag was neither a valid search incident to arrest nor a valid inventory. ## Issue Whether, consistent with the Fourth Amendment, police may search the personal effects of a person under lawful arrest as part of the routine administrative procedure incident to booking and jailing the suspect. ## Rule Yes. As part of the routine stationhouse booking process, police may search and inventory an arrestee's effects without a warrant or probable cause:", "quote_fidelity": "mismatch", "record_id": "Illinois v. Lafayette", "star_marker": null}}
{"assertion_id": "a9217bdce19066fe", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Lafayette"}, "payload": {"as_of_content": "1983-06-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Lafayette", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. Lafayette

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Lafayette",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Lafayette",
    "case_name_short": "Lafayette",
    "case_name_full": "Illinois v. Lafayette",
    "input_case_name": "Illinois v. Lafayette",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-06-20",
    "year": 1983,
    "docket": null,
    "cluster_id": 110976,
    "lead_opinion_id": 9429258,
    "sibling_ids": [
      110976,
      9429258,
      9429259
    ],
    "absolute_url": "/opinion/110976/illinois-v-lafayette/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "462 U.S. 640",
      "volume": "462",
      "reporter": "U.S.",
      "page": "640",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2605",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2605",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 65",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "65",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 71",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "462 U.S. 640",
        "volume": "462",
        "reporter": "U.S.",
        "page": "640",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2605",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2605",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 65",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "65",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 71",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "462 U.S. 640",
    "official_selection": {
      "court_class": "scotus",
      "selected": "462 U.S. 640",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-648",
      "page": null,
      "quote": "--- # Illinois v. Lafayette *462 U.S. 640 (1983)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Lafayette was arrested for disturbing the peace and taken to the police station. During booking, an officer removed the contents of the shoulder bag Lafayette had been carrying and found amphetamine pills. The Illinois courts suppressed the pills, reasoning the search of the bag was neither a valid search incident to arrest nor a valid inventory. ## Issue Whether, consistent with the Fourth Amendment, police may search the personal effects of a person under lawful arrest as part of the routine administrative procedure incident to booking and jailing the suspect. ## Rule Yes. As part of the routine stationhouse booking process, police may search and inventory an arrestee's effects without a warrant or probable cause:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Lafayette",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Najar",
          "cluster_id": 167674,
          "cite": [
            "451 F.3d 710",
            "2006 U.S. App. LEXIS 15171",
            "2006 WL 1689231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Richards v. State",
          "cluster_id": 1464262,
          "cite": [
            "150 S.W.3d 762",
            "2004 WL 2162246"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Gipson",
          "cluster_id": 3135047,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane1_negative"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Wells",
          "cluster_id": 112412,
          "cite": [
            "109 L. Ed. 2d 1",
            "110 S. Ct. 1632",
            "495 U.S. 1",
            "1990 U.S. LEXIS 2035",
            "58 U.S.L.W. 4454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Henrich",
          "cluster_id": 7030666,
          "cite": [
            "39 F.3d 912",
            "1994 WL 596643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Medina v. Cram",
          "cluster_id": 161192,
          "cite": [
            "252 F.3d 1124",
            "2001 Colo. J. C.A.R. 2910",
            "2001 U.S. App. LEXIS 12398",
            "2001 WL 650578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kennedy",
          "cluster_id": 1142841,
          "cite": [
            "666 P.2d 1316",
            "295 Or. 260",
            "1983 Ore. LEXIS 1311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Miranda",
          "cluster_id": 1394991,
          "cite": [
            "744 P.2d 1127",
            "44 Cal. 3d 57",
            "241 Cal. Rptr. 594",
            "1987 Cal. LEXIS 456"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. State",
          "cluster_id": 1960022,
          "cite": [
            "105 S.W.3d 609",
            "2003 Tex. Crim. App. LEXIS 75",
            "2003 WL 1918091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Garcia",
          "cluster_id": 4597966,
          "cite": [
            "302 Neb. 406",
            "923 N.W.2d 725"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 2607511,
          "cite": [
            "833 P.2d 561",
            "3 Cal. 4th 41",
            "10 Cal. Rptr. 2d 554",
            "92 Cal. Daily Op. Serv. 6658",
            "92 Daily Journal DAR 10654",
            "1992 Cal. LEXIS 3491"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Crutcher",
          "cluster_id": 2454155,
          "cite": [
            "989 S.W.2d 295",
            "1999 Tenn. LEXIS 228"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mathieu v. Imperial Toy Corp.",
          "cluster_id": 1783819,
          "cite": [
            "646 So. 2d 318",
            "1994 La. LEXIS 2897",
            "1994 WL 673953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl D. Lyons v. City of Xenia, Christine Keith, Officer Matthew Foubert, Officer",
          "cluster_id": 791266,
          "cite": [
            "417 F.3d 565",
            "2005 U.S. App. LEXIS 16034",
            "2005 WL 1846994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hovey",
          "cluster_id": 1309215,
          "cite": [
            "749 P.2d 776",
            "44 Cal. 3d 543",
            "244 Cal. Rptr. 121",
            "1988 Cal. LEXIS 35"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Henrich",
          "cluster_id": 681668,
          "cite": [
            "39 F.3d 912",
            "94 Cal. Daily Op. Serv. 8379",
            "94 Daily Journal DAR 15497",
            "1994 U.S. App. LEXIS 30487",
            "1994 WL 596643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lafayette:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110976 OR 9429258 OR 9429259) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDQ1Nzg1NjAwMDAwJnM9MjAyOTkwMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110976+OR+9429258+OR+9429259%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(110976 OR 9429258 OR 9429259)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTUmcz02MDA3NDEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110976+OR+9429258+OR+9429259%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110976 OR 9429258 OR 9429259)",
        "reviewed": 24,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 24,
        "triage_read": 0,
        "triage_snippet_classified": 24
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110976 OR 9429258 OR 9429259)",
    "indexed_citing_opinions": 695,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110976,
        "count": 606,
        "count_source": "search"
      },
      {
        "opinion_id": 9429258,
        "count": 106,
        "count_source": "search"
      },
      {
        "opinion_id": 9429259,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1217,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-lafayette.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNDEyMzQmcz05NDExNDg0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110976+OR+9429258+OR+9429259%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110976,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110976,
        "cited_id": 2134938,
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
    "date_created": "2026-07-05T08:03:40Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:03:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:03:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:08:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:03:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Lafayette

```
<opinion type="majority">
<author id="b685-6">Chief Justice Burger</author>
<p id="ADuu">delivered the opinion of the Court.</p>
<p id="b685-7">The question presented is whether, at the time an arrested person arrives at a police station, the police may, without obtaining a warrant, search a shoulder bag carried by that person.</p>
<p id="A017">1</p>
<p id="b685-8">On September 1, 1980, at about 10 p. m., Officer Maurice Mietzner of the Kankakee City Police arrived at the Town Cinema in Kankakee, Ill., in response to a call about a disturbance. There he found respondent involved in an altercation with the theater manager. He arrested respondent for disturbing the peace, handcuffed him, and took him to the police station. Respondent carried a purse-type shoulder bag on the trip to the station.</p>
<p id="b685-9">At the police station respondent was taken to the booking room; there, Officer Mietzner removed the handcuffs from respondent and ordered him to empty his pockets and place <page-number citation-index="1" label="642">*642</page-number>the contents on the counter. After doing so, respondent took a package of cigarettes from his shoulder bag and placed the bag on the counter. Mietzner then removed the contents of the bag, and found 10 amphetamine pills inside the plastic wrap of a cigarette package.</p>
<p id="b686-5">Respondent was subsequently charged with violating § 402(b) of the Illinois Controlled Substances Act, Ill. Rev. Stat., ch. 56/2, ¶ 1402(b) (1981), on the basis of the controlled substances found in his shoulder bag. A pretrial suppression hearing was held at which the State argued that the search of the shoulder bag was a valid inventory search under <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976). Officer Mietz-ner testified that he examined the bag’s contents because it was standard procedure to inventory “everything” in the possession of an arrested person. App. 15, 16. He testified that he was not seeking and did not expect to find drugs or weapons when he searched the bag, and he conceded that the shoulder bag was small enough that it could have been placed and sealed in a bag, container, or locker for protective purposes. <em>Id., </em>at 15. After the hearing, but before any ruling, the State submitted a brief in which it argued for the first time that the search was valid as a delayed search incident to arrest. Thereafter, the trial court ordered the suppression of the amphetamine pills. Id., at 22.</p>
<p id="b686-6">On appeal, the Illinois Appellate Court affirmed. <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/" aria-description="Citation for case: People v. Lafayette">99 Ill. App. 3d 830</a></span>, <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/" aria-description="Citation for case: People v. Lafayette">425 N. E. 2d 1383</a></span> (3d Dist. 1981). It first held that the State had waived the argument that the search was incident to a valid arrest by failing to raise that argument at the suppression hearing. <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#832" aria-description="Citation for case: People v. Lafayette"><em>Id., </em>at 832</a></span>, <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#1385" aria-description="Citation for case: People v. Lafayette">425 N. E. 2d, at 1385</a></span>. However, the court went on to discuss and reject the State’s argument: “[E]ven assuming, <em>arguendo, </em>that the State has not waived this argument, the stationhouse search of the shoulder bag did not constitute a valid search incident to a lawful arrest.” <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#833" aria-description="Citation for case: People v. Lafayette"><em>Id., </em>at 833</a></span>, <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#1385" aria-description="Citation for case: People v. Lafayette">425 N. E. 2d, at 1385</a></span>.</p>
<p id="b686-7">The state court also held that the search was not a valid inventory of respondent’s belongings. It purported to dis<page-number citation-index="1" label="643">*643</page-number>tinguish <em>South Dakota </em>v. <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman, supra,</a></span> </em>on the basis that there is a greater privacy interest in a purse-type shoulder bag than in an automobile, and that the State’s legitimate interests could have been met in a less intrusive manner, by “sealing [the shoulder bag] within a plastic bag or box and placing it in a secured locker.” <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#834" aria-description="Citation for case: People v. Lafayette">99 Ill. App. 3d, at 834-835</a></span>, <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#1386" aria-description="Citation for case: People v. Lafayette">425 N. E. 2d, at 1386</a></span>. The Illinois court concluded:</p>
<blockquote id="AhPC">“Therefore, the postponed warrantless search of the [respondent’s] shoulder bag was neither incident to his lawful arrest nor a valid inventory of his belongings, and thus, violated the fourth amendment.” <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#835" aria-description="Citation for case: People v. Lafayette"><em>Id., </em>at 835</a></span>, <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#1386" aria-description="Citation for case: People v. Lafayette">425 N. E. 2d, at 1386</a></span>.</blockquote>
<p id="A40">The Illinois Supreme Court denied discretionary review. App. to Pet. for Cert. lb. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./459/986/">459 U. S. 986</a></span> (1982), because of the frequency with which this question confronts police and courts, and we reverse.</p>
<p id="A6C">I — Í h-1</p>
<p id="Ac0">The question here is whether, consistent with the Fourth Amendment, it is reasonable for police to search the personal effects of a person under lawful arrest as part of the routine administrative procedure at a police station house incident to booking and jailing the suspect. The justification for such searches does not rest on probable cause, and hence the absence of a warrant is immaterial to the reasonableness of the search. Indeed, we have previously established that the inventory search constitutes a well-defined exception to the warrant requirement. See <em>South Dakota </em>v. <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman, supra.</a></span> </em>The Illinois court and respondent rely on <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), and <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979); in the former, we noted that “probable cause to search is irrelevant” in inventory searches and went on to state:</p>
<blockquote id="ANQ9">“This is so because the salutary functions of a warrant simply have no application in that context; the constitu<page-number citation-index="1" label="644">*644</page-number>tional reasonableness of inventory searches must be determined on other bases.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#10" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 10, n. 5</a></span>.<footnotemark>1</footnotemark></blockquote>
<p id="b688-5">A so-called inventory search is not an independent legal concept but rather an incidental administrative step following arrest and preceding incarceration. To determine whether the search of respondent’s shoulder bag was unreasonable we must “balanc[e] its intrusion on the individual’s Fourth Amendment interests against its promotion of legitimate governmental interests.” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979).</p>
<p id="b688-6">In order to see an inventory search in proper perspective, it is necessary to study the evolution of interests along the continuum from arrest to incarceration. We have held that immediately upon arrest an officer may lawfully search the person of an arrestee, <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); he may also search the area within the arrestee’s immediate control, <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). We explained the basis for this doctrine in <em>United States </em>v. <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra,</a></span> </em>where we said:</p>
<blockquote id="b688-7">“A police officer’s determination as to how and where to search the person of a suspect whom he has arrested is necessarily a quick <em>ad hoc </em>judgment which the Fourth Amendment does not require to be broken down in each instance into an analysis of each step in the search. The authority to search the person incident to a lawful custodial arrest, while based upon the need to disarm and to discover evidence, does not depend on what a court may later decide was the probability in a particular arrest <page-number citation-index="1" label="645">*645</page-number>situation that weapons or evidence would in fact be found upon the person of the suspect. A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification. <em>It is the fact of the lawful arrest which establishes the authority to search, </em>and we hold that in the case of a lawful custodial arrest <em>a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a ‘reasonable’ search under that Amendment.” </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S., at 235</a></span> (emphasis added).</blockquote>
<p id="b689-5">An arrested person is not invariably taken to a police station or confined; if an arrestee is taken to the police station, that is no more than a continuation of the custody inherent in the arrest status. Nonetheless, the factors justifying a search of the person and personal effects of an arrestee upon reaching a police station but prior to being placed in confinement are somewhat different from the factors justifying an immediate search at the time and place of arrest.</p>
<p id="b689-6">The governmental interests underlying a station-house search of the arrestee’s person and possessions may in some circumstances be even greater than those supporting a search immediately following arrest. Consequently, the scope of a station-house search will often vary from that made at the time of arrest. Police conduct that would be impractical or unreasonable — or embarrassingly intrusive — on the street can more readily — and privately — be performed at the station. For example, the interests supporting a search incident to arrest would hardly justify disrobing an arrestee on the street, but the practical necessities of routine jail administration may even justify taking a prisoner’s clothes before confining him, although that step would be rare. This was made clear in <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#804" aria-description="Citation for case: United States v. Edwards">415 U. S. 800, 804</a></span> (1974): “With or without probable cause, the authorities were entitled [at the station house] not only to search [the <page-number citation-index="1" label="646">*646</page-number>arrestee’s] clothing but also to take it from him and keep it in official custody.”<footnotemark>2</footnotemark></p>
<p id="b690-5">At the station house, it is entirely proper for police to remove and list or inventory property found on the person or in the possession of an arrested person who is to be jailed. A range of governmental interests supports an inventory process. It is not unheard of for persons employed in police activities to steal property taken from arrested persons; similarly, arrested persons have been known to make false claims regarding what was taken from their possession at the station house. A standardized procedure for making a list or inventory as soon as reasonable after reaching the station house not only deters false claims but also inhibits theft or careless handling of articles taken from the arrested person. Arrested persons have also been known to injure themselves — or others — with belts, knives, drugs, or other items on their person while being detained. Dangerous instru-mentalities — such as razor blades, bombs, or weapons — can be concealed in innocent-looking articles taken from the arrestee’s possession. The bare recital of these mundane realities justifies reasonable measures by police to limit these risks — either while the items are in police possession or at the time they are returned to the arrestee upon his release. Examining all the items removed from the arrestee’s person or possession and listing or inventorying them is an entirely reasonable administrative procedure. It is immaterial whether the police actually fear any particular package or container; the need to protect against such risks arises independently of a particular officer’s subjective concerns. See <em>United States </em>v. <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><em>Robinson, supra, </em>at 235</a></span>. Finally, inspection of an arrestee’s personal property may assist the police in ascertaining or verifying his identity. See 2 W. LaFave, Search and Seizure §5.3, pp. 306-307 (1978). In short, <page-number citation-index="1" label="647">*647</page-number>every consideration of orderly police administration benefiting both police and the public points toward the appropriateness of the examination of respondent’s shoulder bag prior to his incarceration.</p>
<p id="b691-5">Our prior cases amply support this conclusion. In <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976), we upheld a search of the contents of the glove compartment of an abandoned automobile lawfully impounded by the police. We held that the search was reasonable because it served legitimate governmental interests that outweighed the individual’s privacy interests in the contents of his car. Those measures protected the owner’s property while it was in the custody of the police and protected police against possible false claims of theft. We found no need to consider the existence of less intrusive means of protecting the police and the property in their custody — such as locking the car and impounding it in safe storage under guard. Similarly, standardized inventory procedures are appropriate to serve legitimate governmental interests at stake here.</p>
<p id="b691-6">The Illinois court held that the search of respondent’s shoulder bag was unreasonable because “preservation of the defendant’s property and protection of police from claims of lost or stolen property, ‘could have been achieved in a less intrusive manner.’ For example, . . . the defendant’s shoulder bag could easily have been secured by sealing it within a plastic bag or box and placing it in a secured locker.” <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#835" aria-description="Citation for case: People v. Lafayette">99 Ill. App. 3d, at 835</a></span>, <span class="citation" data-id="2134938"><a href="/opinion/2134938/people-v-lafayette/#1386" aria-description="Citation for case: People v. Lafayette">425 N. E. 2d, at 1386</a></span> (citation omitted). Perhaps so, but the real question is not what “could have been achieved,” but whether the Fourth Amendment <em>requires </em>such steps; it is not our function to write a manual on administering routine, neutral procedures of the station house. Our role is to assure against violations of the Constitution.</p>
<p id="b691-7">The reasonableness of any particular governmental activity does not necessarily or invariably turn on the existence of alternative “less intrusive” means. In <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973), for example, we upheld the search of <page-number citation-index="1" label="648">*648</page-number>the trunk of a car to find a revolver suspected of being there. We rejected the contention that the public could equally well have been protected by the posting of a guard over the automobile. In language equally applicable to this case, we held, “[tjhe fact that the protection of the public might, in the abstract, have been accomplished by ‘less intrusive’ means does not, by itself, render the search unreasonable.” <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski"><em>Id., </em>at 447</a></span>. See also <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 557, n. 12</a></span> (1976). We are hardly in a position to second-guess police departments as to what practical administrative method will best deter theft by and false claims against its employees and preserve the security of the station house. It is evident that a station-house search of every item carried on or by a person who has lawfully been taken into custody by the police will amply serve the important and legitimate governmental interests involved.</p>
<p id="b692-5">Even if less intrusive means existed of protecting some particular types of property, it would be unreasonable to expect police officers in the everyday course of business to make fine and subtle distinctions in deciding which containers or items may be searched and which must be sealed as a unit. Only recently in <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), we stated that “‘[a] single familiar standard is essential to guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.’” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 458</a></span>, quoting <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span> (1979). See also <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 821</a></span> (1982).</p>
<p id="b692-6">Applying these principles, we. hold that it is not “unreasonable” for police, as part of the routine procedure incident to incarcerating an arrested person, to search any container or article in his possession, in accordance with established inventory procedures.<footnotemark>3</footnotemark></p>
<p id="b693-4"><page-number citation-index="1" label="649">*649</page-number>The judgment of the Illinois Appellate Court is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p id="b693-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b688-8"> See also <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">415 U. S. 800</a></span> (1974). In that case we addressed <em>Cooper </em>v. <em>California, 386 </em>U. S. 58 (1967), where the Court sustained a warrantless search of an automobile that occurred a week after its owner had been arrested. We explained <em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span> </em>in the following manner: “It was no answer to say that the police could have obtained a search warrant, for the Court held the test to be, not whether it was reasonable to procure a search warrant, <em>but whether the search itself was reasonable, </em>which it was.” <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#807" aria-description="Citation for case: United States v. Edwards">415 U. S., at 807</a></span> (emphasis added).</p>
</footnote>
<footnote label="2">
<p id="b690-6"> We were not addressing in <em><span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">Edwards</a></span>, </em>and do not discuss here, the circumstances in which a strip search of an arrestee may or may not be appropriate.</p>
</footnote>
<footnote label="3">
<p id="b692-7"> The record is unclear as to whether respondent was to have been incarcerated after being booked for disturbing the peace. That is an appropriate inquiry on remand.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Illinois v. Lidster.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Illinois v. Lidster"
type: case
citation: "540 U.S. 419 (2004)"
parallel_cite: "124 S. Ct. 885; 157 L. Ed. 2d 843"
neutral_cite: 2004 U.S. LEXIS 656
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-01-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-01-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Lidster
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131154/illinois-v-lidster/"
  cluster_id: 131154
  opinion_id: 131154
  identity_checked: true
homes:
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Key — Progeny / Refinement"
related: ["[[City of Indianapolis v. Edmond]]", "[[Michigan Dept. of State Police v. Sitz]]", "[[Brown v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "checkpoint", "special-needs", "information-seeking-stop"]
holding: "An information-seeking checkpoint — stopping motorists to ask whether they witnessed an earlier crime committed by *someone else* — is…"
lake:
  record_id: Illinois v. Lidster
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. Lidster

*540 U.S. 419 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A week after a fatal hit-and-run, police set up a highway checkpoint at the same location and time of night to ask passing motorists for information about the accident, handing out flyers. As Lidster approached the checkpoint his minivan nearly hit an officer; he was found to be intoxicated and convicted of DUI. He argued the checkpoint stop was unconstitutional under *[[City of Indianapolis v. Edmond]]*.

## Issue
Whether a highway checkpoint whose purpose is to ask motorists, as members of the public, for information about a crime committed by someone else is an unreasonable seizure under the Fourth Amendment.

## Rule
No; such information-seeking stops are not [[Common Legal Terms#per-se|per se]] unconstitutional and are judged by a balancing test. "The checkpoint stop here differs significantly from that in Edmond. The stop's primary law enforcement purpose was not to determine whether a vehicle's occupants were committing a crime, but to ask vehicle occupants, as members of the public, for their help in providing information about a crime in all likelihood committed by others." — 540 U.S. at 423. ^pin-423

Reasonableness is judged "on the basis of the individual circumstances." — [*Id.* at 426](https://www.courtlistener.com/opinion/131154/illinois-v-lidster/#:~:text=on%20the%20basis%20of%20the). ^pin-426

Applying the gravity of the public concern, the degree to which the stop advances it, and the severity of the interference with liberty, the Court held: "We hold that the stop was constitutional." — [*Id.* at 427](https://www.courtlistener.com/opinion/131154/illinois-v-lidster/#:~:text=We%20hold%20that%20the%20stop). ^pin-427

## Application
The checkpoint served a grave public concern — investigating a fatal hit-and-run — and was tailored to advance it, set up about a week later at the same place and time to reach motorists who might have witnessed the accident. The stops interfered only minimally with liberty: a brief wait, a few seconds of contact, a request for information and a flyer, applied systematically to all cars. Because the *[[City of Indianapolis v. Edmond|Edmond]]* [[Common Legal Terms#per-se|per se]] rule did not apply and the balance favored the stop, the checkpoint was reasonable.

## Conclusion
The information-seeking checkpoint was constitutional; the judgment suppressing the evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lidster* distinguishes [[City of Indianapolis v. Edmond]] (general crime-control checkpoints barred) and applies the [[Brown v. Texas]] balancing factors used in [[Michigan Dept. of State Police v. Sitz]] to information-seeking stops.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Illinois v. Lidster*, 540 U.S. 419 (2004) — https://www.courtlistener.com/opinion/131154/illinois-v-lidster/ — pinpoints: 423, 426, 427.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6f4990b4b86e380a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Lidster"}, "payload": {"all": [{"cite": "540 U.S. 419", "page": "419", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "540"}, {"cite": "124 S. Ct. 885", "page": "885", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "157 L. Ed. 2d 843", "page": "843", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "157"}, {"cite": "2004 U.S. LEXIS 656", "page": "656", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}], "display": "540 U.S. 419", "official": {"cite": "540 U.S. 419", "page": "419", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "540"}, "official_selection_present": true, "record_id": "Illinois v. Lidster"}}
{"assertion_id": "57e4000156607297", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-423", "record_id": "Illinois v. Lidster"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-423", "pinpoint_status": "slip-only", "quote": "--- # Illinois v. Lidster *540 U.S. 419 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A week after a fatal hit-and-run, police set up a highway checkpoint at the same location and time of night to ask passing motorists for information about the accident, handing out flyers. As Lidster approached the checkpoint his minivan nearly hit an officer; he was found to be intoxicated and convicted of DUI. He argued the checkpoint stop was unconstitutional under *City of Indianapolis v. Edmond*. ## Issue Whether a highway checkpoint whose purpose is to ask motorists, as members of the public, for information about a crime committed by someone else is an unreasonable seizure under the Fourth Amendment. ## Rule No; such information-seeking stops are not per se unconstitutional and are judged by a balancing test.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Lidster", "star_marker": null}}
{"assertion_id": "92cca1e947fbcffa", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-427", "record_id": "Illinois v. Lidster"}, "payload": {"fragment": "#:~:text=We%20hold%20that%20the%20stop", "page": null, "pin_id": "pin-427", "pinpoint_status": "star-verified", "quote": "We hold that the stop was constitutional.", "quote_fidelity": "matched", "record_id": "Illinois v. Lidster", "star_marker": "427"}}
{"assertion_id": "c762054ec4a744ed", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-426", "record_id": "Illinois v. Lidster"}, "payload": {"fragment": "#:~:text=on%20the%20basis%20of%20the", "page": null, "pin_id": "pin-426", "pinpoint_status": "star-verified", "quote": "on the basis of the individual circumstances.", "quote_fidelity": "matched", "record_id": "Illinois v. Lidster", "star_marker": "426"}}
{"assertion_id": "7fc1a0fa643a7ac5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Lidster"}, "payload": {"as_of_content": "2004-01-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Lidster", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. Lidster

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Lidster",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Lidster",
    "case_name_short": "Lidster",
    "case_name_full": "Illinois v. Lidster",
    "input_case_name": "Illinois v. Lidster",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-01-13",
    "year": 2004,
    "docket": null,
    "cluster_id": 131154,
    "lead_opinion_id": 131154,
    "sibling_ids": [
      131154,
      9434532,
      9434533
    ],
    "absolute_url": "/opinion/131154/illinois-v-lidster/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "540 U.S. 419",
      "volume": "540",
      "reporter": "U.S.",
      "page": "419",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 885",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "885",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 843",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 656",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "656",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 419",
        "volume": "540",
        "reporter": "U.S.",
        "page": "419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 885",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "885",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 843",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 656",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "656",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "540 U.S. 419",
    "official_selection": {
      "court_class": "scotus",
      "selected": "540 U.S. 419",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-423",
      "page": null,
      "quote": "--- # Illinois v. Lidster *540 U.S. 419 (2004)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A week after a fatal hit-and-run, police set up a highway checkpoint at the same location and time of night to ask passing motorists for information about the accident, handing out flyers. As Lidster approached the checkpoint his minivan nearly hit an officer; he was found to be intoxicated and convicted of DUI. He argued the checkpoint stop was unconstitutional under *City of Indianapolis v. Edmond*. ## Issue Whether a highway checkpoint whose purpose is to ask motorists, as members of the public, for information about a crime committed by someone else is an unreasonable seizure under the Fourth Amendment. ## Rule No; such information-seeking stops are not per se unconstitutional and are judged by a balancing test.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-426",
      "page": null,
      "quote": "on the basis of the individual circumstances.",
      "star_marker": "426",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15657,
      "fragment": "#:~:text=on%20the%20basis%20of%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-427",
      "page": null,
      "quote": "We hold that the stop was constitutional.",
      "star_marker": "427",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17007,
      "fragment": "#:~:text=We%20hold%20that%20the%20stop",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-01-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Lidster",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Illinois v. Lidster:lane1_negative"
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
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lira",
          "cluster_id": 10134125,
          "cite": [
            "310 Or. App. 237",
            "484 P.3d 1090"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Morris Wise",
          "cluster_id": 4448990,
          "cite": [
            "877 F.3d 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ashworth",
          "cluster_id": 4243394,
          "cite": [
            "790 S.E.2d 173",
            "248 N.C. App. 649",
            "2016 N.C. App. LEXIS 816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 1978636,
          "cite": [
            "2008 VT 53",
            "955 A.2d 1144",
            "184 Vt. 23",
            "2008 Vt. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Burroughs",
          "cluster_id": 1231391,
          "cite": [
            "648 S.E.2d 561",
            "185 N.C. App. 496",
            "2007 N.C. App. LEXIS 1811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Weikert",
          "cluster_id": 202888,
          "cite": [
            "504 F.3d 1",
            "2007 U.S. App. LEXIS 18845",
            "2007 WL 2265660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wesley David Hirmon, Jr. v. State",
          "cluster_id": 2849505,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Derrick L. Foster",
          "cluster_id": 787028,
          "cite": [
            "376 F.3d 577",
            "65 Fed. R. Serv. 1",
            "2004 U.S. App. LEXIS 15267",
            "2004 WL 1606725"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane1_negative"
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
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bucklew v. Precythe",
          "cluster_id": 4605633,
          "cite": [
            "587 U.S. 119",
            "139 S. Ct. 1112",
            "203 L. Ed. 2d 521",
            "2019 U.S. LEXIS 2477"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shukri Baker",
          "cluster_id": 618459,
          "cite": [
            "664 F.3d 467"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
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
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lynch v. City of New York",
          "cluster_id": 1360513,
          "cite": [
            "589 F.3d 94",
            "30 I.E.R. Cas. (BNA) 124",
            "2009 U.S. App. LEXIS 26980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jim Maxwell v. County of San Diego",
          "cluster_id": 820536,
          "cite": [
            "708 F.3d 1075",
            "2013 WL 542756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas George v. William Rehiel",
          "cluster_id": 2647461,
          "cite": [
            "738 F.3d 562",
            "2013 WL 6768151",
            "2013 U.S. App. LEXIS 25604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Erin Lincoln v. City of Colleyville, Texas",
          "cluster_id": 4439435,
          "cite": [
            "874 F.3d 833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Al-Kidd v. Ashcroft",
          "cluster_id": 1204118,
          "cite": [
            "580 F.3d 949",
            "2009 U.S. App. LEXIS 20000",
            "2009 WL 2836448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Electronic Privacy Information Center v. United States Department of Homeland Security",
          "cluster_id": 221052,
          "cite": [
            "653 F.3d 1",
            "397 U.S. App. D.C. 313",
            "2011 U.S. App. LEXIS 14503",
            "2011 WL 2739752"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mitchell",
          "cluster_id": 221722,
          "cite": [
            "652 F.3d 387",
            "2011 U.S. App. LEXIS 15272",
            "2011 WL 3086952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mills v. District of Columbia",
          "cluster_id": 187432,
          "cite": [
            "571 F.3d 1304",
            "387 U.S. App. D.C. 221",
            "2009 U.S. App. LEXIS 15324",
            "2009 WL 1979257"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karen H. Amerson, United States of America v. Julius Graves",
          "cluster_id": 797450,
          "cite": [
            "483 F.3d 73",
            "2007 U.S. App. LEXIS 8610"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Scarborough",
          "cluster_id": 1057956,
          "cite": [
            "201 S.W.3d 607",
            "2006 Tenn. LEXIS 758",
            "2006 WL 2471439"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Underwood v. State",
          "cluster_id": 2448390,
          "cite": [
            "2011 OK CR 12",
            "252 P.3d 221",
            "2011 Okla. Crim. App. LEXIS 11",
            "2011 WL 1129582"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 792582,
          "cite": [
            "430 F.3d 652",
            "2005 U.S. App. LEXIS 25607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brewer",
          "cluster_id": 1372618,
          "cite": [
            "561 F.3d 676",
            "2009 U.S. App. LEXIS 7047",
            "2009 WL 859701"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Watkins",
          "cluster_id": 2572755,
          "cite": [
            "88 P.3d 1174",
            "207 Ariz. 562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David Walker, for Himself and as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker Debbie Walker, for Herself, as Personal Representative of the Estate of David Walker, as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker Patti Walker Stratton Chad Stratton Tyree Lamph, Individually, and for and on Behalf of Dakota (\"Cody\") Lamph Amy Melissa Lamph, Individually, and for and on Behalf of Dakota (\"Cody\") Lamph v. City of Orem, a Utah Municipality Harold Peterson, Officer City of Pleasant Grove, a Utah Municipality John Clayton, Officer B.J. Robinson, Officer Gordon Smith, Officer of the Department of Public Safety, Orem City, Individually, Utah County David Bateman, Sheriff of Utah County, in His Official and Individual Capacity Darin Durfey, Detective Patty Johnston, Detective Tom Hodgson, Detective, and Jerry Monson, Sgt. Meret Lance McDaniel Deputy, All of the Utah County Sheriff's Department, in Their Individual Capacities, David Walker, for Himself and as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker Debbie Walker, for Herself, as Personal Representative of the Estate of David Walker, as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker Patti Walker Stratton Chad Stratton Tyree Lamph, Individually, and for and on Behalf of Dakota (\"Cody\") Lamph Amy Melissa Lamph, Individually, and for and on Behalf of Dakota (\"Cody\") Lamph v. City of Orem, a Utah Municipality City of Pleasant Grove, a Utah Municipality John Clayton, Officer B.J. Robinson, Officer Utah County David Bateman, Sheriff of Utah County, in His Official and Individual Capacity Jerry Monson, Sgt. Darin Durfey, Detective Patty Johnston, Detective Tom Hodgson, Detective Meret Lance McDaniel Deputy, All of the Utah County Sheriff's Department, in Their Individual Capacities Gordon Smith, Officer of the Department of Public Safety, Orem City, Individually, and Harold Peterson, Officer, Debbie Walker, as Personal Representative of the Estate of David Walker, and as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker David B. Walker, for Himself and as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker Tyree Lamph Amy Melissa Lamph Patti Stratton Walker Chad Stratton v. Orem City, a Utah Municipality Harold Peterson, Officer Pleasant Grove City, a Utah Municipality B.J. Robinson, Officer Richard Case Utah County David Bateman Jerry Monson Meret Lance McDaniel Gordon Smith (Fnu) Gilbert, and John Clayton, Officer, Debbie Walker, as Personal Representative of the Estate of David Walker, and as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker David Walker, Sr., for Himself and as Next Best Friend for Cadin Wayne Walker, McKaela Tandi Walker and Andrew Walker Tyree Lamph, and Amy Melissa Lamph, Individually and on Behalf of Dakota (\"Cody\") Lamph Patti Stratton Walker Chad Stratton v. Orem City, a Utah Municipality Harold Peterson, Officer Pleasant Grove City, a Utah Municipality John Clayton, Officer B.J. Robinson, Officer Richard Case David Bateman, Sheriff of Utah County, in His Official and Individual Capacity Darin Durfey Gordon Smith (Fnu) Gilbert, and Utah County Jerry Monson Meret Lance McDaniel",
          "cluster_id": 794712,
          "cite": [
            "451 F.3d 1139",
            "2006 U.S. App. LEXIS 16103"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manzanares v. Higdon",
          "cluster_id": 172499,
          "cite": [
            "575 F.3d 1135",
            "2009 U.S. App. LEXIS 17817",
            "2009 WL 2430643"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Lidster:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131154 OR 9434532 OR 9434533) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 179,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 10,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 179,
        "triage_read": 10,
        "triage_snippet_classified": 169
      },
      "lane2_top_cited": {
        "query": "cites:(131154 OR 9434532 OR 9434533)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MCZzPTEzMDMzMTUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28131154+OR+9434532+OR+9434533%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131154 OR 9434532 OR 9434533)",
        "reviewed": 20,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 20,
        "triage_read": 0,
        "triage_snippet_classified": 20
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(131154 OR 9434532 OR 9434533)",
    "indexed_citing_opinions": 238,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131154,
        "count": 188,
        "count_source": "search"
      },
      {
        "opinion_id": 9434532,
        "count": 53,
        "count_source": "search"
      },
      {
        "opinion_id": 9434533,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 399,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-lidster.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4ODIzMjMmcz03ODU3MTUzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28131154+OR+9434532+OR+9434533%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131154,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 122252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 1059512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 2070661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131154,
        "cited_id": 2119720,
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
    "date_created": "2026-07-05T08:08:48Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:10:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:10:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:14:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:10:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Lidster

```
<div>
<center><b><span class="citation" data-id="9434532"><a href="/opinion/131154/illinois-v-lidster/" aria-description="Citation for case: Illinois v. Lidster">540 U.S. 419</a></span> (2004)</b></center>
<center><h1>ILLINOIS<br>
v.<br>
LIDSTER.</h1></center>
<center>No. 02-1060.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 5, 2003.</center>
<center>Decided January 13, 2004.</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS
<p><span class="star-pagination">*420</span> BREYER, J., delivered the opinion of the Court, in which REHNQUIST, C. J., and O'CONNOR, SCALIA, KENNEDY, and THOMAS, JJ., joined, and in which STEVENS, SOUTER, and GINSBURG, JJ., joined as to Parts I and II. STEVENS, J., filed an opinion concurring in part and dissenting in part, in which SOUTER and GINSBURG, JJ., joined, <i>post,</i> p. 428.</p>
<p><span class="star-pagination">*421</span> <i>Gary Feinerman,</i> Solicitor General of Illinois, argued the cause for petitioner. With him on the briefs were <i>Lisa Madigan,</i> Attorney General, and <i>Linda D. Woloshin, Lisa Anne Hoffman,</i> and <i>Karen Kaplan,</i> Assistant Attorneys General.</p>
<p><i>Patricia A. Millett</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With her on the brief were <i>Solicitor General Olson, Acting Assistant Attorney General Wray, Deputy Solicitor General Dreeben,</i> and <i>Patty Merkamp Stemler.</i></p>
<p><i>Donald John Ramsell</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p>JUSTICE BREYER delivered the opinion of the Court.</p>
<p>This Fourth Amendment case focuses upon a highway checkpoint where police stopped motorists to ask them for information about a recent hit-and-run accident. We hold that the police stops were reasonable, hence, constitutional.</p>
<p></p>
<h2>
<span class="star-pagination">*422</span> I</h2>
<p>The relevant background is as follows: On Saturday, August 23, 1997, just after midnight, an unknown motorist traveling eastbound on a highway in Lombard, Illinois, struck and killed a 70-year-old bicyclist. The motorist drove off without identifying himself. About one week later at about the same time of night and at about the same place, local police set up a highway checkpoint designed to obtain more information about the accident from the motoring public.</p>
<p>Police cars with flashing lights partially blocked the eastbound lanes of the highway. The blockage forced traffic to slow down, leading to lines of up to 15 cars in each lane. As each vehicle drew up to the checkpoint, an officer would stop it for 10 to 15 seconds, ask the occupants whether they had seen anything happen there the previous weekend, and hand each driver a flyer. The flyer said "ALERT . . . FATAL HIT &amp; RUN ACCIDENT" and requested "ASSISTANCE IN IDENTIFYING THE VEHICLE AND DRIVER INVOLVED IN THIS ACCIDENT WHICH KILLED A 70 YEAR OLD BICYCLIST." App. 9.</p>
<p>Robert Lidster, the respondent, drove a minivan toward the checkpoint. As he approached the checkpoint, his van swerved, nearly hitting one of the officers. The officer smelled alcohol on Lidster's breath. He directed Lidster to a side street where another officer administered a sobriety test and then arrested Lidster. Lidster was tried and convicted in Illinois state court of driving under the influence of alcohol.</p>
<p>Lidster challenged the lawfulness of his arrest and conviction on the ground that the government had obtained much of the relevant evidence through use of a checkpoint stop that violated the Fourth Amendment. The trial court rejected that challenge. But an Illinois appellate court reached the opposite conclusion. <span class="citation" data-id="2119720"><a href="/opinion/2119720/people-v-lidster/" aria-description="Citation for case: People v. Lidster">319 Ill. App. 3d 825</a></span>, <span class="citation" data-id="2119720"><a href="/opinion/2119720/people-v-lidster/" aria-description="Citation for case: People v. Lidster">747 N. E. 2d 419</a></span> (2001). The Illinois Supreme Court agreed <span class="star-pagination">*423</span> with the appellate court. It held (by a vote of 4 to 3) that our decision in <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32</a></span> (2000), required it to find the stop unconstitutional. <span class="citation" data-id="9710424"><a href="/opinion/2070661/people-v-lidster/" aria-description="Citation for case: People v. Lidster">202 Ill. 2d 1</a></span>, <span class="citation" data-id="9710424"><a href="/opinion/2070661/people-v-lidster/" aria-description="Citation for case: People v. Lidster">779 N. E. 2d 855</a></span> (2002).</p>
<p>Because lower courts have reached different conclusions about this matter, we granted certiorari. See <i>Burns</i> v. <i>Commonwealth,</i> <span class="citation" data-id="6827527"><a href="/opinion/6931124/burns-v-commonwealth/" aria-description="Citation for case: Burns v. Commonwealth">261 Va. 307</a></span>, <span class="citation" data-id="6827527"><a href="/opinion/6931124/burns-v-commonwealth/" aria-description="Citation for case: Burns v. Commonwealth">541 S. E. 2d 872</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./534/1043/">534 U. S. 1043</a></span> (2001) (finding similar checkpoint stop constitutional). We now reverse the Illinois Supreme Court's determination.</p>
<p></p>
<h2>II</h2>
<p>The Illinois Supreme Court basically held that our decision in <i>Edmond</i> governs the outcome of this case. We do not agree. <i>Edmond</i> involved a checkpoint at which police stopped vehicles to look for evidence of drug crimes committed by occupants of those vehicles. After stopping a vehicle at the checkpoint, police would examine (from outside the vehicle) the vehicle's interior; they would walk a drug-sniffing dog around the exterior; and, if they found sufficient evidence of drug (or other) crimes, they would arrest the vehicle's occupants. <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#35" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 35</a></span>. We found that police had set up this checkpoint primarily for general "crime control" purposes, <i>i.e.,</i> "to detect evidence of ordinary criminal wrongdoing." <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#41" aria-description="Citation for case: City of Indianapolis v. Edmond"><i>Id.,</i> at 41</a></span>. We noted that the stop was made without individualized suspicion. And we held that the Fourth Amendment forbids such a stop, in the absence of special circumstances. <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#44" aria-description="Citation for case: City of Indianapolis v. Edmond"><i>Id.,</i> at 44</a></span>.</p>
<p>The checkpoint stop here differs significantly from that in <i>Edmond.</i> The stop's primary law enforcement purpose was <i>not</i> to determine whether a vehicle's occupants were committing a crime, but to ask vehicle occupants, as members of the public, for their help in providing information about a crime in all likelihood committed by others. The police expected the information elicited to help them apprehend, not the vehicle's occupants, but other individuals.</p>
<p><span class="star-pagination">*424</span> <i>Edmond</i>'s language, as well as its context, makes clear that the constitutionality of this latter, information-seeking kind of stop was not then before the Court. <i>Edmond</i> refers to the subject matter of its holding as "stops justified only by the generalized and ever-present possibility that interrogation and inspection may reveal that <i>any given motorist has committed some crime.</i>" <i>Ibid.</i> (emphasis added). We concede that <i>Edmond</i> describes the law enforcement objective there in question as a "general interest in crime control," but it specifies that the phrase "general interest in crime control" does not refer to every "law enforcement" objective. <i>Id.,</i> at 44, n. 1. We must read this and related general language in <i>Edmond</i> as we often read general language in judicial opinions  as referring in context to circumstances similar to the circumstances then before the Court and not referring to quite different circumstances that the Court was not then considering.</p>
<p>Neither do we believe, <i>Edmond</i> aside, that the Fourth Amendment would have us apply an <i>Edmond</i>-type rule of automatic unconstitutionality to brief, information-seeking highway stops of the kind now before us. For one thing, the fact that such stops normally lack individualized suspicion cannot by itself determine the constitutional outcome. As in <i>Edmond,</i> the stop here at issue involves a motorist. The Fourth Amendment does not treat a motorist's car as his castle. See, <i>e. g., </i><i>New York</i> v. <i>Class,</i> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#112" aria-description="Citation for case: New York v. Class">475 U. S. 106, 112-113</a></span> (1986); <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 561</a></span> (1976). And special law enforcement concerns will sometimes justify highway stops without individualized suspicion. See <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990) (sobriety checkpoint); <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra</a></span></i> (Border Patrol checkpoint). Moreover, unlike <i>Edmond,</i> the context here (seeking information from the public) is one in which, by definition, the concept of individualized suspicion has little role to play. Like certain other forms of police activity, say, <span class="star-pagination">*425</span> crowd control or public safety, an information-seeking stop is not the kind of event that involves suspicion, or lack of suspicion, of the relevant individual.</p>
<p>For another thing, information-seeking highway stops are less likely to provoke anxiety or to prove intrusive. The stops are likely brief. The police are not likely to ask questions designed to elicit self-incriminating information. And citizens will often react positively when police simply ask for their help as "responsible citizen[s]" to "give whatever information they may have to aid in law enforcement." <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 477-478</a></span> (1966).</p>
<p>Further, the law ordinarily permits police to seek the voluntary cooperation of members of the public in the investigation of a crime. "[L]aw enforcement officers do not violate the Fourth Amendment by merely approaching an individual on the street or in another public place, by asking him if he is willing to answer some questions, [or] by putting questions to him if the person is willing to listen." <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 497</a></span> (1983). See also ALI, Model Code of Pre-Arraignment Procedure § 110.1(1) (1975) ("[L]aw enforcement officer may . . . request any person to furnish information or otherwise cooperate in the investigation or prevention of crime"). That, in part, is because voluntary requests play a vital role in police investigatory work. See, <i>e. g., </i><i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span> (1963) ("[I]nterrogation of witnesses . . . is undoubtedly an essential tool in effective law enforcement"); U. S. Dept. of Justice, Eyewitness Evidence: A Guide for Law Enforcement 14-15 (Oct. 1999) (instructing law enforcement to gather information from witnesses near the scene).</p>
<p>The importance of soliciting the public's assistance is offset to some degree by the need to stop a motorist to obtain that help  a need less likely present where a pedestrian, not a motorist, is involved. The difference is significant in light of our determinations that such an involuntary stop amounts <span class="star-pagination">*426</span> to a "seizure" in Fourth Amendment terms. <i>E. g., </i><i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 40</a></span>. That difference, however, is not important enough to justify an <i>Edmond</i>-type rule here. After all, as we have said, the motorist stop will likely be brief. Any accompanying traffic delay should prove no more onerous than many that typically accompany normal traffic congestion. And the resulting voluntary questioning of a motorist is as likely to prove important for police investigation as is the questioning of a pedestrian. Given these considerations, it would seem anomalous were the law (1) ordinarily to allow police freely to seek the voluntary cooperation of pedestrians but (2) ordinarily to forbid police to seek similar voluntary cooperation from motorists.</p>
<p>Finally, we do not believe that an <i>Edmond</i>-type rule is needed to prevent an unreasonable proliferation of police checkpoints. Cf. <span class="citation" data-id="9710424"><a href="/opinion/2070661/people-v-lidster/#9" aria-description="Citation for case: People v. Lidster">202 Ill. 2d, at 9-10</a></span>, <span class="citation" data-id="9710424"><a href="/opinion/2070661/people-v-lidster/#859" aria-description="Citation for case: People v. Lidster">779 N. E. 2d, at 859-860</a></span> (expressing that concern). Practical considerations  namely, limited police resources and community hostility to related traffic tieups  seem likely to inhibit any such proliferation. See Fell, Ferguson, Williams, &amp; Fields, Why Aren't Sobriety Checkpoints Widely Adopted as an Enforcement Strategy in the United States? 35 Accident Analysis &amp; Prevention 897 (Nov. 2003) (finding that sobriety checkpoints are not more widely used due to the lack of police resources and the lack of community support). And, of course, the Fourth Amendment's normal insistence that the stop be reasonable in context will still provide an important legal limitation on police use of this kind of information-seeking checkpoint.</p>
<p>These considerations, taken together, convince us that an <i>Edmond</i>-type presumptive rule of unconstitutionality does not apply here. That does not mean the stop is automatically, or even presumptively, constitutional. It simply means that we must judge its reasonableness, hence, its constitutionality, on the basis of the individual circumstances. And as this Court said in <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span>, 51 <span class="star-pagination">*427</span> (1979), in judging reasonableness, we look to "the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty." See also <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#450" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Sitz, supra,</i> at 450-455</a></span> (balancing these factors in determining reasonableness of a checkpoint stop); <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 556-564</a></span> (same).</p>
<p></p>
<h2>III</h2>
<p>We now consider the reasonableness of the checkpoint stop before us in light of the factors just mentioned, an issue that, in our view, has been fully argued here. See Brief for Petitioner 14-18; Brief for Respondent 17-27. We hold that the stop was constitutional.</p>
<p>The relevant public concern was grave. Police were investigating a crime that had resulted in a human death. No one denies the police's need to obtain more information at that time. And the stop's objective was to help find the perpetrator of a specific and known crime, not of unknown crimes of a general sort. Cf. <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#44" aria-description="Citation for case: City of Indianapolis v. Edmond"><i>Edmond, supra,</i> at 44</a></span>.</p>
<p>The stop advanced this grave public concern to a significant degree. The police appropriately tailored their checkpoint stops to fit important criminal investigatory needs. The stops took place about one week after the hit-and-run accident, on the same highway near the location of the accident, and at about the same time of night. And police used the stops to obtain information from drivers, some of whom might well have been in the vicinity of the crime at the time it occurred. See App. 28-29 (describing police belief that motorists routinely leaving work after night shifts at nearby industrial complexes might have seen something relevant).</p>
<p>Most importantly, the stops interfered only minimally with liberty of the sort the Fourth Amendment seeks to protect. Viewed objectively, each stop required only a brief wait in line  a very few minutes at most. Contact with the police lasted only a few seconds. Cf. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#547" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 547</a></span> (upholding stops of three-to-five minutes); <i>Sitz,</i> 496 <span class="star-pagination">*428</span> U. S., at 448 (upholding delays of 25 seconds). Police contact consisted simply of a request for information and the distribution of a flyer. Cf. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#546" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 546</a></span> (upholding inquiry as to motorists' citizenship and immigration status); <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Sitz, supra,</i> at 447</a></span> (upholding examination of all drivers for signs of intoxication). Viewed subjectively, the contact provided little reason for anxiety or alarm. The police stopped all vehicles systematically. Cf. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 558</a></span>; <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#452" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Sitz, supra,</i> at 452-453</a></span>. And there is no allegation here that the police acted in a discriminatory or otherwise unlawful manner while questioning motorists during stops.</p>
<p>For these reasons we conclude that the checkpoint stop was constitutional.</p>
<p>The judgment of the Illinois Supreme Court is</p>
<p><i>Reversed.</i></p>
<p>JUSTICE STEVENS, with whom JUSTICE SOUTER and JUSTICE GINSBURG join, concurring in part and dissenting in part.</p>
<p>There is a valid and important distinction between seizing a person to determine whether she has committed a crime and seizing a person to ask whether she has any information about an unknown person who committed a crime a week earlier. I therefore join Parts I and II of the Court's opinion explaining why our decision in <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32</a></span> (2000), is not controlling in this case. However, I find the issue discussed in Part III of the opinion closer than the Court does and believe it would be wise to remand the case to the Illinois state courts to address that issue in the first instance.</p>
<p>In contrast to pedestrians, who are free to keep walking when they encounter police officers handing out flyers or seeking information, motorists who confront a roadblock are required to stop, and to remain stopped for as long as the officers choose to detain them. Such a seizure may seem <span class="star-pagination">*429</span> relatively innocuous to some, but annoying to others who are forced to wait for several minutes when the line of cars is lengthened  for example, by a surge of vehicles leaving a factory at the end of a shift. Still other drivers may find an unpublicized roadblock at midnight on a Saturday somewhat alarming.</p>
<p>On the other side of the equation, the likelihood that questioning a random sample of drivers will yield useful information about a hit-and-run accident that occurred a week earlier is speculative at best. To be sure, the sample in this case was not entirely random: The record reveals that the police knew that the victim had finished work at the Post Office shortly before the fatal accident, and hoped that other employees of the Post Office or the nearby industrial park might work on similar schedules and, thus, have been driving the same route at the same time the previous week. That is a plausible theory, but there is no evidence in the record that the police did anything to confirm that the nearby businesses in fact had shift changes at or near midnight on Saturdays, or that they had reason to believe that a roadblock would be more effective than, say, placing flyers on the employees' cars.</p>
<p>In short, the outcome of the multifactor test prescribed in <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979), is by no means clear on the facts of this case. Because the Illinois Appellate Court and the State Supreme Court held that the Lombard roadblock was <i>per se</i> unconstitutional under <i>Indianapolis</i> v. <i>Edmond</i><i>,</i> neither court attempted to apply the <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Brown</a></span></i> test. "We ordinarily do not decide in the first instance issues not resolved below." <i>Pierce County</i> v. <i>Guillen,</i> <span class="citation" data-id="122252"><a href="/opinion/122252/pierce-county-v-guillen/#148" aria-description="Citation for case: Pierce County v. Guillen">537 U. S. 129, 148, n. 10</a></span> (2003). We should be especially reluctant to abandon our role as a court of review in a case in which the constitutional inquiry requires analysis of local conditions and practices more familiar to judges closer to the scene. I would therefore remand the case to the Illinois <span class="star-pagination">*430</span> courts to undertake the initial analysis of the issue that the Court resolves in Part III of its opinion. To that extent, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Ohio et al. by <i>Jim Petro,</i> Attorney General of Ohio, <i>Douglas R. Cole,</i> State Solicitor, and <i>Robert C. Maier,</i> Assistant Solicitor, <i>Robert J. Spagnoletti,</i> Acting Corporation Counsel of the District of Columbia, and by the Attorneys General for their respective jurisdictions as follows: <i>William H. Pryor, Jr.,</i> of Alabama, <i>Terry Goddard</i> of Arizona, <i>M. Jane Brady</i> of Delaware, <i>Steve Carter</i> of Indiana, <i>Thomas J. Miller</i> of Iowa, <i>G. Steven Rowe</i> of Maine, <i>J Joseph Curran, Jr.,</i> of Maryland, <i>Mike Hatch</i> of Minnesota, <i>Mike McGrath</i> of Montana, <i>Brian Sandoval</i> of Nevada, <i>Peter Heed</i> of New Hampshire, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Hardy Myers</i> of Oregon, <i>D. Michael Fisher</i> of Pennsylvania, <i>Henry Dargan McMaster</i> of South Carolina, <i>Lawrence E. Long</i> of South Dakota, <i>Greg Abbott</i> of Texas, <i>Mark L. Shurtleff</i> of Utah, <i>William H. Sorrell</i> of Vermont, <i>Jerry W Kilgore</i> of Virginia, and <i>Iver A. Stridiron</i> of the Virgin Islands; for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the Illinois Association of Chiefs of Police et al. by <i>James G. Sotos.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the National Association of Criminal Defense Lawyers et al. by <i>Lawrence S. Lustberg, Joshua L. Dratel, Steven R. Shapiro,</i> and <i>Harvey Grossman;</i> and for the National College for DUI Defense by <i>Barry T. Simons</i> and <i>W. Troy McKinney.</i></p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Illinois v. McArthur.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Illinois v. McArthur"
type: case
citation: "531 U.S. 326 (2001)"
parallel_cite: "121 S. Ct. 946; 148 L. Ed. 2d 838"
neutral_cite: "2001 U.S. LEXIS 962; 1 Cal. Daily Op. Serv. 1442"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-02-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. McArthur
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118405/illinois-v-mcarthur/"
  cluster_id: 118405
  opinion_id: 118405
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Key — Anchor"
related: ["[[Michigan v. Summers]]", "[[Segura v. United States]]", "[[Bailey v. United States]]", "[[Welsh v. Wisconsin]]"]
aliases: []
tags: ["case", "fourth-amendment", "securing-the-scene", "temporary-seizure", "exigent-circumstances", "warrant"]
holding: "Where police have probable cause to believe a home contains contraband, they may reasonably impose a temporary restraint on a resident —…"
lake:
  record_id: Illinois v. McArthur
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. McArthur

*531 U.S. 326 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While police helped Tera McArthur remove her belongings from the trailer she shared with her husband, she told officers he had marijuana inside. When Charles McArthur refused consent to a search, an officer prevented him from re-entering the trailer unaccompanied while another officer left to obtain a warrant; for about two hours McArthur was allowed inside only with an officer observing. A warrant issued, the search found marijuana and a pipe, and McArthur moved to suppress the temporary restraint as unreasonable.

## Issue
Whether police with probable cause may temporarily prevent a resident from entering his home unaccompanied, to avoid the destruction of evidence, while they diligently obtain a search warrant.

## Rule
Yes, on these combined circumstances. "We conclude that the restriction at issue was reasonable, and hence lawful, in light of the following circumstances, which we consider in combination." — 531 U.S. at 331. ^pin-331

The Court considered: probable cause to believe the home held contraband; good reason to fear the evidence would be destroyed; police efforts to reconcile law-enforcement needs with privacy by imposing only a restraint rather than searching; and a limited duration.

"We have found no case in which this Court has held unlawful a temporary seizure that was supported by probable cause and was designed to prevent the loss of evidence while the police diligently obtained a warrant in a reasonable period of time." — [*Id.* at 334](https://www.courtlistener.com/opinion/118405/illinois-v-mcarthur/#:~:text=We%20have%20found%20no%20case). ^pin-334

## Application
The officers had probable cause from Tera McArthur's reliable, firsthand report; good reason to fear McArthur would destroy the marijuana if left alone inside; and they imposed only a limited restraint — keeping him from entering unaccompanied — rather than searching without a warrant. The restraint lasted only about two hours while an officer diligently obtained the warrant. Considered together, these circumstances made the temporary restriction reasonable.

## Conclusion
The temporary restraint pending the warrant was reasonable; the evidence was admissible and the suppression reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *McArthur* extends the scene-securing logic of [[Michigan v. Summers]] and [[Segura v. United States]] to a brief, probable-cause-based restraint on a resident pending a warrant; it is distinguished from [[Welsh v. Wisconsin]] (warrantless home entry for a nonjailable offense).

## Appears on
- [[Securing the Scene]] — *Key — Anchor*

## Sources
- *Illinois v. McArthur*, 531 U.S. 326 (2001) — https://www.courtlistener.com/opinion/118405/illinois-v-mcarthur/ — pinpoints: 331, 334.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "95ffc38a427b9d5b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. McArthur"}, "payload": {"all": [{"cite": "531 U.S. 326", "page": "326", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "531"}, {"cite": "121 S. Ct. 946", "page": "946", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "148 L. Ed. 2d 838", "page": "838", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "148"}, {"cite": "2001 U.S. LEXIS 962", "page": "962", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}, {"cite": "1 Cal. Daily Op. Serv. 1442", "page": "1442", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1"}], "display": "531 U.S. 326", "official": {"cite": "531 U.S. 326", "page": "326", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "531"}, "official_selection_present": true, "record_id": "Illinois v. McArthur"}}
{"assertion_id": "76f950ed4026aa64", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-331", "record_id": "Illinois v. McArthur"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-331", "pinpoint_status": "slip-only", "quote": "--- # Illinois v. McArthur *531 U.S. 326 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While police helped Tera McArthur remove her belongings from the trailer she shared with her husband, she told officers he had marijuana inside. When Charles McArthur refused consent to a search, an officer prevented him from re-entering the trailer unaccompanied while another officer left to obtain a warrant; for about two hours McArthur was allowed inside only with an officer observing. A warrant issued, the search found marijuana and a pipe, and McArthur moved to suppress the temporary restraint as unreasonable. ## Issue Whether police with probable cause may temporarily prevent a resident from entering his home unaccompanied, to avoid the destruction of evidence, while they diligently obtain a search warrant. ## Rule Yes, on these combined circumstances.", "quote_fidelity": "mismatch", "record_id": "Illinois v. McArthur", "star_marker": null}}
{"assertion_id": "be9a92a927fb9a9b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-334", "record_id": "Illinois v. McArthur"}, "payload": {"fragment": "#:~:text=We%20have%20found%20no%20case", "page": null, "pin_id": "pin-334", "pinpoint_status": "star-verified", "quote": "We have found no case in which this Court has held unlawful a temporary seizure that was supported by probable cause and was designed to prevent the loss of evidence while the police diligently obtained a warrant in a reasonable period of time.", "quote_fidelity": "matched", "record_id": "Illinois v. McArthur", "star_marker": "334"}}
{"assertion_id": "d40ee315839f0c26", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. McArthur"}, "payload": {"as_of_content": "2001-02-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. McArthur", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. McArthur

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. McArthur",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. McArthur",
    "case_name_short": "McArthur",
    "case_name_full": "ILLINOIS v. McARTHUR",
    "input_case_name": "Illinois v. McArthur",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-02-20",
    "year": 2001,
    "docket": null,
    "cluster_id": 118405,
    "lead_opinion_id": 118405,
    "sibling_ids": [
      118405,
      9434039,
      9434040,
      9434041
    ],
    "absolute_url": "/opinion/118405/illinois-v-mcarthur/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "531 U.S. 326",
      "volume": "531",
      "reporter": "U.S.",
      "page": "326",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 946",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "946",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 838",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "838",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 962",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "962",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cal. Daily Op. Serv. 1442",
        "volume": "1",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1442",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "531 U.S. 326",
        "volume": "531",
        "reporter": "U.S.",
        "page": "326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 946",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "946",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 838",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "838",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 962",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "962",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cal. Daily Op. Serv. 1442",
        "volume": "1",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1442",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "531 U.S. 326",
    "official_selection": {
      "court_class": "scotus",
      "selected": "531 U.S. 326",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-331",
      "page": null,
      "quote": "--- # Illinois v. McArthur *531 U.S. 326 (2001)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While police helped Tera McArthur remove her belongings from the trailer she shared with her husband, she told officers he had marijuana inside. When Charles McArthur refused consent to a search, an officer prevented him from re-entering the trailer unaccompanied while another officer left to obtain a warrant; for about two hours McArthur was allowed inside only with an officer observing. A warrant issued, the search found marijuana and a pipe, and McArthur moved to suppress the temporary restraint as unreasonable. ## Issue Whether police with probable cause may temporarily prevent a resident from entering his home unaccompanied, to avoid the destruction of evidence, while they diligently obtain a search warrant. ## Rule Yes, on these combined circumstances.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-334",
      "page": null,
      "quote": "We have found no case in which this Court has held unlawful a temporary seizure that was supported by probable cause and was designed to prevent the loss of evidence while the police diligently obtained a warrant in a reasonable period of time.",
      "star_marker": "334",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19295,
      "fragment": "#:~:text=We%20have%20found%20no%20case",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. McArthur",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789821,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
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
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tremblay",
          "cluster_id": 4428704,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Matthew Vaughn Diamond",
          "cluster_id": 4338873,
          "cite": [
            "890 N.W.2d 143",
            "2017 Minn. App. LEXIS 9",
            "2017 WL 163710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Stacey Renee McRae",
          "cluster_id": 3218840,
          "cite": [
            "194 So. 3d 524",
            "2016 Fla. App. LEXIS 9500",
            "2016 WL 3402450"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olushola Akinmboni v. United States",
          "cluster_id": 3155941,
          "cite": [
            "126 A.3d 694",
            "2015 D.C. App. LEXIS 530",
            "2015 WL 7289524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
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
        "journal_ref": "Illinois v. McArthur:lane1_negative"
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
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dave McNeil v. State",
          "cluster_id": 3094175,
          "cite": [
            "443 S.W.3d 295",
            "2014 WL 3843757",
            "2014 Tex. App. LEXIS 8519"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
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
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. State",
          "cluster_id": 1508583,
          "cite": [
            "221 S.W.3d 680",
            "2007 Tex. Crim. App. LEXIS 500",
            "2007 WL 1217343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Menotti v. City of Seattle",
          "cluster_id": 3032002,
          "cite": [
            "409 F.3d 1113",
            "2005 WL 1300994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2058953,
          "cite": [
            "830 N.E.2d 541",
            "215 Ill. 2d 261",
            "294 Ill. Dec. 129",
            "2005 Ill. LEXIS 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
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
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schriner",
          "cluster_id": 4635000,
          "cite": [
            "303 Neb. 476",
            "929 N.W.2d 514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Swietlicki",
          "cluster_id": 3157591,
          "cite": [
            "2015 CO 67",
            "361 P.3d 411",
            "2015 WL 7423463"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loria v. Gorman",
          "cluster_id": 7108550,
          "cite": [
            "306 F.3d 1271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Burton",
          "cluster_id": 777431,
          "cite": [
            "288 F.3d 91",
            "2002 U.S. App. LEXIS 7851",
            "2002 WL 753492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tierney",
          "cluster_id": 1972558,
          "cite": [
            "703 N.W.2d 204",
            "266 Mich. App. 687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 2200827,
          "cite": [
            "789 N.E.2d 260",
            "204 Ill. 2d 220",
            "273 Ill. Dec. 360",
            "2003 Ill. LEXIS 765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fredrick K. Koch v. Town of Brattleboro, Vermont, Sherwood D. Lake, Jr., and John Doe, Unidentified Brattleboro Police Officer",
          "cluster_id": 777318,
          "cite": [
            "287 F.3d 162",
            "2002 U.S. App. LEXIS 5301"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Bennett v. Wainwright",
          "cluster_id": 203573,
          "cite": [
            "548 F.3d 155",
            "2008 U.S. App. LEXIS 24217",
            "2008 WL 5005534"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McDonough",
          "cluster_id": 2483242,
          "cite": [
            "940 N.E.2d 1100",
            "239 Ill. 2d 260",
            "346 Ill. Dec. 496",
            "2010 Ill. LEXIS 1557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Colon",
          "cluster_id": 773257,
          "cite": [
            "250 F.3d 130",
            "2001 U.S. App. LEXIS 9205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Commonwealth",
          "cluster_id": 1063086,
          "cite": [
            "642 S.E.2d 295",
            "49 Va. App. 439",
            "2007 Va. App. LEXIS 113"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lampitok",
          "cluster_id": 2148470,
          "cite": [
            "798 N.E.2d 91",
            "207 Ill. 2d 231",
            "278 Ill. Dec. 244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjI3NjU3NjAwMDAwJnM9MjAzNTczJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118405+OR+9434039+OR+9434040+OR+9434041%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTgxMjk1MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118405+OR+9434039+OR+9434040+OR+9434041%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041)",
    "indexed_citing_opinions": 421,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118405,
        "count": 350,
        "count_source": "search"
      },
      {
        "opinion_id": 9434039,
        "count": 73,
        "count_source": "search"
      },
      {
        "opinion_id": 9434040,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434041,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 737,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-mcarthur.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNDQxMTYmcz05NDEyMTYxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118405+OR+9434039+OR+9434040+OR+9434041%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118405,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 111172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 2106379,
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
    "date_created": "2026-07-05T08:14:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:20:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. McArthur

```
<div>
<center><b><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">531 U.S. 326</a></span> (2001)</b></center>
<center><h1>ILLINOIS<br>
v.<br>
McARTHUR</h1></center>
<center>No. 99-1132.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued November 1, 2000.</center>
<center>Decided February 20, 2001.</center>
CERTIORARI TO THE APPELLATE COURT OF ILLINOIS, FOURTH DISTRICT
<p><span class="star-pagination">*328</span> Breyer, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Scalia, Kennedy, Souter, Thomas, and Ginsburg, JJ., joined. Souter, J., filed a concurring opinion, <i>post,</i> p. 337. Stevens, J., filed a dissenting opinion, <i>post,</i> p. 338.</p>
<p><i>Joel D. Bertocchi,</i> Solicitor General of Illinois, argued the cause for petitioner. With him on the briefs were <i>James E. Ryan,</i> Attorney General, and <i>William L. Browers</i> and <i>Colleen M. Griffin,</i> Assistant Attorneys General.</p>
<p><i>Matthew D. Roberts</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Waxman, Assistant Attorney General Robinson, Deputy Solicitor General Dreeben,</i> and <i>Deborah Watson.</i> </p>
<p><span class="star-pagination">*328</span> <i>Deanne Fortna Jones</i> argued the cause for respondent. With her on the brief was <i>Jeff Justice.</i><sup>[*]</sup></p>
<p>Justice Breyer, delivered the opinion of the Court.</p>
<p>Police officers, with probable cause to believe that a man had hidden marijuana in his home, prevented that man from entering the home for about two hours while they obtained a search warrant. We must decide whether those officers violated the Fourth Amendment. We conclude that the officers acted reasonably. They did not violate the Amendment's requirements. And we reverse an Illinois court's holding to the contrary.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>On April 2, 1997, Tera McArthur asked two police officers to accompany her to the trailer where she lived with her husband, Charles, so that they could keep the peace while she removed her belongings. The two officers, Assistant Chief John Love and Officer Richard Skidis, arrived with <span class="star-pagination">*329</span> Tera at the trailer at about 3:15 p.m. Tera went inside, where Charles was present. The officers remained outside.</p>
<p>When Tera emerged after collecting her possessions, she spoke to Chief Love, who was then on the porch. She suggested he check the trailer because "Chuck had dope in there." App. 15. She added (in Love's words) that she had seen Chuck "slid[e] some dope underneath the couch." <i>Id.,</i>  at 19.</p>
<p>Love knocked on the trailer door, told Charles what Tera had said, and asked for permission to search the trailer, which Charles denied. Love then sent Officer Skidis with Tera to get a search warrant.</p>
<p>Love told Charles, who by this time was also on the porch, that he could not reenter the trailer unless a police officer accompanied him. Charles subsequently reentered the trailer two or three times (to get cigarettes and to make phone calls), and each time Love stood just inside the door to observe what Charles did.</p>
<p>Officer Skidis obtained the warrant by about 5 p.m. He returned to the trailer and, along with other officers, searched it. The officers found under the sofa a marijuana pipe, a box for marijuana (called a "one-hitter" box), and a small amount of marijuana. They then arrested Charles.</p>
<p></p>
<h2>B</h2>
<p>Illinois subsequently charged Charles McArthur with unlawfully possessing drug paraphernalia and marijuana (less than 2.5 grams), both misdemeanors. See Ill. Comp. Stat., ch. 720, §§ 550/4(a), 600/3.5(a) (1998). McArthur moved to suppress the pipe, box, and marijuana on the ground that they were the "fruit" of an unlawful police seizure, namely, the refusal to let him reenter the trailer unaccompanied, which would have permitted him, he said, to "have destroyed the marijuana." App. 27.</p>
<p>The trial court granted McArthur's suppression motion. The Appellate Court of Illinois affirmed, 304 Ill. App. 3d <span class="star-pagination">*330</span> 395, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/" aria-description="Citation for case: People v. McArthur">713 N. E. 2d 93</a></span> (1999), and the Illinois Supreme Court denied the State's petition for leave to appeal, <span class="citation no-link">185 Ill. 2d 651</span>, <span class="citation no-link">720 N. E. 2d 1101</span> (1999). We granted certiorari to determine whether the Fourth Amendment prohibits the kind of temporary seizure at issue here.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>The Fourth Amendment says that the "right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." U. S. Const., Amdt. 4. Its "central requirement" is one of reasonableness. See <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 739</a></span> (1983). In order to enforce that requirement, this Court has interpreted the Amendment as establishing rules and presumptions designed to control conduct of law enforcement officers that may significantly intrude upon privacy interests. Sometimes those rules require warrants. We have said, for example, that in "the ordinary case," seizures of personal property are "unreasonable within the meaning of the Fourth Amendment," without more, "unless . . . accomplished pursuant to a judicial warrant," issued by a neutral magistrate after finding probable cause. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S. 696, 701</a></span> (1983).</p>
<p>We nonetheless have made it clear that there are exceptions to the warrant requirement. When faced with special law enforcement needs, diminished expectations of privacy, minimal intrusions, or the like, the Court has found that certain general, or individual, circumstances may render a warrantless search or seizure reasonable. See, <i>e. g., </i><i>Pennsylvania</i> v. <i>Labron,</i> <span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/#940" aria-description="Citation for case: Pennsylvania v. Labron">518 U. S. 938, 940-941</a></span> (1996) <i>(per curiam)</i> (search of automobile supported by probable cause); <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#455" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444, 455</a></span> (1990) (suspicionless stops at drunk driver checkpoint); <i>United States</i> v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 706</a></span> (temporary seizure of luggage based on reasonable suspicion); <i>Michigan</i> v. <span class="star-pagination">*331</span> <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 702-705</a></span> (1981) (temporary detention of suspect without arrest warrant to prevent flight and protect officers while executing search warrant); <i>Terry</i> v. <i>Ohio,</i>  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 27</a></span> (1968) (temporary stop and limited search for weapons based on reasonable suspicion).</p>
<p>In the circumstances of the case before us, we cannot say that the warrantless seizure was <i>per se</i> unreasonable. It involves a plausible claim of specially pressing or urgent law enforcement need, <i>i. e.,</i> "exigent circumstances." Cf., <i>e. g., </i><i>United States</i> v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 701</a></span> ("[T]he exigencies of the circumstances" may permit temporary seizure without warrant); <i>Warden, Md. Penitentiary</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span> (1967) (warrantless search for suspect and weapons reasonable where delay posed grave danger); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (1966) (warrantless blood test for alcohol reasonable where delay would have led to loss of evidence). Moreover, the restraint at issue was tailored to that need, being limited in time and scope, cf. <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 29-30</a></span>, and avoiding significant intrusion into the home itself, cf. <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 585</a></span> (1980) ("`[T]he chief evil against which the . . . Fourth Amendment is directed' " is warrantless entry and search of home) (quoting <i>United States</i> v. <i>United States Dist. Court for Eastern Dist. of Mich.,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972)). Consequently, rather than employing a <i>per se</i>  rule of unreasonableness, we balance the privacy-related and law enforcement-related concerns to determine if the intrusion was reasonable. Cf. <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979) (determining lawfulness by balancing privacy and law enforcement interests); <i>United States</i> v. <i>BrignoniPonce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975) (same).</p>
<p>We conclude that the restriction at issue was reasonable, and hence lawful, in light of the following circumstances, which we consider in combination. First, the police had probable cause to believe that McArthur's trailer home contained evidence of a crime and contraband, namely, unlawful <span class="star-pagination">*332</span> drugs. The police had had an opportunity to speak with Tera McArthur and make at least a very rough assessment of her reliability. They knew she had had a firsthand opportunity to observe her husband's behavior, in particular with respect to the drugs at issue. And they thought, with good reason, that her report to them reflected that opportunity. Cf. <i>Massachusetts</i> v. <i>Upton,</i> <span class="citation" data-id="9429595"><a href="/opinion/111172/massachusetts-v-upton/#732" aria-description="Citation for case: Massachusetts v. Upton">466 U. S. 727, 732-734</a></span> (1984) <i>(per curiam)</i> (upholding search warrant issued in similar circumstances).</p>
<p>Second, the police had good reason to fear that, unless restrained, McArthur would destroy the drugs before they could return with a warrant. They reasonably might have thought that McArthur realized that his wife knew about his marijuana stash; observed that she was angry or frightened enough to ask the police to accompany her; saw that after leaving the trailer she had spoken with the police; and noticed that she had walked off with one policeman while leaving the other outside to observe the trailer. They reasonably could have concluded that McArthur, consequently suspecting an imminent search, would, if given the chance, get rid of the drugs fast.</p>
<p>Third, the police made reasonable efforts to reconcile their law enforcement needs with the demands of personal privacy. They neither searched the trailer nor arrested McArthur before obtaining a warrant. Rather, they imposed a significantly less restrictive restraint, preventing McArthur only from entering the trailer unaccompanied. They left his home and his belongings intactuntil a neutral Magistrate, finding probable cause, issued a warrant.</p>
<p>Fourth, the police imposed the restraint for a limited period of time, namely, two hours. Cf. <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i>  at 28</a></span> (manner in which police act is "vital . .. part of . . . inquiry"). As far as the record reveals, this time period was no longer than reasonably necessary for the police, acting with diligence, to obtain the warrant. Compare <i>United</i>  <span class="star-pagination">*333</span> <i>States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709-710</a></span> (holding 90-minute detention of luggage unreasonable based on nature of interference with person's travels and lack of diligence of police), with <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#253" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249, 253</a></span> (1970) (holding 29-hour detention of mailed package reasonable given unavoidable delay in obtaining warrant and minimal nature of intrusion). Given the nature of the intrusion and the law enforcement interest at stake, this brief seizure of the premises was permissible.</p>
<p></p>
<h2>B</h2>
<p>Our conclusion that the restriction was lawful finds significant support in this Court's case law. In <i>Segura</i> v. <i>United States,</i> <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U. S. 796</a></span> (1984), the Court considered the admissibility of drugs which the police had found in a lawful, warrant-based search of an apartment, but only after unlawfully entering the apartment and occupying it for 19 hours. The majority held that the drugs were admissible because, had the police acted lawfully throughout, they could have discovered and seized the drugs pursuant to the validly issued warrant. See <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#799" aria-description="Citation for case: Segura v. United States"><i>id.,</i> at 799</a></span>, 814-815 (citing <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920)). The minority disagreed. However, when describing alternative lawful search and seizure methods, both majority and minority assumed, at least for argument's sake, that the police, armed with reliable information that the apartment contained drugs, might lawfully have sealed the apartment from the outside, restricting entry into the apartment while waiting for the warrant. Compare <i>Segura</i>  v. <i>United States,</i> <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#814" aria-description="Citation for case: Segura v. United States">468 U. S., at 814</a></span> ("Had police never entered the apartment, but instead conducted a perimeter stake out to prevent anyone from entering . . . and destroying evidence, the contraband . . .would have been . . .seized precisely as it was here"), with <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#824" aria-description="Citation for case: Segura v. United States"><i>id.,</i> at 824, n. 15</a></span> (Stevens, J., dissenting) ("I assume impoundment would be permissible <span class="star-pagination">*334</span> even absent exigent circumstances when it occurs `from the outside'when the authorities merely seal off premises pending the issuance of a warrant but do not enter"); see also <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 394</a></span> (1978) (exigent circumstances do not justify search where police guard at door could prevent loss of evidence); <i>United States</i> v. <i>Jeffers,</i>  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 52</a></span> (1951) (same).</p>
<p>In various other circumstances, this Court has upheld temporary restraints where needed to preserve evidence until police could obtain a warrant. See, <i>e. g., </i><i>United States</i>  v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 706</a></span> (reasonable suspicion justifies brief detention of luggage pending further investigation); <i>United States</i> v. <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#253" aria-description="Citation for case: United States v. Van Leeuwen"><i>Van Leeuwen, supra,</i> at 253</a></span> (reasonable suspicion justifies detaining package delivered for mailing). Cf. <i>Richards</i> v. <i>Wisconsin,</i> <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#395" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 395</a></span> (1997) (no need to "knock and announce" when executing a search warrant where officers reasonably suspect that evidence might be destroyed); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span> (1925) (warrantless search of automobile constitutionally permissible).</p>
<p>We have found no case in which this Court has held unlawful a temporary seizure that was supported by probable cause and was designed to prevent the loss of evidence while the police diligently obtained a warrant in a reasonable period of time. But cf. <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#754" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 754</a></span> (1984) (holding warrantless entry into and arrest in home unreasonable despite possibility that evidence of noncriminal offense would be lost while warrant was being obtained).</p>
<p></p>
<h2>C</h2>
<p>Nor are we persuaded by the countervailing considerations that the parties or lower courts have raised. McArthur argues that the police proceeded without probable cause. But McArthur has waived this argument. See <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#397" aria-description="Citation for case: People v. McArthur">304 Ill. App. 3d, at 397</a></span>, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#95" aria-description="Citation for case: People v. McArthur">713 N. E. 2d, at 95</a></span> (stating that McArthur <span class="star-pagination">*335</span> does not contest existence of probable cause); Brief in Opposition 7 (acknowledging probable cause). And, in any event, it is without merit. See <i>supra,</i> at 331-332.</p>
<p>The Appellate Court of Illinois concluded that the police could not order McArthur to stay outside his home because McArthur's porch, where he stood at the time, was part of his home; hence the order "amounted to a constructive eviction" of McArthur from his residence. <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#402" aria-description="Citation for case: People v. McArthur">304 Ill. App. 3d, at 402</a></span>, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#98" aria-description="Citation for case: People v. McArthur">713 N. E. 2d, at 98</a></span>. This Court has held, however, that a person standing in the doorway of a house is "in a `public' place," and hence subject to arrest without a warrant permitting entry of the home. <i>United States</i> v. <i>Santana,</i>  <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42</a></span> (1976). Regardless, we do not believe the difference to which the Appellate Court pointsporch versus, <i>e. g.,</i> front walkcould make a significant difference here as to the reasonableness of the police restraint; and that, from the Fourth Amendment's perspective, is what matters.</p>
<p>The Appellate Court also found negatively significant the fact that Chief Love, with McArthur's consent, stepped inside the trailer's doorway to observe McArthur when McArthur reentered the trailer on two or three occasions. <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#402" aria-description="Citation for case: People v. McArthur">304 Ill. App. 3d, at 402-403</a></span>, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#98" aria-description="Citation for case: People v. McArthur">713 N. E. 2d, at 98</a></span>. McArthur, however, reentered simply for his own convenience, to make phone calls and to obtain cigarettes. Under these circumstances, the reasonableness of the greater restriction (preventing reentry) implies the reasonableness of the lesser (permitting reentry conditioned on observation).</p>
<p>Finally, McArthur points to a case (and we believe it is the only case) that he believes offers direct support, namely, <i>Welsh</i> v. <i>Wisconsin, supra</i><i>.</i> In <i><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">Welsh</a></span>,</i> this Court held that police could not enter a home without a warrant in order to prevent the loss of evidence (namely, the defendant's blood alcohol level) of the "nonjailable traffic offense" of driving while intoxicated. 466 U. S., at 742, 754. McArthur notes <span class="star-pagination">*336</span> that his two convictions are for misdemeanors, which, he says, are as minor, and he adds that the restraint, keeping him out of his home, was nearly as serious.</p>
<p>We nonetheless find significant distinctions. The evidence at issue here was of crimes that were "jailable," not "nonjailable." See Ill. Comp. Stat., ch. 720, § 550/4(a) (1998); ch. 730, § 5/5-83(3) (possession of less than 2.5 grams of marijuana punishable by up to 30 days in jail); ch. 720, § 600/ 3.5; ch. 730, § 5/5-83(1) (possession of drug paraphernalia punishable by up to one year in jail). In <i><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">Welsh</a></span>,</i> we noted that, "[g]iven that the classification of state crimes differs widely among the States, the penalty that may attach to any particular offense seems to provide the clearest and most consistent indication of the State's interest in arresting individuals suspected of committing that offense." 466 U. S., at 754, n. 14. The same reasoning applies here, where class C misdemeanors include such widely diverse offenses as drag racing, drinking alcohol in a railroad car or on a railroad platform, bribery by a candidate for public office, and assault. See, <i>e. g.,</i> Ill. Comp. Stat., ch. 65, § 5/4-82 (1998); ch. 610, § 90/1; ch. 625, § 5/11-504; ch. 720, § 5/12-1.</p>
<p>And the restriction at issue here is less serious. Temporarily keeping a person from entering his home, a consequence whenever police stop a person on the street, is considerably less intrusive than police entry into the home itself in order to make a warrantless arrest or conduct a search. Cf. <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S., at 585</a></span> (the Fourth Amendment's central concern is the warrantless entry and search of the home).</p>
<p>We have explained above why we believe that the need to preserve evidence of a "jailable" offense was sufficiently urgent or pressing to justify the restriction upon entry that the police imposed. We need not decide whether the circumstances before us would have justified a greater restriction for this type of offense or the same restriction were only a "nonjailable" offense at issue.</p>
<p></p>
<h2>
<span class="star-pagination">*337</span> III</h2>
<p>In sum, the police officers in this case had probable cause to believe that a home contained contraband, which was evidence of a crime. They reasonably believed that the home's resident, if left free of any restraint, would destroy that evidence. And they imposed a restraint that was both limited and tailored reasonably to secure law enforcement needs while protecting privacy interests. In our view, the restraint met the Fourth Amendment's demands.</p>
<p>The judgment of the Illinois Appellate Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Souter, concurring.</p>
<p>I join the Court's opinion subject to this afterword on two points: the constitutionality of a greater intrusion than the one here and the permissibility of choosing impoundment over immediate search. Respondent McArthur's location made the difference between the exigency that justified temporarily barring him from his own dwelling and circumstances that would have supported a greater interference with his privacy and property. As long as he was inside his trailer, the police had probable cause to believe that he had illegal drugs stashed as his wife had reported and that with any sense he would flush them down the drain before the police could get a warrant to enter and search. This probability of destruction in anticipation of a warrant exemplifies the kind of present risk that undergirds the accepted exigent circumstances exception to the general warrant requirement. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (1966). That risk would have justified the police in entering McArthur's trailer promptly to make a lawful, warrantless search. <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42-43</a></span> (1976); <i>Warden, Md. Penitentiary</i> v. <i>Hayden,</i>  <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span> (1967). When McArthur stepped <span class="star-pagination">*338</span> outside and left the trailer uninhabited, the risk abated and so did the reasonableness of entry by the police for as long as he was outside. This is so because the only justification claimed for warrantless action here is the immediate risk, and the limit of reasonable response by the police is set by the scope of the risk. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 25-26</a></span> (1968).</p>
<p>Since, however, McArthur wished to go back in, why was it reasonable to keep him out when the police could perfectly well have let him do as he chose, and then enjoyed the ensuing opportunity to follow him and make a warrantless search justified by the renewed danger of destruction? The answer is not that the law officiously insists on safeguarding a suspect's privacy from search, in preference to respecting the suspect's liberty to enter his own dwelling. Instead, the legitimacy of the decision to impound the dwelling follows from the law's strong preference for warrants, which underlies the rule that a search with a warrant has a stronger claim to justification on later, judicial review than a search without one. See <i>United States</i> v<i>. Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#106" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 106</a></span> (1965); see also 5 W. LaFave, Search and Seizure § 11.2(b), p. 38 (3d ed. 1996) ("[M]ost states follow the rule which is utilized in the federal courts: if the search or seizure was pursuant to a warrant, the defendant has the burden of proof; but if the police acted without a warrant the burden of proof is on the prosecution"). The law can hardly raise incentives to obtain a warrant without giving the police a fair chance to take their probable cause to a magistrate and get one.</p>
<p>Justice Stevens, dissenting.</p>
<p>The Illinois General Assembly has decided that the possession of less than 2.5 grams of marijuana is a class C misdemeanor. See Ill. Comp. Stat., ch. 720, § 550/4(a) (1998). In so classifying the offense, the legislature made a concerted policy judgment that the possession of small amounts of <span class="star-pagination">*339</span> marijuana for personal use does not constitute a particularly significant public policy concern. While it is true that this offenselike feeding livestock on a public highway or offering a movie for rent without clearly displaying its rating<sup>[1]</sup> may warrant a jail sentence of up to 30 days, the detection and prosecution of possessors of small quantities of this substance is by no means a law enforcement priority in the State of Illinois.<sup>[2]</sup></p>
<p>Because the governmental interest implicated by the particular criminal prohibition at issue in this case is so slight, this is a poor vehicle for probing the boundaries of the government's power to limit an individual's possessory interest in his or her home pending the arrival of a search warrant. Cf. <i>Segura</i> v. <i>United States,</i> <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U. S. 796</a></span> (1984) (seven Justices decline to address this issue because case does not require its resolution). Given my preference, I would, therefore, dismiss the writ of certiorari as improvidently granted.</p>
<p>Compelled by the vote of my colleagues to reach the merits, I would affirm. As the majority explains, the essential inquiry in this case involves a balancing of the "privacyrelated <span class="star-pagination">*340</span> and law enforcement-related concerns to determine if the intrusion was reasonable." <i>Ante,</i> at 331. Under the specific facts of this case, I believe the majority gets the balance wrong. Each of the Illinois jurists who participated in the decision of this case placed a higher value on the sanctity of the ordinary citizen's home than on the prosecution of this petty offense. They correctly viewed that interestwhether the home be a humble cottage, a secondhand trailer, or a stately mansionas one meriting the most serious constitutional protection.<sup>[3]</sup> Following their analysis and the reasoning in our decision in <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984) (holding that some offenses may be so minor as to make it unreasonable for police to undertake searches that would be constitutionally permissible if graver offenses were suspected), I would affirm.</p>
<h2>NOTES</h2>
<p>[*]   A brief of <i>amici curiae</i> urging reversal was filed for the State of Ohio et al. by <i>Betty D. Montgomery,</i> Attorney General of Ohio, <i>Edward B. Foley,</i> State Solicitor, and <i>Robert C. Maier</i> and <i>Matthew D. Miko,</i> Assistant Solicitors, and by the Attorneys General for their respective States as follows: <i>Bruce M. Botelho</i> of Alaska, <i>Janet Napolitano</i> of Arizona, <i>M. Jane Brady</i> of Delaware, <i>Alan G. Lance</i> of Idaho, <i>Thomas J. Miller</i> of Iowa, <i>Andrew Ketterer</i> of Maine, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Mike Hatch</i> of Minnesota, <i>Joseph P. Mazurek</i> of Montana, <i>Philip McLaughlin</i>  of New Hampshire, <i>John J. Farmer, Jr.,</i> of New Jersey, <i>Don Stenberg</i> of Nebraska, <i>Frankie Sue Del Papa</i> of Nevada, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Charles M. Condon</i> of South Carolina, <i>Mark Barnett</i> of South Dakota, <i>Jan Graham</i> of Utah, <i>William H. Sorrell</i> of Vermont, <i>Christine O. Gregoire</i> of Washington, <i>Thomas F. Reilly</i> of Massachusetts, <i>D. Michael Fisher</i> of Pennsylvania, and <i>Mark L. Earley</i> of Virginia.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the National Association of Criminal Defense Lawyers by <i>Lisa B. Kemler;</i> and for the Rutherford Institute by <i>John W. Whitehead</i> and <i>Steven H. Aden.</i> </p>
<p>[1]  See Ill. Comp. Stat., ch. 605, § 5/9-124.1 (1998) (making feeding livestock on a public highway a class C misdemeanor); ch. 720, §§ 395/3-395/4 (making it a class C misdemeanor to sell or rent a video that does not display the official rating of the motion picture from which it is copied). Other examples of offenses classified as class C misdemeanors in Illinois include camping on the side of a public highway, ch. 605, § 5/9-124, interfering with the "lawful taking of wild animals," ch. 720, § 125/2, and tattooing the body of a person under 21 years of age, ch. 720, § 5/12-10.</p>
<p>[2]  Nor in many other States. Under the laws of many other States, the maximum penalty McArthur would have faced for possession of 2.3 grams of marijuana would have been less than what he faced in Illinois. See, <i>e. g.,</i> Cal. Health &amp; Safety Code Ann. § 11357(b) (West 1991) ($100 fine); <span class="citation no-link">Colo. Rev. Stat. § 18-18-406</span>(1) (1999) ($100 fine); <span class="citation no-link">Minn. Stat. § 152.027</span>(4) (2000) ($200 fine and drug education); <span class="citation no-link">Miss. Code Ann. § 41-29-139</span>(c)(2)(A) (Supp. 1999) ($100$250 fine); <span class="citation no-link">Neb. Rev. Stat. § 28-416</span>(13) (1995) ($100 fine and drug education); N. M. Stat. Ann. § 30-31-23(B) (1997) ($50$100 fine and 15 days in jail); N. Y. Penal Law § 221.05 (McKinney 2000) ($100 fine); Ore. Rev. Stat. § 475.992(4)(f) (Supp. 1998) ($100 fine).</p>
<p>[3]  Principled respect for the sanctity of the home has long animated this Court's Fourth Amendment jurisprudence. See, <i>e. g., </i><i>Wilson</i> v. <i>Layne,</i> <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#610" aria-description="Citation for case: Wilson v. Layne">526 U. S. 603, 610</a></span> (1999) ("The Fourth Amendment embodies this centuries-old principle of respect for the privacy of the home"); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 601</a></span> (1980) (emphasizing "the overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic"); <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978) ("[T]he Fourth Amendment reflects the view of those who wrote the Bill of Rights that the privacy of a person's home and property may not be totally sacrificed in the name of maximum simplicity in enforcement of the criminal law").</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Illinois v. Perkins.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Illinois v. Perkins"
type: case
citation: "496 U.S. 292 (1990)"
parallel_cite: "110 S. Ct. 2394; 110 L. Ed. 2d 243"
neutral_cite: 1990 U.S. LEXIS 2885
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-06-04
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-06-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Perkins
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112452/illinois-v-perkins/"
  cluster_id: 112452
  opinion_id: 9432050
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Hoffa v. United States]]", "[[Rhode Island v. Innis]]", "[[Berkemer v. McCarty]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "undercover", "custodial-interrogation"]
holding: "Miranda warnings are not required when an undercover officer (or agent) posing as an inmate elicits statements from a suspect — because…"
lake:
  record_id: Illinois v. Perkins
  status: verified
  projected_at: 2026-07-06
---

# Illinois v. Perkins

*496 U.S. 292 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police placed an undercover agent, John Parisi (using the alias "Vito Bianco"), and an informant in a cellblock with Perkins, who was jailed on an unrelated charge. Posing as fellow inmates planning a sham escape, they drew Perkins into conversation, and he made statements implicating himself in a murder under investigation. He received no *[[Miranda v. Arizona|Miranda]]* warnings and moved to suppress the statements.

## Issue
Whether *[[Miranda v. Arizona|Miranda]]* warnings are required before an undercover law enforcement officer, posing as a fellow inmate, questions an incarcerated suspect in a manner likely to elicit an incriminating response.

## Rule
No. "Conversations between suspects and undercover agents do not implicate the concerns underlying Miranda. The essential ingredients of a 'police-dominated atmosphere' and compulsion are not present when an incarcerated person speaks freely to someone whom he believes to be a fellow inmate." — 496 U.S. at 296. ^pin-296

"We hold that an undercover law enforcement officer posing as a fellow inmate need not give Miranda warnings to an incarcerated suspect before asking questions that may elicit an incriminating response." — *Id.* at 300. ^pin-300

## Application
Perkins spoke to Parisi believing him to be a fellow inmate, not a person with official power over him, so the coercive, police-dominated atmosphere that *[[Miranda v. Arizona|Miranda]]* guards against was absent; Perkins talked to impress his supposed cellmates and "spoke at his own peril." Because the essential coercion of custodial interrogation was missing, no *[[Miranda v. Arizona|Miranda]]* warnings were required and his voluntary statements were admissible.

## Conclusion
No *[[Miranda v. Arizona|Miranda]]* warnings were required; the statements were admissible and the suppression reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Perkins* limits [[Miranda v. Arizona]] to its coercion rationale and aligns with [[Hoffa v. United States]] on the use of undercover agents; the holding governs the Fifth Amendment only, leaving the Sixth Amendment deliberate-elicitation rule untouched once charges are filed.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Illinois v. Perkins*, 496 U.S. 292 (1990) — https://www.courtlistener.com/opinion/112452/illinois-v-perkins/ — pinpoints: 296, 300.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ea7efac5c6776799", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Perkins"}, "payload": {"all": [{"cite": "496 U.S. 292", "page": "292", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "496"}, {"cite": "110 S. Ct. 2394", "page": "2394", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "110 L. Ed. 2d 243", "page": "243", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "1990 U.S. LEXIS 2885", "page": "2885", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}], "display": "496 U.S. 292", "official": {"cite": "496 U.S. 292", "page": "292", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "496"}, "official_selection_present": true, "record_id": "Illinois v. Perkins"}}
{"assertion_id": "9e3138f8b8da4296", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-296", "record_id": "Illinois v. Perkins"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-296", "pinpoint_status": "slip-only", "quote": "), and an informant in a cellblock with Perkins, who was jailed on an unrelated charge. Posing as fellow inmates planning a sham escape, they drew Perkins into conversation, and he made statements implicating himself in a murder under investigation. He received no *Miranda* warnings and moved to suppress the statements. ## Issue Whether *Miranda* warnings are required before an undercover law enforcement officer, posing as a fellow inmate, questions an incarcerated suspect in a manner likely to elicit an incriminating response. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Perkins", "star_marker": null}}
{"assertion_id": "ebc3c19b250e8763", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-300", "record_id": "Illinois v. Perkins"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-300", "pinpoint_status": "slip-only", "quote": "We hold that an undercover law enforcement officer posing as a fellow inmate need not give Miranda warnings to an incarcerated suspect before asking questions that may elicit an incriminating response.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Perkins", "star_marker": null}}
{"assertion_id": "8b117b8dc67ac545", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Perkins"}, "payload": {"as_of_content": "1990-06-04", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Perkins", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. Perkins

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Perkins",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Perkins",
    "case_name_short": "Perkins",
    "case_name_full": "Illinois v. Perkins",
    "input_case_name": "Illinois v. Perkins",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-06-04",
    "year": 1990,
    "docket": null,
    "cluster_id": 112452,
    "lead_opinion_id": 9432050,
    "sibling_ids": [
      112452,
      9432050,
      9432051,
      9432052
    ],
    "absolute_url": "/opinion/112452/illinois-v-perkins/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9094326,
        "score": 20,
        "case_name": "Illinois v. Perkins"
      },
      {
        "cluster_id": 9094325,
        "score": 20,
        "case_name": "Illinois v. Perkins"
      },
      {
        "cluster_id": 9093481,
        "score": 20,
        "case_name": "Illinois v. Perkins"
      },
      {
        "cluster_id": 9093480,
        "score": 20,
        "case_name": "Illinois v. Perkins"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "496 U.S. 292",
      "volume": "496",
      "reporter": "U.S.",
      "page": "292",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 2394",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 243",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "243",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 2885",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2885",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "496 U.S. 292",
        "volume": "496",
        "reporter": "U.S.",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 2394",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 243",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "243",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 2885",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2885",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "496 U.S. 292",
    "official_selection": {
      "court_class": "scotus",
      "selected": "496 U.S. 292",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-296",
      "page": null,
      "quote": "), and an informant in a cellblock with Perkins, who was jailed on an unrelated charge. Posing as fellow inmates planning a sham escape, they drew Perkins into conversation, and he made statements implicating himself in a murder under investigation. He received no *Miranda* warnings and moved to suppress the statements. ## Issue Whether *Miranda* warnings are required before an undercover law enforcement officer, posing as a fellow inmate, questions an incarcerated suspect in a manner likely to elicit an incriminating response. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-300",
      "page": null,
      "quote": "We hold that an undercover law enforcement officer posing as a fellow inmate need not give Miranda warnings to an incarcerated suspect before asking questions that may elicit an incriminating response.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-06-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Perkins",
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
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hallford",
          "cluster_id": 4444995,
          "cite": [
            "280 F. Supp. 3d 170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "NYIA GORE v. UNITED STATES",
          "cluster_id": 4248978,
          "cite": [
            "145 A.3d 540",
            "2016 D.C. App. LEXIS 313",
            "2016 WL 4411321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
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
        "journal_ref": "Illinois v. Perkins:lane1_negative"
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
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Burgos",
          "cluster_id": 2754022,
          "cite": [
            "470 Mass. 133",
            "19 N.E.3d 843"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
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
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Whitfield",
          "cluster_id": 2968731,
          "cite": [
            "695 F.3d 288",
            "2012 U.S. App. LEXIS 17762",
            "2012 WL 3591038"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
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
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Passino",
          "cluster_id": 5899747,
          "cite": [
            "53 A.D.3d 204",
            "861 N.Y.S.2d 168"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tate, 07 Ma 130 (6-26-2008)",
          "cluster_id": 3981154,
          "cite": [
            "2008 Ohio 3245"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Damon Kimbrough",
          "cluster_id": 796843,
          "cite": [
            "477 F.3d 144",
            "2007 U.S. App. LEXIS 3488",
            "2007 WL 495026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane1_negative"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clair",
          "cluster_id": 1171441,
          "cite": [
            "828 P.2d 705",
            "2 Cal. 4th 629",
            "7 Cal. Rptr. 2d 564",
            "92 Cal. Daily Op. Serv. 3966",
            "92 Daily Journal DAR 6358",
            "1992 Cal. LEXIS 1837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. State",
          "cluster_id": 1872663,
          "cite": [
            "241 S.W.3d 520",
            "2007 Tex. Crim. App. LEXIS 1675",
            "2007 WL 4146707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leger",
          "cluster_id": 1592017,
          "cite": [
            "936 So. 2d 108",
            "2006 WL 1883421"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzales and Soliz",
          "cluster_id": 844263,
          "cite": [
            "256 P.3d 543",
            "52 Cal. 4th 254",
            "128 Cal. Rptr. 3d 417",
            "2011 Cal. LEXIS 7683"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Traylor v. State",
          "cluster_id": 1765408,
          "cite": [
            "596 So. 2d 957",
            "1992 WL 4873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Matheny",
          "cluster_id": 2637091,
          "cite": [
            "46 P.3d 453",
            "2002 WL 1009210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Atwood",
          "cluster_id": 1182224,
          "cite": [
            "832 P.2d 593",
            "171 Ariz. 576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Davis",
          "cluster_id": 2575950,
          "cite": [
            "115 P.3d 417",
            "31 Cal. Rptr. 3d 96",
            "36 Cal. 4th 510",
            "2005 Cal. Daily Op. Serv. 6393",
            "2005 Daily Journal DAR 8733",
            "2005 Cal. LEXIS 7963"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Leonard",
          "cluster_id": 2632907,
          "cite": [
            "157 P.3d 973",
            "58 Cal. Rptr. 3d 368",
            "40 Cal. 4th 1370",
            "2007 Cal. Daily Op. Serv. 5424",
            "2007 Cal. LEXIS 5071"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Perez",
          "cluster_id": 2691798,
          "cite": [
            "2009 Ohio 6179",
            "124 Ohio St. 3d 122",
            "920 N.E.2d 104"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Smalls",
          "cluster_id": 145451,
          "cite": [
            "605 F.3d 765",
            "2010 U.S. App. LEXIS 9107",
            "2010 WL 1745123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Manning",
          "cluster_id": 2074839,
          "cite": [
            "695 N.E.2d 423",
            "182 Ill. 2d 193",
            "230 Ill. Dec. 933",
            "1998 Ill. LEXIS 368"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
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
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tate",
          "cluster_id": 2512108,
          "cite": [
            "234 P.3d 428",
            "49 Cal. 4th 635",
            "112 Cal. Rptr. 3d 156",
            "2010 Cal. LEXIS 6548"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Perkins:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112452 OR 9432050 OR 9432051 OR 9432052) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTI2NzQyNDAwMDAwJnM9MjUxMzc1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112452+OR+9432050+OR+9432051+OR+9432052%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(112452 OR 9432050 OR 9432051 OR 9432052)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDYmcz0xMzc3NTk1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112452+OR+9432050+OR+9432051+OR+9432052%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112452 OR 9432050 OR 9432051 OR 9432052)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 1,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112452 OR 9432050 OR 9432051 OR 9432052)",
    "indexed_citing_opinions": 516,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112452,
        "count": 441,
        "count_source": "search"
      },
      {
        "opinion_id": 9432050,
        "count": 83,
        "count_source": "search"
      },
      {
        "opinion_id": 9432051,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432052,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 908,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-perkins.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0MjUwMzImcz05NDI0MTMxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112452+OR+9432050+OR+9432051+OR+9432052%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112452,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 108231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 112410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112452,
        "cited_id": 2099831,
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
    "date_created": "2026-07-05T08:20:09Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:20:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:20:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:26:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:20:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Perkins

```
<opinion type="majority">
<author id="b336-4"><page-number citation-index="1" label="294">*294</page-number>Justice Kennedy</author>
<p id="A4l">delivered the opinion of the Court.</p>
<p id="b336-5">An undercover government agent was placed in the cell of respondent Perkins, who was incarcerated on charges unrelated to the subject of the agent’s investigation. Respondent made statements that implicated him in the crime that the agent sought to solve. Respondent claims that the statements should be inadmissible because he had not been given <em>Miranda </em>warnings by the agent. We hold that the statements are admissible. <em>Miranda </em>warnings are not required when the suspect is unaware that he is speaking to a law enforcement officer and gives a voluntary statement.</p>
<p id="b336-6">I</p>
<p id="b336-7">In November 1984, Richard Stephenson was murdered in a suburb of East St. Louis, Illinois. The murder remained unsolved until March 1986, when one Donald Charlton told police that he had learned about a homicide from a fellow inmate at the Graham Correctional Facility, where Charlton had been serving a sentence for burglary. The fellow inmate was Lloyd Perkins, who is the respondent here. Charlton told police that, while at Graham, he had befriended respondent, who told him in detail about a murder that respondent had committed in East St. Louis. On hearing Charlton’s account, the police recognized details of the Stephenson murder that were not well known, and so they treated Charlton’s story as a credible one.</p>
<p id="b336-8">By the time the police heard Charlton’s account, respondent had been released from Graham, but police traced him to a jail in Montgomery County, Illinois, where he was being held pending trial on a charge of aggravated battery, unrelated to the Stephenson murder. The police wanted to investigate further respondent’s connection to the Stephenson murder, but feared that the use of an eavesdropping device would prove impracticable and unsafe. They decided instead to place an undercover agent in the cellblock with respondent and Charlton. The plan was for Charlton and un<page-number citation-index="1" label="295">*295</page-number>dercover agent John Parisi to pose as escapees from a work release program who had been arrested in the course of a burglary. Parisi and Charlton were instructed to engage respondent in casual conversation and report anything he said about the Stephenson murder.</p>
<p id="b337-5">Parisi, using the alias “Vito Bianco,” and Charlton, both clothed in jail garb, were placed in the cellblock with respondent at the Montgomery County jail. The cellblock consisted of 12 separate cells that opened onto a common room. Respondent greeted Charlton who, after a brief conversation with respondent, introduced Parisi by his alias. Parisi told respondent that he “wasn’t going to do any more time” and suggested that the three of them escape. Respondent replied that the Montgomery County jail was “rinky-dink” and that they could “break out.” The trio met in respondent’s cell later that evening, after the other inmates were asleep, to refine their plan. Respondent said that his girlfriend could smuggle in a pistol. Charlton said: “Hey, Pm not a murderer, Pm a burglar. That’s your guys’ profession.” After telling Charlton that he would be responsible for any murder that occurred, Parisi asked respondent if he had ever “done” anybody. Respondent said that he had and proceeded to describe at length the events of the Stephenson murder. Parisi and respondent then engaged in some casual conversation before respondent went to sleep. Parisi did not give respondent <em>Miranda </em>warnings before the conversations.</p>
<p id="b337-6">Respondent was charged with the Stephenson murder. Before trial, he moved to suppress the statements made to Parisi in the jail. The trial court granted the motion to suppress, and the State appealed. The Appellate Court of Illinois affirmed, <span class="citation" data-id="2099831"><a href="/opinion/2099831/people-v-perkins/" aria-description="Citation for case: People v. Perkins">176 Ill. App. 3d 443</a></span>, <span class="citation" data-id="2099831"><a href="/opinion/2099831/people-v-perkins/" aria-description="Citation for case: People v. Perkins">531 N. E. 2d 141</a></span> (1988), holding that <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), prohibits all undercover contacts with incarcerated suspects that are reasonably likely to elicit an incriminating response.</p>
<p id="b337-7">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./493/808/">493 U. S. 808</a></span> (1989), to decide whether an undercover law enforcement officer must give <page-number citation-index="1" label="296">*296</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to an incarcerated suspect before asking him questions that may elicit an incriminating response. We now reverse.</p>
<p id="b338-5">II</p>
<p id="b338-6">In <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra,</a></span> </em>the Court held that the Fifth Amendment privilege against self-incrimination prohibits admitting statements given by a suspect during “custodial interrogation” without a prior warning. Custodial interrogation means “questioning initiated by law enforcement officers after a person has been taken into custody . . . .” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. The warning mandated by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was meant to preserve the privilege during “incommunicado interrogation of individuals in a police-dominated atmosphere.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 445</a></span>. That atmosphere is said to generate “inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 467</a></span>. “Fidelity to the doctrine announced in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires that it be enforced strictly, but only in those types of situations in which the concerns that powered the decision are implicated.” <em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#437" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 437</a></span> (1984).</p>
<p id="b338-7">Conversations between suspects and undercover agents do not implicate the concerns underlying <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The essential ingredients of a “police-dominated atmosphere” and compulsion are not present when an incarcerated person speaks freely to someone whom he believes to be a fellow inmate. Coercion is determined from the perspective of the suspect. <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 301</a></span> (1980); <em>Berkemer </em>v. <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty"><em>McCarty, supra, </em>at 442</a></span>. When a suspect considers himself in the company of cellmates and not officers, the coercive atmosphere is lacking. <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#449" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 449</a></span> (“[T]he ‘principal psychological factor contributing to a successful interrogation is privacy—being alone with the person under interrogation’”); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 445</a></span>. There is no empirical basis for the assumption that a suspect speaking to those whom he assumes are not officers will feel compelled to speak by the fear <page-number citation-index="1" label="297">*297</page-number>of reprisal for remaining silent or in the hope of more lenient treatment should he confess.</p>
<p id="b339-5">It is the premise of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that the danger of coercion results from the interaction of custody and official interrogation. We reject the argument that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are required whenever a suspect is in custody in a technical sense and converses with someone who happens to be a government agent. Questioning by captors, who appear to control the suspect’s fate, may create mutually reinforcing pressures that the Court has assumed will weaken the suspect’s will, but where a suspect does not know that he is conversing with a government agent, these pressures do not exist. The state court here mistakenly assumed that because the suspect was in custody, no undercover questioning could take place. When the suspect has no reason to think that the listeners have official power over him, it should not be assumed that his words are motivated by the reaction he expects from his listeners. “[W]hen the agent carries neither badge nor gun and wears not ‘police blue,’ but the same prison gray” as the suspect, there is no <em>“interplay </em>between police interrogation and police custody.” Kamisar, <em>Brewer v. Williams, Massiah </em>and <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>: </em>What is “Interrogation”? When Does it Matter?, 67 Geo. L. J. 1, 67, 63 (1978).</p>
<p id="b339-6"><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>forbids coercion, not mere strategic deception by taking advantage of a suspect’s misplaced trust in one he supposes to be a fellow prisoner. As we recognized in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>: </em>“Confessions remain a proper element in law enforcement. Any statement given freely and voluntarily without any compelling influences is, of course, admissible in evidence.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>. Ploys to mislead a suspect or lull him into a false sense of security that do not rise to the level of compulsion or coercion to speak are not within <em>Miranda’s </em>concerns. Cf. <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495-496</a></span> (1977) <em>(per curiam); Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412</a></span> (1986) (where police fail to inform suspect of attorney’s efforts to reach him, <page-number citation-index="1" label="298">*298</page-number>neither <em>Miranda </em>nor the Fifth Amendment requires suppression of prearraignment confession after voluntary waiver).</p>
<p id="b340-5"><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was not meant to protect suspects from boasting about their criminal activities in front of persons whom they believe to be their cellmates. This case is illustrative. Respondent had no reason to feel that undercover agent Parisi had any legal authority to force him to answer questions or that Parisi could affect respondent’s future treatment. Respondent viewed the cellmate-agent as an equal and showed no hint of being intimidated by the atmosphere of the jail. In recounting the details of the Stephenson murder, respondent was motivated solely by the desire to impress his fellow inmates. He spoke at his own peril.</p>
<p id="b340-6">The tactic employed here to elicit a voluntary confession from a suspect does not violate the Self-Incrimination Clause. We held in <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293</a></span> (1966), that placing an undercover agent near a suspect in order to gather incriminating information was permissible under the Fifth Amendment. In <em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span>, </em>while petitioner Hoffa was on trial, he met often with one Partin, who, unbeknownst to Hoffa, was cooperating with law enforcement officials. Partin reported to officials that Hoffa had divulged his attempts to bribe jury members. We approved using Hoffa’s statements at his subsequent trial for jury tampering, on the rationale that “no claim ha[d] been or could [have been] made that [Hoffa’s] incriminating statements were the product of any sort of coercion, legal or factual.” <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#304" aria-description="Citation for case: Hoffa v. United States"><em>Id., </em>at 304</a></span>. In addition, we found that the fact that Partin had fooled Hoffa into thinking that Partin was a sympathetic colleague did not affect the volun-tariness of the statements. <em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Ibid.</a></span> </em>Cf. <em>Oregon </em>v. <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason"><em>Mathiason, supra, </em>at 495-496</a></span> (officer’s falsely telling suspect that suspect’s fingerprints had been found at crime scene did not render interview “custodial” under <em>Miranda); Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969); <em>Procunier </em>v. <em>Atchley, </em><span class="citation" data-id="108231"><a href="/opinion/108231/procunier-v-atchley/#453" aria-description="Citation for case: Procunier v. Atchley">400 U. S. 446, 453-454</a></span> (1971). The only difference between this case and <em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span> </em>is that the suspect here was incarcerated, but <page-number citation-index="1" label="299">*299</page-number>detention, whether or not for the crime in question, does not warrant a presumption that the use of an undercover agent to speak with an incarcerated suspect makes any confession thus obtained involuntary.</p>
<p id="b341-5">Our decision in <em>Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968), is distinguishable. In <em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span>, </em>an inmate in a state prison was interviewed by an Internal Revenue Service agent about possible tax violations. No <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning was given before questioning. The Court held that the suspect’s incriminating statements were not admissible at his subsequent trial on tax fraud charges. The suspect in <em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span> </em>was aware that the agent was a Government official, investigating the possibility of noncompliance with the tax laws. The case before us now is different. Where the suspect does not know that he is speaking to a government agent there is no reason to assume the possibility that the suspect might feel coerced. (The bare fact of custody may not in every instance require a warning even when the suspect is aware that he is speaking to an official, but we do not have occasion to explore that issue here.)</p>
<p id="b341-6">This Court’s Sixth Amendment decisions in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">447 U. S. 264</a></span> (1980), and <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159</a></span> (1985), also do not avail respondent. We held in those cases that the government may not use an undercover agent to circumvent the Sixth Amendment right to counsel once a suspect has been charged with the crime. After charges have been filed, the Sixth Amendment prevents the government from interfering with the accused’s right to counsel. <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton"><em>Moulton, supra, </em>at 176</a></span>. In the instant case no charges had been filed on the subject of the interrogation, and our Sixth Amendment precedents are not applicable.</p>
<p id="b341-7">Respondent can seek no help from his argument that a bright-line rule for the application of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is desirable. Law enforcement officers will have little difficulty putting into practice our holding that undercover agents need not</p>
<p id="AIST"><page-number citation-index="1" label="300">*300</page-number>give <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to incarcerated suspects. The use of undercover agents is a recognized law enforcement technique, often employed in the prison context to detect violence against correctional officials or inmates, as well as for the purposes served here. The interests protected by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>are not implicated in these cases, and the warnings are not required to safeguard the constitutional rights of inmates who make voluntary statements to undercover agents.</p>
<p id="b342-5">We hold that an undercover law enforcement officer posing as a fellow inmate need not give <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to an incarcerated suspect before asking questions that may elicit an incriminating response. The statements at issue in this case were voluntary, and there is no federal obstacle to their admissibility at trial. We now reverse and remand for proceedings not inconsistent with our opinion.</p>
<p id="b342-6">
<em>It is so ordered.</em>
</p>
</opinion>
```

---
