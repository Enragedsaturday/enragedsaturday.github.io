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

## GROUP: content/cases/Hill v. California.md  (`case`, 6 assertions)

### content_page

```
---
title: "Hill v. California"
type: case
citation: "401 U.S. 797 (1971)"
parallel_cite: "91 S. Ct. 1106; 28 L. Ed. 2d 484; 27 A.F.T.R.2d (RIA) 1006"
neutral_cite: 1971 U.S. LEXIS 59
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-04-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-04-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hill v. California
  varies_by_point: false
  scope_note: "Good law. When police have probable cause to arrest one person and reasonably, in good faith, mistake another for that person, the arrest of the second person is valid, and so is the ensuing search incident to arrest. Sufficient probability, not certainty, is the touchstone of Fourth Amendment reasonableness."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108305/hill-v-california/"
  cluster_id: 108305
  opinion_id: 108305
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Progeny"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
related: ["[[Brinegar v. United States]]", "[[Chimel v. California]]", "[[Heien v. North Carolina]]", "[[Maryland v. Garrison]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "probable-cause", "mistaken-identity", "search-incident-to-arrest"]
holding: "An arrest of the wrong person is valid where police have probable cause to arrest one person and reasonably, in good faith, mistake the arrestee for that person; the search incident to that arrest is likewise valid."
lake:
  record_id: Hill v. California
  status: verified
  projected_at: 2026-07-09
---

# Hill v. California

*401 U.S. 797 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police had probable cause to arrest Hill for robbery and had his address and a verified physical description. At Hill's apartment they encountered Miller, who matched the description of Hill. Miller insisted he was Miller, not Hill, and produced identification, but his explanation for being in the locked apartment was unconvincing, and a pistol and a loaded ammunition clip lay in plain view. Believing Miller was Hill, the officers arrested him and searched the apartment incident to the arrest, seizing evidence later used to convict the actual Hill. Hill moved to suppress, arguing the arrest of the wrong man was invalid and the search therefore unlawful.

## Issue
Whether an arrest is valid — and a search incident to it lawful — when police have probable cause to arrest one person but, reasonably and in good faith, arrest a different person whom they mistake for the suspect.

## Rule
Yes. The Court adopted the rule that "[w]hen the police have probable cause to arrest one party, and when they reasonably mistake a second party for the first party, then the arrest of the second party is a valid arrest." — 401 U.S. at 802. ^pin-802

Good faith alone is not enough; the test is objective reasonableness: "sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time." — [*Id.* at 804](https://www.courtlistener.com/opinion/108305/hill-v-california/#:~:text=sufficient%20probability%2C%20not%20certainty%2C%20is). ^pin-804

A valid arrest of the mistaken person supports a search incident to it: "the police were entitled to do what the law would have allowed them to do if Miller had in fact been Hill, that is, to search incident to arrest and to seize evidence of the crime the police had probable cause to believe Hill had committed." — [*Id.* at 804–805](https://www.courtlistener.com/opinion/108305/hill-v-california/#:~:text=the%20police%20were%20entitled%20to). ^pin-804b

## Application
The officers had unquestionable probable cause to arrest Hill, a verified description, and his address. When they found Miller — who fit that description, gave an unconvincing account of his presence, and had a pistol and ammunition in plain view — their belief that Miller was Hill was an understandable, objectively reasonable mistake, not mere subjective good faith. Because the arrest was therefore valid, the search incident to it (judged under pre-*[[Chimel v. California|Chimel]]* scope, which the Court declined to apply retroactively here) was also valid, and the seized evidence was admissible against Hill.

## Conclusion
The reasonable, good-faith arrest of the wrong man was valid, as was the search incident to it; the judgment was affirmed. Fourth Amendment reasonableness tolerates an understandable mistake of identity where police have probable cause to arrest the intended suspect.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hill*'s reasonable-mistake principle applies the practical probable-cause standard of [[Brinegar v. United States]] and parallels [[Maryland v. Garrison]] (reasonable mistake as to the apartment to be searched) and [[Heien v. North Carolina]] (reasonable mistake of law); the search-incident analysis tracks [[Chimel v. California]].

## Appears on
- [[Probable Cause]] — *Progeny*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *Hill v. California*, 401 U.S. 797 (1971) — https://www.courtlistener.com/opinion/108305/hill-v-california/ — pinpoints: 802, 804–805.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ca0ac06e3903e13e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "401 U.S. 797 (1971)", "court": "U.S. Supreme Court", "neutral_cite": "1971 U.S. LEXIS 59", "official_citation_present": true, "parallel_cite": "91 S. Ct. 1106; 28 L. Ed. 2d 484; 27 A.F.T.R.2d (RIA) 1006", "title": "Hill v. California", "year": "1971"}}
{"assertion_id": "183b8903f795b57b", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Related (cross-doctrine)", "title": "Hill v. California"}}
{"assertion_id": "6bdae4c272fb7f6f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An arrest of the wrong person is valid where police have probable cause to arrest one person and reasonably, in good faith, mistake the arrestee for that person; the search incident to that arrest is likewise valid.", "title": "Hill v. California"}}
{"assertion_id": "6c441665d5cd1508", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Progeny", "title": "Hill v. California"}}
{"assertion_id": "6fb10e57d3b4baf6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1971-04-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hill v. California", "field_i_validity": "good_law", "scope_note": "Good law. When police have probable cause to arrest one person and reasonably, in good faith, mistake another for that person, the arrest of the second person is valid, and so is the ensuing search incident to arrest. Sufficient probability, not certainty, is the touchstone of Fourth Amendment reasonableness.", "title": "Hill v. California", "varies_by_point": "false"}}
{"assertion_id": "d04330eb5eebbd7d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hill v. California"}}
```

