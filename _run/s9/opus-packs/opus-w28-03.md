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

## GROUP: content/cases/California v. Beheler.md  (`case`, 5 assertions)

### content_page

```
---
title: "California v. Beheler"
type: case
citation: "463 U.S. 1121 (1983)"
parallel_cite: "103 S. Ct. 3517; 77 L. Ed. 2d 1275; 51 U.S.L.W. 3934"
neutral_cite: 1983 U.S. LEXIS 114
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-07-06
docket: 82-1666
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-07-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Beheler
  varies_by_point: false
  scope_note: "Good law; the 'Beheler' formulation of Miranda custody — a suspect who voluntarily comes to the station, is told he is not under arrest, and is free to leave is not in custody. The custody test is restraint 'of the degree associated with a formal arrest.'"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111023/california-v-beheler/"
  cluster_id: 111023
  opinion_id: 9429374
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Oregon v. Mathiason]]", "[[Miranda v. Arizona]]", "[[Berkemer v. McCarty]]", "[[Stansbury v. California]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "station-house", "per-curiam"]
holding: "A suspect who is not under arrest, voluntarily comes to the police station, and is allowed to leave after a brief interview is not 'in custody' for Miranda purposes; the ultimate custody inquiry is whether there was a formal arrest or restraint on freedom of movement of the degree associated with a formal arrest."
lake:
  record_id: California v. Beheler
  status: verified
  projected_at: 2026-07-06
---

# California v. Beheler

*463 U.S. 1121 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Beheler and several acquaintances tried to steal hashish from a dealer, his stepbrother shot and killed her. Beheler called the police, told them his stepbrother was the killer, and consented to a search of his yard, where the gun was found. That evening he voluntarily accompanied police to the station, having been told he was not under arrest. He talked to police about the murder for under 30 minutes without receiving [[Miranda and Custodial Interrogation|Miranda warnings]], and was then allowed to return home. Five days later he was arrested, given [[Miranda and Custodial Interrogation|Miranda warnings]], and gave a second, taped confession. The California Court of Appeal held the first, un-warned interview was custodial and reversed his conviction.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] are required when a suspect, not placed under arrest, voluntarily comes to the police station and is allowed to leave unhindered after a brief interview.

## Rule
No. The question "has already been settled clearly by past decisions of this Court." — 463 U.S. at 1121. Beheler "was neither taken into custody nor significantly deprived of his freedom of action. Indeed, Beheler's freedom was not restricted in any way whatsoever." — *Id.* at 1123. ^pin-1123

The custody test is restraint equivalent to arrest: "Although the circumstances of each case must certainly influence a determination of whether a suspect is 'in custody' . . . , the ultimate inquiry is simply whether there is a 'formal arrest or restraint on freedom of movement' of the degree associated with a formal arrest." — *Id.* at 1125 (quoting *Oregon v. Mathiason*, 429 U.S. 492, 495 (1977)). [[Miranda and Custodial Interrogation|Miranda warnings]] are not required "simply because the questioning takes place in the station house, or because the questioned person is one whom the police suspect." — *Id.* (quoting *Mathiason*). ^pin-1125

## Application
The factors the California court emphasized — that the interview occurred at the station and that Beheler was already a suspect because he had spoken to police earlier — do not, by themselves, establish custody. Beheler came voluntarily, was told he was not under arrest, and left to go home afterward; his freedom of movement was never restrained to the degree of a formal arrest. That the police knew more about Beheler than the officers knew in *[[Oregon v. Mathiason|Mathiason]]*, and the time elapsed since the crime, were irrelevant. He was therefore not in custody, and no [[Miranda and Custodial Interrogation|Miranda warnings]] were required before the first interview.

## Conclusion
A voluntary, non-arrest, free-to-leave station-house interview is not custodial; no [[Miranda and Custodial Interrogation|Miranda warnings]] were required. The judgment of the California Court of Appeal was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Beheler* restates and applies [[Oregon v. Mathiason]] in the [[Miranda v. Arizona]] custody line; its "degree associated with a formal arrest" formulation is the standard custody test, later applied to traffic stops in [[Berkemer v. McCarty]] and framed objectively in [[Stansbury v. California]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *California v. Beheler*, 463 U.S. 1121 (1983) (per curiam) — https://www.courtlistener.com/opinion/111023/california-v-beheler/ — pinpoints: 1121, 1123, 1125.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6de32c71082d987c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "463 U.S. 1121 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 114", "official_citation_present": true, "parallel_cite": "103 S. Ct. 3517; 77 L. Ed. 2d 1275; 51 U.S.L.W. 3934", "title": "California v. Beheler", "year": "1983"}}
{"assertion_id": "14578ecbb524cbeb", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "California v. Beheler"}}
{"assertion_id": "c4c9fbf4877a1aec", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspect who is not under arrest, voluntarily comes to the police station, and is allowed to leave after a brief interview is not 'in custody' for Miranda purposes; the ultimate custody inquiry is whether there was a formal arrest or restraint on freedom of movement of the degree associated with a formal arrest.", "title": "California v. Beheler"}}
{"assertion_id": "a3a648d6d96fedd0", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-07-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "California v. Beheler", "field_i_validity": "good_law", "scope_note": "Good law; the 'Beheler' formulation of Miranda custody — a suspect who voluntarily comes to the station, is told he is not under arrest, and is free to leave is not in custody. The custody test is restraint 'of the degree associated with a formal arrest.'", "title": "California v. Beheler", "varies_by_point": "false"}}
{"assertion_id": "c8eb72bfc673febf", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Beheler"}}
```

