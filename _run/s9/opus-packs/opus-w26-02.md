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

## GROUP: content/cases/Arizona v. Mauro.md  (`case`, 5 assertions)

### content_page

```
---
title: "Arizona v. Mauro"
type: case
citation: "481 U.S. 520 (1987)"
parallel_cite: "107 S. Ct. 1931; 95 L. Ed. 2d 458"
neutral_cite: 1987 U.S. LEXIS 1933
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-06-26
docket: 85-2121
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Mauro
  varies_by_point: false
  scope_note: "Good law; allowing a suspect who has invoked Miranda to speak with his spouse in an officer's presence (recorded) is not interrogation or its functional equivalent under Innis."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111878/arizona-v-mauro/"
  cluster_id: 111878
  opinion_id: 9430952
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rhode Island v. Innis]]", "[[Miranda v. Arizona]]", "[[Edwards v. Arizona]]", "[[Oregon v. Elstad]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "interrogation", "functional-equivalent", "custodial-interrogation"]
holding: "Allowing a suspect who has invoked his Miranda rights to speak with his wife, with a police officer present and a recorder running, is not 'interrogation' or its functional equivalent; officers do not interrogate a suspect merely by hoping he will incriminate himself, so the resulting volunteered statements are admissible."
lake:
  record_id: Arizona v. Mauro
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Mauro

*481 U.S. 520 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Mauro was arrested after admitting he had killed his son. After receiving [[Miranda and Custodial Interrogation|Miranda warnings]] he invoked his right to counsel, and questioning stopped. His wife, who was being questioned in another room, insisted on speaking with him. Officers tried to discourage her but relented, requiring that a detective be present and that a tape recorder be running in plain view. During the conversation Mauro made incriminating statements, which the prosecution later used to rebut his insanity defense. The Arizona Supreme Court held that allowing the spousal meeting was the functional equivalent of interrogation under [[Rhode Island v. Innis]].

## Issue
Whether permitting a suspect who has invoked his [[Miranda and Custodial Interrogation|Miranda rights]] to speak with his spouse, in the presence of an officer with a recorder, constitutes interrogation or its functional equivalent.

## Rule
No. "We think it is clear under both *Miranda* and *Innis* that Mauro was not interrogated. . . . There is no evidence that the officers sent Mrs. Mauro in to see her husband for the purpose of eliciting incriminating statements." — 481 U.S. at 527–528. ^pin-528

Merely creating an opportunity is not interrogation: "Officers do not interrogate a suspect simply by hoping that he will incriminate himself." — [*Id.* at 529](https://www.courtlistener.com/opinion/111878/arizona-v-mauro/#:~:text=Officers%20do%20not%20interrogate%20a). ^pin-529

Because "Mauro was not subjected to compelling influences, psychological ploys, or direct questioning[,] . . . his volunteered statements cannot properly be considered the result of police interrogation." — *Id.*

## Application
The tape showed the detective asked Mauro no questions about the crime, and nothing suggested the officers used the meeting as a psychological ploy — they had discouraged the wife and "yielded to her insistent demands," and the officer's presence served legitimate, security-related reasons. Viewed from Mauro's perspective, a suspect told his wife may speak with him would not feel coerced to incriminate himself. The conduct was "far less questionable than the 'subtle compulsion'" held not to be interrogation in *[[Rhode Island v. Innis|Innis]]*, and did not implicate Miranda's purpose of preventing the coercive use of confinement to extract confessions. The officers therefore "acted reasonably and lawfully," and the Constitution did not bar the statements.

## Conclusion
Mauro was not interrogated; his statements to his wife were admissible. The judgment of the Arizona Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mauro* applies the functional-equivalent-of-interrogation test of [[Rhode Island v. Innis]] (the "words or actions . . . reasonably likely to elicit an incriminating response" standard) within the [[Miranda v. Arizona]] / [[Edwards v. Arizona]] framework, and reflects the volunteered-statements principle echoed in [[Oregon v. Elstad]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Mauro*, 481 U.S. 520 (1987) — https://www.courtlistener.com/opinion/111878/arizona-v-mauro/ — pinpoints: 527–530.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8acf6da5f6037565", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "481 U.S. 520 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 1933", "official_citation_present": true, "parallel_cite": "107 S. Ct. 1931; 95 L. Ed. 2d 458", "title": "Arizona v. Mauro", "year": "1987"}}
{"assertion_id": "5a05ca33d48a36c1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Allowing a suspect who has invoked his Miranda rights to speak with his wife, with a police officer present and a recorder running, is not 'interrogation' or its functional equivalent; officers do not interrogate a suspect merely by hoping he will incriminate himself, so the resulting volunteered statements are admissible.", "title": "Arizona v. Mauro"}}
{"assertion_id": "6dc5c596ac92d02a", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Arizona v. Mauro"}}
{"assertion_id": "1b787123d68e11b9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-06-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arizona v. Mauro", "field_i_validity": "good_law", "scope_note": "Good law; allowing a suspect who has invoked Miranda to speak with his spouse in an officer's presence (recorded) is not interrogation or its functional equivalent under Innis.", "title": "Arizona v. Mauro", "varies_by_point": "false"}}
{"assertion_id": "8837e8ba7dfd0609", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Mauro"}}
```