### lake record — Hill v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hill v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hill v. California",
    "case_name_short": "Hill",
    "case_name_full": "Hill v. California",
    "input_case_name": "Hill v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-04-05",
    "year": 1971,
    "docket": null,
    "cluster_id": 108305,
    "lead_opinion_id": 108305,
    "sibling_ids": [
      108305,
      9424518,
      9424519
    ],
    "absolute_url": "/opinion/108305/hill-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "401 U.S. 797",
      "volume": "401",
      "reporter": "U.S.",
      "page": "797",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 1106",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 484",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "27 A.F.T.R.2d (RIA) 1006",
        "volume": "27",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1006",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 59",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "59",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "401 U.S. 797",
        "volume": "401",
        "reporter": "U.S.",
        "page": "797",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 1106",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 484",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 59",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "59",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "27 A.F.T.R.2d (RIA) 1006",
        "volume": "27",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1006",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "401 U.S. 797",
    "official_selection": {
      "court_class": "scotus",
      "selected": "401 U.S. 797",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-802",
      "page": null,
      "quote": "--- # Hill v. California *401 U.S. 797 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police had probable cause to arrest Hill for robbery and had his address and a verified physical description. At Hill's apartment they encountered Miller, who matched the description of Hill. Miller insisted he was Miller, not Hill, and produced identification, but his explanation for being in the locked apartment was unconvincing, and a pistol and a loaded ammunition clip lay in plain view. Believing Miller was Hill, the officers arrested him and searched the apartment incident to the arrest, seizing evidence later used to convict the actual Hill. Hill moved to suppress, arguing the arrest of the wrong man was invalid and the search therefore unlawful. ## Issue Whether an arrest is valid \u2014 and a search incident to it lawful \u2014 when police have probable cause to arrest one person but, reasonably and in good faith, arrest a different person whom they mistake for the suspect. ## Rule Yes. The Court adopted the rule that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-804",
      "page": null,
      "quote": "sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time.",
      "star_marker": "804",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9745,
      "fragment": "#:~:text=sufficient%20probability%2C%20not%20certainty%2C%20is",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-804b",
      "page": null,
      "quote": "the police were entitled to do what the law would have allowed them to do if Miller had in fact been Hill, that is, to search incident to arrest and to seize evidence of the crime the police had probable cause to believe Hill had committed.",
      "star_marker": "804",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10677,
      "fragment": "#:~:text=the%20police%20were%20entitled%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-04-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hill v. California",
    "varies_by_point": false,
    "scope_note": "Good law. When police have probable cause to arrest one person and reasonably, in good faith, mistake another for that person, the arrest of the second person is valid, and so is the ensuing search incident to arrest. Sufficient probability, not certainty, is the touchstone of Fourth Amendment reasonableness.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Hill v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Damian D.",
          "cluster_id": 6578334,
          "cite": [
            "434 Mass. 725",
            "752 N.E.2d 679",
            "2001 Mass. LEXIS 410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mendenhall v. Riser",
          "cluster_id": 21122,
          "cite": [
            "213 F.3d 226",
            "2000 WL 691548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane1_negative"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Graham v. Connor",
          "cluster_id": 112257,
          "cite": [
            "104 L. Ed. 2d 443",
            "109 S. Ct. 1865",
            "490 U.S. 386",
            "1989 U.S. LEXIS 2467",
            "57 U.S.L.W. 4513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia Court of Appeals v. Feldman",
          "cluster_id": 110889,
          "cite": [
            "75 L. Ed. 2d 206",
            "103 S. Ct. 1303",
            "460 U.S. 462",
            "1983 U.S. LEXIS 150",
            "51 U.S.L.W. 4285"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chevron Oil Co. v. Huson",
          "cluster_id": 108406,
          "cite": [
            "30 L. Ed. 2d 296",
            "92 S. Ct. 349",
            "404 U.S. 97",
            "1971 U.S. LEXIS 95"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
          "cluster_id": 112218,
          "cite": [
            "103 L. Ed. 2d 628",
            "109 S. Ct. 1378",
            "489 U.S. 593",
            "1989 U.S. LEXIS 1569",
            "57 U.S.L.W. 4321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cantor",
          "cluster_id": 5681132,
          "cite": [
            "36 N.Y.2d 106",
            "324 N.E.2d 872",
            "365 N.Y.S.2d 509",
            "1975 N.Y. LEXIS 3100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wood v. Georgia",
          "cluster_id": 110425,
          "cite": [
            "67 L. Ed. 2d 220",
            "101 S. Ct. 1097",
            "450 U.S. 261",
            "1981 U.S. LEXIS 76",
            "49 U.S.L.W. 4218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Evans",
          "cluster_id": 1538821,
          "cite": [
            "165 Conn. 61",
            "327 A.2d 576",
            "1973 Conn. LEXIS 709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Outboard Marine Corp.",
          "cluster_id": 762789,
          "cite": [
            "172 F.3d 531",
            "1999 U.S. App. LEXIS 5444",
            "1999 WL 164061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Peltier",
          "cluster_id": 109302,
          "cite": [
            "45 L. Ed. 2d 374",
            "95 S. Ct. 2313",
            "422 U.S. 531",
            "1975 U.S. LEXIS 155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manganiello v. City of New York",
          "cluster_id": 2522805,
          "cite": [
            "612 F.3d 149",
            "2010 U.S. App. LEXIS 15156",
            "2010 WL 2884967"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buchanan v. Kentucky",
          "cluster_id": 111947,
          "cite": [
            "97 L. Ed. 2d 336",
            "107 S. Ct. 2906",
            "483 U.S. 402",
            "1987 U.S. LEXIS 2877",
            "55 U.S.L.W. 5026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patricia Scott v. Clay County, Tennessee Chinn Anderson Billy Pierce Michael Thompson",
          "cluster_id": 767897,
          "cite": [
            "205 F.3d 867",
            "2000 U.S. App. LEXIS 2965",
            "2000 WL 228300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harvey",
          "cluster_id": 1343416,
          "cite": [
            "187 S.E.2d 706",
            "281 N.C. 1",
            "1972 N.C. LEXIS 1321"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. City of Madera",
          "cluster_id": 223714,
          "cite": [
            "648 F.3d 1119",
            "2011 U.S. App. LEXIS 17459",
            "2011 WL 3659355"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glenn v. City of Tyler",
          "cluster_id": 23151,
          "cite": [
            "242 F.3d 307",
            "2001 U.S. App. LEXIS 2585",
            "2001 WL 102270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atkins v. City of Chicago",
          "cluster_id": 183500,
          "cite": [
            "631 F.3d 823",
            "2011 U.S. App. LEXIS 1459",
            "2011 WL 206155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108305 OR 9424518 OR 9424519) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OTU0MzM2MDAwMDAmcz0yMTA0Njg2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108305+OR+9424518+OR+9424519%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(108305 OR 9424518 OR 9424519)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzkmcz00OTA1OTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108305+OR+9424518+OR+9424519%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108305 OR 9424518 OR 9424519)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108305 OR 9424518 OR 9424519)",
    "indexed_citing_opinions": 451,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108305,
        "count": 400,
        "count_source": "search"
      },
      {
        "opinion_id": 9424518,
        "count": 55,
        "count_source": "search"
      },
      {
        "opinion_id": 9424519,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 766,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hill-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY5NDk5NzMmcz00NzkwNjE5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108305+OR+9424518+OR+9424519%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108305,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 107889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 1129895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 1428394,
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
    "date_created": "2026-07-05T07:10:37Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:10:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:10:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:14:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:10:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hill v. California

```
<div>
<center><b><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U.S. 797</a></span> (1971)</b></center>
<center><h1>HILL<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 51.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 19, 1970</center>
<center>Reargued October 21, 1970</center>
<center>Decided April 5, 1971</center>
CERTIORARI TO THE SUPREME COURT OF CALIFORNIA.
<p><span class="star-pagination">*798</span> <i>Joseph Amato,</i> appointed by the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./396/999/">396 U. S. 999</a></span>, reargued the cause for petitioner.</p>
<p><i>Ronald M. George,</i> Deputy Attorney General of California, reargued the cause for respondent. With him on the brief were <i>Thomas C. Lynch,</i> Attorney General, and <i>William E. James,</i> Assistant Attorney General.</p>
<p><i>Keith C. Monroe</i> filed a brief for the Orange County Criminal Courts Bar Association et al. as <i>amici curiae</i> urging reversal. <i>Duke W. Dunbar,</i> Attorney General, <i>pro se,</i> and <i>John P. Moore,</i> Deputy Attorney General, filed a brief for the Attorney General of Colorado et al. as <i>amici curiae.</i></p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>On June 4, 1966, four armed men robbed a residence in Studio City, California. On June 5, Alfred Baum and Richard Bader were arrested for possession of narcotics; at the time of their arrest, they were driving petitioner Hill's car, and a search of the car produced property stolen in the Studio City robbery the day before. Bader and Baum both admitted taking part in the June 4 robbery, and both implicated Hill. Bader told the police that he was sharing an apartment with Hill at 9311 <span class="star-pagination">*799</span> Sepulveda Boulevard. He also stated that the guns used in the robbery and other stolen property were in the apartment. On June 6, Baum and Bader again told the police that Hill had been involved in the June 4 robbery.</p>
<p>One of the investigating officers then checked official records on Hill, verifying his prior association with Bader, his age and physical description, his address, and the make of his car. The information the officer uncovered corresponded with the general descriptions by the robbery victims and the statements made by Baum and Bader.</p>
<p>Hill concedes that this information gave the police probable cause to arrest him, and the police undertook to do so on June 6. Four officers went to the Sepulveda Boulevard apartment, verified the address, and knocked. One of the officers testified: "The door was opened and a person who fit the description exactly of Archie Hill, as I had received it from both the cards and from Baum and Bader, answered the door. . . . We placed him under arrest for robbery."</p>
<p>The police had neither an arrest nor a search warrant. After arresting the man who answered the door, they asked him whether he was Hill and where the guns and stolen goods were. The arrestee replied that he was not Hill, that his name was Miller, that it was Hill's apartment and that he was waiting for Hill. He also claimed that he knew nothing about any stolen property or guns, although the police testified that an automatic pistol and a clip of ammunition were lying in plain view on a coffee table in the living room where the arrest took place. The arrestee then produced identification indicating that he was in fact Miller, but the police were unimpressed and proceeded to search the apartment living room, bedroom, kitchen area, and bathfor a period which one officer described as "a couple of hours."</p>
<p>During the course of the search, the police seized several <span class="star-pagination">*800</span> items: rent receipts and personal correspondence bearing Hill's name from a dresser drawer in the bedroom; a starter pistol, two switchblade knives, a camera and case stolen in the Studio City robbery, and two hoodmasks made from white T-shirts, all from the bedroom; a .22-caliber revolver from under the living room sofa; and two pages of petitioner Hill's diary from a bedroom dresser drawer.<sup>[1]</sup></p>
<p><span class="star-pagination">*801</span> On October 20, 1966, Hill was found guilty of robbery on the basis of evidence produced at the preliminary hearing and the trial.<sup>[2]</sup> Eyewitnesses to the robbery were unable to identify Hill; the only substantial evidence of his guilt consisted of the items seized in the search of his apartment. In sustaining the admissibility of the evidence, the trial judge ruled that the arresting officers had acted in the good-faith belief that Miller was in fact Hill.<sup>[3]</sup> The District Court of Appeal agreed that the officers acted in good faith and that the arrest of Miller was valid but nonetheless thought the incident search of Hill's apartment unreasonable under the Fourth Amendment. <span class="citation no-link">67 Cal. Rptr. 389</span> (1968).<sup>[4]</sup> The California Supreme Court in turn reversed, sustaining both the arrest and the search. <span class="citation multiple-matches"><a href="/c/Cal.%202d/69/550/">69 Cal. 2d 550</a></span>, <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/" aria-description="Citation for case: People v. Hill">446 P. 2d 521</a></span> (1968). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./396/818/">396 U. S. 818</a></span> (1969), and now affirm the judgment of the California Supreme Court.</p>
<p></p>
<h2>
<span class="star-pagination">*802</span> I</h2>
<p>Petitioner argues that <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), decided after his conviction was affirmed by the California Supreme Court, should be applied to his case, which is before us on direct review. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> narrowed the permissible scope of searches incident to arrest, but in <i>Williams</i> v. <i>United States</i> and <i>Elkanich</i> v. <i>United States, ante,</i> p. 646, we held <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> inapplicable to searches occurring before the date of decision in that caseregardless of whether a case was still on direct review when <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> was decided, see <i>Williams, supra,</i> or whether a <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> challenge was asserted in a subsequent collateral attack on a conviction. See <i>Elkanich, supra.</i> We also stated that in light of past decisions there was no difference in constitutional terms between state and federal prisoners insofar as retroactive application to their cases of a new interpretation of the Bill of Rights is concerned. <i>Ante,</i> at 656. The search of Hill's apartment, permissible in scope under pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> standards, will not be retrospectively invalidated because of that decision.</p>
<p></p>
<h2>II</h2>
<p>Based on our own examination of the record, we find no reason to disturb either the findings of the California courts that the police had probable cause to arrest Hill and that the arresting officers had a reasonable, goodfaith belief that the arrestee Miller was in fact Hill, or the conclusion that "[w]hen the police have probable cause to arrest one party, and when they reasonably mistake a second party for the first party, then the arrest of the second party is a valid arrest." <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/#553" aria-description="Citation for case: People v. Hill">69 Cal. 2d, at 553</a></span>, <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/#523" aria-description="Citation for case: People v. Hill">446 P. 2d, at 523</a></span>.<sup>[5]</sup> The police unquestionably had probable <span class="star-pagination">*803</span> cause to arrest Hill; they also had his address and a verified description. The mailbox at the indicated address listed Hill as the occupant of the apartment. Upon gaining entry to the apartment, they were confronted with one who fit the description of Hill received from various sources.<sup>[6]</sup> That person claimed he was Miller, not Hill. But aliases and false identifications are not uncommon.<sup>[7]</sup> Moreover, there was a lock on the door and Miller's explanation for his mode of entry was not convincing.<sup>[8]</sup> He also denied knowledge of firearms in the apartment although a pistol and loaded ammunition clip were in plain view in the room.<sup>[9]</sup> The upshot was that the officers <span class="star-pagination">*804</span> in good faith believed Miller was Hill and arrested him. They were quite wrong as it turned out, and subjective good-faith belief would not in itself justify either the arrest or the subsequent search. But sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time.</p>
<p>Nor can we agree with petitioner that however valid the arrest of Miller, the subsequent search violated the Fourth Amendment. It is true that Miller was not Hill; nor did Miller have authority or control over the premises, although at the very least he was Hill's guest. But the question is not what evidence would have been admissible against Hill (or against Miller for that matter) if the police, with probable cause to arrest Miller, had arrested him in Hill's apartment and then carried out the search at issue. Here there was probable cause to arrest Hill and the police arrested Miller in Hill's apartment, reasonably believing him to be Hill. In these circumstances the police were entitled to do what the law would have allowed them to do if Miller had in fact been Hill, that is, to search incident to arrest and to seize evidence of the crime the police had probable cause to believe Hill had committed. When judged in accordance with "the factual and practical considerations of everyday life on which reasonable and prudent men, not <span class="star-pagination">*805</span> legal technicians, act," <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949), the arrest and subsequent search were reasonable and valid under the Fourth Amendment.</p>
<p></p>
<h2>III</h2>
<p>Finally, in his brief in this Court, petitioner argues that the admission in evidence of the two pages of his diary Pages which contained what amounted to a confession of the robberyviolated the Fifth Amendment under <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886). Counsel for Hill conceded at oral argument that the Fifth Amendment issue was not raised at trial. Nor was the issue raised, briefed, or argued in the California appellate courts.<sup>[10]</sup> The petition for certiorari likewise ignored it. In this posture of the case, the question, although briefed and argued here, is not properly before us. In <i>Cardinale</i> v. <i>Louisiana,</i> <span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S. 437</a></span> (1969), certiorari was granted to consider the constitutionality of a Louisiana statute, but at oral argument it developed that the federal question had never been raised, preserved, or passed upon in the state courts. Relying on a long line of cases, we dismissed the writ for want of jurisdiction. <span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#439" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S., at 439</a></span>. In addition, we stated that there were sound policy reasons for adhering to such a rule. In the context of that case, we indicated the desirability of allowing state courts to pass first on the constitutionality of state statutes in light of a federal constitutional challenge; this assures both an adequate record and that the States have first opportunity to provide a definitive interpretation of their statutes. We also indicated that a federal habeas corpus remedy might remain if no state procedure for raising the issue was available following dismissal of the writ. These considerations are no less applicable in this <span class="star-pagination">*806</span> case. We therefore do not reach the Fifth Amendment question and affirm the judgment of the Supreme Court of California.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACK concurs in the result.</p>
<p>MR. JUSTICE DOUGLAS took no part in the consideration or the decision of this case.</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE MARSHALL joins, concurring in part and dissenting in part.</p>
<p>I agree with the Court's opinion except for its conclusion that the <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> case is not to be applied to this one.</p>
<p>Two Terms ago, in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), we held that a search without a warrant, but incident to a lawful arrest, must be narrowly confined in scope if it is to pass constitutional muster. In such circumstances, we said:</p>
<blockquote>"There is ample justification . . . for a search of the arrestee's person and the area `within his immediate control'construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.</blockquote>
<blockquote>"There is no comparable justification, however, for routinely searching any room other than that in which an arrest occursor, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself. Such searches, in the absence of well-recognized exceptions, may be made only under the authority of a search warrant. The `adherence to judicial processes' mandated by the Fourth Amendment requires no less." <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span> (footnote omitted).</blockquote>
<p><span class="star-pagination">*807</span> The search here involved, fully described in the Court's opinion, plainly exceeded the bounds set forth in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>.</i> The State contends that the search here was consistent with <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> because conducted in the evening when it was not possible to obtain a search warrant. Whatever validity such a limiting principle might have in other contexts, it certainly cannot properly be invoked here. Baum and Bader had implicated Hill at least 24 hours prior to the search of Hill's apartment. Moreover, the State does not explain why it would not have been possible to observe the apartment after the mistaken arrest of Miller as Hill and then test before a magistrate the validity of their belief that they had probable cause for the issuance of a warrant authorizing a complete search of the apartment.</p>
<p>Because I believe this case reveals an obvious violation of <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> and because I consider we are duty bound to apply the principles there enunciated to cases, like this one, before us on direct review, see my separate opinion in <i>Mackey</i> v. <i>United States</i> (and companion cases), <i>ante,</i> p. 675, decided today, I am compelled to cast my vote for reversal of the judgment of the Supreme Court of California.</p>
<h2>NOTES</h2>
<p>[1]  All of these items, except the rent receipts and correspondence, were later introduced in evidence at the preliminary examination involving Baum, Bader, and Hill. A radio stolen in the Studio City robbery was also introduced, since it was found in Hill's car when Baum and Bader were arrested. Finally, the State introduced two handwriting exemplars executed by petitioner Hill after his arrest. Although the rent receipts and personal correspondence were not introduced in evidence, one of the officers who participated in the arrest and search at the Hill apartment testified that in the same drawer where he found the diary pages "there were rent receipts, numerous stack of rent receipts at this particular apartment, made out to Archie Hill, and there were several other pieces of paper, correspondence, notes from girls, and so forth, all to an Archie or an Archie Hill." No objection was offered to this testimony.
</p>
<p>Thereafter, petitioner's case was severed from that of Baum and Bader. Hill waived a jury and submitted the case for trial on the transcript of the preliminary hearing and the exhibits there introduced. The State called one additional witness at trialOfficer Gastaldowho gave a more complete version of the investigation of the robbery and of the arrest of the man who turned out to be Miller. The two diary pages seized in Hill's apartment contained what was in effect a full confession of his participation in the Studio City robbery. The additional testimony of Officer Gastaldo was critical in establishing the legality of the arrest and subsequent search. After hearing this testimony, the trial judge denied petitioner's motion to suppress the items seized, including, of course, the diary pages. Hill presented no further evidence at trial, and was found guilty as charged. A motion for a new trial was subsequently denied, and petitioner's appeals in the California courts followed.</p>
<p>In his brief in this Court, petitioner attacks the admission of the diary pages on a ground never advanced below. For the reasons expressed in Part III of this opinion, we do not rule upon these contentions.</p>
<p>[2]  See n. 1, <i>supra.</i></p>
<p>[3]  The trial judge stated:
</p>
<p>"I have fully reviewed the evidence. I have determined that the officer in good faith believed that the defendant, or that the person who was arrestednot the defendant in this casewas believed by the officer in good faith to be Mr. Hill, and that whether or not this document consisting of two pages of the private diary of Mr. Hill should be admitted depends on whether or not at the time of the arrest and the search of the premises, the officer acted in good faith."</p>
<p>[4]  Justice Ford stated:
</p>
<p>"While the doctrine of probable cause assures a balance between the rights of the individual and those of the government with respect to the matter of arrest, the constitutional protection against unreasonable searches, particularly of a person's home, would be less than complete if a plenary search could be justified as incident to an arrest of a person mistakenly believed by an officer to be in immediate charge of the premises. Such a case is not one where the right of privacy must reasonably yield to the right of search." 67 Cal. Rptr., at 391.</p>
<p>[5]  The California Supreme Court relied on <i>People</i> v. <i>Kitchens,</i> <span class="citation" data-id="9627771"><a href="/opinion/1428394/people-v-kitchens/#263" aria-description="Citation for case: People v. Kitchens">46 Cal. 2d 260, 263-264</a></span>, <span class="citation" data-id="9627771"><a href="/opinion/1428394/people-v-kitchens/#19" aria-description="Citation for case: People v. Kitchens">294 P. 2d 17, 19-20</a></span> (1956); <i>People</i> v. <i>Miller,</i> <span class="citation" data-id="2204229"><a href="/opinion/2204229/people-v-miller/" aria-description="Citation for case: People v. Miller">193 Cal. App. 2d 838</a></span>, <span class="citation" data-id="2204229"><a href="/opinion/2204229/people-v-miller/" aria-description="Citation for case: People v. Miller">14 Cal. Rptr. 704</a></span> (1961), and <i>People</i> v. <i>Campos,</i> <span class="citation" data-id="2192813"><a href="/opinion/2192813/people-v-campos/" aria-description="Citation for case: People v. Campos">184 Cal. App. 2d 489</a></span>, <span class="citation" data-id="2192813"><a href="/opinion/2192813/people-v-campos/" aria-description="Citation for case: People v. Campos">7 Cal. Rptr. 513</a></span> (1960). See also <i>People</i> v. <i>Lopez,</i> <span class="citation" data-id="9736481"><a href="/opinion/2205719/people-v-lopez/" aria-description="Citation for case: People v. Lopez">269 Cal. App. 2d 461</a></span>, 468 n. 2, <span class="citation" data-id="9736481"><a href="/opinion/2205719/people-v-lopez/" aria-description="Citation for case: People v. Lopez">74 Cal. Rptr. 740</a></span>, 744 n. 2 (1969) (dictum).</p>
<p>[6]  At the preliminary hearing and trial, the only disparities in description established were that Miller was two inches taller and 10 pounds heavier than Hill.</p>
<p>[7]  In denying the motion to suppress, the trial judge took judicial notice of the fact "that those who are apprehended and are arrested many times attempt to avoid arrest by giving false identification."</p>
<p>[8]  Petitioner points out that the officers had no idea how Miller gained access to the Hill apartment, and asserts that it was improper for them to assume that he was lawfully there. It is undisputed that Miller was the only occupant of the apartment. One of the officers testified that there was a lock on the door and that he had asked Miller how he had gotten into the apartment; Miller made no specific reply, except to reiterate that he had come in and was waiting for Hill, the tenant.</p>
<p>[9]  Petitioner also claims that it was unreasonable for the officers to disregard Miller's proffered identification. However, Miller's answer to the question about firearms could reasonably be regarded as evasive, and his subsequent production of identification as therefore entitled to little weight. Petitioner stresses that Miller was subsequently booked in his own name when taken to the station house, arguing that this demonstrates that the officers' belief that Miller was Hill was unreasonable. However, the trial judge found that the arresting officer was not responsible for the booking procedures under which Miller would be booked under whatever name he gave at the station house. This conclusion is buttressed by the fact that Miller was not released from custody for a day and a half, after a thorough check of his identification revealed that he had in fact told the truth about his identity, despite his evasiveness in dealing with the officers at the apartment.</p>
<p>[10]  Tr. of Oral Rearg. 34-35.</p>

</div>
```

---

## GROUP: content/cases/Hoffa v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Hoffa v. United States"
type: case
citation: "385 U.S. 293 (1966)"
parallel_cite: "87 S. Ct. 408; 17 L. Ed. 2d 374"
neutral_cite: 1966 U.S. LEXIS 2778
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-12-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-12-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hoffa v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107318/hoffa-v-united-states/"
  cluster_id: 107318
  opinion_id: 9423305
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Massiah v. United States]]", "[[Kuhlmann v. Wilson]]", "[[Illinois v. Perkins]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "informants", "attachment"]
holding: "A defendant has no Sixth Amendment claim when a government informant elicits statements **before** the right has attached; planting an informant raises no 6A problem pre-attachment."
lake:
  record_id: Hoffa v. United States
  status: verified
  projected_at: 2026-07-09
---

# Hoffa v. United States

*385 U.S. 293 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During Hoffa's "Test Fleet" trial, a local union official, Edward Partin, was with Hoffa's entourage and reported to the government that Hoffa made statements about attempting to bribe jurors. Hoffa was later convicted of jury tampering largely on Partin's testimony. Hoffa argued, among other things, that the government violated his Sixth Amendment right to counsel by failing to arrest him as soon as it had probable cause, which (he said) would have caused the right to attach before the statements were made.

## Issue
Whether the government violates the Sixth Amendment right to counsel when an informant obtains incriminating statements before adversary proceedings have begun, where the government did not arrest or charge the suspect earlier even though it may have had grounds to do so.

## Rule
No. The Court rejected the contention that the government must arrest a suspect as soon as it has probable cause so that the right to counsel will attach: "There is no constitutional right to be arrested." — 385 U.S. at 310. ^pin-310

"The police are not required to guess at their peril the precise moment at which they have probable cause to arrest a suspect, risking a violation of the Fourth Amendment if they act too soon, and a violation of the Sixth Amendment if they wait too long." — [*Id.*](https://www.courtlistener.com/opinion/107318/hoffa-v-united-states/#:~:text=The%20police%20are%20not%20required) ^pin-310a

## Application
On these facts no adversary proceedings on the jury-tampering charge had begun when Hoffa spoke in Partin's presence, and the government had no duty to arrest or charge him earlier to trigger the right to counsel. Because the Sixth Amendment right had not attached as to that offense when the statements were made, the use of Partin to gather and report them was no violation of Hoffa's right to counsel.

## Conclusion
The convictions were affirmed. There is no Sixth Amendment violation where an informant elicits statements before the right to counsel has attached.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hoffa* fixes the pre-attachment boundary that frames the deliberate-elicitation rule of [[Massiah v. United States]]; the Sixth Amendment is offense-specific and attaches only at the initiation of adversary judicial proceedings.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Hoffa v. United States*, 385 U.S. 293 (1966) — https://www.courtlistener.com/opinion/107318/hoffa-v-united-states/ — pinpoint: 310.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4ddb1c9efcef78f4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "385 U.S. 293 (1966)", "court": "U.S. Supreme Court", "neutral_cite": "1966 U.S. LEXIS 2778", "official_citation_present": true, "parallel_cite": "87 S. Ct. 408; 17 L. Ed. 2d 374", "title": "Hoffa v. United States", "year": "1966"}}
{"assertion_id": "3bf7168ebd27e009", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "Hoffa v. United States"}}
{"assertion_id": "d83f03a1123141c4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A defendant has no Sixth Amendment claim when a government informant elicits statements **before** the right has attached; planting an informant raises no 6A problem pre-attachment.", "title": "Hoffa v. United States"}}
{"assertion_id": "6324651e8325341a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hoffa v. United States"}}
{"assertion_id": "b8caa207b29f57a8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1966-12-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hoffa v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Hoffa v. United States", "varies_by_point": "false"}}
```

### lake record — Hoffa v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hoffa v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hoffa v. United States",
    "case_name_short": "Hoffa",
    "case_name_full": "Hoffa v. United States",
    "input_case_name": "Hoffa v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-12-12",
    "year": 1966,
    "docket": null,
    "cluster_id": 107318,
    "lead_opinion_id": 9423305,
    "sibling_ids": [
      107318,
      9423305,
      9423306
    ],
    "absolute_url": "/opinion/107318/hoffa-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8963329,
        "score": 20,
        "case_name": "Hoffa v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "385 U.S. 293",
      "volume": "385",
      "reporter": "U.S.",
      "page": "293",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 408",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 374",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 2778",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2778",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "385 U.S. 293",
        "volume": "385",
        "reporter": "U.S.",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 408",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 374",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 2778",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2778",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "385 U.S. 293",
    "official_selection": {
      "court_class": "scotus",
      "selected": "385 U.S. 293",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-310",
      "page": null,
      "quote": "trial, a local union official, Edward Partin, was with Hoffa's entourage and reported to the government that Hoffa made statements about attempting to bribe jurors. Hoffa was later convicted of jury tampering largely on Partin's testimony. Hoffa argued, among other things, that the government violated his Sixth Amendment right to counsel by failing to arrest him as soon as it had probable cause, which (he said) would have caused the right to attach before the statements were made. ## Issue Whether the government violates the Sixth Amendment right to counsel when an informant obtains incriminating statements before adversary proceedings have begun, where the government did not arrest or charge the suspect earlier even though it may have had grounds to do so. ## Rule No. The Court rejected the contention that the government must arrest a suspect as soon as it has probable cause so that the right to counsel will attach:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-310a",
      "page": null,
      "quote": "The police are not required to guess at their peril the precise moment at which they have probable cause to arrest a suspect, risking a violation of the Fourth Amendment if they act too soon, and a violation of the Sixth Amendment if they wait too long.",
      "star_marker": "310",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 32674,
      "fragment": "#:~:text=The%20police%20are%20not%20required",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-12-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hoffa v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Sosa",
          "cluster_id": 9447945,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen",
          "cluster_id": 4409967,
          "cite": [
            "864 F.3d 63",
            "2017 U.S. App. LEXIS 12942",
            "2017 WL 3040201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
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
        "journal_ref": "Hoffa v. United States:lane1_negative"
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
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bernard West v. United States",
          "cluster_id": 2735560,
          "cite": [
            "100 A.3d 1076",
            "2014 D.C. App. LEXIS 382",
            "2014 WL 4636023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fausto Camacho (072525)",
          "cluster_id": 2708330,
          "cite": [
            "218 N.J. 533",
            "95 A.3d 635",
            "2014 WL 3819161",
            "2014 N.J. LEXIS 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Preston v. State",
          "cluster_id": 2686475,
          "cite": [
            "218 Md. App. 60",
            "96 A.3d 800",
            "2014 WL 3736529",
            "2014 Md. App. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Agbodjan",
          "cluster_id": 8716573,
          "cite": [
            "871 F. Supp. 2d 95",
            "2012 WL 2552140"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 2487584,
          "cite": [
            "79 So. 3d 1013",
            "2012 La. LEXIS 268",
            "2012 WL 415483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Caldwell v. Cablevision Systems Corp.",
          "cluster_id": 5969116,
          "cite": [
            "86 A.D.3d 46",
            "925 N.Y.2d 103"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Miranda",
          "cluster_id": 6580219,
          "cite": [
            "458 Mass. 100",
            "934 N.E.2d 222",
            "2010 Mass. LEXIS 685"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alexander",
          "cluster_id": 167490,
          "cite": [
            "447 F.3d 1290",
            "2006 U.S. App. LEXIS 11993",
            "2006 WL 1314663"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cabral",
          "cluster_id": 6579075,
          "cite": [
            "443 Mass. 171",
            "819 N.E.2d 951",
            "2005 Mass. LEXIS 1"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nixon",
          "cluster_id": 109101,
          "cite": [
            "41 L. Ed. 2d 1039",
            "94 S. Ct. 3090",
            "418 U.S. 683",
            "1974 U.S. LEXIS 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marion",
          "cluster_id": 108420,
          "cite": [
            "30 L. Ed. 2d 468",
            "92 S. Ct. 455",
            "404 U.S. 307",
            "1971 U.S. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alderman v. United States",
          "cluster_id": 107872,
          "cite": [
            "22 L. Ed. 2d 176",
            "89 S. Ct. 961",
            "394 U.S. 165",
            "1969 U.S. LEXIS 3287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lovasco",
          "cluster_id": 109682,
          "cite": [
            "52 L. Ed. 2d 752",
            "97 S. Ct. 2044",
            "431 U.S. 783",
            "1977 U.S. LEXIS 107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weatherford v. Bursey",
          "cluster_id": 109590,
          "cite": [
            "51 L. Ed. 2d 30",
            "97 S. Ct. 837",
            "429 U.S. 545",
            "1977 U.S. LEXIS 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berger v. New York",
          "cluster_id": 107483,
          "cite": [
            "18 L. Ed. 2d 1040",
            "87 S. Ct. 1873",
            "388 U.S. 41",
            "1967 U.S. LEXIS 2964"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miller",
          "cluster_id": 109433,
          "cite": [
            "48 L. Ed. 2d 71",
            "96 S. Ct. 1619",
            "425 U.S. 435",
            "1976 U.S. LEXIS 148",
            "37 A.F.T.R.2d (RIA) 1261"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107318 OR 9423305 OR 9423306) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDUwMzY0ODAwMDAwJnM9MjQ4MDM5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107318+OR+9423305+OR+9423306%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107318 OR 9423305 OR 9423306)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMTUmcz0yMDE0MDM0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107318+OR+9423305+OR+9423306%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107318 OR 9423305 OR 9423306)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 1,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107318 OR 9423305 OR 9423306)",
    "indexed_citing_opinions": 1482,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107318,
        "count": 1364,
        "count_source": "search"
      },
      {
        "opinion_id": 9423305,
        "count": 145,
        "count_source": "search"
      },
      {
        "opinion_id": 9423306,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2107,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hoffa-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NzkwMTMmcz02NDc0NzI5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107318+OR+9423305+OR+9423306%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107318,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 102407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 105421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 225410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 232188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 235478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 268758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 272323,
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
    "date_created": "2026-07-05T07:14:48Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:15:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:15:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:19:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:15:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hoffa v. United States

```
<opinion type="majority">
<author id="b398-11">Mr. Justice Stewart</author>
<p id="AM2">delivered the opinion of the Court.</p>
<p id="b398-12">Over a period of several weeks in the late autumn of 1962 there took place in a federal court in Nashville, Tennessee, a trial by jury in which James Hoffa was charged with violating a provision of the Taft-Hartley Act. That trial, known in the present record as the Test Fleet trial, ended with a hung jury. The petitioners now before <em>us </em>— James <em>Hoffa, </em>Thomas Parks, Larry Campbell, and Ewing King — were tried and convicted <page-number citation-index="1" label="295">*295</page-number>in 1964 for endeavoring to bribe members of that jury.<footnotemark>1</footnotemark> The convictions were affirmed by the Court of Appeals.<footnotemark>2</footnotemark> A substantial element in the Government’s proof that led to the convictions of these four petitioners was contributed by a witness named Edward Partin, who testified to several incriminating statements which he said petitioners Hoffa and King had made in his presence during the course of the Test Fleet trial. Our grant of certiorari was limited to the single issue of whether the Government’s use in this case of evidence supplied by Partin operated to invalidate these convictions. <span class="citation multiple-matches"><a href="/c/U.%20S./382/1024/">382 U. S. 1024</a></span>.</p>
<p id="b399-5">The specific question before us, as framed by counsel for the petitioners, is this:</p>
<blockquote id="b399-6">“Whether evidence obtained by the Government by means of deceptively placing a secret informer in the quarters and councils of a defendant during one criminal trial so violates the defendant’s Fourth, Fifth and Sixth Amendment rights that suppression of such evidence is required in a subsequent trial of the same defendant on a different charge.”</blockquote>
<p id="b399-7">At the threshold the Government takes issue with the way this question is worded, refusing to concede that it “ ‘placed’ the informer anywhere, much less that it did so., ‘deceptively.’ ” In the view we take of the matter, however, a resolution of this verbal controversy is unnecessary to a decision of the constitutional issues before üs. The-basic facts are clear enough, and a lengthy discussion of the detailed minutiae to which a large portion of the' briefs and oral arguments was addressed would serve only to divert attention from the real issues before us.</p>
<p id="b400-3"><page-number citation-index="1" label="296">*296</page-number>The controlling facts can be briefly stated. The Test Fleet trial, in which James Hoffa was the sole individual defendant, was in progress between October 22 and December 23, 1962, in Nashville, Tennessee. James Hoffa was president of the International Brotherhood of Teamsters. During the course of the trial he occupied a three-room suite in the Andrew Jackson Hotel in Nashville. One of his constant companions throughout the trial was the petitioner King, president of the Nashville local of the Teamsters Union. Edward Partin, a resident of Baton Rouge, Louisiana, and a local Teamsters Union official there, made repeated visits to Nashville during the period of the trial. On these visits he frequented the Hoffa hotel suite, and was continually in the company of Hoffa and his associates, including King, in and around the hotel suite, the hotel lobby, the courthouse, and elsewhere in Nashville. During this period Partin made frequent reports to a federal agent named Sheridan concerning conversations he said Hoffa and King had had with him and with each other, disclosing endeavors to bribe members of the Test Fleet jury. Partin’s reports and his subsequent testimony at the petitioners’ trial unquestionably contributed, directly or indirectly, to the convictions of all four of the petitioners.<footnotemark>3</footnotemark></p>
<p id="b401-4"><page-number citation-index="1" label="297">*297</page-number>The chain of circumstances which led Partin to be in Nashville during the Test Fleet trial extended back at least to September of 1962. At that time Partin was in jail in Baton Rouge on a state criminal charge. He was <page-number citation-index="1" label="298">*298</page-number>also under a federal indictment for embezzling union funds, and other indictments for state offenses were pending against him. Between that time and Partin’s initial visit to Nashville on October 22 he was released on bail on the state criminal charge, and proceedings under the federal indictment were postponed. On October 8, Partin telephoned Hoffa in Washington, D. C., to discuss local union matters and Partin’s difficulties with the authorities. In the course of this conversation Partin asked if he could see Hoffa to confer about these problems, and Hoffa acquiesced. Partin again called Hoffa on October 18 and arranged to meet him in Nashville. During this period Partin also consulted on several occasions with federal law enforcement agents, who told him that Hoffa might attempt to tamper with the Test Fleet jury, and asked him to be on the lookout in Nashville for such attempts and to report to the federal authorities any evidence of wrongdoing that he discovered. Partin agreed to do so.</p>
<p id="b402-5">After the Test Fleet trial was completed, Partin’s wife received four monthly installment payments of $300 from government funds, and the state and federal charges against Partin were either dropped or not actively pursued.</p>
<p id="b402-6">Reviewing these circumstances in detail, the Govern-"inent insists the fair inference is that Partin went to Nashville on his own initiative to discuss union busi- „ ness and his own problems with Hoffa, that Partin ultimately cooperated closely with federal authorities only after he discovered evidence of jury tampering in the [ Test Fleet trial, that the payments to Partin’s wife were -simply in partial reimbursement of Partin’s subsequent out-of-pocket expenses, and that the failure to prosecute Partin on the state and federal charges had no necessary connection with his services as an informer. The findings of the trial court support this version of the <page-number citation-index="1" label="299">*299</page-number>facts,<footnotemark>4</footnotemark> and these findings were accepted by the Court of Appeals as “supported by substantial evidence.” 349 F. 2d, at 36. But whether or not the Government “placed” Partin with Hoffa in Nashville during the Test Fleet trial, we proceed upon the premise that Partin was a government informer from the time he first arrived in Nashville on October 22, and that the Government compensated him for his services as such. It is upon that premise that we consider the constitutional issues presented.</p>
<p id="b403-5">Before turning to those issues we mention an additional preliminary contention of the Government. The <page-number citation-index="1" label="300">*300</page-number>petitioner Hoffa was the only individual defendant in the Test Fleet case, and Partin had conversations during the Test Fleet trial only with him and with the petitioner King. So far as appears, Partin never saw either of the other two petitioners during that period. Consequently, the Government argues that, of the four petitioners, only Hoffa has standing to raise a claim that his Sixth Amendment right to counsel in the Test Fleet trial was impaired, and only he and King have standing with respect to the other constitutional claims. Cf. <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 487-488, 491-492</a></span>; <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#259" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 259-267</a></span>. It is clear, on the other hand, that Partin’s reports to the agent Sheridan uncovered leads that made possible the development of evidence against petitioners Parks and Campbell. But we need not pursue the nuances of these “standing” questions, because it is evident in any event that none of the petitioners can prevail unless the petitioner Hoffa prevails. For that reason, the ensuing discussion is confined to the claims of the petitioner Hoffa (hereinafter petitioner), all of which he clearly has standing to invoke.</p>
<p id="b404-4">I.</p>
<p id="b404-5">It is contended that only by violating the petitioner’s rights under the Fourth Amendment was Partin able to hear the petitioner’s incriminating statements in the hotel suite, and that Partin’s testimony was therefore inadmissible under the exclusionary rule of <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. The argument is that Partin’s failure to disclose his role as a government informer vitiated the consent that the petitioner gave to Partin’s repeated entries into the suite, and that by listening to the petitioner’s statements Partin conducted an illegal “search” for verbal evidence.</p>
<p id="b405-4"><page-number citation-index="1" label="301">*301</page-number>The preliminary steps of this argument are on solid ground. A hotel room can clearly be the object of Fourth Amendment protection as much as a home or an office. <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>. The Fourth Amendment can certainly be violated by guileful as well as by forcible intrusions into a constitutionally protected area. <em>Gouled </em>v. <em>United States, 255 </em>U. S. 298. And the protections of the Fourth Amendment are surely not limited to tangibles, but can extend as well to oral statements. <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>.</p>
<p id="b405-5">Where the argument falls is in its misapprehension of the fundamental nature and scope of Fourth Amendment protection. What the Fourth Amendment protects is the security a man relies upon when he places himself or his property within a constitutionally protected area, be it his home or his office, his hotel room or his automobile.<footnotemark>5</footnotemark> There he is protected from unwarranted governmental intrusion. And when he puts something in his filing cabinet, in his desk drawer, or in his pocket, he has the right to know it will be secure from an unreasonable search or an unreasonable seizure. So it was that the Fourth Amendment could not tolerate the warrantless search of the hotel room in <em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span>, </em>the purloining of the petitioner’s private papers in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span>, </em>or the surreptitious electronic surveillance in <em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">Silverman</a></span>. </em>Countless other cases which have come to this Court ovér the years have involved a myriad of differing factual contexts in which the protections of the Fourth Amendment have been appropriately invoked. No doubt the future will bring countless others. By nothing we say here do we either foresee or foreclose factual <page-number citation-index="1" label="302">*302</page-number>situations to which the Fourth Amendment may be applicable.</p>
<p id="b406-4">In the present case, however, it is evident that no interest legitimately protected by the Fourth Amendment is involved. It is obvious that the petitioner was not relying on the security of his hotel suite when he made the incriminating statements to Partin or in Partin's presence. Partin did not enter the suite by force or by stealth. He was not a surreptitious eavesdropper. Partin was in the suite by invitation, and every conversation which he heard was either directed to him or knowingly carried on in his presence. The petitioner, in a word, was not relying on the security of the hotel room; he was relying upon his misplaced confidence that Partin would not reveal his wrongdoing.<footnotemark>6</footnotemark> As counsel for the petitioner himself points out, some of the communications with Partin did not take place in the suite at all, but in the “hall of the hotel,” in the “Andrew Jackson Hotel lobby,” and “at the courthouse.”</p>
<p id="b406-5">Neither this Court nor any member of it has ever expressed the view that the Fourth Amendment protects a wrongdoer’s misplaced belief that a person to whom he voluntarily confides his wrongdoing will not reveal it. Indeed, the Court unanimously rejected that very contention less than four years ago in <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>. In that case the petitioner had" been convicted of attempted bribery of an internal revenue agent named Davis. The Court was divided with regard to the admissibility in evidence of a surreptitious electronic recording of an incriminating conversation Lopez had had in his private office with Davis. But there was no dissent from the view that testimony <page-number citation-index="1" label="303">*303</page-number>about the conversation by Davis himself was clearly admissible.</p>
<p id="b407-5">As the Court put it, “Davis was not guilty of an unlawful invasion of petitioner’s office simply because his apparent willingness to accept a bribe was not real. Compare <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span>. He was in the office with petitioner’s consent, and while there he did not violate the privacy of the office by seizing something surreptitiously without petitioner’s knowledge. Compare <em>Gouled </em>v. <em>United States, supra. </em>The only evidence obtained consisted of statements made by Lopez to Davis, statements which Lopez knew full well could be used against him by Davis if he wished. ...” <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#438" aria-description="Citation for case: Lopez v. United States">373 U. S., at 438</a></span>. In the words of the dissenting opinion in <em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">Lopez</a></span>, </em>“The risk of being overheard by an eavesdropper or betrayed by an informer or deceived as to the identity of one with whom one deals is probably inherent in the conditions of human society. It is the kind of risk we necessarily assume whenever we speak.” <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#465" aria-description="Citation for case: Lopez v. United States"><em>Id., </em>at 465</a></span>. See also <em>Lewis </em>v. <em>United States, ante, </em>p. 206.</p>
<p id="b407-6">Adhering to these views, we hold that no right protected by the Fourth Amendment was violated in the present case.</p>
<p id="b407-7">II.</p>
<p id="b407-8">The petitioner argues that his right under the Fifth Amendment not to “be compelled in any criminal case to be a witness against himself” was violated by the admission of Partin’s testimony. The claim is without merit.</p>
<p id="b407-9">There have been sharply differing views within the Court as to the ultimate reach of the Fifth Amendment right against compulsory self-incrimination. Some of those differences were aired last Term in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#499" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 499, 504, 526</a></span>. But since at least as long ago as 1807, when Chief Justice Marshall first <page-number citation-index="1" label="304">*304</page-number>gave attention to the matter in the trial of Aaron Burr,<footnotemark>7</footnotemark> all have agreed that a necessary element of compulsory self-incrimination is some kind of compulsion. Thus, in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case, dealing with the Fifth Amendment’s impact upon police interrogation of persons in custody, the Court predicated its decision upon the conclusion “that without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. . . .” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>.</p>
<p id="b408-6">In the present case no claim has been or could be made that the petitioner’s incriminating statements were the product of any sort of coercion, legal or factual. The petitioner’s conversations with Partin and in Partin’s presence were wholly voluntary. For that reason, if for no other, it is clear that no right protected by the Fifth Amendment privilege against compulsory self-incrimination was violated in this case.</p>
<p id="b408-7">III.</p>
<p id="b408-8">The petitioner makes two separate claims under the Sixth Amendment, and we give them separate consideration.</p>
<p id="b408-9">A.</p>
<p id="b408-10">During the course of the Test Fleet trial the petitioner’s lawyers used his suite as a place to confer with him and with each other, to interview witnesses, and to plan the following day’s trial strategy. Therefore, <page-number citation-index="1" label="305">*305</page-number>argues the petitioner, Partin’s presence in and around the suite violated the petitioner’s Sixth Amendment i right to counsel, because an essential ingredient thereof is the right of a defendant and his counsel to prepare for trial without intrusion upon their confidential relationship by an agent of the Government, the defendant’s i trial adversary. Since Partin’s presence in the suite thus I violated the Sixth Amendment, the argument continues, any evidence acquired by reason of his presence there I was constitutionally tainted and therefore inadmissible <em>I </em>against the petitioner in this case. We reject this <em>I </em>argument.</p>
<p id="b409-6">In the first place, it is far from clear to what extent Partin was present at conversations or conferences of the petitioner’s counsel. Several of the petitioner’s Test Fleet lawyers testified at the hearing on the motion to suppress Partin’s testimony in the present case. Most of them said that Partin had heard or had been in a position to hear at least some of the lawyers’ discussions during the Test Fleet trial. On the other hand, Partin himself testified that the lawyers “would move you out” when they wanted to discuss the case, and denied that he made any effort to “get into or be present at any conversations between lawyers or anything of that sort,” other than engaging in such banalities as “how things looked,” or “how does it look?” He said he might have heard some of the lawyers’ conversations, but he didn’t know what they were talking about, “because I wasn’t interested in what they had to say about the case.” He testified that he did not report any of the lawyers’ conversations to Sheridan, because the latter “wasn’t interested in what the attorneys said.” Partin’s testimony was largely confirmed by Sheridan. Sheridan did testify, however, to one occasion when Partin told him about a group of prospective character witnesses being interviewed in the suite by one of the petitioner’s lawyers, who “was going <page-number citation-index="1" label="306">*306</page-number>over” some written “questions and answers” with them. This information was evidently relayed by Sheridan to the chief government attorney at the Test Fleet trial.<footnotemark>8</footnotemark></p>
<p id="b410-6">The District Court in the present case apparently credited Partin’s testimony, finding “there has been no interference by the government with any attorney-client relationship of any defendant in this case.” The Court of Appeals accepted this finding. 349 F. 2d, at 36. In view of Sheridan’s testimony about Partin’s report of the interviews with the prospective character witnesses, however, we proceed here on the hypothesis that Partin did observe and report to Sheridan at least some of the L.activities of defense counsel in the Test Fleet trial.</p>
<p id="b410-7">The proposition that a surreptitious invasion by a government agent into the legal camp of the defense may violate the protection of the Sixth Amendment has found expression in two cases decided by the Court of Appeals for the District of Columbia Circuit, <em>Caldwell </em>v. <em>Unite</em>d <em>States, </em>92 U. S. App. D. C. 355, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">205 F. 2d 879</a></span>, and <em>Coplon </em>v. <em>United States, </em>89 U. S. App. D. C. 103, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d 749</a></span>. Both of those cases dealt with government intrusion of the grossest kind upon the confidential relationship between the defendant and his counsel. In <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span>, </em>the <page-number citation-index="1" label="307">*307</page-number>defendant alleged that government agents deliberately-intercepted telephone consultations between the defendant and her lawyer before and during trial. In <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span>, </em>the agent, “[i]n his dual capacity as defense assistant and Government agent. . . gained free access to the planning of the defense. . . . Neither his dealings with the defense nor his reports to the prosecution were limited to the proposed unlawful acts of the defense: they covered many matters connected with the impending trial.” 92 U. S. App. D. C., at 356, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#880" aria-description="Citation for case: Caldwell v. United States">205 F. 2d, at 880</a></span>.</p>
<p id="b411-5">’ We may assume that the <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>and <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>cases : were rightly decided, and further assume, without deciding, that the Government’s activities during the Test ¡Fleet trial were sufficiently similar to what went on in j <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>and <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>to invoke the rule of those decisions, f Consequently, if the Test Fleet trial had resulted in a j conviction instead of a hung jury, the conviction would j presumptively have been set aside as constitutionally ; defective. Cf. <em>Black </em>v. <em>United States, ante, </em>p. 26.</p>
<p id="b411-6">! But a holding that it follows from this presumption Cthat the petitioner’s conviction in the present case should be set aside would be both unprecedented and irrational. In <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>and in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span>, </em>the Court of Appeals held [that the Government’s intrusion upon the defendant’s ¡relationship with his lawyer “invalidates the trial at [which it occurred.” 89 U. S. App. D. C., at 114, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/#759" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d, at 759</a></span>; 92 U. S. App. D. C., at 357, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#881" aria-description="Citation for case: Caldwell v. United States">205 F. 2d, at 881</a></span>. In both of those cases the court directed a new trial,<footnotemark>9</footnotemark> and the second trial in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>resulted in a conviction which this Court declined to review. 95 U. S. App. D. C. 35, <span class="citation" data-id="9444417"><a href="/opinion/235478/bennie-c-caldwell-v-united-states/" aria-description="Citation for case: Bennie C. Caldwell v. United States">218 F. 2d 370</a></span>, <span class="citation multiple-matches"><a href="/c/U.%20S./349/930/">349 U. S. 930</a></span>. The argument here, therefore, goes far beyond anything decided in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>or in <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span>. </em>For if the petitioner’s argument were accepted, <page-number citation-index="1" label="308">*308</page-number>not only could there have been no new conviction on the existing charges in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span>, </em>but not even a conviction on other and different charges against the same defendant.</p>
<p id="b412-6">It is possible to imagine a case in which the prosecution might so pervasively insinuate itself into the councils of the defense as to make a new trial on the same charges impermissible under the Sixth Amendment.<footnotemark>10</footnotemark> But even if it were further arguable that a situation could be hypothesized in which the Government’s previous activities in undermining a defendant’s Sixth Amendment rights at one trial would make evidence obtained thereby inadmissible in a different trial on other charges, the case now before us does not remotely approach such a situation.</p>
<p id="b412-7">This is so because of the clinching basic fact in the present case that none of the petitioner’s incriminating • statements which Partin heard were made in the presence of counsel, in the hearing of counsel, or in connection in any way with the legitimate defense of the Test Fleet prosecution. The petitioner’s statements related to the commission of a quite separate offense— attempted bribery of jurors — and the statements were made to Partin out of the presence of any lawyers.</p>
<p id="b412-8">Even assuming, therefore, as we have, that there might have been a Sixth Amendment violation which might have made invalid a conviction, if there had been one, in the Test Fleet case, the evidence supplied by Partin in the present case was in no sense the “fruit” of any such violation. In <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span>, a case involving exclusion of evidence under <page-number citation-index="1" label="309">*309</page-number>the Fourth Amendment, the Court stated that “the more apt question in such a case is ‘whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.’ Maguire, Evidence of Guilt, 221 (1959).” <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 488</a></span>.</p>
<p id="b413-5">Even upon the premise that this same strict standard of excludability should apply under the Sixth Amendment — a question we need not decide — it is clear that Partin’s evidence in this case was not the consequence of any “exploitation” of a Sixth Amendment violation. The petitioner’s incriminating statements to which Partin testified in this case were totally unrelated in both time and subject matter to any assumed intrusion by Partin into the conferences of the petitioner’s counsel in the Test Fleet trial. These incriminating statements, all of them made out of the presence or hearing of any of the petitioner’s counsel, embodied the very antithesis of any legitimate defense in the Test Fleet trial.</p>
<p id="b413-6">B.</p>
<p id="b413-7">The petitioner’s second argument under the Sixth Amendment needs no extended discussion. That argument goes as follows: Not later than October 25, 1962, the Government had sufficient ground for taking the petitioner into custody and charging him with endeavors to tamper with the Test Fleet jury. Had the Government done so, it could not have continued to question the petitioner without observance of his Sixth Amendment right to counsel. <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>; <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>. Therefore, the argument concludes, evidence of statements <page-number citation-index="1" label="310">*310</page-number>made by the petitioner subsequent to October 25 was inadmissible, because the Government acquired that evidence only by flouting the petitioner’s Sixth Amendment right to counsel.</p>
<p id="b414-6">Nothing in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>, </em>in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>or in any other case that has come to our attention, even remotely suggests this novel and paradoxical constitutional doctrine, and we decline to adopt it now. There is no constitutional right to be arrested.<footnotemark>11</footnotemark> The police are not required to guess at their peril the precise moment at which they have probable cause to arrest a suspect, risking a violation of the Fourth Amendment if they act too soon, and a violation of the Sixth Amendment if they wait too long. Law enforcement officers are under no constitutional duty to call a halt to a criminal investigation the moment they have the minimum evidence to establish probable cause, a quantum of evidence which may fall far short of the amount necessary to support a criminal conviction.</p>
<p id="b414-7">IV.</p>
<p id="b414-8">Finally, the petitioner claims that even if there was no violation — “as separately measured by each such Amendment” — of the Fourth Amendment, the compulsory self-incrimination clause of the Fifth Amendment, or of the Sixth Amendment in this case, the judgment of conviction must nonetheless be reversed. The argument is based upon the Due Process Clause of the Fifth Amendment. The “totality” of the Government’s conduct during the Test Fleet trial operated, it is said, to “ ‘offend those canons of decency and fairness which express the notions of justice of English-speaking peoples <page-number citation-index="1" label="311">*311</page-number>even toward those charged with the most heinous offenses’ <em>(Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#169" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 169</a></span>).”</p>
<p id="b415-5">The argument boils down to a general attack upon the use of a government informer as “a shabby thing in any case,” and to the claim that in the circumstances of this particular case the risk that Partin’s testimony might be perjurious was very high. Insofar as the general attack upon the use of informers is based upon historic “notions” of “English-speaking peoples,” it is without historical foundation. In the words of Judge Learned Hand, “Courts have countenanced the use of informers from time immemorial; in cases of conspiracy, or in other cases when the crime consists of preparing for another crime, it is usually necessary to rely upon them or upon accomplices because the criminals will almost certainly proceed covertly. . . .” <em>United States </em>v. <em>Dennis, </em><span class="citation" data-id="9442514"><a href="/opinion/225410/united-states-v-dennis/#224" aria-description="Citation for case: United States v. Dennis">183 F. 2d 201, at 224</a></span>.</p>
<p id="b415-6">This is not to say that a secret government informer is to the slightest degree more free from all relevant constitutional restrictions than is any other government agent. See <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>. It <em>is </em>to say that the use of secret informers is not <em>per se </em>unconstitutional.</p>
<p id="b415-7">The petitioner is quite correct in the contention that Partin, perhaps even more than most informers, may have had motives to lie. But it does not follow that his testimony was untrue, nor does it follow that his testimony was constitutionally inadmissible. The established safeguards of the Anglo-American legal system leave the veracity of a witness to be tested by cross-examination, and the credibility of his testimony to be determined by a properly instructed jury. At the trial of this case, Partin was subjected to rigorous cross-examination, and the extent and nature of his dealings with federal and state authorities were insistently ex<page-number citation-index="1" label="312">*312</page-number>plored.<footnotemark>12</footnotemark> The trial judge instructed the jury, both specifically<footnotemark>13</footnotemark> and generally,<footnotemark>14</footnotemark> with regard to assessing Partin’s credibility. The Constitution does not require us to upset the jury’s verdict.</p>
<p id="b416-4">
<em>Affirmed.</em>
</p>
<judges id="b416-5">Mr. Justice White and Mr. Justice Fortas took no part in the consideration or decision of these cases.</judges>
<p id="b416-6">[For opinion of Mr. Justice Douglas, see <em>post, </em>p. 340.]</p>
<footnote label="1">
<p id="b399-8"> Petitioners Hoffa, Parks, and Campbell were convicted under <span class="citation no-link">18 U. S. C. § 1503</span> for endeavoring corruptly to influence Test Fleet juror Gratín Fields. Petitioners Hoffa and King Were convicted of a similar offense involving Test Fleet juror Mrs. James M. Paschal.</p>
</footnote>
<footnote label="2">
<p id="b399-9"> <span class="citation" data-id="268758"><a href="/opinion/268758/united-states-v-james-r-hoffa-united-states-of-america-v-thomas-ewing/" aria-description="Citation for case: United States v. James R. Hoffa, United States of America...">349 F. 2d 20</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b400-4"> Partin testified at the trial of this case that petitioners Hoffa and King had made the following statements during the course of the Test Fleet trial:</p>
<p id="b400-5">On October 22, the day Partin first arrived in Nashville, King told him that a meeting had been “set up on the jury that night.” That evening Hoffa told Partin that he wanted Partin to stay in Nashville in order to call on some people. Hoffa explained “that they was going to get to one juror or try to get to a few scattered jurors and take their chances.” The next day Partin was told by Hoffa that Hoffa might want him “to pass something for him.” As Hoffa said this, he hit his rear pocket with his hand. On October 25, the day after Test Fleet juror James Tippens had reported to the trial judge that he had been approached with a bribe offer, <page-number citation-index="1" label="297">*297</page-number>Partin asked Hoffa about his wanting Partin to “pass something.” Hoffa replied, “The dirty bastards went in and told the Judge that his neighbor had offered him $10,000,” and added, “We are going to have to lay low for a few days.” King told Partin on October 26 that he intended to influence a female juror, Mrs. Paschal, in Hoffa’s favor, and added that the juror and her husband, a highway patrolman, “loved money, and $10,000.00 [is] a lot of money.” Hoffa informed Partin on October 29 that he “would pay 15 or $20,000, whatever — whatever it cost to get to the jury.” On November 5, in Partin’s presence, Hoffa berated King for failing in his promises to "get the patrolman.” King then told Partin that he was arranging a meeting with the highway patrolman, but on November 7 King admitted to Partin that he had not yet contacted the highway patrolman and that Hoffa had been complaining “about not getting to the jury.” Hoffa criticized King in the presence of Partin on November 14 for “not making a contact like he told him he would,” adding that he “wanted some insurance.” Later the same day, King told Partin that he had arranged to meet with the highway patrolman, and that he had prepared a cover story to allay suspicion. On November 15 Hoffa asked King in Partin’s presence whether he had “made the contacts.” King related to Partin on November 20 a meeting that King had had with juror Paschal’s husband, stating that the highway patrolman wanted a promotion rather than money. The same day Hoffa told Partin that he was disturbed because “the Highway Patrolman wouldn’t take the money,”' adding that if he had “taken the money it would have pinned him down and he couldn’t have backed up.”</p>
<p id="b401-6">There was other evidence at the trial that petitioner Campbell, a union associate of Hoffa’s, and petitioner Parks, Campbell’s uncle, had made bribe offers to Gratín Fields, a Negro juror. On November 7, according to Partin, Hoffa told Partin that he had “the colored male juror in [his] hip pocket,” and that Campbell “took care of it.” Hoffa told Partin that Campbell, a Negro, was related to Fields, and that while Fields had refused the bribe he would not “go against his own people.” Hoffa concluded, “ [IJt looks like our best bet is a hung jury unless we can get to the foreman of the jury. If they have a hung jury, it will be the same as acquittal because they will never try the ease again.”</p>
</footnote>
<footnote label="4">
<p id="b403-6"> In denying the defense motion to suppress Partin’s testimony, the trial court stated: “I would further find that the government did not place this witness Mr. Partin in the defendants’ midst or have anything to do with placing him in their midst, rather that he was knowingly and voluntarily placed in their midst by one of the defendants.”</p>
<p id="b403-7">The trial court’s memorandum denying a motion for a new trial contained the following statement:</p>
<blockquote id="b403-8">“The action of the Court in denying the motions of the defendants to suppress the testimony of the witness Partin is complained of in Grounds 41 and 42 of the motions for new trial. It is contended that one of the findings of fact of the Court with respect to the motion to suppress was rendered incorrect by subsequent evidence in the case. It is contended that the telephone transcriptions of the telephone calls between Partin and Hoffa on October 8 and 18, 1962, established that the defendant Hoffa did not invite Partin to Nashville. The telephone transcriptions reflect that the defendant Hoffa agreed to an appointment to see Partin in Nashville. Even if the defendant Hoffa did not initiate the invitation of Partin to come to Nashville, but rather Partin solicited the invitation, this does not in any way alter the Court’s finding that the Government did not place or keep Partin with the defendant Hoffa. . . . The Government requested of Partin only that he report information of jury tampering or other illegal activity of which he became aware. Partin voluntarily furnished such information. He remained in Nashville or returned to Nashville either at the request or with the consent of the defendant Hoffa and not at the instruction of the Government.”</blockquote>
</footnote>
<footnote label="5">
<p id="b405-6"> We do not deal here with the law of arrest under the Fourth Amendment.</p>
</footnote>
<footnote label="6">
<p id="b406-6"> The applicability of the Fourth Amendment if Partin had been a stranger to the petitioner is a question we do not decide. Cf. <em>Lewis </em>v. <em>United States, ante, </em>p. 206.</p>
</footnote>
<footnote label="7">
<p id="b408-11"> “Many links frequently compose that chain of testimony which is necessary to convict any individual of a crime. It appears to the court to be the true sense of the rule that no witness is <em>com-pellable </em>to furnish any one of them against himself. . . .” <em>In re Willie, </em><span class="citation" data-id="8638363"><a href="/opinion/8658512/united-states-v-burr/#40" aria-description="Citation for case: United States v. Burr">25 Fed. Cas. 38, 40</a></span> (No. 14,692e) (C. C. D. Va. 1807). (Emphasis supplied.)</p>
</footnote>
<footnote label="8">
<p id="b410-8"> Petitioner maintains that the cross-examination of one of these character witnesses at the Test Fleet trial shows that the prosecution availed itself of the information transmitted by Partin. The following exchange between the prosecutor and witness occurred:</p>
<blockquote id="b410-9">Q. “Did [defense counsel] give you anything to read, Mr. Sammut?”</blockquote>
<blockquote id="b410-10">A. “No, sir, not even a newspaper.”</blockquote>
<blockquote id="b410-11">Q. “Not even a newspaper? I am not talking about newspapers, I am talking with respect to your testimony. Did they give you anything to read with respect to your testimony?”</blockquote>
<blockquote id="b410-12">A. “After I talked to them.”</blockquote>
<blockquote id="b410-13">Q. “They gave you written questions and answers, didn’t they?”</blockquote>
<blockquote id="b410-14">A. “The questions that they asked me and the questions that I answered.”</blockquote>
</footnote>
<footnote label="9">
<p id="b411-7"> In <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span>, </em>the grant of a new trial was conditioned on the defendant’s proof of her wiretapping allegations.</p>
</footnote>
<footnote label="10">
<p id="b412-9"> In the <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>case, the Court of Appeals implicitly recognized the possibility of a case arising in which a showing could be made of “prejudice to the defense of such a nature as would necessarily render a subsequent trial unfair to the accused.” 92 U. S. App. D. <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#355" aria-description="Citation for case: Caldwell v. United States">C. 355, 357, n. 11, 205 F. 2d 879, 881-882, n. 11</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b414-9"> We put to one side the extraordinary problems that would have arisen if the petitioner had been arrested and charged during the progress of the Test Fleet trial.</p>
</footnote>
<footnote label="12">
<p id="b416-7"> Partin underwent cross-examination for an entire week. The defense was afforded wide latitude to probe Partin's background, character, and ties to the authorities; it was permitted to explore matters that are normally excludable, for example, whether Partin had been charged with a crime in 1942, even though that charge had never been prosecuted.</p>
</footnote>
<footnote label="13">
<p id="b416-8"> The judge instructed the jury that it was petitioner’s contention that he “did not invite Edward Partin to come to Nashville, Tennessee, during the trial of [the Test Fleet case]' but that the said Edward Partin came of his own accord under the pretense of attempting to convince Mr. Hoffa that the Teamsters local union in Baton Rouge, Louisiana should not be placed in trusteeship by reason of Partin’s being under indictment and other misconduct on Partin’s part, but for the real purpose of fabricating evidence against Hoffa in order to serve his own purposes and interests.”</p>
</footnote>
<footnote label="14">
<p id="b416-9"> The jury was instructed: “You should carefully scrutinize the testimony given and the circumstances under which each witness has testified, and every matter in evidence which tends to indicate whether the witness is worthy of belief. Consider each witness’ intelligence, his motives, state of mind, his demeanor and manner while on the witness stand. Consider also any relation each witness may bear to either side of the case .... All evidence of a witness whose self-interest is shown from either benefits received, detriments suffered, threats or promises made, or any attitude of the witness which might tend to prompt testimony either favorable or unfavorable to the accused should be considered with caution and weighed with care.”</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Hope v. Pelzer.md  (`case`, 5 assertions)

### content_page

```
---
title: "Hope v. Pelzer"
type: case
citation: "536 U.S. 730 (2002)"
parallel_cite: "122 S. Ct. 2508; 153 L. Ed. 2d 666"
neutral_cite: 2002 U.S. LEXIS 4884
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hope v. Pelzer
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121169/hope-v-pelzer/"
  cluster_id: 121169
  opinion_id: 9434318
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Harlow v. Fitzgerald]]", "[[Saucier v. Katz]]", "[[City of Tahlequah v. Bond]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "clearly-established-law", "fair-warning"]
holding: "A right can be clearly established **without a factually identical case** — in an 'obvious case,' officials have fair warning even in novel circumstances (the QI 'obvious case' escape hatch)."
lake:
  record_id: Hope v. Pelzer
  status: verified
  projected_at: 2026-07-09
---

# Hope v. Pelzer

*536 U.S. 730 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Alabama prison guards twice handcuffed inmate Larry Hope to a "hitching post" for extended periods — once for about seven hours, shirtless in the sun, with little water and no bathroom breaks. Hope sued the guards under § 1983 for an Eighth Amendment violation; the guards claimed [[Qualified Immunity|qualified immunity]], and the Eleventh Circuit had granted it on the ground that no earlier case had "materially similar" facts.

## Issue
Whether [[Qualified Immunity|qualified immunity]] protects officials whenever no prior case has "materially similar" facts, or whether a right can be clearly established without such a factually identical precedent.

## Rule
A right may be clearly established without a factually identical case. "[O]fficials can still be on notice that their conduct violates established law even in novel factual circumstances." — 536 U.S. at 741. ^pin-741

The controlling inquiry is fair warning: "the salient question that the Court of Appeals ought to have asked is whether the state of the law in 1995 gave respondents fair warning that their alleged treatment of Hope was unconstitutional." — [*Id.*](https://www.courtlistener.com/opinion/121169/hope-v-pelzer/#:~:text=the%20salient%20question%20that%20the) ^pin-741a

## Application
The Court held the guards had fair warning that handcuffing Hope to the hitching post was unlawful: binding circuit precedent, an Alabama Department of Corrections regulation, and a Justice Department report had all condemned the practice, and the wantonness of the conduct was obvious. Although no prior decision involved the identical hitching-post facts, the state of the law gave the guards fair warning, so they were not entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
The guards were not entitled to [[Qualified Immunity|qualified immunity]]; the Eleventh Circuit's "materially similar" requirement was rejected and its judgment reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hope* refines the "clearly established law" prong of [[Harlow v. Fitzgerald]] and [[Saucier v. Katz]], supplying the "fair warning" / obvious-case route to overcoming [[Qualified Immunity|qualified immunity]] even without a factually identical precedent.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Hope v. Pelzer*, 536 U.S. 730 (2002) — https://www.courtlistener.com/opinion/121169/hope-v-pelzer/ — pinpoint: 741.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e73f28e8212e70e6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "536 U.S. 730 (2002)", "court": "U.S. Supreme Court", "neutral_cite": "2002 U.S. LEXIS 4884", "official_citation_present": true, "parallel_cite": "122 S. Ct. 2508; 153 L. Ed. 2d 666", "title": "Hope v. Pelzer", "year": "2002"}}
{"assertion_id": "42937a6aad2d31d0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A right can be clearly established **without a factually identical case** — in an 'obvious case,' officials have fair warning even in novel circumstances (the QI 'obvious case' escape hatch).", "title": "Hope v. Pelzer"}}
{"assertion_id": "ef3b47bbe68f50e4", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Hope v. Pelzer"}}
{"assertion_id": "5c16293e31bbce82", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hope v. Pelzer"}}
{"assertion_id": "bb48e5c63083e010", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2002-06-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hope v. Pelzer", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Hope v. Pelzer", "varies_by_point": "false"}}
```

### lake record — Hope v. Pelzer

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hope v. Pelzer",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hope v. Pelzer",
    "case_name_short": "Hope",
    "case_name_full": "HOPE v. PELZER Et Al.",
    "input_case_name": "Hope v. Pelzer",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-27",
    "year": 2002,
    "docket": null,
    "cluster_id": 121169,
    "lead_opinion_id": 9434318,
    "sibling_ids": [
      121169,
      9434318,
      9434319
    ],
    "absolute_url": "/opinion/121169/hope-v-pelzer/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 119432,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      },
      {
        "cluster_id": 119246,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      },
      {
        "cluster_id": 9271893,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      },
      {
        "cluster_id": 9268772,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "536 U.S. 730",
      "volume": "536",
      "reporter": "U.S.",
      "page": "730",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 2508",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2508",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 666",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "666",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4884",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 730",
        "volume": "536",
        "reporter": "U.S.",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2508",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2508",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 666",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "666",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4884",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "536 U.S. 730",
    "official_selection": {
      "court_class": "scotus",
      "selected": "536 U.S. 730",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-741",
      "page": null,
      "quote": "facts, or whether a right can be clearly established without such a factually identical precedent. ## Rule A right may be clearly established without a factually identical case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-741a",
      "page": null,
      "quote": "the salient question that the Court of Appeals ought to have asked is whether the state of the law in 1995 gave respondents fair warning that their alleged treatment of Hope was unconstitutional.",
      "star_marker": "741",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17898,
      "fragment": "#:~:text=the%20salient%20question%20that%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hope v. Pelzer",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Nat'l Rifle Ass'n of Am. v. Vullo",
          "cluster_id": 10635063,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane1_negative"
      },
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brosseau v. Haugen",
          "cluster_id": 137736,
          "cite": [
            "160 L. Ed. 2d 583",
            "125 S. Ct. 596",
            "543 U.S. 194",
            "2004 U.S. LEXIS 8275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iko v. Shreve",
          "cluster_id": 1026358,
          "cite": [
            "535 F.3d 225",
            "2008 U.S. App. LEXIS 16607",
            "2008 WL 3018444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Berkshire v. Debra Dahl",
          "cluster_id": 4635241,
          "cite": [
            "928 F.3d 520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randall v. Scott",
          "cluster_id": 149841,
          "cite": [
            "610 F.3d 701",
            "76 Fed. R. Serv. 3d 1566",
            "30 I.E.R. Cas. (BNA) 1544",
            "2010 U.S. App. LEXIS 13377",
            "93 Empl. Prac. Dec. (CCH) 43,922",
            "2010 WL 2595585"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herbert L. Board v. Karl Farnham, Jr.",
          "cluster_id": 788844,
          "cite": [
            "394 F.3d 469",
            "2005 U.S. App. LEXIS 101",
            "2005 WL 18109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bingham v. Thomas",
          "cluster_id": 613095,
          "cite": [
            "654 F.3d 1171",
            "2011 U.S. App. LEXIS 18293",
            "2011 WL 3862101"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terri Vinyard v. Steve Wilson",
          "cluster_id": 76029,
          "cite": [
            "311 F.3d 1340",
            "2002 U.S. App. LEXIS 23576",
            "2002 WL 31521208"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owens v. Baltimore City State's Attorneys Office",
          "cluster_id": 2736472,
          "cite": [
            "767 F.3d 379",
            "2014 U.S. App. LEXIS 18294",
            "2014 WL 4723803"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Blake",
          "cluster_id": 168392,
          "cite": [
            "469 F.3d 910",
            "34 Media L. Rep. (BNA) 2505",
            "2006 U.S. App. LEXIS 28144",
            "2006 WL 3291688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dean Effarage Farrow v. Dr. West",
          "cluster_id": 76092,
          "cite": [
            "320 F.3d 1235",
            "2003 U.S. App. LEXIS 2163",
            "22 Fla. L. Weekly Fed. C 582"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gobert v. Caldwell",
          "cluster_id": 45544,
          "cite": [
            "463 F.3d 339",
            "2006 U.S. App. LEXIS 22216",
            "2006 WL 2474846"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mann v. Taser International, Inc.",
          "cluster_id": 78530,
          "cite": [
            "588 F.3d 1291",
            "2009 U.S. App. LEXIS 26155",
            "2009 WL 4279713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dodds v. Richardson",
          "cluster_id": 158503,
          "cite": [
            "614 F.3d 1185",
            "2010 U.S. App. LEXIS 16326",
            "2010 WL 3064002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Scinto, Sr. v. Warden Stansberry",
          "cluster_id": 4318473,
          "cite": [
            "841 F.3d 219",
            "101 Fed. R. Serv. 1229",
            "2016 U.S. App. LEXIS 19936",
            "2016 WL 6543368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121169 OR 9434318 OR 9434319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjM5NTI2NDAwMDAwJnM9NTMwNjc5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28121169+OR+9434318+OR+9434319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(121169 OR 9434318 OR 9434319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NTQmcz0xNjcwODgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121169+OR+9434318+OR+9434319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121169 OR 9434318 OR 9434319)",
        "reviewed": 163,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 163,
        "triage_read": 1,
        "triage_snippet_classified": 162
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121169 OR 9434318 OR 9434319)",
    "indexed_citing_opinions": 1902,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121169,
        "count": 1518,
        "count_source": "search"
      },
      {
        "opinion_id": 9434318,
        "count": 397,
        "count_source": "search"
      },
      {
        "opinion_id": 9434319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4984,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hope-v-pelzer.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzOTA5OTYmcz0xMDYwMTg0NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28121169+OR+9434318+OR+9434319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121169,
        "cited_id": 70757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 72332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 105659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 109561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 110518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 111610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 112693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 321166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 396175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 484321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 673540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 682819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 711049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 772146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 1087956,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 2314799,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 2503952,
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
    "date_created": "2026-07-05T07:19:38Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:26:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hope v. Pelzer

```
<opinion type="majority">
<author id="b783-8">Justice Stevens</author>
<p id="ARXe">delivered the opinion of the Court.</p>
<p id="b783-9">The Court of Appeals for the Eleventh Circuit concluded that petitioner Larry Hope, a former prison inmate at the Limestone Prison in Alabama, was subjected to cruel and unusual punishment when prison guards twice handcuffed him to a hitching post to sanction him for disruptive conduct. Because that conclusion was not supported by earlier cases with “materially similar” facts, the court held that the respondents were entitled to qualified immunity, and therefore affirmed summary judgment in their favor. We granted cer-tiorari to determine whether the Court of Appeals’ qualified immunity holding comports with our decision in <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/" aria-description="Citation for case: United States v. Lanier">520 U. S. 259</a></span> (1997).</p>
<p id="b783-10">I</p>
<p id="b783-3">In 1995, Alabama was the only State that followed the practice of chaining inmates to one another in work squads. It was also the only State that handcuffed prisoners to “hitching posts” if they either refused to work or otherwise disrupted work squads.<footnotemark>1</footnotemark> Hope was handcuffed to a hitching <page-number citation-index="1" label="734">*734</page-number>post on two occasions. On May 11, 1995, while Hope was working in a chain gang near an interstate highway, he got into an argument with another inmate. Both men were taken back to the Limestone prison and handcuffed to a hitching post. Hope was released two hours later, after the guard captain determined that the altercation had been caused by the other inmate. During his two hours on the post, Hope was offered drinking water and a bathroom break every 15 minutes, and his responses to these offers were recorded on an activity log. Because he was only slightly taller than the hitching post, his arms were above shoulder height and grew tired from being handcuffed so high. Whenever he tried moving his arms to improve his circulation, the handcuffs cut into his wrists, causing pain and discomfort.</p>
<p id="b784-5">On June 7, 1995, Hope was punished more severely. He took a nap during the morning bus ride to the chain gang’s worksite, and when it arrived he was less than prompt in responding to an order to get off the bus. An exchange of vulgar remarks led to a wrestling match with a guard. Four other guards intervened, subdued Hope, handcuffed him, placed him in leg irons and transported him back to the prison where he was put on the hitching post. The guards made him take off his shirt, and he remained shirtless all <page-number citation-index="1" label="735">*735</page-number>day while the sun burned his skin.<footnotemark>2</footnotemark> He remained attached to the post for approximately seven hours. During this 7-hour period, he was given water only once or twice and was given no bathroom breaks.<footnotemark>3</footnotemark> At one point, a guard taunted Hope about his thirst. According to Hope’s affidavit: “[The guard] first gave water to some dogs, then brought the water cooler closer to me, removed its lid, and kicked the cooler over, spilling the water onto the ground.” App. 11.</p>
<p id="b785-5">Hope filed suit under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, in the United States District Court for the Northern District of Alabama against three guards involved in the May incident, one of whom also handcuffed him to the hitching post in June. The case was referred to a Magistrate Judge who treated the responsive affidavits filed by the defendants as a motion for summary judgment. Without deciding whether “the very act of placing him on a restraining bar for a period of hours as a form of punishment” had violated the Eighth Amendment, the Magistrate concluded that the guards were entitled to qualified immunity.<footnotemark>4</footnotemark> Supplemental App. to Pet. for Cert. 21. The District Court agreed, and entered judgment for respondents.</p>
<p id="b785-6">The United States Court of Appeals for the Eleventh Circuit affirmed. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d 975</a></span> (2001). Before reaching the <page-number citation-index="1" label="736">*736</page-number>qualified immunity issue, however, it answered the constitutional question that the District Court had bypassed. The court found that the use of the hitching post for punitive purposes violated the Eighth Amendment. Nevertheless, applying Circuit precedent concerning qualified immunity, the court stated that “‘the federal law by which the government official’s conduct should be evaluated must be preexisting, obvious and mandatory,’” and established, not by “ ‘abstractions,’ ” but by cases that are “ ‘materially similar’ ” to the facts in the case in front of us.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran"><em>Id., </em>at 981</a></span>. The court then concluded that the facts in the two precedents on which Hope primarily <em>relied </em>— Ort v. <em>White, </em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">813 F. 2d 318</a></span> (CA11 1987), and <em>Gates </em>v. <em>Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d 1291</a></span> (CA5 1974) — “[tjhough analogous,” were not “ ‘materially similar’ to Hope’s situation.’ ” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 981</a></span>. We granted certio-rari to review the Eleventh Circuit’s qualified immunity holding. <span class="citation multiple-matches"><a href="/c/U.%20S./534/1073/">534 U. S. 1073</a></span> (2002).</p>
<p id="b786-7">II</p>
<p id="b786-3">The threshold inquiry a court must undertake m a qualified immunity analysis is whether plaintiff’s allegations, if true, establish a constitutional violation. <em>Saucier </em>v. <em>Katz, </em><span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201 (2001). The Court of Appeals held that “the policy and practice of cuffing an inmate to a hitching post or similar stationary object for a period of time that surpasses that necessary to quell a threat or restore order is a violation of the Eighth Amendment.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#980" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 980-981</a></span>. The court rejected respondents’ submission that Hope could have ended his shackling by offering to return to work, finding instead that the purpose of the practice was punitive,<footnotemark>5</footnotemark> and that the circumstances of his confinement created <page-number citation-index="1" label="737">*737</page-number>a substantial risk of harm of which the officers were aware. Moreover, the court relied on Circuit precedent condemning similar practices<footnotemark>6</footnotemark> and the results of a United States Department of Justice (DOJ) report that found Alabama’s systematic use of the hitching post to be improper corporal punishment.<footnotemark>7</footnotemark> We agree with the Court of Appeals that the attachment of Hope to the hitching post under the circumstances alleged in this case violated the Eighth Amendment.</p>
<p id="b787-5">“ ‘[T]he unnecessary and wanton infliction of pain ... constitutes cruel and unusual punishment forbidden by the Eighth Amendment.’ ” <em>Whitley </em>v. <em>Albers, </em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S. 312, 319</a></span> (1986) (some internal quotation marks omitted). We have said that “[a]mong ‘unnecessary and wanton’ inflictions of pain are those that are ‘totally without penological justification.’” <em>Rhodes </em>v. <em>Chapman, </em><span class="citation" data-id="9428405"><a href="/opinion/110518/rhodes-v-chapman/#346" aria-description="Citation for case: Rhodes v. Chapman">452 U. S. 337, 346</a></span> (1981). In making this determination in the context of prison condi<page-number citation-index="1" label="738">*738</page-number>tions, we must ascertain whether the officials involved acted with “deliberate indifference” to the inmates’ health or safety. <em>Hudson </em>v. <em>McMillian, </em><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/#8" aria-description="Citation for case: Hudson v. McMillian">503 U. S. 1, 8</a></span> (1992). We may infer the existence of this subjective state of mind from the fact that the risk of harm is obvious. <em>Farmer </em>v. <em>Brennan, </em><span class="citation" data-id="9527063"><a href="/opinion/1087956/farmer-v-brennan/#842" aria-description="Citation for case: Farmer v. Brennan">511 U. S. 825, 842</a></span> (1994).</p>
<p id="b788-5">As the facts are alleged by Hope, the Eighth Amendment violation is obvious. Any safety concerns had long since abated by the time petitioner was handcuffed to the hitching post because Hope had already been subdued, handcuffed, placed in leg irons, and transported back to the prison. He was separated from his work squad and not given the opportunity to return to work. Despite the clear lack of an emergency situation, the respondents knowingly subjected him to a substantial risk of physical harm, to unnecessary pain caused by the handcuffs and the restricted position of confinement for a 7-hour period, to unnecessary exposure to the heat of the sun, to prolonged thirst and taunting, and to a deprivation of bathroom breaks that created a risk of particular discomfort and humiliation.<footnotemark>8</footnotemark> The use of the hitching post under these circumstances violated the “basic concept underlying the Eighth Amendment[, which] is nothing less than-the dignity of man.” <em>Trop </em>v. <em>Dulles, </em><span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/#100" aria-description="Citation for case: Trop v. Dulles">356 U. S. 86, 100</a></span> (1958). This punitive treatment amounts to gratuitous infliction of “wanton and unnecessary” pain that our precedent clearly prohibits.</p>
<p id="b789-8"><page-number citation-index="1" label="739">*739</page-number>H-l HH I — I</p>
<p id="b789-3">Despite their participation m this constitutionally impermissible conduct, respondents may nevertheless be shielded from liability for civil damages if their actions did not violate “clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982). In assessing whether the Eighth Amendment violation here met the <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>test, the Court of Appeals required that the facts of previous cases be “‘materially similar’ to Hope’s situation.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 981</a></span>. This rigid gloss on the qualified immunity standard, though supported by Circuit precedent,<footnotemark>9</footnotemark> is not consistent with our cases.</p>
<p id="b789-4">As we have explained, qualified immunity operates “to ensure that before they are subjected to suit, officers are on notice their conduct is unlawful.” <em>Saucier </em>v. <em>Katz, </em>533 U. S., at 206. For a constitutional right to be clearly established, its contours “must be sufficiently clear that a reasonable official would understand that what he is doing violates that right. This is not to say that an official action is protected by qualified immunity unless the very action in question has previously been held unlawful, see <em>Mitchell </em>[v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511</a></span>,] 535, n. 12; but it is to say that in the light of pre-existing law the unlawfulness must be apparent.” <em>Anderson </em>v. <em>Creighton, </em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 640</a></span> (1987).</p>
<p id="b789-5">Officers sued in a civil action for damages under <span class="citation no-link">42 U. S. C. § 1983</span> have the same right to fair notice as do defendants charged with the criminal offense defined in <span class="citation no-link">18 U. S. C. §242</span>. Section 242 makes it a crime for a state official to act “willfully” and under color of law to deprive a person of rights protected by the Constitution. In <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/" aria-description="Citation for case: United States v. Lanier">520 U. S. 259</a></span> (1997), we held that the defendant was entitled <page-number citation-index="1" label="740">*740</page-number>to “fair warning” that his conduct deprived his victim of a constitutional right, and that the standard for determining the adequacy of that warning was the same as the standard for determining whether a constitutional right was “clearly established” in civil litigation under § 1983.<footnotemark>10</footnotemark></p>
<p id="b790-5">In <em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/" aria-description="Citation for case: United States v. Lanier">Lanier</a></span>, </em>the Court of Appeals had held that the indictment did not charge an offense under § 242 because the constitutional right allegedly violated had not been identified in any earlier case involving a factual situation “ ‘fundamentally similar’” to the one in issue. <em>Id., </em>at 263 (citing <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="9488829"><a href="/opinion/711049/united-states-v-david-w-lanier/#1393" aria-description="Citation for case: United States v. David W. Lanier">73 F. 3d 1380, 1393</a></span> (CA6 1996)). The Court of Appeals had assumed that the defendant in a criminal case was entitled to a degree of notice “ ‘substantially higher than the “clearly established” standard used to judge qualified immunity’ ” in civil cases under § 1983. <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#263" aria-description="Citation for case: United States v. Lanier">520 U. S., at 263</a></span>. We reversed, explaining that the “fair warning” requirement is identical under §242 and the qualified immunity standard. We pointed out that we had “upheld convictions under § 241 or §242 despite notable factual distinctions between the precedents relied on and the cases then before the Court, so long as the prior decisions gave reasonable warning that the conduct then at issue violated constitutional rights.” <em>Id., </em>at 269. We explained:</p>
<blockquote id="b790-6">“This is not to say, of course, that the single warning standard points to a single level of specificity sufficient in every instance. In some circumstances, as when an <page-number citation-index="1" label="741">*741</page-number>earlier case expressly leaves open whether a general rule applies to the particular type of conduct at issue, a very high degree of prior factual particularity may be necessary. But general statements of the law are not inherently incapable of giving fair and clear warning, and in other instances a general constitutional rule already identified in the decisional law may apply with obvious clarity to the specific conduct in question, even though ‘the very action in question has [not] previously been held unlawful/ <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton"><em>Anderson, supra, </em>at 640</a></span>.” <em>Id., </em>at 270-271 (citation omitted).</blockquote>
<p id="b791-5">Our opinion in <em>Lanier </em>thus makes clear that officials can still be on notice that their conduct violates established law even in novel factual circumstances. Indeed, in <em>Lanier, </em>we expressly rejected a requirement that previous cases be “fundamentally similar.” Although earlier cases involving “fundamentally similar” facts can provide especially strong support for a conclusion that the law is clearly established, they are not necessary to such a finding. The same is true of cases with “materially similar” facts. Accordingly, pursuant to <em>Lanier, </em>the salient question that the Court of Appeals ought to have asked is whether the state of the law in 1995 gave respondents fair warning that their alleged treatment of Hope was unconstitutional. It is to this question that we now turn.</p>
<p id="b791-6">IV</p>
<p id="b791-7">The use of the hitching post as alleged by Hope “unnecessarily] and wanton[ly] inflicted pain,” <em>Whitley, </em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 319</a></span> (internal quotation marks omitted), and thus was a clear violation of the Eighth Amendment. See Part II, <em>supra. </em>Arguably, the violation was so obvious that our own Eighth Amendment cases gave respondents fair warning that their conduct violated the Constitution. Regardless, in light of binding Eleventh Circuit precedent, an Alabama Department of Corrections (ADOC) regulation, and a DOJ report <page-number citation-index="1" label="742">*742</page-number>informing the ADOC of the constitutional infirmity in its use of the hitching post, we readily conclude that the respondents’ conduct violated “clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>.</p>
<p id="b792-5">Cases decided by the Court of Appeals for the Fifth Circuit before 1981 are binding precedent in the Eleventh Circuit today. See <em>Bonner </em>v. <em>Prichard, </em><span class="citation" data-id="396175"><a href="/opinion/396175/larry-bonner-v-city-of-prichard-alabama/" aria-description="Citation for case: Larry Bonner v. City of Prichard, Alabama">661 F. 2d 1206</a></span> (CA11 1981). In one of those cases, decided in 1974, the Court of Appeals reviewed a District Court decision finding a number of constitutional violations in the administration of Mississippi’s prisons. <em>Gates </em>v. <em>Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d 1291</a></span>. That opinion squarely held that several of those “forms of corporal punishment run afoul of the Eighth Amendment [and] offend contemporary concepts of decency, human dignity, and precepts of civilization which we profess to possess.” <em>Id., </em>at 1806. Among those forms of punishment were “handcuffing inmates to the fence and to cells for long periods of time, . . . and forcing inmates to stand, sit or lie on crates, stumps, or otherwise maintain awkward positions for prolonged periods.” <em>Ibid. </em>The fact that <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>found several forms of punishment impermissible does not, as respondents suggest, lessen the force of its holding with respect to handcuffing inmates to cells or fences for long periods of time. Nor, for the purpose of providing fair notice to reasonable officers administering punishment for past misconduct, is there any reason to draw a constitutional distinction between a practice of handcuffing an inmate to a fence for prolonged periods and handcuffing him to a hitching post for seven hours. The Court of Appeals’ conclusion to the contrary exposes the danger of a rigid, overreliance on factual similarity. As the Government submits in its brief <em>amicus curiae: </em>“No reasonable officer could have concluded that the constitutional holding of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>turned on the fact that inmates were handcuffed to fences or the bars of cells, rather than a specially designed metal bar designated for shackling. If anything, the use of <page-number citation-index="1" label="743">*743</page-number>a designated hitching post highlights the constitutional problem.” Brief for United States as <em>Amicus Curiae </em>22. In light of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span>, </em>the unlawfulness of the alleged conduct should have been apparent to respondents.</p>
<p id="b793-5">The reasoning, though not the holding, in a case decided by the Eleventh Circuit in 1987 sent the same message to reasonable officers in that Circuit. In <em>Ort </em>v. <em>White, </em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">813 F. 2d 318</a></span>, the Court of Appeals held that an officer’s temporary denials of drinking water to an inmate who repeatedly refused to do his share of the work assigned to a farm squad “should not be viewed as punishment in the strict sense, but instead as necessary coercive measures undertaken to obtain compliance with a reasonable prison rule, <em>i. e., </em>the requirement that all inmates perform their assigned farm squad duties.” <span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#325" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony..."><em>Id., </em>at 325</a></span>. “The officer’s clear motive was to encourage Ort to comply with the rules and to do the work required of him, after which he would receive the water like everyone else.” <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ibid.</a></span> </em>The court cautioned, however, that a constitutional violation might have been present “if later, once back at the prison, officials had decided to deny [Ort] water as punishment for his refusal to work.” <span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#326" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony..."><em>Id., </em>at 326</a></span>. So too would a violation have occurred if the method of coercion reached a point of severity such that the recalcitrant prisoner’s health was at risk. <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ibid.</a></span> </em>Although the facts of the case are not identical, Ort]s premise is that “physical abuse directed at [a] prisoner <em>after </em>he terminate^] his resistance to authority would constitute an actionable eighth amendment violation.” <span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#324" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony..."><em>Id., </em>at 324</a></span>. This premise has clear applicability in this case. Hope was not restrained at the worksite until he was willing to return to work. Rather, he was removed back to the prison and placed under conditions that threatened his health. <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>therefore gave fair warning to respondents that their conduct crossed the line of what is constitutionally permissible.</p>
<p id="b793-6">Relevant to the question whether <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>provided fair warning to respondents that their conduct violated the Constitu<page-number citation-index="1" label="744">*744</page-number>tion is a regulation promulgated by ADOC in 1993.<footnotemark>11</footnotemark> The regulation authorizes the use of the hitching post when an inmate refuses to work or is otherwise disruptive to a work squad. It provides that an activity log should be completed for each such inmate, detailing his responses to offers of water and bathroom breaks every 15 minutes. Such a log was completed and maintained for petitioner’s shackling in May, but the record contains no such log for the 7-hour shackling in June and the record indicates that the periodic offers contemplated by the regulation were not made. App. 43-48. The regulation also states that an inmate “will be allowed to join his assigned squad” whenever he tells an officer “that he is ready to go to work.” <em>Id., </em>at 103. The findings in <em>Austin </em>v. <em>Hopper, </em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1244" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d 1210, 1244-1246</a></span> (MD Ala. 1998), as well as the record in this case, indicate that this important provision of the regulation was frequently ignored by corrections officers. If regularly observed, a requirement that would effectively give the inmate the keys to the handcuffs that attached him to the hitching post would have made this case more analogous to the practice upheld in <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span>, </em>rather than the kind of punishment <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>described as impermissible. A course of conduct that tends to prove that the requirement was merely a sham, or that respondents could ignore it with impunity, provides equally strong support for the conclusion that they were fully aware of the wrongful character of their conduct.</p>
<p id="b794-5">Respondents violated clearly established law. Our conclusion that “a reasonable person would have known,” <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>, of the violation is buttressed by the fact that the DOJ specifically advised the ADOC of the unconstitutionality of its practices before the incidents in this case took place. The DOJ had conducted a study in 1994 of Alabama’s use of the hitching post. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#979" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 979</a></span>. <page-number citation-index="1" label="745">*745</page-number>Among other findings, the DOJ report noted that ADOC’s officers consistently failed to comply with the policy of immediately releasing any inmate from the hitching post who agrees to return to work. The DOJ concluded that the systematic use of the restraining bar in Alabama constituted improper corporal punishment. <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>Accordingly, the DOJ advised the ADOC to cease use of the hitching post in order to meet constitutional standards. The ADOC replied that it thought the post could permissibly be used “ ‘to preserve prison security and discipline.’ ” <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>In response, the DOJ informed the ADOC that, “‘[although an emergency situation may warrant drastic action by corrections staff, our experts found that the “rail” is being used systematically as an improper punishment for relatively trivial offenses. Therefore, we have concluded that the use of the “rail” is without penological justification.”’ <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>Although there is nothing in the record indicating that the DOJ’s views were communicated to respondents, this exchange lends support to the view that reasonable officials in the ADOC should have realized that the use of the hitching post under the circumstances alleged by Hope violated the Eighth Amendment prohibition against cruel and unusual punishment.</p>
<p id="b795-5">The obvious cruelty inherent in this practice should have provided respondents with some notice that their alleged conduct violated Hope’s constitutional protection against cruel and unusual punishment. Hope was treated in a way antithetical to human dignity — he was hitched to a post for an extended period of time in a position that was painful, and under circumstances that were both degrading and dangerous. This wanton treatment was not done of necessity, but as punishment for prior conduct. Even if there might once have been a question regarding the constitutionality of this practice, the Eleventh Circuit precedent of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>and <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span>, </em>as well as the DOJ report condemning the practice, put a reasonable officer on notice that the use of the hitching <page-number citation-index="1" label="746">*746</page-number>post under the circumstances alleged by Hope was unlawful. The “fair and clear warning,” <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#271" aria-description="Citation for case: United States v. Lanier">520 U. S., at 271</a></span>, that these cases provided was sufficient to preclude the defense of qualified immunity at the summary judgment stage.</p>
<p id="b796-5">V</p>
<p id="b796-6">In response to Justice Thomas’ thoughtful dissent, we make the following three observations. The first is that in granting certiorari to review the summary judgment entered in favor of the officers, we did not take any question about the sufficiency of pleadings and affidavits to raise a genuine possibility that the three named officers were responsible for the punitive acts of shackling alleged. All questions raised by petitioner (the plaintiff against whom summary judgment was entered) go to the application of the standard that no immunity is available for official acts when “it would be clear to a reasonable officer that his conduct was unlawful in the situation he confronted.” <em>Saucier </em>v. <em>Katz, </em>533 U. S., at 202. The officers’ brief in opposition to certiorari likewise addressed only the legal standard of what is clearly established. The resulting focus in the case was the Eleventh Circuit’s position, that a violation is not clearly established unless it is the subject of a prior case of liability on facts “ ‘materially similar’ ” to those charged. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 981</a></span>. We did not take, and do not pass upon, the questions whether or to what extent the three named officers may be held responsible for the acts charged, if proved. Nothing in our decision forecloses any defense other than qualified immunity on the ground relied upon by the Court of Appeals.</p>
<p id="b796-7">Second, we may address the immunity question on the assumption that the act of field discipline charged on each occasion was handcuffing Hope to a hitching post for an extended period apparently to inflict gratuitous pain or discomfort, with no justification in threatened harm or a continuing refusal to work. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#980" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran"><em>Id., </em>at 980</a></span> (on neither occasion did Hope “refus[e] to work or encourag[e] other inmates to refuse to <page-number citation-index="1" label="747">*747</page-number>work”). The Court of Appeals clearly held the act of cuffing petitioner to the hitching post itself to suffice as an unconstitutional act: “We find that cuffing an inmate to a hitching post for a period of time extending past that required to address an immediate danger or threat is a violation of the Eighth Amendment.” <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>Although the court continued that “[t]his violation is exacerbated by the lack of proper clothing, water, or bathroom breaks,” <em>ibid., </em>this embellishment was not the basis of its decision, and our own decision adequately rests on the same assumption that sufficed for the Court of Appeals.</p>
<p id="b797-5">Third, in applying the objective immunity test of what a reasonable officer would understand, the significance of federal judicial precedent is a function in part of the Judiciary’s structure. The unreported District Court opinions cited by the officers are distinguishable on their own terms.<footnotemark>12</footnotemark> But regardless, they would be no match for the Circuit precedents<footnotemark>13</footnotemark> in <em>Gates </em>v. <em>Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/#1306" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d, at 1306</a></span>, which held that “handcuffing inmates to the fence and to cells for long periods of time” was unconstitutional, and <em>Ort </em>v. <em>White, </em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#326" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">813 F. 2d, at 326</a></span>, which suggested that it would be unconstitutional to inflict gratuitous pain on an inmate (by refusing him water) when punishment was unnecessary to enforce <page-number citation-index="1" label="748">*748</page-number>on-the-spot discipline. The vitality of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>and <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>could not seriously be questioned in light of our own decisions holding that gratuitous infliction of punishment is unconstitutional, even in the prison context, see <em>supra, </em>at 787 (citing <em>Whitley </em>v. <em>Albers, </em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 319</a></span>; <em>Rhodes </em>v. <em>Chapman, </em><span class="citation" data-id="9428405"><a href="/opinion/110518/rhodes-v-chapman/#346" aria-description="Citation for case: Rhodes v. Chapman">452 U. S., at 346</a></span>).</p>
<p id="b798-5">The judgment of the Court of Appeals is reversed.</p>
<p id="b798-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b783-5"> In its review of the summary judgment, the Court of Appeals viewed the facts in the light most favorable to Hope, the nonmoving party. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#977" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d 975, 977</a></span> (CA11 2001) (case below). We do the same. <em>Saucier </em>v. <em>Katz, </em><span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201 (2001). The Court of Appeals also referenced facts established in <em>Austin </em>v. <em>Hopper, </em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d 1210</a></span> (MD Ala. 1998). <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#978" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 978, n. 6</a></span>. This was appropriate because <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span> </em>is a class-action suit brought by Alabama prisoners, including Hope, and the District Court opinion in that case discusses Hope’s allegations at some length. <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1247" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d, at 1247-1248</a></span>. In their summary judgment papers, both Hope and respondents referenced the findings in <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span>, </em>and thus those <page-number citation-index="1" label="734">*734</page-number>findings are part of the record in this case. See, <em>e. g., </em>Plaintiff’s Preliminary Response to Defendants’ Special Report, Record 30; Defendants’ Response to Court Order, App. 61. Accordingly, for purposes of our review of the grant of summary judgment, the <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span> </em>findings may also be assumed true, and we reference them when appropriate.</p>
<p id="AtqJ">As <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span> </em>explained, the hitching post is a horizontal bar “‘made of sturdy, nonflexible material,”’ placed between 45 and 57 inches from the ground. Inmates are handcuffed to the hitching post in a standing position and remain standing the entire time they are placed on the post. Most inmates are shackled to the hitching post with their two hands relatively close together and at face level. <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1241" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d, at 1241-1242</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b785-7"> “The most repeated complaint of the hitching post, however, was the strain it produced on inmates’ muscles by forcing them to remain in a standing position with their arms raised in a stationary position for a long period of time. In addition to their exposure to sunburn, dehydration, and muscle aches, the inmates are also placed in substantial pain when the sun heats the handcuffs that shackle them to the hitching post, or heats the hitching post itself. Several of the inmates described the way in which the handcuffs burned and chafed their skin during their placement on the post.” <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1248" aria-description="Citation for case: Austin v. Hopper"><em>Id., </em>at 1248</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b785-8"> The Court of Appeals noted that respondents had not produced any activity log for this incident, despite the policy that required that such a log be maintained. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#977" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 977, n. 1</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b785-9"> Supplemental App. to Pet. for Cert. 21-27.</p>
</footnote>
<footnote label="5">
<p id="b786-4"> In reaching this conclusion, the Court of Appeals stated: “While the DOC claims that Hope would have been released from the hitching post had he asked to return to work, the evidence suggests this is not the case. First, Hope never refused to work. During the May incident, he was the victim in an altercation on the work site, but he never refused to do his <page-number citation-index="1" label="737">*737</page-number>job. During the June incident, Hope was involved in an altercation with prison guards. There is nothing in the record, however, claiming that he refused to work or encouraged other inmates to refuse to work. Therefore, it is not clear that the solution to his hitching post problem was to ask to return to work. Second, Hope was placed in a car and driven back to Limestone to be cuffed to the hitching post on both occasions. Given the facts, it is improbable that had Hope said, T want to go back to work,’ a prison guard would have left his post at Limestone to drive Hope back to the work site. It is more likely that the guards left Hope on the post until his work detail returned to teach the other inmates a lesson.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#980" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 980</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b787-11"> “Since abolishing the pillory over a century ago, our system of justice has consistently moved away from forms of punishment similar to hitching posts in prisons. In <em>Gates v. Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d 1291</a></span> (5th Cir. 1974), in regard to ‘handcuffing inmates to the fence and to cells for long periods of time’ and other such punishments, we stated that ‘[w]e have ho difficulty in reaching the conclusion that these forms of corporal punishment run afoul of the Eighth Amendment, offend contemporary concepts of decency, human dignity, and-precepts of civilization which we profess to possess.’ <em>Gates, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/#1306" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d at 1306</a></span>.” <em>Id., </em>at 979.</p>
</footnote>
<footnote label="7">
<p id="b787-12"> The DOJ report apparently was not before the District Court in this case, but the Court of Appeals took judicial notice of the report and referenced it throughout the decision below. <em>Id., </em>at 979, n. 8.</p>
</footnote>
<footnote label="8">
<p id="b788-6"> The awareness of the risk of harm attributable to any individual respondent may be evaluated in part by considering the pattern of treatment that inmates generally received when attached to the hitching post. In <em>Austin </em>v. <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Hopper</a></span>, </em>the District Court cited examples of humiliating incidents resulting from the denial of bathroom breaks. One inmate “was not permitted to use the restroom or to change his clothing for four and one-half hours after he had defecated on himself.” <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1246" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d, at 1246</a></span>. “Moreover, certain corrections officers not only ignored or denied inmates’ requests for water or access to toilet facilities, but taunted them while they were clearly suffering from dehydration ....” <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1247" aria-description="Citation for case: Austin v. Hopper"><em>Id., </em>at 1247</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b789-6"> See, <em>e. g., Suissa </em>v. <em>Fulton County, </em><span class="citation" data-id="70757"><a href="/opinion/70757/suissa-v-fulton-county-ga/" aria-description="Citation for case: Suissa v. Fulton County, GA">74 F. 3d 266</a></span>-270 (CA11 1996); <em>Lassiter </em>v. <em>Alabama A&amp;M Univ. Bd. of Trustees, </em><span class="citation" data-id="673540"><a href="/opinion/673540/albert-e-lassiter-v-alabama-a-m-university-board-of-trustees-douglas/#1150" aria-description="Citation for case: Albert E. Lassiter v. Alabama a &amp; M University, Board of...">28 F. 3d 1146, 1150</a></span> (CA11 1994); <em>Hill </em>v. <em>Dekalb Regional Youth Detention Center, </em><span class="citation" data-id="6932906"><a href="/opinion/7030810/hill-v-dekalb-regional-youth-detention-center/#1185" aria-description="Citation for case: Hill v. Dekalb Regional Youth Detention Center">40 F. 3d 1176, 1185</a></span> (CA11 1994).</p>
</footnote>
<footnote label="10">
<p id="b790-7"> “[T]he object of the ‘clearly established’ immunity standard is not different from that of ‘fair warning’ as it relates to law ‘made specific’ for the purpose of validly applying § 242. The fact that one has a civil and the other a criminal law role is of no significance; both serve the same objective, and in effect the qualified immunity test is simply the adaptation of the fair warning standard to give officials (and, ultimately, governments) the same protection from civil liability and its consequences that individuals have traditionally possessed in the face of vague criminal statutes. To require something clearer than ‘clearly established’ would, then, call for something beyond ‘fair warning.’” <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#270" aria-description="Citation for case: United States v. Lanier">520 U. S., at 270-271</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b794-6"> The regulation was not provided to the District Court, but it was added to the record at the request of the Court of Appeals. See App. 100-106.</p>
</footnote>
<footnote label="12">
<p id="b797-6"> In three of the decisions, the inmates were given the choice between working or being restrained. See <em>Whitson </em>v. <em>Gillikin, </em>No. CV-93-H-1517-NE (ND Ala., Jan. 24, 1994), p. 4, App. 84; <em>Dale </em>v. <em>Murphy, </em>No. CV-85-1091-H-S (SD Ala., Feb. 4, 1986), p. 2; <em>Ashby </em>v. <em>Dees, </em>No. CV-94-U-0605-NE (ND Ala., Dec. 27, 1994), p. 6. In others, the inmates were offered regular water and bathroom breaks. See <em>Lane </em>v. <em>Findley, </em>No. CV-93-C-1741-S (ND Ala., Aug. 4, 1994), p. 9; <em>Williamson </em>v. <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Anderson</a></span>, </em>No. CV-92-H-675-N (MD Ala., Aug. 18, 1993), p. 2; <em>Hollis </em>v. <em>Folsom, </em>No. CV-94-T-0052-N (MD Ala., Nov. 4, 1994), p. 9. Finally, in <em>Vinson </em>v. <em>Thompson, </em>No. CV-94-A-268-N (MD Ala., Dec. 9,1994), the inmate was restrained for approximately 45 minutes. <em>Id., </em>at 2.</p>
</footnote>
<footnote label="13">
<p id="b797-7"> There are apparently no decisions on similar facts from other Circuits, presumably because Alabama is the only State to authorize the use of the hitching post in its prison system.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Howes v. Fields.md  (`case`, 5 assertions)

### content_page

```
---
title: "Howes v. Fields"
type: case
citation: "565 U.S. 499 (2012)"
parallel_cite: "132 S. Ct. 1181; 182 L. Ed. 2d 17"
neutral_cite: "2012 U.S. LEXIS 1077; 2012 WL 538280"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-02-21
docket: 10-680
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-02-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Howes v. Fields
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/623144/howes-v-fields/"
  cluster_id: 623144
  opinion_id: 623144
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Maryland v. Shatzer]]", "[[Berkemer v. McCarty]]", "[[Miranda v. Arizona]]", "[[Mathis v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "prisoners"]
holding: "Imprisonment alone does not make questioning custodial for Miranda; whether an inmate is \"in custody\" depends on the totality — here,…"
lake:
  record_id: Howes v. Fields
  status: verified
  projected_at: 2026-07-09
---

# Howes v. Fields

*565 U.S. 499 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Randall Fields, serving a sentence in a Michigan jail, was taken from his cell to a conference room and questioned by two sheriff's deputies for five to seven hours about conduct that allegedly occurred before he came to prison. He was told more than once that he was free to leave and return to his cell, was not restrained, and was given food and water; he confessed without receiving *[[Miranda v. Arizona|Miranda]]* warnings. The Sixth Circuit held that questioning a prisoner in isolation about outside conduct is custodial [[Common Legal Terms#per-se|per se]].

## Issue
Whether a prisoner is "in custody" for *[[Miranda v. Arizona|Miranda]]* purposes — requiring warnings — simply because he is incarcerated and is questioned in private about events occurring outside the prison.

## Rule
No; there is no categorical rule, and imprisonment by itself is not *[[Miranda v. Arizona|Miranda]]* custody. "Not all restraints on freedom of movement amount to custody for purposes of Miranda." — *Howes v. Fields*, 565 U.S. 499 (2012) (slip op., at 9). ^pin-op9

"If a break in custody can occur while a prisoner is serving an uninterrupted term of imprisonment, it must follow that imprisonment alone is not enough to create a custodial situation within the meaning of Miranda." — *Id.* (slip op., at [10](https://www.courtlistener.com/opinion/623144/howes-v-fields/#:~:text=If%20a%20break%20in%20custody%20can%20occur%20while)). ^pin-op10

Whether a prisoner is in custody depends on all the features of the interrogation, asking whether the environment presents the same inherently coercive pressures as station-house questioning.

## Application
Taking account of all the circumstances of Fields's interrogation — he was repeatedly told he could leave and return to his cell, was not physically restrained, was questioned in a well-lit conference room sometimes left open, and was offered food and water — a reasonable person in his position would have felt free to terminate the interview and go back to his cell, subject to the ordinary restraints of prison life. He was therefore not in custody, and no *[[Miranda v. Arizona|Miranda]]* warnings were required.

## Conclusion
Fields was not in *[[Miranda v. Arizona|Miranda]]* custody; the categorical rule applied below was rejected and the judgment reversed. Imprisonment alone does not make questioning custodial.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Howes* draws on [[Maryland v. Shatzer]] and [[Berkemer v. McCarty]] to hold that custody for [[Miranda v. Arizona]] turns on the totality of the interrogation's circumstances, not on the bare fact of incarceration.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Howes v. Fields*, 565 U.S. 499 (2012) — https://www.courtlistener.com/opinion/623144/howes-v-fields/ — pinpoints given as slip-opinion pages (slip op., at 9, 10); CourtListener carries the slip opinion, paginated by slip page (opinion 623144).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ea631f519835d762", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "565 U.S. 499 (2012)", "court": "U.S. Supreme Court", "neutral_cite": "2012 U.S. LEXIS 1077; 2012 WL 538280", "official_citation_present": true, "parallel_cite": "132 S. Ct. 1181; 182 L. Ed. 2d 17", "title": "Howes v. Fields", "year": "2012"}}
{"assertion_id": "9c4799ea413a2755", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Howes v. Fields"}}
{"assertion_id": "e2fbec22b627b693", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Imprisonment alone does not make questioning custodial for Miranda; whether an inmate is \\\"in custody\\\" depends on the totality — here,…", "title": "Howes v. Fields"}}
{"assertion_id": "51b89799aa87ce78", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2012-02-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Howes v. Fields", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Howes v. Fields", "varies_by_point": "false"}}
{"assertion_id": "5927d2bdf1d1c6f1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Howes v. Fields"}}
```

### lake record — Howes v. Fields

```json
{
  "schema_version": "s2.v1",
  "record_id": "Howes v. Fields",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Howes v. Fields",
    "case_name_short": "Howes",
    "case_name_full": "Howes, Warden v. Fields",
    "input_case_name": "Howes v. Fields",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-02-21",
    "year": 2012,
    "docket": "10-680",
    "cluster_id": 623144,
    "lead_opinion_id": 623144,
    "sibling_ids": [
      623144,
      9485375,
      9485376
    ],
    "absolute_url": "/opinion/623144/howes-v-fields/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 499",
      "volume": "565",
      "reporter": "U.S.",
      "page": "499",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 1181",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1181",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 17",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 1077",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1077",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 538280",
        "volume": "2012",
        "reporter": "WL",
        "page": "538280",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 1181",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1181",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 17",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 499",
        "volume": "565",
        "reporter": "U.S.",
        "page": "499",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 1077",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1077",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 538280",
        "volume": "2012",
        "reporter": "WL",
        "page": "538280",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 499",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 499",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op9",
      "page": null,
      "quote": "for *Miranda* purposes \u2014 requiring warnings \u2014 simply because he is incarcerated and is questioned in private about events occurring outside the prison. ## Rule No; there is no categorical rule, and imprisonment by itself is not *Miranda* custody.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op10",
      "page": null,
      "quote": "If a break in custody can occur while a prisoner is serving an uninterrupted term of imprisonment, it must follow that imprisonment alone is not enough to create a custodial situation within the meaning of Miranda.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 26225,
      "fragment": "#:~:text=If%20a%20break%20in%20custody%20can%20occur%20while",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-02-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Howes v. Fields",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Barksdale",
          "cluster_id": 4867083,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
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
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cawthron",
          "cluster_id": 4500714,
          "cite": [
            "97 N.E.3d 671",
            "479 Mass. 612"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mattox",
          "cluster_id": 4478290,
          "cite": [
            "2018 Ohio 992",
            "108 N.E.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
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
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hammonds",
          "cluster_id": 4430449,
          "cite": [
            "804 S.E.2d 438",
            "370 N.C. 158",
            "2017 WL 4322423",
            "2017 N.C. LEXIS 702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. MacDonald",
          "cluster_id": 5309859,
          "cite": [
            "2017 UT App 124",
            "402 P.3d 91",
            "844 Utah Adv. Rep. 90",
            "2017 WL 3224516",
            "2017 Utah App. LEXIS 124"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Soto",
          "cluster_id": 4401346,
          "cite": [
            "2017 Ohio 4348",
            "93 N.E.3d 204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Davis",
          "cluster_id": 4667521,
          "cite": [
            "2019 CO 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Todd Peterson v. Timothy Douma",
          "cluster_id": 2708669,
          "cite": [
            "751 F.3d 524",
            "2014 WL 1778150",
            "2014 U.S. App. LEXIS 8524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Ortiz, Octavio",
          "cluster_id": 2945879,
          "cite": [
            "382 S.W.3d 367",
            "2012 Tex. Crim. App. LEXIS 1386",
            "2012 WL 5348503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Keaton",
          "cluster_id": 2301803,
          "cite": [
            "45 A.3d 1050",
            "615 Pa. 675"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Tekoh",
          "cluster_id": 6480695,
          "cite": [
            "597 U.S. 134",
            "213 L. Ed. 2d 479",
            "142 S. Ct. 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caro",
          "cluster_id": 4629272,
          "cite": [
            "248 Cal. Rptr. 3d 96",
            "7 Cal. 5th 463",
            "442 P.3d 316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Zyriah Henry Floyd Schlitter",
          "cluster_id": 3212050,
          "cite": [
            "881 N.W.2d 380",
            "2016 Iowa Sup. LEXIS 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Krebs",
          "cluster_id": 4680693,
          "cite": [
            "452 P.3d 609",
            "255 Cal. Rptr. 3d 95",
            "8 Cal. 5th 265"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Elliott",
          "cluster_id": 2712696,
          "cite": [
            "494 Mich. 292",
            "833 N.W.2d 284",
            "2013 WL 3198007",
            "2013 Mich. LEXIS 938"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Molano",
          "cluster_id": 6240586,
          "cite": [
            "249 Cal. Rptr. 3d 1",
            "7 Cal. 5th 620",
            "443 P.3d 856"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tizon v. Commonwealth",
          "cluster_id": 1061710,
          "cite": [
            "723 S.E.2d 260",
            "60 Va. App. 1",
            "2012 WL 1080167",
            "2012 Va. App. LEXIS 105"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dishon McNary v. Marcus Hardy",
          "cluster_id": 821295,
          "cite": [
            "708 F.3d 905",
            "2013 WL 673653",
            "2013 U.S. App. LEXIS 3885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andrew v. White",
          "cluster_id": 10318017,
          "cite": [
            "604 U.S. 86",
            "220 L. Ed. 2d 340",
            "145 S. Ct. 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Campbell v. Bradshaw",
          "cluster_id": 625704,
          "cite": [
            "674 F.3d 578",
            "2012 WL 913788",
            "2012 U.S. App. LEXIS 5735"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Timothy E. Dobbs",
          "cluster_id": 4765836,
          "cite": [
            "945 N.W.2d 609",
            "392 Wis. 2d 505",
            "2020 WI 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owens v. Trammell",
          "cluster_id": 2814864,
          "cite": [
            "792 F.3d 1234",
            "2015 U.S. App. LEXIS 11687",
            "2015 WL 4081123"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Morva v. David Zook",
          "cluster_id": 3201023,
          "cite": [
            "821 F.3d 517",
            "2016 U.S. App. LEXIS 8336",
            "2016 WL 2587362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Budder v. Addison",
          "cluster_id": 4377018,
          "cite": [
            "851 F.3d 1047",
            "2017 U.S. App. LEXIS 4988",
            "2017 WL 1056094"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. John Edward Barritt",
          "cluster_id": 4525400,
          "cite": [
            "926 N.W.2d 811",
            "325 Mich. App. 556"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Smith",
          "cluster_id": 4408805,
          "cite": [
            "2016 IL 119659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "BAUMRUK v. State",
          "cluster_id": 2546714,
          "cite": [
            "364 S.W.3d 518",
            "2012 WL 1339359",
            "2012 Mo. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ryan Holness",
          "cluster_id": 820254,
          "cite": [
            "706 F.3d 579",
            "2013 WL 491944",
            "2013 U.S. App. LEXIS 2834"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. William Little",
          "cluster_id": 3216832,
          "cite": [
            "499 Mich. 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Saldana",
          "cluster_id": 6239325,
          "cite": [
            "228 Cal. Rptr. 3d 1",
            "19 Cal. App. 5th 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(623144 OR 9485375 OR 9485376) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDc2NDAzMjAwMDAwJnM9NDMxMjM3MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28623144+OR+9485375+OR+9485376%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(623144 OR 9485375 OR 9485376)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNyZzPTQzMzEzNTkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28623144+OR+9485375+OR+9485376%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(623144 OR 9485375 OR 9485376)",
        "reviewed": 61,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 61,
        "triage_read": 0,
        "triage_snippet_classified": 61
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(623144 OR 9485375 OR 9485376)",
    "indexed_citing_opinions": 331,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 623144,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9485375,
        "count": 122,
        "count_source": "search"
      },
      {
        "opinion_id": 9485376,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 785,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/howes-v-fields.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNjY5OTkmcz0xMDMxMzM5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28623144+OR+9485375+OR+9485376%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 623144,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 117982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 134748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 145122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 173739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 275662,
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
    "date_created": "2026-07-05T07:30:59Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:31:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:31:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:37:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:31:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Howes v. Fields

```
(Slip Opinion)              OCTOBER TERM, 2011                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                    HOWES, WARDEN v. FIELDS

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

   No. 10–680.      Argued October 4, 2011—Decided February 21, 2012
Respondent Fields, a Michigan state prisoner, was escorted from his
  prison cell by a corrections officer to a conference room where he was
  questioned by two sheriff’s deputies about criminal activity he had al-
  legedly engaged in before coming to prison. At no time was Fields
  given Miranda warnings or advised that he did not have to speak
  with the deputies. As relevant here: Fields was questioned for be-
  tween five and seven hours; Fields was told more than once that he
  was free to leave and return to his cell; the deputies were armed, but
  Fields remained free of restraints; the conference room door was
  sometimes open and sometimes shut; several times during the inter-
  view Fields stated that he no longer wanted to talk to the deputies,
  but he did not ask to go back to his cell; after Fields confessed and
  the interview concluded, he had to wait an additional 20 minutes for
  an escort and returned to his cell well after the hour when he gener-
  ally retired.
    The trial court denied Fields’ motion to suppress his confession
  under Miranda v. Arizona, 384 U. S. 436, and he was convicted. The
  Michigan Court of Appeals affirmed, rejecting Fields’ contention that
  his statements should have been suppressed because he was subject-
  ed to custodial interrogation without a Miranda warning. The Unit-
  ed States District Court for the Eastern District of Michigan subse-
  quently granted Fields habeas relief under 28 U. S. C. §2254(d)(1).
  Affirming, the Sixth Circuit held that the interview was a custodial
  interrogation within the meaning of Miranda, reasoning that Mathis
  v. United States, 391 U. S. 1, “clearly established,” §2254(d)(1), that
  isolation from the general prison population, combined with question-
  ing about conduct occurring outside the prison, makes any such in-
  terrogation custodial per se.
2                         HOWES v. FIELDS

                                Syllabus

Held:
    1. This Court’s precedents do not clearly establish the categorical
 rule on which the Sixth Circuit relied. The Court has repeatedly de-
 clined to adopt any such rule. See, e.g., Illinois v. Perkins, 496 U. S.
 292. The Sixth Circuit misread Mathis, which simply held, as rele-
 vant here, that a prisoner who otherwise meets the requirements for
 Miranda custody is not taken outside the scope of Miranda because
 he was incarcerated for an unconnected offense. It did not hold that
 imprisonment alone constitutes Miranda custody. Nor does the
 statement in Maryland v. Shatzer, 559 U. S. ___, ___, that “[n]o one
 questions that [inmate] Shatzer was in custody for Miranda purpos-
 es” support a per se rule. It means only that the issue of custody was
 not contested in that case. Finally, contrary to respondent’s sugges-
 tion, Miranda itself did not hold that the inherently compelling pres-
 sures of custodial interrogation are always present when a prisoner is
 taken aside and questioned about events outside the prison walls.
 Pp. 4–7.
    2. The Sixth Circuit’s categorical rule—that imprisonment, ques-
 tioning in private, and questioning about events in the outside world
 create a custodial situation for Miranda purposes—is simply wrong.
 Pp. 8–13.
       (a) The initial step in determining whether a person is in Miran-
 da custody is to ascertain, given “all of the circumstances surround-
 ing the interrogation,” how a suspect would have gauged his freedom
 of movement. Stansbury v. California, 511 U. S. 318, 322, 325. How-
 ever, not all restraints on freedom of movement amount to Miranda
 custody. See, e.g., Berkemer v. McCarty, 468 U. S. 420, 423. Shatzer,
 distinguishing between restraints on freedom of movement and Mi-
 randa custody, held that a break in Miranda custody between a sus-
 pect’s invocation of the right to counsel and the initiation of subse-
 quent questioning may occur while a suspect is serving an
 uninterrupted term of imprisonment. If a break in custody can occur,
 it must follow that imprisonment alone is not enough to create a cus-
 todial situation within the meaning of Miranda. At least three strong
 grounds support this conclusion: Questioning a person who is already
 in prison does not generally involve the shock that very often accom-
 panies arrest; a prisoner is unlikely to be lured into speaking by a
 longing for prompt release; and a prisoner knows that his questioners
 probably lack authority to affect the duration of his sentence. Thus,
 service of a prison term, without more, is not enough to constitute
 Miranda custody. Pp. 8–12.
       (b) The other two elements in the Sixth Circuit’s rule are like-
 wise insufficient. Taking a prisoner aside for questioning may neces-
 sitate some additional limitations on the prisoner’s freedom of move-
                     Cite as: 565 U. S. ____ (2012)                     3

                                Syllabus

  ment, but it does not necessarily convert a noncustodial situation into
  Miranda custody. Isolation may contribute to a coercive atmosphere
  when a nonprisoner is questioned, but questioning a prisoner in pri-
  vate does not generally remove him from a supportive atmosphere
  and may be in his best interest. Neither does questioning a prisoner
  about criminal activity outside the prison have a significantly greater
  potential for coercion than questioning under otherwise identical cir-
  cumstances about criminal activity within the prison walls. The co-
  ercive pressure that Miranda guards against is neither mitigated nor
  magnified by the location of the conduct about which questions are
  asked. Pp. 12–13.
     3. When a prisoner is questioned, the determination of custody
  should focus on all of the features of the interrogation. The record in
  this case reveals that respondent was not taken into custody for Mi-
  randa purposes. While some of the facts lend support to his argu-
  ment that Miranda’s custody requirement was met, they are offset by
  others. Most important, he was told at the outset of the interroga-
  tion, and reminded thereafter, that he was free to leave and could go
  back to his cell whenever he wanted. Moreover, he was not physical-
  ly restrained or threatened, was interviewed in a well-lit, average-
  sized conference room where the door was sometimes left open, and
  was offered food and water. These facts are consistent with an envi-
  ronment in which a reasonable person would have felt free to termi-
  nate the interview and leave, subject to the ordinary restraints of life
  behind bars. Pp. 13–16.
617 F. 3d 813, reversed.

   ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SCALIA, KENNEDY, THOMAS, and KAGAN, JJ., joined. GINSBURG, J.,
filed an opinion concurring in part and dissenting in part, in which
BREYER and SOTOMAYOR, JJ., joined.
                        Cite as: 565 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–680
                                   _________________


CAROL HOWES, WARDEN, PETITIONER v. RANDALL
               LEE FIELDS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE SIXTH CIRCUIT

                              [February 21, 2012]


   JUSTICE ALITO delivered the opinion of the Court.
   The United States Court of Appeals for the Sixth Circuit
held that our precedents clearly establish that a prisoner
is in custody within the meaning of Miranda v. Arizona,
384 U. S. 436 (1966), if the prisoner is taken aside and
questioned about events that occurred outside the prison
walls. Our decisions, however, do not clearly establish
such a rule, and therefore the Court of Appeals erred in
holding that this rule provides a permissible basis for
federal habeas relief under the relevant provision of the
Antiterrorism and Effective Death Penalty Act of 1996
(AEDPA), 28 U. S. C. §2254(d)(1). Indeed, the rule ap-
plied by the court below does not represent a correct inter-
pretation of our Miranda case law. We therefore reverse.
                                          I
  While serving a sentence in a Michigan jail, Randall
Fields was escorted by a corrections officer to a conference
room where two sheriff’s deputies questioned him about
allegations that, before he came to prison, he had engaged
in sexual conduct with a 12-year-old boy. In order to get to
the conference room, Fields had to go down one floor and
2                         HOWES v. FIELDS

                          Opinion of the Court

pass through a locked door that separated two sections
of the facility. See App. to Pet. for Cert. 66a, 69a. Fields
arrived at the conference room between 7 p.m. and 9 p.m.1
and was questioned for between five and seven hours.2
  At the beginning of the interview, Fields was told that
he was free to leave and return to his cell. See id., at 70a.
Later, he was again told that he could leave whenever he
wanted. See id., at 90a. The two interviewing deputies
were armed during the interview, but Fields remained free
of handcuffs and other restraints. The door to the confer-
ence room was sometimes open and sometimes shut. See
id., at 70a–75a.
  About halfway through the interview, after Fields had
been confronted with the allegations of abuse, he became
agitated and began to yell. See id., at 80a, 125a. Fields
testified that one of the deputies, using an expletive, told
him to sit down and said that “if [he] didn’t want to coop-
erate, [he] could leave.” Id., at 89a; see also id., at 70a–
71a. Fields eventually confessed to engaging in sex acts
with the boy. According to Fields’ testimony at a suppres-
sion hearing, he said several times during the interview
that he no longer wanted to talk to the deputies, but he
did not ask to go back to his cell prior to the end of the
interview. See id., at 92a–93a.
  When he was eventually ready to leave, he had to wait
——————
  1 Fields testified that he left his cell around 8 p.m. and that the in-

terview began around 8:30 p.m. App. to Pet. for Cert. 77a. Both the
Michigan Court of Appeals and the Sixth Circuit stated that the inter-
view began between 7 p.m. and 9 p.m. See id., at 4a, 54a.
  2 The Court of Appeals stated that the interview lasted for approxi-

mately seven hours, see id., at 4a, a figure that appears to be based
on the testimony of one of the interviewing deputies, see id., at 123a.
Fields put the number of hours between five and five and a half, saying
the interview began around 8:30 p.m. and continued until 1:30 a.m. or 2
a.m. See id., at 77a. The Michigan Court of Appeals stated that the
interview ended around midnight, which would put the length of the
interview at between three and five hours.
                    Cite as: 565 U. S. ____ (2012)                  3

                        Opinion of the Court

an additional 20 minutes or so because a corrections of-
ficer had to be summoned to escort him back to his cell,
and he did not return to his cell until well after the hour
when he generally retired.3 At no time was Fields given
Miranda warnings or advised that he did not have to
speak with the deputies.
   The State of Michigan charged Fields with criminal
sexual conduct. Relying on Miranda, Fields moved to
suppress his confession, but the trial court denied his
motion. Over the renewed objection of defense counsel,
one of the interviewing deputies testified at trial about
Fields’ admissions. The jury convicted Fields of two
counts of third-degree criminal sexual conduct, and the
judge sentenced him to a term of 10 to 15 years of impris-
onment. On direct appeal, the Michigan Court of Appeals
affirmed, rejecting Fields’ contention that his statements
should have been suppressed because he was subjected to
custodial interrogation without a Miranda warning. The
court ruled that Fields had not been in custody for pur-
poses of Miranda during the interview, so no Miranda
warnings were required. The court emphasized that
Fields was told that he was free to leave and return to his
cell but that he never asked to do so. The Michigan Su-
preme Court denied discretionary review.
   Fields then filed a petition for a writ of habeas corpus in
Federal District Court, and the court granted relief. The
Sixth Circuit affirmed, holding that the interview in the
conference room was a “custodial interrogation” within
the meaning of Miranda because isolation from the general
prison population combined with questioning about con-
duct occurring outside the prison makes any such interro-
gation custodial per se. The Court of Appeals reasoned
that this Court clearly established in Mathis v. United
——————
  3 Fields testified that his normal bedtime was 10:30 p.m. or 11 p.m.

See id., at 78a.
4                     HOWES v. FIELDS

                     Opinion of the Court

States, 391 U. S. 1 (1968), that “Miranda warnings must
be administered when law enforcement officers remove an
inmate from the general prison population and interrogate
him regarding criminal conduct that took place outside the
jail or prison.” 617 F. 3d 813, 820 (CA6 2010); see also id.,
at 818 (“The central holding of Mathis is that a Miranda
warning is required whenever an incarcerated individual
is isolated from the general prison population and interro-
gated, i.e.[,] questioned in a manner likely to lead to self-
incrimination, about conduct occurring outside of the
prison”). Because Fields was isolated from the general
prison population and interrogated about conduct occur-
ring in the outside world, the Court of Appeals found that
the state court’s decision was contrary to clearly estab-
lished federal law as determined by this Court in Mathis.
617 F. 3d, at 823.
   We granted certiorari. 562 U. S. ___ (2011).
                              II
  Under AEDPA, a federal court may grant a state pris-
oner’s application for a writ of habeas corpus if the state-
court adjudication pursuant to which the prisoner is held
“resulted in a decision that was contrary to, or involved an
unreasonable application of, clearly established Federal
law, as determined by the Supreme Court of the United
States.” 28 U. S. C. §2254(d)(1). In this context, “clearly
established law” signifies “the holdings, as opposed to the
dicta, of this Court’s decisions.” Williams v. Taylor, 529
U. S. 362, 412 (2000).
  In this case, it is abundantly clear that our precedents
do not clearly establish the categorical rule on which the
Court of Appeals relied, i.e., that the questioning of a
prisoner is always custodial when the prisoner is removed
from the general prison population and questioned about
events that occurred outside the prison. On the contrary,
we have repeatedly declined to adopt any categorical rule
                 Cite as: 565 U. S. ____ (2012)           5

                     Opinion of the Court

with respect to whether the questioning of a prison inmate
is custodial.
   In Illinois v. Perkins, 496 U. S. 292 (1990), where we
upheld the admission of un-Mirandized statements elicit-
ed from an inmate by an undercover officer masquerading
as another inmate, we noted that “[t]he bare fact of cus-
tody may not in every instance require a warning even when
the suspect is aware that he is speaking to an official, but
we do not have occasion to explore that issue here.” Id., at
299 (emphasis added). Instead, we simply “reject[ed] the
argument that Miranda warnings are required whenever
a suspect is in custody in a technical sense and converses
with someone who happens to be a government agent.”
Id., at 297.
   Most recently, in Maryland v. Shatzer, 559 U. S. ___
(2010), we expressly declined to adopt a bright-line rule
for determining the applicability of Miranda in prisons.
Shatzer considered whether a break in custody ends the
presumption of involuntariness established in Edwards v.
Arizona, 451 U. S. 477 (1981), and, if so, whether a prison-
er’s return to the general prison population after a custo-
dial interrogation constitutes a break in Miranda custody.
See 559 U. S., at ___ (slip op., at 3–4). In considering the
latter question, we noted first that “[w]e have never decid-
ed whether incarceration constitutes custody for Miranda
purposes, and have indeed explicitly declined to address
the issue.” Id., at ___ (slip op., at 13) (citing Perkins,
supra, at 299; emphasis added). The answer to this ques-
tion, we noted, would “depen[d] upon whether [incar-
ceration] exerts the coercive pressure that Miranda was
designed to guard against—the ‘danger of coercion [that]
results from the interaction of custody and official inter-
rogation.’ ” 559 U. S., at ___ (slip op., at 13) (quoting
Perkins, supra, at 297).
   In concluding that our precedents establish a categorical
rule, the Court of Appeals placed great weight on the
6                         HOWES v. FIELDS

                          Opinion of the Court

decision in Mathis, but the Court of Appeals misread the
holding in that case. In Mathis, an inmate in a state
prison was questioned by an Internal Revenue agent and
was subsequently convicted for federal offenses. The
Court of Appeals held that Miranda did not apply to this
interview for two reasons: A criminal investigation had
not been commenced at the time of the interview, and
the prisoner was incarcerated for an “unconnected offense.”
Mathis v. United States, 376 F. 2d 595, 597 (CA5 1967).
This Court rejected both of those grounds for distinguish-
ing Miranda, 391 U. S., at 4, and thus the holding in
Mathis is simply that a prisoner who otherwise meets the
requirements for Miranda custody is not taken outside the
scope of Miranda by either of the two factors on which
the Court of Appeals had relied. Mathis did not hold
that imprisonment, in and of itself, is enough to constitute
Miranda custody.4 Nor, contrary to respondent’s submis-
sion, see Brief for Respondent 14, did Oregon v. Mathia-
son, 429 U. S. 492, 494 (1977) (per curiam), which simply
restated in dictum the holding in Mathis.
   The Court of Appeals purported to find support for its
per se rule in Shatzer, relying on our statement that “[n]o
one questions that Shatzer was in custody for Miranda
purposes” when he was interviewed. 559 U. S., at ___ (slip
op., at 13). But this statement means only that the issue
of custody was not contested before us. It strains credulity
to read the statement as constituting an “unambiguous
conclusion” or “finding” by this Court that Shatzer was in
custody. 617 F. 3d, at 822.
   Finally, contrary to respondent’s suggestion, see Brief
for Respondent 12–15, Miranda itself did not clearly es-

——————
    4 Indeed,
            it is impossible to tell from either the opinion of this Court
or that of the court below whether the prisoner’s interview was routine
or whether there were special features that may have created an
especially coercive atmosphere.
                     Cite as: 565 U. S. ____ (2012)                    7

                          Opinion of the Court

tablish the rule applied by the Court of Appeals. Miranda
adopted a “set of prophylactic measures” designed to ward
off the “ ‘inherently compelling pressures’ of custodial
interrogation,” Shatzer, supra, at ___ (slip op., at 4) (quot-
ing Miranda, 384 U. S., at 467), but Miranda did not hold
that such pressures are always present when a prisoner
is taken aside and questioned about events outside the
prison walls. Indeed, Miranda did not even establish that
police questioning of a suspect at the station house is
always custodial. See Mathiason, supra, at 495 (declining
to find that Miranda warnings are required “simply be-
cause the questioning takes place in the station house, or
because the questioned person is one whom the police
suspect”).
  In sum, our decisions do not clearly establish that a
prisoner is always in custody for purposes of Miranda
whenever a prisoner is isolated from the general prison
population and questioned about conduct outside the
prison.5
——————
   5 The state-court decision applied the traditional context-specific

analysis to determine whether the circumstances of respondent’s
interrogation gave rise to “the coercive pressure that Miranda was
designed to guard against.” Shatzer, 559 U. S., at ___ (slip op., at 13).
The court first observed: “That a defendant is in prison for an unrelated
offense when being questioned does not, without more, mean that he
was in custody for the purpose of determining whether Miranda warn-
ings were required.” App. to Pet. for Cert. 56a (internal quotation
marks omitted and emphasis added). In this case, the court noted, the
“defendant was unquestionably in custody, but on a matter unrelated to
the interrogation.” Ibid. The Sixth Circuit concluded that the state
court thereby limited Miranda in a way rejected by Mathis v. United
States, 391 U. S. 1 (1968), and “curtail[ed] the warnings to be given
persons under interrogation by officers based on the reason why the
person is in custody.” Id., at 4–5. We think the better reading is that
the state court merely meant to draw a distinction between incarcera-
tion and Miranda custody. This reading is supported by the state
court’s subsequent consideration of whether the facts of the case were
likely to create an atmosphere of coercion. App. to Pet. for Cert. 56a.
8                     HOWES v. FIELDS

                     Opinion of the Court 


                            III

  Not only does the categorical rule applied below go well
beyond anything that is clearly established in our prior
decisions, it is simply wrong. The three elements of that
rule—(1) imprisonment, (2) questioning in private, and (3)
questioning about events in the outside world—are not
necessarily enough to create a custodial situation for
Miranda purposes.
                             A
   As used in our Miranda case law, “custody” is a term of
art that specifies circumstances that are thought generally
to present a serious danger of coercion. In determining
whether a person is in custody in this sense, the initial
step is to ascertain whether, in light of “the objective cir-
cumstances of the interrogation,” Stansbury v. Califor-
nia, 511 U. S. 318, 322–323, 325 (1994) (per curiam), a
“reasonable person [would] have felt he or she was not at
liberty to terminate the interrogation and leave.” Thomp-
son v. Keohane, 516 U. S. 99, 112 (1995). And in order to
determine how a suspect would have “gauge[d]” his “free-
dom of movement,” courts must examine “all of the cir-
cumstances surrounding the interrogation.” Stansbury,
supra, at 322, 325 (internal quotation marks omitted).
Relevant factors include the location of the questioning,
see Shatzer, supra, at ___–___ (slip op., at 13–16), its
duration, see Berkemer v. McCarty, 468 U. S. 420, 437–438
(1984), statements made during the interview, see Mathi-
ason, supra, at 495; Yarborough v. Alvarado, 541 U. S.
652, 665 (2004); Stansbury, supra, at 325, the presence or
absence of physical restraints during the questioning, see
New York v. Quarles, 467 U. S. 649, 655 (1984), and the
release of the interviewee at the end of the questioning,
see California v. Beheler, 463 U. S. 1121, 1122–1123
(1983) (per curiam).
   Determining whether an individual’s freedom of move-
                  Cite as: 565 U. S. ____ (2012)             9

                      Opinion of the Court

ment was curtailed, however, is simply the first step in the
analysis, not the last. Not all restraints on freedom of
movement amount to custody for purposes of Miranda.
We have “decline[d] to accord talismanic power” to the
freedom-of-movement inquiry, Berkemer, supra, at 437,
and have instead asked the additional question whether
the relevant environment presents the same inherently
coercive pressures as the type of station house questioning
at issue in Miranda. “Our cases make clear . . . that the
freedom-of-movement test identifies only a necessary and
not a sufficient condition for Miranda custody.” Shatzer,
559 U. S., at ___ (slip op., at 14).
   This important point is illustrated by our decision in
Berkemer v. McCarty, supra. In that case, we held that
the roadside questioning of a motorist who was pulled over
in a routine traffic stop did not constitute custodial inter-
rogation. Id., at 423, 441–442. We acknowledged that “a
traffic stop significantly curtails the ‘freedom of action’ of
the driver and the passengers,” and that it is generally “a
crime either to ignore a policeman’s signal to stop one’s car
or, once having stopped, to drive away without permis-
sion.” Id., at 436. “[F]ew motorists,” we noted, “would feel
free either to disobey a directive to pull over or to leave the
scene of a traffic stop without being told they might do so.”
Ibid. Nevertheless, we held that a person detained as a
result of a traffic stop is not in Miranda custody because
such detention does not “sufficiently impair [the detained
person’s] free exercise of his privilege against self-
incrimination to require that he be warned of his consti-
tutional rights.” 468 U. S., at 437. As we later put it,
the “temporary and relatively nonthreatening detention in-
volved in a traffic stop or Terry stop does not constitute
Miranda custody,” Shatzer, supra, at ___ (slip op., at 14)
(citation omitted). See Terry v. Ohio, 392 U. S. 1 (1968).
   It may be thought that the situation in Berkemer—the
questioning of a motorist subjected to a brief traffic stop—
10                    HOWES v. FIELDS

                      Opinion of the Court

is worlds away from those present when an inmate is
questioned in a prison, but the same cannot be said of
Shatzer, where we again distinguished between restraints
on freedom of movement and Miranda custody. Shatzer,
as noted, concerned the Edwards prophylactic rule, which
limits the ability of the police to initiate further question-
ing of a suspect in Miranda custody once the suspect
invokes the right to counsel. We held in Shatzer that this
rule does not apply when there is a sufficient break in
custody between the suspect’s invocation of the right to
counsel and the initiation of subsequent questioning. See
559 U. S., at ___ (slip op., at 13-16). And, what is signifi-
cant for present purposes, we further held that a break
in custody may occur while a suspect is serving a term in
prison. If a break in custody can occur while a prisoner is
serving an uninterrupted term of imprisonment, it must
follow that imprisonment alone is not enough to create a
custodial situation within the meaning of Miranda.
   There are at least three strong grounds for this conclu-
sion. First, questioning a person who is already serving a
prison term does not generally involve the shock that very
often accompanies arrest. In the paradigmatic Miranda
situation—a person is arrested in his home or on the
street and whisked to a police station for questioning—
detention represents a sharp and ominous change, and the
shock may give rise to coercive pressures. A person who is
“cut off from his normal life and companions,” Shatzer,
supra, at ___ (slip op., at 7), and abruptly transported from
the street into a “police-dominated atmosphere,” Miranda,
384 U. S., at 456, may feel coerced into answering
questions.
   By contrast, when a person who is already serving a
term of imprisonment is questioned, there is usually no
such change. “Interrogated suspects who have previously
been convicted of crime live in prison.” Shatzer, 559 U. S.,
at ___ (slip op., at 14). For a person serving a term of
                  Cite as: 565 U. S. ____ (2012)           11

                      Opinion of the Court

incarceration, we reasoned in Shatzer, the ordinary re-
strictions of prison life, while no doubt unpleasant, are
expected and familiar and thus do not involve the same
“inherently compelling pressures” that are often present
when a suspect is yanked from familiar surroundings in
the outside world and subjected to interrogation in a police
station. Id., at ___ (slip op., at 4).
  Second, a prisoner, unlike a person who has not been
sentenced to a term of incarceration, is unlikely to be
lured into speaking by a longing for prompt release. When
a person is arrested and taken to a station house for inter-
rogation, the person who is questioned may be pressured
to speak by the hope that, after doing so, he will be al-
lowed to leave and go home. On the other hand, when a
prisoner is questioned, he knows that when the question-
ing ceases, he will remain under confinement. Id., at ___–
___, n. 8 (slip op., at 14–15, n. 8).
  Third, a prisoner, unlike a person who has not been
convicted and sentenced, knows that the law enforcement
officers who question him probably lack the authority to
affect the duration of his sentence. Id., at ___–___ (slip
op., at 14–15). And “where the possibility of parole exists,”
the interrogating officers probably also lack the power to
bring about an early release. Ibid. “When the suspect has
no reason to think that the listeners have official power
over him, it should not be assumed that his words are
motivated by the reaction he expects from his listeners.”
Perkins, 496 U. S., at 297. Under such circumstances,
there is little “basis for the assumption that a suspect . . .
will feel compelled to speak by the fear of reprisal for
remaining silent or in the hope of [a] more lenient treat-
ment should he confess.” Id., at 296–297.
  In short, standard conditions of confinement and associ-
ated restrictions on freedom will not necessarily implicate
the same interests that the Court sought to protect when
it afforded special safeguards to persons subjected to
12                    HOWES v. FIELDS

                     Opinion of the Court

custodial interrogation. Thus, service of a term of impris-
onment, without more, is not enough to constitute Miran-
da custody.
                               B
   The two other elements included in the Court of Ap-
peals’ rule—questioning in private and questioning about
events that took place outside the prison—are likewise
insufficient.
   Taking a prisoner aside for questioning—as opposed
to questioning the prisoner in the presence of fellow in-
mates—does not necessarily convert a “noncustodial situa-
tion . . . to one in which Miranda applies.” Mathiason, 429
U. S., at 495. When a person who is not serving a prison
term is questioned, isolation may contribute to a coercive
atmosphere by preventing family members, friends, and
others who may be sympathetic from providing either
advice or emotional support. And without any such assis-
tance, the person who is questioned may feel overwhelm-
ing pressure to speak and to refrain from asking that the
interview be terminated.
   By contrast, questioning a prisoner in private does not
generally remove the prisoner from a supportive atmos-
phere. Fellow inmates are by no means necessarily
friends. On the contrary, they may be hostile and, for a
variety of reasons, may react negatively to what the ques-
tioning reveals. In the present case, for example, would
respondent have felt more at ease if he had been ques-
tioned in the presence of other inmates about the sexual
abuse of an adolescent boy? Isolation from the general
prison population is often in the best interest of the inter-
viewee and, in any event, does not suggest on its own
the atmosphere of coercion that concerned the Court in
Miranda.
   It is true that taking a prisoner aside for questioning
may necessitate some additional limitations on his free-
                 Cite as: 565 U. S. ____ (2012)           13

                     Opinion of the Court

dom of movement. A prisoner may, for example, be re-
moved from an exercise yard and taken, under close
guard, to the room where the interview is to be held. But
such procedures are an ordinary and familiar attribute of
life behind bars. Escorts and special security precautions
may be standard procedures regardless of the purpose for
which an inmate is removed from his regular routine and
taken to a special location. For example, ordinary prison
procedure may require such measures when a prisoner is
led to a meeting with an attorney.
   Finally, we fail to see why questioning about criminal
activity outside the prison should be regarded as having a
significantly greater potential for coercion than question-
ing under otherwise identical circumstances about crimi-
nal activity within the prison walls. In both instances,
there is the potential for additional criminal liability and
punishment. If anything, the distinction would seem to
cut the other way, as an inmate who confesses to miscon-
duct that occurred within the prison may also incur ad-
ministrative penalties, but even this is not enough to tip
the scale in the direction of custody. “The threat to a
citizen’s Fifth Amendment rights that Miranda was de-
signed to neutralize” is neither mitigated nor magnified by
the location of the conduct about which questions are
asked. Berkemer, 468 U. S., at 435, n. 22.
   For these reasons, the Court of Appeals’ categorical rule
is unsound.
                             IV 

                              A

   When a prisoner is questioned, the determination of
custody should focus on all of the features of the interroga-
tion. These include the language that is used in summon-
ing the prisoner to the interview and the manner in which
the interrogation is conducted. See Yarborough, 541 U. S.,
at 665. An inmate who is removed from the general prison
14                    HOWES v. FIELDS

                      Opinion of the Court

population for questioning and is “thereafter . . . subjected
to treatment” in connection with the interrogation “that
renders him ‘in custody’ for practical purposes . . . will be
entitled to the full panoply of protections prescribed by
Miranda.” Berkemer, 468 U. S., at 440.
   “Fidelity to the doctrine announced in Miranda requires
that it be enforced strictly, but only in those types of situa-
tions in which the concerns that powered the decision are
implicated.” Id., at 437; see Shatzer, 559 U. S., at ___ (slip
op., at 9); Mathiason, supra, at 495. Confessions voluntar-
ily made by prisoners in other situations should not be
suppressed. “Voluntary confessions are not merely a
proper element in law enforcement, they are an unmiti-
gated good, essential to society’s compelling interest in
finding, convicting, and punishing those who violate the
law.” Shatzer, supra, at ___ (slip op., at 9) (internal quota-
tion marks and citations omitted).
                              B
   The record in this case reveals that respondent was not
taken into custody for purposes of Miranda. To be sure,
respondent did not invite the interview or consent to it in
advance, and he was not advised that he was free to de-
cline to speak with the deputies. The following facts also
lend some support to respondent’s argument that Miran-
da’s custody requirement was met: The interview lasted
for between five and seven hours in the evening and con-
tinued well past the hour when respondent generally went
to bed; the deputies who questioned respondent were
armed; and one of the deputies, according to respondent,
“[u]sed a very sharp tone,” App. to Pet. for Cert. 76a, and,
on one occasion, profanity, see id., at 77a.
   These circumstances, however, were offset by others.
Most important, respondent was told at the outset of the
interrogation, and was reminded again thereafter, that he
could leave and go back to his cell whenever he wanted.
                     Cite as: 565 U. S. ____ (2012)                  15

                         Opinion of the Court

See id., at 89a–90a (“I was told I could get up and leave
whenever I wanted”); id., at 70a–71a. Moreover, respond-
ent was not physically restrained or threatened and was
interviewed in a well-lit, average-sized conference room,
where he was “not uncomfortable.” Id., at 90a; see id., at
71a, 88a–89a. He was offered food and water, and the
door to the conference room was sometimes left open. See
id., at 70a, 74a. “All of these objective facts are consistent
with an interrogation environment in which a reasonable
person would have felt free to terminate the interview and
leave.” Yarborough, supra, at 664–665.
   Because he was in prison, respondent was not free to
leave the conference room by himself and to make his own
way through the facility to his cell. Instead, he was es-
corted to the conference room and, when he ultimately
decided to end the interview, he had to wait about 20
minutes for a corrections officer to arrive and escort him to
his cell. But he would have been subject to this same
restraint even if he had been taken to the conference room
for some reason other than police questioning; under no
circumstances could he have reasonably expected to be
able to roam free.6 And while respondent testified that he
——————
    6 Respondent did not testify to the contrary. The following colloquy

occurred at his Miranda hearing:
“Q. You’re not generally allowed to just roam around Lenawee County
Jail on your own, are you?
“A. No, I never have.
“Q. So wouldn’t it make sense to you, since you had that experience,
that in fact you would have been escorted just like you were escorted
. . . into this conference room?
“A. That makes common sense.
“Q. So when they said that you were free to leave and you get up—
could get up and go and all you had to do was tell them you wanted to
go, in your mind, did you understand that to mean that somebody
would come get you and take you back to your cell?
“A. But that doesn’t give me freedom to just get up and walk away.
“Q. I understand it doesn’t—
“A. So, no.
16                        HOWES v. FIELDS

                         Opinion of the Court

“was told . . . if I did not want to cooperate, I needed to go
back to my cell,” these words did not coerce cooperation by
threatening harsher conditions. App. to Pet. for Cert. 71a;
see id., at 89a (“I was told, if I didn’t want to cooperate,
I could leave”). Returning to his cell would merely have
returned him to his usual environment. See Shatzer,
supra, at ___ (slip op., at 14) (“Interrogated suspects who
have previously been convicted of crime live in prison.
When they are released back into the general prison popu-
lation, they return to their accustomed surroundings and
daily routine—they regain the degree of control they had
over their lives prior to the interrogation”).
  Taking into account all of the circumstances of the
questioning—including especially the undisputed fact that
respondent was told that he was free to end the question-
ing and to return to his cell—we hold that respondent was
not in custody within the meaning of Miranda.
                         *    *     * 

     The judgment of the Court of Appeals is

                                                             Reversed.

—————— 

“Q. The question is this, sir, not whether you had freedom to get up

and walk away, but did you understand that what that meant was that

a jailer would come get you and— 

“A. No— 

“Q. —take you back to your cell?

“A. I did not understand that. 

“Q. You didn’t? 

“A. No. 

“Q. Why not? That’s how you got there.

“A. Because I did not know if a jailer would take me back or if one of

those gentlemen would take me back. 

“Q. But you understood that, if you asked, one of them or a jailer would 

take you back to your cell? 

“A. I assumed that. 

“Q. And you believed that to be true?

“A. I assumed that.” App. to Pet. for Cert. 91a–92a.

                 Cite as: 565 U. S. ____ (2012)           1

                    Opinion of GINSBURG, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 10–680
                         _________________


CAROL HOWES, WARDEN, PETITIONER v. RANDALL
               LEE FIELDS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE SIXTH CIRCUIT

                     [February 21, 2012]


   JUSTICE GINSBURG, with whom JUSTICE BREYER and
JUSTICE SOTOMAYOR join, concurring in part and dissent-
ing in part.
   Given this Court’s controlling decisions on what counts
as “custody” for Miranda purposes, I agree that the law is
not “clearly established” in respondent Fields’s favor. See,
e.g., Maryland v. Shatzer, 559 U. S. ___, ___ (2010) (slip
op., at 13–16); Thompson v. Keohane, 516 U. S. 99, 112
(1995). But I disagree with the Court’s further determina-
tion that Fields was not in custody under Miranda. Were
the case here on direct review, I would vote to hold that
Miranda precludes the State’s introduction of Fields’s
confession as evidence against him.
   Miranda v. Arizona, 384 U. S. 436 (1966), reacted to
police interrogation tactics that eroded the Fifth Amend-
ment’s ban on compulsory self-incrimination. The opinion
did so by requiring interrogators to convey to suspects
the now-familiar warnings: The suspect is to be informed,
prior to interrogation, that he “has a right to remain si-
lent, that any statement he does make may be used as
evidence against him, and that he has a right to the pres-
ence of an attorney, either retained or appointed.” Id., at
444.
   Under what circumstances are Miranda warnings re-
quired? Miranda tells us “in all settings in which [a per-
2                     HOWES v. FIELDS

                    Opinion of GINSBURG, J.

son’s] freedom of action is curtailed in any significant
way.” Id., at 467. Given the reality that police interroga-
tors “trad[e] on the weakness of individuals,” i.e., their
“insecurity about [themselves] or [their] surroundings,”
id., at 455, the Court found the preinterrogation warnings
set out in the opinion “indispensable,” id., at 469. Those
warnings, the Court elaborated, are “an absolute prerequi-
site in overcoming the inherent pressures of the interroga-
tion atmosphere,” id., at 468; they “insure” that the sus-
pect is timely told of his Fifth Amendment privilege, and
his freedom to exercise it, id., at 469.
   Fields, serving time for disorderly conduct, was, of
course, “i[n] custody,” but not “for purposes of Miranda,”
the Court concludes. Ante, at 14. I would not train, as the
Court does, on the question whether there can be custody
within custody. Instead, I would ask, as Miranda put it,
whether Fields was subjected to “incommunicado interro-
gation . . . in a police-dominated atmosphere,” 384 U. S., at
445, whether he was placed, against his will, in an inher-
ently stressful situation, see id., at 468, and whether his
“freedom of action [was] curtailed in any significant way,”
id., at 467. Those should be the key questions, and to each
I would answer “Yes.”
   As the Court acknowledges, Fields did not invite or
consent to the interview. Ante, at 14. He was removed
from his cell in the evening, taken to a conference room in
the sheriff ’s quarters, and questioned by two armed depu-
ties long into the night and early morning. Ibid. He was
not told at the outset that he had the right to decline to
speak with the deputies. Ibid. Shut in with the armed
officers, Fields felt “trapped.” App. to Pet. for Cert. 71a.
Although told he could return to his cell if he did not want
to cooperate, id., at 71a–72a, Fields believed the deputies
“would not have allowed [him] to leave the room,” id., at
72a. And with good reason. More than once, “he told the
officers . . . he did not want to speak with them anymore.”
                   Cite as: 565 U. S. ____ (2012)                 3

                      Opinion of GINSBURG, J.

617 F. 3d 813, 815 (CA6 2010). He was given water, App.
to Pet. for Cert. 74a, but not his evening medications,
id., at 79a.* Yet the Court concludes that Fields was in
“an interrogation environment in which a reasonable person
would have felt free to terminate the interview and leave.”
Ante, at 15 (quoting Yarborough v. Alvarado, 541 U. S.
652, 665 (2004)).
  Critical to the Court’s judgment is “the undisputed fact
that [Fields] was told that he was free to end the question-
ing and to return to his cell.” Ante, at 17. Never mind
the facts suggesting that Fields’s submission to the over-
night interview was anything but voluntary. Was Fields
“held for interrogation”? See Miranda, 384 U. S., at 471.
Brought to, and left alone with, the gun-bearing deputies,
he surely was in my judgment.
  Miranda instructed that such a person “must be clearly
informed that he has the right to consult with a lawyer
and to have the lawyer with him during interrogation.”
Ibid. Those warnings, along with “warnings of the right
to remain silent and that anything stated can be used in
evidence against [the speaker],” Miranda explained, are
necessary “prerequisite[s] to [an] interrogation” compati-
ble with the Fifth Amendment. Ibid. Today, for people
already in prison, the Court finds it adequate for the police
to say: “You are free to terminate this interrogation and
return to your cell.” Such a statement is no substitute for
one ensuring that an individual is aware of his rights.
  For the reasons stated, I would hold that the “incommu-
nicado interrogation [of Fields] in a police-dominated
atmosphere,” id., at 445, without informing him of his
rights, dishonored the Fifth Amendment privilege Miran-
da was designed to safeguard.
——————
  * Each night, Fields took an antidepressant and, due to his kidney
transplant surgery, two antirejection medications. App. to Pet. for
Cert. 79a.

```

---
