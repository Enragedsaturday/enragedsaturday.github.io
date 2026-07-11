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

## GROUP: _overhaul2/lake/cases/Chimel v. California.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Chimel v. California"
type: case
citation: "395 U.S. 752 (1969)"
parallel_cite: "89 S. Ct. 2034; 23 L. Ed. 2d 685"
neutral_cite: 1969 U.S. LEXIS 1166
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-06-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chimel v. California
  varies_by_point: false
  scope_note: "Good law and the foundational SITA rule; Gant (relying on Chimel's reaching-distance rationale) cabined the broad Belton reading of vehicle searches. Chimel's core is undisturbed."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107979/chimel-v-california/"
  cluster_id: 107979
  opinion_id: 9841975
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Anchor"
related: ["[[Arizona v. Gant]]", "[[New York v. Belton]]", "[[Riley v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "immediate-control", "warrantless-search"]
holding: "Foundational scope of search incident to arrest: the arrestee's person and the area 'within his immediate control' — meaning the area…"
lake:
  record_id: Chimel v. California
  status: verified
  projected_at: 2026-07-09
---

# Chimel v. California

*395 U.S. 752 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers arrested Chimel in his home on a burglary warrant, then — over his objection and without a search warrant — searched the entire three-bedroom house, including drawers, directing his wife to open them so they could view the contents. Coins and other items seized in the search were admitted at his burglary trial.

## Issue
Whether, incident to a lawful arrest, officers may search the arrestee's entire home without a warrant.

## Rule
No; the [[Search Incident to Arrest|search incident to arrest]] is limited to the arrestee's person and the area within his immediate reach. "There is ample justification, therefore, for a search of the arrestee's person and the area 'within his immediate control' — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence." — 395 U.S. 752, 763. ^pin-763

"There is no comparable justification, however, for routinely searching any room other than that in which an arrest occurs — or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself." — [*Id.*](https://www.courtlistener.com/opinion/107979/chimel-v-california/#:~:text=There%20is%20no%20comparable%20justification%2C) ^pin-763a

## Application
The search of Chimel's entire house — every room, drawers opened on command — reached far beyond his person and the area from which he could have grabbed a weapon or destroyed evidence while under arrest. Because nothing justified that house-wide search as incident to the arrest, and the officers had no search warrant, the seizure of items throughout the home was unconstitutional.

## Conclusion
The warrantless, house-wide [[Search Incident to Arrest|search incident to arrest]] was unreasonable; the conviction was reversed. *Chimel* fixed the officer-safety/evidence-preservation rationale and the "immediate control" scope of [[Search Incident to Arrest|search incident to arrest]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Chimel* itself. [[Arizona v. Gant]] **relied on** *Chimel*'s reaching-distance rationale to **narrow** the broad reading of [[New York v. Belton]] for vehicle searches; *Chimel*'s core person-and-immediate-control rule remains controlling.

## Appears on
- [[SIA Persons]] — *Key — Anchor*

## Sources
- *Chimel v. California*, 395 U.S. 752 (1969) — https://www.courtlistener.com/opinion/107979/chimel-v-california/ — pinpoint: 763.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "70706bb24f3f4dfb", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Chimel v. California"}, "payload": {"all": [{"cite": "395 U.S. 752", "page": "752", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "395"}, {"cite": "89 S. Ct. 2034", "page": "2034", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "23 L. Ed. 2d 685", "page": "685", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "23"}, {"cite": "1969 U.S. LEXIS 1166", "page": "1166", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1969"}], "display": "395 U.S. 752", "official": {"cite": "395 U.S. 752", "page": "752", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "395"}, "official_selection_present": true, "record_id": "Chimel v. California"}}
{"assertion_id": "693bfab0f8e5b5d1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-763", "record_id": "Chimel v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-763", "pinpoint_status": "slip-only", "quote": "--- # Chimel v. California *395 U.S. 752 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Chimel in his home on a burglary warrant, then — over his objection and without a search warrant — searched the entire three-bedroom house, including drawers, directing his wife to open them so they could view the contents. Coins and other items seized in the search were admitted at his burglary trial. ## Issue Whether, incident to a lawful arrest, officers may search the arrestee's entire home without a warrant. ## Rule No; the search incident to arrest is limited to the arrestee's person and the area within his immediate reach.", "quote_fidelity": "mismatch", "record_id": "Chimel v. California", "star_marker": null}}
{"assertion_id": "f83b5d994fcb2f15", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-763a", "record_id": "Chimel v. California"}, "payload": {"fragment": "#:~:text=There%20is%20no%20comparable%20justification%2C", "page": null, "pin_id": "pin-763a", "pinpoint_status": "star-verified", "quote": "There is no comparable justification, however, for routinely searching any room other than that in which an arrest occurs — or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself.", "quote_fidelity": "matched", "record_id": "Chimel v. California", "star_marker": "763"}}
{"assertion_id": "64bc08b2b64c7f4b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chimel v. California"}, "payload": {"as_of_content": "1969-06-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Chimel v. California", "scope_note": "Good law and the foundational SITA rule; Gant (relying on Chimel's reaching-distance rationale) cabined the broad Belton reading of vehicle searches. Chimel's core is undisturbed.", "varies_by_point": false}}
```

### lake record — Chimel v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chimel v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chimel v. California",
    "case_name_short": "Chimel",
    "case_name_full": "Chimel v. California",
    "input_case_name": "Chimel v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-06-23",
    "year": 1969,
    "docket": null,
    "cluster_id": 107979,
    "lead_opinion_id": 9841975,
    "sibling_ids": [
      107979,
      9841975,
      9841976,
      9841977
    ],
    "absolute_url": "/opinion/107979/chimel-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8974742,
        "score": 20,
        "case_name": "Chimel v. California"
      },
      {
        "cluster_id": 8973648,
        "score": 20,
        "case_name": "Chimel v. California"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "395 U.S. 752",
      "volume": "395",
      "reporter": "U.S.",
      "page": "752",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 2034",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "2034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 L. Ed. 2d 685",
        "volume": "23",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 1166",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1166",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "395 U.S. 752",
        "volume": "395",
        "reporter": "U.S.",
        "page": "752",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 2034",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "2034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 L. Ed. 2d 685",
        "volume": "23",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 1166",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1166",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "395 U.S. 752",
    "official_selection": {
      "court_class": "scotus",
      "selected": "395 U.S. 752",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-763",
      "page": null,
      "quote": "--- # Chimel v. California *395 U.S. 752 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Chimel in his home on a burglary warrant, then \u2014 over his objection and without a search warrant \u2014 searched the entire three-bedroom house, including drawers, directing his wife to open them so they could view the contents. Coins and other items seized in the search were admitted at his burglary trial. ## Issue Whether, incident to a lawful arrest, officers may search the arrestee's entire home without a warrant. ## Rule No; the search incident to arrest is limited to the arrestee's person and the area within his immediate reach.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-763a",
      "page": null,
      "quote": "There is no comparable justification, however, for routinely searching any room other than that in which an arrest occurs \u2014 or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself.",
      "star_marker": "763",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28275,
      "fragment": "#:~:text=There%20is%20no%20comparable%20justification%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chimel v. California",
    "varies_by_point": false,
    "scope_note": "Good law and the foundational SITA rule; Gant (relying on Chimel's reaching-distance rationale) cabined the broad Belton reading of vehicle searches. Chimel's core is undisturbed.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario-Santiago",
          "cluster_id": 4666565,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane1_negative"
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
        "journal_ref": "Chimel v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Anderson v. State of Indiana",
          "cluster_id": 4327181,
          "cite": [
            "64 N.E.3d 903",
            "2016 Ind. App. LEXIS 432",
            "2016 WL 7078344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane1_negative"
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
        "journal_ref": "Chimel v. California:lane1_negative"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanley v. Illinois",
          "cluster_id": 108497,
          "cite": [
            "31 L. Ed. 2d 551",
            "92 S. Ct. 1208",
            "405 U.S. 645",
            "1972 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQxODQzMjAwMDAwJnM9MzEzMzE3NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107979+OR+9841975+OR+9841976+OR+9841977%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjE2JnM9MTEwOTc2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107979+OR+9841975+OR+9841976+OR+9841977%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977)",
        "reviewed": 58,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 58,
        "triage_read": 0,
        "triage_snippet_classified": 58
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977)",
    "indexed_citing_opinions": 4230,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107979,
        "count": 3919,
        "count_source": "search"
      },
      {
        "opinion_id": 9841975,
        "count": 423,
        "count_source": "search"
      },
      {
        "opinion_id": 9841976,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9841977,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6512,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chimel-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMDk0NDEmcz0xMDMzMDIyMCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107979+OR+9841975+OR+9841976+OR+9841977%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9841976,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841976,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 237181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 1272352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 1481331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 1893679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 88122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 103705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 226125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 229424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 237181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 244962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 246794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 1272352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 1481331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 1893679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 9416821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 9419320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 9841975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 88122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 103705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 226125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 229424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 244962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 246794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 9416821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 9419320,
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
    "date_created": "2026-07-05T00:04:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:05:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:05:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:07:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:05:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chimel v. California

```
<opinion type="majority">
<author id="b827-8">Mb. Justice Stewakt</author>
<p id="AyX">delivered the opinion of the Court.</p>
<p id="b827-9">This case raises basic questions concerning the permissible scope under the Fourth Amendment of a search incident to a lawful arrest.</p>
<p id="b827-10">The relevant facts are essentially undisputed. Late in the afternoon of September 13, 1965, three police officers arrived at the Santa Ana, California, home of the petitioner with a warrant authorizing his arrest for the burglary of a coin shop. The officers knocked on the door, identified themselves to the petitioner’s wife, and asked if they might come inside. She ushered them into the house, where they waited 10 or 15 minutes until the petitioner returned home from work. When the petitioner entered the house, one of the officers handed him the arrest warrant and asked for permission to “look around.” The petitioner objected, but was advised that <page-number citation-index="1" label="754">*754</page-number>“on the basis of the lawful arrest,” the officers would nonetheless conduct a search. No search warrant had been issued.</p>
<p id="b828-5">Accompanied by the petitioner’s wife, the officers then looked through the entire three-bedroom house, including the attic, the garage, and a small workshop. In some rooms the search was relatively cursory. In the master bedroom and sewing room, however, the officers directed the petitioner’s wife to open drawers and “to physically move contents of the drawers from side to side so that [they] might view any items that would have come from [the] burglary.” After completing the search, they seized numerous items — primarily coins, but also several medals, tokens, and a few other objects. The entire search took between 45 minutes and an hour.</p>
<p id="b828-6">At the petitioner’s subsequent state trial on two charges of burglary, the items taken from his house were admitted into evidence against him, over his objection that they had been unconstitutionally seized. He was convicted, and the judgments of conviction were affirmed by both the California Court of Appeal, <span class="citation no-link">61 Cal. Rptr. 714</span>, and the California Supreme Court, <span class="citation" data-id="9848415"><a href="/opinion/1272352/people-v-chimel/" aria-description="Citation for case: People v. Chimel">68 Cal. 2d 436</a></span>, <span class="citation" data-id="9848415"><a href="/opinion/1272352/people-v-chimel/" aria-description="Citation for case: People v. Chimel">439 P. 2d 333</a></span>. Both courts accepted the petitioner’s contention that the arrest warrant was invalid because the supporting affidavit was set out in conclusory terms,<footnotemark>1</footnotemark> but held that since the arresting officers had procured the warrant “in good faith,” and since in any event they had had sufficient information to constitute probable cause for the petitioner’s arrest, that arrest had been lawful. From this conclusion the appellate courts went on to hold that the search of the petitioner’s home <page-number citation-index="1" label="755">*755</page-number>had been justified, despite the absence of a search warrant, on the ground that it had been incident to a valid arrest. We granted certiorari in order to consider the petitioner’s substantial constitutional claims. <span class="citation multiple-matches"><a href="/c/U.%20S./393/958/">393 U. S. 958</a></span>.</p>
<p id="b829-5">Without deciding the question, we proceed on the hypothesis that the California courts were correct in holding that the arrest of the petitioner was valid under the Constitution. This brings us directly to the question whether the warrantless search of the petitioner’s entire house can be constitutionally justified as incident to that arrest. The decisions of this Court bearing upon that question have been far from consistent, as even the most cursory review makes evident.</p>
<p id="b829-6">Approval of a warrantless search incident to a lawful arrest seems first to have been articulated by the Court in 1914 as dictum in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, in which the Court stated:</p>
<blockquote id="b829-7">“What then is the present case? Before answering that inquiry specifically, it may be well by a process of exclusion to state what it is not. It is not an assertion of the right on the part of the Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime.” <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States"><em>Id., </em>at 392</a></span>.</blockquote>
<p id="b829-8">That statement made no reference to any right to search the <em>place </em>where an arrest occurs, but was limited to a right to search the “person.” Eleven years later the case of <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, brought the following embellishment of the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>statement:</p>
<blockquote id="AmR">“When a man is legally arrested for an offense, whatever is found upon his person <em>or in his control </em>which it is unlawful for him to have and which may be used to prove the offense may be seized and held <page-number citation-index="1" label="756">*756</page-number>as evidence in the prosecution.” <em>Id., </em>at 158. (Emphasis added.)</blockquote>
<p id="b830-5">Still, that assertion too was far from a claim that the “place” where one is arrested may be searched so long as the arrest is valid. Without explanation, however, the principle emerged in expanded form a few months later in <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> — although still by way of dictum:</p>
<blockquote id="b830-6">“The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted. See <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>; <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>.” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S., at 30</a></span>.</blockquote>
<p id="b830-7">And in <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>, two years later, the dictum of <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>appeared to be the foundation of the Court’s decision. In that case federal agents had secured a search, warrant authorizing the seizure of liquor and certain articles used in its manufacture. When they arrived at the premises to be searched, they saw “that the place was used for retailing and drinking intoxicating liquors.” <em>Id., </em>at 194. They proceeded to arrest the person in charge and to execute the warrant. In searching a closet for the items listed in the warrant they came across an incriminating ledger, concededly not covered by the warrant, which they also seized. The Court upheld the seizure of the ledger by holding that since the agents had made a lawful arrest, “[t]hey had a right without a warrant contemporaneously to search the place in order to find and seize the things used to carry on the criminal enterprise.” <em>Id., </em>at 199.</p>
<p id="b831-4"><page-number citation-index="1" label="757">*757</page-number>That the <em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span> </em>opinion did not mean all that it seemed to say became evident, however, a few years later in <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>, and <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>. In each of those cases the opinion of the Court was written by Mr. Justice Butler, the author of the opinion in <em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span>. </em>In <em>Go-Bart, </em>agents had searched the office of persons whom they had lawfully arrested,<footnotemark>2</footnotemark> and had taken several papers from a desk, a safe, and other parts of the office. The Court noted that no crime had been committed in the agents’ presence, and that although the agent in charge “had an abundance of information and time to swear out a valid [search] warrant, he failed to do so.” <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 358</a></span>. In holding the search and seizure unlawful, the Court stated:</p>
<blockquote id="b831-5">“Plainly the case before us is essentially different from <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>. There, officers executing a valid search warrant for intoxicating liquors found and arrested one Birdsall who in pursuance of a conspiracy was actually engaged in running a saloon. As an incident to the arrest they seized a ledger in a closet where the liquor or some of it was kept and some bills beside the cash register. These things were visible and accessible and in the offender’s immediate custody. There was no threat of force or general search or rummaging of the place.” <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 358</a></span>.</blockquote>
<p id="b831-6">This limited characterization of <em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span> </em>was reiterated in <em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span>, </em>a case in which the Court held unlawful a search of desk drawers and a cabinet despite the fact that the search had accompanied a lawful arrest. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S., at 465</a></span>.</p>
<p id="b831-7">The limiting views expressed in <em>Go-Bart </em>and <em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span> </em>were thrown to the winds, however, in <em>Harris </em>v. <em>United </em><page-number citation-index="1" label="758">*758</page-number><em>States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, decided in 1947. In that case, officers had obtained a warrant for Harris’ arrest on the basis of his alleged involvement with the cashing and interstate transportation of a forged check. He was arrested in the living room of his four-room apartment, and in an attempt to recover two canceled checks thought to have been used in effecting the forgery, the officers undertook a thorough search of the entire apartment. Inside a desk drawer they found a sealed envelope marked “George Harris, personal papers.” The envelope, which was then torn open, was found to contain altered Selective Service documents, and those documents were used to secure Harris’ conviction for violating the Selective Training and Service Act of 1940. The Court rejected Harris’ Fourth Amendment claim, sustaining the search as “incident to arrest.” <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#151" aria-description="Citation for case: Harris v. United States"><em>Id., </em>at 151</a></span>.</p>
<p id="b832-5">Only a year after <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>, </em>however, the pendulum swung again. In <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>, agents raided the site of an illicit distillery, saw one of several conspirators operating the still, and arrested him, contemporaneously “seiz[ing] the illicit distillery.” <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#702" aria-description="Citation for case: Trupiano v. United States"><em>Id., </em>at 702</a></span>. The Court held that the arrest and others made subsequently had been valid, but that the unexplained failure of the agents to procure a search warrant — in spite of the fact that they had had more than enough time before the raid to do so — rendered the search unlawful. The opinion stated:</p>
<blockquote id="b832-6">“It is a cardinal rule that, in seizing goods and articles, law enforcement agents must secure and use search warrants wherever reasonably practicable. . . . This rule rests upon the desirability of having magistrates rather than police officers determine when searches and seizures are permissible and what limitations should be placed upon such activities. ... To provide the necessary security against unreasonable intrusions upon the private lives of <page-number citation-index="1" label="759">*759</page-number>individuals, the framers of the Fourth Amendment required adherence to judicial processes wherever possible. And subsequent history has confirmed the wisdom of that requirement.</blockquote>
<blockquote id="b833-5">“A search or seizure without a warrant as an incident to a lawful arrest has always been considered to be a strictly limited right. It grows out of the inherent necessities of the situation at the time of the arrest. But there must be something more in the way of necessity than merely a lawful arrest.” <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States"><em>Id., </em>at 705, 708</a></span>.</blockquote>
<p id="b833-6">In 1950, two years after Trupiano,<footnotemark>3</footnotemark> came <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, the decision upon which California primarily relies in the case now before us. In <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>, </em>federal authorities had been informed that the defendant was dealing in stamps bearing forged overprints. On the basis of that information they secured a warrant for his arrest, which they executed at his one-room business office. At the time of the arrest, the officers “searched the desk, safe, and file cabinets in the office for about an hour and a half,” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#59" aria-description="Citation for case: United States v. Rabinowitz"><em>id., </em>at 59</a></span>, and seized 573 stamps with forged overprints. The stamps were admitted into evidence at the defendant’s trial, and this Court affirmed his conviction, rejecting the contention that the warrantless search had been unlawful. The Court held that the search in its entirety fell within the principle giving law enforcement authorities “[t]he right 'to search the place where the arrest is made in order to find and seize things connected with the crime ....’” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#61" aria-description="Citation for case: United States v. Rabinowitz"><em>Id., </em>at 61</a></span>. <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>was regarded as “ample authority” for that conclusion. <em>Id., </em>at 63. The opinion rejected the rule of <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>that “in seizing goods and articles, law enforcement agents must secure and use search war<page-number citation-index="1" label="760">*760</page-number>rants wherever reasonably practicable.” The test, said the Court, “is not whether it is reasonable to procure a search warrant, but whether the search was reasonable.” <em>Id., </em>at 66.</p>
<p id="b834-5"><em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>has come to stand for the proposition, <em>inter alia, </em>that a warrantless search “incident to a lawful arrest” may generally extend to the area that is considered to be in the “possession” or under the “control” of the person arrested.<footnotemark>4</footnotemark> And it was on the basis of that proposition that the California courts upheld the search of the petitioner’s entire house in this case. That doctrine, however, at least in the broad sense in which it was applied by the California courts in this case, can withstand neither historical nor rational analysis.</p>
<p id="b834-6">Even limited to its own facts, the <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>decision was, as we have seen, hardly founded on an unimpeachable line of authority. As Mr. Justice Frankfurter commented in dissent in that case, the “hint” contained in <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>was, without persuasive justification, “loosely turned into dictum and finally elevated to a decision.” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#76" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 76</a></span>. And the approach taken in cases such as <em>Go-Bart, Lefkowitz, </em>and <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>was essentially disregarded by the <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>Court.</p>
<p id="b834-7">Nor is the rationale by which the State seeks here to sustain the search of the petitioner’s house supported by a reasoned view of the background and purpose of the Fourth Amendment. Mr. Justice Frankfurter wisely pointed out in his <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>dissent that the Amendment’s proscription of “unreasonable searches and sei<page-number citation-index="1" label="761">*761</page-number>zures” must be read in light of “the history that gave rise to the words” — a history of “abuses so deeply felt by the Colonies as to be one of the potent causes of the Revolution . . . .” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#69" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 69</a></span>. The Amendment was in large part a reaction to the general warrants and war-rantless searches that had so alienated the colonists and had helped speed the movement for independence.<footnotemark>5</footnotemark> In the scheme of the Amendment, therefore, the requirement that “no Warrants shall issue, but upon probable cause,” plays a crucial part. As the Court put it in <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>:</p>
<blockquote id="b835-5">“We are not dealing with formalities. The presence of a search warrant serves a high function. Absent some grave emergency, the Fourth Amendment has interposed a magistrate between the citizen and the police. This was done not to shield criminals nor to make the home a safe haven for illegal activities. It was done so that an objective mind might weigh the need to invade that privacy in order to enforce the law. The right of privacy was deemed too precious to entrust to the discretion of those whose job is the detection of crime and the arrest of criminals. . . . And so the Constitution requires a magistrate to pass on the desires of the police before they violate the privacy of the home. We cannot be true to that constitutional requirement and excuse the absence of a search warrant without a showing by those who seek exemption from the constitutional mandate that the exigencies of the situation made that course imperative.” <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States"><em>Id., </em>at 455-456</a></span>.</blockquote>
<p id="ArJ"><page-number citation-index="1" label="762">*762</page-number>Even in the <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>case the Court relied upon the rule that “[b]elief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause.” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S., at 33</a></span>. Clearly, the general requirement that a search warrant be obtained is not lightly to be dispensed with, and “the burden is on those seeking [an] exemption [from the requirement] to show the need for it . . . .” <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>.</p>
<p id="b836-5">Only last Term in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, we emphasized that “the police must, whenever practicable, obtain advance judicial approval of searches and seizures through the warrant procedure,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 20</a></span>,<footnotemark>6</footnotemark> and that “[t]he scope of [a] search must be ‘strictly tied to and justified by’ the circumstances which rendered its initiation permissible.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 19</a></span>. The search undertaken by the officer in that “stop and frisk” case was sustained under that test, because it was no more than a “protective . . . search for weapons.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 29</a></span>. But in a companion case, <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span>, we applied the same standard to another set of facts and reached a contrary result, holding that a policeman’s action in thrusting his hand into a suspect’s pocket had been neither motivated by nor limited to the objective of protection.<footnotemark>7</footnotemark> Rather, the search had been made in order to find narcotics, which were in fact found.</p>
<p id="b836-6">A similar analysis underlies the “search incident to arrest” principle, and marks its proper extent. When an <page-number citation-index="1" label="763">*763</page-number>arrest is made, it is reasonable for the arresting officer to search the person arrested in order to remove any weapons that the latter might seek to use in order to resist arrest or effect his escape. Otherwise, the officer’s safety might well be endangered, and the arrest itself frustrated. In addition, it is entirely reasonable for the arresting officer to search for and seize any evidence on the arrestee’s person in order to prevent its concealment or destruction. And the area into which an arrestee might reach in order to grab a weapon or evidentiary items must, of course, be governed by a like rule. A gun on a table or in a drawer in front of one who is arrested can be as dangerous to the arresting officer as one concealed in the clothing of the person arrested. There is ample justification, therefore, for a search of the arrestee’s person and the area “within his immediate control” — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.</p>
<p id="b837-5">There is no comparable justification, however, for routinely searching any room other than that in which an arrest occurs — or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself. Such searches, in the absence of well-recognized exceptions, may be made only under the authority of a search warrant.<footnotemark>8</footnotemark> The “adherence to judicial processes” mandated by the Fourth Amendment requires no less.</p>
<p id="b837-6">This is the principle that underlay our decision in <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>. In that case three men had been arrested in a parked car, which had later been towed to a garage and searched by police. We held the search to have been unlawful under the Fourth Amendment, despite the contention that it had <page-number citation-index="1" label="764">*764</page-number>been incidental to a valid arrest. Our reasoning was straightforward:</p>
<blockquote id="b838-6">“The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime— things which might easily happen where the weapon or evidence is on the accused’s person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest.” <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States"><em>Id., </em>at 367</a></span>.<footnotemark>9</footnotemark></blockquote>
<p id="b838-7">The same basic principle was reflected in our opinion last Term in <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Sibron</a></span>. </em>That opinion dealt with <em>Peters </em>v. <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">New York</a></span>, </em>No. 74, as well as with Sibron’s case, and <em>Peters </em>involved a search that we upheld as incident to a proper arrest. We sustained the search, however, only because its scope had been “reasonably limited” by the “need to seize weapons” and “to prevent the destruction of evidence,” to which <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>had referred. We emphasized that the arresting officer “did not engage in an unrestrained and thoroughgoing examination of Peters and his personal effects. He seized him to cut short his flight, and he searched him primarily for weapons.” 392 U. S., at 67.</p>
<p id="b838-8">It is argued in the present case that it is “reasonable” to search a man’s house when he is arrested in it. But that argument is founded on little more than a subjective view regarding the acceptability of certain sorts of police <page-number citation-index="1" label="765">*765</page-number>conduct, and not on considerations relevant to Fourth Amendment interests. Under such an unconfined analysis, Fourth Amendment protection in this area would approach the evaporation point. It is not easy to explain why, for instance, it is less subjectively “reasonable” to search a man’s house when he is arrested on his front lawn — or just down the street — than it is when he happens to be in the house at the time of arrest.<footnotemark>10</footnotemark> As Mr. Justice Frankfurter put it:</p>
<blockquote id="b839-5">“To say that the search must be reasonable is to require some criterion of reason. It is no guide at all either for a jury or for district judges or the police to say that an 'unreasonable search’ is forbidden— that the search must be reasonable. What is the test of reason which makes a search reasonable? The test is the reason underlying and expressed by the Fourth Amendment: the history and the experience which it embodies and the safeguards afforded by it against the evils to which it was a response.” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#83" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 83</a></span> (dissenting opinion).</blockquote>
<p id="b839-6">Thus, although “[t]he recurring questions of the reasonableness of searches” depend upon “the facts and circumstances — -the total atmosphere of the case,” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz"><em>id., </em>at 63, 66</a></span> (opinion of the Court), those facts and circumstances must be viewed in the light of established Fourth Amendment principles.</p>
<p id="b840-5"><page-number citation-index="1" label="766">*766</page-number>It would be possible, of course, to draw a line between <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>on the one hand, and this case on the other. For <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>involved a single room, and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>a four-room apartment, while in the case before us an entire house was searched. But such a distinction would be highly artificial. The rationale that allowed the searches and seizures in <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>would allow the searches and seizures in this case. No consideration relevant to the Fourth Amendment suggests any point of rational limitation, once the search is allowed to go beyond the area from which the person arrested might obtain weapons or evidentiary items.<footnotemark>11</footnotemark> The only reasoned distinction is one between a search of the person arrested and the area within his reach on the one hand, and more extensive searches on the other.<footnotemark>12</footnotemark></p>
<p id="b841-4"><page-number citation-index="1" label="767">*767</page-number>The petitioner correctly points out that one result of decisions such as <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>is to give law enforcement officials the opportunity to engage in searches not justified by probable cause, by the simple expedient of arranging to arrest suspects at home rather than elsewhere. We do not suggest that the petitioner is necessarily correct in his assertion that such a strategy was utilized here,<footnotemark>13</footnotemark> but the fact remains that had he been arrested earlier in the day, at his place of employment rather than at home, no search of his house could have been made without a search warrant. In any event, even apart from the possibility of such police tactics, the general point so forcefully made by Judge Learned Hand in <em>United States </em>v. <em>Kirschenblatt, </em><span class="citation" data-id="1481331"><a href="/opinion/1481331/united-states-v-kirschenblatt/" aria-description="Citation for case: United States v. Kirschenblatt">16 F. 2d 202</a></span>, remains:</p>
<blockquote id="b841-5">“After arresting a man in his house, to rummage at will among his papers in search of whatever will convict him, appears to us to be indistinguishable from what might be done under a general warrant; indeed, the warrant would give more protection, for presumably it must be issued by a magistrate. True, by hypothesis the power would not exist, if the supposed offender were not found on the prem<page-number citation-index="1" label="768">*768</page-number>ises; but it is small consolation to know that one’s papers are safe only so long as one is not at home.” <span class="citation" data-id="1481331"><a href="/opinion/1481331/united-states-v-kirschenblatt/#203" aria-description="Citation for case: United States v. Kirschenblatt"><em>Id., </em>at 203</a></span>.</blockquote>
<p id="b842-4"><em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>have been the subject of critical commentary for many years,<footnotemark>14</footnotemark> and have been relied upon less and less in our own decisions.<footnotemark>15</footnotemark> It is time, for the reasons we have stated, to hold that on their own facts, and insofar as the principles they stand for are inconsistent with those that we have endorsed today, they are no longer to be followed.</p>
<p id="b842-5">Application of sound Fourth Amendment principles to the facts of this case produces a clear result. The search here went far beyond the petitioner’s person and the area from within which he might have obtained either a weapon or something that could have been used as evidence against him. There was no constitutional justification, in the absence of a search warrant, for extending the search beyond that area. The scope of the search was, therefore, “unreasonable” under the Fourth and Fourteenth Amendments, and the petitioner’s conviction cannot stand.<footnotemark>16</footnotemark> <em>Reversed.</em></p>
<footnote label="1">
<p id="b828-7"> The affidavit supporting the warrant is set out in the opinion of the Court of Appeal, 61 Cal. Rptr., at 715-716, n. 1, and the State does not challenge its insufficiency under the principles of <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>, and <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b831-8"> The Court assumed that the arrests were lawful. <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#356" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 356</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b833-7"> See also <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b834-8"> Decisions of this Court since <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>have applied the abstract doctrine of that case to various factual situations with divergent results. Compare <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42</a></span>; <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span>; and <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>, with <em>Kremen </em>v. <em>United States, </em><span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span> <em>(per curiam). </em>Cf. <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>; <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b835-6"> See generally <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-625</a></span>; <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#389" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 389-391</a></span>; <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#603" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 603-605</a></span> (dissenting opinion); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#157" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 157-162</a></span> (dissenting opinion); <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-482</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b836-7"> See also <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 728</a></span>; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 356-358</a></span>; <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#299" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 299</a></span>; <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b836-8"> Our <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Sibron</a></span> </em>opinion dealt with two cases. We refer here to No. 63, involving the appellant Sibron. See <em>infra, </em>at 764.</p>
</footnote>
<footnote label="8">
<p id="b837-7"> See <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357-358</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b838-9"> Our holding today is of course entirely consistent with the recognized principle that, assuming the existence of probable cause, automobiles and other vehicles may be searched without warrants “where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.” <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span>; see <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b839-7"> Some courts have carried the <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>approach to just such lengths. See, <em>e. g., Clifton </em>v. <em>United States, </em><span class="citation" data-id="237181"><a href="/opinion/237181/robert-francis-clifton-v-united-states/" aria-description="Citation for case: Robert Francis Clifton v. United States">224 F. 2d 329</a></span> (C. A. 4th Cir.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./350/894/">350 U. S. 894</a></span> (purchaser of illicit whiskey arrested in back yard of seller; search of one room of house sustained); <em>United States </em>v. <em>Jackson, </em><span class="citation" data-id="1893679"><a href="/opinion/1893679/united-states-v-jackson/" aria-description="Citation for case: United States v. Jackson">149 F. Supp. 937</a></span> (D. C. D. C.), rev’d on other grounds, 102 U. S. App. D. C. 109, <span class="citation multiple-matches"><a href="/c/F.%202d/250/772/">250 F. 2d 772</a></span> (suspect arrested half a block from his rented room; search of room upheld). But see <em>James </em>v. <em>Louisiana, </em><span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/" aria-description="Citation for case: James v. Louisiana">382 U. S. 36</a></span> <em>(per curiam).</em></p>
</footnote>
<footnote label="11">
<p id="b840-6"> Cf. Mr. Justice Jackson’s dissenting comment in <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>:</em></p>
<p id="b840-7">“The difficulty with this problem for me is that once the search is allowed to go beyond the person arrested and the objects upon him or in his immediate physical control, I see no practical limit short of that set in the opinion of the Court — and that means to me no limit at all.” <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#197" aria-description="Citation for case: Harris v. United States">331 U. S., at 197</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b840-9"> It is argued in dissent that so long as there is probable cause to search the place where an arrest occurs, a search of that place should be permitted even though no search warrant has been obtained. This position seems to be based principally on two premises: first, that once an arrest has been made, the additional invasion of privacy stemming from the accompanying search is “relatively minor”; and second, that the victim of the search may “shortly thereafter” obtain a judicial determination of whether the search was justified by probable cause. With respect to the second premise, one may initially question whether all of the States in fact provide the speedy suppression procedures the dissent assumes. More fundamentally, however, we cannot accept the view that Fourth Amendment interests are vindicated so long as “the rights of the criminal” are “protected] . . . against introduction of evidence seized without probable cause.” The Amendment is designed to prevent, not simply to redress, unlawful police action. In any event, we cannot join in characterizing the invasion <page-number citation-index="1" label="767">*767</page-number>of privacy that results from a top-to-bottom search of a man’s house as “minor.” And we can see no reason why, simply because some interference with an individual’s privacy and freedom of movement has lawfully taken place, further intrusions should automatically be allowed despite the absence of a warrant that the Fourth Amendment would otherwise require.</p>
</footnote>
<footnote label="13">
<p id="b841-7"> Although the warrant was issued at 10:39 a. m. and the arrest was not made until late in the afternoon, the State suggests that the delay is accounted for by normal police procedures and by the heavy workload of the officer in charge. In addition, that officer testified that he and his colleagues went to the petitioner’s house “to keep from approaching him at his place of business to cause him any problem there.”</p>
</footnote>
<footnote label="14">
<p id="b842-6"> See, <em>e. g., </em>J. Landynski, Search and Seizure and the Supreme Court 87-117 (1966); Way, Increasing Scope of Search Incidental to Arrest, 1959 Wash. U. L. Q. 261; Note, Scope Limitations for Searches Incident to Arrest, 78 Yale L. J. 433 (1969); Note, The Supreme Court 1966 Term, <span class="citation no-link">81 Harv. L. Rev. 69</span>, 117-122 (1967).</p>
</footnote>
<footnote label="15">
<p id="b842-7"> Cf. <em>Dyke </em>v. <em>Taylor Implement Mfg. Co., </em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#220" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216, 220</a></span>; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S., at 357-358, n. 20</a></span>; <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#299" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 299</a></span>; <em>Stoner </em>v. <em>California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#487" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 487</a></span>. But see <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#62" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 62</a></span>; <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S., at 42</a></span> (opinion of Clark, J.); cf. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span>; <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#236" aria-description="Citation for case: Abel v. United States">362 U. S., at 236-239</a></span>; <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#488" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 488</a></span>.</p>
</footnote>
<footnote label="16">
<p id="b842-8"> The State has made various subsidiary contentions, including arguments that it would have been unduly burdensome to obtain a warrant specifying the coins to be seized and that introduction of the fruits of the search was harmless error. We reject those contentions as being without merit.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/City and County of San Francisco v. Sheehan.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "City and County of San Francisco v. Sheehan"
type: case
citation: ""
parallel_cite: "575 U.S. 600; 135 S. Ct. 1765; 191 L. Ed. 2d 856; 83 U.S.L.W. 4303; 25 Fla. L. Weekly Fed. S 254"
neutral_cite: 2015 U.S. LEXIS 3200
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-05-18
docket: 13-1412
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-05-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City and County of San Francisco v. Sheehan
  varies_by_point: false
  scope_note: "Good law: QI for force against an armed, mentally ill suspect; the ADA-accommodation question was dismissed as improvidently granted (left open)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2801435/city-and-county-of-san-francisco-v-sheehan/"
  cluster_id: 2801435
  opinion_id: 2801435
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Graham v. Connor]]", "[[Plumhoff v. Rickard]]", "[[Mullenix v. Luna]]"]
aliases: ["San Francisco v. Sheehan"]
tags: ["case", "use-of-force", "qualified-immunity", "mentally-ill", "clearly-established", "ada"]
holding: "Officers who used force against an armed, mentally ill suspect after a second entry into her room were entitled to qualified immunity because they violated no clearly established Fourth Amendment right; the ADA-accommodation question was dismissed as improvidently granted."
lake:
  record_id: City and County of San Francisco v. Sheehan
  status: verified
  projected_at: 2026-07-06
---

# City and County of San Francisco v. Sheehan

*575 U.S. 600 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Teresa Sheehan, who suffered from a schizoaffective disorder, lived in a San Francisco group home. After she threatened a social worker with a knife, Sergeant Kimberly Reynolds and Officer Kathrine Holder came to take her for psychiatric evaluation. They entered her room; Sheehan grabbed a knife and threatened to kill them, so they withdrew and closed the door. Fearing she might escape or gather more weapons, they reopened the door (a "second entry") rather than waiting; when Sheehan again advanced with the knife, they used pepper spray and then shot her several times (she survived). She sued under the Americans with Disabilities Act and under § 1983 for excessive force.

## Issue
Whether the officers were entitled to [[Qualified Immunity|qualified immunity]] for the force used after re-entering Sheehan's room (and whether the ADA's accommodation requirement applies to arrests).