### lake record — California v. Beheler

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Beheler",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "California v. Beheler",
    "case_name_short": "Beheler",
    "case_name_full": "California v. Beheler",
    "input_case_name": "California v. Beheler",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-07-06",
    "year": 1983,
    "docket": "82-1666",
    "cluster_id": 111023,
    "lead_opinion_id": 9429374,
    "sibling_ids": [
      111023,
      9429374,
      9429375
    ],
    "absolute_url": "/opinion/111023/california-v-beheler/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "463 U.S. 1121",
      "volume": "463",
      "reporter": "U.S.",
      "page": "1121",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 3517",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "3517",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 1275",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "1275",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 3934",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "3934",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 114",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "114",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "463 U.S. 1121",
        "volume": "463",
        "reporter": "U.S.",
        "page": "1121",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 3517",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "3517",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 1275",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "1275",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 114",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "114",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 3934",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "3934",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "463 U.S. 1121",
    "official_selection": {
      "court_class": "scotus",
      "selected": "463 U.S. 1121",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1123",
      "page": null,
      "quote": "--- # California v. Beheler *463 U.S. 1121 (1983)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Beheler and several acquaintances tried to steal hashish from a dealer, his stepbrother shot and killed her. Beheler called the police, told them his stepbrother was the killer, and consented to a search of his yard, where the gun was found. That evening he voluntarily accompanied police to the station, having been told he was not under arrest. He talked to police about the murder for under 30 minutes without receiving Miranda warnings, and was then allowed to return home. Five days later he was arrested, given Miranda warnings, and gave a second, taped confession. The California Court of Appeal held the first, un-warned interview was custodial and reversed his conviction. ## Issue Whether Miranda warnings are required when a suspect, not placed under arrest, voluntarily comes to the police station and is allowed to leave unhindered after a brief interview. ## Rule No. The question",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1125",
      "page": null,
      "quote": "Although the circumstances of each case must certainly influence a determination of whether a suspect is 'in custody' . . . , the ultimate inquiry is simply whether there is a 'formal arrest or restraint on freedom of movement' of the degree associated with a formal arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-07-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Beheler",
    "varies_by_point": false,
    "scope_note": "Good law; the 'Beheler' formulation of Miranda custody \u2014 a suspect who voluntarily comes to the station, is told he is not under arrest, and is free to leave is not in custody. The custody test is restraint 'of the degree associated with a formal arrest.'",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. John Noehl and Analise Noehl",
          "cluster_id": 10618700,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane1_negative"
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
        "journal_ref": "California v. Beheler:lane1_negative"
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
        "journal_ref": "California v. Beheler:lane1_negative"
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
        "journal_ref": "California v. Beheler:lane1_negative"
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
        "journal_ref": "California v. Beheler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jovan'z Smith v. Ken Clark",
          "cluster_id": 3134205,
          "cite": [
            "804 F.3d 983",
            "2015 U.S. App. LEXIS 18335",
            "2015 WL 6387862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dowthitt v. State",
          "cluster_id": 1777832,
          "cite": [
            "931 S.W.2d 244",
            "1996 Tex. Crim. App. LEXIS 93",
            "1996 WL 347772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gardner v. State",
          "cluster_id": 1749178,
          "cite": [
            "306 S.W.3d 274",
            "2009 Tex. Crim. App. LEXIS 1441",
            "2009 WL 3365652"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1890229,
          "cite": [
            "313 S.W.3d 274",
            "2010 Tex. Crim. App. LEXIS 722",
            "2010 WL 2382555"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freddie Sevier v. Kenneth Turner",
          "cluster_id": 440363,
          "cite": [
            "742 F.2d 262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 1728885,
          "cite": [
            "868 S.W.2d 561",
            "1993 Tenn. LEXIS 410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Anthony Perdue",
          "cluster_id": 656633,
          "cite": [
            "8 F.3d 1455",
            "1993 U.S. App. LEXIS 28321",
            "1993 WL 437983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Morris",
          "cluster_id": 1454621,
          "cite": [
            "807 P.2d 949",
            "53 Cal. 3d 152",
            "279 Cal. Rptr. 720",
            "91 Daily Journal DAR 3869",
            "91 Cal. Daily Op. Serv. 2303",
            "1991 Cal. LEXIS 1218"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ronald Dean Combs v. Ralph Coyle",
          "cluster_id": 767855,
          "cite": [
            "205 F.3d 269",
            "2000 U.S. App. LEXIS 2578",
            "2000 WL 201970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sewn Newton",
          "cluster_id": 786350,
          "cite": [
            "369 F.3d 659",
            "2004 U.S. App. LEXIS 10343",
            "2004 WL 1161747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
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
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Terrell Hubbard (073539)",
          "cluster_id": 2811145,
          "cite": [
            "222 N.J. 249",
            "118 A.3d 314"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maurice A. Mason v. Betty Mitchell",
          "cluster_id": 780969,
          "cite": [
            "320 F.3d 604",
            "2003 U.S. App. LEXIS 2026",
            "2003 WL 252101"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Russel William Burket v. Ronald Angelone, Director, Virginia Department of Corrections",
          "cluster_id": 768204,
          "cite": [
            "208 F.3d 172",
            "2000 U.S. App. LEXIS 5116",
            "2000 WL 309299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Beheler:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111023 OR 9429374 OR 9429375) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQzMTM5MjAwMDAwJnM9MzAwNDczMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111023+OR+9429374+OR+9429375%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111023 OR 9429374 OR 9429375)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTEmcz03MDM5OTMmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111023+OR+9429374+OR+9429375%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111023 OR 9429374 OR 9429375)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 1,
        "triage_snippet_classified": 41
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111023 OR 9429374 OR 9429375)",
    "indexed_citing_opinions": 1239,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111023,
        "count": 1067,
        "count_source": "search"
      },
      {
        "opinion_id": 9429374,
        "count": 192,
        "count_source": "search"
      },
      {
        "opinion_id": 9429375,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2048,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-beheler.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMDg3NyZzPTEwMTI3NjkzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111023+OR+9429374+OR+9429375%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111023,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 110289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1129634,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1133244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1164451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1193480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1228924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1247133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1289115,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 1450284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 2131068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111023,
        "cited_id": 2144845,
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
    "date_created": "2026-07-04T21:19:23Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:19:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:19:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:19:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Beheler

```
<opinion type="majority">
<author id="b1169-9">Per Curiam.</author>
<p id="b1169-10">The question presented in this petition for certiorari is whether <em>Miranda </em>warnings are required if the suspect is not placed under arrest, voluntarily comes to the police station, and is allowed to leave unhindered by police after a brief interview. Because this question has already been settled <page-number citation-index="1" label="1122">*1122</page-number>clearly by past decisions of this Court, we reverse a decision of the California Court of Appeal holding that <em>Miranda </em>warnings are required in these circumstances.</p>
<p id="AdkZ">H</p>
<p id="AdP">The respondent, Jerry Beheler, and several acquaintances, attempted to steal a quantity of hashish from Peggy Dean, who was selling the drug in the parking lot of a liquor store. Dean was killed by Beheler’s companion and stepbrother, Danny Wilbanks, when she refused to relinquish her hashish. Shortly thereafter, Beheler called the police, who arrived almost immediately. See Brief in Opposition 3. He told the police that Wilbanks had killed the victim, and that other companions had hidden the gun in the Behelers’ backyard. Beheler gave consent to search the yard and the gun was found. Later that evening, Beheler voluntarily agreed to accompany police to the station house, although the police specifically told Beheler that he was not under arrest.</p>
<p id="Alch">At the station house, Beheler agreed to talk to police about the murder, although the police did not advise Beheler of the rights provided him under <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The interview lasted less than 30 minutes. After being told that his statement would be evaluated by the District Attorney, Beheler was permitted to return to his home. Five days later, Beheler was arrested in connection with the Dean murder. After he was fully advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, he waived those rights and gave a second, taped confession during which he admitted that his earlier interview with the police had been given voluntarily. The trial court found that it was not necessary for police to advise Beheler of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights prior to the first interview, and Beheler’s statements at both interviews were admitted into evidence.</p>
<p id="AbTt">The California Court of Appeal reversed Beheler’s conviction for aiding and abetting first-degree murder, holding that the first interview with police constituted custodial interro<page-number citation-index="1" label="1123">*1123</page-number>gation, which activated the need for <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. The court focused on the fact that the interview took place in the station house, that before the station house interview the police had already identified Beheler as a suspect in the case because Beheler had discussed the murder with police earlier, and that the interview was designed to produce incriminating responses. Although the indicia of arrest were not present, the balancing of the other factors led the court to conclude that the State “has not met its burden of establishing that [Beheler] was not in custody” during the first interview. App. to Pet. for Cert. 36.<footnotemark>1</footnotemark></p>
<p id="A0qa">We held in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that “[b]y custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span> (footnote omitted). It is beyond doubt that Beheler was neither taken into custody nor significantly deprived of his freedom of action. Indeed, Beheler’s freedom was not restricted in any way whatsoever.</p>
<p id="ADrb">In <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492</a></span> (1977), which involved a factual context remarkably similar to the present case, we held that the suspect was not “in custody” within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The police initiated contact with Mathiason, who agreed to come to the patrol office. There, the police conducted an interview after informing Mathiason that they suspected him of committing a burglary, and that the truthfulness of any statement that he made would be <page-number citation-index="1" label="1124">*1124</page-number>evaluated by the District Attorney or a judge. The officer also falsely informed Mathiason that his fingerprints were found at the scene of the crime. Mathiason then admitted to his participation in the burglary. The officer advised Mathiason of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, and took a taped confession, but released him pending the District Attorney’s decision to bring formal charges. The interview lasted for 30 minutes.</p>
<p id="b1172-5">In summarily reversing the Oregon Supreme Court decision that Mathiason was in custody for purposes of receiving <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>protection, we stated: “Such a noncustodial situation is not converted to one in which <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>applies simply because a reviewing court concludes that, even in the absence of any formal arrest or restraint on freedom of movement, the questioning took place in a ‘coercive environment.’” <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 495</a></span>. The police are required to give <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings only “where there has been such a restriction on a person’s freedom as to render him ‘in custody.’” <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 495</a></span>. Our holding relied on the very practical recognition that “[a]ny interview of one suspected of a crime by a police officer will have coercive aspects to it, simply by virtue of the fact that the police officer is part of a law enforcement system which may ultimately cause the suspect to be charged with a crime.” <em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Ibid.</a></span></em><footnotemark><em>2</em></footnotemark></p>
<p id="b1172-6">The court below believed incorrectly that <em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span> </em>could be distinguished from the present case because Mathiason was not questioned by police until some 25 days after the burglary. In the present case, Beheler was interviewed shortly after the crime was committed, had been drinking earlier in <page-number citation-index="1" label="1125">*1125</page-number>the day, and was emotionally distraught. See App. to Pet. for Cert. 24-25. In addition, the court observed that the police had a great deal more information about Beheler before their interview than did the police in <em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>, </em>and that Mathiason was a parolee who knew that “it was incumbent upon him to cooperate with police.” App. to Pet. for Cert. 25. Finally, the court noted that our decision in <em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span> </em>did not preclude a consideration of the “totality of circumstances” in determining whether a suspect is “in custody.”</p>
<p id="b1173-4">Although the circumstances of each case must certainly influence a determination of whether a suspect is “in custody” for purposes of receiving <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>protection, the ultimate inquiry is simply whether there is a “formal arrest or restraint on freedom of movement” of the degree associated with a formal arrest. <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason"><em>Mathiason, supra, </em>at 495</a></span>. In the present case, the “totality of circumstances” on which the court focused primarily were that the interview took place in a station house, and that Beheler was a suspect because he had spoken to police earlier. But we have explicitly recognized that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are not required “simply because the questioning takes place in the station house, or because the questioned person is one whom the police suspect. ” <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 495</a></span>. That the police knew more about Beheler before his interview than they did about Mathiason before his is irrelevant, see n. 2, <em>supra, </em>especially because it was Beheler himself who had initiated the earlier communication with police. Moreover, the length of time that elapsed between the commission of the crime and the police interview has no relevance to the inquiry.<footnotemark>3</footnotemark></p>
<p id="ApMW"><page-number citation-index="1" label="1126">*1126</page-number>I — I <em>I </em>— i HH</p>
<p id="Aq2q">Accordingly, the motion of respondent for leave to proceed <em>informa pawperis </em>and the petition for writ of certiorari are granted, the judgment of the California Court of Appeal is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="Ah_">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="AP6r"> Beheler suggests that the decision below rested upon adequate and independent state grounds in that the court applied state “in custody” standards. See Brief in Opposition 9, n. 5. It is clear from the face of the opinion, however, that the opinion below rested exclusively on the court’s “decision on the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>issue.” App. to Pet. for Cert. 37. Although the court relied in part on <em>People </em>v. <em>Herdan, </em><span class="citation" data-id="5661072"><a href="/opinion/5805859/people-v-herdan/" aria-description="Citation for case: People v. Herdan">42 Cal. App. 3d 300</a></span>, <span class="citation" data-id="5661072"><a href="/opinion/5805859/people-v-herdan/" aria-description="Citation for case: People v. Herdan">116 Cal. Rptr. 641</a></span> (1974), that decision applies <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
<footnote label="2">
<p id="b1172-7"> Our holding in <em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span> </em>reflected our earlier decision in <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341</a></span> (1976), in which we rejected the notion that the “in custody” requirement was satisfied merely because the police interviewed a person who was the “focus” of a criminal investigation. We made clear that <em>“Miranda </em>implicitly defined ‘focus’... as ‘questioning initiated by law enforcement officers <em>after </em>a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.’ ” <em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/" aria-description="Citation for case: Beckwith v. United States">Id.,</a></span> </em>at 347 (quoting <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>).</p>
</footnote>
<footnote label="3">
<p id="b1173-5"> Beheler offers a number of arguments in opposition to the State’s petition for certiorari. The thrust of these arguments is that even though he voluntarily engaged in the interview with police, his participation was “coerced” because he was unaware of the consequences of his participation. Beheler cites no authority to support his contention that his lack of awareness transformed the situation into a custodial one. In addition, Beheler argues that it would be unjust to uphold his conviction because the trigger-man was convicted only of voluntary manslaughter. We do not find <page-number citation-index="1" label="1126">*1126</page-number>Beheler’s argument to be persuasive. See <em>Standefer </em>v. <em>United States, </em><span class="citation" data-id="110289"><a href="/opinion/110289/standefer-v-united-states/" aria-description="Citation for case: Standefer v. United States">447 U. S. 10</a></span> (1980).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/California v. Carney.md  (`case`, 5 assertions)

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
{"assertion_id": "c3581dc19cac9565", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "471 U.S. 386 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 8", "official_citation_present": true, "parallel_cite": "105 S. Ct. 2066; 85 L. Ed. 2d 406; 53 U.S.L.W. 4521", "title": "California v. Carney", "year": "1985"}}
{"assertion_id": "170708893b0c6dd1", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "California v. Carney"}}
{"assertion_id": "c6bfde3d137f9867", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The automobile exception applies to a motor home being used as a vehicle, and articulates the exception's TWO justifications: (1) ready…", "title": "California v. Carney"}}
{"assertion_id": "8f4d11f1b7417f04", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-05-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "California v. Carney", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "California v. Carney", "varies_by_point": "false"}}
{"assertion_id": "932b235852be9ae7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Carney"}}
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

## GROUP: content/cases/California v. Ciraolo.md  (`case`, 5 assertions)

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
{"assertion_id": "98757656b77cc5b0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "476 U.S. 207 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 154", "official_citation_present": true, "parallel_cite": "106 S. Ct. 1809; 90 L. Ed. 2d 210", "title": "California v. Ciraolo", "year": "1986"}}
{"assertion_id": "83faa7db461303ed", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Warrantless naked-eye aerial observation of a fenced curtilage from navigable airspace (1,000 ft) is not a search — no reasonable expectation of privacy from the air.", "title": "California v. Ciraolo"}}
{"assertion_id": "a53dd90ed4e2609e", "dimension": "support", "kind": "home_role", "locator": {"home": "Aerial and Enhanced Surveillance"}, "payload": {"home": "Aerial and Enhanced Surveillance", "role": "Key — Anchor", "title": "California v. Ciraolo"}}
{"assertion_id": "81b74d78034e62a5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Ciraolo"}}
{"assertion_id": "96d5810ff70deb64", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-05-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "California v. Ciraolo", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "California v. Ciraolo", "varies_by_point": "false"}}
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

## GROUP: content/cases/California v. Greenwood.md  (`case`, 5 assertions)

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
{"assertion_id": "7c9d762605f1da2a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "486 U.S. 35 (1988)", "court": "U.S. Supreme Court", "neutral_cite": "1988 U.S. LEXIS 2279", "official_citation_present": true, "parallel_cite": "108 S. Ct. 1625; 100 L. Ed. 2d 30; 56 U.S.L.W. 4409", "title": "California v. Greenwood", "year": "1988"}}
{"assertion_id": "7d28acec2f6c0f71", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "No reasonable expectation of privacy in garbage bags left for collection at the curb, outside the curtilage; warrantless search/seizure of curbside trash does not violate the 4A.", "title": "California v. Greenwood"}}
{"assertion_id": "afc24fecf610576f", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Key — Progeny / Refinement", "title": "California v. Greenwood"}}
{"assertion_id": "1cae3d9707978c61", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Greenwood"}}
{"assertion_id": "2d266ef01ce5b92e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1988-05-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "California v. Greenwood", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "California v. Greenwood", "varies_by_point": "false"}}
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
