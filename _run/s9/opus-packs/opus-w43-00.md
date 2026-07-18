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

## GROUP: content/cases/New York v. Harris.md  (`case`, 7 assertions)

### content_page

```
---
title: "New York v. Harris"
type: case
citation: "495 U.S. 14 (1990)"
parallel_cite: "110 S. Ct. 1640; 109 L. Ed. 2d 13; 58 U.S.L.W. 4457"
neutral_cite: 1990 U.S. LEXIS 2037
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-04-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-04-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Harris
  varies_by_point: false
  scope_note: "Good law. Where police have probable cause to arrest, a Payton violation (warrantless in-home arrest) does not require suppression of a statement the suspect later makes outside the home; the exclusionary remedy reaches only what is gathered inside the home. Distinct from the reversed-party case Harris v. New York, 401 U.S. 222 (1971) (Miranda impeachment)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112413/new-york-v-harris/"
  cluster_id: 112413
  opinion_id: 9431975
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Limiting"
  - page: "[[Entry to Arrest]]"
    role: "Limiting"
  - page: "[[Fruits & Attenuation]]"
    role: "Related (cross-doctrine)"
related: ["[[Payton v. New York]]", "[[Brown v. Illinois]]", "[[Wong Sun v. United States]]", "[[Kirk v. Louisiana]]"]
aliases: ["New York v. Harris (1990)"]
tags: ["case", "fourth-amendment", "arrest-in-the-home", "exclusionary-rule", "payton-violation", "fruit-of-the-poisonous-tree"]
holding: "Where police have probable cause to arrest, a Payton violation does not require suppression of a statement the suspect makes outside his home; such a statement is not the fruit of the in-home location of the arrest."
lake:
  record_id: New York v. Harris
  status: verified
  projected_at: 2026-07-06
---

# New York v. Harris

*495 U.S. 14 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police had probable cause to believe Bernard Harris had murdered Thelma Staton. Without an arrest warrant and without consent or [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], three officers entered Harris's home, read him his *[[Miranda v. Arizona|Miranda]]* rights, and obtained an admission inside the home (a *[[Payton v. New York|Payton]]* violation; that in-home statement was suppressed, which the State conceded). They then took Harris to the station house, again administered *[[Miranda v. Arizona|Miranda]]* warnings, and Harris signed a written inculpatory statement. New York's courts suppressed the station-house statement as the fruit of the unlawful in-home arrest.

## Issue
Whether the exclusionary rule requires suppression of a statement a defendant makes at the police station, after a warrantless in-home arrest that violated *[[Payton v. New York|Payton]]*, when the police had probable cause to arrest him.

## Rule
No. "We hold that, where the police have probable cause to arrest a suspect, the exclusionary rule does not bar the State's use of a statement made by the defendant outside of his home, even though the statement is taken after an arrest made in the home in violation of *Payton*." — 495 U.S. at 21. ^pin-21

*[[Payton v. New York|Payton]]*'s remedy is tied to its purpose — protecting the home: "*Payton* was designed to protect the physical integrity of the home; it was not intended to grant criminal suspects, like Harris, protection for statements made outside their premises where the police have probable cause to arrest the suspect for committing a crime." — *Id.* at 17. ^pin-17

The station-house statement therefore was not suppressible: "Harris' statement taken at the police station was not the product of being in unlawful custody. Neither was it the fruit of having been arrested in the home rather than someplace else." — *Id.* at 19. ^pin-19

## Application
Because the officers had probable cause, Harris was in *lawful* custody once removed from the house, properly Mirandized, and allowed to talk; the warrantless entry's only unlawful product — what the police gained by arresting him *inside* the home (the in-home statement) — was already suppressed, vindicating *[[Payton v. New York|Payton]]*'s purpose. The station-house statement was neither the product of unlawful custody nor the fruit of the in-home location of the arrest. This distinguishes *[[Brown v. Illinois]]*, *[[Dunaway v. New York|Dunaway]]*, and *[[Taylor v. Alabama|Taylor]]*, where confessions were suppressed because the police lacked probable cause and the detention itself was illegal.

## Conclusion
With probable cause to arrest, a *[[Payton v. New York|Payton]]* violation does not require suppression of a statement made outside the home; the New York suppression of the station-house statement was reversed. The exclusionary remedy for a *[[Payton v. New York|Payton]]* violation reaches only the evidence obtained from the in-home arrest itself.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *New York v. Harris* limits the exclusionary consequences of [[Payton v. New York]] (reaffirmed in [[Kirk v. Louisiana]]) and turns on the presence of probable cause — contrast [[Brown v. Illinois]] (confession suppressed where the arrest lacked probable cause) and the [[Fruits and Attenuation|attenuation]] framework of [[Wong Sun v. United States]].
- *Disambiguation:* distinct from the reversed-party case *[[Harris v. New York]]*, 401 U.S. 222 (1971) (statements taken in violation of *[[Miranda v. Arizona|Miranda]]* may impeach a testifying defendant).

## Appears on
- [[Arrest in the Home]] — *Limiting*
- [[Entry to Arrest]] — *Limiting*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *New York v. Harris*, 495 U.S. 14 (1990) — https://www.courtlistener.com/opinion/112413/new-york-v-harris/ — pinpoints: 17, 19, 21.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4565e9bb55768548", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "495 U.S. 14 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 2037", "official_citation_present": true, "parallel_cite": "110 S. Ct. 1640; 109 L. Ed. 2d 13; 58 U.S.L.W. 4457", "title": "New York v. Harris", "year": "1990"}}
{"assertion_id": "7f333187d964c823", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where police have probable cause to arrest, a Payton violation does not require suppression of a statement the suspect makes outside his home; such a statement is not the fruit of the in-home location of the arrest.", "title": "New York v. Harris"}}
{"assertion_id": "92228534ff62b429", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Limiting", "title": "New York v. Harris"}}
{"assertion_id": "93e0c5240cbc660f", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Related (cross-doctrine)", "title": "New York v. Harris"}}
{"assertion_id": "c69400b5cc8099b4", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Limiting", "title": "New York v. Harris"}}
{"assertion_id": "a1b8694e8a4b1969", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-04-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "New York v. Harris", "field_i_validity": "good_law", "scope_note": "Good law. Where police have probable cause to arrest, a Payton violation (warrantless in-home arrest) does not require suppression of a statement the suspect later makes outside the home; the exclusionary remedy reaches only what is gathered inside the home. Distinct from the reversed-party case Harris v. New York, 401 U.S. 222 (1971) (Miranda impeachment).", "title": "New York v. Harris", "varies_by_point": "false"}}
{"assertion_id": "e00dba1f83ce9602", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "New York v. Harris"}}
```