### lake record — Arizona v. Mauro

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Mauro",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Mauro",
    "case_name_short": "Mauro",
    "case_name_full": "Arizona v. Mauro",
    "input_case_name": "Arizona v. Mauro",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-06-26",
    "year": 1987,
    "docket": "85-2121",
    "cluster_id": 111878,
    "lead_opinion_id": 9430952,
    "sibling_ids": [
      111878,
      9430952,
      9430953
    ],
    "absolute_url": "/opinion/111878/arizona-v-mauro/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9070020,
        "score": 10,
        "case_name": "Arizona v. Mauro"
      },
      {
        "cluster_id": 9070019,
        "score": 10,
        "case_name": "Arizona v. Mauro"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "481 U.S. 520",
      "volume": "481",
      "reporter": "U.S.",
      "page": "520",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1931",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1931",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 L. Ed. 2d 458",
        "volume": "95",
        "reporter": "L. Ed. 2d",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1933",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1933",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "481 U.S. 520",
        "volume": "481",
        "reporter": "U.S.",
        "page": "520",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1931",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1931",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 L. Ed. 2d 458",
        "volume": "95",
        "reporter": "L. Ed. 2d",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1933",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1933",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "481 U.S. 520",
    "official_selection": {
      "court_class": "scotus",
      "selected": "481 U.S. 520",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-528",
      "page": null,
      "quote": "--- # Arizona v. Mauro *481 U.S. 520 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mauro was arrested after admitting he had killed his son. After receiving Miranda warnings he invoked his right to counsel, and questioning stopped. His wife, who was being questioned in another room, insisted on speaking with him. Officers tried to discourage her but relented, requiring that a detective be present and that a tape recorder be running in plain view. During the conversation Mauro made incriminating statements, which the prosecution later used to rebut his insanity defense. The Arizona Supreme Court held that allowing the spousal meeting was the functional equivalent of interrogation under [[Rhode Island v. Innis]]. ## Issue Whether permitting a suspect who has invoked his Miranda rights to speak with his spouse, in the presence of an officer with a recorder, constitutes interrogation or its functional equivalent. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-529",
      "page": null,
      "quote": "Officers do not interrogate a suspect simply by hoping that he will incriminate himself.",
      "star_marker": "529",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 18639,
      "fragment": "#:~:text=Officers%20do%20not%20interrogate%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Mauro",
    "varies_by_point": false,
    "scope_note": "Good law; allowing a suspect who has invoked Miranda to speak with his spouse in an officer's presence (recorded) is not interrogation or its functional equivalent under Innis.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Colon",
          "cluster_id": 4671866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Broom a/k/a Patrick Brown v. United States",
          "cluster_id": 2809687,
          "cite": [
            "118 A.3d 207",
            "2015 D.C. App. LEXIS 265",
            "2015 WL 3768885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Quarles",
          "cluster_id": 1057961,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
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
        "journal_ref": "Arizona v. Mauro:lane1_negative"
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
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julian Galindo-Gallegos, AKA Jose Reyes-Olague, AKA Aurelio Garcia-Chairez, AKA Jose Olague Reyes",
          "cluster_id": 772608,
          "cite": [
            "244 F.3d 728",
            "2001 Daily Journal DAR 3047",
            "2001 U.S. App. LEXIS 4891",
            "2001 WL 289956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Linton",
          "cluster_id": 944931,
          "cite": [
            "56 Cal. 4th 1146",
            "302 P.3d 927",
            "158 Cal. Rptr. 3d 521",
            "2013 WL 3214690",
            "2013 Cal. LEXIS 5338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
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
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
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
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ray",
          "cluster_id": 1130099,
          "cite": [
            "13 Cal. 4th 313",
            "914 P.2d 846",
            "96 Daily Journal DAR 5231",
            "52 Cal. Rptr. 2d 296",
            "96 Cal. Daily Op. Serv. 3222",
            "1996 Cal. LEXIS 1906"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
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
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
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
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Woodward v. State",
          "cluster_id": 1611371,
          "cite": [
            "533 So. 2d 418",
            "1988 WL 28413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 1121458,
          "cite": [
            "857 P.2d 1099",
            "5 Cal. 4th 950",
            "22 Cal. Rptr. 2d 689",
            "93 Daily Journal DAR 11122",
            "93 Cal. Daily Op. Serv. 6528",
            "1993 Cal. LEXIS 4179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Medina",
          "cluster_id": 2610902,
          "cite": [
            "799 P.2d 1282",
            "51 Cal. 3d 870",
            "274 Cal. Rptr. 849",
            "90 Cal. Daily Op. Serv. 8358",
            "1990 Cal. LEXIS 5054"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Enraca",
          "cluster_id": 844219,
          "cite": [
            "269 P.3d 543",
            "53 Cal. 4th 735",
            "137 Cal. Rptr. 3d 117",
            "2012 WL 360555",
            "2012 Cal. LEXIS 1078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gallego",
          "cluster_id": 1351145,
          "cite": [
            "802 P.2d 169",
            "52 Cal. 3d 115",
            "276 Cal. Rptr. 679",
            "90 Daily Journal DAR 14576",
            "90 Cal. Daily Op. Serv. 9269",
            "1990 Cal. LEXIS 5484"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis Rosa Collazo v. Wayne Estelle, Warden, California Mens Colony",
          "cluster_id": 565270,
          "cite": [
            "940 F.2d 411",
            "91 Daily Journal DAR 8681",
            "91 Cal. Daily Op. Serv. 5640",
            "1991 U.S. App. LEXIS 15265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dement",
          "cluster_id": 844239,
          "cite": [
            "264 P.3d 292",
            "53 Cal. 4th 1",
            "133 Cal. Rptr. 3d 496",
            "2011 Cal. LEXIS 12151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
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
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jessie Dotson",
          "cluster_id": 2738561,
          "cite": [
            "450 S.W.3d 1",
            "2014 Tenn. LEXIS 694"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Doll",
          "cluster_id": 5642287,
          "cite": [
            "21 N.Y.3d 665",
            "998 N.E.2d 384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jaturun Siripongs v. Arthur Calderon, Warden",
          "cluster_id": 678556,
          "cite": [
            "35 F.3d 1308"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Commonwealth",
          "cluster_id": 1420585,
          "cite": [
            "423 S.E.2d 360",
            "244 Va. 445",
            "9 Va. Law Rep. 480",
            "1992 Va. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 4326929,
          "cite": [
            "2016 Ohio 7983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Copeland",
          "cluster_id": 1678832,
          "cite": [
            "530 So. 2d 526",
            "1988 WL 31771"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Snow v. State",
          "cluster_id": 1695079,
          "cite": [
            "800 So. 2d 472",
            "2001 WL 1137390"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adkins v. Commonwealth",
          "cluster_id": 1377595,
          "cite": [
            "96 S.W.3d 779",
            "2003 Ky. LEXIS 13",
            "2003 WL 367054"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold S. Alston v. Walter Redman, Warden Charles M. Oberly, Iii, Attorney General of the State of Delaware and the State of Delaware",
          "cluster_id": 677798,
          "cite": [
            "34 F.3d 1237",
            "1994 U.S. App. LEXIS 24171",
            "1994 WL 480728"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111878 OR 9430952 OR 9430953) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OTY5Mzc2MDAwMDAmcz0xMzQ5MzM1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111878+OR+9430952+OR+9430953%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(111878 OR 9430952 OR 9430953)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OSZzPTQ5ODA0NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111878+OR+9430952+OR+9430953%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111878 OR 9430952 OR 9430953)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111878 OR 9430952 OR 9430953)",
    "indexed_citing_opinions": 268,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111878,
        "count": 230,
        "count_source": "search"
      },
      {
        "opinion_id": 9430952,
        "count": 43,
        "count_source": "search"
      },
      {
        "opinion_id": 9430953,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 419,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-mauro.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY1MjI0NDcmcz00Njc1NDk4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111878+OR+9430952+OR+9430953%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111878,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 111796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 111798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 1160581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 1169190,
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
    "date_created": "2026-07-04T18:35:04Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:35:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:35:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:40:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:35:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Mauro

```
<opinion type="majority">
<author id="b581-9">Justice Powell</author>
<p id="A30">delivered the opinion of the Court.</p>
<p id="b581-10">While respondent in this case was in police custody, he indicated that he did not wish to answer any questions until a lawyer was present. The issue presented is whether, in the circumstances of this case, officers interrogated respondent in violation of the Fifth and Fourteenth Amendments when they allowed him to speak with his wife in the presence of a police officer.</p>
<p id="b581-11">I</p>
<p id="b581-12">On November 23, 1982, the Flagstaff Police Department received a telephone call from a local K mart store. The caller stated that a man had entered the store claiming to have killed his son. When officers reached the store, respondent Mauro freely admitted that he had killed his son. He directed the officers to the child’s body, and then was arrested and advised of his constitutional rights pursuant to <page-number citation-index="1" label="522">*522</page-number><em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The officers then took Mauro to the pólice station, where he was advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights again. At that point, Mauro told the officers that he did not wish to make any more statements without having a lawyer present. All questioning then ceased. As no secure detention area was available, Mauro was held in the office of the police captain.</p>
<p id="b582-5">At the same time, one of the officers, Detective Manson, was questioning Mauro’s wife in another room. After she finished speaking with Manson, Mrs. Mauro asked if she could speak to her husband. Manson was reluctant to allow the meeting, but after Mrs. Mauro insisted, he discussed the request with his supervisor, Sergeant Allen. Allen testified that he “saw no harm in it and suggested to [Manson] that if she really sincerely wanted to talk to him to go ahead and allow it.” App. 74. Allen instructed Manson not to leave Mr. and Mrs. Mauro alone and suggested that Manson tape-record the conversation.</p>
<p id="b582-6">Manson then “told both Mr. and Mrs. Mauro that they could speak together only if an officer were present in the room to observe and hear what was going on.” <em>Id., </em>at 218 (findings of trial court). He brought Mrs. Mauro into the room and seated himself at a desk, placing a tape recorder in plain sight on the desk. He recorded their brief conversation, in which she expressed despair about their situation. During the conversation, Mauro told his wife not to answer questions until a lawyer was present.<footnotemark>1</footnotemark></p>
<p id="b583-4"><page-number citation-index="1" label="523">*523</page-number>Mauro’s defense at trial was that he had been insane at the time of the crime. In rebuttal, the prosecution played the tape of the meeting between Mauro and his wife, arguing that it demonstrated that Mauro was sane on the day of the murder. Mauro sought suppression of the recording on the ground that it was a product of police interrogation in violation of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The trial court refused to suppress the recording. First, it explained the basis of the officers’ decision to allow Mrs. Mauro to meet with her husband in the presence of a policeman:</p>
<blockquote id="b583-5">“The police counseled [Mrs. Mauro] not to [speak with her husband], but she was adamant about that. They finally yielded to her insistent demands. The Police Station lacked a secure interview room. The police justifiably appeared <em>[sic] </em>for Mrs. Mauro’s . . . safety, and they were also concerned about security, both in terms of whether Mr. and Mrs. Mauro might cook up a lie or <page-number citation-index="1" label="524">*524</page-number>swap statements with each other that shouldn’t have been allowed, and whether some escape attempt might have been made, or whether there might have been an attempt to smuggle in a weapon. They really had no idea what to expect along those lines.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></blockquote>
<p id="b584-5">In light of these justifications, the trial court found “that this procedure was not a ruse, nor a subterfuge by the police. They did not create this situation <em>[i. e., </em>allowing the meeting] as an indirect means of avoiding the dictates of Miranda.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>Accordingly, the trial court admitted the evidence. Mauro was convicted of murder and child abuse, and sentenced to death.</p>
<p id="b584-6">The Arizona Supreme Court reversed. <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/" aria-description="Citation for case: State v. Mauro">149 Ariz. 24</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/" aria-description="Citation for case: State v. Mauro">716 P. 2d 393</a></span> (1986). It found that by allowing Mauro to speak with his wife in the presence of a police officer, the detectives interrogated Mauro within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>This interrogation was impermissible, the court said, because Mauro previously had invoked the right to have counsel present before being questioned further. The court noted that both detectives had acknowledged in pretrial hearings that they knew it was “possible” that Mauro might make incriminating statements if he saw his wife.<footnotemark>2</footnotemark> The court relied <page-number citation-index="1" label="525">*525</page-number>on our statement in <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980), that interrogation includes a “practice that the police should know is reasonably likely to evoke an incriminating response from a suspect,” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><em>id., </em>at 301</a></span>. The court then concluded that the officers’ testimony demonstrated that there had been interrogation, because “[t]hey both knew that if the conversation took place, incriminating statements were likely to be made.” <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#31" aria-description="Citation for case: State v. Mauro">149 Ariz., at 31</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#400" aria-description="Citation for case: State v. Mauro">716 P. 2d, at 400</a></span>. Therefore, it held that the tape recording was not properly admitted at Mauro’s trial.</p>
<p id="AeK">Arizona filed a petition for a writ of certiorari. Because the decision below appeared to misconstrue our decision in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra,</a></span> </em>we granted the petition, <span class="citation multiple-matches"><a href="/c/U.%20S./479/811/">479 U. S. 811</a></span> (1986). We now reverse.</p>
<p id="AFJX">HH 1 — 1</p>
<p id="Abe">We begin by summarizing the relevant legal principles. The Fifth Amendment provides that no “person . . . shall be compelled in any criminal case to be a witness against himself.”<footnotemark>3</footnotemark> In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court concluded that “without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. ” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 467</a></span>. “Accordingly, the Court formulated the now-familiar ‘procedural safeguards effective to secure the privilege against self-incrimination.’” <em>Colorado </em>v. <em>Spring, </em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/#572" aria-description="Citation for case: Colorado v. Spring">479 U. S. 564, 572</a></span> (1987) (quoting <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 444</a></span>). Among these is the rule that when an accused has “expressed his desire to deal with the police only through counsel, [he] is not subject to further interrogation by the authori<page-number citation-index="1" label="526">*526</page-number>ties until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 484-485</a></span> (1981).</p>
<p id="b586-5">One of the questions frequently presented in cases in this area is whether particular police conduct constitutes “interrogation.” In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the Court suggested in one passage that “interrogation” referred only to actual “questioning initiated by law enforcement officers.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. But this statement was clarified in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra.</a></span> </em>In that case, the Court reviewed the police practices that had evoked the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court’s concern about the coerciveness of the “‘interrogation environment.’” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 299</a></span> (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 457</a></span>). The questioned practices included “the use of lineups in which a coached witness would pick the defendant as the perpetrator . . .[,] the so-called ‘reverse line-up’ in which a defendant would be identified by coached witnesses as the perpetrator of a fictitious crime,” and a variety of “psychological ploys, such as to ‘posi[t]’ ‘the guilt of the subject,’ to ‘minimize the moral seriousness of the offense,’ and ‘to cast blame on the victim or on society.’” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 299</a></span> (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#450" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 450</a></span>) (brackets by <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span> </em>Court). None of these techniques involves express questioning, and yet the Court found that any of them, coupled with the “interrogation environment,” was likely to “‘subjugate the individual to the will of his examiner’ and thereby undermine the privilege against compulsory self-incrimination.” 466 U. S., at 399 (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 457</a></span>). Thus, the <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span> </em>Court concluded that the goals of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>safeguards could be effectuated if those safeguards extended not only to express questioning, but also to “its functional equivalent.” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span>. The Court explained the phrase “functional equivalent” of interrogation as including “any words or actions on the part of the police (other than those normally attendant to arrest and custody) that the police should know are reasonably likely to elicit an <page-number citation-index="1" label="527">*527</page-number>incriminating response from the suspect.” <em>Ibid, </em>(footnotes omitted). Finally, it noted that “[t]he latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police.” <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Ibid.</a></span></em></p>
<p id="AW2">1 — 1 <em>I </em>— I hH</p>
<p id="Aeal">We now turn to the case before us. The officers gave Mauro the warnings required by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Mauro indicated that he did not wish to be questioned further without a lawyer present. Mauro never waived his right to have a lawyer present. The sole issue, then, is whether the officers’ subsequent actions rose to the level of interrogation — that is, in the language of <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>, </em>whether they were the “functional equivalent” of police interrogation. We think it is clear under both <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span> </em>that Mauro was not interrogated. The tape recording of the conversation between Mauro and his wife shows that Detective Manson asked Mauro no questions about the crime or his conduct.<footnotemark>4</footnotemark> Nor is it suggested — or supported by any evidence — that Sergeant Allen’s decision to allow Mauro’s wife to see him was the kind of psychological ploy that properly could be treated as the functional equivalent of interrogation.<footnotemark>5</footnotemark></p>
<p id="b588-4"><page-number citation-index="1" label="528">*528</page-number>There is no evidence that the officers sent Mrs. Mauro in to see her husband for the purpose of eliciting incriminating statements. As the trial court found, the officers tried to discourage her from talking to her husband, but finally “yielded to her insistent demands,” App. 218. Nor was Detective Manson’s presence improper. His testimony, that the trial court found credible, indicated a number of legitimate reasons — not related to securing incriminating statements — for having a police officer present. See <em>supra, </em>at 523-524 (quoting App. 218). Finally, the weakness of Mauro’s claim that he was interrogated is underscored by examining the situation from his perspective. Cf. <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span> (suggesting that the suspect’s perspective may be relevant in some cases in determining whether police actions constitute interrogation). We doubt that a suspect, told by officers that his wife will be allowed to speak to him, would feel that he was being coerced to incriminate himself in any way.</p>
<p id="b588-5">The Arizona Supreme Court was correct to note that there was a “possibility” that Mauro would incriminate himself while talking to his wife. It also emphasized that the officers were aware of that possibility when they agreéd to allow the Mauros to talk to each other.<footnotemark>6</footnotemark> But the actions in this case <page-number citation-index="1" label="529">*529</page-number>were far less questionable than the “subtle compulsion” that we held <em>not </em>to be interrogation in <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>. </em>See <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#303" aria-description="Citation for case: Rhode Island v. Innis"><em>id., </em>at 303</a></span>. Officers do not interrogate a suspect simply by hoping that he will incriminate himself. In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>and again in <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>, </em>the Court emphasized:</p>
<blockquote id="b589-5">“Confessions remain a proper element in law enforcement. Any statement given freely and voluntarily without any compelling influences is, of course, admissible in evidence. The fundamental import of the privilege while an individual is in custody is not whether he is allowed to talk to the police without the benefit of warnings and counsel, but whether he can be interrogated. . . . Volunteered statements of any kind are not barred by the Fifth Amendment and their admissibility is not affected by our holding today.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>, quoted in <em>Rhode Island </em>v. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#299" aria-description="Citation for case: Rhode Island v. Innis"><em>Innis, supra, </em>at 299-300</a></span>.</blockquote>
<p id="b589-7">See <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#305" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 305</a></span> (1985). (“‘[F]ar from being prohibited by the Constitution, admissions of guilt by wrongdoers, if not coerced, are inherently desirable’” (quoting <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977))). Mauro was not subjected to compelling influences, psychological ploys, or direct questioning. Thus, his volunteered statements cannot properly be considered the result of police interrogation.</p>
<p id="b589-9">In deciding whether particular police conduct is interrogation, we must remember the purpose behind our decisions in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>: </em>preventing government officials from <page-number citation-index="1" label="530">*530</page-number>using the coercive nature of confinement to extract confessions that would not be given in an unrestrained environment. The government actions in this case do not implicate this purpose in any way. Police departments need not adopt inflexible rules barring suspects from speaking with their spouses, nor must they ignore legitimate security concerns by allowing spouses to meet in private. In short, the officers in this case acted reasonably and lawfully by allowing Mrs. Mauro to speak with her husband. In this situation, the Federal Constitution does not forbid use of Mauro’s subsequent statements at his criminal trial.</p>
<p id="A4x">I — I &lt;!</p>
<p id="A_p">The judgment of the Arizona Supreme Court is reversed. The case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b590-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b582-7"> The entire conversation proceeded as follows:</p>
<p id="b582-8">“MRS. MAURO: Please — please, I don’t know what to do. We should have put David [the victim] in the hospital. Please — I don’t know what we’re going to do. We should have went for help — we should have went for help.</p>
<p id="b582-9">“[MR. MAURO]: You tried as best you could to stop it.</p>
<p id="b582-10">“MRS. MAURO: I-</p>
<p id="b582-11">“[MR. MAURO]: Shut up.</p>
<p id="b582-12">“MRS. MAURO: —taken him to a mental hospital or something. What’ll we do?</p>
<p id="Aqd"><page-number citation-index="1" label="523">*523</page-number>“[MR. MAURO]: Shut up.</p>
<p id="A1c">“DET. MANSON: Do you know a reverend or a priest or someone you can talk to — take care of David?</p>
<p id="AWq">“MRS. MAURO: No.</p>
<p id="AQX">“[MR. MAURO]: Don’t answer questions until you get rights of attorney before you find out whats <em>[sic] </em>going on. You tried to stop me as best you can. What are you going to do, kill me? You tried the best you can to stop me.</p>
<p id="AyE">“MRS. MAURO: I don’t — we don’t — I don’t have money.</p>
<p id="A57">“[MR. MAURO]: There’s a public attorney.</p>
<p id="Aq_">“MRS. MAURO: I don’t know.</p>
<p id="AB0">“[MR. MAURO]: There’s a public attorney. Why don’t you just be quiet.</p>
<p id="AnT">“MRS. MAURO: I don’t have any money to bury him. I don’t have any money. All I got is enough money for the rent for the children and that’s it.</p>
<p id="Ahfh">“DET. MANSON: Did you want to talk to your husband any more?</p>
<p id="AFZ">“MRS. MAURO: No, I can’t talk to him.</p>
<p id="AUR">“[MR. MAURO]: Then don’t talk to me — get out.</p>
<p id="A4Y">“MRS. MAURO: I don’t know what to do. O.K.”</p>
<p id="A-O"><span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#30" aria-description="Citation for case: State v. Mauro">149 Ariz. 24, 30-31</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#399" aria-description="Citation for case: State v. Mauro">716 P. 2d 393, 399-400</a></span> (1986).</p>
</footnote>
<footnote label="2">
<p id="b584-7"> The court relied on testimony of the officers at the hearing in the trial court on the suppression motion. Sergeant Allen testified as follows:</p>
<p id="b584-8">“Q. [C]ertainly when you sent an officer in there to listen to that conversation, you knew that it was possible that he might make incriminating statements?</p>
<p id="b584-9"><em>“A. </em>That’s correct.</p>
<p id="b584-10">“Q. And obviously, you wanted to record that conversation so as to have a record of those incriminating statements.</p>
<p id="b584-11">“A. That’s correct.” <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#30" aria-description="Citation for case: State v. Mauro"><em>Id., </em>at 30</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#399" aria-description="Citation for case: State v. Mauro">716 P. 2d, at 399</a></span>. Detective Manson’s testimony was as follows:</p>
<p id="b584-13">“Q. [Detective Manson], certainly you were aware that during the conversation either [Mrs. Mauro] or my client may have given an incriminating statement?</p>
<p id="b584-14">“A. Yes.</p>
<p id="b584-15">“Q. And obviously one of the purposes of your tape recording the interview was to take down any such statements?</p>
<p id="A4dC"><page-number citation-index="1" label="525">*525</page-number>“A. Yes, sir.” <em><span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/" aria-description="Citation for case: State v. Mauro">Ibid.</a></span></em></p>
</footnote>
<footnote label="3">
<p id="b585-5"> In <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), the Court held that the Fourteenth Amendment requires observance of this privilege in state-court proceedings.</p>
</footnote>
<footnote label="4">
<p id="b587-4"> In the course of the conversation, that apparently lasted only a few minutes, Manson made two statements, both apparently directed at Mauro’s wife. See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="5">
<p id="b587-6"> Justice Stevens suggests that the officers “employed a powerful psychological ploy.” <em>Post, </em>at 531. He bases this statement on his reading of the record that the officers “failed to give respondent any advance warning that Mrs. Mauro was coming to talk to him, that a police officer would accompany her, or that their conversation would be recorded.” <em>Ibid. </em>This reading is difficult to reconcile with the trial court’s conclusion that the officers “told both Mr. and Mrs. Mauro that they could speak together only if an officer were present in the room to observe and hear what was going on.” App. 218. This sentence seems to indicate that Mauro received advance warning. But accepting the facts as Justice Stevens states them, the opinion still makes it clear that Mauro was fully informed before the conversation began. Similarly, it may be that the officers did not give Mr. Mauro advance warning that they would record the eonversa<page-number citation-index="1" label="528">*528</page-number>tion, but the trial court noted that “[t]he officer who was present produced a tape recorder and told the couple that their conversation would be recorded and put that tape recorder down on the desk in plain sight and taped their conversation, so they had knowledge that that was going on.” <em>Ibid. </em>Justice Stevens also implies that respondent was forced against his will to talk to his wife. <em>Post, </em>at 581. But, as the trial court observed, “[t]he defendant, with knowledge that the police were listening, could have chosen not to speak to his wife. Instead, he chose to speak.” App. 219. In short, the trial court’s findings completely rebut the atmosphere of oppressive police conduct portrayed by the dissent.</p>
</footnote>
<footnote label="6">
<p id="b588-11"> The dissent suggests that the Arizona Supreme Court found as a fact that the officers intended to interrogate Mauro and faults us for reversing this allegedly factual finding. With due respect, we disagree with this reading of the record. The Arizona Supreme Court did not conclude that the officers intended to interrogate Mauro. Rather it concluded that <page-number citation-index="1" label="529">*529</page-number>“[t]hey both knew that . . . incriminating statements were likely to be made.” <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#31" aria-description="Citation for case: State v. Mauro">149 Ariz., at 31</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#400" aria-description="Citation for case: State v. Mauro">716 P. 2d, at 400</a></span>. Taken in context, this is a determination that the facts known to the officers satisfied the legal standard we established in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>. </em>Our decision today does not overturn any of the factual findings of the Arizona Supreme Court. Rather, it rests on a determination that the facts of this case do not present a sufficient likelihood of incrimination to satisfy the legal standard articulated in <em>Miranda </em>v. <em>Arizona </em>and in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>.</em></p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Arizona v. Roberson.md  (`case`, 5 assertions)

### content_page

```
---
title: "Arizona v. Roberson"
type: case
citation: "486 U.S. 675 (1988)"
parallel_cite: "108 S. Ct. 2093; 100 L. Ed. 2d 704; 56 U.S.L.W. 4590"
neutral_cite: 1988 U.S. LEXIS 2726
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Roberson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112100/arizona-v-roberson/"
  cluster_id: 112100
  opinion_id: 9431349
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Minnick v. Mississippi]]", "[[Maryland v. Shatzer]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "right-to-counsel", "interrogation"]
holding: "The Edwards bar is not offense-specific — once a suspect invokes counsel, police may not interrogate him about ANY offense, including an…"
lake:
  record_id: Arizona v. Roberson
  status: verified
  projected_at: 2026-07-06
---

# Arizona v. Roberson

*486 U.S. 675 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Roberson was arrested at the scene of a burglary and, after [[Miranda and Custodial Interrogation|Miranda warnings]], said he wanted a lawyer before answering any questions. Three days later, while he was still in custody, a different officer — unaware of the earlier invocation — gave fresh [[Miranda and Custodial Interrogation|Miranda warnings]] and questioned Roberson about a *different* burglary, and Roberson made an incriminating statement. He moved to suppress it.

## Issue
Whether the *[[Edwards v. Arizona|Edwards]]* rule barring police-initiated interrogation after a suspect invokes counsel applies when the later interrogation concerns a separate offense or investigation.

## Rule
Yes — the *[[Edwards v. Arizona|Edwards]]* bar is not offense-specific. "[T]he presumption raised by a suspect's request for counsel — that he considers himself unable to deal with the pressures of custodial interrogation without legal assistance — does not disappear simply because the police have approached the suspect, still in custody, still without counsel, about a separate investigation." — 486 U.S. at 683. ^pin-683

"That a suspect's request for counsel should apply to any questions the police wish to pose follows, we think, not only from *Edwards* and *Miranda* . . . ." — *Id.* at 684. ^pin-684

## Application
Roberson had asked for a lawyer before answering "any questions," and the presumption that he could not face custodial interrogation without counsel did not evaporate merely because a second officer approached him — still in custody, still without counsel — about a different burglary three days later. Fresh [[Miranda and Custodial Interrogation|Miranda warnings]] did not cure the bar, and the second officer's ignorance of the earlier invocation was irrelevant. The statement was therefore inadmissible.

## Conclusion
The *[[Edwards v. Arizona|Edwards]]* bar applied to the separate-investigation questioning; the suppression of Roberson's statement was upheld and the Arizona Court of Appeals affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Roberson* extends [[Edwards v. Arizona]] so that a counsel invocation bars police-initiated interrogation about **any** offense. The broader *[[Edwards v. Arizona|Edwards]]* line was later refined by [[Maryland v. Shatzer]] (a 14-day break in Miranda custody ends the *[[Edwards v. Arizona|Edwards]]* bar).

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Roberson*, 486 U.S. 675 (1988) — https://www.courtlistener.com/opinion/112100/arizona-v-roberson/ — pinpoints: 683, 684.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9555c88a39790597", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "486 U.S. 675 (1988)", "court": "U.S. Supreme Court", "neutral_cite": "1988 U.S. LEXIS 2726", "official_citation_present": true, "parallel_cite": "108 S. Ct. 2093; 100 L. Ed. 2d 704; 56 U.S.L.W. 4590", "title": "Arizona v. Roberson", "year": "1988"}}
{"assertion_id": "20922c14d2f2f657", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "Arizona v. Roberson"}}
{"assertion_id": "2e6cc9ee399106e8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Edwards bar is not offense-specific — once a suspect invokes counsel, police may not interrogate him about ANY offense, including an…", "title": "Arizona v. Roberson"}}
{"assertion_id": "85c1536916a5f2c5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1988-06-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arizona v. Roberson", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Arizona v. Roberson", "varies_by_point": "false"}}
{"assertion_id": "ccd6c4c98f98ee8e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Roberson"}}
```

### lake record — Arizona v. Roberson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Roberson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Roberson",
    "case_name_short": "Roberson",
    "case_name_full": "Arizona v. Roberson",
    "input_case_name": "Arizona v. Roberson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-15",
    "year": 1988,
    "docket": null,
    "cluster_id": 112100,
    "lead_opinion_id": 9431349,
    "sibling_ids": [
      112100,
      9431349,
      9431350
    ],
    "absolute_url": "/opinion/112100/arizona-v-roberson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9074843,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      },
      {
        "cluster_id": 9074842,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      },
      {
        "cluster_id": 9074378,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      },
      {
        "cluster_id": 9074377,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "486 U.S. 675",
      "volume": "486",
      "reporter": "U.S.",
      "page": "675",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 2093",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2093",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 704",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "704",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4590",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4590",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2726",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2726",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "486 U.S. 675",
        "volume": "486",
        "reporter": "U.S.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 2093",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2093",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 704",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "704",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2726",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2726",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4590",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4590",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "486 U.S. 675",
    "official_selection": {
      "court_class": "scotus",
      "selected": "486 U.S. 675",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-683",
      "page": null,
      "quote": "--- # Arizona v. Roberson *486 U.S. 675 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Roberson was arrested at the scene of a burglary and, after Miranda warnings, said he wanted a lawyer before answering any questions. Three days later, while he was still in custody, a different officer \u2014 unaware of the earlier invocation \u2014 gave fresh Miranda warnings and questioned Roberson about a *different* burglary, and Roberson made an incriminating statement. He moved to suppress it. ## Issue Whether the *Edwards* rule barring police-initiated interrogation after a suspect invokes counsel applies when the later interrogation concerns a separate offense or investigation. ## Rule Yes \u2014 the *Edwards* bar is not offense-specific.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-684",
      "page": null,
      "quote": "That a suspect's request for counsel should apply to any questions the police wish to pose follows, we think, not only from *Edwards* and *Miranda* . . . .",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Roberson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garcia",
          "cluster_id": 2713978,
          "cite": [
            "2013 SD 46",
            "834 N.W.2d 821",
            "2013 WL 3226703",
            "2013 S.D. LEXIS 71"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
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
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gobert",
          "cluster_id": 1947904,
          "cite": [
            "244 S.W.3d 861",
            "2008 Tex. App. LEXIS 742",
            "2008 WL 269448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Van Hook v. Carl S. Anderson, Warden",
          "cluster_id": 793987,
          "cite": [
            "444 F.3d 830",
            "2006 U.S. App. LEXIS 9628",
            "2006 WL 997203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Houston v. State",
          "cluster_id": 1678067,
          "cite": [
            "185 S.W.3d 917",
            "2006 Tex. App. LEXIS 1352",
            "2006 WL 358070"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moran v. State",
          "cluster_id": 1560713,
          "cite": [
            "171 S.W.3d 382",
            "2005 WL 1583847"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Johnson, A/K/A Little Greg, United States of America v. Gregory Johnson, A/K/A Little Greg",
          "cluster_id": 789459,
          "cite": [
            "400 F.3d 187",
            "2005 WL 526889"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harper v. Virginia Department of Taxation",
          "cluster_id": 112890,
          "cite": [
            "125 L. Ed. 2d 74",
            "113 S. Ct. 2510",
            "509 U.S. 86",
            "1993 U.S. LEXIS 4212",
            "7 Fla. L. Weekly Fed. S 456",
            "16 Employee Benefits Cas. (BNA) 2313",
            "93 Daily Journal DAR 7730",
            "93 Cal. Daily Op. Serv. 4491",
            "61 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waidla",
          "cluster_id": 1316339,
          "cite": [
            "996 P.2d 46",
            "94 Cal. Rptr. 2d 396",
            "22 Cal. 4th 690",
            "22 Cal. 690",
            "2000 Daily Journal DAR 3605",
            "2000 Cal. Daily Op. Serv. 2687",
            "2000 Cal. LEXIS 2229"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saffle v. Parks",
          "cluster_id": 112390,
          "cite": [
            "108 L. Ed. 2d 415",
            "110 S. Ct. 1257",
            "494 U.S. 484",
            "1990 U.S. LEXIS 1178",
            "58 U.S.L.W. 4322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leif Taylor v. Thomas M. Maddox, Interim Director George Galaza Cal Terhune",
          "cluster_id": 786028,
          "cite": [
            "366 F.3d 992",
            "2004 U.S. App. LEXIS 9068",
            "2004 WL 1043343"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Crittenden",
          "cluster_id": 2614001,
          "cite": [
            "885 P.2d 887",
            "9 Cal. 4th 83",
            "36 Cal. Rptr. 2d 474",
            "94 Daily Journal DAR 18013",
            "94 Cal. Daily Op. Serv. 9702",
            "1994 Cal. LEXIS 6570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Butler v. McKellar",
          "cluster_id": 112387,
          "cite": [
            "108 L. Ed. 2d 347",
            "110 S. Ct. 1212",
            "494 U.S. 407",
            "1990 U.S. LEXIS 1246"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J. D. B. v. North Carolina",
          "cluster_id": 218925,
          "cite": [
            "180 L. Ed. 2d 310",
            "131 S. Ct. 2394",
            "564 U.S. 261",
            "2011 U.S. LEXIS 4557",
            "22 Fla. L. Weekly Fed. S 1135",
            "79 U.S.L.W. 4504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herron v. State",
          "cluster_id": 2351946,
          "cite": [
            "86 S.W.3d 621",
            "2002 Tex. Crim. App. LEXIS 197",
            "2002 WL 31255420"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mickey",
          "cluster_id": 1226896,
          "cite": [
            "818 P.2d 84",
            "54 Cal. 3d 612",
            "286 Cal. Rptr. 801",
            "91 Daily Journal DAR 13544",
            "91 Cal. Daily Op. Serv. 8732",
            "1991 Cal. LEXIS 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Spotz",
          "cluster_id": 2074443,
          "cite": [
            "896 A.2d 1191",
            "587 Pa. 1",
            "2006 Pa. LEXIS 659"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1407706,
          "cite": [
            "14 Cal. 4th 1005",
            "929 P.2d 544",
            "97 Daily Journal DAR 899",
            "97 Cal. Daily Op. Serv. 520",
            "60 Cal. Rptr. 2d 225",
            "1997 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112100 OR 9431349 OR 9431350) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDE2NTgyNDAwMDAwJnM9MTgyMTk3MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112100+OR+9431349+OR+9431350%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112100 OR 9431349 OR 9431350)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTYmcz0zMTU5OTk1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112100+OR+9431349+OR+9431350%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112100 OR 9431349 OR 9431350)",
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
    "complete_query": "cites:(112100 OR 9431349 OR 9431350)",
    "indexed_citing_opinions": 589,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112100,
        "count": 547,
        "count_source": "search"
      },
      {
        "opinion_id": 9431349,
        "count": 53,
        "count_source": "search"
      },
      {
        "opinion_id": 9431350,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 963,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-roberson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3NTc0MTcmcz00NzUxMDkzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112100+OR+9431349+OR+9431350%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112100,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 419689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 484283,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 487174,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1177179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1278606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1305977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1314131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1434323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1615933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1713623,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1721254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1817395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1983609,
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
    "date_created": "2026-07-04T18:40:48Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:41:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:41:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:46:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:41:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Roberson

```
<opinion type="majority">
<author id="b735-8">Justice Stevens</author>
<p id="ADqQ">delivered the opinion of the Court.</p>
<p id="b735-9">In <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 484-485</a></span> (1981), we held that a suspect who has “expressed his desire to deal with the police only through counsel is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.” In this case Arizona asks us to craft an exception to that rule for cases in which the police want to interrogate a suspect about an offense that is unrelated to the subject of their initial interrogation. Several years ago the Arizona Supreme Court considered, and rejected, a similar argument, stating:</p>
<blockquote id="b735-10">“The only difference between Edwards and the appellant is that Edwards was questioned about the same of<page-number citation-index="1" label="678">*678</page-number>fense after a request for counsel while the appellant was reinterrogated about an unrelated offense. We do not believe that this factual distinction holds any legal significance for fifth amendment purposes. ” <em>State </em>v. <em>Routhier, </em><span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#97" aria-description="Citation for case: State v. Routhier">137 Ariz. 90, 97</a></span>, <span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#75" aria-description="Citation for case: State v. Routhier">669 P. 2d 68, 75</a></span> (1983), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1073/">464 U. S. 1073</a></span> (1984).</blockquote>
<p id="b736-9">We agree with the Arizona Supreme Court’s conclusion.</p>
<p id="b736-10">PH</p>
<p id="b736-3">On April 16, 1985, respondent was arrested at the scene of a just-completed burglary. The arresting officer advised him that he had a constitutional right to remain silent and also the right to have an attorney present during any interrogation. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467-479</a></span> (1966). Respondent replied that he “wanted a lawyer before answering any questions.”<footnotemark>1</footnotemark> This fact was duly recorded in the officer’s written report of the incident. In due course, respondent was convicted of the April 16, 1985, burglary.</p>
<p id="b736-4">On April 19, 1985, while respondent was still in custody pursuant to the arrest three days earlier, a different officer interrogated him about a different burglary that had occurred on April 15. That officer was not aware of the fact that respondent had requested the assistance of counsel three days earlier. After advising respondent of his rights, the officer obtained an incriminating statement concerning the April 15 burglary. In the prosecution for that offense, the trial court suppressed that statement. In explaining his ruling, the trial judge relied squarely on the Arizona Supreme Court’s opinion in <em>State </em>v. <em>Routhier, </em><span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#97" aria-description="Citation for case: State v. Routhier">137 Ariz., at 97</a></span>, <span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#75" aria-description="Citation for case: State v. Routhier">669 P. 2d, at 75</a></span>, characterizing the rule of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>case as “clear and unequivocal.”<footnotemark>2</footnotemark></p>
<p id="b737-4"><page-number citation-index="1" label="679">*679</page-number>The Arizona Court of Appeals affirmed the suppression order in a brief opinion, stating:</p>
<blockquote id="b737-5">“In <em><span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/" aria-description="Citation for case: State v. Routhier">Routhier</a></span>, </em>as in the instant case, the accused was continuously in police custody from the time of asserting his Fifth Amendment right through the time of the impermissible questioning. The coercive environment never dissipated.” App. to Pet. for Cert. 24.</blockquote>
<p id="b737-6">The Arizona Supreme Court denied a petition for review. <em>Id., </em>at 25. We granted certiorari to resolve a conflict with certain other state court decisions.<footnotemark>3</footnotemark> <span class="citation multiple-matches"><a href="/c/U.%20S./484/975/">484 U. S. 975</a></span> (1987). We now affirm.</p>
<p id="b738-9"><page-number citation-index="1" label="680">*680</page-number>hH HH</p>
<p id="b738-1">A major purpose of the Court’s opinion in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#441" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 441-442</a></span>, was “to give concrete constitutional guidelines for law enforcement agencies and courts to follow.” “As we have stressed on numerous occasions, ‘[o]ne of the principal advantages’ of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is the ease and clarity of its application. <em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 430</a></span> (1984); see also <em>New York </em>v. <em>Quarles, </em>[<span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#662" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 662-664</a></span> (1984)] (concurring opinion); <em>Fare </em>v. <em>Michael C., </em>442 U. S. [707, 718 (1979)].” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#425" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 425</a></span> (1986).</p>
<p id="b738-2">The rule of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>case came as a corollary to <em>Miranda's, </em>admonition that “[i]f the individual states that he wants an attorney, the interrogation must cease until an attorney is present.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>. In such an instance, we had concluded in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>“[i]f the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 475</a></span>. In <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>we “reconfirmed] these views and, to lend them substance, emphasize[d] that it is inconsistent with <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and its progeny for the authorities, at their instance, to reinterro-gate an accused in custody if he has clearly asserted his right to counsel.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>. We concluded that re-interrogation may only occur if “the accused himself initiates <page-number citation-index="1" label="681">*681</page-number>farther communication, exchanges, or conversations with the police.” <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span> </em>Thus, the prophylactic protections that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings provide to counteract the “inherently compelling pressures” of custodial interrogation and to “permit a full opportunity to exercise the privilege against self-incrimination,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>, are implemented by the application of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>corollary that if a suspect believes that he is not capable of undergoing such questioning without advice of counsel, then it is presumed that any subsequent waiver that has come at the authorities’ behest, and not at the suspect’s own instigation, is itself the product of the “inherently compelling pressures” and not the purely voluntary choice of the suspect. As Justice White has explained, “the accused having expressed his own view that he is not competent to deal with the authorities without legal advice, a later decision at the authorities’ insistence to make a statement without counsel’s presence may properly be viewed with skepticism.” <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#110" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 110, n. 2</a></span> (1975) (concurring in result).</p>
<p id="b739-5">We have repeatedly emphasized the virtues of a bright-line rule in cases following <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>as well as <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#634" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 634</a></span> (1986); <em>Smith </em>v. <em>Illinois, </em><span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#98" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 98</a></span> (1984) <em>(per curiam); Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#646" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 646</a></span> (1984); see also <em>Shea </em>v. <em>Louisiana, </em><span class="citation" data-id="9429912"><a href="/opinion/111355/shea-v-louisiana/" aria-description="Citation for case: Shea v. Louisiana">470 U. S. 51</a></span> (1985); <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983) (plurality opinion) (Rehnquist, J.). In <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979), we explained that the “relatively rigid requirement that interrogation must cease upon the accused’s request for an attorney . . . has the virtue of informing police and prosecutors with specificity as to what they may do in conducting custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible. This gain in specificity, which benefits the accused and the State alike, has been thought to outweigh the burdens that the de-<page-number citation-index="1" label="682">*682</page-number>cisión in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>imposes on law enforcement agencies and the courts by requiring the suppression of trustworthy and highly probative evidence even though the confession might be voluntary under traditional Fifth Amendment analysis.”<footnotemark>4</footnotemark> The <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule thus serves the purpose of providing “clear and unequivocal” guidelines to the law enforcement profession. Surely there is nothing ambiguous about the requirement that after a person in custody has expressed his desire to deal with the police only through counsel, he “is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>.</p>
<p id="b740-10">I » — I HH</p>
<p id="b740-3">Petitioner contends that the bright-line, prophylactic <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule should not apply when the police-initiated interrogation following a suspect’s request for counsel occurs in the context of a separate investigation. According to petitioner, both our cases and the nature of the factual setting compel this distinction. We are unpersuaded.</p>
<p id="b741-4"><page-number citation-index="1" label="683">*683</page-number>Petitioner points to our holding in <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U. S., at 103</a></span>-104 (quoting <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>), that when a suspect asserts his right to cut off questioning, the police may “ ‘scrupulously honor’ ” that right by “immediately ceas[ing] the interrogation, resum[ing] questioning only after the passage of a significant period of time and the provision of a fresh set of warnings, and restrict[ing] the second interrogation to a crime that had not been a subject of the earlier interrogation.” <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#106" aria-description="Citation for case: Michigan v. Mosley">423 U. S., at 106</a></span>. The police in this case followed precisely that course, claims the State. However, as <em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">Mosley</a></span> </em>made clear, a suspect’s decision to cut off questioning, unlike his request for counsel, does not raise the presumption that he is unable to proceed without a lawyer’s advice. See <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#101" aria-description="Citation for case: Michigan v. Mosley"><em>id., </em>at 101, n. 7</a></span>; <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#110" aria-description="Citation for case: Michigan v. Mosley"><em>id., </em>at 110, n. 2</a></span> (White, J., concurring in result), quoted <em>supra, </em>at 681.</p>
<p id="b741-5">Petitioner points as well to <em>Connecticut </em>v. <em>Barrett, </em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#525" aria-description="Citation for case: Connecticut v. Barrett">479 U. S. 523, 525</a></span> (1987), which concerned a suspect who had “told the officers that he would not give a written statement unless his attorney was present but had ‘no problem’ talking about the incident.” We held that this was a limited request for counsel, that Barrett himself had drawn a distinction between oral and written statements and thus that the officers could continue to question him. Petitioner argues that Roberson’s request for counsel was similarly limited, this time to the investigation pursuant to which the request was made. This argument is flawed both factually and legally. As a matter of fact, according to the initial police report, respondent stated that “he wanted a lawyer before answering <em>any </em>questions.”<footnotemark>5</footnotemark> As a matter of law, the presumption raised by a suspect’s request for counsel — that he considers himself unable to deal with the pressures of custodial interrogation without legal assistance — does not disappear simply because the police have approached the suspect, still in custody, still without counsel, about a separate investigation.</p>
<p id="b742-4"><page-number citation-index="1" label="684">*684</page-number>That a suspect’s request for counsel should apply to any questions the police wish to pose follows, we think, not only from <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>but also from a case decided the same day as <em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">Barrett</a></span>. </em>In <em>Colorado </em>v. <em>Spring, </em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/#577" aria-description="Citation for case: Colorado v. Spring">479 U. S. 564, 577</a></span> (1987), we held that “a suspect’s awareness of all the possible subjects of questioning in advance of interrogation is not relevant to determining whether the suspect voluntarily, knowingly, and intelligently waived his Fifth Amendment privilege.” In the face of the warning'that anything he said could be used as evidence against him, Spring’s willingness to answer questions, without limiting such a waiver, see <em>Connecticut </em>v. <em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">Barrett, supra,</a></span> </em>indicated that he felt comfortable enough with the pressures of custodial interrogation both to answer questions and to do so without an attorney. Since there is “no qualification of [the] broad and explicit warning” that <em>“anything </em>[a suspect] says may be used against him,” 479 U. S., at 577 (emphasis in original), Spring’s decision to talk was properly considered to be equally unqualified. Conversely, Roberson’s unwillingness to answer any questions without the advice of counsel, without limiting his request for counsel, indicated that he did not feel sufficiently comfortable with the pressures of custodial interrogation to answer questions without an attorney. This discomfort is precisely the state of mind that <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>presumes to persist unless the suspect himself initiates further conversation about the investigation; unless he otherwise states, see <em>Connecticut </em>v. <em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">Barrett, supra,</a></span> </em>there is no reason to assume that a suspect’s state of mind is in any' way investigation-specific, see <em>Colorado </em>v. <em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/" aria-description="Citation for case: Colorado v. Spring">Spring, supra.</a></span></em></p>
<p id="b742-5">Finally, petitioner raises the case of <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#161" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 161</a></span> (1985), which held that Moulton’s “Sixth Amendment right to the assistance of counsel was violated by the admission at trial of incriminating statements made by him to his codefendant, a secret government informant, after indictment and at a meeting of the two to plan defense strategy for the upcoming trial.” That case did not involve any <page-number citation-index="1" label="685">*685</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>issue because Moulton was not in custody. In our opinion, we rejected an argument that the statements should be admissible because the police were seeking information regarding both the crime for which Moulton had already been indicted, and a separate, inchoate scheme. Following <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#207" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 207</a></span> (1964), we recognized, though, that the continuing investigation of uncharged offenses did not violate the defendant’s Sixth Amendment right to the assistance of counsel. Our recognition of that fact, however, surely lends no support to petitioner’s argument that in the Fifth Amendment context, “statements about different offenses, developed at different times, by different investigators, in the course of two wholly independent investigations, should not be treated the same.” Brief for Petitioner 32. This argument overlooks the difference between the Sixth Amendment right to counsel and the Fifth Amendment right against self-incrimination. The former arises from the fact that the suspect has been formally charged with a particular crime and thus is facing a state apparatus that has been geared up to prosecute him. The latter is protected by the prophylaxis of having an attorney present to counteract the inherent pressures of custodial interrogation, which arise from the fact of such interrogation and exist regardless of the number of crimes under investigation or whether those crimes have resulted in formal charges.</p>
<p id="b743-6">In sum, our cases do not support petitioner’s position.</p>
<p id="b743-8"><em>&gt; </em>HH</p>
<p id="b743-3">Petitioner’s attempts at distinguishing the factual setting here from that in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>are equally unavailing. Petitioner first relies on the plurality opinion in <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S., at 1044</a></span> (Rehnquist, J.), which stated that <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>laid down “a prophylactic rule, designed to protect an accused in police custody from being badgered by police officers in the manner in which the defendant in <em>Ed</em><page-number citation-index="1" label="686">*686</page-number><em>wards </em>was.” Petitioner reasons that “the chances that an accused will be questioned so repeatedly and in such quick succession that it will ‘undermine the will’ of the person questioned, or will constitute ‘badger[ing],’ are so minute as not to warrant consideration, if the officers are truly pursuing separate investigations.” Brief for Petitioner 16. It is by no means clear, though, that police engaged in separate investigations will be any less eager than police involved in only one inquiry to question a suspect in custody. Further, to a suspect who has indicated his inability to cope with the pressures of custodial interrogation by requesting counsel, any further interrogation without counsel having been provided will surely exacerbate whatever compulsion to speak the suspect may be feeling. Thus, we also disagree with petitioner’s contention that fresh sets of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings will “reassure” a suspect who has been denied the counsel he has clearly requested that his rights have remained untrammeled. See <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span> </em>Especially in a case such as this, in which a period of three days elapsed between the unsatisfied request for counsel and the interrogation about a second offense, there is a serious risk that the mere repetition of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings would not overcome the presumption of coercion that is created by prolonged police custody.<footnotemark>6</footnotemark></p>
<p id="b745-4"><page-number citation-index="1" label="687">*687</page-number>The United States, as <em>amicus curiae </em>supporting petitioner, suggests that a suspect in custody might have “good reasons for wanting to speak with the police about the offenses involved in the new investigation, or at least to learn from the police what the new investigation is about so that he can decide whether it is in his interest to make a statement about that matter without the assistance of counsel.” Brief for United States as <em>Amicus Curiae </em>11. The simple answer is that the suspect, having requested counsel, can determine how to deal with the separate investigations with counsel’s advice. Further, even if the police have decided temporarily not to provide counsel, see n. 6, <em>supra, </em>they are free to inform the suspect of the facts of the second investigation as long as such communication does not constitute interrogation, see <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980). As we have made clear, any “further communication, exchanges, or conversations with the police” that the suspect himself initiates, <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>, are perfectly valid.</p>
<p id="b745-5">Finally, we attach no significance to the fact that the officer who conducted the second interrogation did not know that respondent had made a request for counsel. In addition to the fact that <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>focuses on the state of mind of the suspect and not of the police, custodial interrogation must be conducted pursuant to established procedures, and those procedures in turn must enable an officer who proposes to initiate an interrogation to determine whether the suspect has previously requested counsel. In this case respondent’s request had been properly memorialized in a written report but the officer who conducted the interrogation simply failed to examine that report. Whether a contemplated reinterrogation concerns the same or a different offense, or whether the same or different law enforcement authorities are involved in the second investigation, the same need to determine <page-number citation-index="1" label="688">*688</page-number>whether the suspect has requested counsel exists.<footnotemark>7</footnotemark> The police department’s failure to honor that request cannot be justified by the lack of diligence of a particular officer. Cf. <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972).</p>
<p id="b746-5">The judgment of the Arizona Court of Appeals is</p>
<p id="b746-6">
<em>Affirmed.</em>
</p>
<p id="b746-7">Justice O’Connor took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b736-5"> Tr. 26 (Apr. 3, 1986).</p>
</footnote>
<footnote label="2">
<p id="b736-6"> “Routhier was based on Edwards versus Arizona which held that once the defendant has invoked his right to counsel, he may not be re-<page-number citation-index="1" label="679">*679</page-number>interrogated unless counsel has been made available to him or he initiates the conversation.</p>
<blockquote id="b737-8">“The Routhier court states that whether the defendant is re-interrogated about the same offense or an unrelated offense makes no difference for Fifth Amendment purposes.</blockquote>
<blockquote id="b737-9">“The Routhier court further stated that Edwards is clear and unequivocal, there is to be no further interrogation by authorities once the right to counsel is invoked. The Court in that ease finding that the assertion of the right to counsel is an assertion by the accused that he is not competent to deal with authorities without legal advice. And that the resumption of questioning by the police without the requested attorney being provided, strongly suggests to the accused that he has no choice but to answer.” App. to Pet. for Cert. 15-16.</blockquote>
</footnote>
<footnote label="3">
<p id="b737-10"> See <em>State </em>v. <em>Dampier, </em><span class="citation" data-id="1314131"><a href="/opinion/1314131/state-v-dampier/" aria-description="Citation for case: State v. Dampier">314 N. C. 292</a></span>, <span class="citation" data-id="1314131"><a href="/opinion/1314131/state-v-dampier/" aria-description="Citation for case: State v. Dampier">333 S. E. 2d 230</a></span> (1985) <em>(Edwards </em>inapplicable to interrogation by authorities from different State concerning unrelated matter); <em>McFadden </em>v. <em>Commonwealth, </em><span class="citation" data-id="1305977"><a href="/opinion/1305977/mcfadden-v-commonwealth/" aria-description="Citation for case: McFadden v. Commonwealth">225 Va. 103</a></span>, <span class="citation" data-id="1305977"><a href="/opinion/1305977/mcfadden-v-commonwealth/" aria-description="Citation for case: McFadden v. Commonwealth">300 S. E. 2d 924</a></span> (1983) <em>(Edwards </em>inapplicable when authorities from different county question suspect about different crime); see also <em>Lofton </em>v. <em>State, </em><span class="citation" data-id="1817395"><a href="/opinion/1817395/lofton-v-state/" aria-description="Citation for case: Lofton v. State">471 So. 2d 665</a></span> (Fla. App.) (no <em>Edwards </em>violation when suspect is represented by attorney in unrelated matter, then questioned without counsel present), review denied, <span class="citation no-link">480 So. 2d 1294</span> (Fla. 1985); <em>State </em>v. <em>Newton, </em><span class="citation" data-id="1278606"><a href="/opinion/1278606/state-v-newton/" aria-description="Citation for case: State v. Newton">682 P. 2d 295</a></span> (Utah 1984) (same); <em>State </em>v. <em>Cornethan, </em><span class="citation" data-id="1434323"><a href="/opinion/1434323/state-v-cornethan/" aria-description="Citation for case: State v. Cornethan">38 Wash. App. 231</a></span>, <span class="citation" data-id="1434323"><a href="/opinion/1434323/state-v-cornethan/" aria-description="Citation for case: State v. Cornethan">684 P. 2d 1355</a></span> (1984) (alternative holding: <em>Edwards </em>inapplicable to interrogation in unrelated investigation; court also holds that representation by attorney in unrelated matter does not suffice as request for counsel for <em>Edwards </em>purposes); cf. <em>State </em>v. <em>Harriman, </em><span class="citation" data-id="1721254"><a href="/opinion/1721254/state-v-harriman/" aria-description="Citation for case: State v. Harriman">434 So. 2d 551</a></span> (La. App.) (adopts petitioner’s view here, but only after holding that suspect had initiated conversation regarding second investigation), writ denied, <span class="citation multiple-matches"><a href="/c/So.%202d/440/729/">440 So. 2d 729</a></span> (La. <page-number citation-index="1" label="680">*680</page-number>1983); but see <em>United States ex rel. Espinoza </em>v. <em>Fairman, </em><span class="citation" data-id="484283"><a href="/opinion/484283/united-states-of-america-ex-rel-miguel-a-espinoza-v-jw-fairman-warden/#124" aria-description="Citation for case: United States of America Ex Rel. Miguel A. Espinoza v....">813 F. 2d 117, 124-126</a></span> (CA7) (same rule as Arizona), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./483/1010/">483 U. S. 1010</a></span> (1987); <em>Luman </em>v. <span class="citation" data-id="1713623"><a href="/opinion/1713623/luman-v-state/" aria-description="Citation for case: Luman v. State"><em>State, 447 </em>So. 2d 428</a></span> (Fla. App. 1984). (same); <em>Radovsky </em>v. <em>State, </em><span class="citation" data-id="1983609"><a href="/opinion/1983609/radovsky-v-state/" aria-description="Citation for case: Radovsky v. State">296 Md. 386</a></span>, <span class="citation" data-id="1983609"><a href="/opinion/1983609/radovsky-v-state/" aria-description="Citation for case: Radovsky v. State">464 A. 2d 239</a></span> (1983) (same); see also <em>Boles </em>v. <em>Foltz, </em><span class="citation" data-id="9476074"><a href="/opinion/487174/robert-lee-boles-jr-v-dale-foltz-warden/#1137" aria-description="Citation for case: Robert Lee Boles, Jr. v. Dale Foltz, Warden">816 F. 2d 1132, 1137-1141</a></span> (CA6) (Gibson, J., dissenting) (same; majority does not reach issue), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./484/857/">484 U. S. 857</a></span> (1987); cf. <em>United States </em>v. <em>Scalf, </em><span class="citation" data-id="419689"><a href="/opinion/419689/united-states-v-george-a-scalf-jr/#1544" aria-description="Citation for case: United States v. George A. Scalf, Jr.">708 F. 2d 1540, 1544</a></span> (CA10 1983) (knowledge of request for counsel “is imputed to all law enforcement officers who subsequently deal with the suspect”); <em>State </em>v. <em>Arceneaux, </em><span class="citation" data-id="1615933"><a href="/opinion/1615933/state-v-arceneaux/" aria-description="Citation for case: State v. Arceneaux">425 So. 2d 740</a></span> (La. 1983) (same).</p>
</footnote>
<footnote label="4">
<p id="b740-4"> It is significant that our explanation of the basis for the <em>“per se </em>aspect of <em>Miranda” </em>in <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 719</a></span>, applies to the application of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule in a case such as this. As we stated in <em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">Fare</a></span>:</em></p>
<blockquote id="b740-5">“The rule in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> . . </em>. was based on this Court’s perception that the lawyer occupies a critical position in our legal system because of his unique ability to protect the Fifth Amendment rights of a client undergoing custodial interrogation. Because of this special ability of the lawyer to help the client preserve his Fifth Amendment rights once the client becomes enmeshed in the adversary process, the Court found that ‘the right to have counsel present at the interrogation is indispensable to the protection of the Fifth Amendment privilege under the system’ established by the Court. [384 U. S.], at 469. Moreover, the lawyer’s presence helps guard against overreaching by the police and ensures that any statements actually obtained are accurately transcribed for presentation into evidence. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 470</a></span>.</blockquote>
<blockquote id="b740-6">“The <em>per se </em>aspect of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was thus based on the unique role the lawyer plays in the adversary system of criminal justice in this country.” <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 719</a></span>.</blockquote>
</footnote>
<footnote label="5">
<p id="b741-6"> Tr. 26 (Apr. 3, 1986) (emphasis added); see <em>id., </em>at 23; Tr. 12 (Oct. 17, 1985, a.m.).</p>
</footnote>
<footnote label="6">
<p id="b744-5"> The United States, as <em>amicus curiae </em>supporting petitioner, suggests similarly that “respondent’s failure to reiterate his request for counsel to [the officer involved in the second investigation], even, after [that officer] gave respondent complete <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, could not have been the result of any doubt on respondent’s part that the police would honor a request for counsel if one were made.” Brief for United States as <em>Amicus Curiae </em>10. This conclusion is surprising, considering that respondent had not been provided with the attorney he had already requested, despite having been subjected to police-initiated interrogation with respect to the first investigation as well. See n. 7, <em>infra. </em>We reiterate here, though, that the “right” to counsel to protect the Fifth Amendment right against self-incrimination is not absolute; that is, “[i]f authorities conclude that they will not provide counsel during a reasonable period of time in which investigation in the field is carried out, they may refrain from doing so without violating the person’s Fifth Amendment privilege so long as they <page-number citation-index="1" label="687">*687</page-number>do not question him during that time.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 474</a></span> (1966).</p>
</footnote>
<footnote label="7">
<p id="b746-10"> Indeed, the facts of this case indicate that different officers investigating the same offense are just as likely to bypass proper procedures as an officer investigating a different offense, inasmuch as the record discloses no less than five violations of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule, four concerning the April 16 burglary and only one concerning the April 15 burglary. See Tr. 23-24, 49 (Apr. 3, 1986); Tr. 8-12 (Oct. 17, 1985, p.m.). It is only the last violation that is at issue in this case.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Arizona v. Youngblood.md  (`case`, 5 assertions)

### content_page

```
---
title: Arizona v. Youngblood
type: case
citation: "488 U.S. 51 (1989)"
parallel_cite: "109 S. Ct. 333; 102 L. Ed. 2d 281"
neutral_cite: 1988 U.S. LEXIS 5404
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-01-23
docket: No. 86-1904
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
  opinion_url: "https://www.courtlistener.com/opinion/112156/arizona-v-youngblood/"
  cluster_id: 112156
  opinion_id: null
  identity_checked: true
lake:
  record_id: Arizona v. Youngblood
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Brady and Giglio]]"
    role: Anchor
related:
  - "[[Brady and Giglio]]"
  - "[[California v. Trombetta]]"
tags:
  - case
  - fourteenth-amendment
  - due-process
  - preservation-of-evidence
  - bad-faith
  - brady
holding: "The government's failure to preserve evidence that is only potentially useful to the defense — as opposed to evidence whose exculpatory value was apparent before it was destroyed — does not deny the defendant due process unless he shows bad faith on the part of the police."
aliases:
  - Arizona v. Youngblood
  - "Arizona v. Youngblood (1988)"
---

# Arizona v. Youngblood

*488 U.S. 51 (1989)* (No. 86-1904) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112156 → combined opinion 112156 (Rehnquist, C.J.; 488 U.S. 51; argued Oct. 11, 1988, decided Nov. 29, 1988). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star *58, confirmed by the dissent's "Ante, at 58"). DATA NOTE: the lake identity carries year 1989 / date 1989-01-23 (CL cluster date_filed), so the projected citation parenthetical reads (1989); the opinion itself was decided Nov. 29, 1988 — flagged for S2. S9 promotes. -->

## Background
A 10-year-old boy was abducted, molested, and repeatedly sodomized; afterward he was examined at a hospital, where a physician collected a rectal swab and preserved the boy's clothing. Investigators did not refrigerate the clothing, and a police criminologist did not perform timely tests on the semen samples. By the time the defense sought to test the samples for blood-group and enzyme markers that might have identified — or excluded — the assailant, the evidence had degraded and could no longer yield useful results. Larry Youngblood was convicted in Pima County, Arizona, of child molestation, sexual assault, and kidnapping. The Arizona Court of Appeals reversed, holding that the State's failure to preserve the testable evidence denied Youngblood due process. The State sought review.

## Issue
Whether the Due Process Clause requires the police to preserve evidentiary material that might have been subjected to tests whose results could have exonerated the defendant — and, if so, whether a failure to do so violates due process absent any showing of bad faith.

## Rule
The Court distinguished evidence whose [[Brady and Giglio|exculpatory]] value is apparent before its destruction — governed by *[[California v. Trombetta|Trombetta]]* — from evidence that is merely "potentially useful," where no more than the possibility of exoneration is at stake. For the latter category the Court fixed the defendant's burden on the police's state of mind rather than on the lost evidence's speculative value: "We therefore hold that unless a criminal defendant can show bad faith on the part of the police, failure to preserve potentially useful evidence does not constitute a denial of due process of law." — 488 U.S. at 58. ^pin-58

## Application
Whatever tests might have been run on the semen samples and clothing, their [[Brady and Giglio|exculpatory]] value was speculative — they might have inculpated Youngblood as easily as cleared him — so the evidence fell in the "potentially useful" category rather than the *[[California v. Trombetta|Trombetta]]* category of apparent [[Brady and Giglio|exculpatory]] value. And the officers' handling of the evidence was, as the Court saw it, at worst negligent; nothing in the record showed the police acted in bad faith or with any awareness that the material could exonerate the accused. Absent that bad faith, the failure to preserve the samples worked no due process violation.

## Conclusion
The judgment of the Arizona Court of Appeals was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Rehnquist, C.J., delivered the opinion of the Court; Stevens, J., concurred in the judgment; Blackmun, J., dissented, joined by Brennan and Marshall, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Youngblood* remains the governing rule for lost or destroyed evidence that is only "potentially useful": the defendant must prove **bad faith**, a demanding standard the Court has adhered to since (see *Illinois v. Fisher* (2004), applying the bad-faith requirement to evidence a defendant had specifically requested). Teach it as the sharp line between the two preservation regimes — *[[California v. Trombetta|Trombetta]]*'s "apparent exculpatory value" duty on one side, and *Youngblood*'s bad-faith gate for merely potentially useful evidence on the other.

## Appears on
- [[Brady and Giglio]] — *Anchor*

## Sources
- [*Arizona v. Youngblood*, 488 U.S. 51 (1989)](https://www.courtlistener.com/opinion/112156/arizona-v-youngblood/) — pinpoint: 58 (Rehnquist, C.J., for the Court; the CL opinion text carries the reporter star `*58` and the dissent cross-references the holding as "Ante, at 58"). Argued Oct. 11, 1988; decided Nov. 29, 1988 (the projected "(1989)" parenthetical follows the lake identity year, which mirrors CourtListener's cluster `date_filed`; flagged for S2). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7787ac8e6da41dda", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "488 U.S. 51 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1988 U.S. LEXIS 5404", "official_citation_present": true, "parallel_cite": "109 S. Ct. 333; 102 L. Ed. 2d 281", "title": "Arizona v. Youngblood", "year": "1989"}}
{"assertion_id": "0d2e89036ae2deb0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The government's failure to preserve evidence that is only potentially useful to the defense — as opposed to evidence whose exculpatory value was apparent before it was destroyed — does not deny the defendant due process unless he shows bad faith on the part of the police.", "title": "Arizona v. Youngblood"}}
{"assertion_id": "daca8fb7302dc4b4", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Anchor", "title": "Arizona v. Youngblood"}}
{"assertion_id": "361f568554fb3461", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Arizona v. Youngblood", "varies_by_point": "false"}}
{"assertion_id": "58dbae195badb2d4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Youngblood"}}
```

### lake record — Arizona v. Youngblood

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Youngblood",
  "status": "under_review",
  "identity": {
    "case_name": "Arizona v. Youngblood",
    "case_name_short": "Youngblood",
    "case_name_full": "Arizona v. Youngblood",
    "input_case_name": "Arizona v. Youngblood",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-01-23",
    "year": 1989,
    "docket": "No. 86-1904",
    "cluster_id": 112156,
    "lead_opinion_id": 9431483,
    "sibling_ids": [],
    "absolute_url": "/opinion/112156/arizona-v-youngblood/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "488 U.S. 51",
      "volume": "488",
      "reporter": "U.S.",
      "page": "51",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 333",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 281",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 5404",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "5404",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "488 U.S. 51",
        "volume": "488",
        "reporter": "U.S.",
        "page": "51",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 333",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 281",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 5404",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "5404",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "488 U.S. 51",
    "official_selection": {
      "court_class": "scotus",
      "selected": "488 U.S. 51",
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
    "date_created": "2026-07-06T13:45:44Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "arizona-v-youngblood--112156",
      "to_record_id": "Arizona v. Youngblood",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Arizona v. Youngblood

```
<opinion type="majority">
<author id="b182-6">Chief Justice Rehnquist</author>
<p id="Ar8">delivered the opinion of the Court.</p>
<p id="b182-7">Respondent Larry Youngblood was convicted by a Pima County, Arizona, jury of child molestation, sexual assault, and kidnaping. The Arizona Court of Appeals reversed his conviction on the ground that the State had failed to preserve semen samples from the victim’s body and clothing. <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/" aria-description="Citation for case: State v. Youngblood">153 Ariz. 50</a></span>, <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/" aria-description="Citation for case: State v. Youngblood">734 P. 2d 592</a></span> (1986). We granted certiorari to consider the extent to which the Due Process Clause of the Fourteenth Amendment requires the State to preserve evidentiary material that might be useful to a criminal defendant.</p>
<p id="b182-8">On October 29, 1983, David L., a 10-year-old boy, attended a church service with his mother. After he left the service at about 9:30 p.m., the boy went to a carnival behind the church, where he was abducted by a middle-aged man of medium height and weight. The assailant drove the boy to a secluded area near a ravine and molested him. He then took the boy to an unidentified, sparsely furnished house where he sodomized the boy four times.. Afterwards, the assailant tied the boy up while he went outside to start his car. Once the assailant started the car, albeit with some difficulty, he returned to the house and again sodomized the boy. The assailant then sent the boy to the bathroom to wash up before he returned him to the carnival. He threatened to kill the boy if he told anyone about the attack. The entire ordeal lasted about <em>YA </em>hours.</p>
<p id="b182-9">After the boy made his way home, his mother took him to Kino Hospital. At the hospital, a physician treated the boy for rectal injuries. The physician also used a “sexual assault kit” to collect evidence of the attack. The Tucson Police De<page-number citation-index="1" label="53">*53</page-number>partment provided such kits to all hospitals in Pima County for use in sexual assault cases. Under standard procedure, the victim of a sexual assault was taken to a hospital, where a physician used the kit to collect evidence. The kit included paper to collect saliva samples, a tube for obtaining a blood sample, microscopic slides for making smears, a set of Q-Tip-like swabs, and a medical examination report. Here, the physician used the swab to collect samples from the boy’s rectum and mouth. He then made a microscopic slide of the samples. The doctor also obtained samples of the boy’s saliva, blood, and hair. The physician did not examine the samples at any time. The police placed the kit in a secure refrigerator at the police station. At the hospital, the police also collected the boy’s underwear and T-shirt. This clothing was not refrigerated or frozen.</p>
<p id="b183-5">Nine days after the attack, on November 7, 1983, the police asked the boy to pick out his assailant from a photographic lineup. The boy identified respondent as the assailant. Respondent was not located by the police until four weeks later; he was arrested on December 9, 1983.</p>
<p id="b183-6">On November 8, 1983, Edward Heller, a police criminologist, examined the sexual assault kit. He testified that he followed standard department procedure, which was to examine the slides and determine whether sexual contact had occurred. After he determined that such contact had occurred, the criminologist did not perform any other tests, although he placed the assault kit back in the refrigerator. He testified that tests to identify blood group substances were not routinely conducted during the initial examination of an assault kit and in only about half of all cases in any event. He did not test the clothing at this time.</p>
<p id="b183-7">Respondent was indicted on charges of child molestation, sexual assault, and kidnaping. The State moved to compel respondent to provide blood and saliva samples for comparison with the material gathered through the use of the sexual assault kit, but the trial court denied the motion on the <page-number citation-index="1" label="54">*54</page-number>ground that the State had not obtained a sufficiently large semen sample to make a valid comparison. The prosecutor then asked the State’s criminologist to perform an ABO blood group test on the rectal swab sample in an attempt to ascertain the blood type of the boy’s assailant. This test failed to detect any blood group substances in the sample.</p>
<p id="b184-5">In January 1985, the police criminologist examined the boy’s clothing for the first time. He found one semen stain on the boy’s underwear and another on the rear of his T-shirt. The criminologist tried to obtain blood group substances from both stains using the ABO technique, but was unsuccessful. He also performed a P-30 protein molecule test on the stains, which indicated that only a small quantity of semen was present on the clothing; it was inconclusive as to the assailant’s identity. The Tucson Police Department had just begun using this test, which was then used in slightly more than half of the crime laboratories in the country.</p>
<p id="b184-6">Respondent’s principal defense at trial was that the boy had erred in identifying him as the perpetrator of the crime. In this connection, both a criminologist for the State and an expert witness for respondent testified as to what might have been shown by tests performed on the samples shortly after they were gathered, or by later tests performed on the samples from the boy’s clothing had the clothing been properly refrigerated. The court instructed the jury that if they found the State had destroyed or lost evidence, they might “infer that the true fact is against the State’s interest.” 10 Tr. 90.</p>
<p id="b184-7">The jury found respondent guilty as charged, but the Arizona Court of Appeals reversed the judgment of conviction. It stated that “‘when identity is an issue at trial and the police permit the destruction of evidence that could eliminate the defendant as the perpetrator, such loss is material to the defense and is a denial of due process.’” <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#54" aria-description="Citation for case: State v. Youngblood">153 Ariz., at 54</a></span>, <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#596" aria-description="Citation for case: State v. Youngblood">734 P. 2d, at 596</a></span>, quoting <em>State </em>v. <em>Escalante, </em><span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/#61" aria-description="Citation for case: State v. Escalante">153 Ariz. 55, 61</a></span>, <span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/#603" aria-description="Citation for case: State v. Escalante">734 P. 2d 597, 603</a></span> (App. 1986). The Court of Ap<page-number citation-index="1" label="55">*55</page-number>peals concluded on the basis of the expert testimony at trial that timely performance of tests with properly preserved semen samples could have produced results that might have completely exonerated respondent. The Court of Appeals reached this conclusion even though it did “not imply any bad faith on the part of the State.” 153 Ariz., at 54, 734 P. 2d, at 596. The Supreme Court of Arizona denied the State’s petition for review, and we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./485/903/">485 U. S. 903</a></span> (1988). We now reverse.</p>
<p id="b185-5">Decision of this case requires us to again consider “what might loosely be called the area of constitutionally guaranteed access to evidence.” <em>United States </em>v. <em>Valenzuela-Bernal, </em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#867" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 867</a></span> (1982). In <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), we held that “the suppression by the prosecution of evidence favorable to the accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland"><em>Id., </em>at 87</a></span>. In <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976), we held that the prosecution had a duty to disclose some evidence of this description even though no requests were made for it, but at the same time we rejected the notion that a “prosecutor has a constitutional duty routinely to deliver his entire file to defense counsel.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 111</a></span>; see also <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972) (“We know of no constitutional requirement that the prosecution make a complete and detailed accounting to the defense of all police investigatory work on a case”).</p>
<p id="b185-6">There is no question but that the State complied with <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>here. The State disclosed relevant police reports to respondent, which contained information about the existence of the swab and the clothing, and the boy’s examination at the hospital. The State provided respondent’s expert with the laboratory reports and notes prepared by the police criminologist, and respondent’s expert had access to the swab and to the clothing.</p>
<p id="b186-4"><page-number citation-index="1" label="56">*56</page-number>If respondent is to prevail on federal constitutional grounds, then, it must be because of some constitutional duty over and above that imposed by cases such as <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>. </em>Our most recent decision in this area of the law, <em>California </em>v. <em>Trombetta, </em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">467 U. S. 479</a></span> (1984), arose out of a drunken driving prosecution in which the State had introduced test results indicating the concentration of alcohol in the blood of two motorists. The defendants sought to suppress the test results on the ground that the State had failed to preserve the breath samples used in the test. We rejected this argument for several reasons: first, “the officers here were acting in ‘good faith and in accord with their normal practice,’” <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#488" aria-description="Citation for case: California v. Trombetta"><em>id., </em>at 488</a></span>, quoting <em>Killian </em>v. <em>United States, </em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/#242" aria-description="Citation for case: Killian v. United States">368 U. S. 231, 242</a></span> (1961); second, in the light of the procedures actually used the chances that preserved samples would have exculpated the defendants were slim, <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#489" aria-description="Citation for case: California v. Trombetta">467 U. S., at 489</a></span>; and, third, even if the samples might have shown inaccuracy in the tests, the defendants had “alternative means of demonstrating their innocence.” <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#490" aria-description="Citation for case: California v. Trombetta"><em>Id., </em>at 490</a></span>. In the present case, the likelihood that the preserved materials would have enabled the defendant to exonerate himself appears to be greater than it was in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span>, </em>but here, unlike in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span>, </em>the State did not attempt to make any use of the materials in its own case in chief. <footnotemark>*</footnotemark></p>
<p id="b187-4"><page-number citation-index="1" label="57">*57</page-number>Our decisions in related areas have stressed the importance for constitutional purposes of good or bad faith on the part of the Government when the claim is based on loss of evidence attributable to the Government. In <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/" aria-description="Citation for case: United States v. Marion">404 U. S. 307</a></span> (1971), we said that “[n]o actual prejudice to the conduct of the defense is alleged or proved, and there is no showing that the Government intentionally delayed to gain some tactical advantage over appellees or to harass them.” <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#325" aria-description="Citation for case: United States v. Marion"><em>Id., </em>at 325</a></span>; see also <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#790" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 790</a></span> (1977). Similarly, in <em>United States </em>v. <em>Valenzuela-Bemal, supra, </em>we considered whether the Government’s deportation of two witnesses who were illegal aliens violated due process. We held that the prompt deportation of the witnesses was justified “upon the Executive’s good-faith determination that they possess no evidence favorable to the defendant in a criminal prosecution.” <em>Id., </em>at 872.</p>
<p id="b187-5">The Due Process Clause of the Fourteenth Amendment, as interpreted in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>makes the good or bad faith of the State irrelevant when the State fails to disclose to the defendant material exculpatory evidence. But we think the Due Process Clause requires a different result when we deal with the failure of the State to preserve evidentiary material of which no more can be said than that it could have been subjected to tests, the results of which might have exonerated the defendant. Part of the reason for the difference in treatment is found in the observation made by the Court in <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#486" aria-description="Citation for case: California v. Trombetta"><em>Trombetta, supra, </em>at 486</a></span>, that “[w]henever potentially excul<page-number citation-index="1" label="58">*58</page-number>patory evidence is permanently lost, courts face the treacherous task of divining the import of materials whose contents are unknown and, very often, disputed.” Part of it stems from our unwillingness to read the “fundamental fairness” requirement of the Due Process Clause, see <em>Lisenba </em>v. <em>California, </em><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 236</a></span> (1941), as imposing on the police an undifferentiated and absolute duty to retain and to preserve all material that might be of conceivable evidentiary significance in a particular prosecution. We think that requiring a defendant to show bad faith on the part of the police both limits the extent of the police’s obligation to preserve evidence to reasonable bounds and confines it to that class of cases where the interests of justice most clearly require it, <em>i. e., </em>those cases in which the police themselves by their conduct indicate that the evidence could form a basis for exonerating the defendant. We therefore hold that unless a criminal defendant can show bad faith on-the part of the police, failure to preserve potentially useful evidence does not constitute a denial of due process of law.</p>
<p id="b188-5">In this case, the police collected the rectal swab and clothing on the night of the crime; respondent was not taken into custody until six weeks later. The failure of the police to refrigerate the clothing and to perform tests on the semen samples can at worst be described as negligent. None of this information was concealed from respondent at trial, and the evidence — such as it was — was made available to respondent’s expert who declined to perform any tests on the samples. The Arizona Court of Appeals noted in its opinion— and we agree — that there was no suggestion of bad faith on the part of the police. It follows, therefore, from what we have said, that there was no violation of the Due Process Clause.</p>
<p id="b188-6">The Arizona Court of Appeals also referred somewhat obliquely to the State’s “inability to quantitatively test” certain semen samples with the newer P-30 test. 153 Ariz., at 54, 734 P. 2d, at 596. If the court meant by this statement <page-number citation-index="1" label="59">*59</page-number>that the Due Process Clause is violated when the police fail to use a particular investigatory tool, we strongly disagree. The situation here is no different than a prosecution for drunken driving that rests on police observation alone; the defendant is free to argue to the finder of fact that a breathalyzer test might have been exculpatory, but the police do not have a constitutional duty to perform any particular tests.</p>
<p id="b189-5">The judgment of the Arizona Court of Appeals is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b189-6">
<em>Reversed.</em>
</p>
<footnote label="*">
<p id="b186-5">In this case, the Arizona Court of Appeals relied on its earlier decision in <em>State </em>v. <em>Escalante, </em><span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/" aria-description="Citation for case: State v. Escalante">153 Ariz. 55</a></span>, <span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/" aria-description="Citation for case: State v. Escalante">734 P. 2d 597</a></span> (1986), holding that ‘“when identity is an issue at trial and the police permit destruction of evidence that <em>could eliminate </em>a defendant as the perpetrator, such loss is material to the defense and is a denial of due process.’ ” <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#54" aria-description="Citation for case: State v. Youngblood">153 Ariz. 50, 54</a></span>, <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#596" aria-description="Citation for case: State v. Youngblood">734 P. 2d 592, 596</a></span> (1986), quoting <span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/#61" aria-description="Citation for case: State v. Escalante"><em>Escalante, supra, </em>at 61</a></span>, 734 P. 2d, at 603 (emphasis added). The reasoning in <em><span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/" aria-description="Citation for case: State v. Escalante">Escalante</a></span> </em>and the instant case mark a sharp departure from <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span> </em>in two respects. First, <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span> </em>speaks of evidence whose exculpatory value is “apparent.” <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#489" aria-description="Citation for case: California v. Trombetta">467 U. S., at 489</a></span>. The possibility that the semen samples could have exculpated respondent if preserved or tested is not enough to satisfy the standard of constitutional materiality in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span>. </em>Second, we made clear in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span> </em>that the exculpatory value of the evidence must be apparent <page-number citation-index="1" label="57">*57</page-number><em>“before </em>the evidence was destroyed.” <em>Ibid, </em>(emphasis added). Here, respondent has not shown that the police knew the semen samples would have exculpated him when they failed to perform certain tests or to refrigerate the boy’s clothing; this evidence was simply an avenue of investigation that might have led in any number of directions. The presence or absence of bad faith by the police for purposes of the Due Process Clause must necessarily turn on the police’s knowledge of the exculpatory value of the evidence at the time it was lost or destroyed. Cf. <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269</a></span> (1959).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Arkansas v. Sanders.md  (`case`, 5 assertions)

### content_page

```
---
title: Arkansas v. Sanders
type: case
citation: "442 U.S. 753 (1979)"
parallel_cite: "99 S. Ct. 2586; 61 L. Ed. 2d 235"
neutral_cite: 1979 U.S. LEXIS 6
court: U.S.
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-20
docket: 77-1497
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
  opinion_url: "https://www.courtlistener.com/opinion/110119/arkansas-v-sanders/"
  cluster_id: 110119
  opinion_id: null
  identity_checked: true
lake:
  record_id: Arkansas v. Sanders
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Automobile Exception]]"
    role: Historical / origin
related:
  - "[[California v. Acevedo]]"
  - "[[United States v. Chadwick]]"
  - "[[United States v. Ross]]"
tags:
  - case
  - fourth-amendment
  - automobile-exception
  - containers
  - luggage
  - warrant-requirement
  - overruled
  - historical
holding: "The Fourth Amendment's warrant requirement applies to personal luggage taken from a lawfully stopped automobile to the same degree it applies to luggage elsewhere, so police may not search a suitcase seized from a car without a warrant absent exigency — a container rule later overruled by California v. Acevedo (1991)."
---

# Arkansas v. Sanders

*442 U.S. 753 (1979)* (No. 77-1497) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — overruled by [[California v. Acevedo]] (1991)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 110119 → 442 U.S. 753, decided 1979-06-20; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
Acting on an informant's tip, Little Rock police watched Sanders retrieve a green suitcase from airport baggage claim, hand it to a companion, and drive off in a taxi with the suitcase in the trunk. Officers stopped the taxi, opened the unlocked suitcase without a warrant, and found marihuana. The Arkansas Supreme Court held the warrantless search unlawful and reversed Sanders's conviction; the State sought review, arguing that the automobile exception justified the search because the luggage came from a lawfully stopped car.

## Issue
Whether, absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], police must obtain a warrant before searching luggage they have seized from a lawfully stopped automobile.

## Rule
Extending *[[United States v. Chadwick|Chadwick]]*, the Court held that the automobile exception does not reach personal luggage merely because it was taken from a car. Once officers have seized a suitcase and reduced it to their exclusive control, the vehicle's mobility no longer supplies an [[Exigent Circumstances and Hot Pursuit|exigency]], and luggage carries the same expectation of privacy wherever it is found: "In sum, we hold that the warrant requirement of the Fourth Amendment applies to personal luggage taken from an automobile to the same degree it applies to such luggage in other locations." — 442 U.S. at 766. ^pin-766

## Application
The Arkansas Supreme Court had found ample probable cause to believe the suitcase held contraband, but no [[Exigent Circumstances and Hot Pursuit|exigency]]: with the police in control of the taxi and its occupants, there was no risk the suitcase would disappear before a warrant could issue. Because the luggage was already secured, the reasons that excuse a warrant for a moving vehicle did not apply, and the officers should have taken the suitcase to the station and obtained a warrant.

## Conclusion
The judgment of the Supreme Court of Arkansas — suppressing the evidence — was **affirmed**. Powell, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Overruled by [[California v. Acevedo]] (1991).** *Sanders* drew a line between the car (searchable on probable cause) and closed containers within it (protected). The Court abandoned that line: *[[United States v. Ross]]* (1982) held that probable cause to search a vehicle extends to containers inside that might hold the object of the search, and *[[California v. Acevedo|Acevedo]]* then unified the rule, expressly overruling *Sanders* so that police with probable cause may search a container found in a car without a warrant.

*Status note (⚪):* this page was authored from a CourtListener-verified identity stub; the overruled treatment above is well-settled but has not yet completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. It is preserved as **history**, never as live law.

## Appears on
- [[Automobile Exception]] — *Historical / origin*

## Sources
- [*Arkansas v. Sanders*, 442 U.S. 753 (1979)](https://www.courtlistener.com/opinion/110119/arkansas-v-sanders/) — pinpoint: 766 (Opinion of the Court; Powell, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Overruled by *California v. Acevedo*, 500 U.S. 565 (1991) (successor page: [[California v. Acevedo]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e2ec4a3e83ac6d28", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "442 U.S. 753 (1979)", "court": "U.S.", "neutral_cite": "1979 U.S. LEXIS 6", "official_citation_present": true, "parallel_cite": "99 S. Ct. 2586; 61 L. Ed. 2d 235", "title": "Arkansas v. Sanders", "year": "1979"}}
{"assertion_id": "1e938dbfbb678116", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Historical / origin", "title": "Arkansas v. Sanders"}}
{"assertion_id": "ccb8612932daa070", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment's warrant requirement applies to personal luggage taken from a lawfully stopped automobile to the same degree it applies to luggage elsewhere, so police may not search a suitcase seized from a car without a warrant absent exigency — a container rule later overruled by California v. Acevedo (1991).", "title": "Arkansas v. Sanders"}}
{"assertion_id": "5e9fa74292df8fcc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Arkansas v. Sanders", "varies_by_point": "false"}}
{"assertion_id": "a416b7d9f8751d5d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arkansas v. Sanders"}}
```

### lake record — Arkansas v. Sanders

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arkansas v. Sanders",
  "status": "under_review",
  "identity": {
    "case_name": "Arkansas v. Sanders",
    "case_name_short": "Sanders",
    "case_name_full": "Arkansas v. Sanders",
    "input_case_name": "Arkansas v. Sanders",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-20",
    "year": 1979,
    "docket": "77-1497",
    "cluster_id": 110119,
    "lead_opinion_id": 9427641,
    "sibling_ids": [],
    "absolute_url": "/opinion/110119/arkansas-v-sanders/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "442 U.S. 753",
      "volume": "442",
      "reporter": "U.S.",
      "page": "753",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2586",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 235",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 6",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "442 U.S. 753",
        "volume": "442",
        "reporter": "U.S.",
        "page": "753",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2586",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 235",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 6",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "442 U.S. 753",
    "official_selection": {
      "court_class": "scotus",
      "selected": "442 U.S. 753",
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
    "date_created": "2026-07-07T01:36:08Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "arkansas-v-sanders--110119",
      "to_record_id": "Arkansas v. Sanders",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Arkansas v. Sanders

```
<opinion type="majority">
<author id="b800-9">Me. Justice Powell</author>
<p id="A_Ph">delivered the opinion of the Court.</p>
<p id="Adc">This case presents the question whether, in the absence of exigent circumstances, police are required to obtain a warrant before searching luggage taken from an automobile properly stopped and searched for contraband. We took this case by writ of certiorari to the Supreme Court of Arkansas to resolve some apparent misunderstanding as to the application of our decision in <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), to warrantless searches of luggage seized from automobiles.<footnotemark>1</footnotemark></p>
<p id="b801-4"><page-number citation-index="1" label="755">*755</page-number>I</p>
<p id="b801-5">On April 23, 1976, Officer David Isom of the Little Rock, Ark., Police Department received word from an informant that at 4:35 that afternoon respondent would arrive aboard an American Airlines flight at gate No. 1 of the Municipal Airport of Little Rock. According to the informant, respondent would be carrying a green suitcase containing marihuana. Both Isom and the informant knew respondent well, as in January 1976 the informant had given the Little Rock Police Department information that had led to respondent’s arrest and conviction for possession of marihuana. Acting on the tip, Officer Isom and two other police officers placed the airport under surveillance. As the informant had predicted, respondent duly arrived at gate No. 1. The police watched as respondent deposited some hand luggage in a waiting taxicab, returned to the baggage claim area, and met a man whom police subsequently identified as David Rambo. While Rambo waited, respondent retrieved from the airline baggage service a green suitcase matching that described by the informant. Respondent gave this suitcase to his companion and went outside, where he entered the taxi into which he had put his luggage. Rambo waited a short while in the airport and then joined respondent in the taxi, after placing the green suitcase in the trunk of the vehicle.</p>
<p id="b801-6">When respondent’s taxi drove away carrying respondent, Rambo, and the suitcase, Officer Isom and one of his fellow officers gave pursuit and, with the help of a patrol car, stopped the vehicle several blocks from the airport. At the request of the police, the taxi driver opened the trunk of his vehicle, where the officers found the green suitcase. Without asking the permission of either respondent or Rambo, the police opened the unlocked suitcase and discovered what proved to be 9.3 pounds of marihuana packaged in 10 plastic bags.</p>
<p id="b801-7">On October 14, 1976, respondent and Rambo were charged with possession of marihuana with intent to deliver in viola<page-number citation-index="1" label="756">*756</page-number>tion of Ark. Stat. Ann. § 82-2617 (1976).<footnotemark>2</footnotemark> Before trial, respondent moved to suppress the evidence obtained from the suitcase, contending that the search violated his rights under the Fourth and Fourteenth Amendments. The trial court held a hearing on January 31, 1977, and denied the suppression motion without explanation. After respondent’s conviction by a jury on February 3, 1977, he was sentenced to 10 years in prison and was fined $15,000.</p>
<p id="b802-5">On appeal the Supreme Court of Arkansas reversed respondent’s conviction, ruling that the trial court should have suppressed the marihuana because it was obtained through an unlawful search of the suitcase. <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/" aria-description="Citation for case: Sanders v. State">262 Ark. 595</a></span>, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/" aria-description="Citation for case: Sanders v. State">559 S. W. 2d 704</a></span> (1977). Relying upon <em>United States </em>v. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra,</a></span> </em>and <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), the court concluded that a warrantless search generally must be supported by “probable cause coupled with exigent circumstances.” 262 Ark., at 599, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#706" aria-description="Citation for case: Sanders v. State">559 S. W. 2d, at 706</a></span>. In the present case, the court found there was ample probable cause for the police officers’ belief that contraband was contained in the suitcase they searched. The court found to be wholly lacking, however, any exigent circumstance justifying the officers’ failure to secure a warrant for the search of the luggage. With the police in control of the automobile and its occupants, there was no danger that the suitcase and its contents would be rendered unavailable to due legal process. The court concluded, therefore, that there was “nothing in this set of circumstances that would lend credence to an assertion of impracticality in obtaining a search warrant.” <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#600" aria-description="Citation for case: Sanders v. State"><em>Id., </em>at 600</a></span>, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#706" aria-description="Citation for case: Sanders v. State">559 S. W. 2d, at 706</a></span>.<footnotemark>3</footnotemark></p>
<p id="b803-4"><page-number citation-index="1" label="757">*757</page-number>II</p>
<p id="b803-5">Although the general principles applicable to claims of Fourth Amendment violations are well settled, litigation over requests for suppression of highly relevant evidence continues to occupy much of the attention of courts at all levels of the state and federal judiciary. Courts and law enforcement officials often find it difficult to discern the proper application of these principles to individual cases, because the circumstances giving rise to suppression requests can vary almost infinitely. Moreover, an apparently small difference in the factual situation frequently is viewed as a controlling difference in determining Fourth Amendment rights. The present case presents an example. Only two Terms ago, we held that a locked footlocker could not lawfully be searched without a warrant, even though it had been loaded into the trunk of an automobile parked at a curb. <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). In earlier cases, on the other hand, the Court sustained the constitutionality of warrantless searches of automobiles and their contents under what has become known as the “automobile exception” to the warrant requirement. See, e. <em>g., Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> <em>(1970); Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). We thus are presented with the task of determining whether the warrantless search of respondent's suitcase falls on the <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>or the <em>Chambers/Carroll </em>side of the Fourth Amendment line. Although in a sense this is a line-drawing process, it must be guided by established principles.</p>
<p id="b803-6">We commence with a summary of these principles. The Fourth Amendment protects the privacy and security of per<page-number citation-index="1" label="758">*758</page-number>sons in two important ways. First, it guarantees ''[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” In addition, this Court has interpreted the Amendment to include the requirement that normally searches of private property be performed pursuant to a search warrant issued in compliance with the Warrant Clause.<footnotemark>4</footnotemark> See, <em>e. g., Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978); <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 9</a></span>; <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972); <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span> (1925). In the ordinary case, therefore, a search of private property must be both reasonable and pursuant to a properly issued search warrant. The mere reasonableness of a search, assessed in the light of the surrounding circumstances, is not a substitute for the judicial warrant required under the Fourth Amendment. See <em>United States </em>v. <em>United States District <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">Court, supra.</a></span> </em>As the Court said in <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra,</a></span> </em>at 481:</p>
<blockquote id="b804-5">“The warrant requirement has been a valued part of our constitutional law for decades, and it has determined the result in scores and scores of cases in courts all over this country. It is not an inconvenience to be somehow 'weighed’ against the claims of police efficiency. It is, or should be, an important working part of our machinery of government, operating as a matter of course to check the 'well-intentioned but mistakenly overzealous executive officers’ who are a part of any system of law enforcement.”</blockquote>
<p id="b805-4"><page-number citation-index="1" label="759">*759</page-number>The prominent place the warrant requirement is given in our decisions reflects the “basic constitutional doctrine that individual freedoms will best be preserved through a separation of powers and division of functions among the different branches and levels of Government.” <em>United States </em>v. <em>United States District Court, supra, </em>at 317. By requiring that conclusions concerning probable cause and the scope of a search “be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime,” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948), we minimize the risk of unreasonable assertions of executive authority. See <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455-456</a></span> (1948).<footnotemark>5</footnotemark></p>
<p id="b805-5">Nonetheless, there are some exceptions to the warrant requirement. These have been established where it was concluded that the public interest required some flexibility in the application of the general rule that a valid warrant is a prerequisite for a search. See <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 555</a></span> (1976). Thus, a few “jealously and carefully drawn” <footnotemark>6</footnotemark> exceptions provide for those cases where the societal costs of obtaining a warrant, such as danger to law officers or the risk of loss or destruction of evidence, outweigh the reasons for prior recourse to a neutral magistrate. See <em>United States </em>v. <em>United States District Court, supra, </em>at 318. But because each exception to the warrant requirement invariably impinges to some extent on the protective purpose of <page-number citation-index="1" label="760">*760</page-number>the Fourth Amendment, the few situations in which a search may be conducted in the absence of a warrant have been carefully delineated and “the burden is on those seeking the exemption to show the need for it.” <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span> (1951). See <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 762</a></span> (1969); <em>Katz </em>v. <em>United States, supra, </em>at 357. Moreover, we have limited the reach of each exception to that which is necessary to accommodate the identified needs of society. See <em>Mincey </em>v. <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona"><em>Arizona, supra, </em>at 393</a></span>; <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#15" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 15</a></span>; <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#455" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 455</a></span>.</p>
<p id="b806-5">One of the circumstances in which the Constitution does not require a search warrant is when the police stop an automobile on the street or highway because they have probable cause to believe it contains contraband or evidence of a crime. See <em>United States </em>v. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><em>Martinez-Fuerte, supra, </em>at 561-562</a></span>; <em>United States </em>v. <em>Ortiz, </em><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#896" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 896</a></span> (1975); <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/#68" aria-description="Citation for case: Texas v. White">423 U. S. 67, 68</a></span> (1975). As the Court said in <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>:</p>
<blockquote id="b806-6">“[T]he guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant . ...”<footnotemark>7</footnotemark></blockquote>
<p id="b807-4"><page-number citation-index="1" label="761">*761</page-number>There are essentially two reasons for the distinction between automobiles and other private property. First, as the Court repeatedly has recognized, the inherent mobility of automobiles often makes it impracticable to obtain a warrant. See, <em>e. g., United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 12</a></span>; <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#49" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 49-50</a></span>; <em>Carroll </em>v. <em>United States, supra. </em>In addition, the configuration, use, and regulation of automobiles often may dilute the reasonable expectation of privacy that exists with respect to differently situated property. See <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#155" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 155</a></span> (1978) (Powell, J., concurring); <em>United States </em>v. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra;</a></span> South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1978); <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span> (1973); <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279</a></span> (1973) (Powell, J., concurring).</p>
<p id="b807-5">Ill</p>
<p id="b807-6">In the present case, the State argues that the warrantless search of respondent’s suitcase was proper under <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>and its progeny.<footnotemark>8</footnotemark> The police acted properly — indeed commendably — in apprehending respondent and his luggage. They had ample probable cause to believe that respondent’s green suitcase contained marihuana. A previously reliable informant had provided a detailed account of respondent’s expected arrival at the Little Rock Airport, which account proved to be accurate in every detail, including the color of the suitcase in which respondent would be carrying the marihuana. Having probable cause to believe that contraband was being driven away in the taxi, the police were justified in stopping the vehicle, searching it on the spot, and seizing the suitcase they suspected contained contraband. See <em>Chambers </em>v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney"><em>Maroney, supra, </em>at 52</a></span>. At oral argument, respondent conceded that the <page-number citation-index="1" label="762">*762</page-number>stopping of the taxi and the seizure of the suitcase were constitutionally unobjectionable. See Tr. of Oral Arg. 30, 44-46.</p>
<p id="b808-5">The only question, therefore, is whether the police, rather than immediately searching the suitcase without a warrant, should have taken it, along with respondent, to the police station and there obtained a warrant for the search. A lawful search of luggage generally may be performed only pursuant to a warrant. In <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>we declined an invitation to extend the <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>exception to all searches of luggage, noting that neither of the two policies supporting warrantless searches of automobiles applies to luggage. Here, as in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>the officers had seized the luggage and had it exclusively within their control at the time of the search. Consequently, “there was not the slightest danger that [the luggage] or its contents could have been removed before a valid search warrant could be obtained.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>. And, as we observed in that case, luggage is a common repository for one’s personal effects, and therefore is inevitably associated with the expectation of privacy. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Ibid.</a></span></em></p>
<p id="b808-6">The State argues, nevertheless, that the warrantless search of respondent’s suitcase was proper, not because the property searched was luggage, but rather because it was taken from an automobile lawfully stopped and searched on the street. In effect, the State would have us extend <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>to allow war-rantless searches of everything found within an automobile, as well as of the vehicle itself. As noted above, the Supreme Court of Arkansas found our decision in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>virtually controlling in this case.<footnotemark>9</footnotemark> The State contends, however, that <page-number citation-index="1" label="763">*763</page-number><em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>does not control because in that case the vehicle had remained parked at the curb where the footlocker had been placed in its trunk and that therefore no argument was made that the “automobile exception” was applicable. This Court has not had occasion previously to rule on the constitutionality of a warrantless search of luggage taken from an automobile lawfully stopped. Rather, the decisions to date have involved searches of some integral part of the automobile. See, <em>e. g., South Dakota </em>v. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#366" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 366</a></span> (glove compartment); <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/#68" aria-description="Citation for case: Texas v. White">423 U. S., at 68</a></span> (passenger compartment); <em>Cady </em>v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#437" aria-description="Citation for case: Cady v. Dombrowski"><em>Dombrowski, supra, </em>at 437</a></span> (trunk); <em>Chambers </em>v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#44" aria-description="Citation for case: Chambers v. Maroney"><em>Maroney, supra, </em>at 44</a></span> (concealed compartment under the dashboard); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#136" aria-description="Citation for case: Carroll v. United States">267 U. S., at 136</a></span> (behind the upholstering of the seats).</p>
<p id="b809-5">We conclude that the State has failed to carry its burden of demonstrating the need for warrantless searches of luggage properly taken from automobiles. A closed suitcase in the trunk of an automobile may be as mobile as the vehicle in which it rides. But as we noted in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>the exigency of mobility must be assessed at the point immediately before the search — after the police have seized the object to be searched and have it securely within their control.<footnotemark>10</footnotemark> See <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>. Once police have seized a suitcase, as they did here, the extent of its mobility is in no way affected by the place from which it was taken.<footnotemark>11</footnotemark> Accordingly, as a general rule there is <page-number citation-index="1" label="764">*764</page-number>no greater need for warrantless searches of luggage taken from automobiles than of luggage taken from other places.<footnotemark>12</footnotemark></p>
<p id="b810-5">Similarly, a suitcase taken from an automobile stopped on the highway is not necessarily attended by any lesser expectation of privacy than is associated with luggage taken from other locations. One is not less inclined to place private, personal possessions in a suitcase merely because the suitcase is to be carried in an automobile rather than transported by other means or temporarily checked or stored. Indeed, the very purpose of a suitcase is to serve as a repository for personal items when one wishes to transport them.<footnotemark>13</footnotemark> Accord<page-number citation-index="1" label="765">*765</page-number>ingly, the reasons for not requiring a warrant for the search of an automobile do not apply to searches of personal luggage taken by police from automobiles. We therefore find no justification for the extension of <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>and its progeny to the warrantless search of one’s personal luggage merely because it was located in an automobile lawfully stopped by the police.<footnotemark>14</footnotemark></p>
<p id="b812-4"><page-number citation-index="1" label="766">*766</page-number>In sum, we hold that the warrant requirement of the Fourth Amendment applies to personal luggage taken from an automobile to the same degree it applies to such luggage in other locations. Thus, insofar as the police are entitled to search such luggage without a warrant, their actions must be justified under some exception to the warrant requirement other than that applicable to automobiles stopped on the highway. Where — as in the present case — the police, without endangering themselves or risking loss of the evidence, lawfully have detained one suspected of criminal activity and secured his suitcase, they should delay the search thereof until after judicial approval has been obtained. In this way, constitutional rights of suspects to prior judicial review of searches will be fully protected.</p>
<p id="b812-5">The judgment of the Arkansas Supreme Court is</p>
<p id="b812-6">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b800-11"> Compare <em>United States </em>v. <em>Finnegan, </em><span class="citation" data-id="351991"><a href="/opinion/351991/united-states-v-gary-charles-finnegan/#641" aria-description="Citation for case: United States v. Gary Charles Finnegan">568 F. 2d 637, 641-642</a></span> (CA9 1977), with <em>United States </em>v. <em>Stevie, </em><span class="citation" data-id="9465095"><a href="/opinion/359034/united-states-v-robert-charles-stevie-united-states-of-america-v-raymond/#1178" aria-description="Citation for case: United States v. Robert Charles Stevie, United States of...">582 F. 2d 1175, 1178-1179</a></span> (CA8 1978) (en banc).</p>
</footnote>
<footnote label="2">
<p id="b802-6"> In addition <em>to the </em>marihuana found in the suitcase, <em>police officers </em>found one ounce of heroin hidden in their patrol car after transporting Rambo to police headquarters. Accordingly, Rambo also was charged with possession of heroin with intent to deliver. Immediately before trial on both counts, the court severed the heroin-possession count for later trial.</p>
</footnote>
<footnote label="3">
<p id="b802-7"> “With the suitcase safely immobilized, it was unreasonable to under<page-number citation-index="1" label="757">*757</page-number>take the additional and greater intrusion of a search without a warrant.” 262 Ark., at 601, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#707" aria-description="Citation for case: Sanders v. State">559 S. W. 2d, at 707</a></span>. The court also rejected the State's contention that luggage is entitled to a lesser protection against warrantless searches than are other private areas, such as homes. It noted that suitcases, unlike automobiles, customarily are the repositories for personal effects.</p>
</footnote>
<footnote label="4">
<p id="b804-6"> The Warrant Clause of <em>the </em>Fourth Amendment provides that “no Warrants shall issue but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched and the persons or things to be seized.” The Fourth Amendment has been made fully applicable to the States by the Fourteenth Amendment. See <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949). In this opinion we refer to the Fourth Amendment as it so applies to the State of Arkansas.</p>
</footnote>
<footnote label="5">
<p id="b805-6"> The need for a carefully drawn, limited warrant for searches of private premises was the product in large part of the colonists’ resentment of the writs of assistance to which they were subjected by the English. See <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#8" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 8</a></span> (1977); J. Landynski, Search and Seizure and the Supreme Court 19 (1966); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 51-78 (1937). Mr. Justice Frankfurter went so far as to suggest that abuses of the writs of assistance were “so deeply felt by the Colonies as to be one of the potent causes of the Revolution.” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#69" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 69</a></span> (1950) (dissenting opinion).</p>
</footnote>
<footnote label="6">
<p id="b805-7"> <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958).</p>
</footnote>
<footnote label="7">
<p id="b806-7"> The willingness of courts to excuse the absence of a warrant where spontaneous searches are required of a vehicle on the road has led to what is called the “automobile exception” to the warrant requirement, although the exception does not invariably apply whenever automobiles are searched. See, <em>e. g., Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#461" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 461-462</a></span> (1971) (“The word 'automobile' is not a talisman in whose presence the Fourth Amendment fades away and disappears”). See generally Moylan, The Automobile Exception: What it is and What it is not — A Rationale in Search of a Clearer Label, <span class="citation no-link">27 Mercer L. Rev. 987</span> (1976).</p>
</footnote>
<footnote label="8">
<p id="b807-7"> Respondent concedes that the suitcase was his property, see Brief for Respondent 3, and so there is no question of his standing to challenge the search. See <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#387" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 387-388</a></span> (1968). Cf. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#148" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 148-149</a></span> (1978).</p>
</footnote>
<footnote label="9">
<p id="b808-7"> The facts of the two cases are similar in several critical respects. In <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>a locked, 200-pound footlocker was searched without a warrant after the police, acting with probable cause, had taken it from the trunk of a parked automobile. In the present case, respondent’s comparatively small, unlocked suitcase also had been placed in the trunk of an automobile and was searched without a warrant by police acting upon probable cause. We do not view the difference in the sizes of the footlocker and suitcase as material here; nor did respondent’s failure to lock his suitcase alter its <page-number citation-index="1" label="763">*763</page-number>fundamental character as a repository for personal, private effects. Cf. Note, A Reconsideration of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>Expectation of Privacy Test, <span class="citation no-link">76 Mich. L. Rev. 154</span>, 170 (1977).</p>
</footnote>
<footnote label="10">
<p id="b809-7"> The difficulties in seizing and securing automobiles have led the Court to make special allowances for their search. See n. 14, <em>infra.</em></p>
</footnote>
<footnote label="11">
<p id="b809-8"> There may be cases in which the special exigencies of the situation would justify the warrantless search of a suitcase. Cf. <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973) (police had reason to suspect automobile trunk contained a weapon). Generally, however, such exigencies will depend upon the probable contents of the luggage and the suspect’s access to those contents — not upon whether the luggage is taken from an automobile. In <page-number citation-index="1" label="764">*764</page-number>the present case the State has conceded that there were no special exigencies. See Tr. of Oral Arg. 16.</p>
<p id="b810-7">Nor do we consider the constitutionality of searches of luggage incident to the arrest of its possessor. See, e. <em>g., United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973). The State has not argued that respondent's suitcase was searched incident to his arrest, and it appears'that the bag was not within his “immediate control” at the time of the search.</p>
</footnote>
<footnote label="12">
<p id="b810-8"> We have recognized that personal property brought into the country may be searched at the border under circumstances that would not otherwise justify a warrantless search. See <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616-617</a></span> (1977). Arkansas does not assert, however, that the search of respondent’s luggage was a border search. Moreover, it may be that the public safety requires luggage to be searched without a warrant in some circumstances — such as when luggage is about to be placed onto an airplane. This presents questions under the Fourth Amendment wholly absent from the present case.</p>
<p id="b810-9">It is beyond question that the police easily could have obtained a warrant to search respondent’s bag if they had taken the suitcase to a magistrate. They had probable cause to believe not only that respondent was carrying marihuana, but also that the contraband was contained in the suitcase that they seized. The State argues that under the circumstances of this case inconvenience to all concerned would have been the only result of deferring search of the suitcase until a warrant was obtained. Those in respondent’s position who find such inconvenience unacceptable may avoid it simply by consenting to the search.</p>
</footnote>
<footnote label="13">
<p id="b810-10"> Not all containers and packages found by police during the course of a search will deserve the full protection of the Fourth Amendment. Thus, some containers (for example a kit of burglar tools or a gun case) by their <page-number citation-index="1" label="765">*765</page-number>very nature cannot support any reasonable expectation of privacy because their contents can be inferred from their outward appearance. Similarly, in some cases the contents of a package will be open to “plain view,” thereby obviating the need for a warrant. See <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968) <em>(per curiam). </em>There will be difficulties in determining which parcels taken from an automobile require a warrant for their search and which do not. Our decision in this case means only that a warrant generally is required before personal luggage can be searched and that the extent to which the Fourth Amendment applies to containers and other parcels depends not at all upon whether they are seized from an automobile.</p>
</footnote>
<footnote label="14">
<p id="b811-6"> We are not persuaded by the State’s argument that, under <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), if the police were entitled to seize the suitcase, then they were entitled to search it. In <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>, </em>the Court upheld the warrantless search of an automobile stopped on the highway by police who believed that its occupants had robbed a gasoline station a short time before. The Court recognized that “[a]rguably, because of the preference for a magistrate’s judgment, only the immobilization of the car should be permitted until a search warrant is obtained <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><em>Id., </em>at 51</a></span>. Nonetheless, the Court ruled that a warrantless search was permissible, concluding that there was no constitutional difference between the intrusion of seizing and holding the automobile until a warrant could be obtained, on the one hand, and searching the vehicle without a warrant, on the other.</p>
<p id="b811-8">We view, however, the seizure of a suitcase as quite different from the seizure of an automobile. In <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>, </em>if the Court had required seizure and holding of the vehicle, it would have imposed a constitutional requirement upon police departments of all sizes around the country to have available the people and equipment necessary to transport impounded automobiles to some central location until warrants could be secured. Moreover, once seized automobiles were taken from the highway the police would be responsible for providing some appropriate location where they could be kept, with due regard to the safety of the vehicles and their contents, until a magistrate ruled on the application for a warrant. Such <page-number citation-index="1" label="766">*766</page-number>a constitutional requirement therefore would have imposed severe, even impossible, burdens on many police departments. See Note, Warrant-less Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span>, 841-842 (1974). No comparable burdens are likely to exist with respect to the seizure of personal luggage.</p>
</footnote>
</opinion>
```

---