## Rule
The Court declined to resolve the ADA question and held the officers immune. "we dismiss the first question as improvidently granted. We decide the second question and hold that the officers are entitled to qualified immunity because they did not violate any clearly established Fourth Amendment rights." — 575 U.S. at 600. ^pin-600

Even assuming the second entry could be found unreasonable, "no precedent clearly established that there was not 'an objective need for immediate entry' here," and "[w]ithout that 'fair notice,' an officer is entitled to qualified immunity." "In sum, we hold that qualified immunity applies because these officers had no 'fair and clear warning of what the Constitution requires.'" — 135 S. Ct. at 1778. ^pin-1778

## Application
The Ninth Circuit had relied on general circuit precedent to deny immunity, but no decision clearly established that reopening the door of an armed, violent, mentally ill suspect — to keep her from escaping or arming herself further — was unlawful. That the officers may have departed from their training in handling the mentally ill did not negate immunity, because an expert's view that a confrontation could have been handled differently cannot defeat immunity where a reasonable officer could have believed the conduct justified. The ADA question, whether accommodation duties apply when officers arrest an armed and dangerous suspect, was left unresolved as improvidently granted.

## Conclusion
Reversed in part; the first (ADA) question dismissed as improvidently granted. The officers were entitled to [[Qualified Immunity|qualified immunity]] on the Fourth Amendment claim because they violated no clearly established law.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Sheehan* applies the [[Graham v. Connor]] reasonableness standard and the high-specificity qualified-immunity approach of [[Mullenix v. Luna]] and [[Plumhoff v. Rickard]] to force against a mentally ill suspect, while expressly leaving open whether the ADA requires accommodation during an arrest. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *City and County of San Francisco v. Sheehan*, 575 U.S. 600 (2015) — https://www.courtlistener.com/opinion/2801435/city-and-county-of-san-francisco-v-sheehan/ — pinpoints: 600 (U.S. Reports, opening holding); 135 S. Ct. at 1778 (parallel reporter page-label confirmed in CL for the QI conclusion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d6f8fac61ffea312", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "City and County of San Francisco v. Sheehan"}, "payload": {"all": [{"cite": "575 U.S. 600", "page": "600", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "575"}, {"cite": "135 S. Ct. 1765", "page": "1765", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "135"}, {"cite": "191 L. Ed. 2d 856", "page": "856", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "191"}, {"cite": "2015 U.S. LEXIS 3200", "page": "3200", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2015"}, {"cite": "83 U.S.L.W. 4303", "page": "4303", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "83"}, {"cite": "25 Fla. L. Weekly Fed. S 254", "page": "254", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "25"}], "display": null, "official": null, "official_selection_present": false, "record_id": "City and County of San Francisco v. Sheehan"}}
{"assertion_id": "4e1a9097bcdfbe0f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1778", "record_id": "City and County of San Francisco v. Sheehan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1778", "pinpoint_status": "slip-only", "quote": "no precedent clearly established that there was not 'an objective need for immediate entry' here,", "quote_fidelity": "mismatch", "record_id": "City and County of San Francisco v. Sheehan", "star_marker": null}}
{"assertion_id": "8f2cd00be0517190", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-600", "record_id": "City and County of San Francisco v. Sheehan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-600", "pinpoint_status": "slip-only", "quote": ") rather than waiting; when Sheehan again advanced with the knife, they used pepper spray and then shot her several times (she survived). She sued under the Americans with Disabilities Act and under § 1983 for excessive force. ## Issue Whether the officers were entitled to qualified immunity for the force used after re-entering Sheehan's room (and whether the ADA's accommodation requirement applies to arrests). ## Rule The Court declined to resolve the ADA question and held the officers immune.", "quote_fidelity": "mismatch", "record_id": "City and County of San Francisco v. Sheehan", "star_marker": null}}
{"assertion_id": "9568641791d4b973", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "City and County of San Francisco v. Sheehan"}, "payload": {"as_of_content": "2015-05-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "City and County of San Francisco v. Sheehan", "scope_note": "Good law: QI for force against an armed, mentally ill suspect; the ADA-accommodation question was dismissed as improvidently granted (left open).", "varies_by_point": false}}
```

### lake record — City and County of San Francisco v. Sheehan

```json
{
  "schema_version": "s2.v1",
  "record_id": "City and County of San Francisco v. Sheehan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City and County of San Francisco v. Sheehan",
    "case_name_short": "Sheehan",
    "case_name_full": "CITY AND COUNTY OF SAN FRANCISCO, CALIFORNIA, Et Al., Petitioners v. Teresa SHEEHAN.",
    "input_case_name": "City and County of San Francisco v. Sheehan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-05-18",
    "year": 2015,
    "docket": "13-1412",
    "cluster_id": 2801435,
    "lead_opinion_id": 2801435,
    "sibling_ids": [
      2801435
    ],
    "absolute_url": "/opinion/2801435/city-and-county-of-san-francisco-v-sheehan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "575 U.S. 600",
        "volume": "575",
        "reporter": "U.S.",
        "page": "600",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 1765",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 856",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4303",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4303",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 254",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "254",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 3200",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "3200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "575 U.S. 600",
        "volume": "575",
        "reporter": "U.S.",
        "page": "600",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 1765",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 856",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 3200",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "3200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4303",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4303",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 254",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "254",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-600",
      "page": null,
      "quote": ") rather than waiting; when Sheehan again advanced with the knife, they used pepper spray and then shot her several times (she survived). She sued under the Americans with Disabilities Act and under \u00a7 1983 for excessive force. ## Issue Whether the officers were entitled to qualified immunity for the force used after re-entering Sheehan's room (and whether the ADA's accommodation requirement applies to arrests). ## Rule The Court declined to resolve the ADA question and held the officers immune.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1778",
      "page": null,
      "quote": "no precedent clearly established that there was not 'an objective need for immediate entry' here,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-05-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City and County of San Francisco v. Sheehan",
    "varies_by_point": false,
    "scope_note": "Good law: QI for force against an armed, mentally ill suspect; the ADA-accommodation question was dismissed as improvidently granted (left open).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Morrow v. Meachum",
          "cluster_id": 8443910,
          "cite": [
            "917 F.3d 870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eunice Winzer v. Kaufman County",
          "cluster_id": 4591565,
          "cite": [
            "916 F.3d 464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael Kingsley v. Stan Hendrickson",
          "cluster_id": 2898269,
          "cite": [
            "801 F.3d 828",
            "2015 U.S. App. LEXIS 15963",
            "2015 WL 5210679"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barton Ex Rel. Estate of Barton v. Taber",
          "cluster_id": 3198370,
          "cite": [
            "820 F.3d 958",
            "2016 WL 1658098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Benavidez v. County of San Diego",
          "cluster_id": 4872698,
          "cite": [
            "993 F.3d 1134"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Reese, Jr. v. County of Sacramento",
          "cluster_id": 4489118,
          "cite": [
            "888 F.3d 1030"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fleet Hamby v. Steven Hammond",
          "cluster_id": 3199645,
          "cite": [
            "821 F.3d 1085",
            "2016 U.S. App. LEXIS 7894",
            "2016 WL 1730532"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katie Joseph v. John Doe",
          "cluster_id": 4821017,
          "cite": [
            "981 F.3d 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffery Mays v. Ronald Sprinkle",
          "cluster_id": 4869132,
          "cite": [
            "992 F.3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. Luna County",
          "cluster_id": 4321034,
          "cite": [
            "841 F.3d 895",
            "96 Fed. R. Serv. 3d 126",
            "2016 U.S. App. LEXIS 20466",
            "2016 WL 6694533"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Damon Wilson v. Prince George's County, Md",
          "cluster_id": 4508229,
          "cite": [
            "893 F.3d 213"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joan Kedra v. Richard Schroeter",
          "cluster_id": 4446761,
          "cite": [
            "876 F.3d 424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Austin Gates v. Hassan Khokar",
          "cluster_id": 4476683,
          "cite": [
            "884 F.3d 1290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Vos v. City of Newport Beach",
          "cluster_id": 4506067,
          "cite": [
            "892 F.3d 1024"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott Lee Rudlaff v. Brandon Gillispie",
          "cluster_id": 2813642,
          "cite": [
            "791 F.3d 638",
            "2015 FED App. 0133p",
            "2015 U.S. App. LEXIS 11304",
            "2015 WL 3981335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jamie Kirkpatrick v. County of Washoe",
          "cluster_id": 4328788,
          "cite": [
            "843 F.3d 784",
            "2016 U.S. App. LEXIS 21925",
            "2016 WL 7176654"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knight Ex Rel. Kerr v. Miami-Dade County",
          "cluster_id": 4389467,
          "cite": [
            "856 F.3d 795",
            "103 Fed. R. Serv. 388",
            "97 Fed. R. Serv. 3d 1086",
            "2017 WL 1755573",
            "2017 U.S. App. LEXIS 8036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darrell Frederick v. City of Rogers, Arkansas",
          "cluster_id": 4434883,
          "cite": [
            "873 F.3d 641",
            "2017 WL 4622313",
            "2017 U.S. App. LEXIS 20221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Haberle v. Daniel Troxell",
          "cluster_id": 4479031,
          "cite": [
            "885 F.3d 170"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Cole v. Michael Hunter",
          "cluster_id": 4654098,
          "cite": [
            "935 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yvette Felarca v. Robert Birgeneau",
          "cluster_id": 4502868,
          "cite": [
            "891 F.3d 809"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Debbie Latits v. Lowell Phillips",
          "cluster_id": 4455479,
          "cite": [
            "878 F.3d 541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Capp v. County of San Diego",
          "cluster_id": 4667181,
          "cite": [
            "940 F.3d 1046"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmon v. City of Arlington",
          "cluster_id": 5292775,
          "cite": [
            "16 F.4th 1159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caniglia v. Strom",
          "cluster_id": 4883694,
          "cite": [
            "593 U.S. 194",
            "209 L. Ed. 2d 604",
            "141 S. Ct. 1596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leonard Young, Jr. v. Deputy Superintendent Greene S",
          "cluster_id": 2898025,
          "cite": [
            "801 F.3d 172",
            "2015 U.S. App. LEXIS 15922",
            "2015 WL 5202968"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Entler v. Christine Gregoire",
          "cluster_id": 4432666,
          "cite": [
            "872 F.3d 1031",
            "2017 WL 4448218",
            "2017 U.S. App. LEXIS 19657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2801435) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDM5ODU2MDAwMDAwJnM9MjgyODAxMSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282801435%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(2801435)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDcmcz00Njg4Nzk3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%282801435%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2801435)",
        "reviewed": 43,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 43,
        "triage_read": 0,
        "triage_snippet_classified": 43
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2801435)",
    "indexed_citing_opinions": 271,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2801435,
        "count": 271,
        "count_source": "search"
      }
    ],
    "citation_count": 1024,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-and-county-of-san-francisco-v-sheehan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxOTQyNzImcz0xMDMyNTMyNSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282801435%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2801435,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 112524,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 118228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 118407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 195798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 670832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 674655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 768131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 769161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 775749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 777936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 796573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 796758,
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
    "date_created": "2026-07-05T00:07:42Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:11:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City and County of San Francisco v. Sheehan

```
(Slip Opinion)              OCTOBER TERM, 2014                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

          CITY AND COUNTY OF SAN FRANCISCO, 

             CALIFORNIA, ET AL. v. SHEEHAN


CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

     No. 13–1412. Argued March 23, 2015—Decided May 18, 2015
Respondent Sheehan lived in a group home for individuals with mental
  illness. After Sheehan began acting erratically and threatened to kill
  her social worker, the City and County of San Francisco (San Fran-
  cisco) dispatched police officers Reynolds and Holder to help escort
  Sheehan to a facility for temporary evaluation and treatment. When
  the officers first entered Sheehan’s room, she grabbed a knife and
  threatened to kill them. They retreated and closed the door. Con-
  cerned about what Sheehan might do behind the closed door, and
  without considering if they could accommodate her disability, the of-
  ficers reentered her room. Sheehan, knife in hand, again confronted
  them. After pepper spray proved ineffective, the officers shot
  Sheehan multiple times. Sheehan later sued petitioner San Francis-
  co for, among other things, violating Title II of the Americans with
  Disabilities Act of 1990 (ADA) by arresting her without accommodat-
  ing her disability. See 42 U. S. C. §12132. She also sued petitioners
  Reynolds and Holder in their personal capacities under 42 U. S. C.
  §1983, claiming that they violated her Fourth Amendment rights.
  The District Court granted summary judgment because it concluded
  that officers making an arrest are not required to determine whether
  their actions would comply with the ADA before protecting them-
  selves and others, and also that Reynolds and Holder did not violate
  the Constitution. Vacating in part, the Ninth Circuit held that the
  ADA applied and that a jury must decide whether San Francisco
  should have accommodated Sheehan. The court also held that Reyn-
  olds and Holder are not entitled to qualified immunity because it is
  clearly established that, absent an objective need for immediate en-
  try, officers cannot forcibly enter the home of an armed, mentally ill
2             CITY AND COUNTY OF SAN FRANCISCO
                         v. SHEEHAN
                            Syllabus

    person who has been acting irrationally and has threatened anyone
    who enters.
Held:
    1. The question whether §12132 “requires law enforcement officers
 to provide accommodations to an armed, violent, and mentally ill
 suspect in the course of bringing the suspect into custody,” Pet. for
 Cert. i, is dismissed as improvidently granted. Certiorari was grant-
 ed on the understanding that San Francisco would argue that Title II
 of the ADA does not apply when an officer faces an armed and dan-
 gerous individual. Instead, San Francisco merely argues that
 Sheehan was not “qualified” for an accommodation, §12132, because
 she “pose[d] a direct threat to the health or safety of others,” which
 threat could not “be eliminated by a modification of policies, practices
 or procedures, or by the provision of auxiliary aids or services,” 28
 CFR §§35.139(a), 35.104. This argument was not passed on by the
 court below. The decision to dismiss this question as improvidently
 granted, moreover, is reinforced by the parties’ failure to address the
 related question whether a public entity can be vicariously liable for
 damages under Title II for an arrest made by its police officers.
 Pp. 7–10.
    2. Reynolds and Holder are entitled to qualified immunity from lia-
 bility for the injuries suffered by Sheehan. Public officials are im-
 mune from suit under 42 U. S. C. §1983 unless they have “violated a
 statutory or constitutional right that was ‘ “ ‘clearly established’ ” ’ at
 the time of the challenged conduct,” Plumhoff v. Rickard, 572 U. S.
 ___, ___, an exacting standard that “gives government officials
 breathing room to make reasonable but mistaken judgments,” Ash-
 croft v. al-Kidd, 563 U. S. ___, ___. The officers did not violate the
 Fourth Amendment when they opened Sheehan’s door the first time,
 and there is no doubt that they could have opened her door the sec-
 ond time without violating her rights had Sheehan not been disabled.
 Their use of force was also reasonable. The only question therefore is
 whether they violated the Fourth Amendment when they decided to
 reopen Sheehan’s door rather than attempt to accommodate her dis-
 ability. Because any such Fourth Amendment right, even assuming
 it exists, was not clearly established, Reynolds and Holder are enti-
 tled to qualified immunity. Likewise, an alleged failure on the part of
 the officers to follow their training does not itself negate qualified
 immunity where it would otherwise be warranted. Pp. 10–17.
Certiorari dismissed in part; 743 F. 3d 1211, reversed in part and re-
  manded.

  ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and KENNEDY, THOMAS, GINSBURG, and SOTOMAYOR, JJ., joined. SCALIA,
                     Cite as: 575 U. S. ____ (2015)                    3

                                Syllabus

J., filed an opinion concurring in part and dissenting in part, in which
KAGAN, J., joined. BREYER, J., took no part in the consideration or deci-
sion of the case.
                       Cite as: 575 U. S. ____ (2015)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 13–1412
                                  _________________


       CITY AND COUNTY OF SAN FRANCISCO, 

         CALIFORNIA, ET AL., PETITIONERS v.

                TERESA SHEEHAN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                                [May 18, 2015] 


  JUSTICE ALITO delivered the opinion of the Court.
  We granted certiorari to consider two questions relating
to the manner in which San Francisco police officers ar-
rested a woman who was suffering from a mental illness
and had become violent. After reviewing the parties’
submissions, we dismiss the first question as improvidently
granted. We decide the second question and hold that
the officers are entitled to qualified immunity because
they did not violate any clearly established Fourth
Amendment rights.
                             I
   Petitioners are the City and County of San Francisco,
California (San Francisco), and two police officers, Ser-
geant Kimberly Reynolds and Officer Kathrine Holder.
Respondent is Teresa Sheehan, a woman who suffers from
a schizoaffective disorder. Because this case arises in a
summary judgment posture, we view the facts in the light
most favorable to Sheehan, the nonmoving party. See,
e.g., Plumhoff v. Rickard, 572 U. S. ___, ___–___ (2014)
(slip op., at 1–2).
2          CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

  In August 2008, Sheehan lived in a group home for
people dealing with mental illness. Although she shared
common areas of the building with others, she had a pri-
vate room. On August 7, Heath Hodge, a social worker
who supervised the counseling staff in the building, at-
tempted to visit Sheehan to conduct a welfare check.
Hodge was concerned because Sheehan had stopped tak-
ing her medication, no longer spoke with her psychiatrist,
and reportedly was no longer changing her clothes or
eating. See 743 F. 3d 1211, 1218 (CA9 2014); App. 23–24.
  Hodge knocked on Sheehan’s door but received no an-
swer. He then used a key to enter her room and found
Sheehan on her bed. Initially, she would not respond to
questions. But she then sprang up, reportedly yelling,
“Get out of here! You don’t have a warrant! I have a
knife, and I’ll kill you if I have to.” Hodge left without
seeing whether she actually had a knife, and Sheehan
slammed the door shut behind him. See 743 F. 3d, at
1218.
  Sheehan, Hodge realized, required “some sort of inter-
vention,” App. 96, but he also knew that he would need
help. Hodge took steps to clear the building of other peo-
ple and completed an application to have Sheehan de-
tained for temporary evaluation and treatment. See Cal.
Welf. & Inst. Code Ann. §5150 (West 2015 Cum. Supp.)
(authorizing temporary detention of someone who “as a
result of a mental health disorder, is a danger to others, or
to himself or herself, or gravely disabled”). On that appli-
cation, Hodge checked off boxes indicating that Sheehan
was a “threat to others” and “gravely disabled,” but he did
not mark that she was a danger to herself. 743 F. 3d, at
1218. He telephoned the police and asked for help to take
Sheehan to a secure facility.
  Officer Holder responded to police dispatch and headed
toward the group home. When she arrived, Holder re-
viewed the temporary-detention application and spoke
                  Cite as: 575 U. S. ____ (2015)            3

                      Opinion of the Court

with Hodge. Holder then sought assistance from Sergeant
Reynolds, a more experienced officer. After Reynolds
arrived and was brought up to speed, Hodge spoke with a
nurse at the psychiatric emergency services unit at San
Francisco General Hospital who said that the hospital
would be able to admit Sheehan.
  Accompanied by Hodge, the officers went to Sheehan’s
room, knocked on her door, announced who they were, and
told Sheehan that “we want to help you.” App. 36. When
Sheehan did not answer, the officers used Hodge’s key to
enter the room. Sheehan reacted violently. She grabbed a
kitchen knife with an approximately 5-inch blade and
began approaching the officers, yelling something along
the lines of “I am going to kill you. I don’t need help. Get
out.” Ibid. See also id., at 284 (“[Q.] Did you tell them I’ll
kill you if you don’t get out of here? A. Yes”). The offic-
ers—who did not have their weapons drawn—“retreated
and Sheehan closed the door, leaving Sheehan in her room
and the officers and Hodge in the hallway.” 743 F. 3d, at
1219. The officers called for backup and sent Hodge
downstairs to let in reinforcements when they arrived.
  The officers were concerned that the door to Sheehan’s
room was closed. They worried that Sheehan, out of their
sight, might gather more weapons—Reynolds had already
observed other knives in her room, see App. 228—or even
try to flee through the back window, id., at 227. Because
Sheehan’s room was on the second floor, she likely would
have needed a ladder to escape. Fire escapes, however,
are common in San Francisco, and the officers did not
know whether Sheehan’s room had such an escape. (Nei-
ther officer asked Hodge about a fire escape, but if they
had, it seems he “probably” would have said there was
one, id., at 117). With the door closed, all that Reynolds
and Holder knew for sure was that Sheehan was unstable,
she had just threatened to kill three people, and she had a
4             CITY AND COUNTY OF SAN FRANCISCO
                          v. SHEEHAN
                       Opinion of the Court

weapon.1
  Reynolds and Holder had to make a decision. They
could wait for backup—indeed, they already heard sirens.
Or they could quickly reenter the room and try to subdue
Sheehan before more time elapsed. Because Reynolds
believed that the situation “required [their] immediate
attention,” id., at 235, the officers chose reentry. In mak-
ing that decision, they did not pause to consider whether
Sheehan’s disability should be accommodated. See 743
F. 3d, at 1219. The officers obviously knew that Sheehan
was unwell, but in Reynolds’ words, that was “a secondary
issue” given that they were “faced with a violent woman
who had already threatened to kill her social worker” and
“two uniformed police officers.” App. 235.
  The officers ultimately decided that Holder—the larger
officer—should push the door open while Reynolds used
pepper spray on Sheehan. With pistols drawn, the officers
moved in. When Sheehan, knife in hand, saw them, she
again yelled for them to leave. She may also have again
said that she was going to kill them. Sheehan is “not
sure” if she threatened death a second time, id., at 284,
but “concedes that it was her intent to resist arrest and to
use the knife,” 743 F. 3d, at 1220. In any event, Reynolds
began pepper-spraying Sheehan in the face, but Sheehan
would not drop the knife. When Sheehan was only a few
——————
   1 The officers also may have feared that another person was with

Sheehan. Reynolds testified that the officers had not been “able to do a
complete assessment of the entire room.” App. 38. Sheehan, by con-
trast, testified during a deposition that the officers “could see . . . that
no one else was in the room.” Id., at 279. Before the Ninth Circuit,
Sheehan conceded that some of her deposition testimony “smacks of
irrationality that begs the question whether any of it is credible.” Brief
for Appellant in No. 11–16401 (CA9), p. 41; see also Reply Brief in No.
11–16401, p. 17 (explaining that “the inherent inconsistences in her
testimony cast suspicion over all of it”). We need not decide whether
there is a genuine dispute of fact here because the officers’ other,
independent concerns make this point immaterial.
                     Cite as: 575 U. S. ____ (2015)                   5

                         Opinion of the Court

feet away, Holder shot her twice, but she did not collapse.
Reynolds then fired multiple shots.2 After Sheehan finally
fell, a third officer (who had just arrived) kicked the knife
out of her hand. Sheehan survived.
   Sometime later, San Francisco prosecuted Sheehan for
assault with a deadly weapon, assault on a peace officer
with a deadly weapon, and making criminal threats. The
jury acquitted Sheehan of making threats but was unable
to reach a verdict on the assault counts, and prosecutors
decided not to retry her.
   Sheehan then brought suit, alleging, among other
things, that San Francisco violated the Americans with
Disabilities Act of 1990 (ADA), 104 Stat. 327, 42 U. S. C.
§12101 et seq., by subduing her in a manner that did not
reasonably accommodate her disability. She also sued
Reynolds and Holder in their personal capacities under
Rev. Stat. §1979, 42 U. S. C. §1983, for violating her
Fourth Amendment rights. In support of her claims, she
offered testimony from a former deputy police chief, Lou
Reiter, who contended that Reynolds and Holder fell short
of their training by not using practices designed to mini-
mize the risk of violence when dealing with the mentally
ill.
   The District Court granted summary judgment for
petitioners. Relying on Hainze v. Richards, 207 F. 3d 795
(CA5 2000), the court held that officers making an arrest
are not required “to first determine whether their actions
would comply with the ADA before protecting themselves
and others.” App. to Pet. for Cert. 80. The court also held
that the officers did not violate the Fourth Amendment.
The court wrote that the officers “had no way of knowing

——————
  2 There  is a dispute regarding whether Sheehan was on the ground
for the last shot. This dispute is not material: “Even if Sheehan was on
the ground, she was certainly not subdued.” 743 F. 3d 1211, 1230 (CA9
2014).
6          CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

whether [Sheehan] might escape through a back window
or fire escape, whether she might hurt herself, or whether
there was anyone else in her room whom she might hurt.”
Id., at 71. In addition, the court observed that Holder did
not begin shooting until it was necessary for her to do so in
order “to protect herself ” and that “Reynolds used deadly
force only after she found that pepper spray was not
enough force to contain the situation.” Id., at 75, 76–77.
  On appeal, the Ninth Circuit vacated in part. Relevant
here, the panel held that because the ADA covers public
“services, programs, or activities,” §12132, the ADA’s
accommodation requirement should be read to “to encom-
pass ‘anything a public entity does,’ ” 743 F. 3d, at 1232.
The Ninth Circuit agreed “that exigent circumstances
inform the reasonableness analysis under the ADA,” ibid.,
but concluded that it was for a jury to decide whether San
Francisco should have accommodated Sheehan by, for
instance, “respect[ing] her comfort zone, engag[ing] in non-
threatening communications and us[ing] the passage of
time to defuse the situation rather than precipitating a
deadly confrontation.” Id., at 1233.
  As to Reynolds and Holder, the panel held that their
initial entry into Sheehan’s room was lawful and that,
after the officers opened the door for the second time, they
reasonably used their firearms when the pepper spray
failed to stop Sheehan’s advance. Nonetheless, the panel
also held that a jury could find that the officers “provoked”
Sheehan by needlessly forcing that second confrontation.
Id., at 1216, 1229. The panel further found that it was
clearly established that an officer cannot “forcibly enter
the home of an armed, mentally ill subject who had been
acting irrationally and had threatened anyone who en-
tered when there was no objective need for immediate
entry.” Id., at 1229. Dissenting in part, Judge Graber
would have held that the officers were entitled to qualified
immunity.
                  Cite as: 575 U. S. ____ (2015)             7

                      Opinion of the Court

  San Francisco and the officers petitioned for a writ of
certiorari and asked us to review two questions. We
granted the petition. 574 U. S. ___ (2014).
                              II
   Title II of the ADA commands that “no qualified indi-
vidual with a disability shall, by reason of such disability,
be excluded from participation in or be denied the benefits
of the services, programs, or activities of a public entity, or
be subjected to discrimination by any such entity.” 42
U. S. C. §12132. The first question on which we granted
review asks whether this provision “requires law enforce-
ment officers to provide accommodations to an armed,
violent, and mentally ill suspect in the course of bringing
the suspect into custody.” Pet. for Cert. i. When we
granted review, we understood this question to embody
what appears to be the thrust of the argument that San
Francisco made in the Ninth Circuit, namely that “ ‘Title II
does not apply to an officer’s on-the-street responses to
reported disturbances or other similar incidents, whether
or not those calls involve subjects with mental disabilities,
prior to the officer’s securing the scene and ensuring that
there is no threat to human life.’ ” Brief for Appellees in
No. 11–16401 (CA9), p. 36 (quoting Hainze, supra, at 801;
emphasis added); see also Brief for Appellees in No. 11–
16401, at 37 (similar).
   As San Francisco explained in its reply brief at the
certiorari stage, resolving its “question presented” “does
not require a fact-intensive ‘reasonable accommodation’
inquiry,” since “the only question for this Court to resolve
is whether any accommodation of an armed and violent
individual is reasonable or required under Title II of the
ADA.” Reply to Brief in Opposition 3.
   Having persuaded us to grant certiorari, San Francisco
chose to rely on a different argument than what it pressed
below. In its brief in this Court, San Francisco focuses on
8          CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

the statutory phrase “qualified individual,” §12132, and a
regulation declaring that Title II “does not require a public
entity to permit an individual to participate in or benefit
from the services, programs, or activities of that public
entity when that individual poses a direct threat to the
health or safety of others.” 28 CFR §35.139(a) (2014).
Another regulation defines a “direct threat” as “a signifi-
cant risk to the health or safety of others that cannot be
eliminated by a modification of policies, practices or proce-
dures, or by the provision of auxiliary aids or services.”
§35.104. Putting these authorities together, San Fran-
cisco argues that “a person who poses a direct threat or
significant risk to the safety of others is not qualified for
accommodations under the ADA,” Brief for Petitioners 17.
Contending that Sheehan clearly posed a “direct threat,”
San Francisco concludes that she was therefore not “quali-
fied” for an accommodation.
   Though, to be sure, this “qualified” argument does ap-
pear in San Francisco’s certiorari petition, San Francisco
never hinted at it in the Ninth Circuit. The Court does
not ordinarily decide questions that were not passed on
below. More than that, San Francisco’s new argument
effectively concedes that the relevant provision of the
ADA, 42 U. S. C. §12132, may “requir[e] law enforcement
officers to provide accommodations to an armed, violent,
and mentally ill suspect in the course of bringing the
suspect into custody.” Pet. for Cert. i. This is so because
there may be circumstances in which any “significant risk”
presented by “an armed, violent, and mentally ill suspect”
can be “eliminated by a modification of policies, practices
or procedures, or by the provision of auxiliary aids or
services.”
   The argument that San Francisco now advances is
predicated on the proposition that the ADA governs the
manner in which a qualified individual with a disability is
arrested. The relevant provision provides that a public
                  Cite as: 575 U. S. ____ (2015)             9

                      Opinion of the Court

entity may not “exclud[e]” a qualified individual with a
disability from “participat[ing] in,” and may not “den[y]”
that individual the “benefits of[,] the services, programs,
or activities of a public entity.” §12132. This language
would apply to an arrest if an arrest is an “activity” in
which the arrestee “participat[es]” or from which the
arrestee may “benefi[t].”
   This same provision also commands that “no qualified
individual with a disability shall be . . . subjected to dis-
crimination by any [public] entity.” Ibid. This part of the
statute would apply to an arrest if the failure to arrest an
individual with a mental disability in a manner that
reasonably accommodates that disability constitutes “dis-
crimination.” Ibid.
   Whether the statutory language quoted above applies to
arrests is an important question that would benefit from
briefing and an adversary presentation. But San Fran-
cisco, the United States as amicus curiae, and Sheehan all
argue (or at least accept) that §12132 applies to arrests.
No one argues the contrary view. As a result, we do not
think that it would be prudent to decide the question in
this case.
   Our decision not to decide whether the ADA applies to
arrests is reinforced by the parties’ failure to address a
related question: whether a public entity can be liable for
damages under Title II for an arrest made by its police
officers. Only public entities are subject to Title II, see,
e.g., Pennsylvania Dept. of Corrections v. Yeskey, 524 U. S.
206, 208 (1998), and the parties agree that such an entity
can be held vicariously liable for money damages for the
purposeful or deliberately indifferent conduct of its em-
ployees. See Tr. of Oral Arg. 10–12, 22. But we have
never decided whether that is correct, and we decline to do
so here, in the absence of adversarial briefing.
   Because certiorari jurisdiction exists to clarify the law,
its exercise “is not a matter of right, but of judicial discre-
10           CITY AND COUNTY OF SAN FRANCISCO
                         v. SHEEHAN
                      Opinion of the Court

tion.” Supreme Court Rule 10. Exercising that discretion,
we dismiss the first question presented as improvidently
granted. See, e.g., Board of Trustees of Univ. of Ala. v.
Garrett, 531 U. S. 356, 360, n. 1 (2001) (partial dismissal);
Parker v. Dugger, 498 U. S. 308, 323 (1991) (same).
                             III
   The second question presented is whether Reynolds and
Holder can be held personally liable for the injuries that
Sheehan suffered. We conclude they are entitled to quali-
fied immunity.3
   Public officials are immune from suit under 42 U. S. C.
§1983 unless they have “violated a statutory or constitu-
tional right that was clearly established at the time of the
challenged conduct.” Plumhoff, 572 U. S., at ___ (slip op.,
at 12) (internal quotation marks omitted). An officer
“cannot be said to have violated a clearly established right
unless the right’s contours were sufficiently definite that
any reasonable official in [his] shoes would have under-
——————
   3 Not satisfied with dismissing question one, which concerns San

Francisco’s liability, our dissenting colleagues would further punish
San Francisco by dismissing question two as well. See post, at 3
(opinion of SCALIA, J.) (arguing that deciding the second question would
“reward” San Francisco and “spar[e it] the significant expense of
defending the suit, and satisfying any judgment, against the individual
petitioners”). But question two concerns the liability of the individual
officers. Whatever contractual obligations San Francisco may (or may
not) have to represent and indemnify the officers are not our concern.
At a minimum, these officers have a personal interest in the correctness
of the judgment below, which holds that they may have violated the
Constitution. Moreover, when we granted the petition, we determined
that both questions independently merited review. Because of the
importance of qualified immunity “to society as a whole,” Harlow v.
Fitzgerald, 457 U. S. 800, 814 (1982), the Court often corrects lower
courts when they wrongly subject individual officers to liability. See,
e.g., Carroll v. Carman, 574 U. S. ___ (2014) (per curiam); Wood v.
Moss, 572 U. S. ___ (2014); Plumhoff v. Rickard, 572 U. S. ___ (2014);
Stanton v. Sims, 571 U. S. ___ (2013) (per curiam); Reichle v. Howards,
566 U. S. ___ (2012).
                 Cite as: 575 U. S. ____ (2015)          11

                     Opinion of the Court

stood that he was violating it,” ibid., meaning that “exist-
ing precedent . . . placed the statutory or constitutional
question beyond debate.” Ashcroft v. al-Kidd, 563 U. S.
___, ___ (2011) (slip op., at 9). This exacting standard
“gives government officials breathing room to make rea-
sonable but mistaken judgments” by “protect[ing] all but
the plainly incompetent or those who knowingly violate
the law.” Id., at ___ (slip op., at 12).
   In this case, although we disagree with the Ninth Cir-
cuit’s ultimate conclusion on the question of qualified
immunity, we agree with its analysis in many respects.
For instance, there is no doubt that the officers did not
violate any federal right when they opened Sheehan’s door
the first time. See 743 F. 3d, at 1216, 1223. Reynolds and
Holder knocked on the door, announced that they were
police officers, and informed Sheehan that they wanted to
help her. When Sheehan did not come to the door, they
entered her room. This was not unconstitutional. “[L]aw
enforcement officers may enter a home without a warrant
to render emergency assistance to an injured occupant or
to protect an occupant from imminent injury.” Brigham
City v. Stuart, 547 U. S. 398, 403 (2006). See also Ken-
tucky v. King, 563 U. S. ___, ___ (2011) (slip op., at 6).
   Nor is there any doubt that had Sheehan not been dis-
abled, the officers could have opened her door the second
time without violating any constitutional rights. For one
thing, “because the two entries were part of a single,
continuous search or seizure, the officers [were] not re-
quired to justify the continuing emergency with respect to
the second entry.” 743 F. 3d, at 1224 (following Michigan
v. Tyler, 436 U. S. 499, 511 (1978)). In addition, Reynolds
and Holder knew that Sheehan had a weapon and had
threatened to use it to kill three people. They also knew
that delay could make the situation more dangerous. The
Fourth Amendment standard is reasonableness, and it is
reasonable for police to move quickly if delay “would
12         CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

gravely endanger their lives or the lives of others.” War-
den, Md. Penitentiary v. Hayden, 387 U. S. 294, 298–299
(1967). This is true even when, judged with the benefit of
hindsight, the officers may have made “some mistakes.”
Heien v. North Carolina, 574 U. S. ___, ___ (2014) (slip op.,
at 5). The Constitution is not blind to “the fact that police
officers are often forced to make split-second judgments.”
Plumhoff, supra, at ___ (slip op., at 8).
   We also agree with the Ninth Circuit that after the
officers opened Sheehan’s door the second time, their use
of force was reasonable.         Reynolds tried to subdue
Sheehan with pepper spray, but Sheehan kept coming at
the officers until she was “only a few feet from a cornered
Officer Holder.” 743 F. 3d, at 1229. At this point, the use
of potentially deadly force was justified. See Scott v.
Harris, 550 U. S. 372, 384 (2007). Nothing in the Fourth
Amendment barred Reynolds and Holder from protecting
themselves, even though it meant firing multiple rounds.
See Plumhoff, supra, at ___ (slip op., at 11).
   The real question, then, is whether, despite these dan-
gerous circumstances, the officers violated the Fourth
Amendment when they decided to reopen Sheehan’s door
rather than attempting to accommodate her disability.
Here we come to another problem. San Francisco, whose
attorneys represent Reynolds and Holder, devotes scant
briefing to this question. Instead, San Francisco argues
almost exclusively that even if it is assumed that there
was a Fourth Amendment violation, the right was not
clearly established. This Court, of course, could decide the
constitutional question anyway. See Pearson v. Callahan,
555 U. S. 223, 242 (2009) (recognizing discretion). But
because this question has not been adequately briefed, we
decline to do so. See id., at 239. Rather, we simply decide
whether the officers’ failure to accommodate Sheehan’s
illness violated clearly established law. It did not.
   To begin, nothing in our cases suggests the constitu-
                 Cite as: 575 U. S. ____ (2015)           13

                     Opinion of the Court

tional rule applied by the Ninth Circuit. The Ninth Circuit
focused on Graham v. Connor, 490 U. S. 386 (1989), but
Graham holds only that the “ ‘objective reasonableness’ ”
test applies to excessive-force claims under the Fourth
Amendment. See id., at 388. That is far too general a
proposition to control this case. “We have repeatedly told
courts—and the Ninth Circuit in particular—not to define
clearly established law at a high level of generality.” al-
Kidd, supra, at ___ (citation omitted) (slip op., at 10); cf.
Lopez v. Smith, 574 U. S. ___, ___ (2014) (per curiam) (slip
op., at 5). Qualified immunity is no immunity at all if
“clearly established” law can simply be defined as the
right to be free from unreasonable searches and seizures.
   Even a cursory glance at the facts of Graham confirms
just how different that case is from this one. That case did
not involve a dangerous, obviously unstable person mak-
ing threats, much less was there a weapon involved.
There is a world of difference between needlessly with-
holding sugar from an innocent person who is suffering
from an insulin reaction, see Graham, supra, at 388–389,
and responding to the perilous situation Reynolds and
Holder confronted. Graham is a nonstarter.
   Moving beyond Graham, the Ninth Circuit also turned
to two of its own cases. But even if “a controlling circuit
precedent could constitute clearly established federal law
in these circumstances,” Carroll v. Carman, 574 U. S. ___,
___ (2014) (per curiam) (slip op., at 4), it does not do so
here.
   The Ninth Circuit first pointed to Deorle v. Rutherford,
272 F. 3d 1272 (CA9 2001), but from the very first para-
graph of that opinion we learn that Deorle involved an
officer’s use of a beanbag gun to subdue “an emotionally
disturbed” person who “was unarmed, had not attacked or
even touched anyone, had generally obeyed the instruc-
tions given him by various police officers, and had not
committed any serious offense.” Id., at 1275. The officer
14            CITY AND COUNTY OF SAN FRANCISCO
                          v. SHEEHAN
                       Opinion of the Court

there, moreover, “observed Deorle at close proximity for
about five to ten minutes before shooting him” in the face.
See id., at 1281. Whatever the merits of the decision in
Deorle, the differences between that case and the case
before us leap from the page. Unlike Deorle, Sheehan was
dangerous, recalcitrant, law-breaking, and out of sight.
   The Ninth Circuit also leaned on Alexander v. City and
County of San Francisco, 29 F. 3d 1355 (CA9 1994), an-
other case involving mental illness. There, officials from
San Francisco attempted to enter Henry Quade’s home
“for the primary purpose of arresting him” even though
they lacked an arrest warrant. Id., at 1361. Quade, in
response, fired a handgun; police officers “shot back, and
Quade died from gunshot wounds shortly thereafter.” Id.,
at 1358. The panel concluded that a jury should decide
whether the officers used excessive force. The court rea-
soned that the officers provoked the confrontation because
there were no “exigent circumstances” excusing their
entrance. Id., at 1361.
   Alexander too is a poor fit. As Judge Graber observed
below in her dissent, the Ninth Circuit has long read
Alexander narrowly. See 743 F. 3d, at 1235 (Graber, J.,
concurring in part and dissenting in part) (citing Billing-
ton v. Smith, 292 F. 3d 1177 (CA9 2002)). Under Ninth
Circuit law,4 an entry that otherwise complies with the
Fourth Amendment is not rendered unreasonable because
it provokes a violent reaction. See id., at 1189–1190.
——————
   4 Our citation to Ninth Circuit cases should not be read to suggest our

agreement (or, for that matter, disagreement) with them. The Ninth
Circuit’s “provocation” rule, for instance, has been sharply questioned
elsewhere. See Livermore v. Lubelan, 476 F. 3d 397, 406–407 (CA6
2007); see also, e.g., Hector v. Watt, 235 F. 3d 154, 160 (CA3 2001) (“[I]f
the officers’ use of force was reasonable given the plaintiff’s acts, then
despite the illegal entry, the plaintiff’s own conduct would be an inter-
vening cause”). Whatever their merits, all that matters for our quali-
fied immunity analysis is that they do not clearly establish any right
that the officers violated.
                 Cite as: 575 U. S. ____ (2015)           15

                     Opinion of the Court

Under this rule, qualified immunity necessarily applies
here because, as explained above, competent officers could
have believed that the second entry was justified under
both continuous search and exigent circumstance ration-
ales. Indeed, even if Reynolds and Holder misjudged the
situation, Sheehan cannot “establish a Fourth Amend-
ment violation based merely on bad tactics that result in a
deadly confrontation that could have been avoided.” Id.,
at 1190. Courts must not judge officers with “the 20/20
vision of hindsight.’ ” Ibid. (quoting Graham, 490 U. S., at
396).
   When Graham, Deorle, and Alexander are viewed to-
gether, the central error in the Ninth Circuit’s reasoning
is apparent. The panel majority concluded that these
three cases “would have placed any reasonable, competent
officer on notice that it is unreasonable to forcibly enter
the home of an armed, mentally ill suspect who had been
acting irrationally and had threatened anyone who en-
tered when there was no objective need for immediate
entry.” 743 F. 3d, at 1229. But even assuming that is
true, no precedent clearly established that there was not
“an objective need for immediate entry” here. No matter
how carefully a reasonable officer read Graham, Deorle,
and Alexander beforehand, that officer could not know
that reopening Sheehan’s door to prevent her from escap-
ing or gathering more weapons would violate the Ninth
Circuit’s test, even if all the disputed facts are viewed in
respondent’s favor. Without that “fair notice,” an officer is
entitled to qualified immunity. See, e.g., Plumhoff, 572
U. S., at ___ (slip op., at 13).
   Nor does it matter for purposes of qualified immunity
that Sheehan’s expert, Reiter, testified that the officers
did not follow their training. According to Reiter, San
Francisco trains its officers when dealing with the mentally
ill to “ensure that sufficient resources are brought to the
scene,” “contain the subject” and “respect the suspect’s
16          CITY AND COUNTY OF SAN FRANCISCO
                        v. SHEEHAN
                     Opinion of the Court

“comfort zone,” “use time to their advantage,” and “employ
non-threatening verbal communication and open-ended
questions to facilitate the subject’s participation in com-
munication.” Brief for Respondent 7. Likewise, San Fran-
cisco’s policy is “ ‘to use hostage negotiators’ ” when dealing
with “ ‘a suspect [who] resists arrest by barricading him-
self.’ ” Id., at 8 (quoting San Francisco Police Department
General Order 8.02, §II(B) (Aug. 3, 1994), online at
http://www.sf-police.org (as visited May 14, 2015, and
available in Clerk of Court’s case file)).
   Even if an officer acts contrary to her training, however,
(and here, given the generality of that training, it is not at
all clear that Reynolds and Holder did so), that does not
itself negate qualified immunity where it would otherwise
be warranted. Rather, so long as “a reasonable officer
could have believed that his conduct was justified,” a
plaintiff cannot “avoi[d] summary judgment by simply
producing an expert’s report that an officer’s conduct
leading up to a deadly confrontation was imprudent,
inappropriate, or even reckless.” Billington, supra, at
1189. Cf. Saucier v. Katz, 533 U. S. 194, 216, n. 6 (2001)
(GINSBURG, J., concurring in judgment) (“ ‘[I]n close cases,
a jury does not automatically get to second-guess these life
and death decisions, even though a plaintiff has an expert
and a plausible claim that the situation could better have
been handled differently’ ” (quoting Roy v. Inhabitants of
Lewiston, 42 F. 3d 691, 695 (CA1 1994))). Considering the
specific situation confronting Reynolds and Holder, they
had sufficient reason to believe that their conduct was
justified.
   Finally, to the extent that a “robust consensus of cases
of persuasive authority” could itself clearly establish the
federal right respondent alleges, al-Kidd, 563 U. S., at ___
(slip op., at 10), no such consensus exists here. If any-
thing, the opposite may be true. See, e.g., Bates v. Ches-
terfield County, 216 F. 3d 367, 372 (CA4 2000)
                 Cite as: 575 U. S. ____ (2015)           17

                     Opinion of the Court

(“Knowledge of a person’s disability simply cannot fore-
close officers from protecting themselves, the disabled
person, and the general public”); Sanders v. Minneapolis,
474 F. 3d 523, 527 (CA8 2007) (following Bates, supra);
Menuel v. Atlanta, 25 F. 3d 990 (CA11 1994) (upholding
use of deadly force to try to apprehend a mentally ill man
who had a knife and was hiding behind a door).
  In sum, we hold that qualified immunity applies be-
cause these officers had no “fair and clear warning of what
the Constitution requires.” al-Kidd, supra, at ___ (KEN-
NEDY, J., concurring) (slip op., at 3). Because the qualified
immunity analysis is straightforward, we need not decide
whether the Constitution was violated by the officers’
failure to accommodate Sheehan’s illness.
                      *     *    *
  For these reasons, the first question presented is dis-
missed as improvidently granted. On the second question,
we reverse the judgment of the Ninth Circuit. The case is
remanded for further proceedings consistent with this
opinion.
                                          It is so ordered.

  JUSTICE BREYER took no part in the consideration or
decision of this case.
                 Cite as: 575 U. S. ____ (2015)           1

                     Opinion of SCALIA, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 13–1412
                         _________________


       CITY AND COUNTY OF SAN FRANCISCO, 

         CALIFORNIA, ET AL., PETITIONERS v.

                TERESA SHEEHAN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                        [May 18, 2015] 


  JUSTICE SCALIA, with whom JUSTICE KAGAN joins,
concurring in part and dissenting in part.
  The first question presented (QP) in the petition for
certiorari was “Whether Title II of the Americans with
Disabilities Act [(ADA)] requires law enforcement officers
to provide accommodations to an armed, violent, and
mentally ill suspect in the course of bringing the suspect
into custody.” Pet. for Cert. i. The petition assured us
(quite accurately), and devoted a section of its argument to
the point, that “The Circuits Are In Conflict On This
Question.” Id., at 18. And petitioners faulted the Ninth
Circuit for “holding that the ADA’s reasonable accommo-
dation requirement applies to officers facing violent cir-
cumstances,” a conclusion that was “in direct conflict with
the categorical prohibition on such claims adopted by the
Fifth and Sixth Circuits.” Ibid. Petitioners had expressly
advocated for the Fifth and Sixth Circuits’ position in the
Court of Appeals. See Appellees’ Answering Brief in No.
11–16401 (CA9), pp. 35–37 (“[T]he ADA does not apply to
police officers’ responses to violent individuals who happen
to be mentally ill, where officers have not yet brought the
violent situation under control”).
  Imagine our surprise, then, when the petitioners’ prin-
cipal brief, reply brief, and oral argument had nary a word
2          CITY AND COUNTY OF SAN FRANCISCO
                            v. SHEEHAN
        SCALIA, J., concurring
                        Opinion inof
                                   part and,dissenting
                                     SCALIA J.         in part

to say about that subject. Instead, petitioners bluntly
announced in their principal brief that they “do not assert
that the actions of individual police officers [in arresting
violent and armed disabled persons] are never subject to
scrutiny under Title II,” and proclaimed that “[t]he only
ADA issue here is what Title II requires of individual
officers who are facing an armed and dangerous suspect.”
Brief for Petitioners 34 (emphasis added). In other words,
the issue is not (as the petition had asserted) whether Title
II applies to arrests of violent, mentally ill individuals, but
rather how it applies under the circumstances of this case,
where the plaintiff threatened officers with a weapon. We
were thus deprived of the opportunity to consider, and
settle, a controverted question of law that has divided the
Circuits, and were invited instead to decide an ADA ques-
tion that has relevance only if we assume the Ninth Cir-
cuit correctly resolved the antecedent, unargued question
on which we granted certiorari. The Court is correct to
dismiss the first QP as improvidently granted.
   Why, one might ask, would a petitioner take a position
on a Circuit split that it had no intention of arguing, or at
least was so little keen to argue that it cast the argument
aside uninvited? The answer is simple. Petitioners in-
cluded that issue to induce us to grant certiorari. As the
Court rightly observes, there are numerous reasons why
we would not have agreed to hear petitioners’ first QP if
their petition for certiorari presented it in the same form
that it was argued on the merits. See ante, at 7–10. But it
is also true that there was little chance that we would
have taken this case to decide only the second, fact-bound
QP—that is, whether the individual petitioners are en-
titled to qualified immunity on respondent’s Fourth
Amendment claim.
   This Court’s Rule 10, entitled “Considerations Govern-
ing Review on Certiorari,” says that certiorari will be
granted “only for compelling reasons,” which include the
                     Cite as: 575 U. S. ____ (2015)                     3

          SCALIA, J., concurring
                          Opinioninof
                                    part and,dissenting
                                      SCALIA J.         in part

existence of conflicting decisions on issues of law among
federal courts of appeals, among state courts of last resort,
or between federal courts of appeals and state courts of
last resort. The Rule concludes: “A petition for a writ of
certiorari is rarely granted when the asserted error con-
sists of erroneous factual findings or the misapplication of
a properly stated rule of law.” The second QP implicates,
at most, the latter. It is unlikely that we would have
granted certiorari on that question alone.
   But (and here is what lies beneath the present case)
when we do grant certiorari on a question for which there
is a “compelling reason” for our review, we often also grant
certiorari on attendant questions that are not inde-
pendently “certworthy,” but that are sufficiently connected
to the ultimate disposition of the case that the efficient
administration of justice supports their consideration. In
other words, by promising argument on the Circuit conflict
that their first question presented, petitioners got us to
grant certiorari not only on the first question but also on
the second.
   I would not reward such bait-and-switch tactics by
proceeding to decide the independently “uncertworthy”
second question. And make no mistake about it: Today’s
judgment is a reward. It gives the individual petitioners
all that they seek, and spares San Francisco the signifi-
cant expense of defending the suit, and satisfying any
judgment, against the individual petitioners.* I would not
encourage future litigants to seek review premised on
arguments they never plan to press, secure in the
knowledge that once they find a toehold on this Court’s
docket, we will consider whatever workaday arguments
——————
   * San Francisco will still be subject to liability under the ADA if the
trial court determines that the facts demanded accommodation. The
Court of Appeals vacated the District Court’s judgment that the ADA
was inapplicable to police arrests of violent and armed disabled per-
sons, and remanded for the accommodation determination.
4          CITY AND COUNTY OF SAN FRANCISCO
                            v. SHEEHAN
        SCALIA, J., concurring
                        Opinion inof
                                   part and,dissenting
                                     SCALIA J.         in part

they choose to present in their merits briefs.
   There is no injustice in my vote to dismiss both ques-
tions as improvidently granted. To be sure, ex post—after
the Court has improvidently decided the uncertworthy
question—it appears that refusal to reverse the judgment
below would have left a wrong unrighted. Ex ante, how-
ever—before we considered and deliberated upon the second
QP but after petitioners’ principal brief made clear that
they would not address the Circuit conflict presented by
the first QP—we had no more assurance that this question
was decided incorrectly than we do for the thousands of
other uncertworthy questions we refuse to hear each
Term. Many of them have undoubtedly been decided
wrongly, but we are not, and for well over a century have
not been, a court of error correction. The fair course—the
just course—is to treat this now-nakedly uncertworthy
question the way we treat all others: by declining to decide
it. In fact, there is in this case an even greater reason to
decline: to avoid being snookered, and to deter future
snookering.
   Because I agree with the Court that “certiorari jurisdic-
tion exists to clarify the law,” ante, at 9 (emphasis added),
I would dismiss both questions presented as improvidently
granted.

```

---

## GROUP: _overhaul2/lake/cases/City of Canton v. Harris.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "City of Canton v. Harris"
type: case
citation: "489 U.S. 378 (1989)"
parallel_cite: "109 S. Ct. 1197; 103 L. Ed. 2d 412; 57 U.S.L.W. 4270"
neutral_cite: 1989 U.S. LEXIS 1200
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-02-28
docket: 86-1088
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-02-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Canton v. Harris
  varies_by_point: false
  scope_note: "Good law: the 'deliberate indifference' standard for municipal failure-to-train liability."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112209/city-of-canton-v-harris/"
  cluster_id: 112209
  opinion_id: 112209
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Monell v. Department of Social Services]]", "[[Pembaur v. City of Cincinnati]]", "[[Connick v. Thompson]]"]
aliases: ["Canton v. Harris", "City of Canton, Ohio v. Harris"]
tags: ["case", "section-1983", "municipal-liability", "failure-to-train", "deliberate-indifference", "monell"]
holding: "A municipality is liable under § 1983 for inadequate police training only where the failure to train amounts to deliberate indifference to the rights of persons with whom the police come into contact."
lake:
  record_id: City of Canton v. Harris
  status: verified
  projected_at: 2026-07-09
---

# City of Canton v. Harris

*489 U.S. 378 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Geraldine Harris was arrested and brought to the Canton, Ohio police station, where she slumped to the floor several times and behaved incoherently. Officers summoned no medical care; she was later diagnosed with emotional ailments requiring treatment. She sued the city under § 1983, claiming it had failed to train its officers on when to provide medical care to detainees in custody.

## Issue
Whether, and on what fault standard, a municipality can be held liable under § 1983 for a constitutional injury caused by its failure to adequately train its police officers.

## Rule
Failure-to-train liability requires [[Section 1983 Liability and Qualified Immunity|deliberate indifference]]. "We hold today that the inadequacy of police training may serve as the basis for § 1983 liability only where the failure to train amounts to deliberate indifference to the rights of persons with whom the police come into contact." — 489 U.S. at 388. ^pin-388

That high standard is met where "the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need." — [*Id.* at 390](https://www.courtlistener.com/opinion/112209/city-of-canton-v-harris/#:~:text=employees-,the%20need%20for%20more%20or%20different%20training%20is%20so%20obvious%2C%20and%20the%20inadequacy%20so%20likely%20to%20result%20in%20the%20violation%20of%20constitutional%20rights%2C%20that%20the%20policymakers%20of%20the%20city%20can%20reasonably%20be%20said%20to%20have%20been%20deliberately%20indifferent%20to%20the%20need.). ^pin-390

Only then does the training failure represent a municipal "policy" for which the city is responsible under *[[Monell v. Department of Social Services|Monell]]*.

## Application
Because the trial court's instructions had permitted liability on a theory closer to [[Common Legal Terms#respondeat-superior|respondeat superior]] than [[Section 1983 Liability and Qualified Immunity|deliberate indifference]], the Court could not sustain the verdict and [[Reading and Citing Cases#on-remand|remanded]]. The plaintiff would have to show that the city's failure to train reflected a deliberate or conscious choice — a policy of inaction in the face of an obvious need — and that the identified training deficiency actually caused her injury, not merely that an officer was unsatisfactorily trained or that better training could have avoided the harm.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. Inadequate training supports municipal § 1983 liability only on a showing of [[Section 1983 Liability and Qualified Immunity|deliberate indifference]], applied to the specific training deficiency that caused the constitutional injury.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Canton* builds on [[Monell v. Department of Social Services]] (policy-or-custom) and [[Pembaur v. City of Cincinnati]] (policymaker decisions) by defining the fault standard for inaction. Its "deliberate indifference" rule and the difficulty of proving it without a pattern were later underscored in [[Connick v. Thompson]]. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *City of Canton v. Harris*, 489 U.S. 378 (1989) — https://www.courtlistener.com/opinion/112209/city-of-canton-v-harris/ — pinpoints: 388, 390.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ca5f337add59c190", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "City of Canton v. Harris"}, "payload": {"all": [{"cite": "489 U.S. 378", "page": "378", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "489"}, {"cite": "109 S. Ct. 1197", "page": "1197", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "103 L. Ed. 2d 412", "page": "412", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "1989 U.S. LEXIS 1200", "page": "1200", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "57 U.S.L.W. 4270", "page": "4270", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}], "display": "489 U.S. 378", "official": {"cite": "489 U.S. 378", "page": "378", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "489"}, "official_selection_present": true, "record_id": "City of Canton v. Harris"}}
{"assertion_id": "6b1a7561567c4619", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-390", "record_id": "City of Canton v. Harris"}, "payload": {"fragment": "#:~:text=employees-,the%20need%20for%20more%20or%20different%20training%20is%20so%20obvious%2C%20and%20the%20inadequacy%20so%20likely%20to%20result%20in%20the%20violation%20of%20constitutional%20rights%2C%20that%20the%20policymakers%20of%20the%20city%20can%20reasonably%20be%20said%20to%20have%20been%20deliberately%20indifferent%20to%20the%20need.", "page": null, "pin_id": "pin-390", "pinpoint_status": "star-verified", "quote": "the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need.", "quote_fidelity": "matched", "record_id": "City of Canton v. Harris", "star_marker": "390"}}
{"assertion_id": "80628cd63f2ea2fd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-388", "record_id": "City of Canton v. Harris"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-388", "pinpoint_status": "slip-only", "quote": "--- # City of Canton v. Harris *489 U.S. 378 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Geraldine Harris was arrested and brought to the Canton, Ohio police station, where she slumped to the floor several times and behaved incoherently. Officers summoned no medical care; she was later diagnosed with emotional ailments requiring treatment. She sued the city under § 1983, claiming it had failed to train its officers on when to provide medical care to detainees in custody. ## Issue Whether, and on what fault standard, a municipality can be held liable under § 1983 for a constitutional injury caused by its failure to adequately train its police officers. ## Rule Failure-to-train liability requires deliberate indifference.", "quote_fidelity": "mismatch", "record_id": "City of Canton v. Harris", "star_marker": null}}
{"assertion_id": "7b0619a3eceb6a67", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "City of Canton v. Harris"}, "payload": {"as_of_content": "1989-02-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "City of Canton v. Harris", "scope_note": "Good law: the 'deliberate indifference' standard for municipal failure-to-train liability.", "varies_by_point": false}}
```

### lake record — City of Canton v. Harris

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Canton v. Harris",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Canton v. Harris",
    "case_name_short": "Canton",
    "case_name_full": "CITY OF CANTON, OHIO v. HARRIS Et Al.",
    "input_case_name": "City of Canton v. Harris",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-02-28",
    "year": 1989,
    "docket": "86-1088",
    "cluster_id": 112209,
    "lead_opinion_id": 112209,
    "sibling_ids": [
      112209,
      9431589,
      9431590,
      9431591
    ],
    "absolute_url": "/opinion/112209/city-of-canton-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 378",
      "volume": "489",
      "reporter": "U.S.",
      "page": "378",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1197",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1197",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 412",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4270",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4270",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1200",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 378",
        "volume": "489",
        "reporter": "U.S.",
        "page": "378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1197",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1197",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 412",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1200",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4270",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4270",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 378",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 378",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-388",
      "page": null,
      "quote": "--- # City of Canton v. Harris *489 U.S. 378 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Geraldine Harris was arrested and brought to the Canton, Ohio police station, where she slumped to the floor several times and behaved incoherently. Officers summoned no medical care; she was later diagnosed with emotional ailments requiring treatment. She sued the city under \u00a7 1983, claiming it had failed to train its officers on when to provide medical care to detainees in custody. ## Issue Whether, and on what fault standard, a municipality can be held liable under \u00a7 1983 for a constitutional injury caused by its failure to adequately train its police officers. ## Rule Failure-to-train liability requires deliberate indifference.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-390",
      "page": null,
      "quote": "the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need.",
      "star_marker": "390",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19335,
      "fragment": "#:~:text=employees-,the%20need%20for%20more%20or%20different%20training%20is%20so%20obvious%2C%20and%20the%20inadequacy%20so%20likely%20to%20result%20in%20the%20violation%20of%20constitutional%20rights%2C%20that%20the%20policymakers%20of%20the%20city%20can%20reasonably%20be%20said%20to%20have%20been%20deliberately%20indifferent%20to%20the%20need.",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-02-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Canton v. Harris",
    "varies_by_point": false,
    "scope_note": "Good law: the 'deliberate indifference' standard for municipal failure-to-train liability.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Alanda Forrest v. Kevin Parry",
          "cluster_id": 4638072,
          "cite": [
            "930 F.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gregory Baldwin v. City of Estherville, Iowa",
          "cluster_id": 4629600,
          "cite": [
            "929 N.W.2d 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Keyon Harrison v. Curt Vanderkooi",
          "cluster_id": 4522518,
          "cite": [
            "918 N.W.2d 785",
            "502 Mich. 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Farmer v. Brennan",
          "cluster_id": 1087956,
          "cite": [
            "128 L. Ed. 2d 811",
            "114 S. Ct. 1970",
            "511 U.S. 825",
            "1994 U.S. LEXIS 4274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of the County Commissioners of Bryan County v. Brown",
          "cluster_id": 118104,
          "cite": [
            "137 L. Ed. 2d 626",
            "117 S. Ct. 1382",
            "520 U.S. 397",
            "1997 U.S. LEXIS 2793",
            "65 U.S.L.W. 4286",
            "10 Fla. L. Weekly Fed. S 405",
            "12 I.E.R. Cas. (BNA) 1217",
            "97 Cal. Daily Op. Serv. 3033",
            "97 Daily Journal DAR 5311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Seiter",
          "cluster_id": 112626,
          "cite": [
            "115 L. Ed. 2d 271",
            "111 S. Ct. 2321",
            "501 U.S. 294",
            "1991 U.S. LEXIS 3490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. City of Harker Heights",
          "cluster_id": 112699,
          "cite": [
            "117 L. Ed. 2d 261",
            "112 S. Ct. 1061",
            "503 U.S. 115",
            "1992 U.S. LEXIS 1376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leatherman v. Tarrant County Narcotics Intelligence and Coordination Unit",
          "cluster_id": 112825,
          "cite": [
            "122 L. Ed. 2d 517",
            "113 S. Ct. 1160",
            "507 U.S. 163",
            "1993 U.S. LEXIS 1941",
            "61 U.S.L.W. 4205",
            "25 Fed. R. Serv. 3d 1",
            "93 Cal. Daily Op. Serv. 1493",
            "8 I.E.R. Cas. (BNA) 428",
            "7 Fla. L. Weekly Fed. S 40",
            "93 Daily Journal DAR 2747"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City of Los Angeles",
          "cluster_id": 7092482,
          "cite": [
            "250 F.3d 668",
            "2001 WL 468408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City Of Los Angeles",
          "cluster_id": 773312,
          "cite": [
            "250 F.3d 668",
            "2001 Cal. Daily Op. Serv. 3507",
            "2001 Daily Journal DAR 4351",
            "56 Fed. R. Serv. 698",
            "2001 U.S. App. LEXIS 8150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christopher J. Weiland v. Palm Beach County Sheriff's Office",
          "cluster_id": 2815299,
          "cite": [
            "792 F.3d 1313",
            "92 Fed. R. Serv. 3d 378",
            "2015 U.S. App. LEXIS 11750",
            "2015 WL 4098270"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jett v. Dallas Independent School District",
          "cluster_id": 112313,
          "cite": [
            "105 L. Ed. 2d 598",
            "109 S. Ct. 2702",
            "491 U.S. 701",
            "1989 U.S. LEXIS 3130",
            "57 U.S.L.W. 4858",
            "50 Fair Empl. Prac. Cas. (BNA) 27",
            "50 Empl. Prac. Dec. (CCH) 39,070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John C. McGuckin v. Dr. Smith John C. Medlen, Dr.",
          "cluster_id": 590324,
          "cite": [
            "974 F.2d 1050",
            "92 Cal. Daily Op. Serv. 7224",
            "23 Fed. R. Serv. 3d 922",
            "92 Daily Journal DAR 11690",
            "1992 U.S. App. LEXIS 19402",
            "1992 WL 201087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis Ex Rel. LaShonda D. v. Monroe County Board of Education",
          "cluster_id": 118290,
          "cite": [
            "143 L. Ed. 2d 839",
            "119 S. Ct. 1661",
            "526 U.S. 629",
            "1999 U.S. LEXIS 3452",
            "12 Fla. L. Weekly Fed. S 280",
            "67 U.S.L.W. 4329",
            "1999 Colo. J. C.A.R. 2948",
            "99 Cal. Daily Op. Serv. 3861",
            "99 Daily Journal DAR 4931"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James C. Dunkel",
          "cluster_id": 557241,
          "cite": [
            "927 F.2d 955",
            "67 A.F.T.R.2d (RIA) 637",
            "1991 U.S. App. LEXIS 3599",
            "1991 WL 28790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alfredo Miranda v. County of Lake",
          "cluster_id": 4525558,
          "cite": [
            "900 F.3d 335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gebser v. Lago Vista Independent School District",
          "cluster_id": 118232,
          "cite": [
            "141 L. Ed. 2d 277",
            "118 S. Ct. 1989",
            "524 U.S. 274",
            "1998 U.S. LEXIS 4173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Piotrowski v. City of Houston",
          "cluster_id": 22972,
          "cite": [
            "237 F.3d 567",
            "2001 U.S. App. LEXIS 603",
            "2001 WL 6712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tjymas Blackmore v. Kalamazoo County",
          "cluster_id": 788501,
          "cite": [
            "390 F.3d 890",
            "2004 U.S. App. LEXIS 25057",
            "2004 WL 2792016"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Philomene Long, Surviving Spouse and Heir-At-Law of John Thomas Idlet, Deceased v. County of Los Angeles",
          "cluster_id": 793848,
          "cite": [
            "442 F.3d 1178",
            "2006 U.S. App. LEXIS 7552",
            "2006 WL 770615"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kneipp v. Tedder",
          "cluster_id": 726573,
          "cite": [
            "95 F.3d 1199",
            "159 A.L.R. Fed. 619",
            "1996 U.S. App. LEXIS 24401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grieveson v. Anderson",
          "cluster_id": 1443143,
          "cite": [
            "538 F.3d 763",
            "2008 WL 3823872"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howlett Ex Rel. Howlett v. Rose",
          "cluster_id": 112456,
          "cite": [
            "110 L. Ed. 2d 332",
            "110 S. Ct. 2430",
            "496 U.S. 356",
            "1990 U.S. LEXIS 3077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott L. Matthews v. Leon E. Jones, Sr., Jefferson County Police Department, and Unknown Police Officer, Jefferson County Police Department",
          "cluster_id": 678528,
          "cite": [
            "35 F.3d 1046",
            "1994 U.S. App. LEXIS 25924",
            "1994 WL 509049"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Everson v. Leis",
          "cluster_id": 1464717,
          "cite": [
            "556 F.3d 484",
            "2009 U.S. App. LEXIS 3288",
            "2009 WL 414625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTE0NDE5MjAwMDAwJnM9NzMyODI4MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112209+OR+9431589+OR+9431590+OR+9431591%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MTImcz0xNTYyOTMmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112209+OR+9431589+OR+9431590+OR+9431591%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591)",
        "reviewed": 85,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 85,
        "triage_read": 0,
        "triage_snippet_classified": 85
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591)",
    "indexed_citing_opinions": 3328,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112209,
        "count": 2907,
        "count_source": "search"
      },
      {
        "opinion_id": 9431589,
        "count": 451,
        "count_source": "search"
      },
      {
        "opinion_id": 9431590,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431591,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 10152,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-canton-v-harris.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MTI0OCZzPTEwNjE1NDQyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112209+OR+9431589+OR+9431590+OR+9431591%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112209,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 110076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 110589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 110998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111615,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 112017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 366970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 392242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 398831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 414191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 424798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 424905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 447620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 453103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 459876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 460084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 462512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 464799,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 469366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 480385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 487192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 489887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 492036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 501192,
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
    "date_created": "2026-07-05T00:11:30Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:11:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:11:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:17:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:11:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Canton v. Harris

```
<div>
<center><b><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">489 U.S. 378</a></span> (1989)</b></center>
<center><h1>CITY OF CANTON, OHIO<br>
v.<br>
HARRIS ET AL.</h1></center>
<center>No. 86-1088.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 8, 1988</center>
<center>Decided February 28, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT
<p><span class="star-pagination">*380</span> <i>Carter G. Phillips</i> argued the cause for petitioner. With him on the briefs were <i>Mark D. Hopson, W. Scott Gwin, William J. Hamann,</i> and <i>John S. Coury.</i></p>
<p><i>David Rudovsky</i> argued the cause for respondent. With him on the brief were <i>Emanuella Harris Groves</i> and <i>Dexter W. Clark.</i><sup>[*]</sup></p>
<p><i>John A. Powell, Steven R. Shapiro, Howard A. Friedman,</i> and <i>Michael Aaron Avery</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>JUSTICE WHITE delivered the opinion of the Court.</p>
<p>In this case, we are asked to determine if a municipality can ever be liable under <span class="citation no-link">42 U. S. C. § 1983</span><sup>[1]</sup> for constitutional violations resulting from its failure to train municipal employees. We hold that, under certain circumstances, such liability is permitted by the statute.</p>
<p></p>
<h2>
<span class="star-pagination">*381</span> I</h2>
<p>In April 1978, respondent Geraldine Harris was arrested by officers of the Canton Police Department. Mrs. Harris was brought to the police station in a patrol wagon.</p>
<p>When she arrived at the station, Mrs. Harris was found sitting on the floor of the wagon. She was asked if she needed medical attention, and responded with an incoherent remark. After she was brought inside the station for processing, Mrs. Harris slumped to the floor on two occasions. Eventually, the police officers left Mrs. Harris lying on the floor to prevent her from falling again. No medical attention was ever summoned for Mrs. Harris. After about an hour, Mrs. Harris was released from custody, and taken by an ambulance (provided by her family) to a nearby hospital. There, Mrs. Harris was diagnosed as suffering from several emotional ailments; she was hospitalized for one week and received subsequent outpatient treatment for an additional year.</p>
<p>Some time later, Mrs. Harris commenced this action alleging many state-law and constitutional claims against the city of Canton and its officials. Among these claims was one seeking to hold the city liable under <span class="citation no-link">42 U. S. C. § 1983</span> for its violation of Mrs. Harris' right, under the Due Process Clause of the Fourteenth Amendment, to receive necessary medical attention while in police custody.</p>
<p>A jury trial was held on Mrs. Harris' claims. Evidence was presented that indicated that, pursuant to a municipal regulation,<sup>[2]</sup> shift commanders were authorized to determine, in their sole discretion, whether a detainee required medical <span class="star-pagination">*382</span> care. Tr. X-XXX-X-XXX. In addition, testimony also suggested that Canton shift commanders were not provided with any special training (beyond first-aid training) to make a determination as to when to summon medical care for an injured detainee. <i>Ibid.;</i> App. to Pet. for Cert. 4a.</p>
<p>At the close of the evidence, the District Court submitted the case to the jury, which rejected all of Mrs. Harris' claims except one: her § 1983 claim against the city resulting from its failure to provide her with medical treatment while in custody. In rejecting the city's subsequent motion for judgment notwithstanding the verdict, the District Court explained the theory of liability as follows:</p>
<blockquote>"The evidence construed in a manner most favorable to Mrs. Harris could be found by a jury to demonstrate that the City of Canton had a custom or policy of vesting complete authority with the police supervisor of when medical treatment would be administered to prisoners. Further, the jury could find from the evidence that the vesting of such <i>carte blanche</i> authority with the police supervisor without adequate training to recognize when medical treatment is needed was grossly negligent or so reckless that future police misconduct was almost inevitable or substantially certain to result." <i>Id.,</i> at 16a.</blockquote>
<p>On appeal, the Sixth Circuit affirmed this aspect of the District Court's analysis, holding that "a municipality is liable for failure to train its police force, [where] the plaintiff . . . prove[s] that the municipality acted recklessly, intentionally, or with gross negligence." <i>Id.,</i> at 5a.<sup>[3]</sup> The Court of Appeals also stated that an additional prerequisite of this theory <span class="star-pagination">*383</span> of liability was that the plaintiff must prove "that the lack of training was so reckless or grossly negligent that deprivations of persons' constitutional rights were substantially certain to result." <i>Ibid.</i> Thus, the Court of Appeals found that there had been no error in submitting Mrs. Harris' "failure to train" claim to the jury. However, the Court of Appeals reversed the judgment for respondent, and remanded this case for a new trial, because it found that certain aspects of the District Court's jury instructions might have led the jury to believe that it could find against the city on a mere <i>respondeat superior</i> theory. Because the jury's verdict did not state the basis on which it had ruled for Mrs. Harris on her § 1983 claim, a new trial was ordered.</p>
<p>The city petitioned for certiorari, arguing that the Sixth Circuit's holding represented an impermissible broadening of municipal liability under § 1983. We granted the petition. <span class="citation multiple-matches"><a href="/c/U.%20S./485/933/">485 U. S. 933</a></span> (1988).</p>
<p></p>
<h2>II</h2>
<p>We first address respondent's contention that the writ of certiorari should be dismissed as improvidently granted, because "petitioner failed to preserve for review the principal issues it now argues in this Court." Brief for Respondent 5.</p>
<p>We think it clear enough that petitioner's three "Questions Presented" in its petition for certiorari encompass the critical question before us in this case: Under what circumstances can inadequate training be found to be a "policy" that is actionable under § 1983? See Pet. for Cert. i. The petition itself addressed this issue directly, attacking the Sixth Circuit's "failure to train" theory as inconsistent with this Court's precedents. See <i>id.,</i> at 8-12. It is also clear  as respondent conceded at argument, Tr. of Oral Arg. 34, 54  that her brief in opposition to our granting of certiorari did not raise the objection that petitioner had failed to press its claims on the courts below.</p>
<p>As to respondent's contention that the claims made by petitioner here were not made in the same fashion below, that <span class="star-pagination">*384</span> failure, if it occurred, does not affect our jurisdiction; and because respondent did not oppose our grant of review at that time based on her contention that these claims were not pressed below, we will not dismiss the writ as improvidently granted. "[T]he `decision to grant certiorari represents a commitment of scarce judicial resources with a view to deciding the merits . . . of the questions presented in the petition.' " <i>St. Louis</i> v. <i>Praprotnik,</i> <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#120" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112, 120</a></span> (1988) (quoting <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#816" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 816</a></span> (1985)). As we have expressly admonished litigants in respondent's position: "Nonjurisdictional defects of this sort should be brought to our attention <i>no later</i> than in respondent's brief in opposition to the petition for certiorari; if not, we consider it within our discretion to deem the defect waived." <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#816" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 816</a></span>.</p>
<p>It is true that petitioner's litigation posture with respect to the questions presented here has not been consistent; most importantly, petitioner conceded below that " `inadequate training' [is] a means of establishing municipal liability under Section 1983." Reply Brief for Petitioner 4, n. 3; see also Petition for Rehearing in No. 85-3314 (CA6), p. 1. However, at each stage in the proceedings below, petitioner contested any finding of liability on this ground, with objections of varying specificity. It opposed the District Court's jury instructions on this issue, Tr. 4-369; claimed in its judgment notwithstanding verdict motion that there was "no evidence of a . . . policy or practice on the part of the City . . . [of] den[ying] medical treatment to prisoners," Motion for Judgment Notwithstanding Verdict in No. C80-18-A (ND Ohio), p. 1; and argued to the Court of Appeals that there was no basis for finding a policy of denying medical treatment to prisoners in this case. See Brief for Appellant in No. 85-3314 (CA6), pp. 26-29. Indeed, petitioner specifically contended that the Sixth Circuit precedents that permitted inadequate training to be a basis for municipal liability on facts similar to these, see n. 3, <i>supra,</i> were in conflict with <span class="star-pagination">*385</span> our decision in <i><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span>.</i> Brief for Appellant in No. 85-3314 (CA6), p. 29. These various presentations of the issues below might have been so inexact that we would have denied certiorari had this matter been brought to our attention at the appropriate stage in the proceedings. But they were at least adequate to yield a decision by the Sixth Circuit on the questions presented for our review now.</p>
<p>Here the Sixth Circuit held that where a plaintiff proves that a municipality, acting recklessly, intentionally, or with gross negligence, has failed to train its police force  resulting in a deprivation of constitutional rights that was "substantially certain to result"  § 1983 permits that municipality to be held liable for its actions. Petitioner's petition for certiorari challenged the soundness of that conclusion, and respondent did not inform us prior to the time that review was granted that petitioner had arguably conceded this point below. Consequently, we will not abstain from addressing the question before us.</p>
<p></p>
<h2>III</h2>
<p>In <i>Monell</i> v. <i>New York City Dept. of Social Services,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), we decided that a municipality can be found liable under § 1983 only where the municipality <i>itself</i> causes the constitutional violation at issue. <i>Respondeat superior</i> or vicarious liability will not attach under § 1983. <i>Id.,</i> at 694-695. "It is only when the `execution of the government's policy or custom . . . inflicts the injury' that the municipality may be held liable under § 1983." <i>Springfield</i> v. <i>Kibbe,</i> <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#267" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257, 267</a></span> (1987) (O'CONNOR, J., dissenting) (quoting <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><i>Monell, supra,</i> at 694</a></span>).</p>
<p>Thus, our first inquiry in any case alleging municipal liability under § 1983 is the question whether there is a direct causal link between a municipal policy or custom and the alleged constitutional deprivation. The inquiry is a difficult one; one that has left this Court deeply divided in a series of <span class="star-pagination">*386</span> cases that have followed <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>;</i><sup>[4]</sup> one that is the principal focus of our decision again today.</p>
<p></p>
<h2>A</h2>
<p>Based on the difficulty that this Court has had defining the contours of municipal liability in these circumstances, petitioner urges us to adopt the rule that a municipality can be found liable under § 1983 only where "the policy in question [is] itself unconstitutional." Brief for Petitioner 15. Whether such a rule is a valid construction of § 1983 is a question the Court has left unresolved. See, <i>e. g., </i><i>St. Louis</i> v. <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#147" aria-description="Citation for case: City of St. Louis v. Praprotnik"><i>Praprotnik, supra,</i> at 147</a></span> (BRENNAN, J., concurring in judgment); <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#824" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 824, n. 7</a></span>. Under such an approach, the outcome here would be rather clear: we would have to reverse and remand the case with instructions that judgment be entered for petitioner.<sup>[5]</sup> There can be little doubt that on its face the city's policy regarding medical treatment for detainees is constitutional. The policy states that the city jailer "shall . . . have [a person needing medical care] taken to a hospital for medical treatment, with <span class="star-pagination">*387</span> permission of his supervisor . . . ." App. 33. It is difficult to see what constitutional guarantees are violated by such a policy.</p>
<p>Nor, without more, would a city automatically be liable under § 1983 if one of its employees happened to apply the policy in an unconstitutional manner, for liability would then rest on <i>respondeat superior.</i> The claim in this case, however, is that if a concededly valid policy is unconstitutionally applied by a municipal employee, the city is liable if the employee has not been adequately trained and the constitutional wrong has been caused by that failure to train. For reasons explained below, we conclude, as have all the Courts of Appeals that have addressed this issue,<sup>[6]</sup> that there are limited circumstances in which an allegation of a "failure to train" can be the basis for liability under § 1983. Thus, we reject petitioner's contention that only unconstitutional policies are actionable under the statute.</p>
<p></p>
<h2>
<span class="star-pagination">*388</span> B</h2>
<p>Though we agree with the court below that a city can be liable under § 1983 for inadequate training of its employees, we cannot agree that the District Court's jury instructions on this issue were proper, for we conclude that the Court of Appeals provided an overly broad rule for when a municipality can be held liable under the "failure to train" theory. Unlike the question whether a municipality's failure to train employees can ever be a basis for § 1983 liability  on which the Courts of Appeals have all agreed, see n. 6, <i>supra,</i>  there is substantial division among the lower courts as to what <i>degree of fault</i> must be evidenced by the municipality's inaction before liability will be permitted.<sup>[7]</sup> We hold today that the inadequacy of police training may serve as the basis for § 1983 liability only where the failure to train amounts to deliberate indifference to the rights of persons with whom the police come into contact.<sup>[8]</sup> This rule is most consistent with our admonition <span class="star-pagination">*389</span> in <i>Monell,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 694</a></span>, and <i>Polk County</i> v. <i>Dodson,</i> <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/#326" aria-description="Citation for case: Polk County v. Dodson">454 U. S. 312, 326</a></span> (1981), that a municipality can be liable under § 1983 only where its policies are the "moving force [behind] the constitutional violation." Only where a municipality's failure to train its employees in a relevant respect evidences a "deliberate indifference" to the rights of its inhabitants can such a shortcoming be properly thought of as a city "policy or custom" that is actionable under § 1983. As JUSTICE BRENNAN's opinion in <i>Pembaur</i> v. <i>Cincinnati,</i> <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#483" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S. 469, 483-484</a></span> (1986) (plurality) put it: "[M]unicipal liability under § 1983 attaches where  and only where  a deliberate choice to follow a course of action is made from among various alternatives" by city policymakers. See also <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823</a></span> (opinion of REHNQUIST, J.). Only where a failure to train reflects a "deliberate" or "conscious" choice by a municipality  a "policy" as defined by our prior cases  can a city be liable for such a failure under § 1983.</p>
<p><i>Monell's</i> rule that a city is not liable under § 1983 unless a municipal policy causes a constitutional deprivation will not be satisfied by merely alleging that the existing training program for a class of employees, such as police officers, represents a policy for which the city is responsible.<sup>[9]</sup> That much <span class="star-pagination">*390</span> may be true. The issue in a case like this one, however, is whether that training program is adequate; and if it is not, the question becomes whether such inadequate training can justifiably be said to represent "city policy." It may seem contrary to common sense to assert that a municipality will actually have a policy of not taking reasonable steps to train its employees. But it may happen that in light of the duties assigned to specific officers or employees the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need.<sup>[10]</sup> In that event, the failure to provide proper training may fairly be said to represent a policy for which the city is responsible, and for which the city may be held liable if it actually causes injury.<sup>[11]</sup></p>
<p>In resolving the issue of a city's liability, the focus must be on adequacy of the training program in relation to the tasks the particular officers must perform. That a particular officer may be unsatisfactorily trained will not alone suffice to fasten liability on the city, for the officer's shortcomings may <span class="star-pagination">*391</span> have resulted from factors other than a faulty training program. See <i>Springfield</i> v. <i>Kibbe,</i> <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#268" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S., at 268</a></span> (O'CONNOR, J., dissenting); <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#821" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 821</a></span> (opinion of REHNQUIST, J.). It may be, for example, that an otherwise sound program has occasionally been negligently administered. Neither will it suffice to prove that an injury or accident could have been avoided if an officer had had better or more training, sufficient to equip him to avoid the particular injury-causing conduct. Such a claim could be made about almost any encounter resulting in injury, yet not condemn the adequacy of the program to enable officers to respond properly to the usual and recurring situations with which they must deal. And plainly, adequately trained officers occasionally make mistakes; the fact that they do says little about the training program or the legal basis for holding the city liable.</p>
<p>Moreover, for liability to attach in this circumstance the identified deficiency in a city's training program must be closely related to the ultimate injury. Thus in the case at hand, respondent must still prove that the deficiency in training actually caused the police officers' indifference to her medical needs.<sup>[12]</sup> Would the injury have been avoided had the employee been trained under a program that was not deficient in the identified respect? Predicting how a hypothetically well-trained officer would have acted under the circumstances may not be an easy task for the factfinder, particularly since matters of judgment may be involved, and since officers who are well trained are not free from error and perhaps might react very much like the untrained officer in similar circumstances. But judge and jury, doing their respective jobs, will be adequate to the task.</p>
<p>To adopt lesser standards of fault and causation would open municipalities to unprecedented liability under § 1983. <span class="star-pagination">*392</span> In virtually every instance where a person has had his or her constitutional rights violated by a city employee, a § 1983 plaintiff will be able to point to something the city "could have done" to prevent the unfortunate incident. See <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823</a></span> (opinion of REHNQUIST, J.). Thus, permitting cases against cities for their "failure to train" employees to go forward under § 1983 on a lesser standard of fault would result in <i>de facto respondeat superior</i> liability on municipalities  a result we rejected in <i>Monell,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#693" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 693-694</a></span>. It would also engage the federal courts in an endless exercise of second-guessing municipal employee-training programs. This is an exercise we believe the federal courts are ill suited to undertake, as well as one that would implicate serious questions of federalism. Cf. <i>Rizzo</i> v. <i>Goode,</i> <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#378" aria-description="Citation for case: Rizzo v. Goode">423 U. S. 362, 378-380</a></span> (1976).</p>
<p>Consequently, while claims such as respondent's  alleging that the city's failure to provide training to municipal employees resulted in the constitutional deprivation she suffered  are cognizable under § 1983, they can only yield liability against a municipality where that city's failure to train reflects deliberate indifference to the constitutional rights of its inhabitants.</p>
<p></p>
<h2>IV</h2>
<p>The final question here is whether this case should be remanded for a new trial, or whether, as petitioner suggests, we should conclude that there are no possible grounds on which respondent can prevail. See Tr. of Oral Arg. 57-58. It is true that the evidence in the record now does not meet the standard of § 1983 liability we have set forth above. But, the standard of proof the District Court ultimately imposed on respondent (which was consistent with Sixth Circuit precedent) was a lesser one than the one we adopt today, see Tr. X-XXX-X-XXX. Whether respondent should have an opportunity to prove her case under the "deliberate indifference" rule we have adopted is a matter for the Court of Appeals to deal with on remand.</p>
<p></p>
<h2>
<span class="star-pagination">*393</span> V</h2>
<p>Consequently, for the reasons given above, we vacate the judgment of the Court of Appeals and remand this case for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BRENNAN, concurring.</p>
<p>The Court's opinion, which I join, makes clear that the Court of Appeals is free to remand this case for a new trial.</p>
<p>JUSTICE O'CONNOR, with whom JUSTICE SCALIA and JUSTICE KENNEDY join, concurring in part and dissenting in part.</p>
<p>I join Parts I and II and all of Part III of the Court's opinion except footnote 11, see <i>ante,</i> at 390, n. 11. I thus agree that where municipal policymakers are confronted with an obvious need to train city personnel to avoid the violation of constitutional rights and they are deliberately indifferent to that need, the lack of necessary training may be appropriately considered a city "policy" subjecting the city itself to liability under our decision in <i>Monell</i> v. <i>New York City Dept. of Social Services,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978). As the Court observes, "[o]nly where a failure to train reflects a `deliberate' or `conscious' choice by a municipality  a `policy' as defined by our prior cases  can a city be liable for such a failure under [42 U. S. C.] § 1983." <i>Ante,</i> at 389. I further agree that a § 1983 plaintiff pressing a "failure to train" claim must prove that the lack of training was the "cause" of the constitutional injury at issue and that this entails more than simply showing "but for" causation. <i>Ante,</i> at 392. Lesser requirements of fault and causation in this context would "open municipalities to unprecedented liability under § 1983," <i>ante,</i> at 391, and would pose serious federalism concerns. <i>Ante,</i> at 392.</p>
<p>My single point of disagreement with the majority is thus a small one. Because I believe, as the majority strongly hints, <span class="star-pagination">*394</span> see <i>ibid.,</i> that respondent has not and could not satisfy the fault and causation requirements we adopt today, I think it unnecessary to remand this case to the Court of Appeals for further proceedings. This case comes to us after a full trial during which respondent vigorously pursued numerous theories of municipal liability including an allegation that the city had a "custom" of not providing medical care to detainees suffering from emotional illnesses. Respondent thus had every opportunity and incentive to adduce the type of proof necessary to satisfy the deliberate indifference standard we adopt today. Rather than remand in this context, I would apply the deliberate indifference standard to the facts of this case. After undertaking that analysis below, I conclude that there is no evidence in the record indicating that the city of Canton has been deliberately indifferent to the constitutional rights of pretrial detainees.</p>
<p></p>
<h2>I</h2>
<p>In <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> the Court held that municipal liability can be imposed under § 1983 only where the municipality, as an entity, can be said to be "responsible" for a constitutional violation committed by one of its employees. "[T]he touchstone of the § 1983 action against a government body is an allegation that official policy is responsible for a deprivation of rights protected by the Constitution." <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 690</a></span>. The Court found that the language of § 1983, and rejection of the "Sherman Amendment" by the 42d Congress, were both strong indicators that the framers of the Civil Rights Act of 1871 did not intend that municipal governments be held vicariously liable for the constitutional torts of their employees. Thus a § 1983 plaintiff seeking to attach liability to the city for the acts of one of its employees may not rest on the employment relationship alone; both fault and causation <i>as to the acts or omissions of the city itself</i> must be proved. The Court reaffirms these requirements today.</p>
<p>Where, as here, a claim of municipal liability is predicated upon a failure to act, the requisite degree of fault must be <span class="star-pagination">*395</span> shown by proof of a background of events and circumstances which establish that the "policy of inaction" is the functional equivalent of a decision by the city itself to violate the Constitution. Without some form of notice to the city, and the opportunity to conform to constitutional dictates both what it does and what it chooses not to do, the failure to train theory of liability could completely engulf <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> imposing liability without regard to fault. Moreover, absent a requirement that the lack of training at issue bear a very close causal connection to the violation of constitutional rights, the failure to train theory of municipal liability could impose "prophylactic" duties on municipal governments only remotely connected to underlying constitutional requirements themselves.</p>
<p>Such results would be directly contrary to the intent of the drafters of § 1983. The central vice of the Sherman Amendment, as noted by the Court's opinion in <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> was that it "impose[d] a species of vicarious liability on municipalities since it could be construed to impose liability even if the municipality <i>did not know</i> of an impending or ensuing riot or did not have the wherewithal to do anything about it." <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#692" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 692, n. 57</a></span> (emphasis added). Moreover, as noted in <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> the authors of § 1 of the Ku Klux Act did not intend to create any new rights or duties beyond those contained in the Constitution. <i>Id.,</i> at 684-685. Thus, § 1 was referred to as "reenacting the Constitution." Cong. Globe, 42d Cong., 1st Sess., 569 (1871) (Rep. Edmunds). Representative Bingham, the author of § 1 of the Fourteenth Amendment, saw the purpose of § 1983 as "the enforcement . . . of the Constitution on behalf of every individual citizen of the Republic . . . to the extent of the rights guaranteed to him by the Constitution." <i>Id.,</i> at App. 81. See also <i>Chapman</i> v. <i>Houston Welfare Rights Organization,</i> <span class="citation" data-id="9427567"><a href="/opinion/110076/chapman-v-houston-welfare-rights-organization/#617" aria-description="Citation for case: Chapman v. Houston Welfare Rights Organization">441 U. S. 600, 617</a></span> (1979) ("[Section] 1 of the Civil Rights Act of 1871 did not provide for any substantive rights  equal or otherwise. As introduced and enacted, it served only to insure that an individual had a cause of action for violations of the Constitution"). <span class="star-pagination">*396</span> Thus § 1983 is not a "federal good government act" for municipalities. Rather it creates a federal cause of action against persons, including municipalities, who deprive citizens of the United States of their constitutional rights.</p>
<p>Sensitive to these concerns, the Court's opinion correctly requires a high degree of fault on the part of city officials before an omission that is not in itself unconstitutional can support liability as a municipal policy under <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>.</i> As the Court indicates, "it may happen that . . . the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need." <i>Ante,</i> at 390. Where a § 1983 plaintiff can establish that the facts available to city policymakers put them on actual or constructive notice that the particular omission is substantially certain to result in the violation of the constitutional rights of their citizens, the dictates of <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span></i> are satisfied. Only then can it be said that the municipality has made " `a deliberate choice to follow a course of action . . . from among various alternatives.' " <i>Ante,</i> at 389, quoting <i>Pembaur</i> v. <i>Cincinnati,</i> <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#483" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S. 469, 483-484</a></span> (1986).</p>
<p>In my view, it could be shown that the need for training was obvious in one of two ways. First, a municipality could fail to train its employees concerning a clear constitutional duty implicated in recurrent situations that a particular employee is certain to face. As the majority notes, see <i>ante,</i> at 390, n. 10, the constitutional limitations established by this Court on the use of deadly force by police officers present one such situation. The constitutional duty of the individual officer is clear, and it is equally clear that failure to inform city personnel of that duty will create an extremely high risk that constitutional violations will ensue.</p>
<p>The claim in this case  that police officers were inadequately trained in diagnosing the symptoms of emotional illness  falls far short of the kind of "obvious" need for training <span class="star-pagination">*397</span> that would support a finding of deliberate indifference to constitutional rights on the part of the city. As the Court's opinion observes, <i>ante,</i> at 388-389, n. 8, this Court has not yet addressed the precise nature of the obligations that the Due Process Clause places upon the police to seek medical care for pretrial detainees who have been <i>physically</i> injured while being apprehended by the police. See <i>Revere</i> v. <i>Massachusetts General Hospital,</i> <span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/#246" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">463 U. S. 239, 246</a></span> (1983) (REHNQUIST, J., concurring). There are thus no clear constitutional guideposts for municipalities in this area, and the diagnosis of mental illness is not one of the "usual and recurring situations with which [the police] must deal." <i>Ante,</i> at 391. The lack of training at issue here is not the kind of omission that can be characterized, in and of itself, as a "deliberate indifference" to constitutional rights.</p>
<p>Second, I think municipal liability for failure to train may be proper where it can be shown that policymakers were aware of, and acquiesced in, a pattern of constitutional violations involving the exercise of police discretion. In such cases, the need for training may not be obvious from the outset, but a pattern of constitutional violations could put the municipality on notice that its officers confront the particular situation on a regular basis, and that they often react in a manner contrary to constitutional requirements. The lower courts that have applied the "deliberate indifference" standard we adopt today have required a showing of a pattern of violations from which a kind of "tacit authorization" by city policymakers can be inferred. See, <i>e. g., </i><i>Fiacco</i> v. <i>Rensselaer,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/783/319/">783 F. 2d 319</a></span>, 327 (CA2 1986) (multiple incidents required for finding of deliberate indifference); <i>Patzner</i> v. <i>Burkett,</i> <span class="citation" data-id="462512"><a href="/opinion/462512/leland-patzner-v-joyce-burkett-aka-joyce-mclaughlin-deborah-myerchin-and/#1367" aria-description="Citation for case: Leland Patzner v. Joyce Burkett A/K/A Joyce McLaughlin...">779 F. 2d 1363, 1367</a></span> (CA8 1985) ("[A] municipality may be liable if it had notice of prior misbehavior by its officers and failed to take remedial steps amounting to deliberate indifference to the offensive acts"); <i>Languirand</i> v. <i>Hayden,</i> <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#227" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an...">717 F. 2d 220, 227-228</a></span> (CA5 1983) (municipal liability for failure to train requires "evidence at least of a pattern of similar <span class="star-pagination">*398</span> incidents in which citizens were injured or endangered"); <i>Wellington</i> v. <i>Daniels,</i> <span class="citation" data-id="424905"><a href="/opinion/424905/cynthia-wellington-guardian-of-the-estate-of-robert-d-gravelle-v-brian/#936" aria-description="Citation for case: Cynthia Wellington, Guardian of the Estate of Robert D....">717 F. 2d 932, 936</a></span> (CA4 1983) ("[A] failure to supervise gives rise to § 1983 liability, however, only in those situations where there is a history of widespread abuse. Only then may knowledge be imputed to the supervisory personnel").</p>
<p>The Court's opinion recognizes this requirement, see <i>ante,</i> at 390, and n. 10, but declines to evaluate the evidence presented in this case in light of the new legal standard. <i>Ante,</i> at 392. From the outset of this litigation, respondent has pressed a claim that the city of Canton had a custom of denying medical care to pretrial detainees with emotional disorders. See Amended Complaint ¶ 28, App. 27. Indeed, up to and including oral argument before this Court, counsel for respondent continued to assert that respondent was attempting to hinge municipal liability upon "both a custom of denying medical care to a certain class of prisoners, and a failure to train police that led to this particular violation." Tr. of Oral Arg. 37-38. At the time respondent filed her complaint in 1980, it was clear that proof of the existence of a custom entailed a showing of "practices . . . so permanent and well settled as to constitute a `custom or usage' with the force of law." <i>Adickes</i> v. <i>S. H. Kress &amp; Co.,</i> <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#168" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 168</a></span> (1970); see also <i>Garner</i> v. <i>Memphis Police Department,</i> <span class="citation" data-id="366970"><a href="/opinion/366970/garner-v-memphis-police-department/#54" aria-description="Citation for case: Garner v. Memphis Police Department">600 F. 2d 52, 54-55</a></span>, and n. 4 (CA6 1979) (discussing proof of custom in light of <i>Monell</i>).</p>
<p>Whatever the prevailing standard at the time concerning liability for failure to train, respondent thus had every incentive to adduce proof at trial of a pattern of violations to support her claim that the city had an unwritten custom of denying medical care to emotionally ill detainees. In fact, respondent presented no testimony from any witness indicating that there had been past incidents of "deliberate indifference" to the medical needs of emotionally disturbed detainees or that any other circumstance had put the city on actual or constructive notice of a need for additional training in this <span class="star-pagination">*399</span> regard. At trial, David Maser, who was Chief of Police of the city of Canton from 1971 to 1980, testified without contradiction that during his tenure he received no complaints that detainees in the Canton jails were not being accorded proper medical treatment. Tr. 4-347  4-348. Former Officer Cherry, who had served as a jailer for the Canton Police Department, indicated that he had never had to seek medical treatment for persons who were emotionally upset at the prospect of arrest, because they usually calmed down when a member of the department spoke with them or one of their family members arrived. <i><span class="citation" data-id="366970"><a href="/opinion/366970/garner-v-memphis-police-department/" aria-description="Citation for case: Garner v. Memphis Police Department">Id.,</a></span></i> at 4-83  4-84. There is quite simply nothing in this record to indicate that the city of Canton had any reason to suspect that failing to provide this kind of training would lead to injuries of any kind, let alone violations of the Due Process Clause. None of the Courts of Appeals that already apply the standard we adopt today would allow respondent to take her claim to a jury based on the facts she adduced at trial. See <i>Patzner</i> v. <span class="citation" data-id="462512"><a href="/opinion/462512/leland-patzner-v-joyce-burkett-aka-joyce-mclaughlin-deborah-myerchin-and/#1367" aria-description="Citation for case: Leland Patzner v. Joyce Burkett A/K/A Joyce McLaughlin..."><i>Burkett, supra,</i> at 1367</a></span> (summary judgment proper under "deliberate indifference" standard where evidence of only single incident adduced); <i>Languirand</i> v. <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#229" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an..."><i>Hayden, supra,</i> at 229</a></span> (reversing jury verdict rendered under failure to train theory where there was no evidence of prior incidents to support a finding that municipal policymakers were "consciously indifferent" to constitutional rights); <i>Wellington</i> v. <span class="citation" data-id="424905"><a href="/opinion/424905/cynthia-wellington-guardian-of-the-estate-of-robert-d-gravelle-v-brian/#937" aria-description="Citation for case: Cynthia Wellington, Guardian of the Estate of Robert D...."><i>Daniels, supra,</i> at 937</a></span> (affirming judgment notwithstanding verdict for municipality under "deliberate indifference" standard where evidence of only a single incident was presented at trial); cf. <i>Fiacco</i> v. <i>Rensselaer, supra,</i> at 328-332 (finding evidence of "deliberate indifference" sufficient to support jury verdict where a pattern of similar violations was shown at trial).</p>
<p>Allowing an inadequate training claim such as this one to go to the jury based upon a single incident would only invite jury nullification of <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>.</i> "To infer the existence of a city policy from the isolated misconduct of a single, low-level officer, and then to hold the city liable on the basis of that policy, <span class="star-pagination">*400</span> would amount to permitting precisely the theory of strict <i>respondeat superior</i> liability rejected in <i>Monell." Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#831" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 831</a></span> (1985) (BRENNAN, J., concurring in part and concurring in judgment). As the authors of the Ku Klux Act themselves realized, the resources of local government are not inexhaustible. The grave step of shifting those resources to particular areas where constitutional violations are likely to result through the deterrent power of § 1983 should certainly not be taken on the basis of an isolated incident. If § 1983 and the Constitution require the city of Canton to provide detailed medical and psychological training to its police officers, or to station paramedics at its jails, other city services will necessarily suffer, including those with far more direct implications for the protection of constitutional rights. Because respondent's evidence falls far short of establishing the high degree of fault on the part of the city required by our decision today, and because there is no indication that respondent could produce any new proof in this regard, I would reverse the judgment of the Court of Appeals and order entry of judgment for the city.</p>
<h2>NOTES</h2>
<p>[*]  <i>Benna Ruth Solomon, Beate Bloch,</i> and <i>Richard K. Willard</i> filed a brief for the International City Management Association et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  Title <span class="citation no-link">42 U. S. C. § 1983</span> provides, in relevant part, that:
</p>
<p>"Every person who, under color of any statute, ordinance, regulation, custom, or usage . . . subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress. . . ."</p>
<p>[2]  The city regulation in question provides that a police officer assigned to act as "jailer" at the city police station
</p>
<p>"shall, when a prisoner is found to be unconscious or semi-unconscious, or when he or she is unable to explain his or her condition, or who complains of being ill, have such person taken to a hospital for medical treatment, with permission of his supervisor before admitting the person to City Jail." App. 33.</p>
<p>[3]  In upholding Mrs. Harris' "failure to train" claim, the Sixth Circuit relied on two of its previous decisions which had approved such a theory of municipal liability under § 1983. See <i>Rymer</i> v. <i>Davis,</i> <span class="citation" data-id="447620"><a href="/opinion/447620/paul-d-rymer-v-trooper-ha-davis-city-of-shepherdsville-kentucky-and/" aria-description="Citation for case: Paul D. Rymer v. Trooper H.A. Davis, City of...">754 F. 2d 198</a></span>, vacated and remanded <i>sub nom. </i><i>Shepherdsville</i> v. <i>Rhymer,</i> <span class="citation" data-id="9048113"><a href="/opinion/9054597/city-of-shepherdsville-v-rymer/" aria-description="Citation for case: City of Shepherdsville v. Rymer">473 U. S. 901</a></span>, reinstated, <span class="citation" data-id="460084"><a href="/opinion/460084/paul-d-rymer-v-trooper-ha-davis-city-of-shepherdsville-kentucky-and/#757" aria-description="Citation for case: Paul D. Rymer v. Trooper H.A. Davis, City of...">775 F. 2d 756, 757</a></span> (1985); <i>Hays</i> v. <i>Jefferson County,</i> <span class="citation" data-id="9468792"><a href="/opinion/398831/donald-l-hays-jr-and-michael-c-potter-cross-appellants-v-jefferson/#874" aria-description="Citation for case: Donald L. Hays, Jr., and Michael C. Potter,...">668 F. 2d 869, 874</a></span> (1982).</p>
<p>[4]  See, <i>e. g., </i><i>St. Louis</i> v. <i>Praprotnik,</i> <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112</a></span> (1988); <i>Springfield</i> v. <i>Kibbe,</i> <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257</a></span> (1987); <i>Los Angeles</i> v. <i>Heller,</i> <span class="citation" data-id="9430425"><a href="/opinion/111630/city-of-los-angeles-v-heller/" aria-description="Citation for case: City of Los Angeles v. Heller">475 U. S. 796</a></span> (1986); <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808</a></span> (1985).</p>
<p>[5]  In this Court, in addition to suggesting that the city's failure to train its officers amounted to a "policy" that resulted in the denial of medical care to detainees, respondent also contended the city had a "custom" of denying medical care to those detainees suffering from emotional or mental ailments. See Brief for Respondent 31-32; Tr. of Oral Arg. 38-39. As respondent described it in her brief, and at argument, this claim of an unconstitutional "custom" appears to be little more than a restatement of her "failure-to-train as policy" claim. See <i><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">ibid.</a></span></i>
</p>
<p>However, to the extent that this claim poses a distinct basis for the city's liability under § 1983, we decline to determine whether respondent's contention that such a "custom" existed is an alternative ground for affirmance. The "custom" claim was not passed on by the Court of Appeals  nor does it appear to have been presented to that court as a distinct ground for its decision. See Brief of Appellee in No. 85-3314 (CA6), pp. 4-9, 11. Thus, we will not consider it here.</p>
<p>[6]  In addition to the Sixth Circuit decisions discussed in n. 3, <i>supra,</i> most of the other Courts of Appeals have held that a failure to train can create liability under § 1983. See, <i>e. g., </i><i>Spell</i> v. <i>McDaniel,</i> <span class="citation" data-id="8952845"><a href="/opinion/8961657/spell-v-mcdaniel/#1389" aria-description="Citation for case: Spell v. McDaniel">824 F. 2d 1380, 1389-1391</a></span> (CA4 1987); <i>Haynesworth</i> v. <i>Miller,</i> 261 U. S. App. D. C. 66, 80-83, <span class="citation" data-id="9476300"><a href="/opinion/489887/josiah-haynesworth-and-fred-hancock-v-frank-p-miller-chief-law/#1259" aria-description="Citation for case: Josiah Haynesworth and Fred Hancock v. Frank P. Miller,...">820 F. 2d 1245, 1259-1262</a></span> (1987); <i>Warren</i> v. <i>Lincoln,</i> <span class="citation" data-id="487192"><a href="/opinion/487192/jackson-warren-v-city-of-lincoln-nebraska-james-breen-sandra-l-myers-and/#1262" aria-description="Citation for case: Jackson Warren v. City of Lincoln, Nebraska James Breen...">816 F. 2d 1254, 1262-1263</a></span> (CA8 1987); <i>Bergquist</i> v. <i>County of Cochise,</i> <span class="citation" data-id="8946582"><a href="/opinion/8955600/bergquist-v-county-of-cochise/#1369" aria-description="Citation for case: Bergquist v. County of Cochise">806 F. 2d 1364, 1369-1370</a></span> (CA9 1986); <i>Wierstak</i> v. <i>Heffernan,</i> <span class="citation" data-id="469366"><a href="/opinion/469366/philip-f-wierstak-v-james-w-heffernan-philip-f-wierstak-v-james-w/#974" aria-description="Citation for case: Philip F. Wierstak v. James W. Heffernan, Philip F....">789 F. 2d 968, 974</a></span> (CA1 1986); <i>Fiacco</i> v. <i>Rensselaer,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/783/319/">783 F. 2d 319</a></span>, 326-327 (CA2 1986); <i>Gilmere</i> v. <i>Atlanta,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/774/1495/">774 F. 2d 1495</a></span>, 1503-1504 (CA11 1985) (en banc); <i>Rock</i> v. <i>McCoy,</i> <span class="citation" data-id="453103"><a href="/opinion/453103/charlie-rock-jr-v-roy-mccoy-and-the-city-of-checotah-oklahoma-a/#397" aria-description="Citation for case: Charlie Rock, Jr. v. Roy McCoy and the City of Checotah,...">763 F. 2d 394, 397-398</a></span> (CA10 1985); <i>Languirand</i> v. <i>Hayden,</i> <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#227" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an...">717 F. 2d 220, 227-228</a></span> (CA5 1983). Two other Courts of Appeals have stopped short of expressly embracing this rule, and have instead only implicitly endorsed it. See, <i>e. g., </i><i>Colburn</i> v. <i>Upper Darby Township,</i> <span class="citation" data-id="8957077"><a href="/opinion/8965741/colburn-v-upper-darby-township/#672" aria-description="Citation for case: Colburn v. Upper Darby Township">838 F. 2d 663, 672-673</a></span> (CA3 1988); <i>Lenard</i> v. <i>Argento,</i> <span class="citation" data-id="414191"><a href="/opinion/414191/bennie-lenard-cross-appellant-v-robert-argento-joseph-sansone-v/#885" aria-description="Citation for case: Bennie Lenard, Cross-Appellant v. Robert Argento &amp; Joseph...">699 F. 2d 874, 885-887</a></span> (CA7 1983).
</p>
<p>In addition, six current Members of this Court have joined opinions in the past that have (at least implicitly) endorsed this theory of liability under § 1983. See <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#829" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 829-831</a></span> (BRENNAN, J., joined by MARSHALL and BLACKMUN, JJ., concurring in part and concurring in judgment); <i>Springfield</i> v. <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#268" aria-description="Citation for case: City of Springfield v. Kibbe"><i>Kibbe, supra,</i> at 268-270</a></span> (O'CONNOR, J., joined by REHNQUIST, C. J., and Powell and WHITE, JJ., dissenting).</p>
<p>[7]  Some courts have held that a showing of "gross negligence" in a city's failure to train its employees is adequate to make out a claim under § 1983. See, <i>e. g., </i><i>Bergquist</i> v. <span class="citation" data-id="8946582"><a href="/opinion/8955600/bergquist-v-county-of-cochise/#1370" aria-description="Citation for case: Bergquist v. County of Cochise"><i>County of Cochise, supra,</i> at 1370</a></span>; <i>Herrera</i> v. <i>Valentine,</i> <span class="citation" data-id="392242"><a href="/opinion/392242/herrera-v-valentine/#1224" aria-description="Citation for case: Herrera v. Valentine">653 F. 2d 1220, 1224</a></span> (CA8 1981). But the more common rule is that a city must exhibit "deliberate indifference" towards the constitutional rights of persons in its domain before a § 1983 action for "failure to train" is permissible. See, <i>e. g., </i><i>Fiacco</i> v. <i>Rensselaer, supra,</i> at 326; <i>Patzner</i> v. <i>Burkett,</i> <span class="citation" data-id="462512"><a href="/opinion/462512/leland-patzner-v-joyce-burkett-aka-joyce-mclaughlin-deborah-myerchin-and/#1367" aria-description="Citation for case: Leland Patzner v. Joyce Burkett A/K/A Joyce McLaughlin...">779 F. 2d 1363, 1367</a></span> (CA8 1985); <i>Wellington</i> v. <i>Daniels,</i> <span class="citation" data-id="424905"><a href="/opinion/424905/cynthia-wellington-guardian-of-the-estate-of-robert-d-gravelle-v-brian/#936" aria-description="Citation for case: Cynthia Wellington, Guardian of the Estate of Robert D....">717 F. 2d 932, 936</a></span> (CA4 1983); <i>Languirand</i> v. <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#227" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an..."><i>Hayden, supra,</i> at 227</a></span>.</p>
<p>[8]  The "deliberate indifference" standard we adopt for § 1983 "failure to train" claims does not turn upon the degree of fault (if any) that a plaintiff must show to make out an underlying claim of a constitutional violation. For example, this Court has never determined what degree of culpability must be shown before the particular constitutional deprivation asserted in this case  a denial of the due process right to medical care while in detention  is established. Indeed, in <i>Revere</i> v. <i>Massachusetts General Hospital,</i> <span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/#243" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">463 U. S. 239, 243-245</a></span> (1983), we reserved decision on the question whether something less than the Eighth Amendment's "deliberate indifference" test may be applicable in claims by detainees asserting violations of their due process right to medical care while in custody.
</p>
<p>We need not resolve here the question left open in <i><span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">Revere</a></span></i> for two reasons. First, petitioner has conceded that, as the case comes to us, we must assume that respondent's constitutional right to receive medical care was denied by city employees  whatever the nature of that right might be. See Tr. of Oral Arg. 8-9. Second, the proper standard for determining when a municipality will be liable under § 1983 for constitutional wrongs does not turn on any underlying culpability test that determines when such wrongs have occurred. Cf. Brief for Respondent 27.</p>
<p>[9]  The plurality opinion in <i><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span></i> explained why this must be so:
</p>
<p>"Obviously, if one retreats far enough from a constitutional violation some municipal `policy' can be identified behind almost any . . . harm inflicted by a municipal official; for example, [a police officer] would never have killed Tuttle if Oklahoma City did not have a `policy' of establishing a police force. But <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span></i> must be taken to require proof of a city policy different in kind from this latter example before a claim can be sent to a jury on the theory that a particular violation was `caused' by the municipal `policy.' " <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823</a></span>. Cf. also <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#833" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>id.,</i> at 833, n. 9</a></span> (opinion of BRENNAN, J.).</p>
<p>[10]  For example, city policymakers know to a moral certainty that their police officers will be required to arrest fleeing felons. The city has armed its officers with firearms, in part to allow them to accomplish this task. Thus, the need to train officers in the constitutional limitations on the use of deadly force, see <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), can be said to be "so obvious," that failure to do so could properly be characterized as "deliberate indifference" to constitutional rights.
</p>
<p>It could also be that the police, in exercising their discretion, so often violate constitutional rights that the need for further training must have been plainly obvious to the city policymakers, who, nevertheless, are "deliberately indifferent" to the need.</p>
<p>[11]  The record indicates that city did train its officers and that its training included first-aid instruction. See App. to Pet. for Cert. 4a. Petitioner argues that it could not have been obvious to the city that such training was insufficient to administer the written policy, which was itself constitutional. This is a question to be resolved on remand. See Part IV, <i>infra.</i></p>
<p>[12]  Respondent conceded as much at argument. See Tr. of Oral Arg. 50-51; cf. also <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#831" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 831</a></span> (opinion of BRENNAN, J.).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/City of Indianapolis v. Edmond.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "City of Indianapolis v. Edmond"
type: case
citation: ""
parallel_cite: "531 U.S. 32; 121 S. Ct. 447; 148 L. Ed. 2d 333; 69 U.S.L.W. 4009; 14 Fla. L. Weekly Fed. S 9; 2000 Colo. J. C.A.R. 6401"
neutral_cite: "2000 U.S. LEXIS 8084; 2000 Cal. Daily Op. Serv. 9549"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-11-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-11-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Indianapolis v. Edmond
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118391/city-of-indianapolis-v-edmond/"
  cluster_id: 118391
  opinion_id: 118391
  identity_checked: true
homes:
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Key — Anchor"
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Related (cross-doctrine)"
  - page: "[[Border Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[Illinois v. Lidster]]", "[[Delaware v. Prouse]]", "[[Ferguson v. City of Charleston]]"]
aliases: ["Indianapolis v. Edmond"]
tags: ["case", "fourth-amendment", "checkpoint", "roadblock", "special-needs", "programmatic-purpose"]
holding: "A checkpoint program whose primary purpose is to detect ordinary criminal wrongdoing / general crime control (here, drug interdiction)…"
lake:
  record_id: City of Indianapolis v. Edmond
  status: verified
  projected_at: 2026-07-06
---

# City of Indianapolis v. Edmond

*531 U.S. 32 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Indianapolis operated vehicle checkpoints at which officers stopped a set number of cars, checked the driver's license and registration, looked for signs of impairment, and walked a drug-detection dog around each vehicle. The city conceded the program's purpose was to interdict narcotics. Motorists stopped at the checkpoints sued, challenging the program under the Fourth Amendment.

## Issue
Whether a vehicle checkpoint program whose primary purpose is the general interest in crime control (narcotics interdiction) is consistent with the Fourth Amendment.

## Rule
No. Suspicionless checkpoint seizures are measured by their programmatic purpose, and ordinary crime control will not justify them: "We have never approved a checkpoint program whose primary purpose was to detect evidence of ordinary criminal wrongdoing." — 531 U.S. 32, 41. ^pin-41

"Because the primary purpose of the Indianapolis narcotics checkpoint program is to uncover evidence of ordinary criminal wrongdoing, the program contravenes the Fourth Amendment." — *Id.* at 42. ^pin-42

## Application
Indianapolis's checkpoints were aimed primarily at detecting and interdicting unlawful drugs — a general crime-control end, not the border-policing or roadway-safety interests that had justified prior checkpoints. Because that primary purpose was indistinguishable from the general interest in crime control, the suspicionless stops were unreasonable on these facts.

## Conclusion
The narcotics checkpoint program violated the Fourth Amendment; the injunction against it was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Edmond*'s primary-purpose test was distinguished in [[Illinois v. Lidster]] (information-seeking checkpoint about a crime committed by someone else) and applied to invalidate law-enforcement-purpose programs in [[Ferguson v. City of Charleston]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *City of Indianapolis v. Edmond*, 531 U.S. 32 (2000) — https://www.courtlistener.com/opinion/118391/city-of-indianapolis-v-edmond/ — pinpoints: 41, 42.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "387fd7c8b12c7e0f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "City of Indianapolis v. Edmond"}, "payload": {"all": [{"cite": "531 U.S. 32", "page": "32", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "531"}, {"cite": "121 S. Ct. 447", "page": "447", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "148 L. Ed. 2d 333", "page": "333", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "148"}, {"cite": "2000 U.S. LEXIS 8084", "page": "8084", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}, {"cite": "69 U.S.L.W. 4009", "page": "4009", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "69"}, {"cite": "14 Fla. L. Weekly Fed. S 9", "page": "9", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "14"}, {"cite": "2000 Colo. J. C.A.R. 6401", "page": "6401", "reporter": "Colo. J. C.A.R.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2000"}, {"cite": "2000 Cal. Daily Op. Serv. 9549", "page": "9549", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}], "display": null, "official": null, "official_selection_present": false, "record_id": "City of Indianapolis v. Edmond"}}
{"assertion_id": "281de380a721c06b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-42", "record_id": "City of Indianapolis v. Edmond"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-42", "pinpoint_status": "slip-only", "quote": "Because the primary purpose of the Indianapolis narcotics checkpoint program is to uncover evidence of ordinary criminal wrongdoing, the program contravenes the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "City of Indianapolis v. Edmond", "star_marker": null}}
{"assertion_id": "8140fa2678c738ef", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-41", "record_id": "City of Indianapolis v. Edmond"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-41", "pinpoint_status": "slip-only", "quote": "--- # City of Indianapolis v. Edmond *531 U.S. 32 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Indianapolis operated vehicle checkpoints at which officers stopped a set number of cars, checked the driver's license and registration, looked for signs of impairment, and walked a drug-detection dog around each vehicle. The city conceded the program's purpose was to interdict narcotics. Motorists stopped at the checkpoints sued, challenging the program under the Fourth Amendment. ## Issue Whether a vehicle checkpoint program whose primary purpose is the general interest in crime control (narcotics interdiction) is consistent with the Fourth Amendment. ## Rule No. Suspicionless checkpoint seizures are measured by their programmatic purpose, and ordinary crime control will not justify them:", "quote_fidelity": "mismatch", "record_id": "City of Indianapolis v. Edmond", "star_marker": null}}
{"assertion_id": "8b18dc8707f447e3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "City of Indianapolis v. Edmond"}, "payload": {"as_of_content": "2000-11-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "City of Indianapolis v. Edmond", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — City of Indianapolis v. Edmond

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Indianapolis v. Edmond",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Indianapolis v. Edmond",
    "case_name_short": "Edmond",
    "case_name_full": "CITY OF INDIANAPOLIS Et Al. v. EDMOND Et Al.",
    "input_case_name": "City of Indianapolis v. Edmond",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-11-28",
    "year": 2000,
    "docket": null,
    "cluster_id": 118391,
    "lead_opinion_id": 118391,
    "sibling_ids": [
      118391,
      9434014,
      9434015,
      9434016
    ],
    "absolute_url": "/opinion/118391/city-of-indianapolis-v-edmond/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9194630,
        "score": 20,
        "case_name": "City of Indianapolis v. Edmond"
      },
      {
        "cluster_id": 9194629,
        "score": 20,
        "case_name": "City of Indianapolis v. Edmond"
      },
      {
        "cluster_id": 9266095,
        "score": 20,
        "case_name": "City of Indianapolis v. Edmond"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "531 U.S. 32",
        "volume": "531",
        "reporter": "U.S.",
        "page": "32",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 447",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "447",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 333",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4009",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4009",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 9",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Colo. J. C.A.R. 6401",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6401",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. LEXIS 8084",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "8084",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Cal. Daily Op. Serv. 9549",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9549",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "531 U.S. 32",
        "volume": "531",
        "reporter": "U.S.",
        "page": "32",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 447",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "447",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 333",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. LEXIS 8084",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "8084",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4009",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4009",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 9",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Colo. J. C.A.R. 6401",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6401",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Cal. Daily Op. Serv. 9549",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9549",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-41",
      "page": null,
      "quote": "--- # City of Indianapolis v. Edmond *531 U.S. 32 (2000)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Indianapolis operated vehicle checkpoints at which officers stopped a set number of cars, checked the driver's license and registration, looked for signs of impairment, and walked a drug-detection dog around each vehicle. The city conceded the program's purpose was to interdict narcotics. Motorists stopped at the checkpoints sued, challenging the program under the Fourth Amendment. ## Issue Whether a vehicle checkpoint program whose primary purpose is the general interest in crime control (narcotics interdiction) is consistent with the Fourth Amendment. ## Rule No. Suspicionless checkpoint seizures are measured by their programmatic purpose, and ordinary crime control will not justify them:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-42",
      "page": null,
      "quote": "Because the primary purpose of the Indianapolis narcotics checkpoint program is to uncover evidence of ordinary criminal wrongdoing, the program contravenes the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-11-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Indianapolis v. Edmond",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nicholson",
          "cluster_id": 4505529,
          "cite": [
            "813 S.E.2d 840",
            "371 N.C. 284"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gigliotti",
          "cluster_id": 7316853,
          "cite": [
            "145 F. Supp. 3d 203",
            "2015 WL 6830675"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Evans",
          "cluster_id": 2802206,
          "cite": [
            "786 F.3d 779",
            "15 Cal. Daily Op. Serv. 4997",
            "2015 U.S. App. LEXIS 8293",
            "2015 WL 2385010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Bohman",
          "cluster_id": 803265,
          "cite": [
            "683 F.3d 861",
            "2012 WL 2432595",
            "2012 U.S. App. LEXIS 13195"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lidster",
          "cluster_id": 131154,
          "cite": [
            "157 L. Ed. 2d 843",
            "124 S. Ct. 885",
            "540 U.S. 419",
            "2004 U.S. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McIntosh",
          "cluster_id": 2058958,
          "cite": [
            "755 N.E.2d 329",
            "96 N.Y.2d 521",
            "730 N.Y.S.2d 265",
            "2001 N.Y. LEXIS 1978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caballes",
          "cluster_id": 2192166,
          "cite": [
            "851 N.E.2d 26",
            "221 Ill. 2d 282",
            "303 Ill. Dec. 128",
            "2006 Ill. LEXIS 625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crowe v. County of San Diego",
          "cluster_id": 148932,
          "cite": [
            "608 F.3d 406",
            "2010 U.S. App. LEXIS 12917",
            "2010 WL 2431842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kimler",
          "cluster_id": 163635,
          "cite": [
            "335 F.3d 1132",
            "2003 WL 21519916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hicks",
          "cluster_id": 1060443,
          "cite": [
            "55 S.W.3d 515",
            "2001 Tenn. LEXIS 658",
            "2001 WL 1035172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEyNDE2MDAwMDAwJnM9Mjk5MTY0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118391+OR+9434014+OR+9434015+OR+9434016%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTImcz0yNjEmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118391+OR+9434014+OR+9434015+OR+9434016%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016)",
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
    "complete_query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016)",
    "indexed_citing_opinions": 745,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118391,
        "count": 644,
        "count_source": "search"
      },
      {
        "opinion_id": 9434014,
        "count": 125,
        "count_source": "search"
      },
      {
        "opinion_id": 9434015,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434016,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1207,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-indianapolis-v-edmond.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTAwNTkmcz0xMDAxNTMwMSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118391+OR+9434014+OR+9434015+OR+9434016%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118391,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 156261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 517399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 552811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 765145,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 2311329,
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
    "date_created": "2026-07-05T00:17:27Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:17:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:17:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:21:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:17:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Indianapolis v. Edmond

```
<div>
<center><b><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32</a></span> (2000)</b></center>
<center><h1>CITY OF INDIANAPOLIS et al.<br>
v.<br>
EDMOND et al.</h1></center>
<center>No. 99-1030.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued October 3, 2000.</center>
<center>Decided November 28, 2000.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT
<p><span class="star-pagination">*33</span> O'Connor, J., delivered the opinion of the Court, in which Stevens, Kennedy, Souter, Ginsburg, and Breyer, JJ., joined. Rehnquist, C. J., filed a dissenting opinion, in which Thomas, J., joined, and in which Scalia, J., joined as to Part I, <i>post,</i> p. 48. Thomas, J., filed a dissenting opinion, <i>post,</i> p. 56.</p>
<p><i>A. Scott Chinn</i> argued the cause for petitioners. With him on the briefs were <i>Anthony W. Overholt, Matthew R. Gutwein,</i> and <i>Thomas M. Fisher.</i> </p>
<p><i>Patricia A. Millett</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With her on the brief were <i>Solicitor General Waxman, Assistant Attorney General Robinson,</i> and <i>Deputy Solicitor General Dreeben.</i> </p>
<p><span class="star-pagination">*34</span> <i>Kenneth J. Falk</i> argued the cause for respondents. With him on the brief were <i>Jacquelyn E. Bowie, Sean C. Lemieux,</i>  and <i>Steven R. Shapiro.</i><sup>[*]</sup></p>
<p>Justice O'Connor, delivered the opinion of the Court.</p>
<p>In <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990), and <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), we held that brief, suspicionless seizures at highway checkpoints for the purposes of combating drunk driving and intercepting illegal immigrants were constitutional. We now consider the constitutionality of a highway checkpoint program whose primary purpose is the discovery and interdiction of illegal narcotics.</p>
<p></p>
<h2>I</h2>
<p>In August 1998, the city of Indianapolis began to operate vehicle checkpoints on Indianapolis roads in an effort to interdict unlawful drugs. The city conducted six such roadblocks between August and November that year, stopping <span class="star-pagination">*35</span> 1,161 vehicles and arresting 104 motorists. Fifty-five arrests were for drug-related crimes, while 49 were for offenses unrelated to drugs. <i>Edmond</i> v. <i>Goldsmith,</i> <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#661" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d 659, 661</a></span> (CA7 1999). The overall "hit rate" of the program was thus approximately nine percent.</p>
<p>The parties stipulated to the facts concerning the operation of the checkpoints by the Indianapolis Police Department (IPD) for purposes of the preliminary injunction proceedings instituted below. At each checkpoint location, the police stop a predetermined number of vehicles. Approximately 30 officers are stationed at the checkpoint. Pursuant to written directives issued by the chief of police, at least one officer approaches the vehicle, advises the driver that he or she is being stopped briefly at a drug checkpoint, and asks the driver to produce a license and registration. The officer also looks for signs of impairment and conducts an open-view examination of the vehicle from the outside. A narcoticsdetection dog walks around the outside of each stopped vehicle.</p>
<p>The directives instruct the officers that they may conduct a search only by consent or based on the appropriate quantum of particularized suspicion. The officers must conduct each stop in the same manner until particularized suspicion develops, and the officers have no discretion to stop any vehicle out of sequence. The city agreed in the stipulation to operate the checkpoints in such a way as to ensure that the total duration of each stop, absent reasonable suspicion or probable cause, would be five minutes or less.</p>
<p>The affidavit of Indianapolis Police Sergeant Marshall DePew, although it is technically outside the parties' stipulation, provides further insight concerning the operation of the checkpoints. According to Sergeant DePew, checkpoint locations are selected weeks in advance based on such considerations as area crime statistics and traffic flow. The checkpoints are generally operated during daylight hours and are identified with lighted signs reading, "`NARCOTICS <span class="star-pagination">*36</span> CHECKPOINT MILE AHEAD, NARCOTICS K-9 IN USE, BE PREPARED TO STOP.'" App. to Pet. for Cert. 57a. Once a group of cars has been stopped, other traffic proceeds without interruption until all the stopped cars have been processed or diverted for further processing. Sergeant DePew also stated that the average stop for a vehicle not subject to further processing lasts two to three minutes or less.</p>
<p>Respondents James Edmond and Joell Palmer were each stopped at a narcotics checkpoint in late September 1998. Respondents then filed a lawsuit on behalf of themselves and the class of all motorists who had been stopped or were subject to being stopped in the future at the Indianapolis drug checkpoints. Respondents claimed that the roadblocks violated the Fourth Amendment of the United States Constitution and the search and seizure provision of the Indiana Constitution. Respondents requested declaratory and injunctive relief for the class, as well as damages and attorney's fees for themselves.</p>
<p>Respondents then moved for a preliminary injunction. Although respondents alleged that the officers who stopped them did not follow the written directives, they agreed to the stipulation concerning the operation of the checkpoints for purposes of the preliminary injunction proceedings. The parties also stipulated to certification of the plaintiff class. The United States District Court for the Southern District of Indiana agreed to class certification and denied the motion for a preliminary injunction, holding that the checkpoint program did not violate the Fourth Amendment. <i>Edmond</i>  v. <i>Goldsmith,</i> <span class="citation" data-id="2311329"><a href="/opinion/2311329/edmond-v-goldsmith/" aria-description="Citation for case: Edmond v. Goldsmith">38 F. Supp. 2d 1016</a></span> (1998). A divided panel of the United States Court of Appeals for the Seventh Circuit reversed, holding that the checkpoints contravened the Fourth Amendment. <span class="citation multiple-matches"><a href="/c/F.%203d/183/659/">183 F. 3d 659</a></span> (1999). The panel denied rehearing. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./528/1153/">528 U. S. 1153</a></span> (2000), and now affirm.</p>
<p></p>
<h2>
<span class="star-pagination">*37</span> II</h2>
<p>The Fourth Amendment requires that searches and seizures be reasonable. A search or seizure is ordinarily unreasonable in the absence of individualized suspicion of wrongdoing. <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#308" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 308</a></span> (1997). While such suspicion is not an "irreducible" component of reasonableness, <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 561</a></span>, we have recognized only limited circumstances in which the usual rule does not apply. For example, we have upheld certain regimes of suspicion less searches where the program was designed to serve "special needs, beyond the normal need for law enforcement." See, <i>e. g., </i><i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995) (random drug testing of studentathletes); <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989) (drug tests for United States Customs Service employees seeking transfer or promotion to certain positions); <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989) (drug and alcohol tests for railway employees involved in train accidents or found to be in violation of particular safety regulations). We have also allowed searches for certain administrative purposes without particularized suspicion of misconduct, provided that those searches are appropriately limited. See, <i>e. g., </i><i>New York</i> v. <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#702" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 702-704</a></span> (1987) (warrantless administrative inspection of premises of "closely regulated" business); <i>Michigan</i> v. <i>Tyler,</i>  <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#507" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 507-509, 511-512</a></span> (1978) (administrative inspection of fire-damaged premises to determine cause of blaze); <i>Camara</i> v. <i>Municipal Court of City and County of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-539</a></span> (1967) (administrative inspection to ensure compliance with city housing code).</p>
<p>We have also upheld brief, suspicion less seizures of motorists at a fixed Border Patrol checkpoint designed to intercept illegal aliens, <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> and at a sobriety checkpoint aimed at removing drunk drivers from the road, <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990). In addition, in <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span> (1979), <span class="star-pagination">*38</span> we suggested that a similar type of roadblock with the purpose of verifying drivers' licenses and vehicle registrations would be permissible. In none of these cases, however, did we indicate approval of a checkpoint program whose primary purpose was to detect evidence of ordinary criminal wrongdoing.</p>
<p>In <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> we entertained Fourth Amendment challenges to stops at two permanent immigration checkpoints located on major United States highways less than 100 miles from the Mexican border. We noted at the outset the particular context in which the constitutional question arose, describing in some detail the "formidable law enforcement problems" posed by the northbound tide of illegal entrants into the United States. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#551" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 551-554</a></span>. These problems had also been the focus of several earlier cases addressing the constitutionality of other Border Patrol traffic-checking operations. See <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973). In <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> we found that the balance tipped in favor of the Government's interests in policing the Nation's borders. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 561-564</a></span>. In so finding, we emphasized the difficulty of effectively containing illegal immigration at the border itself. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 556</a></span>. We also stressed the impracticality of the particularized study of a given car to discern whether it was transporting illegal aliens, as well as the relatively modest degree of intrusion entailed by the stops. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 556-564</a></span>.</p>
<p>Our subsequent cases have confirmed that considerations specifically related to the need to police the border were a significant factor in our <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> decision. For example, in <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 538</a></span> (1985), we counted <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> as one of a number of Fourth Amendment cases that "reflect longstanding concern for the protection of the integrity of the border." Although the stops in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> did not occur at the <span class="star-pagination">*39</span> border itself, the checkpoints were located near the border and served a border control function made necessary by the difficulty of guarding the border's entire length. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 556</a></span>.</p>
<p>In <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>,</i> we evaluated the constitutionality of a Michigan highway sobriety checkpoint program. The <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> checkpoint involved brief, suspicion less stops of motorists so that police officers could detect signs of intoxication and remove impaired drivers from the road. <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 447-448</a></span>. Motorists who exhibited signs of intoxication were diverted for a license and registration check and, if warranted, further sobriety tests. <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Id.,</i> at 447</a></span>. This checkpoint program was clearly aimed at reducing the immediate hazard posed by the presence of drunk drivers on the highways, and there was an obvious connection between the imperative of highway safety and the law enforcement practice at issue. The gravity of the drunk driving problem and the magnitude of the State's interest in getting drunk drivers off the road weighed heavily in our determination that the program was constitutional. See <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#451" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>id.,</i> at 451</a></span>.</p>
<p>In <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>,</i> we invalidated a discretionary, suspicion less stop for a spot check of a motorist's driver's license and vehicle registration. The officer's conduct in that case was unconstitutional primarily on account of his exercise of "standardless and unconstrained discretion." <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 661</a></span>. We nonetheless acknowledged the States' "vital interest in ensuring that only those qualified to do so are permitted to operate motor vehicles, that these vehicles are fit for safe operation, and hence that licensing, registration, and vehicle inspection requirements are being observed." <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse"><i>Id.,</i> at 658</a></span>. Accordingly, we suggested that "[q]uestioning of all oncoming traffic at roadblock-type stops" would be a lawful means of serving this interest in highway safety. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><i>Id.,</i> at 663</a></span>.</p>
<p>We further indicated in <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span></i> that we considered the purposes of such a hypothetical roadblock to be distinct from a general purpose of investigating crime. The State proffered <span class="star-pagination">*40</span> the additional interests of "the apprehension of stolen motor vehicles and of drivers under the influence of alcohol or narcotics" in its effort to justify the discretionary spot check. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><i>Id.,</i> at 659, n. 18</a></span>. We attributed the entirety of the latter interest to the State's interest in roadway safety. <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Ibid.</a></span></i> We also noted that the interest in apprehending stolen vehicles may be partly subsumed by the interest in roadway safety. <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Ibid.</a></span></i> We observed, however, that "[t]he remaining governmental interest in controlling automobile thefts is not distinguishable from the general interest in crime control." <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Ibid.</a></span></i> Not only does the common thread of highway safety thus run through <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>,</i> but <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span></i> itself reveals a difference in the Fourth Amendment significance of highway safety interests and the general interest in crime control.</p>
<p></p>
<h2>III</h2>
<p>It is well established that a vehicle stop at a highway checkpoint effectuates a seizure within the meaning of the Fourth Amendment. See, <i>e. g., </i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#450" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Sitz, supra,</i> at 450</a></span>. The fact that officers walk a narcotics-detection dog around the exterior of each car at the Indianapolis checkpoints does not transform the seizure into a search. See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). Just as in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> an exterior sniff of an automobile does not require entry into the car and is not designed to disclose any information other than the presence or absence of narcotics. See <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">ibid.</a></span></i> Like the dog sniff in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> a sniff by a dog that simply walks around a car is "much less intrusive than a typical search." <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Ibid.</a></span></i>  Cf. <i>United States</i> v. <i>Turpin,</i> <span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/#1385" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">920 F. 2d 1377, 1385</a></span> (CA8 1990). Rather, what principally distinguishes these checkpoints from those we have previously approved is their primary purpose.</p>
<p>As petitioners concede, the Indianapolis checkpoint program unquestionably has the primary purpose of interdicting illegal narcotics. In their stipulation of facts, the parties repeatedly refer to the checkpoints as "drug checkpoints" and <span class="star-pagination">*41</span> describe them as "being operated by the City of Indianapolis in an effort to interdict unlawful drugs in Indianapolis." App. to Pet. for Cert. 51a52a. In addition, the first document attached to the parties' stipulation is entitled "DRUG CHECKPOINT CONTACT OFFICER DIRECTIVES BY ORDER OF THE CHIEF OF POLICE." <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Id.,</a></span></i> at 53a. These directives instruct officers to "[a]dvise the citizen that they are being stopped briefly at a drug checkpoint." <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Ibid.</a></span></i>  The second document attached to the stipulation is entitled "1998 Drug Road Blocks" and contains a statistical breakdown of information relating to the checkpoints conducted. <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Id.,</a></span></i> at 55a. Further, according to Sergeant DePew, the checkpoints are identified with lighted signs reading, "`NARCOTICS CHECKPOINT MILE AHEAD, NARCOTICS K-9 IN USE, BE PREPARED TO STOP.' " <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Id.,</a></span></i> at 57a. Finally, both the District Court and the Court of Appeals recognized that the primary purpose of the roadblocks is the interdiction of narcotics. <span class="citation" data-id="2311329"><a href="/opinion/2311329/edmond-v-goldsmith/#1026" aria-description="Citation for case: Edmond v. Goldsmith">38 F. Supp. 2d, at 1026</a></span> (noting that both parties "stress the primary purpose of the roadblocks as the interdiction of narcotics" and that "[t]he IPD has made it clear that the purpose for its checkpoints is to interdict narcotics traffic"); <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#665" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d, at 665</a></span> (observing that "the City concedes that its proximate goal is to catch drug offenders").</p>
<p>We have never approved a checkpoint program whose primary purpose was to detect evidence of ordinary criminal wrongdoing. Rather, our checkpoint cases have recognized only limited exceptions to the general rule that a seizure must be accompanied by some measure of individualized suspicion. We suggested in <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span></i> that we would not credit the "general interest in crime control" as justification for a regime of suspicionless stops. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 659, n. 18</a></span>. Consistent with this suggestion, each of the checkpoint programs that we have approved was designed primarily to serve purposes closely related to the problems of policing the border or the necessity of ensuring roadway safety. Because the <span class="star-pagination">*42</span> primary purpose of the Indianapolis narcotics checkpoint program is to uncover evidence of ordinary criminal wrongdoing, the program contravenes the Fourth Amendment.</p>
<p>Petitioners propose several ways in which the narcoticsdetection purpose of the instant checkpoint program may instead resemble the primary purposes of the checkpoints in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>.</i> Petitioners state that the checkpoints in those cases had the same ultimate purpose of arresting those suspected of committing crimes. Brief for Petitioners 22. Securing the border and apprehending drunk drivers are, of course, law enforcement activities, and law enforcement officers employ arrests and criminal prosecutions in pursuit of these goals. See <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 447, 450</a></span>; <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#545" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 545-550</a></span>. If we were to rest the case at this high level of generality, there would be little check on the ability of the authorities to construct roadblocks for almost any conceivable law enforcement purpose. Without drawing the line at roadblocks designed primarily to serve the general interest in crime control, the Fourth Amendment would do little to prevent such intrusions from becoming a routine part of American life.</p>
<p>Petitioners also emphasize the severe and intractable nature of the drug problem as justification for the checkpoint program. Brief for Petitioners 14-17, 31. There is no doubt that traffic in illegal narcotics creates social harms of the first magnitude. Cf. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 668</a></span>. The law enforcement problems that the drug trade creates likewise remain daunting and complex, particularly in light of the myriad forms of spin-off crime that it spawns. Cf. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S., at 538</a></span>. The same can be said of various other illegal activities, if only to a lesser degree. But the gravity of the threat alone cannot be dispositive of questions concerning what means law enforcement officers may employ to pursue a given purpose. Rather, in determining whether individualized suspicion is required, we must consider the nature of the interests threatened and their connection <span class="star-pagination">*43</span> to the particular law enforcement practices at issue. We are particularly reluctant to recognize exceptions to the general rule of individualized suspicion where governmental authorities primarily pursue their general crime control ends.</p>
<p>Nor can the narcotics-interdiction purpose of the checkpoints be rationalized in terms of a highway safety concern similar to that present in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>.</i> The detection and punishment of almost any criminal offense serves broadly the safety of the community, and our streets would no doubt be safer but for the scourge of illegal drugs. Only with respect to a smaller class of offenses, however, is society confronted with the type of immediate, vehicle-bound threat to life and limb that the sobriety checkpoint in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> was designed to eliminate.</p>
<p>Petitioners also liken the anticontraband agenda of the Indianapolis checkpoints to the antismuggling purpose of the checkpoints in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>.</i> Brief for Petitioners 15 16. Petitioners cite this Court's conclusion in <i>MartinezFuerte</i> that the flow of traffic was too heavy to permit "particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens," <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 557</a></span>, and claim that this logic has even more force here. The problem with this argument is that the same logic prevails any time a vehicle is employed to conceal contraband or other evidence of a crime. This type of connection to the roadway is very different from the close connection to roadway safety that was present in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>.</i> Further, the Indianapolis checkpoints are far removed from the border context that was crucial in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>.</i> While the difficulty of examining each passing car was an important factor in validating the law enforcement technique employed in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> this factor alone cannot justify a regime of suspicionless searches or seizures. Rather, we must look more closely at the nature of the public interests that such a regime is designed principally to serve.</p>
<p><span class="star-pagination">*44</span> The primary purpose of the Indianapolis narcotics checkpoints is in the end to advance "the general interest in crime control," <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 659, n. 18</a></span>. We decline to suspend the usual requirement of individualized suspicion where the police seek to employ a checkpoint primarily for the ordinary enterprise of investigating crimes. We cannot sanction stops justified only by the generalized and everpresent possibility that interrogation and inspection may reveal that any given motorist has committed some crime.</p>
<p>Of course, there are circumstances that may justify a law enforcement checkpoint where the primary purpose would otherwise, but for some emergency, relate to ordinary crime control. For example, as the Court of Appeals noted, the Fourth Amendment would almost certainly permit an appropriately tailored roadblock set up to thwart an imminent terrorist attack or to catch a dangerous criminal who is likely to flee by way of a particular route. See 183 F. 3d, at 662 663. The exigencies created by these scenarios are far removed from the circumstances under which authorities might simply stop cars as a matter of course to see if there just happens to be a felon leaving the jurisdiction. While we do not limit the purposes that may justify a checkpoint program to any rigid set of categories, we decline to approve a program whose primary purpose is ultimately indistinguishable from the general interest in crime control.<sup>[1]</sup></p>
<p><span class="star-pagination">*45</span> Petitioners argue that our prior cases preclude an inquiry into the purposes of the checkpoint program. For example, they cite <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), and <i>Bond</i> v. <i>United States,</i> <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">529 U. S. 334</a></span> (2000), to support the proposition that "where the government articulates and pursues a legitimate interest for a suspicionless stop, courts should not look behind that interest to determine whether the government's `primary purpose' is valid." Brief for Petitioners 34; see also <i>id.,</i> at 9. These cases, however, do not control the instant situation.</p>
<p>In <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>,</i> we held that an individual officer's subjective intentions are irrelevant to the Fourth Amendment validity of a traffic stop that is justified objectively by probable cause to believe that a traffic violation has occurred. <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#810" aria-description="Citation for case: Whren v. United States">517 U. S., at 810-813</a></span>. We observed that our prior cases "foreclose any argument that the constitutional reasonableness of traffic stops depends on the actual motivations of the individual officers involved." <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States"><i>Id.,</i> at 813</a></span>. In so holding, we expressly distinguished cases where we had addressed the validity of searches conducted in the absence of probable cause. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States"><i>id.,</i> at 811-812</a></span> (distinguishing <i>Florida</i> v. <i>Wells,</i> <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#4" aria-description="Citation for case: Florida v. Wells">495 U. S. 1, 4</a></span> (1990) (stating that "an inventory search must not be a ruse for a general rummaging in order to discover incriminating evidence"), <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#372" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 372</a></span> (1987) (suggesting that the absence of bad faith and the lack of a purely investigative purpose were relevant to the validity of an inventory search), and <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#716" aria-description="Citation for case: New York v. Burger">482 U. S., at 716-717, n. 27</a></span> (observing that a valid administrative inspection conducted with neither a warrant nor probable cause did not appear to be a pretext for gathering evidence of violations of the penal laws)).</p>
<p><i>Whren</i> therefore reinforces the principle that, while "[s]ubjective intentions play no role in ordinary, probablecause Fourth Amendment analysis," <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S., at 813</a></span>, programmatic purposes may be relevant to the validity of Fourth Amendment intrusions undertaken pursuant to a <span class="star-pagination">*46</span> general scheme without individualized suspicion. Accordingly, <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> does not preclude an inquiry into programmatic purpose in such contexts. Cf. <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305</a></span> (1997); <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989); <i><span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/" aria-description="Citation for case: New York v. Burger">Burger, supra;</a></span> </i><i>Michigan</i> v. <i>Tyler,</i> <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499</a></span> (1978); <i>Camara</i> v. <i>Municipal Court of City and County of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). It likewise does not preclude an inquiry into programmatic purpose here.</p>
<p>Last Term in <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span>,</i> we addressed the question whether a law enforcement officer violated a reasonable expectation of privacy in conducting a tactile examination of carry-on luggage in the overhead compartment of a bus. In doing so, we simply noted that the principle of <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> rendered the subjective intent of an officer irrelevant to this analysis. <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U. S., at 338, n. 2</a></span>. While, as petitioners correctly observe, the analytical rubric of <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span></i> was not "ordinary, probable-cause Fourth Amendment analysis," <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States"><i>Whren, supra,</i>  at 813</a></span>, nothing in <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span></i> suggests that we would extend the principle of <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> to all situations where individualized suspicion was lacking. Rather, subjective intent was irrelevant in <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span></i> because the inquiry that our precedents required focused on the objective effects of the actions of an individual officer. By contrast, our cases dealing with intrusions that occur pursuant to a general scheme absent individualized suspicion have often required an inquiry into purpose at the programmatic level.</p>
<p>Petitioners argue that the Indianapolis checkpoint program is justified by its lawful secondary purposes of keeping impaired motorists off the road and verifying licenses and registrations. Brief for Petitioners 31-34. If this were the case, however, law enforcement authorities would be able to establish checkpoints for virtually any purpose so long as they also included a license or sobriety check. For this reason, we examine the available evidence to determine the primary purpose of the checkpoint program. While we recognize the challenges inherent in a purpose inquiry, courts <span class="star-pagination">*47</span> routinely engage in this enterprise in many areas of constitutional jurisprudence as a means of sifting abusive governmental conduct from that which is lawful. Cf. <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#665" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d, at 665</a></span>. As a result, a program driven by an impermissible purpose may be proscribed while a program impelled by licit purposes is permitted, even though the challenged conduct may be outwardly similar. While reasonableness under the Fourth Amendment is predominantly an objective inquiry, our special needs and administrative search cases demonstrate that purpose is often relevant when suspicionless intrusions pursuant to a general scheme are at issue.<sup>[2]</sup></p>
<p>It goes without saying that our holding today does nothing to alter the constitutional status of the sobriety and border checkpoints that we approved in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i>  or of the type of traffic checkpoint that we suggested would be lawful in <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>.</i> The constitutionality of such checkpoint programs still depends on a balancing of the competing interests at stake and the effectiveness of the program. See <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#450" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 450-455</a></span>; <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-564</a></span>. When law enforcement authorities pursue primarily general crime control purposes at checkpoints such as here, however, stops can only be justified by some quantum of individualized suspicion.</p>
<p>Our holding also does not affect the validity of border searches or searches at places like airports and government <span class="star-pagination">*48</span> buildings, where the need for such measures to ensure public safety can be particularly acute. Nor does our opinion speak to other intrusions aimed primarily at purposes beyond the general interest in crime control. Our holding also does not impair the ability of police officers to act appropriately upon information that they properly learn during a checkpoint stop justified by a lawful primary purpose, even where such action may result in the arrest of a motorist for an offense unrelated to that purpose. Finally, we caution that the purpose inquiry in this context is to be conducted only at the programmatic level and is not an invitation to probe the minds of individual officers acting at the scene. Cf. <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren, supra</a></span></i><i>.</i> </p>
<p>Because the primary purpose of the Indianapolis checkpoint program is ultimately indistinguishable from the general interest in crime control, the checkpoints violate the Fourth Amendment. The judgment of the Court of Appeals is, accordingly, affirmed.</p>
<p><i>It is so ordered.</i> </p>
<p>Chief Justice Rehnquist, with whom Justice Thomas joins, and with whom Justice Scalia joins as to Part I, dissenting.</p>
<p>The State's use of a drug-sniffing dog, according to the Court's holding, annuls what is otherwise plainly constitutional under our Fourth Amendment jurisprudence: brief, standardized, discretionless, roadblock seizures of automobiles, seizures which effectively serve a weighty state interest with only minimal intrusion on the privacy of their occupants. Because these seizures serve the State's accepted and significant interests of preventing drunken driving and checking for driver's licenses and vehicle registrations, and because there is nothing in the record to indicate that the addition of the dog sniff lengthens these otherwise legitimate seizures, I dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*49</span> I</h2>
<p>As it is nowhere to be found in the Court's opinion, I begin with blackletter roadblock seizure law. "The principal protection of Fourth Amendment rights at checkpoints lies in appropriate limitations on the scope of the stop." <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#566" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 566-567</a></span> (1976). Roadblock seizures are consistent with the Fourth Amendment if they are "carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers." <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979). Specifically, the constitutionality of a seizure turns upon "a weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty." <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 50-51</a></span>.</p>
<p>We first applied these principles in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> which approved highway checkpoints for detecting illegal aliens. In <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> we balanced the United States' formidable interest in checking the flow of illegal immigrants against the limited "objective" and "subjective" intrusion on the motorists. The objective intrusionthe stop itself,<sup>[1]</sup> the brief questioning of the occupants, and the visual inspection of the carwas considered "limited" because "[n]either the vehicle nor its occupants [were] searched." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 558</a></span>. Likewise, the subjective intrusion, or the fear and surprise engendered in law-abiding motorists by the nature of the stop, was found to be minimal because the "regularized manner in which [the] established checkpoints [were] operated [was] visible evidence, reassuring to law-abiding motorists, that the stops [were] duly authorized and believed to serve the public interest." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#559" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 559</a></span>. Indeed, the standardized operation of the roadblocks was viewed as <span class="star-pagination">*50</span> markedly different from roving patrols, where the unbridled discretion of officers in the field could result in unlimited interference with motorists' use of the highways. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975). And although the decision in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> did not turn on the checkpoints' effectiveness, the record in one of the consolidated cases demonstrated that illegal aliens were found in 0.12 percent of the stopped vehicles. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 554</a></span>.</p>
<p>In <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990), we upheld the State's use of a highway sobriety checkpoint after applying the framework set out in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> and <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas, supra</a></span></i><i>.</i> There, we recognized the gravity of the State's interest in curbing drunken driving and found the objective intrusion of the approximately 25-second seizure to be "slight." <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#451" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 451</a></span>. Turning to the subjective intrusion, we noted that the checkpoint was selected pursuant to guidelines and was operated by uniformed officers. See <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#453" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>id.,</i> at 453</a></span>. Finally, we concluded that the program effectively furthered the State's interest because the checkpoint resulted in the arrest of two drunk drivers, or 1.6 percent of the 126 drivers stopped. See <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#455" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>id.,</i> at 455-456</a></span>.</p>
<p>This case follows naturally from <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>.</i>  Petitioners acknowledge that the "primary purpose" of these roadblocks is to interdict illegal drugs, but this fact should not be controlling. Even accepting the Court's conclusion that the checkpoints at issue in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i>  were not primarily related to criminal law enforcement,<sup>[2]</sup> the <span class="star-pagination">*51</span> question whether a law enforcement purpose could support a roadblock seizure is not presented in this case. The District Court found that another "purpose of the checkpoints is to check driver's licenses and vehicle registrations," App. to Pet. for Cert. 44a, and the written directives state that the police officers are to "[l]ook for signs of impairment," <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">id.,</a></span></i> at 53a. The use of roadblocks to look for signs of impairment was validated by <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>,</i> and the use of roadblocks to check for driver's licenses and vehicle registrations was expressly recognized in <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span> (1979).<sup>[3]</sup> That the roadblocks serve these legitimate state interests cannot be seriously disputed, as the 49 people arrested for offenses unrelated to drugs can attest. <i>Edmond</i> v. <i>Goldsmith,</i> <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#661" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d 659, 661</a></span> (CA7 1999). And it would be speculative to concludegiven the District Court's findings, the written directives, and the actual arreststhat petitioners would not have operated these roadblocks but for the State's interest in interdicting drugs.</p>
<p>Because of the valid reasons for conducting these roadblock seizures, it is constitutionally irrelevant that petitioners also hoped to interdict drugs. In <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), we held that an officer's subjective intent would not invalidate an otherwise objectively justifiable stop of an automobile. The reasonableness of an officer's discretionary decision to stop an automobile, at issue in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>,</i> turns on whether there is probable cause to believe that a traffic violation has occurred. The reasonableness of highway checkpoints, at issue here, turns on whether they effectively serve a significant state interest with minimal intrusion on motorists. The stop in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> was objectively reasonable because the police officers had witnessed traffic violations; so too the roadblocks here are objectively <span class="star-pagination">*52</span> reasonable because they serve the substantial interests of preventing drunken driving and checking for driver's licenses and vehicle registrations with minimal intrusion on motorists.</p>
<p>Once the constitutional requirements for a particular seizure are satisfied, the subjective expectations of those responsible for it, be it police officers or members of a city council, are irrelevant. Cf. <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#136" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 136</a></span> (1978) ("Subjective intent alone . . . does not make otherwise lawful conduct illegal or unconstitutional"). It is the objective effect of the State's actions on the privacy of the individual that animates the Fourth Amendment. See <i>Bond</i> v. <i>United States,</i> <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U. S. 334, 338, n. 2</a></span> (2000) (applying <i>Whren</i> to determine if an officer's conduct amounted to a "search" under the Fourth Amendment because "the issue is not his state of mind, but the objective effect of his actions"). Because the objective intrusion of a valid seizure does not turn upon anyone's subjective thoughts, neither should our constitutional analysis.<sup>[4]</sup></p>
<p>With these checkpoints serving two important state interests, the remaining prongs of the <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas</a></span></i> balancing test are easily met. The seizure is objectively reasonable as it lasts, on average, two to three minutes and does not involve a search. App. to Pet. for Cert. 57a. The subjective intrusion is likewise limited as the checkpoints are clearly marked and operated by uniformed officers who are directed to stop every vehicle in the same manner. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Ibid.</a></span></i> The only difference between this case and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> is the presence of the dog. We have already held, however, that a "sniff test" by a trained narcotics dog is not a "search" within the meaning of the Fourth Amendment because it does not require physical intrusion of the object being sniffed and it does not expose <span class="star-pagination">*53</span> anything other than the contraband items. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U. S. 696, 706-707</a></span> (1983). And there is nothing in the record to indicate that the dog sniff lengthens the stop. Finally, the checkpoints' success rate49 arrests for offenses unrelated to drugsonly confirms the State's legitimate interests in preventing drunken driving and ensuring the proper licensing of drivers and registration of their vehicles. <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#661" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d, at 661</a></span>.<sup>[5]</sup></p>
<p>These stops effectively serve the State's legitimate interests; they are executed in a regularized and neutral manner; and they only minimally intrude upon the privacy of the motorists. They should therefore be constitutional.</p>
<p></p>
<h2>II</h2>
<p>The Court, unwilling to adopt the straightforward analysis that these precedents dictate, adds a new non-lawenforcement primary purpose test lifted from a distinct area of Fourth Amendment jurisprudence relating to the <i>searches</i>  of homes and businesses. As discussed above, the question that the Court answers is not even posed in this case given the accepted reasons for the seizures. But more fundamentally, whatever sense a non-law-enforcement primary purpose test may make in the search setting, it is ill suited to brief roadblock seizures, where we have consistently looked at "the scope of the stop" in assessing a program's constitutionality. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#567" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 567</a></span>.</p>
<p>We have already rejected an invitation to apply the nonlaw-enforcement primary purpose test that the Court now finds so indispensable. The respondents in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> argued that the <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas</a></span></i> balancing test was not the "proper method of analysis" with regards to roadblock seizures:</p>
<blockquote>"Respondents argue that there must be a showing of some special governmental need `beyond the normal <span class="star-pagination">*54</span> need' for criminal law enforcement before a balancing analysis is appropriate, and that [the State] ha[s] demonstrated no such special need.</blockquote>
<blockquote>"But it is perfectly plain from a reading of [<i>Treasury</i>  <i>Employees</i> v.] <i>Von Raab</i> [, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989)], which cited and discussed with approval our earlier decision in <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), that it was in no way designed to repudiate our prior cases dealing with police stops of motorists on public highways. <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> which utilized a balancing analysis in approving highway checkpoints for detecting illegal aliens, and <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas, supra</a></span></i><i>,</i> are the relevant authorities here." <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#449" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 449, 450</a></span>.</blockquote>
<p>Considerations of <i>stare decisis</i> aside, the "perfectly plain" reason for not incorporating the "special needs" test in our roadblock seizure cases is that seizures of automobiles "deal neither with searches nor with the sanctity of private dwellings, ordinarily afforded the most stringent Fourth Amendment protection." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 561</a></span>.</p>
<p>The "special needs" doctrine, which has been used to uphold certain suspicionless searches performed for reasons unrelated to law enforcement, is an exception to the general rule that a search must be based on individualized suspicion of wrongdoing. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989) (drug test search); <i>Camara</i>  v. <i>Municipal Court of City and County of San Francisco,</i>  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967) (home administrative search). The doctrine permits intrusions into a person's body and home, areas afforded the greatest Fourth Amendment protection. But there were no such intrusions here.</p>
<p>"[O]ne's expectation of privacy in an automobile and of freedom in its operation are significantly different from the traditional expectation of privacy and freedom in one's residence." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 561</a></span>. This is because "[a]utomobiles, unlike homes, are subjected to pervasive and continuing governmental regulation and controls." <i>South</i>  <span class="star-pagination">*55</span> <i>Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976); see also <i>New York</i> v. <i>Class,</i> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#113" aria-description="Citation for case: New York v. Class">475 U. S. 106, 113</a></span> (1986) ("[A]utomobiles are justifiably the subject of pervasive regulation by the State"); <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) ("One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects"). The lowered expectation of privacy in one's automobile is coupled with the limited nature of the intrusion: a brief, standardized, nonintrusive seizure.<sup>[6]</sup> The brief seizure of an automobile can hardly be compared to the intrusive search of the body or the home. Thus, just as the "special needs" inquiry serves to both define and limit the permissible scope of those searches, the <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas</a></span></i> balancing test serves to define and limit the permissible scope of automobile seizures.</p>
<p>Because of these extrinsic limitations upon roadblock seizures, the Court's newfound non-law-enforcement primary purpose test is both unnecessary to secure Fourth Amendment rights and bound to produce wide-ranging litigation over the "purpose" of any given seizure. Police designing highway roadblocks can never be sure of their validity, since a jury might later determine that a forbidden purpose exists. Roadblock stops identical to the one that we upheld in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i>  10 years ago, or to the one that we upheld 24 years ago in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> may now be challenged on the grounds that they have some concealed forbidden purpose.</p>
<p>Efforts to enforce the law on public highways used by millions of motorists are obviously necessary to our society. The Court's opinion today casts a shadow over what had been assumed, on the basis of <i>stare decisis,</i> to be a perfectly lawful activity. Conversely, if the Indianapolis police had assigned a different purpose to their activity here, but in no way changed what was done on the ground to individual <span class="star-pagination">*56</span> motorists, it might well be valid. See <i>ante,</i> at 47, n. 2. The Court's non-law-enforcement primary purpose test simply does not serve as a proxy for anything that the Fourth Amendment is, or should be, concerned about in the automobile seizure context.</p>
<p>Petitioners' program complies with our decisions regarding roadblock seizures of automobiles, and the addition of a dog sniff does not add to the length or the intrusion of the stop. Because such stops are consistent with the Fourth Amendment, I would reverse the decision of the Court of Appeals.</p>
<p>Justice Thomas, dissenting.</p>
<p>Taken together, our decisions in <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990), and <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), stand for the proposition that suspicionless roadblock seizures are constitutionally permissible if conducted according to a plan that limits the discretion of the officers conducting the stops. I am not convinced that <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> were correctly decided. Indeed, I rather doubt that the Framers of the Fourth Amendment would have considered "reasonable" a program of indiscriminate stops of individuals not suspected of wrongdoing.</p>
<p>Respondents did not, however, advocate the overruling of <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> and I am reluctant to consider such a step without the benefit of briefing and argument. For the reasons given by The Chief Justice, I believe that those cases compel upholding the program at issue here. I, therefore, join his opinion.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Kansas et al. by <i>Carla J. Stovall,</i> Attorney General of Kansas, <i>Stephen R. McAllister,</i> State Solicitor, <i>Jared S. Maag,</i> Assistant Attorney General, and <i>John M. Bailey,</i> Chief State's Attorney of Connecticut, and by the Attorneys General for their respective States as follows: <i>Bill Pryor</i> of Alabama, <i>Janet Napolitano</i> of Arizona, <i>Mark Pryor</i> of Arkansas, <i>Bill Lockyer</i> of California, <i>Robert A. Butterworth</i> of Florida, <i>James E. Ryan</i>  of Illinois, <i>Karen M. Freeman-Wilson</i> of Indiana, <i>Thomas J. Miller</i> of Iowa, <i>Michael C. Moore</i> of Mississippi, <i>Don Stenberg</i> of Nebraska, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Jan Graham</i> of Utah, and <i>Mark L. Earley</i>  of Virginia; for the National League of Cities et al. by <i>Richard Ruda</i> and <i>James I. Crowley;</i> and for the Washington Legal Foundation et al. by <i>Daniel J. Popeo.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the National Association of Criminal Defense Lawyers et al. by <i>Wesley MacNeil Oliver</i>  and <i>Barbara Bergman;</i> and for the Rutherford Institute by <i>John W. Whitehead</i> and <i>Steven H. Aden.</i> </p>
<p><i>Wayne W. Schmidt, James P. Manak, Richard Weintraub,</i> and <i>Bernard J. Farber</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae.</i> </p>
<p>[1]  The Chief Justice's dissent erroneously characterizes our opinion as resting on the application of a "non-law-enforcement primary purpose test." <i>Post,</i> at 53. Our opinion nowhere describes the purposes of the <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> checkpoints as being "not primarily related to criminal law enforcement." <i>Post,</i> at 50. Rather, our judgment turns on the fact that the primary purpose of the Indianapolis checkpoints is to advance the general interest in crime control.
</p>
<p>The Chief Justice's dissent also erroneously characterizes our opinion as holding that the "use of a drug-sniffing dog . . . annuls what is otherwise plainly constitutional under our Fourth Amendment jurisprudence." <i>Post,</i> at 48. Again, the constitutional defect of the program is that its primary purpose is to advance the general interest in crime control.</p>
<p>[2]  Because petitioners concede that the primary purpose of the Indianapolis checkpoints is narcotics detection, we need not decide whether the State may establish a checkpoint program with the primary purpose of checking licenses or driver sobriety and a secondary purpose of interdicting narcotics. Specifically, we express no view on the question whether police may expand the scope of a license or sobriety checkpoint seizure in order to detect the presence of drugs in a stopped car. Cf. <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 341</a></span> (1985) (search must be "`reasonably related in scope to the circumstances which justified the interference in the first place' " (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968))); <i>Michigan</i> v. <i>Clifford,</i> <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#294" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287, 294-295</a></span> (1984) (plurality opinion).</p>
<p>[1]  The record from one of the consolidated cases indicated that the stops lasted between three and five minutes. See <i>United States</i> v. <i>MartinezFuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#546" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 546-547</a></span> (1976).</p>
<p>[2]  This gloss, see <i>ante,</i> at 38-40, 41-43, is not at all obvious. The respondents in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> were criminally prosecuted for illegally transporting aliens, and the Court expressly noted that "[i]nterdicting the flow of illegal entrants from Mexico poses formidable law enforcement problems." 428 U. S., at 552. And the <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> Court recognized that if an "officer's observations suggest that the driver was intoxicated, an arrest would be made." <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 447</a></span>. But however persuasive the distinction, the Court's opinion does not impugn the continuing validity of <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>.</i> See <i>ante,</i> at 47.</p>
<p>[3]  Several Courts of Appeals have upheld roadblocks that check for driver's licenses and vehicle registrations. See, <i>e. g., </i><i>United States</i>  v. <i>Galindo-Gonzales,</i> <span class="citation" data-id="156261"><a href="/opinion/156261/united-states-v-galindo-gonzales/" aria-description="Citation for case: United States v. Galindo-Gonzales">142 F. 3d 1217</a></span> (CA10 1998); <i>United States</i> v. <i>McFayden,</i> <span class="citation" data-id="517399"><a href="/opinion/517399/united-states-v-gregory-mcfayden/" aria-description="Citation for case: United States v. Gregory McFayden">865 F. 2d 1306</a></span> (CADC 1989).</p>
<p>[4]  Of course we have looked to the purpose of the program in analyzing the constitutionality of certain suspicionless searches. As discussed in Part II, <i>infra,</i> that doctrine has never been applied to seizures of automobiles.</p>
<p>[5]  Put in statistical terms, 4.2 percent of the 1,161 motorists stopped were arrested for offenses unrelated to drugs.</p>
<p>[6]  This fact distinguishes the roadblock seizure of an automobile from an inventory search of an automobile. Cf. <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367</a></span> (1987) (automobile inventory search).</p>

</div>
```

---