### lake record — New York v. Harris

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Harris",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Harris",
    "case_name_short": "Harris",
    "case_name_full": "New York v. Harris",
    "input_case_name": "New York v. Harris",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-04-18",
    "year": 1990,
    "docket": null,
    "cluster_id": 112413,
    "lead_opinion_id": 9431975,
    "sibling_ids": [
      112413,
      9431975,
      9431976
    ],
    "absolute_url": "/opinion/112413/new-york-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "495 U.S. 14",
      "volume": "495",
      "reporter": "U.S.",
      "page": "14",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 1640",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1640",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 13",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "13",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4457",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4457",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 2037",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2037",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "495 U.S. 14",
        "volume": "495",
        "reporter": "U.S.",
        "page": "14",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1640",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1640",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 13",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "13",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 2037",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2037",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4457",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4457",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "495 U.S. 14",
    "official_selection": {
      "court_class": "scotus",
      "selected": "495 U.S. 14",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-21",
      "page": null,
      "quote": "--- # New York v. Harris *495 U.S. 14 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police had probable cause to believe Bernard Harris had murdered Thelma Staton. Without an arrest warrant and without consent or exigent circumstances, three officers entered Harris's home, read him his *Miranda* rights, and obtained an admission inside the home (a *Payton* violation; that in-home statement was suppressed, which the State conceded). They then took Harris to the station house, again administered *Miranda* warnings, and Harris signed a written inculpatory statement. New York's courts suppressed the station-house statement as the fruit of the unlawful in-home arrest. ## Issue Whether the exclusionary rule requires suppression of a statement a defendant makes at the police station, after a warrantless in-home arrest that violated *Payton*, when the police had probable cause to arrest him. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-17",
      "page": null,
      "quote": "*Payton* was designed to protect the physical integrity of the home; it was not intended to grant criminal suspects, like Harris, protection for statements made outside their premises where the police have probable cause to arrest the suspect for committing a crime.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-19",
      "page": null,
      "quote": "Harris' statement taken at the police station was not the product of being in unlawful custody. Neither was it the fruit of having been arrested in the home rather than someplace else.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-04-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Harris",
    "varies_by_point": false,
    "scope_note": "Good law. Where police have probable cause to arrest, a Payton violation (warrantless in-home arrest) does not require suppression of a statement the suspect later makes outside the home; the exclusionary remedy reaches only what is gathered inside the home. Distinct from the reversed-party case Harris v. New York, 401 U.S. 222 (1971) (Miranda impeachment).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Serrano-Acevedo",
          "cluster_id": 4506969,
          "cite": [
            "892 F.3d 454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
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
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jenkins",
          "cluster_id": 2444991,
          "cite": [
            "3 A.3d 806",
            "298 Conn. 209",
            "2010 Conn. LEXIS 304"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Molina",
          "cluster_id": 6578709,
          "cite": [
            "439 Mass. 206",
            "786 N.E.2d 1191",
            "2003 Mass. LEXIS 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Nieto",
          "cluster_id": 6346309,
          "cite": [
            "192 Misc. 2d 537",
            "746 N.Y.S.2d 371",
            "2002 N.Y. Misc. LEXIS 979"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Patrick Flores Oaxaca",
          "cluster_id": 771307,
          "cite": [
            "233 F.3d 1154",
            "2000 Cal. Daily Op. Serv. 9159",
            "2000 Daily Journal DAR 12172",
            "2000 U.S. App. LEXIS 28971",
            "2000 WL 1701453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
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
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 2347917,
          "cite": [
            "256 S.W.3d 264",
            "2008 Tex. Crim. App. LEXIS 754",
            "2008 WL 2437667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ballard",
          "cluster_id": 1533349,
          "cite": [
            "987 S.W.2d 889",
            "1999 Tex. Crim. App. LEXIS 14",
            "1999 WL 89535"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Geisler",
          "cluster_id": 7894925,
          "cite": [
            "222 Conn. 672",
            "610 A.2d 1225",
            "61 U.S.L.W. 2093",
            "1992 Conn. LEXIS 214"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Louis Lalonde v. County of Riverside, Robert Moquin, and Jason Horton, Opinion",
          "cluster_id": 767803,
          "cite": [
            "204 F.3d 947",
            "2000 Daily Journal DAR 2031",
            "2000 Cal. Daily Op. Serv. 1433",
            "2000 U.S. App. LEXIS 2778",
            "2000 WL 217552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Riley",
          "cluster_id": 1367783,
          "cite": [
            "846 P.2d 1365",
            "121 Wash. 2d 22",
            "1993 Wash. LEXIS 66"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 1057155,
          "cite": [
            "2013 IL 114040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Snider",
          "cluster_id": 1746280,
          "cite": [
            "608 N.W.2d 502",
            "239 Mich. App. 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huddleston",
          "cluster_id": 2435833,
          "cite": [
            "924 S.W.2d 666",
            "1996 Tenn. LEXIS 387",
            "1996 WL 328642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ernest Martin v. Betty Mitchell, Warden",
          "cluster_id": 776544,
          "cite": [
            "280 F.3d 594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thurman",
          "cluster_id": 1367765,
          "cite": [
            "846 P.2d 1256",
            "203 Utah Adv. Rep. 18",
            "1993 Utah LEXIS 40",
            "1993 WL 4794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
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
        "journal_ref": "New York v. Harris:lane2_top_cited"
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
        "journal_ref": "New York v. Harris:lane2_top_cited"
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
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Osvaldo Rodriguez-Morales",
          "cluster_id": 558566,
          "cite": [
            "929 F.2d 780",
            "1991 U.S. App. LEXIS 4854",
            "1991 WL 40569"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 2012814,
          "cite": [
            "927 N.E.2d 1179",
            "237 Ill. 2d 81",
            "340 Ill. Dec. 168",
            "2010 Ill. LEXIS 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. Nevada",
          "cluster_id": 117833,
          "cite": [
            "128 L. Ed. 2d 1",
            "114 S. Ct. 1280",
            "511 U.S. 79",
            "1994 U.S. LEXIS 2655"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCauley",
          "cluster_id": 2127673,
          "cite": [
            "645 N.E.2d 923",
            "163 Ill. 2d 414",
            "206 Ill. Dec. 671",
            "63 U.S.L.W. 2476",
            "1994 Ill. LEXIS 175"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lovejoy",
          "cluster_id": 2162437,
          "cite": [
            "919 N.E.2d 843",
            "235 Ill. 2d 97",
            "335 Ill. Dec. 818",
            "2009 Ill. LEXIS 1302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Busby v. State",
          "cluster_id": 2390040,
          "cite": [
            "990 S.W.2d 263",
            "1999 Tex. Crim. App. LEXIS 26",
            "1999 WL 172911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Othoudt",
          "cluster_id": 2185300,
          "cite": [
            "482 N.W.2d 218",
            "1992 Minn. LEXIS 73",
            "1992 WL 45841"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Perry",
          "cluster_id": 2390579,
          "cite": [
            "590 A.2d 624",
            "124 N.J. 128",
            "1991 N.J. LEXIS 45"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Canez",
          "cluster_id": 867610,
          "cite": [
            "42 P.3d 564",
            "202 Ariz. 133"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. State",
          "cluster_id": 2385168,
          "cite": [
            "932 S.W.2d 502",
            "1996 Tex. Crim. App. LEXIS 193",
            "1996 WL 512397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Harris",
          "cluster_id": 5690319,
          "cite": [
            "77 N.Y.2d 434",
            "568 N.Y.S.2d 702",
            "570 N.E.2d 1051",
            "1991 N.Y. LEXIS 210"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112413 OR 9431975 OR 9431976) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NTA3NDU2MDAwMDAmcz0yMDQwMDc4JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112413+OR+9431975+OR+9431976%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112413 OR 9431975 OR 9431976)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTE5ODcyNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112413+OR+9431975+OR+9431976%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112413 OR 9431975 OR 9431976)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112413 OR 9431975 OR 9431976)",
    "indexed_citing_opinions": 428,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112413,
        "count": 372,
        "count_source": "search"
      },
      {
        "opinion_id": 9431975,
        "count": 67,
        "count_source": "search"
      },
      {
        "opinion_id": 9431976,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 659,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-harris.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0MTM5OTQmcz02MjQwNzAzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112413+OR+9431975+OR+9431976%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112413,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 112136,
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
    "date_created": "2026-07-05T15:43:14Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Harris

```
<opinion type="majority">
<author id="b71-10">Justice White</author>
<p id="AuY">delivered the opinion of the Court.</p>
<p id="b71-11">On January 11, 1984, New York City police found the body of Ms. Thelma Staton murdered in her apartment. Various facts gave the officers probable cause to believe that the respondent in this case, Bernard Harris, had killed Ms. Staton. As a result, on January 16, 1984, three police officers went to Harris’ apartment to take him into custody. They did not first obtain an arrest warrant.</p>
<p id="b71-12">When the police arrived, they knocked on the door, displaying their guns and badges. Harris let them enter. <page-number citation-index="1" label="16">*16</page-number>Once inside, the officers read Harris his rights under <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Harris acknowledged that he understood the warnings, and agreed to answer the officers’ questions. At that point, he reportedly admitted that he had killed Ms. Staton.</p>
<p id="b72-5">Harris was arrested, taken to the station house, and again informed of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. He then signed a written inculpatory statement. The police subsequently read Harris the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings a third time and videotaped an incriminating interview between Harris and a district attorney, even though Harris had indicated that he wanted to end the interrogation.</p>
<p id="b72-6">The trial court suppressed Harris’ first and third statements; the State does not challenge those rulings. The sole issue in this case is whether Harris’ second statement — the written statement made at the station house — should have been suppressed because the police, by entering Harris’ home without a warrant and without his consent, violated <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), which held that the Fourth Amendment prohibits the police from effecting a warrantless and nonconsensual entry into a suspect’s home in order to make a routine felony arrest. The New York trial court concluded that the statement was admissible. Following a bench trial, Harris was convicted of second-degree murder. The Appellate Division affirmed, 124 App. Div. 2d 472, 507 N. Y. S. 2d 823 (1986).</p>
<p id="b72-7">A divided New York Court of Appeals reversed, 72 N. Y. 2d 614, <span class="citation" data-id="5538549"><a href="/opinion/5689309/people-v-harris/" aria-description="Citation for case: People v. Harris">532 N. E. 2d 1229</a></span> (1988). That court first accepted the trial court’s finding that Harris did not consent to the police officers’ entry into his home and that the warrantless arrest therefore violated <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>even though there was probable cause. Applying <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), and its progeny, the court then determined that the station house statement must be deemed to be the inadmissible fruit of the illegal arrest because the connection between the statement and the arrest was not sufficiently attenuated. <page-number citation-index="1" label="17">*17</page-number>The court noted that some courts had reasoned that the “wrong in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>cases . . . lies not in the arrest, ‘but in the unlawful <em>entry </em>into a dwelling without proper judicial authorization’ ” and had therefore declined to suppress confessions that were made following <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violations. 72 N. Y. 2d, at 623, <span class="citation" data-id="5538549"><a href="/opinion/5689309/people-v-harris/#1234" aria-description="Citation for case: People v. Harris">532 N. E. 2d, at 1234</a></span>. The New York court disagreed with this analysis, finding it contrary to <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and its own decisions interpreting <em>Payton’s, </em>scope. We granted certiorari to resolve the admissibility of the station house statement. <span class="citation multiple-matches"><a href="/c/U.%20S./490/1018/">490 U. S. 1018</a></span> (1989).</p>
<p id="b73-5">For present purposes, we accept the finding below that Harris did not consent to the police officers’ entry into his home and the conclusion that the police had probable cause to arrest him. It is also evident, in light of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>that arresting Harris in his home without an arrest warrant violated the Fourth Amendment. But, as emphasized in earlier cases, “we have declined to adopt a <em>‘per se </em>or “but for” rule’ that would make inadmissible any. evidence, whether tangible or five-witness testimony, which somehow came to fight through a chain of causation that began with an illegal arrest.” <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#276" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 276</a></span> (1978). Rather, in this context, we have stated that “[t]he penalties visited upon the Government, and in turn upon the public, because its officers have violated the law must bear some relation to the purposes which the law is to serve. ” <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#279" aria-description="Citation for case: United States v. Ceccolini">Id., at 279</a></span>. In fight of these principles, we decline to apply the exclusionary rule in this context because the rule in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>was designed to protect the physical integrity of the home; it was not intended to grant criminal suspects, like Harris, protection for statements made outside their premises where the police have probable cause to arrest the suspect for committing a crime.</p>
<p id="b73-6"><em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>itself emphasized that our holding in that case stemmed from the “overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York">445 U. S., at 601</a></span>. Although it had <page-number citation-index="1" label="18">*18</page-number>long been settled that a warrantless arrest in a public place was permissible as long as the arresting officer had probable cause, see <em>United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>nevertheless drew a line at the entrance to the home. This special solicitude was necessary because ‘“physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed.’” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S., at 585</a></span> (citation omitted). The arrest warrant was required to “interpose the magistrate’s determination of probable cause” to arrest before the officers could enter a house to effect an arrest. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 602-603</a></span>.</p>
<p id="b74-5">Nothing in the reasoning of that case suggests that an arrest in a home without a warrant but with probable cause somehow renders unlawful continued custody of the suspect once he is removed from the house. There could be no valid claim here that Harris was immune from prosecution because his person was the fruit of an illegal arrest. <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#474" aria-description="Citation for case: United States v. Crews">445 U. S. 463, 474</a></span> (1980). Nor is there any claim that the warrantless arrest required the police to release Harris or that Harris could not be immediately rearrested if momentarily released. Because the officers had probable cause to arrest Harris for a crime, Harris was not unlawfully in custody when he was removed to the station house, given <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, and allowed to talk. For Fourth Amendment purposes, the legal issue is the same as it would be had the police arrested Harris on his doorstep, illegally entered his home to search for evidence, and later interrogated Harris at the station house. Similarly, if the police had made a warrantless entry into Harris’ home, not found him there, but arrested him on the street when he returned, a later statement made by him after proper warnings would no doubt be admissible.</p>
<p id="b74-6">This case is therefore different from <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), and <em>Taylor </em>v. <em>Alabama, </em><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">457 U. S. 687</a></span> (1982). In each of those cases, evidence obtained from a criminal de<page-number citation-index="1" label="19">*19</page-number>fendant following arrest was suppressed because the police lacked probable cause. The three cases stand for the familiar proposition that the indirect fruits of an illegal search or arrest should be suppressed when they bear a sufficiently close relationship to the underlying illegality. See also <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). We have emphasized, however, that attenuation analysis is only appropriate where, as a threshold matter, courts determine that “the challenged evidence is in some sense the product of illegal governmental activity.” <em>United States </em>v. <span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#471" aria-description="Citation for case: United States v. Crews"><em>Crews, supra, </em>at 471</a></span>. As Judge Titone, concurring in the judgment on the basis of New York state precedent, cogently argued below, “[i]n cases such as <em>Brown </em>v. <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois (supra)</a></span> </em>and its progeny, an affirmative answer to that preliminary question may be assumed, since the ‘illegality’ is the absence of probable cause and the wrong consists of the police’s having control of the defendant’s person at the time he made the challenged statement. In these cases, the ‘challenged <em>evidence’ </em>— i. <em>e., </em>the post arrest confession — is unquestionably ‘the product,of [the] illegal governmental <em>activity’ </em>— i. <em>e., </em>the wrongful detention.” 72 N. Y. 2d, at 625, <span class="citation" data-id="5538549"><a href="/opinion/5689309/people-v-harris/#1235" aria-description="Citation for case: People v. Harris">532 N. E. 2d, at 1235</a></span>.</p>
<p id="b75-5">Harris’ statement taken at the police station was not the product of being in unlawful custody. Neither was it the fruit of having been arrested in the home rather than someplace else. The case is analogous to <em>United States </em>v. <em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/" aria-description="Citation for case: United States v. Crews">Crews, supra.</a></span> </em>In that case, we refused to suppress a victim’s in-court identification despite the defendant’s illegal arrest. The Court found that the evidence was not “‘come at by exploitation’ of . . . the defendant’s Fourth Amendment rights,” and that it was not necessary to inquire whether the “taint” of the Fourth Amendment violation was sufficiently attenuated to permit the introduction of the evidence. 445 U. S., at 471. Here, likewise, the police had a justification to question Harris prior to his arrest; therefore, his subsequent statement was not an exploitation of the illegal entry into Harris’ home.</p>
<p id="b76-4"><page-number citation-index="1" label="20">*20</page-number>We do not hold, as the dissent suggests, that a statement taken by the police while a suspect is in custody is always admissible as long as the suspect is in legal custody. Statements taken during legal custody would of course be inadmissible, for example, if they were the product of coercion, if <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were not given, or if there was a violation of the rule of <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). We do hold that the station house statement in this case was admissible because Harris was in legal custody, as the dissent concedes, and because the statement, while the product of an arrest and being in custody, was not the fruit of the fact that the arrest was made in the house rather than someplace else.</p>
<p id="b76-5">To put the matter another way, suppressing the statement taken outside the house would not serve the purpose of the rule that made Harris’ in-house arrest illegal. The warrant requirement for an arrest in the home is imposed to protect the home, and anything incriminating the police gathered from arresting Harris in his home, rather than elsewhere, has been excluded, as it should have been; the purpose of the rule has thereby been vindicated. We are not required by the Constitution to go further and suppress statements later made by Harris in order to deter police from violating <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>“As cases considering the use of unlawfully obtained evidence in criminal trials themselves make clear, it does not follow from the emphasis on the exclusionary rule’s deterrent value that ‘anything which deters illegal searches is thereby commanded by the Fourth Amendment.’” <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#910" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 910</a></span> (1984) (citation omitted). Even though we decline to suppress statements made outside the home following a <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation, the principal incentive to obey <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>still obtains: the police know that a warrant-less entry will lead to the suppression of any evidence found, or statements taken, inside the home. If we did suppress statements like Harris’, moreover, the incremental deterrent value would be minimal. Given that the police have probable cause to arrest a suspect in Harris’ position, they need <page-number citation-index="1" label="21">*21</page-number>not violate <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>in order to interrogate the suspect. It is doubtful therefore that the desire to secure a statement from a criminal suspect would motivate the police to violate <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>As a result, suppressing a station house statement obtained after a <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation will have little effect on the officers’ actions, one way or another.</p>
<p id="b77-5">We hold that, where the police have probable cause to arrest a suspect, the exclusionary rule does not bar the State’s use of a statement made by the defendant outside of his home, even though the statement is taken after an arrest made in the home in violation of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>The judgment of the court below is accordingly</p>
<p id="b77-6">
<em>Reversed.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/Steagald v. United States.md  (`case`, 7 assertions)

### content_page

```
---
title: "Steagald v. United States"
type: case
citation: "451 U.S. 204 (1981)"
parallel_cite: "101 S. Ct. 1642; 68 L. Ed. 2d 38; 49 U.S.L.W. 4418"
neutral_cite: 1981 U.S. LEXIS 89
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-04-21
docket: 79-6777
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Steagald v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110464/steagald-v-united-states/"
  cluster_id: 110464
  opinion_id: 9428299
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Entry to Arrest]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Securing the Scene]]"
    role: "Related (cross-doctrine)"
related: ["[[Payton v. New York]]", "[[Bailey v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-warrant", "search-warrant", "third-party-home"]
holding: "To search a THIRD PARTY'S home for the subject of an arrest warrant, police need a SEARCH warrant (absent exigency or consent); an…"
lake:
  record_id: Steagald v. United States
  status: verified
  projected_at: 2026-07-06
---

# Steagald v. United States

*451 U.S. 204 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Armed with an arrest warrant for fugitive Ricky Lyons, DEA agents entered and searched Steagald's home—where they believed Lyons might be found—without a search warrant and without Steagald's consent. They did not find Lyons but found cocaine, and Steagald, who was not named in the arrest warrant, was convicted.

## Issue
Whether an arrest warrant for one person justifies entering and searching a third party's home, without that person's consent and absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], to look for the subject of the arrest warrant.

## Rule
An arrest warrant does not authorize searching a third party's home. "The issue in this case is whether, under the Fourth Amendment, a law enforcement officer may legally search for the subject of an arrest warrant in the home of a third party without first obtaining a search warrant. Concluding that a search warrant must be obtained absent exigent circumstances or consent, we reverse ...." — 451 U.S. at 205–206. ^pin-205

## Application
The agents held only an arrest warrant for Lyons, which protected Lyons's interests but did nothing to protect Steagald's privacy in his own home. Absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] or consent, the agents needed a search warrant to enter Steagald's home to look for Lyons; because they had none, the search violated Steagald's Fourth Amendment rights and the evidence against him should have been suppressed.

## Conclusion
A search warrant was required to search the third party's home for the subject of the arrest warrant; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Companion to [[Payton v. New York]] (an arrest warrant suffices to enter the suspect's own home to arrest him); the related authority to detain occupants incident to a premises search is bounded in [[Bailey v. United States]].

## Appears on
- [[Arrest in the Home]] — *Key — Progeny / Refinement*
- [[Entry to Arrest]] — *Key — Progeny / Refinement*
- [[Securing the Scene]] — *Related (cross-doctrine)*

## Sources
- *Steagald v. United States*, 451 U.S. 204 (1981) — https://www.courtlistener.com/opinion/110464/steagald-v-united-states/ — pinpoint: 205–206.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ce428d165641f3fc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "451 U.S. 204 (1981)", "court": "U.S. Supreme Court", "neutral_cite": "1981 U.S. LEXIS 89", "official_citation_present": true, "parallel_cite": "101 S. Ct. 1642; 68 L. Ed. 2d 38; 49 U.S.L.W. 4418", "title": "Steagald v. United States", "year": "1981"}}
{"assertion_id": "07c192b89c60b66c", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — Progeny / Refinement", "title": "Steagald v. United States"}}
{"assertion_id": "5fa6d6e2c1a67df4", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Key — Progeny / Refinement", "title": "Steagald v. United States"}}
{"assertion_id": "922caaafa4893fa4", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (cross-doctrine)", "title": "Steagald v. United States"}}
{"assertion_id": "ecdc80d3af538620", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "To search a THIRD PARTY'S home for the subject of an arrest warrant, police need a SEARCH warrant (absent exigency or consent); an…", "title": "Steagald v. United States"}}
{"assertion_id": "43992255a645ee13", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Steagald v. United States"}}
{"assertion_id": "ab819e838559940d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1981-04-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Steagald v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Steagald v. United States", "varies_by_point": "false"}}
```

### lake record — Steagald v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Steagald v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Steagald v. United States",
    "case_name_short": "Steagald",
    "case_name_full": "Steagald v. United States",
    "input_case_name": "Steagald v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-04-21",
    "year": 1981,
    "docket": "79-6777",
    "cluster_id": 110464,
    "lead_opinion_id": 9428299,
    "sibling_ids": [
      110464,
      9428299,
      9428300
    ],
    "absolute_url": "/opinion/110464/steagald-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "451 U.S. 204",
      "volume": "451",
      "reporter": "U.S.",
      "page": "204",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 1642",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 2d 38",
        "volume": "68",
        "reporter": "L. Ed. 2d",
        "page": "38",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4418",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4418",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 89",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "451 U.S. 204",
        "volume": "451",
        "reporter": "U.S.",
        "page": "204",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 1642",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 2d 38",
        "volume": "68",
        "reporter": "L. Ed. 2d",
        "page": "38",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 89",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4418",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4418",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "451 U.S. 204",
    "official_selection": {
      "court_class": "scotus",
      "selected": "451 U.S. 204",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-205",
      "page": null,
      "quote": "--- # Steagald v. United States *451 U.S. 204 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Armed with an arrest warrant for fugitive Ricky Lyons, DEA agents entered and searched Steagald's home\u2014where they believed Lyons might be found\u2014without a search warrant and without Steagald's consent. They did not find Lyons but found cocaine, and Steagald, who was not named in the arrest warrant, was convicted. ## Issue Whether an arrest warrant for one person justifies entering and searching a third party's home, without that person's consent and absent exigent circumstances, to look for the subject of the arrest warrant. ## Rule An arrest warrant does not authorize searching a third party's home.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Steagald v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
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
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Doe v. United States",
          "cluster_id": 4590628,
          "cite": [
            "915 F.3d 905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hinshaw",
          "cluster_id": 4545610,
          "cite": [
            "2018 Ohio 4226",
            "120 N.E.3d 514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532256,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532255,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532251,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Causey v. the State",
          "cluster_id": 3148713,
          "cite": [
            "334 Ga. App. 170",
            "778 S.E.2d 800"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Lee Douds v. State",
          "cluster_id": 2983813,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCollum",
          "cluster_id": 6589541,
          "cite": [
            "79 Mass. App. Ct. 239",
            "945 N.E.2d 937",
            "2011 Mass. App. LEXIS 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
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
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ricky Dale Williams v. State",
          "cluster_id": 2857082,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pembaur v. City of Cincinnati",
          "cluster_id": 111615,
          "cite": [
            "89 L. Ed. 2d 452",
            "106 S. Ct. 1292",
            "475 U.S. 469",
            "1986 U.S. LEXIS 33",
            "54 U.S.L.W. 4289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of St. Louis v. Praprotnik",
          "cluster_id": 112017,
          "cite": [
            "99 L. Ed. 2d 107",
            "108 S. Ct. 915",
            "485 U.S. 112",
            "1988 U.S. LEXIS 1069"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Massachusetts v. Sheppard",
          "cluster_id": 111263,
          "cite": [
            "82 L. Ed. 2d 737",
            "104 S. Ct. 3424",
            "468 U.S. 981",
            "1984 U.S. LEXIS 154",
            "52 U.S.L.W. 5177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Joshua M. AARNESS",
          "cluster_id": 10014025,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donovan v. Dewey",
          "cluster_id": 110530,
          "cite": [
            "69 L. Ed. 2d 262",
            "101 S. Ct. 2534",
            "452 U.S. 594",
            "1980 U.S. LEXIS 58"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brian A. Moreland, United States of America v. Brian A. Moreland",
          "cluster_id": 793267,
          "cite": [
            "437 F.3d 424",
            "69 Fed. R. Serv. 627",
            "2006 U.S. App. LEXIS 4166",
            "2006 WL 399691"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Oody",
          "cluster_id": 1740610,
          "cite": [
            "823 S.W.2d 554",
            "1991 Tenn. Crim. App. LEXIS 405"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cooke",
          "cluster_id": 1332990,
          "cite": [
            "291 S.E.2d 618",
            "306 N.C. 132",
            "1982 N.C. LEXIS 1378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lebron v. National Railroad Passenger Corporation",
          "cluster_id": 117895,
          "cite": [
            "130 L. Ed. 2d 902",
            "115 S. Ct. 961",
            "513 U.S. 374",
            "1995 U.S. LEXIS 909",
            "95 Cal. Daily Op. Serv. 1228",
            "63 U.S.L.W. 4109",
            "8 Fla. L. Weekly Fed. S 564",
            "95 Daily Journal DAR 2219"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110464 OR 9428299 OR 9428300) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjI3NjU3NjAwMDAwJnM9MzA0NTU0MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110464+OR+9428299+OR+9428300%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 17,
        "triage_snippet_classified": 183
      },
      "lane2_top_cited": {
        "query": "cites:(110464 OR 9428299 OR 9428300)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDkmcz01NjA3OTQ0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110464+OR+9428299+OR+9428300%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110464 OR 9428299 OR 9428300)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 1,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110464 OR 9428299 OR 9428300)",
    "indexed_citing_opinions": 1037,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110464,
        "count": 926,
        "count_source": "search"
      },
      {
        "opinion_id": 9428299,
        "count": 135,
        "count_source": "search"
      },
      {
        "opinion_id": 9428300,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1585,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/steagald-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5OTA1Mzkmcz04NDM2ODEzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110464+OR+9428299+OR+9428300%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110464,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 272664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 276331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 319014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 343372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 344771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 358848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 370304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 374768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 377954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 380771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 382937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 1356897,
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
    "date_created": "2026-07-05T20:36:09Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:36:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:36:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:41:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:36:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Steagald v. United States

```
<opinion type="majority">
<author id="b271-10">Justice Marshall</author>
<p id="AL1">delivered the opinion of the Court.</p>
<p id="b271-11">The issue in this case is whether, under the Fourth Amendment, a law enforcement officer may legally search for the subject of an arrest warrant in the home of a third party without first obtaining a search warrant. Concluding that a search warrant must be obtained absent exigent circum<page-number citation-index="1" label="206">*206</page-number>stances or consent, we reverse the judgment of the United States Court of Appeals for the Fifth Circuit affirming petitioner’s conviction.</p>
<p id="b272-5">I</p>
<p id="b272-6">In early January 1978, an agent of the Drug Enforcement Administration (DEA) was contacted in Detroit, Mich., by a confidential informant who suggested that he might be able to locate Ricky Lyons, a federal fugitive wanted on drug charges. On January 14, 1978, the informant called the agent again, and gave him a telephone number in the Atlanta, Ga., area where, according to the informant, Ricky Lyons could be reached during the next 24 hours. On January 16, 1978, the agent called fellow DEA Agent Kelly Goodowens in Atlanta and relayed the information he had obtained from the informant. Goodowens contacted Southern Bell Telephone Co., and secured the address corresponding to the telephone number obtained by the informant. Good-owens also discovered that Lyons was the subject of a 6-month-old arrest warrant.</p>
<p id="b272-7">Two days later, Goodowens and 11 other officers drove to the address supplied by the telephone company to search for Lyons. The officers observed two men standing outside the house to be searched. These men were Hoyt Gaultney and petitioner Gary Steagald. The officers approached with guns drawn, frisked both men, and, after demanding identification, determined that neither man was Lyons. Several agents proceeded to the house. Gaultney’s wife answered the door, and informed the agents that she was alone in the house. She was told to place her hands against the wall and was guarded in that position while one agent searched the house. Ricky Lyons was not found, but during the search of the house the agent observed what he believed to be cocaine. Upon being informed of this discovery, Agent Goodowens sent an officer to obtain a search warrant and in the meantime conducted a second search of the house, which uncovered <page-number citation-index="1" label="207">*207</page-number>additional incriminating evidence. During a third search conducted pursuant to a search warrant, the agents uncovered 43 pounds of cocaine. Petitioner was arrested and indicted on- federal drug charges.</p>
<p id="b273-5">Prior to trial, petitioner moved to suppress all evidence uncovered during the various searches on the ground that it was illegally obtained because the agents had failed to secure a search warrant before entering the house. Agent Goodowens testified at the suppression hearing that there had been no “physical hinderance” preventing him from obtaining a search warrant and that he did not do so because he believed that the arrest warrant for Ricky Lyons was sufficient to justify the entry and search. The District Court agreed with this view, and denied the suppression motion. Petitioner was convicted, and renewed his challenge to the search in his appeal. A divided Court of Appeals for the Fifth Circuit affirmed the District Court’s denial of petitioner’s suppression motion. <em>United States </em>v. <em>Gaultney, </em><span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d 540</a></span> (1979).<footnotemark>1</footnotemark> Because the issue presented by this case is an important one<footnotemark>2</footnotemark> that has divided the Circuits,<footnotemark>3</footnotemark> we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./449/819/">449 U. S. 819</a></span>.</p>
<p id="b274-4"><page-number citation-index="1" label="208">*208</page-number>II</p>
<p id="b274-5">The Government initially seeks to avert our consideration of the Fifth Circuit’s decision by suggesting that petitioner may, regardless of the merits of that decision, lack an expectation of privacy in the house sufficient to prevail on his Fourth Amendment claim. This argument was never raised by the Government in the courts below. Moreover, in its brief in opposition to certiorari the Government represented <page-number citation-index="1" label="209">*209</page-number>to this Court that the house in question was “petitioner’s residence” and was “occupied by petitioner, Gaultney, and Gaultney’s wife.” Brief in Opposition 1, 3. However, the Government now contends that the record does not clearly show that petitioner had a reasonable expectation of privacy in the house, and hence urges us to remand the case to the District Court for re-examination of this factual question.</p>
<p id="b275-5">We decline to follow the suggested disposition. Aside from arguing that a search warrant was not constitutionally required, the Government was initially entitled to defend against petitioner’s charge of an unlawful search by asserting that petitioner lacked a reasonable expectation of privacy in the searched home, or that he consented to the search, or that exigent circumstances justified the entry. The Government, however, may lose its right to raise factual issues of this sort before this Court when it has made contrary assertions in the courts below, when it has acquiesced in contrary findings by those courts, or when it has failed to raise such questions in a timely fashion during the litigation.</p>
<p id="b275-6">We conclude that this is such a case. The Magistrate’s report on petitioner’s suppression motion, which was adopted by the District Court, characterized the issue as whether an arrest warrant was sufficient to justify the search of “the home of a third person” for the subject of the warrant. App. 12. The Government never sought to correct this characterization on appeal, and instead acquiesced in the District Court’s view of petitioner’s Fourth Amendment claim. Moreover, during both the trial and the appeal in this case the Government argued successfully that petitioner’s connection with the searched home was sufficient to establish his constructive possession of the cocaine found in a suitcase in the closet of the house.<footnotemark>4</footnotemark> Moreover, the Court of Appeals concluded, as <page-number citation-index="1" label="210">*210</page-number>had the Magistrate and the District Court, that petitioner’s Fourth Amendment claim involved the type of warrant necessary to search “premises belonging to a third party.” <span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#544" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d, at 544</a></span>. Again, the Government declined to disturb this characterization. When petitioner sought review in this Court, the Government could have filed a cross-petition for certiorari suggesting, as it does now, that the case be remanded to the District Court for further proceedings. Instead, the Government argued that further review was unnecessary. Finally, the Government in its opposition to certiorari expressly represented that the searched home was petitioner’s residence.</p>
<p id="b276-5">Thus, during the course of these proceedings the Government has directly sought to connect petitioner with the house, has acquiesced in statements by the courts below characterizing the search as one of petitioner’s residence, and has made similar concessions of its own. Now, two years after petitioner’s trial, the Government seeks to return the case to the District Court for a re-examination of this factual issue.<footnotemark>5</footnotemark> <page-number citation-index="1" label="211">*211</page-number>The tactical advantages to the Government of this disposition are obvious, for if the Government prevailed on this claim upon a remand, it would be relieved of the task of defending the judgment of the Court of Appeals before this Court. We conclude, however, that the Government, through its assertions, concessions, and acquiescence, has lost its right to challenge petitioner’s assertion that he possessed a legitimate expectation of privacy in the searched home. We therefore turn to the merits of petitioner’s claim.</p>
<p id="b277-5">Ill</p>
<p id="b277-6">The question before us is a narrow one.<footnotemark>6</footnotemark> The search at issue here took place in the absence of consent or exigent circumstances. Except in such special situations, we have consistently held that the entry into a home to conduct a search or make an arrest is unreasonable under the Fourth Amendment unless done pursuant to a warrant. See <em>Payton </em>v. <em>New </em><page-number citation-index="1" label="212">*212</page-number><em>York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-15</a></span> (1948). Thus, as we recently observed: “[I]n terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance 'to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.” <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 590</a></span>. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-475, 477-478</a></span> (1971); <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-498</a></span> <em>(1958); Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#32" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 32-33</a></span> (1925). Here, of course, the agents had a warrant — one authorizing the arrest of Ricky Lyons. However, the Fourth Amendment claim here is not being raised by Ricky Lyons. Instead, the challenge to the search is asserted by a person not named in the warrant who was convicted on the basis of evidence uncovered during a search of his residence for Ricky Lyons. Thus, the narrow issue before us is whether an arrest warrant — as opposed to a search warrant — is adequate to protect the Fourth Amendment interests of persons not named in the warrant, when their homes are searched without their consent and in the absence of exigent circumstances.</p>
<p id="b278-5">The purpose of a warrant is to allow a neutral judicial officer to' assess whether the police have probable cause to make an arrest or conduct a search. As we have often explained, the placement of this checkpoint between the Government and the citizen implicitly acknowledges that an “officer engaged in the often competitive enterprise of ferreting out crime,” <em>Johnson </em>v. <em>United States, supra, </em>at 14, may lack sufficient objectivity to weigh correctly the strength of the evidence supporting the contemplated action against the individual’s interests in protecting his own liberty and the privacy of his home. <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 449-451</a></span>; <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455-456</a></span> (1948). However, while an arrest warrant and a search warrant both serve to subject the probable-cause determina<page-number citation-index="1" label="213">*213</page-number>tion of the police to judicial review, the interests protected by the two warrants differ. An arrest warrant is issued by a magistrate upon a showing that probable cause exists to believe that the subject of the warrant has committed an offense and thus the warrant primarily serves to protect an individual from an unreasonable seizure. A search warrant, in contrast, is issued upon a showing of probable cause to believe that the legitimate object of a search is located in a particular place, and therefore safeguards an individual’s interest in the privacy of his home and possessions against the unjustified intrusion of the police.</p>
<p id="b279-5">Thus, whether the arrest warrant issued in this case adequately safeguarded the interests protected by the Fourth Amendment depends upon what the warrant authorized the agents to do. To be sure, the warrant embodied a judicial finding that there was probable cause to believe that Ricky Lyons had committed a felony, and the warrant therefore authorized the officers to seize Lyons. However, the agents sought to do more than use the warrant to arrest Lyons in a public place or in his home; instead, they relied on the warrant as legal authority to enter the home of a third person based on their belief that Ricky Lyons might be a guest there. Regardless of how reasonable this belief might have been, it was never subjected to the detached scrutiny of a judicial officer. Thus, while the warrant in this case may have protected Lyons from an unreasonable seizure, it' did absolutely nothing to protect petitioner’s privacy interest in being free from an unreasonable invasion and search of his home. Instead, petitioner’s only protection from an illegal entry and search was the agent’s personal determination of probable cause. In the absence of exigent circumstances, we have consistently held that such judicially untested determinations are not reliable enough to justify an entry into a person’s home to arrest him without a warrant, or a search of a home for objects in the absence of a search warrant. <page-number citation-index="1" label="214">*214</page-number><em>Payton </em>v. <em>New <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">York, supra;</a></span> Johnson </em>v. <em>United States, supra. </em>We see no reason to depart from this settled course when the search of a home is for a person rather than an object.<footnotemark>7</footnotemark></p>
<p id="b281-4"><page-number citation-index="1" label="215">*215</page-number>A contrary conclusion — that the police, acting alone and in the absence of exigent circumstances, may decide when there is sufficient justification for searching the home of a third party for the subject of an arrest warrant — would create a significant potential for abuse. Armed solely with an arrest warrant for a single person, the police could search all the homes of that individual’s friends and acquaintances. See, <em>e. g., Lankford </em>v. <em>Gelston, </em><span class="citation" data-id="8876108"><a href="/opinion/8889937/lankford-v-gelston/" aria-description="Citation for case: Lankford v. Gelston">364 F. 2d 197</a></span> (CA4 1966) (enjoining police practice under which 300 homes were searched pursuant to arrest warrants for two fugitives). Moreover, an arrest warrant may serve as the pretext for entering a home in which the police have a suspicion, but not probable cause to believe, that illegal activity is taking place. Cf. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#767" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 767</a></span> (1969). The Government recognizes the potential for such abuses,<footnotemark>8</footnotemark> but contends that existing remedies — such as motions to suppress illegally procured evidence and damages actions for Fourth Amendment violations — provide adequate means of redress. We do not agree. As we observed on a previous occasion, “[t]he [Fourth] Amendment is designed to prevent, not simply to redress, unlawful police action.” <em>Chimel </em>v. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#766" aria-description="Citation for case: Chimel v. California"><em>California, supra, </em>at 766, n. 12</a></span>. Indeed, if suppression motions and damages actions were sufficient to implement the Fourth Amendment’s prohibition against unreasonable searches and seizures, there would be no need for the constitutional requirement that in the absence of exigent circumstances a warrant <page-number citation-index="1" label="216">*216</page-number>must be obtained for a home arrest or a search of a home for objects. We have instead concluded that in such cases the participation of a detached magistrate in the probable-cause determination is an essential element of a reasonable search or seizure, and we believe that the same conclusion should apply here.<footnotemark>9</footnotemark></p>
<p id="b282-5">In sum, two distinct interests were implicated by the search at issue here — Ricky Lyons’ interest in being free from an unreasonable seizure and petitioner’s interest in being free from an unreasonable search of his home. Because the arrest warrant for Lyons addressed only the former interest, the search of petitioner’s home was no more reasonable from petitioner’s perspective than it would have been if conducted in the absence of any warrant. Since warrantless searches of a home are impermissible absent consent or exigent circumstances, we conclude that the instant search violated the Fourth Amendment.</p>
<p id="b282-6">IV</p>
<p id="b282-7">The Government concedes that this view is “apparently logical,” that it furthers the general policies underlying the Fourth Amendment, and that it “has the virtue of producing symmetry between the law of entry to conduct a search for things to be seized and the law of entry to conduct a search for persons to be seized.” Brief for United States 36. Yet we are informed that this conclusion is “not without its flaws” in that it is contrary to common-law precedent and creates some practical problems of law enforcement. We treat these contentions in turn.</p>
<p id="b283-4"><page-number citation-index="1" label="217">*217</page-number>A</p>
<p id="b283-5">The common law may, within limits,<footnotemark>10</footnotemark> be instructive in determining what sorts of searches the Framers of the Fourth Amendment regarded as reasonable. See, <em>e. g., Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S., at 591</a></span>. The Government contends that at common law an officer could forcibly enter the home of a third party to execute an arrest warrant. To be sure, several commentators do suggest that a constable could “break open doors” to effect such an arrest. See 1 J. Chitty, Criminal Law *57 <em>(Chitty); </em>M. Foster, Crown Law 320 (1762) (Foster); 2 M. Hale, Pleas of the Crown 116-117 (1st Am. ed. 1847) (Hale). But see 4 E. Coke, Institutes *177. As support for this proposition, these commentators all rely on a single decision, <em>Semayne’s Case, 5 Co. </em>Rep. 91a, 92b-93a, 77 Eng. Rep. 194, 198 (K. B. 1603).<footnotemark>11</footnotemark> See 1 Chitty *57; <page-number citation-index="1" label="218">*218</page-number>Foster 320; 2 Hale 116. Although that case involved only the authority of a sheriff to effect civil service on a person within his own home, the court noted in dictum that a person could not “escape the ordinary process of law” by seeking refuge in the home of a third party. 5 Co. Rep., at 93a, 77 Eng. Rep., at 198. However, the language of the decision, while not free from ambiguity, suggests that forcible entry into a third party’s house was permissible only when the person to be arrested was pursued to the house. The decision refers to a person who “flies” to another’s home, <em>ibid., </em>and the annotation notes that “in order to justify the breaking of the outer door; after denial on request to take a person . . . in the house of a stranger, it must be understood . . . that the person <em>upon a pursuit </em>taketh refuge in the house of another.” <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Id.,</a></span> </em>at 93a, n. (I), 77 Eng. Rep., at 198, n. (I) (emphasis in original). The common-law commentators appear to have adopted this limitation. See 1 Chitty *57 (sheriff may enter third parties’ home “if the offender fly to it for refuge”); Foster 320 (“For if a Stranger whose ordinary Residence is elsewhere, upon a Pursuit taketh Refuge in the House of another, this is not <em>his </em>Castle, He cannot claim the Benefit of Sanctuary in it”); 2 Hale 116, n. 20 (forcible entry permissible “only upon strong necessity”). We have long recognized that such “hot pursuit” cases fall within the exigent-circumstances exception to the warrant requirement, see <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), and therefore are distinguishable from the routine search situation presented here.</p>
<p id="b284-5">More important, the general question addressed by the common-law commentators was very different from the issue presented by this case. The authorities on which the Government relies were concerned with whether the <em>subject </em>of the arrest warrant could claim sanctuary from arrest by hiding <page-number citation-index="1" label="219">*219</page-number>in the home of a third party. See 1 Chitty *57; Foster 320; 2 Hale 116-117. Thus, in <em>Semayne’s Case </em>it was observed:</p>
<blockquote id="ATD">“[T]he house of any one is not a castle or privilege but for himself, and shall not extend to protect any person who flies to his house, or the goods of any other which are brought and conveyed into his house, to prevent a lawful execution, and to escape the ordinary process of law; for the privilege of his house extends only to him and his family, and to his own proper goods.” 5 Co. Rep., at 93a, 77 Eng. Rep., at 128.</blockquote>
<p id="b285-5">The common law thus recognized, as have our recent decisions, that rights such as those conferred by the Fourth Amendment are personal in nature, and cannot bestow vicarious protection on those who do not have a reasonable expectation of privacy in the place to be searched. See <em>United States </em>v. <em>Salvucci, </em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">448 U. S. 83</a></span> (1980); <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). The issue here, however, is not whether the subject of an arrest warrant can object to the absence of a search warrant when he is apprehended in another person’s home, but rather whether the residents of that home can complain of the search. Because the authorities relied on by the Government focus on the former question without addressing the latter, we find their usefulness limited. Indeed, if anything, the little guidance that can be gleaned from common-law authorities undercuts the Government’s position. The language of <em>Semayne’s Case </em>quoted above, for example, suggests that although the subject of an arrest warrant could not find sanctuary in the home of the third party, the home remained a “castle or privilege” for its residents. Similarly, several commentators suggested that a search warrant, rather than an arrest warrant, was necessary to fully insulate a constable from an action for trespass brought by a party whose home was searched. See, <em>e. g., </em>1 Chitty *57; 2 Hale 116-117, 151.</p>
<p id="b286-4"><page-number citation-index="1" label="220">*220</page-number>While the common law thus sheds relatively little light on the narrow question before us, the history of the Fourth Amendment strongly suggests that its Framers would not have sanctioned the instant search. The Fourth Amendment was intended partly to protect against the abuses of the general warrants that had occurred in England and of the writs of assistance used in the Colonies. See <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#608" aria-description="Citation for case: Payton v. New York">445 U. S., at 608-609</a></span> (White, J., dissenting); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-629</a></span> (1886); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 13-78 (1937). The general warrant specified only an offense — typically seditious libel— and left to the discretion of the executing officials the decision as to which persons should be arrested and which places should be searched. Similarly, the writs of assistance used in the Colonies noted only the object of the search — any uncus-tomed goods — and thus left customs officials completely free to search any place where they believed such goods might be. The central objectionable feature of both warrants was that they provided no judicial check on the determination of the executing officials that the evidence available justified an intrusion into any particular home. <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span>, 481 — 485 (1965). An arrest warrant, to the extent that it is invoked as authority to enter the homes of third parties, suffers from the same infirmity.<footnotemark>12</footnotemark> Like a writ of assistance, it specifies only the object of a search — in this case, Ricky Lyons — and leaves to the unfettered discretion of the police the decision as to which particular homes should be searched. We do not believe that the Framers of the Fourth Amendment would have condoned such a result.</p>
<p id="b286-5">B</p>
<p id="b286-6">The Government also suggests that practical problems might arise if law enforcement officers are required to obtain <page-number citation-index="1" label="221">*221</page-number>a search warrant before entering the home of a third party to make an arrest.<footnotemark>13</footnotemark> The basis of this concern is that persons, as opposed to objects, are inherently mobile, and thus officers seeking to effect an arrest may be forced to return to the magistrate several times as the subject of the arrest warrant moves from place to place. We are convinced, however, that a search warrant requirement will not significantly impede effective law enforcement efforts.</p>
<p id="b287-5">First, the situations in which a search warrant will be necessary are few. As noted in <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 602-603</a></span>, an arrest warrant alone will suffice to enter a suspect’s own residence to effect his arrest. Furthermore, if probable cause exists, no warrant is required to apprehend a suspected felon in a public place. <em>United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976). Thus, the subject of an arrest warrant can be readily seized before entering or after leaving the home of a third party.<footnotemark>14</footnotemark> Finally, the exigent-circumstances doctrine significantly limits the situations in which a search warrant would be needed. For example, a warrant-less entry of a home would be justified if the police were in “hot pursuit” of a fugitive. See <em>United States </em>v. <em>Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42-43</a></span> (1976); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> <page-number citation-index="1" label="222">*222</page-number>(1967). Thus, to the extent that searches for persons pose special problems, we believe that the exigent-circumstances doctrine is adequate to accommodate legitimate law enforcement needs.</p>
<p id="b288-4">Moreover, in those situations in which a search warrant is necessary, the inconvenience incurred by the police is simply not that significant. First, if the police know of the location of the felon when they obtain an arrest warrant, the additional burden of obtaining a search warrant at the same time is miniscule. The inconvenience of obtaining such a warrant does not increase significantly when an outstanding arrest warrant already exists. In this case, for example, Agent Goodowens knew the address of the house to be searched two days in advance, and planned the raid from the federal courthouse in Atlanta where, we are informed, three full-time magistrates were on duty. In routine search cases such as this, the short time required to obtain a search warrant from a magistrate will seldom hinder efforts to apprehend a felon. Finally, if a magistrate is not nearby, a telephonic search warrant can usually be obtained. See Fed. Rule Crim. Proc. 41 (c)(1), (2).</p>
<p id="b288-5">Whatever practical problems remain, however, cannot outweigh the constitutional interests at stake. Any warrant requirement impedes to some extent the vigor with which the Government can . seek to enforce its laws, yet the Fourth Amendment recognizes that this restraint is necessary in some cases to protect against unreasonable searches and seizures. We conclude that this is such a case. The additional burden imposed on the police by a warrant requirement is minimal. In contrast, the right protected — that of presumptively innocent people to be secure in their homes from unjustified, forcible intrusions by the Government — is weighty. Thus, in order to render the instant search reasonable under the Fourth Amendment, a search warrant was required.</p>
<p id="b289-4"><page-number citation-index="1" label="223">*223</page-number>Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b289-5">
<em>So ordered.</em>
</p>
<p id="b289-6">The Chief Justice concurs in the judgment.</p>
<footnote label="1">
<p id="b273-6"> The court relied on a previous decision in the Circuit that held that “when an officer holds a valid arrest warrant and reasonably believes that its subject is within premises belonging to a third party, he need not obtain a search warrant to enter for the purpose of arresting the subject.” <em>United States </em>v. <em>Cravero, </em>545 E. 2d 406, 421 (1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./430/983/">430 U. S. 983</a></span> (1977). Circuit Judge Kraviteh dissented on the ground that the information known to the agents was insufficient to establish a reasonable belief that Lyons could be found in the house to be searched. <span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#548" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d at 548</a></span>. On the petition for rehearing, Judge Kraviteh, again in dissent, contended that the majority’s decision announced a “rule of questionable validity and wisdom” and represented a “disturbing erosion of the Fourth Amendment rights of third parties.” <em>United States </em>v. <em>Gaultney, </em><span class="citation" data-id="9466489"><a href="/opinion/374768/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#644" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">615 F. 2d 642, 644</a></span> (1980).</p>
</footnote>
<footnote label="2">
<p id="b273-7"> Last Term we noted that this question remained unresolved. See <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 583</a></span> (1980).</p>
</footnote>
<footnote label="3">
<p id="b273-8"> Three Circuits have held that in ,the absence of exigent circumstances a search warrant is required before law officers may enter the home of <page-number citation-index="1" label="208">*208</page-number>a third party to execute an arrest warrant. See <em>Government of Virgin Islands </em>v. <em>Gereau, </em><span class="citation" data-id="8173389"><a href="/opinion/8210936/government-of-virgin-islands-v-gereau/#928" aria-description="Citation for case: Government of Virgin Islands v. Gereau">502 <em>F. 2d 914, </em>928</a></span> (CA3 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/909/">420 U. S. 909</a></span> (1975); <em>Wallace </em>v. <em>King, </em><span class="citation" data-id="8911894"><a href="/opinion/8922855/wallace-v-king/#1158" aria-description="Citation for case: Wallace v. King">626 F. 2d 1157, 1158-1159</a></span> (CA4 1980), cert. pending, No. 80-503; <em>United States v. Prescott, </em><span class="citation" data-id="9465056"><a href="/opinion/358848/united-states-v-saundra-prescott/#1347" aria-description="Citation for case: United States v. Saundra Prescott">581 F. 2d 1343, 1347-1350</a></span> (CA9 1978). Two Circuits have joined the Court of Appeals in this case in adopting the contrary view that a search warrant is not required in such situations if the police have an arrest warrant an'd reason to believe that the person to be arrested is within the home to be searched. See <em>United States </em>v. <em>McKinney, </em><span class="citation" data-id="276331"><a href="/opinion/276331/united-states-v-roy-mckinney/#262" aria-description="Citation for case: United States v. Roy McKinney">379 F. 2d 259, 262-263</a></span> (CA6 1967); <em>United States </em>v. <em>Harper, </em><span class="citation" data-id="343372"><a href="/opinion/343372/united-states-v-maurice-harper/#612" aria-description="Citation for case: United States v. Maurice Harper">550 F. 2d 610, 612-614</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./434/837/">434 U. S. 837</a></span> (1977). The Second Circuit has suggested in dictum that it subscribes to this latter view, see <em>United States </em>v. <em>Manley, </em><span class="citation" data-id="382937"><a href="/opinion/382937/united-states-v-david-manley-and-fluer-williams/#983" aria-description="Citation for case: United States v. David Manley and Fluer Williams">632 F. 2d 978, 983</a></span> (1980), while the Court of Appeals for the District of Columbia Circuit has recently indicated that it would require a search warrant in such cases. See <em>United States </em>v. <em>Ford, </em>180 U. S. App. D. C. 1, 14, n. 45, <span class="citation multiple-matches"><a href="/c/F.%202d/553/146/">553 F. 2d 146</a></span>, 159, n. 45 (1977). Two other Courts of Appeals have left the issue open. See <em>United States </em>v. <span class="citation" data-id="377954"><a href="/opinion/377954/united-states-v-carol-e-adams/#44" aria-description="Citation for case: United States v. Carol E. Adams"><em>Adams, 621 </em>F. 2d 41, 44, n. 7</a></span> (CA1 1980); <em>Rice </em>v. <em>Wolff, </em>513 F. 2d-1280, 1291-1292, and n. 7 (CA8 1975), rev’d on other grounds <em>sub nom. Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976). The Seventh Circuit has not considered the question.</p>
<p id="b274-7">While the courts are in conflict, most modem commentators agree that a search warrant is necessary to fully protect the privacy interests of third parties when their home is searched for the subject of an arrest warrant. See 2 W. LaFave, Search and Seizure: A Treatise on the Fourth Amendment 374, 38A-385 (1978); Rotenberg &amp; Tanzer, Searching for the Person to Be Seized, 35 Ohio St. L. J. 56, 67-71 (1974); Groot, Arrests in Private Dwellings, <span class="citation no-link">67 Va. L. Rev. 275</span> (1981); Note, The Neglected Fourth Amendment Problem in Arrest Entries, <span class="citation no-link">23 Stan. L. Rev. 995</span>, 997-999 (1971); Comment, Arresting a Suspect in a Third Party’s Home: What is Reasonable?, 72 J. Crim. L. &amp; C. 293 <em>(1981). </em>But see Mascolo, Arrest Warrants and Search Warrants: The Seizure of A Suspect in the Home of a Third Party, 54 Conn. Bar J. 299 (1980).</p>
</footnote>
<footnote label="4">
<p id="b275-7"> The Court of Appeals, in accepting this contention, cited the Government’s own evidence that several checks and papers bearing petitioner’s name were found in the house and that “Steagald, when taken into cus<page-number citation-index="1" label="210">*210</page-number>tody, was wearing only slacks and a long-sleeve shirt, clothing inconsistent with the coldness of the January afternoon, and that once taken inside the . . . house, told a DEA agent that he was cold and requested that she get a sweater or coat for him from the kitchen area.” <span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#546" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d, at 546-547</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b276-10"> The Government asserts that it was unable to raise this issue in the courts below because both courts had acted before this Court decided <em>United States </em>v. <em>Salvucci, </em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">448 U. S. 83</a></span> (1980). We do not find this justification to be compelling. Under the “automatic standing” rule of <em>Jones </em>v. <em>United States, </em>362 U. S.-257 (1960), any person charged with a possessory offense could challenge the search in which the incriminating evidence was obtained. <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>overruled <em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>and instead limited such Fourth Amendment claims to those persons who had a reasonable expecta^tion of privacy in the area or object of the search. Although <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>thus altered Fourth Amendment jurisprudence to some extent, the rationale of that decision was in large part simply an extension of this Court’s earlier reasoning in <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). The <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span> </em>decision held that an illegal search violated the Fourth Amendment rights only of those persons who had a “legitimate expectation of <page-number citation-index="1" label="211">*211</page-number>privacy in the invaded place.” <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois"><em>Id., </em>at 143</a></span>. While that decision did not directly address the “automatic standing” rule of <em>Jones </em>v. <em>United States, </em>it was clearly an ill omen for the continued vitality of that decision. Since <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span> </em>was decided well before this case was briefed and argued in the Court of Appeals, the Government could easily have raised before that court the question of whether petitioner’s Fourth Amendment rights were even implicated by the search at issue here. Indeed, the Government in <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>clearly recognized the significance of <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>for in that case, despite the contrary authority of <em>Jones </em>v. <em>United States, </em>it argued from the outset that the defendant lacked a sufficient expectation of privacy to challenge the legality of the search under the Fourth Amendment. We are given no explanation why the Government failed to regard <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span> </em>as of equal significance to this case. In any event, <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>was decided before certiorari was sought in this case, but rather than oppose certiorari on the ground that petitioner lacked a legitimate expectation of privacy in the searched home, the Government made explicit concessions to the contrary.</p>
</footnote>
<footnote label="6">
<p id="b277-8"> Initially, we assume without deciding that the information relayed to Agent Goodowens concerning the whereabouts of Ricky Lyons would have been sufficient to establish probable Cause to believe that Lyons was at the house searched by the agents.</p>
</footnote>
<footnote label="7">
<p id="b280-5"> Indeed, the plain wording of the Fourth Amendment admits of no exemption from the warrant requirement when the search of a home is for a person rather than for a thing. As previously noted, absent exigent circumstances or consent, an entry into a private dwelling to conduct a search or effect an arrest is unreasonable without a warrant. The second clause of the Fourth Amendment, which governs the issuance of such warrants, provides that “no Warrants shall issue but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” This language plainly suggests that the same sort of judicial determination must be made when the search of a person’s home is for another person as is necessary when the search is for an object. Specifically, absent exigent circumstances the magistrate, rather than the police officer, must make the decision that probable cause exists- to believe that the person or object to be seized is within a particular place.</p>
<p id="b280-6">In <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>of course, we recognized that an arrest warrant alone was sufficient to authorize the entry into a person’s home to effect his arrest. We reasoned:</p>
<blockquote id="b280-7">“If there is sufficient evidence of a citizen’s participation in a felony to persuade a judicial officer that his arrest is justified, it is constitutionally reasonable to require him to open his doors to the officers of the law. Thus, for Fourth Amendment purposes, an arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York">445 U. S., at 602-603</a></span>.</blockquote>
<p id="b280-8">Because an arrest warrant authorizes the police to deprive a person of his liberty, it necessarily also authorizes a limited invasion of that person’s privacy interest when it is necessary to arrest him in his home. This analysis, however, is plainly inapplicable when the police seek to use an arrest warrant as legal authority to enter the home of a third party to conduct a search. Such a warrant embodies no judicial determination whatsoever regarding the person whose home is to be searched. Because it does not authorize the police to deprive the third person of his liberty, it cannot embody any derivative authority to deprive this person of his interest in the privacy of his home. Such a deprivation must instead be based on an independent showing that a legitimate object of a search is located in the third party’s home. We have consistently held, however, <page-number citation-index="1" label="215">*215</page-number>that such a determination is the province of the magistrate, and not that of the police officer.</p>
</footnote>
<footnote label="8">
<p id="b281-7"> The Government concedes that "an arrest warrant may be thought to have some of the undesirable attributes of a general warrant if it authorizes entry into third party premises.” Brief for United States 42. Similarly, the Government agrees that “the potential for abuse is much less if the implicit entry authorization of an arrest warrant is confined to the suspect’s own residence and is not held to make the police free to search for the suspect in anyone else’s house without obtaining a particularized judicial determination that the suspect is present.” <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Ibid.</a></span></em></p>
</footnote>
<footnote label="9">
<p id="b282-8"> Moreover, the remedies suggested by the Government are not without their pitfalls and limitations. For example, absent a search warrant requirement, a person seeking to recover civil damages for the unjustified search of his home may possibly be thwarted if a good-faith defense to such unlawful conduct is recognized. See, e. <em>g., Wallace </em>v. <em>King, </em><span class="citation" data-id="8911894"><a href="/opinion/8922855/wallace-v-king/#1161" aria-description="Citation for case: Wallace v. King">626 F. 2d, at <em>1161.</em></a></span></p>
</footnote>
<footnote label="10">
<p id="b283-6"> The significance accorded to such authority, however, must be kept in perspective, for our decisions in this area have not "simply frozen into constitutional law those enforcement practices that existed at the time of the Fourth Amendment’s passage.” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S., at 591, n. 33</a></span>. The common-law rules governing searches and arrests evolved in a society far simpler than ours is today. Crime has changed, as have the means of law enforcement, and it would therefore be naive to assume that those actions a constable could take in an English or American village three centuries ago should necessarily govern what we, as a society, now regard as proper. Cf. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352-353</a></span> (1967). Instead, the Amendment’s prohibition against “unreasonable searches and seizures” must be interpreted “in light of contemporary norms, and conditions.” <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 591, n. 33</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b283-7"> The three other decisions cited by the Government do not address the issue raised here. <em>Johnson </em>v. <em>Leigh, </em>6 Taunt. 246, 248, 128 Eng. Rep. 1029, 1029-1030 (C. P. 1815), dealt with the authority of a constable to enter the home of a third person to make an arrest when the “outer door” was open. Under the common law, “a privilege attaches to the outer door of a dwelling, because ... it is the owner’s castle.” <em>Hutchison </em>v. <em>Birch, 4 </em>Taunt. 619, 625, 128 Eng. Rep. 473, 476 (C. P. 1812). Thus, an open outer door was apparently regarded as the equivalent of a consent of the occupant for the constable to enter the home and conduct a search. The other two decisions cited by the Government, <em>Sheers </em>v. <em>Brooks, </em>2 Bl. H. <page-number citation-index="1" label="218">*218</page-number>120, 122, 126 Eng. Rep. 463, 464 (C. P. 1792), and <em>Kelsy </em>v. <span class="citation" data-id="6613353"><a href="/opinion/6731697/kelsy-v-wright/" aria-description="Citation for case: Kelsy v. Wright"><em>Wright, 1 </em>Root 83</a></span> (Conn. 1783), dealt only with the authority of the constable to enter the home of the person to be arrested.</p>
</footnote>
<footnote label="12">
<p id="b286-7"> The Government recognizes this problem. See n. 8, <em>supra.</em></p>
</footnote>
<footnote label="13">
<p id="b287-6"> A number of Circuits already require a search warrant for entries of this sort, see n. 3, supra, and there is no indication in the record that law enforcement efforts in these jurisdictions have suffered as a result. Thus, we are inclined to view the Government’s argument on this point with considerable skepticism. Cf. <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York">445 U. S., at 602</a></span>.</p>
<p id="b287-7">Moreover, we are informed by the Government that “it is the present policy of the Drug Enforcement Administration, whose agents conducted the search in the present case, to secure a search warrant prior to making an arrest entry into third party premises, in the absence of exigent circumstances or consent.” Brief in Opposition 0, n. 7.</p>
</footnote>
<footnote label="14">
<p id="b287-8"> Indeed, the “inherent mobility” of persons noted by the Government suggests that in most situations the police may avoid altogether the need to obtain a search warrant simply by waiting for a suspect to leave the third person’s home before attempting to arrest that suspect.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Van Leeuwen.md  (`case`, 7 assertions)

### content_page

```
---
title: "United States v. Van Leeuwen"
type: case
citation: "397 U.S. 249 (1970)"
parallel_cite: "90 S. Ct. 1029; 25 L. Ed. 2d 282"
neutral_cite: 1970 U.S. LEXIS 57
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-04-27
docket: 403
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1970-04-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Van Leeuwen
  varies_by_point: false
  scope_note: "Controlling: a brief detention of mailed packages on reasonable suspicion, while a warrant is diligently sought, is reasonable; mere detention invades no privacy interest until the package is opened under a warrant. A precursor to the property-detention analysis of United States v. Place."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108099/united-states-v-van-leeuwen/"
  cluster_id: 108099
  opinion_id: 108099
  identity_checked: true
homes:
  - page: "[[Seizure of Property]]"
    role: "Key — package / mail detention"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Place]]", "[[Terry v. Ohio]]", "[[Illinois v. McArthur]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure-of-property", "reasonable-suspicion", "mail", "warrant-requirement"]
holding: "First-class mail may be detained without a warrant on reasonable suspicion while officers diligently pursue a search warrant; the brief detention invades no Fourth Amendment privacy interest, which is implicated only when the package is opened under a warrant."
lake:
  record_id: United States v. Van Leeuwen
  status: verified
  projected_at: 2026-07-09
---

# United States v. Van Leeuwen

*397 U.S. 249 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Van Leeuwen mailed two 12-pound insured first-class packages — declared to contain coins — at a Washington post office near the Canadian border, addressed to post-office boxes in California and Tennessee. A suspicious postal clerk alerted an officer, who noticed the return address was a vacant area of a nearby junior college and that Van Leeuwen's car bore British Columbia plates. Investigation revealed that both addressees were under investigation for trafficking in illegal coins. The packages were detained while a warrant was sought; because of a time difference in reaching Tennessee, the warrant did not issue and reach the post office until about 29 hours after mailing. The packages were then opened (revealing illegally imported gold coins), resealed, and promptly sent on. The Ninth Circuit reversed Van Leeuwen's conviction for want of a timely warrant.

## Issue
Did the warrantless detention of first-class mail packages — on reasonable suspicion, while officers diligently pursued a search warrant — violate the Fourth Amendment?

## Rule
No. While first-class mail may be opened only under a warrant, the suspicious circumstances "certainly justified detention, without a warrant, while an investigation was made." — 397 U.S. at 252. ^pin-252

Mere detention invaded no protected interest: "No interest protected by the Fourth Amendment was invaded by forwarding the packages the following day rather than the day when they were deposited. The significant Fourth Amendment interest was in the privacy of this first-class mail; and that privacy was not disturbed or invaded until the approval of the magistrate was obtained." — [*Id.* at 253](https://www.courtlistener.com/opinion/108099/united-states-v-van-leeuwen/#:~:text=No%20interest%20protected%20by%20the). ^pin-253

The Court cautioned that the rule "is not that first-class mail can be detained 29 hours . . . to obtain the search warrant"; rather, "on the facts of this case — the nature of the mailings, their suspicious character, the fact that there were two packages going to separate destinations, the unavoidable delay in contacting the more distant of the two destinations . . . — a 29-hour delay between the mailings and the service of the warrant cannot be said to be 'unreasonable.'" — *Id.* ^pin-253b

## Application
The packages' weight, the fictitious return address, and the British Columbia plates of a mailer in a border town supplied reasonable suspicion justifying detention while officers investigated. The only thing done on suspicion was to detain the packages — no search occurred and no privacy interest was invaded until the magistrate approved the warrant. The 29-hour interval reflected diligent, unavoidable investigation of two distant destinations across a time difference, not delay or indifference, and was therefore reasonable on these particular facts.

## Conclusion
The detention of the packages pending the warrant was reasonable; the evidence was properly admitted, and the judgment of the Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Van Leeuwen* remains the controlling authority that property (here, mail) may be briefly detained on reasonable suspicion while a warrant is diligently sought, reasoning by analogy to [[Terry v. Ohio]]. It is the direct predecessor of [[United States v. Place]] (luggage-detention duration limit) and runs alongside [[Illinois v. McArthur]] (temporary seizure of premises pending a warrant). No negative treatment.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *United States v. Van Leeuwen*, 397 U.S. 249 (1970) — https://www.courtlistener.com/opinion/108099/united-states-v-van-leeuwen/ — pinpoints: 252, 253.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c8264bfcb367f4c0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "397 U.S. 249 (1970)", "court": "U.S. Supreme Court", "neutral_cite": "1970 U.S. LEXIS 57", "official_citation_present": true, "parallel_cite": "90 S. Ct. 1029; 25 L. Ed. 2d 282", "title": "United States v. Van Leeuwen", "year": "1970"}}
{"assertion_id": "3a4177a6bb1d7466", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "United States v. Van Leeuwen"}}
{"assertion_id": "c9e4e952e5ccbaa0", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of Property"}, "payload": {"home": "Seizure of Property", "role": "Key — package / mail detention", "title": "United States v. Van Leeuwen"}}
{"assertion_id": "e757a946416b949f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "First-class mail may be detained without a warrant on reasonable suspicion while officers diligently pursue a search warrant; the brief detention invades no Fourth Amendment privacy interest, which is implicated only when the package is opened under a warrant.", "title": "United States v. Van Leeuwen"}}
{"assertion_id": "ed63f72add514f67", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "United States v. Van Leeuwen"}}
{"assertion_id": "3bef2bb2525dd2ed", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1970-04-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Van Leeuwen", "field_i_validity": "good_law", "scope_note": "Controlling: a brief detention of mailed packages on reasonable suspicion, while a warrant is diligently sought, is reasonable; mere detention invades no privacy interest until the package is opened under a warrant. A precursor to the property-detention analysis of United States v. Place.", "title": "United States v. Van Leeuwen", "varies_by_point": "false"}}
{"assertion_id": "feb36527d6ff93d1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Van Leeuwen"}}
```

### lake record — United States v. Van Leeuwen

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Van Leeuwen",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Van Leeuwen",
    "case_name_short": "",
    "case_name_full": "United States v. Van Leeuwen",
    "input_case_name": "United States v. Van Leeuwen",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-04-27",
    "year": 1970,
    "docket": "403",
    "cluster_id": 108099,
    "lead_opinion_id": 108099,
    "sibling_ids": [
      108099
    ],
    "absolute_url": "/opinion/108099/united-states-v-van-leeuwen/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "397 U.S. 249",
      "volume": "397",
      "reporter": "U.S.",
      "page": "249",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 1029",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1029",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 282",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "282",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 57",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "57",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "397 U.S. 249",
        "volume": "397",
        "reporter": "U.S.",
        "page": "249",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1029",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1029",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 282",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "282",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 57",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "57",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "397 U.S. 249",
    "official_selection": {
      "court_class": "scotus",
      "selected": "397 U.S. 249",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-252",
      "page": null,
      "quote": "--- # United States v. Van Leeuwen *397 U.S. 249 (1970)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Van Leeuwen mailed two 12-pound insured first-class packages \u2014 declared to contain coins \u2014 at a Washington post office near the Canadian border, addressed to post-office boxes in California and Tennessee. A suspicious postal clerk alerted an officer, who noticed the return address was a vacant area of a nearby junior college and that Van Leeuwen's car bore British Columbia plates. Investigation revealed that both addressees were under investigation for trafficking in illegal coins. The packages were detained while a warrant was sought; because of a time difference in reaching Tennessee, the warrant did not issue and reach the post office until about 29 hours after mailing. The packages were then opened (revealing illegally imported gold coins), resealed, and promptly sent on. The Ninth Circuit reversed Van Leeuwen's conviction for want of a timely warrant. ## Issue Did the warrantless detention of first-class mail packages \u2014 on reasonable suspicion, while officers diligently pursued a search warrant \u2014 violate the Fourth Amendment? ## Rule No. While first-class mail may be opened only under a warrant, the suspicious circumstances",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-253",
      "page": null,
      "quote": "No interest protected by the Fourth Amendment was invaded by forwarding the packages the following day rather than the day when they were deposited. The significant Fourth Amendment interest was in the privacy of this first-class mail; and that privacy was not disturbed or invaded until the approval of the magistrate was obtained.",
      "star_marker": "253",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8102,
      "fragment": "#:~:text=No%20interest%20protected%20by%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-253b",
      "page": null,
      "quote": "is not that first-class mail can be detained 29 hours . . . to obtain the search warrant",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1970-04-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Van Leeuwen",
    "varies_by_point": false,
    "scope_note": "Controlling: a brief detention of mailed packages on reasonable suspicion, while a warrant is diligently sought, is reasonable; mere detention invades no privacy interest until the package is opened under a warrant. A precursor to the property-detention analysis of United States v. Place.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Corey Joel Eichers",
          "cluster_id": 2731770,
          "cite": [
            "853 N.W.2d 114",
            "2014 Minn. LEXIS 456"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Noel Lee Decker, Barbara K. Decker",
          "cluster_id": 577733,
          "cite": [
            "956 F.2d 773",
            "1992 U.S. App. LEXIS 1519",
            "1992 WL 19476"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
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
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Neem Shiva Dass and Ma Surina Dasi, Marvin Neer, Gerald Terpak",
          "cluster_id": 507432,
          "cite": [
            "849 F.2d 414",
            "1988 U.S. App. LEXIS 8007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. John Christopher Beale",
          "cluster_id": 437319,
          "cite": [
            "736 F.2d 1289"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reedo Eric Corbitt",
          "cluster_id": 402364,
          "cite": [
            "675 F.2d 626",
            "1982 U.S. App. LEXIS 20065"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond J. Place",
          "cluster_id": 394856,
          "cite": [
            "660 F.2d 44"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Vito Giacalone",
          "cluster_id": 361931,
          "cite": [
            "588 F.2d 1158",
            "1978 U.S. App. LEXIS 6938"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Bolton",
          "cluster_id": 108714,
          "cite": [
            "35 L. Ed. 2d 201",
            "93 S. Ct. 739",
            "410 U.S. 179",
            "1973 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marshall",
          "cluster_id": 2316658,
          "cite": [
            "586 A.2d 85",
            "123 N.J. 1",
            "1991 N.J. LEXIS 17"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Athan",
          "cluster_id": 2622136,
          "cite": [
            "158 P.3d 27"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mooney",
          "cluster_id": 7894385,
          "cite": [
            "218 Conn. 85",
            "588 A.2d 145",
            "1991 Conn. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Francis Lafrance",
          "cluster_id": 526045,
          "cite": [
            "879 F.2d 1",
            "1989 U.S. App. LEXIS 10185",
            "1989 WL 77159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government, Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government",
          "cluster_id": 539907,
          "cite": [
            "900 F.2d 1234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKinnon",
          "cluster_id": 2616887,
          "cite": [
            "500 P.2d 1097",
            "7 Cal. 3d 899",
            "103 Cal. Rptr. 897",
            "1972 Cal. LEXIS 233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 1192493,
          "cite": [
            "918 P.2d 945",
            "82 Wash. App. 594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas J. Licata",
          "cluster_id": 451773,
          "cite": [
            "761 F.2d 537"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Irving Hillison, United States of America v. Murray David Jacobson, United States of America v. Jeffrey Ketchum Mansfield",
          "cluster_id": 435104,
          "cite": [
            "733 F.2d 692"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Richards",
          "cluster_id": 386047,
          "cite": [
            "638 F.2d 765"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Darrell Jay Glover, United States of America v. Susan Noreen Kozak",
          "cluster_id": 733387,
          "cite": [
            "104 F.3d 1570",
            "1997 U.S. App. LEXIS 1060",
            "1997 WL 25529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108099) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 172,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 172,
        "triage_read": 11,
        "triage_snippet_classified": 161
      },
      "lane2_top_cited": {
        "query": "cites:(108099)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NSZzPTU5NzE1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108099%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108099)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108099)",
    "indexed_citing_opinions": 259,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108099,
        "count": 259,
        "count_source": "search"
      }
    ],
    "citation_count": 399,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-van-leeuwen.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjUyMjA1ODImcz00MzM3MzA4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108099%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108099,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 99756,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 104235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 107064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 286052,
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
    "date_created": "2026-07-06T03:15:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:19:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Van Leeuwen

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b351-9">
  Mr. Justice Douglas
 </author>
<p id="Aj0">
  delivered the opinion of the Court.
 </p>
<p id="b351-10">
  Respondent, at about 1:30 p. m. on Thursday, March 28, 1968, mailed two 12-pound packages at the post office in Mt. Vernon, Washington, a town some 60 miles from the Canadian border. One package was addressed to a post office box in Van Nuys, California, and the other to a post office box in Nashville, Tennessee. Respondent declared they contained coins. Each pack
  <span citation-index="1" class="star-pagination" label="250"> 
   *250
   </span>
  age was to be sent airmail registered and each was insured for $10,000, a type of mailing that the parties agree was first class, making them not subject to discretionary inspection.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b352-5">
  When the postal clerk told a policeman who happened to be present that he was suspicious of the packages, the policeman at once noticed that the return address on the packages was a vacant housing area of a nearby junior college, and that the license plates of respondent’s car were British Columbia. The policeman called the Canadian police, who called customs in Seattle. At 3 o’clock that afternoon customs called Van Nuys and learned that the addressee of one package was under investigation in Van Nuys for trafficking in illegal coins. Due to the time differential, Seattle customs was unable to reach Nashville until the following morning, March 29, when Seattle was advised that the second addressee was also being investigated for the same crime. A customs official in Seattle thereupon filed an affidavit for a search warrant for both packages with a United States commissioner, who issued the search warrant at 4 p. m., and it was executed in Mt. Vernon at 6:30 p. m., 2% hours later. Thereupon the packages were opened, inspected, resealed, and promptly sent on their way.
 </p>
<p id="b352-6">
  Other evidence showed that respondent had brought the two packages in from Canada without declaring them. He was tried for illegally importing gold coins in violation of <span class="citation no-link">18 U. S. C. § 545</span> and found guilty and sentenced and fined. On appeal, the Court of Appeals reversed, holding that the coins were improperly admitted in evidence because a timely warrant had not been obtained. <span class="citation" data-id="9454782"><a href="/opinion/286052/united-states-v-gerritt-johannes-van-leeuwen/" aria-description="Citation for case: United States v. Gerritt Johannes Van Leeuwen">414 F. 2d 758</a></span>. The case is here on a petition for a writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./396/885/">396 U. S. 885</a></span>. We reverse.
 </p>
<p id="b353-2">
<span citation-index="1" class="star-pagination" label="251"> 
   *251
   </span>
  It has long been held that first-class mail such as letters and sealed packages subject to letter postage— as distinguished from newspapers, magazines, pamphlets, and other printed matter — is free from inspection by-postal authorities, except in the manner provided by the Fourth Amendment. As stated in
  <em>
   Ex parte Jackson,
  </em>
  <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span>, decided in 1878:
 </p>
<blockquote id="b353-3">
  “Letters and sealed packages of this kind in the mail are as fully guarded from examination and inspection, except as to their outward form and weight, as if they were retained by the parties forwarding them in their own domiciles. The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures extends to their papers, thus closed against inspection, wherever they may be. Whilst in the mail, they can only be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one’s own household. No law of Congress can place in the hands of officials connected with the postal service any authority to invade the secrecy of letters and such sealed packages in the
  <em>
   mail;
  </em>
  and all regulations adopted as to mail matter of this kind must be in subordination to the great principle embodied in the fourth amendment of the Constitution.”
 </blockquote>
<p id="b353-4">
  The course of events since 1878 has underlined the relevance and importance of the Post Office to our constitutional rights. Mr. Justice Holmes in
  <em>
   Milwaukee Pub. Co.
  </em>
  v.
  <em>
   Burleson, 255
  </em>
  U. S. 407, 437 (dissenting opinion), said that “the use of the mails is almost as much a part of free speech as the right to use our tongues.” We have emphasized over and over again that while Congress may classify the mail and fix the charges
  <span citation-index="1" class="star-pagination" label="252"> 
   *252
   </span>
  for its carriage, it may not set up regimes of censorship over it,
  <em>
   Hannegan
  </em>
  v.
  <em>
   Esquire, Inc.,
  </em>
  <span class="citation" data-id="9419751"><a href="/opinion/104235/hannegan-v-esquire-inc/" aria-description="Citation for case: Hannegan v. Esquire, Inc.">327 U. S. 146</a></span>, or encumber its flow by setting “administrative officials astride the flow of mail to inspect it, appraise it, write the addressee about it, and await a response before dispatching the mail” to him.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
<em>
   Lamont
  </em>
  v.
  <em>
   Postmaster General,
  </em>
  <span class="citation" data-id="9423040"><a href="/opinion/107064/lamont-v-postmaster-general/#306" aria-description="Citation for case: Lamont v. Postmaster General">381 U. S. 301, 306</a></span>. Yet even first-class mail is not beyond the reach of all
  <em>
   inspection;
  </em>
  and the sole question here is whether the conditions for its detention and inspection had been satisfied. We think they had been.
 </p>
<p id="b354-6">
  The nature and weight of the packages, the fictitious return address, and the British Columbia license plates of respondent who made the mailings in this border town certainly justified detention, without a warrant, while an investigation was made. The “protective search for weapons” of a suspect which the Court approved in
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-27</a></span>, even when probable cause for an arrest did not exist, went further than we need go here. The only thing done here on the basis of suspicion was detention of the packages. There was at that point no possible invasion of the right “to be secure” in the “persons, houses, papers, and effects” protected by the Fourth Amendment against “unreasonable searches and seizures.” Theoretically — and it is theory only that respondent has on his side — detention of mail could at some point become an unreasonable seizure of “papers” or “effects” within the meaning of the Fourth Amendment. Detention for 1% hours — from 1:30 p. m. to 3 p. m. — for an investigation certainly was not excessive; and at the end of that time probable cause existed for believing that the California package was part of an illicit project. A warrant could have been obtained that
  <span citation-index="1" class="star-pagination" label="253"> 
   *253
   </span>
  day for the one package; yet the mystery of the other package remained unsolved and federal officials in Tennessee could not be reached because of the time differential. The next morning they were reached and it was learned that the second package was also probably part of an illicit project. By 4 p. m. — or 26% hours after the mailing in Mt. Vernon — a search warrant was obtained in Seattle and at 6:30 p. m., or 29 hours after the mailing, the search warrant reached Mt. Vernon, a speedy transmission considering the rush-hour time of day and the congested highway.
 </p>
<p id="b355-4">
  No interest protected by the Fourth Amendment was invaded by forwarding the packages the following day rather than the day when they were deposited. The significant Fourth Amendment interest was in the privacy of this first-class mail; and that privacy was not disturbed or invaded until the approval of the magistrate was obtained.
 </p>
<p id="b355-5">
  The rule of our decisions certainly is not that first-class mail can be detained 29 hours after mailing in order to obtain the search warrant needed for its inspection. We only hold that on the facts of this case— the nature of the mailings, their suspicious character, the fact that there were two packages going to separate destinations, the unavoidable delay in contacting the more distant of the two destinations, the distance between Mt. Vernon and Seattle — a 29-hour delay between the mailings and the service of the warrant cannot be said to be “unreasonable” within the meaning of the Fourth Amendment. Detention for this limited time was, indeed, the prudent act rather than letting the packages enter the mails and then, in case the initial suspicions were confirmed, trying to locate them en route and enlisting the help of distant federal officials in serving the warrant.
 </p>
<p id="b355-6">
<em>
   Reversed.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b352-7">
   <span class="citation no-link">39 CFR §131.2</span> describes “first class” mail as “matter closed against postal inspection,” which follows the definition in <span class="citation no-link">39 U. S. C. §4251</span> (a).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b354-7">
   The question as to the right of the addressee to stop deliveries is a separate and distinct one. See No. 399,
   <em>
    Rowan
   </em>
   v.
   <em>
    Post Office, post,
   </em>
   p. 728.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Virginia v. Moore.md  (`case`, 8 assertions)

### content_page

```
---
title: "Virginia v. Moore"
type: case
citation: "553 U.S. 164 (2008)"
parallel_cite: "128 S. Ct. 1598; 170 L. Ed. 2d 559"
neutral_cite: 2008 U.S. LEXIS 3674
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2008
date_decided: 2008-04-23
docket: 06-1082
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2008-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Virginia v. Moore
  varies_by_point: false
  scope_note: "Controlling: an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law; the search incident follows and no suppression results from the state-law violation."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145814/virginia-v-moore/"
  cluster_id: 145814
  opinion_id: 145814
  identity_checked: true
homes:
  - page: "[[Arrest and Arrest Warrants]]"
    role: "Key — a state-law arrest violation is not a Fourth Amendment violation"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
  - page: "[[The Exclusionary Rule]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Robinson]]", "[[Atwater v. City of Lago Vista]]", "[[Knowles v. Iowa]]", "[[Devenpeck v. Alford]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "search-incident-to-arrest", "exclusionary-rule", "state-law"]
holding: "A warrantless arrest on probable cause for a crime committed in the officer's presence is reasonable under the Fourth Amendment even if state law forbade the arrest (requiring a summons); the search incident requires no additional justification, and a state-law-only violation does not trigger exclusion."
lake:
  record_id: Virginia v. Moore
  status: verified
  projected_at: 2026-07-06
---

# Virginia v. Moore

*553 U.S. 164 (2008)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers stopped Moore and determined he was driving on a suspended license — a misdemeanor for which Virginia law directed officers to issue a summons rather than make a custodial arrest. The officers arrested Moore anyway, searched him incident to the arrest, and found crack cocaine. Moore moved to suppress, arguing the arrest violated state law and the search was therefore invalid.

## Issue
Does the Fourth Amendment require suppression of evidence found in a search incident to an arrest that was based on probable cause but prohibited by state law, where state law required a citation instead of a custodial arrest?

## Rule
No. "[W]arrantless arrests for crimes committed in the presence of an arresting officer are reasonable under the Constitution, and . . . while States are free to regulate such arrests however they desire, state restrictions do not alter the Fourth Amendment's protections." — 128 S. Ct. at 1607. ^pin-1607

Because such an arrest is constitutionally valid, "officers may perform searches incident to constitutionally permissible arrests in order to ensure their safety and safeguard evidence" — a "search incident to the arrest requires no additional justification." — *Id.* (quoting *United States v. Robinson*). And because only state law, not the Constitution, was violated, "[t]hat Amendment does not require the exclusion of evidence obtained from a constitutionally permissible arrest." Reaffirming the rule, the Court held: "When officers have probable cause to believe that a person has committed a crime in their presence, the Fourth Amendment permits them to make an arrest, and to search the suspect in order to safeguard evidence and ensure their own safety." — *Id.* at 1608. ^pin-1608

## Application
The officers had probable cause to believe Moore was driving on a suspended license — an offense committed in their presence — so the arrest was reasonable under the Fourth Amendment even though Virginia law called for a summons. The Fourth Amendment is not a vehicle for enforcing state arrest law. Because the arrest was constitutionally permissible, the search incident to it required no additional justification, and the cocaine it produced was admissible. *[[Knowles v. Iowa]]* did not control, because Moore was arrested — and therefore the officers faced the custodial risks that justify a full search — rather than merely cited.

## Conclusion
The arrest and the search incident to it were constitutional; the Fourth Amendment did not require suppression. The judgment of the Supreme Court of Virginia was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Moore* remains controlling: a probable-cause arrest is Fourth-Amendment-reasonable regardless of contrary state arrest law, the search incident follows automatically, and a state-law-only violation does not trigger the exclusionary rule. It applies [[United States v. Robinson]] and runs alongside [[Atwater v. City of Lago Vista]] and [[Devenpeck v. Alford]]. No negative treatment.

## Appears on
- [[Arrest and Arrest Warrants]] — *Key*
- [[Seizure of the Person]] — *Related (cross-doctrine)*
- [[SIA Persons]] — *Related (cross-doctrine)*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Virginia v. Moore*, 553 U.S. 164 (2008) — https://www.courtlistener.com/opinion/145814/virginia-v-moore/ — pinpoints (S. Ct. reporter, per CL copy): 1607, 1608.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "540d7c0322253b75", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "553 U.S. 164 (2008)", "court": "U.S. Supreme Court", "neutral_cite": "2008 U.S. LEXIS 3674", "official_citation_present": true, "parallel_cite": "128 S. Ct. 1598; 170 L. Ed. 2d 559", "title": "Virginia v. Moore", "year": "2008"}}
{"assertion_id": "3b76a8564562ea87", "dimension": "support", "kind": "home_role", "locator": {"home": "The Exclusionary Rule"}, "payload": {"home": "The Exclusionary Rule", "role": "Related (cross-doctrine)", "title": "Virginia v. Moore"}}
{"assertion_id": "426bc39f3117ac0a", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest and Arrest Warrants"}, "payload": {"home": "Arrest and Arrest Warrants", "role": "Key — a state-law arrest violation is not a Fourth Amendment violation", "title": "Virginia v. Moore"}}
{"assertion_id": "5b4ad5a26be9bda4", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Related (cross-doctrine)", "title": "Virginia v. Moore"}}
{"assertion_id": "f4908d8d03b358ab", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "Virginia v. Moore"}}
{"assertion_id": "ff03ee699c91dfda", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless arrest on probable cause for a crime committed in the officer's presence is reasonable under the Fourth Amendment even if state law forbade the arrest (requiring a summons); the search incident requires no additional justification, and a state-law-only violation does not trigger exclusion.", "title": "Virginia v. Moore"}}
{"assertion_id": "662c9e978792d0dd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Virginia v. Moore"}}
{"assertion_id": "deb194fbef316f17", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2008-04-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Virginia v. Moore", "field_i_validity": "good_law", "scope_note": "Controlling: an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law; the search incident follows and no suppression results from the state-law violation.", "title": "Virginia v. Moore", "varies_by_point": "false"}}
```

### lake record — Virginia v. Moore

```json
{
  "schema_version": "s2.v1",
  "record_id": "Virginia v. Moore",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Virginia v. Moore",
    "case_name_short": "Moore",
    "case_name_full": "Virginia v. Moore",
    "input_case_name": "Virginia v. Moore",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2008-04-23",
    "year": 2008,
    "docket": "06-1082",
    "cluster_id": 145814,
    "lead_opinion_id": 145814,
    "sibling_ids": [
      145814,
      9435233,
      9435234
    ],
    "absolute_url": "/opinion/145814/virginia-v-moore/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "553 U.S. 164",
      "volume": "553",
      "reporter": "U.S.",
      "page": "164",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "128 S. Ct. 1598",
        "volume": "128",
        "reporter": "S. Ct.",
        "page": "1598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "170 L. Ed. 2d 559",
        "volume": "170",
        "reporter": "L. Ed. 2d",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2008 U.S. LEXIS 3674",
        "volume": "2008",
        "reporter": "U.S. LEXIS",
        "page": "3674",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "553 U.S. 164",
        "volume": "553",
        "reporter": "U.S.",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "128 S. Ct. 1598",
        "volume": "128",
        "reporter": "S. Ct.",
        "page": "1598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "170 L. Ed. 2d 559",
        "volume": "170",
        "reporter": "L. Ed. 2d",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 U.S. LEXIS 3674",
        "volume": "2008",
        "reporter": "U.S. LEXIS",
        "page": "3674",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "553 U.S. 164",
    "official_selection": {
      "court_class": "scotus",
      "selected": "553 U.S. 164",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1607",
      "page": null,
      "quote": "--- # Virginia v. Moore *553 U.S. 164 (2008)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers stopped Moore and determined he was driving on a suspended license \u2014 a misdemeanor for which Virginia law directed officers to issue a summons rather than make a custodial arrest. The officers arrested Moore anyway, searched him incident to the arrest, and found crack cocaine. Moore moved to suppress, arguing the arrest violated state law and the search was therefore invalid. ## Issue Does the Fourth Amendment require suppression of evidence found in a search incident to an arrest that was based on probable cause but prohibited by state law, where state law required a citation instead of a custodial arrest? ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1608",
      "page": null,
      "quote": "officers may perform searches incident to constitutionally permissible arrests in order to ensure their safety and safeguard evidence",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2008-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Virginia v. Moore",
    "varies_by_point": false,
    "scope_note": "Controlling: an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law; the search incident follows and no suppression results from the state-law violation.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Bohigian",
          "cluster_id": 4806187,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ragbir v. Homan",
          "cluster_id": 8443991,
          "cite": [
            "923 F.3d 53"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Islas",
          "cluster_id": 4597157,
          "cite": [
            "443 P.3d 274",
            "165 Idaho 260"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ted Phillips",
          "cluster_id": 4250252,
          "cite": [
            "834 F.3d 1176",
            "2016 WL 4435613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kelm",
          "cluster_id": 890265,
          "cite": [
            "2013 MT 115",
            "370 Mont. 61",
            "300 P.3d 687",
            "2013 WL 1804265",
            "2013 Mont. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
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
        "journal_ref": "Virginia v. Moore:lane1_negative"
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
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mattos v. Agarano",
          "cluster_id": 615433,
          "cite": [
            "661 F.3d 433",
            "2011 WL 4908374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York State Rifle & Pistol Assn., Inc. v. Bruen",
          "cluster_id": 6480696,
          "cite": [
            "597 U.S. 1",
            "142 S. Ct. 2111",
            "213 L. Ed. 2d 387"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Redd",
          "cluster_id": 2387024,
          "cite": [
            "48 Cal. 4th 691",
            "229 P.3d 101",
            "108 Cal. Rptr. 3d 192",
            "2010 Cal. LEXIS 3749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. City of Los Angeles",
          "cluster_id": 3053953,
          "cite": [
            "548 F.3d 1197",
            "2008 WL 4878904"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Quinn v. Young",
          "cluster_id": 2786042,
          "cite": [
            "780 F.3d 998",
            "2015 U.S. App. LEXIS 3959",
            "2015 WL 1089573"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elliott v. State",
          "cluster_id": 7479349,
          "cite": [
            "824 S.E.2d 265",
            "305 Ga. 179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Ontario v. Quon",
          "cluster_id": 148797,
          "cite": [
            "177 L. Ed. 2d 216",
            "130 S. Ct. 2619",
            "560 U.S. 746",
            "2010 U.S. LEXIS 4972"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edgerly v. City and County of San Francisco",
          "cluster_id": 409,
          "cite": [
            "599 F.3d 946",
            "2010 U.S. App. LEXIS 5697",
            "2010 WL 986764"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Victor Garcia-Rodriguez",
          "cluster_id": 4400153,
          "cite": [
            "162 Idaho 271",
            "396 P.3d 700",
            "2017 WL 2569786",
            "2017 Ida. LEXIS 171"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bishop",
          "cluster_id": 2640962,
          "cite": [
            "203 P.3d 1203",
            "146 Idaho 804",
            "2009 Ida. LEXIS 19"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buck v. City of Albuquerque",
          "cluster_id": 171480,
          "cite": [
            "549 F.3d 1269",
            "2008 U.S. App. LEXIS 25450",
            "2008 WL 5147474"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stephen G. House",
          "cluster_id": 802697,
          "cite": [
            "684 F.3d 1173",
            "2012 U.S. App. LEXIS 12596",
            "2012 WL 2343665"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liberal v. Estrada",
          "cluster_id": 183026,
          "cite": [
            "632 F.3d 1064",
            "2011 U.S. App. LEXIS 957",
            "2011 WL 149348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2637645,
          "cite": [
            "224 P.3d 55",
            "47 Cal. 4th 1104",
            "104 Cal. Rptr. 3d 727",
            "2010 Cal. LEXIS 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amobi v. District of Columbia Department of Corrections",
          "cluster_id": 2680783,
          "cite": [
            "410 U.S. App. D.C. 338",
            "755 F.3d 980",
            "38 I.E.R. Cas. (BNA) 1116",
            "2014 WL 2895933",
            "2014 U.S. App. LEXIS 12117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Antoine Jones v. Steve Kirchner",
          "cluster_id": 4251490,
          "cite": [
            "835 F.3d 74",
            "2016 U.S. App. LEXIS 15759"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walker v. Prince George's County, Md.",
          "cluster_id": 1029542,
          "cite": [
            "575 F.3d 426",
            "2009 U.S. App. LEXIS 16872",
            "2009 WL 2343614"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miguel Gutierrez v. Michael Kermon",
          "cluster_id": 2709559,
          "cite": [
            "722 F.3d 1003",
            "2013 WL 3481359",
            "2013 U.S. App. LEXIS 14101"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145814 OR 9435233 OR 9435234) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjk3MzgyNDAwMDAwJnM9MjQ2NzYwOCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145814+OR+9435233+OR+9435234%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(145814 OR 9435233 OR 9435234)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MiZzPTE4MDMzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145814+OR+9435233+OR+9435234%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145814 OR 9435233 OR 9435234)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 0,
        "triage_snippet_classified": 40
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145814 OR 9435233 OR 9435234)",
    "indexed_citing_opinions": 401,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145814,
        "count": 306,
        "count_source": "search"
      },
      {
        "opinion_id": 9435233,
        "count": 96,
        "count_source": "search"
      },
      {
        "opinion_id": 9435234,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 795,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/virginia-v-moore.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxOTI3NTUmcz0xMDMyNTMyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145814+OR+9435233+OR+9435234%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145814,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 137733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 1063368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 1322589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 1344610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 3579530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 3580565,
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
    "date_created": "2026-07-06T03:53:16Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:53:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:53:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:56:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:53:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Virginia v. Moore

```
(Slip Opinion)              OCTOBER TERM, 2007                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                           VIRGINIA v. MOORE

        CERTIORARI TO THE SUPREME COURT OF VIRGINIA

    No. 06–1082. Argued January 14, 2008—Decided April 23, 2008
Rather than issuing the summons required by Virginia law, police ar-
  rested respondent Moore for the misdemeanor of driving on a sus-
  pended license. A search incident to the arrest yielded crack cocaine,
  and Moore was tried on drug charges. The trial court declined to
  suppress the evidence on Fourth Amendment grounds. Moore was
  convicted. Ultimately, the Virginia Supreme Court reversed, reason-
  ing that the search violated the Fourth Amendment because the ar-
  resting officers should have issued a citation under state law, and the
  Fourth Amendment does not permit search incident to citation.
Held: The police did not violate the Fourth Amendment when they
 made an arrest that was based on probable cause but prohibited by
 state law, or when they performed a search incident to the arrest.
 Pp. 3–13.
    (a) Because the founding era’s statutes and common law do not
 support Moore’s view that the Fourth Amendment was intended to
 incorporate statutes, this is “not a case in which the claimant can
 point to a ‘clear answer [that] existed in 1791 and has been generally
 adhered to by the traditions of our society ever since,’ ” Atwater v.
 Lago Vista, 532 U. S. 318, 345. Pp. 3–5.
    (b) Where history provides no conclusive answer, this Court has
 analyzed a search or seizure in light of traditional reasonableness
 standards “by assessing, on the one hand, the degree to which it in-
 trudes upon an individual’s privacy and, on the other, the degree to
 which it is needed for the promotion of legitimate governmental in-
 terests.” Wyoming v. Houghton, 526 U. S. 295, 300. Applying that
 methodology, this Court has held that when an officer has probable
 cause to believe a person committed even a minor crime, the arrest is
 constitutionally reasonable. Atwater, supra, at 354. This Court’s de-
 cisions counsel against changing the calculus when a State chooses to
2                          VIRGINIA v. MOORE

                                  Syllabus

    protect privacy beyond the level required by the Fourth Amendment.
    See, e.g., Whren v. United States, 517 U. S. 35. United States v. Di
    Re, 332 U. S. 581, distinguished. Pp. 6–8.
       (c) The Court adheres to this approach because an arrest based on
    probable cause serves interests that justify seizure. Arrest ensures
    that a suspect appears to answer charges and does not continue a
    crime, and it safeguards evidence and enables officers to conduct an
    in-custody investigation. A State’s choice of a more restrictive
    search-and-seizure policy does not render less restrictive ones unrea-
    sonable, and hence unconstitutional. While States are free to require
    their officers to engage in nuanced determinations of the need for ar-
    rest as a matter of their own law, the Fourth Amendment should re-
    flect administrable bright-line rules. Incorporating state arrest rules
    into the Constitution would make Fourth Amendment protections as
    complex as the underlying state law, and variable from place to place
    and time to time. Pp. 8–11.
       (d) The Court rejects Moore’s argument that even if the Constitu-
    tion allowed his arrest, it did not allow the arresting officers to
    search him. Officers may perform searches incident to constitution-
    ally permissible arrests in order to ensure their safety and safeguard
    evidence. United States v. Robinson, 414 U. S. 218. While officers is-
    suing citations do not face the same danger, and thus do not have the
    same authority to search, Knowles v. Iowa, 525 U. S. 113, the officers
    arrested Moore, and therefore faced the risks that are “an adequate
    basis for treating all custodial arrests alike for purposes of search
    justification,” Robinson, supra, at 235. Pp. 11–13.
272 Va. 717, 636 S. E. 2d 395, reversed and remanded.

   SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and STEVENS, KENNEDY, SOUTER, THOMAS, BREYER, and ALITO, JJ.,
joined. GINSBURG, J., filed an opinion concurring in the judgment.
                        Cite as: 553 U. S. ____ (2008)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 06–1082
                                   _________________


    VIRGINIA, PETITIONER v. DAVID LEE MOORE
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       VIRGINIA

                                 [April 23, 2008] 


  JUSTICE SCALIA delivered the opinion of the Court.
  We consider whether a police officer violates the Fourth
Amendment by making an arrest based on probable cause
but prohibited by state law.
                             I
  On February 20, 2003, two City of Portsmouth police
officers stopped a car driven by David Lee Moore. They
had heard over the police radio that a person known as
“Chubs” was driving with a suspended license, and one of
the officers knew Moore by that nickname. The officers
determined that Moore’s license was in fact suspended,
and arrested him for the misdemeanor of driving on a
suspended license, which is punishable under Virginia law
by a year in jail and a $2,500 fine, Va. Code Ann. §§18.2–
11, 18.2–272, 46.2–301(C) (Lexis 2005). The officers sub-
sequently searched Moore and found that he was carrying
16 grams of crack cocaine and $516 in cash.1 See 272 Va.
——————
  1 The arresting officers did not perform a search incident to arrest

immediately upon taking Moore into custody, because each of them
mistakenly believed that the other had done so. App. 54–55; see also
id., at 33–34. They realized their mistake after arriving with Moore at
Moore’s hotel room, which they had obtained his consent to search, and
2                       VIRGINIA v. MOORE

                         Opinion of the Court

717, 636 S. E. 2d 395 (2006); 45 Va. App. 146, 609 S. E. 2d
74 (2005).
   Under state law, the officers should have issued Moore a
summons instead of arresting him. Driving on a sus-
pended license, like some other misdemeanors, is not an
arrestable offense except as to those who “fail or refuse to
discontinue” the violation, and those whom the officer
reasonably believes to be likely to disregard a summons,
or likely to harm themselves or others. Va. Code Ann.
§19.2–74 (Lexis 2004). The intermediate appellate court
found none of these circumstances applicable, and Virginia
did not appeal that determination. See 272 Va., at 720,
n. 3, 636 S. E. 2d, at 396–397, n. 3. Virginia also permits
arrest for driving on a suspended license in jurisdictions
where “prior general approval has been granted by order
of the general district court,” Va. Code Ann. §46.2–936;
Virginia has never claimed such approval was in effect in
the county where Moore was arrested.
   Moore was charged with possessing cocaine with the
intent to distribute it in violation of Virginia law. He filed
a pretrial motion to suppress the evidence from the arrest
search. Virginia law does not, as a general matter, require
suppression of evidence obtained in violation of state law.
See 45 Va. App., at 160–162, 609 S. E. 2d, at 82 (Annun-
ziata, J., dissenting). Moore argued, however, that sup-
pression was required by the Fourth Amendment. The
trial court denied the motion, and after a bench trial found
Moore guilty of the drug charge and sentenced him to a 5-
year prison term, with one year and six months of the
sentence suspended. The conviction was reversed by a
panel of Virginia’s intermediate court on Fourth Amend-
ment grounds, id., at 149–150, 609 S. E. 2d, at 76, rein-
stated by the intermediate court sitting en banc, 47 Va.
—————— 

they searched his person there. Ibid. Moore does not contend that this

delay violated the Fourth Amendment. 

                    Cite as: 553 U. S. ____ (2008)                   3

                         Opinion of the Court

App. 55, 622 S. E. 2d 253 (2005), and finally reversed
again by the Virginia Supreme Court, 272 Va., at 725, 636
S. E. 2d, at 400. The Court reasoned that since the arrest-
ing officers should have issued Moore a citation under
state law, and the Fourth Amendment does not permit
search incident to citation, the arrest search violated the
Fourth Amendment. Ibid. We granted certiorari. 551
U. S. ___ (2007).
                            II
  The Fourth Amendment protects “against unreasonable
searches and seizures” of (among other things) the person.
In determining whether a search or seizure is unreason-
able, we begin with history. We look to the statutes and
common law of the founding era to determine the norms
that the Fourth Amendment was meant to preserve. See
Wyoming v. Houghton, 526 U. S. 295, 299 (1999); Wilson v.
Arkansas, 514 U. S. 927, 931 (1995).
  We are aware of no historical indication that those who
ratified the Fourth Amendment understood it as a redun-
dant guarantee of whatever limits on search and seizure
legislatures might have enacted.2 The immediate object of
the Fourth Amendment was to prohibit the general war-
——————
   2 Atwater v. Lago Vista, 532 U. S. 318 (2001), rejected the view

JUSTICE GINSBURG advances that the legality of arrests for misdemean-
ors involving no breach of the peace “depended on statutory authoriza-
tion.” Post, at 1, n. 1 (opinion concurring in judgment). Atwater cited
both of the sources on which JUSTICE GINSBURG relies for a limited view
of common-law arrest authority, but it also identified and quoted
numerous treatises that described common-law authority to arrest for
minor misdemeanors without limitation to cases in which a statute
authorized arrest. See 532 U. S., at 330–332. Atwater noted that many
statutes authorized arrest for misdemeanors other than breaches of the
peace, but it concluded that the view of arrest authority as extending
beyond breaches of the peace also reflected judge-made common law.
Id., at 330–331. Particularly since Atwater considered the materials on
which JUSTICE GINSBURG relies, we see no reason to revisit the case’s
conclusion.
4                         VIRGINIA v. MOORE

                           Opinion of the Court

rants and writs of assistance that English judges had
employed against the colonists, Boyd v. United States, 116
U. S. 616, 624–627 (1886); Payton v. New York, 445 U. S.
573, 583–584 (1980). That suggests, if anything, that
founding-era citizens were skeptical of using the rules for
search and seizure set by government actors as the index
of reasonableness.
   Joseph Story, among others, saw the Fourth Amend-
ment as “little more than the affirmance of a great consti-
tutional doctrine of the common law,” 3 Commentaries on
the Constitution of the United States §1895, p. 748 (1833),
which Story defined in opposition to statutes, see Codifica-
tion of the Common Law in The Miscellaneous Writings of
Joseph Story 698, 699, 701 (W. Story ed. 1852). No early
case or commentary, to our knowledge, suggested the
Amendment was intended to incorporate subsequently
enacted statutes. None of the early Fourth Amendment
cases that scholars have identified sought to base a consti-
tutional claim on a violation of a state or federal statute
concerning arrest. See Davies, Recovering the Original
Fourth Amendment, 98 Mich. L. Rev. 547, 613–614
(1999);3 see also T. Taylor, Two Studies in Constitutional
Interpretation 44–45 (1969).
   Of course such a claim would not have been available
against state officers, since the Fourth Amendment was a
restriction only upon federal power, see Barron ex rel.
Tiernan v. Mayor of Baltimore, 7 Pet. 243 (1833). But
early Congresses tied the arrest authority of federal offi-
cers to state laws of arrest. See United States v. Di Re,
——————
  3 Of the early cases that Davies collects, see 98 Mich. L. Rev., at 613,

n. 174; id., at 614, n. 175, the lone decision to treat statutes as relevant
to the Fourth Amendment’s contours simply applied the principle that
statutes enacted in the years immediately before or after the Amend-
ment was adopted shed light on what citizens at the time of the Amend-
ment’s enactment saw as reasonable. Boyd v. United States, 116 U. S.
616, 622–623 (1886).
                     Cite as: 553 U. S. ____ (2008)                 5

                         Opinion of the Court

332 U. S. 581, 589 (1948); United States v. Watson, 423
U. S. 411, 420 (1976). Moreover, even though several
state constitutions also prohibited unreasonable searches
and seizures, citizens who claimed officers had violated
state restrictions on arrest did not claim that the viola-
tions also ran afoul of the state constitutions.4 The appar-
ent absence of such litigation is particularly striking in
light of the fact that searches incident to warrantless
arrests (which is to say arrests in which the officer was
not insulated from private suit) were, as one commentator
has put it, “taken for granted” at the founding, Taylor,
supra, at 45, as were warrantless arrests themselves,
Amar, Fourth Amendment First Principles, 107 Harv.
L. Rev. 757, 764 (1994).
   There are a number of possible explanations of why such
constitutional claims were not raised. Davies, for exam-
ple, argues that actions taken in violation of state law
could not qualify as state action subject to Fourth
Amendment constraints. 98 Mich. L. Rev., at 660–663.
Be that as it may, as Moore adduces neither case law nor
commentaries to support his view that the Fourth
Amendment was intended to incorporate statutes, this is
“not a case in which the claimant can point to ‘a clear
answer [that] existed in 1791 and has been generally
adhered to by the traditions of our society ever since.’ ”
Atwater v. Lago Vista, 532 U. S. 318, 345 (2001) (altera-
tion in original).


——————
  4 Massachusetts,  for example, had a state constitutional provision
paralleling the Fourth Amendment, but the litigants in the earliest
cases we have identified claiming violations of arrest statutes in the
Commonwealth did not argue that their arrests violated the Common-
wealth’s Constitution. See Brock v. Stimson, 108 Mass. 520 (1871);
Phillips v. Fadden, 125 Mass. 198 (1878); see also Tubbs v. Tukey, 57
Mass. 438 (1849) (asserting violation of state common law concerning
arrest but not asserting violation of state constitution).
6                   VIRGINIA v. MOORE

                     Opinion of the Court

                             III
                              A
  When history has not provided a conclusive answer, we
have analyzed a search or seizure in light of traditional
standards of reasonableness “by assessing, on the one
hand, the degree to which it intrudes upon an individual’s
privacy and, on the other, the degree to which it is needed
for the promotion of legitimate governmental interests.”
Houghton, 526 U. S., at 300; see also Atwater, 532 U. S., at
346. That methodology provides no support for Moore’s
Fourth Amendment claim. In a long line of cases, we have
said that when an officer has probable cause to believe a
person committed even a minor crime in his presence, the
balancing of private and public interests is not in doubt.
The arrest is constitutionally reasonable. Id., at 354; see
also, e.g., Devenpeck v. Alford, 543 U. S. 146, 152 (2004);
Gerstein v. Pugh, 420 U. S. 103, 111 (1975); Brinegar v.
United States, 338 U. S. 160, 164, 170, 175–176 (1949).
  Our decisions counsel against changing this calculus
when a State chooses to protect privacy beyond the level
that the Fourth Amendment requires. We have treated
additional protections exclusively as matters of state law.
In Cooper v. California, 386 U. S. 58 (1967), we reversed a
state court that had held the search of a seized vehicle to
be in violation of the Fourth Amendment because state
law did not explicitly authorize the search. We concluded
that whether state law authorized the search was irrele-
vant. States, we said, remained free “to impose higher
standards on searches and seizures than required by the
Federal Constitution,” id., at 62, but regardless of state
rules, police could search a lawfully seized vehicle as a
matter of federal constitutional law.
  In California v. Greenwood, 486 U. S. 35 (1988), we held
that search of an individual’s garbage forbidden by Cali-
fornia’s Constitution was not forbidden by the Fourth
Amendment. “[W]hether or not a search is reasonable
                 Cite as: 553 U. S. ____ (2008)           7

                     Opinion of the Court

within the meaning of the Fourth Amendment,” we said,
has never “depend[ed] on the law of the particular State in
which the search occurs.” Id., at 43. While “[i]ndividual
States may surely construe their own constitutions as
imposing more stringent constraints on police conduct
than does the Federal Constitution,” ibid., state law did
not alter the content of the Fourth Amendment.
   We have applied the same principle in the seizure con-
text. Whren v. United States, 517 U. S. 806 (1996), held
that police officers had acted reasonably in stopping a car,
even though their action violated regulations limiting the
authority of plainclothes officers in unmarked vehicles.
We thought it obvious that the Fourth Amendment’s
meaning did not change with local law enforcement prac-
tices—even practices set by rule. While those practices
“vary from place to place and from time to time,” Fourth
Amendment protections are not “so variable” and cannot
“be made to turn upon such trivialities.” Id., at 815.
   Some decisions earlier than these excluded evidence
obtained in violation of state law, but those decisions
rested on our supervisory power over the federal courts,
rather than the Constitution. In Di Re, 332 U. S. 581,
federal and state officers collaborated in an investigation
that led to an arrest for a federal crime. The Government
argued that the legality of an arrest for a federal offense
was a matter of federal law. Id., at 589. We concluded,
however, that since Congress had provided that arrests
with warrants must be made in accordance with state law,
the legality of arrests without warrants should also be
judged according to state-law standards. Id., at 589–590.
This was plainly not a rule we derived from the Constitu-
tion, however, because we repeatedly invited Congress to
change it by statute—saying that state law governs the
validity of a warrantless arrest “in [the] absence of an
applicable federal statute,” id., at 589, and that the Di Re
rule applies “except in those cases where Congress has
8                    VIRGINIA v. MOORE

                     Opinion of the Court

enacted a federal rule,” id., at 589–590.
  Later decisions did not expand the rule of Di Re. John-
son v. United States, 333 U. S. 10 (1948), relied on Di Re to
suppress evidence obtained under circumstances identical
in relevant respects to those in that case. See 333 U. S., at
12, 15, n. 5. And Michigan v. DeFillippo, 443 U. S. 31
(1979), upheld a warrantless arrest in a case where com-
pliance with state law was not at issue. While our opinion
said that “[w]hether an officer is authorized to make an
arrest ordinarily depends, in the first instance, on state
law,” it also said that a warrantless arrest satisfies the
Constitution so long as the officer has “probable cause to
believe that the suspect has committed or is committing a
crime.” Id., at 36. We need not pick and choose among the
dicta: Neither Di Re nor the cases following it held that
violations of state arrest law are also violations of the
Fourth Amendment, and our more recent decisions, dis-
cussed above, have indicated that when States go above
the Fourth Amendment minimum, the Constitution’s
protections concerning search and seizure remain the
same.
                            B
   We are convinced that the approach of our prior cases is
correct, because an arrest based on probable cause serves
interests that have long been seen as sufficient to justify
the seizure. Whren, supra, at 817; Atwater, supra, at 354.
Arrest ensures that a suspect appears to answer charges
and does not continue a crime, and it safeguards evidence
and enables officers to conduct an in-custody investiga-
tion. See W. LaFave, Arrest: The Decision to Take a
Suspect into Custody 177–202 (1965).
   Moore argues that a State has no interest in arrest
when it has a policy against arresting for certain crimes.
That is not so, because arrest will still ensure a suspect’s
appearance at trial, prevent him from continuing his
                 Cite as: 553 U. S. ____ (2008)            9

                     Opinion of the Court

offense, and enable officers to investigate the incident
more thoroughly. State arrest restrictions are more accu-
rately characterized as showing that the State values its
interests in forgoing arrests more highly than its interests
in making them, see, e.g., Dept. of Justice, National Insti-
tute of Justice, D. Whitcomb, B. Lewin, & M. Levine,
Issues and Practices: Citation Release 17 (Mar. 1984)
(describing cost savings as a principal benefit of citation-
release ordinances); or as showing that the State places a
higher premium on privacy than the Fourth Amendment
requires. A State is free to prefer one search-and-seizure
policy among the range of constitutionally permissible
options, but its choice of a more restrictive option does not
render the less restrictive ones unreasonable, and hence
unconstitutional.
   If we concluded otherwise, we would often frustrate
rather than further state policy. Virginia chooses to pro-
tect individual privacy and dignity more than the Fourth
Amendment requires, but it also chooses not to attach to
violations of its arrest rules the potent remedies that
federal courts have applied to Fourth Amendment viola-
tions. Virginia does not, for example, ordinarily exclude
from criminal trials evidence obtained in violation of its
statutes. See 45 Va. App., at 161, 609 S. E. 2d, at 82
(Annunziata, J., dissenting) (citing Janis v. Common-
wealth, 22 Va. App. 646, 651, 472 S. E. 2d 649, 652
(1996)). Moore would allow Virginia to accord enhanced
protection against arrest only on pain of accompanying
that protection with federal remedies for Fourth Amend-
ment violations, which often include the exclusionary rule.
States unwilling to lose control over the remedy would
have to abandon restrictions on arrest altogether. This is
an odd consequence of a provision designed to protect
against searches and seizures.
   Even if we thought that state law changed the nature of
the Commonwealth’s interests for purposes of the Fourth
10                   VIRGINIA v. MOORE

                     Opinion of the Court

Amendment, we would adhere to the probable-cause stan-
dard. In determining what is reasonable under the Fourth
Amendment, we have given great weight to the “essential
interest in readily administrable rules.” Atwater, 532
U. S., at 347. In Atwater, we acknowledged that nuanced
judgments about the need for warrantless arrest were
desirable, but we nonetheless declined to limit to felonies
and disturbances of the peace the Fourth Amendment rule
allowing arrest based on probable cause to believe a law
has been broken in the presence of the arresting officer.
Id., at 346–347. The rule extends even to minor misde-
meanors, we concluded, because of the need for a bright-
line constitutional standard. If the constitutionality of
arrest for minor offenses turned in part on inquiries as to
risk of flight and danger of repetition, officers might be
deterred from making legitimate arrests. Id., at 351. We
found little to justify this cost, because there was no “epi-
demic of unnecessary minor-offense arrests,” and hence “a
dearth of horribles demanding redress.” Id., at 353.
   Incorporating state-law arrest limitations into the Con-
stitution would produce a constitutional regime no less
vague and unpredictable than the one we rejected in
Atwater. The constitutional standard would be only as
easy to apply as the underlying state law, and state law
can be complicated indeed. The Virginia statute in this
case, for example, calls on law enforcement officers to
weigh just the sort of case-specific factors that Atwater
said would deter legitimate arrests if made part of the
constitutional inquiry. It would authorize arrest if a
misdemeanor suspect fails or refuses to discontinue the
unlawful act, or if the officer believes the suspect to be
likely to disregard a summons. Va. Code Ann. §19.2–
74.A.1. Atwater specifically noted the “extremely poor
judgment” displayed in arresting a local resident who
would “almost certainly” have discontinued the offense
and who had “no place to hide and no incentive to flee.”
                  Cite as: 553 U. S. ____ (2008)           11

                      Opinion of the Court

532 U. S., at 346–347. It nonetheless declined to make
those considerations part of the constitutional calculus.
Atwater differs from this case in only one significant re-
spect: It considered (and rejected) federal constitutional
remedies for all minor-misdemeanor arrests; Moore seeks
them in only that subset of minor-misdemeanor arrests in
which there is the least to be gained—that is, where the
State has already acted to constrain officers’ discretion
and prevent abuse. Here we confront fewer horribles than
in Atwater, and less of a need for redress.
   Finally, linking Fourth Amendment protections to state
law would cause them to “vary from place to place and
from time to time,” Whren, 517 U. S., at 815. Even at the
same place and time, the Fourth Amendment’s protections
might vary if federal officers were not subject to the same
statutory constraints as state officers. In Elkins v. United
States, 364 U. S. 206, 210–212 (1960), we noted the practi-
cal difficulties posed by the “silver-platter doctrine,” which
had imposed more stringent limitations on federal officers
than on state police acting independent of them. It would
be strange to construe a constitutional provision that did
not apply to the States at all when it was adopted to now
restrict state officers more than federal officers, solely
because the States have passed search-and-seizure laws
that are the prerogative of independent sovereigns.
   We conclude that warrantless arrests for crimes com-
mitted in the presence of an arresting officer are reason-
able under the Constitution, and that while States are free
to regulate such arrests however they desire, state restric-
tions do not alter the Fourth Amendment’s protections.
                              IV
  Moore argues that even if the Constitution allowed his
arrest, it did not allow the arresting officers to search him.
We have recognized, however, that officers may perform
searches incident to constitutionally permissible arrests in
12                   VIRGINIA v. MOORE

                      Opinion of the Court

order to ensure their safety and safeguard evidence.
United States v. Robinson, 414 U. S. 218 (1973). We have
described this rule as covering any “lawful arrest,” id., at
235, with constitutional law as the reference point. That
is to say, we have equated a lawful arrest with an arrest
based on probable cause: “A custodial arrest of a suspect
based on probable cause is a reasonable intrusion under
the Fourth Amendment; that intrusion being lawful, a
search incident to the arrest requires no additional justifi-
cation.” Ibid. (emphasis added). Moore correctly notes
that several important state-court decisions have defined
the lawfulness of arrest in terms of compliance with state
law. See Brief for Respondent 32–33 (citing People v.
Chiagles, 237 N. Y. 193, 197, 142 N. E. 583, 584 (1923);
People v. DeFore, 242 N. Y. 13, 17–19, 150 N. E. 585, 586
(1926)). But it is not surprising that States have used
“lawful” as shorthand for compliance with state law, while
our constitutional decision in Robinson used “lawful” as
shorthand for compliance with constitutional constraints.
   The interests justifying search are present whenever an
officer makes an arrest. A search enables officers to safe-
guard evidence, and, most critically, to ensure their safety
during “the extended exposure which follows the taking of
a suspect into custody and transporting him to the police
station.” Robinson, supra, at 234–235. Officers issuing
citations do not face the same danger, and we therefore
held in Knowles v. Iowa, 525 U. S. 113 (1998), that they do
not have the same authority to search. We cannot agree
with the Virginia Supreme Court that Knowles controls
here. The state officers arrested Moore, and therefore
faced the risks that are “an adequate basis for treating all
custodial arrests alike for purposes of search justification.”
Robinson, supra, at 235.
   The Virginia Supreme Court may have concluded that
Knowles required the exclusion of evidence seized from
Moore because, under state law, the officers who arrested
                 Cite as: 553 U. S. ____ (2008)           13

                     Opinion of the Court

Moore should have issued him a citation instead. This
argument might have force if the Constitution forbade
Moore’s arrest, because we have sometimes excluded
evidence obtained through unconstitutional methods in
order to deter constitutional violations. See Wong Sun v.
United States, 371 U. S. 471, 484–485, 488 (1963). But the
arrest rules that the officers violated were those of state
law alone, and as we have just concluded, it is not the
province of the Fourth Amendment to enforce state law.
That Amendment does not require the exclusion of evi-
dence obtained from a constitutionally permissible arrest.
                        *    *    *
  We reaffirm against a novel challenge what we have
signaled for more than half a century. When officers have
probable cause to believe that a person has committed a
crime in their presence, the Fourth Amendment permits
them to make an arrest, and to search the suspect in order
to safeguard evidence and ensure their own safety. The
judgment of the Supreme Court of Virginia is reversed,
and the case is remanded for further proceedings not
inconsistent with this opinion.
                                           It is so ordered.
                         Cite as: 553 U. S. ____ (2008)                              1

                    GINSBURG, J., concurring in judgment

      NOTICE: This opinion is subject to formal revision before publication in the
      preliminary print of the United States Reports. Readers are requested to
      notify the Reporter of Decisions, Supreme Court of the United States, Wash-
      ington, D. C. 20543, of any typographical or other formal errors, in order
      that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                    No. 06–1082
                                    _________________


     VIRGINIA, PETITIONER v. DAVID LEE MOORE
     ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                        VIRGINIA

                                  [April 23, 2008] 


  JUSTICE GINSBURG, concurring in the judgment.
  I find in the historical record more support for Moore’s
position than the Court does, ante, at 3–5.1 Further, our
decision in United States v. Di Re, 332 U. S. 581, 587–590
(1948), requiring suppression of evidence gained in a
search incident to an unlawful arrest, seems to me pinned
——————
  1 Under the common law prevailing at the end of the 19th century, it

appears that arrests for minor misdemeanors, typically involving no
breach of the peace, depended on statutory authorization. See Wilgus,
Arrest Without a Warrant, 22 Mich. L. Rev. 541, 674 (1924) (“Neither
[an officer] nor [a citizen], without statutory authority, may arrest [a
defendant] for . . . a misdemeanor which is not a [breach of the peace]”
(emphasis added)); 9 Halsbury, Laws of England §§608, 611–612, 615
(1909). See also Atwater v. Lago Vista, 532 U. S. 318, 342–345 (2001)
(noting 19th-century decisions upholding statutes extending war-
rantless arrest authority to misdemeanors, other than breaches of the
peace, committed in a police officer’s presence); Wilgus, supra, at 551
(warrantless misdemeanor arrests “made under authority of a statute
must conform strictly to its provisions; otherwise they will not be valid,
and the one arresting becomes a trespasser”).
  Noting colonial hostility to general warrants and writs of assistance,
the Court observes that “founding-era citizens were skeptical of using
the rules for search and seizure set by government actors as the index
of reasonableness.” Ante, at 4. The practices resisted by the citizenry,
however, served to invade the people’s privacy, not to shield it.
2                        VIRGINIA v. MOORE

                 GINSBURG, J., concurring in judgment

to the Fourth Amendment and not to our “supervisory
power,” ante, at 7.2 And I am aware of no “long line of
cases” holding that, regardless of state law, probable cause
renders every warrantless arrest for crimes committed in
the presence of an arresting officer “constitutionally rea-
sonable,” ante, at 6.3
  I agree with the Court’s conclusion and its reasoning,
however, to this extent. In line with the Court’s decision
——————
   2 The Court attributes Di Re’s suppression ruling to our “supervisory

power,” not to “a rule we derived from the Constitution.” Ante, at 7.
Justice Jackson, author of Di Re, however, did not mention “supervisory
power,” placed the decision in a Fourth Amendment context, see 332
U. S., at 585, and ended with a reminder that “our Constitution [places]
obstacles in the way of a too permeating police surveillance,” id., at 595.
The Di Re opinion, I recognize, is somewhat difficult to parse. Allied to
Di Re’s Fourth Amendment instruction, the Court announced a choice-
of-law rule not derived from the Constitution: When a state officer
makes a warrantless arrest for a federal crime, federal arrest law
governs the legality of the arrest; but absent a federal statute in point,
“the law of the state where an arrest without warrant takes place
determines its validity.” Id., at 588–589.
   3 Demonstrative of the “long line,” the Court lists Atwater, 532 U. S.,

at 354, Devenpeck v. Alford, 543 U. S. 146, 152 (2004), Brinegar v.
United States, 338 U. S. 160, 164, 170, 175–176 (1949), and Gerstein v.
Pugh, 420 U. S. 103, 111 (1975). Ante, at 6. But in all of these cases,
unlike Moore’s case, state law authorized the arrests. The warrantless
misdemeanor arrest in Atwater was authorized by Tex. Transp. Code
Ann. §543.001 (West 1999). See 532 U. S., at 323. The warrantless
misdemeanor arrest in Devenpeck was authorized by Wash. Rev. Code
Ann. §10.31.100 (Michie 1997). In Brinegar, whether the warrantless
arrest was for a misdemeanor or a felony, it was authorized by state
law. See Okla. Stat., Tit. 22, §196 (1941). Gerstein involved a challenge
to the State’s preliminary hearing procedures, not to the validity of a
particular arrest. See 420 U. S., at 105. The record does not indicate
whether the respondents’ offenses were committed in the officer’s
presence or whether the arrests were made under warrant. See id.,
at 105, n. 1. But it does indicate that the crimes involved were serious
felonies, see ibid., and state law authorized arrest without warrant
when “[a] felony has been committed and [the officer] reasonably
believes that the [apprehended] person committed it,” Fla. Stat. Ann.
§901.15(2) (West 1973).
                 Cite as: 553 U. S. ____ (2008)            3

              GINSBURG, J., concurring in judgment

in Atwater v. Lago Vista, 532 U. S. 318, 354 (2001), Vir-
ginia could have made driving on a suspended license an
arrestable offense. The Commonwealth chose not to do so.
Moore asks us to credit Virginia law on a police officer’s
arrest authority, but only in part. He emphasizes Vir-
ginia’s classification of driving on a suspended license as a
nonarrestable misdemeanor. Moore would have us ignore,
however, the limited consequences Virginia attaches to a
police officer’s failure to follow the Commonwealth’s sum-
mons-only instruction. For such an infraction, the officer
may be disciplined and the person arrested may bring a
tort suit against the officer. But Virginia law does not
demand the suppression of evidence seized by an officer
who arrests when he should have issued a summons.
  The Fourth Amendment, today’s decision holds, does not
put States to an all-or-nothing choice in this regard. A
State may accord protection against arrest beyond what
the Fourth Amendment requires, yet restrict the remedies
available when police deny to persons they apprehend the
extra protection state law orders. See ante, at 9. Because
I agree that the arrest and search Moore challenges vio-
lated Virginia law, but did not violate the Fourth Amend-
ment, I join the Court’s judgment.

```

---
